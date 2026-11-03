"""Exact full certificate, without importing the numerical search or its polynomial routine."""
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as s

HERE=(_J_PROGRAM / 'verify.py').parent
t,x=s.symbols('t x'); n=7
V0=[[1,1,-4,1,1,2,1],[0,1,-1,2,2,2,-1],[0,0,1,-1,-1,-4,-2],
    [0,0,0,1,3,3,-2],[0,0,0,0,1,2,-1],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]
Q0=[[1,1,-2,1,1,1,0],[-1,0,3,0,1,1,-2],[0,0,0,1,0,0,0],
    [0,-1,0,0,-1,0,1],[1,0,-2,0,0,0,1],[0,1,-3,0,1,0,0],[0,0,1,0,0,0,0]]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def trans(a):return list(map(list,zip(*a)))
def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def energy(v):return sum(int(v[i,j])**2 for i in range(v.rows) for j in range(i+1,v.cols))
def coeff(p):return [int(v) for v in s.Poly(p,t).all_coeffs()]
def main():
    data=json.loads(((_J_OUTPUT / 'search_result.json')).read_text());b=data['best']
    v=[r[:] for r in V0];q=[r[:] for r in Q0];u=identity(n)
    max_energy=87;max_height=4;max_basis=3
    for i,forward in b['path']:
        assert isinstance(i,int) and 0<=i<6 and isinstance(forward,bool)
        a=v[i][i+1];m=identity(n)
        block=[[0,1],[1,-a]] if forward else [[-a,1],[1,0]]
        for j in range(2):
            for k in range(2):m[i+j][i+k]=block[j][k]
        v=mul(mul(trans(m),v),m);q=mul(q,m);u=mul(u,m)
        assert all(v[j][k]==int(j==k) for j in range(n) for k in range(j+1))
        max_energy=max(max_energy,sum(v[j][k]**2 for j in range(n) for k in range(j+1,n)))
        max_height=max(max_height,max(abs(z) for row in v for z in row))
        max_basis=max(max_basis,max(abs(z) for row in q for z in row))
    assert v==b['matrix'] and q==b['basis']
    assert max_energy<=160 and max_height<=6 and max_basis<=1000000
    v=s.Matrix(v);q=s.Matrix(q);u=s.Matrix(u)
    g0=s.diag(2,s.Matrix([[0,1],[1,0]]),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,1],[1,0]]))
    assert abs(q.det())==1 and q.T*g0*q==v+v.T
    assert u.T*s.Matrix(V0)*u==v and s.Matrix(Q0)*u==q
    p=s.Poly((t*v+v.T).det(method='domain-ge'),t)
    target=(t+1)*(t**6-t**5-t**3-t+1)
    assert p.as_expr()==s.expand(target)
    va=s.eye(n)
    for i in range(n):
        for j in range(i+1,n):va[i,j]=-abs(v[i,j])
    pa=s.Poly((t*va+va.T).det(method='domain-ge'),t)
    assert coeff(pa)==b['absolute_polynomial']==[1,-80,-5,-7,-7,-5,-80,1]
    r=s.div(pa.as_expr(),t+1,t);assert r[1]==0
    trace=x**3-81*x**2+73*x+79
    assert s.expand(t**3*trace.subs(x,t+1/t)-r[0])==0
    signs={str(z):int(trace.subs(x,z)) for z in [-1,0,1,2,80,81]}
    assert list(signs.values())==[-76,79,72,-91,-481,5992]
    residues=[int(trace.subs(x,j))%5 for j in range(5)]
    assert residues==[4,2,4,1,4]
    endpoint=trace.subs(x,s.Rational(6401,80))
    assert endpoint<0  # 80+1/80; the root in (80,81) is larger.
    assert s.Poly(r[0],t).is_irreducible
    w=s.eye(14)
    for i in range(n):
        for j in range(i+1,n):
            a=v[i,j]
            block=a*s.eye(2) if a<=0 else s.Matrix([[0,-a],[-a,0]])
            w[2*i:2*i+2,2*j:2*j+2]=block
    full=s.Poly(p.as_expr()*pa.as_expr(),t)
    values=[]
    for z in range(-7,8):
        actual=int((z*w+w.T).det(method='domain-ge'))
        assert actual==full.eval(z);values.append(actual)
    # Monic degree14 pencils and15 points certify the entire cover determinant.
    c=-v.inv()*v.T;ca=-va.inv()*va.T
    nn=v-s.eye(n);bb=s.eye(n)-va
    signed_terms=[int((-1)**(k+1)*s.trace(nn**k*nn.T)) for k in range(2,n)]
    absolute_terms=[int(s.trace(bb**k*bb.T)) for k in range(2,n)]
    e=energy(v)
    assert s.trace(c)==0 and s.trace(c*c)==2 and s.trace(ca)==80
    assert sum(signed_terms)==7-e and sum(absolute_terms)==80+7-e
    assert sum(absolute_terms)>=abs(sum(signed_terms))
    out={'status':'passed','path_length':len(b['path']),
         'path_maxima':{'energy':max_energy,'height':max_height,'basis_coordinate':max_basis},
         'root_basis_det':int(q.det()),'change_of_basis_det':int(u.det()),
         'root_basis':q.tolist(),'change_of_basis':u.tolist(),
         'original_polynomial':coeff(p),'absolute_polynomial':coeff(pa),
         'absolute_residual':coeff(r[0]),'trace_cubic':[1,-81,73,79],
         'trace_sign_values':signs,'trace_mod5_values':residues,
         'trace_at_80_plus_inverse80':str(endpoint),'absolute_expanding_root_interval':[80,81],
         'absolute_residual_irreducible_sympy_check':True,
         'rank':7,'height':max(abs(int(v[i,j])) for i in range(n) for j in range(i+1,n)),
         'energy':e,'symmetric_determinant':int((v+v.T).det()),
         'original_trace':int(s.trace(c)),'original_trace_square':int(s.trace(c*c)),'absolute_trace':int(s.trace(ca)),
         'signed_cycle_terms':signed_terms,'absolute_cycle_terms':absolute_terms,
         'cover_rank':14,'cover_energy':energy(w),'cover_polynomial':coeff(full),
         'cover_direct_determinants_at_minus7_to7':values,
         'universal_rank7_trace_lower_bound':12,'universal_rank7_mahler_cosh_lower_bound':'9/2'}
    def integers(o):
        if isinstance(o,s.Integer):return int(o)
        raise TypeError(type(o).__name__)
    ((_J_OUTPUT / 'verification.json')).write_text(json.dumps(out,indent=2,default=integers)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ['root_basis','change_of_basis','cover_direct_determinants_at_minus7_to7']},indent=2,default=integers))
if __name__=='__main__':main()
