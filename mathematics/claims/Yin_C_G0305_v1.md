---
author: Yin
---

# Repeated-sign algebraic entropy converges to Mahler measure with exact quadratic cost

This retains the complete original2026-10-07 [L108 proof](../ledger/Yin_L_G0108_v1.md).
The coordinator proposed the endpoint chain-rule/leverage mechanism; the assembling review_matrix_completion agent supplied the complete conditional-information proof and domain/monotonicity arguments.
The assess_shortness_route agent supplied the all-k scalar telescoping estimate.
The actual old checks and distinct contributor/partial scopes remain in the formal review linked by L108.
No source, computation or Task is newly executed.

## Statement

Let alpha be any nonzero algebraic integer, P its monic irreducible polynomial of degree d,and m=log M(P)>=0.
For every integer k>=1 use independent fair signs xi_(j,b),D_j^(k)=sum_(b=1)^k xi_(j,b),and
H_(N,k)=H(sum_(j=0)^(N-1)D_j^(k)alpha^j),H_(0,k)=0,Delta_(N,k)=H_(N,k)-H_(N-1,k).
All logarithms are natural.
Put

    a=exp(2m)-1,
    F(l)=l/2+l²(3-2l)^4/324,
    L_k(m)=sum_(r=1)^k F(a/(k+r a)),
    C(m)=(5a²/12)(1-(1+a)^(-2)).

The time increments decrease to h_k=lim_N H_(N,k)/N, and for every integer N,k>=1,

    Delta_(N,k)>=h_k>=L_k(m),
    0<=m-h_k<=C(m)/k²,
    h_(k+1)>=h_k, h_k tends to m as k tends to infinity.

The time increments are not asserted monotone in k.
When m=0,h_k=C(m)=L_k(m)=0,but finite increments need not vanish.
No unit,reciprocity or hyperbolicity assumption is required for these algebraic-sum assertions.

For N>d the actual endpoint-bit chain,subtracting each revealed translation,has leverage
a_N/(k+r a_N),where a_N=G_N/G_(N-1)-1>=a.
It gives the exact finite lower sum before passage to the rate.
Earlier times follow from decreasing increments,without using an inverse of a rank-deficient matrix.
The full finite-digit norm grid gives
|supp S_(N,k)|<=(4kN)^d M(P)^(N-1).
The scalar telescope compares sum J(a/(k+ra))=m with F and yields the displayed all-k constant.
It is uniform in degree for specified m,with the full m dependence:
C(m)=(20/3)m³+O(m^4) near zero,with an absolute local remainder.
This is an upper deficit bound,not asymptotic equality or existence of a small-positive-m sequence.

