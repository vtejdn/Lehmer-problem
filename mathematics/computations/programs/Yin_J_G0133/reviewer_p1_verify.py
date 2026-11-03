"""Independent full P1 certificate check for C839; no source code execution.

Fixed contract: 455137 sign representatives, 1365411 digit edges, height180,
t=68883/40000, Lambda=2**80, source ZIP<=25000000 bytes, two exact binary
member lengths3641096 and7282192.  No graph search or enlarged parameter is
performed.  Coordinate identities are derived modulo P.  Power intervals
enclose the four strip coefficients, and a centered absolute-error test
classifies every supplied state and every recomputed successor.  Every row's
inequality is checked directly from the witness weights and paid terminal
values.  The source replay report is read only after independent verification.
This is a separate implementation of the same finite mathematical criterion,
not a second independently constructed supersolution.  Progress is bounded;
the fixed finite input/iteration caps, not a hard memory ceiling, are enforced.
"""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import argparse
import json
import struct
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'repository/config.json').is_file())
OUTPUT = ROOT/'mathematics/computations/outputs'/HERE.name
ARCHIVE = ROOT/'mathematics/literature/pdf/CFMZ26/Quartic-Salem-Verification-v1.0.zip'
PREFIX = 'Quartic-Salem-Verification-v1.0/verification/lower_p1/'
N, H, LAMBDA, NUM, DEN = 455137, 180, 1 << 80, 68883, 40000
P = (1, -1, -1, -1, 1)
L = ((-1,-1,-1,1), (-1,-1,1,0), (-1,1,0,0), (1,0,0,0))


def require(ok, message):
    if not ok:
        raise ValueError(message)


def progress(stage, **kw):
    print(json.dumps({'stage':stage, **kw}), flush=True)


def reduce_poly(coeff):
    c = list(coeff)
    while len(c) > 4:
        lead, shift = c[-1], len(c)-5
        for j, value in enumerate(P):
            c[shift+j] -= lead*value
        c.pop()
    return tuple(c+[0]*(4-len(c)))


def times_x(c):
    return reduce_poly((0,)+tuple(c))


def form(x):
    return tuple(sum(x[j]*L[j][k] for j in range(4)) for k in range(4))


def successor(x, digit):
    return (x[1], x[2], x[3], sum(x[1:])-x[0]+digit)


