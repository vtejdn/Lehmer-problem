---
author: Yin
---
# Finite Haar-saving costs for geometric polynomial shears

Human author Yin.
The complete author proof was first retained in D36 at2026-10-20T11:01.
Root supplied the pointwise geometric-family comparison and necessary Haar-budget formula, and proposed the finite-saving research question.
The draft_comparison_cleanup agent supplies the signed-moment argument, complete coefficient/annihilator adaptations and original-cost deductions.
This candidate is registered for separate whole review; neither contributor selects its acceptance here.

<a id="statement"></a>
## Complete statement

Let P be an actual monic irreducible reciprocal nontorsion polynomial in Z[z], of even degree d>=2 and constant1, with root alpha and totally real F=Q(alpha+alpha^(-1)).
Put K=Q(alpha), m=m(P)>0, and use normalized unit-circle Haar measure mu.
Define the complete unreduced polynomials and centered real Laurent functions

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    E=-z^(-3d)H23/72, F_0=-z^(-5d)H25/800,
    G=-z^(-15d/2)H35/30375,
    G1=||H35||_1/30375,
    delta=||H35||_2^2/||H35||_1^2,
    p0=|coefficient of z^0 in G|/G1,
    A0=(||H23||_1/72)^2+(||H25||_1/800)^2.

Coefficient norms use all collected coefficients; l2 equals Haar L2 after the stated scalar and monomial normalizations.
Thus0<delta<=1 and p0<=sqrt(delta).
For EVERY rational c>G1^2 and integer N>=0 let

    xi=G1^2/c, u=G^2/c,
    B_base=E^2+F_0^2+2G^2,
    B_N=(E^2+F_0^2)(1-u)^(2N+2)+2G^2,
    I_base=integral log B_base dmu, I_N=integral log B_N dmu,
    L_c=integral -log(1-u) dmu,
    Phi(x)=x[3+2log(1/x)] for0<x<=1.

The usual circle choice c=1+G1^2 is included.
B_base is the untransformed symbol, whereas B_0 is the first geometric symbol.

**A. Complete moment and distribution bound.**
If p0<=1/2, then for every integer k>=1,

    integral (G/G1)^(2k) dmu
       <=min{delta, binom(2k,k)/4^k}
       <=min{delta,(k+1)^(-1/2)},
    0<L_c<=Phi(delta).

The condition is automatic when delta<=1/4.
For every delta without that condition one still has xi delta<=L_c<=delta[-log(1-xi)].
The scale-independent bound retains arbitrary coefficient signs and imposes no degree, coefficient-height or denominator bound.

**B. Necessary finite geometric step count.**
For every N,

    0<=I_base-I_N<=2(N+1)L_c,
    0<=I_0-I_N<=2N L_c.

Consequently under p0<=1/2, a supplied eta>0 with I_base-I_N>=eta forces

    N>=max{0,ceil[eta/(2Phi(delta))]-1}.

Improvement eta relative to I_0 instead forces N>=ceil[eta/(2Phi(delta))].
To infer a needed improvement from the target I_N<=log2-eta one must retain the actual difference I_base-log2+eta; no general I_base>=log2 premise is supplied.
These lower bounds concern only this geometric sequence, not arbitrary polynomial shears.

**C. Exact original-input conditions.**
Use the accepted C92 constants and function, here written explicitly:

    c0=log2/4, h0=c0 exp(-20),
    b(t)=max{t,sqrt(t/c0)log sqrt(c0/t)},
    epsilon(t)=min{1,15sqrt(b(t))+4t}, 0<t<=h0,
    V(t)=[epsilon(t)+2t]/[1+epsilon(t)].

