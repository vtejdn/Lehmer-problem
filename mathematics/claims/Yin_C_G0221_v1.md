---
author: Yin
---

# Sparse neutral completions, exact degree costs and controlled entropy overhead

This retains the complete original2026-10-06 [L18](../ledger/Yin_L_G0018_v1.md) and [L19](../ledger/Yin_L_G0019_v1.md) deductions, keeping classical source scope and every failed inference.

## Statement

Let p in Z[t] be monic irreducible noncyclotomic, p(0) nonzero, degree d, and m(p)>0.
For every monic product c of cyclotomic polynomials, including repeated factors and c=1, q=pc of degree D has m(q)=m(p), and the exact rational t-module sequence in the Argument proves equality of total entropies without semisimplicity or equality of finite trajectories.
For every prime ell, with S=norm(q)_1,

    m(p) >= (d/D) log(ell/S)/ell.

For each fixed positive finite S0 and C>=1, bounds S<=S0 and D/d<=C give a degree-independent positive bound by choosing ell>S0.
Neither bounded S nor height-one binary collisions supplies the needed degree/support/multiplier-entropy bound: q=(t^N−1)p for N>d has S=2 norm(p)_1, D/d tending to infinity and the same positive entropy.
For the unit core M(p)<2 the binary bound produces a nonzero coefficient set{−1,0,1} relation divisible by p, without a bound on its support, first collision time or quotient entropy.
For every fixed integer K>=2 and finite real A>=0, if a nonzero integer c gives at mostK nonzero coefficients of pc and m(c)<=A m(p), then

    m(p)>=eta_K/(1+A)>0,

