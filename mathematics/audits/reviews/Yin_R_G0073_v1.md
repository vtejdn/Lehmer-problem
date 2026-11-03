---
author: Yin
---

# Retained project review: Salem dyadic energy, the plastic-family resultant and doubling-auxiliary universality

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0174_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="salem-phase-mixed-local-review"></a>

### Separate complete local review

On 2026-10-10 the coordinating AI for Yin read the complete Sections 1--3 and scope discussion, inspected all three J30 programs, and actually reran all three with their output destination redirected to disposable local files.
Every retained mathematical JSON field matched, with the execution timestamp excluded.
The author outputs were left unchanged.
The reviewer assigned the broad high-band question and received progress explanations but supplied no formula, residue certificate, phase-map argument or program in this round.
This was separately organized and nonblind.
No mathematical defect was found in the stated scope.

The reviewer counted all ordered unit/exceptional root pairs in (2), checked the signs and factor two in the absolutely summable correction, and recomputed the positive-Salem radial term (3d-2)m.
Nonvanishing of the full cross-power resultant and its 2^d floor are reused at L59's actual-root, full-multiplicity scope.
Thus the Abel correlation exists for each fixed input, and (4) is the existing resultant floor transferred exactly, with no added arithmetic income.
This result is restricted to one positive Salem exterior pair.

The fixed family interfaces in L38/L131/L137 were checked for N=9 modulo120, N>=129, irreducibility without a cyclotomic factor, the actual degree N+3, and the distinct fixed positive limiting measure.
The reviewer verified g's one-inside/two-inside zero-pole count and winding -1, the smooth periodic lifted phase, monotone phase quantization for sufficiently large N, and the O(1) smooth-test sum error.
The exact relation zeta^N=g(zeta) is essential to (8); a moving Fourier character is not inserted directly into weak convergence.
The exceptional-pair O(d) bound and the conversion N to d=N+3 justify (9) and the O(1) remainder in (15).

At infinity g tends to one, so the residue of g^k/z there is -1; theta is its only exterior finite pole.
The reviewer expanded numerator and denominator at theta to check every term of (11), the finite coefficient extraction, and the exact field/root-isolation arithmetic underlying (12)--(14).
The exact rerun reproduced all reduced coefficients and rational sign intervals.
The Arb rerun reproduced all32 moments and16 dyadic products.
The finite-input program's sparse Newton recurrence has the correct j<k and k<=d cases, the exact rational polynomial sign formula retains all six coefficients, and its narrow exterior-root bracket uses the already established Salem uniqueness.
The interval subtraction controls the large cancellation in the actual n=516 and1032 sums.
Its output and pair-type consistency comparison were reproduced.

These are a complete written mathematical review and a rerun of author programs, not an independently written computational implementation or a formal proof-assistant check.
The fixed family proof and older accepted resultant inputs were reused, not newly reproved.
The evidence supports the exact damping identity and the single positive degree-scale contribution.
It does not lower-bound a full signed sum from one term, commute the infinite series and degree limit, or establish a near-one estimate.
Later substantive changes are not covered automatically.

<a id="plastic-resultant-independent-review"></a>

### Separate complete noncontributor review

On 2026-10-10 the assigned orbit_research AI for Yin independently checked the complete statement and equations(1)--(15), the retained input interfaces, and every line of J35's verify.py together with its readme and verification.json.
The reviewer supplied none of the resultant reductions, limit expressions, phase-moment formulas or numerical program.
It had shared project context and a requested review checklist; this is separately organized noncontributor review, not blind or human review.
No mathematical defect was found.
One inaccurate reuse statement was found and corrected by the coordinator before this final review: the first identity of(4) already appears verbatim in L38's odd-order elimination row.
The reviewer directly confirmed the revised equation introduction and reuse/contribution paragraphs.
They now identify the rediscovery, retain the history of the erroneous absence claim, and separate the full resultant/energy deductions from that older identity.
The reviewer made no changes to the author's mathematical proof.

The exact algebraic check retained every sign and multiplicity.
On the actual progression d_N=N+3 is even; hence the switches between Res(P_N,f), Res(f,P_N), and the substituted-versus-powered resultant introduce the displayed positive signs.
Direct expansion verifies both identities in(4).
At a root u of f the equality h(u)=-u(u+1), together with the two unit products, gives Res(f,h)=-1 and then Res(f,L)=Res(L,f)=1.
Thus f does not vanish at a P_N root, its squared denominator in(7) has norm one, and the factor z also has norm one.
Evaluation at every L root gives the factorization z^8 f(z)(z^q+1) with no omitted resultant factor.
All powered conjugates retain their multiplicities; no minimal-polynomial degree preservation assumption is used.
The actual two positive real roots and four nonreal conjugate pairs of L prove positivity of the final plus-cyclic resultant, while its nontorsion irreducibility proves nonvanishing.