If the ACTUAL original defect g=G(alpha) is zero and0<15m<=h0, then delta<=V(15m).
If all coefficients of P(sigma z) are nonnegative for one sigma in{1,-1} and0<m<=h0, then delta<=(277/223)^2 V(m).
More generally put H=||P||_1 and beta(P)=||H35||_1/(250H^5+243H^3).
For0<m<=h0, delta<=V(m)/beta(P)^2, and the sign condition automatically gives beta(P)>=223/277.
Whenever one of these explicit upper bounds for delta is at most1/4, it can replace delta inside the increasing Phi in part B.
Along any hypothetical permitted sequence with m tending to0 and a fixed positive required Haar improvement, the first two conditions force N to infinity.
They assert no such sequence exists, no g=0 example is constructed, and no new Mahler-gap coverage follows.
The sign class is nonempty at fixed positive measure by the accepted L265 quartic under z maps to-z, as checked in the proof.

**D. Complete original cost and the prescribed safe cutoff.**
The exact C176 original return retains the numerator A_N, denominator D_N and nonzero endpoints in(V11), with

    deg A_N=(60N+80)d,
    Norm_K(B_N(alpha))=Res(P,A_N)/D_N^d>=2^d.

Thus the necessary N divergence in part C forces this construction's ordinary degree divided by d to diverge.
Its complete coefficients, denominators, radial bound and normalized coefficient upper budget remain exactly(V11), without treating an upper budget as a necessary growth rate.
For the PARTICULAR C177 cutoff

    R=1+max_(j<d)|p_j|>=2,
    c_*=1+G1^2 R^(15d),

one has L_(c_*)<=2delta R^(-15d), so any improvement eta from B_base necessarily requires

    N+1>=eta R^(15d)/(4delta).

This cutoff prevents expansion at the actual original embeddings but is not claimed minimal, and the exponential necessity is not transferred to every legal c.
The existing C177 Fourier lower bound is retained in(V13) only with its circle-zero hypothesis and full input-dependent threshold and subtraction.
No automatic upper transfer budget, unconditional signed-cancellation bound, general-shear obstruction or unrestricted D36/G0001 conclusion is asserted.

<a id="exact-inputs"></a>
## Exact inputs and scope

