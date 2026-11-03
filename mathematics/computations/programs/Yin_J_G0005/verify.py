"""Independent exact verification of main.py's mathematical payload.

No byte/hash gates and no import of main.py. Integer quotient rings, finite
field arithmetic, Newton trace identities and resultant root squaring supply
independent paths. Numerical probes are expressly not certified.
"""
from fractions import Fraction
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import math
import sympy as sp

HERE = _J_OUTPUT
source = json.loads((HERE / 'result.json').read_text(encoding='utf-8'))
control = source['control']
checks = []

def check(name, statement):
    if not statement:
        raise AssertionError(name)
    checks.append(name)

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]

def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return trim(c)

def neg(a): return [-v for v in a]

def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return trim(c)

def divrem(a, b, prime=None):
    a, b = trim(a), trim(b)
    if prime:
        a, b = trim([int(x) % prime for x in a]), trim([int(x) % prime for x in b])
    q = [0] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        delta = len(a) - len(b)
        c = a[-1] * pow(b[-1], -1, prime) % prime if prime else Fraction(a[-1], b[-1])
        q[delta] += c
        for j in range(len(b)):
            a[delta+j] -= c*b[j]
            if prime: a[delta+j] %= prime
        a = trim(a)
    return trim(q), a

def exact_div(a, b):
    q, r = divrem(a, b)
    assert r == [0] and all(v.denominator == 1 for v in q)
    return [int(v) for v in q]

def mod(a, f, prime=None): return divrem(a, f, prime)[1]

def power_mod(a, n, f, prime):
    v = [1]
    while n:
        if n & 1: v = mod(mul(v, a), f, prime)
        a = mod(mul(a, a), f, prime)
        n //= 2
    return v

def gcd_poly(a, b, prime):
    while trim(b) != [0]: a, b = b, mod(a, b, prime)
    a = trim(a)
    inv = pow(a[-1], -1, prime)
    return [int(v)*inv % prime for v in a]

def evaluate(a, x):
    value = 0
    for coefficient in reversed(a): value = value*x + coefficient
    return value

cyclotomic = {
    1: [-1, 1], 2: [1, 1], 3: [1, 1, 1], 4: [1, 0, 1],
    5: [1, 1, 1, 1, 1], 6: [1, -1, 1],
    10: [1, -1, 1, -1, 1], 12: [1, 0, -1, 0, 1],
}
residue_tables = {}
for order, phi in cyclotomic.items():
    powers = []
    current = [1]
    for j in range(order):
        powers.append(current)
        current = mod([0] + current, phi)
    assert current == [1]
    pairs = []
    for n in range(order):
        for a in range(order):
            if math.gcd(math.gcd(n, a), order) != 1: continue
            value = add(add(powers[n], powers[(-n) % order]),
                        neg(add(powers[a], powers[(-a) % order])))
            if add(value, [-1]) == [0]: pairs.append([n, a])
    residue_tables[str(order)] = pairs
check('all displayed cyclotomic residue tables',
      residue_tables == source['cyclotomic_residue_pairs_n_a'])

n, k, a = 21, 13, 8
check('control parameters', (control['n'], control['k'], control['a']) == (n, k, a))
q = [0] * 43
for exponent, coefficient in ((0,1), (13,-1), (21,-1), (29,-1), (42,1)):
    q[exponent] = coefficient
c = mul(cyclotomic[10], cyclotomic[12])
p = exact_div(q, c)
check('q coefficient vector', q == control['q_coefficients_ascending'])
check('p coefficient vector from integer division', p == control['p_coefficients_ascending'])
check('reciprocal unit degree 34', len(p) == 35 and p == p[::-1] and p[0] == p[-1] == 1)

# Reconstruct the trace polynomial from the reciprocal coefficients, without
# the author's Chebyshev construction or division of the trace polynomial.
C = [[2], [0, 1]]
for j in range(2, 18): C.append(add([0] + C[-1], neg(C[-2])))
trace = [p[17]]
for j in range(1, 18): trace = add(trace, [p[17+j]*v for v in C[j]])
check('trace polynomial via reciprocal triangular basis', trace == control['trace_p_coefficients_ascending'])

codes = []
modular_status = {}
for prime in (2, 3, 5, 7, 11, 13):
    f = [v % prime for v in trace]
    value = [0, 1]
    for j in range(17):
        value = power_mod(value, prime, f, prime)
        if prime == 3: codes.append(sum(v*3**i for i, v in enumerate(value)))
    first = add(power_mod([0, 1], prime, f, prime), [0, -1])
    # Degree 17 is prime: Rabin's criterion has just the divisor test 17/17=1.
    modular_status[str(prime)] = value == [0, 1] and gcd_poly(f, first, prime) == [1]