The reviewer read the fixed family conditions in L38/L131 and distinguished the progression's actual irreducible degree from the fixed residual degree ten.
N>=129 satisfies the separate N>=16 root bound; the N=9 computational control is used only for the exact polynomial identity.
The actual Dim16-U001 all-index interface was read in full.
For the fixed polynomial L its degree, unit, nontorsion and 0<mu<1 hypotheses hold, so a single fixed logarithmic-form constant applies to C_q and C_(2q) for every q.
Subtracting their upper and lower bounds gives exactly(11).
This reuse retains the source unit's external Baker--Wustholz statement boundary, uncalibrated constant and separately guarded exponent-one case.
It does not substitute L168's degree-linear exponent restriction or assert a new audit of the original transcendence proof.

The conversion to energy was checked against D29's exact damping identity and its retained review.
The identity is applied to each fixed input before any degree limit, so no interchange of an Abel limit and N tending to infinity is needed.
Here q=d_N-11, the explicit correction is bounded, and the family equation with f'(t)>=3theta^2-1 and -h(t)<=85/27 gives the stated exponential approach to theta.
Therefore the replacement of (3d_N-2)m_N by 3d_N log(theta) has only a bounded error, and the fixed cyclic-norm O(log q) error gives(13).
The ratio bound351/350 follows from the exact retained root intervals and proves positivity independently of decimal output.

For(15), the reviewer read D29's complete phase-moment and fourth-mode derivation, its exact c_4,c_8 expressions, and the recorded independent verification.
Those retained expressions and the complete fixed-input Abel identity are the inputs used here; the older J30 programs were not rerun in this review.
The positive removed contribution is -C_(4N)/(4N), so adding C_(4N)/(4N) has the correct sign.
Taking the difference of the two proved quantities yields kappa-gamma.
This proves the total contribution of the other modes without summing limits of individual modes.
It supplies no positivity of every mode, near-one estimate or variable-input uniformity.

The J35 implementation was checked as an exact finite and validated-constant control.
For even-degree P(z)=E(z^2)+zO(z^2), E(t)^2-tO(t)^2 equals the monic full squared-root polynomial because P(sqrt(t))P(-sqrt(t))=product_i(t-alpha_i^2) in even degree.
Thus its direct resultant check does not define the left side through the reduction under test.
The remainder reductions modulo monic L preserve evaluation at all L roots.
The two finite controls check the unit factors, positivity and C_(2q)=C_q A_q exactly; only N=9 additionally checks the larger substitution resultant, as disclosed.
Exact rational Horner signs and bisection enclose theta and lambda; retained uniqueness identifies the intended roots.
Arb receives exact rational center/radius enclosures and propagates uncertainty through the logarithms and c_4,c_8 expressions.
The strict rational comparisons certify(14)--(15).
The overlapping alternative kappa enclosure is only a consistency check; its exact equality is supplied by theta^3=theta+1 in the written proof.

This review did not rerun J35 or create an independent verifier.
It checked the full implementation and retained output, while the coordinator's separately recorded successful rerun remains the actual repeated-execution evidence.
The finite resultants and validated constants are not used to extrapolate an all-index theorem.
With the corrected reuse record, the whole stated derivation has no outstanding review defect.
It proves the complete signed-energy limit for this fixed-positive-measure primitive family and the stated benchmark on any bound covering it.
It does not prove a uniform near-one estimate, controlled auxiliary cofactor costs, or completion of G0001.
Fixed retention and Claim adoption remain separate coordinator actions.

<a id="doubling-auxiliary-universality-independent-review"></a>

### Separate complete noncontributor review

On 2026-10-10 the assigned orbit_research AI for Yin independently read and checked the complete final statement and Sections1-5, including the later content-normalization guard.
The reviewer supplied none of the construction, functional equation, evaluations or height arguments.
It had shared project context and received the coordinator's requested checklist, so this was separately organized noncontributor review, not a blind or human review.
No mathematical defect was found.
The earlier opening terminology was clarified by the author before this final review: the plastic identity has unnormalized numerator 2tL and normalized G_f=tL.
The reviewer did not alter the author's mathematical proof.

