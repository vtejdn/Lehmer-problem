---
author: Yin
---

# Exact original-core density from contracting unit cells

Root supplied the explicit beta-minus-one unit cells, exact quartic covolume, whole-core two-sided volume bounds and their sharp density/overlap constants.
Contributor original_signed_asymptotic checked and developed the full argument, reused the already known balanced trace unit, and derived the explicit all-radius counting error, Gaussian-count error and finite-dyadic consequences.
These are joint author contributions for Yin; no independent review or adoption is asserted here.

## Statement

Fix the actual quartic P=t^4-t^3-t^2-t+1, its exterior root beta, upper neutral conjugate zeta and O=Z[beta].
Write x_+,x_- for the beta,beta^(-1) embeddings, rho(x)=|x(zeta)|, B=1/(beta-1), S=beta B and tau=BS=(3+sqrt13)/2.
The actual original-digit accessible/coaccessible core is

    D={x in O:|x_+|<B,|x_-|<S}.

Put N(r)=card{x in D:rho(x)<=r}, for real r>=0, and

    Delta=13sqrt3/2,
    L_+=(1+beta+beta^2+beta^3)/2,
    L_-=(1+beta^(-1)+beta^(-2)+beta^(-3))/2,
    c_D=4pi BS/Delta=8pi BS/(13sqrt3).

There are TWO explicit integral-unit bases of the same actual order, indexed by integers k>=0.
For w=beta-1 set

    delta_+(w,k)=L_+(beta-1)^k,
    delta_-(w,k)=L_-(1-beta^(-1))^k,
    delta_c(w,k)=2tau^(k/2).

For v=beta+beta^(-1)-2, the already known balanced trace unit, set

    delta_+(v,k)=L_+tau^(-k),
    delta_-(v,k)=L_-tau^(-k),
    delta_c(v,k)=2tau^k.

For EITHER unit u in {w,v} and EVERY k>=0,r>=0 define

    A^+_(u,k)=(4pi/Delta)(B+delta_+)(S+delta_-),
    A^-_(u,k)=(4pi/Delta)(B-delta_+)_+(S-delta_-)_+.

The positive part is max(t,0).
Then the complete actual core count satisfies

    A^-_(u,k)(r-delta_c)_+^2
          <=N(r)<=A^+_(u,k)(r+delta_c)^2.             (UC1)

In particular the ENTIRE limit exists and is exact:

    lim_(r->infinity)N(r)/r^2=c_D.                    (UC2)

There is an explicit fixed-input error valid for EVERY real r>=1.
Set alpha_+=tau L_+, alpha_-=tau L_-,

    T0=B alpha_-+S alpha_+,
    T1=alpha_+alpha_-,
    E=(4pi/Delta)[8BS+9T0+9T1].

Then

    |N(r)-c_D r^2|<=E r^(3/2), r>=1.                 (UC3)

For every h>0 the full Gaussian CORE COUNT Sigma(h)=sum_(x in D)exp(-rho(x)^2/h) is finite.
It obeys, for each explicit cell,

    Sigma(h)<=A^+_(u,k)[h+delta_c sqrt(pi h)+delta_c^2],
    |Sigma(h)-c_D h|
       <=E Gamma(7/4)h^(3/4)+(2c_D+E)/h,
    lim_(h->infinity)Sigma(h)/h=c_D,                  (UC4)

where Gamma(7/4)=integral_0^infinity t^(3/4)exp(-t)dt<=1.
The second bound pays the unexpanded region0<=r<1 separately.

Now use ONLY the original iid digit law1/4,1/2,1/4, its complete return probability p_n, D_n=p_(2n)/p_n^2, true radius R and h_n=n/2+kappa with kappa=1/|1-zeta^2|.
For EACH cell put

    G_(u,k)(n)=A^+_(u,k)[h_n+delta_c sqrt(pi h_n)+delta_c^2].

Then for every n>=1,

    D_n<=G_(u,k)(n),
    R^n p_n>=1/[2G_(u,k)(n)],
    limsup_(n->infinity)D_n/n<=c_D/2=4pi BS/(13sqrt3),
    liminf_(n->infinity)n R^n p_n>=1/c_D=13sqrt3/(8pi BS).
                                                               (UC5)

