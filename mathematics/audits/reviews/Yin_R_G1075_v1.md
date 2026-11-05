---
author: Yin
---
# Independent review of the denominator-three resonance and balanced-lift scope

Review act: 2026-11-04T16:34 UTC.
The human record author is Yin.
This separately organized reviewer did not develop C0859 and received no substantive proof-development conversation, proposing-agent mathematical summary or earlier verdict about that candidate.
The complete fixed statement and argument, including the final balanced-lift comparison, were read directly with their necessary inputs and current rules.
D13, J134 and the CK21 construction were not consulted or used.
No substantive proof repair was supplied by the reviewer.

<a id="resonance-balanced-lift-whole"></a>
## Whole independent finding

**Finding:** no unresolved mathematical gap was found in the complete [C0859 statement](../../claims/Yin_C_G0859_v1.md#statement), [argument](../../claims/Yin_C_G0859_v1.md#complete-argument) and [balanced-lift application](../../claims/Yin_C_G0859_v1.md#balanced-lift-coverage).
The finding covers the exact seed family, the strict Haar margin, absolute irreducibility in characteristic three, exclusion of every finite Laurent-binomial product, and the existing scalar certificate for actual arithmetic inputs.
It does not establish any additional specialized binomial-cover bound or complete the unrestricted Lehmer Task.

### Seed, collected coefficients and scope

For positive n and a, the three exponents 0,a,n+2a of H are distinct, with coefficient energy 1+4+1=6<9.
The actual reversal degree is k=n+2a, and the displayed expansion of x^n H+H* gives exactly the five exponents 0,n,n+a,n+2a,2(n+a), in increasing order.
The collected central coefficient is four, and the two other exponent pairs are symmetric about n+a.
Thus the degree, span, monicity, reciprocity and specialization through L all hold for every allowed pair, including n=a.

The allowed-seed definition was checked directly in [C845's statement](../../claims/Yin_C_G0845_v1.md#statement).
This nonconstant seed meets that definition without the excluded constant +/-q case.
The independent phase-separation hypothesis of C845 is not assumed satisfied.
The [C849 template definition](../../claims/Yin_C_G0849_v1.md#fixed-bivariate-template-specialization-class) requires a strict Haar mean below log q; the displayed template instead lies strictly above log 3.
Those are exact comparisons of hypotheses, not uses or new reviews of the complete C845 and C849 proofs.
The natural logarithm, normalized Haar probability and Laurent-monomial conventions match [Den09 U001](../literature/Den09/Yin_U001.md#mahler-measure).
The singularity at the torus zero is retained and treated by the argument rather than removed from the integral.

### Strict Haar estimate and its endpoint

The map (u,v) to (u+v,u-v) is a surjective torus homomorphism with finite kernel, so it pushes Haar probability to Haar probability without a factor of two.
Consequently the even moments of X equal the product of two cosine moments, namely binom(2j,j)^2/16^j.
Symmetry removes the odd terms from the absolutely convergent logarithmic expansion for 0<t<1.
The displayed recurrence and the induction identity with remainder j verify c_j<=1/(3j+1), including c_0=1 and c_1=1/4.
For j>=2 the replacement of 3j+1 by 3j is strict, and the decreasing-integrand comparison bounds the remaining square-reciprocal sum strictly by 3/4.
The resulting sum c_j/(2j) is therefore strictly less than 1/4, as required.

The functions -log(1-t^2 X^2) are nonnegative and increase as t tends to one.
Their bounded expectations, supplied by the same positive-term series, permit monotone convergence and give an integrable endpoint.
The positive part of log(1+X) is bounded by log 2, and the negative part is controlled by -log(1-X^2) plus a bounded term.
Thus the endpoint identity and m_2(L)=log 4-sum_(j>=1)c_j/(2j) are legitimate finite expectations.
The elementary integral bound log(4/3)>1/4 is strict, so both inequalities m_2(L)>log 4-1/4>log 3 follow.
No numerical quadrature or external exact evaluation is needed for this proof.

The actual [GR12 publication PDF](../../literature/pdf/GR12.pdf) was inspected at its title page and printed page 3/PDF page 4.
The square-lattice display uses normalized measure 1/(4 pi^2), integrand log[4-2(cos k1+cos k2)] and value 4G/pi.
Translating both angles by pi gives exactly the present plus-sign template.
This confirms the stated known-measure attribution at the displayed-identity scope; it is not a new audit of that evaluation's derivation or the earlier proofs cited by GR12.

### Absolute irreducibility and all binomial products

In characteristic three, multiplying the residue template by the Laurent unit YZ gives the displayed primitive quadratic Q=ZY^2+(Z^2+Z+1)Y+Z.
Its discriminant factors exactly as (Z+1)^2(Z^2+1).
The two roots of Z^2+1 are simple and differ from -1, so the discriminant has odd valuations and is not a square in the rational function field over the algebraic closure.
The characteristic is different from two, making the quadratic irreducibility test applicable.
The three coefficients have no common nonconstant divisor in k[Z].
Thus irreducibility over k(Z) descends to the polynomial ring, and localization at Y and Z preserves it because Q has neither of those variables as a factor.
This verifies absolute irreducibility of the Laurent residue, not merely irreducibility over F3.

In the Laurent polynomial unique-factorization domain this irreducible element is prime.
Divisibility of a finite binomial product would therefore give divisibility of one factor, irrespective of repetitions or characteristic-three multiplicities.
For each nonzero integer pair (u,v), an integer perpendicular weight exists and is nonzero.
The binomial Y^u Z^v-c has width zero in that weight, while the four retained corner exponents of L give strictly positive width for every nonzero weight.
The extreme homogeneous parts of a product multiply nontrivially in the domain, so highest and lowest weights add even when other coefficients cancel.
This rules out the purported binomial divisibility and proves the full finite-product assertion, with negative exponents and arbitrary nonzero constants allowed.

The actual [Ip17 Lecture 8 PDF](../../literature/pdf/Ip17.pdf) was inspected at pages 1 and 6.
Its title and 12 June 2017 update match the cited version; Proposition 8.25(1) gives the Newton-polytope product formula and Example 8.26 gives the segment constraint on factors of a binomial.
These displayed statements supply the stated attribution only.
The needed conclusion in characteristic three is justified by the explicit weight-domain argument above, without importing the lecture's cluster-algebra or subtraction-free assumptions.
No full lecture proof audit or exhaustive priority search is claimed.

### Balanced lift and actual arithmetic coverage

Replacing the coefficient two of H by minus one preserves its residue modulo three.
The reversal uses the same actual degree k, so the two middle contributions change the central coefficient of V from four to minus two, giving V-Vhat=6x^(n+a).
The five distinct exponents stay unchanged; the collected energy of Vhat is exactly 1+1+4+1+1=8<9, and its span remains T=2(n+a)>0.
For an actual algebraic integer unit alpha, the difference of the two quotient values is the algebraic integer 2 alpha^(n+a).
Algebraic integrality of either quotient in the original field is therefore equivalent to integrality of the other, including a possible zero value.
No original field, degree, span or denominator is changed by this replacement.

The reusable input is precisely [C844 Statement A](../../claims/Yin_C_G0844_v1.md#statement), at its [selected proved decision](../../claims/Yin_C_G0844_v1.md#decision-whole-reviewed-2026-10-28).
Its exact hypotheses and the coverage of the adopted [R1064 whole scalar-energy finding](Yin_R_G1064_v1.md#whole-scalar-energy-finding) were inspected.
C844 permits all nonzero integer Laurent polynomials of true energy at most q^2, requires algebraic integrality rather than membership in Z[alpha], retains the original d and total m, and explicitly includes zero evaluated values before any norm logarithm.
These are exactly the required interfaces at q=3 and F=Vhat.
The present review reuses that accepted result and its recorded original-source limits; it does not assert a new proof review of C844 or its recursive dependencies.

If Tm/d<=u_3, C844 forces Vhat to be a signed monomial with coefficient three, which its five distinct nonzero coefficients exclude.
Hence Tm/d>u_3, and T<=Cd implies m>u_3/C with the same fixed positive cutoff.
The argument does not numerically evaluate that cutoff or construct an integral auxiliary for an arbitrary original input.
It correctly covers this family's actual integral-value inputs without solving its one-variable binomial-cover cost.

The template-level failures therefore coexist with existing arithmetic coverage after a permitted coefficient lift.
Absolute irreducibility of the bivariate residue gives no quantitative bound for a specialized one-variable period, and the text makes no such inference.
The usual finite-field root orders and a sufficiently large power of the characteristic do permit a binomial annihilator for each fixed specialization with nonzero constant term, but give no uniform linear-cost conclusion here.
Neither irreducibility of V nor existence of arbitrarily small positive-measure original inputs is proved.
The final applicability conclusion and retained [G0001 contract](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth) are therefore consistent: this result identifies and closes a proposed example-level coverage objection, not the unrestricted Mahler-gap problem.

No mathematical program or proof assistant was run for this review.
Its mathematical evidence is the fixed derivations, the checked accepted-input interfaces and the stated limited source inspections.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#resonance-balanced-lift-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#resonance-balanced-lift-whole) | [C0859 statement](../../claims/Yin_C_G0859_v1.md#statement) | All positive n,a seeds, collected coefficients and span, the strict Haar margin, absolute residue irreducibility and every finite Laurent-binomial product, with exact exclusions. |
| [Whole finding](#resonance-balanced-lift-whole) | [C0859 complete argument](../../claims/Yin_C_G0859_v1.md#complete-argument) | Complete Haar, endpoint-integrability, residue, weight-width, attribution and original-task applicability chain, including the final balanced-lift comparison. |
| [Whole finding](#resonance-balanced-lift-whole) | [C0859 balanced lift](../../claims/Yin_C_G0859_v1.md#balanced-lift-coverage) | Exact coefficient replacement, energy eight, same original field/degree/span, integral-value equivalence, C844 zero-inclusive interface and conditional original-window bound. |
| [Whole finding](#resonance-balanced-lift-whole) | [C844 input](../../claims/Yin_C_G0844_v1.md#statement) | Statement A only, reused at its selected proved scope: fixed q, true coefficient energy, original degree and total measure, full algebraic integrality and zero-value guard; no new whole C844 review. |