| Input | Actual role |
| --- | --- |
| [C176 geometric family](Yin_C_G0176_v1.md#polynomial-shear-exact-infimum) | Complete actual domain, real centered functions, geometric identity, integrable logarithms, all original norms, exact degree/endpoint/denominator and coefficient budgets. |
| [C177 original and Fourier price](Yin_C_G0177_v1.md#argument) | General rational c, actual original-root expansion and safe cutoff, and Fourier lower bound only at its precise circle-zero threshold. |
| [C92 effective-support theorem](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Actual rational annihilators P or H35, original degree d, full span d or15d, explicit epsilon domain and growing effective support; not only bounded literal support. |
| [C522 complete cosine moment calculation](Yin_C_G0522_v1.md#original-binary-degree-block-holder) | Exact central-binomial integral and its elementary induction, without the different affine-growth conclusions. |
| [L265 actual quartic](../ledger/Yin_L_G0265_v1.md#trace-unit-orbit-fixed-scope) | Nonempty sign-coefficient class at fixed positive measure; no near-one sequence. |
| [Complete comparison in C574](Yin_C_G0574_v2.md#statement) | Existing effective-support/coherence boundaries; no new gap from a reformulated bounded-complexity condition. |
| [L318 bundle bound](Yin_C_G0600_v1.md#weighted-integral-bundle-bound) | Reuse screen for fully paid signed correlation and original norm costs, not a new logical premise for the moment inequality. |
| [C140 sparse transfer](Yin_C_G0140_v1.md#statement) | Existing sufficient degree/term/normalized-coefficient conditions remain unprovided; no automatic transfer from a favorable Haar value. |
| [C42 scalar recipe price](Yin_C_G0042_v2.md#quadratic-damping-fixed-recipe-order-boundary) | Comparison with a different scalar full-interval filter, not an input to the present distribution proof. |

<a id="argument"></a>
## Complete retained author argument

<a id="geometric-finite-saving-distribution-cost"></a>
## Finite geometric saving, normalized coefficient concentration and necessary degree

Date: 2026-10-20T11:01.
Human author Yin.
Root supplied the pointwise geometric-family comparison and necessary Haar-budget formula, and asked for a finite-saving discriminator with the original costs retained.
The draft_comparison_cleanup agent supplies the signed-moment proof, the original coefficient and annihilator interfaces, and the necessary cost deductions below.
This is author work awaiting separate whole review.
No parameter scan, numerical integral, polynomial search or new source acquisition is performed.

### Reuse and the exact changed question

The complete [L430 effective-support and coherence comparison](../ledger/Yin_L_G0430_v1.md) and [L318 signed bundle theorem](Yin_C_G0600_v1.md#weighted-integral-bundle-bound) were read first.
They retain signed correlation costs and distinguish necessary coefficient dispersion from a missing arithmetic upper estimate; neither is a distribution bound for the present G.
The [C140 normalized sparse transfer](Yin_C_G0140_v1.md#statement), [C176 exact shear construction](Yin_C_G0176_v1.md#polynomial-shear-exact-infimum), and [C177 actual original-root/Fourier prices](Yin_C_G0177_v1.md#argument) retain their existing scopes.
This continuation asks how much Haar improvement a finite number of the prescribed geometric steps can produce, not whether the full shear infimum exists.
The central-binomial cosine identity and its elementary induction are already retained in [C522](Yin_C_G0522_v1.md#original-binary-degree-block-holder); they are reused below.
[C92's effective-support theorem](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) will supply the exact original-input arithmetic condition, without a fixed term-count assumption.
The [C42 fixed scalar damping price](Yin_C_G0042_v2.md#quadratic-damping-fixed-recipe-order-boundary) is a comparison for a different full-interval recipe; it does not supply the actual Haar-distribution estimate proved here.
This bounded reuse screen does not claim mathematical novelty or a new Mahler-gap domain.

Keep an actual monic irreducible reciprocal nontorsion integer-unit P of even degree d, constant1, root alpha and totally real trace field Q(alpha+alpha^(-1)).
Use the exact real centered Laurent polynomials E,F_0,G of C176, with

    H35=250P(z^3)^5-243P(z^5)^3,
    G=-z^(-15d/2)H35/30375,
    G1=||H35||_1/30375>0,
    delta=||G||_2^2/G1^2=||H35||_2^2/||H35||_1^2,
    p0=|coefficient of z^0 in G|/G1,
    A0=(||H23||_1/72)^2+(||H25||_1/800)^2.          (V1)

Here coefficient l1 and coefficient l2 are for the complete collected polynomial, and l2 equals normalized Haar L2 by Parseval.
In particular0<delta<=1 and p0<=sqrt(delta).
All signs in G are retained; no positivity of its coefficients is assumed.

For ANY rational c>G1^2, put

    xi=G1^2/c in(0,1), u=G^2/c,
    B_base=E^2+F_0^2+2G^2,
    B_N=(E^2+F_0^2)(1-u)^(2N+2)+2G^2,
    I_base=integral log B_base, I_N=integral log B_N,
    L_c=integral -log(1-u), N>=0.                 (V2)

Both c=1+G1^2 and the larger C177 original-root cutoff belong to this domain.
B_base is the untransformed symbol; it is NOT C176's B_0, which already contains one geometric step.
All these logarithms are integrable by the exact nonzero G lower bound from C176, and1-u is strictly positive on the entire circle.

### Complete signed-moment estimate

For0<x<=1 define

    Phi(x)=x[3+2log(1/x)].

If p0<=1/2, then for every integer k>=1,

    integral (G/G1)^(2k)
       <=min{delta, I_k},
    I_k=binom(2k,k)/4^k<=(k+1)^(-1/2),
    0<L_c<=Phi(delta).                            (V3)

The condition p0<=1/2 is automatically satisfied when delta<=1/4.
No degree, coefficient height, rational denominator or factor log c occurs in this upper bound.

Here is the full proof, including the signed constant term.
Write the real symmetric Laurent polynomial Q=G/G1 as

    Q(e^(i theta))=a0+2sum_(j>=1) a_j cos(j theta),
    |a0|+2sum_(j>=1)|a_j|=1.

Put p=|a0|, choose s0 in{1,-1} with a0=s0 p, and choose signs s_j for the nonzero a_j.
For p<=1/2 the nonconstant coefficient mass1-p is positive.
Define w_j=2|a_j|/(1-p), so the nonzero weights sum to1 and

    Q=sum_j w_j[s0 p+(1-p)s_j cos(j theta)].

The function x maps to x^(2k) is convex on all real numbers.
Applying this pointwise and using Haar invariance under every integer frequency and under a cosine sign change gives

    integral Q^(2k)<=integral[p+(1-p)cos theta]^(2k).

The sign s0 is harmless because the power is even and cos theta has the same distribution as its negative.
For0<=p<=1/2,

    p+(1-p)cos theta
       =(1-2p)cos theta+2p(1+cos theta)/2.

A second application of the same real convexity gives the upper integral

    (1-2p) I_k+2p I_(2k)<=I_k.

Indeed (1+cos theta)/2=cos^2(theta/2), and its2k-th power has Haar mean I_(2k).
The coefficient identity I_k=binom(2k,k)/4^k and the induction I_k<=(k+1)^(-1/2) are the existing elementary L215 calculation; I_(2k)<=I_k also follows pointwise from even cosine powers.
Since |Q|<=1, its2k moment is separately at most its second moment delta.
This proves both bounds in(V3) for every signed coefficient configuration.

The nonnegative logarithmic series can be integrated termwise, since0<=xi Q^2<1, giving

    L_c=sum_(k>=1) xi^k integral Q^(2k)/k
       <=sum_(k>=1) min{delta/k,k^(-3/2)}.

The function min{delta/x,x^(-3/2)} decreases for x>=1.
Its crossover is x=delta^(-2)>=1, so its first value plus its integral bounds the sum by

    delta+integral_1^(delta^-2) delta/x dx
          +integral_(delta^-2)^infinity x^(-3/2) dx
       =delta[3+2log(1/delta)].

This avoids any rounded cutoff or omitted endpoint term.
Phi is increasing on(0,1], since Phi'(x)=1+2log(1/x)>0, and Phi(x) tends to0 as x tends to0.
A single cosine has p0=0 and delta=1/2 and is covered by the explicit p0 version, although not by the sufficient delta<=1/4 shortcut.
A constant Q=1 or-1 has p0=delta=1 and is excluded: its L_c=-log(1-xi) can grow without bound.
Thus the constant-term condition cannot be silently dropped.

For later comparison the ordinary convex chord gives, for every delta and without the p0 restriction,

    xi delta<=L_c<=delta[-log(1-xi)].              (V4)

For c=1+G1^2 this upper bound is delta log c.
This is merely the general mean/chord estimate, not a new original-input theorem; the stronger feature of(V3) is removal of log c when the actual coefficient distribution permits it.

### Exact finite-saving necessity and integer endpoints

Pointwise0<1-u<=1 gives

    (1-u)^(2N+2)B_base<=B_N<=B_base,
    (1-u)^(2N)B_0<=B_N<=B_0.                      (V5)

The second line uses B_0 from the actual geometric family and includes N=0 exactly.
Taking integrable logarithms and means gives

    0<=I_base-I_N<=2(N+1)L_c,
    0<=I_0-I_N<=2N L_c.                           (V6)

Consequently a supplied improvement eta>0, meaning I_base-I_N>=eta, necessarily satisfies

    N>=max{0,ceil[eta/(2L_c)]-1}.

Under p0<=1/2 a fully coefficient-explicit weaker necessary bound is

    N>=max{0,ceil[eta/(2Phi(delta))]-1}.           (V7)

For an improvement eta relative to the actual I_0, the corresponding bound is N>=ceil[eta/(2Phi(delta))].
These are necessary bounds for this prescribed geometric sequence, not for arbitrary rational polynomial shears.
If one instead seeks I_N<=log2-eta, the needed improvement is I_base-log2+eta and(V7) applies only when that number is positive.
In particular I_base>=log2 makes eta a valid required improvement.
No general lower bound I_base>=log2 is assumed or proved here.

### Two exact original-input interfaces and the remaining coefficient cancellation

Write H=||P||_1, D_P=||P||_2^2/H^2, and define the actual cancellation ratio

    beta(P)=||H35||_1/[250H^5+243H^3] in(0,1].

Coefficient convolution and the triangle inequality give, with all original coefficients retained,

    ||H35||_2
       <=250H^4||P||_2+243H^2||P||_2,
    delta<=D_P/beta(P)^2.                         (V8)

The convolution estimate ||AB||_2<=||A||_1||B||_2 follows by summing shifted coefficient vectors and the ordinary Euclidean triangle inequality; iterating it proves the displayed powers.
Substitution z maps to z^j preserves each coefficient norm, so there is no degree factor hidden in(V8).
Nothing here bounds beta(P) away from zero for arbitrary signed P.
This is the precise cancellation quantity left unresolved by separate coefficient upper estimates.

Use the original increasing epsilon and h0 from the accepted C92 statement and set

    V(t)=[epsilon(t)+2t]/[1+epsilon(t)],
       0<t<=h0.

First suppose the ACTUAL original defect g=G(alpha) is zero.
Then the nonzero ordinary polynomial H35 vanishes at alpha and at every original conjugate, and has exact span15d.
C92's rational-annihilator statement therefore gives

    delta<=V(15m(P)), provided0<15m(P)<=h0.        (V9)

Whenever V(15m)<=1/4, combine(V3), monotonicity of Phi and(V7) to obtain the explicit necessary bound with Phi(V(15m)) in place of Phi(delta).
This uses the full effective-support theorem, not a fixed term-count version: H35 is allowed to have a growing number of terms.
It asserts no actual existence of a g=0 small-measure input and no Mahler gap on that class.

Second, suppose for one sign sigma in{1,-1} every coefficient of P(sigma z) is nonnegative.
Then every coefficient of each of its positive integer powers is nonnegative, so ||P^j||_1=H^j.
The reverse triangle inequality, including the actual constants250 and243, gives

    ||H35||_1>=250H^5-243H^3>0,
    beta(P)>=(250H^2-243)/(250H^2+243)>=223/277.

Here H>=3 because the monic reciprocal unit polynomial with H=2 would be z^d+1 and torsion.
Both substitutions3 and5 are odd, so the single sign substitution preserves the two l1 power identities simultaneously.
Applying C92 to the actual annihilator P itself gives, for0<m<=h0,

    D_P<=V(m),
    delta<=(277/223)^2 V(m).                      (V10)

If the last right side is at most1/4, the same explicit finite-saving bound applies using that quantity inside Phi.
More generally the actual condition beta(P)>=beta_0>0 gives the bound V(m)/beta_0^2 whenever it is at most1/4.
The sign condition supplies such a lower bound by proof; it is not assumed for all original inputs.

This sign class is not an abstract coefficient model: the accepted actual quartic P_2=z^4-2z^3+z^2-2z+1 in [L265](../ledger/Yin_L_G0265_v1.md#trace-unit-orbit-fixed-scope) gives P_2(-z) with all nonnegative coefficients.
Changing alpha to-alpha preserves irreducibility, degree, unit property, total measure and total reality of the trace field.
This is only a nonempty fixed positive-measure control, not a near-one family or a scan.
A bounded literal support subfamily is already inside the old C92/DS17 gap domains; the deductions above permit unbounded support and establish a geometric-recipe cost, not new gap coverage.

In either(V9) or(V10), along any HYPOTHETICAL allowed input sequence with positive total m tending to zero, delta tends to zero.
Thus every prescribed fixed improvement eta requires N tending to infinity by(V7).
This is an automatic necessary loss of a bounded geometric step count on those actual conditional domains; it neither constructs the hypothetical sequence nor rules out a favorable untransformed symbol.

### Original degree, denominators, cutoff and Fourier expense

The exact C176 return must be kept after the lower bound on N.
For c=A_c/B_c in positive integers, put n=N+1 and

    W_N=(30N+40)d,
    D_N=972000^2(A_c*30375^2)^(2N+2),
    A_N=D_N z^(W_N)B_N.

Then A_N is an integer reciprocal polynomial of EXACT degree

    deg A_N=(60N+80)d=(60n+20)d,

with leading and constant coefficient121*1215^2*(49B_c)^(2n).
The exact full original return and the existing coefficient budget are

    Norm_K(B_N(alpha))=Res(P,A_N)/D_N^d>=2^d,
    I_N=m(A_N)-log D_N,
    log2<=L_N:=(1/d)log Norm_K(B_N(alpha))
          <=log sup_circle B_N+(60N+80)m(P),
    term_count(A_N/(2D_N))<=2W_N+1,
    ||A_N/(2D_N)||_1
       <=(A0/2)(1+G1^2/c)^(2n)+G1^2.             (V11)

These are the already proved exact original-degree/norm formulas and coefficient UPPER budgets, not newly inferred necessary growth of each individual coefficient or term count.
Since the leading coefficient in(V11) is nonzero, the new necessary N growth does force this prescribed ordinary degree divided by d to diverge in the stated conditional regimes.
It therefore prevents a fixed degree multiplier for these geometric improvements; it does not exclude a different shear or a different transfer theorem with growing width.

There is also a sharp scope distinction for C177's prescribed safe original-root cutoff.
Let R=1+max_(j<d)|p_j|>=2 and use

    c_*=1+G1^2 R^(15d).

This guarantees g_i^2<c_* at every actual original trace embedding by C177.
For this PARTICULAR c, xi<G1^2/(G1^2 R^(15d))=R^(-15d)<=1/2.
The old scalar inequality -log(1-xi)<=xi/(1-xi)<=2xi and(V4) give

    L_(c_*)<=2delta R^(-15d),
    I_base-I_N>=eta implies
       N+1>=eta R^(15d)/(4delta).                 (V12)

Thus the very conservative cutoff has a necessary exponential degree price even for one fixed Haar improvement, not merely a large sufficient-N estimate.
It is not asserted minimal: a cheaper c can be admissible on a particular original input, and the statement does not extend(V12) to all choices of c.
With the circle choice1+G1^2, C177 retains the actual expanding-root rate gamma_c, all threshold and zero-defect cases and the exact resultant/Haar discrepancy; the current circle estimate does not bound them.

Finally, if this input's G has a circle zero, the already proved C177 Fourier lower bound remains

    W_*(log B_N)>=log n-log log n+log2+J_G-log(A0+2c)
    for n>=ceil(max{16,(2c/(7/30375)^2)^2}).        (V13)

The threshold and subtraction depend on the actual input and c.
The new lower bound(V7) alone need not reach this threshold or control those subtractions along varying P, so it does not by itself prove Fourier divergence for every varying-input fixed-saving choice.
No upper Fourier/radial transfer budget, automatic signed-cancellation lower bound beta_0, or unrestricted D36/G0001 conclusion has been supplied.
The useful change is the rigorous distribution-level finite-saving obstruction and its exact automatic coefficient/annihilator domains, with the unchanged original-return obligations explicit.

## Current assessment
[Selected decision](#decision-current-binary-matching-proof-home-maintenance)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T11:03 |
| status | open |
| reason | Register the complete new signed-moment distribution bound and finite geometric-saving necessity, exact original annihilator/coefficient conditions and all original costs for separate whole review. The original general-shear and uniform-transfer inquiry remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete finite-saving statement](#statement) | All actual original inputs, signed moments, every rational c>G1^2, exact N endpoints, two original-input domains, prescribed cutoff and explicit noncompletion boundaries. |
| argument | [Complete proof](#argument) | Entire V1--V13, both convexity steps, full logarithmic sum, exact cost distinction, C92 adaptations, complete coefficient ratios, actual quartic and original-return/Fourier limits. |
| dependency | [Exact geometric construction](Yin_C_G0176_v1.md#polynomial-shear-exact-infimum) | Same actual original domain and full geometric identity, norm and cost interfaces, not an inferred changed arithmetic floor. |
| dependency | [Original-root and Fourier account](Yin_C_G0177_v1.md#argument) | General rational c, actual safe cutoff and Fourier inequality with every hypothesis and input-dependent cost retained. |
| dependency | [Original effective support](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Rational annihilator inequality for full original P and, when g=0, H35; actual span, epsilon and zero-value branch. |
| dependency | [Cosine moments](../ledger/Yin_L_G0215_v1.md#original-binary-degree-block-holder) | Central-binomial identity and elementary induction only. |
| dependency | [Actual sign-class control](../ledger/Yin_L_G0265_v1.md#trace-unit-orbit-fixed-scope) | Accepted irreducible quartic and trace-field domain preserved under alpha maps to-alpha; fixed positive measure only. |
| support | [Exact input and comparison roles](#exact-inputs) | All nine inputs, existing L430/L318/C140/C42 reuse, no new gap coverage, computation or source acquisition. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T11:13 |
| status | proved |
| authority | Internal adoption within Yin's selected remaining draft inquiries. |
| reason | Adopt the complete signed-moment and finite geometric-saving theorem through noncontributor R460. Both exact original-input interfaces, every step-count endpoint, prescribed cutoff price and input-dependent Fourier boundary are retained. No all-shear or uniform-transfer impossibility is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete finite-saving statement](#statement) | All actual original inputs, signed moments, every rational c>G1^2, exact N endpoints, two original-input domains, prescribed cutoff and explicit noncompletion boundaries. |
| argument | [Complete proof](#argument) | Entire V1--V13, both convexity steps, full logarithmic sum, exact cost distinction, C92 adaptations, complete coefficient ratios, actual quartic and original-return/Fourier limits. |
| dependency | [Exact geometric construction](Yin_C_G0176_v1.md#polynomial-shear-exact-infimum) | Same actual original domain and full geometric identity, norm and cost interfaces, not an inferred changed arithmetic floor. |
| dependency | [Original-root and Fourier account](Yin_C_G0177_v1.md#argument) | General rational c, actual safe cutoff and Fourier inequality with every hypothesis and input-dependent cost retained. |
| dependency | [Original effective support](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Rational annihilator inequality for full original P and, when g=0, H35; actual span, epsilon and zero-value branch. |
| dependency | [Cosine moments](../ledger/Yin_L_G0215_v1.md#original-binary-degree-block-holder) | Central-binomial identity and elementary induction only. |
| dependency | [Actual sign-class control](../ledger/Yin_L_G0265_v1.md#trace-unit-orbit-fixed-scope) | Accepted irreducible quartic and trace-field domain preserved under alpha maps to-alpha; fixed positive measure only. |
| support | [Exact input and comparison roles](#exact-inputs) | All nine inputs, existing L430/L318/C140/C42 reuse, no new gap coverage, computation or source acquisition. |
| review | [Whole finding](../audits/reviews/Yin_R_G0460_v1.md#geometric-finite-saving-whole-independent-finding) | Entire final registered statement and argument, every actual input, contribution/inspection boundary and original-cost limitation. |


### Decision current-actual-quartic-home-maintenance

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:58 |
| status | proved |
| authority | Internal adoption within Yin's selected remaining draft inquiries. |
| reason | Maintain only the same-object current a2 actual quartic proof home at complete C464 after full consumer proof/current-finding reading and exact irreducibility/trace/root/order/measure comparison. Original mathematics, formulas, all OTHER selected fields/tuples/reviews, dated old input/read accounts and decisions remain unchanged. The new R671 finding is narrow administrative SELF, not a new whole mathematical or isolated review; existing whole relationship and actual old L265 bindings remain. No source proof/native run, near-one input or Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete finite-saving statement](#statement) | All actual original inputs, signed moments, every rational c>G1^2, exact N endpoints, two original-input domains, prescribed cutoff and explicit noncompletion boundaries. |
| argument | [Complete proof](#argument) | Entire V1--V13, both convexity steps, full logarithmic sum, exact cost distinction, C92 adaptations, complete coefficient ratios, actual quartic and original-return/Fourier limits. |
| dependency | [Exact geometric construction](Yin_C_G0176_v1.md#polynomial-shear-exact-infimum) | Same actual original domain and full geometric identity, norm and cost interfaces, not an inferred changed arithmetic floor. |
| dependency | [Original-root and Fourier account](Yin_C_G0177_v1.md#argument) | General rational c, actual safe cutoff and Fourier inequality with every hypothesis and input-dependent cost retained. |
| dependency | [Original effective support](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Rational annihilator inequality for full original P and, when g=0, H35; actual span, epsilon and zero-value branch. |
| dependency | [Cosine moments](../ledger/Yin_L_G0215_v1.md#original-binary-degree-block-holder) | Central-binomial identity and elementary induction only. |
| dependency | [Complete actual quartic input](Yin_C_G0464_v1.md#actual-quartic-trace-unit-family) | Same actual a2 irreducible quartic and real trace-field domain preserved under alpha maps to-alpha, nonempty fixed-positive-measure sign control only; no complete orbit optimum or near-one family imported. |
| support | [Exact input and comparison roles](#exact-inputs) | All nine inputs, existing L430/L318/C140/C42 reuse, no new gap coverage, computation or source acquisition. |
| review | [Whole finding](../audits/reviews/Yin_R_G0460_v1.md#geometric-finite-saving-whole-independent-finding) | Entire final registered statement and argument, every actual input, contribution/inspection boundary and original-cost limitation. |
| review | [Actual narrow quartic-home SELF finding](../audits/reviews/Yin_R_G0671_v1.md#quartic-current-consumer-home-finding) | Only same-object a2 actual polynomial/field/root/order/measure and current proof-home comparison; no new whole consumer verdict, changed mathematical scope or fresh isolated coverage. All original whole findings and their actual old L265 inputs remain. |


### Decision current-binary-matching-proof-home-maintenance

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:56 |
| status | proved |
| authority | Internal adoption within Yin's selected remaining draft inquiries. |
| reason | Maintain only the same-object current L215 interface at the now complete C522 proof home after full scope comparison: central-binomial identity and elementary induction ONLY. Preserve all mathematical assertions, all other current fields and tuples, exact relation role/scope, every prior decision and every old R binding/date/actual input. Existing review findings retain their actual scopes and do not claim to have read C522. This proof-home/input-locator maintenance supplies no new mathematical verdict, fresh isolated review, source reading, native execution or research Task/E. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | All actual original inputs, signed moments, every rational c>G1^2, exact N endpoints, two original-input domains, prescribed cutoff and explicit noncompletion boundaries. |
| argument | [Exact retained argument](#argument) | Entire V1--V13, both convexity steps, full logarithmic sum, exact cost distinction, C92 adaptations, complete coefficient ratios, actual quartic and original-return/Fourier limits. |
| dependency | [Exact retained dependency](Yin_C_G0176_v1.md#polynomial-shear-exact-infimum) | Same actual original domain and full geometric identity, norm and cost interfaces, not an inferred changed arithmetic floor. |
| dependency | [Exact retained dependency](Yin_C_G0177_v1.md#argument) | General rational c, actual safe cutoff and Fourier inequality with every hypothesis and input-dependent cost retained. |
| dependency | [Exact retained dependency](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Rational annihilator inequality for full original P and, when g=0, H35; actual span, epsilon and zero-value branch. |
| dependency | [Exact retained dependency](Yin_C_G0522_v1.md#original-binary-degree-block-holder) | Central-binomial identity and elementary induction only. |
| dependency | [Exact retained dependency](Yin_C_G0464_v1.md#actual-quartic-trace-unit-family) | Same actual a2 irreducible quartic and real trace-field domain preserved under alpha maps to-alpha, nonempty fixed-positive-measure sign control only; no complete orbit optimum or near-one family imported. |
| support | [Exact retained support](#exact-inputs) | All nine inputs, existing L430/L318/C140/C42 reuse, no new gap coverage, computation or source acquisition. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0460_v1.md#geometric-finite-saving-whole-independent-finding) | Entire final registered statement and argument, every actual input, contribution/inspection boundary and original-cost limitation. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0671_v1.md#quartic-current-consumer-home-finding) | Only same-object a2 actual polynomial/field/root/order/measure and current proof-home comparison; no new whole consumer verdict, changed mathematical scope or fresh isolated coverage. All original whole findings and their actual old L265 inputs remain. |

