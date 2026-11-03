---
author: Yin
---

# Two-node trace residual rigidity beyond the accumulated-gain regime

Date: 2026-10-15T09:22.
Continuing author work by strategy_critique for Yin.
Root proposed reintroducing trace derivatives, repeated-node/Hermite or divided-difference constraints and the original integer endpoint in the regime k*m bounded away from zero.
This is a substantive root contribution if used, as it is below; root cannot independently review the new argument.
The author develops the precise two-node and coefficient estimates.

## Responsible question

For the exact C128 product/trace-remainder family, test whether a fixed raw product gain can survive on hypothetical actual Salem m->0 inputs with k polynomially bounded in1/m, even when k*m does not tend to zero.
Do not assume a large derivative, a node separation or a smaller original degree.
Keep the full-factor positive control, arbitrary real/repeated nodes, all PSD costs and the distinction from different Gram repairs.

## Bounded reuse and source check

Read the actual adopted C128 and C131 arguments and decisions, L229's exact angular modulus, and the C107 original integer endpoint floor.
Search G claims/ledgers for Hermite, Rolle, divided differences, repeated nodes and polynomial inverse-measure counts.
The existing single-node and moving-cutoff controls do not state the proposed two-node argument.
The classical symmetric Laurent/Chebyshev identity is already attributed and checked in C43 v2; only its elementary recurrence and derivative identity are needed here, not a Bernstein inequality.

The accepted Smy08-U001 Section4 Dobrowolski benchmark was reread at its original scope.
An attempted primary arXiv PDF open failed; the actual retained Smy08.pdf was then text-read with pdftotext on PDFpp5--6 (printed326--327).
Equation11 states M(alpha)>1+(1/1200)(log log d/log d)^3 for nonzero non-root-of-unity algebraic integers of degree d>=2.
The stronger reported Voutier constant is not used.
The already flagged minimal-polynomial-resultant mistake in its explanatory paragraph is NOT used; the external theorem keeps its accepted statement/applicability status and no original1979 proof audit is asserted.
For d>=exp(exp1), the displayed theorem and log(1+x)>=x/2 for0<=x<=1 give the safe explicit consequence m>=1/[2400(log d)^3].
This converts k<=C*m^(-A) into a fixed power of log d, retaining original total m.
No new source acquisition, numerical mathematical program or J is proposed.

The candidate is to force two non-negligible nodes close to the unique exterior trace root using their small interpolated values, and then contradict the residual derivative bound through Rolle or exact repeated-node divisibility.
No complete result is asserted at allocation; the full inequalities and limitations will be developed here.

<a id="statement"></a>
## Statement: fixed product gain is impossible throughout the two-condition range

Use ONLY the actual C128 PRODUCT/trace-remainder construction, on a monic irreducible positive Salem input P of ORIGINAL degree d=2h>=4.
Write lambda=M(P), m=log lambda.
Select1<=k<=h real b_i>1, repetitions allowed; divide T=product_i(x-b_i-b_i^-1)S+R, deg R<k, with P=z^hT(z+z^-1).
Put e=z^hR(z+z^-1), B=product_i b_i, and let Q,R_u be C128's original-width same-symbol matrix and PSD repair.
Its ACTUAL income, at any u>0, is

    F(u)=(1/2)log[(B^2u+1)/(u+1)]
                  -(1/2)integral log(1+u|e|^2/|P|^2),
    Q00=B^2.

All degree and measure quantities remain original and total.
No mixing of different packets or different repair class is included.

**A. Finite two-node obstruction.**
Fix gamma>0, assume k>=2, lambda<=2 and max_i b_i<=min{2,exp(gamma/2)}.
Put L0=gamma/(2k), assume0<L0<=log2, and define a=m/d, ell=log(1/a), c=log2/4, h0=c exp(-20), A0=75c^(-1/4), and

    J=max{1,ceil{L0^-1 log[8/(L0(e^L0-1))]}},
    S0=A0(a/L0)^(1/4)sqrt(ell)+4a/L0,
    U_min=max{1/(lambda+lambda^-1-2),
                         [L0^2/(4exp1)]exp(dL0/4)},
    C_k=4*9^(k-1), D_k=k^2 16^k.

If Ja<=h0, S0<=L0/8 and

    U_min>d C_k/L0^2, U_min>2D_k,

