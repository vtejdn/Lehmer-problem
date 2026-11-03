---
author: Yin
---

# The actual finite-window cost of a four-term defect

Date: 2026-10-08.
Bounded G0001 cost test by the assigned growth_arithmetic_status AI for Yin.
This AI derived and checked the three-gap specialization, the actual strict-cube control, and the origin-anchored finite cutoff below.
The coordinator requested the test but did not contribute to these new derivations; its contributions to the already fixed L G0116/L G0119/L G0140/L G0145 are reused only as fixed interfaces.
Full independent review is recorded below.
No numerical run, new external source, optimization search, or novelty claim is involved.
The coordinator accepted this reviewed proof for fixed-ledger preservation on 2026-10-08.

The relevant fixed results are [L G0116](Yin_L_G0116_v1.md#unit-circle-scattering-coefficients), [L G0119](Yin_L_G0119_v1.md#three-interval-optimized-transient), [L G0140](Yin_L_G0140_v1.md#summed-gap-weighted-variance), [L G0144](Yin_L_G0144_v1.md#degree-measure-separation-bound), and [L G0145](Yin_L_G0145_v1.md#successful-cut-width-cost-control).

<a id="four-term-actual-gap-variance"></a>
## 1. Three actual gaps and their exact scalar variance

First use the general L G0140 domain: P is a monic irreducible integer unit polynomial with positive logarithmic Mahler measure and q>0 unit-circle roots.
All its roots are distinct and nonzero.
No root is a root of unity.
Write P=CQ, where C is the monic factor of all central roots and Q is the monic factor of the other h roots.
Put

    W_Q=||Q||_1,
    D_C=max_i sum_(k!=i) 2/|beta_i-beta_k|,
    (G_n)_(i,k)=sum_(t=0)^(n-1) conjugate(beta_i)^t beta_k^t,
    g_n=lambda_min(G_n),              g_0=0,
    omega(J)=g_max(J-h,0)/W_Q^2.                          (1)

Here J is a nonnegative integer.
All conjugates, including both members of complex pairs, are counted.
The fixed geometric-sum estimate is g_n>=max(n-D_C,0).

Let L>=3 be an integer.
The convention Z(t)=sum_j z_j t^(-j-1) identifies

    Z_L(t)=(1+t)(1-t^L)
    z_(-L-2)=z_(-L-1)=-1,       z_(-2)=z_(-1)=1.          (2)

Suppose an actual real finite vector x has these four defects in the displayed range, and no defects in the three raw gaps

    G_-=[-L-2-T,-L-3],   G_0=[-L,-3],   G_+=[0,T-1],     (3)

where T>=1.
Thus their lengths are T,L-2,T.
The full recurrence range [-L-2-T,T-1] and all its required x coordinates through T+d-1 must be available; no recurrence outside that finite range is used.
Other energy outside these raw gaps is merely nonnegative.

In the normalization of L G0140, central gap amplitudes are a_(j,beta)=Q(beta)c_(j,beta).
Define

    u_beta=(1+beta)/C'(beta),       zeta_beta=beta^L,
    U=||u||_2^2>0,                A_L=||(1-zeta)u||_2^2.

The exact flux jump formula, including every intervening defect, gives the three amplitudes

    a,                 a-zeta u,                 a+(1-zeta)u.
                                                               (4)

Indeed the left pair contributes -(beta^(L+1)+beta^L)/C'(beta)=-zeta_beta u_beta; the right pair contributes (beta+1)/C'(beta)=u_beta.
The initial a is arbitrary.
The fact U>0 uses beta!=-1 and C'(beta)!=0, not a quantitative separation assertion.
Also 0<=A_L<=4U.

Put w=omega(T), v=omega(L-2).
The disjoint actual gap energies and the single common-offset completion of squares give, if 2w+v>0,

    E >= w||a||^2+v||a-zeta u||^2+w||a+(1-zeta)u||^2
      >= [2wv U+w^2 A_L]/(2w+v).                         (5)

The second right side is exactly the minimum of the preceding scalar-weight quadratic expression over a.
It is not asserted to be the minimum energy of an actual cube-feasible x.
The two middle differences have squared norm U; the outside difference has squared norm A_L.
If 2w+v=0, the lower bound is zero.
No pairwise charge is summed twice.

For fixed P and T with w>0, v tends to infinity as L grows, and the final expression tends to 2wU, uniformly for 0<=A_L<=4U.
Thus this certificate does not charge linearly in a growing middle gap when the two outer collars stay fixed.
In contrast, if T=L, all three weights grow linearly with L for fixed P, so (5) gives a positive linear lower bound even along returns A_L->0.

This is the same three-region tradeoff exhibited for the binomial by L G0119, here with the fixed multiplier 1+t and the finite actual gap normalization of L G0140.
The latter permits arbitrary finite hyperbolic boundary data and does not assume a globally bounded extension.
It does not turn a fixed-P rate into uniform near-one coverage.

<a id="strict-cube-bounded-middle-control"></a>
## 2. A real strict-cube response with bounded middle energy

The saturation just described is compatible with actual cube realizability.
The following large-measure control refutes an unconditional linear-energy assertion for the middle gap alone.
It is not a small-measure construction.

For an integer A>=32 let

    P_A(t)=t^4-A t^3-t^2-A t+1
          =t^2 q_A(t+t^(-1)),       q_A(y)=y^2-Ay-3,
    D=sqrt(A^2+12),       y_+=(A+D)/2,   y_-=(A-D)/2.
                                                               (6)

One has A^2<A^2+12<(A+1)^2, so q_A is irreducible over Q.
Furthermore y_+>A>2 and y_-=-6/(A+D) lies in (-3/A,0).
The roots of P_A are alpha,r=alpha^(-1),beta,conjugate(beta), where alpha>1, alpha+r=y_+, and beta+beta^(-1)=y_-.
In particular alpha>A-1>2, r<1/2, and |beta|=1 with beta nonreal.

The field Q(y_-) is a real quadratic field, and beta is not in it because beta is nonreal.
Since beta satisfies t^2-y_- t+1=0 and y_-=beta+beta^(-1), beta has degree four over Q.
Thus P_A is its monic irreducible polynomial.
It is an integral unit polynomial with exactly one reciprocal exterior/interior pair and two central roots.
This proves the claimed Salem domain without assuming irreducibility from the shape of the polynomial.
Its Mahler measure alpha>A-1 is large.

At a root gamma with y=gamma+gamma^(-1), differentiation of (6) gives

    P_A'(gamma)=(gamma^2-1)(2y-A).
                                                               (7)

Put b_gamma=1/P_A'(gamma).
The two values |2y-A| are D>A.
For a central root, |beta^2-1|=sqrt(4-y_-^2)>3/2, since |y_-|<3/A<1/2.
For r<1/2 one has 1-r^2>3/4; for alpha>2 one has alpha^2-1>3.
Consequently the following deliberately conservative bounds hold:

    H:=sum_C |b_beta|<4/(3A),
    |b_r|<2/A,                 |b_alpha|<1/(3A).          (8)

Use the already proved causal-center kernel of L G0116:

    w_j=b_r r^j+sum_C b_beta beta^j,     j>=0,
    w_j=-b_alpha alpha^j,               j<0,
    P_A(S)w=delta_(-1).

For j>=0, |w_j|<=|b_r|+H<10/(3A).
For j<0, alpha^j<=alpha^(-1)<1/2, so |w_j|<1/(6A).
Thus ||w||_infinity<10/(3A).

For every L>=3 define the real sequence

    e_j=w_j+w_(j+1)-w_(j+L)-w_(j+L+1)
              +sum_C beta^L(1+beta)b_beta beta^j.         (9)

Conjugate symmetry makes it real.
Each shift of w gives the corresponding shifted delta, and the last sum is homogeneous.
Hence P_A(S)e has exactly the four integer defects (2), and no others.
This checks the forcing convention and every shift.
The kernel and the added central sum are bounded on all integers.
Equations (8)--(9) give the strict bound

    ||e||_infinity
       <=4||w||_infinity+2H<16/A<=1/2.                  (10)

Thus (9) is a genuine global strict-cube solution, not merely a formal residue or an unconstrained minimizer.

For -L<=j<=-2, both j,j+1 are negative and both j+L,j+L+1 are nonnegative.
The added central term in (9) cancels the two shifted central kernel terms exactly.
Therefore

    e_j=-b_alpha(1+alpha)alpha^j
                    -b_r(1+r)r^(j+L),       -L<=j<=-2.
                                                               (11)

The sums at these endpoints are finite parts of convergent geometric series.
They yield

    sum_(j=-L)^(-2)|e_j|
      <=|b_alpha|(1+alpha)/[alpha(alpha-1)]
                             +|b_r|(1+r)/(1-r)
      <13/(2A),
    sum_(j=-L)^(-2)e_j^2<169/(4A^2).                    (12)

Here (1+alpha)/[alpha(alpha-1)]<3/2 for alpha>2 and (1+r)/(1-r)<3 for r<1/2; (8) then supplies 1/(2A)+6/A.
The squared-sum bound follows from sum e_j^2<=(sum |e_j|)^2.

For clarity about the observed window, restrict (9) to the actual coordinate interval

    I_local=[-L-2-T,T+3],       T>=1,

for the recurrence indices [-L-2-T,T-1].
Its two raw collars are exactly (3), and P_A has degree four.
There are L+2T+6 coordinates in I_local, of which L-1 lie in [-L,-2].
By (10)--(12),

    sum_(j in I_local)e_j^2
          <(2T+7)/4+169/(4A^2).                         (13)

For fixed A,T this is bounded independently of L.
This is a genuine finite non-symmetric-window example with integer defects and strict cube membership.
It is not the original origin-anchored symmetric E_R problem.
That distinction cannot be removed by a translation without also changing which outside coordinates are observed.

<a id="origin-anchored-four-term-cutoff"></a>
## 3. The original anchored problem still charges a long gap

Now return to the exact finite closed-cube domain of L G0130: x is given on I_R={-R,...,R+d}, integer defects are constrained on [-R,R], z_0!=0, and E=sum_(I_R)x_j^2.
In this section assume P is a Salem minimal polynomial, with 0<m<=1, exterior root alpha=exp(m), and q=d-2>=2 central roots.
No globally bounded extension of x is assumed.

First consider any two actual zero-defect gaps of lengths at least J, separated by exactly two consecutive defects with the same coefficient 1 or -1 and no other intervening defect.
The jump has the form unit_phase_beta times (1+beta)/C'(beta), so its squared norm is U.
Put

    Q=(t-alpha)(t-alpha^(-1)),
    W_Q=2+alpha+alpha^(-1)<6.

The last bound uses alpha<=e<3 and alpha^(-1)<1.
Because P(-1) is a nonzero integer,

    product_C |1+beta|=|C(-1)|=|P(-1)|/W_Q>=1/W_Q.

Let V_C=(beta_i^k)_(0<=k<q).
Every column has Euclidean norm sqrt(q), so Hadamard gives

    D_*:=product_C |C'(beta)|=|det V_C|^2<=q^q.

This is an upper bound for the central factor's absolute discriminant; no integrality of that discriminant is asserted.
Arithmetic-geometric mean now gives

    U=sum_C |(1+beta)/C'(beta)|^2
       >=q[1/(W_Q D_*)]^(2/q)
       >=1/[q W_Q^(2/q)].                              (14)

If J>2+D_C, both weights in the L G0140 two-gap inequality are at least (J-2-D_C)/W_Q^2.
For positive a,b both at least c, ab/(a+b)>=c/2.
Thus every actual finite x satisfies

    E>=(J-2-D_C)/[2q W_Q^(2+2/q)]
       >=(J-2-D_C)/(432q).                             (15)

Indeed q>=2, W_Q>1, and W_Q<6 imply W_Q^(2+2/q)<6^3=216.
The non-strict last inequality is convenient.
In particular, J>2+D_C+432Bq excludes energy E<=B for any supplied B>0.
This charge is independent of an assumed initial central amplitude and already holds without the cube restriction.

Assume next that the whole constrained interval [-R,R] contains exactly a translated copy of the four defects (2), and no other nonzero defects.
All four positions must lie in that interval.
Since z_0!=0, there are just four translated position sets:

| Occupied indices | Empty outside gap | Its length | Forced lower bound |
| --- | --- | --- | --- |
| {-L-1,-L,-1,0} | [1,R] | R | R>=L+1 |
| {-L,-L+1,0,1} | [2,R] | R-1 | R-1>=L-1 |
| {-1,0,L-1,L} | [-R,-2] | R-1 | R-1>=L-1 |
| {0,1,L,L+1} | [-R,-1] | R | R>=L+1 |

In every case the middle zero-defect gap has length L-2.
It and the displayed outside gap are separated by one of the adjacent same-sign two-defect blocks.
Both gaps lie inside [-R,R], so all states and filter coordinates required by L G0140 lie in I_R.
Taking J=L-2 in (15) proves the explicit exclusion

    L>4+D_C+432Bq  implies  E>B.                        (16)

This covers arbitrary feasible finite x, with free central and hyperbolic data, and not only the special global response (9).
It explains why that response's bounded middle energy does not give an escape from the original E_R problem.
After origin anchoring, the symmetric observation necessarily includes a long outside interval where the offset has moved the energy.

The assumption of only these four defects throughout [-R,R] is essential for the last geometry.
If further defects are allowed in the outside interval, it need not be one empty gap.
One must then use the full multi-gap variance with those actual defects; no free long-collar charge is claimed.
The local three-gap formula (5) retains its own stated hypotheses independently.

<a id="four-term-cost-stop-boundary"></a>
## 4. Cost and the resulting stop criterion

Equation (16) is an explicit varying-Salem conditional cutoff for this forcing pattern.
It retains D_C.
The degree-and-m estimate in L G0144 can replace D_C, but can have exp(O(d log d+dm)) size.
Thus the calculation gives neither a small uniform near-one observation radius nor a new lower bound for an actual rounded transition product.
The fixed-P behavior and the distinction between tail suppression and growing-window energy agree with L G0116/L G0119.
The finite normalization and free-boundary coverage here follow directly from L G0140.

This closes the proposed four-term cost test without opening an additional optimization route.
Repeating its fixed multiplier, common-offset minimization, or root-data bookkeeping does not change the missing near-one input.
A further investigation should require new varying-input separation control, a new restriction on actual finite defect patterns, or an actual product lower bound.

For the arithmetic route, the current [S G0008](../strategies/Yin_S_G0008.md#next-coverage-test) and [L G0139](Yin_L_G0139_v1.md#encoding-inverse-and-cyclic-cost) retain a separate substantive gap.
The canonical half-degree seed encoding is an exact coordinate change: its odd cyclic norm gains only the factor two paying its added degree, while its even full returns vanish.
A near-one core forces failure of an exterior-root margin or of the sufficient exterior-count/relative-delay bound.

The next arithmetic mechanism must control those failures on a new varying-input class or give a core-specific partial return with certified positive surplus A(n)-d log 2 and a common exponent cost that does not depend on an unknown reciprocal measure 1/m.
An exterior-count, height, or phase-occurrence estimate is not enough unless it actually meets L G0139's hypotheses or L G0074's mass/time criterion.
No such new coverage input is proved here.
There is no new literature claim, experiment, uniform Lehmer gap, or resolution of the unrestricted G0001 contract.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0049_v1.md#contributions-and-actual-review), with its original inspected scope and relationship.