The review read L59's actual full-powered polynomial convention, the nonzero mixed-resultant assertion for distinct positive exponents, and the prime-power Frobenius floor at their retained scope.
The hypotheses here imply even d: a reciprocal odd-degree polynomial has -1 as a root, contradicting the present irreducible nontorsion domain.
Consequently the complete squared-root multiset has degree d and constant coefficient1 and is closed under inversion, even when different conjugates have the same square.
L59 applies to Res(P,P^[2]) with every multiplicity retained, so R is nonzero and divisible by 2^d.
No assumption that alpha^2 has degree d was introduced, and the prior source proof was not re-audited as a new external theorem.

For the integral construction, the reviewer checked the coefficient map (A,B) -> AP+BQ from two degree-less-than-d spaces to degree-less-than-2d polynomials.
Its integral Sylvester determinant is the signed resultant up to the stated basis convention.
The adjugate applied to the constant coefficient vector therefore supplies exactly R on the right of(3), after a common sign adjustment, rather than an unspecified rational denominator.
The two reductions in(5) and the degree bound2d+1 follow directly from(4).
Nonzero R and f(alpha)=R alpha ensure f is nonzero; they also force k>=1 because alpha has degree at least2.

The four evaluations at alpha, alpha^(-1), alpha^2 and alpha^(-2) were checked with the actual degree k of f.
In particular f(0) is allowed to vanish: f* may then have degree less than k, but the identities f*(alpha)=alpha^k f(alpha^(-1)) and f*(alpha^2)=alpha^(2k)f(alpha^(-2)) remain exactly valid.
They give the two cancelling terms R^3 alpha^(2k-2)(alpha^4-1) with opposite signs.
The characteristic-two calculation makes G_f integral for every integer f, independently of this cancellation.
Irreducibility and then monic division justify P|G_f in Z[t].

The nonvanishing argument retains rational functions and possible poles at zero correctly.
If G_f vanished identically, division by the nonzero f(t)^2 f(t^2) gives r(t^2)=-r(t)^2.
For s=-r, the Laurent order j can be any integer.
The leading coefficient equation forces c=1, and the least positive higher-order term would have coefficient2a only on the squared side.
Thus the normalized Laurent series is identically1 and s=t^j as a rational identity.
Evaluating r at alpha is legitimate since f(alpha) is nonzero; it would force a nonzero power of alpha to be -1, or1=-1 in the zero-exponent case.
This proves that the constructed auxiliary is not the zero polynomial.

The reviewer also checked formal reciprocity at length4k, including the possible initial and final coefficient cancellations.
For a nonzero formally reciprocal polynomial the least exponent ell pairs with greatest exponent4k-ell; dividing by t^ell gives actual reciprocal degree4k-2ell.
The constant coefficient of P is one, so no target factor is lost in removing that monomial.
These facts give the asserted degree bound8d+4 without assuming that f or G_f is monic or primitive.

Finally, Section5's height bound uses the actual polynomial after all cancellations.
Applying the maximum-modulus principle to z^k f(1/z) gives ||f||_circle >= |R||alpha|^(1-k) for |alpha|>=1.
Since |alpha|<=M(P), k-1<=2d and ||f||_circle<=(k+1)H(f), equation(6) follows with the stated denominator.
A unit-circle conjugate supplies the stronger direct evaluation bound.
For content c, f_0(alpha)/alpha is an algebraic integer precisely because alpha is a unit; its rational value R/c must therefore be an integer.
The auxiliary scales cubically, remains integral by the same characteristic-two calculation, and stays nonzero and divisible by P after primitive normalization.
The review confirms that the resultant floor does not automatically survive in D=R/c, and that neither height bound controls Mahler measure or the complementary factor's measure.