check('finite-field irreducibility status by custom Frobenius/gcd',
      modular_status == control['trace_modular_irreducibility'])
check('trace irreducible modulo 3', modular_status['3'])
check('GF3 polynomial ternary code', sum((v % 3)*3**i for i, v in enumerate(trace)) == control['trace_GF3_ternary_code'])
check('all GF3 Frobenius remainder codes', codes == control['trace_GF3_frobenius_remainders_codes'])
check('GF3 values at 0,1,2', [evaluate(trace, j) % 3 for j in range(3)] == control['trace_GF3_values_at_0_1_2'])
check('all retained rational trace values',
      {str(Fraction(j,8)): str(evaluate(trace, Fraction(j,8))) for j in range(-15,16)} == control['trace_values'])
left, right = evaluate(trace, Fraction(1,2)), evaluate(trace, Fraction(5,8))
check('trace has a real root in (1/2,5/8)', left < 0 < right)
# The real embedding in (-2,2) makes y^2-4 negative, hence nonsquare in
# Q(y). Together with the degree-17 irreducible trace this proves degree 34.
check('irreducibility payload justified by nonsquare quadratic lift', control['p_irreducible_over_Q'] is True)

# Auxiliary exact real-root counts by a Fraction Sturm implementation.
sturm = [list(map(Fraction, trace)), [Fraction(i*trace[i]) for i in range(1,len(trace))]]
while sturm[-1] != [0]:
    remainder = divrem(sturm[-2], sturm[-1])[1]
    if remainder == [0]: break
    sturm.append(neg(remainder))
def variations(point):
    signs = []
    for f in sturm:
        if point == 'plus': value = f[-1]
        elif point == 'minus': value = f[-1] * (-1)**(len(f)-1)
        else: value = evaluate(f, point)
        if value: signs.append(1 if value > 0 else -1)
    return sum(x != y for x, y in zip(signs, signs[1:]))
check('auxiliary trace real roots in (-2,2)',
      variations(Fraction(-2)) - variations(Fraction(2)) == control['trace_roots_minus2_to2'])
check('auxiliary trace total real-root count',
      variations('minus') - variations('plus') == control['trace_real_roots_total'])

# Independently count marked closed walks rather than calling charpoly.
size = 42
edges = [(j, (j+1) % 13) for j in range(13)]
edges += [(13+j, 13+(j+1) % 29) for j in range(29)]
edges += [(12,13), (20,0)]
check('graph dimension and edge count', size == control['graph_vertices'] and len(edges) == control['graph_edges'])
adj = [[] for _ in range(size)]
for u,v in edges: adj[u].append(v)
def distances(start):
    dist = {start:0}
    queue = [start]
    for u in queue:
        for v in adj[u]:
            if v not in dist: dist[v] = dist[u] + 1; queue.append(v)
    return dist
check('graph strongly connected', all(len(distances(j)) == size for j in range(size)))
depth = distances(0)
period = math.gcd(*(abs(depth[u]+1-depth[v]) for u,v in edges))
check('graph period one', period == 1)
girth = min(distances(v)[u]+1 for u,v in edges)
check('graph girth 13', girth == 13)
walks = [[int(i == j) for j in range(size)] for i in range(size)]
power_traces = [size]
for step in range(1, size+1):
    next_walks = [[0]*size for _ in range(size)]
    for i in range(size):
        for u,v in edges: next_walks[i][v] += walks[i][u]
    walks = next_walks
    power_traces.append(sum(walks[i][i] for i in range(size)))
