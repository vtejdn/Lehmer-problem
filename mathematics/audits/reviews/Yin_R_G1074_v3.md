---
author: Yin
---
# Independent review of actual Hankel valuations from nonrational reduction

Review act: 2026-11-05T00:17 UTC.
The human record author is Yin.
This is a separately organized whole-proof agent review of the fixed [C858 v2 statement](../../claims/Yin_C_G0858_v2.md#statement) and [complete argument](../../claims/Yin_C_G0858_v2.md#argument), covering Parts A--C, HV1--HV5 and the exact consequence and limitation paragraphs.
The reviewer did not participate in this proof's development and received no substantive development conversation, proposing-agent mathematical summary or previous verdict on this candidate.
The fixed candidate, current rules and necessary mathematical inputs were read directly.
No Draft, proof-generation note or development dialogue was consulted, and the reviewer supplied no substantive proof repair.
Initial mathematical findings were formed before consulting the earlier R1074 findings for their actual retained scope and declaration format.

The earlier [R1074 v1 Hankel finding](Yin_R_G1074_v1.md#hankel-all-place-whole) concerns C858 v1's supplied all-place divisibility theorem and disk comparison.
The [R1074 v2 finding](Yin_R_G1074_v2.md#all-place-mask-whole) concerns C857 v2's all-place masks and coherent centers.
Neither verdict transfers to the present candidate.
Their unchanged applicable source and mathematical interfaces are used only as identified below.

<a id="actual-hankel-residue-whole"></a>
## Complete residue-layer and original-input finding

**Finding:** no unresolved mathematical gap was found in the whole C858 v2 statement and complete argument under their stated hypotheses.
The exact equalities along infinite index sets concern the actual original shifted leading Hankel determinants, including both liminf conclusions.
The nonzero dyadic class requires no squarefree reduction hypothesis, and the good-odd-prime conclusion applies independently of that dyadic class.
The proof supplies no common equality subsequence for distinct primes or upper bound on their total valuation contribution.
This review records evidence only and selects no Claim assessment or Task completion.

### Part A: exact factor, reduction and determinant indexing

Because the matrix starts at coefficient index one, its constant coefficient never enters.
The identity A=a_0+p^k B with B(0)=0 therefore gives exactly Delta_h(A)=p^(kh) Delta_h(B) for every h>=1.
The latter determinant is integral over Z_p, including when it is zero, so the lower bound v_p(Delta_h(A))>=kh holds with the stated infinity convention.
No cancellation or approximation error enters this row-factor identity.

The coefficient of x^n in Bbar/x is bbar_(n+1).
Consequently its source determinant Delta_(0,h-1) is precisely the reduction of Delta_h(B), with h rows and columns and entries bbar_(i+j+1).
Division by x is legitimate because B(0)=0, and Bbar/x is nonrational exactly when Bbar is nonrational.
The accepted field-valued Kronecker criterion now makes these determinants nonzero for infinitely many h.
For each such h, Delta_h(B) is a unit and Delta_h(A) is nonzero of valuation exactly kh.

An infinite subset of the positive integers is unbounded.
Thus the nonzero-determinant index set is infinite, the linear quotient is always at least k and equals k along an unbounded subsequence, and the nonnegative quadratic quotient equals k/h along that same subsequence.
This proves both liminf assertions, including k=0, without an assertion at every large index.
The proof does not identify the equality index sets for different residue fields.

### Source applicability in positive characteristic

The exact accepted source interface is [C858 v1, Preparation and exact remaining inputs](../../claims/Yin_C_G0858_v1.md#preparation-and-exact-remaining-inputs).
The reviewer additionally read the actual retained [BNZ22 PDF](../../literature/pdf/BNZ22.pdf), identifying the title, authors and arXiv:2205.02145v3 dated 21 November 2022, then Section 2.2 on printed/PDF pages 4--6.
That subsection explicitly permits an arbitrary field k.
Its definition uses the (m+1)-square matrix with entries a_(ell+i+j), and Corollary 2.3 says that rationality is equivalent to eventual vanishing of the leading determinants.
The nearby Lemma 2.1 and Corollary 2.2 were read to check the finite polynomial-approximation interface; there is no characteristic-zero or D-finite hypothesis on this criterion.
The characteristic-zero hypothesis begins separately at Section 2.3 and is not imported into Part A.
The nonzero-series convention in Section 2.2 is satisfied because the series to which the criterion is applied is nonrational.

This is direct inspection of the selected source statement, field scope and application, with the accepted Kronecker input reused.
It is not a new independent proof audit of the complete paper or its external inputs, and no later differential theorem is used.
The finite shift is verified above rather than inferred from an infinite-operator statement.

### Part B: integrality and the actual nonzero Artin--Schreier class

The [C857 v2 reduction](../../claims/Yin_C_G0857_v2.md#reduced-representative) was read at A1, A5--A6 and the uniqueness argument, together with its original-input statement and dependency table.
The original congruence V-U in 4 Z[x] is its accepted [C860 v2 input](../../claims/Yin_C_G0860_v2.md#statement), with the exact Dimitrov arXiv:1912.12545v1 Lemma 2.1 scope retained there.
This review reuses that already accepted congruence and does not claim a new inspection of Dimitrov's original proof.
The numerator W=(V-U)/4 has zero constant coefficient, while U(0)=1.
Hence W/U belongs to x Z[[x]], and the normalized binomial expansion is coefficientwise finite in each x degree.

For j>=1, the stated scaled coefficient has valuation j-v_2(j!)=s_2(j)>=1 and no odd denominator.
It is therefore an even ordinary integer, not merely a dyadic integer.
The resulting normalized square root is G=1+2H with H in Z[[x]] and H(0)=0.
Squaring and cancelling the factor four gives exactly H+H^2=W/U, and reduction gives HV5 with the correct signs in characteristic two.

C857 v2 proves r=c+wp(h) over F_2(x), including descent and normalization, and a nonzero reduced c cannot lie in wp(F_2(x)).
Indeed any finite pole of a rational v produces an even highest pole order in v^2+v, whereas a nonzero reduced proper c has an odd highest order at a pole.
With no finite pole, v is polynomial and a proper Artin--Schreier image is zero.
Thus a rational Hbar satisfying HV5 would contradict c!=0.
Repeated poles of r are already handled by the retained reduction, so no squarefreeness assumption is introduced here.
Applying Part A to p=2, k=1, A=G and B=H proves HV2 and both actual valuation limits.
The distinct modulo-eight premise of C858 v1 is neither assumed nor needed.

For the comparison only, [C860 v8's Artin--Schreier subsection](../../claims/Yin_C_G0860_v8.md#argument) was read at CB13--CB16 and its stated input scope.
In its squarefree branch c=r, and its retained Lehmer identity V=U-4x^4-4x^6 gives a nonzero proper residue numerator modulo two.
This is the same nonzero branch used here.
That accepted control is not a sequence with measure tending to zero, and its historical native computations and underlying Salem data were not rerun or newly audited in this review.
No minimum-approximation-rank theorem is used to deduce an upper bound on actual valuations.

### Part C: original noncollision and good odd primes

The supplied degree stability ensures that the d squared conjugates are distinct and that the d fourth-powered conjugates are distinct.
It is used directly at the stated general original-input scope; no Salem-only uniqueness argument is extended to other polynomials.
All original conjugates have the same positive absolute Weil height, since they are conjugate nonzero algebraic integers and are not roots of unity.
Height multiplication under powers excludes alpha_i^2=alpha_j^4, since it would give 2h_abs(alpha)=4h_abs(alpha)>0.
Thus U and V are squarefree and coprime over Q, and their discriminants and cross-resultant are nonzero integers.
This directly checks the needed noncollision also retained in [C858 v1](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget); it does not require the componentwise rank theorem of C860 v7.

An irreducible reciprocal polynomial of odd degree would have -1 as a root, contradicting d>=2, so d is even here.
Together with the original constant term one, this verifies the asserted leading coefficient one for U and V.
Their degrees and constant terms therefore survive every prime reduction.
For p not dividing T=2 disc(U) disc(V) Res(U,V), the two reductions remain squarefree and coprime over the algebraic closure of F_p.
Their ratio consequently has simple zeros and simple poles, and it cannot be a rational square because a rational square has even valuation at each such point.
The hypotheses leave at least one such zero and pole, since both polynomials retain degree d>=2.

Integrality from Part B was established without using c!=0, so G^2=V/U reduces at each of these odd primes for either dyadic class.
A rational Gbar would make Vbar/Ubar a rational square, which was excluded.
Thus (G-1)bar is nonrational, and Part A applies with k=0 and B=G-1 to give HV3.
The finite exceptional set may depend on P.
Each prime has its own infinite equality set; no intersection assertion follows from separate applications of Kronecker's criterion.

### Consequences and retained limits

For fixed eta>0 the dyadic equality v_2(Delta_h(G))=h contradicts an all-late positive quadratic lower bound on the nonzero determinants as soon as an equality index satisfies h>1/eta.
At a good odd prime the equality valuation zero gives the corresponding contradiction directly.
These conclusions exclude precisely the asserted all-late quadratic lower bounds for the same original determinant sequence.
They leave selected subsequences avoiding those indices, exceptional primes, sums of valuations over varying primes, the zero dyadic class, other matrices and the original unrestricted positive total-Mahler-gap question unresolved.
No numerical determinant experiment, formal verification or source-wide proof audit supplies additional evidence here.
The review found no source-applicability or attribution gap affecting the exact invoked criterion and retained project inputs at the stated depth.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete finding](#actual-hankel-residue-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete finding](#actual-hankel-residue-whole) | [C858 v2 statement](../../claims/Yin_C_G0858_v2.md#statement) | Entire Parts A--C, all original and residue hypotheses, HV1--HV3, both liminf assertions and all index, prime and original-task limitations. |
| [Complete finding](#actual-hankel-residue-whole) | [C858 v2 argument](../../claims/Yin_C_G0858_v2.md#argument) | Entire proof, HV1--HV5, finite shift, characteristic-p applicability, integrality, nonzero Artin--Schreier obstruction, general original noncollision, good-prime reduction and final consequences. |
| [Complete finding](#actual-hankel-residue-whole) | [Canonical reduction input](../../claims/Yin_C_G0857_v2.md#reduced-representative) | Only A1/A5--A6, normalization and descent, and the nonzero reduced-class obstruction to a rational solution, including repeated poles. |
| [Complete finding](#actual-hankel-residue-whole) | [Original congruence input](../../claims/Yin_C_G0860_v2.md#statement) | Only original P_4-P_2 divisibility by four and polynomial conventions, retaining the existing Dimitrov statement and source-proof scope. |
| [Complete finding](#actual-hankel-residue-whole) | [Accepted Kronecker interface](../../claims/Yin_C_G0858_v1.md#preparation-and-exact-remaining-inputs) | Exact field-valued eventual leading-Hankel criterion, additionally checked in BNZ22 v3 Section 2.2 for positive characteristic and the present finite shifted indexing. |
| [Complete finding](#actual-hankel-residue-whole) | [Squarefree-branch comparison](../../claims/Yin_C_G0860_v8.md#argument) | Only CB13--CB16 and the retained actual Lehmer control as a comparison; no minimum-rank inference, original native rerun or near-one sequence assertion. |
