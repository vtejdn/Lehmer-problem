---
author: Yin
---

# Growing trace-factor counts and a paid moving cutoff

Date: 2026-10-15T08:44.
Continuing author work by strategy_critique for Yin.
Root proposed the substantive moving-cutoff mechanism: a fixed product gain B>=exp(gamma) forces a node at least exp(gamma/k), so apply finite estimates with the cutoff varying with k rather than infer a uniform limit from C128's fixed-cutoff result.
This is a root mathematical contribution, and root cannot independently review that new part.
The strategy_critique author develops the frequency-weighted and radial refinements and complete costs.

## Responsible question

Close a genuinely growing factor-count regime left open by C128: even when every node tends to1, can their product retain fixed gain at positive actual income?
Pay every moving frequency cutoff J, logarithmic factor, original angular modulus, radial separation and residual degree expense.
A restatement of C128's finite formula is not by itself the desired new result.

## Exact reuse and intended improvement

Read the actual fixed C128 v1 full author argument first at its initial selection and, before completing this proof, confirmed its selected whole-reviewed decision.
Reuse its exact product/remainder matrices and short-residual node bound.
Read C125's actual finite angular/root argument and L229's precise finite-frequency modulus and powered-degree multiplicity interface.
A targeted G-library search for moving cutoff, frequency-weighted angular sums, epsilon(nm/d), n^(-3/4) and related scales found no matching retained conclusion.
Existing L229/C125/C128 inputs suffice for the finite direct estimates; no new external theorem or native program is needed.

The first improvement to test is to sum epsilon(nm/d)/(n b^n) with its ACTUAL n-dependence, instead of replacing every term by epsilon(Jm/d).
This may remove artificial logarithmic losses.
A second proposed refinement sets log b=m+w and explicitly pays the radial gap w, rather than assuming log b>=2m.
Both must be proved before a quantitative or asymptotic conclusion is asserted.

<a id="statement"></a>
## Statement: a paid bound for growing near-one products

The input is an ACTUAL monic irreducible positive Salem polynomial P of ORIGINAL degree d=2h>=4, total m=log M(P)>0.
Use precisely C128's PRODUCT construction: choose1<=k<=h real b_i>1, repetitions permitted; put s_i=b_i+b_i^-1 and divide T=product_i(x-s_i)S+R, where P=z^hT(z+z^-1) and deg R<k.
Let

    C=z^(h-k)S(z+z^-1), e=z^hR(z+z^-1),
    f=C product_i(b_i-2z+b_i^-1z^2), B=product_i b_i.

On the ORIGINAL coefficient window0,...,d, use Q=ff^T+pe^T+ep^T-ee^T and R_u=u^-1pp^T+(1+u)ee^T at any real u>0.
C128 proves their exact symbol and PSD assertions, Q00=B^2 and the actual income

    F(u)=(1/2)log[(B^2u+1)/(u+1)]
                     -(1/2)integral log(1+u|e|^2/|P|^2).

Positive income below ALWAYS means this ACTUAL F(u)>0.
Nothing is inferred from a potentially positive upper envelope.
No positive mixture or different repair is included.

**A. Finite moving-cutoff bound.**
Put c=log2/4, h0=c exp(-20), A=75c^(-1/4), K=(16A)^(4/5), a=m/d and ell=log(1/a).
Define

    W=max{K(a ell^2)^(1/5),8sqrt(a),
                      [2klog625+16log(2d)+32]/d},
    L=m+W,
    J=max{1,ceil{L^-1 log[8/(L(e^L-1))]}}.

Assume1<=k<=d/16,0<m<=log2,L<=1 and Ja<=h0.
Then a packet with ANY node b_i>=exp L has strictly NEGATIVE actual income at EVERY u>0.
Consequently every positive-income packet satisfies

    max_i log b_i<m+W,
    log B<k(m+W), Q00<exp[2k(m+W)].

Every frequency, radial gap, original angle, residual-degree and large-radius cost is explicit in Sections1--3.
The source estimate is used only on n<=J.
If a proposed fixed product gain is B>=exp(gamma), gamma>0, the additional finite condition k(m+W)<=gamma therefore rules out positive income.

