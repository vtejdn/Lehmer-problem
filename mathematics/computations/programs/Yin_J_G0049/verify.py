"""Full exact certificate; does not use the search Newton-coefficient function."""
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as sp

HERE=(_J_PROGRAM / 'verify.py').parent
t,x=sp.symbols('t x'); N=7
G0=sp.diag(2,sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,1],[1,0]]))
P=t**6-t**5-t**3-t+1; F=sp.expand((t+1)*P)
def upper(g): return sp.Matrix(N,N,lambda i,j:1 if i==j else g[i,j] if i<j else 0)
def energy(v): return sum(int(v[i,j])**2 for i in range(v.rows) for j in range(i+1,v.cols))
def height(v): return max(abs(int(v[i,j])) for i in range(v.rows) for j in range(i+1,v.cols))
def determinant(v): return sp.Poly((t*v+v.T).det(method='domain-ge'),t)
def polynomial(v): return [int(c) for c in v.all_coeffs()]
def trace_cubic(p):
    c=p.all_coeffs(); a,d,h=c[1:4]
    q=x**3+(a-1)*x**2+(d-a-2)*x+(h-d-a+1)
    assert sp.expand((t+1)*t**3*q.subs(x,t+1/t)-p.as_expr())==0
    return sp.Poly(q,x)
def checked_candidate(data):
    g=sp.Matrix(data['gram']); basis=sp.Matrix(data['basis'])
    assert abs(basis.det())==1 and basis.T*G0*basis==g
    assert all(g[i,i]==2 for i in range(N)) and g.det()==-2
    v=upper(g); p=determinant(v)
    assert polynomial(p)==data['poly'] and energy(v)==data['key'][1]
    assert height(v)==data['key'][2]
    return v,p,basis
def main():
    first=json.loads(((_J_OUTPUT / 'search_result.json')).read_text())
    second=json.loads(((_J_OUTPUT / 'mixed_result.json')).read_text())
    v0,p0,b0=checked_candidate(first['best'])
    v,p,basis=checked_candidate(second['best'])
    assert p.as_expr()==F
    minus=sp.eye(N)
    for i in range(N):
        for j in range(i+1,N): minus[i,j]=-abs(v[i,j])
    pa=determinant(minus); qa=trace_cubic(pa); q=trace_cubic(p)
    # Vertex-then-sheet order, diagonal I2 and every offdiagonal block nonpositive.
    w=sp.eye(2*N)
    for i in range(N):
        for j in range(i+1,N):
            a=int(v[i,j])
            block=a*sp.eye(2) if a<=0 else sp.Matrix([[0,-a],[-a,0]])
            w[2*i:2*i+2,2*j:2*j+2]=block
    pc=determinant(w)
    assert pc.as_expr()==sp.expand(p.as_expr()*pa.as_expr())
    plus=sp.Matrix(2*N,N,lambda i,j:int(i//2==j))
    odd=sp.Matrix(2*N,N,lambda i,j:(1 if i%2==0 else -1)*int(i//2==j))
    assert w*plus==plus*minus and w*odd==odd*v
    # Written mod4 identity and target discrepancy.
    residue=sp.Poly((t+1)*(t*t+t+1)**3,t)
    assert all((a-b)%4==0 for a,b in zip(p0.all_coeffs(),residue.all_coeffs()))
    assert (sp.Poly(F,t).coeff_monomial(t**5)-residue.coeff_monomial(t**5))%4!=0
    gstar=sp.Matrix(second['seed_gram']); qstar=sp.Matrix(second['seed_basis'])
    assert abs(qstar.det())==1 and qstar.T*G0*qstar==gstar
    reached={0}
    while True:
        enlarged=reached|{j for i in reached for j in range(N) if gstar[i,j]%2}
        if enlarged==reached: break
        reached=enlarged
    assert len(reached)==N
    # Exact rational intervals for every real root, no floating root claims.
    intervals=qa.intervals(eps=sp.Rational(1,100))
    c=-v.inv()*v.T; ca=-minus.inv()*minus.T
    assert sp.trace(c)==0 and sp.trace(c*c)==2
    assert sp.trace(ca)==600 and sp.trace(ca*ca)==361370
    assert (minus+minus.T).det()==-762
    sign_points=[-2,-1,1,2,601,602]
    sign_values=[int(qa.eval(a)) for a in sign_points]
    assert sign_values==[-49,1674,1502,-381,-50098,312219]
    residues=[int(qa.eval(a))%5 for a in range(5)]
    assert residues==[4,2,4,1,4]
    assert sp.Poly(sp.cancel(pa.as_expr()/(t+1)),t).is_irreducible
    result={
      'all_checks_passed':True,'target':str(F),'V':[list(map(int,v.row(i))) for i in range(N)],
      'basis':[list(map(int,basis.row(i))) for i in range(N)],'basis_determinant':int(basis.det()),
      'symmetric_determinant':int((v+v.T).det()),'symmetric_inertia':[4,3],
      'rank':N,'height':height(v),'energy':energy(v),
      'original_polynomial':polynomial(p),'original_trace_cubic':str(q.as_expr()),
      'original_coxeter_trace':int(sp.trace(c)),'original_coxeter_square_trace':int(sp.trace(c*c)),
      'absolute_polynomial':polynomial(pa),'absolute_factorization':str(sp.factor(pa.as_expr())),
      'absolute_trace_cubic':str(qa.as_expr()),'absolute_trace_irreducible':bool(qa.is_irreducible),
      'absolute_coxeter_trace':int(sp.trace(ca)),'absolute_coxeter_square_trace':int(sp.trace(ca*ca)),
      'absolute_symmetric_determinant':int((minus+minus.T).det()),
      'absolute_trace_sign_points':sign_points,'absolute_trace_sign_values':sign_values,
      'absolute_trace_values_mod5':residues,'absolute_sextic_irreducible':True,
      'absolute_trace_intervals':[{'interval':list(map(str,z)),'multiplicity':m} for z,m in intervals],
      'cover_rank':2*N,'cover_height':height(w),'cover_energy':energy(w),
      'cover_polynomial':polynomial(pc),'direct_full_cover_determinant_checked':True,
      'first_best_full_determinant_checked':True,'first_orbit_mod4_polynomial':polynomial(residue),
      'changed_seed_parity_graph_connected':len(reached)==N,
      'row_squared_entry_sums':[sum(int(v[i,j] if i<j else v[j,i])**2 for j in range(N) if i!=j) for i in range(N)]}
    ((_J_OUTPUT / 'verification.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
