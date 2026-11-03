from itertools import product
from pathlib import Path
import re
p=Path('mathematics/ledger/Yin_L_G0003_v1.md')
s=p.read_text(encoding='utf-8')
assert not any(ord(c)<32 and c not in '\n\r\t' for c in s)
assert 'k\\,m(p_\\beta)=e\\,m(p_\\alpha)' in s
for link in re.findall(r'\]\(([^)]+)\)',s):
    if '://' not in link:
        f=link.split('#')[0]
        assert (p.parent/f).resolve().exists(),link
cases=0
for modulus in [4,5,6]:
  for a in range(modulus):
    for k in [1,2,3]:
      def phi(v):return (a*v[-1]%modulus,)+v[:-1]
      def add(v,w):return tuple((x+y)%modulus for x,y in zip(v,w))
      def trajectory(F,n):
        T={tuple([0]*k)}; cur=set(F)
        for _ in range(n):
          T={add(v,w) for v in T for w in cur};cur={phi(v) for v in cur}
        return T
      def base(A,n):
        T={0};cur=set(A)
        for _ in range(n):
          T={(x+y)%modulus for x in T for y in cur};cur={a*x%modulus for x in cur}
        return T
      for A in [{1},{1,2},{0,1,2}]:
        F={(x,)+tuple([0]*(k-1)) for x in A}
        for n in range(10):
          q,r=divmod(n,k)
          expected=set(product(*[base(A,q+(i<r)) for i in range(k)]))
          assert trajectory(F,n)==expected
          cases+=1
      sets=[{1,2} if i%2 else {0,1} for i in range(k)]
      R=set(product(*sets)); C=[]
      for r in range(k):
        z={0}
        for i,A in enumerate(sets):
          B={a*x%modulus for x in A} if i>r else A
          z={(x+y)%modulus for x in z for y in B}
        C.append(z)
      for q in range(4):
        assert trajectory(R,q*k)==set(product(*[base(c,q) for c in C]))
        cases+=1
print({'trajectory_set_checks':cases,'local_link_targets':'passed','control_characters':'passed','formula_5_4_spacing':'passed'})
