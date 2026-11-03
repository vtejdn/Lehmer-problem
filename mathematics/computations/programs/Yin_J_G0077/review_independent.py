"""Independent complete J77 payload check; stdlib only, no author imports.
Declared domain: three inputs, fifteen windows, <=120 seconds aggregate run.
Norms/traces use quotient multiplication matrices; no symbolic resultant helper.
Byte observations are nonblocking and optional prose is not a mathematical input.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from math import gcd, lcm
from functools import reduce
from time import perf_counter
import json
import traceback

HERE = (_J_PROGRAM / 'review_independent.py').parent
CAP = 120
START = perf_counter()

# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = (_J_OUTPUT / 'review_failure.json').relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def tick():
    if perf_counter() - START > CAP:
        raise TimeoutError('120-second independent aggregate cap exceeded')

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]

def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])

def scale(a, c):
    return trim([v*c for v in a])

def mul(a, b):
    c = [0] * (len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i+j] += u*v
    return trim(c)

def divmodp(a, b):
    a, b = trim([F(v) for v in a]), trim([F(v) for v in b])
    assert b != [0]
    q = [F(0)] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        j, v = len(a)-len(b), a[-1]/b[-1]
        q[j] += v
        a = add(a, [0]*j + scale(b, -v))
    return trim(q), a

def rem(a, p):
    return divmodp(a, p)[1]

def pad(a, n):
    assert len(trim(a)) <= n
    return list(a) + [0]*(n-len(a))

def ints(a):
    assert all(F(v).denominator == 1 for v in a)
    return [int(v) for v in a]

def content(a):
    return reduce(gcd, (abs(int(v)) for v in a), 0)

def dot(a, b):
    return sum(u*v for u, v in zip(a, b))

def transpose(a):
    return list(map(list, zip(*a)))

def mm(a, b):
    return [[dot(row, col) for col in transpose(b)] for row in a]

def mv(a, v):
    return [dot(row, v) for row in a]

def det(a):
    a = [[F(v) for v in row] for row in a]
    n, ans = len(a), F(1)
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        if k is None:
            return F(0)
        if k != j:
            a[k], a[j] = a[j], a[k]
            ans = -ans
        v = a[j][j]
        ans *= v
        for k in range(j+1, n):
            c = a[k][j]/v
            for i in range(j+1, n):
                a[k][i] -= c*a[j][i]
    return ans

def inverse(a):
    n = len(a)
    a = [[F(v) for v in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        k = next(k for k in range(j, n) if a[k][j])
        a[k], a[j] = a[j], a[k]
        v = a[j][j]
        a[j] = [u/v for u in a[j]]
        for k in range(n):
            if k != j:
                v = a[k][j]
                a[k] = [u-v*w for u, w in zip(a[k], a[j])]
    return [row[n:] for row in a]

def multiplication(a, p):
    d = len(p)-1
    return transpose([pad(rem([0]*j+a, p), d) for j in range(d)])

def norm(a, p):
    return ints([det(multiplication(a, p))])[0]

def trace(a, p):
    mat = multiplication(a, p)
    return sum(mat[j][j] for j in range(len(mat)))

def invmod(a, p):
    mat = inverse(multiplication(a, p))
    ans = [row[0] for row in mat]
    assert rem(mul(a, ans), p) == [1]
    return trim(ans)

def powmod(a, n, p):
    out = [1]
    while n:
        if n & 1:
            out = rem(mul(out, a), p)
        a = rem(mul(a, a), p)
        n //= 2
    return out

def evalmod(a, x, p):
    out = [0]
    for c in a[::-1]:
        out = rem(add(mul(out, x), [c]), p)
    return out

def evaluate(a, x):
    out = 0
    for c in a[::-1]:
        out = out*x+c
    return out

def mrem(a, b, p):
    a, b = trim([v % p for v in a]), trim([v % p for v in b])
    while a != [0] and len(a) >= len(b):
        j = len(a)-len(b)
        c = a[-1]*pow(b[-1], -1, p) % p
        for k, v in enumerate(b):
            a[j+k] = (a[j+k]-c*v) % p
        a = trim(a)
    return a

def mpow(a, n, q, p):
    out = [1]
    while n:
        if n & 1:
            out = mrem(mul(out, a), q, p)
        a = mrem(mul(a, a), q, p)
        n //= 2
    return out

def mgcd(a, b, p):
    while b != [0]:
        a, b = b, mrem(a, b, p)
    return a

def irreducibility(q):
    d = len(q)-1
    cert = None
    for prime in [2,3,5,7,11,13,17,19,23,29,31]:
        frob = [0,1]
        ok = True
        for j in range(1, d+1):
            frob = mpow(frob, prime, q, prime)
            diff = [(frob[i] if i < len(frob) else 0) - (i == 1)
                    for i in range(max(2, len(frob)))]
            diff = trim([v % prime for v in diff])
            if j <= d//2 and len(mgcd(q, diff, prime)) != 1:
                ok = False
            if j == d and diff != [0]:
                ok = False
        if ok:
            cert = prime
            break
    assert cert is not None, ('no declared irreducibility prime', q)
    # This exact fixed grid suffices to exhibit a real trace in (-2,2).
    grid = [F(-3,2), F(-1), F(-1,2), F(0), F(1,2), F(1), F(3,2)]
    pair = next(((a,b) for a,b in zip(grid,grid[1:])
                 if evaluate(q,a)*evaluate(q,b)<0), None)
    assert pair is not None
    # Q irreducible and one real embedding has tau^2-4<0, hence no square
    # in Q(tau).  Thus t^s Q(t+t^-1) is irreducible of degree 2s.
    return {'trace_irreducible_mod_prime':cert,
            'negative_discriminant_trace_interval':[str(v) for v in pair]}

def tracepoly(p):
    s = (len(p)-1)//2
    assert p == p[::-1] and p[-1] == 1
    # C_j(x)=t^j+t^-j, not the author's descending Laurent elimination.
    cs = [[2],[0,1]]
    for j in range(2,s+1):
        cs.append(add(mul([0,1],cs[-1]),scale(cs[-2],-1)))
    q = [p[s]]
    for j in range(1,s+1):
        q = add(q,scale(cs[j],p[s+j]))
    # Full Laurent substitution identity after multiplication by t^s.
    poly = [0]
    for j,c in enumerate(q):
        term = [1]
        for _ in range(j):
            term = mul(term,[1,0,1])
        poly = add(poly,[0]*(s-j)+scale(term,c))
    assert poly == p
    return q

def anti(c,n):
    out = [0]*(2*n+1)
    for j,v in enumerate(c,1):
        out[n+j] += v
        out[n-j] -= v
    return trim(out)

def lowedge(f,p,n):
    d = len(p)-1
    prod = mul(f,p)
    a = trim(prod[:d])
    star = pad(a,d)[::-1]
    assert prod == add(a,[0]*(2*n+1)+scale(star,-1))
    return a

def costs(f):
    f = ints(trim(f))
    lo = next(j for j,c in enumerate(f) if c)
    energy,one = sum(c*c for c in f),sum(abs(c) for c in f)
    return dict(actual_degree=len(f)-1,monomial_degree=lo,
                degree_without_monomial=len(f)-1-lo,content=content(f),
                height=max(map(abs,f)),leading_coefficient=f[-1],S1=one,
                S2_squared=energy,rho=str(F(one*one,energy)),
                mahler_lower_leading=abs(f[-1]),mahler_upper_squared=energy)

def factors(n):
    ans = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            ans[str(p)] = ans.get(str(p),0)+1
            n //= p
        p += 1
    if n>1:
        ans[str(n)] = 1
    return ans

def reconstruct():
    inputs = [('quartic',[1,-1,-1,-1,1]),
              ('sextic',[1,-1,0,-1,0,-1,1]),
              ('Lehmer',[1,1,0,-1,-1,-1,-1,-1,0,1,1])]
    records, certificates = [], []
    edges = diagonals = 0
    for label,p in inputs:
        tick()
        d,s = len(p)-1,(len(p)-1)//2
        q = tracepoly(p)
        certificates.append({'label':label,**irreducibility(q)})
        S = [[q[i+j+1] if i+j+1<=s else 0 for j in range(s)] for i in range(s)]
        assert det(S) == (-1)**(s*(s-1)//2)
        rr = [[1],[0,1]]
        for _ in range(2,3*s):
            rr.append(rem(add(mul([0,1],rr[-1]),scale(rr[-2],-1)),q))
        rr = [ints(pad(rem(v,q),s)) for v in rr]
        invprime = invmod([j*q[j] for j in range(1,s+1)],q)
        taut = add([0,1],invmod([0,1],p))
        windows = []
        for n in [s,2*s-1,2*s,2*s+1,3*s]:
            tick()
            R = transpose(rr[:n])
            H = mm(R,transpose(R))
            Delta = ints([det(H)])[0]
            Hi = inverse(H)
            ell = [dot(r,mv(Hi,r)) for r in rr[:n]]
            assert all(v>0 for v in ell) and sum(ell)==s
            minimizing = [i+1 for i,v in enumerate(ell) if v == min(ell)]
            k = minimizing[0]
            rk = rr[k-1]
            delta = content(rk)
            u = [v//delta for v in rk]
            rational = mv(Hi,rk)
            denominator = lcm(*(v.denominator for v in rational))
            w = ints([v*denominator for v in rational])
            g = content(w)
            w = [v//g for v in w]
            qscale = F(denominator,g)
            hw = mv(H,w)
            L = next(F(a,b) for a,b in zip(hw,u) if b)
            assert L.denominator == 1
            L = int(L)
            assert hw == [L*v for v in u] and qscale == F(L,delta)
            assert Delta % L == 0
            gamma = Delta//L
            assert content(mv([[Delta*v for v in row] for row in Hi],u))==gamma
            c = mv(transpose(R),w)
            full = anti(c,n)
            edge = lowedge(full,p,n)
            aw = mv(S,w)
            expected = rem(mul(powmod([0,1],n+s,p),evalmod(aw,taut,p)),p)
            assert edge == expected
            basis = []
            for j in range(s):
                fj = anti(R[j],n)
                aj = lowedge(fj,p,n)
                ej = [int(i==j) for i in range(s)]
                want = rem(mul(powmod([0,1],n+s,p),evalmod(mv(S,ej),taut,p)),p)
                assert aj == want
                basis.append(ints(aj))
                edges += 1
            dual = [trace(rem(mul(mul(aw,r),invprime),q),q) for r in rr[:n]]
            assert dual == c
            nf,na = norm(full,p),norm(edge,p)
            nt,nu,nv = norm(aw,q),norm(u,q),norm(hw,q)
            endpoint = evaluate(p,1)*evaluate(p,-1)
            cyc = norm([-1]+[0]*(2*k-1)+[1],p)
            assert nf == endpoint*nv*nv == L**d*endpoint*nu*nu == qscale**d*cyc
            assert na == nt*nt > 0
            fc,ac = costs(full),costs(edge)
            assert fc['content']==ac['content']==content(aw)==1
            assert fc['S2_squared']==2*dot(w,hw)==2*qscale*qscale*ell[k-1]
            frem = ints(pad(rem(full,p),d))
            oc = content(frem)
            assert oc % L == 0 and fc['height']<=Delta
            windows.append(dict(n=n,R=R,H=H,Delta=Delta,S_Q=S,
                all_projection_diagonals=[str(z) for z in ell],
                minimizing_indices=minimizing,selected_index=k,delta=delta,u=u,
                gamma=gamma,L=L,q=str(qscale),w=w,c=c,
                trace_edge_coefficients=aw,trace_value_coefficients=hw,
                F_coefficients=ints(full),A_coefficients=ints(edge),
                basis_edge_coefficients=basis,dual_trace_coefficients=ints(dual),
                F_resultant=nf,A_resultant=na,trace_edge_norm=nt,
                primitive_trace_remainder_norm=nu,cyclic_resultant=cyc,
                endpoint_product=endpoint,F_cost=fc,A_cost=ac,
                actual_order_remainder=frem,actual_order_remainder_content=oc,
                L_prime_factors=factors(L),
                full_net_ratio=str(F(abs(nf),fc['S2_squared']**s)),
                edge_to_F_energy_ratio=str(F(na,fc['S2_squared']**s)),
                scalar_floor_energy_squared_ratio=str(F(L*L,fc['S2_squared'])),
                radial_charge_multiple_of_m=str(F(fc['degree_without_monomial'],d)),
                edge_is_unit=abs(nt)==1))
            diagonals += n
        records.append(dict(label=label,P_coefficients=p,Q_coefficients=q,
            actual_degree=d,trace_degree=s,original_irreducible=True,
            trace_irreducible=True,windows=windows))
    assert edges==50 and diagonals==100
    return dict(scope='Exactly three named actual inputs and n in {s,2s-1,2s,2s+1,3s};15 windows;120s aggregate cap',
        coefficient_order='ascending',inputs=records,window_count=15,
        basis_edges_checked=edges,projection_diagonals_checked=diagonals,
        all_exact_checks_passed=True), certificates

def compare(got,expected,path='root'):
    assert type(got) is type(expected), (path,type(got),type(expected))
    if isinstance(got,dict):
        assert got.keys()==expected.keys(), (path,got.keys(),expected.keys())
        return sum(compare(got[k],expected[k],path+'.'+k) for k in got)
    if isinstance(got,list):
        assert len(got)==len(expected), (path,len(got),len(expected))
        return sum(compare(a,b,path+f'[{i}]') for i,(a,b) in enumerate(zip(got,expected)))
    assert got==expected, (path,got,expected)
    return 1

def main():
    native = {name:(((_J_PROGRAM if name in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in ['readme.md','verify.py','result.json']}
    expected = json.loads(native['result.json'])
    payload, certificates = reconstruct()
    count = compare(payload,expected)
    tick()
    preserved = {name:(((_J_PROGRAM if name in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes()==data for name,data in native.items()}
    return dict(passed=True, scope='All 15 native windows; every non-execution field and JSON type', mathematical_scalar_fields_checked=count, windows=15, row_basis_edges=50, projection_diagonals=100, irreducibility_certificates=certificates, method='stdlib exact quotient arithmetic, Gaussian inverse and multiplication determinants/traces; no author imports', proof_only_rank_two_boundary_identities_checked_by_this_program=False)

if __name__=='__main__':
    try:
        report=main()
        ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(report))
    except BaseException:
        path=(_J_OUTPUT / 'review_failure.json')
        i=1
        while path.exists():
            path=_J_OUTPUT / 'review_failure.json'
            i+=1
        path.write_text(json.dumps(dict(traceback=_record_text(traceback.format_exc())), indent=2) + '\n', encoding='utf-8')
        raise
