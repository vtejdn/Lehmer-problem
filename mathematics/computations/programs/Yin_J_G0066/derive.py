"""Declared three-input, k=1,2 norm-moment and 16-step exact direction pilot."""
import json, math, time
from fractions import Fraction
from functools import reduce
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as S

START=time.perf_counter()
def gate():
    if time.perf_counter()-START>120: raise RuntimeError('author 120-second cap reached')
t,x=S.symbols('t x')
INPUTS=[('quartic',t**4-t**3-t**2-t+1),('sextic',t**6-t**5-t**3-t+1),
        ('Lehmer',t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1)]
def sparse_mul(a,b):
    out={}
    for i,(u,c) in enumerate(a.items()):
        if i%32==0: gate()
        for v,e in b.items():
            z=tuple(y+w for y,w in zip(u,v)); out[z]=out.get(z,0)+c*e
    return {u:c for u,c in out.items() if c}
def sphere_moment(poly,s):
    total=Fraction(0)
    for u,c in poly.items():
        if any(k%2 for k in u): continue
        num=c; den=1
        for k in u:
            for j in range(1,k,2): num*=j
        for j in range(sum(u)//2): den*=s+2*j
        total+=Fraction(num,den)
    return total
def ev(poly,c): return sum(a*math.prod(v**k for v,k in zip(c,u)) for u,a in poly.items())
def nearest(a,b):
    sg=1 if a>=0 else -1; return sg*((2*abs(a)+b)//(2*b))
def primitive(c):
    g=reduce(math.gcd,c); return tuple(v//g for v in c)
def fs(q): return str(q.numerator)+'/'+str(q.denominator)
rows=[]
for name,P in INPUTS:
    gate(); d=S.degree(P,t); s=int(d//2)
    # Descending elimination reconstructs Q from the full reciprocal input.
    rem=S.expand(P); Q=0
    for j in range(s,-1,-1):
        a=rem.coeff(t,s+j); Q+=a*x**j
        rem=S.expand(rem-a*S.expand(t**s*(t+1/t)**j))
    assert rem==0 and S.Poly(Q,x).is_irreducible and S.Poly(P,t).is_irreducible
    cs=S.symbols('c0:'+str(s)); U=[S.Integer(1),x]
    for j in range(2,s): U.append(S.expand(x*U[-1]-U[-2]))
    V=sum(cs[j]*U[j] for j in range(s))
    N=S.Poly(S.resultant(Q,V,x),*cs)
    nd={tuple(u):int(a) for u,a in N.terms()}
    derivatives=[{tuple(u[j]-(j==i) for j in range(s)):a*u[i] for u,a in nd.items() if u[i]} for i in range(s)]
    nsq=sparse_mul(nd,nd); moments=[]
    for k,terms in [(1,nsq),(2,sparse_mul(nsq,nsq))]:
        A=sphere_moment(terms,s); D=math.comb((k+1)*s-1,s-1)
        ends=abs(int(P.subs(t,1)*P.subs(t,-1)))
        lower=math.log(ends)/(2*s)-math.log(2)/2+math.log(A.numerator/A.denominator)/(2*k*s)
        moments.append({'k':k,'A':fs(A),'dimension':D,'lower_discovery':lower,'upper_discovery':lower+math.log(D)/(2*k*s)})
    starts=[tuple(int(i==j) for i in range(s)) for j in range(s)]+[(1,)*s,tuple((-1)**j for j in range(s))]
    paths=[]; best=None
    for start in starts:
        c=start; path=[]
        for step in range(17):
            gate(); nv=ev(nd,c); E=2*sum(v*v for v in c)
            ratio=Fraction(ends*nv*nv,E**s)
            entry={'step':step,'c':c,'norm':nv,'energy':E,'exp_dB':fs(ratio),'B_discovery':math.log(ratio.numerator/ratio.denominator)/(2*s)}
            path.append(entry)
            if best is None or ratio>best[0]: best=(ratio,c,nv,E)
            if step<16:
                grad=[ev(p,c) for p in derivatives]; scale=max(map(abs,grad)); assert scale
                c=primitive(tuple(nearest(1024*a,scale) for a in grad)); assert any(c)
        paths.append(path)
    ratio,c,nv,E=best
    Vbest=S.expand(V.subs(dict(zip(cs,c))))
    C=S.expand(sum(c[j]*(t**(s+j+1)-t**(s-j-1)) for j in range(s)))
    R=int(S.resultant(P,C,t)); assert R==int(P.subs(t,1)*P.subs(t,-1))*nv*nv
    assert int(S.Poly(C,t).content())==1 and sum(int(z)**2 for z in S.Poly(C,t).all_coeffs())==E
    qints=[([str(a),str(b)],int(mult)) for (a,b),mult in S.Poly(Q,x).intervals(eps=S.Rational(1,10**12))]
    assert len(qints)==s and all(mult==1 for _,mult in qints)
    assert sum(Fraction(ab[0])>2 for ab,_ in qints)==1
    assert sum(-2<Fraction(ab[0]) and Fraction(ab[1])<2 for ab,_ in qints)==s-1
    pints=S.Poly(P,t).intervals(eps=S.Rational(1,10**12))
    expanding=[(a,b) for (a,b),mult in pints if a>1]
    assert len(expanding)==1
    blo,bhi=map(Fraction,map(str,expanding[0])); advantage=ratio>bhi**(2*s)
    ints=[([str(a),str(b)],int(mult)) for (a,b),mult in S.Poly(Vbest,x).intervals(eps=S.Rational(1,10**10))] if S.degree(Vbest,x)>0 else []
    inside=int(S.Poly(Vbest,x).count_roots(-2,2)) if ints else 0
    if name=='quartic':
        assert Fraction(225,32)<blo**4
        income_factor=None; aux_measure=['512/1','512/1']
    elif name=='sextic':
        income_factor=Fraction(21,20); aux_measure=['512/1','512/1']
        assert ratio>income_factor*bhi**(2*s)
    else:
        income_factor=Fraction(7,5); aux_measure=['1152/1','1248/1']
        assert ratio>income_factor*bhi**(2*s)
        assert inside==3 and len(ints)==4 and Fraction(-7,2)<Fraction(ints[0][0][0])<Fraction(ints[0][0][1])<Fraction(-17,5)
    rows.append({'name':name,'P':str(P),'Q':str(Q),'s':s,'norm_terms':[{'exponent':u,'coefficient':a} for u,a in nd.items()],
      'moments':moments,'paths':paths,'trace_root_intervals':qints,
      'best':{'c':c,'V':str(Vbest),'C':str(C),'norm':nv,'resultant':R,'energy':E,'exp_dB':fs(ratio),
        'B_discovery':math.log(ratio.numerator/ratio.denominator)/(2*s),'beta_interval':[fs(blo),fs(bhi)],
        'm_discovery':math.log(float((blo+bhi)/2)),'certified_B_above_m':advantage,
        'certified_exp_dB_over_beta_d_exceeds':fs(income_factor) if income_factor else None,
        'actual_degree':int(S.degree(C,t)),'leading':int(S.LC(S.Poly(C,t))),'content':1,
        'trace_aux_intervals':ints,'trace_aux_roots_inside_minus2_2':inside,
        'all_aux_roots_on_circle':inside==int(S.degree(Vbest,x)) and int(S.degree(Vbest,x))==s-1,
        'auxiliary_M_interval':aux_measure,
        'degree_energy_mean':fs(Fraction(sum(j*int(a)**2 for (j,),a in S.Poly(C,t).terms()),E)),
        'rho_l1_over_l2_squared':fs(Fraction(sum(abs(int(a)) for a in S.Poly(C,t).all_coeffs())**2,E))}})
    print(name, rows[-1]['best'],flush=True)
gate()
output={'scope': 'Three predetermined actual inputs, k=1,2, s+2 starts, 16 steps each; no expanded domain', 'rounding': 'nearest integer with half ties away from zero, normalize max gradient to 1024, divide positive gcd', 'rows': rows}
(_J_OUTPUT / 'derivation.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print('complete', len(rows), 'declared inputs')
