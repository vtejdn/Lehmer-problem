---
author: Yin
---

<a id="bv19b-u002"></a>
# BV19b-U002: Exceptional primes and lifting finite polynomial collisions

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [BV19b](../../../literature/pdf/BV19b.pdf), arXiv:1810.13363v2, 20 May 2019.

Passages: Definitions and Theorem 4, p.3; complete Section 2 and Claims 1--3, pp.5--6. Printed and PDF pages coincide.

Inspection: 2026-10-11, human author Yin; direct AI source reading and self-review. All source pages and their renders were inspected; factor integrality, collision existence, resultants, finite-time growth, cyclotomic order and the global prime count were checked as detailed below. The original Hardy--Wright proof of the totient estimate was not reviewed. No second independent reviewer or formal verification.


## Assessment

**Audited within scope**, with the explicit completions and F05--F06 below, for Claim 1's collision transfer, Claim 2's exponential exceptional-prime count, and Theorem 4(a) implies (c) implies (b).
**Questioned at literal scope** for the max/min display and the final base-two exponent.
The repaired argument uses the positive qualitative growth constant from [U001](Yin_U001.md#bv19b-u001), not a certified value 0.44.

<a id="bv19b-bad-primes"></a>
## Bad and very bad primes

Use the [polynomial families and base-two convention](Yin_U001.md#bv19b-polynomial-families).
For all sufficiently large primes p:

- p is delta-bad if some x in F_p^* has order at least (log p)(log log log p), and |S_d(x)| <= p^delta for every integer 0 <= d <= log p.
- p is (delta,epsilon)-very bad if some x in F_p^* has order at least sqrt(p/log p), and |S_d^K(x)| <= p^delta for every integer 0 <= d <= (log p)/delta and 1 <= K <= 2^(epsilon d).

The same x witnesses all degrees and coefficient bounds.
The nested logs are interpreted only where defined and positive; choices for finitely many small primes have no effect on the asymptotic assertions.

Theorem 4 is the equivalence between the standard nonzero Lehmer gap and:
\[
\exists\delta>0\ \forall\epsilon>0:\quad
\#\{p\le X:p\text{ is }(\delta,\epsilon)\text{-very bad}\}=o(\pi(X)),
\]
and
\[
\forall\epsilon>0\ \exists\delta>0:\quad
\#\{p\le X:p\text{ is }\delta\text{-bad}\}\ll_\epsilon X^\epsilon.
\]
The delta and epsilon quantifiers must not be reversed.
These are prime-counting statements, not a deterministic estimate for each prime.

<a id="bv19b-collision-partitions"></a>
## Collision partitions and exceptional primes

Let P_d=S_d-S_d be the integer polynomials of degree at most d with coefficients in {-1,0,1}.
Let I_d consist of the distinct monic Q-irreducible factors of its nonzero members.
A nonzero P in P_d has leading coefficient +/-1; Gauss's lemma therefore puts every such monic factor in Z[X].
This justifies reduction without a denominator exception.

The collision partition pi_(x,d) of S_d identifies P,Q when P(x)=Q(x).
A prime is d-exceptional if it divides Res(D_1,D_2) for some distinct D_1,D_2 in I_d.
These integer resultants are nonzero, since the factors are distinct irreducibles in characteristic zero.
Self-resultants are not used.

For a nonexceptional prime, at most one D in I_d vanishes at a given x in F_p.
If such D exists, choose a complex algebraic root beta of D.
Factoring any nonzero P-Q in Z[X] shows
\[
P(x)=Q(x)\quad\Longleftrightarrow\quad D\mid P-Q
\quad\Longleftrightarrow\quad P(\beta)=Q(\beta).
\]
Thus pi_(x,d)=pi_(beta,d), including its restrictions to every n <= d.
For x != 0 the factor D is not X and beta != 0.
Existence of D is conditional on a collision; Claim 1 supplies uniqueness, not existence for every residue.

For D in I_d, multiplicativity of Mahler measure and integrality of the complementary factors give M(D) <= d+1.
Coefficient expansion and Jensen's formula give
\[
\|D\|_2\le\|D\|_1\le2^d(d+1).
\]
Hadamard's inequality for the Sylvester determinant consequently yields
\[
0<|\operatorname{Res}(D_1,D_2)|\le
2^{2d^2}(d+1)^{2d}\le 2^{4d^2}.
\]
Its number of distinct prime factors is at most 4d^2.
Also |I_d| <= d*3^(d+1); hence the exceptional-prime count is at most
\[
4d^4 9^{d+1}\le10^d
\]
for sufficiently large d.
This proves the exact qualitative Claim 2.

## Corrected Claim 3 and Theorem 4(a) implies (c)

Assume the standard Lehmer gap and write
\[
\mu=c_*\min\{1,\log_2(1+\kappa)\}>0.
\]
By U001, every nonzero algebraic beta that is not a root of unity satisfies
\[
|S_d(\beta)|\ge2^{\mu(d+1)}.
\]

Choose delta > 0 sufficiently small and let d=floor(sqrt(delta)*log X).
For p in [sqrt(X),X], a delta-bad witness x has |S_d(x)| <= X^delta, with d <= log p once delta < 1/4 and X is large.
Since
\[
2^{d+1}>X^\delta
\]
for small delta and sufficiently large X, evaluation S_d -> F_p has a nontrivial collision.
This is the missing existence justification when the source invokes Claim 1 on p.6.

If p were nonexceptional, lift to beta as above.
Since
\[
X^\delta<2^{\sqrt\delta(d+1)},
\]
choosing sqrt(delta)<mu rules out a non-torsion beta.
Thus beta is a root of unity of order m, with degree at most d.

Retain the established totient estimate stated at BV19b p.6 and attributed there to reference [HW79], Theorem 328:
\[
\varphi(m)\gg m/\log\log m.
\]
Its inversion gives m <= B*d*log log d for an absolute B and large d, with small cases absorbed.
The minimal polynomial is Phi_m in I_d, so Phi_m(x)=0 and x^m=1 in F_p, even when reduction is inseparable.
For p in [sqrt(X),X], the ratio
\[
\frac{B d\log\log d}{(\log p)(\log\log\log p)}
\]
is at most 2B*sqrt(delta)+o(1).
A further fixed decrease of delta makes it less than one, contradicting the witness's order.
Therefore a delta-bad prime in this interval is d-exceptional.

Claim 2 now gives
\[
\#\{p\in[\sqrt X,X]:p\text{ is }\delta\text{-bad}\}
\le10^d\le X^{(\log_2 10)\sqrt\delta}\le X^{4\sqrt\delta}.
\]
Apply the same estimate to X, sqrt(X), X^(1/4), and so on, stopping once the lower remainder is at most X^delta.
Only finitely many steps depending on delta are needed.
Below the source's large-X thresholds use the trivial finite bound.
The resulting global count is
\[
\#\{p\le X:p\text{ is }\delta\text{-bad}\}
\ll_\delta X^{4\sqrt\delta}.
\]
Given any epsilon > 0, also choose 4sqrt(delta)<epsilon.
This proves Theorem 4(c).
No numerical Lehmer gap, optimized exponent, or effective field-uniform prime threshold is obtained.

**F05 -- wrong min/max and an incomplete invocation, p.6.**
The displayed max{2,M(beta)}^c contradicts Theorem 1 and fails for beta=1 at large d, because |S_d(1)|^(1/d) tends to one.
Replace max by min.
If inferring an upper bound on M from the truncated estimate, require the resulting bound to be below two.
The argument above instead uses the uniform non-torsion growth floor directly, and explicitly proves a collision before lifting.
The same page calls this the (c) implies (a) proof, although Section 2 proves (a) implies (c).

**F06 -- wrong base-two exponent, p.6.**
The source declares log to be base two, but log_2(10)>3.
For delta=1/100 and X=2^10000, d=1000 and 10^d>2^3000=X^(3sqrt(delta)).
Replace 3 by 4, or keep log_2(10).
Decreasing delta preserves Theorem 4(c).
The exact inequality 10>2^3 was rerun on 2026-10-11.

## Theorem 4(c) implies (b)

Apply (c) with counting exponent 1/2.
Decrease its chosen delta, if necessary, to less than 1/2; the delta-bad set only becomes smaller.
This fixed delta works for every coefficient exponent epsilon > 0.
A (delta,epsilon)-very bad witness has K=1 available, all required degrees d <= log p available, and order sqrt(p/log p) larger than (log p)(log log log p) for large p.
It is therefore delta-bad.
Its count is O(X^(1/2))=o(pi(X)).

## Verification and limits

Factor integrality, the conditional-existence distinction, collision equivalence, resultant count, truncation boundary, logarithm conversion and finite square-root iteration were checked directly.
The classical totient lower bound is accepted at the precise interface stated in the primary article; its original book proof and earliest attribution were not independently checked.
All source defects above concern the retained, unchanged v2 artifact.
No extension-field, product-ring or individual-prime conclusion is supplied.
