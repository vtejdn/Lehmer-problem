---
author: Yin
---

# Literal improved collar minima, inverse-measure costs and same-input envelope cutoff

The full mathematical input is the original 2026-10-08 [L146](../ledger/Yin_L_G0146_v1.md).
Its necessary original fixed input, contributions, negative findings and review arrangements remain inspectable.

## Statement

For every hypothetical irreducible Salem input with q=d-2>=2 and 0<m<=1/32, and every rational B>=B_m in (1), retain the exact constants Phi, Psi and D_C and the literal local minimum L=min(L_flux,L_new) in (2), with physical L_obs carrying no extra d factor.
Use that same L in both the origin-centered and balanced sufficient radii of (3), and take R_use to be their minimum.
Then E_(R_use)>B, both branches satisfy the strict common bound (6), the two global lower bounds and R_use>R_0 in (8) hold, and the explicit parameter-dependent upper comparison has exactly the nesting count in (10).
Phi>=1; if also 0<m<=1/4096, the conditional radius satisfies the explicit inverse-m lower bound (12), without assuming any such Salem input exists.
For every fixed integer orbit length N>=1 and the actual enlarged product, multiplier/height/tail/window data specified below, N<=m M_0/(64 U(M_0)) forces the actual positive-part upper envelope to equal one at every integer R>=R_use.
For B>B_m, the displayed sufficient choice N>=N_suff, with equality allowed by the strict energy certificate, gives C_delta<16m; its threshold retains (15), including the full b_P and C_P rather than suppressing height cost.
These are costs and cutoff facts for the literal sufficient recipes, not lower bounds for the true first successful energy window or transition product, an optimized energy, necessity for other constructions, a uniform near-one gap or a resolution of G0001.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T12:19 |
| status | open |
| reason | Retain the exact whole theorem and complete necessary proof in its responsible home; actual full checking and adoption are recorded separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)–(15), both local/global minima, strict lower/upper comparisons, conditional inverse-m and same-input actual-envelope cutoff and sufficient-length costs. |
| argument | [Complete argument](#argument) | All literal physical lengths, K=1/floor/ceiling constants, Phi monic-row/matrix-column bound, full U/b_P/C_P and strict sufficient-length equality boundary, with non-necessity limits. |
| dependency | [Shared flux and endpoint cost](Yin_C_G0348_v1.md#joint-collar-flux-radius) | Exact Phi/Psi and two-case strict endpoint term, not a transplanted tower obstruction for the new branch. |
| dependency | [Projected observability](Yin_C_G0351_v2.md#full-collar-flux-interface) | Exact literal L_obs/L_new/L_best, all-cluster validity and physical length with no extra d. |
| dependency | [Balanced finite closure](Yin_C_G0350_v1.md#every-cluster-energy-coercivity) | Every nonempty actual cluster, exact balanced/origin-centered sufficient radii and nesting upper comparison. |
| dependency | [Actual energy envelope](Yin_C_G0337_v1.md#logarithmic-finite-energy-witnesses) | Complete logarithmic energy upper witness and enlarged Salem product with B_m, U(M), b_P and exact N/R/tail guards. |
| dependency | [Polynomial-height multiplier](Yin_C_G0328_v1.md#polynomial-height-central-approximation) | Exact fixed C_P>=1 with all conjugate-height/root parameters, no uniform height estimate. |
| dependency | [All-central domain guards](Yin_C_G0344_v1.md#all-central-coercivity-radius) | Original W>=3, rational B>2/15 and K>=1 guards at the specified hypothetical Salem target. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T12:23 |
| status | proved |
| reason | Adopt the actual whole self-review of both literal local/global minima, exact inverse-measure costs and same-input actual-envelope cutoff, retaining every height/tail/parameter and equality guard. These are costs for sufficient recipes and provide neither a least-window necessity nor a transition-product lower bound; the original separate relationship remains unknown. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)–(15), both local/global minima, strict lower/upper comparisons, conditional inverse-m and same-input actual-envelope cutoff and sufficient-length costs. |
| argument | [Complete argument](#argument) | All literal physical lengths, K=1/floor/ceiling constants, Phi monic-row/matrix-column bound, full U/b_P/C_P and strict sufficient-length equality boundary, with non-necessity limits. |
| dependency | [Shared flux and endpoint cost](Yin_C_G0348_v1.md#joint-collar-flux-radius) | Exact Phi/Psi and two-case strict endpoint term, not a transplanted tower obstruction for the new branch. |
| dependency | [Projected observability](Yin_C_G0351_v2.md#full-collar-flux-interface) | Exact literal L_obs/L_new/L_best, all-cluster validity and physical length with no extra d. |
| dependency | [Balanced finite closure](Yin_C_G0350_v1.md#every-cluster-energy-coercivity) | Every nonempty actual cluster, exact balanced/origin-centered sufficient radii and nesting upper comparison. |
| dependency | [Actual energy envelope](Yin_C_G0337_v1.md#logarithmic-finite-energy-witnesses) | Complete logarithmic energy upper witness and enlarged Salem product with B_m, U(M), b_P and exact N/R/tail guards. |
| dependency | [Polynomial-height multiplier](Yin_C_G0328_v1.md#polynomial-height-central-approximation) | Exact fixed C_P>=1 with all conjugate-height/root parameters, no uniform height estimate. |
| dependency | [All-central domain guards](Yin_C_G0344_v1.md#all-central-coercivity-radius) | Original W>=3, rational B>2/15 and K>=1 guards at the specified hypothetical Salem target. |
| review | [Complete current self finding](../audits/reviews/Yin_R_G0569_v1.md#literal-cost-whole-current-finding) | Entire original theorem, complete argument, actual dependency interfaces, negative/cost/source limits and original-review comparison, at its disclosed self-reviewed whole scope. |

## Complete retained argument

<a id="argument"></a>
### Fixed input, literal choices and constants

Use a hypothetical irreducible Salem input in the exact L G0132 domain: degree d, q=d-2>=2, m=log M(P) in (0,1/32], W=||P||_1.
Let B>0 be rational and satisfy

    B>=B_m=-2log(16m)/pi^2+m exp(-2m)/(32d^2),
    K=floor(W^2 B),        lambda=2m/q.                   (1)

Then W>=3, B>2/15 and K>=1 by the fixed L G0138 bounds.
All statements below concern these literal sufficient constructions, not an optimized finite energy value or the smallest valid window.

Retain exactly Phi and Psi from L G0141, D_C from L G0144, and put

    A_*(ell)=min(K,floor(W/2)(ell+1)),
    X(ell)=2B Phi A_*(ell)^(4/q) exp(lambda ell),
    L_flux(ell)=d[1+ceil(X(ell)+4B Psi^2)],
    L_obs=1+ceil[D_C+32q/m+32qB+16B],
    L_new(ell)=max{d[1+ceil X(ell)],L_obs},
    L(ell)=L_best(ell)=min{L_flux(ell),L_new(ell)}.        (2)

Here ell is a nonnegative integer and L is a positive nondecreasing integer function.
L_obs is a physical length, with no extra factor d.
These are precisely the safe local choices of [L G0144](Yin_C_G0351_v2.md#full-collar-flux-interface).
Neither the exact projected-Gramian test nor a sharper justified separation estimate is substituted into the definition (2).

Define the origin-centered and balanced sufficient radii with this SAME L:

    s_0=0, s_(j+1)=s_j+L(s_j), 0<=j<K,
    R_orig=s_K,
    F(1)=0, F(n)=(n-1)L(F(floor(n/2))), n>=2,
    R_bal=K L(F(K)),
    R_use=min(R_orig,R_bal).                             (3)

Both constructions are valid by the fixed local cube exclusion and [L G0143](Yin_C_G0350_v1.md#every-cluster-energy-coercivity).
In particular E_(R_use)>B.
Keeping the minimum prevents a lower bound on R_bal alone from being mistaken for a limitation of the available old-radius fallback.

<a id="literal-collar-radius-cost"></a>
### A common lower bound survives the local minimum

Put

    a=2lambda d B Phi=4mdB Phi/q,
    b_0=min(8B,64).                                      (4)

Both are positive, and b_0>1 in (1).
The two cases already proved in L G0141's endpoint calculation give the stronger common inequality

    lambda d(4B Psi^2)>8B.                               (5)

Indeed that proof gives >12B when dm<=1, and >4qB>=8B when dm>1.
On the other branch the literal formula in (2) gives lambda L_obs>64.
It follows that BOTH candidates in the minimum L are strictly greater, after scaling by lambda, than b_0.
Separately both are strictly greater than d X(ell), and A_*(ell)>=1.
Therefore

    lambda L(ell)>max{b_0,a exp(lambda ell)}.             (6)

This does not apply the old inverse-row obstruction to the new branch.
The constants 8B and 64 come from different valid bounds on the two branches, and their minimum is essential.
It does not assume a>=1.

Writing y_n=lambda F(n), (3) and (6) give, for n>=2,

    y_n>(n-1)max{b_0,a exp(y_floor(n/2))},
    y_n>(n-1)b_0.                                       (7)

The second inequality implies

    R_bal>2d K B Phi exp((K-1)b_0),
    R_orig>2d B Phi exp((K-1)b_0),
    R_use>R_0:=2d B Phi exp((K-1)b_0).                   (8)

For the balanced radius with K>=2, apply the exponential part of (6) to F(K) and use (7).
For the origin-centered radius, the constant part of (6) gives lambda s_(K-1)>(K-1)b_0 when K>=2, and its final step supplies the exponential bound.
When K=1 both radii equal L(0), and (6) proves the same displayed inequalities directly.
All bounds in (8) are strict.
A separately retained origin-centered radius with a collar function pointwise at least L is also at least R_orig.

### An explicit upper comparison retains all parameters

For completeness let

    A=2B Phi K^(4/q),
    C_flux=d(A+4B Psi^2+2),
    C_new=dA+max(2d,L_obs),
    C=min(C_flux,C_new).                                 (9)

The ceiling inequality 1+ceil(u)<=u+2 and exp(lambda ell)>=1 show L_flux(ell)<=C_flux exp(lambda ell) and L_new(ell)<=C_new exp(lambda ell).
Thus L(ell)<=C exp(lambda ell).
Define H_0=0 and H_(j+1)=K C exp(lambda H_j).
The fixed balanced comparison gives

    R_use<=R_bal<=H_(1+floor(log_2 K)).                  (10)

This is a finite explicit upper bound retaining Phi, Psi, D_C, degree, B and m, including the physical L_obs length.
The count 1+floor(log_2 K) is a nesting depth, not a proof that every level has a normalized exponential coefficient at least one or that the actual radius has a specific tower height.
Neither (9) nor (10) gives a practicable or degree-uniform complexity bound.

<a id="literal-inverse-measure-cost"></a>
### A uniform inverse-m lower cost in the smaller conditional domain

The elementary lower bound

    Phi>=1                                                (11)

holds without a numerical root estimate.
Each polynomial q_beta(t)=P(t)/(t-beta) is monic of degree d-1, so its squared coefficient norm is at least one and hence F_geo^2>=1.
The last column of the central coefficient matrix B_c consists of q ones, so ||B_c||_op^2>=q and F_mat^2>=1.
Their minimum Phi is at least one.

Now assume additionally 0<m<=1/4096, and set

    ell_m=log(1/(16m))>=log256.

Using log2>2/3 and pi^2<10 gives B>=B_m>16/15>1.
Therefore b_0>=8.
Also B>=B_m>ell_m/5, and the integer floor gives

    K>9B-1,
    (K-1)b_0 > (72/5)ell_m-16.

Substitution in (8) proves the genuine inverse-m bound

    R_use>2 exp(-16)d B Phi (16m)^(-72/5)
          >=2 exp(-16)d B (16m)^(-72/5).                (12)

No existence of a Salem input in this smaller range is assumed.
The bound applies conditionally to every such input and every rational B>=B_m, with all the definitions in (2)--(3).
It is a lower bound on the radius produced by those sufficient recipes, not on the least R with E_R>B.
Earlier exact energy windows are unrestricted by (12).

<a id="literal-same-window-cutoff"></a>
### Same-input cutoff and the free-length sufficient recipe

Every product statement in this section uses exactly the actual L G0132 enlarged Salem product.
For an integer N>=1, take a nonzero integral multiplier theta whose central conjugates have modulus at most sqrt(m)/(16q sqrt(N)); let H>=1 bound all conjugate moduli, and use delta_tail=sqrt(m(1-exp(-2m)))/16 and J=ceil(log(dH/delta_tail)/m).
C_delta denotes that fixed enlarged transition product.
No shorter J or unsupported amplitude lower bound is substituted.
The energy envelope itself needs no additional entropy/noise guard.

Use the complete fixed logarithmic upper witness of [L G0132](Yin_C_G0337_v1.md#logarithmic-finite-energy-witnesses),

    U(M)=q log M/(8m)+b_P,       M_R=2R+d+1,
    E_R<=U(M_R),
    b_P=25/32+[log(16d C_P)+(q/2)log(16q)]/(2m)
                        +3 exp(-2m)/[64(1-exp(-2m))].

Here C_P is exactly the retained L G0123 multiplier constant; no uniform bound on it is inserted.
Let M_0=2R_0+d+1, with R_0 from (8).
It is greater than three, and U(M)/M decreases strictly there.
For every fixed integer orbit length N>=1 satisfying

    N<=m M_0/[64 U(M_0)],                                (13)

ALL integer energy windows R>=R_use give only the value one in the actual L G0132 positive-part upper envelope.
Indeed R_use>R_0 implies M_R>M_0 and U(M_R)/M_R<U(M_0)/M_0<=m/(64N).
Hence E_R<=m M_R/(64N), so that envelope's positive part is zero.
This is a statement about the actual upper envelope, not merely failure to certify it from the lower bound B.
It excludes only the guaranteed-radius range; windows R<R_use remain available.

The same valid exclusion follows by replacing R_0 in (13) by the smaller uniform lower expression in (12), retaining the complete U including b_P.
Dropping b_P would not be a valid uniform cutoff comparison.

For the converse free-orbit-length sufficient recipe, require B>B_m and set g_B=sqrt(B)-sqrt(B_m)>0.
The strict certificate E_(R_use)>B and the same fixed envelope imply C_delta<16m when one chooses

    N>=N_suff:=m(2R_use+d+1)/(64 g_B^2).                 (14)

Equality in this sufficient condition is allowed because the energy certificate is strict.
Formula (8) shows

    N_suff>m d B Phi exp((K-1)b_0)/(16 g_B^2)
           >m d Phi exp((K-1)b_0)/16,

where the last inequality uses g_B^2<B.
In the smaller domain of (12), this yields

    N_suff>exp(-16)d/256 * (16m)^(-67/5).                (15)

This quantifies the cost of that displayed sufficient combination, even after keeping the old/balanced global minimum and the old/new local minimum.
It does not prove that the actual product, the exact energy at a smaller window, a larger certified energy at this window, or another amplitude construction requires N as large as (15).
No transition-product lower bound is obtained.

### Decision boundary

The literal choices (2) give both the explicit parameter-dependent same-input exclusion (13) and the uniform inverse-m cost (15) for their free-length sufficient use.
Logarithmic nesting depth and replacement of the inverse-row endpoint alone therefore do not make those formulas a useful short-window certificate.
The unrestricted G0001 contract remains unresolved.

Further progress would require actual improvements to a specified ingredient: the exact projected-Gramian endpoint test instead of the literal L_obs, sharper phase/flux information, earlier exact energy, or a product/arithmetic mechanism that meets the same finite costs.
Repeating the same literal recursion or suppressing its constants is not a new estimate.
No claim is made here about one of those different ingredients or about execution of a search.
