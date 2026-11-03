---
author: Yin
---

# Counting degree-lowering primes by expanding conjugates

Date: 2026-10-06.
Coordinating AI agent for Yin under [T G0001](../tasks/Yin_T_G0001_v1.md#contract), continuing the primary entropy route.
This weakens the common-good-prime hypothesis of [L G0015](Yin_L_G0015_v1.md#finite-prime-discriminant-gap) on a precisely restricted class.
No unrestricted gap or counterexample is obtained.

## Reuse and search scope

Mat96 Lemma 3, printed p.416 / PDF p.2 of the retained original, states that the number of primes with deg(alpha^p)<deg(alpha) is at most log_2(deg alpha).
Its statement was read from the rendered page in the preceding source inspection.
The source attributes Lemmas 1--3 to Dobrowolski; that original proof was not separately audited.
The argument below uses the same degree-loss mechanism but counts expanding conjugates instead of all conjugates and proves the resulting statement directly.
No novelty claim is made.

A bounded web lookup on 2026-10-06 used the queries "Mahler measure discriminant Matveev degree powers condition algebraic units", "Matveev discriminant Mahler measure remove restriction degree alpha prime", "Matveev discriminant Lehmer relative", and "Mahler discriminant deg prime Matveev 2024".
It did not identify a checked general removal theorem.
The primary [Rhin 2004 opening](https://www.impan.pl/shop/publication/transaction/download/product/87614), already registered as Rhi04, still states Matveev with all-prime preservation.
This is a bounded search outcome, not a claim that no strengthening exists.
Other indexed leads were not adopted.
The retained Mat96 input and the elementary argument below were sufficient, so the search stopped.

<a id="expanding-prime-count"></a>
## Exact fiber count under arbitrary positive powers

Let alpha be a nonzero algebraic number, of degree d.
Let r(alpha)>0 be the number of its distinct conjugates outside the complex unit circle, counted with the usual complex embedding multiplicity (a nonreal conjugate pair contributes two).
For an integer n>=1 write beta=alpha^n, d_n=deg beta and e_n=[Q(alpha):Q(beta)]=d/d_n.
Separability and extension of embeddings imply that each conjugate of beta has exactly e_n preimages among the conjugates of alpha.
Since |z^n|>1 if and only if |z|>1,

\[
 r(\alpha)=e_n r(\alpha^n). \tag{1}
\]

In particular e_n divides r(alpha), as well as d.
A single expanding conjugate forces e_n=1 for every n, regardless of total degree.
This includes the Pisot and Salem situations used earlier; it does not identify the whole reciprocal core with them.

Call a prime p bad for alpha if deg(alpha^p)<d.
This holds exactly when two distinct conjugates alpha_i,alpha_j have ratio a nontrivial p-th root of unity.
If n is coprime to p, their n-th powers remain distinct, are conjugates of alpha^n, and have equal p-th powers.
Therefore p remains bad for alpha^n.

Take any k distinct bad primes p_1,...,p_k.
Successively raise alpha to p_1, then p_2, and so on.
At each step the next prime is still bad by the preceding coprimality observation.
Each relative degree is at least two; by (1) the positive integer number of expanding conjugates drops by that factor.
Thus

\[
 2^k\le r(\alpha),\qquad
 \#\{p:\deg(\alpha^p)<\deg\alpha\}
 \le\lfloor\log_2 r(\alpha)\rfloor. \tag{2}
\]

The proof applies to every finite subset of bad primes and hence also proves that their total set is finite.
No independence of fields or assumption that different primes divide the original degree was used.
The r>0 condition is essential to this argument; for positive Mahler measure of an algebraic integer it follows from its monic root-product formula.
We make no assertion for arbitrary nonintegral alpha whose positive measure may come entirely from its leading coefficient.

<a id="finite-prime-cover-capture"></a>
## Finite-prime cover and a larger finite-capture class

Fix B>0 and an integer R>=1.
Choose K=1+floor(log_2 R) distinct primes p_1,...,p_K, each greater than 2B, and set

\[
 c_{B,R}=\min_{1\le j\le K}
 \frac{\log(p_j/(2B))}{2(p_j+1)}>0. \tag{3}
\]

Let alpha be a nonzero nontorsion algebraic integer of degree d>=2 with D(alpha)=d/|disc(alpha)|^(1/d)<=B and r(alpha)<=R.
At least one of the chosen primes is good by (2).
Applying L G0015 at that prime gives m(alpha)>=c_(B,R).
The good prime may depend on alpha; the finite minimum remains uniform.
No upper bound on d or on the number of unit-circle conjugates is imposed.

Consequently a finite-entropy rational flow attains entropy on a finite set if every positive monic unit primary factor has D<=B and r<=R, for common B,R.
Nonmonic primitive and monic nonunit factors have weight at least log2; positive monic unit factors have degree at least two and satisfy (3).
All positive primary weights are at least eta=min(log2,c_(B,R)), so [L G0002](Yin_L_G0002_v1.md#capture-equivalence) bounds the sum of their lengths by h_alg/eta and gives finite capture.
Zero-entropy primary components may remain infinite-dimensional.
This removes the explicitly assumed common good prime on this restricted class; it does not remove the arithmetic bounds.

For arbitrary positive-measure integral sequences with m(alpha_n)->0, (3) shows that D(alpha_n) and r(alpha_n) cannot both stay bounded, even without degree reduction.
If r stays bounded, then D tends to infinity: any bounded-D subsequence would contradict (3).
If D stays bounded, r tends to infinity by the same argument.
These are necessary conditions, not existence statements.
The all-prime reduced sequence of L G0014 already has D tending to infinity by L G0015 without an r bound.

## Entropy interpretation and next boundary

For a simple rational primary flow of a monic unit polynomial, r is the real dimension of its expanding subspace after extending scalars to R.
The theorem allows unbounded neutral dimension, so its scope is wider than a fixed-rank statement.
For primary powers, expanding dimension includes their lengths; the hypotheses above are stated on irreducible factors and the entropy sum handles those lengths explicitly.

The full target still permits both unbounded D and unbounded expanding-conjugate count.
A bound on r alone would not supply a gap through this estimate; even r=1 leaves D unbounded.
Thus this calculation strengthens the restricted finite-capture theorem but does not solve the Salem subproblem, much less the whole reciprocal-unit case.

## Review

The original author check is retained at [R509](../audits/reviews/Yin_R_G0509_v1.md#original-expanding-count-author-check).
The complete current finite-prime and expanding-count theorem is [C219](../claims/Yin_C_G0219_v1.md#statement), at the [actual whole current self-review](../audits/reviews/Yin_R_G0509_v1.md#current-finite-prime-finding) scope.
