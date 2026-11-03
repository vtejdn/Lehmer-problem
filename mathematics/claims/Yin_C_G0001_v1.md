---
author: Yin
---

# Fixed doubling resultants, radial decomposition and low-frequency controls

Date: 2026-10-10T14:16.
Human author: Yin.
Provenance: project deduction.

Context: [G0001](../tasks/Yin_T_G0001_v1.md), presently paused.
The user requested completed drafts to be placed in the material area matching their role.
This is result organization, not renewed exploration or a change to that Task decision.

## Current assessment
[Selected decision](#decision-current-confluent-proof-homes)

## Assessment history
### Decision initial
The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-10T14:16 |
| status | open |
| reason | Complete historical argument extracted for precise registration; current extraction-interface review and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only the explicitly enumerated conclusions and hypotheses. |
| argument | [Argument](#argument) | The selected completed derivations retained below; speculative and computational-history passages are excluded as proof premises. |
| dependency | [Complete mixed resultants](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | Noncoincidence and full multiplicity convention for actual unit conjugates, and the nonzero integral doubling resultant with its Frobenius floor. |


### Decision organized-reviewed
| Field | Value |
| --- | --- |
| date | 2026-10-10T14:24 |
| status | proved |
| reason | The precisely enumerated completed results have unchanged complete historical arguments and reviews; the fixed extraction finding checks the new statement and actual dependency interfaces. Original conjectures, finite discovery statistics and unchecked source generalizations are excluded. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exactly the enumerated parts with all their separate hypotheses and exclusions. |
| argument | [Argument](#argument) | The complete selected retained derivations, with their explicit supporting inputs and historical review boundaries. |
| dependency | [Complete mixed resultants](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | Noncoincidence and full multiplicity convention for actual unit conjugates, and the nonzero integral doubling resultant with its Frobenius floor. |
| review | [Extraction finding](../audits/reviews/Yin_R_G0001_v1.md#c1-extraction) | Exact current statement and argument interfaces; relies on unchanged historical mathematical reviews at their preserved scopes. |


### Decision current-confluent-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:11 |
| status | proved |
| reason | Select C231#mixed-power-resultant-identities as the complete current home of the identical original L59 full-root cross-exponent nonvanishing, multiplicity and exact resultant conventions at the unchanged used scope. The complete retained proof and actual current statement were read, including non-torsion and degree-drop boundaries; this is routine same-content interface adoption. Mathematical status, selected statement/argument/finding and every relation scope remain. Original dated decisions and R bindings retain their actual L59 inputs, and no new independent review or additional arithmetic surplus is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exactly the enumerated parts with all their separate hypotheses and exclusions. |
| argument | [Argument](#argument) | The complete selected retained derivations, with their explicit supporting inputs and historical review boundaries. |
| dependency | [Dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Noncoincidence and full multiplicity convention for actual unit conjugates, and the nonzero integral doubling resultant with its Frobenius floor. |
| review | [Review](../audits/reviews/Yin_R_G0001_v1.md#c1-extraction) | Exact current statement and argument interfaces; relies on unchanged historical mathematical reviews at their preserved scopes. |

## Statement

All polynomial root lists include their full multiplicities.
Mahler measure below means the unnormalized logarithmic measure \(m\).

**A. Exact saturation.**
For every integer \(d\ge2\), \(F_d(x)=x^d-x-1\) and \(F_d^{[2]}(x)=\prod_{F_d(\alpha)=0}(x-\alpha^2)\) satisfy
\[
 |\operatorname{Res}(F_d,F_d^{[2]})|=2^d.
\]
No irreducibility hypothesis is imposed on this control family.

**B. Actual radial-angular split.**
Let \(P\) be the monic minimal polynomial of a nontorsion algebraic unit, of degree \(d\), with all conjugates \(\alpha_i=e^{\ell_i+i\theta_i}\) and \(m=\sum_i\max(\ell_i,0)\).
Set \(R=\operatorname{Res}(P,P^{[2]})\) and
\[
 B_{\rm rad}=\tfrac12\sum_{i,j}|\ell_i-2\ell_j|,\qquad
 K=\sum_{i,j}\log|1-e^{-|\ell_i-2\ell_j|+i(\theta_i-2\theta_j)}|.
\]
Then \(R\ne0\), \(\log|R|=B_{\rm rad}+K\), \(0\le B_{\rm rad}\le3dm\), and \(K\ge d\log2-3dm\).
For the Salem radial configuration \((m,-m,0,\ldots,0)\), \(B_{\rm rad}=(3d-2)m\).

**C. Low-frequency continuous control and actual trace error.**
With uniform circle probability \(\mu\), let
\[
 d\nu_\varepsilon=(1+2\varepsilon(\cos\theta-\cos2\theta))\,d\mu,\qquad 0<\varepsilon\le1/4.
\]
For \(0<r\le1\), define \(J_r\) and \(I_r\) by the double integrals of \(\log|1-r e^{i(\theta-2\phi)}|\) and \(\log|1-r e^{i(\theta-\phi)}|\), respectively, against \(\nu_\varepsilon\otimes\nu_\varepsilon\).
The integrals exist, including the endpoint, and
\[
 J_r=r\varepsilon^2,\qquad I_r=-\varepsilon^2(r+r^2/2).
\]
For fixed \(c>0\) and integers \(d\ge16c^2\), \(\varepsilon=c/\sqrt d\) gives total-variation convergence to \(\mu\), but \(d^2J_r=rc^2d\).
Separately, the actual input in B satisfies, for every integer \(n\ge1\),
\[
 s_n=\sum_i\alpha_i^n\in\mathbb Z,\qquad
 \left|s_n-\sum_i e^{in\theta_i}\right|\le2ne^{nm}m.
\]

The continuous control is not asserted to be an algebraic orbit.
The unrestricted fixed-trace conjecture in historical equation (11), arithmetic realizability, and high-frequency estimates are not part of this Claim.

## Argument

Parts A--C use exactly the retained calculations (1)--(10), including the integrable Abel endpoint and degree-free trace error.
The direct fixed input is L G0059 as declared above.
L G0063/G0064 explain prior Frobenius reuse; L G0066 supplies comparison controls.
LL25 and MS05 are source screens, not premises.
The historical local calculation review below covers (1)--(10), not the speculative (11).

### Organization and extraction provenance

The entire text of Yin_D_G0007 dated 2026-10-09 is retained below, including its original title, derivations, equation labels, historical reviews, failed attempts, source boundaries and open questions.
Only heading depth and relocated link targets change.
Its historical statements that adoption was outstanding describe that date; the explicit Current assessment above owns the present judgment.
The source draft is extraction ancestry, not a mutable proof dependency.
Open questions and historical future plans remain historical/exploratory and do not authorize execution while G0001 is paused.
Programs and native certificates remain in their J homes.

### Fixed doubling resultants: exact surplus and conjugate correlation

Date: 2026-10-09 (Asia/Hong_Kong).
Exploratory draft by assigned AI resultant_research for Yin under the resumed G0001 execution.
This draft is not fixed; its later separately organized local calculation review is recorded below.

#### Current question and scope

For a nontorsion algebraic unit alpha with minimal polynomial P of degree d, can the complete nonzero resultant R=Res(P,P^[2]) exploit correlations between conjugates to improve its upper bound to a useful linear scale?
In parallel, what forces or obstructs a genuine arithmetic surplus |R|/2^d beyond the elementary Frobenius floor?

The current inputs are [C231 retained L59](Yin_C_G0231_v1.md#mixed-power-resultant-identities), [C232v2 retained L60](Yin_C_G0232_v2.md#multilevel-surplus-boundary), and [L G0168](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost).
The draft retains actual root multiplicities and distinguishes reciprocal near-one inputs from nonreciprocal control families.
No Lehmer conclusion or new source theorem is assumed.

<a id="fixed-doubling-reuse-boundary"></a>
#### Reuse and the exact arithmetic object

Write P^[2]-P=2H_P with H_P in Z[x], deg H_P<d.
Frobenius gives integrality, and evaluation at the roots of P gives exactly

    Res(P,P^[2])=2^d Res(P,H_P).

This is another presentation of the normalized Frobenius quotient already developed in [C237](Yin_C_G0237_v1.md#base-prime-power-extra-valuation) and [C241](Yin_C_G0241_v1.md#frobenius-repetition-hypotheses).
It is not claimed as a new mechanism.
The complete reciprocal square, trace-order and two-copy identities are already in [C243](Yin_C_G0243_v1.md#reciprocal-mixed-resultant-square).
Its Lehmer control has individual normalized R_(1,2)=1 and R_(1,3)=1, whereas its full confluent Q_P=9 also includes the index factor I_2^2.
Those are different objects.

For the control family F_d=x^d-x-1, d>=2, an elementary exact identity is

    |Res(F_d,F_d^[2])|=2^d.                         (1)

No irreducibility assertion is needed for this polynomial identity.
If d=2k, root squaring gives

    F_d^[2]=x^d-2x^k+1-x,
    H_(F_d)=1-x^k.

At x^k=1, F_d(x)=-x, so the absolute resultant with 1-x^k is one.
If d=2k+1, then k>=1 and

    F_d^[2]=x^d-2x^(k+1)+x-1,
    H_(F_d)=x(1-x^k).

The constant term of F_d has absolute value one, and at x^k=1 one has F_d(x)=-1; the two resultant factors again have absolute value one.
This establishes (1) by direct polynomial arithmetic.
This family is a nonreciprocal control, not a hypothetical near-one sequence.
Its exact saturation shows why an unconditional strict surplus for all unit polynomials would have the wrong scope.
The already retained Lehmer control shows that reciprocity alone does not impose strict surplus either.

<a id="doubling-exact-radial-angular-split"></a>
#### Exact radial and angular separation

Let alpha_1,...,alpha_d be the conjugates of a nontorsion algebraic unit, with alpha_i=exp(l_i+i theta_i), l_i real.
Then sum_i l_i=0 and sum_i max(l_i,0)=m.
The mixed-root separation in L G0059 shows alpha_i!=alpha_j^2, including through a powered-degree drop.

For any nonzero complex z=exp(a+i theta), w=exp(b+i phi) with z!=w,

    log|z-w|=max(a,b)
       +log|1-exp(-|a-b|+i(theta-phi))|.             (2)

When a<b the sign of the phase reverses in the direct factorization; the absolute value is unchanged.
Consequently

    log|R_(1,2)|=B+K,
    B=sum_(i,j) max(l_i,2l_j)
     =(1/2)sum_(i,j)|l_i-2l_j|,
    K=sum_(i,j)log|1-exp(-|l_i-2l_j|
                                   +i(theta_i-2theta_j))|.      (3)

The equality for B uses sum l_i=0.
The elementary inequality max(a,b)<=max(a,0)+max(b,0) gives

    0<=B<=3dm.                                      (4)

Thus a putative sequence with m->0 must have K/d>=log 2-o(1), by the actual 2^d Frobenius divisibility.
This is an exact necessary condition, not a contradiction or a new lower-income theorem.
It identifies the part of a complete-resultant upper estimate that has to be addressed after the radial contribution has already become small.

For a Salem input with logarithmic measure m, the radial list is m,-m,0,...,0.
Counting the four exceptional pairs and their interactions with the d-2 unit-circle roots in (3) gives the sharper exact value

    B=(3d-2)m.                                      (5)

The summands with both l_i=l_j=0 are logarithmically singular as their phases approach a doubling match; the other summands retain their actual radial smoothing.
Replacing all of these damping factors by a common cutoff, or replacing the original roots by their phases, needs a separate error estimate.
Equation (3) does not authorize that replacement.

<a id="two-frequency-linear-coupling-control"></a>
#### An explicit low-frequency model with linear mixed energy

The following calculation isolates a second issue beyond a singular tail.
Let mu be uniform measure on the unit circle, write z=exp(i theta), and, for 0<epsilon<=1/4, let

    dnu_epsilon=(1+2epsilon(cos theta-cos 2theta)) dmu.

The density is nonnegative because |cos theta-cos 2theta|<=2, and its integral is one.
In the convention a_n=int exp(i n theta)dnu_epsilon, one has

    a_1=epsilon, a_2=-epsilon, a_n=0 for n>=3.        (6)

For 0<r<1 define the smooth mixed logarithmic energy

    J_r(nu)=int int log|1-r exp(i(theta-2phi))|
                                     dnu(theta)dnu(phi).

The uniformly absolutely convergent Fourier expansion of this kernel gives

    J_r(nu)=-sum_(n>=1) (r^n/n) Re(a_n conjugate(a_(2n))).

For (6), this is exactly

    J_r(nu_epsilon)=r epsilon^2.                     (7)

Likewise the self logarithmic energy is

    I_r(nu_epsilon):=int int log|1-r exp(i(theta-phi))|
                      dnu_epsilon(theta)dnu_epsilon(phi)
       =-epsilon^2(r+r^2/2).                         (8)

At r=1 both logarithmic integrals exist.
The densities are uniformly bounded and the logarithmic circle kernel is integrable.
Its Abel regularizations converge in L1, so (7)--(8) yield J_1=epsilon^2 and I_1=-3epsilon^2/2 as well.
One elementary justification of the L1 passage is to bound |1-r exp(it)| below by a fixed multiple of |t| when r>=1/2 and |t|<=pi, up to a constant independent of r; the resulting negative-log majorant is integrable, while positive parts are bounded by log 2.

Fix c>0 and set epsilon=c/sqrt(d), for d>=16c^2.
Then nu_epsilon tends to mu even in total variation, while

    d^2 J_r(nu_epsilon)=r c^2 d,
    d^2 I_r(nu_epsilon)=-(r+r^2/2)c^2 d.              (9)

Thus a positive linear mixed logarithmic energy can already be carried by frequencies 1 and 2.
It need not come only from extremely close pairs or from an unbounded test function: (9) holds for each fixed smooth kernel r<1.
At the scale of unnormalized traces the model has opposite biases of size c sqrt(d).
A general estimate that only controls their normalized values by a quantity of order sqrt(log d/d) permits these biases.

This is a measure-theoretic control, not an empirical d-point set, an algebraic polynomial, a Galois orbit, or a counterexample to a proposed assertion with the missing arithmetic hypotheses included.
Its limited conclusion is precise: one-point weak convergence, even with O(d^(-1/2)) discrepancy for these modes, does not force o(d) mixed energy.
A useful arithmetic proof should distinguish global low-mode correlation from the singular or growing-frequency tail instead of assigning every obstruction to the latter.

<a id="integer-trace-low-mode-question"></a>
#### A concrete speculative follow-up

For actual conjugates put s_n=sum_i alpha_i^n in Z and let a_n=sum_i exp(i n theta_i)/d.
Since all |l_i|<=m and sum_i|l_i|=2m, the elementary mean-value bound gives, for every fixed n>=1,

    |s_n-d a_n|<=n exp(nm) sum_i|l_i|
                 =2n exp(nm)m.                      (10)

This has no factor d.
It connects the low angular modes in (7) directly to integer power sums when total m is small, rather than only when absolute height m/d is small.
For a hypothetical m->0 sequence, s_n-d a_n->0 for each fixed n.
Therefore the two-frequency model's mechanism would require actual power sums of opposite signs and order sqrt(d), not merely uncontrolled radial errors.

The first proposed test is whether this can occur in genuine irreducible small-measure families after actual cyclotomic factor removal.
More ambitiously, a candidate statement to investigate is

    for each fixed n, |s_n|=o(sqrt(d)) whenever m->0.  (11)

Statement (11) is unproved here and is not claimed necessary for Lehmer.
It would eliminate the specific fixed-mode mechanism above, while leaving growing frequencies, the singular tail and the full mixed kernel in (3) unresolved.
Its all-power-stable variant may be worth testing as a separate, weaker-scope conjecture.
The elementary Frobenius congruence s_(2n)=s_n mod 2 by itself does not exclude opposite square-root-sized values: such integer pairs can have equal parity.
Newton integrality at all orders and actual root geometry are the additional information to inspect.

For a finite experiment, first use exact Newton sums and certified factorization on existing small-measure inputs, recording s_1 s_2/d and a few higher dyadic correlations.
Then attempt an actual reciprocal construction with prescribed larger traces, keeping control of the complete irreducible factor's Mahler measure.
A construction with large traces but uncontrolled measure is a control only.
A failure to produce such a family is not evidence for (11).

#### Search, computation and current review scope

On 2026-10-09 the authoring agent read the relevant L G0058--60, L G0064, L G0066 and L G0168 interfaces, searched local ledgers, drafts and the literature registry for doubling/resultant, Chebyshev, energy and power-sum information, and then searched primary literature for small-height conjugate pair correlation and fixed-power resultants.
The exact identities above use no new external theorem.

The inspected introduction and Theorems 1.1/1.4 of [LL25](../literature/pdf/LL25.pdf), Levenberg--Londhe, arXiv:2504.11599v1, provide weak equidistribution, including a two-variable lifting formulation.
The stated height is normalized by degree squared in the lifted result.
These statements do not supply a linear-scale mixed logarithmic estimate for the present moving conjugate-pair kernel.
This is a statement-level relevance screen, not a full proof audit or an adopted new input.
Following the initial HTML reading, the exact v1 PDF was acquired and registered on 2026-10-09; its relevant pages were visually checked.
The [scoped source reading](../audits/literature/LL25/readme.md) records that boundary.

A further search for small-Mahler power-sum bounds found [MS05](../literature/pdf/MS05.pdf), McKee--Smyth, *There are Salem numbers of every trace*, whose abstract supplied a relevant construction lead but no small-measure bound at the scale (11).
Only its primary abstract was used in this draft's first round.
In the subsequent [D G0011](Yin_C_G0008_v1.md#arbitrary-trace-construction-measure-screen) round, arXiv:math/0308213v2 was acquired and registered, and the particular construction's polynomial and exterior-root equation were inspected; the [scoped source reading](../audits/literature/MS05/readme.md) records the checks and remaining proof-review boundary.
No construction theorem is adopted here.
The search did not settle (11), and no novelty or absence-of-literature claim is made.

There is no retained numerical evidence supporting (1)--(11); (1)--(10) are direct written calculations and (11) is a speculative target.
An incidental exact symbolic examination of the Lehmer Frobenius remainder was not used as a premise or route decision and needs no continuing program.
The authoring AI self-checked the written calculations.
Any fixed-result adoption remains outstanding.
G0001 is unresolved.

#### Local calculation review

At 2026-10-09T15:16, the coordinating AI for Yin separately checked the complete elementary calculations (1)--(10): even/odd squaring and resultant saturation, the unit radial sums and exact Salem count, Fourier signs and coefficients, density positivity, the integrable Abel-limit majorant and the degree-free trace error.
No mathematical defect was found at their stated scope.
The reviewer had supplied the broad research question and received progress explanations, but did not derive these formulas or the two-frequency example.
The review uses the retained L59 noncoincidence/resultant convention and its elementary height implication; it does not re-audit that fixed proof or the searched literature.
In particular (11) remains a conjectural target, and no arithmetic realizability of the smooth model or permissible common radial replacement was inferred.
This is a separately organized local exploratory check, not a fixed acceptance finding or a Claim/Task assessment.
