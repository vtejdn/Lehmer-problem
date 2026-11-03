from fractions import Fraction as F
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

def trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def scale(a,s): return trim([s*x for x in a])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def ev(p,x):
    z=0
    for a in reversed(p): z=z*x+a
    return z

C=[[2],[0,1]]
for j in range(2,13):
    C.append(add([0]+C[-1],scale(C[-2],-1)))
Q=[-1,4,40,35,-70,-69,43,43,-11,-11,1,1]
assert mul([-1,1],Q)==add(add(C[12],scale(C[5],-1)),[-1])

p=[1,1,0,-1,-1,0,1,0,-1,-1,0,1,0,-1,-1,0,1,0,-1,-1,0,1,1]
q=[0]*25
for i,a in [(0,1),(7,-1),(12,-1),(17,-1),(24,1)]: q[i]=a
assert mul([1,-1,1],p)==q
assert p==list(reversed(p)) and p[0]==p[-1]==1

# Binary polynomial arithmetic: integer bit i is coefficient of y^i.
f=sum((a%2)<<i for i,a in enumerate(Q))
assert f==4073
def binary_rem(a,b):
    while a.bit_length()>=b.bit_length():
        a^=b<<(a.bit_length()-b.bit_length())
    return a
chain=[]
r=2
for j in range(1,12):
    r=binary_rem(sum(1<<(2*i) for i in range(r.bit_length()) if (r>>i)&1),f)
    chain.append(r)
assert chain==[4,16,256,944,1909,791,908,549,1336,596,2]
assert ev(Q,0)%2==ev(Q,1)%2==1
assert ev(Q,0)==-1 and ev(Q,1)==5

endpoints=[(F(-2),F(-31,16)),(F(-19,16),F(-9,8)),
           (F(-11,16),F(-5,8)),(F(-5,16),F(-1,4)),
           (F(1,16),F(1,8)),(F(17,16),F(9,8)),
           (F(3,2),F(25,16)),(F(29,16),F(15,8))]
sign_checks=[]
for a,b in endpoints:
    va,vb=ev(Q,a),ev(Q,b)
    assert -2<=a<b<2 and va*vb<0
    sign_checks.append({'a':str(a),'b':str(b),'Q_a':str(va),'Q_b':str(vb)})
assert all(endpoints[i][1]<endpoints[i+1][0] for i in range(7))
qbound=ev(q,F(12,11))
assert qbound==F(18502323789625876807201,9849732675807611094711841)>0
assert F(12,11)**3<F(13,10)
assert F(13,10)**3-F(13,10)-1<0

def mu(n):
    parity=0
    d=2
    while d*d<=n:
        if n%d==0:
            n//=d
            parity+=1
            if n%d==0: return 0
        d+=1
    if n>1: parity+=1
    return -1 if parity%2 else 1

a=list(reversed(p))
traces=[len(p)-1]
for n in range(1,7):
    traces.append(-sum(a[j]*traces[n-j] for j in range(1,n))-n*a[n])
b=[]
for n in range(1,7):
    net=sum(mu(n//j)*traces[j] for j in range(1,n+1) if n%j==0)
    assert net%n==0
    b.append(net//n)
assert b==[-1,1,1,0,0,-1]
canonical=mul(mul(p,[-1,1]),[-1,0,0,0,0,0,1])
assert len(canonical)-1==29 and sum(abs(c) for c in canonical)==20

out={     'scope':'Exact certificate for q24=Phi6*p22; global net-trace positivity comes from the displayed graph proof',
     'trace_Q_coefficients_ascending':Q,'p_coefficients_ascending':p,
     'q_coefficients_ascending':q,
     'verified_identities':{'Phi6_times_p_equals_q':True,
                            '(y_minus_1)_times_Q_equals_C12_minus_C5_minus_1':True,
                            'p_is_monic_reciprocal_with_constant_one':True},
     'Q_mod2_bitmask':f,'squaring_remainders_for_y_2power1_through11':chain,
     'Q_0':-1,'Q_1':5,'eight_unit_circle_trace_intervals':sign_checks,
     'q_at_12_over_11':str(qbound),'strict_M_upper_bound':'1728/1331 < 13/10 < theta_0',
     'b_p_indices_1_through6':b,'canonical_repair_degree':7,
     'unique_optimal_repair':'Phi_6=t^2-t+1','optimal_repair_degree':2,
     'canonical_completion_coefficients_ascending':canonical,
     'canonical_completion_length':20,'optimal_completion_length':5}
text=json.dumps(out,indent=2)
(_J_OUTPUT / 'result.json').write_text(text+'\n',encoding='utf-8')
print(text)
