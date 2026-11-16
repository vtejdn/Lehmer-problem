---
author: Yin
---

# Four times the original degree is the first uniform integer multiple for the plastic seed

<a id="statement"></a>
## The cyclic norm on the original Salem polynomial

Let \(f=z^3-z-1,\ g=z^3 f(1/z)=1-z^2-z^3\), and take either sign \(\sigma\in\{1,-1\}\).
For every sufficiently large integer \(N\), let \(S\) be the minimal polynomial of the unique exterior root of \(D=z^Nf-\sigma g\) and let \(d=\deg S\).
Write \(C_n=|\operatorname{Res}(S,z^n-1)|\).
Then
\[
        C_{4d}>(41/20)^d,\qquad
        \log M(S)>\tfrac14\log(41/40).
\]
There is an infinite sequence for the sign \(\sigma=1\) on which
\[
            \log C_d,\quad \log C_{2d},\quad \log C_{3d}=O(\log d).
\]
Here each of the three logarithms satisfies the indicated bound.
Thus four is the least positive integer multiplier \(j\) for which \(d^{-1}\log C_{jd}\) stays bounded away from zero on the complete two-sign family.
It is also the least such multiplier that uniformly exceeds the elementary threshold \(\log 2\).
The actual measures tend to the plastic number.
The [earlier triple-return selection](Yin_C_G0336_v1.md#statement) used a different exponent on a selected progression.
The proof here tests one integer determined solely by the degree after removing all torsion factors.

<a id="transfer"></a>
## A product over the phases, including common torsion roots

The [torsion sieve and circle count](../ledger/Yin_L_G0462_v24.md#all-delays) give \(D=HS\), where \(S\) is monic reciprocal and irreducible, \(H\) is monic and, for large \(N\), its roots are simple and drawn from a fixed finite set of roots of unity.
In particular \(h=\deg H\le30,\ d=N+3-h\).
Put \(k=h-3=N-d,\ a=\max(k,0),\ b=\max(-k,0)\).
For any fixed positive integer \(j\), define the nonzero integer polynomial
\[
                 V_{k,j,\sigma}=z^{ja} f^j-(\sigma z^b g)^j.
\]
It is nonzero because \(f\) and \(g\) have no common root and have nonzero constants.
We claim that for the original degree and original polynomial
\[
                   \log C_{jd}=d\log M(V_{k,j,\sigma})+O_j(\log d).       \tag{1}
\]
Uniformity in \(N,\sigma\) follows below from finite lists of polynomials and algebraic numbers for fixed \(j\).

For \(w^j=1\), let \(Y=\{y:y^d=w\}\), \(E=\{y\in Y:H(y)=0\}\) and \(Q=wz^a f-\sigma z^b g\).
At each \(y\in Y\), \(Q(y)=y^b D(y)\).
All roots of \(D\) in \(Y\) lie in \(H\), since \(S\) is irreducible with an exterior root.
In particular the roots of \(Q\) in \(Y\) are precisely \(E\), with their multiplicities in \(Q\) allowed to differ from those in \(H\).
For \(\eta\in E\),
\[
    |S(\eta)|=|D'(\eta)/H'(\eta)|\asymp d .
\]
Indeed \(D'(\eta)=\sigma g(\eta)(N/\eta+f'(\eta)/f(\eta)-g'(\eta)/g(\eta))\), and \(H'(\eta)\) ranges over a finite set of nonzero values.
Both \(f\) and \(g\) are nonzero on the unit circle.

For a fixed polynomial \(A\) from the finite list of possibilities for \(Q,H\), let \(l\) be its leading coefficient.
Its product of absolute values at \(Y\setminus E\) is \(|l|^{d-|E|}\) times the products of \(|r-y|\) over that set for all roots \(r\), counted with multiplicity.
If \(r\in E\), its product is \(d/\prod_{\eta\in E,\eta\ne r}|r-\eta|\), by differentiating \(z^d-w\).
For \(r\notin E\), its product is \(|r^d-w|/\prod_{\eta\in E}|r-\eta|\).
All denominators belong to a finite positive set.
For \(|r|\ne1\), \(\log|r^d-w|=d\log^+|r|+O(1)\), with the value zero for the logarithmic contribution at \(r=0\).
For a torsion root outside \(E\) the distance is bounded away from zero.
For a nontorsion \(r\) on the circle,
\[
           |r^d-w|\ \ge\ |r^{jd}-1|/j\ \gg_j d^{-C_j},
\]
by factoring \(r^{jd}-w^j\) and applying the [fixed algebraic power estimate](../audits/literature/Wus02/Yin_U001.md#unit-circle).
These estimates yield
\[
      \sum_{y\in Y\setminus E}\log|A(y)|=d\log M(A)+O_j(\log d).
\]
Apply this first to \(Q\), then to \(H\), which has \(M(H)=1\).
Dividing the products on \(Y\setminus E\) and restoring the bounded number of derivative factors on \(E\) gives \(\sum_{y\in Y}\log|S(y)|=d\log M(Q)+O_j(\log d)\).
Finally the product of \(Q\) over \(w^j=1\) is \(V_{k,j,\sigma}\) up to sign.
Multiplicativity of Mahler measure and the partition of the roots of \(z^{jd}-1\) into the sets \(Y\) prove (1).

<a id="fourth"></a>
## The strict fourth-multiple bound

For \(j=4\), the polynomial \(V_k=z^{4a}f^4-z^{4b}g^4\) is independent of the sign \(\sigma\).
There are only the 31 indices \(-3\le k\le27\).
The [exact integer calculation](../computations/programs/Yin_J_G0161/readme.md#four-phase-certificate) proves \(M(V_k)>41/20\) for every one.
For the underlying coefficient test, write \(A(z)=E(z^2)+zO(z^2)\) and replace it by \(E(X)^2-XO(X)^2\).
Its roots are the squares of the roots of \(A\), with multiplicity, and its leading coefficient has modulus the square of the original one.
Thus eight steps give a polynomial \(B\) of the same degree \(s\) and measure \(M(A)^{256}\).
The elementary symmetric functions of its roots give \(|[X^u]B|\le\binom{s}{u}M(A)^{256}\), including for nonmonic \(A\).
For \(A=V_1\) use \(u=1\); for every other \(k\) use \(u=3\).
The integer part of \(|[X^u]B|20^{256}/(\binom{s}{u}41^{256})\) is at least two throughout the list.
Because the list is finite, its smallest measure strictly exceeds \(41/20\).
Applying (1) gives \(C_{4d}>(41/20)^d\) for all sufficiently large \(d\).
At the roots \(x\) of \(S\), \(|x^{4d}-1|\le2\max(1,|x|)^{4d}\).
Taking their product and rearranging gives the claimed lower bound for \(\log M(S)\).

<a id="sharpness"></a>
## A single sequence defeats each smaller multiple

Let \(L\) be the least common multiple of the finitely many orders \(m\) with \(\varphi(m)\le12\), and take \(\sigma=1,\ N\equiv-1\bmod L\).
Every torsion root \(\eta\) of \(D\) has degree at most twelve by the same [torsion sieve](../ledger/Yin_L_G0462_v24.md#all-delays).
Thus \(\eta^N=\eta^{-1}\) and \(f(\eta)-\eta g(\eta)=0\).
The factorization \(f-zg=(z-1)(z+1)^3\) leaves only \(1,-1\), both of which are indeed roots of \(D\) since \(N\) is odd.
Both are simple for large \(N\), so \(H=z^2-1,\ h=2,\ k=-1\), and \(d=N+1\) tends to infinity.
For \(j=1,2,3\) direct multiplication gives
\[
\begin{aligned}
  V_{-1,1,1}&=(z-1)(z+1)^3,\\
  V_{-1,2,1}&=-(z-1)(z+1)^3(z^4+1),\\
  V_{-1,3,1}&=(z-1)(z+1)^3(z^2+z+1)(z^6-z^3+1).
\end{aligned}
\]
Each displayed polynomial has measure one, as \(z^6-z^3+1\) divides \(z^9+1\) and the remaining factors are cyclotomic up to sign.
Equation (1) gives all three logarithmic bounds on the same sequence.

## Assessment history

### Decision fourfold-plastic-return

| Field | Value |
| --- | --- |
| date | 2026-11-16T11:42 |
| status | open |
| reason | Submit the all-delay original-degree return, exact finite bound and simultaneous three-multiple obstruction for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform multiplier and obstruction](#statement) | Both signs and every sufficiently large delay, and one infinite sequence witnessing failure at the first three multiples. |
| argument | [Transfer on the original polynomial](#transfer) | All fixed phases, common torsion roots, varying quotient and fixed algebraic unit-circle distances. |
| argument | [Fourth-multiple estimate](#fourth) | Finite index range, Graeffe coefficient comparison and direct unweighted cyclic-norm certificate. |
| argument | [Three smaller multiples](#sharpness) | Fixed residue class, exact torsion quotient and three simultaneous cyclotomic factorizations. |
| dependency | [Circle and torsion analysis](../ledger/Yin_L_G0462_v24.md#all-delays) | Existence of the original irreducible Salem factor, finite torsion list, simplicity and degree bound. |
| dependency | [Logarithmic distance](../audits/literature/Wus02/Yin_U001.md#wus02-u001) | Fixed nonperiodic algebraic unit-circle points at arbitrary positive integer powers. |
| support | [Exact four-phase certificate](../computations/programs/Yin_J_G0161/readme.md#four-phase-certificate) | All 31 fixed polynomials, original coefficient and exact strict whole-measure bound. |


### Decision fourfold-return-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T11:48 |
| status | proved |
| reason | Adopt the optimal fourth multiple on the complete plastic-seed family after independent proof review and separate exact arithmetic verification. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform multiplier and obstruction](#statement) | Both signs and every sufficiently large delay, and one infinite sequence witnessing failure at the first three multiples. |
| argument | [Transfer on the original polynomial](#transfer) | All fixed phases, common torsion roots, varying quotient and fixed algebraic unit-circle distances. |
| argument | [Fourth-multiple estimate](#fourth) | Finite index range, Graeffe coefficient comparison and direct unweighted cyclic-norm certificate. |
| argument | [Three smaller multiples](#sharpness) | Fixed residue class, exact torsion quotient and three simultaneous cyclotomic factorizations. |
| dependency | [Circle and torsion analysis](../ledger/Yin_L_G0462_v24.md#all-delays) | Existence of the original irreducible Salem factor, finite torsion list, simplicity and degree bound. |
| dependency | [Logarithmic distance](../audits/literature/Wus02/Yin_U001.md#wus02-u001) | Fixed nonperiodic algebraic unit-circle points at arbitrary positive integer powers. |
| support | [Exact four-phase certificate](../computations/programs/Yin_J_G0161/readme.md#four-phase-certificate) | All 31 fixed polynomials, original coefficient and exact strict whole-measure bound. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G0556_v2.md#fourfold-return) | Whole transfer argument, torsion cancellations, uniform positive rate and optimality among integer multiples. |
| review | [Independent integer calculation](../audits/reviews/Yin_R_G0556_v3.md#four-phase-arithmetic-review) | Independent Newton sums verified all 31 inputs and the conversion to the strict threshold. |

## Current assessment
[Selected decision](#decision-fourfold-return-reviewed)