Finite choices of these envelopes, and the earlier valid envelopes, may be combined by their pointwise minimum.
The analytically paid finite-dyadic tail is UC12 below.
The upper probability bound also admits the explicit error c_D h_n+E Gamma(7/4)h_n^(3/4)+(2c_D+E)/h_n.
The exact limits in UC2 and UC4 are STATE/GAUSSIAN COUNTS; no matching lower bound for the ORIGINAL weighted D_n is claimed.
There is no assumption of equidistribution, a maximal-order substitution, a changed stationary law, R=beta, critical-mean classification, positive diffusive bridge moment, varying-input uniform constant, new numerical radius certificate or unrestricted G0001 conclusion.

## Complete argument

### Reuse, actual source scope and the changed count

The adopted C400 fixed-quartic application supplies equality of the displayed strict strip with the ORIGINAL accessible/coaccessible core, using C396's actual narrow co-return premise at its retained computer-assisted and review scope.
C396 also supplies the actual degree-four order/embeddings and17/10<beta<18/10; no new native certificate is run.
The complete C645 original two-factor endpoint envelope and C555 true-radius dyadic identity are reused only after the new state count is proved.

A bounded current search for fundamental cells, parallelepipeds, covolumes, contracting units and lattice-density estimates found C560's actual-order half-open cell upper count, C44's classical cell/lattice attribution and C400's fixed-input O(r^2) two-sided count.
C401 already identifies v=beta+beta^(-1)-2=(beta-1)^2/beta as an actual order unit with both real embeddings contracting for this fixed P(1)=-1 input.
That unit and the elementary cell mechanism are not claimed new.
The new deduction uses explicit unit powers to shrink BOTH fixed real widths of a fundamental cell of the SAME lattice, proves complete two-sided cylinder bounds and a sharp leading constant, and uses the balanced unit for a paid error rate.
No general unit-existence theorem, logarithmic density, equidistribution or lattice-counting asymptotic is imported.
All determinants, coverings and limiting steps needed here are given below.

### Explicit units and exact real-coordinate covolume

Let theta_+=(1+sqrt13)/2 and theta_-=(1-sqrt13)/2.
They satisfy theta^2-theta-3=0, and

    P(t)=(t^2-theta_+t+1)(t^2-theta_-t+1).

For w=beta-1, substitution gives

    w^4+3w^3+2w^2-2w-1=0,
    w^(-1)=w^3+3w^2+2w-2 in O.

Thus multiplication by w is an integral automorphism of the ACTUAL order O.
Its two real absolute values are beta-1 and1-beta^(-1), both strictly below1.
At the neutral place,

    |w(zeta)|^2=2-theta_-=(3+sqrt13)/2=tau.

For the already known balanced unit v=theta_+-2, one has v^2+3v-1=0 and v^(-1)=v+3 in O.
Both real embeddings of v equal theta_+-2=tau^(-1), and its neutral value is theta_--2=-tau.
These explicit inverses suffice; no inference from a field unit to a possibly smaller order is needed.

Let V be the complex embedding matrix with columns1,beta,beta^2,beta^3 and rows the four embeddings beta,beta^(-1),zeta,conjugate(zeta).
Its determinant is the Vandermonde product of distinct conjugates.
The squared product is computed by separating the two quadratic factors:

    disc(P)=(theta_+^2-4)(theta_-^2-4)(theta_+-theta_-)^4
           =(-3)*13^2=-507.

Indeed theta^2-4=theta-1, whose product over the two theta values is-3, and the squared theta difference is13.
The cross-root product is(theta_+-theta_-)^2: evaluating the second quadratic at each root of the first gives(theta_+-theta_-) times that root, and their product is1.
This explains the fourth power and retains all conjugates.

Convert the last two embedding rows to real and imaginary parts by the two-by-two matrix with rows(1/2,1/2) and(1/(2i),-1/(2i)), whose determinant has absolute value1/2.
The REAL coordinate matrix M therefore has

    |det M|=sqrt(507)/2=13sqrt3/2=Delta.              (UC6)

This is the covolume of Lambda=M Z^4=tau_M(O) in(real+,real-,Re zeta,Im zeta) coordinates, with no extra sqrt2 scaling and no maximal-order index assumption.
The symbol tau_M denotes this embedding map only, distinct from the scalar tau=BS.

### Same-lattice cells and all-radius two-sided bounds

For either unit u in{w,v} and k>=0, the four elements u^k,u^k beta,u^k beta^2,u^k beta^3 form a Z-basis of the SAME order O, because multiplication by u^k has an integral inverse.
Let M_(u,k) be their real-coordinate embedding matrix.
The half-open centered parallelepiped

    F_(u,k)=M_(u,k)[-1/2,1/2)^4

