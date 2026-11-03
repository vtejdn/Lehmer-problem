---
author: Yin
---

# G0001: the binary law gives actual group Følner sets with explicit costs

The current complete mathematical proof is retained in [C289](../claims/Yin_C_G0289_v1.md#argument).
The original mathematical text below remains the fixed old input; current Claim adoption does not rewrite its old date or review bindings.

Date: 2026-10-07.
Direct reconstruction by the assigned review_matrix_completion AI agent for Yin.
The coordinator proposed the product-height lift and the free group-ball overlap test.
This note proves their exact normalizations, extracts finite sets, and compares the result with the original Mahler cost.
It reuses [L G0092](Yin_L_G0092_v1.md#effective-binary-near-invariance-time), the elementary grid proof in [L G0091](Yin_L_G0091_v1.md#norm-grid-support-bound), and the accepted entropy comparison in [L G0089](Yin_L_G0089_v1.md#mahler-to-binary-min-entropy).
No new source or computation is used, and no novelty is claimed for the general coarea or group-ball arguments.

Let alpha be a nontorsion algebraic unit, O=Z[alpha], d=[Q(alpha):Q], A multiplication by alpha, and m=log M(P)>0.
Define

    Gamma=O semidirect_A Z,
    (x,j)(y,k)=(x+A^j y,j+k),
    a=(1,0), t=(0,1), S={a,a^(-1),t,t^(-1)}.

These generators generate Gamma: their conjugates give every alpha^j, and alpha^(-1) belongs to O because P is a unit polynomial.
All translations of measures and sets below are LEFT translations.
Total variation is half the l1 distance.

<a id="binary-law-group-lift"></a>
## 1. Exact product-height lift

Let mu be any finitely supported probability on O, and set

    delta_a=TV(mu,tau_1 mu),  delta_A=TV(mu,A_*mu).

For an integer L>=0 put h=2L+1, I=[-L,L] intersect Z, and let rho(x,j)=mu(x)/h for j in I, zero otherwise.
Since

    a(x,j)=(x+1,j),       t(x,j)=(Ax,j+1),

the errors are exactly

    TV(a_*rho,rho)=delta_a,
    TV(t_*rho,rho)=(1-1/h)delta_A+1/h.                  (1)

Indeed there are h-1 common height layers, each contributing the original l1 difference divided by h, and two unmatched height layers of mass 1/h.
The errors for inverse generators are equal to the corresponding forward errors.
Also

    |supp rho|=h |supp mu|.                            (2)

This is a lift to the regular action on Gamma, not merely a statement about the affine action on O, which has stabilizers.

The height cost has an elementary lower bound.
For any finitely supported probability eta on Gamma, let p be its height marginal, with H nonzero height levels.
Projection contracts TV, and

    TV(t_*eta,eta)>=TV(p,shift p)>=max_j p(j)>=1/H.      (3)

For the middle inequality, a finite sequence starts and ends at zero, so its total absolute variation is at least twice its maximum.
Thus height support of order 1/error is necessary for any such group lift, not just the product choice.

<a id="coarea-actual-folner-set"></a>
## 2. Coarea produces a finite set, with the boundary convention fixed

For a nonempty finite F in Gamma define

    b_s(F)=|sF symmetric-difference F|/(2|F|)
          =|sF minus F|/|F|,
    b(F)=b_a(F)+b_t(F).

Thus b_(s^(-1))(F)=b_s(F), each generator's one-sided boundary ratio is at most b(F), and the total directed edge boundary over the symmetric S is 2b(F)|F|.
These conventions must not be interchanged without their factors of two.

For a finite probability eta define F_u={g:eta(g)>u}.
The layer-cake identities are

    integral_0^infinity |F_u| du=1,
    integral_0^infinity |sF_u symmetric-difference F_u| du
          =||s_*eta-eta||_1=2TV(s_*eta,eta).

Therefore some nonempty level set satisfies

    b(F)<=TV(a_*eta,eta)+TV(t_*eta,eta),
    F subset supp eta.                                (4)

This is an exact finite construction: there are only finitely many distinct positive levels.
Applying (4) to the product rho above gives a set of the form E x I and

    b(F)<=delta_a+(1-1/h)delta_A+1/h,
    |F|<=h |supp mu|.                                  (5)

No assertion of efficient enumeration of its binary fibers is required for this existence statement.

<a id="binary-folner-degree-cost"></a>
## 3. Substitution of the actual binary-law bounds

For 0<epsilon<=1, L G0092 constructs the centered binary law mu from

    k=ceil[(2d/epsilon)log(8d/epsilon)],  N=2k-1,
    delta_a,delta_A<=delta=sqrt(2(m+epsilon)),
    log|supp mu|<=(m+epsilon)N.                         (6)

For 0<delta<=1 choose L=ceil[1/(2delta)] and h=2L+1.
Then 1/h<=delta and h<=4/delta.
Equations (5)--(6) give an actual nonempty finite F with

    max_(s in S) b_s(F)<=b(F)<=3delta,
    log|F|<=(m+epsilon)N+log(4/delta).                   (7)

In particular, for 0<m<=1/4 take epsilon=m.
There is an actual F with

    max_(s in S) b_s(F)<=6sqrt(m),
    log|F|<8d log(8d/m)+2m+log(2/sqrt(m)).               (8)

The support is also at controlled word distance.
Each centered binary translation uses exponents from -(k-1) to k-1.
Traverse this height interval, insert its at most N unit translations, and return to height zero; this costs at most 3N generator steps.
Appending a height j in I gives

    F subset B_(3N+L)(1).                              (9)

The harmless bound 3N is not optimized.
These are finite sets at the displayed error scale.
For a fixed positive-m input, (8) is not a construction of errors tending to zero from the same binary estimate.
For a hypothetical sequence m tending to zero, it produces sets with errors tending to zero in varying groups, with the displayed degree-dependent volume and time costs.

<a id="free-group-ball-folner-test"></a>
## 4. What a group growth lower bound actually forces

Let B_r be the radius-r ball for S.
If a finite probability eta has TV(s_*eta,eta)<=e for all s in S, telescoping gives TV(g_*eta,eta)<=re for g in B_r.
With K=supp eta this implies eta(gK)>=1-re.
For each x, at most |K| group elements g satisfy x in gK, since g=x y^(-1) for some y in K.
Summing yields

    |K|>=(1-re)|B_r|                  when re<1.        (10)

In particular, if max_s b_s(F)<=e, the uniform law on F gives

    |F|>=(1-re)|B_r|.                                  (11)

Equivalently, sum_(g in Gamma)|F intersect gF|=|F|^2 gives the same proof.
The free left action of the group on itself is essential to this counting step; replacing Gamma by its affine orbit of zero would introduce stabilizers and invalidate that count.

Let v_S=lim_R log|B_R|/R.
The limit exists and equals the infimum of those ratios, because B_(R+Q)=B_R B_Q.
For 0<e<1/2, choosing r=floor[1/(2e)] gives

    log|F|>=v_S floor[1/(2e)]-log2.                     (12)

Thus a growth lower bound supplies a volume requirement at reciprocal boundary scale.
It does not by itself turn a degree-dependent upper volume into a dimension-independent entropy lower bound.

<a id="group-growth-mahler-cost"></a>
## 5. The standard group growth itself has Mahler cost

The same norm grid gives a direct upper bound for these generators.
In a word of length R>=1, record its least and greatest visited heights u,v.
They satisfy u<=0<=v, v-u<=R.
Its translation coordinate is

    x=sum_(j=u)^v c_j alpha^j,   sum_j |c_j|<=R.

At a place with modulus rho>=1, |sigma(x)|<=R rho^v; at a place with rho<=1, |sigma(x)|<=R rho^u.
Both displayed radii are at least R.
For each fixed pair (u,v), the uncentered grid counts at most 4 times the radius in a real coordinate and at most the square of 5 times the radius in a complex coordinate.
As alpha is a unit,

    sum_(all embeddings, |alpha_i|>1) log|alpha_i|=m,
    sum_(all embeddings, |alpha_i|<1) log|alpha_i|=-m.

Consequently, for each fixed u,v and final height there are at most (5R)^d exp[m(v-u)] possible translation coordinates.
There are at most (R+1)^2(2R+1) choices of the pair and final height.
Hence

    |B_R|<=(R+1)^2(2R+1)(5R)^d exp(mR),
    v_S<=m.                                            (13)

For the reverse comparison, every binary word of length n gives

    (a^(xi_0)t)...(a^(xi_(n-1))t)=(S_n,n) in B_(2n).

Distinct translations give distinct group elements.
If h_0 is the binary support rate, submultiplicativity of the support cardinalities gives |T_n|>=exp(nh_0) at every n.
Therefore

    h_0/2<=v_S<=m,
    v_S>=(c_B/2) min(m,log2).                           (14)

The last inequality uses exactly the retained BV20/L G0089 Shannon lower bound and h_0>=h_1.
It does not assume h_0=m.
All remaining steps are elementary; no uniform exponential-growth theorem is silently imported.

There is a finite degree-controlled lower bound as well.
For n<=d the first n powers are independent, so |T_n|=2^n.
At any r, padding the ball radius if needed gives

    |B_r|>=2^(min(d,floor(r/2))).                       (15)

Applied to (11), this detects the initial free window, while (14) detects asymptotic growth.
Neither removes the degree dependence in (8).
In particular, substituting e=6sqrt(m) in (12) and the proved m-proportional lower growth bound gives a required logarithmic volume only of order sqrt(m) in the small-m regime.
A hypothetical input-uniform positive floor for v_S would already imply a Mahler gap by (13); it cannot be treated as an independent conclusion of the Følner lift.

## Primary-flow and review boundary

This construction attaches a finitely generated group to an integral irreducible unit core.
It does not identify an arbitrary rational algebraic flow with O or with Gamma.
The positive-weight existence reduction and the finite-capture interpretation retain exactly the scope of [L G0002](Yin_L_G0002_v1.md#capture-equivalence).
Replacing a rational flow by a selected unit-core group is a research reduction at that scope, not an equality of the original underlying groups.

The complete original author, separate-agent and coordinator checking account is retained in [R537](../audits/reviews/Yin_R_G0537_v1.md#complete-original-l96-checking-account).
Its old collaborator and independent wording is preserved there with the exact current relationship qualifications and original fixed inputs.
