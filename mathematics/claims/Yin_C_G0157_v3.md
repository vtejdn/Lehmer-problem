---
author: Yin
---
# Rational two-shear forms with a preserved full original norm floor

Date: 2026-10-18T13:15.
Human author Yin.
Root proposed the rational two-shear family, independent buffer, elementary norm cases, sharp abstract control and aligned original numerator.
The angular_envelope_review author developed and checked the complete arithmetic, polynomial, scalar and logarithmic account in D46.
Root and this author are contributors; neither can independently review this new complete proof.
The earlier v1/v2 authorship and actual accepted scopes remain in those preserved physical versions.
No mathematical program, parameter scan, numerical integral or new source acquisition is used here.
This is a complete author proof prepared for separate whole review, not an adopted arithmetic gate or a numerical result.

## Actual reuse and retention decision

The complete accepted C157v2, actual D36 and the J100/J101 records were read before this draft was allocated.
C157v2 has the form q[(E+sG)^2+2G^2]+q^(-1)F_0^2, with an arithmetic theorem only for integer s and q>=1.
The generalization here permits rational s,t and positive rational q, replaces F_0 by F_0+tG, and uses an independent rational coefficient b>=2 on G^2.
It retains the same defects, original trace-field domain and complete norm threshold, so this third physical version generalizes C157 while preserving the accepted v2 at its exact earlier scope.
The old fixed-s and all-parameter circle screens remain true on their old subfamily t=0,b=2q only.
They will not be asserted for the new entire parameter domain.

D36 already explains why an unchanged F_0^2 term obstructs the old shears and why a cross term involving F_0 can change its protected component.
J100 certifies the old quartic exclusion and its limited Lehmer component screen; J101 closes the old Lehmer family using two separated sets for E/G.
These are finite-input evidence for the old family, not a proof about independently moving F_0/G+t with a buffer no longer proportional to q.
No old numerical certificate is recomputed or relabeled as evidence for the new family.
The mathematical gate below is independent of those numerical signs.
The elementary square, norm and Jensen inputs are already present in accepted C153v2, C149 and C157v2.
Their actual pairwise exclusions, trace quotients, original phases and scalar conventions were reread and matched before freeze.

<a id="rational-two-shear-statement"></a>
## Statement

Let F be a totally real number field of degree r and let a_0,b_0,c_0 be nonzero algebraic integers in F.
Put

    e=b_0^2-a_0^3, f=2c_0^2-3a_0^5, g=c_0^3-2b_0^5.

For rational s,t, rational q>0 and rational b>=2 define

    Q_(s,t,q,b)=q(e+s g)^2+q^(-1)(f+t g)^2+b g^2.

Then this element is totally positive and

    Norm_F(Q_(s,t,q,b))>=2^r.                       (1)

The element itself is not asserted integral.
The rational parameters are fixed under every embedding.
The constant b=2 is the least buffer that can give this floor uniformly over all allowed triples and all s,t,q in the abstract theorem.
This sharpness statement is not an assertion that the extremal triple is realized by the original-polynomial construction below.

Let P be an original monic irreducible reciprocal nontorsion integer polynomial of even degree d=2r and constant coefficient1, with actual trace field F=Q(alpha+alpha^(-1)) totally real.
Use the exact C153v2 nonzero integral trace quotients a_0,b_0,c_0.
This domain includes every genuine Salem input by the accepted actual trace-field proof in C153v2; reciprocal degree2 inputs are covered without being called Salem numbers.
Define the original unreduced polynomials and common-phase numerators

    H23(z)=9P(z^2)^3-8P(z^3)^2,
    H25(z)=75P(z^2)^5-64P(z^5)^2,
    H35(z)=250P(z^3)^5-243P(z^5)^3,
    L=972000,
    X(z)=13500 z^(9d/2)H23(z),
    Y_0(z)=1215 z^(5d/2)H25(z),
    Z(z)=32H35(z).

Choose ANY positive integer D clearing the coefficients of the rational quadratic form

    qX^2+q^(-1)Y_0^2+2qs XZ+2q^(-1)t Y_0 Z
                 +(qs^2+q^(-1)t^2+b)Z^2.

Equivalently, require all five numbers Dq,D/q,2Dqs,2Dt/q and D(qs^2+t^2/q+b) to be integers.
Such a D exists for every stated rational parameter choice.
Put

    A_(s,t,q,b,D)(z)
       =D[q(X+sZ)^2+q^(-1)(Y_0+tZ)^2+bZ^2],
    B_(s,t,q,b)(z)=z^(-15d)A_(s,t,q,b,D)(z)/(D L^2).

