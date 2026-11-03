"""Independent complete n=4..12 J76 review, declared cap120s.

No author or previous computation imports. Fraction Gaussian determinants and
Newton interpolation; the author used charpolys plus Bareiss. Saved JSON is a
comparison target only. The source draft is not a required execution input.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from time import perf_counter
import ast
import json
import traceback

HERE = (_J_PROGRAM / 'review_independent.py').parent
CAP = 120
START = perf_counter()
NATIVE = ['readme.md', 'verify.py', 'result.json']
BEFORE = {name: (((_J_PROGRAM if name in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in NATIVE}

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
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def tick():
    if perf_counter() - START > CAP:
        raise TimeoutError('Independent aggregate 120-second cap exceeded')

def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add(p, q):
    out = [0] * max(len(p), len(q))
    for i, v in enumerate(p): out[i] += v
    for i, v in enumerate(q): out[i] += v
    return trim(out)

def neg(p): return [-v for v in p]

def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q): out[i+j] += a*b
    return trim(out)

def divide(p, q):
    a, q = [F(v) for v in trim(p)], [F(v) for v in trim(q)]
    out = [F(0)] * max(1, len(a)-len(q)+1)
    while len(a) >= len(q) and a != [0]:
        k = len(a)-len(q)
        c = a[-1]/q[-1]
        out[k] += c
        for j in range(len(q)): a[k+j] -= c*q[j]
        a = trim(a)
    assert a == [0]
    assert all(c.denominator == 1 for c in out)
    return trim([int(c) for c in out])

def value(p, x):
    s = 0
    for c in reversed(p): s = s*x+c
    return s

def identity(n): return [[int(i == j) for j in range(n)] for i in range(n)]
def trans(a): return [list(c) for c in zip(*a)]
def mm(a, b):
    bt = trans(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]

def det(a):
    """Ordinary rational Gaussian elimination, not fraction-free Bareiss."""
    tick()
    a = [[F(v) for v in row] for row in a]
    n = len(a)
    ans = F(1)
    for k in range(n):
        pivot = next((i for i in range(k,n) if a[i][k]), None)
        if pivot is None: return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            ans = -ans
        v = a[k][k]
        ans *= v
        row = a[k]
        for i in range(k+1,n):
            if not a[i][k]: continue
            ratio = a[i][k]/v
            a[i][k] = F(0)
            for j in range(k+1,n):
                if row[j]: a[i][j] -= ratio*row[j]
    assert ans.denominator == 1
    return int(ans)

def interpolate(vals):
    """p(t)=sum_k Delta^k p(0) binom(t,k), assembled exactly."""
    differences = list(vals)
    basis, answer = [F(1)], [F(0)]
    for k in range(len(vals)):
        answer = add(answer, [differences[0]*v for v in basis])
        differences = [b-a for a,b in zip(differences,differences[1:])]
        basis = [v/F(k+1) for v in mul(basis,[-k,1])]
    assert all(v.denominator == 1 for v in answer)
    return trim([int(v) for v in answer])

def literal_cover(v):
    # Construct two grouped sheets first; then permute to interleaved sheets.
    n = len(v)
    g = identity(2*n)
    for i in range(n):
        for j in range(i+1,n):
            negative, positive = min(v[i][j],0), max(v[i][j],0)
            g[i][j] = g[n+i][n+j] = negative
            g[i][n+j] = g[n+i][j] = -positive
    order = [index for i in range(n) for index in (i,n+i)]
    return [[g[i][j] for j in order] for i in order]

def matrix_certificate(v):
    n = len(v)
    assert all(v[i][j] == int(i == j) for i in range(n) for j in range(i+1))
    times = list(range(n+1))
    vals = [det([[t*v[i][j]+v[j][i] for j in range(n)] for i in range(n)]) for t in times]
    cs = interpolate(vals)
    # Degree <=n follows from the literal linear pencil; its leading det(v)=1.
    assert len(cs) == n+1 and cs[-1] == 1 and cs == cs[::-1]
    up = [v[i][j] for i in range(n) for j in range(i+1,n)]
    return dict(matrix=v, coefficients_ascending=cs, pencil_times=times,
                pencil_values=vals, rank=n, height=max([1]+[abs(x) for x in up]),
                energy=sum(x*x for x in up))

def cyclotomic(n, cache):
    if n in cache: return cache[n]
    p = [-1] + [0]*(n-1) + [1]
    for d in range(1,n):
        if n % d == 0: p = divide(p,cyclotomic(d,cache))
    cache[n] = p
    return p

def bi_add(a,b):
    c = dict(a)
    for k,v in b.items(): c[k] = c.get(k,0)+v
    return {k:v for k,v in c.items() if v}

def bi_mul(a,b):
    c = {}
    for (i,j),v in a.items():
        for (k,l),w in b.items(): c[(i+k,j+l)] = c.get((i+k,j+l),0)+v*w
    return {k:v for k,v in c.items() if v}

def parse_bivariate(text):
    def walk(node):
        if isinstance(node,ast.Constant) and type(node.value) is int:
            return {(0,0):node.value} if node.value else {}
        if isinstance(node,ast.Name) and node.id in ('t','y'):
            return {(1,0) if node.id == 't' else (0,1):1}
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):
            return {k:-v for k,v in walk(node.operand).items()}
        if isinstance(node,ast.BinOp):
            a = walk(node.left)
            if isinstance(node.op,ast.Pow):
                assert isinstance(node.right,ast.Constant) and type(node.right.value) is int
                n = node.right.value
                assert 0 <= n <= 6
                ans = {(0,0):1}
                for _ in range(n): ans = bi_mul(ans,a)
                return ans
            b = walk(node.right)
            if isinstance(node.op,ast.Add): return bi_add(a,b)
            if isinstance(node.op,ast.Sub): return bi_add(a,{k:-v for k,v in b.items()})
            if isinstance(node.op,ast.Mult): return bi_mul(a,b)
        raise ValueError('Unexpected expression syntax')
    return walk(ast.parse(text,mode='eval').body)

def scalar_count(x):
    if isinstance(x,dict): return sum(scalar_count(v) for v in x.values())
    if isinstance(x,list): return sum(scalar_count(v) for v in x)
    return 1

def same(a,b,path=''):
    assert type(a) is type(b), (path,type(a),type(b))
    if isinstance(a,dict):
        assert a.keys() == b.keys(), (path,a.keys(),b.keys())
        for k in a: same(a[k],b[k],path+'/'+k)
    elif isinstance(a,list):
        assert len(a) == len(b), (path,len(a),len(b))
        for i,(x,y) in enumerate(zip(a,b)): same(x,y,path+'/'+str(i))
    else: assert a == b, (path,a,b)

def main():
    saved = json.loads(BEFORE['result.json'])
    assert saved['scope'] == 'Exactly n=4..12, nine fixed controls,120s aggregate cap, no search'
    assert saved['coefficient_order'] == 'ascending'
    f, g = [-1,-1,0,1], [1,-1,-2,1]
    fs, gs = f[::-1], g[::-1]
    formal = saved['formal']
    assert set(formal) == {'F','Fstar','G','Gstar','signed_numerator','absolute_numerator'}
    for key,p in [('F',f),('Fstar',fs),('G',g),('Gstar',gs)]: same(p,formal[key],key)
    for seed,star,key,cycle in [
        (f,fs,'signed_numerator','(t-1)*(t+1)**2*(y+1)-t*(t*y-1)'),
        (g,gs,'absolute_numerator','(t-1)**2*(t+1)*(y-1)-t*(t*y-1)')]:
        target = bi_add({(i,1):c for i,c in enumerate(seed) if c},
                        {(i,0):-c for i,c in enumerate(star) if c})
        assert parse_bivariate(formal[key]) == target == parse_bivariate(cycle)
    bounds = {4:[2,8],5:[3,12],6:[2,18],7:[30],8:[1,1,2,3,5]}
    cache = {}
    reports = []
    all_expected = []
    lehmer = [1,1,0,-1,-1,-1,-1,-1,0,1,1]
    assert len(saved['controls']) == 9
    for n in range(4,13):
        tick()
        d = n+1
        v = identity(d)
        for j in range(1,n-1): v[j-1][j] = -1
        v[n-2][n-1], v[0][n-1], v[n-1][n] = 1,-1,-1
        va = [[int(i == j) if i >= j else -abs(v[i][j]) for j in range(d)] for i in range(d)]
        q = [[0]*d for _ in range(d)]
        q[0][0] = q[n][n] = 1
        for j in range(1,n-2): q[j+1][j] = -1
        for i in range(1,n-1): q[i][n-2], q[i][n-1] = -1,1
        q[n-1][n-2] = 1
        qi = [[0]*d for _ in range(d)]
        qi[0][0] = qi[n][n] = 1
        for j in range(1,n-2): qi[j][1], qi[j][j+1] = 1,-1
        qi[n-2][n-1] = 1
        qi[n-1][1] = qi[n-1][n-1] = 1
        assert mm(q,qi) == mm(qi,q) == identity(d)
        qdet = det(q)
        assert abs(qdet) == 1
        w = mm(trans(q),mm(v,q))
        edges = [[j,j+1] for j in range(1,n-3)] + [[0,n-1],[n-3,n-1],[n-2,n-1],[n-2,n]]
        tree = identity(d)
        for i,j in edges: tree[i][j] = -1
        assert w == tree and all(w[i][j] <= 0 for i in range(d) for j in range(i+1,d))
        p = divide(add([0]*(n-1)+f,neg(fs)),[-1,1])
        a = divide(add([0]*(n-1)+g,neg(gs)),[-1,1])
        # Independently check the cycle/leaf expressions and every endpoint.
        tn = [1] + [0]*(n-2) + [1]
        cycle_p = add(mul([1,2,1],tn),[0]+[-1]*n)
        cycle_a = add(mul([-1,0,1],[-1]+[0]*(n-2)+[1]),[0]+[-1]*n)
        assert p == cycle_p and a == cycle_a
        assert value(p,1) == 8-n and value(a,1) == -n
        c = dict(n=n,Q=q,Q_inverse=qi,Q_determinant=qdet,tree_edges=edges,P1=8-n,A1=-n)
        shapes = [('initial',v,p,n+1),('initial_absolute',va,a,n+1),
                  ('final_tree',w,p,n),('initial_cover',literal_cover(v),mul(p,a),2*n+2),
                  ('final_cover',literal_cover(w),mul(p,p),2*n)]
        for name,mat,poly,energy in shapes:
            c[name] = matrix_certificate(mat)
            assert c[name]['coefficients_ascending'] == poly
            assert c[name]['energy'] == energy and c[name]['height'] == 1
        if n in bounds:
            product = [1]
            for index in bounds[n]: product = mul(product,cyclotomic(index,cache))
            assert product == p
            c['zero_measure_boundary_cyclotomic_indices'] = bounds[n]
        if n == 9:
            assert p == lehmer
            c['original_Lehmer'] = dict(coefficients=lehmer,neutral_degree=0,rank=10,
                energy=9,companion_coefficients=lehmer,cover_coefficients=mul(lehmer,lehmer))
        same(c,saved['controls'][n-4],f'n={n}')
        all_expected.append(c)
        reports.append(dict(n=n,polynomials=5,pencils=sum(len(c[k]['pencil_values']) for k,_,_,_ in shapes),
                            complete_fields_and_types_equal=True,unimodular_determinant=qdet))
    endpoints = []
    for p,points in [(f,[F(1),F(4,3)]),(g,[F(-1),F(0),F(1),F(2),F(5,2)]),(gs,[F(2),F(3)])]:
        endpoints.append(dict(polynomial=p,points=[str(x) for x in points],values=[str(value(p,x)) for x in points]))
    same(endpoints,saved['seed_endpoints'],'endpoints')
    assert saved['full_polynomial_count'] == 45
    assert saved['full_integer_pencil_count'] == sum(x['pencils'] for x in reports) == 612
    assert set(saved) == {'scope', 'coefficient_order', 'formal', 'controls', 'seed_endpoints', 'full_polynomial_count', 'full_integer_pencil_count'}
    pass
    assert all((((_J_PROGRAM if name in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() == before for name,before in BEFORE.items())
    tick()
    return dict(passed=True, domain='All n=4..12, no search', controls=reports, complete_polynomials=45, complete_integer_pencils=612, mathematical_scalar_fields_checked=scalar_count({k: v for k, v in saved.items() if k != 'execution'}), full_native_json_schema_and_mathematical_types_checked=True, method='Fresh Fraction Gaussian elimination and full Newton interpolation; coordinate inverse; grouped-sheet lift; recursive cyclotomic division; restricted polynomial AST verification', imports_author_or_prior_helpers=False, source_scope='No external theorem/source proof checked by this program; all-n statements remain written proof obligations')

if __name__ == '__main__':
    try:
        answer = main()
        ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(answer,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(answer))
    except BaseException:
        report = dict(passed=False, traceback=_record_text(traceback.format_exc()))
        target = _J_OUTPUT/'review_failure.json'
        if target.exists(): target = _J_OUTPUT / 'review_failure.json'
        target.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        raise