char_descending = [1]
for j in range(1,size+1):
    numerator = -sum(char_descending[j-i]*power_traces[i] for i in range(1,j+1))
    assert numerator % j == 0
    char_descending.append(numerator//j)
check('graph characteristic polynomial by integer walks/Newton', char_descending[::-1] == q)
check('author graph characteristic status', control['graph_characteristic_polynomial_checked'] is True)

def mobius(n):
    count, candidate = 0, 2
    while candidate*candidate <= n:
        if n % candidate == 0:
            n //= candidate
            if n % candidate == 0: return 0
            count += 1
        candidate += 1
    return (-1)**(count + int(n>1))
def divisors(n): return [j for j in range(1,n+1) if n%j == 0]
def normalized_trace(traces, j):
    value = sum(mobius(j//d)*traces[d] for d in divisors(j))
    assert value % j == 0
    return value//j
def root_power_sums(coefficients, limit):
    desc = coefficients[::-1]
    degree = len(desc)-1
    sums = [degree]
    for j in range(1,limit+1):
        if j <= degree:
            value = -sum(desc[i]*sums[j-i] for i in range(1,j))-j*desc[j]
        else:
            value = -sum(desc[i]*sums[j-i] for i in range(1,degree+1))
        sums.append(value)
    return sums
p_sums = root_power_sums(p,42)
b_p = {j:normalized_trace(p_sums,j) for j in range(1,43)}
b_q = {j:normalized_trace(power_traces,j) for j in range(1,43)}
b_c = {j:sum(mobius(order//j) for order in (10,12) if order % j == 0) for j in range(1,43)}
check('net-trace additivity through degree 42', all(b_p[j]+b_c[j] == b_q[j] for j in b_p))
check('nonnegative graph net traces through degree 42', all(value >= 0 for value in b_q.values()))
negative = [j for j in range(1,13) if b_p[j] < 0]
check('negative indices below girth', negative == control['canonical_negative_indices'] == [1,10,12])
check('negative values all minus one', all(b_p[j] == -1 for j in negative))
check('cyclotomic correction supported at indices <=12', all(order <= 12 for order in (10,12)))
# For all j>12, b_c(j)=0 and b_p(j)=b_q(j)>=0 by primitive orbit counting.
D = sum(j*(-b_p[j]) for j in negative)
check('all-index canonical repair degree', D == control['canonical_repair_degree'] == 23)
check('repair Phi10 Phi12 has degree eight', len(c)-1 == control['optimal_repair_degree'] == 8)
check('repair gives entire nonnegative graph spectrum', mul(p,c) == q)
# Any repair must give positive corrections at both 10 and 12. Distinct
# covering factors have degrees >=phi(10)+phi(12)=8. A single factor
# covering both has order divisible by 60, and degree >=phi(60)=16.
check('degree lower-bound arithmetic', int(sp.totient(10))+int(sp.totient(12)) == 8 and int(sp.totient(60)) == 16)

# Different root-squaring path: eliminate x from p(x) and x^2-y using
# SymPy's resultant, instead of the author's even/odd coefficient identity.
x,y = sp.symbols('x y')
G = sp.Poly.from_list(list(reversed(p)),x,domain=sp.ZZ)
recomputed_steps = []
for iteration, retained in enumerate(control['graeffe_upper_certificate']['steps']):
    norm_squared = sum(int(value)**2 for value in G.all_coeffs())
    exponent = 2**(iteration+1)
    record = {'iteration':iteration, 'norm_squared':str(norm_squared),
              'comparison_exponent':exponent,
              'strict_upper_13_over10':norm_squared*10**exponent < 13**exponent}
    check('Graeffe/resultant norm and inequality at iteration '+str(iteration), record == retained)
    recomputed_steps.append(record)
    if iteration+1 < len(control['graeffe_upper_certificate']['steps']):
        resultant = sp.resultant(G.as_expr(), x*x-y, x)
        G = sp.Poly(resultant,y,domain=sp.ZZ).replace(y,x)
        assert G.degree() == 34 and G.LC() == 1
check('first strict norm certificate occurs at iteration nine',
      len(recomputed_steps) == 10 and all(not row['strict_upper_13_over10'] for row in recomputed_steps[:-1]) and recomputed_steps[-1]['strict_upper_13_over10'])
check('all final resultant coefficients',
      [str(G.nth(j)) for j in range(35)] == control['graeffe_upper_certificate']['final_coefficients_ascending'])
check('Mahler threshold payload', control['graeffe_upper_certificate']['threshold'] == '13/10')

out = {
    'status':'passed', 'checks':checks, 'check_count':len(checks),
    'scope':'Independent exact arithmetic and proof interfaces; no byte/hash gates; no numerical root probe certified; no global cyclotomic-order classification inferred from finite residue tables',
    'graph':{'vertices':size,'edges':len(edges),'girth':girth,'period':period},
    'trace':{'degree':len(trace)-1,'irreducible_mod3':modular_status['3'],
             'quadratic_lift_interval':['1/2','5/8'],
             'quadratic_lift_interval_values':[str(left),str(right)]},
    'repair':{'negative_indices':negative,'negative_values':[b_p[j] for j in negative],
              'canonical_degree':D,'optimal_degree':8,
              'all_index_reason':'b_c(j)=0 for j>12 and b_p=b_q there; graph primitive orbit counts are nonnegative',
              'optimality_reason':'Positive correction at 10 and 12 needs separate degree>=4 factors, or a common factor of order divisible by 60 and degree>=16'},
    'mahler_bound':{'strict_upper':'13/10','resultant_iterations':9,
                    'final_norm_squared':recomputed_steps[-1]['norm_squared'],
                    'comparison_exponent':1024},
    'not_certified':['numerical_probe_only','completeness of cyclotomic orders outside the displayed finite candidate list'],
}
(HERE / 'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