For a hyperbolic algebraic unit and every fixed full-order toral coding nu_R,the finite-integer iid extension gives
h_(nu_R^(star k))(T)=h_k and0<=m-h_(nu_R^(star k))(T)<=C(m)/k².
This entropy limit is proved directly,not inferred from weak convergence to Haar.
The digit law changes with k and does not identify the original binary entropy with m.
Inputs with unit-circle conjugates retain only the algebraic-sum conclusions,no homoclinic coding construction.
No positive uniform Mahler gap follows.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:27 |
| status | open |
| reason | Complete original conditional endpoint chain, both monotonicities, full integral norm grid and all-k scalar telescope retained; current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire nonzero-algebraic-integer repeated-sign every-time/rate theorem, exact degree-free C(m)/k² deficit and zero-measure case, monotonicities and fixed-full-order hyperbolic toral consequence with all changed-digit and asymptotic limits. |
| argument | [Complete argument](#argument) | Complete original1–12: both endpoint mutual-information identities, actual conditional independent-sign reveal/subtraction, repeated-column inverse/finite Gram guard and all-time passage, real/complex norm cells, both scalar inequalities/reciprocal telescope, absolute cubic expansion and finite-digit coding interface. |
| dependency | [Finite monic Gram/Jensen theorem](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy) | Exact every-N nonzero-algebraic-integer endpoint ratio G_N/G_(N-1)>=M(P)^2 for N>d, including unit-circle roots and nonunits. |
| dependency | [Generic fair-cube fourth moment](Yin_C_G0290_v1.md#fourth-posterior-moment) | Exact increasing F(l) mutual-information lower bound on each actual conditional independent fair-sign observation; no conditional independence of the aggregate endpoint sum is assumed. |
| dependency | [Finite-integer iid coding equality](Yin_C_G0303_v1.md#coding-entropy-scope-and-costs) | Only the separate fixed-full-order hyperbolic toral conclusion12 and its changed per-time integer digit law; not a premise of the broad algebraic-sum theorem1–11. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:31 |
| status | proved |
| reason | Adopt the entire original nonzero-algebraic-integer repeated-sign every-time/rate theorem, both monotonicities, exact norm grid and all-k C(m)/k² comparison after actual whole self-review; retain m=0/nonunit/unit-circle domains for1–11 and only the separate hyperbolic full-order coding scope for12, with changed digit laws and no deficit equality or uniform gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire nonzero-algebraic-integer repeated-sign every-time/rate theorem, exact degree-free C(m)/k² deficit and zero-measure case, monotonicities and fixed-full-order hyperbolic toral consequence with all changed-digit and asymptotic limits. |
| argument | [Argument](#argument) | Complete original1–12: both endpoint mutual-information identities, actual conditional independent-sign reveal/subtraction, repeated-column inverse/finite Gram guard and all-time passage, real/complex norm cells, both scalar inequalities/reciprocal telescope, absolute cubic expansion and finite-digit coding interface. |
| dependency | [Dependency](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy) | Exact every-N nonzero-algebraic-integer endpoint ratio G_N/G_(N-1)>=M(P)^2 for N>d, including unit-circle roots and nonunits. |
| dependency | [Dependency](Yin_C_G0290_v1.md#fourth-posterior-moment) | Exact increasing F(l) mutual-information lower bound on each actual conditional independent fair-sign observation; no conditional independence of the aggregate endpoint sum is assumed. |
| dependency | [Dependency](Yin_C_G0303_v1.md#coding-entropy-scope-and-costs) | Only the separate fixed-full-order hyperbolic toral conclusion12 and its changed per-time integer digit law; not a premise of the broad algebraic-sum theorem1–11. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0543_v1.md#current-repeated-sign-finding) | Exact full current statement, complete retained original argument and every selected interface, self-reviewed; old findings keep only their actual original inputs and precise relationships. |

## Complete retained argument

<a id="argument"></a>
Let alpha be any nonzero algebraic integer, with monic irreducible polynomial P of degree d and m=log M(P).
There is no unit or hyperbolicity assumption for the algebraic-sum assertions.
For k>=1 take independent fair signs xi_(j,b), and define

    D_j^(k)=sum_(b=1)^k xi_(j,b),
    S_(N,k)=sum_(j=0)^(N-1) D_j^(k) alpha^j,
    H_(N,k)=H(S_(N,k)),
    Delta_(N,k)=H_(N,k)-H_(N-1,k),  H_(0,k)=0.          (1)

All entropies and logarithms are natural.
Coordinates in the rational power basis preserve exactly the fibers of these sums.
Put

    a=exp(2m)-1,
    F(l)=l/2+l^2(3-2l)^4/324,
    L_k(m)=sum_(r=1)^k F(a/(k+r a)),
    C(m)=(5a^2/12)(1-(1+a)^(-2)).                      (2)

The claimed conclusions are

    Delta_(N,k)>=h_k>=L_k(m) for every N,k>=1,
    h_k:=lim_(N->infinity) H_(N,k)/N,
    0<=m-h_k<=C(m)/k^2,
    h_k is nondecreasing in k and h_k->m.              (3)

When m=0, a=C(m)=0 and h_k=0.
The finite increments need not vanish.
Thus this result supplies no positive Mahler gap.

<a id="convolution-digit-entropy-limits"></a>
### Exact increment identities and the two monotonicities

For fixed k write Y=S_(N,k), E_N=(xi_(N-1,1)...,xi_(N-1,k)), and let Z be the contribution from times 0,...,N-2.
Since E_N is independent of Z and its conditional contribution to Y is a deterministic translation,

    Delta_(N,k)=H(Y)-H(Y|E_N)=I(E_N;Y).                (4)

The endpoint sum D_(N-1)^(k) is a sufficient function of E_N for this observation, so (4) also equals I(D_(N-1)^(k);Y).
It does not assert that the endpoint bits are conditionally independent.

There is a second identity at the first digit:

    Delta_(N,k)=I(D_0^(k);S_(N,k)).                    (5)

Indeed, conditioning on D_0^(k) leaves alpha times an independent sum with N-1 digits.
Multiplication by alpha is injective, so its entropy is H_(N-1,k).
The added term alpha^N D_N^(k) is independent of the old sum and D_0^(k).
Data processing applied to this independent-noise channel yields Delta_(N+1,k)<=Delta_(N,k).
The increments are nonnegative by (4), hence decrease to a limit.
Their Cesaro averages are H_(N,k)/N, proving existence of h_k and Delta_(N,k)>=h_k for every N.

For the other monotonicity, couple S_(N,k+1)=S_(N,k)+S'_(N,1), with the last summand independent.
Conditioning on it gives

    H_(N,k+1)>=H(S_(N,k+1)|S'_(N,1))=H_(N,k).

After division by N and passage to the already established limits, h_(k+1)>=h_k.
This does not require that the time increments themselves be monotone in k.

<a id="endpoint-chain-rule-convolution-leverage"></a>
### Revealing the endpoint bits and subtracting their known translations

Let v_j=t^j mod P in the rational power basis, V_N=[v_0 ... v_(N-1)], W_N=V_NV_N^T and G_N=det W_N.
When N>d, W_(N-1) is invertible.
Write v=v_(N-1) and

    a_N=v^T W_(N-1)^(-1)v=G_N/G_(N-1)-1.

The finite dual-Gram/monic-Jensen argument of [C G0288](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy) gives

    a_N>=M(P)^2-1=a.                                  (6)

That exact finite argument permits unit-circle roots; no limiting Gram ratio is used here.

Apply the mutual-information chain rule to (4), revealing the endpoint signs in any fixed order.
After revealing k-r of them, subtract their known contribution to Y.
Conditioned on any values of those revealed bits, the remaining observation has precisely k independent fair-sign copies of each earlier column v_0,...,v_(N-2), and r independent fair-sign copies of v.
Its matrix W is

    k W_(N-1)+r vv^T.

All unrevealed signs retain their independent fair priors.
The conditional observation differs only by the subtracted translation, so the information of the next endpoint sign is the same for every value of the already revealed bits.
Its diagonal row-space leverage is

    l_(N,k,r)=v^T(k W_(N-1)+r vv^T)^(-1)v
             =a_N/(k+r a_N).                           (7)

The last equality is the rank-one inverse identity applied to k W_(N-1).
These matrices have full row rank; repeated columns cause no difficulty.
Each leverage lies in [0,1], as is also clear from its projection interpretation.

The generic fair-cube result of [C G0291](Yin_C_G0290_v1.md#fourth-posterior-moment) states that the mutual information of one fair sign in a full-row-rank linear observation is at least F(l), and that F is increasing on [0,1].
Moreover x/(k+r x) is increasing for x>=0.
Thus summing the k conditional-information terms in their actual chain-rule order gives the finite bound

    Delta_(N,k)>=sum_(r=1)^k F(a_N/(k+r a_N))
                 >=L_k(m),  N>d.                      (8)

No conditioning on the total endpoint sum replaces the bit-revealing chain; such a replacement would not leave independent fair signs.
Passing N to infinity in (8) gives h_k>=L_k(m).
Equation (5) then gives the same lower bound for every earlier increment, without needing to assign it a fictitious invertible W_(N-1).

<a id="finite-digit-mahler-upper"></a>
### A finite digit norm-grid upper bound

At an embedding sigma, every possible S_(N,k) has modulus at most

    R_sigma=kN max(1,|sigma(alpha)|)^(N-1),

which is at least 1.
Partition each real coordinate interval [-R_sigma,R_sigma] into half-open cells of width 1 starting at its lower endpoint.
Partition each real and imaginary coordinate of a complex place into cells of width 1/sqrt(2), also starting at the lower endpoint.
If two distinct algebraic integers occupy the same full cell, the modulus of their difference at every embedding is strictly less than 1.
Their nonzero integral field norm would then have modulus less than 1, impossible.

There are at most 2R_sigma+1<=3R_sigma real cells.
For each Cartesian coordinate of a complex place there are at most 2sqrt(2)R_sigma+1<=4R_sigma cells; the conjugate pair is counted twice.
Consequently

    |supp S_(N,k)|<=(4kN)^d M(P)^(N-1),
    H_(N,k)<=(N-1)m+d log(4kN),
    h_k<=m.                                           (9)

The last limit fixes k and the input before N tends to infinity.
The proof uses algebraic integrality, not that alpha is a unit, reciprocal or hyperbolic.
It includes the unit-circle case.

<a id="quantitative-convolution-entropy-convergence"></a>
### An all-k telescoping comparison

For 0<=l<1 put J(l)=-(1/2)log(1-l).
The positive logarithm series and (3-2l)^4<=81 imply

    0<=J(l)-F(l).

More explicitly, the series tail after l^2/4 is at most l^3/[6(1-l)], while Bernoulli's elementary inequality gives (1-2l/3)^4>=1-8l/3.
Hence

    F(l)>=l/2+l^2/4-(2/3)l^3,
    0<=J(l)-F(l)<=l^3(5-4l)/[6(1-l)]
                         <=(5/6)l^3/(1-l).            (10)

For a>0 set l_r=a/(k+r a).
The logarithmic terms telescope exactly:

    sum_(r=1)^k J(l_r)
      =(1/2)log[(k+k a)/k]=(1/2)log(1+a)=m.

Writing x=k+r a, direct subtraction of reciprocal squares gives

    l_r^3/(1-l_r)=a^3/[x^2(x-a)]
      <=(a^2/2)[(x-a)^(-2)-x^(-2)].

For example the ratio of the left side to the right side is 2(x-a)/(2x-a)<=1.
Sum over r and use (10) to obtain

    0<=m-L_k(m)
      <=(5a^2/12)[k^(-2)-(k+k a)^(-2)]
      =C(m)/k^2.                                      (11)

When a=0 the same assertion holds directly without dividing by a.
Combining (8), (9) and (11) proves (3), including h_k increasing to m.
The bound is uniform in the degree for each specified m, with its full m dependence displayed.
It bounds the actual entropy deficit from above; it does not assert equality of that deficit with the comparison error m-L_k(m).

For comparison with the original binary estimate in L G0097, a=2m+O(m^2) and 1-(1+a)^(-2)=1-exp(-4m)=4m+O(m^2), so

    C(m)=(20/3)m^3+O(m^4) as m decreases to zero.

The O-constant is absolute on a fixed sufficiently small neighborhood of zero.
Thus the established near-zero cubic upper cost becomes [(20/3)m^3+O(m^4)]/k^2.
This is an upper bound, not an asymptotic equality for the actual deficit m-h_k, and does not assume a sequence of positive Mahler measures tending to zero exists.

<a id="convolution-coding-entropy-scope"></a>
### Consequence for the actual toral measures

If alpha is a hyperbolic algebraic unit, fix any full order R containing Z[alpha] and use the actual coding measure nu_R of L G0104.
The k-fold convolution of that measure is the coding of the fixed integer digit law D_j^(k), because addition of k independent absolutely convergent coding series is allowed.
The finite-digit extension of [C G0304](Yin_C_G0303_v1.md#coding-entropy-scope-and-costs) therefore gives

    h_(nu_R^(star k))(T)=h_k,
    0<=m-h_(nu_R^(star k))(T)<=C(m)/k^2.                (12)

Thus these specific convolution entropies converge to m by a direct finite-information and arithmetic proof.
Weak convergence to Haar or decay of each nontrivial Fourier coefficient is not used to justify an entropy limit.
The measures and their digit laws change with k; (12) does not replace the entropy of the original fair-binary law by m.
For inputs with unit-circle conjugates only the algebraic-sum conclusions (1)--(11) are asserted, not a homoclinic torus construction.