Then A is an integer reciprocal polynomial of exact degree30d, with equal leading and constant coefficient

    50176 D(qs^2+q^(-1)t^2+b)>0.                   (2)

B is independent of the chosen clearing integer and has centered support[-15d,15d].
Its actual original value is Q_(s,t,q,b), and, with K=Q(alpha),

    Norm_K(B(alpha))=Norm_F(Q_(s,t,q,b))^2>=2^d,
    Norm_K(B(alpha))=Res(P,A)/(D L^2)^d.             (3)

Neither the algebraic value B(alpha) nor its quotient by2 is asserted integral.
Every original conjugate and all proper-subfield multiplicities are retained.

On the unit circle use the REAL centered functions

    E(z)=-z^(-3d)H23(z)/72,
    F_0(z)=-z^(-5d)H25(z)/800,
    G(z)=-z^(-15d/2)H35(z)/30375.

They satisfy the exact global Laurent identity

    B=q(E+sG)^2+q^(-1)(F_0+tG)^2+bG^2.             (4)

The circle identity and the next integrability/screen statements also make sense for real s,t, real q>0 and real b>=2, without importing the rational arithmetic theorem into that larger parameter domain.
The logarithm is integrable, allowing possible circle zeros, and

    I_(s,t,q,b)=integral log B dmu
        =m(A)-log D-2log L,                        (5)
    I_(s,t,q,b)>=log b+J_G,
    J_G=integral log G^2=2m(H35)-2log30375.         (6)

The Jensen identity in (5) is stated for the integer A and rational parameters above, retaining its leading coefficient and all root multiplicities.
For real parameters its real-coefficient polynomial analogue also holds, but supplies no arithmetic assertion.
For the rational arithmetic domain the complete supremum return is

    log2<=log Norm_K(B(alpha))/d
         <=log sup_circle B+30m(P).                (7)

No replacement of the supremum by the Haar mean is claimed.
For fixed s,t,q and P, the circle symbol is nondecreasing in b, so b=2 is optimal within this universally certified buffer range when seeking a small Haar logarithm.
This does not assert the existence of a parameter giving I<log2.

<a id="argument"></a>
<a id="rational-two-shear-proof"></a>
## 1. All arithmetic cases and sharp universal buffer

