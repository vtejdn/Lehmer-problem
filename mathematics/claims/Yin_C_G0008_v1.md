---
author: Yin
---

# Cyclotomic rigidity and forced compensation of fixed trace modes

Date: 2026-10-10T14:59.
Human author: Yin.
Provenance: project deduction.
Organization requested by Yin; [G0001 remains paused](../tasks/Yin_T_G0001_v1.md#decision-human-pause-after-closeout).

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history
### Decision initial
The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-10T14:59 |
| status | open |
| reason | Complete historically reviewed argument fixed for registration; the current extraction/interface finding and its adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only the enumerated conclusions under their stated hypotheses and exclusions. |
| argument | [Argument](#argument) | The selected retained derivations and declared fixed inputs; open transfers and source-screen conclusions are excluded. |
| dependency | [Fixed smoothing input](Yin_C_G0004_v1.md#damped-cyclotomic-norm-inequalities) | Already fixed D11 equations (3)--(5), with the actual minimal-polynomial domain, trace error and nonzero integral cyclotomic norms. Only that subsection is used, not C4's later conclusions. |
| dependency | [Abel/Fourier convention](Yin_C_G0001_v1.md#two-frequency-linear-coupling-control) | Integrable logarithmic kernel and Abel endpoint convention; the retained finite-band calculation gives its complete specialization. |


### Decision organized-reviewed
| Field | Value |
| --- | --- |
| date | 2026-10-10T15:02 |
| status | proved |
| reason | The exact completed local conclusions retain their full historical arguments and reviews; the current extraction finding verifies registered scope and fixed-input interfaces, without resolving excluded open questions or enlarging source inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only the enumerated conclusions under their stated hypotheses and exclusions. |
| argument | [Argument](#argument) | The selected retained derivations and declared fixed inputs; open transfers and source-screen conclusions are excluded. |
| dependency | [Fixed smoothing input](Yin_C_G0004_v1.md#damped-cyclotomic-norm-inequalities) | Already fixed D11 equations (3)--(5), with the actual minimal-polynomial domain, trace error and nonzero integral cyclotomic norms. Only that subsection is used, not C4's later conclusions. |
| dependency | [Abel/Fourier convention](Yin_C_G0001_v1.md#two-frequency-linear-coupling-control) | Integrable logarithmic kernel and Abel endpoint convention; the retained finite-band calculation gives its complete specialization. |
| review | [Extraction finding](../audits/reviews/Yin_R_G0002_v1.md#c8-extraction) | Exact statement/argument registration and fixed-input interfaces, relying on preserved historical local reviews at their actual scopes. |

## Statement

**A. Finite Fourier rigidity.** Let nu be a conjugate-symmetric circle probability measure with real Fourier coefficients a_n and a_n=0 for n>N, where N>=1.
Let q>N be prime, c_r(n) the Ramanujan sum, and L_r(nu)=int log|Phi_r(exp(i theta))| dnu(theta).
If L_r(nu)>=0 and L_(qr)(nu)>=0 for every 1<=r<=N, then nu is uniform circle probability.
The N=2 four-test and cyclic-versus-cyclotomic distinctions are precisely those in the retained argument; no finite Fourier support is asserted for algebraic conjugate measures.

**B. Exact signed-tail inequalities and inversion.** Let alpha be a nontorsion algebraic unit of degree d, with conjugates exp(l_i+i theta_i), total logarithmic measure m, damped roots z_i=exp(-|l_i|+i theta_i), b_n=sum_i z_i^n and actual traces s_n=sum_i alpha_i^n.
For 0<t<1, N>=1 and prime q>N, define

    H=m-(d/2)log t,
    A_r=sum_(n=1)^N c_r(n)t^n b_n/n,
    T_r=sum_(n>N) c_r(n)t^n b_n/n,
    E_N=max_(1<=r<=N)(|T_r|,|T_(qr)|),
    B_N=max_(1<=r<=N)phi(qr) H+E_N.

For 1<=r<=N,

    T_(qr)-phi(qr)H <= A_r <= phi(r)H-T_r.

Put D_j=sum_(r|j)A_r.
For 1<=k<=N, with mu the Mobius function and tau the divisor-count function,

    t^k b_k=sum_(j<=N/k) mu(j)D_(kj)/j,
    |b_k|<=t^(-k)B_N sum_(j<=N/k)tau(kj)/j.

**C. Conditional asymptotic implication.** Along any sequence of these actual units with d->infinity and m->0, take t=1-1/d and fixed N,q.
Then E_N=o(sqrt(d)) implies s_k=o(sqrt(d)) for every 1<=k<=N.
This proves an implication, not its general tail hypothesis.
The extra r=4, N=2 test is the separately displayed equation (10), not an r<=N specialization.

**D. Pure root-equation bound.** If n=2T+2>0, k_i are positive integers and alpha>1 satisfies alpha-alpha^(-1)=(1/2)sum_(i=1)^n (alpha^(k_i)+1)/(alpha^(k_i)-1), then log alpha>asinh((T+1)/2).
The retained MS05 comparison identifies one source construction motivating this equation at the author's recorded reading depth.
No existence theorem, trace assertion for that construction, or statement about every Salem number of trace -T is adopted as a premise of D.

The unrestricted fixed-trace conjecture, general tail smallness, realization of low-mode models and G0001 remain unresolved.

## Argument

Parts A--D select the complete self-contained calculations (1)--(10) and the direct inequality (11) from the displayed root equation.
The smoothing proof (3)--(5) is already fixed at the C4 subsection declared above; the duplicate passage below is preserved as historical full-draft context, not a competing proof selection.
C4 retains its existing selected evidence and does not acquire a backward dependency on this Claim.
The historical 23:25 review covers the entire calculation at these limits; it does not validate MS05's construction/trace theorem or general tail smallness.
No numerical program was run for D11.

## Organization and retained complete draft

The full original D G0011 body follows, preserving all formulas, titles, open questions, source screens, contribution disclosures and historical reviews.
Only heading depth and relocated links change.
Historical descriptions as a working draft, unadopted result or pending fixed review refer to the original date; the Current assessment above owns the present judgment.
Fixing this record does not reopen exploration.
Necessary programs/data remain in their existing J groups.
The old D can be removed only after full-body preservation and consumer repair checks.

### Fixed trace fluctuations in small-Mahler reciprocal families

Date: 2026-10-09 (Asia/Hong_Kong).
Second bounded arithmetic exploration by assigned AI resultant_research for Yin, under the resumed G0001 execution.
This is a working draft, not a fixed or independently reviewed result.

#### Current question

The [two-frequency control](Yin_C_G0001_v1.md#two-frequency-linear-coupling-control) shows that square-root-sized opposite dyadic angular biases can carry positive linear mixed energy.
Its exact radial-to-trace estimate makes actual integer power sums the relevant arithmetic data when total m tends to zero.
Can genuine irreducible reciprocal small-measure families realize such a trace pattern?
Can a quantitative bound on total m exclude it, perhaps in a restricted but useful class?

The trial target is |Tr(alpha^n)|=o(sqrt(d)) for each fixed n along a hypothetical m(alpha)->0 sequence.
This is speculative and may be replaced.
Work will keep total m separate from absolute height m/d, cyclotomic padding from irreducible inputs, and measures from realized conjugate sets.
The local screen includes L G0010's exact Newton/orbit constraints, L G0034's net-trace distinction, and L G0167's regularized discriminant energy.
None currently gives the desired fixed-mode arithmetic rate.

<a id="finite-fourier-cyclotomic-rigidity"></a>
#### Finite Fourier perturbations fail the full cyclotomic tests

Let mu be uniform measure on the circle and nu a conjugate-symmetric probability measure having finite Fourier support: a_n=int exp(i n theta)dnu is real and a_n=0 for n>N.
Such a measure has a trigonometric-polynomial density with respect to mu.
Put

    L_r(nu)=int log|Phi_r(exp(i theta))|dnu(theta),
    c_r(n)=sum_(zeta primitive of order r) zeta^n.

The logarithmic integral is finite because the density is bounded and circle logarithmic singularities are integrable.
Expanding each linear factor by Abel regularization and then passing in L1, as in D G0007, gives

    L_r(nu)=-sum_(n=1)^N c_r(n)a_n/n.                 (1)

Fix a prime q>N.
For every r<=N and n<=N, q does not divide r or n.
Primitive roots of coprime orders r and q multiply bijectively to primitive roots of order rq.
The finite geometric sum over the nontrivial q-th roots equals -1 at n.
Therefore

    c_(rq)(n)=-c_r(n),
    L_(rq)(nu)=-L_r(nu).                             (2)

If the 2N inequalities L_r(nu)>=0 and L_(rq)(nu)>=0 hold for 1<=r<=N, then every L_r(nu)=0 for r<=N.
The factorization x^j-1=product_(r|j)Phi_r(x) now gives

    0=sum_(r|j)L_r(nu)
     =-sum_(h<=N/j) a_(jh)/h,       1<=j<=N.

Starting at j=N and descending proves a_N=a_(N-1)=...=a_1=0.
Thus nu=mu.
This is an exact finite-band rigidity calculation, not a statement that actual conjugate measures have finite Fourier support.

For N=2 the four tests Phi_1,Phi_2,Phi_3,Phi_6 already suffice.
Their first two Ramanujan vectors are respectively (1,1),(-1,1),(-1,-1),(1,-1), so they test both signs of a_1+a_2/2 and -a_1+a_2/2.

This clarifies the D G0007 model's arithmetic limitation.
Its a_1=epsilon,a_2=-epsilon has L_1=-epsilon/2<0.
Changing the amplitudes to a_1=epsilon/2,a_2=-epsilon makes every x^k-1 logarithmic integral nonnegative, but L_4=-epsilon<0.
Full cyclotomic norms impose strictly more information than nonnegativity of each cyclic norm C_k alone.
Neither model was asserted to be an actual algebraic orbit.

<a id="damped-cyclotomic-norm-inequalities"></a>
#### Exact smoothed inequalities for actual units

Now let alpha be a nontorsion algebraic unit with degree d, conjugates exp(l_i+i theta_i), and m=sum_i max(l_i,0).
Put

    z_i=exp(-|l_i|+i theta_i),
    b_n=sum_i z_i^n in R,             |z_i|<=1.

The b_n need not be integers.
They differ from the actual integer power sums s_n=sum_i alpha_i^n by

    |s_n-b_n|<=2n exp(nm)m.                           (3)

Indeed, for l_i<=0 the summands agree; for l_i>=0 use exp(nl_i)-exp(-nl_i)<=2n exp(nm)l_i and sum the positive l_i.
Reality follows from complex-conjugate pairing.

The cyclotomic resultant is a nonzero integer, and direct root factorization gives

    log|Res(P,Phi_r)|=phi(r)m
         +sum_i sum_(zeta primitive r)log|1-z_i conjugate(zeta)|
       >=0.                                             (4)

For l_i<0 the phase sign in the elementary factorization may reverse; conjugate symmetry of the complete primitive-root set makes the displayed total unchanged.
No individual value at a single nonreal primitive root is being declared rational or integral.

For 0<t<1 and |z|<=1,

    |1-tz|^2-t|1-z|^2=(1-t)(1-t|z|^2)>=0.

Thus replacing every z_i in (4) by t z_i decreases the total by at most -(d phi(r)/2)log t.
Expanding the now absolutely convergent logarithms yields the rigorous inequality

    sum_(n>=1) t^n c_r(n)b_n/n <=phi(r)H,
    H=m-(d/2)log t>0.                                (5)

The d log t term is a retained smoothing cost.
It is not discarded because total m is small.

<a id="fixed-mode-forced-tail-interface"></a>
#### Opposite cyclotomic tests force explicit tail compensation

Fix N>=1 and a prime q>N.
For r<=N define the actual finite low part and convergent tail

    A_r=sum_(n=1)^N c_r(n)t^n b_n/n,
    T_r=sum_(n>N) c_r(n)t^n b_n/n,
    T_(qr)=sum_(n>N) c_(qr)(n)t^n b_n/n.

Pairing (5) at r and qr, and using (2) only in the low part, proves

    T_(qr)-phi(qr)H <= A_r <= phi(r)H-T_r.             (6)

In particular, with

    E_N=max_(1<=r<=N)(|T_r|,|T_(qr)|),
    B_N=max_(1<=r<=N)phi(qr) H+E_N,

one has |A_r|<=B_N.
This is a precise arithmetic restriction absent from the continuous two-frequency control.
It leaves a genuine high-frequency compensation mechanism available; the tails are not presumed small.

For completeness the low coefficients can be recovered explicitly.
For j<=N set

    D_j=sum_(r|j) A_r
       =sum_(h<=N/j) t^(jh)b_(jh)/h.

The equality follows by summing primitive roots of all orders dividing j: sum_(r|j)c_r(n) is j when j divides n and zero otherwise.
Finite Mobius inversion gives

    t^k b_k=sum_(j<=N/k) mu(j)D_(kj)/j,
    |b_k|<=t^(-k) B_N sum_(j<=N/k) tau(kj)/j,
                         1<=k<=N,                   (7)

where tau counts positive divisors.
To verify inversion, the coefficient of t^(k ell)b_(k ell) after substitution is (1/ell)sum_(j|ell)mu(j), which vanishes unless ell=1.

Choose t=1-1/d for d>=2.
Since -log(1-1/d)<=1/(d-1),

    H<=m+d/(2(d-1))<=m+1.                            (8)

For a hypothetical m->0 sequence, its degrees tend to infinity by the accepted fixed-degree finiteness argument.
With N,q fixed, (3), (7)--(8) show the concrete conditional implication

    E_N=o(sqrt(d))  =>  s_k=o(sqrt(d)) for 1<=k<=N.   (9)

Conversely any fixed-mode square-root-sized actual trace forces at least one of the finitely many tails in E_N to have square-root scale, by the same inequalities.
This is a conditional bridge and a localization of the missing information, not proof of the tail hypothesis or of the fixed-trace target.
The general discriminant energy in L G0167 does not by itself pay for E_N=o(sqrt(d)); its diagonal cost remains.

One explicit component may be useful experimentally.
If N=2, r=4 is also tested directly, then c_4(1)=0 and c_4(2)=-2.
Thus (5) gives

    -t^2 b_2+sum_(k>=2) (-1)^k t^(2k)b_(2k)/k <=2H. (10)

A negative b_2 of order sqrt(d) requires a comparably negative signed tail at even frequencies.
Formula (10) uses the r=4 test in addition to the paired set used in (6); it is not an r<=N specialization.

<a id="arbitrary-trace-construction-measure-screen"></a>
#### A real construction lead whose measure grows with its trace

The primary source screen inspected [MS05](../literature/pdf/MS05.pdf), McKee--Smyth, *There are Salem numbers of every trace*, arXiv:math/0308213v2, especially equation (10) on printed p.8 and Lemma 12 on pp.9--10.
Its retained acquisition and [scoped reading](../audits/literature/MS05/readme.md) are complete; no full source theorem is adopted as a new premise here.

The relevant polynomial construction is encoded by

    h(x_0,...,x_n)=2(x_0^2-1)product_i(x_i-1)
           -x_0 sum_j (x_j+1)product_(i!=j)(x_i-1).

For the source's even n=2T+2 construction and its specified choices of k_i, the noncyclotomic Salem factor has trace -T.
Any real root alpha>1 of h(alpha,alpha^(k_1)...,alpha^(k_n)) satisfies directly

    alpha-alpha^(-1)
       =(1/2)sum_i (alpha^(k_i)+1)/(alpha^(k_i)-1)
       >n/2=T+1.

Hence its logarithmic exterior-root size obeys

    log alpha>asinh((T+1)/2).                         (11)

This direct inequality excludes that particular construction as a source of unbounded negative trace with m->0; its right side grows with T.
It is not a theorem about every Salem number of trace -T.
The source's nonnegative-trace quartics also have growing exterior roots.
No irreducible small-measure family with square-root dyadic traces was constructed in this round.

#### Reuse, experiments, and status

The local screen covered L G0010's power-sum and inverse-trace identities, L G0034's Euler/net-trace bookkeeping, the Smy08 house and power-sum audit passage, L G0167's diagonal-energy cost, and the G0007 working calculations.
Searches for trace/Mahler inequalities and arbitrary-trace Salem constructions led to the primary source above.
Its polynomial and relevant real-root equation were read and pp.8--9 visually checked from the retained PDF; the entire torsion-coset construction was not audited or used as a new accepted theorem.
The assigned agent completed acquisition and registration of MS05 and LL25 under the shared writer lock after the main agent authorized that disjoint scope.

Equations (1)--(10) are self-contained written calculations.
There was no numerical execution supporting them and no retained program in this round.
A useful future computation is to evaluate the actual tails in (6) from polynomial values at scaled roots of unity, subtracting exact finite Newton terms, on genuine inputs; this avoids blindly truncating a long trace series.
Interval or exact algebraic-log bounds would be needed for an asserted tail certificate.

The next mathematical question is whether a genuinely useful arithmetic estimate on one of these signed tails is available, or whether explicit reciprocal constructions can make it large at bounded total m.
The finite-band rigidity result does not close the entire Fourier or resultant route: it explains why a successful arithmetic model requires linked low and high modes.
The fixed-trace conjecture, its near-one coverage and the unrestricted G0001 contract remain unresolved.
The authoring AI self-checked this draft.

#### Local review of the self-contained calculations

At 2026-10-09T15:25 the coordinating AI for Yin separately checked equations (1)--(10) and their complete derivations.
It rechecked the coprime primitive-root multiplication and q>N guards, the descending finite-band argument, all four N=2 Ramanujan vectors, the damped-root/actual-trace difference, nonzero integral cyclotomic resultants, the exact smoothing inequality and retained d log t cost, both signed-tail inequalities, finite Mobius inversion and the fixed-N asymptotic implication.
It found no defect at this explicitly conditional scope.
The author supplied progress explanations and the draft; the reviewer had assigned the broad follow-up question but contributed no displayed derivation.
It also checked the algebraic implication from the displayed MS05 root equation to (11), without independently rereading that source's construction or verifying its trace assertion; that source interface retains the author's scoped reading.
The review establishes neither high-tail smallness nor arithmetic realization of a trace model.
It is a local exploratory check, not a fixed R/L finding or a Claim/Task adoption.