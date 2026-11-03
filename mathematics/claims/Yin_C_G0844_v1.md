---
author: Yin
---

# Fixed-denominator scalar energy rigidity without covariance

Human author Yin.
Root supplied the fixed-denominator variance argument, concavity constants, finite logarithmic cutoff, zero-value guard and proposed scalar and positive-weight conclusions.
Contributor core_feedback_structure checked the complete derivation, original norm/monomial normalization, computable cutoff, all-width and zero-value cases, and the targeted reuse interfaces retained below.
Both are proof contributors.
The [selected adopted decision](#decision-whole-reviewed-2026-10-28) is proved through [whole independent R1064](../audits/reviews/Yin_R_G1064_v1.md#whole-scalar-energy-finding).
The original OPEN decision and fixed body retain their historical wording; the separate review covers all fixed-q scalar and real-weight conclusions.


The [C95 comparison precision in R1064](../audits/reviews/Yin_R_G1064_v1.md#6-exact-reuse-and-limitations) distinguishes its literal eight-power family clause, which uses a common union dictionary, from the own-span family consequence obtained by applying its scalar bound separately and summing.
The latter is a direct consequence, not a quotation of that literal family clause; the denominator-independent C93/C95 domains do not imply a strict numerical ordering against C844 for every fixed q.

## Statement

Let alpha be an ACTUAL nontorsion algebraic integer unit, P its monic irreducible minimal polynomial, d>=2 its ORIGINAL degree and m=m(P)>0 its TOTAL logarithmic Mahler measure.
All norms and angular/radial averages use all d original conjugates.
Fix an integer q>=2; q is a coefficient-clearing integer and need not be the least denominator.
For a nonzero rational Laurent polynomial, energy is the sum of squares of its TRUE collected coefficients and span is its maximum exponent minus its minimum exponent.
An integral value means algebraic integrality over Z in Q(alpha), with no requirement of membership in the monogenic order Z[alpha].

Use exactly

    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log sqrt(c0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0,
    B=q^2+1, delta=1/(2q^2 B), eta=1/(8q^4 B^2),
    J=ceil(B/(4eta^2)), A_q=1+q/delta.

There is a computable positive dyadic rational u_q, depending only on q, with

    Ju_q<h0,
    A_q u_q+2^J epsilon(Ju_q)<eta,
    (q^2-1)epsilon(u_q)+2q^2 u_q<1.

The [ordered cutoff recipe](#scalar-setting-and-q-only-cutoff) certifies Ju<h0 BEFORE evaluating either epsilon term and then certifies the remaining strict inequalities.
Every choice with these properties has all the conclusions below.

**A. Complete low-energy numerator rigidity, including a possible zero value.**
For every NONZERO integer Laurent polynomial F with sum_j F_j^2<=q^2, algebraically integral F(alpha)/q, and span(F)*m/d<=u_q,

    F=+/-q x^j for some integer j.

The value F(alpha)/q is allowed to be zero in the hypotheses and is proved nonzero in this range before a norm logarithm is used.
Width zero is settled separately and never uses epsilon(0).

**B. Arbitrary-support scalar energy and its exact equality case.**
For every rational Laurent polynomial f with qf in Z[x,x^(-1)], NONZERO algebraically integral value f(alpha), and its OWN span T satisfying T*m/d<=u_q,

    ||f||_2^2>=1,
    ||f||_2^2=1 if and only if f=+/-x^j,
    f not a signed monomial implies ||f||_2^2>=1+1/q^2.

There is no term-count hypothesis in B.
The last alternative includes a one-term polynomial whose coefficient is neither+1 nor-1.
The conclusion concerns the true polynomial, not a value-equivalent replacement.

**C. Every finite positive-real-weight family with individual spans.**
For any finite indexed family satisfying B with the SAME q and each member's OWN span bound, give the members arbitrary real weights omega_i>0 with sum_i omega_i=1.
With E=sum_i omega_i||f_i||_2^2 and mu=sum_(i:f_i is not a signed monomial)omega_i,

    E>=1+mu/q^2,             0<=mu<=q^2(E-1).

In particular E=1 if and only if every indexed polynomial is a signed monomial.
No common union-span bound, covariance identity, rationality of the weights, minimum positive weight or label-count bound is required.
No rational copied-resultant assertion is attached to these real weights.

**D. Conditional fixed-denominator scalar-class gap in every degree.**
For every fixed C>0, a nonmonomial integer Laurent F with at least two terms, energy<=q^2, algebraically integral F(alpha)/q including a possible zero value, and0<T=span(F)<=C*d must satisfy

    T*m/d>u_q,                    m>u_q/C.

Equivalently the same class can be expressed using a NONZERO rational Laurent f that is not a signed monomial, qf integral, energy<=1, integral value and span(f)<=C*d; the zero-width case is already settled by A.
No certificate in this class is constructed for an arbitrary actual input.
The cutoff may be extremely small; no improved numerical constant, uniform varying-denominator conclusion or unrestricted Mahler gap is asserted.
The stronger denominator-independent small-support floors of C93/C95 and the distinct quantitative complementary-packet bounds of C71 retain their original scopes.

## Exact reuse and source limits

[C50 Statement D](Yin_C_G0050_v1.md#statement) already excludes strict-below-one energy for bounded coefficient denominators, but does not cover scalar energy equality.
[C71 Statement A](Yin_C_G0071_v1.md#statement) treats E=1 through exact complementary covariance and an auxiliary atom or cross product; that covariance hypothesis is absent here.
[C90 Statement B](Yin_C_G0090_v1.md#statement) explicitly does not assert monomial rigidity from coefficient energy1 alone, and its general-rank lattice theorem uses an independent dictionary and O0 values.
[C93 Statement B](Yin_C_G0093_v1.md#statement) and [C95 Statement C](Yin_C_G0095_v1.md#statement) already give stronger denominator-independent floors5/4 and17/16 on at most seven and eight powers at their fixed K0, with O0 values and own-span positive-weight consequences.
Those small-support statements are retained as stronger results on their domains; in particular binary four-term rigidity is not new.

[C137 Sections1--2](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) supply the complete finite logarithmic upper certificate, all original roots, radial expense and finite-frequency cost.
[C92 Statement A](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) supplies the separate zero-value inequality, before any norm logarithm is used.
[C140](Yin_C_G0140_v1.md#statement) already gives a normalized sparse logarithmic transfer once a uniform negative logarithmic margin is supplied, including its [zero-value closure](Yin_C_G0140_v1.md#normalized-cost-zero-value-closure); its general regularization uses the accepted BS13 interface.
[C151's fixed-lattice accounting](Yin_C_G0151_v1.md#fixed-lattice-energy-accounting) already gives l1 bounds from fixed denominator and energy, but its resulting fixed-denominator exclusion is still strict-below-one reuse.
[C27's fixed-denominator exclusion](Yin_C_G0027_v1.md#near-one-denominator-complete-proof) concerns below-one first-window packets in its flat class and does not supply the equality claim below.

The contribution here is the uniform finite logarithmic margin at scalar energy<=1 for nonmonomials on a fixed coefficient lattice, and its direct assembly with C137 and C92.
The margin would also provide the missing hypothesis for C140; the direct argument below avoids a BS13 constant, Lawton comparison, finite coefficient-family classification or bounded-degree completion.
Parseval and endpoint autocorrelation are elementary mechanisms already used in C71 and C151; their complete required calculation is given below.
No exhaustive literature search or novelty claim is made.

[C570's actual finite-frequency theorem](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) owns the exact epsilon, monotonicity, positive domain and original powered-degree repetitions used through C137 and C92.
Its inherited Pri11/Dim19 source-inspection limits are retained; no source proof or discrepancy domain is enlarged here.
The argument invokes only the required finite certificate and annihilator interfaces, not C137's seed family or bounded-degree completion, C140's computed BS13 constant, or C394.
The [D7 scalar-rigidity section](../drafts/Yin_D_G0007.md#fixed-denominator-scalar-energy-rigidity) records extraction provenance only and supplies no mutable proof premise.
The entire proof and q-only recipe are fixed below; no source acquisition, native calculation or J output is an input.

## Complete argument

<a id="scalar-setting-and-q-only-cutoff"></a>
### ER2. Exact scalar setting and computable constants

Let alpha be an ACTUAL nontorsion algebraic integer unit, P its monic irreducible minimal polynomial, d>=2 its ORIGINAL degree, and m=m(P)>0 its TOTAL logarithmic Mahler measure.
All norms and angular/radial averages retain all d original conjugates.
Fix an integer q>=2; q need only clear the coefficients and is not required to be their least denominator.
For a rational Laurent polynomial, energy means the sum of squares of its TRUE collected rational coefficients, and span means its maximum exponent minus its minimum exponent.
An integral value below means algebraic integrality over Z in Q(alpha), not necessarily membership in Z[alpha].

Retain the exact C137/C92 functions

    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log sqrt(c0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0.

They are increasing on this specified positive domain and epsilon(u) tends to0 with u.
For the fixed q put

    B=q^2+1,
    delta=1/(2q^2 B),
    eta=1/(8q^4 B^2),                 delta^2=2eta,
    J=ceil(B/(4eta^2)),
    A_q=1+q/delta.                                     (ER1)

Choose a positive dyadic rational u_q satisfying all three strict conditions

    J u_q<h0,
    A_q u_q+2^J epsilon(Ju_q)<eta,
    (q^2-1)epsilon(u_q)+2q^2 u_q<1.                    (ER2)

Such a choice exists because J and A_q are fixed and epsilon tends to0.
It is computable by dovetailing the positive integer N in u=2^(-N) and certified rational interval precision.
FIRST certify Ju<h0 for a candidate; do not evaluate epsilon(u) or epsilon(Ju) unless this domain check has passed.
For a domain-certified candidate, compute interval upper bounds for the two remaining left sides and accept only when both strict inequalities are certified.
A sufficiently small dyadic u has strict margins in all three conditions, so some finite certificate is eventually reached.
No undecided equality comparison is required to choose u_q, and no numerical search has been run here.
All quantities in ER1 are rational or integer; the inherited functions in ER2 are computable on their exact positive domain.

The low-energy assertion to prove is: for every NONZERO integer Laurent F with coefficient energy<=q^2 and algebraically integral F(alpha)/q, allowing that value to be zero, span(F)*m/d<=u_q implies

    F=+/-q x^j for some integer j.                    (ER3)

In particular every polynomial with at least two terms under these integrality and energy hypotheses must satisfy span(F)*m/d>u_q.
No reciprocity, coefficient-height restriction on P, assumption span(F)<d, or fixed list of exponent patterns is imposed.

<a id="uniform-energy-logarithmic-margin"></a>
### ER3. A uniform logarithmic margin from the extreme lag

First let F have at least two terms.
Multiply by one unit monomial so that its actual support starts at0 and ends at T>0, and keep the name F for this normalized integer polynomial.
Since its coefficients are integers and their squares sum to at most q^2,

    number of nonzero coefficients<=q^2,
    ||F||_1<=sum_j F_j^2<=q^2.

Put f=F/q and W(z)=|f(z)|^2 on the unit circle with normalized Haar measure.
Then

    E:=integral W=||f||_2^2<=1,
    0<=W<=q^2.

The Fourier coefficient of W at its extreme nonzero lag T is F_T F_0/q^2, and at-T it is the same real number.
Each has absolute value at least1/q^2 because the integer endpoint coefficients are nonzero.
Parseval for the finite Laurent polynomial W-E therefore gives

    Var(W):=integral(W-E)^2
          =sum_(l!=0)|widehat W(l)|^2>=2/q^4.          (ER4)

Interior exponent collisions cannot cancel either extreme-lag coefficient.
This is an individual scalar variance bound, not a covariance identity for a family.

For0<x,mu<=B, the second derivative of log x is at most-1/B^2, and hence

    log x<=log mu+(x-mu)/mu-(x-mu)^2/(2B^2).

For completeness subtract the right side from log x: the resulting function has nonpositive second derivative, value0 and derivative0 at x=mu, so its maximum is0.
Apply this with x=W+delta^2 and mu=E+delta^2.
Both lie in(0,B] because W<=q^2 and delta^2<1.
Integration cancels the linear term, preserves variance, and gives

    (1/2)integral log(W+delta^2)
      <=(1/2)log(E+delta^2)-Var(W)/(4B^2)
      <=delta^2/2-1/(2q^4 B^2)=-3eta.                (ER5)

The second line uses E<=1 and log(1+delta^2)<=delta^2.
No logarithm of a zero circle value is taken because delta>0.

Define the finite Laurent polynomial

    Y=1-(W+delta^2)/B,
    Phi_J=(1/2)log B-(1/2)sum_(j=1)^J Y^j/j.

Since0<=Y<=1-delta^2/B<1, C137's elementary finite logarithm tail gives

    0<=Phi_J-(1/2)log(W+delta^2)
       <=B/[2(J+1)delta^2]
       =B/[4eta(J+1)]<eta.                            (ER6)

The strict last inequality is exactly J+1>B/(4eta^2), which follows from ER1 even when the quantity inside the ceiling is an integer.
Taking constant coefficients, equivalently normalized circle integrals, yields the UNIFORM finite certificate

    CT Phi_J<-2eta.                                   (ER7)

Its margin depends only on q, not on T, the positions of the exponents or the original minimal polynomial.
Every actual Phi_J is finite; no limiting frequency argument or evaluation of a Mahler integral through its zeros is required.

<a id="zero-exclusion-and-full-norm-transfer"></a>
### ER4. Excluding zero before paying the complete original norm

Put h=T*m/d and suppose0<h<=u_q.
If F(alpha)=0, C92 applies to this NONZERO rational polynomial with effective support

    rho=||F||_1^2/||F||_2^2<=number of nonzero terms<=q^2.

It forces1<=(rho-1)epsilon(h)+2rho h, whereas monotonicity and ER2 give

    (rho-1)epsilon(h)+2rho h
       <=(q^2-1)epsilon(u_q)+2q^2 u_q<1.

Thus F(alpha) cannot be zero in this range.
The norm floor below is used only AFTER this exclusion.

The preceding monomial normalization preserves algebraic integrality because alpha and alpha^(-1) are algebraic integers.
If the original first exponent was j, its full norm changes only by Norm(alpha)^(-j), a sign in{+1,-1}.
For the normalized F, algebraic integrality now gives the complete original signed identity

    Res(P,F)=q^d N,
    N=Norm_(Q(alpha)/Q)(F(alpha)/q) in Z minus{0}.

Consequently log|Res(P,F)|/d>=log q, with no requirement that F(alpha)/q belong to the monogenic order.

Apply C137 Sections1--2 to the INTEGER F with raw parameters

    delta_raw=q delta, B_raw=q^2 B,
    S_raw=||F||_1<=q^2.

They satisfy B_raw>=S_raw^2+delta_raw^2 because B=q^2+1 and delta^2<=1.
The raw Y equals the normalized Y above, and the raw finite log majorant equals log q+Phi_J.
C137 therefore gives, with its entire original radial and finite-frequency expenses,

    0<=CT Phi_J+(1+S_raw/(q delta))h+2^J epsilon(Jh)
       <=CT Phi_J+A_q u_q+2^J epsilon(Ju_q)
       <-2eta+eta=-eta<0.                             (ER8)

All evaluations are in the actual domain0<Jh<=Ju_q<h0.
The finite matrix size behind C137 remains2JT+1 and its Fourier coefficient price remains2^J; neither cost is removed by fixing q.
This contradiction proves the positive-span part of ER3 for every original degree d, without a separate bounded-degree completion.

If F has a single term a x^j, its width is0 and its nonzero integer coefficient satisfies a^2<=q^2.
Algebraic integrality of(a/q)alpha^j, multiplied by the algebraic-integer unit alpha^(-j), makes a/q a rational algebraic integer and hence an ordinary integer.
Thus a=+/-q.
This settles width0 directly without epsilon(0), a norm at a zero value, or a fake positive width.

<a id="scalar-energy-and-real-weight-consequences"></a>
### ER5. Arbitrary scalar support and positive-weight consequences

Let f be ANY rational Laurent polynomial with qf having integer coefficients, NONZERO algebraically integral value f(alpha), and its OWN actual span T satisfying T*m/d<=u_q.
There is no term-count hypothesis on f.
If its energy is at most1, apply ER3 to F=qf; then f is a signed monomial and its energy is exactly1.
Otherwise its energy already exceeds1.
Since q^2||f||_2^2 is an integer, the complete conclusion is

    ||f||_2^2>=1,
    ||f||_2^2=1 if and only if f=+/-x^j,
    f not a signed monomial implies ||f||_2^2>=1+1/q^2. (ER9)

The last phrase includes a one-term polynomial whose coefficient is not+1 or-1.
Large energy is the trivial branch of this proof; the support bound q^2 was used only inside the low-energy contradiction and is not an added final hypothesis.
The conclusion concerns the true polynomial, not a value-equivalent replacement.

For any finite indexed family of such f_i with the SAME coefficient-clearing q, each satisfying its OWN span condition, let omega_i>0 be arbitrary REAL weights with sum_i omega_i=1.
Put E_family=sum_i omega_i||f_i||_2^2 and mu=sum_(i:f_i is not a signed monomial)omega_i.
Summing ER9 yields

    E_family>=1+mu/q^2,
    0<=mu<=q^2(E_family-1).                            (ER10)

Thus E_family=1 forces every indexed atom to be a signed monomial.
No common union-span bound, covariance identity, minimum positive weight, rational-weight denominator or label-count bound is needed.
Real weights enter only this finite linear inequality, with no rational resultant-product assertion attached to them.

<a id="fixed-denominator-window-gap"></a>
Finally, if a nonmonomial integer Laurent F has energy<=q^2, algebraically integral F(alpha)/q including a possible zero value, and0<T=span(F)<=C*d for a fixed C>0, ER3 gives

    T*m/d>u_q,                  m>u_q/C.               (ER11)

The same conditional class can be expressed as a NONZERO rational Laurent polynomial f that is not a signed monomial, with qf integral, energy<=1 and integral value, since the zero-width case was already settled exactly.
This is an all-degree fixed-denominator scalar-class gap, with a potentially enormous q-dependent finite certificate and no numerical improvement asserted.
It neither replaces C93/C95's stronger small-support, denominator-independent constants nor C71's distinct quantitative complementary-packet bounds.
No such scalar certificate is constructed for every actual input, and no unrestricted Mahler gap, covariance statement or general growing-denominator obstruction is claimed.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision scalar-energy-rigidity-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T22:06 |
| status | open |
| reason | Fix the complete ER1--ER11 fixed-q scalar energy theorem and author proof, including arbitrary final support, full algebraic-integral values, the ordered computable dyadic cutoff, variance and finite logarithmic margin, zero exclusion before norms, width-zero branch, own-span positive-real-weight families and all-degree conditional class gap. Separate whole review and adoption remain outstanding; no uniform varying-q or unrestricted Mahler conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete scalar and family statement](#statement) | Entire actual nontorsion integer-unit/full-degree/full-integrality setting, fixed coefficient-clearing q, ordered cutoff and all A--D hypotheses, equality cases, arbitrary-support/individual-span/real-weight quantifiers and limits. |
| argument | [Complete ER1--ER11 argument](#complete-argument) | Full finite q-only construction, endpoint variance, strong concavity, finite Taylor tail, C92 zero branch, original signed norm and raw C137 costs, monomial case, coefficient spacing, positive-weight sum and conditional gap without a low-degree patch. |
| dependency | [Finite logarithmic original-root certificate](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Sections1--2 and equations1--7 only: finite upper log majorant/tail, raw delta/B hypotheses, complete original radial expense, coefficient price2^J, actual domain and nonzero algebraic-integer norm income; no seed-family or bounded-degree completion. |
| dependency | [Short rational annihilator inequality](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Exact zero-value effective-support lower bound at positive actual span, original d and inherited epsilon domain; used before any logarithm of a resultant. |
| dependency | [Exact finite-frequency modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c0,h0,b,epsilon, monotonicity and limit, negative-frequency convention, all original powered-field repetitions and accepted source limits; no infinite-frequency interchange. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T22:18 |
| status | proved |
| reason | Adopt the complete Statement A--D and ER1--ER11 proof after root read the entire author argument, fixed statement and fresh whole independent R1064. The fixed-q variance/regularization margin, exact finite Taylor tail, ordered computable cutoff, zero-before-norm guard, original signed norm and all raw frequency costs, width-zero case, arbitrary-support scalar equality, own-span real-weight consequences and all-degree conditional gap are covered. R1064 preserves the distinction between C95's literal common-dictionary family clause and its own-span scalar consequence. No growing-q uniformity, automatic certificate coverage, numerical improvement or unrestricted Lehmer conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete scalar and family statement](#statement) | Entire actual nontorsion integer-unit/full-degree/full-integrality setting, fixed coefficient-clearing q, ordered cutoff and all A--D hypotheses, equality cases, arbitrary-support/individual-span/real-weight quantifiers and limits. |
| argument | [Complete ER1--ER11 argument](#complete-argument) | Full finite q-only construction, endpoint variance, strong concavity, finite Taylor tail, C92 zero branch, original signed norm and raw C137 costs, monomial case, coefficient spacing, positive-weight sum and conditional gap without a low-degree patch. |
| dependency | [Finite logarithmic original-root certificate](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Sections1--2 and equations1--7 only: finite upper log majorant/tail, raw delta/B hypotheses, complete original radial expense, coefficient price2^J, actual domain and nonzero algebraic-integer norm income; no seed-family or bounded-degree completion. |
| dependency | [Short rational annihilator inequality](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Exact zero-value effective-support lower bound at positive actual span, original d and inherited epsilon domain; used before any logarithm of a resultant. |
| dependency | [Exact finite-frequency modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c0,h0,b,epsilon, monotonicity and limit, negative-frequency convention, all original powered-field repetitions and accepted source limits; no infinite-frequency interchange. |
| review | [Whole independent scalar-energy finding](../audits/reviews/Yin_R_G1064_v1.md#whole-scalar-energy-finding) | Complete Statement A--D and ER1--ER11, six exact bindings, every coefficient/norm/domain/zero/span/algorithm/weight/source comparison boundary; no author development, mutable Draft or substantive repair. |