The accepted [C153v2 pairwise exclusions](Yin_C_G0153_v2.md#argument) give e!=0 and f!=0 whenever g=0.
If g!=0, then g has no zero image at any real embedding and

    sigma(Q)>=b sigma(g)^2>=2sigma(g)^2>0.

Multiplication over all r embeddings yields Norm_F(Q)>=b^r Norm_F(g)^2>=2^r, because the full norm of the nonzero integer g is a nonzero integer.
No condition on e+s g or f+t g is needed in this case.
If g=0, then at every real embedding

    sigma(Q)=q sigma(e)^2+q^(-1)sigma(f)^2
             >=2abs(sigma(e)sigma(f))>0.

Multiplying gives Norm_F(Q)>=2^r abs(Norm_F(e)Norm_F(f))>=2^r.
These cases exhaust the field element g=0 or g!=0, rather than choosing a different defect separately at each embedding.
All rational parameters remain fixed under every sigma; no transformed expression is required to be an algebraic integer.
This proves (1), including arbitrarily small or large positive rational q and arbitrary rational shifts of either sign.

For sharpness in the abstract triple theorem take F=Q and a_0=b_0=c_0=1.
Then (e,f,g)=(0,-1,-1).
Choose s=0 and t=-1, with any rational q>0.
Both shifted squares vanish and Q=b.
For any rational buffer b<2 its norm is below2, disproving a uniform threshold2 over those parameters; buffers that are nonpositive also fail positivity.
The claim of least admissible universal buffer is therefore exact, while no polynomial input realizing this triple is assumed.

<a id="original-return"></a>
## 2. Actual original phases, all endpoints and norm multiplicities

Use [C153v2's actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain), its trace polynomial T, original trace generator and [K:F]=2.
Explicitly, with x=alpha+alpha^(-1) and C_0(x)=2,C_1(x)=x,C_(j+1)=xC_j-C_(j-1), the three elements are the values of rem_T(T(C_2)/2), rem_T(T(C_3)/3) and rem_T(T(C_5)/5) at x.
Their integrality and nonvanishing use exactly that accepted original trace-quotient construction, including every phase removed from the nonzero base quotients.
Its integral nonzero quotients evaluate to a_0,b_0,c_0, and the exact C149/C153v2 identities give

    H23(alpha)=-72 alpha^(3d)e,
    H25(alpha)=-800 alpha^(5d)f,
    H35(alpha)=-30375 alpha^(15d/2)g.

The [C149 original numerator interface](Yin_C_G0149_v1.md#original-polynomials-and-norms) gives degrees6d,10d,15d and leading coefficients1,11,7 respectively.
Reciprocity of P makes each numerator reciprocal, so its constant coefficient is the same as its leading coefficient.
These are the original unreduced polynomials; reduction modulo T identifies only their actual values, not global circle expressions.
The half-degree shifts are integers because d is even.
Each real reciprocal H centered at half its degree is real on the circle.
Thus E,F_0,G are real there and evaluate at alpha to e,f,g.

As GLOBAL Laurent identities, all three aligned numerators have the same phase:

    X=-L z^(15d/2)E,
    Y_0=-L z^(15d/2)F_0,
    Z=-L z^(15d/2)G.

Squaring the two shifted sums and the buffer proves (4) exactly.
X has support[9d/2,21d/2], Y_0 has support[5d/2,25d/2], and Z has support[0,15d].
All have reciprocal center15d/2.
The quadratic form is reciprocal about15d; only its Z^2 coefficient reaches either endpoint0 or30d.
Since the endpoint coefficient of Z is224, its square is50176.
The positive coefficient qs^2+q^(-1)t^2+b proves (2), with no cancellation or degree drop at any allowed parameters.
The five cleared coefficients make A integral, whether or not its chosen scalar D is minimal.
The supplied D is retained in every scalar and norm formula.

At alpha, (4) gives B(alpha)=Q.
The norm tower and [K:F]=2 give the first identity (3).
The monic even-degree P has constant coefficient1, so Norm_K(alpha)=1.
Taking its full norm in the centered Laurent identity gives the exact resultant identity in (3), including the entire factor(DL^2)^d.
No substitution of the actual own degree of Q, an angular conjugate list or a shortened trace orbit occurs.

<a id="logarithmic-screen"></a>
## 3. Integrable logarithms, Jensen and the complete radial fee

For every real parameter choice in the stated circle domain, B>=bG^2>=2G^2.
The polynomial H35 is nonzero, with degree15d and leading coefficient7, so it has at most finitely many circle zeros of finite order.
Its logarithm is integrable; hence log(bG^2) is an integrable lower bound for log B almost everywhere.
The continuous nonnegative B is bounded above and cannot vanish outside that finite set.
Therefore log B is integrable even if some of those zeros persist.
The accepted [C_F6 scalar Laurent Jensen identity](Yin_C_F0006_v1.md#scalar-capacity-normalization) with |z|=1 gives (5) and (6), including every leading coefficient and root multiplicity.
Replacing D by a positive integer multiple multiplies A by the same scalar and adds its logarithm to m(A), so the normalized identity is unchanged.
No denominator or polynomial content is silently discarded.

Let M_B=sup_circle B>0.
On the circle |A|=D L^2 B.
The maximum principle on the disk and the same bound for the reciprocal degree30d polynomial give

    abs(B(z))<=M_B max(abs(z),abs(z)^(-1))^(15d)

for every nonzero z.
Applying this to ALL d original roots and using sum abs(log abs(alpha_i))=2m(P) gives (7).
The centered degree is15d on each side, and the resulting normalized radial fee is30m(P).
This is a supremum return only, with no original-root/Haar estimate or new Fourier budget.

<a id="retained-old-subfamily"></a>
## 4. Exactly retained old subfamily and old finite exclusions

For integer s and integer q>=1 set t=0,b=2q and choose D=q.
Then all five cleared quadratic coefficients are integers and

    A=q^2[(X+sZ)^2+2Z^2]+Y_0^2,
    B=q[(E+sG)^2+2G^2]+q^(-1)F_0^2,

exactly the old C157v2 numerator, denominator qL^2 and centered circle form.
The abstract old element H_(s,q) equals qQ, so (1) recovers Norm_F(H_(s,q))>=(2q)^r.
No formerly accepted integer-parameter conclusion is lost.

For the old circle subfamily t=0,b=2q, its real s and q>0 identities retain the C157v2 component screens even when b=2q<2 and the new general buffer theorem does not apply there.
In that subfamily define U_s=(E+sG)^2+2G^2 and V=F_0^2.
Then, with J_U(s)=integral log U_s and J_V=integral log V,

    I>=log2+(J_U(s)+J_V)/2,
    I>=3log2/2+(J_G+J_V)/2.

Their integrable-zero proofs are unchanged: U_s>=2G^2, V=F_0^2, and qU_s+q^(-1)V>=2sqrt(U_s V) almost everywhere.
Taking logarithms and integrating gives the first inequality; J_U(s)>=log2+J_G gives the second.
The exact old scalar normalizations are retained as well:

    A_(U,s)=(X+sZ)^2+2Z^2,
    J_U(s)=m(A_(U,s))-2log L,
    J_V=2m(H25)-2log800,
    I=m(q^2 A_(U,s)+Y_0^2)-log q-2log L.

The latter original integer-polynomial normalization is for integer s,q with q>=1; its real-coefficient Jensen analogue remains a circle identity for real s and q>0.
These are statements about the explicitly identified old circle forms, not about every new(s,t,q,b).
J100 and J101 certify exclusions on the two fixed controls only for that old family.
J101's T=E/G two-set correction is not a certificate for the new independently shifted F_0/G+t expression.
The existing [J100 component certificate](../computations/programs/Yin_J_G0100/readme.md#certified-results) and [J101 two-set certificate](../computations/programs/Yin_J_G0101/readme.md#certified-results) retain their original scopes; this version asserts no new numerical sign.

<a id="paid-source-cost"></a>
## 5. Paid source cost and exact remaining transfer gap

For the new rational gate put the ordinary rational auxiliary f=A/(2D L^2).
Then Norm_K(f(alpha))=Norm_K(B(alpha))/2^d>=1 because the removed phase alpha^(15d) has norm1.
Its Haar cost is m(f)=I-log2, and its exact ordinary degree is30d.
These are exact arithmetic and scalar identities, not a completed uniform transfer theorem.
The existing [C140 normalized sparse theorem](Yin_C_G0140_v1.md#statement) supplies a comparison boundary for this normalization.
The printed accepted C140 theorem requires an integral normalized value as well as uniformly bounded term count and normalized coefficient l1 norm.
Those hypotheses are not supplied here: a fixed number of squares or parameters gives no such bound for the expanded P-dependent numerator, and the original algebraic value need not become integral after division by2.
No C140 conclusion or unreviewed proof adaptation is invoked as a premise of this gate.
A positive Haar saving would still need a separately justified original-root transfer with actual coefficient/support or alternative regularization/Fourier budgets.
The coefficient scalar, all original norm factors, full polynomial degree and radial fee remain paid.

## Complete author check and exact limits

The actual C153v2 pairwise and trace interfaces, C149 numerator phases and F109 scalar Jensen statement were reread and matched.
The author checked the rational field domain, both exhaustive g cases, abstract-only buffer sharpness, all five coefficient-clearing conditions, common negative phase, original degree30d and both endpoints, full scalar/resultant powers, integrable zeros, the old real-q circle boundary and the exact30m fee.
The abstract sharpness triple is not an asserted original-polynomial realization.
The new arithmetic conclusion does not require integrality of either shifted term or of the resulting value.
The separate old circle screens are retained only on t=0,b=2q, including their real q<1 scope where the new b>=2 theorem is not invoked.
The existing two fixed-input exclusions therefore do not close this larger family.
No Haar-saving parameter, complete parameter optimum, new numerical sign, uniform original-root/Haar transfer or unrestricted Mahler gap is asserted.
The source proof-reading boundaries of all reused inputs remain unchanged.
The separate finite-test proposal belongs to the continuing working/J material and is not evidence for this theorem.

## Current assessment
[Selected decision](#decision-current-haar-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T13:15 |
| status | open |
| reason | Generalize accepted C157v2 to rational shifts in both defect components, arbitrary positive rational q and an independent rational buffer b>=2. Preserve the full original norm floor, exact degree/scalar/radial costs and old component screens at their old subfamily only. Root and the author contribute; separate whole review precedes gate adoption and any finite new-family run. No numerical sign, original transfer or unrestricted gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete rational two-shear statement](#statement) | All nonzero integral triples in a totally real field, rational s,t,q,b in their exact domains, universal buffer sharpness, actual original trace input, exact polynomial/norm/Jensen/radial costs, integrable circle screen and old-subfamily preservation. |
| argument | [Complete proof and paid source boundary](#argument) | All five sections and author limits; exhaustive g cases, original phases and five coefficient-clearing conditions, exact reciprocal endpoints and denominator powers, full norms, logarithmic zeros, supremum return, old subfamily and absent transfer hypotheses. |
| dependency | [Totally real pairwise exclusions](Yin_C_G0153_v2.md#argument) | Only e=g=0 and f=g=0 are impossible for nonzero a_0,b_0,c_0; no transformed singleton or C155 norm estimate is used. |
| dependency | [Actual trace domain and phases](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Nonzero integral trace quotients, actual degrees r and2r, quadratic K/F, exact phases and Salem total-reality coverage. |
| dependency | [Original numerator formulas](Yin_C_G0149_v1.md#original-polynomials-and-norms) | H23,H25,H35, supplied denominators, exact degrees and leading coefficients; reciprocity and common phase reconstructed here. |
| dependency | [Scalar Laurent Jensen formula](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Full nonmonic scalar, every root multiplicity and finite-order circle-zero integrability; no optimization theorem is invoked. |
| dependency | [Accepted old buffered subfamily](Yin_C_G0157_v2.md#statement) | Exact t=0,b=2q specialization, integer s/q arithmetic and separately all-real-s/all-positive-q component screens and scalar normalizations; no transfer of those screens to arbitrary moving t or independent b. |
| support | [Existing component-only fixed controls](../computations/programs/Yin_J_G0100/readme.md#certified-results) | Prior quartic all-parameter exclusion and limited Lehmer screen for the old family only; no new component calculation or certificate for this generalized family. |
| support | [Existing two-set Lehmer closure](../computations/programs/Yin_J_G0101/readme.md#certified-results) | Previously certified E/G phase-set correction closes the old real-s/positive-q family on Lehmer; not a certificate for moving F_0/G+t or a fixed independent buffer. |
| support | [Accepted sparse transfer boundary](Yin_C_G0140_v1.md#statement) | Comparison only: actual integral normalized value, uniform term count and normalized coefficient budget are required by its printed statement and are not supplied here; exact norm-only/source-cost identities do not invoke that theorem. |

### Decision whole-reviewed-2026-10-18

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T13:20 |
| status | proved |
| reason | Adopt the complete rational two-shear and independent-buffer generalization after R396 whole noncontributor review. All rational domains, complete norms, abstract buffer sharpness, original trace phases, exact integer numerator/denominator/endpoints, integrable logarithms, old-subfamily screens and the full radial/source cost are covered. This authorizes its use as the mathematical gate for the separately declared bounded J102 diagnostic, without claiming a numerical sign, original-root/Haar transfer or unrestricted gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete rational two-shear statement](#statement) | All nonzero integral triples in a totally real field, rational s,t,q,b in their exact domains, universal buffer sharpness, actual original trace input, exact polynomial/norm/Jensen/radial costs, integrable circle screen and old-subfamily preservation. |
| argument | [Complete proof and paid source boundary](#argument) | All five sections and author limits; exhaustive g cases, original phases and five coefficient-clearing conditions, exact reciprocal endpoints and denominator powers, full norms, logarithmic zeros, supremum return, old subfamily and absent transfer hypotheses. |
| dependency | [Totally real pairwise exclusions](Yin_C_G0153_v2.md#argument) | Only e=g=0 and f=g=0 are impossible for nonzero a_0,b_0,c_0; no transformed singleton or C155 norm estimate is used. |
| dependency | [Actual trace domain and phases](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Nonzero integral trace quotients, actual degrees r and2r, quadratic K/F, exact phases and Salem total-reality coverage. |
| dependency | [Original numerator formulas](Yin_C_G0149_v1.md#original-polynomials-and-norms) | H23,H25,H35, supplied denominators, exact degrees and leading coefficients; reciprocity and common phase reconstructed here. |
| dependency | [Scalar Laurent Jensen formula](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Full nonmonic scalar, every root multiplicity and finite-order circle-zero integrability; no optimization theorem is invoked. |
| dependency | [Accepted old buffered subfamily](Yin_C_G0157_v2.md#statement) | Exact t=0,b=2q specialization, integer s/q arithmetic and separately all-real-s/all-positive-q component screens and scalar normalizations; no transfer of those screens to arbitrary moving t or independent b. |
| support | [Existing component-only fixed controls](../computations/programs/Yin_J_G0100/readme.md#certified-results) | Prior quartic all-parameter exclusion and limited Lehmer screen for the old family only; no new component calculation or certificate for this generalized family. |
| support | [Existing two-set Lehmer closure](../computations/programs/Yin_J_G0101/readme.md#certified-results) | Previously certified E/G phase-set correction closes the old real-s/positive-q family on Lehmer; not a certificate for moving F_0/G+t or a fixed independent buffer. |
| support | [Accepted sparse transfer boundary](Yin_C_G0140_v1.md#statement) | Comparison only: actual integral normalized value, uniform term count and normalized coefficient budget are required by its printed statement and are not supplied here; exact norm-only/source-cost identities do not invoke that theorem. |
| review | [Whole independent rational two-shear finding](../audits/reviews/Yin_R_G0396_v1.md#rational-two-shear-whole-independent-finding) | Entire fixed statement, all five argument sections and every declared dependency/support interface; rational parameter scope, complete original costs, old real-q subfamily and missing transfer hypotheses are explicitly checked. |

### Decision current-haar-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:45 |
| status | proved |
| reason | Select adopted C_F6 as the current complete responsible home of the identical retained scalar Haar/Jensen normalization. Its actual selected adoption and complete normalization section were read and matched to the original fixed L_F5 text, including Laurent shifts, leading coefficients, all root multiplicities and integrable circle zeros. Only that normalization is reused here, with every original scalar, phase and cost retained; no Gram optimization, root-distribution transfer or new review is supplied. Mathematical status, statement, full argument, selected findings and every relation scope remain unchanged; original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete rational two-shear statement](#statement) | All nonzero integral triples in a totally real field, rational s,t,q,b in their exact domains, universal buffer sharpness, actual original trace input, exact polynomial/norm/Jensen/radial costs, integrable circle screen and old-subfamily preservation. |
| argument | [Complete proof and paid source boundary](#argument) | All five sections and author limits; exhaustive g cases, original phases and five coefficient-clearing conditions, exact reciprocal endpoints and denominator powers, full norms, logarithmic zeros, supremum return, old subfamily and absent transfer hypotheses. |
| dependency | [Totally real pairwise exclusions](Yin_C_G0153_v2.md#argument) | Only e=g=0 and f=g=0 are impossible for nonzero a_0,b_0,c_0; no transformed singleton or C155 norm estimate is used. |
| dependency | [Actual trace domain and phases](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Nonzero integral trace quotients, actual degrees r and2r, quadratic K/F, exact phases and Salem total-reality coverage. |
| dependency | [Original numerator formulas](Yin_C_G0149_v1.md#original-polynomials-and-norms) | H23,H25,H35, supplied denominators, exact degrees and leading coefficients; reciprocity and common phase reconstructed here. |
| dependency | [Scalar Laurent Jensen formula](Yin_C_F0006_v1.md#scalar-capacity-normalization) | Full nonmonic scalar, every root multiplicity and finite-order circle-zero integrability; no optimization theorem is invoked. |
| dependency | [Accepted old buffered subfamily](Yin_C_G0157_v2.md#statement) | Exact t=0,b=2q specialization, integer s/q arithmetic and separately all-real-s/all-positive-q component screens and scalar normalizations; no transfer of those screens to arbitrary moving t or independent b. |
| support | [Existing component-only fixed controls](../computations/programs/Yin_J_G0100/readme.md#certified-results) | Prior quartic all-parameter exclusion and limited Lehmer screen for the old family only; no new component calculation or certificate for this generalized family. |
| support | [Existing two-set Lehmer closure](../computations/programs/Yin_J_G0101/readme.md#certified-results) | Previously certified E/G phase-set correction closes the old real-s/positive-q family on Lehmer; not a certificate for moving F_0/G+t or a fixed independent buffer. |
| support | [Accepted sparse transfer boundary](Yin_C_G0140_v1.md#statement) | Comparison only: actual integral normalized value, uniform term count and normalized coefficient budget are required by its printed statement and are not supplied here; exact norm-only/source-cost identities do not invoke that theorem. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0396_v1.md#rational-two-shear-whole-independent-finding) | Entire fixed statement, all five argument sections and every declared dependency/support interface; rational parameter scope, complete original costs, old real-q subfamily and missing transfer hypotheses are explicitly checked. |
