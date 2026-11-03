---
author: Yin
---
# Trace-congruent unbuffered shears with their exact Haar infimum and original costs

Date: 2026-10-20T12:15.
Human author Yin.
Root supplied the complete new trace-congruence construction and all formulas below.
The arithmetic input C191v2 was developed by root and entropy_attainment_bridge and retains its separate whole-review requirement.
That input does not supply this new construction, approximation or cost calculation.
A reviewer who contributed only to that accepted upstream result must disclose that relationship and reuse its actual independent finding rather than independently reviewing their own upstream proof.
No new mathematical program, numerical integration, chosen numerical cutoff or parameter scan was executed.

<a id="statement"></a>
## Exact theorem statement

Let P be a monic irreducible reciprocal nontorsion integer-unit polynomial of degree d=2r and constant1, with alpha a root and totally real actual trace field F=Q(alpha+alpha^(-1)).
Put K=Q(alpha), x=z+z^(-1), and let Theta in Z[X] be the actual monic degree-r trace polynomial, so P(z)=z^r Theta(x).
Use the actual centered rational Laurent functions

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    E=-z^(-3d)H23/72, F0=-z^(-5d)H25/800,
    G=-z^(-15d/2)H35/30375,
    L=972000, J_G=integral log G^2 dmu.            (1)

Here mu is normalized Haar probability and F0 denotes a function, not the number field.
Write E0,F00,G0 for their rational polynomial expressions in x.
Fix s in{1,-1} and consider ALL pairs S,V in Q[x] with

    Theta divides S-s and Theta divides V.

Define

    B_(S,V)=(E+S(x)G)^2+(F0+V(x)G)^2+G^2.         (2)

Then every such symbol has the exact same original value

    B_(S,V)(alpha)=Q_s=(e+s g)^2+f^2+g^2,
    Norm_K(B_(S,V)(alpha))=Norm_F(Q_s)^2>=2^d,     (3)

where e,f,g are the actual integral trace defects from C191v2.
The exact full-class infimum is

    inf_(S,V in the stated rational class)
           integral log B_(S,V) dmu=J_G.          (4)

No individual polynomial pair, even in the analogous real congruence class, attains this infimum.
The explicit rational pairs in(5) below achieve every fixed positive error above J_G with a finite integer N.
Their exact ordinary numerator degree is(64N+94)d, with supplied scalar denominator, endpoint coefficient, full original resultant and radial fee in(8)--(11).
Their finite error bound(12) and sufficient integer choice(13) retain the full degree16d of P H35, all coefficient factors and its nonmonic scalar7.

For any fixed P with J_G<log2, every strict saving0<eta<log2-J_G is obtained by a finite pair with Haar mean at most log2-eta.
This is a fixed-input statement, not a degree-uniform transfer bound.
The normalized coefficient and Fourier lower bounds(14)--(15) show why the changed arithmetic gate does not remove the existing growing-cost obstacle along a hypothetical near-one input sequence.

<a id="argument"></a>
## Complete proof

### 1. Actual original-value congruence and arithmetic gate

