---
author: Yin
---

# Full-collar projected observability and physical integer-response exclusion for Salem inputs

This retains the complete original 2026-10-08 [L144 mathematical argument](../ledger/Yin_L_G0144_v1.md).
The entropy_status agent derived the central/hyperbolic decomposition, projected Gramian, two-collar endpoint estimate and two-column discriminant bound.
The coordinator supplied the uniform constants and actual plastic-family phase separation; the assigned agent checked and assembled those contributions, and the coordinator actually checked the entire assembled proof.
The complete old account remains at R45, with the original contributor whole check and the separate whole inspection whose initial isolation is unestablished; neither is relabeled as a new current independent check.
No Task/E resumption, source acquisition, mathematical native run or algorithm implementation is performed by this maintenance.

## Statement

For every monic irreducible Salem minimal polynomial P of degree d=q+2 with q>=2 distinct unit-circle roots and off-circle roots exp(m),exp(-m), assume 0<m<=1 and let B>0 be rational.
For every nonnegative integer R use the exact finite closed cube x_j in [-1/2,1/2] on I_R={-R,...,R+d}, integer defects z_j=P(S)x_j for -R<=j<=R, nonzero origin defect and energy at most B.
Every nonzero P-divisible cluster on [a,b], with both raw length-L zero-defect collars inside [-R,R], has a nonzero integer response supported in [a+d,b] and one homogeneous difference expression on [a-L,b+L+d].
For each integer L>=2 the projected Gramian (3) is defined and positive semidefinite; it is positive definite for L>=d, and the two actual collars share the single coefficient bound B/(2 eta_L).
The scalar interpolation estimate (10), with all its endpoints in that one interval, excludes the integer-response branch whenever its right side is strictly below one half.
The explicit physical length L_obs=1+ceil[D_C+32q/m+32qB+16B] and every integer L>=L_obs satisfy that strict test, with no additional factor d.
The four-distinct-root determinant argument gives D_C<=D_hat in (12)--(13), retaining its exp(O(d log d+dm)) separation cost.
On the actual irreducible plastic-seed progression N=9 modulo120, N>=129, the full phase, wrap and chord proof gives the explicit endpoint length (16) of order O_B(d log d), compared with the old endpoint term of order Omega_B(d^3).
That family stays away from measure one and this comparison concerns the endpoint branch, not the whole flux cost or coercivity radius.
The physical maximum and safe monotone minimum in (17) combine the complete flux and endpoint tests for every nonzero cluster and with the unchanged finite closure.
The inequality (2m/q)L_obs>64 concerns this literal sufficient choice; it is no lower bound for the true first successful window or obstruction to the exact projected test, another argument, or an energy optimization.
No transition-product lower bound, uniform near-one coverage or resolution of G0001 is asserted.