has volume Delta, and its translates by Lambda tile R^4 with disjoint interiors and only measure-zero shared boundaries.
Triangle inequalities on its four coefficient coordinates give

    |y_+|<=delta_+(u,k), |y_-|<=delta_-(u,k),
    |y_c|<=delta_c(u,k), y in F_(u,k),                (UC7)

with EXACTLY the displayed two families of bounds in the Statement.
The neutral estimate is one half of the sum of four unit-modulus beta powers times |u(zeta)|^k, hence2|u(zeta)|^k.
No projected coordinate is treated as an integer.

Take all lattice centers with |x_+|<B, |x_-|<S and |x_c|<=r.
Their number is N(r) by the actual exact-core theorem, and their disjoint cells have total volume Delta N(r).
The union lies in the cylinder with real half-widths B+delta_+,S+delta_- and neutral radius r+delta_c.
Its volume gives the upper UC1 bound.

For the lower bound, if any reduced width or radius is nonpositive, the stated lower bound is zero.
Otherwise take the OPEN cylinder with real half-widths B-delta_+,S-delta_- and neutral radius r-delta_c.
Every point, outside the negligible cell boundaries if needed, belongs to some center's half-open cell.
Subtracting its cell coordinate and using UC7 puts that center STRICTLY inside both actual real strips and at neutral radius less than r.
Thus the entire inner cylinder is covered by cells counted in N(r), up to null boundaries.
Its volume gives the lower UC1 bound.
Using an open inner cylinder is what preserves the strict original-core inequalities; no boundary state is inserted into D.

For each FIXED unit and k, divide UC1 by r^2 and let r tend to infinity.
This bounds the liminf and limsup between A^-_(u,k) and A^+_(u,k).
Then let k tend to infinity: both real cell widths tend to zero, so both coefficients tend to c_D.
This proves the ENTIRE limit UC2, not a subsequence and not a joint limit with an unpaid neutral radius.

### Explicit all-r counting error from the balanced unit

Use u=v and, for every real r>=1, choose the integer

    k=floor(log_(tau)(sqrt(r))).

Then tau^k<=sqrt(r)<tau^(k+1), and hence

    delta_+<=alpha_+/sqrt(r),
    delta_-<=alpha_-/sqrt(r),
    delta_c<=2sqrt(r).                               (UC8)

At r=1 this is k=0, so no small-radius exception is hidden.
Write t=1/sqrt(r)<=1.
The upper UC1 bound and UC8 give

    N(r)<=(4pi/Delta)r^2(B+alpha_+t)(S+alpha_-t)(1+2t)^2.

Here (B+alpha_+t)(S+alpha_-t)=BS+T0 t+T1 t^2<=BS+(T0+T1)t and(1+2t)^2<=1+8t.
Their product is at most BS+[8BS+9T0+9T1]t, yielding N(r)<=c_D r^2+E r^(3/2).

For the lower bound use the elementary inequality

    product_j(1-y_j)_+>=1-sum_j y_j, y_j>=0.

If the sum exceeds1 its right side is nonpositive; otherwise it follows by expanding successive products and induction.
Apply it to the two real losses and TWICE the neutral radial loss in UC1.
Equations UC8 give

    N(r)>=c_D r^2
       -(4pi/Delta)[4BS+T0]r^(3/2).

This remains valid when an inner width vanishes, because the displayed loss bound then has nonpositive right side.
The latter constant is at most E.
This proves UC3 for every r>=1 with every fixed-input expense explicitly retained.

### Exact Gaussian core-count asymptotic and error

For h>0 the nonnegative layer identity gives

    Sigma(h)=integral_0^infinity (2r/h)exp(-r^2/h)N(r)dr.

Any fixed upper cell bound UC1 makes the integral finite.
Integrating its quadratic expression exactly yields the first inequality in UC4.
For the lower cell bound, (r-delta_c)_+^2>=r^2-2delta_c r, so

    Sigma(h)>=A^-_(u,k)[h-delta_c sqrt(pi h)].          (UC9)

Divide the two cell inequalities by h, first let h tend to infinity with k fixed, then let k tend to infinity.
Both limiting cell coefficients tend to c_D, proving the exact Gaussian COUNT limit in UC4 without a dominated-limit or equidistribution premise.

For its quantitative error, UC3 bounds |N(r)-c_D r^2| by E r^(3/2) for r>=1.
For0<=r<1, monotonicity and the r=1 upper estimate give

    |N(r)-c_D r^2|<=N(1)+c_D<=2c_D+E.

