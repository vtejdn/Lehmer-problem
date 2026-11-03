---
author: Yin
---

# Complete integral conjugate-hull rigidity and logarithmic costs of rational combinations

This retains the complete necessary mathematical argument from [original complete L399](../ledger/Yin_L_G0399_v1.md#conjugate-hull-statement).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let alpha be a nonzero algebraic integer of original degree d>=1, X its distinct conjugate set, L its normal closure, G=Gal(L/Q), and X_pm=X union(-X) as a set of distinct signed values.
For z in L define q(z)=|G|^(-1)sum_g abs(g(z))^2, using all embeddings with their actual constant fibers.
This is the square norm of a real rational inner product, independent of enlarging the ambient number field; it is not assumed to be a field trace of z times its complex conjugate.
For rational coefficients c_xi put Y=sum_(xi in X)c_xi xi and A=sum abs(c_xi).
If Y belongs to X_pm then A>=1, attained by a single signed vertex.
If Y is a nonzero algebraic integer outside X_pm, then A>=2/q(alpha).
If q(alpha)<2, every nonempty subset Z of X satisfies

    O_L intersect {sum_(xi in Z)c_xi xi: c_xi in Q,
                   sum abs(c_xi)<=1}={0} union Z union(-Z).

There is no additive-independence, representation-uniqueness or integral-output existence claim.
The q=2 endpoint fails in the exact nonunit control alpha=1+i, whose conjugate mean is1 outside X_pm.

If alpha is an integer unit, M=M(alpha), m=log M>=0, then

    q(alpha)<=1+(M-M^(-1))^2/d,
    A>=2/[1+(M-M^(-1))^2/d]

for every new nonzero integral Y.
The strict condition d>(M-M^(-1))^2 therefore suffices for the subset hull equality.
Writing Lambda for the infimum of A over such new integral outputs, one has 2/q(alpha)<=Lambda<=2, with no infimum-attainment assertion.
The upper control is the actual output2alpha.
For bounded M and d tending to infinity, Lambda tends to2.
For genuine Salem roots the two-root output alpha+alpha^(-1) also has coefficient cost2 and is outside X_pm; the radial-square bound is exact there.
The fixed C160 Salem factors for integers n>=16 have d>=n-9 and theta<M<4/3, with measures tending to log theta>0, so they give actual bounded-measure degree growth, without a near-one family or an output-height assertion.

For an integer unit alpha, take k>=2 distinct signed values psi_1,...,psi_k in X_pm, positive rational weights w_i with sum w_i=1, and rational A>0.
Assume Y=A sum_i w_i psi_i is nonzero, and put

    S=sum_(i<j)w_i w_j>0,
    B(m,d)=4(exp(2m)+1)m^2/d-exp(-2m)/2.

For N=[Q(Y):Q], the full own-field norm and absolute logarithmic height satisfy

    (1/N)log abs(Norm_(Q(Y)/Q)(Y))<=log A+B(m,d)S,
    h_abs(Y)>=max{0,-log A-B(m,d)S}.

These bounds hold for every m>=0, including torsion units, without assuming nontorsion pair ratios, independence, an output-degree bound or integrality of Y.
The height uses the primitive integer minimal polynomial with positive leading coefficient and every finite-place cost.
If

    d>=16m^2(exp(4m)+exp(2m)),

then B(m,d)<=-exp(-2m)/4.
For a supplied fixed M0>=1 it suffices that

    M<=M0,
    d>=16(log M0)^2(M0^4+M0^2).

One then has h_abs(Y)>=max{0,S/(4M0^2)-log A}; if max w_i<=1-eta for eta>0, this implies h_abs(Y)>=max{0,eta/(8M0^2)-log A}.
A positive floor requires its displayed expression to be positive; no uniform separation of concentrated weights is presumed.

For every unit with M<=6/5, one has B(m,d)<-1/100: for d>=2 the exact estimate is B<122/625-25/72=-6841/45000, while d=1 is the separate m=0 case.
Thus the normalized logarithmic norm is strictly less than log A-S/100, and h_abs(Y)>S/100-log A.
If Y is additionally integral, log A>S/100 is necessary.
If A<=1 and max w_i<=1-eta, then h_abs(Y)>eta/200-log A.
Signed rational representations must first consolidate identical signed values, preserving A and Y, and compute S for that actual representation.
Combining opposite signs is a different representation that may reduce A and requires its own new S.
The exact cancellation control .5xi-.5(-xi)=xi prohibits assigning the unmerged S=1/4 to a one-value output.
Zero outputs are excluded before logarithms, and a single signed value has no positive pair-loss conclusion.
All six original sections, formulas1--23, complete Hilbert/radial/difference/Jensen/norm proofs, source and comparison boundaries, actual author contributions/checks and remaining limitations are retained below.
The results concern rational linear combinations; they establish no nonlinear exclusion, original Mahler gap or Task/E completion.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:57 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Complete proof](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Gent21 normalized square norm](../audits/literature/Gent21/Yin_U001.md#gent21-u001) | Only full embedding normalization, complete norm AMGM and q(z)>=1 for nonzero integers at actual elementary proof scope; q<2 indecomposability is attribution, not a hull substitute. |
| dependency | [Smy08 full height convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Primitive integer own minimal polynomial, total measure and all finite-place leading-coefficient costs; no lower-bound or questioned resultant input. |
| dependency | [Actual fixed positive-measure Salem family](Yin_C_G0160_v1.md#statement) | Only genuine Salem factors n>=16, original d>=n-9, theta<M<4/3 and retained fixed positive limit; no projection/Fourier theorem or new near-one sequence. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:58 |
| status | proved |
| reason | Adopt the entire exact registered theorem after direct whole SELF inspection of all six retained sections and formulas1--23, all general/unit/weight/own-output domains, full proof and source/contribution/control/remaining boundaries. Preserve original R540 whole UNKNOWN, actual complete original author SELF and original document/review/adoption/source-reading precision; no fresh isolation, native experiment or Task/E resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Exact argument](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact dependency](../audits/literature/Gent21/Yin_U001.md#gent21-u001) | Only full embedding normalization, complete norm AMGM and q(z)>=1 for nonzero integers at actual elementary proof scope; q<2 indecomposability is attribution, not a hull substitute. |
| dependency | [Exact dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Primitive integer own minimal polynomial, total measure and all finite-place leading-coefficient costs; no lower-bound or questioned resultant input. |
| dependency | [Exact dependency](Yin_C_G0160_v1.md#statement) | Only genuine Salem factors n>=16, original d>=n-9, theta<M<4/3 and retained fixed positive limit; no projection/Fourier theorem or new near-one sequence. |
| review | [Exact review](../audits/reviews/Yin_R_G0696_v1.md#complete-conjugate-combination-whole-self-finding) | Entire exact general-integer/unit/original-degree/rational-coefficient theorem, arbitrary-A gates, subset hull, all quantitative norm/height/threshold/consolidation and excluded scopes. Entire original account, six sections and formulas1--23, all positive and negative proofs, accepted sources, controls, author checks/contributions and remaining boundaries. |

## Complete retained argument

<a id="argument"></a>

The original proofs and input descriptions below retain their dated mathematical scope; they supply no Task/E resumption.

Date: 2026-10-18T13:00.
Human author Yin.
Root contributed the convex-mean question, the Hilbert-space coefficient gate, the unit radial-square bound and the initial logarithmic mechanism.
The loglog_cyclic_review author checked the scope, signed-value consolidation, arithmetic interfaces, reuse and unified argument.
The entropy_attainment_bridge author contributed the direct-difference quantitative logarithmic proof retained in Section4.
All three are contributors to this account, not independent reviewers of it.
This is author-level fixed exploration prepared for separate whole review under the continuing G0001 authority; it creates no new Claim or original Mahler-gap conclusion.
No mathematical computation, numerical scan or new field construction is performed.

<a id="conjugate-hull-reuse"></a>
## Reuse, source boundary and why the proposed mechanism fails

The inquiry asked whether varying rational convex combinations of conjugates could produce inexpensive nonzero integral auxiliaries for a small-total-measure unit.
The bounded local screen searched rational means, convex combinations of conjugates, weighted conjugate sums and l1/cross-polytope language in Claims, ledgers and source units, and checked relevant local bibliography leads.
[L318](Yin_C_G0600_v1.md#weighted-integral-bundle-bound) concerns weighted integer auxiliary bundles and aggregate Fourier coherence.
[L357](Yin_C_G0378_v2.md#inverse-symmetric-circle-obstruction) concerns inverse-paired actual-order unit bundles and the original residual projection.
[L372](Yin_C_G0407_v1.md#mixed-unit-reuse-and-domain) uses full norm signs, rational weights and arithmetic/geometric mean for actual relative-unit symbols.
Those inspected accounts do not state the rational conjugate-image result below.
The complete norm, arithmetic/geometric-mean inequality and Hilbert variance identity are standard mechanisms and are not claimed as new.

[Bil97-U001](../audits/literature/Bil97/Yin_U001.md#bil97-u001) is the inspected fixed-function comparison: its stated application fixes the function and arity and assumes multiplicative independence of the input tuple.
This account allows varying coefficients and support and imposes no multiplicative independence.
[Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) supplies the original total-measure and full absolute-height conventions, including the primitive minimal polynomial and its finite-place leading-coefficient cost.
[Gent21-U001](../audits/literature/Gent21/Yin_U001.md#gent21-u001) now supplies the exact classical normalized square norm, common-field fibers, minimum q(z)>=1 for nonzero algebraic integers and the related strict q<2 indecomposability statement.
Its inspected source is van Gent's arXiv:2111.00499v1, especially Lemma7.2, Lemma7.7, Theorem7.9 and Remark7.10 on pages14--15, and Proposition8.1 on page16.
The relevant elementary norm and strict-threshold proofs were actually checked in that source unit; the original Kronecker proof and the paper's main capacity, algorithmic and enumeration results were not audited.
The source's indecomposability concerns a decomposition with nonnegative inner product and is not itself the arbitrary rational convex-hull classification below.
The finite variance deduction and quantitative logarithmic extension remain the local arguments here, with the classical norm input attributed explicitly.
No novelty or priority conclusion follows from the bounded search.

The initial route applied [C159](Yin_C_G0159_v1.md#statement) to nontorsion pair ratios under m<=exp(-40).
An elementary integral-difference argument removed that input and enlarged the explicit range to M<=6/5.
The still simpler Hilbert identity below then showed that the INTEGRAL-output exclusion was already an elementary lattice consequence throughout a much wider domain.
Accordingly the responsible result is retained as one synthesis and unsuccessful construction mechanism, not a new Claim for a purported gap frontier.
The distinct quantitative content is the full logarithmic norm and height cost for NONINTEGRAL outputs with arbitrary varying rational weights.
Neither C159, a cyclic-logarithm estimate, Salem independence nor a rank-dependent height theorem is a proof premise.

<a id="conjugate-hull-statement"></a>
## 1. Exact general hull and coefficient statements

Let alpha be a nonzero algebraic integer of degree d>=1, let X be its set of conjugates, and let L be its normal closure in C.
Write G=Gal(L/Q), O_L for the ring of integers, and

    q(z)=|G|^(-1)sum_(g in G) abs(g(z))^2, z in L.

The associated real inner product is E_G Re(g(z) conjugate(g(t))).
Every own-field conjugate is counted with its constant number of extensions, so q is independent of enlarging the ambient normal number field.
It is not assumed to be a rational field trace of z times its complex conjugate.
Let X_pm=X union(-X), interpreted as a set of distinct signed values.
Every psi in X_pm has q(psi)=q(alpha).
For a rational representation

    Y=sum_(xi in X) c_xi xi,
    A=sum_(xi in X) abs(c_xi),

the following conclusions hold.

* If Y is a signed conjugate, then A>=1, and the bound is attained by its single-vertex representation.
* If Y is a nonzero algebraic integer and Y is not in X_pm, then

      A>=2/q(alpha).                               (1)

* In particular, if q(alpha)<2, then for every nonempty subset Z of X,

      O_L intersect B_Z={0} union Z union(-Z),       (2)
      B_Z={sum_(xi in Z)c_xi xi:
                    c_xi in Q, sum abs(c_xi)<=1}.

No additive independence or uniqueness of representation is asserted.
The zero output is allowed.
The fact that rational coefficients are fixed by all elements of G is required when identifying the algebraic combination with its full embedding vector.

For an INTEGER UNIT alpha, put M=M(alpha), m=log M>=0.
Then

    q(alpha)<=1+(M-M^(-1))^2/d.                     (3)

Consequently d>(M-M^(-1))^2 suffices for (2), and every new nonzero integral output in (1) satisfies

    A>=2/[1+(M-M^(-1))^2/d].                        (4)

If M remains bounded while d tends to infinity, this necessary coefficient cost tends to2.
These are integral-image restrictions, not a positive lower bound for the original m.

<a id="hilbert-coefficient-proof"></a>
## 2. Full elementary Hilbert proof and the unit refinement

Every nonzero algebraic integer z in L has a nonzero integer norm.
Arithmetic/geometric mean on the positive numbers abs(g(z))^2 gives

    q(z)>=abs(Norm_(L/Q)(z))^(2/|G|)>=1.             (5)

This includes all embeddings and retains nonunit norms.
It supplies no requirement that z, a difference or an output be nontorsion.

Replace each nonzero coefficient term by b_i psi_i, with b_i>0 rational and psi_i a signed conjugate, so A=sum b_i and Y=sum b_i psi_i.
Identical signed values may be collected, but collection is not needed for the identity in this section.
If Y is a signed conjugate, the triangle inequality for sqrt(q) gives

    sqrt(q(alpha))=sqrt(q(Y))
                    <=sum_i b_i sqrt(q(psi_i))
                     =A sqrt(q(alpha)),

so A>=1.
The single signed conjugate gives equality.
Now suppose Y is a nonzero algebraic integer outside X_pm.
Every Y-psi_i is a nonzero algebraic integer, and (5) and the exact Hilbert identity yield

    A<=sum_i b_i q(Y-psi_i)
       =(A-2)q(Y)+Aq(alpha).                        (6)

If A<2, rearrange (6) and use q(Y)>=1 to obtain

    Aq(alpha)>=A+(2-A)q(Y)>=2.

If A>=2, the same conclusion follows from q(alpha)>=1.
This proves (1) for arbitrary coefficient mass A, not only for A<=1.

For (2), an integral point of B_Z different from zero and all signed roots of alpha is excluded by (1).
A signed root outside Z union(-Z) must also be excluded, since (1) alone does not do that.
Write an A<=1 representation using signed values in Z union(-Z).
The triangle inequality first gives A>=1 if its output is any signed root, so A=1.
The exact variance identity for those weights is

    sum_i b_i q(Y-psi_i)=q(alpha)-q(Y)=0.

Every summand is nonnegative and every b_i is positive, so every represented value equals Y.
Thus Y belongs to Z union(-Z).
The reverse inclusion of zero and those signed roots is immediate, proving exactly (2).
The same strict-variance argument shows that a positive mean of at least two distinct signed values never equals any signed-conjugate vertex.

For the unit refinement, write a_1,...,a_d for all original radial logarithms.
The unit norm gives sum a_j=0, and the sums of their positive and negative parts are both m.
For x,y>=0 the two functions

    f_+(x)=exp(2x)-1, f_-(x)=exp(-2x)-1

satisfy f_+(x)+f_+(y)<=f_+(x+y) and f_-(x)+f_-(y)<=f_-(x+y).
Indeed the respective differences are (exp(2x)-1)(exp(2y)-1) and (1-exp(-2x))(1-exp(-2y)), both nonnegative.
Applying these inequalities repeatedly to each sign's radial logarithms gives

    sum_j[exp(2a_j)-1]
      <=exp(2m)+exp(-2m)-2=(M-M^(-1))^2.

Since q(alpha)=d^(-1)sum_j exp(2a_j), this proves (3), including m=0.
It also proves (4) and the stated sufficient q(alpha)<2 range.
There is no substitution of small absolute height for bounded TOTAL measure.

The strict threshold q<2 in the general algebraic-integer hull statement cannot simply be changed to q<=2.
For alpha=1+i, the two conjugates have q(alpha)=2 and their rational mean is1, a nonzero algebraic integer different from both signed conjugates.
This direct quadratic example is a boundary check, not a unit counterexample or a numerical experiment.

<a id="coefficient-two-sharpness"></a>
## 3. What coefficient cost two does and does not mean

Let Lambda(alpha) be the infimum of A over rational conjugate representations of all nonzero algebraic integers outside X_pm.
The set is nonempty because 2alpha is such an integer: q(2alpha)=4q(alpha), so it is not a signed conjugate, and its one-term representation has A=2.
Thus

    2/q(alpha)<=Lambda(alpha)<=2.                   (7)

No attainment of the infimum is asserted.
For units of bounded M and unbounded d, (3) and (7) force Lambda(alpha)->2.
This compares arithmetic coefficient cost; it does not construct an output of small height.

For a genuine Salem number alpha>1, the two-root output alpha+alpha^(-1) is also integral and has coefficient mass2.
It is greater than alpha, the house of its signed conjugate set, so it is nonzero and is not a signed conjugate.
Therefore the same limiting upper control remains available even if one insists on an explicitly two-root output.
For Salem inputs the radial population actually gives equality in (3).

There are existing actual bounded-measure Salem families of unbounded original degree in the repository; no hypothetical zero-gap sequence is needed for this cost comparison.
The accepted [C160 family statement](Yin_C_G0160_v1.md#statement), with its L38 inputs, supplies n>=16, a genuine Salem minimal factor of degree d>=n-9, and theta<M<4/3.
Consequently (7) tends to2 along that actual family, with the two-root output just described.
Only those family facts are used, not its projection or Fourier estimates.
Its measures have a fixed positive limit log theta, so this is not a near-one construction or an original-gap conclusion.

<a id="quantitative-combination-statement"></a>
## 4. Full logarithmic norm and height stability for nonintegral outputs

Here alpha is an algebraic integer UNIT of degree d>=1, with arbitrary total m>=0.
Choose k>=2 pairwise DISTINCT signed conjugate values psi_i and positive rational weights w_i with sum1.
Let A>0 be rational and put

    Y=A sum_i w_i psi_i !=0,
    S=sum_(i<j)w_i w_j>0,
    B(m,d)=4(exp(2m)+1)m^2/d-(1/2)exp(-2m).

Then

    log abs(Norm_(Q(Y)/Q)(Y))/[Q(Y):Q]
       <=log A+B(m,d)S,                            (8)
    h_abs(Y)>=max{0,-log A-B(m,d)S}.                (9)

No nontorsion-quotient, fixed-arity, multiplicative-independence, Salem-signature or bounded-denominator hypothesis is imposed.
The value m=0 gives B(0,d)=-1/2.
Under

    d>=16m^2(exp(4m)+exp(2m)),                      (10)

one obtains

    log abs(Norm_(Q(Y)/Q)(Y))/[Q(Y):Q]
       <=log A-(1/4)exp(-2m)S,
    h_abs(Y)>=max{0,(1/4)exp(-2m)S-log A}.          (11)

For any fixed M_0>=1, it is sufficient to assume M(alpha)<=M_0 and

    d>=16(log M_0)^2(M_0^4+M_0^2).                 (12)

Then exp(-2m) in the positive term of (11) can be replaced by M_0^(-2).
If max_i w_i<=1-eta, one has S>=eta/2 and hence

    h_abs(Y)>=max{0,eta/(8M_0^2)-log A}.            (13)

These assertions concern all nonzero outputs, whether integral or not.
The simple Hilbert criterion is stronger for the mere exclusion of new integral points; (10)--(13) do not supply a new integrality coverage class.
Their distinct content is an explicit logarithmic norm and output-height price, uniform over varying supports and coefficients.

### 4.1. Actual radial-square averages

Write a_i(g)=log abs(g(psi_i)), r_i=exp(a_i), and u_i=g(psi_i)/r_i.
Every signed conjugate has the same absolute-value multiset under G, with constant original fibers.
The original positive and negative logarithmic sums both equal m, giving

    abs(a_i)<=m, E_G a_i=0,
    E_G a_i^2<=2m^2/d,
    E_G(a_i-a_j)^2<=8m^2/d.                        (14)

The square-sum bound uses sum x_j^2<=(sum x_j)^2 for each of the nonnegative positive and negative logarithmic parts.
The pair bound follows from (a_i-a_j)^2<=2a_i^2+2a_j^2.
It requires no ratio-degree equality and includes d=1,m=0.

### 4.2. Integer differences and the exact tilted angular loss

For i!=j, psi_i-psi_j is a nonzero algebraic integer.
Applying (5), or applying own-field norm AMGM with the constant fibers, gives

    E_G abs(g(psi_i)-g(psi_j))^2>=1.                (15)

For each g set M_g=sum_i w_i r_i, p_i=w_i r_i/M_g and

    T_g=sum_(i<j)p_i p_j[1-Re(u_i conjugate(u_j))].

Then exp(-m)<=M_g<=exp(m), sum_i p_i=1, and

    abs(sum_i p_i u_i)^2=1-2T_g>0.                 (16)

Positivity follows from Y!=0, since field automorphisms preserve nonzero values.
Each term in T_g is nonnegative.
Rationality fixes A and all weights, so log(1-x)<=-x for 0<=x<1 gives

    log abs(g(Y))<=log A+log M_g-T_g.               (17)

The exact squared-distance identity yields

    T_g=(1/(2M_g^2))sum_(i<j)w_i w_j
          [abs(g(psi_i)-g(psi_j))^2-(r_i-r_j)^2].  (18)

Each bracket equals 2r_i r_j[1-Re(u_i conjugate(u_j))] and is nonnegative.
Thus M_g^2<=exp(2m) may be used BEFORE averaging, without assuming independence of radii and angles.
By the mean-value bound for exp on [-m,m],

    (r_i-r_j)^2<=exp(2m)(a_i-a_j)^2.

Together with (14)--(15) and (18), this gives

    E_G T_g>=[(1/2)exp(-2m)-4m^2/d]S.              (19)

The lower bound may be negative outside the useful range and is not claimed to equal the actual nonnegative expectation.

### 4.3. Radial Jensen expense, own-output norm and finite places

Put abar=sum_i w_i a_i and t_i=a_i-abar.
Then sum_i w_i t_i=0 and abs(t_i)<=2m.
Taylor's formula with second derivative bounded by exp(2m), followed by log(1+x)<=x, gives

    log M_g-abar<=exp(2m)Var_w(a)/2,
    Var_w(a)=sum_(i<j)w_i w_j(a_i-a_j)^2.

Use (14) and E_G abar=0 to obtain

    E_G log M_g<=4exp(2m)m^2 S/d.                  (20)

Combining (17), (19) and (20) proves the upper bound log A+B(m,d)S for E_G log abs(g(Y)).
Every distinct conjugate of Y occurs exactly |G|/[Q(Y):Q] times, so this average is exactly the OWN-field normalized logarithmic norm in (8).
No divisibility or equality between the original degree, output degree and a pair-field degree is assumed.

For full denominator accounting, let a product_(j=1)^N(T-Y_j) be the primitive integer minimal polynomial of Y, with a>0 and nonzero constant coefficient b.
The accepted full-height convention gives

    N h_abs(Y)=log a+sum_j log^+ abs(Y_j),
    N E_G log abs(g(Y))=log abs(b)-log a.

Since abs(b)>=1, these imply

    h_abs(Y)>=max{0,-E_G log abs(g(Y))},             (21)

which proves (9).
The finite-place contribution log a is retained, not replaced by an archimedean-only expression for a possibly nonintegral output.
Condition (10) gives 4(exp(2m)+1)m^2/d<=(1/4)exp(-2m), proving (11).
The nondecreasing functions m^2, exp(2m) and exp(4m) on m>=0 give (12).
Finally S=(1-sum_i w_i^2)/2>=eta/2 under max_i w_i<=1-eta, proving (13).

<a id="small-measure-explicit-output-cost"></a>
## 5. Explicit M<=6/5 consequence and signed-representation boundary

For d>=2 and m<=log(6/5)<1/5, put R=exp(2m)<=36/25.
The coefficient in (8) satisfies the exact strict bound

    B(m,d)=4(R+1)m^2/d-1/(2R)
           <122/625-25/72
            =-6841/45000<-1/100.                   (22)

The strict log(6/5)<1/5 follows from log(1+x)<x at x=1/5.
If d=1, an integer unit is plus or minus1 and m=0, so B=-1/2 and the same final strict bound holds.
Thus throughout M<=6/5, (8)--(9) yield

    E_G log abs(g(Y))<log A-S/100,
    h_abs(Y)>S/100-log A.                          (23)

A nonzero integral output of a genuinely multi-value combination must therefore satisfy log A>S/100.
When A<=1 and max_i w_i<=1-eta, the height consequence is h_abs(Y)>eta/200-log A>=eta/200.
A positive floor is inferred only when the displayed right side is positive.
The stronger general integral-point coefficient gate remains (1), not this small-range consequence.
The constants and the threshold are convenient safe choices; no optimality is asserted.

To use (8)--(23) for arbitrary signed rational coefficients, first omit zero coefficients, write c_xi xi=abs(c_xi) times sign(c_xi)xi, and consolidate IDENTICAL signed values by adding their positive magnitudes.
This preserves Y and A=sum abs(c_xi), and S is computed from the resulting distinct values.
One may instead first combine coefficients modulo +/-; the resulting effective A can only decrease, and its own S must then be used.
These are different valid representations; no representation-independent S is asserted.

For example (1/2)xi-(1/2)(-xi)=xi has A=1 but only one signed value after consolidation.
Using an unmerged S=1/4 would falsely treat a vertex as a genuine two-value mean.
The one-value case Y=A psi has no asserted positive pair loss, and the zero-output case is excluded before logarithms.
Distinct positive-weight original conjugates need no such consolidation, even when some roots are negatives of others.
Rationality is essential to pass the same weights through every field embedding.

<a id="conjugate-combination-conclusion"></a>
## 6. Research consequence and remaining scope

The proposed route of obtaining a new nonzero integer point by inexpensive rational conjugate averaging has an elementary obstruction: q(alpha)<2 already leaves only zero and the signed vertices in the coefficient-l1 unit ball.
For units of bounded M and large original degree, every new nonzero integral output must instead pay coefficient cost approaching2.
The fixed positive-measure Salem family gives an actual sharp asymptotic coefficient control, without producing small output height or a new near-one source.
The general logarithmic bound adds a distinct output-height restriction for NONINTEGRAL combinations, including varying functions, arities, weights and denominators.

No additive independence, nonzero integral-average existence, output-degree bound or original Mahler gap is established.
Coefficients outside the rational fixed-field setting, nonlinear constructions and larger coefficient costs remain outside the stated exclusion.
Weights may concentrate at one value, so no uniform positive height floor follows without the displayed lower control on S or its eta substitute.
Small absolute height does not replace small or bounded TOTAL measure in the radial estimates.
The result explains a failed arithmetic construction mechanism and does not complete G0001 or automatically change its execution state.

## Author checks and review limits

The complete author checks cover norm multiplicities, the Hilbert identity for arbitrary A, the signed-vertex exception, subset hull equality, both radial-log signs, the unit q bound, exact coefficient-cost examples and actual fixed-family scope.
They also cover the direct integer differences, nonzero logarithms, nonnegative brackets before averaging, the shared pair-weight factor, own-output degree, finite-place height, all scalar endpoints and every zero/single-value/consolidation case.
Root, loglog_cyclic_review and entropy_attainment_bridge contributed to this unified argument.
No contributor is an independent reviewer of it, and no independent acceptance is asserted by this author record.
The accepted source and comparison records retain their actual inspection limits.

<a id="conjugate-combination-fixed-inputs"></a>
## Fixed inputs and comparison scopes

| Role | Fixed target | Exact use |
| --- | --- | --- |
| Source input and attribution | [Gent21-U001](../audits/literature/Gent21/Yin_U001.md#gent21-u001) | Normalized q, common-field multiplicities and q(z)>=1 for nonzero algebraic integers, with its inspected elementary proof; q<2 indecomposability is related scope only, not a substitute for the local convex-variance proof. |
| Height convention | [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Original TOTAL measure, primitive integer minimal polynomial and the full absolute-height formula, including finite places for nonintegral Y; no external lower-bound theorem is invoked. |
| Actual family input | [C160 statement](Yin_C_G0160_v1.md#statement) | Only the accepted genuine Salem factors for n>=16, original degree d>=n-9 and theta<M<4/3 in the actual coefficient-cost sharpness control; no projection or Fourier conclusion is used. |
| Fixed-function comparison | [Bil97-U001](../audits/literature/Bil97/Yin_U001.md#bil97-u001) | Fixed arity/function and multiplicatively independent tuple application, compared with the variable-weight/support assertion; no source theorem from it proves the present bounds. |
| Superseded angular comparison | [C159 statement](Yin_C_G0159_v1.md#statement) | Earlier pair-ratio route needed nontorsion quotients and m<=exp(-40); the final argument removes this premise and does not invoke any angular estimate. |
| Local bundle comparison | [L318 bundle bound](Yin_C_G0600_v1.md#weighted-integral-bundle-bound) | Weighted integer auxiliary/Fourier-coherence scope, distinct from rational averaging of conjugate values. |
| Local inverse-pair comparison | [L357 circle obstruction](Yin_C_G0378_v2.md#inverse-symmetric-circle-obstruction) | Actual-order inverse-unit bundles and residual projection scope; no inference of the present hull classification. |
| Local norm/weight comparison | [L372 reuse and domain](Yin_C_G0407_v1.md#mixed-unit-reuse-and-domain) | Relative-unit symbols, full norms and rational weights; acknowledges the reused elementary norm/AMGM method without claiming those records already state this deduction. |