**B. Growing-count comparison and product collapse.**
Along ANY hypothetical sequence of actual positive Salem inputs m_j->0 and positive-income product packets, if k_j=o(d_j), then ALL finite hypotheses of A eventually hold and its displayed bound applies.
If moreover

    k_j^2/d_j->0,
    k_j^5(m_j/d_j)log^2(d_j/m_j)->0,

then limsup_j(log B_j-k_j m_j)<=0.
If also k_jm_j->0, then B_j->1 and Q_j00->1.
These conditions permit unbounded integer k_j; the sufficient combined range is exactly(20).
Under the first two displayed limits, any retained fixed gain B_j>=exp(gamma)>1 instead requires liminf_j k_jm_j>=gamma.

**C. A simpler sufficient degree scale, with its essential limitation.**
The first two limits in B hold whenever k_j=O(d_j^(1/5)/(log d_j)^(2/5)), without imposing a rate on m_j->0.
Thus that growing-count scale gives log B_j<=k_jm_j+o(1); product collapse STILL requires k_jm_j->0.
Neither this scale nor the theorem excludes every growing near1-node family.

No near-one input sequence is asserted to exist.
The theorem closes a previously open growing-factor range for the specific C128 construction, not the unrestricted Task or all same-symbol corrections.
All original matrix/denominator/norm costs remain those in C128.
Root supplied the moving-cutoff mechanism and is a contributor; independent whole review must be by a noncontributor.

<a id="argument"></a>
## Complete argument

<a id="frequency-weighted-angular-bound"></a>
## 1. A finite frequency-weighted estimate, with its tail separated

Let P be an actual monic irreducible positive Salem polynomial of degree d=2h>=4, m=log lambda>0, a=m/d.
Put c=log2/4, h0=c exp(-20), and retain L229's exact modulus

    v(x)=max{x,sqrt(x/c)log sqrt(c/x)},
    epsilon(x)=min{1,15sqrt(v(x))+4x}, 0<x<=h0.

For each positive integer n with na<=h0, L229 applied at its FINITE range T=n gives the actual angular sum |Z_n|<=d epsilon(na).
This keeps its original powered-degree multiplicities.
The two positive real off-circle roots have angular contribution2, so the sum U_n over all d-2 unit roots satisfies

    |U_n|<=d epsilon(na)+2.                            (1)

For0<x<=h0 the second term in v dominates x.
Indeed, writing x=cy with0<y<=exp(-20), one has sqrt(y)log(1/y)/2>=10sqrt(y)>=cy.
Since c<1, this gives the safe pointwise estimate

    epsilon(x)<=15 c^(-1/4)x^(1/4)sqrt(log(1/x))+4x.

Let ell=log(1/a)>0 and choose L>0 and an integer J>=1 with Ja<=h0.
For1<=n<=J, log(1/(na))<=ell.
Therefore

    S_J:=sum_(n=1)^J epsilon(na)e^(-nL)/n
       <=A(a/L)^(1/4)sqrt(ell)+4a/L,
    A=75 c^(-1/4).                                    (2)

Here is the complete summation price.
The decreasing positive function x^(-3/4)exp(-Lx) gives

    sum_(n>=1)n^(-3/4)e^(-nL)
      <=integral_0^infinity x^(-3/4)e^(-Lx)dx
      <=(4+exp(-1))L^(-1/4)<5L^(-1/4).

For the last inequality split at1/L; below it discard the exponential, and above it bound x^(-3/4) by L^(3/4).
Also sum_(n>=1)e^(-nL)=1/(e^L-1)<=1/L.
These estimates prove(2) with the stated A.
Only explicit NUMERICAL MAJORANTS have been summed to infinity; the actual angular estimate is used solely at n<=J.
No unbounded-frequency application of L229 or a singular boundary test is hidden.

For0<L<=1 define

    J=max{1,ceil{L^-1 log[8/(L(e^L-1))]}},
    r_J=e^(-JL)/[(J+1)(e^L-1)]<=L/8.                  (3)

The inequality follows directly from the chosen exponent after discarding J+1.
For a real b>=exp L the complete circle-root logarithm series is absolutely convergent and has tail at most d r_J.
With H=-log(1-e^-L), equations(1)--(3) give

    sum_unit log|b-zeta|
      >=(d-2)log b-d S_J-2H-d r_J.                    (4)