The mass of the layer kernel on[0,1] is1-exp(-1/h)<=1/h.
For the large-radius part substitute t=r^2/h; enlarging its nonnegative integral to all r>=0 gives

    integral_0^infinity (2r/h)exp(-r^2/h)r^(3/2)dr
       =h^(3/4)integral_0^infinity t^(3/4)exp(-t)dt
       =Gamma(7/4)h^(3/4).

This proves the second UC4 bound and explicitly pays the region not covered by UC3.
The elementary power-mean/Holder inequality with exponential density of mass1 and mean1 gives Gamma(7/4)<=1; no special-function numerical value is used.

### Original endpoint probability and the paid infinite-time limits

Retain precisely C645's original quantities

    nu_n(x)=Pr(sum_(j<n)eta_j beta^j=x), p_n=nu_n(0),
    w_n(x)=nu_n(x)nu_n(beta^n x)/p_n^2,
    D_n=sum_(x in D)w_n(x)=p_(2n)/p_n^2.

The actual normalized endpoint-product weight w_n retains all word multiplicities and both endpoint factors; its total mass is D_n.
C645 proves w_n(x)<=exp(-rho(x)^2/h_n) for every n>=1, h_n=n/2+kappa.
Summation therefore gives D_n<=Sigma(h_n)<=G_(u,k)(n), or the stated Gaussian error upper bound.
The state-count LOWER bounds do not give a lower bound on any w_n or on D_n.

For each fixed cell, h_(tn)<=t h_n for t>=1, so term by term

    G_(u,k)(tn)<=t G_(u,k)(n).

C555's exact true-radius identity is

    -log(R^n p_n)=sum_(j>=0)2^(-j-1)log D_(2^j n).

Using the preceding scaling bound gives-log(R^n p_n)<=log(2G_(u,k)(n)), proving the all-n UC5 lower normalized-return bound.
For fixed k, the ratio G_(u,k)(n)/n tends to A^+_(u,k)/2.
Hence limsup D_n/n<=A^+_(u,k)/2 and liminf nR^n p_n>=1/A^+_(u,k).
These inequalities hold for EVERY fixed k; letting k tend to infinity proves the two sharp stated constants in UC5.
No identification R=beta or finite-mean premise has entered this limit order.

For actual finite observations n,J>=1 define

    H_(n,J)=sum_(j=0)^(J-1)2^(-j-1)log D_(2^j n),
    H_n=-log(R^n p_n).

Applying the same scaling to the tail from m0=2^J n gives

    0<=H_n-H_(n,J)<=2^(-J)log(2G_(u,k)(2^J n)),
    exp[-H_(n,J)-2^(-J)log(2G_(u,k)(2^J n))]
          <=R^n p_n<=exp[-H_(n,J)].                   (UC12)

Every unobserved dyadic term is bounded analytically.
A pointwise minimum of any finite set of valid cell envelopes retains both the upper bound and the same scaling inequality, as do the earlier envelopes when their stated scaling condition holds.
One may choose the cell after specifying n,J; no claim of a cheap uniform optimizer or a new numerical certificate is made.

## Limits

