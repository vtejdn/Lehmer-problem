---
author: Yin
---

# Whole independent review of finite Fourier budgets and explicit scalar and phase cutoffs

Review act: 2026-10-28T23:53 UTC.
Human record author Yin.
A separately assigned review subagent, outside substantive development of C851, performed this initial whole review.
The assignment supplied the exact fixed artifact, its dependency locators and a checklist of its stated formulas and cases.
No proof-development dialogue, author explanation outside the fixed artifact, mutable Draft, or prior C851 review conclusion was supplied or consulted.
The reviewer contributed no proof step, repair, mathematical edit or numerical result to the candidate.
The fixed artifact's own contribution disclosures were read as part of its text.
Applicable accepted-dependency findings were compared at their recorded scopes; they do not substitute for the reconstruction below.

## Exact input and scope

The reviewed input is the complete 507-line [C851 v1](../../claims/Yin_C_G0851_v1.md#statement), dated by its [open decision](../../claims/Yin_C_G0851_v1.md#decision-finite-fourier-budget-open) at 2026-10-28T23:44.
Coverage includes Statement A--F, all FQ1--FQ7 and FQ6a, all nineteen numbered formulas, every unnumbered deduction, declared dependency/support interface and stated limitation.
No fixed Git commit was supplied; the physical version, actual dated decision and complete inspected text identify the input.
C851's currently linked D7 section was treated solely as extraction provenance and was not followed.

The directly used accepted interfaces were C137 Sections 1--2, C844's field-free ER3 calculation through ER7, C845's field-free phase margin and finite separated specialization, C848's finite support/endpoint/noncollision interfaces, C92's short-annihilator inequality and C570's exact finite-frequency modulus.
Their applicable findings in [R801](Yin_R_G0801_v1.md#g0137-m04-isolated-whole-finding), [R1064](Yin_R_G1064_v1.md#whole-scalar-energy-finding), [R1065](Yin_R_G1065_v1.md#whole-varying-seed-phase-finding), [R1068](Yin_R_G1068_v1.md#whole-finite-support-phase-finding), [R796](Yin_R_G0796_v1.md#fresh-c0092-whole-finding) and [R781](Yin_R_G0781_v1.md#fresh-whole-finding) were inspected at those interfaces and limits.
C168's finite range/Parseval/Cauchy--Schwarz calculation and C145's frequency-dimension comparison were read directly.
Their [R403](Yin_R_G0403_v1.md#projection-sobolev-whole-independent-finding) and [R356](Yin_R_G0356_v1.md#dense-kernel-whole-independent-finding) findings expressly retain unknown relationships.
This review does not upgrade those historical relationships or re-review their unrelated projection and Salem conclusions.
The elementary identities needed for C851 were independently rederived here.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole Fourier-budget finding](#whole-finite-fourier-budget-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finite-fourier-budget-finding) | [C851 complete statement](../../claims/Yin_C_G0851_v1.md#statement) | Entire A--F: real Laurent coefficient budget, true-term and mean distinction, original arithmetic setting, explicit scalar/phase cutoffs, every zero/width/sign/support/weight/window branch, sharper exception count and conditional growing-denominator consequence. |
| [Whole finding](#whole-finite-fourier-budget-finding) | [C851 complete argument](../../claims/Yin_C_G0851_v1.md#complete-argument) | Every FQ1--FQ19 formula and all intervening FQ1--FQ7/FQ6a reasoning, actual constants, all-q strict inequalities, changed norm transfer, complete scalar/phase assembly and precise source/computation/noncompletion limits. |
| [Whole finding](#whole-finite-fourier-budget-finding) | [C137 finite logarithmic certificate](../../claims/Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Sections 1--2/equations 1--7: actual constant and finite tail, original radial identities, frequency/matrix cost, nonzero integral full norm and old coefficient estimate for the optional minimum; no special seed or low-degree completion. |
| [Whole finding](#whole-finite-fourier-budget-finding) | [C844 field-free scalar margin](../../claims/Yin_C_G0844_v1.md#uniform-energy-logarithmic-margin) | ER3 through ER7 only, including endpoint variance, strong concavity and strict finite Taylor margin at the unchanged scalar parameters; no older arithmetic cutoff is applied. |
| [Whole finding](#whole-finite-fourier-budget-finding) | [C845 field-free phase statement](../../claims/Yin_C_G0845_v1.md#statement) | Statement A and actual parameters, allowed constants and signs, regularized torus margin and exact separated specialization; arithmetic Statement B at its old cutoff is not invoked. |
| [Whole finding](#whole-finite-fourier-budget-finding) | [C848 finite-support interface](../../claims/Yin_C_G0848_v1.md#statement) | A_H/E_H/W_J/Bad, good-shift coefficient identity, old cardinality bound, original true endpoints and coefficient bounds with overlap, and support-lattice criterion; no old arithmetic cutoff or comparison-class proof is imported. |
| [Whole finding](#whole-finite-fourier-budget-finding) | [C92 zero-value inequality](../../claims/Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Original positive-span rational annihilator inequality with effective support at most q^2 or 2q^2, applied before logarithmic norms. |
| [Whole finding](#whole-finite-fourier-budget-finding) | [C570 exact angular modulus](../../claims/Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c0/h0/b/epsilon, monotonicity and zero limit, negative frequencies and original powered-field repetitions, at the inherited Pri11/Dim19 statement/applicability depth. |
| [Whole finding](#whole-finite-fourier-budget-finding) | [C168 range and finite l2 mechanism](../../claims/Yin_C_G0168_v1.md#actual-cubic-l2-cost) | Section 1 range-variance identity, finite Parseval and coefficient Cauchy--Schwarz, rederived for C851's different independent-variable support; no Salem-energy theorem is imported. |
| [Whole finding](#whole-finite-fourier-budget-finding) | [C145 frequency-dimension comparison](../../claims/Yin_C_G0145_v1.md#statement) | Exact earlier bounded-range square-root frequency-dimension comparison, read with its finite-logarithm expense section; attribution rather than a new original-input certificate. |

<a id="whole-finite-fourier-budget-finding"></a>
## Whole mathematical finding

**PASS for the entire fixed Statement A--F and complete FQ1--FQ7/FQ6a argument at their declared accepted-input scopes.**
No mathematical gap requiring repair was found.
This finding supplies whole independent review evidence for a separate responsible adoption; it does not select a Claim decision or complete G0001.

### 1. Finite independent-variable coefficient estimate and actual mean

For real coefficients, the dagger operation on the torus is complex conjugation.
The coefficient-length hypothesis gives 0<=Yhat<=1, so Gammahat is a real function in [-H_J/2,0].
Integrating (X-a)(b-X)>=0 gives Var(X)<=(mean X-a)(b-mean X)<=(b-a)^2/4.
The resulting variance bound is H_J^2/16.
Finite character orthogonality gives exactly the squared l2 norm of the nonzero Laurent coefficients; no infinite Fourier expansion is required.

Each exponent of Fhat Fhat^dagger is a coordinate-unit difference.
A product of at most J such terms has integer coordinates of absolute value at most J and coordinate sum zero.
The first N-1 coordinates therefore leave at most (2J+1)^(N-1) possibilities, including zero.
Cauchy--Schwarz on the nonzero coefficients gives precisely

    (H_J/4)*sqrt((2J+1)^(N-1)-1).

For N=1 the set has only its zero frequency and the bound is exactly zero.
Sparse or negative original integer exponents do not affect this count.
Under z_i=x^(e_i), only nonzero lifted frequencies can contribute to a nonzero original frequency.
Collecting coefficients and the triangle inequality prove the asserted nonconstant l1 bound.
Lifted frequencies that collapse to zero are omitted from this inequality, so it transfers no mean identity.
C137's direct coefficient-length calculation also works for these real coefficients, validating the optional minimum with 2^J.

For the stated control, |1+x+x^2|^2 has Laurent coefficients 3,2,2,1,1 and second moment 19.
The independent-variable fourth moment is 2*3^2-3=15, while both first moments are 3.
The J=2 finite logarithm has coefficient -1/(4B^2) on the square of |F|^2.
Thus the actual-minus-lifted constant is -(19-15)/(4*100)=-1/100.
The distinction is necessary and is maintained in every later application.

### 2. Original norm, radial cost, actual constant and finite size

The unit identities sum log^+r_i=m and sum|log r_i|=2m hold over all original d conjugates.
For V_i=F(alpha_i)/max(1,r_i)^T, each radial coefficient lies in [0,1] and differs from one by at most min(1,T|log r_i|).
The derivative bound 1/(2delta) for log(t^2+delta^2)/2 therefore pays S h/delta, in addition to the exact h from normalization.
The finite logarithm majorizes the regularized logarithm in the correct upper direction.
Its original nonzero frequencies have absolute value at most JT, so the exact C570 angular estimate applies at J h without losing original powered-field repetitions.
Combining that estimate with the new nonconstant coefficient bound gives FQ5 and retains the actual circle constant c_J.

The old geometric Taylor tail is unchanged.
For the Hermitian bandwidth-T matrix on indices -JT,...,JT, every path of at most J steps from zero stays within that interval.
Consequently its central powers give the same exact constant coefficients and its full size remains 2JT+1.
No smaller matrix, new radial gain or reduced frequency cutoff follows from the new coefficient estimate.

For a nonzero algebraically integral F(alpha)/q, multiplicativity of the full degree-d signed norm gives Res(P,F)=q^d Norm(F(alpha)/q).
Its integer norm is nonzero and has absolute value at least one.
This yields the full log q floor even when the value lies outside Z[alpha].
Laurent monomial normalization preserves coefficient energy/count and circle modulus, and changes the signed norm only by a unit norm.
The zero-value and width-zero cases are kept separate from this logarithmic step.

### 3. Exact modulus and all scalar cutoff inequalities

Writing t=sqrt(v/c0) gives v=c0 t^2 and 0<t<=exp(-10).
The elementary maximum of log x/sqrt x gives t log(1/t)<=sqrt t.
Also v<=sqrt t, so b(v)<=(v/c0)^(1/4).
Since 1/8<c0<1 and v<=1, this proves epsilon(v)<=34 v^(1/8)<=q^6 v^(1/8) on its stated domain.
The independent lower estimate h0>(1/8)4^(-20)=2^(-43) is valid.

All FQ9 bounds hold for every integer q>=2.
In particular B_s<=(5/4)q^2 gives eta>=(2/25)q^(-8)>=q^(-12).
The quantity inside the scalar ceiling is exactly the integer 16q^8 B_s^5, so no rounding loss is hidden in J_s.
The inequalities 16(5/4)^5<50<=q^6 prove J_s<=q^24.
The radial factor is at most q^7; H_(J_s)<=1+24log q<=q^6 follows because q^6-1-24log q is positive at 2 and increasing thereafter.
Then 2J_s+1<=q^26 and the stated Lambda bound follow, with deliberately generous exponents.

The domain check is genuinely first: J_s u_s<=q^(24-256q^2)<=2^(-1000)<h0.
Only afterward may the modulus bound give epsilon(J_s u_s)<=q^9 u_s^(1/8).
The Fourier error is at most q^(15-19q^2)<=q^(-14), and the radial error is at most q^(7-256q^2)<=q^(-14).
Their sum is at most 2q^(-14)<q^(-12)<=eta.
The zero guard is at most 3q^(-4)<=3/16<1.
These verify FQ7--FQ11 symbolically for all q>=2, without a cutoff search or the old exponential coefficient test.

The accepted field-free scalar proof is applicable to any nonmonomial low-energy integer numerator.
Its two extreme lags each have squared magnitude at least q^(-4), so Var(W)>=2/q^4 regardless of interior collisions.
Strong concavity gives the regularized integral at most -3eta, and the finite tail is strictly less than eta even at an integer ceiling.
Thus c_s<-2eta is the actual normalized circle constant.
C92 excludes a zero value first, using rho<=N<=q^2 and the checked positive span/domain.

Under delta_raw=q delta_s and B_raw=q^2 B_s, S_raw<=q^2 ensures B_raw>=S_raw^2+delta_raw^2.
The raw majorant has constant log q+c_s and unchanged nonconstant coefficients.
Its radial factor is at most 1+q/delta_s.
The new FQ5 and full norm therefore give the stated contradiction c_s+error<-eta.
No arithmetic conclusion at C844's older cutoff was used.

### 4. Width zero, arbitrary support, real weights and scalar windows

For a one-term numerator a x^j, the integral value multiplied by alpha^(-j) implies a/q is a rational algebraic integer.
Thus a/q is an integer, and the positive energy bound a^2<=q^2 forces a=+/-q.
No epsilon(0) is evaluated.
For a general rational f of energy at most one, qf has the low-energy integer hypotheses; the numerator conclusion forces a true signed monomial.
For energy greater than one, q^2||f||_2^2 is an integer and gives the exact spacing 1/q^2.
This proves both the equality characterization and the strict alternative, including a one-term coefficient different from +/-1, with no final term-count hypothesis.

Summing these inequalities with arbitrary positive real weights gives E>=1+mu/q^2.
Positivity of every indexed weight makes E=1 equivalent to every atom being a true signed monomial.
Only the individual spans are used; no common dictionary, covariance, common union span or rationality of weights enters.
For a supplied nonmonomial low-energy numerator, Tm/d>u_s together with T<=Cd gives the strict all-degree bound m>u_s/C, including integral quotient values initially allowed to vanish.

### 5. Every phase parameter, allowed seed and changed arithmetic proof

The phase parameters satisfy delta_p=1/(16q^6 B_s^3)>q^(-17), since (4/125)q^5>1 at every q>=2.
Together with B_p<=q^5 and eta>=q^(-12), this gives the displayed ceiling bound J_p<=q^52.
The radial factor is at most q^20, the harmonic sum is at most q^7, and 2J_p+1<=q^54.
The resulting Lambda_(2q^2,J_p)<=q^(54q^2+7) is valid.

The separate domain estimate J_p u_p<=2^(-1996)<h0 precedes either modulus evaluation.
Then epsilon(J_p u_p)<=q^(25/2)u_p^(1/8)<=q^13 u_p^(1/8).
The Fourier error is at most q^(20-10q^2)<=q^(-20)<q^(-14); the radial error is strictly less than q^(-14).
Their sum is strictly less than 2q^(-14)<eta.
The zero guard is at most 6q^(-4)<=3/8<1.
This verifies every FQ12--FQ15 estimate and strict inequality for all q>=2.

The field-free C845 margin applies to every stated seed.
For positive degree, the same endpoint variance proves its seed margin.
For an allowed constant, 0<|H|<=q-1 supplies the separate strict deficit.
On the two-torus the reversal identity gives equal moduli, both signs are removed by a circle rotation, and the positively regularized factorization permits bounded Fubini.
The exact scalar factorization yields a phase integral increase at most eta/2, and the finite Taylor tail is strictly below eta/2.
Thus the actual torus constant is below -2eta.
The finite separated specialization, or C848's good-shift support identity, transfers this particular constant exactly; this is distinct from the independent-variable coefficient lift of FQ2.

For every positive n, the constant and top coefficients of F_n are sigma H_k and H_k.
They are nonzero, so the true span is T=n+k even with overlapping intervals and interior cancellations.
The support and length bounds N<=2q^2 and S_raw<=2q^2 remain valid.
C92 applies with rho<=2q^2 and excludes zero before the full norm.
The raw scaling delta_raw=q delta_p and B_raw=q^2 B_p satisfies the required length inequality and adds exactly log q to the normalized constant.
The new Lambda bound therefore gives FQ16 directly.
Nonmonic seeds, nonreciprocal original minimal polynomials, both signs, allowed constants and all original embeddings need no additional assumption.
C845/C848's old arithmetic cutoff is never substituted into this new proof.

### 6. Sharper exception count, distinct shifts and growing denominators

The 2s points of A_H are distinct because the two support copies have different second coordinates.
Each sum of J differences has the form sum_i z_i v_i with sum_i z_i=0 and |z_i|<=J.
Counting the first 2s-1 coordinates gives the new cardinality bound; noninjectivity and vectors not realized by J differences can only reduce the image.
Combining it with the old (4s^2)^J bound yields FQ17 and its uniform q-only version.

Every supported pair with b!=0 determines at most one positive integer resonance.
Consequently |Bad(H)| is bounded by the same minimum, while the actual set remains unchanged.
Its inclusion in {1,...,kJ} and its empty value for k=0 remain valid.
For more than N'_q distinct supplied shifts, at least one lies outside this common sign-independent bad set.
Two signs at one shift do not increase the number of shifts.
The support-lattice condition is valid because g divides a and coprimality forces g to divide b, while |b|<=J<g forces b=0.
No shift supply or practical enumeration follows.
The improved combinatorial bound also applies to the unchanged older C848 arithmetic theorem at its own cutoff.

Finally m_j>q_j^(-Aq_j^2)/C gives log(1/m_j)<Aq_j^2 log q_j+log C, with A=256 or 512 as appropriate.
When m_j tends to zero, division by log(1/m_j) makes the asserted little-o condition incompatible with that strict inequality.
This is FQ18--FQ19 under the actual supplied certificates and original windows.
The scalar certificate must be a nonmonomial low-energy numerator; an arbitrary high-energy integral scalar value supplies no such exclusion.

## Source, execution and conclusion limits

C137/C92/C570 retain the exact original finite-frequency modulus and the accepted Pri11 and retained Dim19 v1 statement/applicability scopes.
C845's scalar Jensen use retains its already accepted factorwise normalization.
No original source proof, later source edition, source PDF or external theorem was newly audited.
C113's discriminant/Gram regularization and C140's normalized sparse transfer were checked only as the stated comparisons; neither supplies the new majorant.
The author's targeted-search report is not treated as a fresh exhaustive search or a novelty finding by this reviewer.
The actual C168/C145 antecedents prevent attributing range variance, Parseval or coefficient Cauchy--Schwarz as new principles.

No numerical cutoff search, native mathematical program, finite matrix evaluation, support enumeration or formal verification was performed or needed.
The positive rational cutoffs need not be dyadic, are proved for the new Lambda expense, and are not certified against the older 2^J tests.
The whole finding retains every radial, frequency, matrix, original-degree, supplied-integrality and source-inspection cost.
It asserts neither optimal exponents, numerical superiority to every older K0 bound, an unrestricted growing-denominator gap, automatic auxiliary coverage nor a solution of Lehmer's conjecture.
