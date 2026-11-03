---
author: Yin
---

# Complete four-coset next-half screen with thirty-two exclusions and thirty-two unresolved cases

Human author Yin.
Root proposed the bounded complete sixteen-by-four screen and its actual representative/cost scope.
Characteristic_zero_bridge implemented the producer, checked the exact inputs, source and original-array interfaces, and assembled this fixed result.
The different AUTHOR verifier was implemented by eighth_kernel_verifier, with its logic prepared before reading the new producer outcome.
Both programs completed without repair; these author implementations and checks are not a cold independent review.
The unchanged result is adopted through [whole independent mathematical/native R1051](../audits/reviews/Yin_R_G1051_v1.md#whole-finding), as selected by the [current decision](#decision-whole-reviewed-2026-10-28).
The symbolic transport and four-coset argument are reused from adopted C830 at their exact scope, without a mutable Draft proof premise.

## Statement

### A. Same original integer family and exact finite input

Use the actual family and canonical system of [adopted C828](Yin_C_G0828_v1.md#statement) and [adopted C830](Yin_C_G0830_v1.md#statement).
In particular, C_j(z+z^(-1))=z^j+z^(-j), the complete primitive traces satisfy z^(varphi(n)/2)F_n(z+z^(-1))=Phi_n(z), and for odd n>1 put B_n=1+sum_(j=1..(n-1)/2)C_j.
Fix

    P=F_15=X^4-X^3-4X^2+4X+1, f=Pbar=X^4+X^3+1,
    V=F_960, J=P^4 V, deg J=144,
    H_0=(X-2)^2F_3^2F_5^3F_9^4B_187,
    T_0=JH_0^2, deg T_0=374.

The monoid M contains all actual finite products Q of X-2 and B_n(C_(3^a5^b)), with n>1 odd prime to15 and a,b>=0, with all nonnegative multiplicities and complete-factor overlaps retained.
For T_Q=T_0Q use the SAME-divisor canonical integer variables

    a_Q=rem_(T_Q)(T_Q(C_2))/2,
    b_Q=rem_(T_Q)(T_Q(C_3))/3,
    c_Q=rem_(T_Q)(T_Q(C_5))/5,
    F_Q=rem_(T_Q)(2c_Q^2-3a_Q^5),
    G_Q=rem_(T_Q)(c_Q^3-2b_Q^5),
    X_(epsilon,Q)=rem_(T_Q)(b_Q^2-a_Q^3+epsilon G_Q),
    epsilon in{1,-1}.

Every prime division is over the integers before modular reduction.
Keep the single F_960, the actual endpoint X-2 and every actual q=3^a5^b; no residue representative is substituted into the degree of an existing factor.
The original trace degree is374+deg Q and full reciprocal degree twice that value.

Use C826's [extended-source kernel](Yin_C_G0826_v1.md#extended-source-joint-kernel) and [projected target](Yin_C_G0826_v1.md#general-reference-lowest-joint-target), as selected by C828/C830:

    Xi_16(Q)=(Qbar mod f^16,Qbar(Y) mod(Y+1)^24,Qbar(Y) mod p(Y)^12),
    Xi_plus(Q)=(Qbar mod f^16,Qbar(Y) mod(Y+1)^28,Qbar(Y) mod p(Y)^14),
    Theta(Q)=(Xi_plus(Q),Omega(Q)), p(Y)=Y^2+Y+1,
    W_plus=alpha_plus(ker(Theta(M)->Xi_16(M))).

Its intrinsic coordinates are(A,r_old,s_old), of binary lengths112,4,4.
The subscripts distinguish these earlier source12/24 increments from the NEXT source increments in Part C.
Adopted C828 supplies the complete59-dimensional W_plus, its ordered59-row basis and actual positive basis words, the common57-rank map Phi_R, and all16 attained targets.

Take EXACTLY C825's [retained references](Yin_C_G0825_v1.md#retained-old-fiber-reference-system) R_i and C828's returned K_i, for

    i=203,235,331,363,715,747,843,875,
      1171,1203,1299,1331,1683,1715,1811,1843.

No reference, word optimization or other parameter profile is selected.

<a id="retained-four-coset-representatives"></a>
### B. Two actual nullspace words and all sixty-four representatives

In the zero-based retained59-row basis order, ordered high-pivot image elimination with coefficient tracking gives the two nullspace coefficient vectors

    c_1=2^54+2^57=162129586585337856,
    c_2=2^56+2^58=360287970189639680.

Their intrinsic W_plus vectors are

    nu_1=(A,r_old,s_old)=(0,1,1),
    nu_2=(A,r_old,s_old)=(0,Y^3,Y^2).

These span the entire kernel of the common Phi_R restricted to W_plus.
They are not next-source increments in C830's actual Sigma_2, and their representatives need not lie in ker Theta.

Let N_1 and N_2 be the actual positive words obtained by multiplying the retained basis words selected by c_1 and c_2 and reducing each final label exponent modulo960 into0..959.
Their exact sizes and costs are:

| Word | Literal terms | Endpoint exponent | Cofactor trace degree | Reciprocal degree |
| --- | --- | --- | --- | --- |
| N_1 | 128 | 540 | 77221089 | 154442178 |
| N_2 | 127 | 840 | 63236394 | 126472788 |

For each i and e in{0,1,2,3}, let e_1=e mod2 and e_2=floor(e/2).
Reduce the final combined label exponent vector of K_i N_1^e_1 N_2^e_2 modulo960, call the resulting actual positive word K_(i,e), and select

    Q_(i,e)=R_i K_(i,e).                                   (SC1)

The old literal bundles constituting R_i are unchanged.
The complete label parameters and every word are specified by cases[source_mask=i,coset_bits=e] in the selected producer certificate.
Each case's bundle_words and literal_word use the complete actual labels in that same file; costs.terms and both complete factor-multiplicity lists record every degree and overlap.
The nullspace_certificate similarly contains both full N words and their costs.
This is an exact finite specification, not uninstantiated cofactor existence.

All four kernel vectors over each i are distinct and are exactly the target preimage.
By adopted C830 they give the four relevant Theta fibers containing every possible original F8 plus f8-half-zero member of Xi_16(R_i).
Exponent reduction changes the selected integer word and its cost; its use is justified by the proved higher-source exponent.
Nevertheless every selected SC1 word has its OWN original residue arrays computed below.

### C. Common next-half image and the exact sixty-four decisions

Use C830's [next normalized second half and source response](Yin_C_G0830_v1.md#next-normalized-second-half-response), with R_j=F_2[X]/f^j, lambda=X^3+X, chi=Xp(X)^2 and delta=(V-P^32)/2 over Z.
For each actual Q_(i,e), the original F8 and both X2 gates hold, and both genuine binary half classes are divisible by f^8.
Define

    g2_(epsilon,Q)=( [X_(epsilon,Q)/2]_J bar/f^8 ) mod f^4,
    beta_Q=b_Jbar/f^6, gamma_Q=c_Jbar/f^4,
    L2_Q(r,s)=deltabar[beta_Q^2 p(X)^28 r(lambda)^2
                       +gamma_Q^3(X+1)^28 s(chi)] mod f^4. (SC2)

The halves are formed over the integers before binary division and projection.
Here r and s range over the AMBIENT spaces F_2[Y]/p(Y)^2 and F_2[Y]/(Y+1)^4.
Their attainment by an actual Theta-kernel cofactor is not assumed.
The two g2 signs agree at this precision only.

All64 actual coefficient classes equal

    deltabar=1+X^8,
    beta_Q^2=gamma_Q^3=X^6+X^10 in R_4.

The common ambient map has rank6.
In source order r=1,Y,Y^2,Y^3 followed by s=1,Y,Y^2,Y^3, its eight columns are

    17412,257,17476,4097,64,2688,257,10794.                 (SC3)

A polynomial bitset uses bit j for the coefficient of X^j in its unique degree-below16 representative.
All256 ambient source images and every matching source mask are retained.
The functional ell(v)=[X^4]rem_(f^4)v, encoded by16, annihilates all eight columns and takes value1 on each of the32 nonmember targets.
For the other32 targets actual ambient preimages are checked; ell(v)=0 is not asserted sufficient for arbitrary elements of R_4.

<a id="complete-sixty-four-next-half-classification"></a>
The following table gives ALL64 targets and decisions.
Each four-entry tuple follows e=0,1,2,3 from SC1; the omitted cosets in the member column are the negative cases.
The degree entries include the fixed374-degree base, and the full reciprocal degree is twice each entry.

| Old source mask i | Four g2 target bitsets | Ambient member cosets e | Four actual original trace degrees |
| --- | --- | --- | --- |
| 203 | 4097, 11051, 6865, 8699 | 0, 1 | 65635185, 100393554, 67042779, 89572668 |
| 235 | 11131, 4177, 8619, 6785 | 2, 3 | 63767987, 88910996, 74753501, 100340990 |
| 331 | 7056, 8378, 4416, 10858 | 2, 3 | 82339440, 78169809, 69735834, 99127803 |
| 363 | 8426, 7104, 10810, 4368 | 0, 1 | 64972892, 90216701, 69935366, 70398695 |
| 715 | 7120, 8442, 4352, 10794 | 2, 3 | 81262740, 77093109, 68659134, 98051103 |
| 747 | 8362, 7040, 10874, 4432 | 0, 1 | 67456292, 92700101, 72418766, 72882095 |
| 843 | 4161, 11115, 6801, 8635 | 0, 1 | 67340385, 102098754, 68747979, 91277868 |
| 875 | 11067, 4113, 8683, 6849 | 2, 3 | 61761887, 86904896, 72747401, 98334890 |
| 1171 | 12523, 3009, 14907, 273 | 0, 1 | 79906502, 64300391, 90550256, 80839505 |
| 1203 | 64, 15210, 2704, 12730 | 0, 1 | 88751421, 68262750, 80537895, 75535944 |
| 1299 | 15226, 80, 12714, 2688 | 2, 3 | 71261237, 92946326, 87030431, 63873920 |
| 1331 | 3025, 12539, 257, 14891 | 2, 3 | 81161856, 79601505, 88773930, 67516299 |
| 1683 | 15162, 16, 12778, 2752 | 2, 3 | 70078937, 91764026, 85848131, 62691620 |
| 1715 | 2961, 12475, 321, 14955 | 2, 3 | 83215956, 81655605, 90828030, 69570399 |
| 1811 | 12459, 2945, 14971, 337 | 0, 1 | 81376502, 65770391, 92020256, 82309505 |
| 1843 | 0, 15146, 2768, 12794 | 0, 1 | 86788821, 66300150, 78575295, 73573344 |

Consequently EXACTLY32 of these Theta fibers are excluded from either complete original X4 gate, while32 are unresolved ambient members.
Every old source mask has two remaining cosets, so this screen excludes NO additional entire old Xi fiber.
Combining it with C825 therefore leaves the same16 old masks unresolved; it does not prove a whole-family exclusion.
Positive ambient membership asserts neither actual Sigma_2 attainment nor a complete X4 solution.

### D. Actual global gates, costs and limitations

Every one of the64 selected integer inputs has

    v2(a)=v2(b)=v2(c)=v2(G)=0,
    v2(F)>=3,
    v2(X_plus)=v2(X_minus)=1.

Their respective unscaled binary f-orders for a,b,c,G are8,6,4,12, so binary G is nonzero.
For EACH sign, the genuine half f-order distribution is56 cases of order8, four of order9, two of order10, one of order11 and one of order12.
Thus all64 chosen words pass F8 and both X2 but fail both complete X4 gates, including the ambient-member cases.
For(i,e)=(1843,0), g2=0 and both half orders are12, with initial units X and1+X+X^2 for the plus and minus signs, respectively; this is still not complete X4.
No F/8 class, exact v2(F)=3, modulo16 or every-root valuation is asserted.

The actual trace degrees range from61761887 to102098754, and the full reciprocal degrees from123523774 to204197508.
These are the extrema among the explicitly selected64 words, not optimal costs for their fibers.
All factors and multiplicities remain cyclotomic, so the total logarithmic Mahler measure is0 and the fixed base remains reducible.
No irreducible reciprocal nontorsion integer-unit input with controlled positive total measure is constructed.
Local f-order improvement is not additional global coefficient precision, and this result does not improve C757's same-input degree/precision certificate or resolve the unrestricted G0001 Task.

## Complete argument

### 1. Reused scope and complete finite reduction

C828 supplies the exact complete W_plus basis, common Phi_R, all actual K_i and the accepted native input scope.
C825 supplies the original R_i, their lower-gate hypotheses, actual arrays and the exhaustive old-fiber reduction.
C830 proves the genuine next-half formula, its actual source32/16 precision, the direct higher-source exponent960, whole-Theta-fiber obstruction and complete four-coset reduction.
Only those adopted conclusions are invoked here; the symbolic carry and period proof are not duplicated or inferred from a native sample.
C830's sufficient4194 higher alphabet is not evaluated by this calculation.

For every member Q of M, the adopted complete-factor argument gives H=H_0^2Q dividing a,c,b^2 and the residuals over Z, with Hbar prime to Jbar and residual/H degree below144.
C817/C736 therefore identify original GLOBAL coefficient congruences throughmod8 with the fully weighted restrictions at J.
In particular

    theta_p(T_0Q)|J=H_0(C_p)^2 Q(C_p) theta_p(J)

uses actual integer division by p, not unweighted canonical variables for a proper factor.
This is why the degree144 computation decides the original residuals despite the large complete degree.

### 2. Exact nullspace, both span directions and positive words

The producer reads precisely C828's joint image certificate and complete different verification, compares their generator data,59 kernel rows, projected-space data and all16 target/reference bindings, and retains the exact basis order.
It also compares the C825 reference arrays, words and costs with their complete different verification.
The four files are the explicit required inputs listed below.
No old4193/6310 image is regenerated.

For each of the59 images, high-pivot elimination tracks its59-bit source coefficients.
A nonzero reduction creates an image pivot, and a zero reduction supplies a source null relation with coefficient1 on its current basis index and no later coefficient.
The57 independent image pivots and two independent zero reductions therefore give the complete nullspace.
For all59 rows the certificate additionally retains a full image-basis reduction and the resulting null residue's coordinates in the two zero relations.
These identities establish both coverage and completeness, rather than exhibiting two sampled null vectors.
Their source coefficient masks are exactly c_1,c_2 above, and direct coordinate extraction gives nu_1,nu_2.

The producer multiplies the retained positive basis words and reduces final exponents modulo960.
Multiplication of the ADOPTED full Theta generator values checks each N_j and every new K_(i,e), including the entire first coordinate, both full sources and mixed Omega value.
Thus the words realize the stated intrinsic vectors.
Each four-vector set maps to the exact original target and is distinct.
C830's accepted injection and whole-fiber argument now make this the complete four-Theta-fiber cover for the relevant Xi16 input.

Complete factor multiplicities are recomputed from every actual rectangle:
for each divisor r>1 of n and every0<=u<=a,0<=v<=b the word contributes the trace factor F_(r3^u5^v) with its full exponent.
Endpoint and fixed-base multiplicities are added separately, including all overlaps.
The totient degree sum equals the literal actual q(n-1)/2 cost, and the reciprocal sum is twice the trace degree.
No degree is paid using q modulo a period.

### 3. Full original arithmetic for all sixty-four chosen words

The producer forms the exact integer P,V,J,H_0 and T_0 of degrees4,128,144,115 and374.
For p=2,3,5 the canonical numerator is calculated at coefficient precision8p, checked divisible by p and divided over the integers before reduction modulo8.
Both the direct full-base remainder and its H_0(C_p)^2 theta_p(J) transfer are retained and compared.

For every actual factor label and p it evaluates X-2 or the complete B_n(C_(p q)) using exact Chebyshev recurrences in the monic J quotient.
The actual integer q and selected exponent are unchanged during this arithmetic.
Caching powers of two is ordinary exponentiation, not an assumed mod8 image period.
The old R_i bundles, selected combined kernel bundle, total Q weight and full H weight remain separately bound to each word.
The old-reference weights are compared directly with the adopted C825 arrays.

All seven complete original classes are then calculated for EACH of the64 representatives, with the identity X_plus-X_minus=2G checked.
The complete output retains129 actual labels,387 factor values,9150 distinct powers and17444 literal occurrences, with all448 arrays, factor costs and exact cache-key bindings.
Every expected factor and power key is present and no unrelated key enters the result.
The first gate is checked modulo8; the true second halves are formed from even canonical coefficient representatives before binary f8 division.
Their complete R_4 targets and actual beta/gamma/delta classes are computed separately for every representative.
These are not transferred from an earlier word solely because its old Theta value agrees.

### 4. Different arithmetic and all ambient certificates

The different AUTHOR verifier was implemented without importing the producer's arithmetic.
It independently checks the rank59 source matrix, rank57 image matrix and rank2 nullspace using GF(2) matrix reduction.
Coefficient identities and the fixed prior pivot coordinates check every deterministic elimination row, all59 full reductions and both null masks.
It reconstructs both positive null words, every combined kernel word and every actual cost.
Adopted Theta values are multiplied with separate coefficient arithmetic; no new group image is claimed.

For original residues, the verifier reconstructs the complete integer factors from cyclotomic polynomials and performs both full-base and J prime divisions over Z.
It checks the exact integral identity

    z^144 J(z+z^(-1))=Phi_15(z)^4 Phi_960(z),

and works in the faithful degree288 Laurent quotient over Z/8.
The actual centered geometric sums are evaluated by denominator-free recursion with the unreduced integer p q and correct negative centering.
A full triangular trace-basis recovery checks all387 factor values,9150 powers, bundle/full weights and448 original arrays against the producer.
This uses full repeated-primary precision, not evaluation at individual roots.

For every case the verifier independently forms the genuine halves and normalized coefficients with SymPy over GF(2), evaluates all256 source pairs directly, checks the eight columns, full rank and each target's augmented rank, and compares the complete source-image and matching-preimage lists.
Each producer basis vector is a checked image, the basis has full image rank, and its target normal remainder and all negative separating functionals are checked.
Both signs are covered.
The producer and verifier agree completely on the nullspace, representative words/costs, original arrays, source-image values and all64 decisions, without implementation repair.
These remain author checks; the separately arranged [whole independent R1051](../audits/reviews/Yin_R_G1051_v1.md#whole-finding) subsequently inspected and reproduced their complete selected scope.

### 5. Exact exclusions and failure of complete old-fiber elimination

The verified common map has rank6 and columns SC3.
Since each negative target has ell=1 while ell annihilates the complete image, it is not an ambient member.
For each positive target the retained source masks give actual ambient preimages, with no inference that these source pairs arise from M.
C830's whole-Theta-fiber theorem excludes BOTH original X4 signs in each negative case, including arbitrary actual words sharing that Theta value and not just the chosen representative.
Its actual positive-common-word costs remain part of the invoked theorem.

The exact four-coset cover and the table show that every remaining old mask has two ambient-member cosets.
Therefore none satisfies the four-negative sufficient condition for a whole Xi16 exclusion, and C825 supplies no new old-fiber exclusion from this result.
All chosen representatives happen to fail full X4 by their nonzero full half arrays, but that one-word fact cannot replace the missing actual correction obstruction in an ambient-member Theta fiber.
In particular the zero g2 at mask1843/coset0 merely marks a later nonzero half term.

The calculation rules out32 exact Theta alternatives and demonstrates that this ambient next-half screen does not close any of the16 remaining old fibers.
It neither determines Sigma_2 nor solves complete X4.
Its large-degree, reducible, total-measure-zero inputs remain outside the irreducible positive-measure domain of C757.
No automatic further precision or image iteration is part of the conclusion.

### 6. Selected native inputs and reproduction boundary

The two NEW selected programs are [complete_four_coset_next_half_screen.py](../computations/programs/Yin_J_G0132/complete_four_coset_next_half_screen.py) and [verify_complete_four_coset_next_half_screen.py](../computations/programs/Yin_J_G0132/verify_complete_four_coset_next_half_screen.py).
The complete selected producer certificate (`mathematics/computations/outputs/Yin_J_G0132/complete_four_coset_next_half_screen.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/complete_four_coset_next_half_screen_verification.json`) retain the entire64-case payload and exact word/factor/source bindings.
The four required adopted files are C828 image (`mathematics/computations/outputs/Yin_J_G0132/joint_eighth_second_half_kernel_image.json`), C828 verification (`mathematics/computations/outputs/Yin_J_G0132/joint_eighth_second_half_kernel_image_verification.json`), C825 screen (`mathematics/computations/outputs/Yin_J_G0132/complete_local_target_second_half_screen.json`) and C825 verification (`mathematics/computations/outputs/Yin_J_G0132/complete_local_target_second_half_screen_verification.json`).
These supply the old mathematical data at their accepted scopes; saved constants from commentary are not used as an oracle.

The existing J132 [phase entrance](../computations/programs/Yin_J_G0132/readme.md#complete-four-coset-next-half-screen) gives command order and arithmetic dependencies.
Only the two new programs and their actual imported helpers at the used arithmetic scope are selected for this calculation; older unrelated producer bodies are not executed by imports guarded by main.
All64 cases are completed, with no early exit, optimization, other word choice, new4194 image, higher modulus or full huge-degree expansion.
No measured elapsed time or peak memory was collected; the actual completed cache counts and input-derived caps are retained instead.
The theorem does not identify this new different AUTHOR verification with an independent review.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision complete-four-coset-screen-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T17:44 |
| status | open |
| reason | Fix the complete actual four-coset screen:59 tracked images and two positive nullspace words, all64 original mod8 systems and costs, rank6 next-half image,32 exact Theta-fiber exclusions and32 unresolved ambient members with two over each old mask. Both distinct AUTHOR implementations completed without repair. No additional old-fiber exclusion, full X4 witness, actual Sigma2 image, larger modulus, irreducible positive-measure input or unrestricted Task conclusion is claimed. Cold whole mathematical/native review remains outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact representative system and complete64 classification](#statement) | Actual fixed integer family, two intrinsic null directions and positive words, all64 selected representatives/costs, complete ambient image and both-sign decisions, original gates and all limitations. |
| argument | [Complete finite/native proof](#complete-argument) | Adopted four-coset and original-weighting interfaces, full nullspace and actual word checks, all original arrays, different exact arithmetic, full ambient certificates and precise whole-fiber consequences. No mutable Draft premise. |
| dependency | [Adopted next-half and four-coset theorem](Yin_C_G0830_v1.md#decision-whole-reviewed-2026-10-28) | Genuine next-half formula, exact new sources, direct exponent960 and complete four-Theta-fiber cover, negative ambient whole-fiber implication and original domain/measure limits. Its higher4194 image is not computed. |
| dependency | [Adopted actual complete joint image](Yin_C_G0828_v1.md#decision-whole-reviewed-2026-10-28) | Complete59-row W_plus basis and actual words, common projected rank57, all16 target/reference/word bindings and required native certificate with verification; no old image regeneration. |
| dependency | [Adopted old-fiber reduction and references](Yin_C_G0825_v1.md#decision-whole-reviewed-2026-10-27) | Exact16 unresolved original R_i and lower-gate data, common normalized coefficient classes, exhaustive old-source reduction and already excluded other16 old fibers. |
| dependency | [Adopted original global quotient interface](Yin_C_G0817_v1.md#decision-whole-reviewed-2026-10-26) | Full endpoint/rectangle factor coverage and original-global monic unit/degree equivalence throughmod8, with actual single F960 and all repeated factors. |
| dependency | [Adopted integer canonical weighting](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Genuine prime divisions before restriction and complete original cofactor weights, not canonical inheritance from an unweighted proper factor. |
| support | [Complete two-program native phase](../computations/programs/Yin_J_G0132/readme.md#complete-four-coset-next-half-screen) | Both new sources and complete outputs, four explicit adopted inputs, all59 reductions/two actual null words, all64 representative/array/cost/ambient records and different AUTHOR checking scope. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T17:55 |
| status | proved |
| reason | Adopt the unchanged complete64 classification after whole independent mathematical/native R1051 and responsible inspection of the entire fixed theorem, argument, exact inputs and full review. The reviewer reproduced all64 cases with the different verifier and reconciled every native field, while separately deriving the complete ambient system and all statement values. Exactly32 Theta fibers are excluded and32 remain ambient members, with two survivors for each old mask and no additional entire old-fiber exclusion. Every selected word still fails full X4. All original costs, modulo8 limits, actual-attainment gaps and cyclotomic/reducible/zero-measure boundaries remain; G0001 is unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact representative system and complete64 classification](#statement) | Actual fixed integer family, two intrinsic null directions and positive words, all64 selected representatives/costs, complete ambient image and both-sign decisions, original gates and all limitations. |
| argument | [Complete finite/native proof](#complete-argument) | Adopted four-coset and original-weighting interfaces, full nullspace and actual word checks, all original arrays, different exact arithmetic, full ambient certificates and precise whole-fiber consequences. No mutable Draft premise. |
| dependency | [Adopted next-half and four-coset theorem](Yin_C_G0830_v1.md#decision-whole-reviewed-2026-10-28) | Genuine next-half formula, exact new sources, direct exponent960 and complete four-Theta-fiber cover, negative ambient whole-fiber implication and original domain/measure limits. Its higher4194 image is not computed. |
| dependency | [Adopted actual complete joint image](Yin_C_G0828_v1.md#decision-whole-reviewed-2026-10-28) | Complete59-row W_plus basis and actual words, common projected rank57, all16 target/reference/word bindings and required native certificate with verification; no old image regeneration. |
| dependency | [Adopted old-fiber reduction and references](Yin_C_G0825_v1.md#decision-whole-reviewed-2026-10-27) | Exact16 unresolved original R_i and lower-gate data, common normalized coefficient classes, exhaustive old-source reduction and already excluded other16 old fibers. |
| dependency | [Adopted original global quotient interface](Yin_C_G0817_v1.md#decision-whole-reviewed-2026-10-26) | Full endpoint/rectangle factor coverage and original-global monic unit/degree equivalence throughmod8, with actual single F960 and all repeated factors. |
| dependency | [Adopted integer canonical weighting](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Genuine prime divisions before restriction and complete original cofactor weights, not canonical inheritance from an unweighted proper factor. |
| support | [Complete two-program native phase](../computations/programs/Yin_J_G0132/readme.md#complete-four-coset-next-half-screen) | Both new sources and complete outputs, four explicit adopted inputs, all59 reductions/two actual null words, all64 representative/array/cost/ambient records and different AUTHOR checking scope. |
| review | [Whole independent mathematical/native R1051](../audits/reviews/Yin_R_G1051_v1.md#whole-finding) | Entire fixed statement and argument, all exact adopted/native inputs and64 bindings, full different-verifier reproduction and complete payload equality, separate direct ambient/table reconciliation and all limitations. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0132](../computations/programs/Yin_J_G0132/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