then NO packet with B>=exp(gamma) has positive actual F at any scale u>0.
The proof treats two distinct nodes by Rolle and coincident nodes by exact multiplicity.
It assumes no lower node spacing and no derivative size beyond the displayed paid conditions.

**B. The full C131 two-condition range now has raw-product collapse.**
Along ANY hypothetical actual positive Salem sequence m_j->0, suppose C128 packets have positive actual income and

    k_j^2/d_j->0,
    k_j^5(m_j/d_j)log^2(d_j/m_j)->0.

Then B_j->1 and Q_j00->1.
There is NO extra assumption that k_j m_j tends to zero or remains bounded.
Thus this conclusion also excludes the accumulated-gain branch left open by C131 within this whole range.
It follows from the finite theorem after explicitly verifying every moving cutoff and original derivative cost, not by interchanging a fixed-cutoff limit.

**C. Concrete count ranges.**
The conclusion in B holds in particular if k_j=O(d_j^(1/5)/(log d_j)^(2/5)).
Using the additional already accepted Dobrowolski theorem ONLY for this corollary, it also holds for every fixed A,C>0 whenever k_j<=C m_j^(-A).
Consequently any hypothetical positive-income family with B_j>=exp(gamma)>1 would require k_j>C m_j^(-A) eventually for every fixed A,C>0.
The original retained equation for M and its conversion to total m are kept in(18).

The full k=h C128 positive control and the universal diagonal-transfer control remain valid outside the asserted scope.
No positive uniform Mahler bound, near-one input sequence or all-Gram prohibition follows.
The source proofs and inherited original matrix/denominator/norm costs retain their exact boundaries.
Root contributed the derivative/repeated-node direction and the full two-condition extension; independent review must be by a noncontributor.

<a id="argument"></a>
## Complete argument

<a id="short-residual-value-and-derivative-budgets"></a>
## 1. Positive income gives both value and derivative budgets

Use the ACTUAL C128 packet: P monic irreducible positive Salem, d=2h>=4, lambda=M(P)>1, m=log lambda; T(x) is the original trace polynomial.
Choose1<=k<=h real b_i>1 with repetitions allowed, set s_i=b_i+b_i^-1 and divide

    T=D_x S+R, D_x=product_i(x-s_i), deg R<k,
    e(z)=z^h R(z+z^-1), B=product_i b_i.

All matrices, their original width, rational-denominator and spectral expenses, and the exact corrected income F(u) are precisely C128's unchanged construction.
Suppose the ACTUAL income at some u>0 is positive.
For nonzero e, C128 gives

    M(e)<lambda sqrt(B^2-1)<lambda B.                    (1)

Now suppose k>=2, lambda<=2 and max_i b_i<=2.
The residual cannot be identically zero: T has only ONE simple root above2, whereas D_x has k>=2 such roots counted with multiplicity.
Thus(1) applies and

    M(e)<2^(k+1).                                       (2)

Write E(z)=z^(k-1)R(z+z^-1), so e=z^(h-k+1)E and M(E)=M(e).
Its effective degree is at most2k-2 and its coefficients are symmetric about position k-1, allowing zero endpoint coefficients.
The complete root product gives ||E||_1<=2^(2k-2)M(E), including every leading factor and any zero root.
For x=b+b^-1 with1<=b<=2, C128's same node-evaluation inequality, now applied at an arbitrary real b, gives

    |R(x)|<=M(e)(b+2+b^-1)^(k-1)
            <=C_k:=4*9^(k-1).                          (3)

The interval of these x values is[2,5/2].
To bound its derivative, write

    R(x)=E_(k-1)+sum_(j=1)^(k-1)E_(k-1+j) C_j(x),
    C_j(b+b^-1)=b^j+b^-j.

The polynomials C_j obey C_0=2,C_1=x,C_(j+1)=x C_j-C_(j-1), the standard symmetric Laurent/Chebyshev identity already attributed in C43 v2.
Differentiating for b>1 gives

    C_j'(b+b^-1)=j(b^j-b^-j)/(b-b^-1)
       =j sum_(l=0)^(j-1)b^(j-1-2l)
       <=j^2 2^(j-1).

At b1 continuity gives j^2, so the same bound holds.
Therefore

    max_(2<=x<=5/2)|R'(x)|
      <=k^2 2^(k-2) ||E||_1
      <k^2 2^(4k-3)<=D_k:=k^2 16^k.                   (4)

All k costs are retained.
This is a bound on the ACTUAL short interpolation residual, not a new field norm or an assumed bound on T'.
It uses no minimum node separation and no generic polynomial-derivative theorem.