The +2 actual real-root angular contribution and its full logarithmic sum2H are retained.
This replaces the earlier uniform epsilon(Ja)H estimate by a frequency-weighted bound; merely substituting a moving cutoff into C128 would not produce(2).

<a id="explicit-moving-error-scale"></a>
## 2. Explicit angular, degree and radial payments

Take an integer1<=k<=d/16, so d>=16.
Define

    K=(16A)^(4/5), Psi(a)=[a log^2(1/a)]^(1/5),
    W=max{K Psi(a),8sqrt(a),
                    [2klog625+16log(2d)+32]/d},
    L=m+W.                                           (5)

For the finite argument assume0<m<=log2, L<=1, and the J in(3) satisfies Ja<=h0.
These are explicit checks, not consequences assumed from the fixed-cutoff theorem.
In particular a<=h0 and ell>0.

Since L>=W and W^5>=(16A)^4 a ell^2, the first term of(2) is at most W/16.
Since W^2>=64a, its second term is at most W/16.
Thus

    S_J<=W/8<=L/8, S_J+r_J<=L/4.                      (6)

Unlike C125's stronger exterior separation assumption, the present test radius is beta=exp L=lambda exp W.
For every b>=beta,

    b-lambda>=exp(m)(exp W-1)>=W,
    b-lambda^-1>=b-1>=L.

If also b<=4, the COMPLETE original root product delta_b=b^-hP(b)>0 and(4),(6) imply

    log delta_b>=(h-2)L+log(WL)-dL/4-2H
       =dL/4-2L+log W+log L-2H
       >=dL/4+4log W-log(4 exp(2)).                  (7)

Indeed0<L<=1 gives1-exp(-L)>=L/2, hence H<=log(2/L); also W<=L and -2L>=-2.
Thus

    delta_b>=W^4 exp(dL/4)/(4 exp(2))
                                      (exp L<=b<=4). (8)

All radial separation has been paid by W^4 in(8); no unknown uniform gap from lambda to1 or from the moving beta to lambda is assumed.
For b>=4, lambda<=2 and all unit roots give the separate old elementary bound

    delta_b>=(b-2)(b-1)^(d-1)/b^h.                    (9)

Thus the two radial regimes still cover every unbounded real test parameter.
The purpose of L=m+W, instead of L>=2m, is to retain the coefficient1 of the actual m in the eventual product bound.

<a id="finite-product-objective-bound"></a>
## 3. Every positive-income packet has a bounded product

Use the EXACT C128 product packet with1<=k<=h: T=product_i(x-b_i-b_i^-1)S+R, e=z^hR(z+z^-1), B=product_i b_i, and its exact same-symbol Q, PSD R_u, and actual income F(u).
Keep ALL parameters real b_i>1, repetitions allowed, and any scale u>0.
Its independently established necessary condition for positive actual income is

    M(e)^2<M(P)^2(B^2-1)                              (10)

when e is nonzero.
The effective-residual-degree estimate at each selected node is

    M(e)>=|delta_(b_i)|/(b_i+2+b_i^-1)^(k-1).         (11)

Suppose some node is>=exp L and choose b=max_i b_i.
Then B<=b^k and e(b)=P(b)>0, so the residual is nonzero.
If b<=4, use(8),(11), M(P)<=2, and b+2+b^-1<=25/4 to obtain

    M(e)^2/[M(P)^2(B^2-1)]
       >=exp(dL/2)W^8/[1024 exp(4)625^(k-1)].        (12)

The last term of W in(5) is at least1/d.
Hence log W>=-log d, while

    dL/2>=dW/2>=klog625+8log(2d)+16.

The logarithm of the right side of(12) is therefore at least

    log625+8log2+16-log1024-4
       =12+log(625/4)>0.                             (13)

For b>=4, the old large-radius calculation in C128 applies, since k<=d/16 implies h>=2k-1.
It gives instead

    M(e)^2/[M(P)^2(B^2-1)]
       >=9(9/4)^(d-2)/[256*625^(k-1)]>1.             (14)

To verify the strict inequality without decimal approximations, its logarithm is at least

    d[log(9/4)-(log625)/16]+log(625/144)>0.

Both terms are positive: (9/4)^4>25, so certainly (9/4)^16>625, and625>144.
Thus every possible far node contradicts(10).
More strongly, the all-scale C128 inequality makes its actual income negative at every u.
Consequently, under ALL finite hypotheses above, a positive-income packet must satisfy

    max_i log b_i<m+W,
    log B<k(m+W), Q00<exp[2k(m+W)].                 (15)

