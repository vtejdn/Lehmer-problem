---
author: Yin
---

<a id="bv19b-u003"></a>
# BV19b-U003: Sum-product growth and positive geometric-progression covering

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [BV19b](../../../literature/pdf/BV19b.pdf), arXiv:1810.13363v2, 20 May 2019. Acquisition.

Passages: C-wild definition and Theorem 3, p.2; coefficient inclusion (1), p.3; complete Section 3 and Theorem 8, p.7; references, pp.7--8. Printed and PDF pages coincide.

Inspection: 2026-10-11, human author Yin, direct AI reading and self-review. The finite-field growth/covering proof, singleton and coefficient controls, and the exact necessary BKT04 statement were checked. All BV19b page renders and BKT04's title/theorem page were inspected. Original BKT04 proof and the Tao--Vu book's complete proof were not audited. No independent reviewer or proof-assistant check.


## Assessment

**Audited within scope**, with F07--F09 below and the explicitly accepted external input, for both directions of qualitative Theorem 3.
**Questioned at literal scope** for Theorem 8's all-subsets statement and the product-coefficient display.
The repaired proof uses a parameter-dependent sum-product estimate in the actual large-set range; this unit does not certify the source's universal exponent for every nonsingleton subset.

<a id="bv19b-wild-primes"></a>
## C-wild primes

For fixed C >= 1 put
\[
L=\lfloor C\log p\rfloor,\qquad H=\{x,x^2,\ldots,x^L\}\subset\mathbb F_p.
\]
A prime p is C-wild if some x in F_p^* of multiplicative order at least (log p)^2 has an element of F_p not expressible as a sum of at most floor((log p)^C) elements of H.
Repeated elements are permitted; the empty sum represents zero.
C is fixed independently of p and of its witness x.

Theorem 3 equates the standard nonzero Lehmer gap to the existence of some fixed C>1 for which C-wild primes have zero natural density among primes.
It proves neither that gap nor a covering theorem for every prime.

## Zero-density wild primes imply Lehmer