using only the exact accepted DS17 fixed-support gap.
If m(p_n)>0 tends to zero and each p_n has a K-term multiple p_n c_n, then m(c_n)>=eta_K−m(p_n), eventually at least eta_K/2, and m(c_n)/m(p_n) tends to infinity.
The minimum cyclotomic-completion support s_cyc(p_n) therefore tends to infinity on any such vanishing sequence.
Finite-entropy rational flows attain entropy on a finite set if all positive monic primary types satisfy one common stated positive length/degree certificate, or one common K,A controlled-overhead certificate; primitive nonmonic types are handled by their log2 leading-coefficient bound.
Zero-weight primary components may remain infinite-dimensional.
These are restricted presentation criteria and complexity obstructions; they supply neither a general completion theorem, an unrestricted gap nor a bound uniform over unbounded support.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:13 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every monic irreducible noncyclotomic p with p(0) nonzero, each exact cyclotomic completion and prime, positive fixed length/degree bounds, and each fixed integer K>=2/real A>=0 sparse multiplier; all stated escape/rational and binary-relation quantifiers. |
| argument | [Argument](#argument) | Full neutral exact-sequence/entropy identity, actual norm d/D cost and disjoint-block counterfamily, binary-pigeonhole direction, complete DS17 multiplier inequality, absolute/relative-overhead and minimum-support escape with primary-weight accounting. |
| dependency | [Rational primary entropy](Yin_C_G0205_v1.md#capture-equivalence) | Exact rational finite-dimensional/primary entropy and capture formula, repeated factors included; primitive nonmonic positive weights cost at least log2. |
| dependency | [Frobenius nonvanishing](Yin_C_G0217_v2.md#bounded-length-gap) | Finite-order Galois argument and integer norm divisibility only, retaining the actual d/D degree cost for a multiple. |
| dependency | [General unit support packing](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Proof-route item 6 counting upper bound for any fixed algebraic unit: retain every expanding conjugate and unit-circle polynomial factor, with parameter-dependent constants; used only to obtain a height-one relation. |
| dependency | [Accepted bounded-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) | For each fixed K>=2, nonzero integer polynomial support at mostK has m=0 or m>=eta_K>0; no explicit eta, degree/height bound or original-foundation proof audit. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:14 |
| status | proved |
| reason | Adopt the exact complete retained theorem after actual whole current self-review, retaining every source, parameter, finite-time and unrestricted-goal boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every monic irreducible noncyclotomic p with p(0) nonzero, each exact cyclotomic completion and prime, positive fixed length/degree bounds, and each fixed integer K>=2/real A>=0 sparse multiplier; all stated escape/rational and binary-relation quantifiers. |
| argument | [Argument](#argument) | Full neutral exact-sequence/entropy identity, actual norm d/D cost and disjoint-block counterfamily, binary-pigeonhole direction, complete DS17 multiplier inequality, absolute/relative-overhead and minimum-support escape with primary-weight accounting. |
| dependency | [Rational primary entropy](Yin_C_G0205_v1.md#capture-equivalence) | Exact rational finite-dimensional/primary entropy and capture formula, repeated factors included; primitive nonmonic positive weights cost at least log2. |
| dependency | [Frobenius nonvanishing](Yin_C_G0217_v2.md#bounded-length-gap) | Finite-order Galois argument and integer norm divisibility only, retaining the actual d/D degree cost for a multiple. |
| dependency | [General unit support packing](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Proof-route item 6 counting upper bound for any fixed algebraic unit: retain every expanding conjugate and unit-circle polynomial factor, with parameter-dependent constants; used only to obtain a height-one relation. |
| dependency | [Accepted bounded-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) | For each fixed K>=2, nonzero integer polynomial support at mostK has m=0 or m>=eta_K>0; no explicit eta, degree/height bound or original-foundation proof audit. |
| review | [Complete current finding](../audits/reviews/Yin_R_G0510_v1.md#current-sparse-completion-finding) | Entire exact Statement and Argument after actual current contributor self-review, with resolved accepted inputs and no isolated-review or original-proof-audit claim. |

## Complete retained argument

<a id="argument"></a>

<a id="neutral-completion"></a>
## 1. What a cyclotomic multiple preserves

Let p in Z[t] be monic irreducible, noncyclotomic, with p(0) nonzero and degree d.
Let c be a monic product of cyclotomic polynomials, allowing repeated factors and c=1, and put q=pc, D=deg q.
On Q[t]/(q), multiplication by t has an exact sequence

    0 -> Q[t]/(c) -- multiplication by p --> Q[t]/(pc)
      -- reduction modulo p --> Q[t]/(p) -> 0.

The first map is well-defined and injective by cancellation in Q[t]; its image is exactly the kernel of reduction.
Both maps commute with t.
The characteristic polynomial of each quotient operator is its defining monic polynomial.
The rational entropy formula therefore gives

    h(q)=m(q)=m(p)+m(c)=m(p)=h(p),  h(c)=0.

Here m is logarithmic Mahler measure.
This remains true with repeated cyclotomic factors, without assuming the neutral operator is diagonalizable.
It is an equality of total entropies of two finite-rank flows, not an identification of every finite-set trajectory.
Arbitrary reciprocal multiplication does not preserve entropy: for reciprocal p, taking c=p gives h(p^2)=2m(p)>m(p).

<a id="short-annihilator-degree-cost"></a>
## 2. An elementary norm certificate and its exact loss

Write S=||q||_1 and let ell be any prime.
If alpha is a root of p, q(alpha)=0 and Frobenius gives q(alpha^ell) in ell Z[alpha].
This algebraic integer is nonzero: alpha^ell cannot be a root of c because alpha is not a root of unity; it cannot be a root of p by the finite-order Galois argument already proved in C217.
Thus its norm over Q(alpha) is a nonzero integer divisible by ell^d.
For each conjugate alpha_i,

    |q(alpha_i^ell)| <= S max(1,|alpha_i|)^(ell D).

Taking products gives

    ell^d <= S^d M(p)^(ell D),
    m(p) >= (d/D) log(ell/S)/ell.                         (1)

For S<=S0 and D/d<=C, any fixed prime ell>S0 yields the uniform positive bound log(ell/S0)/(ell C).
This transfers the previously checked minimal-polynomial certificate to an entropy-preserving presentation with an explicit degree cost.
In the rational primary formula of [C205](Yin_C_G0205_v1.md#capture-equivalence), imposing these two fixed bounds on every positive irreducible type therefore ensures finite capture: infinitely many positive types would have infinite total entropy.
This is a restricted consequence only.

Bounded coefficient length does not bound D/d for an arbitrarily chosen completion.
For any fixed p and N>d, take c=t^N-1.
It is a product of cyclotomic polynomials, the two coefficient blocks in q=t^N p-p are disjoint, and

    ||q||_1=2||p||_1,   D/d=1+N/d -> infinity,
    m(q)=m(p)>0.

Thus (1) degenerates on presentations of exactly the same positive-entropy flow value.
This refutes an automatic presentation-degree bound, not the possibility of choosing a better multiplier or proving a stronger sparse-polynomial theorem.
In particular, the existing Mignotte minimal-polynomial result must not be applied to reducible q without checking its hypotheses.
The stronger known sparsity bounds reported in Smy08 have different proofs and are not refuted by this loss.

<a id="binary-relations-boundary"></a>
## 3. What binary trajectory counting actually supplies

For the unit core with M(p)<2, let X_n={sum_(j=0)^(n-1) epsilon_j alpha^j : epsilon_j in {0,1}}.
The accepted [BV20 general unit counting bound, proof-route item 6](../audits/literature/BV20/Yin_U001.md#bv20-random-walk-entropy) gives |X_n|<=C_alpha n^s M(p)^n, retaining every expanding conjugate, with s counting unit-circle conjugates and constants depending on alpha.
Eventually this is less than 2^n.
Two distinct binary words then have equal value, yielding a nonzero r in Z[t] with coefficients in {-1,0,1}, deg r<n, and p dividing r.

This guarantees a height-one annihilator, but gives neither a uniform bound on its number of terms or coefficient length, nor that r/p is cyclotomic.
Since r/p is an integer polynomial, multiplicativity only gives m(r)=m(p)+m(r/p)>=m(p).
A lower bound on m(r) alone does not give a lower bound on m(p).
Reciprocal symmetrization does not repair this: r(t) t^(deg r)r(t^-1) is reciprocal and has measure M(r)^2; the unwanted factor's measure is doubled as well.

Consequently the finite-digit route needs a controlled annihilator construction (including its multiplier's entropy), or a direct estimate on p.
Pigeonhole collisions by themselves do not supply such a construction.
No upper bound on first collision length uniform in p is asserted.

### The bounded-support multiplier theorem

<a id="controlled-entropy-completion"></a>
## A sufficient presentation criterion

Fix K>=2 and A>=0.
Let p be monic irreducible integral, p(0) nonzero, and m(p)>0.
Suppose there is a nonzero c in Z[t] such that q=pc has at most K nonzero coefficients and

    m(c) <= A m(p).

Let eta_K>0 be the accepted external gap in [DS17-U001](../audits/literature/DS17/Yin_U001.md#ds17-u001).
Integer polynomials have nonnegative logarithmic Mahler measure.
Thus

    0 < m(p) <= m(q) = m(p)+m(c) <= (1+A)m(p),
    eta_K <= m(q),
    m(p) >= eta_K/(1+A).                              (1)

No bound on deg(q)/deg(p) is needed.
In particular, cyclotomic completion permits A=0, including repeated cyclotomic factors.
This removes the degree loss of the elementary certificate in the preceding elementary certificate, within the bounded-support hypothesis.
It does not establish that hypothesis for arbitrary small-entropy p.

More generally, for fixed K, if a proposed positive sequence m(p_n)->0 has K-term multiples q_n=p_n c_n, then

    m(c_n) >= eta_K-m(p_n).

Hence for all sufficiently large n, m(c_n)>=eta_K/2 and m(c_n)/m(p_n)->infinity.
Fixed-support completions cannot have even vanishing absolute extra entropy along such a sequence.
This is stronger than merely excluding a fixed relative overhead A.

<a id="cyclotomic-support-escape"></a>
## Necessary complexity escape and finite capture

Define s_cyc(p) as the minimum number of nonzero coefficients of p*c, over monic products c of cyclotomic polynomials, including c=1.
The minimum exists: the possible counts form a nonempty set of positive integers.
This is a support-count invariant; it is not the coefficient-length shortness used by El-Serafy--McKee.

If m(p_n)>0 tends to zero, then s_cyc(p_n)->infinity.
Indeed, for each fixed K, an infinite subsequence with s_cyc<=K would satisfy m(p_n)>=eta_K by (1), a contradiction.
Accordingly, no counterexample search restricted to uniformly bounded cyclotomic support can settle the negative direction, even with unbounded degree and neutral dimension.

For rational flows in [C205](Yin_C_G0205_v1.md#capture-equivalence), suppose each positive irreducible primary type admits a completion with the same K,A.
Formula (1) bounds every positive weight below.
The primary entropy sum then shows that finite total entropy permits only finitely many positive types, hence finite capture at that record's exact scope.
Zero-entropy primary parts may still be infinite.
No unrestricted representation theorem has been proved.

For the current rational-flow statement, apply these complete monic-factor estimates to every positive monic primitive primary polynomial and use C205’s log2 bound for every primitive nonmonic factor.
The minimum of those positive constants bounds the sum of positive composition lengths by finite entropy divided by that minimum; the exact C205 realization then gives finite capture.
This explicitly retains the primitive-leading-coefficient branch without assuming all rational primary types are monic.
