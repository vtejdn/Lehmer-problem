---
author: Yin
---

# Radicals of arbitrary separate Salem conjugate-field factors

Human author Yin.
The coordinating agent proposed the ordinary-norm dichotomy, and the arithmetic-return contributor checked its external-torsion towers, finite-place costs, factor cancellation and actual-degree inequalities on 2026-11-05.
This extension of the same arithmetic-return family has a selected independent whole assessment at its exact stated scope.
The complete [v1 statements and proof](Yin_C_G0866_v1.md#statement), its [selected independent assessment](Yin_C_G0866_v1.md#decision-whole-independent-review-2026-11-04), and its [exact quartic control](Yin_C_G0866_v1.md#quadratic-saturation-control) remain at their unchanged fixed home.
The extraction source is [D1's separate-factor dichotomy](../drafts/Yin_D_G0001.md#p2-separable-radical-dichotomy); that mutable working section and the earlier coupled-unit inquiry are not proof premises.

## Exact fixed inputs and their boundaries

[C866 v1](Yin_C_G0866_v1.md#statement), at its selected assessment linked above, supplies the actual-degree raw-norm bound for every nontorsion radical of a conjugate monomial, allowing arbitrary external torsion and extensions.
For a primitive Salem source alpha, its conclusion is M_2(beta)>=M_2(alpha)/2.
Its complete integer-monomial orbit proof, denominator and own-degree costs, and nonprimitive boundary remain fixed there; none is replaced by an unreviewed D1 calculation.
The final application below explicitly normalizes its integer exponents into v1's coprime numerator/denominator domain.
The quartic control proves sharpness of the degree multiplier relative to the intermediate monomial, not sharpness of the final one-half comparison with alpha.

[C383's trace fixed field](Yin_C_G0383_v1.md#actual-inversion-matching-average) and [actual Salem conjugations](Yin_C_G0383_v1.md#salem-kernel-class-population) supply the inversion kernel, its trace splitting field, and the conjugate complex conjugations fixing one pair and flipping all others.
Their exact elementary argument and the needed half-coordinate count are also given below.
The ancestor's selected assessment remains SELF, with its retained CM10 attribution and source-inspection limits.
No split-extension theorem, full symmetric top group, kernel-size lower bound or prime estimate is required.

[C485's full-field norm-one identity](Yin_C_G0485_v1.md#salem-relative-regulator-identity), at its [selected SELF scope](Yin_C_G0485_v1.md#decision-complete-current-self-adoption), identifies the full ring of integer units with relative norm one as the signed powers of the smallest Salem generator.
It is used for the units r_i/iota_i(r_i), not for the arbitrary individual factors r_i.
Its accepted source is [Smy15-U001](../audits/literature/Smy15/Yin_U001.md#smy15-u001), Lemma 2 and Proposition 3, at the retained statement/displayed-proof inspection: every positive Salem power retains its degree and field, and every Salem number in its full field is a positive power of the smallest one.
The original Salem publications are not newly inspected, and no regulator estimate is imported.

The only new external height interface is [Smy08-U002's Schinzel statement](../audits/literature/Smy08/Yin_U002.md#smy08-restricted-height-gap), equation (22) of the retained arXiv:math/0701397v2 survey, Section 6.1, printed pp.330--331.
For a totally real algebraic integer gamma outside {0,1,-1}, it states h_abs(gamma)>=log(phi)/2, where phi=(1+sqrt(5))/2.
This is accepted at the retained survey statement and applicability scope; the original Schinzel proof is not newly audited.
It is applied only to an actual nontorsion unit in a totally real field, at that element's own degree.

Neither the universal raw-p2 floor nor a unit-rank, real-or-circle, fixed-function or unit-lattice theorem is a premise.
No original-source proof upgrade or mathematical novelty is claimed.

## All-place normalization

All logarithms are natural.
For any nonzero algebraic number z of actual degree D_z and own field K_z=Q(z), use the places v of K_z with the usual extensions of the rational absolute values.
At an archimedean place use the usual real or complex modulus and local degree n_v equal to 1 or 2.
At a finite place over a prime p, write e_v and f_v for its ramification and residue degrees, take the integer valuation ord_v, and set

    n_v=e_v f_v,
    log|z|_v=-(ord_v(z)/e_v)log p.

Define the absolute height, total logarithmic Mahler measure, and raw all-place p=2 quantity by

    h_abs(z)=(1/D_z) sum_v n_v log^+|z|_v,
    m(z)=D_z h_abs(z),
    M_2(z)=D_z [(1/D_z) sum_v n_v (log|z|_v)^2]^(1/2).
                                                               (F1)

Only finitely many finite-place terms are nonzero.
Thus m(z) is the logarithm of the usual total Mahler measure of the primitive irreducible polynomial, including its leading coefficient.
For an algebraic integer unit all finite terms vanish, and, counting all D_z complex embeddings separately, including both members of each nonreal pair,

    M_2(z)^2=D_z sum_(j=1)^(D_z) log^2|z_j|,
    2m(z)=sum_(j=1)^(D_z) |log|z_j||,
    M_2(z)>=2m(z).                                             (F2)

The middle identity follows from the product formula, and the last inequality is Cauchy--Schwarz on these D_z entries.
The unit inequality is used only after integrality and invertibility have been established.

## Statement

Let alpha>1 be a genuine Salem number of degree d=2t>=4, with K=Q(alpha), splitting field L and G=Gal(L/Q).
Choose one oriented root u_i from each of its t inverse pairs and set

    K_i=Q(u_i),
    iota_i(u_i)=u_i^(-1),
    r_i in K_i^*,
    w=product_(i=1)^t r_i.                                    (F3)

The involution iota_i is the inverse involution of K_i over its trace field.
Each r_i is arbitrary and nonzero: there is no individual integrality, unit, relative-norm, degree-of-expression or height hypothesis.
Let s>=1 be an integer, xi an arbitrary root of unity, and beta a nonzero nontorsion algebraic number satisfying

    beta^s=xi w,
    D=[Q(beta):Q].                                             (F4)

Neither beta nor xi is assumed to belong to L.

### A. Primitive source and the three paid branches

Suppose alpha is primitive in its full field, meaning it is the smallest Salem number in K in the accepted fixed-field sense.
Then

    M_2(beta)>=min{log(phi), M_2(alpha)/2},
    M_2(alpha)=sqrt(2d)m(alpha)=sqrt(2d)log alpha.               (F5)

More precisely, if beta is not an algebraic integer unit, its finite-place terms already give M_2(beta)>=log 2.
If beta is a unit, let V be the kernel of G acting on the inverse pairs, put E_0=L^V, and define

    M=E_0(beta), q=[M:E_0]<=D,
    Gamma=Norm_(M/E_0)(beta).                                  (F6)

The field E_0 is totally real.
If Gamma is nontorsion, then

    M_2(beta)>=(D/q)log(phi)>=log(phi).                        (F7)

If Gamma is torsion, there exist integers b_i, not all zero, and a root of unity chi such that

    beta^(2s)=chi product_i u_i^(b_i),
    M_2(beta)>=M_2(alpha)/2.                                  (F8)

Thus the torsion-norm branch lies in the exact radical domain of v1, even when the r_i have nontrivial finite valuations cancelling in w.

### B. Nonprimitive source

If alpha=alpha_0^A, where alpha_0 is the smallest Salem generator in K and A>=1 is an integer, the same conclusion becomes

    M_2(beta)>=min{log(phi), M_2(alpha)/(2A)}.                  (F9)

The nonunit and nontorsion-norm bounds are unchanged.
The factor A is the actual source power and is not suppressed in a uniform comparison with alpha.

### C. Consequence for a hypothetical sequence approaching measure one

For primitive Salem sources, F5 implies

    M_2(beta)/m(alpha)
      >=min{log(phi)/m(alpha), sqrt(2d)/2}.                    (F10)

Along any hypothetical sequence of primitive Salem alpha with m(alpha) tending to zero, both entries on the right tend to infinity.
Consequently this entire separate-factor radical class cannot supply outputs with M_2(beta)<=C m(alpha) for one fixed C along such a sequence.
This statement does not assert that all sources with m(alpha)<=1 have bounded degree: the constant-height branch F7 does not give that conclusion.
It also does not assert that every coupled unit of L admits a factorization of the form F3.

## Argument

### 1. The finite-place branch

If beta is not an algebraic integer unit, some finite place v of its own field Q(beta) has a nonzero integer ord_v(beta).
Its single term in F1 is

    M_2(beta)^2
      >=D(f_v/e_v)ord_v(beta)^2(log p)^2
      >=(log 2)^2.                                           (F11)

Here e_v<=D, f_v>=1, |ord_v(beta)|>=1 and p>=2.
This includes nonintegral outputs as well as algebraic integers that are not units.
Since 1<phi<2, F11 proves both F5 and F9 in this branch without any universal raw-norm input.

<a id="trace-field-and-unit-norm"></a>
### 2. The actual trace splitting field and unit norm

Assume henceforth that beta is a unit.
Then w=xi^(-1)beta^s is an algebraic integer unit and belongs to L, regardless of the separate finite valuations of the r_i.

Put theta_i=u_i+u_i^(-1).
These values are distinct, since the two roots of X^2-theta_i X+1 are exactly the inverse pair i.
An automorphism in G fixes all theta_i if and only if it fixes every inverse pair, so

    E_0=L^V=Q(theta_1,...,theta_t).

All theta_i are real, and every embedding permutes them, which proves that E_0 is totally real.
An element of V either fixes or inverts each u_i, so the i-th sign is a homomorphism V->F_2.
For every i choose g_i in G sending u_i to the expanding real conjugate alpha.
If c is complex conjugation in this embedding of L, then c_i=g_i^(-1)c g_i fixes pair i pointwise and flips every other pair.
This holds because the other Salem pairs are nonreal and on the unit circle.
For each coordinate j, some c_i with i!=j flips it, since t>=2.
Its coordinate homomorphism on V is therefore nonzero, and exactly |V|/2 elements of V flip that coordinate.
These are the needed C383 interfaces, proved without any stronger classification of V or G.

The element Gamma in F6 is a unit in E_0, because the ordinary relative norm of a unit is a unit.
The minimal polynomial of beta over Q is also a polynomial over E_0, so q<=D.
If Gamma is nontorsion, its totally real minimal field and integrality satisfy the Schinzel statement exactly, giving

    h_abs(Gamma)>=log(phi)/2.

The ordinary norm is a product of q conjugates of beta.
Absolute-height subadditivity and invariance under embeddings therefore give

    h_abs(Gamma)<=q h_abs(beta).

There is no additional factor [E_0:Q] in this inequality.
Using the unit inequality F2 gives

    M_2(beta)>=2D h_abs(beta)
             >=(D/q)log(phi),

which proves F7 at the actual own output degree D.

<a id="external-torsion-intersection"></a>
### 3. Torsion norm and the actual intersection field

Suppose Gamma is torsion.
Let k be the actual finite order of xi.
Then w^k=beta^(sk), and the field

    F=E_0(w^k)

is contained in both M and L.
Neither xi nor w itself is presumed to belong to M.
The first norm tower is thus legitimate and gives

    Norm_(M/E_0)(w^k)=Gamma^(sk)
      =Norm_(F/E_0)(w^k)^([M:F]).                             (F12)

If a positive integer power of a nonzero algebraic number is torsion, that number is torsion.
It follows from F12 that Norm_(F/E_0)(w^k) is torsion.
The second tower, now through F inside L, gives

    Norm_(L/E_0)(w^k)
      =Norm_(F/E_0)(w^k)^([L:F]),

so this norm is torsion as well.
It equals Norm_(L/E_0)(w)^k, and hence Norm_(L/E_0)(w) is torsion.
No equality of M and L, containment of the external torsion, or unproved intersection degree has been used.

<a id="separate-factor-cancellation"></a>
### 4. Arbitrary factor cancellation forces a monomial square

Set

    n_i=r_i iota_i(r_i) in Q(theta_i) subset E_0,
    N_0=product_i n_i.

The half-coordinate count from Section 2 gives the exact identity

    Norm_(L/E_0)(w)=product_(v in V) v(w)
      =product_i [r_i^(|V|/2) iota_i(r_i)^(|V|/2)]
      =N_0^(|V|/2).                                          (F13)

Section 3 implies that N_0 is torsion.
It lies in the totally real field E_0, whose roots of unity are precisely 1 and -1; hence N_0 is 1 or -1.
The individual n_i have not been assumed integral or units.

For the conjugate complex conjugation c_i from Section 2, direct multiplication gives

    w c_i(w)=r_i^2 product_(j!=i) n_j
            =N_0 r_i/iota_i(r_i).                            (F14)

The left side is a unit, because w is a unit, and N_0 is a unit.
Consequently a_i=r_i/iota_i(r_i) is a unit.
It belongs to K_i, so both it and its inverse are algebraic integers in that field, and it has relative norm one under iota_i.
For a primitive alpha, C485's full-field kernel, transported to K_i through an automorphism sending u_i to alpha, therefore gives

    a_i=epsilon_i u_i^(b_i),
    epsilon_i in {1,-1}, b_i in Z.                            (F15)

Every kernel hypothesis has been established for a_i; none has been imposed retrospectively on r_i.
Multiplying F15 and using the definitions of n_i yields

    w^2=N_0 product_i a_i
       =zeta product_i u_i^(b_i), zeta in {1,-1},
    beta^(2s)=xi^2 zeta product_i u_i^(b_i).                   (F16)

The vector b is nonzero, since otherwise a positive integer power of beta would be torsion and beta would be torsion, contrary to F4.

To apply the exact v1 domain, put h=gcd(|b_1|,...,|b_t|)>0, b'_i=b_i/h and eta=product_i u_i^(b'_i).
Let c_0=gcd(h,2s), g_0=h/c_0 and s_0=2s/c_0, so gcd(g_0,s_0)=1.
Equation F16 implies

    (beta^(s_0)/eta^(g_0))^(c_0)=xi^2 zeta.

The quotient is a root of unity, possibly outside L, so beta^(s_0)=xi_0 eta^(g_0) for some root of unity xi_0.
This is exactly v1 Part A with nonzero gcd-one b', positive coprime g_0,s_0, arbitrary external torsion and actual own output degree D.
Its full degree accounting gives M_2(beta)>=M_2(alpha)/2, proving F8 and then F5.
No extension or denominator has been discarded in invoking that fixed bound.

<a id="nonprimitive-and-sequence-boundaries"></a>
### 5. The source-power boundary and the sequence consequence

For a nonprimitive alpha=alpha_0^A, the accepted fixed-field theorem gives Q(alpha_0)=K and the same degree d.
Every positive Salem power preserves degree and field, so the corresponding conjugates v_i of alpha_0 can be oriented with v_i^A=u_i and Q(v_i)=K_i.
Their inverse involutions agree with iota_i.
Their splitting field is L as well: each root field Q(v_i) equals Q(u_i), and the splitting fields are the composita of these fields.
Thus F14 still yields units a_i in the same full fields, and the full-field kernel now gives a_i=epsilon_i v_i^(b_i).
The argument F16 applies with alpha_0 and its conjugates, so v1 gives

    M_2(beta)>=M_2(alpha_0)/2=M_2(alpha)/(2A)

in the torsion-norm branch.
The finite-place and Schinzel branches are unchanged, proving F9.

Finally, for primitive sources divide F5 by the positive value m(alpha)=log alpha to obtain F10.
If there were a bounded-degree subsequence while these Salem measures tend to zero, its degrees and houses would both be bounded: eventually alpha<=e and every other conjugate has modulus at most alpha.
Each coefficient of each monic minimal polynomial is then bounded by an elementary symmetric-sum bound, and only finitely many such integer polynomials exist.
Their finitely many expanding roots greater than one have a positive minimum logarithm, a contradiction.
Thus d tends to infinity whenever m(alpha) tends to zero.
Both entries in the minimum in F10 tend to infinity, proving Part C.

## Scope and review limits

Each factor r_i may be a value of a rational function in the single conjugate u_i, with rational coefficients, degree and denominators chosen from the whole original input.
No fixed-function assumption is used, and finite valuations may cancel arbitrarily among the separate factors.
The argument also allows arbitrary external radicals and torsion.
It does not cover a general algebraic number expressed by a genuinely coupled function of several conjugates merely because that number lies in L.
In particular it does not prove that every norm-one unit in L factors as F3, and it supplies no sufficiently small coupled-unit construction.

F10 excludes a bounded raw-p2 return ratio along a hypothetical primitive Salem sequence with total measure tending to zero for this precise construction class.
The constant-height branch F7 supplies no assertion that all inputs with m(alpha)<=1 have bounded degree.
Neither this class restriction nor the fixed v1 control proves the unrestricted [G0001 total-Mahler gap](../tasks/Yin_T_G0001_v1.md#contract), favorable new total-gap coverage, or attainment of the final one-half constant.

No numerical experiment, polynomial enumeration, native computation or new original-proof audit is used.
The contributor checks and the separately selected independent whole finding concern this larger domain; v1's independent review remains at its own fixed scope.
All prior SELF relationships and accepted-source inspection limits remain unchanged.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T23:10 |
| status | proved |
| reason | Adopt the complete all-place conventions, Statement A--C and F1--F16 after independent R1088 v2. Arbitrary separate conjugate-field factors, their finite-place cancellation, external torsion and radicals are paid through the finite-place floor, the actual totally real norm, or the exact v1 monomial-radical domain. The nonprimitive power cost and precise hypothetical-sequence consequence are retained. Prior fixed results, ancestor SELF/unknown relationships and source-proof limits remain unchanged; no general coupled-unit factorization, small coupled-unit supply or unrestricted G0001 conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | All A--C and F3--F10, arbitrary nonzero individual factors and external data, three branches, primitive/nonprimitive distinctions and exact sequence limits. |
| argument | [Complete argument](#argument) | All five proof sections and F11--F16, using F1--F2 all-place normalization, actual norm towers, half-coordinate count, recovered unit hypotheses and coprime invocation of v1. |
| dependency | [Adopted radical degree cost](Yin_C_G0866_v1.md#statement) | Exact Part A for a nonzero gcd-one conjugate-monomial vector, coprime positive exponents, arbitrary external torsion and actual own degree; its fixed proof and independent review remain at v1. |
| dependency | [Actual trace fixed field](Yin_C_G0383_v1.md#actual-inversion-matching-average) | Only the inverse-pair kernel and field generated by the distinct original traces; directly reconstructed here. |
| dependency | [Actual Salem conjugations](Yin_C_G0383_v1.md#salem-kernel-class-population) | Only one-pair-fixed/all-other-pairs-flipped conjugations and the exact half-coordinate count, preserving the ancestor's SELF/source scope. |
| dependency | [Full-ring norm-one kernel](Yin_C_G0485_v1.md#salem-relative-regulator-identity) | Signed powers of the smallest Salem generator, applied only after the norm-one ratios have been proved units; no regulator comparison. |
| support | [Smy15 fixed-field theorem](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Accepted Lemma 2/Proposition 3 and positive-power degree/field preservation at retained statement/displayed-proof inspection. |
| support | [Schinzel canonical source](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only retained survey equation (22), totally real integer height at least log(phi)/2 outside {0,1,-1}, at accepted statement/applicability scope; no original Schinzel proof audit. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1088_v2.md#whole-separate-factor-radical-finding) | Complete conventions, A--C and proof, exact source interfaces and v1 invocation, all three branches, nonprimitive and sequence boundaries, with unchanged ancestor review relationships. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