<a id="uniform-circle-factor-floor"></a>
## 2. The complete circle factor has a paid uniform lower bound

Write a_star=lambda+lambda^-1 and

    T(x)=(x-a_star)U(x),
    U(x)=product_(j=1)^(h-1)(x-c_j), -2<c_j<2.

All h-1 original unit-circle inverse pairs occur; U is positive and increasing on x>2.
The exact integer endpoint is

    |P(1)|=(a_star-2)U(2)>=1,
    U(x)>=1/(a_star-2) for every x>=2.                 (5)

This is the OLD original endpoint information, now retained alongside the angular estimate, not advertised as a new uniform Mahler bound.

Fix0<L0<=log2.
Set a=m/d, ell=log(1/a), c=log2/4, h0=c exp(-20), and A0=75c^(-1/4).
Let

    J=max{1,ceil{L0^-1 log[8/(L0(e^L0-1))]}},
    S0=A0(a/L0)^(1/4)sqrt(ell)+4a/L0.

Assume the explicit finite conditions

    Ja<=h0, S0<=L0/8.                                 (6)

C131's frequency-weighted proof then supplies, for the complete unit-root angular sums U_n, the first-J expense d S0+2H0, H0=-log(1-e^-L0), and a separate tail at most dL0/8, uniformly for b>=exp L0.
These are exactly its finite source/range and original-root costs, not an application of its final product-collapse conclusion.

For any b=exp L in[exp L0,2], the complete circle factor satisfies

    log U(b+b^-1)
      =(h-1)L-Re sum_(n>=1)U_n/(n b^n)
      >=(h-1)L-dL0/4-2H0
      >=dL0/4-L0-2H0.

Here the infinite logarithm series is absolutely convergent at1/b; the actual angular theorem has been used ONLY through J and its remaining tail has the displayed elementary bound.
Since L0<=1, H0<=log(2/L0).
Thus throughout that whole real trace interval,

    U(x)>=U_min:=max{1/(a_star-2),
                         [L0^2/(4exp1)]exp(dL0/4)}.    (7)

The first term is(5).
The second term retains all original d, the +2 off-circle angular contribution and the exact test radius.
No distance from the input lambda to1 has been declared fixed.

<a id="two-node-hermite-rolle-obstruction"></a>
## 3. Two nodes force a derivative contradiction, even without spacing

Fix gamma>0 and suppose a packet has

    B>=exp(gamma), max_i b_i<=min{2,exp(gamma/2)}.

Put L0=gamma/(2k) and assume0<L0<=log2 and(6).
If at most one node had log b_i>=L0, then

    log B<=gamma/2+(k-1)L0<gamma,

a contradiction.
Hence there are at least TWO such nodes, counting repetitions.
For their traces x_i=s_i, monic division gives T(x_i)=R(x_i).
Equations(3),(7) imply

    |x_i-a_star|<=eta:=C_k/U_min.                     (8)

Suppose also the completely finite inequalities

    U_min>d C_k/L0^2, U_min>2D_k.                    (9)

The interval between the two traces (a singleton if repeated) lies in[2cosh L0,5/2] and inside[a_star-eta,a_star+eta].
At every x in it,

    U'(x)/U(x)=sum_(j=1)^(h-1)1/(x-c_j)
       <=(h-1)/(x-2)<=d/(2L0^2),

because2cosh L0-2>=L0^2.
Therefore, using(8)--(9),

    T'(x)=U(x)[1+(x-a_star)U'(x)/U(x)]
          >=U(x)/2>=U_min/2>D_k.                    (10)

If the two traces are distinct, Rolle's theorem applied to T-R on their interval forces T'(x)=R'(x) at an interior point.
If they coincide, D_x contains that factor at least twice, so its exact divisibility into T-R forces the SAME derivative equality at the repeated node.
Both cases contradict(4),(10).
No quantitative separation, nonconfluent Vandermonde inversion or assumed large derivative has been used.
The large derivative was proved from the explicit U_min and the d/L0^2 cost.

Consequently, under all displayed finite hypotheses, there is NO positive-ACTUAL-income C128 packet with fixed product gain B>=exp(gamma).
This statement covers distinct and repeated nodes jointly.
It is stronger than checking only P(b) near lambda, where the original value can indeed vanish.

<a id="two-node-growing-count-collapse"></a>
## 4. The whole C131 two-condition range collapses, without k*m tending to zero

