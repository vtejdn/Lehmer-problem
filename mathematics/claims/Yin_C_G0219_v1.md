---
author: Yin
---

# Finite-prime discriminant gaps, expanding-conjugate covers and restricted rational capture

The complete complementary proofs below are retained from original2026-10-06 [L15](../ledger/Yin_L_G0015_v1.md) and [L16](../ledger/Yin_L_G0016_v1.md).
Mat96 supplies the identified established finite mechanism; neither a full Lehmer theorem nor a new source audit is claimed.

## Statement

A. For every nonzero nontorsion algebraic integer alpha of degree d>=2, put Delta=absolute polynomial discriminant and D=d/Delta^(1/d).
For every prime p with deg(alpha^p)=d,

    log(p/(2D)) <= (2−1/d)(p+1)m(alpha).

For each fixed B>0 and prime p>2B this gives c_(B,p)=log(p/(2B))/(2(p+1))>0 whenever D<=B and that prime is good.
B. For every nonzero algebraic alpha with r(alpha)>0 expanding conjugates counted with complex multiplicity and every integer n>=1, r(alpha)=[Q(alpha):Q(alpha^n)] r(alpha^n).
In particular the number of degree-lowering primes is at most floor(log_2 r(alpha)), by persistence under coprime powers and successive integer fiber drops.
C. Given B>0 and an integer R>=1, choose 1+floor(log_2 R) distinct primes above2B and the finite minimum of the constants in A.
It bounds m uniformly below on the integral nonzero nontorsion family d>=2,D<=B,r<=R without a common good prime or degree/neutral-dimension bound.
The corresponding finite-entropy rational flows attain entropy on a finite set when every positive monic unit primary factor satisfies the stated common-prime condition in A, or the common B,R bounds in C.
Other positive primitive factors cost at least log2 and zero-weight components may be infinite-dimensional.
D. A prime-stable vanishing positive-measure sequence has D tending to infinity; without reduction, D and r cannot both stay bounded, and boundedness of either forces the other to diverge.
At N=2d the exact Gram ratio R_(2d)=G_(2d)/(2D)^d obeys, only when R_(2d)>1,

    0 < log(G_(2d))/d−log(2D) <= (4−2/d)m.