## Current assessment
[Selected decision](#decision-retained-registration)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T12:14 |
| status | open |
| reason | Retain the complete exact theorem and original reasoning; actual current whole checking and adoption are recorded separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original Sections1--7/(1)--(17), exact finite homogeneous interval and response support, projected Gramian and positivity, shared 2 eta_L energy, explicit 32q/m loss, scalar minima, sinh and strict half bound, four-column discriminant and separation cost, complete actual-family phase, wrap and chord proof, physical max/min flux closure and every sufficient-versus-actual limitation. |
| argument | [Complete argument](#argument) | Entire original Sections1--7/(1)--(17), exact finite homogeneous interval and response support, projected Gramian and positivity, shared 2 eta_L energy, explicit 32q/m loss, scalar minima, sinh and strict half bound, four-column discriminant and separation cost, complete actual-family phase, wrap and chord proof, physical max/min flux closure and every sufficient-versus-actual limitation. |
| dependency | [Exact retained input](Yin_C_G0335_v1.md#finite-rational-energy-coercivity) | The exact finite closed-cube problem and compact minimum, with no infinite extension or changed integrality domain. |
| dependency | [Exact retained input](Yin_C_G0341_v1.md#explicit-finite-energy-coercivity-radius) | Monic integral response, support [a+d,b], the single finite homogeneous interval, available collars and inherited finite closure. |
| dependency | [Exact retained input](Yin_C_G0346_v1.md#filtered-gap-energy-charge) | Only the fixed finite Gramian and root/filter conventions used by the original input; this proof controls full raw collars separately. |
| dependency | [Exact retained input](Yin_C_G0348_v1.md#joint-collar-flux-radius) | Exactly Phi, Psi, the shared two-collar flux proof and physical dT normalization; the old endpoint comparison remains endpoint-only. |
| dependency | [Exact retained input](Yin_C_G0336_v1.md#linear-exponent-cyclic-coverage) | The actual irreducible N=9mod120 family, degree N+3 and root band; the phase comparison here additionally requires N>=129. |

## Complete retained argument

<a id="argument"></a>

The fixed interfaces are [L G0130](Yin_C_G0335_v1.md#finite-rational-energy-coercivity), [L G0135](Yin_C_G0341_v1.md#explicit-finite-energy-coercivity-radius), [L G0140](Yin_C_G0346_v1.md#filtered-gap-energy-charge), [L G0141](Yin_C_G0348_v1.md#joint-collar-flux-radius), and the actual family in [L G0131](Yin_C_G0336_v1.md#linear-exponent-cyclic-coverage).

## 1. Domain and the finite homogeneous interval

Let P be a monic irreducible Salem minimal polynomial of degree d, with exterior root alpha=exp(m), 0<m<=1.
Its other off-circle root is r=alpha^(-1)=exp(-m), and its q=d-2>=2 central roots beta_i are distinct.
All conjugates, including both members of each complex pair, are counted.
Thus P has constant coefficient one.
Let B>0 be rational, and retain the exact finite closed-cube problem defining E_R in L G0130.

Suppose a feasible x on I_R={-R,...,R+d} has energy at most B and integer defects z_j=P(S)x_j on [-R,R].
Consider a nonzero defect cluster contained in [a,b], with both length-L zero-defect collars

    G_-=[a-L,a-1],      G_+=[b+1,b+L] subset [-R,R].       (1)

The cluster need not contain the origin for the local conclusion below.
Assume its polynomial Z_c(t)=sum_(j=a)^b z_j t^(b-j) is divisible by P.
By the fixed monic-division interface, there is a nonzero integer w with support in [a+d,b], whose P(S)w equals the cluster defects and vanishes elsewhere.
In particular the case b-a<d cannot occur in this branch.

The difference v=x-w satisfies P(S)v_j=0 for every recurrence index a-L<=j<=b+L, and hence has a single homogeneous representation on [a-L,b+L+d]:

    v_j=c_j+y_j,
    c_j=sum_(i=1)^q c_i beta_i^j,
    y_j=A alpha^j+D alpha^(-j).                         (2)

These are real combined sequences.
On both raw collars v=x because w is zero there.
No recurrence outside the original available indices is used.
The coefficients in (2) can be complex with conjugate symmetry; relaxing that symmetry in a Gramian lower bound remains valid.

<a id="full-collar-projected-gramian"></a>
## 2. The exact full-collar projected Gramian

For L>=2 and 0<=t<L define the L by q matrix U and the L by 2 matrix H by

    U_(t,i)=beta_i^t,
    H_(t,1)=r^t,       H_(t,2)=r^(L-1-t).

The columns of H span precisely the two hyperbolic modes restricted to this interval.
Set

    S_L=sum_(t=0)^(L-1) r^(2t)=(1-r^(2L))/(1-r^2),
    H^*H=[[S_L,L r^(L-1)],[L r^(L-1),S_L]],
    C_L=U^*[I-H(H^*H)^(-1)H^*]U,
    eta_L=lambda_min(C_L).                              (3)

The two columns of H are independent because 0<r<1 and L>=2.
Thus (3) is defined and C_L is positive semidefinite.
For L>=d it is positive definite: if Uc belongs to range H, the resulting combination of all d distinct root columns vanishes on at least d consecutive indices, so the initial Vandermonde block forces all coefficients to zero.
All entries of (3) are algebraic for a fixed integer L.
Exact algebraic eigenvalue bounds or certified rational lower bounds may be used; none has been computed here.

Orthogonal projection away from the two hyperbolic columns gives

    ||Uc+Hh||_2^2>=c^*C_L c>=eta_L ||c||_2^2.             (4)

Shifting a collar to start u multiplies the central coefficients by the unitary diagonal diag(beta_i^u); it does not change their Euclidean norm or eta_L.
Hyperbolic coefficients are freely rescaled within range H.
Consequently each of the two actual collars in (1) has energy at least eta_L sum_i|c_i|^2.
Since the raw collars are disjoint, eta_L>0 implies

    sum_i|c_i|^2<=B/(2 eta_L),
    |c_j|<=epsilon_L:=sqrt(qB/(2 eta_L))
                         for every integer j.           (5)

The last inequality bounds the displayed finite homogeneous expression; it asserts no extension of x or of its cube constraints to other indices.

## 3. A uniform explicit loss, retaining degree and m

Write

    D_C=max_i sum_(k!=i) 2/|beta_i-beta_k|.

The central Gramian U^*U has diagonal L and off-diagonal absolute values at most 2/|beta_i-beta_k|.
Hence its least eigenvalue is at least L-D_C.
Each entry of H^*U has absolute value at most sum_(t=0)^(L-1)r^t and thus at most 1/(1-r).
The Schur subtraction in (3) therefore gives the entirely explicit bound

    eta_L>=L-D_C-
       2q/[(1-r)^2 (S_L-L r^(L-1))].                    (6)

This is a bound for the actual Gramian, not a substitution of a selected collection of individually small d-coordinate states.

For 0<m<=1 and L>=8/m, the denominator in (6) has a useful uniform lower bound.
The elementary inequalities 2<e<3, 1-r^2<=2m and e^m<3 give

    S_L>(1-1/65536)/(2m),
    L r^(L-1)=e^m (mL)e^(-mL)/m<24/(256m).

For the second inequality, t e^(-t) decreases for t>=8.
Subtracting the two displayed bounds gives S_L-Lr^(L-1)>1/(4m).
Also 1-r>=m/(1+m)>=m/2.
Substitution in (6) yields

    eta_L>=L-D_C-32q/m,             L>=8/m.              (7)

Strict inequalities above are more than required for this non-strict lower bound.
The loss is linear in q/m; it is not the m^(-4) loss obtained by separately inverting the hyperbolic annihilator on every central mode.
No inverse Vandermonde row norm appears in (3)--(7).

<a id="full-collar-endpoint-bound"></a>
## 4. Scalar hyperbolic interpolation inside the two collars

Choose a point l in G_- and a point s in G_+ minimizing x_j^2 on their respective raw collars.
The two minima share the actual energy budget:

    |x_l|^2+|x_s|^2<=B/L.                               (8)

For every core index a<=j<=b, one has l<j<s.
The solution y in (2) has the exact two-point interpolation formula

    y_j=A_j y_l+B_j y_s,
    A_j=sinh(m(s-j))/sinh(m(s-l)),
    B_j=sinh(m(j-l))/sinh(m(s-l)).                       (9)

Both coefficients are nonnegative, and A_j+B_j<=1 because sinh u+sinh v<=sinh(u+v) for u,v>=0.
In particular A_j^2+B_j^2<=1.
Using y_l=x_l-c_l and y_s=x_s-c_s, (5), (8) and (9) imply

    |v_j|<=sqrt(B/L)+2 epsilon_L
           =sqrt(B/L)+sqrt(2qB/eta_L).                  (10)

This avoids dividing a nearly coincident pair of hyperbolic eigenvectors in a d-coordinate endpoint state.
It is interpolation between two real observed scalar values, after the central component has been controlled by the full collar energy.
All chosen points and core indices lie in the single finite homogeneous interval already justified in Section 1.

Thus any L>=d with eta_L>0 and the right side of (10) strictly below 1/2 excludes the integer-response branch: some core w_j is a nonzero integer, whereas |x_j|<=1/2 and |v_j|<1/2 make x_j=w_j+v_j impossible.

A convenient fully explicit sufficient length is

    L_obs(P,B)=1+ceil[D_C+32q/m+32qB+16B].               (11)

It is at least 8/m and at least d, since q>=2 and m<=1.
Equation (7) then gives eta_L>32qB, while L>16B.
The two summands in (10) are strictly below 1/4.
The same conclusion holds at every L>=L_obs.
The expression (11) is a sufficient length, not the first successful length or a lower bound on such a length.
The exact test (3), (10) can be stronger and remains separately available.

<a id="degree-measure-separation-bound"></a>
## 5. An explicit degree-and-m bound for the remaining root separation

The D_C cost has not been suppressed.
It can be retained as exact algebraic root data, bounded through a special family, or bounded solely in terms of d,m as follows.
Put

    s_d=sum_(k=0)^(d-1) k^2=d(d-1)(2d-1)/6,
    D_hat=4(q-1)m exp((d-1)m) s_d d^((d-2)/2).           (12)

Then D_C<=D_hat.
To prove this for any pair of central roots beta,beta', start with V=(gamma_i^k)_(0<=k<d).
Replace the beta column by its difference from the beta' column, and independently the alpha column by its difference from the r column.
These two determinant-preserving operations involve four distinct columns.
The first new column has norm at most |beta-beta'|sqrt(s_d), by the geometric identity for beta^k-beta'^k.
The second has norm at most 2m exp((d-1)m)sqrt(s_d), because alpha^k-r^k=2sinh(km)<=2km exp(km).
Every remaining column has norm at most sqrt(d): they are central columns or the remaining stable column.

Since P is monic, integral and separable, |det V|=sqrt(|disc P|)>=1.
Hadamard's inequality therefore gives

    |beta-beta'|>=
       [2m exp((d-1)m)s_d d^((d-2)/2)]^(-1).             (13)

Summing the reciprocals in D_C proves (12).
No root computation or assumption of well-separated phases enters this bound.
In particular (11) has the coefficient-free, degree-and-measure upper bound obtained by replacing D_C with D_hat.
Its separation term can grow like exp(O(d log d+dm)); that explicit cost is retained.
This is not a claim of polynomial cost uniformly over all Salem inputs or of near-one coverage.

<a id="plastic-family-endpoint-cost"></a>
## 6. A strict asymptotic improvement on an adopted actual family

Use the actual L G0131 family

    P_N=t^N f+f*,   f=t^3-t-1,   f*=1-t^2-t^3,
    N=9 mod 120,   N>=129,   d=N+3,   q=d-2.

The fixed result gives irreducibility, exactly q central roots, and theta<alpha_N<4/3, where theta is the real root of f.
Since f(5/4)<0 and f is increasing above 1, theta>5/4.
Thus log(5/4)<m_N<log(4/3)<1, and 1/m_N<5 by log(1+x)>=x/(1+x) at x=1/4.

The exact identity

    t f+(t-1)f*=-1

implies |f(t)|>=1/3 on |t|=1, since |f*|=|f| there and |t-1|<=2.
Also |f'(t)|<=4.
Choose a continuous real lift of arg f(e^(i theta)) along the real theta axis.
The central-root equation P_N(e^(i theta))=0 is equivalent to H(theta) being an odd multiple of pi, where

    H(theta)=(N-3)theta+2 arg f(e^(i theta)),
    N-27<=H'(theta)<=N+21.                              (14)

The derivative bound follows from |d arg f/dtheta|<=|f'|/|f|<=12.
For N>=129 this phase is strictly increasing.
Between consecutive solutions on the circle, including the wrap to the same ordering lifted by 2pi, its increment is 2pi; an intermediate odd multiple would be another root.
Hence consecutive central-root angles are separated by at least 2pi/(N+21)=2pi/(d+18).

For cyclic rank distance k<=floor(q/2), both angular arcs between the two roots contain at least k consecutive gaps.
Their smaller arc is at least 2pi k/(d+18).
The chord bound sin u>=2u/pi on [0,pi/2] gives |beta_i-beta_j|>=4k/(d+18).
At each such rank there are at most two roots.
Consequently

    D_C<=(d+18) H_floor(q/2)
         <=(d+18)[1+log(q/2)].                          (15)

Combining (11) with 1/m_N<5 supplies the completely explicit upper choice

    1+ceil[(d+18)(1+log(q/2))+160q+32qB+16B].            (16)

For fixed B>0 this physical collar length is O_B(d log d).
By contrast the retained L G0141 endpoint term alone was 4Bd Psi^2>=2Bdq^2: each central inverse row has l1 norm at least one, so Gamma>=q and Psi^2>=Gamma^2/2.
That old physical endpoint term is Omega_B(d^3).
Thus (16) certifies a genuine asymptotic improvement of the endpoint cost on an infinite family of actual irreducible inputs, without a root-separation run.
This comparison concerns the endpoint branch, not the full flux cost, the final coercivity radius, or the actual E_R.
The family tends to the plastic-number measure and is not a near-one family.

<a id="full-collar-flux-interface"></a>
## 7. Safe use with the fixed flux test and the remaining boundary

For the Salem domain here let W=||P||_1, Z=floor(W/2), K=floor(W^2B).
If K=0 the fixed integer budget already rules out a nonzero defect.
Otherwise retain Phi and Psi from L G0141 and set

    A_*(ell)=min(K,Z(ell+1)),
    F(ell)=2B Phi A_*(ell)^(4/q) exp(2m ell/q),
    L_new(ell)=max{d[1+ceil F(ell)],L_obs(P,B)},
    L_best(ell)=min{L_flux(ell),L_new(ell)}.              (17)

At physical length L_new, the first d[1+ceil F] coordinates in both empty collars permit the existing shared-block flux/norm proof to force P|Z_c.
The full length L_new then permits Sections 1--4 to exclude that branch.
No extra factor d belongs on L_obs.
Both tests are valid local exclusions for every nonzero cluster; they do not require the cluster to contain the origin.
The minimum in (17) is safe because whichever length is selected carries its own complete proof.
It is nondecreasing and never exceeds the fixed L_flux.

In particular the existing origin-cluster closure, with s_0=0 and s_(j+1)=s_j+L_best(s_j), 0<=j<K, gives E_R>B whenever R>=s_K.
This is only an application of that fixed closure, not a new claim about a superior cluster-merging rule.
Every last collar and recurrence index remains inside the same finite interval, as in the fixed proof.

For hypothetical 0<m<=1/32 inputs the new sufficient endpoint cost is O(D_C+q/m+Bq), with the explicit degree-and-m bound (12) available.
The central-root separation cost can still be large.
Moreover the literal choice (11) has (2m/q)L_obs>64.
Thus retaining (11) within an exponential-envelope comparison cannot satisfy the old small-Euler-step condition.
This is a limitation of this convenient sufficient choice; it is not the inverse-row lower obstruction of L G0141, not a lower bound for the first true successful window, and not an obstruction to the exact projected-Gramian test (3), (10) or another argument.

The new information is a finite, Gamma/Psi-free endpoint proof with explicit degree,m and separation costs and a proved actual-family asymptotic improvement.
It supplies no transition-product lower bound, uniform near-one energy coverage, optimized E_R, or resolution of G0001.
