---
author: Yin
---
# Uniform moment certificates, restriction-stable signs and explicit finite obstruction hosts

Human author Yin.
This version strengthens the four-pair torus theorem within the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The rank_two_route contributor developed the lower-rank arguments and exact certificates.
Root proposed the Fourier-derivative refinement, order128 cutoff and saturated sign-average locality improvement, and checked the paired-slope calculation as a fellow contributor.
These are proof contributions, not independent review.

## Revision scope and inputs

On 2026-11-04, this version retains all nine conclusions of [v2](Yin_C_G0863_v2.md#statement) and adds the restriction-stable unit-relation factorization, an infinite paired-slope rank-two family, a stronger uniform higher-dimensional moment certificate and explicit finite candidate hosts.
The exact inherited dependency is the [selected v2 decision](Yin_C_G0863_v2.md#decision-whole-independent-review-2026-11-04), supported by [R1081](../audits/reviews/Yin_R_G1081_v1.md#whole-version-and-finite-computation), including its inherited v1 source/native evidence and review limits.
That review does not inspect the new arguments or computation in this version.
The new moment proof of the higher-dimensional bound does not use v2 Part7's higher-dimensional conclusion; its necessary Haar, integrability and Jensen interfaces remain those accepted in v1.
The selected assessment and this version's separate independent review are recorded in its decision below.

| Input | Adopted scope |
| --- | --- |
| [C863 v2](Yin_C_G0863_v2.md#decision-whole-independent-review-2026-11-04) | All nine unchanged conclusions and exact inherited proofs, including v1, native certificates and existing source-inspection limits; the new proof below separately strengthens its higher-dimensional bound. |
| [C863 v1](Yin_C_G0863_v1.md#statement) and [Den09 U001](../audits/literature/Den09/Yin_U001.md#mahler-measure) | Actual normalized Haar, nonzero Laurent logarithmic integrability, one-variable Jensen, monomial invariance and source-proof inspection boundaries used in the new arguments. |
| [Exact program](../computations/programs/Yin_J_G0134/rank-two-locality.py) | Order128 free and sign-averaged moment calculation, complete bounded canonical scope, exact comparisons, direct small controls and reproduction. |
| [Selected native certificate](../computations/programs/Yin_J_G0134/inputs/rank-two-moment-certificate.json) | Exact free fraction at threshold59/20 and all275 admissible primitive canonical rank-three relation fractions at threshold14/5. |

The reuse comparison with the existing four-pair product analysis, graph1111 special case and selected C92/C144/C848 scopes found no already retained statement of the full new lower-rank families or effective moment reduction.
The arguments are direct algebra, calculus and finite coefficient calculations using the identified interfaces.
No new external theorem, original-source proof inspection, exhaustive search or priority claim is made.
No rolling Draft or ignored computation output is a proof premise.

## Statement

Let K be the same compact space of connected subtori H of T^4 as in v2: the four restricted coordinate characters chi_j are nontrivial and distinct up to inversion.
Their saturated annihilator is L(H)={a in Z^4:product_j chi_j^(a_j)=1}; admissibility excludes e_j and e_i+/-e_j from this lattice.
Put

    F_epsilon=sum_(j=1..4)epsilon_j(chi_j-chi_j^(-1)),
    G_epsilon=F_epsilon/i,
    m_H(F_epsilon)=integral_H log|F_epsilon|,
    g(H)=min_epsilon m_H(F_epsilon),
    P_N(u)=sum_(j=1..N)(1-u^2/64)^j/j,
    Sbar_N(H)=(1/16)sum_epsilon integral_H P_N(G_epsilon),
    B_R={a in Z^4:||a||_1<=R},
    eta_*=23/2025.

All integrals use normalized Haar measure and natural logarithms.
Every F_epsilon is nonzero and logarithmically integrable.
A full-rank integer parametrization pushes Haar measure onto Haar measure on its image even when it has a finite kernel.
The conclusions are as follows.

1. All nine conclusions of the exact [v2 statement](Yin_C_G0863_v2.md#statement) remain valid with their original constants, quantifiers and limits.
2. If L(H) contains a vector delta in {+1,-1}^4, then m_H(F_delta)=0.
   This holds in every rank and on every admissible connected restriction preserving that relation.
3. For arbitrary nonzero integers p,q, the rank-two configuration (1,p),(1,-p),(2,q),(2,-q) satisfies m_H(F_++++)<=log2-1/8.
   Permutations, coordinate inversions and full-rank reparametrizations retain a corresponding favorable sign.
   This is a Haar-template bound, without the same asserted bound for every rank-one restriction.
   When |p|!=|q| it has neither a common-phase circle nor a unit-coefficient relation; for p=1 and odd q>=3, all four deletion indices are one.
4. Every admissible H of dimension at least three satisfies Sbar_128(H)>14/5 and therefore g(H)<17/25<log2-eta_*.
   More generally the same conclusion holds in every rank whenever span_Q(L(H) intersect B_128) has dimension at most one.
   The order128 average depends only on the indicated short intersection, with no logarithmic approximation error.
5. Form the finite list of distinct admissible rank-two tori whose annihilator is span_Q(u,v) intersect Z^4 for independent u,v in B_128, and optionally discard tori whose exact Sbar_128 is greater than14/5.
   Every rank-two H outside the retained list satisfies g(H)<17/25<log2-eta_*.
   Similarly form a finite rank-one list from independent triples u,v,w in B_128, optionally discarding passing certificates.
   Every rank-one H outside the union of the retained rank-two host families and this rank-one list satisfies the same bound.
   Each circle in the triple list has a primitive integer frequency representative whose four absolute values are at most128^3=2097152.

The new finite lists are explicit candidate lists, not lists of verified counterexamples or tori known to have large g.
They may contain tori whose good-sign inequality is already true, and a candidate circle may also lie in a candidate rank-two host.
This distinction leaves intact v2's separate qualitative existence statement whose hosts were selected by an actual bad-threshold condition.
Neither explicit candidate enumeration has been executed here.
The finite rank-two remainder, the circles inside retained hosts and arbitrary original-input integral-auxiliary supply remain unresolved.

<a id="inherited-arguments"></a>
## Exact inherited argument scope

Part1 invokes all nine conclusions under the exact [v2 adopted decision](Yin_C_G0863_v2.md#decision-whole-independent-review-2026-11-04), without changing any of that version's hypotheses or proof inputs.
Its [inherited arguments](Yin_C_G0863_v2.md#inherited-arguments), [forty-two-case certificate](Yin_C_G0863_v2.md#finite-rank-three-certificate) and subsequent rank/finite-host assembly remain at their responsible fixed homes.
Their old reviews and actual native/source limits retain exactly that scope.
The following complete new arguments prove Parts2--5 and their stated comparisons.

<a id="complete-new-argument"></a>
<a id="unit-relation-factorization"></a>
## One unit-coefficient relation gives a zero-measure sign in every rank

Suppose that L(H) contains a vector delta in {+1,-1}^4.
This hypothesis requires one unit-coefficient relation, rather than a vector delta annihilated by every relation as in the separate common-phase criterion.
Set w_j=chi_j^(delta_j), so w_1 w_2 w_3 w_4=1.
Writing a=w_1, b=w_2, c=w_3 gives the exact Laurent identity

    sum_(j=1..4)(w_j-w_j^(-1))
      =-(ab-1)(ac-1)(bc-1)/(abc).                       (UR1)

Expansion proves (UR1) directly.
The left side is F_delta for the original characters.
Each of ab, ac and bc is nontrivial, since a trivial product would identify two original characters up to inversion.
A nontrivial character on a connected torus pushes Haar measure to Haar measure on T, and the circle Jensen integral of log|z-1| is zero.
Each factor on the right therefore has logarithmic mean zero, while the denominator has absolute value one.
The finite sum of those integrable logarithms proves

    m_H(F_delta)=0.                                     (UR2)

This conclusion applies to every admissible connected subtorus satisfying the one relation, including rank-one specializations.
It is stronger in that restriction sense than merely applying a mean bound on the ambient rank-three host.
For example the rank-two vectors (1,0),(0,1),(2,4),(-3,-5) sum to zero, so (UR2) applies.
They have no common-phase circle: a functional taking values +/-1 on the first two vectors takes one of +/-6 or +/-2 on the third.
Thus (UR2) is not subsumed by C863's common-phase hypothesis.

<a id="paired-slope-family"></a>
## An infinite rank-two family with uniform margin 1/8

For arbitrary nonzero integers p and q, consider

    v_1=(1,p), v_2=(1,-p),
    v_3=(2,q), v_4=(2,-q).                              (PS1)

These four vectors have rank two and are nonzero and distinct up to inversion.
Choose all four signs positive.
On the parametrizing two-torus their antisymmetric sum has the exact factorization

    F=2i[sin(x+py)+sin(x-py)+sin(2x+qy)+sin(2x-qy)]
     =4i sin x [cos(py)+2cos x cos(qy)].                 (PS2)

Both factors are nonzero trigonometric Laurent polynomials and have integrable logarithms.
Since the x-mean of log|4sin x| is log2, (PS2) yields

    m(F)=log2+integral_(T^2) log|A(y)+2B(y)cos x|,
    A(y)=cos(py), B(y)=cos(qy).                         (PS3)

For fixed real A,B, with (A,B)!=(0,0), multiplying A+B(z+z^(-1)) by z gives Bz^2+Az+B.
When B!=0 and |A|<=2|B| its two roots have modulus one, including the repeated-root boundary.
Its circle logarithmic mean is log|B|.
When |A|>2|B| its roots have reciprocal moduli, and Jensen gives the mean log[(|A|+sqrt(A^2-4B^2))/2].
For B=0 and A!=0 the second formula reduces to log|A|, the actual constant-section value.
Thus, with the value minus infinity when A=B=0, the x-mean equals log R(y), where

    R=|B|                              if |A|<=2|B|,
      (|A|+sqrt(A^2-4B^2))/2           if |A|>2|B|.     (PS4)

The simultaneous-zero sections form a finite set because p and q are nonzero.
The nonzero two-variable Laurent polynomial in (PS3) has an integrable logarithm, so Fubini identifies its integral with the integral of (PS4); the exceptional sections do not change that integral.
In both cases

    R<=max(|A|,|B|)<=1.                                 (PS5)

Put V=max(cos^2(py),cos^2(qy)).
For V>0, log R<=log V/2<=-(1-V)/2, and the same extended-real upper bound is valid at V=0.
Moreover

    1-V=min(sin^2(py),sin^2(qy))
        >=sin^2(py)sin^2(qy).                           (PS6)

Orthogonality gives

    integral_T sin^2(py)sin^2(qy)
      =1/4  if |p|!=|q|,
      =3/8  if |p|=|q|.                                (PS7)

For unequal absolute frequencies, expand each square as (1-cos(2py))/2 and use the vanishing of the nonconstant mixed Fourier terms.
For equal absolute frequencies, the integral is the elementary fourth sine moment 3/8.
Equations (PS3)--(PS7) prove

    m_H(F_++++)<=log2-1/8                               (PS8)

uniformly in every nonzero p,q, with the stronger intermediate margin 3/16 when |p|=|q|.
The bound also holds after any coordinate permutation/inversion or full-rank torus reparametrization of this configuration, with the corresponding favorable sign.
It is a rank-two Haar assertion, without a claimed uniform bound for every rank-one restriction of (PS1).

### Why this family exceeds the earlier sufficient cases

When |p|!=|q|, (PS1) has no common-phase circle.
Indeed a functional with values delta_j in {+1,-1} would satisfy 2a=delta_1+delta_2 and 4a=delta_3+delta_4, forcing a=0 and opposite signs within each pair.
The remaining equations require pb=+/-1 and qb=+/-1, which force |p|=|q|.
The same first-coordinate calculation shows that a unit-coefficient relation must have opposite signs within each pair, and its second coordinate again forces |p|=|q|.
Thus the unequal-frequency part is outside both (UR1) and the common-phase test.

For the infinite subfamily p=1 and odd q>=3, all four deletion indices are one.
After deleting column3 or column4, the remaining first two columns give (0,2), while subtracting twice column1 from the remaining third-or-fourth column gives a vertical vector with odd second coordinate.
Their integer combinations give (0,1), and then column1 gives (1,0).
After deleting column1, subtract twice column2 from columns3 and4 to obtain (0,q+2) and (0,2-q).
The gcd of q+2 and q-2 is one for odd q, so again (0,1) and then (1,0) are generated.
Reflection in the second coordinate gives the same conclusion after deleting column2.
Thus every remaining three-column lattice is Z^2, so X_j=X=Z^2 for every j.
There is no coloop, since deletion of any column leaves rank two.
These facts show that the large-deletion-index criterion does not already cover this infinite subfamily.
They are not a classification of every possible overlap with older individual templates.

<a id="finite-moment-locality"></a>
## Sign-averaged finite logarithm certificates and short relations

Put G_epsilon=F_epsilon/i, so G_epsilon is real and |G_epsilon|<=8, and set X_epsilon=G_epsilon^2/64.
For an integer N>=1 define

    P_N(u)=sum_(j=1..N)(1-u^2/64)^j/j,
    S_N(H,epsilon)=integral_H P_N(G_epsilon),
    Sbar_N(H)=(1/16)sum_epsilon S_N(H,epsilon).          (ML1)

The finite logarithm series gives

    m_H(F_epsilon)<=1/2[log64-S_N(H,epsilon)].           (ML2)

Every quantity S_N is nonnegative and rational, since it is the integral of a Laurent polynomial with rational coefficients.
For each fixed H and sign, monotone convergence and logarithmic integrability give S_N increasing to log64-2m_H(F_epsilon).
Only the finite inequality (ML2) is needed below.

Before sign averaging, S_N(H,epsilon) depends only on L(H) intersect B_(2N), where B_R={a in Z^4:||a||_1<=R}.
Indeed integration keeps exactly the Laurent coefficients at those supported exponents lying in L(H).
Sign averaging improves the radius by a factor of two.
Changing epsilon_j translates the ambient theta_j by pi, so averaging over all signs kills every Fourier coefficient having an odd coordinate.
The retained exponents are 2a with ||a||_1<=N.
Saturation gives 2a in L(H) if and only if a in L(H), so

    Sbar_N(H) depends only on L(H) intersect B_N.        (ML3)

This is exact finite coefficient equality, without a limiting or approximation error.
It is not a bound on deletion indices or on a chosen character parametrization.

A certificate Sbar_N(H)>14/5 implies that some sign has S_N(H,epsilon)>14/5.
The existing elementary logarithm estimates 56/81<log2<1123/1620<52/75 give log64<104/25.
Consequently (ML2) yields

    g(H)<17/25<log2-23/2025.                            (ML4)

The result below supplies this same order128 certificate for every admissible torus of dimension at least three.

<a id="fourier-derivative-bound"></a>
## A Fourier bound for the finite logarithm polynomial

For real |u|<=8 and u!=0, summing the derivative of the finite geometric series gives

    P_N'(u)=-2[1-(1-u^2/64)^N]/u.                       (FD1)

Its value at u=0 is zero by polynomial continuity.
The inequality 1-(1-t)^N<=min(Nt,1) for 0<=t<=1 implies

    |P_N'(u)|<=min(N|u|/32,2/|u|)<=sqrt(N)/4.           (FD2)

The function |P_N'(u)| on 0<=u<=8 has a single maximum, allowing an endpoint maximum.
Here is a direct check covering every N.
For N=1 it is u/32 and is increasing.
For N>=2, put t=u^2/64 and q=1-t.
Apart from a positive factor, the derivative of [1-(1-t)^N]/sqrt(t) has the sign of

    K(q)-1,
    K(q)=q^(N-1)[2N-(2N-1)q],
    K'(q)=N q^(N-2)[2(N-1)-(2N-1)q].                  (FD3)

On [0,1], K increases from zero to a unique maximum greater than1, then decreases to K(1)=1.
Thus K(q)=1 has exactly one solution in (0,1), and (FD3), with q decreasing as u increases, gives the asserted increase followed by decrease.
Together with the oddness of P_N', its value zero at the origin and (FD2), this bounds its total variation by

    integral_(-8)^8 |P_N''(u)|du<=sqrt(N).              (FD4)

This also holds for N=1 directly.
All endpoint derivatives are polynomial derivatives; no singular division at u=0 is used.

On T^4 put G=2sum_(j=1..4)sin(theta_j) and Q_N(theta)=P_N(G).
Fix all angles except theta_i and write G=A+2sin(theta_i), with |A|<=6.
The chain rule and |G'|<=2 give

    E_(theta_i) |P_N''(G)(G')^2|
      =(1/pi)integral_(A-2)^(A+2)
           |P_N''(u)|sqrt(4-(u-A)^2)du
      <=2sqrt(N)/pi.                                  (FD5)

The equality splits the circle into the two monotone passages through the interval [A-2,A+2].
The other chain-rule term is bounded by

    E_(theta_i)|P_N'(G)G''|
      <=(sqrt(N)/4) E_(theta_i)(2|sin(theta_i)|)
      =sqrt(N)/pi.                                    (FD6)

Hence the full normalized L1 bound is

    integral_(T^4)|partial_i^2 Q_N|<=3sqrt(N)/pi.       (FD7)

For an ambient Fourier exponent a with a_i!=0, two periodic integrations by parts give

    |Qhat_N(a)|<=3sqrt(N)/(pi*a_i^2).                  (FD8)

The function Q_N is a trigonometric polynomial, so its Fourier expansion is finite and both integrations by parts are ordinary smooth calculations.

<a id="large-rank-three-coefficients"></a>
## Rank-three relations with a coefficient at least eight

Let c be primitive and H_c={z in T^4:z^c=1} be admissible, and put q=max_j|c_j|.
The sign average removes all odd-coordinate Fourier exponents, while integration over H_c keeps precisely the exponents in Zc.
At least one coordinate of c is odd, so the retained nonzero exponents are exactly 2r c for nonzero integers r.
Choose i with |c_i|=q.
By (FD8),

    |Sbar_N(H_c)-S_N(T^4)|
      <=[3sqrt(N)/(2pi*q^2)]sum_(r=1)^infinity 1/r^2
      <5sqrt(N)/(2pi*q^2).                             (LC1)

For the last inequality, use 1/r^2<1/(r^2-1/4)=1/(r-1/2)-1/(r+1/2) for r>=2.
Its telescoping tail is2/3, which proves sum_(r>=1)1/r^2<5/3 without an exact evaluation of that series.
The notation S_N(T^4) is independent of the signs by ambient coordinate translations.

The native certificate proved below gives S_128(T^4)>59/20.
Since sqrt128<23/2 and pi>3, (LC1) implies, whenever q>=8,

    Sbar_128(H_c)>59/20-115/768
                 =14/5+1/3840>14/5.                  (LC2)

The elementary inequality pi>3 follows, for example, because the circumference of the unit circle is greater than the perimeter6 of its inscribed regular hexagon.
This proves a uniform order128 certificate for every rank-three relation having a coefficient of modulus at least eight.
It is a sign-averaged statement, not a bound for every individual sign.

<a id="bounded-rank-three-average-certificate"></a>
## Exact order128 certificates for all smaller rank-three relations

Permuting and inverting coordinates preserves Sbar_N, so it remains to consider

    0<=c_1<=c_2<=c_3<=c_4<=7,
    gcd(c_1,c_2,c_3,c_4)=1.                             (BC1)

The only inadmissible primitive vectors in this canonical set are (0,0,0,1), which kills a coordinate, and (0,0,1,1), which identifies two coordinates up to inversion.
Indeed a forbidden vector e_j or e_i+/-e_j can belong to Zc only when the two primitive vectors agree up to sign.
The native program enumerates all nondecreasing quadruples in {0,...,7}, applies exactly these tests, and obtains275 canonical admissible classes.
Zero coefficients, balanced relations and repeated positive coefficients are all included.
This finite scope is larger than the earlier forty-two full-support unbalanced classes.

Let A_n(v) be the coefficient of z^v in [sum_j(z_j+z_j^(-1))]^n.
The pair-coordinate walk formula already developed in the C863 moment mechanism is

    A_n(v)=sum_(t=0..n) binom(n,t)
       binom(t,(t+v_1+v_2)/2)binom(t,(t+v_1-v_2)/2)
       binom(n-t,(n-t+v_3+v_4)/2)
       binom(n-t,(n-t+v_3-v_4)/2),                      (BC2)

with nonintegral or out-of-range binomial indices interpreted as zero.
For a direct derivation, each step in one coordinate pair becomes two independent signs after replacing its endpoint coordinates (u,v) by (u+v,u-v).
The outer binomial chooses which steps belong to the first pair.
The same formula permits zero endpoint coordinates.

Write s=sum_j c_j and let Mbar_k be the sign average of the G_epsilon^(2k) moment on H_c.
A walk ending at v has sine coefficient (-1)^(sum_j v_j/2) times its positive cosine-walk count whenever the even-length parity condition holds.
This follows directly by multiplying the step coefficients -i for a positive step and i for a negative step.
Sign averaging keeps only even endpoint vectors.
Thus integration and pairing opposite endpoints give

    Mbar_k=A_(2k)(0)
        +2sum_(1<=r<=k/s)(-1)^(r*s)A_(2k)(2r c).       (BC3)

This is valid with zero coordinates in c; primitive c is nonzero, so s>0.
The free moment is Mfree_k=A_(2k)(0), explicitly

    Mfree_k=sum_(t=0..2k, t even)binom(2k,t)
        binom(t,t/2)^2 binom(2k-t,(2k-t)/2)^2.          (BC4)

Finally

    Sbar_128(H_c)=sum_(j=1..128)R_j/(j*64^j),
    R_j=sum_(k=0..j)(-1)^k binom(j,k)64^(j-k)Mbar_k.    (BC5)

All moments and R_j are integers, and 0<=R_j<=64^j with R_j<=64 R_(j-1).
These inequalities follow also from the underlying residual integrals, providing arithmetic controls.

The [native program](../computations/programs/Yin_J_G0134/rank-two-locality.py) computes (BC2)--(BC5) using only Python integers and Fraction.
The [selected native certificate](../computations/programs/Yin_J_G0134/inputs/rank-two-moment-certificate.json) retains the exact free-torus fraction and all275 exact canonical relation/fraction rows.
For the free fraction N/D, it checks20N-59D>0.
For every rank-three fraction N/D, it checks5N-14D>0.
The completed full run passed every one of these comparisons.
Thus

    S_128(T^4)>59/20,
    Sbar_128(H_c)>14/5 for all275 classes in (BC1).     (BC6)

The minimum class is c=(0,1,1,1), and exact integer division gives

    2944235671458/10^12<=Sbar_128(H_c)
                         <2944235671459/10^12.         (BC7)

This decimal-scale rational display is not an input to the proof.
The program's separate short Laurent expansion checks all5301 supported cosine-walk coefficients through degree8 against (BC2).
It additionally expands the antisymmetric Laurent polynomial directly, sign-averages by deleting odd endpoint coordinates and multiplies the degree2k coefficient sum by (-1)^k.
It compares those moments through degree8 with (BC3) for (0,0,1,2), (0,0,1,3), (0,1,1,1) and (1,1,1,1).
Its relation-membership test chooses an actual nonzero coordinate, so zero leading coordinates are handled without division by zero or a full-support assumption.
These are author controls, not an independent review of the full computation or proof.

The calculation used CPython3.13.15 and only its standard library.
The native certificate was generated, then the following command recomputed and matched every field:

    python mathematics/computations/programs/Yin_J_G0134/rank-two-locality.py --verify-certificate

No quadrature, rounded floating-point moment or ignored-output file is a premise.
Combining (LC2) and (BC6) gives

    Sbar_128(H)>14/5 for every admissible dim H>=3.     (BC8)

The rank-four case uses its free certificate directly.
By (ML4), this proves g(H)<17/25<log2-23/2025 on that entire higher-dimensional domain, through the present new moment argument without using the higher-dimensional conclusion of v2 as a premise.

<a id="effective-finite-rank-two-reduction"></a>
## Explicit finite exceptional hosts from relations of norm at most128

Put B=B_128={a in Z^4:||a||_1<=128}.
For any admissible torus H, let

    W(H)=span_Q(L(H) intersect B).                     (ER1)

If dim W(H)<=1, then Sbar_128(H)>14/5.
To prove this, if W=0, there are no nonzero visible relations and (ML3) transfers the free certificate.
If dim W=1, choose its primitive integer generator c.
Some nonzero multiple of c belongs to L(H), so saturation implies c in L(H).
Every short member of L(H) is a multiple of c, and conversely every multiple of c in B belongs to L(H).
Thus L(H) and Zc have exactly the same intersection with B.
The rank-three H_c is admissible because Zc is a sublattice of the admissible L(H), and (ML3) transfers its (BC8) certificate exactly.
This proves the assertion without a lattice-basis norm assumption.

Enumerate every pair of independent u,v in B and form

    L_(u,v)=span_Q(u,v) intersect Z^4,
    H_(u,v)={z in T^4:z^a=1 for all a in L_(u,v)}.    (ER2)

Discard inadmissible tori and duplicates; optionally discard those whose exact Sbar_128 exceeds14/5.
This is a finite, explicitly bounded enumeration, with rational linear algebra and integer divisibility supplying membership and equality tests.
Every admissible rank-two H not retained in this list has

    g(H)<17/25<log2-23/2025.                            (ER3)

Indeed if dim W<=1 the preceding argument applies.
Otherwise dim W=2=rank L(H), so independent u,v in the short intersection span its rational space.
Saturation then gives L(H)=L_(u,v), which puts H in the enumeration unless its own exact certificate already passes.
This proves the rank-two reduction with the explicit radius128.
The enumeration has not been run, so no actual exceptional-host list or practical computational cost is asserted.
Failing this sufficient finite certificate does not establish failure of the desired good-sign inequality.

### An effective version of the finite circle-host consequence

One can also enumerate every independent triple u,v,w in B and form the admissible rank-one tori annihilated by span_Q(u,v,w) intersect Z^4.
After discarding duplicates and optionally the passing moment certificates, this gives a second finite list.
Every admissible rank-one H outside the union of the rank-two hosts in (ER2) and this finite rank-one list satisfies (ER3).

If dim W<=1 the certificate has already been transferred.
If dim W=2, choose independent u,v in L(H) intersect B.
Then L_(u,v) is a sublattice of L(H), so H is contained in H_(u,v).
Moreover the short intersections of these two lattices coincide: every short member of L(H) lies in W=span_Q(u,v), while saturation supplies the reverse inclusion.
Their sign-averaged order128 certificates therefore agree by (ML3), so any omitted passing host already supplies the same passing certificate for this H.
If dim W=3, three independent short vectors span the rational space of the rank-three L(H), and saturation identifies H with an enumerated rank-one torus.
These cases prove the effective circle-host conclusion.

A primitive integer frequency vector for a circle in the triple list is given by the signed3-by-3 minors of the matrix with rows u,v,w, divided by their common gcd.
Each minor has absolute value at most ||u||_1||v||_1||w||_1<=128^3, by expanding the determinant and bounding the sum of its absolute terms by the full product of the row sums.
Consequently every circle in the triple list has a representative with all four primitive frequency magnitudes at most2097152.
This is a bound for that explicitly defined triple list; it gives no such bound for arbitrary circles inside a rank-two host, and no bound derived merely from small deletion indices.
Neither finite exceptional enumeration has been carried out here.

## Remaining original-task boundary

The unit-relation and paired-slope arguments remove concrete lower-rank classes from the unresolved analytic question.
The all-rank-three sign-averaged certificate makes the finite rank-two and circle-host reduction explicit, but does not evaluate every retained host or every circle lying inside one.
Even a uniform good-sign theorem for every admissible torus would still need the separate original-input integral-auxiliary supply in the [binary reflection inquiry](../drafts/Yin_D_G0013.md#binary-reflection-reduction) before it could resolve unrestricted G0001.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T18:33 |
| status | proved |
| reason | Adopt the complete five-part strengthened theorem after independent R1083: restriction-stable zero-measure signs, the infinite paired-slope family, uniform order128 certificates in dimension at least three and explicit finite candidate hosts from relations of norm at most128. All275 new finite cases and the free fraction were independently recomputed; candidate enumeration, remaining lower-rank inequalities and original-input supply remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact strengthened statement](#statement) | All five conclusions, exact inherited v2 scope, every sign/rank/normalization, uniform margins, candidate lists and primitive frequency bound. |
| argument | [Complete assembled argument](#inherited-arguments) | Exact inherited theorem and all new UR, PS, ML, FD, LC, BC and ER arguments through the stated arithmetic boundary. |
| dependency | [Adopted v2 theorem](Yin_C_G0863_v2.md#decision-whole-independent-review-2026-11-04) | All nine unchanged conclusions and their actual inherited v1/native/source/review scope; the new higher-dimensional moment proof does not assume old Part7. |
| support | [Mahler source unit](../audits/literature/Den09/Yin_U001.md#den09-u001) | The unit's accepted Mahler-measure interface: normalized Haar, Laurent integrability, circle Jensen through zeros and monomial invariance, at its recorded source-proof limits. |
| dependency | [Exact order128 program](../computations/programs/Yin_J_G0134/rank-two-locality.py) | Complete free and sign-averaged finite reconstruction, canonical scope and author control procedures inspected in R1083. |
| dependency | [Selected native certificate](../computations/programs/Yin_J_G0134/inputs/rank-two-moment-certificate.json) | All275 bounded canonical relations plus free-torus exact fraction, with every mathematical field independently recomputed in R1083. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1083_v1.md#whole-version-and-effective-certificate) | Complete statement and new proof, inherited interfaces, all new exact native inputs and actual independent implementation; no new order4096 run or source-proof audit. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
