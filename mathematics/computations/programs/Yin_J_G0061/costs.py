"""Complete costs of exactly the five already retained integer representatives."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json,time
import sympy as sp
from lift import V,T,F,array

def coeff(poly):return [int(c) for c in sp.Poly(poly,T).all_coeffs()][::-1]
def proper(a):return all(a[i,i]==1 for i in range(a.rows)) and all(a[i,j]==0 for i in range(a.rows) for j in range(i))
def run():
    start=time.perf_counter();saved=json.loads((_J_OUTPUT / 'lift_result.json').read_text(encoding='utf8'))
    inputs=[]
    for row in saved['tests']:
        inputs.append((row['prime'],row['initial']['basis']))
        for step in row['steps']:inputs.append((step['modulus'],step['basis']))
    assert [m for m,q in inputs]==[2,3,9,27,81]
    f=sum(c*T**i for i,c in enumerate(F));out=[]
    for modulus,q in inputs:
        q=sp.Matrix(q);d=int(q.det());assert d!=0;b=q.T*V*q;a=-b.applyfunc(abs)
        pb=sp.expand((T*b+b.T).det(method='domain-ge'));assert pb==d*d*f
        pa=sp.expand((T*a+a.T).det(method='domain-ge'));w=sp.zeros(12)
        for i in range(6):
            for j in range(6):
                x=int(b[i,j])
                for s in range(2):w[2*i+s,2*j+(s if x<=0 else 1-s)]=-abs(x)
        pw=sp.expand(pb*pa)
        for val in range(-6,7):
            assert time.perf_counter()-start<120
            assert (val*w+w.T).det(method='domain-ge')==pw.subs(T,val)
        energy=sum(int(x)**2 for x in b);height=max(abs(int(x)) for x in b)
        assert sum(int(x)**2 for x in a)==energy and sum(int(x)**2 for x in w)==2*energy
        out.append(dict(modulus=modulus,basis_determinant=d,matrix=array(b),absolute_matrix=array(a),
                        full_entry_lift=array(w),original_polynomial=coeff(pb),absolute_polynomial=coeff(pa),
                        full_cover_polynomial=coeff(pw),absolute_factorization=str(sp.factor(pa)),
                        absolute_zero=pa==0,absolute_coefficient_l1=sum(abs(c) for c in coeff(pa)),
                        rank=int(b.rank()),absolute_rank=int(a.rank()),cover_rank=int(w.rank()),
                        original_degree=int(sp.degree(pb,T)),absolute_degree=None if pa==0 else int(sp.degree(pa,T)),
                        full_cover_degree=None if pw==0 else int(sp.degree(pw,T)),height=height,
                        whole_squared_entry_sum=energy,cover_whole_squared_entry_sum=2*energy,
                        proper_integer_matrix=proper(b),proper_integer_cover=proper(w),
                        direct_cover_determinant_checks=13))
    return dict(scope=dict(moduli=[2, 3, 9, 27, 81], new_basis_search=False), costs=out)
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'cost_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    print(json.dumps([{k:v for k,v in r.items() if k in ['modulus','basis_determinant','height','whole_squared_entry_sum','absolute_zero','absolute_degree','proper_integer_matrix']} for r in out['costs']]))
