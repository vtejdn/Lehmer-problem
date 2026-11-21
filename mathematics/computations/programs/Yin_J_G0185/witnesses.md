---
author: Yin
---

# A Salem unit at consecutive coefficients 2 and 3

<a id="witness"></a>
## An exact factorization

For \(q=2,\ u=1,\ v=13,\ a=2,\ b=-3,\ \epsilon=1\), polynomial multiplication gives
\[
 \begin{aligned}
 2(1+X^{14})-3(X+X^{13})
 &=S(X)\bigl(2X^8-X^7-X^6+X^5+X^3-X^2-X+2\bigr),\\
 S(X)&=X^6-X^5-X^3-X+1 .
 \end{aligned}
\]
Since \(S(1)=-1\) and \(S(2)=23\), \(S\) has a real zero \(\lambda\in(1,2)\).
It is an algebraic unit because \(S\) is monic with constant term one, and \(\lambda>1\) gives infinite multiplicative order.
This supplies a nontorsion unit in a primitive nonmonic parent.
For each \(g\ge1\), every \(g\)-th root of \(\lambda\) is a nontorsion unit of the parent with exponents \(g,13g\), since it satisfies \(S(X^g)=0\).

In fact \(\lambda\) is a Salem number of degree six.
One has \(S(X)=X^3T(X+X^{-1})\) for \(T(t)=t^3-t^2-3t+1\).
The values of \(T\) at \(-2,-1,0,1,2,3\) are \(-5,2,1,-2,-1,10\).
Thus its three real roots lie respectively in \((-2,-1),(0,1),(2,3)\).
The monic cubic has no rational root since neither \(1\) nor \(-1\) is a root.
For the root \(t>2\), the quadratic \(X^2-tX+1\) is irreducible over \(\mathbb Q(t)\), since \(t^2-4\) is negative at an embedding corresponding to either of the first two roots.
The three pairs above the trace conjugates therefore give \(\lambda,\lambda^{-1}\) and four conjugates on the unit circle.

<a id="search"></a>
## Exact finite search

For each \(2\le q\le12\), each coprime \(1\le u\le6,\ u<v\le70\), and each \(b=\pm(q+1),\ \epsilon=\pm1\), the [program](witnesses.py) factors \(q(1+\epsilon X^{u+v})+b(X^u+\epsilon X^v)\) over the integers and checks reconstruction with multiplicities.
Normalizing \(a=q\) covers both signs of \(a\).
Each \(q\) gives 1,016 parents.
The only monic irreducible factors of constant coefficient \(\pm1\) that are not cyclotomic are \(S(X)\) above and \(S(-X)\) in the parent obtained by changing \(b\) to \(3\), each with multiplicity one.
Two additional ranges, \(q=3,\ u\le4,\ 71\le v\le190\) and \(q=4,\ u\le2,\ 71\le v\le160\), under the same sign and coprimality conditions, gave respectively 1,280 and 540 parents without any nontorsion unit factor.
The finite exclusions extend to every common dilation of those parents, because a power of a nontorsion unit is again a nontorsion unit.
These ranges leave existence at higher coefficients outside the search open.

Run the following command from the repository root with Python 3 and python-flint 0.9.0.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0185/witnesses.py
~~~~
