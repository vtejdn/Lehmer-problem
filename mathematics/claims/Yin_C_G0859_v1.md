---
author: Yin
---
# Low-energy phase resonance without a template binomial cover

Human author Yin.
The arithmetic agent developed the exact seed family, direct Haar-margin estimate and residue-template argument during G0001 on 2026-11-05.
The main agent selected the research question and supplied the final balanced-lift applicability comparison.
The selected decision below owns the assessment and exact independent review evidence.
Provenance: project deduction with checked attribution of the known square-lattice Mahler measure.

The entire required argument is fixed below; mutable drafts, J134 quadrature and CK21 primitive trace-one existence are not proof inputs.
The scope concerns a failed template-level extension of [C845's low-energy phase criterion](Yin_C_G0845_v1.md#statement) and [C849's negative-mean template criterion](Yin_C_G0849_v1.md#fixed-bivariate-template-specialization-class); neither criterion is used to prove this result.
The [Den09 Mahler conventions](../audits/literature/Den09/Yin_U001.md#mahler-measure) supply natural logarithms, normalized torus Haar measure and invariance under Laurent monomials.
The proof below establishes integrability for this specific template directly.

## Statement

Fix the denominator q=3.
For every pair of positive integers n,a set

    H_(n,a)(x)=1+2x^a+x^(n+2a),
    k=n+2a,
    V_(n,a)(x)=x^n H_(n,a)(x)+x^k H_(n,a)(x^(-1)).

The seed has exactly three distinct nonzero coefficients, energy6<9, constant1 and leading coefficient1.
It belongs to the allowed low-energy seed class, with no constant-seed exception.
Direct expansion gives

    V_(n,a)=x^(2n+2a)+x^(n+2a)+4x^(n+a)+x^n+1
           =x^(n+a) L(x^(n+a),x^a),
    L(Y,Z)=4+Y+Y^(-1)+Z+Z^(-1).

All five exponents are distinct, the full degree and span are2(n+a), and V is monic reciprocal.
The following assertions hold for the exact template, independently of n,a.

1. Its full logarithmic Haar measure satisfies m_2(L)>log4-1/4>log3.
2. The reduction of L modulo3 is absolutely irreducible in the two-variable Laurent polynomial ring.
3. Over the algebraic closure of F_3 it divides no finite product of nonzero binomials Y^u Z^v-c, for nonzero integer pairs(u,v), nonzero constants c and arbitrary positive multiplicities.

They establish neither irreducibility of V nor a near-zero original minimal polynomial admitting V(alpha)/3 as an integer.
They do not assert an upper or lower bound on the degree of a one-variable binomial cover after specialization.

## Complete argument

### Strict Haar margin in the wrong direction

The following direct estimate proves

    m_2(L)>log4-1/4>log3.                     (R1)

Use independent uniform angles theta,phi, and put X=(cos theta+cos phi)/2.
Its distribution is symmetric, and |X|<=1.
For0<t<1 the absolutely convergent logarithmic series gives

    E log(1+tX)=-sum_(j>=1) t^(2j) E(X^(2j))/(2j).

The torus homomorphism (u,v) -> (u+v,u-v) preserves Haar probability, since it is surjective with finite kernel.
The identity (cos(u+v)+cos(u-v))/2=cos u cos v and the elementary constant-term formula for cos^(2j) therefore give

    E(X^(2j))=binom(2j,j)^2/16^j=:c_j.

One has c_1=1/4 and c_j<=1/(3j+1) for every j>=0.
For the latter assertion use c_0=1 and c_(j+1)/c_j=(2j+1)^2/(4(j+1)^2).
The induction step reduces to

    4(j+1)^2(3j+1)-(2j+1)^2(3j+4)=j>=0.

Consequently

    sum_(j>=1)c_j/(2j)
      <1/8+(1/6)sum_(j>=2)1/j^2
      <1/8+(1/6)(1/4+integral_2^infinity t^(-2)dt)
      =1/4.

The inequalities are strict because3j+1>3j and t^(-2) is strictly decreasing.
Symmetry gives E log(1+tX)=(1/2)E log(1-t^2X^2).
Monotone convergence for the nonnegative functions -log(1-t^2X^2), together with the finite series bound, proves integrability at t=1 and the same limiting series.
The positive part of log(1+X) is bounded, while symmetry and integrability of log(1-X^2) control its negative part.
Since L on the torus equals4(1+X), the first inequality in(R1) follows.
Finally log(4/3)=integral_1^(4/3)dt/t> (1/3)(3/4)=1/4, which proves the second.

This is a local elementary margin estimate for a known square-lattice Mahler measure, not a new evaluation of that measure.
GR12, Guttmann--Rogers, Spanning tree generating functions and Mahler measures, J.Phys.A45(2012)494001, printed p.3/PDF p.4 of the [retained publication](../literature/pdf/GR12.pdf), gives the corresponding square-lattice integral as4G/pi, where G is Catalan's constant.
The primary published PDF was directly read at [the author's university-hosted copy](https://cpb-ap-se2.wpmucdn.com/blogs.unimelb.edu.au/dist/0/310/files/2019/12/Guttmann_2012_J._Phys._A__Math._Theor._45_494001.pdf).
Replacing both circle variables by their negatives matches its minus-sign integral with L exactly.
That exact displayed identity is checked attribution, not a proof premise of(R1), and the paper's full derivation and cited earlier proofs were not audited.

### The full residue template is absolutely irreducible

Reduce L modulo3 and multiply by YZ, a Laurent unit.
Over the algebraic closure k of F_3 the result is

    Q(Y,Z)=Z*Y^2+(Z^2+Z+1)*Y+Z.

As a quadratic in Y over k(Z), its discriminant is

    (Z^2+Z+1)^2-4Z^2=(Z+1)^2(Z^2+1).

The two roots of Z^2+1 are distinct and neither equals-1, so this rational function has simple zeros and cannot be a square in k(Z).
The elementary quadratic formula in characteristic3 therefore proves irreducibility over k(Z).
The polynomial is primitive in k[Z][Y]: any common factor of its coefficients divides Z and also Z^2+Z+1, hence is constant.
To see directly that no factorization is lost on passing to k(Z), clear a denominator and inspect a putative pole at Z=z_0.
At least one coefficient of Q remains nonzero modulo Z-z_0, so the product relation forces the other polynomial's numerator to vanish coefficientwise there; cancel that denominator factor and repeat.
The same reasoning permits powers of Z as Laurent units.
It follows that Q, and thus L modulo3, is irreducible in k[Y^(+/-1),Z^(+/-1)].

### No finite binomial product covers this template

By a nonzero binomial here mean Y^u Z^v-c, where(u,v) is a nonzero integer pair and c is nonzero in k.
The absolutely irreducible L modulo3 divides no finite product of such binomials, including products with arbitrary multiplicities.
Indeed irreducibility in the Laurent polynomial unique-factorization domain would force divisibility of one binomial.
For completeness, the needed primeness can equivalently be checked first over k(Z)[Y] and then by the preceding denominator-cancellation argument.
Choose a nonzero integer weight vector perpendicular to(u,v).
The highest and lowest weights of a product are the sums of those of its factors: the products of the nonzero extreme homogeneous pieces cannot vanish in the Laurent polynomial domain.
The binomial has weight width0, while L modulo3 has positive width for every nonzero weight because its support contains(1,0),(-1,0),(0,1),(0,-1).
Thus no Laurent multiple of L can be that binomial, proving the assertion.
The elementary width argument is the Newton-polytope product mechanism, used here with its full direct justification rather than a new polytope theorem.
For checked attribution, Ivan C.H. Ip's [Introduction to Cluster Algebra, Lecture8](https://www.math.hkust.edu.hk/~ivanip/teaching/cluster/Lecture8-UpperBound.pdf), version2017-06-12, p.6, Proposition8.25(1) and Example8.26, states the Laurent product formula and its binomial-factor segment consequence.
The displayed statements were directly read; the lecture's cluster-algebra setting is not imported, and the needed characteristic3 conclusion follows from the explicit domain-and-weight proof above.

### What this refutes and what remains open

The seed family and(R1) disprove removal of the phase-separation condition by a universal strict template Haar bound for all allowed q=3 seeds.
Its absolutely irreducible residue curve also disproves the stronger proposed template-level alternative that every such bad-Haar resonance admits a finite binomial cover of its entire residue template.
This is not yet a counterexample to a theorem about specialized one-variable linear-cost covers.
Every fixed nonzero finite-field specialization with nonzero constant term divides some x^B-1 after a sufficiently large characteristic-power multiplicity factor, and its required exponent may vary with n,a.
Template irreducibility supplies no quantitative lower bound for that B.
Nor does it rule out a different useful rational auxiliary, a suitable factor of V, a different modulus, or coverage restricted to genuinely small positive total Mahler measure.
The exact one-variable binomial cost remains unevaluated, but the following direct application already covers this family's actual arithmetic inputs without such a cover.
It therefore removes that cost question from the next-step priority for advancing G0001 through this example.

<a id="balanced-lift-coverage"></a>
### A balanced coefficient lift already gives an existing scalar certificate

Replace the coefficient 2 in H by -1, preserving its class modulo3:

    Hhat=1-x^a+x^(n+2a),
    Vhat=x^n Hhat+Hhat*=V-6x^(n+a)
        =x^(2n+2a)+x^(n+2a)-2x^(n+a)+x^n+1.

For n,a>0 the five exponents are distinct, so the true coefficient energy of Vhat is exactly8<9, and its span is still T=2(n+a).
For any actual nontorsion algebraic integer unit alpha, integrality of V(alpha)/3 implies integrality of Vhat(alpha)/3, because their difference is the algebraic integer 2 alpha^(n+a).
The converse holds as well.
There is no change of the original field, degree, span or denominator.

Let d be the original degree of alpha and m its total logarithmic Mahler measure.
Apply the already adopted [C844 Part A](Yin_C_G0844_v1.md#statement), including its zero-value guard, at q=3 to the nonzero polynomial Vhat.
If Tm/d<=u_3 for that theorem's fixed computable positive cutoff, it would force Vhat=+/-3x^j, contrary to its five coefficients.
Consequently every such arithmetic input satisfies

    Tm/d>u_3,
    T<=C d  implies  m>u_3/C.

This is a direct application of existing scalar-energy rigidity, not a new gap mechanism or a numerical execution of u_3.
It includes a possible zero value of the original auxiliary and requires only the actual integrality and original-window hypotheses already needed by the phase route.
Thus the fixed-lift template counterexample above does not show failure of arithmetic certificate coverage for this family.
Further investigation of a general resonance/coverage alternative must first minimize the actual coefficients in the permitted congruence class and reuse adequate scalar bounds; an unfavorable chosen lift alone is insufficient.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T16:37 |
| status | proved |
| reason | Adopt the exact template obstruction and final balanced-lift applicability comparison after independent R1075. The bad chosen template does not expose a new arithmetic coverage gap: its actual integral-value inputs already satisfy the existing C844 scalar criterion after a permitted coefficient change. No unrestricted auxiliary supply or G0001 completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All positive-parameter seeds, actual phase template, strict Haar bound, absolute residue irreducibility and every finite binomial product, with the stated limits. |
| argument | [Complete argument](#complete-argument) | Entire direct Haar, residue and width proof and the final balanced-lift comparison, including all source-attribution limits. |
| dependency | [Existing scalar rigidity](Yin_C_G0844_v1.md#statement) | Part A only at q=3, including true coefficient energy, original field/degree/span and its zero-value guard, for the balanced-lift application. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1075_v1.md#resonance-balanced-lift-whole) | Entire fixed theorem and balanced-lift addition, precise C844 reuse, sources at checked attribution scope and original-task limits. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
