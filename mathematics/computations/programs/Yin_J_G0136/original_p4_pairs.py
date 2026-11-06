import itertools
for d, target in [(2,(6,2,2))]:
 rows={}
 for a in itertools.product(range(-2,3),repeat=d+1):
  e=sum(x*x for x in a)
  if 0<e<=6:
   ac=tuple(sum(a[i]*a[i+k] for i in range(d+1-k)) for k in range(d+1))
   rows.setdefault(ac,a)
 pairs=[]
 for ac,a in rows.items():
  bc=tuple(t-x for t,x in zip(target,ac))
  if bc in rows:
   pairs.append((a,rows[bc]))
 print('p4 degree<=2 square pairs:',pairs[:5], 'count',len(pairs))
