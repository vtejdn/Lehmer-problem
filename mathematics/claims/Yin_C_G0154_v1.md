---
author: Yin
---
# Complete diagonal-sign Frobenius determinant averages and their exact coefficient costs

Human author Yin.
New G0001 author inquiry by g_bridge_audit.
Root supplied the concrete noncommuting family V=diag(epsilon_0,...,epsilon_(d-1)), the focus p=2 and the question of the complete2^d determinant-square average.
This is a substantive family/question contribution, retained separately from C152's older joint contributions.
The author supplies the new sign/band reduction and is responsible for the proof and costs.
No numerical scan or native mathematical program is used.

## Exact question and bounded reuse

Use the actual original monic irreducible nontorsion integer-unit polynomial P=t^d+sum_(j=0)^(d-1)c_j t^j, d>=2,c0=+/-1.
The responsible adopted antecedent [C152](Yin_C_G0152_v1.md#decision-whole-reviewed-2026-10-16) supplies the actual companion convention, q=rho2(A)e0, C(V)=q ell+A^2V-VA and its free integer polynomial columns at window N=2d.
C152's actual whole independent adoption does not review the new deductions here; all interfaces needed for them are reconstructed below.

The bounded reuse screen read [C50's complete finite sign cancellation](Yin_C_G0050_v1.md), [L223's Boolean character convention/orthogonality](../ledger/Yin_L_G0223_v1.md#partial-mask-collision-information-retention) and [L234's precise reused attribution](../ledger/Yin_L_G0234_v1.md#walsh-companion-ratio-construction).
Existing diagonal-sign matches concern congruences, Coxeter presentations or scalar substitutions, not this full Frobenius determinant family.
Those searches do not establish novelty.
Only finite character orthogonality, proved by independent sign averaging, is needed; no hypercontractivity or random-matrix theorem is imported.
[C226 retained projection identity](Yin_C_G0226_v1.md#projection-cost-identity) remains the exact fixed-window upper interface, so an average numerator must retain the matching average coefficient cost.
The return uses [L4's original Gram entropy bound](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate); its [already proved composition identities](../ledger/Yin_L_G0004_v1.md#degree-window-tests) are reused in Section 7, not treated as new here.

<a id="statement"></a>
## Complete author statement

For every P in the stated domain, with the actual original companion matrix and p=2, the complete uniform family of all 2^d diagonal signs has the exact determinant-square average A_P in (7)--(8) and the exact FREE coefficient-volume average B_P in (10).
At least 2^(d-2) actual determinants are nonzero.
Both averages include every sign, including singular labels, and their ratio is a positive lower certificate for the original window-2d orbit Gram as in (13); its full entropy return is exactly (14).
All coefficients of rho2 and delta_2P in these formulas refer to their distinct stated representatives.
The quarter nonzero bound is not a new prime-valuation surplus, and the raw mandatory power of 2 cancels against the matching raw coefficient cost.

If P=P0(t^N) is ACTUALLY irreducible with N>=3, the conditional composition calibration (15)--(19) holds with all original discriminant, degree and coefficient costs.
No infinite irreducible composition family, near-one sequence or uniform Lehmer gap is asserted.
The derivation and hand controls below constitute a complete author proof, still subject to the separately arranged whole independent review and adoption.

<a id="argument"></a>
## Complete argument

<a id="sign-family-and-path-reduction"></a>
## 1. Exact family and independent path coordinates

Use the basis e0,...,e_(d-1), with A e_j=e_(j+1) for j<d-1 and A e_(d-1)=-sum c_j e_j.
Let ell=e_(d-1)^T and let U0 have column j equal to A^(2j)e0.
Then A^2U0-U0A has only its last column nonzero, equal to P(A^2)e0.
Write rho2(t)=rem_P P(t^2)/2=sum_(j=0)^(d-1)q_j t^j and z(t)=delta_2 P(t)=[P(t^2)-P(t)^2]/2=sum_(j=0)^(2d-1)z_j t^j, including zero coefficients.
Reduction of the integral polynomial z shows that rho2 is integral and q=rho2(A)e0; hence A^2U0-U0A=2q ell.
Moreover rho2 is nonzero: if P(alpha^2)=0, conjugating over all roots makes the finite nonzero root set closed under squaring; every element then has a repeated pair of powers of 2 and is a root of unity, contrary to the domain.
For each epsilon in{+/-1}^d take V_epsilon=diag(epsilon_j), U=U0+2V_epsilon and C_epsilon=q ell+A^2V_epsilon-V_epsilon A.
Thus A^2U-UA=2C_epsilon.
Its determinant is an integer; it may be zero for individual signs.
The complete average includes all 2^d signs equally.

Let eta=epsilon_(d-1), tau_j=epsilon_j epsilon_(j+1) for0<=j<d-1, and omega_1=1,omega_k=product_(h=0)^(k-2)tau_h for2<=k<=d.
Then eta,omega_2,...,omega_d are independent uniform signs: the inverse is epsilon_j=eta omega_d omega_(j+1).
Also epsilon_j epsilon_(d-1)=omega_d omega_(j+1).

Right multiplication of the actual column matrices by V_epsilon preserves their determinant square and coefficient Gram determinant.
After this multiplication the first d-1 FREE polynomial columns are

    b_j=t^(j+2)-tau_j t^(j+1),   0<=j<d-1,             (1)

and the last is

    g=t^(d+1)+sum_(j=0)^(d-1)c_j omega_d omega_(j+1)t^j
                                                   +eta z(t). (2)

Their ORIGINAL reduction matrix is C_epsilon V_epsilon.
They are genuine coefficient columns within[0,2d-1], not assumed independent after original evaluation.
In particular the free z(t) in(2) and its reduced remainder rho2 are different representatives with different coefficient costs; they agree only after evaluation at alpha.

<a id="cofactor-and-numerator-identity"></a>
## 2. Exact cofactor functional and the full average numerator

Define a linear functional w on the actual power-basis value vectors by

    w0=-sum_(i=1)^(d-1)c_i omega_i-omega_d,
    w_i=c0 omega_i,       1<=i<=d-1.                    (3)

The recurrence omega_(j+2)=tau_j omega_(j+1) and the relation alpha^d=-sum c_j alpha^j show w(b_j(alpha))=0 for every first column.
The minor obtained by deleting row1 from those first d-1 columns has the appropriate signed value -c0 as coefficient of the last column's row1.
Expanding on the sole row0 entry -c0 in the last of those columns verifies this sign directly; the remaining path minor is triangular with unit diagonal.
Hence those columns are linearly independent in the original d-dimensional value space and their determinant cofactor functional is EXACTLY -w.
This includes d=2, where the single column is -c0 e0-(c1+tau0)e1.

Extend w to evaluated polynomials by the original quotient relation.
It has w(alpha^j)=c0 omega_j for1<=j<=d and therefore w(alpha^(d+1))=-c0 sum_(j=0)^(d-1)c_j omega_(j+1).
Define

    K_j=omega_(j+1)+omega_d omega_j
                              -omega_d omega_j omega_(j+1),
                                  1<=j<=d-1,
    B(omega)=c0+1+sum_(j=1)^(d-1)c_j K_j,
    R(omega)=sum_(i=1)^(d-1)(c0 q_i-q0 c_i)omega_i
                                                   -q0 omega_d.
                                                               (4)

Substitution in(2)--(3) gives w(g-eta z)=-c0 B and w(q)=R.
Consequently

    det(C_epsilon V_epsilon)=c0 B(omega)-eta R(omega),
    average_epsilon det(C_epsilon)^2
                         =average_omega B^2+average_omega R^2.   (5)

The second equality first averages the INDEPENDENT eta and uses c0^2=1.
No independence between polynomial columns or root values is assumed.

Set

    r(t)=[c0 rho2(t)-q0 P(t)]/t in Z[t], deg r<d.       (6)

The numerator has zero constant coefficient, so this is an actual polynomial, not a rational function.
Its coefficients are exactly c0q_i-q0c_i for1<=i<=d-1 followed by -q0.
At alpha, r(alpha)=c0 q(alpha)/alpha.
Thus it is the unique degree<d representative of a signed UNIT TWIST of the OLD base Frobenius quotient.
In particular r is nonzero and ||r||_2^2>=1.
Finite sign orthogonality gives average R^2=||r||_2^2, where coefficient2-norm is meant, not an embedding norm.

The remaining quadratic form in the ORIGINAL coefficients is

    Q_P=(c0+1-c1)^2+4c1^2,                         d=2;

    Q_P=(c0+1)^2+3 sum_(j=1)^(d-1)c_j^2
             -2c1 c2-2c_(d-2)c_(d-1)+2c1 c_(d-1), d>=3.
                                                               (7)

The complete answer for the numerator is therefore

    A_P:=2^(-d) sum_epsilon det(C_epsilon)^2
                                =Q_P+||r||_2^2.        (8)

Here is the full finite-character check, including overlapping boundary indices.
If d=2, K1=2omega2-1, giving the first line.
If d>=4, every K_j has squared average3 and mean0.
The only nonzero off-diagonal inner products are <K1,K2>=-1, <K_(d-2),K_(d-1)>=-1 and <K1,K_(d-1)>=1.
They follow from the shared singleton/pair characters; each remaining singleton, pair or triple is distinct.
At d=4 these are three different pairs and the rule still holds.
At d=3 the two functions are omega2+omega3-omega2omega3 and omega3+omega2omega3-omega2, whose inner product is-1 and squared averages are3.
In the displayed formula the three overlapping boundary terms combine to exactly-2c1c2, as required.
This establishes(7)--(8) for every allowed d without an asymptotic or numerical check.

<a id="quarter-nonzero-signs"></a>
## 3. At least one quarter of all signs are actually nonzero

The affine linear sign polynomial R in(4) is nonzero because r!=0.
If its variable coefficients all vanish, its constant coefficient is nonzero, so R never vanishes.
Otherwise fix a variable with a nonzero coefficient and condition on all the other signs: at most one of its two choices makes R zero.
Hence at least half of all omega have R!=0.
For each such omega, the two eta choices in(5) cannot both give zero.
Thus

    #{epsilon:det C_epsilon!=0}>=2^(d-2).              (9)

This is an all-degree bound for the ACTUAL integer matrices, not merely positivity of the mean and not a choice of separate signs at different roots.
Each nonzero raw determinant det(A^2 U-U A)=2^d det C_epsilon has the original mandatory2^d divisibility.
It remains an integer matrix determinant; no conversion into a degree-d field norm is asserted.
Deleting zero labels or changing weights would be a different finite distribution and is not done in the mean identities.

<a id="exact-average-coefficient-volume"></a>
## 4. The matching full coefficient-volume average

Let Q_epsilon be the actual 2d by d FREE coefficient matrix before right multiplication.
Its columns are epsilon_j t^(j+2)-epsilon_(j+1)t^(j+1) for j<d-1, and epsilon_(d-1)t^(d+1)+sum c_j epsilon_j t^j+z(t) last.
Thus C_epsilon=R_(2d)Q_epsilon exactly.
The path-form coefficient matrix in (1)--(2) is Q_epsilon V_epsilon, which has the same Gram determinant; the matrices themselves are not being identified.
Define

    B_P:=2^(-d)sum_epsilon det(Q_epsilon^T Q_epsilon).

Then the exact formula is

    B_P=d[2+z0^2+sum_(k=d+1)^(2d-1) z_k^2]
                   +sum_(j=1)^(d-1)c_j^2+sum_(k=1)^d z_k^2.
                                                               (10)

To prove it, the first d-1 coefficient columns form a signed path incidence matrix on coordinates1,...,d.
Diagonal sign conjugation transforms their Gram matrix into the usual tridiagonal matrix with diagonal2 and adjacent entries-1.
Its determinant is d: expanding successively gives D_n=2D_(n-1)-D_(n-2),D_0=1,D_1=2, so D_(d-1)=d.
Their span has orthogonal complement inside those d coordinates generated by (omega1,...,omega_d), of squared norm d.
It also has every external coordinate0,d+1,...,2d-1 in its orthogonal complement.
For any last coefficient column g, the squared full volume is consequently

    d[g0^2+sum_(k=d+1)^(2d-1)g_k^2]
                             +(sum_(k=1)^d omega_k g_k)^2.       (11)

This follows by resolving g into its component orthogonal to the first columns; it remains true if that component is zero.
For the actual g in(2),

    g0=c0 omega_d+eta z0,
    g_k=1_(k=d+1)+eta z_k,                   k>d,
    sum_(k=1)^d omega_k g_k
      =omega_d sum_(k=1)^(d-1)c_k omega_k omega_(k+1)
                                      +eta sum_(k=1)^d z_k omega_k.
                                                               (12)

Average first in eta.
The edge characters omega_k omega_(k+1),1<=k<d, are distinct and orthogonal, including k=1 with omega1=1.
Multiplication of all of them by omega_d preserves orthogonality.
The coordinate characters omega1,...,omega_d are also orthogonal.
Thus the two last squared terms average to sum c_k^2 and sum z_k^2, respectively.
The external-coordinate contribution averages to d[1+z0^2+1+sum_(k>d)z_k^2].
This proves(10), including d=2 and c0=-1, where z0=-1 rather than0.
The coefficient z here is the FREE delta_2P, not its reduced rho2.

<a id="averaged-projection-and-paid-return"></a>
## 5. Exact averaged certificate and the retained projection boundary

For every sign, C_epsilon=R_(2d) Q_epsilon.
Let G_(2d)=det(R_(2d)R_(2d)^T).
By L56, including singular images by continuity or the zero determinant inequality,

    det(C_epsilon)^2<=G_(2d) det(Q_epsilon^T Q_epsilon).

Summing this exact inequality gives

    0<A_P/B_P<=G_(2d),
    2^(-d)sum det(A^2U-U A)^2=2^(2d) A_P,
    2^(-d)sum det((2Q_epsilon)^T(2Q_epsilon))=2^(2d) B_P.
                                                               (13)

Thus the mandatory prime factor cancels in the ratio of these FULL averages as well.
Since B_P>=2d>0, there is at least one sign with positive coefficient cost and det(C_epsilon)^2/det(Q_epsilon^T Q_epsilon)>=A_P/B_P; terms of zero coefficient cost also have zero image determinant and cause no division.
This existence statement uses the appropriate cost-weighted mean, not the mean of undefined ratios at zero-cost labels.

The exact numerator(8) is a sparse quadratic form in P's original coefficients plus the coefficient energy of the old base quotient after a unit twist.
It is not a new independent prime valuation floor.
Its second term can be large precisely because remainder coefficients can be large; the denominator(10) retains the different unreduced representative's coefficients.
Equation(13) identifies the resulting finite test as an explicit lower certificate for the ALREADY KNOWN original orbit Gram at the same window.
It does not prove that A_P/B_P is the Gram itself, that it is always at most1, or that every arithmetic estimate on it is impossible.

If it is inserted into the [adopted original Gram entropy inequality](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate), with Delta_P=|disc P| and N=2d, the complete candidate is

    m(P)>=[log(Delta_P A_P/B_P)-d log(2d)]/[2(2d-1)].   (14)

The original discriminant and width cost are retained.
A positive or large unnormalized average A_P alone is not enough to make this lower bound positive.
The standard p-adic floor, the quarter of nonzero signs, or finite sign orthogonality does not remove B_P or d log(2d).
No covariance/packet feasibility or actual field-norm product is inferred from averaging these matrix determinants.

<a id="exact-hand-controls-and-scope"></a>
## 6. Hand controls and precise outcome

For the actual reciprocal P=t^2-3t+1 from C152, q=-2+6t and z=3t^3-7t^2+3t.
Formula(6) gives r=2t, Q_P=61, hence A_P=65.
Formula(10) gives B_P=89.
For the four sign choices(epsilon0,epsilon1)=(+,+),(-,-),(+,-),(-,+), direct2 by2 determinants give respectively -3,1,-9,-13; their squared average is65.
The corresponding coefficient Gram determinants are83,11,179,83, whose average is89.
This checks both orientations and the FREE-versus-reduced representative boundary without a native program.
All four matrices here are nonzero, stronger than the general quarter bound but not used to extrapolate it.

For the actual golden unit P=t^2-t-1, q=t and z=t^3-t-1.
Here r=-1, Q_P=5, A_P=6 and B_P=10.
Both inputs are fixed positive-measure controls, not near-one sequences.
No numerical root approximation, finite coefficient scan or program output is used.

The exact full-family average has therefore been reduced to original coefficient data with its matching full cost, and a fixed positive fraction of actual nonzero determinant labels is proved.
A uniform gain would still require a genuinely new lower estimate for the combination Delta_P A_P/B_P in(14), or a different analytic return.
This round neither assumes that such an estimate follows from small m nor packages its absence as a new bounded-complexity theorem.
The old projection boundary remains, but the entire sign family is now explicit rather than an unexamined2^d search.

<a id="composition-frequency-calibration"></a>
## 7. Conditional composition calibration with the full original costs

Root subsequently supplied a substantive calibration lead: consider an ACTUALLY irreducible P(t)=P0(t^N), N>=3, and check that its numerator stays bounded while its averaged coefficient cost grows linearly in N.
This section verifies that lead, pays the discriminant/window return, and reuses L4's existing composition identities.
It does not assert that a fixed P0 admits infinitely many irreducible compositions.

Write P0=t^e+sum_(j=0)^(e-1)a_j t^j, e>=2, a0=c0=+/-1, d=Ne.
Irreducibility and nontorsion of P imply those properties for P0.
Denote the corresponding base remainders by rho_(2,0), r0 and the base FREE polynomial by z_base=sum_(k=0)^(2e-1)b_k t^k.
Substituting into the exact remainder division gives

    rho_(2,P)(t)=rho_(2,0)(t^N),
    z_P(t)=z_base(t^N),
    r_P(t)=t^(N-1)r0(t^N).                            (15)

The first line follows because the substituted remainder has degree <Ne, so it is the actual original remainder.
The final shift leaves the coefficient 2-norm unchanged.
Since N>=3, the coefficients c1,c2,c_(d-2),c_(d-1) all vanish: none of those indices is a multiple of N.
There is no d=2 or d=3 boundary collision because d>=6.
Therefore put

    A_*=(a0+1)^2+3 sum_(j=1)^(e-1)a_j^2+||r0||_2^2,
    L_*=2+b0^2+sum_(k=e+1)^(2e-1)b_k^2 >=2,
    J_*=sum_(j=1)^(e-1)a_j^2+sum_(k=1)^e b_k^2 >=0.

Then the exact full-family ratio is

    A_P=A_*,       B_P=Ne L_*+J_*,
    A_P/B_P=A_*/(Ne L_*+J_*).                         (16)

For a fixed base this decays as 1/N along any unbounded sequence of admissible N; no existence of such a sequence is part of the statement.
This is a calibration of the unprocessed diagonal-sign family, not a counterexample to all possible certificates or to a method that first strips a legal composition.

To retain the actual original degree cost, reuse L4's composition formulas (also obtained directly from P'(alpha)=N alpha^(N-1)P0'(alpha^N) and separation into exponent residue classes):

    Delta_P=N^(Ne) Delta_0^N,
    G_(2Ne)(P)=G_(2e)(P0)^N,
    m(P)=m(P0).                                      (17)

The absolute unit constant term removes the factor product|alpha|^(N-1) in the discriminant.
The Mahler identity follows by grouping the N roots above each base root; their products of max(1,|alpha|) equal max(1,|beta|).
Inserting (16)--(17) into the FULL bound (14), rather than ignoring the discriminant, yields

    m(P0)>=[N(log Delta_0-e log(2e))
                    +log A_*-log(Ne L_*+J_*)]/[2(2Ne-1)].       (18)

Thus the d log N from the composition discriminant exactly cancels the corresponding part of the original d log(2d) penalty.
Along an unbounded admissible sequence the right side tends to [log Delta_0-e log(2e)]/(4e); it need not tend to zero and is not claimed positive.
The average numerator's additional logarithm contributes only o(1) to that return.

One can also see the lost orbit information exactly.
The normalized projection fraction for the full average is

    (A_P/B_P)/G_(2Ne)(P)
           =A_*/[(Ne L_*+J_*)G_(2e)(P0)^N].           (19)

Here G_(2e)(P0)>=e+1: its orbit matrix contains I_e and e further nonzero integer columns; Cauchy--Binet includes the identity minor and all one-column replacements, contributing at least 1+e.
Hence (19) has exponential loss in N for a fixed base whenever unbounded admissible compositions exist.
This quantifies the specific averaged projection, while L4's FULL Gram scales by the exact power in (17).
No term in (18)--(19) removes or changes the original polynomial's multiplicities or degree.

Contribution boundary: root supplied the specific diagonal-sign family, p=2 focus and complete-square-average research question, and later the substantive constant-numerator/linear-cost composition calibration lead used in Section 7.
The cofactor/path reduction, formulas (3)--(14), quarter nonzero count, exact paired coefficient-volume formula and hand controls are this author's new deductions; this author also checked the composition lead and derived its explicit entropy return and averaged projection loss (18)--(19).
The inherited C152/C50/L4/L56/L223/L234 results keep their actual earlier authorship and review limits.
No new external theorem, native computation, independent review or G0001 completion is claimed.

<a id="author-freeze-2026-10-16"></a>
## Author freeze and actual self-check

2026-10-15T16:28.
The entire statement and Sections 1--7, formulas (1)--(19), are author-complete and frozen for fixed retention and separate whole independent review.
The author recomputed the cofactor sign, the d=2 and d=3 character collisions, original versus right-multiplied coefficient matrices, nonzero sign count, both full averages, raw-prime cancellation, both hand controls, and the conditional composition discriminant/window return.
The actual C152 selected whole-reviewed decision and the exact L4/L56 inputs were checked.
The bounded material structure check returned checked1; it is not mathematical or independent review.
No new program or numerical experiment was executed.
Later mathematical changes require the responsible author/reviewer coordination rather than silently changing this frozen account.

## Current assessment
[Selected decision](#decision-current-isolated-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T16:29 |
| status | open |
| reason | Fix the entire complete diagonal-sign determinant and coefficient-volume calculation, quarter nonzero count, exact paid Gram/entropy return and conditional irreducible-composition calibration for whole independent review. Root and g_bridge_audit are new proof contributors. The result replaces an unexamined finite family by exact original coefficient formulas; it does not supply a new prime-valuation floor, uniform arithmetic coverage or unrestricted gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete sign-family statement](#statement) | All original nontorsion integer units, every one of the2^d signs including singular labels, exact matching averages, nonzero count, paid return and actual conditional compositions. |
| argument | [Whole seven-section proof](#argument) | All19 formulas, original cofactor/character signs and d2/d3 boundaries, free versus reduced coefficients, entire cost and composition accounting. |
| dependency | [Accepted integer lift interface](Yin_C_G0152_v1.md#canonical-lift-rank-one) | Actual companion convention, original divided remainder, canonical lift and affine integer perturbation; reconstructed locally without a good-prime restriction. |
| dependency | [Actual free coefficient window](Yin_C_G0152_v1.md#full-original-coefficient-window) | Exact N=2d free polynomial columns, image matrix and mandatory prime scaling, not the same coefficients as the reduced representative. |
| dependency | [Original projection inequality](../ledger/Yin_L_G0056_v1.md#projection-cost-identity) | Full matched image determinant and coefficient Gram cost, including zero-image boundaries, and exact original-window return. |
| dependency | [Original Gram entropy bound](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate) | Actual discriminant, original degree, window2d and d log(2d) penalty in the complete entropy inequality. |
| dependency | [Existing composition identities](../ledger/Yin_L_G0004_v1.md#degree-window-tests) | Original Mahler measure, composition discriminant and full orbit-Gram power, under actual supplied irreducibility; no infinite-family existence asserted. |
| support | [Finite Boolean characters](../ledger/Yin_L_G0223_v1.md#partial-mask-collision-information-retention) | Existing independent-sign/character convention; the needed finite orthogonality and exact collisions are proved locally. |
| support | [Earlier Walsh attribution](../ledger/Yin_L_G0234_v1.md#walsh-companion-ratio-construction) | Bounded reuse/attribution only, without importing packet feasibility or original-law conclusions. |
| support | [Earlier finite-sign mechanism](Yin_C_G0050_v1.md#statement) | General finite sign averaging is not new; the specified Frobenius determinant and matching full-volume averages are the present deductions. |

### Decision current-scalar-gram-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:39 |
| status | proved |
| reason | Select C209 as the current responsible home of the identical retained L4 scalar Gram certificate and composition identities at the two exact anchors below. Its actual statement, saturated-kernel/dual-Gram/Vandermonde proof and full original composition/discriminant costs were read at the used scopes. Mathematical status, statement, complete argument, selected R517 and all relation scopes are inherited unchanged; R517 now declares unknown initial context and no new mathematical or independent review is claimed. The older dated decisions and R517 retain their actual original L4 inputs, fields and dates. This locator maintenance preserves the paused round and supplies no new research or Task authority. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete sign-family statement](#statement) | All original nontorsion integer units, every one of the2^d signs including singular labels, exact matching averages, nonzero count, paid return and actual conditional compositions. |
| argument | [Whole seven-section proof](#argument) | All19 formulas, original cofactor/character signs and d2/d3 boundaries, free versus reduced coefficients, entire cost and composition accounting. |
| dependency | [Accepted integer lift interface](Yin_C_G0152_v1.md#canonical-lift-rank-one) | Actual companion convention, original divided remainder, canonical lift and affine integer perturbation; reconstructed locally without a good-prime restriction. |
| dependency | [Actual free coefficient window](Yin_C_G0152_v1.md#full-original-coefficient-window) | Exact N=2d free polynomial columns, image matrix and mandatory prime scaling, not the same coefficients as the reduced representative. |
| dependency | [Original projection inequality](../ledger/Yin_L_G0056_v1.md#projection-cost-identity) | Full matched image determinant and coefficient Gram cost, including zero-image boundaries, and exact original-window return. |
| dependency | [Original Gram entropy bound](Yin_C_G0209_v1.md#gram-lower-certificate) | Actual discriminant, original degree, window2d and d log(2d) penalty in the complete entropy inequality. |
| dependency | [Existing composition identities](Yin_C_G0209_v1.md#degree-window-tests) | Original Mahler measure, composition discriminant and full orbit-Gram power, under actual supplied irreducibility; no infinite-family existence asserted. |
| support | [Finite Boolean characters](../ledger/Yin_L_G0223_v1.md#partial-mask-collision-information-retention) | Existing independent-sign/character convention; the needed finite orthogonality and exact collisions are proved locally. |
| support | [Earlier Walsh attribution](../ledger/Yin_L_G0234_v1.md#walsh-companion-ratio-construction) | Bounded reuse/attribution only, without importing packet feasibility or original-law conclusions. |
| support | [Earlier finite-sign mechanism](Yin_C_G0050_v1.md#statement) | General finite sign averaging is not new; the specified Frobenius determinant and matching full-volume averages are the present deductions. |
| review | [Actual whole finding](../audits/reviews/Yin_R_G0796_v1.md#diagonal-sign-frobenius-whole-independent-finding) | Complete seven sections/nineteen formulas, both controls including zero-cost labels, exact original means/ratios/window/discriminant/composition expenses and source/contribution limits. |


### Decision current-joint-minor-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:52 |
| status | proved |
| reason | Select C226 as the complete current home of the identical retained L55/L56 coefficient-space comparison and full original fixed-window projection/lift proofs at the exact anchors below. The complete argument, scalar/rank domains and actual current statement were read; mathematical status, own proof and selected finding remain. This is routine same-content interface adoption, not a new proof or independent review. Original dated decisions and R bindings keep their actual L inputs. The zero-image inequality is already local in C154; no undefined zero-determinant ratio is imported from C226's full-rank identity. The current C209 Gram/composition homes remain selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All original nontorsion integer units, every one of the2^d signs including singular labels, exact matching averages, nonzero count, paid return and actual conditional compositions. |
| argument | [Argument](#argument) | All19 formulas, original cofactor/character signs and d2/d3 boundaries, free versus reduced coefficients, entire cost and composition accounting. |
| dependency | [Dependency](Yin_C_G0152_v1.md#canonical-lift-rank-one) | Actual companion convention, original divided remainder, canonical lift and affine integer perturbation; reconstructed locally without a good-prime restriction. |
| dependency | [Dependency](Yin_C_G0152_v1.md#full-original-coefficient-window) | Exact N=2d free polynomial columns, image matrix and mandatory prime scaling, not the same coefficients as the reduced representative. |
| dependency | [Dependency](Yin_C_G0226_v1.md#projection-cost-identity) | Full matched-image determinant/coefficient-Gram inequality at the original fixed window; apply the full-rank projection identity for nonzero determinants and C154's locally proved trivial inequality at zero images, without a zero-denominator ratio. |
| dependency | [Dependency](Yin_C_G0209_v1.md#gram-lower-certificate) | Actual discriminant, original degree, window2d and d log(2d) penalty in the complete entropy inequality. |
| dependency | [Dependency](Yin_C_G0209_v1.md#degree-window-tests) | Original Mahler measure, composition discriminant and full orbit-Gram power, under actual supplied irreducibility; no infinite-family existence asserted. |
| support | [Support](Yin_C_G0534_v1.md#partial-mask-collision-information-retention) | Existing independent-sign/character convention; the needed finite orthogonality and exact collisions are proved locally. |
| support | [Support](Yin_C_G0573_v1.md#walsh-companion-ratio-construction) | Bounded reuse/attribution only, without importing packet feasibility or original-law conclusions. |
| support | [Support](Yin_C_G0050_v1.md#statement) | General finite sign averaging is not new; the specified Frobenius determinant and matching full-volume averages are the present deductions. |
| review | [Review](../audits/reviews/Yin_R_G0796_v1.md#diagonal-sign-frobenius-whole-independent-finding) | Complete seven sections/nineteen formulas, both controls including zero-cost labels, exact original means/ratios/window/discriminant/composition expenses and source/contribution limits. |


### Decision current-isolated-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:29 |
| status | proved |
| reason | Adopt the current isolated whole statement/argument review in R796 after direct mathematical initial judgment and subsequent complete comparison of the original findings. The new finding is independently reviewed and the complete superseded original account retains its actual unknown relationship, date, bindings, source depth and limitations in that R. Preserve the exact statement, complete argument, proved status, every selected support/dependency and its scope, all prior decisions and all fixed mathematics. No historical relationship is promoted, original external proof or native computation is newly certified, unrestricted coverage or Task completion is inferred, or stopped research resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All original nontorsion integer units, every one of the2^d signs including singular labels, exact matching averages, nonzero count, paid return and actual conditional compositions. |
| argument | [Argument](#argument) | All19 formulas, original cofactor/character signs and d2/d3 boundaries, free versus reduced coefficients, entire cost and composition accounting. |
| dependency | [Dependency](Yin_C_G0152_v1.md#canonical-lift-rank-one) | Actual companion convention, original divided remainder, canonical lift and affine integer perturbation; reconstructed locally without a good-prime restriction. |
| dependency | [Dependency](Yin_C_G0152_v1.md#full-original-coefficient-window) | Exact N=2d free polynomial columns, image matrix and mandatory prime scaling, not the same coefficients as the reduced representative. |
| dependency | [Dependency](Yin_C_G0226_v1.md#projection-cost-identity) | Full matched-image determinant/coefficient-Gram inequality at the original fixed window; apply the full-rank projection identity for nonzero determinants and C154's locally proved trivial inequality at zero images, without a zero-denominator ratio. |
| dependency | [Dependency](Yin_C_G0209_v1.md#gram-lower-certificate) | Actual discriminant, original degree, window2d and d log(2d) penalty in the complete entropy inequality. |
| dependency | [Dependency](Yin_C_G0209_v1.md#degree-window-tests) | Original Mahler measure, composition discriminant and full orbit-Gram power, under actual supplied irreducibility; no infinite-family existence asserted. |
| support | [Support](Yin_C_G0534_v1.md#partial-mask-collision-information-retention) | Existing independent-sign/character convention; the needed finite orthogonality and exact collisions are proved locally. |
| support | [Support](Yin_C_G0573_v1.md#walsh-companion-ratio-construction) | Bounded reuse/attribution only, without importing packet feasibility or original-law conclusions. |
| support | [Support](Yin_C_G0050_v1.md#statement) | General finite sign averaging is not new; the specified Frobenius determinant and matching full-volume averages are the present deductions. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0796_v1.md#fresh-c0154-whole-finding) | Entire exact current statement and complete retained argument, every finite/conditional/asymptotic scope, decisive direct input interfaces, controls, original arithmetic costs and source/negative/execution limitations. Current isolated whole review after fixed-input initial judgment, with complete original unknown account preserved separately in the same R; no mathematical repair or scope enlargement. |

## Historical assessments

<a id="decision-whole-reviewed-2026-10-16"></a>

### Historical assessment whole-reviewed-2026-10-16

| Field | Value |
| --- | --- |
| date | 2026-10-15T16:41 |
| status | proved |
| review-status | independently reviewed |
| reason | Adopt the complete diagonal-sign determinant/volume averages after R517 whole independent review. Exact original coefficient formulas, a quarter nonzero fraction, matched full-average Gram/entropy return and actual conditional composition calibration are proved with all original costs. The mandatory prime factor still cancels, and no uniform arithmetic coverage or unrestricted G0001 gap follows. This adoption closes the assigned round under Yin's instruction to organize progress and pause. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete sign-family statement](#statement) | All original nontorsion integer units, every one of the2^d signs including singular labels, exact matching averages, nonzero count, paid return and actual conditional compositions. |
| argument | [Whole seven-section proof](#argument) | All19 formulas, original cofactor/character signs and d2/d3 boundaries, free versus reduced coefficients, entire cost and composition accounting. |
| dependency | [Accepted integer lift interface](Yin_C_G0152_v1.md#canonical-lift-rank-one) | Actual companion convention, original divided remainder, canonical lift and affine integer perturbation; reconstructed locally without a good-prime restriction. |
| dependency | [Actual free coefficient window](Yin_C_G0152_v1.md#full-original-coefficient-window) | Exact N=2d free polynomial columns, image matrix and mandatory prime scaling, not the same coefficients as the reduced representative. |
| dependency | [Original projection inequality](../ledger/Yin_L_G0056_v1.md#projection-cost-identity) | Full matched image determinant and coefficient Gram cost, including zero-image boundaries, and exact original-window return. |
| dependency | [Original Gram entropy bound](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate) | Actual discriminant, original degree, window2d and d log(2d) penalty in the complete entropy inequality. |
| dependency | [Existing composition identities](../ledger/Yin_L_G0004_v1.md#degree-window-tests) | Original Mahler measure, composition discriminant and full orbit-Gram power, under actual supplied irreducibility; no infinite-family existence asserted. |
| support | [Finite Boolean characters](../ledger/Yin_L_G0223_v1.md#partial-mask-collision-information-retention) | Existing independent-sign/character convention; the needed finite orthogonality and exact collisions are proved locally. |
| support | [Earlier Walsh attribution](../ledger/Yin_L_G0234_v1.md#walsh-companion-ratio-construction) | Bounded reuse/attribution only, without importing packet feasibility or original-law conclusions. |
| support | [Earlier finite-sign mechanism](Yin_C_G0050_v1.md#statement) | General finite sign averaging is not new; the specified Frobenius determinant and matching full-volume averages are the present deductions. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0796_v1.md#diagonal-sign-frobenius-whole-independent-finding) | Complete seven sections/nineteen formulas, both controls including zero-cost labels, exact original means/ratios/window/discriminant/composition expenses and source/contribution limits. |