After the finite argument was written, root proposed checking its costs on the WHOLE pair of conditions left by C131 rather than first specializing to polynomial inverse-measure counts.
This is an additional substantive root contribution.
The following verification closes that larger range and removes the extra k*m premise from the product-collapse conclusion.

Consider ANY hypothetical sequence of actual positive Salem inputs P_j with m_j->0, original degrees d_j, and C128 packets with POSITIVE ACTUAL income at some scales u_j>0.
Suppose

    k_j^2/d_j->0,
    z_j:=k_j^5(m_j/d_j)log^2(d_j/m_j)->0.              (11)

No hypothesis on k_j m_j is imposed.
The old original endpoint argument gives d_j->infinity.
Suppose, for contradiction, that B_j does not tend to1.
Since B_j>1, restrict to a subsequence with B_j>=exp(gamma) for some FIXED gamma>0.
All following limits are on that subsequence.

The first condition implies k_j=o(d_j), so C128's adopted fixed-cutoff theorem gives max_i b_(j,i)->1.
Thus eventually lambda_j<=2 and max_i b_(j,i)<=min{2,exp(gamma/2)}.
Also gamma<=log B_j<=k_j max_i log b_(j,i), so k_j->infinity.
Consequently L0,j=gamma/(2k_j)->0 and eventually0<L0,j<=log2.
These are derived actual packet facts, not node-spacing assumptions.

Write a=m/d and ell=log(1/a), suppressing j.
Eventually m<1 and k<=sqrt d, so log k<=ell/2.
The J prescribed before(6) obeys

    Ja<=a+(a/L0)[log8+2log(1/L0)]
        <=C_gamma a k ell
        =C_gamma z/(k^4 ell)->0.                     (12)

Here C_gamma is a fixed finite bound for the displayed elementary expression once k,ell are large; no asymptotic source constant replaces the explicit finite J.
Moreover

    S0/L0=A0(2/gamma)^(5/4) z^(1/4)
                              +(16/gamma^2)a k^2->0. (13)

The last term vanishes because a k^2=m(k^2/d).
Thus the precise source and expense conditions Ja<=h0 and S0<=L0/8 in(6) eventually hold.
Every growing frequency has remained inside its accepted range, and the unbounded tail was paid separately.

The angular part of(7) gives

    log U_min>=gamma d/(8k)-2log k+C_gamma',           (14)

where C_gamma'=2log(gamma/2)-log(4exp1) is an exact fixed constant.
The two right sides required in(9) have logarithms

    log[d C_k/L0^2]=log d+(k-1)log9+2log k
                                      +log4+2log(2/gamma),
    log(2D_k)=klog16+2log k+log2.                     (15)

The term d/k dominates EVERY term in(15): k/(d/k)=k^2/d->0, and (log d)/(d/k)=klog d/d<=log d/sqrt d->0.
Also log k<=log d eventually.
Since d/k->infinity, subtracting(15) from(14) tends to infinity.
Both strict inequalities(9) eventually follow.
The finite two-node theorem now contradicts positive income.

Therefore under(11), necessarily

    B_j->1, Q_j00=B_j^2->1.                           (16)

This closes the formerly permitted k*m>=gamma branch throughout the full C131 two-condition range.
Its proof uses neither Dobrowolski nor an assumed derivative or node separation.
The argument permits arbitrary real nodes and repeated nodes, arbitrary correction scales and any growth of k*m consistent with(11).
It is still a theorem only about the specified product/remainder family, not every corrected Gram.

<a id="two-node-degree-and-inverse-measure-scales"></a>
## 5. Two concrete growing-count consequences

First, C131's proved elementary scale comparison shows that for ANY hypothetical m_j->0 sequence,

    k_j=O(d_j^(1/5)/(log d_j)^(2/5))                   (17)

implies BOTH conditions(11).
The exact check is k^2/d->0 and

    k^5(m/d)log^2(d/m)
       <=C m[1+log(1/m)/log d]^2
       <=2C m+2C m log^2(1/m)/(log d)^2->0.

Thus every positive-income C128 packet throughout(17) now has B->1 WITHOUT the formerly additional k*m->0 hypothesis.
No rate for the input m->0 is imposed.

Second, use the separately identified already accepted Dobrowolski benchmark ONLY for this additional corollary.
The retained Smy08 equation11 and its source range give, for d>=exp(exp1),

    M(P)>1+1/[1200(log d)^3],
    m(P)>=1/[2400(log d)^3].                          (18)

