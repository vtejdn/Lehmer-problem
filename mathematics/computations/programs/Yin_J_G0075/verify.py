"""D166 exact a=3..8 unit cycles with one leaf.120s cap; no search.
Own J74 exact helpers reused; all new fixed matrices and formulas below.
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
    H=t*t-t-1
    Hr=1-t-t*t
    numerator_plus=sp.expand(H*y*y+2*(t*t-1)*y-Hr)
    numerator_minus=sp.expand(H*y*y-2*(t*t-1)*y-Hr)
    assert sp.expand(numerator_plus-(y+1)*(y*H-Hr))==0
    assert sp.expand(numerator_minus-(y-1)*(y*H+Hr))==0
    S6=t**6-t**4-t**3-t*t+1
    P4=t**4-t**3-t*t-t+1
    phi={i:sp.cyclotomic_poly(i,t) for i in [1,2,3,5,6,8,10,12]}
    controls=[]
    for a in range(3,9):
        tick()
        B0=sp.eye(a)
        for i in range(a-1):
            B0[i,i+1]=1
        B0[a-1,0]=-1
        leaf=sp.zeros(1,a)
        leaf[0,0]=1
        B=B0.col_join(leaf)
        D=B.applyfunc(abs)
        U=sp.eye(2*a+1)
        U[:a+1,a+1:]=-B
        Uabs=sp.eye(2*a+1)
        Uabs[:a+1,a+1:]=-D
        W=cover(U)
        C=sum(t**i for i in range(2*a))
        P=sp.expand((t+1)*(t**a+1)**2-t*C)
        A=sp.expand((t+1)*(t**a-1)**2-t*C)
        assert sp.expand((t-1)*P-numerator_plus.subs(y,t**a))==0
        assert sp.expand((t-1)*A-numerator_minus.subs(y,t**a))==0
        minor_rows=list(range(a-1))+[a]
        bm=bareiss(matrix_list(B[minor_rows,:]))
        dm=bareiss(matrix_list(D[minor_rows,:]))
        assert bm==dm==(-1)**(a-1)
        bgram=bareiss(matrix_list(B.T*B))
        dgram=bareiss(matrix_list(D.T*D))
        assert bgram>0 and dgram>0
        Pdiv=sp.div(P,t+1,t)
        Adiv=sp.div(A,t+1,t)
        assert Pdiv[1]==Adiv[1]==0
        assert Pdiv[0].subs(t,-1)==bgram and Adiv[0].subs(t,-1)==dgram
        endpoints=dict(P1=int(P.subs(t,1)),A1=int(A.subs(t,1)),
                       absolute_Qplus2=2**a-5)
        assert endpoints['P1']==8-2*a and endpoints['A1']==-2*a
        assert endpoints['absolute_Qplus2']>0
        c=dict(a=a,B0=matrix_list(B0),B=matrix_list(B),D=matrix_list(D),minor_rows=minor_rows,
               full_rank_minor_B=bm,full_rank_minor_D=dm,det_Gram_B=bgram,det_Gram_D=dgram,
               original=certify(U,P),absolute=certify(Uabs,A),cover=certify(W,sp.expand(P*A)),
               endpoints=endpoints,original_quotient_trace_ascending=trace(Pdiv[0]),
               absolute_quotient_trace_ascending=trace(Adiv[0]))
        assert c['original']['energy']==c['absolute']['energy']==2*a+1
        assert c['cover']['energy']==4*a+2
        assert c['original']['height']==c['absolute']['height']==c['cover']['height']==1
        if a==3:
            assert sp.expand(P-phi[2]*phi[6]*phi[12])==0
            c['original_boundary_factorization']='Phi2 Phi6 Phi12; zero measure'
        if a==4:
            assert sp.expand(P-phi[1]**2*phi[2]*phi[3]*phi[8])==0
            c['original_boundary_factorization']='Phi1^2 Phi2 Phi3 Phi8; zero measure'
        if a==5:
            assert sp.expand(P-phi[2]*phi[10]*S6)==0
            assert sp.expand(A-phi[2]*phi[5]*phi[6]*P4)==0
            c['paid_target_factorization']=dict(original='Phi2 Phi10 S6',absolute='Phi2 Phi5 Phi6 P4',
                cover='Phi2^2 Phi5 Phi6 Phi10 S6 P4',neutral_degrees=[5,7,12])
        controls.append(c)
    f=v**3-4*v-1
    g=v*v-v-3
    assert trace(S6)==[-1,-4,0,1]
    assert trace(P4)==[-3,-1,1]
    sv=[sp.Rational(7,5),sp.Rational(3,2)]
    pv=[sp.Rational(5,3),sp.Rational(7,4)]
    se=[sp.factor(S6.subs(t,x)) for x in sv]
    pe=[sp.factor(P4.subs(t,x)) for x in pv]
    assert se==[sp.Rational(-251,15625),sp.Rational(109,64)]
    assert pe==[sp.Rational(-29,81),sp.Rational(53,256)]
    trvals=[int(f.subs(v,x)) for x in [-2,-1,0,2,3]]
    assert trvals==[-1,2,-1,-1,14]
    assert [int(f.subs(v,x)) for x in [1,-1]]==[-4,2]
    return dict(scope='Exactly a=3,4,5,6,7,8; no search;120s aggregate cap',coefficient_order='ascending',
                formal=dict(H=str(H),Hstar=str(Hr),numerator_plus=str(numerator_plus),numerator_minus=str(numerator_minus),
                            factored_plus=str((y+1)*(y*H-Hr)),factored_minus=str((y-1)*(y*H+Hr))),
                controls=controls,paid_target=dict(S6_coefficients=coeff(S6),P4_coefficients=coeff(P4),
                S6_trace=[-1,-4,0,1],P4_trace=[-3,-1,1],S6_endpoints=[str(x) for x in sv],S6_values=[str(x) for x in se],
                P4_endpoints=[str(x) for x in pv],P4_values=[str(x) for x in pe],S6_trace_points=[-2,-1,0,2,3],
                S6_trace_values=trvals,rational_candidates=[1,-1],rational_values=[-4,2]),
                full_polynomial_count=18,full_integer_pencil_count=sum(len(c[key]['pencil_values'])
                    for c in controls for key in ['original','absolute','cover']))

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
