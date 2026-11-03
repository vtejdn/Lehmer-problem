---
author: Yin
---

# Sparse neutral completions from integral matrix excess and the Jordan obstruction

This retains the complete original L25/L26 proofs and exact controls, distinguishing a sufficient bounded-complexity gap from an impossible whole-flow compression target.

## Statement

Let N>=1, A in GL_N(Z), k=||A||_F^2−N, and K(k)=k!3^k2^{k(2k−1)} for integer k>=1.
Then k>=0; if k=0, A is a signed permutation and h_alg(A)=0.
If k>=1, the construction below gives a nonzero monic integer F with at most K(k) nonzero terms and exactly m(F)=h_alg(A), using full natural-log entropy without division by N.
For each fixed integer k0>=1, all such A with k<=k0 satisfy h_alg(A)=0 or h_alg(A)>=eta_{K(k0)}>0 at the accepted DS17 scope.
This uses one fixed term bound K(k0), not an assumed monotonicity of the unspecified source constants eta_K.

If A has a Jordan block of size n>=2 at any complex z nonzero, then k>=1 and n<=K(k)−1.
Define k_min(A) to be the minimum excess among all integral conjugates of all matrices A direct-sum P with arbitrary finite signed permutation P, permitting no added block.
This nonempty subset of nonnegative integers has a minimum, obeys the same bounded-excess gap, and must diverge along any hypothetical sequence with positive entropy tending to0.
For the unipotent Jordan J_n, however, k_min(J_n) tends to infinity while entropy is0; for any fixed B in GL_m(Z), k_min(B direct-sum J_n) tends to infinity while entropy stays h_alg(B).
Thus no finite-valued upper bound on this whole-flow optimized complexity can depend only on entropy, even at fixed positive entropy log(phi).
For every proposed positive-entropy threshold that actually contains a positive-entropy matrix, neutral Jordan padding supplies the same obstruction within that threshold; no existence of arbitrarily small positive entropy is assumed.
Deleting neutral primary components is a strictly stronger operation than the permitted stabilizations and may remove this obstruction.
No bounded excess for the positive irreducible unit core, uniform compression theorem or Lehmer gap is established.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:49 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every positive size and every integral unimodular matrix, each fixed excess bound k0>=1, exact sparse neutral completion, all nonzero-eigenvalue Jordan blocks and all integral conjugates after arbitrary signed-permutation stabilizations; no entropy-only complexity bound or compression of the positive irreducible core. |
| argument | [Argument](#argument) | Complete signed matching inequality, active/inactive cycle removal, rational inverse and determinant-lemma polynomial, exact factorial/exponential term count and controls, full derivative Vandermonde multiplicity proof, optimized-excess escape and constant-entropy Jordan counterfamilies. |
| dependency | [DS17 bounded support](../audits/literature/DS17/Yin_U001.md#ds17-u001) | For each fixed K, a positive total-log-Mahler gap for every nonzero integer polynomial of at most K terms; no effective eta_K or monotonic eta convention. |
| dependency | [Exact entropy normalization](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Full finite-dimensional rational characteristic-polynomial entropy, specializing to monic integral units with no leading penalty or rank normalization. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:50 |
| status | proved |
| reason | Actual complete current theorem and proof self-review confirms the exact retained arguments and accepted inputs, with every restricted domain, entropy normalization and negative-result boundary explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every positive size and every integral unimodular matrix, each fixed excess bound k0>=1, exact sparse neutral completion, all nonzero-eigenvalue Jordan blocks and all integral conjugates after arbitrary signed-permutation stabilizations; no entropy-only complexity bound or compression of the positive irreducible core. |
| argument | [Argument](#argument) | Complete signed matching inequality, active/inactive cycle removal, rational inverse and determinant-lemma polynomial, exact factorial/exponential term count and controls, full derivative Vandermonde multiplicity proof, optimized-excess escape and constant-entropy Jordan counterfamilies. |
| dependency | [DS17 bounded support](../audits/literature/DS17/Yin_U001.md#ds17-u001) | For each fixed K, a positive total-log-Mahler gap for every nonzero integer polynomial of at most K terms; no effective eta_K or monotonic eta convention. |
| dependency | [Exact entropy normalization](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Full finite-dimensional rational characteristic-polynomial entropy, specializing to monic integral units with no leading penalty or rank normalization. |
| review | [Complete actual self-review](../audits/reviews/Yin_R_G0514_v1.md#current-excess-jordan-finding) | Exact complete statement and full necessary proof, source applicability and controls; no isolated independent or general research conclusion is asserted. |

## Argument

### Complete sparse neutral construction

<a id="bounded-excess-gap"></a>
### Statement and inputs

Let A belong to GL_N(Z), with N unrestricted, and put k=||A||_F^2-N.
For every fixed integer k_0>=1, matrices with k<=k_0 have either zero algebraic entropy or entropy at least eta_{K(k_0)}>0, where

    K(k)=k! 3^k 2^{k(2k-1)}.

Here eta_K is the accepted [DS17 bounded-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001).
The other external input is the Task's integral characteristic-polynomial entropy formula h_alg(A)=m(det(tI-A)); m is logarithmic Mahler measure, without dimension normalization.
Normality and a positive metric are not assumed.
The proof constructs a monic integer polynomial F with at most K(k) terms and exactly the same Mahler measure as A.

### Signed permutation reduction

Since det A is nonzero, its determinant expansion contains a nonzero permutation term.
Choose its matching and let P have the signs of the matched entries there and zeros elsewhere.
P is a signed permutation matrix.
Set E=A-P and let s be the number of its nonzero entries.
Entrywise integrality gives

    s <= sum_{i,j}|E_ij| <= sum_{i,j} A_ij^2-N = k.

Indeed, on matching entries |a|-1<=a^2-1; off the matching |a|<=a^2.
Thus k>=0.
If k=0, E=0 and A=P has entropy zero.
In what follows E is nonzero, so 1<=s<=k.

The permutation cycles of P are signed cycles.
A cycle of length l with sign product sigma has characteristic polynomial t^l-sigma, of Mahler measure zero.
Call a cycle active if it contains a row or column index of a nonzero entry of E.
There are r<=2s active cycles.
Every inactive cycle remains a separate invariant block of A: no row or column of E touches it.
Removing these blocks gives A_0=P_0+E_0 with exactly the same Mahler measure as A.
Put

    D(t)=det(tI-P_0)=product_{active cycles}(t^l-sigma).

It has at most 2^r terms and m(D)=0.
Its degree may be arbitrarily large.

### Determinant construction and term count

Write each of the s nonzero entries of E_0 as c_h e_{i_h}e_{j_h}^T, and form U with columns c_h e_{i_h}, V with columns e_{j_h}.
Thus E_0=UV^T.
For R=(tI-P_0)^{-1}, each entry is zero between different cycles; within one cycle it is a signed monomial divided by t^l-sigma.
This follows from

    (tI-P_cycle)^{-1}
      =(t^{l-1}I+t^{l-2}P_cycle+...+P_cycle^{l-1})/(t^l-sigma),

since exactly one of these l powers has a nonzero entry at a fixed pair of positions.
Consequently every entry of D V^T R U is an integer multiple of a monomial times the product of the other r-1 cycle binomials.
It has at most 2^{r-1} terms, including when some cycle binomials coincide.

Define the s by s polynomial matrix B=D I_s-D V^T R U and F=det B.
The matrix determinant lemma over Q(t) gives the polynomial identity

    F=D^s det(I_s-V^T R U)=D^{s-1} det(tI-A_0).

In particular F is nonzero, monic and integral, and m(F)=m(det(tI-A_0))=h_alg(A).
Each entry of B has at most 3*2^{r-1} terms (the diagonal includes D).
Expanding its determinant therefore gives

    number of nonzero terms of F
      <= s! (3*2^{r-1})^s
      <= s! 3^s 2^{s(2s-1)} <= K(k).

Coincident exponents and cancellation only decrease this bound.
Applying DS17 proves the statement; for k<=k_0 use the monotonicity of K.
Neither the number of inactive cycles nor active cycle lengths enter the bound.

<a id="complexity-escape"></a>
### Consequence and remaining obstruction

This realizes the zero-overhead special case of [L G0019](Yin_C_G0221_v1.md#controlled-entropy-completion) using an integral matrix rather than assuming a sparse characteristic polynomial.
Any hypothetical sequence A_n of integral unimodular matrices with 0<h_alg(A_n)->0 must have ||A_n||_F^2-dim(A_n)->infinity.
Otherwise a fixed-k subsequence contradicts the proved gap.

Integer conjugacy can change k; adding signed permutation blocks leaves k unchanged.
One may minimize k over all integral conjugates of all such stabilizations.
This is a nonempty set of nonnegative integers, so a minimum exists.
The same gap applies if this optimized quantity is bounded, and a hypothetical vanishing-entropy sequence forces these minima to infinity as well.
No bound on these minima in terms of small entropy is proved.

For the standard companion matrix of a monic unit polynomial p=t^d+sum_{i<d}a_i t^i, k=sum_{i<d}a_i^2-1 (also for d=1).
Thus the criterion includes familiar bounded-coefficient restrictions.
The missing step is a uniform structural compression of general small-entropy dynamics; bounded excess must not be inferred from small entropy or from a rational realization.

### Exact controls and review scope

For A=[[1,1],[1,0]], choose P=[[0,1],[1,0]].
Then E=e_11, D=t^2-1, R_11=t/(t^2-1), and F=t^2-t-1, with unchanged positive entropy.
For A=[[1,1],[0,1]], choose P=I.
There are two active length-one cycles, D=(t-1)^2, but R_21=0, so F=D and the entropy is zero despite k=1.
These are direct symbolic checks, not a computer experiment.

### Complete multiplicity and neutral-padding obstruction

<a id="jordan-complexity-obstruction"></a>
### A multiplicity bound

Write K(k)=k!3^k2^{k(2k-1)} for k>=1.
Suppose an integral unimodular matrix A has a Jordan block of size n>=2 at a nonzero eigenvalue z.
Then its Frobenius excess k=||A||_F^2-dim(A) satisfies

    n <= K(k)-1.

To prove this, use the signed permutation decomposition of L G0025.
If k=0, A is a signed permutation and is diagonalizable over C, contradicting n>=2.
For k>=1, remove the inactive signed cycles to obtain the active block A_0.
Inactive cycles are diagonalizable: their polynomials t^l-sigma have simple roots in characteristic zero.
Hence the size-n Jordan block must occur in A_0.
The polynomial

    F=D^{s-1} det(tI-A_0)

constructed there is nonzero, has at most K(k) nonzero terms, and has a root of multiplicity at least n at z.

For completeness, a nonzero polynomial with q distinct nonzero terms has multiplicity at most q-1 at any z!=0.
Write f(t)=sum_{j=1}^q c_j t^{a_j}, with distinct nonnegative integers a_j.
If its multiplicity were at least q, then applying (t d/dt)^r for 0<=r<q and evaluating at z gives

    sum_j a_j^r c_j z^{a_j}=0.

These vanish because each such differential operator is a linear combination of derivatives of order at most r multiplied by powers of t.
The Vandermonde matrix (a_j^r) is invertible, forcing every c_j z^{a_j}=0, a contradiction.
This proves the bound, including complex z.

<a id="neutral-padding-failure"></a>
### Counterfamily to entropy-only whole-flow compression

Let J_n be the integral unipotent Jordan block of size n.
Its characteristic polynomial is (t-1)^n, so h_alg(J_n)=0.
Let k_min be the minimum excess over all integral conjugates after adjoining arbitrary signed permutation blocks, exactly as in L G0025.
Such operations retain its size-n Jordan block.
Thus, for every fixed k_0>=1, n>K(k_0)-1 implies k_min(J_n)>k_0.
Consequently k_min(J_n) tends to infinity despite identically zero entropy.

For any fixed integral unimodular B, the same reasoning applies to B direct-sum J_n, whose entropy is exactly h_alg(B).
In particular B=[[1,1],[1,0]] gives strictly positive constant entropy log((1+sqrt(5))/2) with unbounded optimized excess.
More generally, if a positive-entropy matrix lies below any proposed threshold, adjoining these neutral blocks preserves that same entropy while defeating any uniform excess bound for all flows in that threshold class.
This conditional observation assumes no arbitrarily small positive entropy exists.

Thus no finite-valued bound on this whole-flow complexity depending only on entropy can hold, even after the stated stabilization and integral basis optimization.
This does not contradict L G0025's sufficient condition or its vanishing-entropy escape consequence.
It shows that neutral algebraic multiplicity is an independent source of complexity.

<a id="positive-primary-restriction"></a>
### Revised target

An entropy-preserving deletion of a neutral primary component is stronger than adjoining signed permutation blocks and conjugating.
The bounded-excess approach must first allow such deletion, or restrict directly to the companion matrices of irreducible positive-Mahler unit polynomials.
For the counterfamily above, deleting the (t-1)-primary component removes the obstruction entirely.
General rational primary decomposition does not by itself produce an integral direct-sum basis; an argument may instead choose a new integral companion representative of the relevant polynomial.
No bounded excess for these positive irreducible representatives is established here.

The next meaningful question is therefore compression of the positive irreducible unit core, rather than of arbitrary finite-rank flows.
Its degree remains unbounded; the full Task and algebraic-entropy priority are unchanged.
