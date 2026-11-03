"""D212: declared k3..6/all subsets, exact full pencils and trace roots. No imports of prior programs."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from math import isqrt
import argparse,json,time,platform,subprocess,sys,traceback
HERE=(_J_PROGRAM / 'repeated-cell-author.py').parent
CAP=120
START=time.perf_counter()
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


def gate():
    if time.perf_counter()-START>CAP:raise TimeoutError('aggregate120second deadline')
def rat(x):return {'numerator':int(x.numerator),'denominator':int(x.denominator)}
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def transpose(a):return list(map(list,zip(*a)))
def mm(a,b):
    bt=transpose(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]
def det(a):
    a=[r[:] for r in a];n=len(a);previous=1;sgn=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sgn=-sgn
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=v*a[i][j]-a[i][k]*a[k][j];assert z%previous==0
                a[i][j]=z//previous
            a[i][k]=0
        previous=v
    return sgn*a[-1][-1] if n else 1
def graph(k):
    n=4*k+1;V=eye(n);ak=n-1
    for i in range(k):
        a,b,c=3*i,3*i+1,3*i+2;nexta=3*i+3 if i+1<k else ak
        V[a][b]=V[a][c]=V[b][nexta]=-1;V[c][nexta]=1
    path=[0]+list(range(3*k,4*k))+[ak]
    V[0][ak]=-1
    for i,j in zip(path,path[1:]):V[i][j]=-1
    return V
def absolute(V):return [[1 if i==j else -abs(v) for j,v in enumerate(row)] for i,row in enumerate(V)]
def cover(V):
    n=len(V);W=eye(2*n)
    for i in range(n):
        for j in range(i+1,n):
            v=V[i][j]
            for s in (0,1):W[2*i+s][2*j+(s if v<=0 else 1-s)]=-abs(v)
    return W
def cost(V):
    n=len(V);assert all(V[i][i]==1 and not any(V[i][:i]) for i in range(n))
    return {'rank':n,'height':max(abs(x) for r in V for x in r),
            'energy':sum(V[i][j]**2 for i in range(n) for j in range(i+1,n)),
            'full_squared_sum':sum(x*x for r in V for x in r)}
def pencil(V,x):return det([[x*V[i][j]+V[j][i] for j in range(len(V))] for i in range(len(V))])
def coeff(p,t):return [int(x) for x in reversed(p.all_coeffs())]
def sqrtbounds(x):
    assert x>=0;scale=1<<64
    a=isqrt(x.numerator*scale*scale//x.denominator)
    return F(a,scale),F(a+1,scale)
def outerbounds(x):
    assert x>=2
    l,u=sqrtbounds(x*x-4)
    return (x+l)/2,(x+u)/2
def roots_record(p,t,sp):
    n=p.degree();assert n%2==1
    f=sp.div(p,sp.Poly(t+1,t));assert f[1].is_zero
    cs=coeff(f[0],t);h=(n-1)//2;assert cs==cs[::-1]
    z=sp.Symbol('z');E=[sp.Integer(2),z]
    for j in range(2,h+1):E.append(sp.expand(z*E[-1]-E[-2]))
    R=sp.Poly(cs[h]+sum(cs[h+j]*E[j] for j in range(1,h+1)),z)
    assert sp.expand(t**h*R.as_expr().subs(z,t+1/t)-f[0].as_expr())==0
    iv=R.intervals(eps=sp.Rational(1,1<<24));items=[];lo=F(1);hi=F(1);certain=True;nr=0
    for (a,b),m in iv:
        a,b=F(a),F(b);nr+=m
        item={'lower':rat(a),'upper':rat(b),'multiplicity':int(m)}
        if -2<=a<=b<=2:item['type']='unit-circle'
        elif a>2 or b<-2:
            x,y=(a,b) if a>2 else(-b,-a)
            l=outerbounds(x)[0];u=outerbounds(y)[1]
            lo*=l**m;hi*=u**m;item.update(type='exterior-pair',outer_lower=rat(l),outer_upper=rat(u))
        else:item['type']='boundary-undecided';certain=False
        items.append(item)
    certain=certain and nr==R.degree()
    result={'trace_coefficients':coeff(R,z),'trace_degree':R.degree(),'real_root_count':nr,
            'real_intervals':items,'all_trace_roots_real':nr==R.degree(),
            'complete_mahler_product_certified':certain}
    if certain:result['mahler_product_bounds']={'lower':rat(lo),'upper':rat(hi)}
    return result
def save(p,out):
    tmp=p.with_suffix('.partial.json');tmp.write_text(json.dumps(out,indent=2),encoding='utf-8');tmp.replace(p)
def worker(p):
    import sympy as sp
    t=sp.Symbol('t');out={'schema': 'J82-repeated-cell-v1', 'status': 'running', 'inputs': []}
    counts={'subsets':0,'companion_polynomials':0,'pencil_evaluations':0,'full_selected_matrices':0}
    try:
        for k in range(3,7):
            gate();n=4*k+1;q=t+1;d=t*t+1;e=(t-1)**2
            C={-1:0,**{j:sum(t**l for l in range(j+1)) for j in range(k+1)}}
            T={-1:0,0:1,1:e}
            for j in range(2,k):T[j]=sp.expand(e*T[j-1]-4*t*t*T[j-2])
            fk=sp.expand((d*d-t*q*q)*C[k]-2*d*q*t*C[k-1]+q*q*t*t*C[k-2]-q*q*(t**(k+1)+t))
            B=sp.expand(fk*T[k-1]-8*t*t*(d*C[k]-q*t*C[k-1])*T[k-2]+16*t**4*C[k]*T[k-3])
            orig=sp.Poly(q**(k-1)*e**(k-1)*fk,t);V=graph(k)
            rec={'k':k,'original_matrix':V,'original_coefficients':coeff(orig,t),'subsets':[],'companions':[]}
            ps=[]
            for s in range(k+1):
                gate();G=B-2**k*q*(t**(2*k-s)*(C[k]+1)+t**(s+1)*C[k]+t**(k+s+1))
                p0=sp.Poly(sp.expand(q**(k-1)*G),t);assert p0.degree()==n and p0.LC()==1
                ps.append(p0);unit,fac=sp.factor_list(p0)
                pr={'s':s,'coefficients':coeff(p0,t),'factorization':{'unit':int(unit),'factors':[{'coefficients':coeff(f,t),'multiplicity':int(m)} for f,m in fac]},'root_certificate':roots_record(p0,t,sp)}
                rec['companions'].append(pr);counts['companion_polynomials']+=1
            out['inputs'].append(rec)
            for mask in range(1<<k):
                gate();Q=eye(n)
                for i in range(k):
                    if mask>>i&1:
                        for a,row in enumerate([[0,0,1],[1,0,1],[0,1,1]]):
                            for b,v in enumerate(row):Q[3*i+a][3*i+b]=v
                X=mm(transpose(Q),mm(V,Q));s=mask.bit_count();assert det(Q)==1
                cs=cost(X);assert cs=={'rank':n,'height':1,'energy':5*k+2,'full_squared_sum':9*k+3}
                U=absolute(X);vals=[]
                for x in range(n+1):
                    v=pencil(U,x);assert v==int(ps[s].eval(x));vals.append(v);counts['pencil_evaluations']+=1
                item={'mask':mask,'selected_cells':[i for i in range(k) if mask>>i&1],'Q':Q,'det_Q':1,'X':X,'cost':cs,'companion_s':s,'pencil_nodes':list(range(n+1)),'pencil_values':vals}
                if s==k:
                    selected=[]
                    for name,mat,pol in [('original',X,orig),('absolute',U,ps[s]),('proper_cover',cover(X),orig*ps[s])]:
                        vs=[]
                        for x in range(len(mat)+1):
                            gate();v=pencil(mat,x);assert v==int(pol.eval(x));vs.append(v);counts['pencil_evaluations']+=1
                        selected.append({'name':name,'matrix':mat,'cost':cost(mat),'coefficients':coeff(pol,t),'nodes':list(range(len(mat)+1)),'values':vs})
                        counts['full_selected_matrices']+=1
                    rec['all_selected_complete']=selected
                rec['subsets'].append(item);counts['subsets']+=1
                if mask%16==0:out['counts']=counts;save(p,out)
            comparisons=[]
            for a in range(k+1):
                for b in range(a+1,k+1):
                    ca=rec['companions'][a]['root_certificate'];cb=rec['companions'][b]['root_certificate']
                    status='undecided'
                    if ca['complete_mahler_product_certified'] and cb['complete_mahler_product_certified']:
                        def read(d):return F(d['numerator'],d['denominator'])
                        aa=ca['mahler_product_bounds'];bb=cb['mahler_product_bounds']
                        if read(aa['upper'])<read(bb['lower']):status='first-strictly-smaller'
                        elif read(bb['upper'])<read(aa['lower']):status='second-strictly-smaller'
                    comparisons.append({'s_first':a,'s_second':b,'decision':status})
            rec['pairwise_measure_comparisons']=comparisons
            out['counts']=counts;save(p,out)
        out['status']='complete'
    except BaseException:
        out['status']='failed';out['exception']=_record_text(traceback.format_exc())
    out['counts']=counts;pass;pass;save(p,out)
    return 0 if out['status']=='complete' else 1
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--worker',action='store_true');ap.add_argument('--output',type=Path,default=(_J_OUTPUT / 'repeated-cell-output.json'));args=ap.parse_args()
    p=args.output.resolve();assert p.parent == _J_OUTPUT
    if args.worker:return worker(p)
    if p.exists():raise FileExistsError(p)
    process=subprocess.Popen([sys.executable,__file__,'--worker','--output',str(p)])
    timeout=False
    try:code=process.wait(timeout=CAP)
    except subprocess.TimeoutExpired:process.kill();code=process.wait();timeout=True
    out=json.loads(p.read_text()) if p.exists() else {'schema':'J82-repeated-cell-v1','status':'no-checkpoint'}
    out.update(worker_returncode=code, outer_deadline_triggered=timeout)
    if timeout:out['status']='timeout-partial'
    save(p,out);print(json.dumps({'status':out['status'],'counts':out.get('counts'),}))
    return code or int(timeout)
if __name__=='__main__':raise SystemExit(main())
