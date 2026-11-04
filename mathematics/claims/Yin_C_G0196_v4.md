---
author: Yin
---
# Joint C3 and C5 closure forces canonical reduction degree at least34

Date: 2026-10-20T14:27.
Human author Yin.
This substantive v4 preserves physical [v1](Yin_C_G0196_v1.md#statement), [v2](Yin_C_G0196_v2.md#statement) and [v3](Yin_C_G0196_v3.md#statement), their mathematical scopes and earlier review/adoption decisions.
Root supplied the new C3 closure, quartic identities, multiplicity refinements and joint global budget.
The draft_comparison_cleanup agent developed and checked the full original-domain proof, all orbit cases and degree-drop boundary in the JB1--JB9 author argument recorded on2026-10-20T14:03.
Both are contributors to this new proof.
The quadratic-source input is now the exact adopted [C197v3 degree41 consequence](Yin_C_G0197_v3.md#quadratic-primary-degree41-consequence), with actual [R477 coverage](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding).
Root and entropy_attainment_bridge authored that upstream input; draft_comparison_cleanup reviewed it as a new consumer while disclosing earlier author relationships.
The older C196 graph and arithmetic inputs retain their actual R468/R473/R474 independent scopes; none is a new review of this JB proof.
The Haar consequence uses the unchanged exact scalar Jensen normalization.
No mathematical program, orbit scan, new source acquisition or actual boundary example is supplied.
No independent whole review or adoption of this v4 is claimed.

<a id="statement"></a>
## Complete original-domain statement

Let P be monic irreducible reciprocal nontorsion in Z[z], of degree d=2r and constant coefficient1.
For a root alpha put delta=alpha+alpha^(-1), F=Q(delta), assume F totally real, and let T be the actual monic degree-r trace polynomial, with P(z)=z^r T(z+z^(-1)).
Use the actual integer polynomials and values

    C2=X^2-2, C3=X^3-3X, C5=X^5-5X^3+5X,
    theta_p=rem_T(T(C_p))/p,
    a=theta_2(delta), b=theta_3(delta),
    c=theta_5(delta), g=c^3-2b^5,
    2c^2-3a^5=0,
    b^2-a^3+s g=0, g!=0, s in{1,-1}.             (JB1)

Thus both residual equations use the original quotients of the SAME T, as in [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain).
The three values a,b,c are the actual nonzero algebraic integers from that interface, not freely chosen coordinates.
Put

    G_can=rem_T(theta_5^3-2theta_3^5),
    w=deg G_can<r,
    U=Tbar, R=G_can mod2,
    chi=C5bar=X^5+X^3+X,
    tau=C3bar=X^3+X,
    phi=X^2+X+1.                                 (JB2)

The nonzero value g ensures that G_can is a nonzero integer polynomial, so w is a well-defined nonnegative integer.
Then

    R!=0 implies deg R>=34, hence w>=34.          (JB3)

The degree bound applies to the REDUCED canonical polynomial, so a drop from w to deg R is permitted.
No actual input with degree34 is asserted to exist.
Without assuming R nonzero, one consequently has

    w<=33 implies every coefficient of G_can is even,
    I_can=integral_(|z|=1) log(G_can(z+z^(-1))^2) dmu
                              >=2log2.           (JB10)

Here mu is normalized Haar measure on the unit circle and all logarithms are natural.
The integral includes the integrable logarithmic singularities at circle zeros.
The conclusion includes nonzero constant G_can, holds at every original Mahler measure and contains no division by r,d or auxiliary degree.
It concerns all coefficients, not merely the leading one.
No assertion about arbitrary rational representatives, every canonical degree or a uniform original logarithmic transfer is made.

<a id="argument"></a>
<a id="actual-c3-c5-global-degree-budget"></a>
## Complete joint-orbit proof

For the degree assertion, assume R is nonzero.
Write U as the product of distinct monic irreducible psi to the full exponents N_psi.
The accepted [C196v3 graph and multiplicity argument](Yin_C_G0196_v3.md#canonical-c5-residue-graph), using [C191v2 per-cluster arithmetic](Yin_C_G0191_v2.md#argument) and [C178](Yin_C_G0178_v1.md#statement), supplies N_psi>=2 and at least one unsaturated orbit.
Here unsaturated means nu_psi=ord_psi R<N_psi.
The complete exponent is the original sum of local e_p f_p/deg psi; it is not a separability assumption or a statement that the generator has the full residue degree.

The exact additional input is the adopted [C197v3 actual quadratic-source consequence](Yin_C_G0197_v3.md#quadratic-primary-degree41-consequence):

    (H2) If phi is unsaturated for the actual
         full residual input(JB1), then deg R>=41.

Its hypotheses are exactly the current original domain, with the same canonical R and all original multiplicities.
The adopted result permits reduction degree drop and is conditional on this quadratic source; it is not used as a global all-orbit bound41.
Its complete proof and actual whole consumer review remain in C197v3 and R477, rather than a mutable draft.
The following cases combine that fixed input with the full degree budget for every other possible unsaturated source.

### Both composition maps preserve the entire root set

The actual trace polynomial T is the monic minimal polynomial of delta.
Thus the two exact value equations(JB1) give polynomial divisibilities by T in Z[X], and their reductions hold modulo the whole U.
For every irreducible psi dividing U, the actual per-cluster positive income in C191 gives psi|R, as already retained in C196v2/v3.
This conclusion comes from income in EACH cluster, not merely a positive global norm.
At any geometric root x of U, the reduction of g=c^3-2b^5 therefore gives theta_5bar(x)=0.
The first equation in(JB1) gives theta_2bar(x)=0.
The second then gives theta_3bar(x)=0.
The actual odd-quotient identities are

    theta_3bar congruent U(tau) modulo U,
    theta_5bar congruent U(chi) modulo U.

They follow from monic integer division and the fact that3 and5 reduce to1.
It follows that

    tau(Sigma(U)) is contained in Sigma(U),
    chi(Sigma(U)) is contained in Sigma(U).      (JB4)

Here Sigma(U) is the entire geometric root set; its multiplicities are still retained in U.

For a geometric root x with multiplicity N_x and chi-target y, let e_chi(x) be the local order of chi(X)-chi(x).
The exact canonical remainder identity gives

    ord_x R>=min{3e_chi(x)N_y,N_x};
    ord_x R<N_x implies
       ord_x R=3e_chi(x)N_y.                     (JB5)

Every orbit contributes at least twice its degree to deg R, and the general stronger bound

    ord_psi R>=min{3,N_psi}

is available from [C196v2](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape).
A chi-self-target orbit is saturated.
Since deg R<deg U, some orbit is unsaturated; choose one and denote its degree by h.
All orbit orders below allow infinity for a zero quotient polynomial, with every asserted finite order forced by the displayed congruences.

### All degrees except4 are covered

The complete fixed C5 graph shows that both degree1 orbits and both degree3 orbits are individually preserved.
They cannot be the chosen unsaturated source.
If h=2, the adopted input(H2) supplies deg R>=41.

For h>=4 the C5 local degree is1, since chi'=phi^2 has only the degree2 critical orbit.
The target is a distinct Frobenius orbit of degree k dividing h.
If its multiplicity is M>=2, the unsaturated source contributes3Mh>=6h, and the distinct target contributes at least2k.
Thus

    deg R>=6h+2k.                                (JB6)

For h>=6 this is at least38.
For h=5, the target degree is1 or5.
But

    chi=X phi^2,
    chi+1=(X+1)(X^4+X^3+1)

shows that a preimage of0 or1 has degree1,2 or4, never5.
Thus k=5, and(JB6) gives deg R>=40.
This uses the two exact factorizations, not a search of degree5 polynomials.
It leaves only degree4.

### The two quartic orbits exchanged by both maps

Write

    A4=X^4+X+1,
    B4=X^4+X^3+1,
    C4=X^4+X^3+X^2+X+1.

These are labels for the three irreducible quartics, not names for the integer C_p.
Their completeness and C5 arrows are in the fixed C196v3 table.
In particular chi exchanges A4 and C4, while B4 maps to1.
The map tau ALSO exchanges A4 and C4, as follows directly.
If x is a root of A4, x^4=x+1 and y=tau(x)=x^3+x satisfies

    y^2=x^3,
    y^3=x^3+x^2+x+1,
    y^4=x^3+x^2,
    y^4+y^3+y^2+y+1=0.

Hence y is a root of C4.
If x is a root of C4, x^5=1 and the same y satisfies

    y^2=x+x^2, y^4=x^2+x^4,
    y^4+y+1=0.

Thus y is a root of A4.
The target polynomials are irreducible, so these images have degree4.
Both local derivatives are units at these roots:

    tau'=(X+1)^2, chi'=phi^2.

Let the chosen source be A4 or C4, with multiplicity N_s, and let its common target under both maps have multiplicity M.
Unsaturation in(JB5) means

    N_s>3M, ord_source R=3M.

The actual composition congruences then force BOTH theta_3bar and theta_5bar to have exact source order M.
Their square and cube have orders2M and3M, both below N_s.
In the residual equation modulo the source factor to power N_s, theta_2bar^3 must therefore have order exactly2M, to cancel the unique smallest of those two known terms.
It follows that3 divides2M, hence3 divides M and M>=3.

The target is saturated for chi: it maps back to the source of multiplicity N_s>3M, so(JB5) gives target order at least M.
Counting BOTH distinct degree4 orbits yields

    deg R>=4(3M)+4M=16M>=48.                    (JB7)

No original conjugate or repeated factor is discarded in this comparison.

### The B4-to1 branch and the mandatory extra roots

Suppose the chosen source is B4.
Let N_1 be the multiplicity of the root1.
Then N_s>3N_1, the source order is3N_1, and the fixed point1 is saturated for chi with order at least N_1.
These two orbits alone give13N_1.
If N_1>=3, this is at least39.
It remains to handle N_1=2.

The exact identity

    phi(tau(X))=phi(X) B4(X)                     (JB8)

shows that tau sends every B4 root into the degree2 orbit phi.
It has local degree1 there because tau' is a unit at the B4 roots.
Also tau(1)=0.
By the full closure(JB4), both phi and0 occur in U, with multiplicities N_phi>=2 and N_0>=2.
The four orbits B4,1,phi,0 are distinct.

If N_phi were2, the source order of theta_3bar would be2, while its theta_5bar order is N_1=2.
Since N_s>6, the square and cube orders4 and6 are below N_s.
The same residual equation would force theta_2bar^3 to have order4, impossible because a finite order of a cube is divisible by3.
Thus N_phi>=3.
The general multiplicity bound gives ord_phi R>=min{3,N_phi}>=3.
The point0 is fixed by chi and is saturated, with order at least N_0>=2.
Adding all four original orbit contributions gives

    deg R>=4*6+1*2+2*3+1*2=34.                 (JB9)

This argument allows arbitrarily many primes in each cluster and any additional orbits.
Extra roots only increase the degree budget; none is assumed absent.

### Complete assembly

Every possible unsaturated source has been covered.
Degrees1 and3 are impossible; degree2 uses the adopted(H2) and gives at least41; the two exchanged quartics give at least48; B4 gives at least34; degree5 gives at least40; degree at least6 gives at least38.
Thus deg R>=34 in every nonzero case, proving(JB3).
This count retains every required repeated factor of the SAME actual canonical reduction and permits any additional factors.
No case assumes an original boundary input exists or identifies reduction degree with integer leading degree.

<a id="canonical-degree34-even-haar-consequence"></a>
## All coefficients and the full Haar normalization

If w<=33 and R were nonzero, then deg R<=w would contradict(JB3).
Therefore R=0 and every integer coefficient of G_can is divisible by2.
The condition g!=0 keeps G_can nonzero even in this zero-reduction branch.
Put

    H_1(z)=z^w (G_can/2)(z+z^(-1)).

This is a nonzero integer polynomial.
For w>=1 it has degree2w, with both leading and constant coefficient equal to the nonzero leading coefficient of G_can/2.
For w=0 it is a nonzero integer constant.
By the exact [Smy08-U001 scalar Jensen interface](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), its total logarithmic Mahler measure is at least0: its leading coefficient is a nonzero integer and each root factor contributes log^+ of its modulus.
All root multiplicities and integrable circle zeros are included.
On the circle the monomial z^w has modulus1, and G_can(z+z^(-1)) is real.
Consequently

    I_can=2log2+2 integral log|H_1(z)| dmu
         =2log2+2m(H_1)>=2log2.

This proves(JB10), including constants and zeros of G_can on the trace of the circle.
The argument does not require a bound on m(P), does not discard an original inverse pair and does not divide the logarithm by any degree.
The zero-reduction conclusion is stronger than evenness of only the leading coefficient.
It supplies no claim that G_can vanishes or that every larger degree satisfies the same restriction.

<a id="exact-inputs"></a>
## Exact fixed inputs and boundaries

| Input | Exact scope used |
| --- | --- |
| [Actual original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original P/K/F/T, same actual integer quotient polynomials, nonzero values and full residual identities. |
| [Complete per-cluster arithmetic](Yin_C_G0191_v2.md#argument) | Positive g-income in each cluster and full original exponent formula; no global-income substitution. |
| [Full residual ramification](Yin_C_G0178_v1.md#statement) | Exclusion of every unramified2-prime under both residual equations, giving all support multiplicities at least2. |
| [Exact general multiplicities](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape) | min{3,N_psi} and saturation interface at all relevant factors. |
| [Complete accepted C196 graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | Exact canonical composition, unsaturated existence, local degrees and all degree1--4 orbits; new C3 identities are proved here. |
| [Adopted quadratic-source theorem](Yin_C_G0197_v3.md#quadratic-primary-degree41-consequence) | Only the exact actual phi-unsaturated degree41 branch, with degree drop and all extra factors. |
| [Scalar Jensen and circle zeros](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact height-normalization subsection: nonzero integer H_1 including constants, full root-product measure and integrable zeros;2log2 with no degree division. |
| [Whole independent arithmetic finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Actual C191 input coverage; old author relationships remain disclosed. |
| [Whole independent multiplicity finding](../audits/reviews/Yin_R_G0473_v1.md#residual-dyadic-multiplicity-whole-finding) | Exact C196v2 fixed scope, not a new review of JB. |
| [Whole independent predecessor finding](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Exact C196v3 graph/scalar coverage and preserved old mechanisms; not evidence for the new C3 budget itself. |
| [Whole independent quadratic-source consumer finding](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Actual C197v3 QX1--QX21, all original41/52 hypotheses and disclosed overlapping upstream author roles. |
| [Earlier complete C196v3](Yin_C_G0196_v3.md#argument) | Full old CG/DQ proof, formal models and same-T higher-adic obstructions remain physically preserved with their exact scopes. |

All original primes, geometric roots and multiplicities remain accounted for in the fixed interfaces and in the new budget.
The C3 closure is proved from both actual residual equations and per-cluster C5 support; it is not assumed for an arbitrary polynomial graph.
The local quotient orders used in the quartic comparisons are strictly below their source multiplicity, so they are exact rather than unsupported equalities in tied saturation cases.
Both signs reduce to the same characteristic-two identities, while the original statement retains them separately.
The main new result is the cutoff34 and its exact w<=33 scalar consequence only.
No further cutoff increment, actual realization at34, general canonical-Haar theorem or completion of the original transfer task is asserted.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T14:27 |
| status | open |
| reason | Register the complete joint C3/C5 global degree34 budget with the actual adopted C197v3 quadratic-source input, all original multiplicities and reduction degree drop, and the full all-coefficient/every-measure Haar consequence for integer canonical degree at most33. Preserve prior physical versions and input reviews; this new consumer requires independent whole review and is not adopted here. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete original-domain conclusion](#statement) | Both exact residual signs, actual nonzero quotient values, nonzero reduction degree at least34, zero-reduction/every-coefficient consequence for w<=33, constants and full Haar>=2log2 without degree normalization or original-measure restriction. |
| argument | [Complete joint budget and scalar proof](#argument) | All JB1--JB10, actual C3/C5 closure, every possible unsaturated degree, exact quartic source/target orders and extra-root cost, fixed H2 and full scalar conversion. |
| dependency | [Actual original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original P/K/F/T, same actual integer quotient polynomials, nonzero values and full residual identities. |
| dependency | [Complete per-cluster arithmetic](Yin_C_G0191_v2.md#argument) | Positive g-income in each cluster and full original exponent formula; no global-income substitution. |
| dependency | [Full residual ramification](Yin_C_G0178_v1.md#statement) | Exclusion of every unramified2-prime under both residual equations, giving all support multiplicities at least2. |
| dependency | [Exact general multiplicities](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape) | min{3,N_psi} and saturation interface at all relevant factors. |
| dependency | [Complete accepted C196 graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | Exact canonical composition, unsaturated existence, local degrees and all degree1--4 orbits; new C3 identities are proved here. |
| dependency | [Adopted quadratic-source theorem](Yin_C_G0197_v3.md#quadratic-primary-degree41-consequence) | Only the exact actual phi-unsaturated degree41 branch, with degree drop and all extra factors. |
| dependency | [Scalar Jensen and circle zeros](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact height-normalization subsection: nonzero integer H_1 including constants, full root-product measure and integrable zeros;2log2 with no degree division. |
| support | [Whole independent arithmetic finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Actual C191 input coverage; old author relationships remain disclosed. |
| support | [Whole independent multiplicity finding](../audits/reviews/Yin_R_G0473_v1.md#residual-dyadic-multiplicity-whole-finding) | Exact C196v2 fixed scope, not a new review of JB. |
| support | [Whole independent predecessor finding](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Exact C196v3 graph/scalar coverage and preserved old mechanisms; not evidence for the new C3 budget itself. |
| support | [Whole independent quadratic-source consumer finding](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Actual C197v3 QX1--QX21, all original41/52 hypotheses and disclosed overlapping upstream author roles. |
| support | [Earlier complete C196v3](Yin_C_G0196_v3.md#argument) | Full old CG/DQ proof, formal models and same-T higher-adic obstructions remain physically preserved with their exact scopes. |
| support | [Exact current inputs and limitations](#exact-inputs) | Root/draft_comparison_cleanup new author relationship, adopted fixed H2, every prime/orbit/repetition, degree drop, scalar constants and no realization or unrestricted-transfer claim. |

### Decision whole-reviewed-2026-10-20

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T14:37 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft inquiries. |
| reason | Adopt the complete joint C3/C5 budget and full scalar consequence through actual whole consumer R478. Every nonzero canonical reduction has degree at least34; integer canonical degree at most33 forces all coefficients even and Haar logarithm at least2log2. Keep all original residual hypotheses, both signs, every residue multiplicity, reduction degree drop and the precise conditional quadratic-source input. The old physical versions and independently checked upstream scopes remain unchanged; no realization at34 or uniform original transfer is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete original-domain conclusion](#statement) | Both exact residual signs, actual nonzero quotient values, nonzero reduction degree at least34, zero-reduction/every-coefficient consequence for w<=33, constants and full Haar>=2log2 without degree normalization or original-measure restriction. |
| argument | [Complete joint budget and scalar proof](#argument) | All JB1--JB10, actual C3/C5 closure, every possible unsaturated degree, exact quartic source/target orders and extra-root cost, fixed H2 and full scalar conversion. |
| dependency | [Actual original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original P/K/F/T, same actual integer quotient polynomials, nonzero values and full residual identities. |
| dependency | [Complete per-cluster arithmetic](Yin_C_G0191_v2.md#argument) | Positive g-income in each cluster and full original exponent formula; no global-income substitution. |
| dependency | [Full residual ramification](Yin_C_G0178_v1.md#statement) | Exclusion of every unramified2-prime under both residual equations, giving all support multiplicities at least2. |
| dependency | [Exact general multiplicities](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape) | min{3,N_psi} and saturation interface at all relevant factors. |
| dependency | [Complete accepted C196 graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | Exact canonical composition, unsaturated existence, local degrees and all degree1--4 orbits; new C3 identities are proved here. |
| dependency | [Adopted quadratic-source theorem](Yin_C_G0197_v3.md#quadratic-primary-degree41-consequence) | Only the exact actual phi-unsaturated degree41 branch, with degree drop and all extra factors. |
| dependency | [Scalar Jensen and circle zeros](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact height-normalization subsection: nonzero integer H_1 including constants, full root-product measure and integrable zeros;2log2 with no degree division. |
| support | [Whole independent arithmetic finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Actual C191 input coverage; old author relationships remain disclosed. |
| support | [Whole independent multiplicity finding](../audits/reviews/Yin_R_G0473_v1.md#residual-dyadic-multiplicity-whole-finding) | Exact C196v2 fixed scope, not a new review of JB. |
| support | [Whole independent predecessor finding](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Exact C196v3 graph/scalar coverage and preserved old mechanisms; not evidence for the new C3 budget itself. |
| support | [Whole independent quadratic-source consumer finding](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Actual C197v3 QX1--QX21, all original41/52 hypotheses and disclosed overlapping upstream author roles. |
| support | [Earlier complete C196v3](Yin_C_G0196_v3.md#argument) | Full old CG/DQ proof, formal models and same-T higher-adic obstructions remain physically preserved with their exact scopes. |
| support | [Exact current inputs and limitations](#exact-inputs) | Root/draft_comparison_cleanup new author relationship, adopted fixed H2, every prime/orbit/repetition, degree drop, scalar constants and no realization or unrestricted-transfer claim. |
| review | [Whole joint-orbit consumer finding with unknown relationship](../audits/reviews/Yin_R_G0478_v1.md#joint-c3-c5-degree34-consumer-whole-finding) | Complete actual JB1--JB10, twelve input rows and all selected relations; full original closure, all degree cases, exact below-saturation orders, canonical coefficient/scalar conversion and degree drop; contributor-overlapping upstream results reuse the actual findings at their declared relationships. |