def coordinate_and_strip_polynomials():
    for j in range(4):
        basis = tuple(int(k == j) for k in range(4))
        require(form(successor(basis,0)) == times_x(form(basis)), 'Wrong integral dynamics')
    require(form((0,0,0,1)) == (1,0,0,0), 'Wrong digit direction')
    determinant = 0
    for perm in permutations(range(4)):
        sign = (-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term = sign
        for j in range(4):
            term *= L[j][perm[j]]
        determinant += term
    require(abs(determinant) == 1, 'Coordinate matrix not unimodular')
    d = [tuple(a-b for a,b in zip(times_x(c),c)) for c in L]
    require(d == [(0,1,1,-1),(1,0,-2,1),(1,-2,1,0),(-1,1,0,0)], 'Wrong reduced strip forms')
    return d, determinant


def pvalue(x):
    return x**4-x**3-x**2-x+1


def root_and_coefficients(polys):
    lo, hi = Q(17,10), Q(7,4)
    require(pvalue(lo)<0<pvalue(hi), 'Wrong root bracket')
    # P'' is positive above3/2 and P'(3/2)=11/4, independently proving monotonicity.
    require(12*Q(3,2)**2-6*Q(3,2)-2 > 0, 'Convexity base')
    require(4*Q(3,2)**3-3*Q(3,2)**2-2*Q(3,2)-1 == Q(11,4), 'Derivative base')
    initial_width = hi-lo
    for _ in range(200):
        mid = (lo+hi)/2
        sign = pvalue(mid)
        require(sign != 0, 'Unexpected rational root')
        if sign < 0:
            lo = mid
        else:
            hi = mid
    require(hi-lo == initial_width/2**200 and pvalue(lo)<0<pvalue(hi), 'Final root enclosure')
    intervals = []
    for coeff in polys:
        # Direct power enclosure, independently of the source's interval Horner.
        low = sum(c*(lo**k if c>=0 else hi**k) for k,c in enumerate(coeff))
        high = sum(c*(hi**k if c>=0 else lo**k) for k,c in enumerate(coeff))
        a = (low*LAMBDA).numerator//(low*LAMBDA).denominator
        b = -((-high*LAMBDA).numerator//(-high*LAMBDA).denominator)
        require(b == a+1, 'Strip grid not resolved at fixed200 bisections')
        intervals.append((a,b))
    return (lo,hi), intervals


def strip_member(x, centers):
    # |d(x)-C/(2Lambda)|<=E/(2Lambda), where E=sum|x_j|.
    center = sum(v*c for v,c in zip(x,centers))
    error = sum(map(abs,x))
    if abs(center)+error < 2*LAMBDA:
        return True
    if abs(center)-error >= 2*LAMBDA:
        return False
    raise ValueError('Undecided strip membership at fixed scope: '+str(x))


def canonical(x):
    require(any(x), 'Zero is terminal, not a sign representative')
    return x if next(v for v in x if v) > 0 else tuple(-v for v in x)


def atomic_write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix+'.partial')
    tmp.write_text(json.dumps(value, indent=2)+'\n', encoding='utf8')
    tmp.replace(path)


def verify():
    progress('fixed_scope', rows=N, edges=3*N, height=H, tilt=str(Q(NUM,DEN)))
    polys, determinant = coordinate_and_strip_polynomials()
    roots, intervals = root_and_coefficients(polys)
    centers = [a+b for a,b in intervals]
    require(ARCHIVE.is_file() and ARCHIVE.stat().st_size<=25_000_000, 'Archive absent or size cap exceeded')
    with ZipFile(ARCHIVE) as archive:
        names = archive.namelist()
        for member,size in [('states.bin',8*N),('W.bin',16*N)]:
            name = PREFIX+member
            require(names.count(name) == 1, 'Duplicate or missing selected ZIP member')
            require(archive.getinfo(name).file_size == size, 'Wrong selected member length before read')
        state_bytes, weight_bytes = archive.read(PREFIX+'states.bin'), archive.read(PREFIX+'W.bin')
    require(len(state_bytes)==8*N and len(weight_bytes)==16*N, 'Wrong actual binary lengths')
    states = [struct.unpack_from('<4h',state_bytes,8*j) for j in range(N)]
    # Decode the128-bit witness as two explicit64-bit little-endian limbs.
    weights = []
    for low, high in struct.iter_unpack('<QQ',weight_bytes):
        weights.append(low+(high<<64))
    del state_bytes,weight_bytes
    require(states[0] == (0,0,0,1) and len(weights)==N, 'Wrong source row or count')
    lookup = {}
    for j,(x,w) in enumerate(zip(states,weights,strict=True)):
        require(x == canonical(x), 'Noncanonical source row '+str(j))
        require(max(map(abs,x))<=H and strip_member(x,centers), 'Source row outside strict region '+str(j))
        require(x not in lookup and w>=0, 'Duplicate row or negative weight')
        lookup[x] = w
        if j%65536 == 0:
            progress('state_validation', completed=j+1)
    counts = {'internal':0,'zero':0,'exit':0,'noncompletion':0}
    minimum, min_index, row_count, edge_count = None, None, 0, 0
    for j,(x,w) in enumerate(zip(states,weights,strict=True)):
        rhs = 0
        for digit in range(-1,2):
            y = successor(x,digit)
            edge_count += 1
            if not any(y):
                cls, value = 'zero', LAMBDA
            elif strip_member(y,centers):
                if max(map(abs,y))>H:
                    cls, value = 'exit', LAMBDA
                else:
                    key = canonical(y)
                    require(key in lookup, 'Missing internal successor at row '+str(j)+' digit '+str(digit))
                    cls, value = 'internal', lookup[key]
            else:
                cls, value = 'noncompletion', 0
            counts[cls] += 1
            rhs += (2-abs(digit))*value
        residual = (4*DEN)*w-NUM*rhs
        require(residual >= 0, 'Negative row residual '+str(j))
        row_count += 1
        if minimum is None or residual<minimum:
            minimum,min_index = residual,j
        if j%65536 == 0:
            progress('all_successors_and_rows', rows=row_count, edges=edge_count)
    require(row_count==N and edge_count==3*N and sum(counts.values())==3*N, 'Incomplete finite coverage')
    t = Q(NUM,DEN)
    require(1<t<roots[0], 'Tilt outside required interval')
    gap = 1-t*(1+Q(weights[0],LAMBDA))/2
    require(gap>Q(1,105), 'Complete Green comparison fails')
    require(gap == Q(2894667437079809876755951,302231454903657293676544000), 'Wrong claimed exact gap')
    return {'status':'PASS', 'parameter':'P1', 'H':H, 'state_count':N,
        'expanded_nonzero_states':2*N, 'scale':str(LAMBDA), 'tilt':str(t),
        'root_bisections':200, 'root_interval':[str(x) for x in roots],
        'strip_intervals':[[str(v) for v in pair] for pair in intervals],
        'edge_counts':counts, 'digit_labelled_edges':edge_count,
        'all_integer_rows_checked':row_count, 'min_row_margin':str(minimum),
        'min_row_margin_index':min_index, 'source_W0':str(weights[0]),
        'source_gap':str(gap), 'green_upper_fraction':str(1/gap), 'green_strict_bound':105,
        'coordinate_matrix_determinant':determinant, 'derived_strip_polynomials':polys,
        'unresolved_strip_comparisons':0, 'acceptance_uses_floating_point':False,
        'source_program_executed':False, 'reads_stored_transition_graph':False,
        'source_members':[PREFIX+'states.bin',PREFIX+'W.bin'],
        'scope_limits':{'archive_max_bytes':25000000, 'state_bytes':8*N,'weight_bytes':16*N,
            'hard_memory_ceiling':None, 'live_memory_monitor':False},
        'not_checked':'P2, quantitative upper bounds, logarithmic dimension decimals, qualitative packet construction'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay-report',type=Path,default=OUTPUT/'cfmz26_p1_lower.json')
    parser.add_argument('--output',type=Path,default=OUTPUT/'reviewer_p1_result.json')
    args = parser.parse_args()
    require(args.output.resolve().parent == OUTPUT.resolve(), 'Output outside this J home')
    try:
        result = verify()
        original = json.loads(args.replay_report.read_text(encoding='utf8'))
        compared = []
        for key,value in result.items():
            if key in original:
                require(value == original[key], 'Replay report mismatch: '+key)
                compared.append(key)
        require(original['boundary_diagnostics']=={'constant_fallbacks':0,'boundary_equalities':0,'unresolved_nonconstant':0}, 'Reported strip ambiguity')
        result['exact_replay_report_fields_compared'] = compared
        atomic_write(args.output,result)
        progress('complete', rows=result['all_integer_rows_checked'], edges=result['digit_labelled_edges'],
                 minimum=result['min_row_margin'], green_upper=result['green_upper_fraction'])
    except BaseException as exc:
        atomic_write(args.output.with_suffix('.incomplete.json'),{'status':'incomplete',
            'scope':{'rows':N,'edges':3*N,'height':H,'tilt':str(Q(NUM,DEN))},
            'failure_type':type(exc).__name__,'failure':str(exc)})
        raise


if __name__=='__main__':
    main()
