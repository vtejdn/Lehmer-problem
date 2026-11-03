---
author: Yin
---

# Effective primitive-trinomial positivity with a zero-compatible error bound

Date: 2026-10-10.
Fixed retention of the complete D G0050 proof and its full noncontributor review under the coordinating AI for Yin's explicit adoption instruction.
The retaining orbit_research AI authored the local coarse repair and cutoff; the coordinator supplied none of those derivations and independently checked the whole argument and specified primary preprint passages.
The accepted external interface, questioned later source steps and actual inspection boundaries remain distinct.

<a id="effective-trinomial-cutoff-fixed-scope"></a>
## Adopted conclusion and retained source scope

For every primitive exponent pair0<b<a, gcd(a,b)=1, the complete doubling phase balance of f=t^a-t^b-1 satisfies Delta>1/500 whenever a>=2^2049.
More precisely, for either fixed polynomial F or G in the [complete proof](#effective-trinomial-phase-cutoff), the specialization error is at most

    E(q)=2^26 q^(-1/40)+6(log q+9)exp(-sqrt(q)/44),
    q=max(b,a-b)>=1024.

This makes the earlier L179 eventual-positivity boundary effective.
The cutoff is deliberately very large and does not make the remaining finite range practical to enumerate or prove that it contains no sign exceptions.
All factors and leading coefficients remain in the measures; no controlled-small-measure or unrestricted G0001 conclusion follows.

The sole newly accepted external input is BGMP24's earlier Proposition4.10 at its exact preprint statement/applicability scope, with the underlying sublevel theorem retained externally.
The local branch and Fourier argument avoids the false later numerical comparison in the inspected Theorem4.1 proof.
That questioned comparison is not a polynomial counterexample to the theorem's numerical assertion, and the source inspection is not a full-paper audit.
The independently reviewed cutoff remains valid at its explicitly accepted earlier-input scope.

The entire original proof, preliminary checkpoints, source findings and full independent review follow.
Dated pending-review or draft-status wording preserves the history at writing; the present adoption and appended review determine current status.
Only heading depth and relative navigation are relocated.
No new numerical run or source-proof inspection was performed by retention.

<a id="retained-effective-trinomial-cutoff-argument"></a>
## An effective degree cutoff for primitive trinomial phase balance

Date: 2026-10-10.
Assigned orbit_research AI for Yin.
The [fixed paired sign boundary](Yin_L_G0179_v1.md#phase-sign-boundaries-fixed-scope) proves eventual primitive-trinomial positivity without a degree cutoff.
This new bounded follow-up checks an existing effective Lawton theorem including zeros, with the aim of an explicit sufficient cutoff rather than a larger numerical scan.
It does not reopen the frozen L179 mathematics.


Current result after the bounded source check: the exact earlier zero-compatible regularization interface is now accepted at its disclosed inspection depth, and the complete local proof below gives Delta_(a,b)>1/500 whenever gcd(a,b)=1 and a>=2^2049.
The questioned final constant in the printed source is not used.
This is a self-checked new deduction awaiting independent project review, not fixed adoption or an all-degree sign result.
The earlier checkpoints below are preserved as chronology.

The current retained source is the [published BGMP24](../literature/pdf/BGMP24.pdf).
Its Proposition4.10, printed pp.1429--1431 / PDF pp.24--26, and the branch/Fourier passages, pp.1431--1434 / PDF pp.26--29, match the originally accepted interfaces.
The2026-10-14 source comparison preserves the numerical objection at equations(4.25)--(4.26), pp.1436--1437 / PDF pp.31--32; it changes neither this proof nor its original review scope.

### Historical checkpoint before the separate global-control review

On2026-10-10 the arXiv2203.12259v2 artifact was acquired and its title/version and PDF pages6 and14 visually inspected.
The published PDF was text-inspected via the primary Numdam endpoint, printed pp.1420 and1436--1437.
Both versions contain the same unsupported final constant comparison: the prefactor50 k^2(18 n k^2)^(n-1)e^n/[n(k-1)]^(n-1) is claimed to be at most8(36 e k)^(n-1).
For n=2,k=3 their ratio is(2025/48)e>1.
Thus this step is numerically false; the claimed optimizing alpha=n(k-1)/log(rho) also differs from the actual optimizer(n-1)(k-1)/log(rho), though the chosen alpha may still be used without an optimality claim.
This is a finding about the displayed proof step, not a counterexample to the stated Mahler bound.
No author contact, erratum search or full-paper audit has occurred.

A bounded repair route avoids the disputed final simplification altogether: use Proposition4.10 and Corollary4.14 with alpha=1/2 and epsilon=q^(-1).
For the fixed F and G of L179, n=2, k<=11, diam<=4 and coefficient-normalized length<=11.
The resulting candidate bound is

    |m(P(t^b,t^(a-b)))-m(P)|
       <=2^26 q^(-1/40)+6(log q+9)exp(-sqrt(q)/44),
    q=max(b,a-b), q>=1024.

If the two earlier source interfaces are accepted after their exact statement/applicability and affected proof checks, elementary inequalities make this bound less than2^(-24) for q>=2^2048, yielding the conservative cutoff a>=2^2049 and Delta>1/500.
This explicit calculation is a retained candidate pending those source checks, not an adopted cutoff.
It does not require evaluating any new trinomial or expanding an enormous polynomial.
The earlier fixed qualitative conclusion remains unaffected.

Work on this bounded follow-up yields priority to the separately assigned D51 review.
This is scheduling, not a strategy pause.
The next step is to record and check the two precise earlier source interfaces and finish the displayed error deduction, or to retain the questioned main constant as a clear scope boundary.


<a id="effective-trinomial-phase-cutoff"></a>
### 1. Effective statement and exact dependencies

For integers0<b<a with gcd(a,b)=1 retain the complete original balance

    f_(a,b)=t^a-t^b-1,
    G_(a,b)=((f*_(a,b))^2 f_(a,b)(t^2)
                         +f_(a,b)^2 f*_(a,b)(t^2))/2,
    Delta_(a,b)=log2+m(G_(a,b))-3m(f_(a,b)).

Every factor and leading coefficient stays inside the logarithmic Mahler measure.
The claim is the explicit sufficient bound

    a>=2^2049  =>  Delta_(a,b)>1/500.                 (1)

The conclusion is uniform over the indicated primitive exponent pairs.
It does not certify every lower degree or turn the residual range into a practical computation.
The exact finite exceptional question remains open.

Use the already fixed [L179 universal limit and its rational margin](Yin_L_G0179_v1.md#positive-trinomial-limit-certificate).
It gives fixed polynomials

    F(u,v)=uv-u-1,
    G(u,v)=u^4v^3-u^4v^2+u^3v^4-2u^3v^2+u^3v
             -u^2v^2+uv^3-2uv^2+u-v^2+v,
    Delta_infinity=log2+m(G)-3m(F)>1/250.            (2)

Their specializations at(u,v)=(t^b,t^(a-b)) are precisely the original f_(a,b) and G_(a,b), without discarded factors.
The new external input is only [BGMP24-U001's earlier Proposition4.10 regularization bound](../audits/literature/BGMP24/Yin_U001.md#bgmp24-u001), originally inspected in the preprint and now compared with the corresponding published passage, with the same acceptance limits.
The local analytic argument below is based on the same paper's Proposition4.11/Fourier mechanism and is explicitly attributed to it; it proves the required coarse bounds directly, avoiding the questioned Theorem4.1 final constant and its optimization.
No external novelty is asserted.

### 2. A uniform regularized error for the two actual polynomials

Put q=max(b,a-b).
Coprimality gives

    ker_Z(b,a-b)={ell(a-b,-b): ell in Z},
    rho(b,a-b)=q>=a/2.                              (3)

Normalize either actual polynomial by its maximum coefficient modulus: P=F for the seed and P=G/2 for the auxiliary.
Such scalar normalization changes both specialized and torus Mahler measures by the same constant, so it leaves their difference unchanged.
For both normalized polynomials

    L_infinity(P)=1, 3<=k(P)<=11,
    1<=D=diam(P)<=4, 1<=L1(P)<=11.                  (4)

In fact the auxiliary has exactly11 distinct support monomials and length13/2; the displayed common upper bounds are deliberately coarse.
Assume q>=1024, and take epsilon=q^(-1), alpha=1/2.
Define

    H_epsilon=(1/2)log(|P|^2+epsilon) on T^2.

The accepted Proposition4.10 applies to A=(b,a-b), and separately to the identity map for Haar measure on T^2.
The support does not collide under A because rho=q>D.
Each regularization cost is at most

    C2(2,k,1/2) epsilon^(1/(4(k-1)))
       =1728 k^4 q^(-1/(4(k-1))).

Adding the two costs and using k<=11 gives

    total regularization cost <=2^26 q^(-1/40),     (5)

since2*1728*11^4=50599296<2^26.
This is the step retaining the zeros of P and P_A.
No positive lower bound on the original polynomial's torus modulus is assumed.

For completeness the regularized Fourier estimate is proved next.
Let P*(z)=conjugate(P(1/conjugate(z))) and Q=PP*, so Q=|P|^2 on the torus, and put

    delta=min(sqrt(epsilon)/(D L1(P)),log(4/3)/D).

Consider the closed radial neighborhood C_delta defined by sum_j|log|z_j||<=delta.
For z_j=e^(h_j)u_j, |u_j|=1, the function g(h)=Q(e^h u) has nonnegative real value at zero and purely imaginary first derivatives there, since g(-h)=conjugate(g(h)).
Its second derivatives satisfy

    |partial_i partial_j g(h)|
       <=D^2 L1(P)^2 exp(D||h||_1).

Indeed every monomial of Q has exponent v-w, with each coordinate difference bounded by D.
The integral remainder in the real Taylor formula therefore gives

    Re Q(e^h u)>=-(1/2)D^2 L1(P)^2
                              exp(D||h||_1)||h||_1^2
                 >=-(2/3)epsilon   on C_delta.

Thus Re(Q+epsilon)>=epsilon/3>0, and the principal-branch function

    H(z)=(1/2)Log(Q(z)+epsilon)

is holomorphic on an open neighborhood of C_delta and restricts to H_epsilon on the torus.
This supplies the branch and zero guard directly.
Also |Q|<=(4/3)L1(P)^2 on C_delta.
With(4), q>=1024 and epsilon<=1, the modulus of Q+epsilon is between1/(3q) and163<q, and its argument has modulus less than pi/2.
Hence

    max_(C_delta)|H|<=log q+9=:M_q.                 (6)

For example the stronger bound(1/2)log(3q)+pi/4 suffices, using log3<2 and pi<4.
The looser(6) keeps the arithmetic simple and retains the essential factor1/2 that a line in the source's Lemma4.13 proof omits.

Let c_v be H's Laurent/Fourier coefficients.
Shifting the torus radius by delta in one coordinate attaining ||v||_infinity, with the appropriate sign, gives by Cauchy's integral formula

    |c_v|<=M_q exp(-delta ||v||_infinity).

These coefficients are absolutely summable.
Thus the difference between H's specialized circle integral and its full torus integral is the sum over the nonzero integer kernel vectors in(3).
Its modulus is at most

    2M_q exp(-delta q)/(1-exp(-delta q)).

From log(4/3)>1/4 and(4), for q>=1024 we have

    delta>=q^(-1/2)/44,
    delta q>=sqrt(q)/44>=8/11>2/3.

The second entry in the minimum defining delta is greater than1/16, while q^(-1/2)/44<=1/1408; the first entry is bounded below as displayed.
Since exp(2/3)>3/2, the geometric sum is at most6M_q exp(-delta q).
Combining this with(5)--(6) proves, for either original polynomial F or G,

    |m(P_original(t^b,t^(a-b)))-m(P_original)|
       <=2^26 q^(-1/40)
                   +6(log q+9)exp(-sqrt(q)/44)
       =:E(q),       q>=1024.                      (7)

Only the two regularization costs use the accepted external sublevel input.
The branch, Fourier and kernel estimates were checked directly here.
In particular the false final constant comparison identified in the source record is not a dependency of(7).

### 3. Exact cutoff arithmetic and scope

For q>=2^16 the elementary inequality log q+9<=sqrt(q) holds: sqrt(x)-log x-9 is increasing for x>=4, and at x=2^16 it exceeds256-16-9>0.
Also exp(t)>=t^2/2 for t>0.
Consequently the second term of(7) is at most

    12*44^2(log q+9)/q <2^15 q^(-1/2).

When q>=2^2048, the first term satisfies

    2^26 q^(-1/40)<=2^(26-2048/40)<2^(-25),

and the second is below2^(-1009).
Therefore

    E(q)<2^(-24),
    |Delta_(a,b)-Delta_infinity|<=E(q)+3E(q)
                                  <2^(-22)<1/500.   (8)

Equations(2)--(3) imply(1).
This is an explicit, very conservative finite degree boundary, proved without a numerical quadrature, parameter scan or expanded high-degree polynomial.
It resolves the previous non-effective cutoff obligation for this exact primitive trinomial class.
It supplies neither the signs of all pairs below the cutoff nor a controlled-small-measure statement for general height-one seeds.
The broader negative family retained in L179 is fully compatible with it.
No unrestricted Lehmer gap follows.

### 4. Actual work and review status

The orbit_research AI for Yin authored this local coarse repair and deduction after the source's final numerical comparison failed inspection.
The initial candidate expression and its pending status were retained above; after the separately assigned D51 review, the exact earlier regularization input, scalar normalization, full integer-kernel parameter, holomorphic branch, rank-one Fourier sum and cutoff arithmetic were checked as written.
The result now has a complete self-checked proof with the accepted external input precisely identified; independent review and fixed adoption are pending.

The source's arXiv-v2 title and four authors match the published bibliographic record; the actual edition and source inspection remain separate from work-level publication status.
The published final proof formulas were inspected online and agree with the preprint's questioned comparison, while the accepted earlier proposition is bound explicitly to the locally retained preprint.
No source-proof re-audit of the underlying Theorem4.6, broad erratum search, author communication, full-paper theorem adoption or computation was performed.
No new J is needed for these elementary inequalities.
L179's fixed proofs, conclusions and historical non-effective scope were left unchanged.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0081_v1.md#effective-trinomial-cutoff-independent-review), with its original inspected scope and relationship.



<a id="effective-trinomial-cutoff-retention-record"></a>
## Retention record

On2026-10-10 D G0050 was fully promoted after its complete noncontributor review passed.
Actual consumers in the BGMP24 source unit/readme, source navigation/registry and S1/S8 were repaired.
The source artifacts and accepted earlier input remain unchanged; only their application links move.
There is no new J or recalculation in this proof-only closeout.
Later substantive improvements require a separate mathematical version or responsible draft and appropriate review.