The logarithmic conversion uses log(1+x)>=x/2 for0<=x<=1.
It does not replace total m by absolute height.
Fix ANY constants A>0 and C>0.
If

    k_j<=C m_j^(-A),                                 (19)

then k_j<=C*2400^A (log d_j)^(3A) eventually.
Also m_j<1 and(18) imply ell_j=log(d_j/m_j)=O(log d_j).
Hence

    k_j^2/d_j=O((log d_j)^(6A)/d_j)->0,
    k_j^5(m_j/d_j)ell_j^2
                =O((log d_j)^(15A+2)/d_j)->0.        (20)

We used m_j<=1 for the last bound.
Thus(19) implies the main conditions(11), and positive-income packets again have B_j->1.
The constants and sufficiently large degree threshold depend on A,C and the stated accepted theorem, not on a hypothetical uniform Mahler gap.

Equivalently, if a hypothetical near-one sequence retained a fixed B_j>=exp(gamma)>1 at positive actual income, then for EVERY fixed A,C>0 it would eventually have k_j>C m_j^(-A).
Otherwise restrict to an infinite subsequence violating that inequality and apply the preceding corollary.
This is a superpolynomial factor-count requirement in1/m for this construction, not a new lower bound for m itself.

The C128 positive full-factor control has k=d/2 and is outside(11).
It remains a valid countercontrol to any universal prohibition: it spends an old endpoint floor and permits huge corrections.
Its existence is compatible with(18), which makes original degree grow faster than every fixed power of1/m along any hypothetical near-one sequence.
No contradiction to that control or to a different Gram repair is asserted.

<a id="two-node-source-contribution-and-limits"></a>
## 6. Source, contribution and surviving-interface boundaries

