---
author: Yin
---
# All-place binary masks and coherent rational centers

Human author Yin.
This project deduction strengthens the original-input part of [C857 v1](Yin_C_G0857_v1.md#statement) by imposing the actual simultaneous condition at every prime above two.
The original v1 statement, including the arbitrary-field one-place cyclic classification, its simple-pole specialization, and its high-precision reciprocal units of measure greater than log 2, remains fixed with its [complete argument](Yin_C_G0857_v1.md#argument) and [actual selected assessment](Yin_C_G0857_v1.md#decision-whole-independent-review-2026-11-04).
This version does not transfer that assessment or its review to the new mathematics.
The near-one arithmetic-supply contributor developed the new argument for Yin; the coordinating main agent checked the supplied derivation as a contributor.
No independent review is claimed by that development or checking.

## Statement

Let P in Z[t] be monic, irreducible, reciprocal and noncyclotomic, of degree d>=2 and constant term one, and suppose every positive power of a root has degree d.
For all its conjugates alpha_1,...,alpha_d, put P_n(x)=product_i(1-alpha_i^n x), U=P_2, V=P_4, W=(V-U)/4, and r=bar W/bar U in F_2(x), with bars denoting reduction modulo two.
These are the original inputs and notation of [C860 v2](Yin_C_G0860_v2.md#statement), with no degree-normalized measure substituted.
The equal leading and constant coefficients of U and V imply that r is proper, regular at zero, and r(0)=0.
Its reduced denominator has degree at most d.
No squarefree-reduction hypothesis is imposed.

There are a unique proper rational function c in F_2(x) whose partial fractions have only odd negative exponents and a unique rational function h in F_2(x), regular at zero and infinity with h(0)=0, such that

    r=c+h^2+h.                                               (A1)

The function c is regular at zero, c(0)=0, and its poles are among those of r.
At each such geometric pole beta, its order is at most the order of r there.
Writing m_beta>0 for the pole order of r at beta, the reduced denominator degree e of h is at most sum_beta floor(m_beta/2), and hence e<=floor(d/2).
For h=0 put e=0.
The numerator degree of h is at most e; it need not be strictly smaller after normalization at zero.

For an odd prime q, choose a primitive q-th root zeta=zeta_q and put K=Q(zeta).
Let K_q^all(r) consist of masks epsilon=(epsilon_0,...,epsilon_(q-1)) in F_2^q for which

    sum_j epsilon_j r(xi_p^j x) belongs to wp(k_p(x))        (A2)

at every prime p of K above two, with k_p its residue field and xi_p the reduction of the same chosen zeta_q.
Here wp(z)=z^2+z.
Let 1_q denote the full mask and E_q the even-weight subspace.

If c=0, then K_q^all(r)=F_2^q for every odd prime q.
If c is nonzero, define the positive integer

    g=gcd{n>=1 : [x^n]c(x) != 0}.                            (A3)

Then g is odd, c=s(x^g) for some s in F_2(x), and g divides both the total geometric pole degree and the number of distinct geometric poles of c.
In particular 1<=g<=d.
The all-place mask space is exactly

    E_q,                        if q divides g;
    span_F2(1_q),               if q does not divide g and
                                  [x^(qn)]c(x)=0 for every n>=1;
    {0},                        otherwise.                 (A4)

Consequently a nonempty proper all-place mask exists precisely when c=0 or q divides g.
In the latter case the admissible masks are exactly the nonempty proper even masks.
For nonzero c this requires q to divide both its pole degree and its distinct-pole count, so q<=d; more precisely q is at most the degree of the squarefree part of bar U.
For several distinct such primes, their product divides g and both pole counts.
This conclusion holds for every odd q, without any assumption on ord_q(2).

The four possibilities are thus zero, the full-mask line, the even-weight space, and the entire mask space.
The statement concerns the original r in F_2(x) and simultaneous residue factors.
It does not replace C857's more general one-place classification for an arbitrary fixed r in k(x).

The same normalized h supplies the coherent integer centers and rational trace approximants (A10)--(A15) below.
Precisely, for any nonempty admissible mask I with orbit O and union S, these centers are fixed by their mask stabilizers, their simultaneous initial precision is at least three, and every common valid depth lambda>=3 gives integral approximants F_t satisfying (A13) with shifted Hankel rank at most t|S|(d+2e)<=2td|S| for all t>=1.
Here e is the denominator degree of h, all radicals use the original conjugates, and no minimal-rank or small-measure supply assertion is included.

## Exact inputs and retained scope

| Role | Input and exact use |
| --- | --- |
| Dependency | [C860 v2](Yin_C_G0860_v2.md#statement), at its [selected assessment](Yin_C_G0860_v2.md#decision-whole-independent-review-2026-11-04): the original P_4-P_2 divisibility by four, with its exact Dimitrov v1 Lemma 2.1 source interface retained in that version. |
| Dependency | [C860 v1](Yin_C_G0860_v1.md#statement), at its [selected assessment](Yin_C_G0860_v1.md#decision-whole-independent-review-2026-11-04): only the scaled-binomial valuation used in (A13). |
| Dependency | [C858](Yin_C_G0858_v1.md#all-place-hankel-budget), at its [selected assessment](Yin_C_G0858_v1.md#decision-whole-independent-review-2026-11-04): the finite rational-series recurrence bounds the shifted Hankel rank from numerator and denominator degrees in (A15). |
| Accepted source input | [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001): the prime-cyclotomic integer ring Z[zeta_q] and its degree, giving O_K/2O_K=F_2[z]/(Phi_q). Its already retained statement scope is reused, without a fresh inspection of the original integer-ring proof. |
| Source attribution | [Dang, arXiv:2002.03719v3, Section 2.1, Example 2.1 and Remark 2.2, printed/PDF page 4](../literature/pdf/Dan20--arxiv-v3.pdf#page=4): standard Artin--Schreier partial-fraction reduction, proved explicitly here as (A5)--(A6). The [source notes](../audits/literature/Dan20/readme.md) retain edition and inspection limits. |
| Fixed comparison | [C857 v1](Yin_C_G0857_v1.md#statement): the arbitrary-field one-place statement and large-measure controls retain their exact old scopes. They are not a source of near-one input supply. |

<a id="argument"></a>
## Complete argument

<a id="reduced-representative"></a>
### The explicit reduced representative

Work temporarily over the algebraic closure of F_2 and write the finite partial-fraction expansion

    r(x)=sum_beta sum_(m>=1) a_(beta,m)/(x-beta)^m.

There is no polynomial part because r is proper, and beta is never zero.
For every odd u>=1 set

    c_(beta,u)=sum_(s>=0) a_(beta,2^s u)^(2^(-s)),
    c(x)=sum_beta sum_(u odd) c_(beta,u)/(x-beta)^u.           (A5)

All displayed sums are finite, and inverse Frobenius powers are uniquely defined in the algebraic closure.
For an individual term with m=2^s u, the identity

    a/(x-beta)^(2^s u) + a^(2^(-s))/(x-beta)^u
      =wp(sum_(l=1)^s a^(2^(-l))/(x-beta)^(2^(s-l)u))        (A6)

is obtained by telescoping.
Summing (A6) gives r=c+wp(h_0), where h_0 is proper and has pole order at beta at most floor(m_beta/2).
The formulas commute with coefficient Frobenius, which permutes beta and sends each coefficient a to a^2.
Since r is fixed by this action, so are c and h_0; their normalized rational numerators and denominators therefore have coefficients in F_2.
They are regular at zero.
Evaluating there gives c(0)=r(0)+h_0(0)^2+h_0(0)=0 because h_0(0) lies in F_2.
Set h=h_0+h_0(0).
This preserves (A1), preserves all pole orders and regularity at infinity, and gives h(0)=0.

For uniqueness, a nonzero proper rational function with only odd negative exponents in its partial fractions cannot be wp(v) for a rational v over the algebraic closure.
Indeed a pole of v of order b produces a pole of wp(v) of order 2b, whereas a nonzero reduced proper function has a pole of odd order.
If v has no finite poles, it is a polynomial; properness of wp(v) forces v to be constant and wp(v)=0.
The difference of two reduced proper representatives again has only odd negative exponents, so it must be zero.
Two rational solutions h of (A1) differ by zero or one, and normalization at zero selects one.
The pole-order bounds from (A6) give all denominator-degree bounds in the statement.

This is the usual Artin--Schreier partial-fraction reduction, here written explicitly to retain finite-field descent, normalization, and degree costs.
For attribution, [Dang, arXiv:2002.03719v3, 3 January 2021, Section 2.1, Example 2.1 and Remark 2.2, printed/PDF page 4](../literature/pdf/Dan20--arxiv-v3.pdf#page=4), states the reduction to partial fractions of orders prime to the characteristic.
The title, author, exact v3 identifier, displayed example and reduced-form statement were read in the selected original.
The [source notes](../audits/literature/Dan20/readme.md) record the sign slip in Example 2.1; the reduced-form statement supplies attribution, while (A5)--(A6) prove the characteristic-two reduction directly.
That standard reduction is attribution, not an unproved input to the complete calculation (A5)--(A6).
The explicit F_2 descent, all-place classification and coherent-center consequences below are established here.
No whole-paper inspection or novelty claim is made.

<a id="all-place-mask-kernel"></a>
### Local solvability, all residue factors, and multiplier invariance

Fix a primitive q-th root xi in the algebraic closure of F_2.
Substitution x->xi^j x in (A1) gives the reduced representative c(xi^j x) of r(xi^j x).
Scaling x preserves odd partial-fraction orders; a sum of such representatives again has only odd negative exponents.
Therefore for every mask epsilon,

    sum_j epsilon_j r(xi^j x) in wp(F_2(xi)(x))
      iff sum_j epsilon_j c(xi^j x)=0.                     (A7)

The forward direction follows from the odd-pole uniqueness argument even after extending constants to the algebraic closure.
For the reverse direction, sum_j epsilon_j h(xi^j x) is an explicit rational solution over F_2(xi), normalized at zero.
Thus extension of constants introduces no unaccounted constant-class obstruction in (A7).

The accepted prime-cyclotomic integer-ring input used in C860 v2 gives

    O_K/2O_K = F_2[z]/(Phi_q(z)).

The polynomial Phi_q is squarefree modulo two because q is odd.
Its residue factors correspond to Frobenius orbits of primitive q-th roots.
Embeddings of all these residue fields into the algebraic closure send zeta_q to xi^a for every a in (Z/qZ)^*, exactly once when the Frobenius embeddings are also listed.
Because r,c,h have F_2 coefficients, (A7) is equivariant under these Frobenius embeddings.
Thus (A2) at every residue factor is exactly

    sum_j epsilon_j c(xi^(aj) x)=0 for every a in (Z/qZ)^*. (A8)

This proves directly that the all-place space is stable under all multipliers j->a j.
It is also stable under cyclic translation, by replacing x with xi^b x in every equation.
Equivalently it is the intersection of the multiplier translates of one residue-place kernel.
[C857 v1's cyclic-ideal description](Yin_C_G0857_v1.md#binary-cyclic-mask) applies to each of those kernels, but the following coefficient proof avoids any further representation-theoretic input.

<a id="four-spaces-symmetry"></a>
### The four spaces and the exact symmetry integer

Write c(x)=sum_(n>=1)c_n x^n, and define the binary mask polynomial

    A_epsilon(z)=sum_(j=0)^(q-1) epsilon_j z^j.

Equation (A8) is equivalent to

    c_n A_epsilon(xi^(an))=0
      for every n>=1 and every a!=0 mod q.                 (A9)

If c=0 there is no condition, giving the entire space.
Suppose c is nonzero.
If every supported n is divisible by q, (A9) is exactly A_epsilon(1)=0, giving E_q.
If at least one supported n is not divisible by q, multiplication by n permutes all nonzero residue classes.
Then A_epsilon vanishes at every primitive q-th root, so Phi_q divides A_epsilon over F_2.
Since deg A_epsilon<=q-1, this forces A_epsilon=0 or A_epsilon=Phi_q.
The latter is the full mask; it satisfies (A9) precisely when no supported n is divisible by q, because Phi_q(1)=q=1 in F_2.
If the support has both kinds of exponent, only the zero mask survives.
This proves the full-mask and mixed-support cases in (A4), including when Phi_q is reducible modulo two.

The gcd in (A3) is well defined because c is nonzero and c(0)=0.
It is odd: at a pole of c of odd order M, the derivative c' has nonzero leading term of order M+1, so c' is not zero, and some supported Taylor exponent is odd.
Take a reduced expression c=A_0/B_0 with coprime A_0,B_0 in F_2[x] and B_0(0)=1.
Let eta be a primitive g-th root, which exists because g is odd.
The Taylor support gives c(eta x)=c(x).
Uniqueness of the reduced rational expression with denominator constant one gives

    A_0(eta x)=A_0(x), B_0(eta x)=B_0(x).

Consequently every nonzero coefficient exponent of both polynomials is divisible by g, proving c=s(x^g) with s in F_2(x).
Conversely, any common divisor of those positive polynomial exponents divides the Taylor support, so g can equivalently be computed as the gcd of the positive exponents occurring in A_0 and B_0.
This is a finite calculation on the original reduced representative.
The action beta->eta beta is free on the nonzero finite poles and preserves their orders.
Its orbits have length g, proving the divisibility of both pole degree and distinct-pole count.
Those poles are among the roots of bar U, proving the stated original-degree and squarefree-part bounds.

The same normalization also shows directly that r in wp(k(x)) for any finite extension k/F_2 is equivalent to r in wp(F_2(x)).
A solution is regular at zero; after adding one if necessary its value there is zero, and this normalized solution is unique.
Every Frobenius conjugate is then the same solution, so it descends to F_2(x).
Equivalently this is precisely the case c=0 in (A1).

<a id="coherent-centers"></a>
### Coherent centers with each rotation paid only once

Write the normalized h of (A1) as a/b, with a,b in F_2[x], a(0)=0, b(0)=1 and deg a<=deg b=e<=floor(d/2).
Choose integer coefficient lifts A,B of those same degrees with A(0)=0 and B(0)=1, and put C=B+2A.
Define

    R_*(x)=V(x)B(x)^2/(U(x)C(x)^2).

Its constant coefficient is one, R_*-1 belongs to 4x Z[[x]], and

    (R_*-1)/4 mod 2
      =[W B^2-U(AB+A^2)]/(U C^2) mod 2
      =r+h+h^2=c.                                          (A10)

For a mask I put B_I=product_(j in I)B(zeta^j x), C_I=product_(j in I)C(zeta^j x), D_I=product_(j in I)U(zeta^j x), and N_I=product_(j in I)V(zeta^j x).
Products of the factors 1+4((R_*-1)/4) show that

    N_I B_I^2-D_I C_I^2 belongs to 8 O_K[x]
      iff I belongs to K_q^all(r).                          (A11)

Indeed dividing the difference by 4D_I C_I^2 and reducing at each prime above two gives exactly the sum of c(xi_p^j x) over I.
All denominators have constant coefficient one, so the formal-series congruence is equivalent to polynomial coefficient divisibility.
The squarefree cyclotomic residue decomposition makes simultaneous reduction zero equivalent to divisibility by two of the already integral numerator divided by four.

Thus one integer rational function supplies coherent centers for every all-place mask, including the full-mask line and both larger kernels.
The center C_I/B_I is fixed by the mask stabilizer, because it is a product of copies of the same rational function over the positions of I.
No separate CRT choice or division by stabilizer order is needed.

Fix a nonempty admissible I, let O be its full Galois orbit and S=union_(J in O)J.
Let lambda>=3 be a common valid coefficient depth in (A11), put a=lambda-2, and define

    Z_J=N_J B_J^2/(D_J C_J^2)-1,
    T_(J,t)=(C_J/B_J) sum_(v=0)^t binom(1/2,v) Z_J^v,
    F_t=sum_(J in O)T_(J,t),
    f=sum_(J in O)(N_J/D_J)^(1/2),                          (A12)

where t>=1 and the original square roots have constant coefficient one.
The normalized identity G_J=(C_J/B_J)(1+Z_J)^(1/2) and C860 v1's binomial valuation give

    f-F_t belongs to 2^[a(t+1)+1] Z[[x]].                   (A13)

Each truncation has algebraic-integral Taylor coefficients: binom(1/2,v) has only powers of two in its denominator, and lambda>=3 pays those denominators.
The Galois-invariant sum and its difference from f therefore have integral coefficients; no stabilizer-division loss occurs.

For X=B,C,U set Q_X=product_(j in S)X(zeta^j x).
These polynomials belong to Z[x] and have constant coefficient one.
A common denominator for F_t is

    Q_B Q_U^t Q_C^(2t-1).                                  (A14)

Its degree, and the degree of the resulting numerator, are at most

    t kappa_0,  where kappa_0=|S|(d+2e)<=2d|S|.             (A15)

For one J, the denominator B_J D_J^t C_J^(2t-1) gives numerator and denominator degree at most t|J|(d+2e).
Multiplying by the missing rotation factors in (A14) adds at most t(|S|-|J|)(d+2e), proving the numerator bound as well.
The numerator is integral because (A14) is an integer polynomial with constant coefficient one and F_t has integral Taylor coefficients.
The shifted rational Hankel rank is therefore at most t kappa_0 by the finite recurrence argument already accepted in C858.
The denominator charges each original or center rotation once and requires no stabilizer division.
It is an upper bound, not a minimal-rank assertion; the actual-rank analysis remains separate.

## Return to the unresolved original question

These statements give an exact test on the actual P and an explicit coherent all-place center whenever that test succeeds.
For a nonzero reduced representative, rich proper-mask supply is equivalent to a specific finite symmetry of that representative, not a dimension count or a primitive-root-prime assumption.
They do not show that positive total m(P) tending to zero forces c=0, forces g>1, or forces favorable precision divided by actual rank.
The automatic construction only guarantees lambda=3 and retains kappa_0 of order d|S|.
The [high-measure controls of C857 v1](Yin_C_G0857_v1.md#large-period-full-mask) remain controls and are not converted into near-one inputs.
No unrestricted Mahler gap or near-one counterexample family follows.

The comparison with C857 v1 uses its actual one-place scope; the coefficient proof here adds the all-place intersection and the original F_2 descent.
The checked standard source attributes partial-fraction reduction, without a novelty or whole-literature assertion.

## Current assessment
[Selected decision](#decision-whole-independent-review-2026-11-04)

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T20:32 |
| status | proved |
| reason | Adopt the entire all-place classification and coherent-center construction after independent R1074 v2. The original reduced representative determines all four mask spaces for every odd prime, and the constructed centers pay all precision and degree costs. Earlier one-place and large-measure v1 scopes remain separate. No near-one supply or unrestricted Mahler gap follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact new statement](#statement) | Complete A1--A15, all original-input hypotheses, normalized reduction, every all-place mask case, finite symmetry, coherent centers and integral rank bounds. |
| argument | [Complete argument](#argument) | Entire explicit reduction and descent, residue-factor equivalence, Taylor classification, finite symmetry, integer-center construction and all-precision degree accounting. |
| dependency | [Original modulo-four input](Yin_C_G0860_v2.md#statement) | Only the same original polynomials and their unconditional modulo-four congruence, with the exact retained Dimitrov source scope. |
| dependency | [Scaled-binomial valuation](Yin_C_G0860_v1.md#higher-depth-hankel-comparison) | Exact integer valuation and formal remainder for every supplied lambda at least three. |
| dependency | [Finite rational-series rank](Yin_C_G0858_v1.md#all-place-hankel-budget) | Only the finite recurrence from bounded numerator and denominator degrees to shifted Hankel rank. |
| support | [Cyclotomic integer-ring input](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Exact accepted integer-ring and degree statements, with original-proof inspection limits retained. |
| review | [Independent all-place finding](../audits/reviews/Yin_R_G1074_v2.md#all-place-mask-whole) | Whole new theorem and argument, corrected exact dependency attribution, source limitations and preservation of v1 scope. |