This complete written review used no new computation, finite scan, source acquisition or proof-assistant check.
It supports factor universality and the carefully delimited unnormalized height statement.
It does not establish controlled primitive height, a cyclotomic cofactor, bounded complementary Mahler cost, a near-one exclusion or completion of G0001.
Fixed retention or Claim adoption remains the coordinator's separate action.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete Salem identity and phase-moment finding](#salem-phase-mixed-local-review) | [Exact damping identity](../../ledger/Yin_L_G0174_v1.md#salem-exact-damped-mixed-identity) | Entire original D29 Section1, all root-pair types, Abel existence, explicit correction and exact radial/resultant transfer; positive Salem domain and retained full-resultant input. |
| [Complete Salem identity and phase-moment finding](#salem-phase-mixed-local-review) | [Primitive phase moments](../../ledger/Yin_L_G0174_v1.md#primitive-plastic-phase-moments) | Entire original D29 Sections2--3, primitive family conditions, phase quantization, fixed-k moving-frequency limit, residue and exact c4/c8 calculation, stated actual finite control; the recorded three author-program reruns are not independently written verifiers. |
| [Complete Salem identity and phase-moment finding](#salem-phase-mixed-local-review) | [fourth-mode certificate](../../ledger/Yin_L_G0174_v1.md#plastic-fourth-mode-certificate) | Entire original D29 Sections2--3, primitive family conditions, phase quantization, fixed-k moving-frequency limit, residue and exact c4/c8 calculation, stated actual finite control; the recorded three author-program reruns are not independently written verifiers. |
| [Complete plastic-resultant finding](#plastic-resultant-independent-review) | [Complete resultant and energy argument](../../ledger/Yin_L_G0174_v1.md#retained-plastic-resultant-argument) | Entire original D38 equations(1)--(15), fixed-family hypotheses, every resultant factor/sign/multiplicity, accepted fixed-L all-index input, energy/error/cancellation limits, entire J35 code and retained output, and verified closure of the reuse correction; no new rerun or external proof audit. |
| [Complete doubling-universality finding](#doubling-auxiliary-universality-independent-review) | [Factor-universality argument](../../ledger/Yin_L_G0174_v1.md#doubling-auxiliary-factor-universality) | Entire original D39 statement and Sections1--5: full powered polynomial, integer Bezout scalar, degree and actual-degree reversal, nonzero rational-functional-equation argument, reciprocal monomial removal, unnormalized height and primitive-content boundary; later L38/L139 reuse clarification is excluded from this earlier review. |
| [Original complete collaborator finding](#plastic-resultant-original-collaborator-check-finding) | [Original complete plastic-resultant proof](../../ledger/Yin_L_G0174_v1.md#retained-plastic-resultant-argument) | Actual original2026-10-10day-precision coordinator whole proof/equations(1)--(15), exact fixed-family/all-index source and D29 inputs, every J35 program line and retained mathematical output field plus redirected author-program rerun; known earlier contribution of the limiting expression makes this self-reviewed. Its original reuse correction and stated native/source boundaries remain exact. |
| [Original complete author finding](#doubling-universality-original-author-check-finding) | [Original complete doubling-universality statement/proof](../../ledger/Yin_L_G0174_v1.md#doubling-auxiliary-factor-universality) | Actual original2026-10-10day-precision complete coordinator-author self-check of the final statement/Sections1--5, full powered multiset/integral Bezout/vanishing/nonzero/reversal and height/content guard; the later L38/L139 reuse clarification is outside this original whole scope. |

## Review relationships

The entire original mathematical account, every date/precision, verdict, source/native depth and all five original binding rows above remain unchanged.
These declarations record the actual arrangements; they perform no new historical review, source reading or native rerun.

The original D29 whole finding records a separately organized nonblind coordinator inspection and three actual redirected reruns of fully read author programs.
The coordinator assigned the broad question and received progress explanations, but their actual target-mathematical content and the initial review arrangement are not preserved.
The absence of a supplied formula/program does not establish either initial isolation or prior substantive mathematical sharing.
Necessary fixed family and full-resultant inputs are ordinary inspected interfaces, not automatic evidence of a new-target contribution.
The entire positive-Salem identity/Abel/radial transfer, primitive family/phase quantization/moving-frequency/residue/sign/actual finite-control target therefore remains unknown for independent-review purposes.

The original D38 whole finding records shared project context and a requested checklist, without establishing their actual initial target-mathematical content.
Its complete equations(1)--(15), source specialization, all J35 code and output, and closure of the inaccurate reuse statement remain at the stated scope.
The false absence claim concerned the already retained first identity, and the original final whole account explicitly includes confirmation of the corrected introduction and reuse/contribution paragraphs without changing the mathematical proof.
That actual correction and reread do not create a further whole repaired-proof inspection.
The D38 whole noncontributor relationship remains unknown.

The original D39 whole finding likewise discloses shared project context and a checklist without establishing its actual pre-review mathematical content or initial isolation.
Its complete final statement/Sections1--5 and content guard remain intact.
The unnormalized numerator2tL versus normalized G_f=tL terminology was clarified before that final review, without a mathematical proof change.
The later L38/L139 reuse clarification is explicitly excluded from the original reviewed scope.
The D39 whole noncontributor relationship remains unknown.
A noncontributor title, its original independently-checked wording, or a later self-check does not close any of these three whole unknown targets.
They remain candidates for fresh isolated coverage at their distinct complete scopes.

The original L174 also explicitly records two different complete checks with known contribution.
The coordinator checked D38 after contributing its expected limiting expression and actually reran J35.
The coordinator authored and self-checked the complete D39 direct proof.
The following findings retain those actual whole self-review facts at original day precision, without inventing another old event, a finer minute, an additional D29/D38 author whole review, or later-comparison coverage.

| Review | Relationship |
| --- | --- |
| [Original complete Salem phase finding](#salem-phase-mixed-local-review) | unknown |
| [Original complete plastic-resultant noncontributor finding](#plastic-resultant-independent-review) | unknown |
| [Original complete doubling-universality noncontributor finding](#doubling-auxiliary-universality-independent-review) | unknown |
| [Original complete collaborator finding](#plastic-resultant-original-collaborator-check-finding) | self-reviewed |
| [Original complete author finding](#doubling-universality-original-author-check-finding) | self-reviewed |

<a id="plastic-resultant-original-collaborator-check-finding"></a>
## Original complete plastic-resultant collaborator check

Date: 2026-10-10.
This is the complete original collaborator account retained verbatim from L174, with its actual contributor relationship and author-program rerun depth.
It is self-reviewed, and does not establish the separately assigned whole noncontributor review's isolation.

On 2026-10-10 the coordinating AI for Yin read and checked the complete proof, all equations(1)--(15), the exact accepted Dim16-U001 source interface, the fixed L38/L131/L137 family conditions, D29's energy and fourth-mode conclusions, and the full J35 program.
No mathematical defect was found.
The coordinator had identified the expected limiting expression after receiving the author's exact reduction, so this is a complete collaborator check rather than noncontributor review of the whole result.

The check verified both integer identities in(4), all unit resultants and their signs in(5)--(9), the distinct meanings of substituting z^2 and powering all roots, and the degree-dependent signs using d_N even.
The factor z and the f denominator each have norm one and do not hide costs.
The final plus-cyclic resultant is positive by the actual two-real/eight-circle conjugate configuration of L.
The existing Dim16 unit supplies the all-index bound at fixed degree ten, positive mu<1, and its stated external Baker--Wustholz boundary.
Its quotient C_(2q)/C_q gives both logarithmic error bounds in(11); the variable exponent q is not subject to L168's degree-linear restriction here.

The conversion uses the exact finite-input Abel identity before taking N to infinity.
The elementary derivative and -h bounds on [theta,4/3] give exponentially small tau_N-theta, sufficient for the O(log N) total-energy remainder.
The positivity ratio 351/350, the distinction between full quotient income and radial subtraction, and the sign of the remaining-mode limit kappa-gamma were checked directly.
The subtraction in(15) removes the positive contribution -C_(4N)/(4N) with the displayed plus sign and does not interchange infinite sums with the degree limit.

The coordinator separately reran J35 with its output redirected to a disposable task-local directory.
Both direct complete powered-resultant checks and every exact/validated constant passed.
Every mathematical result field matched the retained author JSON; the original output was unchanged.
The review checked the even/odd construction of the full squared-root polynomial, exact remainder/resultant arithmetic, rational sign brackets, propagated Arb intervals and the use of fixed root uniqueness.
This is a rerun of the fully inspected author implementation, not a new independent verifier or a proof of the asymptotic by finite testing.
Noncontributor whole-proof review remains separately assigned; G0001 remains unresolved.

<a id="doubling-universality-original-author-check-finding"></a>
## Original complete doubling-universality author check

Date: 2026-10-10.
The following original contribution/checking account explicitly records the complete direct proof as author self-checked.
Its scope is the final statement and Sections1--5 including the content-normalization guard.
The later L38/L139 comparison is excluded, and no finer timestamp or additional check event is supplied.

The arithmetic agent supplied the special plastic auxiliary identity that motivated the question.
The coordinator alone supplied the general Sylvester/Bezout construction, its evaluations, nonvanishing proof, reciprocal-degree argument and the explicitly normalized height boundary above.
The only reused non-elementary mathematical interface is L59's already accepted full mixed-resultant nonvanishing/floor at its recorded scope; no new literature acquisition or computation is needed.
The complete direct proof has been self-checked and is ready for separately assigned noncontributor review.
