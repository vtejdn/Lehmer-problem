---
author: Yin
---

# A reciprocal shell sampled from circular units of conductor 13

This computation for the [strict Mahler shell](../../../tasks/Yin_T_G0001_v1.md#decision-resume-small-shell-2026-11-08) generates each reciprocal polynomial from a real circular unit and an integer.
It requires no positive-measure input.
The pole polynomial is the minimal polynomial of a single Galois orbit of prime-conductor traces.
This differs from the [full Chebyshev grid](../../../ledger/Yin_L_G0462_v2.md#chebyshev-variation).

<a id="unit-law"></a>
## The integer probability space

Let \(p\) be an odd prime, \(n=(p-1)/2\), \(\zeta=\exp(2\pi i/p)\), \(b_k=\zeta^k+\zeta^{-k}\) in decreasing order for \(1\le k\le n\), and \(B(t)=\prod_{k=1}^n(t-b_k)\).
Then \(z^n B(z+z^{-1})=\Phi_p(z)\).
Use the [prime-conductor circular units and their signatures](../../../audits/literature/DDK19/Yin_U001.md#sine-signatures)
\[
   u_j=(\zeta^j-\zeta^{-j})/(\zeta-\zeta^{-1}),\qquad 2\le j\le n .
\]
The finite law here fixes \(p=13\).
Choose \(s\in\{-1,1\}\), \(e_j\in\{-1,0,1\}\) for \(2\le j\le6\), and \(a\in\{-3,-2,-1,0,1,2,3\}\) independently and uniformly.
There are \(2\cdot3^5\cdot7=3402\) parameter atoms.
Let \(C\in\mathbb Z[t]\) be the unique representative of degree below \(n\) with \(C(b_1)=s\prod_j u_j^{e_j}\).
The recurrence for \(U_{j-1}(t/2)\) represents \(u_j\), and the program verifies its inverse in \(\mathbb Z[t]/B\) by multiplication.
Put
\[
       Q=(t-a)B+C,\qquad P(z)=z^{n+1}Q(z+z^{-1}).
\]
Thus \(P\) is monic reciprocal of degree \(14\), with constant one and \(|\operatorname{Res}(B,Q)|=1\) because the conjugate product of \(C(b_1)\) is a unit norm.
The target is the multiplicative measure \(M(P)=\prod_{P(\alpha)=0}\max(1,|\alpha|)\) counting multiplicity.

At \(b_k\) the sign of \(u_j\) is \((-1)^{\lfloor2jk/p\rfloor}\), and \(B'(b_k)\) has sign \((-1)^{k-1}\).
Condition on the event \(A\) that \(C(b_k)/B'(b_k)>0\) for \(k\le r\) and \(<0\) thereafter, for some \(1\le r<n\), and \(Q(-2)/B(-2)<0\).
This is a negative-to-positive transition in increasing trace order.
The sign matrix acts on the exponent parities, so changing individual nonzero exponents from \(1\) to \(-1\) preserves all six signs while changing the magnitudes of the conjugates.
The program verifies the generator signs against rational isolation of the roots of \(B\) before applying the signature table.

<a id="finite-shell"></a>
## Exact mass and the four whole polynomials

There are 34 choices of the signed unit with the required transition.
The 102 parameter atoms satisfying \(A\) give 102 distinct whole polynomials.
For cuts \(r=1,2,3,4,5\) the respective counts are \(13,9,11,5,64\).
Exactly four satisfy \(6/5<M(P)<13/10\), and every other conditioned input has \(M(P)>13/10\).
In particular \(\mathbb P(A,\ 6/5<M(P)<13/10)=4/3402\), the conditional probability is \(4/102\), and \(\mathbb P(1<M(P)\le6/5\mid A)=0\).

Each coefficient prefix runs from the leading coefficient through the central coefficient and determines the entire reciprocal polynomial.
The interval endpoints in the table are exact rational numbers with denominator 1000.
All four hits have \(s=1\).

| \(r\) | \(a\) | \((e_2,e_3,e_4,e_5,e_6)\) | Coefficient prefix | Interval for \(1000M(P)\) | Degree of positive irreducible factor |
| ---: | ---: | --- | --- | --- | ---: |
| 1 | 1 | \((-1,0,-1,1,0)\) | \(1,0,-1,-1,0,1,0,-1\) | \((1250,1260)\) | 14 |
| 2 | 1 | \((0,1,0,-1,0)\) | \(1,0,0,1,1,1,1,1\) | \((1260,1266)\) | 14 |
| 3 | 0 | \((1,0,0,0,-1)\) | \(1,1,2,3,3,3,3,3\) | \((1266,1275)\) | 10 |
| 3 | 2 | \((-1,0,0,0,1)\) | \(1,-1,0,1,0,0,0,1\) | \((1275,1290)\) | 14 |

Exact real-root isolation gives six trace roots in \((-2,2)\) and one above 2 for the first row.
Its degree-seven trace polynomial is irreducible modulo 2.
For a root \(t_0\) of that polynomial the quadratic \(z^2-t_0z+1\) is irreducible over the totally real field \(\mathbb Q(t_0)\), since under an embedding with \(-2<t_0<2\) it has no real root.
Thus the whole degree-fourteen lift is irreducible.
The other three rows each have five trace roots in \((-2,2)\) and one nonreal conjugate pair, with two exterior roots in the lift.
The second and fourth whole lifts are irreducible modulo 2.
The third lift factors as \(\Phi_5(z)(z^{10}+z^8+z^7+z^5+z^3+z^2+1)\), whose degree-ten factor is irreducible modulo 3.
These four distinct measures are generated within this model.
No claim of a new entry in the published small-measure tables is made.

<a id="replay"></a>
## Reproduction and extension

Run the following command from this directory with Python and SymPy (tested with SymPy 1.14).

~~~text
python -B shell.py
~~~

The [program](shell.py) regenerates every numerator modulo \(B\), the exact endpoint sign, every retained polynomial and its whole-measure bounds.
It reuses the integer [Graeffe map from J144](../Yin_J_G0144/pilot.py) and needs no generated files.
After \(h\) squarings the resulting monic degree-\(D\) polynomial with coefficients \(v_j\) has measure \(M(P)^{2^h}\).
Its coefficient lower bound \(\max_j |v_j|/\binom Dj\) and the Parseval鈥揓ensen upper bound \((\sum_j v_j^2)^{1/2}\) give rational comparisons by integer cross multiplication.
At most nine squarings classify all 102 inputs against \(6/5\) and \(13/10\).
At most thirteen separate the four narrower intervals.
The program also checks the root locations and irreducibility certificates in the table with exact polynomial arithmetic.
The model developer executed this program and checked the census with a separate construction in the integral group ring of the cyclic group of order 13 reduced by \(1+\zeta+\cdots+\zeta^{12}=0\).

For a change of conductor the same program tests every possible transition sign vector at \(p=29\) by binary elimination.
The 14-dimensional signature space of the embeddings has an 11-dimensional circular-unit image, and \(r=4,7,9\) are the only attainable cuts, even with arbitrary integer exponents in these generators.
This separate calculation imposes no left endpoint or Mahler condition.
The remaining construction problem is to choose magnitudes in a realizable signature class at varying conductor so that the same positive core has total measure arbitrarily close to one.
The degree-fourteen census supplies no positive input below \(6/5\).

<a id="four-conductors"></a>
## A strict \(6/5\) shell at four further conductors

For the same prime-conductor law, choose all integer exponents in \([-H,H]\), both signs, and \(a\) uniformly in \(\{-10,\ldots,6\}\).
These \(17\) choices of \(a\) cover every integer shift capable of giving \(M(P)\le6/5\) under the condition \(A\).
To see this, the same-sign gaps and the left endpoint force one real zero of \(Q\) in \((-2,b_n)\) and one in each \((b_{k+1},b_k)\) for \(1\le k<n,\ k\ne r\).
The pole residues are strict, and \(Q/B\) has opposite signs at the ends of each of these open intervals, using the one-sided pole limits.
Choose one zero per interval.
For \(R=6/5\), any outstanding trace root \(q\) satisfies \(|q|\le R+R^{-1}=\gamma\), since the reciprocal lift has \(q=\lambda+\lambda^{-1}\) with \(1\le|\lambda|\le R\).
Summing the interval endpoints and using \(a=\sum_{Q(q)=0}q-\sum_{k=1}^n b_k\) gives
\[
     -2-b_1-b_{r+1}-2\gamma<a<-b_r+2\gamma .
\]
As all poles lie strictly between \(-2\) and \(2\), integrality gives \(-10\le a\le6\).

The [four-conductor program](prime_shells.py) first solves the sign equations modulo two and enumerates every allowed magnitude within each matching parity class.
It multiplies the units and inverses in \(\mathbb Z[\zeta_p]\) using cyclic convolution modulo \(\Phi_p\).
After subtracting the common coefficient at the conjugate positions \(n,-n\) from every position, the symmetric Laurent representative has degree below \(n\) in \(\zeta_p+\zeta_p^{-1}\).
The lift is then given by \((1-az+z^2)\Phi_p(z)+z^{n+1}C(z+z^{-1})\).

The integer Newton sums provide a first whole-measure exclusion.
For \(D=p+1\), an input with \(M(P)\le R\) satisfies
\[
   \left|\sum_{P(\alpha)=0}\alpha^k\right|\le D-2+R^k+R^{-k},\qquad k\ge1.
\]
Indeed the reciprocal pairs have larger moduli \(e^{u_j}\), with \(u_j\ge0\) and \(\sum u_j\le\log R\).
The triangle inequality bounds each pair by \(2\cosh(ku_j)\), and \(\cosh(s)+\cosh(t)\le1+\cosh(s+t)\) for \(s,t\ge0\) concentrates the bound in one pair.
Every remaining input is classified by integer Graeffe bounds and exact cyclotomic factorization when a whole measure below \(R\) is certified.
The strict inequalities leave no ties or undecided inputs in the four runs.

| \(p\) | \(H\) | Raw parameter atoms | Signed units with a cut | Conditioned atoms | \(M=1\) | \(1<M<6/5\) | \(M>6/5\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 17 | 3 | 28,000,462 | 46,020 | 212,299 | 0 | 0 | 212,299 |
| 19 | 3 | 196,003,234 | 165,708 | 683,146 | 1 | 0 | 683,145 |
| 23 | 2 | 332,031,250 | 122,670 | 458,025 | 0 | 0 | 458,025 |
| 29 | 1 | 54,206,982 | 4,458 | 10,954 | 0 | 0 | 10,954 |

The unique neutral hit at \(p=19\) has \(r=5,\ s=1,\ a=2\) and exponent vector \((-1,0,0,-1,-1,0,-1,2)\).
Its lift is exactly \(\Phi_{20}\Phi_{21}\).
At \(p=29\), the input \(r=7,\ s=1,\ a=2\) and \((e_2,\ldots,e_{14})=(-1,-1,0,0,1,1,-1,1,0,0,-1,0,0)\) gives \(\Phi_{12}(z)\Phi_{20}(z)P_{18}(-z)\).
Here \(P_{18}\) is the [degree-eighteen Mossinghoff input certified in J144](../Yin_J_G0144/readme.md), with \(1.2013475236<M(P_{18})<1.20143521\).
The program verifies both polynomial identities directly.
This recovers a known positive core from the circular-unit law; it gives no hit below \(6/5\).

Run the four finite censuses from this directory with the same Python environment.

~~~text
python -B prime_shells.py 17 3
python -B prime_shells.py 19 3
python -B prime_shells.py 23 2
python -B prime_shells.py 29 1
~~~

On the developer's first complete run of these four boxes the measured census times, excluding interpreter startup, were respectively \(1.32,5.30,5.03,0.32\) seconds while the processes shared the machine.
The numerator, the transition and the full measure are tested on the same whole polynomial.
The conclusion extends to every integer \(a\) for the stated exponent boxes; different exponents and conductors remain open here.