This is a bound on the raw product and original raw Gram objective.
It holds for arbitrary scales and repeated nodes; no comparison of separately optimized packets is involved.
The full denominators, coefficient norms and PSD repairs remain those already established for the unchanged C128 construction.
The new estimate does not suppress these expenses or assert small correction norm.

For a requested fixed product gain B>=exp(gamma), gamma>0, the explicit finite condition k(m+W)<=gamma rules out positive actual income.
This is the proposed moving-cutoff mechanism with every source range and radial price now visible.

<a id="growing-factor-product-collapse"></a>
## 4. A genuinely growing-count range closes the product loophole

Let P_j be ANY hypothetical sequence of actual positive Salem inputs with m_j->0, d_j=2h_j.
Let k_j be any positive integer factor counts and take C128 packets with positive ACTUAL income.
The original endpoint argument retained in C128 gives d_j->infinity.
Put a_j=m_j/d_j, ell_j=log(1/a_j), and define W_j,L_j,J_j by(3),(5).

First suppose only k_j=o(d_j).
Then a_j->0 and each term defining W_j tends to0: in particular (k_j+log d_j)/d_j->0.
Thus W_j->0 and L_j=m_j+W_j->0.
Eventually k_j<=d_j/16, m_j<=log2 and L_j<=1.
The source-range guard also holds, rather than being inferred from a fixed-cutoff limit.
Indeed the explicit ceil bound gives

    J_j a_j<=a_j+(a_j/L_j)[log8+2log(1/L_j)].

Eventually W_j>=K a_j^(1/5)ell_j^(2/5)>=a_j^(1/5), so log(1/L_j)<=ell_j/5 and

    J_j a_j<=a_j+K^-1 a_j^(4/5)ell_j^(-2/5)
                                         [log8+2ell_j/5]
              ->0.                                 (16)

Therefore eventually J_j a_j<=h0, and EVERY hypothesis of the finite theorem is valid.
Formula(15) applies with the moving parameters, and gives

    log B_j<k_j m_j+k_j W_j.                         (17)

This deduction does not exchange a growing Fourier range with a fixed-input limit: the explicit estimate(16) verifies that whole growing range before use, and the untouched tail was already paid in(3)--(4).

Now impose the quantitative growing-count conditions

    k_j^2/d_j->0,
    k_j^5 (m_j/d_j)log^2(d_j/m_j)->0.                (18)

They imply k_j=o(d_j).
Also k_j Psi(a_j)->0, exactly by the second condition.
Since sqrt(a)/Psi(a)=a^(3/10)/log(1/a)^(2/5)->0, the square-root term contributes k_j sqrt(a_j)->0.
Finally

    k_j[2k_jlog625+16log(2d_j)+32]/d_j->0:

the quadratic term is the first condition, and k_j=o(sqrt d_j) implies k_jlog d_j/d_j->0.
Hence k_j W_j->0.
Equation(17) yields the quantitative conclusion

    limsup_j [log B_j-k_j m_j]<=0.                    (19)

If in addition k_j m_j->0, then log B_j->0, B_j->1 and the ORIGINAL raw objective Q_j00=B_j^2 tends to1.
Unlike C128's bounded-count corollary, this explicitly permits k_j->infinity.
Equivalently, the sufficient product-collapse regime can be written

    k_j=o(min{m_j^-1,sqrt(d_j),
                       [d_j/(m_j log^2(d_j/m_j))]^(1/5)}). (20)

Each quantity inside this minimum tends to infinity along a hypothetical input sequence, so(20) really contains unbounded integer factor-count sequences.
It is not a disguised bounded-k assumption.
No existence of a near-one Salem input sequence is supplied.

Conversely, under(18), retaining a fixed raw product gain B_j>=exp(gamma)>1 forces

    liminf_j k_j m_j>=gamma.                         (21)

The ACTUAL total m, rather than m/d, enters this final radial payment.
Omitting the k m term would be unjustified.
The theorem leaves open whether this necessary accumulation of exterior gain can ever coexist with an affordable residual in this construction.

<a id="degree-scale-corollary"></a>
## 5. A simpler original-degree scale, retaining the radial price