Fix C>1.
For any fixed epsilon>0 and sufficiently large p, a (1/C,epsilon)-very bad witness has order at least sqrt(p/log p)>(log p)^2.
Put d=floor(C log p) and K=floor((log p)^C).
Since K <= 2^(epsilon*d) for large p, all sums allowed in the definition of C-wild lie in S_d^K(x), of cardinality at most p^(1/C)<p.
Consequently every such very bad prime is C-wild.
Zero density of the latter supplies Theorem 4(b) with delta=1/C for every epsilon>0; [U001](Yin_U001.md#bv19b-u001) then supplies the standard Lehmer gap.

## Lehmer implies zero-density wild primes

By [U002](Yin_U002.md#bv19b-u002), select delta>0 for which the delta-bad prime count is O(X^(1/2)).
If p is not delta-bad, then every x of order at least (log p)^2 has |S_d(x)|>p^delta for some d <= log p, once p is large.
Enlarging d to floor(log p) preserves that lower bound.

The necessary primary sum-product input was checked in the newly retained [BKT04](../../../literature/pdf/BKT04.pdf), arXiv:math/0301343v3, Theorem 1.1, printed/PDF p.1.
[Its statement-only audit](../BKT04/Yin_U001.md#bkt04-u001) owns the precise range and proof-inspection limit:
\[
p^a<|A|<p^{1-a}
\Longrightarrow
\max\{|A+A|,|AA|\}\ge c(a)|A|^{1+\eta(a)},
\quad c(a),\eta(a)>0.
\]
Choose a=min(delta/2,1/16).
As long as p^delta <= |A| <= p^(7/8), these hypotheses hold.
For sufficiently large p the fixed prefactor can be absorbed to obtain growth at least |A|^(1+eta(a)/2).
Thus a bounded number of additions or multiplications, depending only on delta, reaches a set of size at least p^(7/8).

Here is a direct check of the large-set covering step, without importing the unread proof of the paper's reference [TV10], Lemma 4.10.
For B=A minus {0}, N=|B|>p^(3/4) for large p.
Put
\[
F(t)=\sum_{b,c\in B}e^{2\pi i tbc/p}.
\]
Cauchy--Schwarz and additive orthogonality give |F(t)| <= sqrt(p)*N for t != 0.
Multiplicative energy is at most N^3, since fixing three nonzero factors fixes the fourth; hence sum_t |F(t)|^2 <= p*N^3.
The number of representations of y as a sum of three products from B is at least
\[
N^6/p-\sqrt p\,N^4>0.
\]
Therefore BB+BB+BB=F_p, and also AA+AA+AA=F_p.
This is an elementary completion of the same source mechanism, not a new project Claim.

## Track degree and coefficient bounds correctly

For evaluation sets, including their signed coefficients,
\[
S_D^K(x)+S_D^K(x)\subset S_D^{2K}(x),\qquad
S_D^K(x)S_D^K(x)\subset S_{2D}^{(D+1)K^2}(x).
\]
With L=floor(log p), initialize D_0=L,K_0=1 and use the harmless upper envelopes
\[
D_{i+1}=2D_i,\qquad K_{i+1}=(D_i+1)K_i^2.
\]
They cover either operation when L>=1.
The terminal three-product sum fits after one product and two sum envelopes; these envelopes contain zero and their fourfold sum contains the threefold sum.
After a fixed total n>=1, some S_D^K(x)=F_p with
\[
D\le2^n L,\qquad K\le A_n L^{2^n-1}
\]
for a constant A_n.
This follows inductively from D_i+1 <= (2^i+1)L.
All constants and n depend on delta, not on p or x.

<a id="bv19b-positive-covering"></a>
## Convert a signed full field into permitted positive sums

Multiplication by x sends the entire F_p to itself.
Thus
\[
\left\{\sum_{i=1}^{D+1}a_i x^i: -K\le a_i\le K\right\}=\mathbb F_p.
\]
Translate by the fixed element K*sum_(i=1)^(D+1) x^i.
The result is still F_p, and now every coefficient is between 0 and 2K.
Every residue consequently has a representation by at most 2K(D+1) **positive** terms drawn from {x,...,x^(D+1)}.

For sufficiently large p, C=2^(n+1) dominates both the required progression length and the power of log p in that term count:
\[
D+1\le\lfloor C\log p\rfloor,\qquad
2K(D+1)\le(\log p)^C.
\]
This supplies exactly the definition of not C-wild, including its missing constant-term and sign conversions.
Hence large C-wild primes are delta-bad, giving O(X^(1/2))=o(pi(X)).
Finitely many small primes do not affect Theorem 3.

## Located defects and exact controls

**F07 -- false all-subsets formulation, Theorem 8 p.7.**
With p=101 and A={0}, AA+AA+AA={0}, while |A+A|=|AA|=1 is not greater than |A|^(1+epsilon)=1.
The empty set fails too.
At least singleton/empty exclusions are necessary.
The actual application starts with size >p^delta; the verified BKT04 range and the large-set argument above suffice without accepting the literal statement.

**F08 -- product coefficient bound misses one term, p.7.**
The displayed d*K^2 must be (d+1)*K^2.
A central convolution coefficient can have d+1 contributions.
This is also an evaluation-set failure: d=K=1, p=101, x=5 gives (1+x)^2=36, but 36 is absent from S_2^1(5), whose 27 values were enumerated and checked on 2026-10-11.
The corrected target S_2^2 contains it.
The recurrence above retains a polynomial-in-log-p coefficient bound.

**F09 -- signed-covering conclusion needs a completion, p.7.**
Inclusion (1) by itself gives signed sums, while C-wild permits positive sums of positive powers only.
Multiplying by x removes the constant term, and one fixed translation changes signed coefficients into nonnegative coefficients while preserving the full field.
The explicit bound 2K(D+1) verifies the permitted number of terms.
Merely replacing each negative term by p-1 positive copies would lose the polylogarithmic bound.

## Dependency and search limits

The source's internal [TV10] is a Tao--Vu book citation, not an existing EMA key.
The [author's public book page](https://www.math.ucla.edu/~tao/preprints/books.html) was checked; its [linked sample](https://www.math.ucla.edu/~tao/preprints/additive_sample.dvi) is a DVI artifact, and the original Corollary 2.58/Lemma 4.10 pages were not directly inspected.
The [author-maintained errata page](https://terrytao.wordpress.com/books/additive-combinatorics/) also records corrections to Lemma 4.10's proof.
The audit therefore uses the identified BKT04 primary theorem for growth and the displayed elementary saturation calculation for the large-set step.

The bounded searches used the exact BV19b title and DOI, exact-title plus erratum/correction terms, the cited theorem numbers and the author's official book pages.
Search stopped when the needed primary range was available.
No author-confirmed BV19b erratum was established; no absence claim, extension-field transfer, individual-prime guarantee, or full BKT04/book audit is asserted.