The exact density counts actual core states, and the exact Gaussian limit weights those states only by the stated Gaussian function.
The complete original endpoint product is only bounded above by that function.
Neither a lower original word probability, a return local limit theorem, a positive linear midpoint level, a true-H approximation, a critical-mean classification nor unrestricted G0001 completion follows from the count lower bound.
The finite phase derivative gate in C828 and the continuation imbalance in C826 remain genuine unresolved original-law estimates.
No native program, enlarged finite graph, source acquisition or external theorem beyond the retained input scopes was used.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision unit-cell-density-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T11:35 |
| status | open |
| reason | Fix complete author unit-cell theorem: exact actual-order covolume and two explicit integral-unit bases, all-radius two-sided strict-core cylinder bounds, entire sharp density, balanced-unit all-r paid counting rate, exact Gaussian-count limit and finite error, complete original overlap upper envelope and true-radius all-n/dyadic/limiting consequences. Root and original_signed_asymptotic contributed. Whole independent review remains outstanding. Lower state counts give no lower original probabilities, mean branch or unrestricted Task result. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire unit-cell density statement](#statement) | Same actual fixed quartic/order/core, both explicit unit families and every k/r/h/n, exact covolume and count limits, paid all-r error and small-radius Gaussian piece, original upper and normalized-return bounds, all limits and exclusions. |
| argument | [Complete UC1--UC12 proof](#complete-argument) | Explicit unit inverses/conjugates and same-lattice basis, full Vandermonde/real-coordinate determinant, open-inner and outer tilings with strict boundaries, ordered limits and balanced integer scale, explicit error constants, Gaussian layers and finite small piece, original complete endpoint envelope and true dyadic costs. |
| dependency | [Actual exact core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Fixed-quartic strict strip equals the actual original accessible/coaccessible order core through C396's retained co-return premise; no arbitrary Salem extension. |
| support | [Quartic field and original certificate scope](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Existing irreducible degree-four order/unit/embeddings and beta interval; actual core premise at its retained certificate and review limits, without new execution. |
| support | [Existing balanced trace unit](Yin_C_G0401_v1.md#decision-complete-isolated-whole-adoption) | Already retained explicit actual-order v=(beta-1)^2/beta unit at P(1)=-1 with contracting real embeddings; not a newly claimed unit-existence theorem. Exact specialized inverse and conjugates are checked here. |
| support | [Classical actual-order cell count](Yin_C_G0560_v1.md#typical-minkowski-collision-lower-bound) | Existing real/imaginary full-lattice and half-open fundamental-cell volume mechanism and covolume convention; the present explicit unit lower/upper cylinders and sharp limits are proved in this argument. |
| dependency | [Complete original endpoint product envelope](Yin_C_G0645_v1.md#decision-whole-reviewed-2026-10-23) | Both original normalized endpoint factors and all-n Gaussian upper bound w_n<=exp(-rho^2/h_n), actual complete D_n and unchanged original weights; no probability lower bound imported. |
| dependency | [True-radius dyadic identity](Yin_C_G0555_v1.md#decision-isolated-whole-review-adoption-20261022) | Exact full nonnegative dyadic identity at the actual R and complete chronological probabilities; no finite extrapolation or radius equality assumed. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T12:01 |
| status | proved |
| reason | Root read the complete fixed unit-cell proof and whole independent R1010 and adopts the exact actual-order covolume, both same-lattice unit families, strict-core two-sided count, exact density and Gaussian-count limits, all-r error and complete original upper/dyadic consequences without substantive repair. Normalized endpoint weights retain totalD_n. Count lower bounds do not supply original probability lower bounds, a critical-mean branch or unrestricted Task conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire unit-cell density statement](#statement) | Same actual fixed quartic/order/core, both explicit unit families and every k/r/h/n, exact covolume and count limits, paid all-r error and small-radius Gaussian piece, original upper and normalized-return bounds, all limits and exclusions. |
| argument | [Complete UC1--UC12 proof](#complete-argument) | Explicit unit inverses/conjugates and same-lattice basis, full Vandermonde/real-coordinate determinant, open-inner and outer tilings with strict boundaries, ordered limits and balanced integer scale, explicit error constants, Gaussian layers and finite small piece, original complete endpoint envelope and true dyadic costs. |
| dependency | [Actual exact core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Fixed-quartic strict strip equals the actual original accessible/coaccessible order core through C396's retained co-return premise; no arbitrary Salem extension. |
| support | [Quartic field and original certificate scope](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Existing irreducible degree-four order/unit/embeddings and beta interval; actual core premise at its retained certificate and review limits, without new execution. |
| support | [Existing balanced trace unit](Yin_C_G0401_v1.md#decision-complete-isolated-whole-adoption) | Already retained explicit actual-order v=(beta-1)^2/beta unit at P(1)=-1 with contracting real embeddings; not a newly claimed unit-existence theorem. Exact specialized inverse and conjugates are checked here. |
| support | [Classical actual-order cell count](Yin_C_G0560_v1.md#typical-minkowski-collision-lower-bound) | Existing real/imaginary full-lattice and half-open fundamental-cell volume mechanism and covolume convention; the present explicit unit lower/upper cylinders and sharp limits are proved in this argument. |
| dependency | [Complete original endpoint product envelope](Yin_C_G0645_v1.md#decision-whole-reviewed-2026-10-23) | Both original normalized endpoint factors and all-n Gaussian upper bound w_n<=exp(-rho^2/h_n), actual complete D_n and unchanged original weights; no probability lower bound imported. |
| dependency | [True-radius dyadic identity](Yin_C_G0555_v1.md#decision-isolated-whole-review-adoption-20261022) | Exact full nonnegative dyadic identity at the actual R and complete chronological probabilities; no finite extrapolation or radius equality assumed. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1010_v1.md#whole-unit-cell-density-finding) | Entire saved statement and UC1--UC12, actual-order units/covolume and clipped strict cells, every ordered limit and explicit small-radius error, original endpoint-weight upper bound and complete dyadic normalization, all input scopes and exclusions. |