These are restricted gaps and necessary escape/cancellation conditions.
No full-core B or r bound, all-prime removal theorem, arbitrary nonintegral leading-coefficient version, unrestricted rational capture or uniform small-measure conclusion is supplied.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:55 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every stated nonzero nontorsion integral alpha, fixed B>0 and selected good prime, plus every algebraic alpha with positive expanding count under arbitrary positive powers; all finite-prime cover/rational-capture and necessary-escape quantifiers. |
| argument | [Argument](#argument) | Complete L15 finite Vandermonde proof and L16 embedding-fiber/bad-prime count proof, every positive constant, actual degree/discriminant/Gram normalization, zero-weight/degree-one branches and unbounded-parameter limits. |
| dependency | [Mat96 finite determinant interface](../audits/literature/Mat96/Yin_U001.md#mat96-u001) | Exact finite formula, selected-prime degree and non-torsion guards; no prime asymptotics, threshold or full original-proof audit. The local single-prime proof here is complete. |
| dependency | [Degree reduction](Yin_C_G0218_v1.md#statement) | Actual prime-stable endpoint existence and small-measure reciprocity threshold only, without preservation of the old discriminant parameter. |
| dependency | [Rational primary capture](Yin_C_G0205_v1.md#capture-equivalence) | Exact positive weight and composition-length formula plus finite-dimensional realization; zero-weight components may remain infinite. |
| dependency | [Actual Gram bound](Yin_C_G0209_v1.md#gram-lower-certificate) | Exact Delta G_N upper bound and actual power-basis G_N normalization, used only for the necessary short-window cancellation. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:59 |
| status | proved |
| reason | Adopt the exact complete retained theorem after actual whole current self-review with resolved inputs; every restricted-family, source and failed-generalization boundary remains. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every stated nonzero nontorsion integral alpha, fixed B>0 and selected good prime, plus every algebraic alpha with positive expanding count under arbitrary positive powers; all finite-prime cover/rational-capture and necessary-escape quantifiers. |
| argument | [Argument](#argument) | Complete L15 finite Vandermonde proof and L16 embedding-fiber/bad-prime count proof, every positive constant, actual degree/discriminant/Gram normalization, zero-weight/degree-one branches and unbounded-parameter limits. |
| dependency | [Mat96 finite determinant interface](../audits/literature/Mat96/Yin_U001.md#mat96-u001) | Exact finite formula, selected-prime degree and non-torsion guards; no prime asymptotics, threshold or full original-proof audit. The local single-prime proof here is complete. |
| dependency | [Degree reduction](Yin_C_G0218_v1.md#statement) | Actual prime-stable endpoint existence and small-measure reciprocity threshold only, without preservation of the old discriminant parameter. |
| dependency | [Rational primary capture](Yin_C_G0205_v1.md#capture-equivalence) | Exact positive weight and composition-length formula plus finite-dimensional realization; zero-weight components may remain infinite. |
| dependency | [Actual Gram bound](Yin_C_G0209_v1.md#gram-lower-certificate) | Exact Delta G_N upper bound and actual power-basis G_N normalization, used only for the necessary short-window cancellation. |
| review | [Complete current finding](../audits/reviews/Yin_R_G0509_v1.md#current-finite-prime-finding) | Actual whole exact Statement/Argument verification; constructor self-review, without a new isolated or original-source inspection claim. |

## Complete retained argument

<a id="argument"></a>

### The finite-prime determinant and discriminant theorem

Throughout m=log M uses natural logarithms, d is actual degree, and Delta is the absolute polynomial discriminant, not the number-field discriminant.

<a id="finite-prime-discriminant-gap"></a>
## Direct finite-prime proof

Let alpha be a nonzero nontorsion algebraic integer of degree d>=2, with monic minimal polynomial P and conjugates alpha_i.
Fix a prime p with deg(alpha^p)=d.
Set Q(t)=product_i(t-alpha_i^p), Delta=|disc P| and D=d/Delta^(1/d).
Then Q is monic integral and squarefree, and M(Q)=M(P)^p.

The Frobenius congruence Q=P mod p gives p^d dividing Res(P,Q): write Q=P+pR and take the norm of Q(alpha)=pR(alpha).
The resultant is nonzero.
Indeed, if alpha_i^p=alpha_j, a Galois automorphism sigma of the splitting field sends alpha_i to alpha_j.
Iterating its finite order r gives alpha_i^(p^r)=alpha_i, contrary to nonzero nontorsion.

The quotient J=product_(i<j) (alpha_i^p-alpha_j^p)/(alpha_i-alpha_j) is an integer: each quotient is a polynomial in the roots, and their product is symmetric with integer coefficients.
Degree preservation makes J nonzero.
Hence |disc Q|=Delta J^2>=Delta.
This is the essential degree-preservation step.

Form the Vandermonde matrix W of the 2d distinct roots of P Q with powers 0 through 2d-1.
Its product formula and Hadamard inequality give

\[
 \Delta^2p^{2d}\le |\det W|^2
 =\Delta|\operatorname{disc}Q|\,|\operatorname{Res}(P,Q)|^2
 \le(2d)^{2d}M(P)^{2(2d-1)(p+1)}.
\]

Taking logarithms and dividing by 2d proves

\[
 \log\frac{p}{2D}\le (2-1/d)(p+1)m(\alpha). \tag{1}
\]

For fixed B>0 choose one prime p>2B.
On D<=B and deg(alpha^p)=d this gives

\[
 m(\alpha)\ge c_{B,p}:=\frac{\log(p/(2B))}{2(p+1)}>0. \tag{2}
\]

Only infinitude of primes is needed to choose p, not a quantitative distribution estimate.
Formula (2) is the weaker degree-free form of (1).
It matches Mat96 (7) with k=S=1, f(S)=log p and g(S)=p, as directed in the proof of Theorem 2.
The theorem statement gives the D<=1 case.
General fixed B is a direct specialization of that known mechanism, not a new unrestricted Lehmer bound.

<a id="discriminant-escape"></a>
## Vanishing entropy and restricted finite capture

Suppose alpha_n satisfy all-prime degree preservation and 0<m(alpha_n)->0.
Degree-one nonzero nontorsion integers have m>=log2, so eventually d_n>=2.
For each B choose the fixed prime above; (2) excludes D(alpha_n)<=B for all sufficiently large n.
Therefore

\[
 D(\alpha_n)\longrightarrow\infty,\qquad
 \frac{|\operatorname{disc}(\alpha_n)|^{1/d_n}}{d_n}\longrightarrow0. \tag{3}
\]

[C218](Yin_C_G0218_v1.md#power-degree-reduction) replaces any hypothetical vanishing positive-measure sequence by one satisfying those degree conditions, with no larger positive weights.
Endpoints of a sufficiently small unit sequence are reciprocal by the accepted nonreciprocal gap.
Formula (3) applies to the reduced sequence; twists need not preserve its original discriminant parameter.
This restricts possible counterexamples without constructing or excluding them.

For a concrete restricted rational-flow result, fix B>0 and a prime p>2B.
Assume a finite-entropy Q-linear flow has, for each positive monic unit primary factor, a root alpha with D(alpha)<=B and deg(alpha^p)=deg(alpha).
Such positive unit factors have degree at least two.
Every positive monic nonunit or nonmonic primitive factor has weight at least log2.
All positive weights are therefore at least eta=min(log2,c_(B,p))>0.
By the [C205 primary formula](Yin_C_G0205_v1.md#capture-equivalence), the sum of positive primary lengths is at most h_alg/eta.
Only finitely many positive types occur, and a finite set attains entropy.
Zero-entropy components may remain infinite-dimensional.
Neither a uniform B nor that common-prime hypothesis has been established for the unrestricted Task.

<a id="gram-cancellation-boundary"></a>
## Short-window Gram consequence

For a monic minimal P in the integer core, use [C209](Yin_C_G0209_v1.md#gram-lower-certificate)'s G_N and R_N=Delta G_N/N^d.
At N=2d,

\[
 R_{2d}=G_{2d}/(2D)^d.
\]

If R_(2d)>1, that record's upper bound Delta G_N<=N^d exp(2(N-1)m) gives

\[
 0<d^{-1}\log G_{2d}-\log(2D)\le(4-2/d)m. \tag{4}
\]

Along a hypothetical reduced vanishing-measure sequence passing positivity, D diverges while G_(2d)^(1/d)/(2D) tends to one.
Positivity is compatible with this precise cancellation.
An arithmetic strengthening must prevent it or supply a uniform positive lower bound for the difference in (4).
Discriminant integrality and the estimate above do not do so.

### The expanding-conjugate refinement and finite cover

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
Applying the preceding finite-prime theorem at that prime gives m(alpha)>=c_(B,R).
The good prime may depend on alpha; the finite minimum remains uniform.
No upper bound on d or on the number of unit-circle conjugates is imposed.

Consequently a finite-entropy rational flow attains entropy on a finite set if every positive monic unit primary factor has D<=B and r<=R, for common B,R.
Nonmonic primitive and monic nonunit factors have weight at least log2; positive monic unit factors have degree at least two and satisfy (3).
All positive primary weights are at least eta=min(log2,c_(B,R)), so [C205](Yin_C_G0205_v1.md#capture-equivalence) bounds the sum of their lengths by h_alg/eta and gives finite capture.
Zero-entropy primary components may remain infinite-dimensional.
This removes the explicitly assumed common good prime on this restricted class; it does not remove the arithmetic bounds.

For arbitrary positive-measure integral sequences with m(alpha_n)->0, (3) shows that D(alpha_n) and r(alpha_n) cannot both stay bounded, even without degree reduction.
If r stays bounded, then D tends to infinity: any bounded-D subsequence would contradict (3).
If D stays bounded, r tends to infinity by the same argument.
These are necessary conditions, not existence statements.
The all-prime reduced sequence of C218 already has D tending to infinity by the preceding finite-prime theorem without an r bound.

## Entropy interpretation and next boundary

For a simple rational primary flow of a monic unit polynomial, r is the real dimension of its expanding subspace after extending scalars to R.
The theorem allows unbounded neutral dimension, so its scope is wider than a fixed-rank statement.
For primary powers, expanding dimension includes their lengths; the hypotheses above are stated on irreducible factors and the entropy sum handles those lengths explicitly.

The full target still permits both unbounded D and unbounded expanding-conjugate count.
A bound on r alone would not supply a gap through this estimate; even r=1 leaves D unbounded.
Thus this calculation strengthens the restricted finite-capture theorem but does not solve the Salem subproblem, much less the whole reciprocal-unit case.