A useful sufficient scale for(18), on ANY such hypothetical near-one sequence, is

    k_j=O(d_j^(1/5)/(log d_j)^(2/5)).                 (22)

The first condition in(18) is immediate.
Since m_j<1 eventually, write ell_j=log d_j+log(1/m_j).
The second condition is bounded by a fixed constant times

    m_j[1+log(1/m_j)/log d_j]^2
      <=2m_j+2m_j log^2(1/m_j)/(log d_j)^2 ->0.        (23)

Here m log^2(1/m)->0 is the elementary exponential limit.
Thus (19) and(21) hold throughout(22), with no assumed rate for m_j->0.
To conclude B_j->1 one must STILL require k_jm_j->0; the degree scale alone does not supply it.
In particular, this does not rule out every polynomially growing count when m tends slowly to zero.

The powers1/5 and2/5 are sufficient exponents from the accepted angular modulus and its paid sum, not claimed optimal.
A coarse replacement of all epsilon(na) by epsilon(Ja) would carry additional logarithmic factors; the actual weighted estimate(2) is what gives(22).
The explicit finite statement, not the big-O shorthand, is the operative bound for an individual input.

<a id="moving-cutoff-source-and-contribution-boundary"></a>
## 6. Exact reuse, contribution boundary and remaining scope

