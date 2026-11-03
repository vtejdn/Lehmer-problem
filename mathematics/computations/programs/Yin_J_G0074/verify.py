"""D162 exact a=3..8 weighted cycles.120s aggregate cap; no search.
Own J72 characteristic/cover patterns reused; integer Bareiss pencils separate.
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

def trace(p):
    cs=coeff(p)
    a=(len(cs)-1)//2
    cheb=[sp.Integer(2),v]
    for j in range(2,a+1):
        cheb.append(sp.expand(v*cheb[-1]-cheb[-2]))
    f=sp.expand(cs[a]+sum(cs[a+j]*cheb[j] for j in range(1,a+1)))
    assert sp.expand(t**a*f.subs(v,t+1/t)-p)==0
    return [int(x) for x in sp.Poly(f,v).all_coeffs()[::-1]]

def main():
    plus=(t-4)*y*y+4*(t-1)*y+4*t-1
    minus=(t-4)*y*y-4*(t-1)*y+4*t-1
    diffplus=sp.expand(plus.subs(y,t*y)-t*t*plus)
    diffminus=sp.expand(minus.subs(y,t*y)-t*t*minus)
    assert sp.expand(diffplus+4*t*(t-1)**2*y+(4*t-1)*(t*t-1))==0
    assert sp.expand(diffminus-4*t*(t-1)**2*y+(4*t-1)*(t*t-1))==0
    controls=[]
    for a in range(3,9):
        tick()
        B=sp.eye(a)
        for i in range(a-1):
            B[i,i+1]=1
        B[a-1,0]=-2
        D=B.applyfunc(abs)
        U=sp.eye(2*a)
        U[:a,a:]=-B
        Uabs=sp.eye(2*a)
        Uabs[:a,a:]=-D
        W=cover(U)
        assert W==W.applyfunc(lambda x: x)  # literal integer matrix retained below
        P=sp.expand(t**(2*a)+1-3*sum(t**j for j in range(1,2*a))+4*t**a)
        A=sp.expand(P-8*t**a)
        assert sp.expand((t-1)*P-plus.subs(y,t**a))==0
        assert sp.expand((t-1)*A-minus.subs(y,t**a))==0
        detB=bareiss(matrix_list(B))
        detD=bareiss(matrix_list(D))
        assert detB==1+2*(-1)**a
        assert detD==1-2*(-1)**a
        endpoints=dict(P1=int(P.subs(t,1)),A1=int(A.subs(t,1)),
                       twice_P3=int(2*P.subs(t,3)),triple_P4=int(3*P.subs(t,4)),
                       triple_A4=int(3*A.subs(t,4)),quadruple_A5=int(4*A.subs(t,5)))
        assert endpoints['P1']==9-6*a and endpoints['A1']==1-6*a
        assert endpoints['twice_P3']==-3**(2*a)+8*3**a+11<0
        assert endpoints['triple_P4']==12*4**a+15>0
        assert endpoints['triple_A4']==-12*4**a+15<0
        assert endpoints['quadruple_A5']==5**(2*a)-16*5**a+19>0
        c=dict(a=a,B=matrix_list(B),D=matrix_list(D),det_B=detB,det_D=detD,
               original=certify(U,P),absolute=certify(Uabs,A),cover=certify(W,sp.expand(P*A)),
               endpoints=endpoints,original_trace_ascending=trace(P),absolute_trace_ascending=trace(A))
        assert c['original']['energy']==c['absolute']['energy']==2*a+3
        assert c['cover']['energy']==4*a+6
        assert c['original']['height']==c['absolute']['height']==c['cover']['height']==2
        controls.append(c)
    f=v**3-3*v**2-6*v+7
    g=v**3-3*v**2-6*v-1
    fs=[int(f.subs(v,x)) for x in [1,-1,7,-7]]
    gs=[int(g.subs(v,x)) for x in [1,-1]]
    assert fs==[-1,9,161,-441] and gs==[-9,1]
    assert controls[0]['original_trace_ascending']==[7,-6,-3,1]
    assert controls[0]['absolute_trace_ascending']==[-1,-6,-3,1]
    return dict(scope='Exactly a=3,4,5,6,7,8; no search;120s aggregate cap',
                coefficient_order='ascending',formal=dict(numerator_plus=str(plus),numerator_minus=str(minus),
                next_difference_plus=str(diffplus),next_difference_minus=str(diffminus)),
                first_index=dict(f_rational_candidates=[1,-1,7,-7],f_values=fs,g_rational_candidates=[1,-1],g_values=gs),
                controls=controls,full_polynomial_count=18,
                full_integer_pencil_count=sum(len(c[key]['pencil_values']) for c in controls for key in ['original','absolute','cover']))

if __name__=='__main__':
    try:
        result=main()
        pass
        tick()
        ((_J_OUTPUT / 'result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'passed':True,'controls':6,'polynomials':18,'pencils':result['full_integer_pencil_count']}))
    except BaseException:
        (_J_OUTPUT / 'failure.json').write_text(json.dumps(dict(traceback=_record_text(traceback.format_exc())), indent=2) + '\n', encoding='utf-8')
        raise
