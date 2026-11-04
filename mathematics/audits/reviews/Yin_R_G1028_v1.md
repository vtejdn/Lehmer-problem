---
author: Yin
---

# Independent whole review of the explicit varying-source global-eight Mahler floor

Review act: 2026-10-26T17:14 UTC, human record author Yin.
This is an initial independent whole-proof review of fixed [C808 v1](../../claims/Yin_C_G0808_v1.md#statement), its entire [effective comparison proof](../../claims/Yin_C_G0808_v1.md#effective-varying-window-proof), and its [open decision](../../claims/Yin_C_G0808_v1.md#decision-effective-varying-window-open) dated 2026-10-26T17:01.
The reviewer is a separate agent outside C808's substantive development and received the fixed target and exact input locators directly.
No C808 development draft, author dialogue or mathematical summary, other C808 verdict or persistent memory was supplied or consulted.
Contributor disclosures in the fixed target were read as part of that target.
This C808 review was performed by this reviewer alone; no new helper finding is relied upon.

The reviewer previously performed the independent whole C804 inspection recorded in [R1024](Yin_R_G1024_v1.md#whole-global-eight-window-mahler-finding), without contributing to that proof.
Its unchanged template, integer prefix, normalization, actual domain and nonempty-realization conclusions are reused only at their recorded scopes after reading C804's current statement and adopted decision.
This input reuse is distinct from the new complete C808 verification below.
The current source check additionally inspected the actual published BGMP24 passages at the limited depth stated below.
No mathematical repair or author-side construction was supplied during this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole varying-source finding](#whole-effective-varying-window-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole varying-source finding](#whole-effective-varying-window-finding) | [C808 Statement](../../claims/Yin_C_G0808_v1.md#statement) | Entire EW1--EW6, actual source/mask/global-eight domain, all constants and normalization, paid original progression, conditional common numerical floor, varying-source hypotheses and limitations. |
| [Whole varying-source finding](#whole-effective-varying-window-finding) | [C808 complete effective proof](../../claims/Yin_C_G0808_v1.md#effective-varying-window-proof) | Entire Sections 1--5: support/height/length/diameter, both normalized Proposition 4.10 applications, logarithmic-zero regularization, smooth equal-interval averaging, error cancellation, tolerance arithmetic, varying-source limit and realized nonempty families. |
| [Whole varying-source finding](#whole-effective-varying-window-finding) | [C808 open decision](../../claims/Yin_C_G0808_v1.md#decision-effective-varying-window-open) | Exact fixed input selection and qualified scope; this R supplies review evidence without selecting acceptance. |

## Fixed project and source inputs

The mathematical project input is [adopted C804 v1](../../claims/Yin_C_G0804_v1.md#decision-whole-reviewed-2026-10-26).
Its exact F_A identity, full-factor equality m(P)=m(K)=m(L_0), nonempty Jensen floor m_2(F_A)>=log 2, actual C799/C801 domain and paid nonempty masks are used.
The source and original N progression retain all full primary, multiplicity, canonical-divisor, gap and original minimum-s conditions.
C808 does not obtain a rate from C804's qualitative Lawton theorem and does not need C804's cyclotomic-degree certificate.
The earlier source-proof and complete-construction limits of R1024 remain unchanged for the adopted inputs.

The external analytic input is the exact general Proposition 4.10 in [BGMP24-U001](../literature/BGMP24/Yin_U001.md#bgmp24-u001).
The reviewer read its complete accepted-interface and scope account, then directly text-read the retained [published BGMP24 article](../../literature/pdf/BGMP24.pdf), Sections 2.2--2.5 at printed pp.1414--1415 / PDF pp.9--10, and Proposition 4.10 with its proof at printed pp.1429--1431 / PDF pp.24--26.
Rendered PDF pp.24--25 were visually inspected to verify the hypotheses, half-log normalization, exponent and C_2 formula.
The inspected edition is published; no acquisition or edition substitution is recorded here.

The original statement explicitly permits every integer k>=2 and n>=1, coefficient maximum one, m<=n, strict rho(A)>diam(P), 0<alpha<1 and every epsilon>0.
Diameter is maximum coordinate support width, rho uses the infinity norm of integer kernel vectors, and the measures are probability Haar pushforwards.
The identity matrix has rho=infinity and full Haar pushforward; the row matrix (1,N) gives precisely the circle specialization used here.
The general-k application is consequently supported by the original proposition, not extrapolated from C433's fixed k=3 or 11 applications.

The displayed nonnegative layer-cake reduction and its dependence on the sublevel estimate were checked, including the trivial probability bound when the sublevel parameter exceeds one.
Theorem 4.6 remains an accepted established external input; its proof was not independently re-audited.
This is not a full-paper source audit.
The questioned later Theorem 4.1 optimization/constant and the later half-log issue are not used.
The [C433 statement](../../claims/Yin_C_G0433_v1.md#statement) was read only to verify the earlier application boundary.
The [C425 statement](../../claims/Yin_C_G0425_v1.md#statement) was read only to distinguish its different nonvanishing family and averaging precedent from C808's complete regularized argument.
Other qualitative comparison links in C808 Section 1 are context rather than premises of EW1--EW6; their unrelated assertions are not covered by this review.

## Exact coefficient and specialization checks

The actual nonempty mask starts at or above h>0, so J=deg A>=h and h<M=J+1<=h+7P_8.
For g=A_H-2(1-z)A, coefficients below h remain those of A_H, the coefficient at h is 1-2A_h in {-1,1}, coefficients above h are in {-2,0,2}, and the coefficient at M is exactly two.
In particular no coefficient of magnitude three is hidden at the joining point h.
Expanding (1-Y)(1+Y^2)(1-Y^4) gives exactly the two extreme rows g and z^h g(z^(-1)), with six signed A_H middle rows at distinct Y exponents.
Therefore F_A has coefficient height exactly two.

Since (1-z)A has both support size and coefficient length at most 2wt(A),

    k(F_A)<=6w_H+2(w_H+2b)=S,
    ||F_A||_1<=6w_H+2(w_H+4b)=2L.

The extreme rows are nonzero, so k>=2.
Their nonzero endpoints give exact z range [h-M,M] and Y range [0,7]; hence diam(F_A)=max(2M-h,7)<=V.
The normalized shift R=z^(M-h)F_A/2 has coefficient maximum one, unchanged k, length at most L and z exponents in [0,2M-h].
Its monomial has modulus one on both tori and the specialized circle, and its scalar subtracts log 2 from both measures, so the normalization cancels exactly in their difference.

Every integer relation of (1,N) is a multiple of (N,-1), giving rho=N for positive N.
A collision of different Y rows would require a z-exponent difference of magnitude at least N, whereas the available width is at most V.
When N>V, no such collision occurs; equal Y exponents collide only for the same formal term.
Thus the specialized polynomial is nonzero and retains the coefficient normalization and count required by the source.
The strict N>V condition is correctly treated as an additional paid restriction, not inferred from h+7P_8<N alone.

## Zero-compatible comparison and error constant

Substituting n=2 and alpha=1/2 in the original source formula gives

    C_2=12k^2(36k^2)*2/(1/2)=1728k^4,
    exponent=1/(4(k-1)).

Both maps have m<=n and satisfy the strict diameter condition.
The proposition gives finite nonnegative regularization errors at every positive epsilon, including all torus or circle zeros.
For 0<epsilon<=1 and 2<=k<=S,

    k^4 epsilon^(1/(4(k-1)))
       <=S^4 epsilon^(1/(4(S-1))),

so e_N and e_2 lie in the same interval [0,C] with C=1728S^4 epsilon^(1/(4(S-1))).
The exponent comparison has the correct direction, including k=2 and epsilon=1.
No positive lower bound for the original modulus is imported from C425.
The logarithms are integrable at the accepted source depth, and H_epsilon is smooth even at zeros.

With the second circle coordinate fixed, the shifted support gives |partial_theta R|<=sum a|c_(a,q)|<=(2M-h)||R||_1<=VL.
The scalar inequality u/(u^2+epsilon)<=1/(2sqrt(epsilon)) gives |partial_theta H_epsilon|<=VL/(2sqrt(epsilon)).
This differentiates only the slow coordinate, not the diagonal; no factor N is omitted.
Splitting theta into N equal intervals and substituting theta=(2pi j+phi)/N proves the displayed diagonal average by periodicity.
Independently splitting the full-torus first coordinate proves the second displayed average.
The paired first arguments differ by at most 2pi/N, so integration of the derivative bound gives exactly pi VL/(N sqrt(epsilon)).

The logarithmic measure difference equals this smooth-average difference plus e_2-e_N.
Since e_2,e_N belong to [0,C], their difference has absolute value at most C.
The error constant therefore needs no extra factor two.
Scalar and monomial normalizations cancel, proving the full absolute EW1 estimate.
C804's exact total-measure identity and nonempty m_2(F_A)>=log 2 give its stated lower direction.
Every factor and multiplicity is retained; no degree normalization or factorwise residual implication is used.
The common S,V,L bound gives pointwise uniformity over all actual admissible masks of that budget, without choosing a constant-mask subsequence.

## Exact cutoff and varying-source consequences

For 0<eta<=1, epsilon=(eta/(3456S^4))^(4(S-1)) lies in (0,1] and makes the regularization term eta/2.
Its square root is (eta/(3456S^4))^(2(S-1)).
The displayed integer T_eta and N>=T_eta make the averaging term at most pi eta/8<eta/2.
The same cutoff is greater than V, since 8VL/eta>=8V and the remaining positive power exceeds one.
Thus it supplies the strict diameter hypothesis and proves EW2--EW3 with the claimed constants.

The actual step 2B_step Delta_crit is a positive integer.
The ceiling in EW4 therefore implies N=1+2B_step Delta_crit s>=T_eta while preserving the original progression and s_min.
At eta=1/2 the constants become 16VL and 6912S^4, exactly as in EW5.
The identity log 2=int_1^2 dt/t>1/2 proves its numerical floor is positive.
This gives a common numerical lower value on families satisfying their separately paid source/budget cutoffs, not an unconditional bound for every original admissible s.

For EW6, V_j L_j=o(sqrt(N_j)) and L_j>=1 imply N_j>V_j eventually.
The permitted choice epsilon_j=N_j^(-1) yields the two displayed terms.
The averaging term tends to zero by the second hypothesis.
The logarithm of the regularization term is

    log 1728+4 log S_j-log N_j/(4(S_j-1)).

The first hypothesis log N_j/(S_j log S_j)->infinity and S_j>=2 force this expression to minus infinity, including bounded or intermittently bounded S_j.
The total error tends to zero, and the pointwise integral floor gives liminf m(P_(N_j))>=log 2.
Neither convergence of the changing integral values nor convergence of the changing measures is deduced.
The conditions are sufficient only; necessity and an implication from s_min are not claimed.

## Genuine families and complete finding

The C804 one-extra-bit family has b_+=7D+1, hence exactly S_+=8w_H+28D+4 and L_+=4w_H+28D+4.
The full-window family has b_win=7P_8, hence exactly S_win=8w_H+28P_8 and L_win=4w_H+28P_8.
Both use the same V and actual nonempty existence at every original s; the latter retains at least 2^(7(P_8-D))-1 nonempty outputs for each separately chosen sign.
The global-eight constraints come from these genuine adopted sign completions, not from declaring arbitrary masks admissible.
All extra flips are paid, and increasing the original unbounded parameter s to meet the cutoff is compatible with the actual constructions.
No source factor, original cost, canonical divisor or full-product/core distinction is changed.

<a id="whole-effective-varying-window-finding"></a>
## Verdict and retained limits

No mathematical defect or missing applicability hypothesis was found in the entire fixed C808 Statement, Sections 1--5, EW1--EW6 or its selected open decision's actual input scope.
The normalized coefficient bounds, zero-compatible comparison, one-sided regularization constant, original-progression cutoff and varying-source liminf are supported at the source depth stated above.
The nonempty realizations are actual original global-eight outputs with separately paid budgets.
The proof supplies the explicit paid threshold and sufficient varying-source conditions without improperly applying fixed-polynomial convergence uniformly over changing templates.

The empty mask remains excluded with its separate C804 measure m(A_H) and unresolved global-eight admissibility.
Outside-window masks, original parameters below the cutoff, necessity or optimality of the cutoff, uniform control without the paid conditions, nearzero constructions and the unrestricted G0001 objective remain outside the conclusion.
The underlying Theorem 4.6 proof and earlier complete source-construction proofs retain their accepted-input boundaries.
No native polynomial expansion, quadrature, sign enumeration, numerical factorization or proof-assistant verification was performed.
The direct original-source check has the specific passage depth stated above and is not a full-source audit.
No substantive correction is needed for adoption at this exact theorem scope.
Adoption and shared navigation remain the responsible main agent's separate actions.