The accepted construction and required residual facts are the actual [C128 complete argument](Yin_C_G0128_v1.md#argument), especially its [exact multiple-factor repair](Yin_C_G0128_v1.md#multiple-trace-factor-exact-repair), [short-residual node estimate](Yin_C_G0128_v1.md#effective-residual-degree-and-node-test), and [large-radius monotonicity with its guard](Yin_C_G0128_v1.md#finite-multifactor-all-scale-obstruction).
Its selected whole-reviewed decision adopts [R798](../audits/reviews/Yin_R_G0798_v1.md#multiple-factor-whole-independent-finding), which does NOT review this new moving-cutoff proof.
The author contributed C128 and is not its independent reviewer.

The actual angular theorem is [L229](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence), used separately with finite T=n and na<=h0.
Its accepted Pri11 compact Lipschitz discrepancy and Dim19 house-to-powered-height source scopes are unchanged.
[C125](Yin_C_G0125_v1.md#finite-angular-residual-growth) supplies the previous finite-angle/radial proof to compare, but its fixed beta separation and fixed-cutoff limits are NOT substituted into this moving statement.
The frequency-weighted estimate, new radial gap W, finite source-range check and growing-count limits are proved explicitly here.
No infinite-frequency external theorem or original source-proof re-audit has been performed.

Root contributed the substantive moving-cutoff proposal through the implication B>=exp(gamma) => max b_i>=exp(gamma/k), and explicitly requested that all J,L,H,epsilon and original costs be retained.
The strategy_critique author supplied the improved weighted summation, the radial L=m+W refinement, the explicit finite constants and the complete derivations.
Root therefore cannot serve as the independent reviewer of this new proof.
Separate review by a noncontributor of the actual fixed whole artifact remains necessary before independent adoption.
No native mathematical program or J was needed; all estimates are analytic finite inequalities.

The result closes a genuine subset of the many-near1-node interface: under(18) and k m->0, even an unbounded number of nodes cannot retain a fixed product gain at positive actual income.
It is neither a general constraint on all same-symbol repairs nor a proof that every growing-count product fails.
The full k=h C128 positive control is outside(18).
The universal diagonal-transfer control also remains outside this product-specific statement.
No inverse claim that passing the necessary bounds supplies a positive certificate is made.

For the unrestricted Task, the surviving regimes include sufficiently large factor counts, accumulated k m bounded away from0, or a different residual/Gram algebra.
No useful upper bound for their correction error, original uniform positive margin or near-one counterfamily is supplied here.
The additional arithmetic work required is retained as an open interface rather than absorbed into the symbols W or Psi.
The following author freeze records the complete current argument, not independent acceptance or Task completion.

<a id="moving-cutoff-entire-author-freeze"></a>
## Entire author freeze

2026-10-15T08:57.
The strategy_critique author freezes the ENTIRE D41: original question and root contribution, bounded reuse screen and candidate refinements, final Statement A--C, complete Sections1--6 and all23 numbered formulas, direct source interfaces and unresolved regimes.
The final actual full-file self-check reconstructed the exact C128 packet and actual-income scope; L229 applied separately at each finite T=n; dominance of the explicit modulus term; the numerical integral majorant and linear moment term; all +2 and tail expenses; the ceil cutoff and source-domain condition; both W-dependent angular inequalities; the moving radial gap beta-lambda and its W^4 payment; the effective-residual node estimate; constants1024,625 and both strict ratio comparisons; all branches for unbounded test b; the explicit growing J a limit; the max defining W after multiplication by k; the distinct k m, k^2/d and k^5 a log^2(1/a) limits; the simple original-degree scale; and the exact C128/source/review/contribution boundaries.

No remaining mathematical gap was found by this author check.
The proof uses no native mathematical program, numerical approximation or new external theorem.
Root is a mathematical contributor through the moving-cutoff mechanism and cannot independently review this new result.
An actual fixed whole review by a noncontributor remains to be arranged.
The original construction's full coefficient, denominator and spectral prices are unchanged and explicitly inherited, not waived.
A scoped material-format pass is separate from proof verification.
Neither this freeze nor the quantitative obstruction establishes a universal Mahler gap, all-construction exclusion, existence of a near-one sequence or Task completion.

## Fixed organization

The entire frozen author account is retained without mathematical abridgment.
The entire finite moving-cutoff bound and its growing-factor asymptotic consequence, all angular, radial, effective-degree and cutoff-domain costs.
Raw-product collapse additionally requires k times m tending to zero.
Root contributed the moving-cutoff mechanism and is not eligible as an independent reviewer of this argument.
Actual fixed whole independent review is pending.

## Current assessment
[Selected decision](#decision-isolated-current-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T09:00 |
| status | open |
| reason | The entire finite moving-cutoff bound and its growing-factor asymptotic consequence, all angular, radial, effective-degree and cutoff-domain costs. Raw-product collapse additionally requires k times m tending to zero. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Moving-cutoff product-residual obstruction](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Complete frozen argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Direct accepted interface](Yin_C_G0128_v1.md#statement) | Exact multiple-factor residual interface, original degree and positive actual-income obstruction. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T09:12 |
| status | proved |
| reason | Adopt the complete noncontributor [R798 original moving-cutoff](../audits/reviews/Yin_R_G0798_v1.md#moving-cutoff-whole-independent-finding) finding of the finite moving-cutoff obstruction and growing-factor conclusions. Retain km and all original angular/radial costs. Add the directly used L229 input omitted from the initial table without changing the proof; all larger-count or different-algebra regimes remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Moving-cutoff product-residual obstruction](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Complete frozen argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Direct accepted interface](Yin_C_G0128_v1.md#statement) | Exact multiple-factor residual interface, original degree and positive actual-income obstruction. |
| dependency | [Exact body-used input](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Direct finite angular modulus at T=n with nm/d in its stated domain, all original powered-degree multiplicities and existing source scope. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0798_v1.md#moving-cutoff-whole-independent-finding) | Entire fixed mathematical account, exact original costs, all boundaries and disclosed contribution limits. |


### Decision isolated-current-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:50 |
| status | proved |
| reason | Adopt the new isolated R798 whole finding for this exact highest physical statement and complete argument, after necessary fixed-mathematics/source inspection and subsequent comparison with all original review accounts. Preserve the complete current mathematical status, input relations and scopes, all original costs and open coverage limits. R798 separately retains the original unknown findings, dates, exact historical bindings, missing-table observations and negative predecessor findings; this new independent review does not retrospectively upgrade them or claim source-proof audits or Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Moving-cutoff product-residual obstruction](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Complete frozen argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Direct accepted interface](Yin_C_G0128_v1.md#statement) | Exact multiple-factor residual interface, original degree and positive actual-income obstruction. |
| dependency | [Exact body-used input](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Direct finite angular modulus at T=n with nm/d in its stated domain, all original powered-degree multiplicities and existing source scope. |
| review | [Isolated current whole finding](../audits/reviews/Yin_R_G0798_v1.md#g131-current-whole-independent) | Entire exact current statement and complete argument, every necessary original/current mathematical interface, original norms/weights/times/costs, source depth, finite controls and explicit limits; old physical-version and relationship findings remain separate in R798. |
