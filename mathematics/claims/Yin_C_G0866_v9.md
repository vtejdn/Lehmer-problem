---
author: Yin
---

# Basal degree and raw-norm minima can differ at Salem Mahler values

Human author Yin.
The coordinating agent proposed the half-norm counterexample and the exact low-degree separation.
The arithmetic contributor checked the actual exponent orbit, source power, raw normalization and degree comparison, and a separate contributor checked the counterexample chain.
These are contributor checks, not independent whole review of this version.
The complete fixed statement and proof are adopted at the [selected whole assessment](#decision-whole-independent-review-2026-11-05), supported by the [independent R1088 v9 finding](../audits/reviews/Yin_R_G1088_v9.md#basal-raw-separation-whole).
The adopted [v8 inverse-signature result](Yin_C_G0866_v8.md#decision-whole-independent-review-2026-11-05), [v7 general block descent](Yin_C_G0866_v7.md#decision-whole-independent-review-2026-11-05), and all earlier v1--v6 results retain their exact proved statements and source/review scopes.
The unproved unrestricted BD12 assertion discussed in v7 is the assertion refuted here; v7's proved block descent and finite attainment are not contradicted.
No earlier review covers this new counterexample or its basal/raw comparison automatically.
The extraction source is [D1's half-norm inquiry](../drafts/Yin_D_G0001.md#p2-basal-raw-descent-counterexample), which is provenance rather than a proof premise.

## Exact inputs and scope

Use the adopted [C866 v8 statement](Yin_C_G0866_v8.md#statement), specifically its actual endpoint degree b<=deg(z), signature size 1<=r<=t, exact support-Cauchy inequality M_2(z)>=log(alpha)sqrt(2d/r), and orbit bounds

    b>=2^r t/r for r<t,
    b>=2^(t-1) for r=t.                                (IN1)

These statements apply to every realization of a genuine Salem Mahler value of degree d=2t, without a small-measure or primitive-source restriction.
The same fixed statement at C=2 gives the raw-minimizer degree bound used for comparison.
No asymptotic fixed-B estimate, numerical Dobrowolski input or degree-normalized height is used.
The v8 proof does not assume a reciprocal minimal polynomial for the realization or a monomial identity for its generic block endpoint.

The [C866 v1 monomial-orbit proof](Yin_C_G0866_v1.md#salem-monomial-orbits), at its [selected assessment](Yin_C_G0866_v1.md#decision-whole-independent-review-2026-11-04), supplies independence of original conjugates from distinct inverse pairs modulo torsion and the actual signed-permutation exponent action.
Only that integer-monomial scope is used; its separate radical theorem's primitive-source condition is not imposed on the present tau.
The actual even-flip subgroup and its retained [C383 interface](Yin_C_G0383_v1.md#salem-kernel-class-population) remain at their established source/SELF scopes.
The two possible actual half-norm degrees are proved directly below from that action, without identifying a generic top Galois group or choosing one parity outcome in advance.

The accepted [Smy15-U001 positive-power statement](../audits/literature/Smy15/Yin_U001.md#smy15-u001) ensures that tau^(D/2) remains a genuine Salem number of the same degree and field.
Its retained statement/displayed-proof inspection applies; no original Salem proof or generator/regulator bound is newly adopted.
The adopted [v7 unit argument](Yin_C_G0866_v7.md#argument) ensures every algebraic realization of the resulting algebraic-unit measure is itself a unit, which makes the elementary raw lower bound fully all-place.

For a concrete actual input, use only the degree-ten irreducible genuine-Salem identification at [C226](Yin_C_G0226_v1.md#lehmer-joint-prime-control), at its [retained assessment](Yin_C_G0226_v1.md#decision-complete-retained-proof-adoption), and the exact 23/20<tau<6/5 proof at [C227](Yin_C_G0227_v1.md#exact-coarse-bounds-for-the-lehmer-root), at its [retained assessment](Yin_C_G0227_v1.md#decision-complete-retained-proof-adoption).
Their earlier source and checking scopes remain unchanged.
No matrix bound, catalogue approximation or old native computation is used or rerun.

The meaning of globally basal here is minimum irreducible realization degree among all same-measure algebraic realizations, as retained in [v7's basal boundary](Yin_C_G0866_v7.md#basal-boundary).
It is not merely a minimum among compatible block partitions of one starting realization.
No new original source classification or mathematical novelty is claimed.

## All-place normalization

For a nonzero algebraic number z of actual degree n_z and own field K_z, use the usual rational absolute values extended to its places v and local degrees n_v.
At finite v above p, use integer ord_v and n_v=e_v f_v with log|z|_v=-(ord_v(z)/e_v)log p; at complex places n_v=2 and the usual modulus is used.
Set

    h_abs(z)=(1/n_z)sum_v n_v log^+|z|_v,
    m(z)=n_z h_abs(z), M(z)=exp(m(z)),
    M_2(z)^2=n_z sum_v n_v(log|z|_v)^2.                (N1)

All logarithms are natural.
For a unit the finite terms vanish; counting its n_z actual complex embeddings, the product formula and Cauchy--Schwarz give

    2m(z)=sum_j |log|z_j||,
    M_2(z)^2=n_z sum_j log^2|z_j|,
    M_2(z)>=2m(z).                                     (N2)

These are actual own-degree raw quantities and total Mahler measure, not normalized heights.
Every use of N2 is for an actual unit, either constructed as a product of units or supplied by v7's unit-measure argument.

## Statement

### A. Low-degree realizations of every Salem value of degree at least ten

Let alpha be ANY genuine Salem number of degree d=2t>=10.
For every nonzero algebraic z satisfying M(z)=alpha and deg(z)<=d, one has

    deg(z)=d,
    M_2(z)>=sqrt(d)log(alpha).                           (S1)

Consequently the globally basal realization degree for alpha is exactly d, since alpha itself is a degree-d realization of its measure.
This conclusion has no half-norm, primitive-source, upper-measure or numerical-height hypothesis.
It does not assert that the raw minimum at every such alpha equals 2log(alpha).

### B. Actual half norms separate the two minimization problems

Let tau>1 be any genuine Salem number of degree d=2t>=10.
Select one oriented root u_i from each of its inverse pairs, with u_1=tau, and set

    eta=product_(i=1)^t u_i,
    D=deg(eta),
    alpha=M(eta).                                      (S2)

Then eta is an actual algebraic integer unit and

    D in {2^(t-1),2^t},
    alpha=tau^(D/2), deg(alpha)=d,
    M_2(eta)=D log(tau)=2log(alpha).                     (S3)

The two possibilities are retained at the actual D; neither a particular Galois group nor primitiveness of tau is assumed.
The value alpha is again a genuine Salem number, and

    inf_(z:M(z)=alpha) M_2(z)=2log(alpha),                (S4)

with the infimum attained by eta.
For this constructed alpha, every globally basal realization has degree d and raw norm at least sqrt(d)log(alpha), so its ratio to the global raw minimum is at least sqrt(d)/2>1.
Every raw-minimizing realization has degree at least 2^(t-1)>d.
Thus no same-measure realization of degree at most d can have raw norm at most M_2(eta), even without any field-containment requirement.

### C. Concrete high-measure counterexample and exact refutation scope

Take tau to be the expanding root of the actual retained Lehmer polynomial

    p_L(T)=T^10+T^9-T^7-T^6-T^5-T^4-T^3+T+1.

It is a genuine degree-ten Salem number with 23/20<tau<6/5.
Part B yields an actual eta with D in {16,32} and the actual degree-ten Salem value alpha=tau^(D/2), respectively tau^8 or tau^16.
In either actual degree case,

    alpha>3,
    log(alpha)>log 3>1.                                (S5)

This pair alpha,eta refutes the unrestricted [BD12 assertion](Yin_C_G0866_v7.md#basal-boundary) that every realization of a degree-d Salem measure can be replaced at no greater raw M_2 by one of degree at most d.
The explicit example is outside the region log(alpha)<=1.
No near-zero family, failure of a sufficiently-small-measure variant, or resolution or refutation of the unrestricted G0001 total-Mahler conjecture is asserted.

## Argument

<a id="p2-basal-raw-descent-counterexample"></a>
### A half-norm counterexample to unrestricted raw-monotone basal descent

The target is precisely the unrestricted [C866 v7 BD12 assertion](Yin_C_G0866_v7.md#basal-boundary): every realization of a Salem Mahler value of degree d can be replaced, at no greater raw M_2, by a same-measure realization of degree at most d.
No small-measure restriction occurs in that assertion.

#### A general actual half-norm minimizer

Let tau>1 be any genuine Salem number of degree d=2t>=10.
Choose one oriented root u_i from each of its t inverse pairs, with u_1=tau, and put

    eta=product_(i=1)^t u_i,
    D=[Q(eta):Q].                                       (HR1)

Every u_i is an integer unit, so eta is an actual integer unit.
Use the exact multiplicative independence and actual exponent-orbit mechanism in [C866 v1](Yin_C_G0866_v1.md#salem-monomial-orbits), without its primitive-source hypothesis for the separate radical theorem.
Distinct sign vectors on the t selected coordinates give distinct products.
The exponent vector of eta is the all-one vector, and every actual Galois image has an exponent vector in {1,-1}^t.
The actual even-flip subgroup supplies every even-parity sign vector.
If any odd-parity vector occurs in the orbit, its even-flip orbit supplies every odd-parity vector as well.
Thus the actual own degree has exactly the two possibilities

    D in {2^(t-1),2^t}.                                (HR2)

This does not choose which possibility occurs for a particular source, assume a full top permutation group, or require tau to be primitive.

Every image of the selected roots still takes one root from every inverse pair.
Exactly one factor has modulus tau or tau^(-1), and all remaining factors have modulus one.
Therefore every actual conjugate of eta has modulus tau or tau^(-1).
The unit product formula makes the two counts equal, hence each is D/2.
Define the actual measure value

    alpha=M(eta)=tau^(D/2).                             (HR3)

By the accepted [Smy15-U001 positive-power interface](../audits/literature/Smy15/Yin_U001.md#smy15-u001), alpha is a genuine Salem number of the same degree d and field as tau.
The exponent D/2 is a positive integer; its full original power cost is retained.
At the actual own degree D, with all finite places zero,

    M_2(eta)^2=D[D(log tau)^2],
    M_2(eta)=D log tau=2log alpha.                      (HR4)

This is the global raw minimum for the measure alpha.
Indeed the adopted [C866 v7 unit argument](Yin_C_G0866_v7.md#argument) proves every nonzero z with M(z)=alpha is a unit, and Cauchy--Schwarz at its actual degree gives M_2(z)>=2log alpha.
Thus eta attains the infimum, without assuming its degree is globally basal.

#### All low-degree realizations have strictly larger raw norm

In this subsection let alpha be ANY genuine Salem number of degree d=2t>=10, independently of the half-norm construction HR3.
Let z be any realization with M(z)=alpha and n_z=deg(z)<=d.
Apply the adopted [C866 v8 exact signature bounds](Yin_C_G0866_v8.md#statement) to its endpoint delta, of actual degree b<=n_z, with signature size r.
If r=t, its actual orbit bound gives b>=2^(t-1)>2t=d for t>=5, a contradiction.
For completeness, the strict inequality holds at t=5, where 16>10, and is preserved on increasing t because the left side doubles while 2(t+1)<2(2t).

Thus r<t, and the other v8 orbit bound gives

    2^r t/r<=b<=2t,
    2^(r-1)<=r.

For integer r>=3 one has 2^(r-1)>r, starting with 4>3 and preserved by doubling.
Hence r is 1 or 2.
For either possibility 2^r t/r=d, so

    b=n_z=d,
    M_2(z)>=M_2(delta)>=log(alpha)sqrt(2d/r)
                           >=sqrt(d)log(alpha).         (HR5)

This proves Part A for every genuine Salem alpha of degree at least ten, without an imposed field constraint and without using HR3 or HR4.
The Salem number alpha itself is a degree-d realization of its measure.
HR5 excludes every realization of smaller degree, so the globally basal degree for every such alpha is exactly d.

Return now to the particular measure alpha constructed in HR3.
Since sqrt(d)>2, HR5 is strictly larger than its attained raw minimum HR4.
No realization of degree at most d can therefore have M_2(z)<=M_2(eta).
Equivalently, the direct v8 bound with C=2 forces every raw minimizer of this particular measure to have degree at least 2^(t-1)>d.
Every globally basal realization has raw norm at least sqrt(d)log(alpha), while its global raw minimum is 2log(alpha).
Their ratio is at least sqrt(d)/2>1.
Thus least realization degree and least raw M_2 do not select the same realization for this constructed measure; no assertion that every Salem value attains 2log(alpha) is made.

#### A retained degree-ten source makes the counterexample concrete

Take tau to be the positive expanding root of the retained Lehmer polynomial

    p_L(T)=T^10+T^9-T^7-T^6-T^5-T^4-T^3+T+1.

Its actual irreducible genuine-Salem identification is the accepted input at [C226](Yin_C_G0226_v1.md#lehmer-joint-prime-control).
The exact retained trace-polynomial proof of its coarse size bounds is [C227](Yin_C_G0227_v1.md#exact-coarse-bounds-for-the-lehmer-root), giving 23/20<tau<6/5.
Only those input and root-bound scopes are used; no matrix certificate or native computation is used or rerun.

Here t=5 and HR2 permits D=16 or D=32.
The actual degree D determines the actual value alpha in HR3, which is respectively tau^8 or tau^16; the proof does not assume either degree in advance.
In both cases,

    alpha>=tau^8>(23/20)^8>3,
    23^8-3*20^8=1510985281>0.                           (HR6)

Thus m(alpha)>log 3>1.
The construction is an actual high-power counterexample to the unrestricted BD12 quantifiers, not a near-zero family and not a counterexample to a hypothetical variant restricted to sufficiently small total measure.
No primitive-source assumption or uncomputed Galois-group identification is needed.

#### Exact conclusion and remaining original goal

For this actual degree-ten Salem value alpha and the actual unit eta, every same-measure realization of degree at most ten has raw norm strictly greater than M_2(eta).
The unrestricted raw-monotone degree-at-most-d descent assertion BD12 is therefore false.
The general degree-binomial/raw-monotone descent and finite raw attainment of C866 v7, and the exact signature bounds of v8, remain consistent with the counterexample.
No assertion is made about existence of a uniformly cheap inverse for original near-one inputs, and no small-measure basal-descent variant is resolved here.
The unrestricted G0001 total-Mahler objective remains unresolved.

## Scope and review boundary

This fixed result contains N1--N2, Statement A--C/S1--S5 and the complete HR1--HR6 argument.
Part A applies to every genuine Salem value of degree at least ten; only the claim that the raw minimum is exactly 2log(alpha) uses the half-norm construction of Part B.
The actual half-norm degree is retained in both permitted cases and its positive-power cost is fully paid.
The concrete degree-ten source has total logarithmic measure above one, so the refutation concerns the original unrestricted BD12 quantifiers and leaves small-measure variants unresolved.
The earlier block-descent and signature theorems remain valid and are inputs to the counterexample, not statements refuted by it.
No numerical experiment, native computation or new original-source proof audit is claimed; the independent whole finding is selected below at its actual source and dependency scope.
The unrestricted [G0001 total-Mahler objective](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

## Assessment history

### Decision whole-independent-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T03:29 |
| status | proved |
| reason | Adopt complete N1--N2, A--C/S1--S5 and HR1--HR6 after independent whole R1088 v9. Every genuine Salem value of degree at least ten has basal realization degree equal to its own degree, and each such low-degree realization pays at least sqrt(d) times the log measure. Actual half norms attain the global raw minimum 2log(alpha) at constructed higher-power Salem values, strictly separating the two minimizations and refuting the unrestricted BD12 replacement assertion. The concrete degree-ten source gives log(alpha)>1; no sufficiently-small-measure variant or unrestricted G0001 conclusion is established. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire A--C/S1--S5 with N1--N2: general low-degree and basal result, actual half-norm orbit cases, exact global raw minimum and separation, and the concrete high-measure counterexample with its precise refutation scope. |
| argument | [Complete argument](#argument) | All HR1--HR6, independent general quantifiers in Part A, both actual parity/degree cases, full original power and all-place costs, strict comparison of every low-degree competitor and exact input bounds. |
| dependency | [Adopted signature bounds](Yin_C_G0866_v8.md#decision-whole-independent-review-2026-11-05) | Only actual endpoint degree, support-Cauchy and both r<t/r=t orbit bounds, including the C=2 specialization; no numerical-height or fixed-B estimate. |
| dependency | [Unit-measure and basal interfaces](Yin_C_G0866_v7.md#argument) | Every realization of a unit measure is a unit; the exact unrestricted BD12 and global basal definition remain at v7's basal-boundary section, without importing BD12 as a theorem. |
| dependency | [Integer-monomial orbit proof](Yin_C_G0866_v1.md#salem-monomial-orbits) | Independence modulo torsion and actual signed exponent orbit only, without the separate radical theorem's primitive-source condition. |
| dependency | [Actual even flips](Yin_C_G0383_v1.md#salem-kernel-class-population) | Actual conjugate complex-conjugation patterns and their even-flip span at retained SELF/source scope; no top-group or extension-splitting hypothesis. |
| dependency | [Actual Lehmer input](Yin_C_G0226_v1.md#lehmer-joint-prime-control) | Only the retained displayed degree-ten irreducible genuine-Salem polynomial identification; no historical native or matrix result is used or rerun. |
| dependency | [Exact root bounds](Yin_C_G0227_v1.md#exact-coarse-bounds-for-the-lehmer-root) | Exact trace and derivative proof of 23/20<tau<6/5 only, retaining prior input and inspection scope. |
| support | [Positive-power source](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Positive integral powers preserve genuine Salem degree and field at retained statement/displayed-proof inspection; no new original-source audit. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1088_v9.md#basal-raw-separation-whole) | Complete N1--N2, A--C/S1--S5 and HR1--HR6, all actual dependencies, source limits, low-degree and global-minimum separation, and unresolved small-measure/G0001 boundaries. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-05)
