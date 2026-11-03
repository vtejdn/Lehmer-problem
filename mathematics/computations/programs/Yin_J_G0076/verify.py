"""D170 fixed n4..12 exact cycle/tree controls, 120s aggregate cap; no search.
Exact helper functions reused from own J75. All new matrices and main below.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from time import perf_counter
import json
import traceback
import sympy as sp

HERE=(_J_PROGRAM / 'verify.py').parent
START=perf_counter()
CAP=120
t,v,y=sp.symbols('t v y')

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
    if perf_counter()-START>CAP:
        raise TimeoutError('Declared120-second aggregate cap exceeded')

def matrix_list(M):
    return [[int(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

def coeff(p):
    return [int(x) for x in sp.Poly(sp.expand(p),t).all_coeffs()[::-1]]

def cover(V):
    W=sp.eye(2*V.rows)
    for i in range(V.rows):
        for j in range(i+1,V.rows):
            x=int(V[i,j])
            if x<=0:
                W[2*i,2*j]=W[2*i+1,2*j+1]=x
            else:
                W[2*i,2*j+1]=W[2*i+1,2*j]=-x
    return W

def bareiss(A):
    n=len(A)
    A=[list(row) for row in A]
    sign=1
    prev=1
    for k in range(n-1):
        tick()
        if A[k][k]==0:
            r=next((r for r in range(k+1,n) if A[r][k]),None)
            if r is None:
                return 0
            A[k],A[r]=A[r],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                val,rem=divmod(num,prev)
                assert rem==0
                A[i][j]=val
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]

def cost(V):
    up=[int(V[i,j]) for i in range(V.rows) for j in range(i+1,V.rows)]
    return dict(rank=V.rows,height=max([1]+[abs(x) for x in up]),energy=sum(x*x for x in up))

def certify(V,expected):
    tick()
    assert V.is_upper and all(V[i,i]==1 for i in range(V.rows))
    p=sp.expand((-V.inv()*V.T).charpoly(t).as_expr())
    assert sp.expand(p-expected)==0
    cs=coeff(p)
    assert cs==cs[::-1]
    M=matrix_list(V)
    pencils=[]
    for h in range(V.rows+1):
        tick()
        A=[[h*M[i][j]+M[j][i] for j in range(V.rows)] for i in range(V.rows)]
        actual=bareiss(A)
        wanted=sum(c*h**j for j,c in enumerate(cs))
        assert actual==wanted
        pencils.append(actual)
    return dict(matrix=M,coefficients_ascending=cs,pencil_times=list(range(V.rows+1)),pencil_values=pencils,**cost(V))


def main():
    F=t**3-t-1
    Fs=1-t*t-t**3
    G=t**3-2*t*t-t+1
    Gs=1-2*t-t*t+t**3
    L=t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1
    assert sp.expand(t**3*F.subs(t,1/t)-Fs)==0
    assert sp.expand(t**3*G.subs(t,1/t)-Gs)==0
    cycplus=(t-1)*(t+1)**2*(y+1)-t*(t*y-1)
    cycminus=(t-1)*(t+1)*(t-1)*(y-1)-t*(t*y-1)
    assert sp.expand(cycplus-(y*F-Fs))==0
    assert sp.expand(cycminus-(y*G-Gs))==0
    boundary={4:[2,8],5:[3,12],6:[2,18],7:[30],8:[1,1,2,3,5]}
    controls=[]
    for n in range(4,13):
        tick()
        V=sp.eye(n+1)
        for i in range(n-2):
            V[i,i+1]=-1
        V[n-2,n-1]=1
        V[0,n-1]=-1
        V[n-1,n]=-1
        Va=V.copy()
        for i in range(n+1):
            for j in range(i+1,n+1):
                Va[i,j]=-abs(V[i,j])
        E=sp.eye(n+1)
        h=sum((E[:,i] for i in range(1,n-1)),sp.zeros(n+1,1))
        cols=[E[:,0]]+[-E[:,i] for i in range(2,n-1)]+[E[:,n-1]-h,h,E[:,n]]
        Q=sp.Matrix.hstack(*cols)
        qdet=bareiss(matrix_list(Q))
        assert abs(qdet)==1
        Qi=Q.inv()
        assert all(x.q==1 for x in Qi)
        assert Q*Qi==Qi*Q==E
        W=Q.T*V*Q
        edges=[(j,j+1) for j in range(1,n-3)]+[(0,n-1),(n-3,n-1),(n-2,n-1),(n-2,n)]
        target=sp.eye(n+1)
        for i,j in edges:
            target[i,j]=-1
        assert W==target
        assert all(W[i,j]<=0 for i in range(n+1) for j in range(i+1,n+1))
        P=sp.expand((t+1)**2*(t**(n-1)+1)-t*sum(t**j for j in range(n)))
        A=sp.expand((t+1)*(t-1)*(t**(n-1)-1)-t*sum(t**j for j in range(n)))
        assert sp.expand((t-1)*P-(t**(n-1)*F-Fs))==0
        assert sp.expand((t-1)*A-(t**(n-1)*G-Gs))==0
        assert P.subs(t,1)==8-n and A.subs(t,1)==-n
        c=dict(n=n,Q=matrix_list(Q),Q_inverse=matrix_list(Qi),Q_determinant=qdet,
               tree_edges=[list(e) for e in edges],P1=8-n,A1=-n,
               initial=certify(V,P),initial_absolute=certify(Va,A),final_tree=certify(W,P),
               initial_cover=certify(cover(V),sp.expand(P*A)),
               final_cover=certify(cover(W),sp.expand(P*P)))
        for key,energy in [('initial',n+1),('initial_absolute',n+1),('final_tree',n),
                           ('initial_cover',2*n+2),('final_cover',2*n)]:
            assert c[key]['energy']==energy and c[key]['height']==1
            assert c[key]['rank']==(2*n+2 if 'cover' in key else n+1)
        if n in boundary:
            fac=sp.prod(sp.cyclotomic_poly(i,t) for i in boundary[n])
            assert sp.expand(P-fac)==0
            c['zero_measure_boundary_cyclotomic_indices']=boundary[n]
        if n==9:
            assert sp.expand(P-L)==0
            c['original_Lehmer']=dict(coefficients=coeff(L),neutral_degree=0,
                  rank=10,energy=9,companion_coefficients=coeff(L),cover_coefficients=coeff(L*L))
        controls.append(c)
    endpoints=[]
    for poly,points in [(F,[sp.Integer(1),sp.Rational(4,3)]),
                        (G,[sp.Integer(-1),sp.Integer(0),sp.Integer(1),sp.Integer(2),sp.Rational(5,2)]),
                        (Gs,[sp.Integer(2),sp.Integer(3)])]:
        endpoints.append(dict(polynomial=coeff(poly),points=[str(x) for x in points],
                             values=[str(sp.factor(poly.subs(t,x))) for x in points]))
    assert endpoints[0]['values']==['-1','1/27']
    assert endpoints[1]['values']==['-1','1','-1','-1','13/8']
    assert endpoints[2]['values']==['1','13']
    return dict(scope='Exactly n=4..12, nine fixed controls,120s aggregate cap, no search',
      coefficient_order='ascending',formal=dict(F=coeff(F),Fstar=coeff(Fs),G=coeff(G),Gstar=coeff(Gs),
        signed_numerator=str(sp.expand(cycplus)),absolute_numerator=str(sp.expand(cycminus))),
      controls=controls,seed_endpoints=endpoints,full_polynomial_count=45,
      full_integer_pencil_count=sum(len(c[key]['pencil_values']) for c in controls
          for key in ['initial','initial_absolute','final_tree','initial_cover','final_cover']))

if __name__=='__main__':
    try:
        result=main()
        pass
        tick()
        ((_J_OUTPUT / 'result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'passed':True,'controls':9,'polynomials':45,'pencils':result['full_integer_pencil_count']}))
    except BaseException:
        (_J_OUTPUT / 'failure.json').write_text(json.dumps(dict(traceback=_record_text(traceback.format_exc())), indent=2) + '\n', encoding='utf-8')
        raise