The exact trace interface in [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) gives E(alpha)=e, F0(alpha)=f, G(alpha)=g and Theta(alpha+alpha^(-1))=0, with all original field degrees intact.
A rational polynomial divisible by Theta vanishes at every conjugate of that same original trace point.
Thus the displayed congruences give S(delta)=s and V(delta)=0 in F, proving the equality in(3).
The [actual all-prime trace theorem C191v2](Yin_C_G0191_v2.md#statement) gives its lower norm bound without any extra ramification hypothesis.
Only these original values need be integral; the coefficients of S,V and their values at unrelated real points need not be integers.

The abstract unit residuals of C192 do not contradict this conclusion: they do not supply the actual three self-composition quotients required by C191v2.
Conversely, the present proof does not assert coefficient1 works for arbitrary rational shears without the stated trace congruences.
Those congruences are the additional arithmetic restriction that permits the changed protected coefficient.

Since B>=G^2 and G is a nonzero Laurent polynomial, every log B is integrable and is at least log G^2 almost everywhere.
This proves the lower bound in(4).
If equality held, the nonnegative difference of the two logarithms would vanish almost everywhere.
Continuity then forces E0+SG0 and F00+VG0 to be zero polynomials.
Already the first equality is impossible: deg(E0)=3d, deg(G0)=15d/2 and E0 is nonzero, so multiplication of nonzero G0 by a polynomial cannot equal-E0.
This also excludes S=0 and all real-coefficient pairs.

### 2. A finite rational construction preserving all original values

Put

    H=Theta(x)G(z)=-z^(-8d)P(z)H35(z)/30375,
    H1=||P H35||_1/30375, c=1+H1^2,
    q(x)=1-Theta(x)^2 G0(x)^2/c.

On the circle0<q<=1, since H^2<=H1^2<c.
For N>=0 let Z_N=sum_(k=0)^N q^k, and set

    S_N=s-(E0+sG0)Theta^2 G0 Z_N/c,
    V_N=-F00 Theta^2 G0 Z_N/c.                    (5)

These are rational polynomials, and S_N-s and V_N are divisible even by Theta^2.
The finite geometric identity gives EXACTLY

    E+S_N G=(E+sG)q^(N+1),
    F0+V_N G=F0 q^(N+1),
    B_N=[(E+sG)^2+F0^2]q^(2N+2)+G^2.             (6)

At every original conjugate q=1, so B_N(alpha)=Q_s for every N.
Off the finite circle zero set of H, q^(2N+2) tends to0 and B_N tends to G^2.
The logarithms lie between the integrable log G^2 and log([(E+sG)^2+F0^2]+G^2), independently of N.
Dominated convergence therefore proves integral log B_N -> J_G.
Combined with the first section, this proves the exact infimum and its nonattainment.
No convergence at an original circle root of P is required, since that finite set has Haar measure zero; its original value is preserved, not discarded from the arithmetic mean.

### 3. Exact ordinary numerator, denominator, endpoints and original return

Write c=a_c/b_c in lowest terms with positive integers a_c,b_c, and put

    D_c=30375^2 a_c,
    Q_c(z)=D_c z^(16d)-b_c P(z)^2 H35(z)^2,
    U_s(z)=[13500 z^(9d/2)H23+32s H35]^2
                         +1215^2 z^(5d)H25^2,
    W_N=(32N+47)d,
    D_N=L^2 D_c^(2N+2).                           (7)

All exponents are integers since d is even.
The exact polynomial identity corresponding to(6) is

    A_N=U_s Q_c^(2N+2)
          +1024 H35^2 D_c^(2N+2) z^(32d(N+1)),
    B_N=z^(-W_N) A_N/D_N.                        (8)

Here A_N is an integer reciprocal polynomial of exact degree2W_N=(64N+94)d, with leading and constant coefficient

    50176(49b_c)^(2N+2)>0.                       (9)

Indeed Theta(x)=z^(-r)P(z), so H^2=z^(-16d)P^2H35^2/30375^2 and q=Q_c/(D_c z^(16d)).
The common factor L^2 clears both squares in U_s and G^2 with L/72=13500, L/800=1215 and L/30375=32.
The exact degree of Q_c is32d and both endpoints are-49b_c.
The exact degree of U_s is30d and both endpoints are(32s*7)^2=50176.
Only the G part of its first square reaches those endpoints; s is nonzero and the F0 square has smaller trace degree.
The first summand of A_N has degree(64N+94)d and nonzero constant, while the second has degree(32N+62)d and positive monomial shift32d(N+1).
It cannot cancel either endpoint of the first summand.
Both summands are centered at W_N, proving reciprocity and the exact width.
D_N is the supplied denominator; no minimal-denominator claim is made.

Since Norm_K(alpha)=1 and every original value is Q_s, the full equalities are

    Norm_K(B_N(alpha))=Res(P,A_N)/D_N^d
       =Norm_F(Q_s)^2>=2^d,
    I_N=integral log B_N dmu=m(A_N)-log D_N.        (10)

In the full residual case of C191v2 the first lower bound is2^(12d/11).
For M_N=sup_circle B_N, the maximum principle applied to the degree2W_N ordinary polynomial gives

    log2<=log Norm_K(B_N(alpha))/d
       <=log M_N+(64N+94)m(P).                   (11)

The original unit relation sum_i abs(log|alpha_i|)=2m(P) pays this full radial coefficient.
No Haar mean is substituted for the supremum, and no factor D_N^d or original quadratic norm multiplicity is removed.

For an explicit upper coefficient account set

    A_s0=(||H23||_1/72+||H35||_1/30375)^2
                             +(||H25||_1/800)^2,
    G1=||H35||_1/30375, F_N=A_N/(2D_N).

Laurent coefficient convolution gives

    term_count(F_N)<=2W_N+1,
    ||F_N||_1<=(A_s0/2)(1+H1^2/c)^(2N+2)+G1^2/2.

These are actual input-dependent upper budgets, not necessary growth rates of this chosen sequence or uniform hypotheses of a transfer theorem.

### 4. Fully paid finite error, including every zero of P H35

Let R1=||P||_1, A=A_s0 R1^2 and D=16d, the exact ordinary degree of the nonmonic integer polynomial P H35, whose leading coefficient is7.
On the circle H^2=|P|^2 G^2<=R1^2 G^2.
Consequently, away from its finite zero set,

    log(B_N/G^2)
       <=log(1+A(1-H^2/c)^(2N+2)/H^2).

For rho>0 put C(rho)=1+log_+(A/rho^2)/log2 and epsilon_N=I_N-J_G.
Then

    0<epsilon_N
      <=2C(rho) E_(30375rho)(P H35)
             +(A/rho^2)exp(-2(N+1)rho^2/c)
      <=D C(rho)(30375rho/7)^(1/D)
             +(A/rho^2)exp(-2(N+1)rho^2/c).        (12)

Here E_delta(Hpoly)=(1/2)integral log(1+delta^2/|Hpoly|^2) dmu.
To verify the first bound, split into H^2<rho^2 and its complement.
On the complement use(1-H^2/c)^(2N+2)<=exp(-2(N+1)H^2/c) and log(1+y)<=y.
On the small set drop that power and use

    log(1+A/H^2)<=log_+(A/rho^2)+log(1+rho^2/H^2).

Its measure is at most the integral of the latter logarithm divided by log2.
Enlarging the nonnegative integrals to the full circle gives the claimed expression, since |H|=|P H35|/30375.
The accepted all-root product estimate in [C379](Yin_C_G0379_v1.md#zero-compatible-root-error) gives

    E_delta(P H35)<=D asinh((delta/M(P H35))^(1/D)/2).

Its complete multiplicities and leading scalar are allowed.
Use M(P H35)>=7 and asinh y<=y to obtain the second bound.
There is no squarefree assumption and no omission of the additional original P zeros.

A sufficient finite integer N for any0<epsilon<=1 is explicit.
Put

    C_A=1+log_+(A(30375/7)^2)/log2,
    k=ceil(max{4,2log_2(2D(C_A+2D)/epsilon)}),
    rho=(7/30375)2^(-kD),
    N=ceil[(c/(2rho^2))log_+(2A/(epsilon rho^2))].  (13)

One has C(rho)<=C_A+2kD<=k(C_A+2D), and k<=2^(k/2) for integers k>=4.
The first term of(12) is therefore at most epsilon/2.
The choice of N makes its second term at most epsilon/2, including the branch in which log_+ vanishes.
Thus epsilon_N<=epsilon.
For J_G<log2 and0<eta<log2-J_G, choose epsilon<=1 strictly below log2-eta-J_G and then use(13).
The resulting finite pair has I_N<log2-eta.
This supplies a constructive sufficient bound, not an optimal or input-uniform value of N.

### 5. The surviving coefficient and Fourier price

The original energy inequality in [C189v4](Yin_C_G0189_v4.md#argument) concerns the same G^2 and original P.
That version's opposite sign convention for G leaves this squared energy unchanged.
Its exact bound is

    E_G=integral G^2 dmu
       >=(169/30375)^2 ||P||_2^10.

It is a statement about G alone; the original coefficient proof does not require the changed shear family to equal its earlier protected2G^2 family.
For any symbol(2), any ordinary monomial shift and normalization B/2, the absolute sum of ordinary coefficients is at least the absolute constant coefficient of its centered Laurent expression.
That constant is its mean and is positive, since B>=G^2.
Thus

    ||z^M B/2||_1>=E_G/2
       >=(169/30375)^2 ||P||_2^10/2.              (14)

For I=integral log B and W_*=sum_(k!=0)|hat(log B)(k)|, with all signed frequencies included, the corresponding Fourier bound is

    W_*>=log(integral B)-I>=log E_G-I.
    I<=log2-eta, eta>=0 implies
    W_*>=log E_G-log2+eta.                        (15)

Here is the complete analytic interface.
The nonzero nonnegative Laurent B has only finitely many circle zeros, and log B is integrable and continuous off them because B>=G^2.
If W_* is infinite, the asserted finite right sides are immediate.
Otherwise its full Fourier series is absolutely summable and represents a continuous function with the same coefficients.
The difference from log B is integrable, locally continuous off that finite set and has zero Fourier coefficients.
The exact Fejer mechanism accepted in [C177](Yin_C_G0177_v1.md#argument) applies: every Fejer convolution is zero; near a continuity point the local error tends to0, while outside an arc of radius delta the kernel is at most1/[m sin(delta/2)^2] times the finite L1 bound.
The difference is consequently zero off the finite zero set.
Hence log B<=I+W_* almost everywhere; exponentiating and integrating proves(15).
This is the same specific local-continuity argument, not an undeclared general L1 convergence theorem.

The accepted fixed-support input retained in C189v4 implies ||P||_2 tends to infinity along any permitted hypothetical sequence with positive m(P) tending to0.
Equations(14)--(15) therefore rule out uniform normalized coefficient or Wiener bounds for these finite-saving choices along such a sequence.
They do not bound the full product of a growing Fourier cost and a shrinking original-root discrepancy.
The revised arithmetic constraint improves the attainable Haar infimum by log2 relative to the formerly unrestricted protected2G^2 family, while this separate complete transfer question remains open.

<a id="inputs-and-limits"></a>
## Inputs and boundaries

| Input | Exact scope used |
| --- | --- |
| [C191v2](Yin_C_G0191_v2.md#statement) | Complete actual original-trace unbuffered norm floor, including its all-prime proof and exact quadratic original tower; its actual whole R468 finding and adoption retain their fixed scope, while the initial review context is currently unknown. |
| [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original trace polynomial, real centered functions, nonzero integral quotient values and exact phases. |
| [C176](Yin_C_G0176_v1.md#statement) | Existing protected2G^2 class and original Laurent conventions, as comparison only; its unrestricted rational-shear norm statement is not applied to coefficient1. |
| [C379](Yin_C_G0379_v1.md#zero-compatible-root-error) | Complete nonmonic all-root logarithmic regularization bound, now applied to the full degree16d polynomial P H35. |
| [C189v4](Yin_C_G0189_v4.md#argument) | Its checked energy inequality for G and retained fixed-support consequence, not a direct assertion that its old B-family contains the new class. |
| [C177](Yin_C_G0177_v1.md#argument) | Exact integrable-difference, local-continuity and Fejer-tail uniqueness mechanism with all its hypotheses supplied here. |
| Elementary polynomial identities and inequalities | Trace congruence, finite geometric sum, complete degree and coefficient convolution, dominated convergence and the displayed positive scalar bounds. |

The full original value is independent of N even when an original root lies on the circle.
Its finite set of pointwise constraints has Haar measure zero but is retained in every arithmetic norm and original-root comparison.
This distinction is precisely why a small Haar mean alone does not complete the moving-symbol transfer.
The input-dependent denominator, width, regularization exponent and coefficient/Fourier bounds are retained without a uniformity assertion.
No numerical cutoff, new certified integral or original near-one sequence is asserted to exist.

## Current assessment
[Selected decision](#decision-current-complete-root-error-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T12:15 |
| status | open |
| reason | Register the complete actual trace-congruence construction, improved unbuffered Haar infimum, fixed original value and every degree/scalar/error cost. Whole review and adoption of the upstream all-prime C191v2 are separate prerequisites; the uniform transfer remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Trace-congruent family and all costs](#statement) | Every actual original input, both signs, full rational congruence class, exact infimum, finite construction and original costs. |
| argument | [Complete five-section proof](#argument) | Original arithmetic, finite geometric shears, exact endpoints and norms, complete zero-compatible error and surviving price. |
| dependency | [Actual all-prime unbuffered gate](Yin_C_G0191_v2.md#statement) | Same original polynomial and actual three quotient values; no substitution of abstract unit residuals. |
| dependency | [Exact original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original degrees, phases, polynomial conventions and nonzero integrality. |
| dependency | [Complete regularization estimate](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Nonmonic degree16d full polynomial P H35, all repeated and original circle roots retained. |
| dependency | [Energy and fixed-support inputs](Yin_C_G0189_v4.md#argument) | Its exact energy lower bound for the original G and accepted hypothetical near-one support escape, with the modified coefficient explicitly paid. |
| dependency | [Exact Fejer interface](Yin_C_G0177_v1.md#argument) | Integrable difference, local continuity and explicit tail bound in the supplied new analytic argument. |
| support | [Protected2G^2 comparison](Yin_C_G0176_v1.md#statement) | Earlier exact infimum and costs only; no expansion of that theorem to the new protected coefficient. |
| support | [Exact input and review limits](#inputs-and-limits) | Sole new author, upstream contributor relationships, no computation and no uniform original transfer conclusion. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T12:26 |
| status | proved |
| authority | Internal adoption within Yin's selected mixed-form and actual original-transfer inquiries. |
| reason | Adopt the complete trace-congruent coefficient1 family through whole R469, after actual adoption of its C191v2 arithmetic input through whole R468. The construction preserves every original value, improves the Haar infimum by log2 and supplies every finite degree/scalar/error cost. The surviving coefficient/Wiener growth and complete original-root comparison remain explicit, so no uniform transfer or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Trace-congruent family and all costs](#statement) | Every actual original input, both signs, full rational congruence class, exact infimum, finite construction and original costs. |
| argument | [Complete five-section proof](#argument) | Original arithmetic, finite geometric shears, exact endpoints and norms, complete zero-compatible error and surviving price. |
| dependency | [Actual all-prime unbuffered gate](Yin_C_G0191_v2.md#statement) | Same original polynomial and actual three quotient values; no substitution of abstract unit residuals. |
| dependency | [Exact original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original degrees, phases, polynomial conventions and nonzero integrality. |
| dependency | [Complete regularization estimate](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Nonmonic degree16d full polynomial P H35, all repeated and original circle roots retained. |
| dependency | [Energy and fixed-support inputs](Yin_C_G0189_v4.md#argument) | Its exact energy lower bound for the original G and accepted hypothetical near-one support escape, with the modified coefficient explicitly paid. |
| dependency | [Exact Fejer interface](Yin_C_G0177_v1.md#argument) | Integrable difference, local continuity and explicit tail bound in the supplied new analytic argument. |
| support | [Protected2G^2 comparison](Yin_C_G0176_v1.md#statement) | Earlier exact infimum and costs only; no expansion of that theorem to the new protected coefficient. |
| support | [Exact input and review limits](#inputs-and-limits) | Sole new author, upstream contributor relationships, no computation and no uniform original transfer conclusion. |
| review | [Whole trace-congruent finding](../audits/reviews/Yin_R_G0469_v1.md#trace-congruent-shear-whole-independent-finding) | Entire actual five-section proof, all1--15 formulas and seven inputs, exact original value, cost and sign interfaces, with upstream authorship disclosed and R468 reused at its actual independent scope. |
| support | [Whole upstream arithmetic finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Actual all-prime C191v2 and original-return gate; no self-review of that upstream input is substituted by C193's contributor reviewer. |


### Decision current-complete-root-error-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:22 |
| status | proved |
| reason | The unchanged complete all-root product and normalized scalar bound is now owned by C379, including its nonmonic, repeated-root, circle-zero and actual Mahler-scale cases. Retain the current statement, full argument, every other input and actual existing review scopes; the old reviewers are not described as having inspected this later proof-home placement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every actual original input, both signs, full rational congruence class, exact infimum, finite construction and original costs. |
| argument | [Exact argument](#argument) | Original arithmetic, finite geometric shears, exact endpoints and norms, complete zero-compatible error and surviving price. |
| dependency | [Exact dependency](Yin_C_G0191_v2.md#statement) | Same original polynomial and actual three quotient values; no substitution of abstract unit residuals. |
| dependency | [Exact dependency](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original degrees, phases, polynomial conventions and nonzero integrality. |
| dependency | [Exact dependency](Yin_C_G0379_v1.md#zero-compatible-root-error) | Nonmonic degree16d full polynomial P H35, all repeated and original circle roots retained. |
| dependency | [Exact dependency](Yin_C_G0189_v4.md#argument) | Its exact energy lower bound for the original G and accepted hypothetical near-one support escape, with the modified coefficient explicitly paid. |
| dependency | [Exact dependency](Yin_C_G0177_v1.md#argument) | Integrable difference, local continuity and explicit tail bound in the supplied new analytic argument. |
| support | [Exact support](Yin_C_G0176_v1.md#statement) | Earlier exact infimum and costs only; no expansion of that theorem to the new protected coefficient. |
| support | [Exact support](#inputs-and-limits) | Sole new author, upstream contributor relationships, no computation and no uniform original transfer conclusion. |
| review | [Exact review](../audits/reviews/Yin_R_G0469_v1.md#trace-congruent-shear-whole-independent-finding) | Entire actual five-section proof, all1--15 formulas and seven inputs, exact original value, cost and sign interfaces, with upstream authorship disclosed and R468 reused at its actual independent scope. |
| support | [Exact support](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Actual all-prime C191v2 and original-return gate; no self-review of that upstream input is substituted by C193's contributor reviewer. |