The direct construction input is [C128](Yin_C_G0128_v1.md#statement), with its actual [short residual](Yin_C_G0128_v1.md#effective-residual-degree-and-node-test), [positive-income all-scale inequality](Yin_C_G0128_v1.md#multiple-trace-factor-exact-repair), [fixed-cutoff limit](Yin_C_G0128_v1.md#linear-factor-demand-near-one) and original matrix/denominator/norm costs.
The author contributed that work.
The new proof does not change or reoptimize its matrices, so all those original costs survive unchanged.

The angular input is the actual adopted [C131 frequency-weighted estimate](Yin_C_G0131_v1.md#frequency-weighted-angular-bound), itself directly using [L229](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence).
This round checked their precise n*m/d range, finite cutoff, +2 original real-root contribution and separate tail.
Their accepted Pri11/Dim19 theorem and source-proof limits remain unchanged; no new infinite-frequency theorem is invoked.
The endpoint part of(7) is the old [C107 integer endpoint mechanism](Yin_C_G0107_v1.md#signed-norm-gap-assessment), proved at its actual P(1) normalization in(5).
It is not needed to smuggle a uniform derivative bound into(10).

The symmetric Laurent/Chebyshev identity uses [C43 v2's established normalization and attribution](Yin_C_G0043_v2.md#chebyshev-damping-reuse-and-source-scope) and its [explicit recurrence](Yin_C_G0043_v2.md#chebyshev-damping-real-contact-polynomial); its body records the checked NIST DLMF18.5.1 identity.
Only that ordinary recurrence/normalization is reused, and the derivative and coefficient bounds here are explicitly derived.
No Bernstein or external interpolation theorem is needed.
Distinct nodes use ordinary real Rolle; repeated nodes use exact polynomial multiplicity, so no reciprocal node-distance factor appears.

Only the additional inverse-measure corollary uses the [accepted Dobrowolski benchmark in Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001).
The actual retained source equation11 on printed326/PDFp5 was inspected in text in this round; it states a bound for M, and the conversion to m is explicitly paid in(18).
Its original1979 proof is not newly audited.
The explanatory minimal-polynomial-resultant error already recorded by U001 is not invoked, and stronger reported constants are unnecessary.
The primary arXiv fetch failure did not change the retained source edition.
No numerical computation, mathematical program, new J or source acquisition supplies any result here.

Root supplied the derivative/repeated-node direction and subsequently proposed testing the entire C131 two-condition range.
Both are substantive mathematical contributions and are disclosed.
The strategy_critique author supplied the coefficient/derivative bounds, uniform circle-factor lower bound, exact two-node contradiction, and complete finite/asymptotic costs.
Root cannot independently review this new proof; a noncontributor must review the actual fixed whole artifact.
The original author contributed C128/C131 and is not claiming independent review of those inputs.

The new restriction is substantial within its exact family: it removes the need for k*m->0 from C131's product-collapse range, and thereby also excludes all fixed polynomial counts in1/m at a fixed raw product gain.
It does not establish that all larger factor counts fail, or that the original small-measure integer inputs cannot exist.
Superpolynomial counts, other product residual architectures, cross terms not reducible to this construction, and different PSD repairs remain outside this conclusion.
An unrestricted Mahler gap or a zero-gap family is not proved.

<a id="two-node-entire-author-freeze"></a>
## Entire author freeze

2026-10-15T09:37.
The strategy_critique author freezes the ENTIRE current D38 with this title: responsible question and its later larger-range refinement, bounded reuse and exact source check, Statement A--C, complete Sections1--6 and all20 numbered formulas.
This is the newly allocated two-node draft, not the older D38 already retained in C128.
The final actual full-file self-check reconstructed C128's exact positive-income residual inequality and the nonzero residual at k>=2; the full coefficient-norm budget and symmetric Laurent representation; the derivative formula including b1 and lower actual residual degrees; the original trace-root product and integer endpoint; all d-2 unit roots, the +2 angular charge and finite tail; the uniform circle-factor floor without a fixed radial gap; the existence of two high nodes at fixed product gain; the d/L0^2 logarithmic-derivative cost on their whole interval; exact repeated-node multiplicity versus distinct-node Rolle; and every strict comparison in(9)--(10).

The same check covered the fixed-gamma subsequence and k->infinity deduction, the explicit J*a and S0/L0 limits, dominance of d/k over k and log d, removal of EVERY extra k*m assumption, the simpler degree scale, the exact retained M-form Dobrowolski statement and its safe total-m conversion, polynomial inverse-measure counts and their eventual quantifiers, and compatibility with the full-factor positive control and other repairs.
No remaining mathematical gap was found by this author check.
The main finite and two-condition statements do not use Dobrowolski; only the separately identified extra corollary does.
No native mathematical program or new source theorem/proof audit was used.

Root contributed both the derivative/Hermite direction and the proposal to check the full two-condition range.
That contribution is retained and precludes root independent review of this new proof.
A noncontributor's actual fixed whole review remains necessary for independent adoption.
The structural material check is separate from mathematical review.
This freeze does not assert unrestricted Mahler completion, existence of near-one inputs, a uniform gain for the original problem or a prohibition on all Gram corrections.

## Fixed organization

Retain the complete frozen two-node proof, its finite value/derivative and circle-factor costs, distinct/repeated-node argument, full C131 two-condition collapse without a km premise, original-degree and inverse-measure corollaries, all controls and source/contribution limits.
Root contributed the derivative direction and enlarged-range proposal and cannot serve as an independent reviewer of this artifact.

## Current assessment
[Selected decision](#decision-isolated-current-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T09:39 |
| status | open |
| reason | Retain the complete finite two-node obstruction and raw-product collapse across C131's two-condition range without the additional km assumption. All original trace-residual and source costs remain; the full-factor control and other Gram repairs remain outside this restricted result. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire two-node statement](#statement) | A--C, explicit finite guards, full two-condition collapse and exact additional Dobrowolski corollary. |
| argument | [Complete two-node proof](#argument) | Sections1--6 and20 formulas, all source/endpoint/coefficient/derivative/count costs, controls and contribution limits. |
| dependency | [Actual product construction](Yin_C_G0128_v1.md#statement) | Exact original-width packet, true-income residual bound, effective degree, fixed-cutoff maximum-node consequence and all original costs. |
| dependency | [Finite weighted angular sum](Yin_C_G0131_v1.md#frequency-weighted-angular-bound) | Exact finite source domain, actual frequency weighting, real-root contribution and separately paid tail. |
| dependency | [Original angular modulus](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Precise finite T=n and original powered-degree multiplicities, with existing source inspection limits. |
| dependency | [Original endpoint arithmetic](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Nonzero integer P(1), bounded-degree escape and exact original factor normalization, rederived locally where used. |
| dependency | [Symmetric Laurent normalization](Yin_C_G0043_v2.md#argument) | Existing Chebyshev recurrence/normalization attribution only; actual derivative and coefficient bounds are explicitly derived here. |
| dependency | [Accepted Dobrowolski benchmark](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | ONLY the additional inverse-measure-count corollary, exact retained equation11 for M and paid conversion to total m; not a premise of the main finite or two-condition theorem. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T09:46 |
| status | proved |
| reason | Adopt R488 actual noncontributor whole review. The exact two-node value/derivative contradiction gives product collapse throughout C131's two-condition range without an additional km premise. The inverse-measure count consequence alone uses the accepted Dobrowolski benchmark. All original costs and full-factor controls remain; larger-count or different Gram constructions and the unrestricted goal are open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire two-node statement](#statement) | A--C, explicit finite guards, full two-condition collapse and exact additional Dobrowolski corollary. |
| argument | [Complete two-node proof](#argument) | Sections1--6 and20 formulas, all source/endpoint/coefficient/derivative/count costs, controls and contribution limits. |
| dependency | [Actual product construction](Yin_C_G0128_v1.md#statement) | Exact original-width packet, true-income residual bound, effective degree, fixed-cutoff maximum-node consequence and all original costs. |
| dependency | [Finite weighted angular sum](Yin_C_G0131_v1.md#frequency-weighted-angular-bound) | Exact finite source domain, actual frequency weighting, real-root contribution and separately paid tail. |
| dependency | [Original angular modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Precise finite T=n and original powered-degree multiplicities, with existing source inspection limits. |
| dependency | [Original endpoint arithmetic](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Nonzero integer P(1), bounded-degree escape and exact original factor normalization, rederived locally where used. |
| dependency | [Symmetric Laurent normalization](Yin_C_G0043_v2.md#argument) | Existing Chebyshev recurrence/normalization attribution only; actual derivative and coefficient bounds are explicitly derived here. |
| dependency | [Accepted Dobrowolski benchmark](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | ONLY the additional inverse-measure-count corollary, exact retained equation11 for M and paid conversion to total m; not a premise of the main finite or two-condition theorem. |
| review | [Actual whole two-node finding](../audits/reviews/Yin_R_G0798_v1.md#two-node-whole-independent-finding) | Entire fixed theorem and20 formulas, finite and asymptotic guards, distinct/repeated nodes, all original costs and precisely separated source corollary; contributor relationships disclosed. |


### Decision isolated-current-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:50 |
| status | proved |
| reason | Adopt the new isolated R798 whole finding for this exact highest physical statement and complete argument, after necessary fixed-mathematics/source inspection and subsequent comparison with all original review accounts. Preserve the complete current mathematical status, input relations and scopes, all original costs and open coverage limits. R798 separately retains the original unknown findings, dates, exact historical bindings, missing-table observations and negative predecessor findings; this new independent review does not retrospectively upgrade them or claim source-proof audits or Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire two-node statement](#statement) | A--C, explicit finite guards, full two-condition collapse and exact additional Dobrowolski corollary. |
| argument | [Complete two-node proof](#argument) | Sections1--6 and20 formulas, all source/endpoint/coefficient/derivative/count costs, controls and contribution limits. |
| dependency | [Actual product construction](Yin_C_G0128_v1.md#statement) | Exact original-width packet, true-income residual bound, effective degree, fixed-cutoff maximum-node consequence and all original costs. |
| dependency | [Finite weighted angular sum](Yin_C_G0131_v1.md#frequency-weighted-angular-bound) | Exact finite source domain, actual frequency weighting, real-root contribution and separately paid tail. |
| dependency | [Original angular modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Precise finite T=n and original powered-degree multiplicities, with existing source inspection limits. |
| dependency | [Original endpoint arithmetic](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Nonzero integer P(1), bounded-degree escape and exact original factor normalization, rederived locally where used. |
| dependency | [Symmetric Laurent normalization](Yin_C_G0043_v2.md#argument) | Existing Chebyshev recurrence/normalization attribution only; actual derivative and coefficient bounds are explicitly derived here. |
| dependency | [Accepted Dobrowolski benchmark](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | ONLY the additional inverse-measure-count corollary, exact retained equation11 for M and paid conversion to total m; not a premise of the main finite or two-condition theorem. |
| review | [Isolated current whole finding](../audits/reviews/Yin_R_G0798_v1.md#g134-current-whole-independent) | Entire exact current statement and complete argument, every necessary original/current mathematical interface, original norms/weights/times/costs, source depth, finite controls and explicit limits; old physical-version and relationship findings remain separate in R798. |
