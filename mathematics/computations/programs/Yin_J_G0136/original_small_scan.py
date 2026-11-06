import itertools, numpy as np
from numpy.polynomial import chebyshev as ch
for d in [3,4,5]:
 rows={e:set() for e in range(1,7)}
 for a in itertools.product(range(-2,3),repeat=d+1):
  e=sum(x*x for x in a)
  if 0<e<=6:
   ac=tuple(sum(a[i]*a[i+k] for i in range(d+1-k)) for k in range(1,d+1))
   rows[e].add(ac)
 states=[{(0,)*d}]+[set() for _ in range(6)]
 for e in range(1,7):
  for k in range(1,e+1):
   for a in states[e-k]:
    for b in rows[k]:
     states[e].add(tuple(x+y for x,y in zip(a,b)))
 counts=0; failures=[]
 for b in itertools.product(range(-2,3),repeat=d-1):
  b=b+(1,); coeff=(3,)+tuple(2*x for x in b)
  roots=ch.chebroots(ch.chebder(coeff))
  points=[-1,1]+[x.real for x in roots if abs(x.imag)<1e-8 and -1<x.real<1]
  minimum=min(ch.chebval(x,coeff) for x in points)
  if minimum>1e-8:
   counts+=1
   if tuple(2*x for x in b) not in states[6]: failures.append((b,minimum))
 print('d',d,'all exact SOS states',len(states[6]),'screened positive monic inputs',counts,'failures',failures[:10],flush=True)
