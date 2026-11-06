---
author: Yin
---

# Original-input costs for analytic integer damping

Date: 2026-11-05.
Prepared for Yin under the [unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
The witt_moment_compatibility delegate developed the cyclotomic-denominator cost identity, inner/outer and divided-difference controls, and checked the full deductions below.
The coordinating agent proposed the \(P^*/P\) comparison and the all-cyclotomic-denominator cost floor, which the delegate checked and incorporated.
These are author-side development checks, not independent review or a new Claim assessment.

<a id="original-input-damping-scope"></a>
## Scope, retained sources and the actual missing interface

Can an actual original reciprocal integer polynomial supply the integral analytic input of C868 with a nonnegative Poisson expense bounded by a degree-independent constant times its total Mahler measure?
This version tests division by a complete cyclotomic product, normalized inner/outer separation and an actual integer divided difference.
It also retains the exact nonreciprocal comparison proposed by the coordinating agent, whose reciprocal degeneration is decisive.

[L133 v5](Yin_L_G0133_v5.md#integral-rescaling-scope) remains the complete home of the preceding rescaling tests.
Its [integer decimation](Yin_L_G0133_v5.md#integer-decimation-and-cost), [rotation-norm threshold expense](Yin_L_G0133_v5.md#rotation-norm-and-threshold-cost) and [exact-descent boundary](Yin_L_G0133_v5.md#exact-descent-and-parity) are reused without copying their proofs.
Versions v1--v5 remain fixed.
The current comparison continues the same analytic integer-quotient construction and cost question, so it is retained in the same L133 family.

The only analytic-majorant theorem used here is the exact [C868 v1 statement AM1--AM2](../claims/Yin_C_G0868_v1.md#statement), with its [selected assessment](../claims/Yin_C_G0868_v1.md#decision-whole-independent-review-2026-11-05).
Write
\[
 \gamma=\frac{(\sqrt5-2)^2}{50}.
\]
That statement applies to a function holomorphic throughout the open unit disk, with integer Taylor coefficients and constant coefficient one, satisfying
\[
 \log|f(z)|\le\log2+\mathcal P[g](z),\qquad
 g\ge0,\quad g\in L^1(\mathbb T).
 \tag{1}
\]
If a finite coefficient prefix has square energy at least five, then \(\int g\ge\gamma\).
Neither its complete proof nor any later extension is imported or duplicated here.
The C868 assessment belongs to that Claim; none of its existing review coverage is asserted to cover the new deductions in this ledger.

The existing [C4 root contraction](../claims/Yin_C_G0004_v1.md#coefficient-size-tail-control) already supplies the normalized outer polynomial and its exact boundary modulus.
[C296](../claims/Yin_C_G0296_v1.md#endpoint-row-hardy-closure) supplies the actual normalized finite Blaschke setup and coefficient-space conventions.
[C475](../claims/Yin_C_G0475_v1.md#statement) retains its finite compressions and the distinction between a formal inverse near zero and a disk-analytic function.
These adequate mechanisms are not new source inputs.
The corrected total-measure conventions and the existing [Smyth nonreciprocal interface](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number) retain their stated inspection limits.

<a id="cyclotomic-denominator-minimal-cost"></a>
## Division by a cyclotomic product and the exact minimum expense

Let P be a monic polynomial in \(\mathbb Z[z]\), with \(P(0)=1\).
Reciprocity and even degree are not required in this section.
Let A be a monic cyclotomic product with \(A(0)=1\), including the empty product, without assuming \(A\mid P\).
Set
\[
 f=P/A,\qquad
 u(\zeta)=\log|P(\zeta)/A(\zeta)|,\qquad \zeta\in\mathbb T.
 \tag{2}
\]
The finitely many undefined boundary values may be assigned arbitrarily.
The function f is holomorphic in the open disk, and division of Taylor series with \(A(0)=1\) gives \(f\in1+z\mathbb Z[[z]]\).
Zeros of P inside the disk are allowed; C868 does not require f to be zero-free.

All logarithms use their integrable finite-root boundary values, including circle zeros and poles.
Jensen's identity and \(m(A)=0\) give
\[
 u\in L^1(\mathbb T),\qquad \int_{\mathbb T}u=m(P)=:m.
 \tag{3}
\]
For clarity the corresponding Jensen--Poisson identity can be kept exactly.
Let
\[
 I_P(z)=
 \prod_{\substack{P(\alpha)=0\\|\alpha|<1}}
 |\alpha|\frac{1-z/\alpha}{1-\overline\alpha z},
 \tag{4}
\]
with all multiplicities retained.
No root is zero, because \(P(0)=1\).
This finite product is analytic on a neighborhood of the closed disk, has modulus one on the circle and satisfies \(|I_P|\le1\) in the disk.
Since the product of all root moduli is one,
\[
 I_P(0)=\prod_{|\alpha|<1}|\alpha|=e^{-m}.
 \tag{5}
\]
An empty product is one.

Dividing P by \(I_P\) cancels each inside zero and reflects its factor to a zero outside the disk.
Thus \(O=P/I_P\) is a polynomial without an open-disk zero and \(O(0)=e^m\).
Its boundary modulus is \(|P|\).
The finite-root Poisson identity, including the circle-root \(L^1\) passage retained in [L133 v3](Yin_L_G0133_v3.md#integer-prefix-estimate), gives
\[
 \log|f(z)|
 =\mathcal P[u](z)+\log|I_P(z)|
 \le\mathcal P[u](z).
 \tag{6}
\]
At an inside zero the equality is understood with \(\log0=-\infty\).
The denominator A has only circle zeros, so its logarithm contributes its harmonic Poisson value without an additional inner factor.

Define
\[
 g_A=(u-\log2)_+,\qquad
 E_A(P)=\int_{\mathbb T}(u-\log2)_+.
 \tag{7}
\]
Since \(u\le\log2+g_A\), positivity and normalization of the Poisson kernel combine with (6) to prove (1) for this \(g_A\).
It is a genuine nonnegative integrable expense on the same original input.

In fact (7) is the minimum possible expense among all nonnegative \(g\in L^1(\mathbb T)\) satisfying (1) for this f.
Here is the full necessity argument.
As \(r\uparrow1\),
\[
 u_r(\zeta):=\log|f(r\zeta)|\longrightarrow u(\zeta)
       \quad\hbox{in }L^1(\mathbb T).
 \tag{8}
\]
To justify (8), factor P and A.
For each root off the unit circle, its logarithmic factor converges uniformly once r is sufficiently near one.
For a circle root, after rotation the factor is \(\log|1-r e^{i\theta}|\).
Its positive part is bounded by \(\log2\), while for \(r\ge1/2\) and \(|\theta|\le\pi\),
\[
 |1-r e^{i\theta}|\ge\sqrt2\,|\theta|/\pi.
\]
Its negative part is therefore dominated by a constant plus \(|\log|\theta||\), which is integrable.
Dominated convergence gives the required \(L^1\) limit for each circle factor, and the finite signed sum proves (8).

Now let \(\psi\ge0\) be any continuous function on the circle.
Integrating (1) at \(z=r\zeta\), using the symmetry of the Poisson kernel and Fubini, gives
\[
 \int\psi u_r
 \le\log2\int\psi+\int g\,\mathcal P_r[\psi].
 \tag{9}
\]
The finite values of r at which an inside root lies on that radius cause no problem for the integrable logarithm; one may also restrict to r larger than every strictly inside root modulus.
The Poisson integrals of a continuous circle function converge uniformly to that function.
This follows from uniform continuity, total kernel mass one, and the kernel mass outside any fixed angular neighborhood tending to zero.
Thus (8)--(9) imply
\[
 \int\psi(u-\log2-g)\le0
       \quad\hbox{for every continuous }\psi\ge0.
 \tag{10}
\]
An integrable function whose integrals against all such tests are nonpositive is nonpositive almost everywhere.
Indeed, if \(h=u-\log2-g\) had a positive part of positive measure, some set \(\{h\ge\delta\}\), with \(\delta>0\), would contain a compact subset K of positive measure.
Choose an open neighborhood U of K with \(\int_{U\setminus K}|h|<\delta\mu(K)/2\), using regularity and absolute continuity of the integral.
A continuous function with \(0\le\psi\le1\), equal to one on K and supported in U, would then satisfy \(\int\psi h>0\), contradicting (10).
Consequently \(u-\log2\le g\) almost everywhere.
Since \(g\ge0\),
\[
 g\ge(u-\log2)_+\quad\hbox{almost everywhere},\qquad
 \int g\ge E_A(P).
 \tag{11}
\]
Together with the constructed \(g_A\), this proves the exact minimum.

Splitting \(u-\log2\) into positive and negative parts yields the useful cost identity
\[
 \boxed{
 E_A(P)=m(P)-\log2+
             \int_{\mathbb T}(\log2-u)_+.
 }
 \tag{12}
\]
Jensen controls the mean in (3), not the last term of (12).
There is no degree-independent upper bound for that term supplied by this calculation.

A zero-measure control shows why it cannot simply be omitted:
\[
 P=(1+z)^4,\qquad A=1,\qquad m(P)=0,\qquad E_A(P)>0.
 \tag{13}
\]
Indeed \(|P(1)|=16>2\), so the integrand in (7) is strictly positive on a nonempty arc.
This does not refute adaptive choice of A, since in (13) one may choose \(A=P\) and obtain f equal to one.
If A must be an actual cyclotomic divisor and P is irreducible noncyclotomic, however, the only choice is \(A=1\).
Removing the complete actual cyclotomic divisor then supplies no further transformation on the irreducible reciprocal difficulty.
Allowing nondividing A changes the question to a full boundary approximation with exactly the cost (12).
Formal coefficient matching does not establish that approximation; [L133 v2](Yin_L_G0133_v2.md#raw-euler-truncations-not-cauchy) already retains the failure of raw Euler truncations to be boundary-\(L^1\) Cauchy.

<a id="all-cyclotomic-denominators-cost-floor"></a>
## A genuine lower floor for every allowed cyclotomic denominator

Now assume P is monic reciprocal of even degree, with integer coefficients, \(P(0)=1\) and \(m(P)>0\).
Let A be any monic reciprocal cyclotomic product of even degree and constant coefficient one.
Divisibility \(A\mid P\) is still not assumed.
Then
\[
 \boxed{E_A(P)\ge\gamma
       \quad\hbox{for every such }A.}
 \tag{14}
\]

To prove this, write \(f=P/A=\sum c_jz^j\), with \(c_0=1\) and every \(c_j\) integral.
Suppose no finite prefix has square energy at least five.
Then \(\sum_{j\ge0}c_j^2\le4\), so integrality makes f a polynomial.
The polynomial identity \(P=Af\) implies that f is monic with constant coefficient one.
Its degree d is even, because the degrees of P and A are even.
Reciprocal reversal of that identity and \(P^*=P,A^*=A\) give \(f^*=f\).

If f is constant, it is one.
Otherwise every nonzero coefficient has absolute value one: the constant coefficient already contributes one, and any coefficient of absolute value at least two would bring the energy to at least five.
Monicity fixes both endpoint coefficients to be positive one.
All possible energies at most four can now be listed completely.

Energy one gives \(f=1\).
Energy two gives \(f=1+z^d\), with positive even d.
Energy three, by reciprocal symmetry, gives
\[
 f=1+\sigma z^h+z^{2h},
 \qquad h\ge1,\quad \sigma\in\{1,-1\}.
 \tag{15}
\]
For energy four there are exactly two interior nonzero coefficients.
They must form a reciprocal pair, with the same sign, because a single central coefficient would leave an unpaired interior term.
Hence
\[
 \begin{aligned}
 f&=1+\sigma z^k+\sigma z^{d-k}+z^d\\
  &=(1+\sigma z^k)(1+\sigma z^{d-k}),
 \qquad 1\le k<d/2,\quad \sigma\in\{1,-1\}.
 \end{aligned}
 \tag{16}
\]
Every polynomial in this list has all its roots on the unit circle.
For (15), putting \(v=z^h\) gives \(v^2+\sigma v+1\), whose roots are roots of unity.
For (16), each binomial has roots of unity; the signs of its leading coefficients cancel when \(\sigma=-1\).
Thus each listed f is a monic cyclotomic product and \(m(f)=0\).
Together with \(m(A)=0\), the identity \(P=Af\) would give \(m(P)=0\), a contradiction.

Therefore a finite energy crossing exists for every allowed A.
Formula (7) supplies AM1 with cost exactly \(E_A(P)\), so C868 v1 AM2 gives (14).
The proof uses only that selected v1 interface, not a proposed later generalization.

This is a lower bound on the actual analytic expense for every cyclotomic denominator, not an upper bound by the original measure.
To infer a positive original Mahler gap from it one would still need an actual choice of A and a uniform upper estimate \(E_A(P)\le C m(P)\), or another equally effective transfer.
Neither (12) nor (14) supplies that missing upper estimate.

<a id="inner-outer-integrality-control"></a>
## Normalized inner and outer factors lose the required integer coefficients

The exact inner factor (4) has inexpensive normalization \(I_P(0)=e^{-m(P)}\).
The normalized outer polynomial
\[
 Q=e^{-m(P)}\,P/I_P
 \tag{17}
\]
is zero-free in the disk, has \(Q(0)=1\), and obeys
\[
 |Q|=e^{-m(P)}|P|
       \quad\hbox{on }\mathbb T.
 \tag{18}
\]
These are the existing C4 contraction identities, not a new factorization theorem.
The normalization and modulus relation do not make Q an integer polynomial.
Likewise normalizing the inner factor to constant coefficient one does not give integral Taylor coefficients.

For an exact original reciprocal unit control, take
\[
 P(z)=z^2-3z+1,\qquad
 a=\frac{3-\sqrt5}{2}\in(0,1),\qquad m(P)=-\log a.
\]
Its roots are \(a,a^{-1}\), so
\[
 I_P(z)=\frac{a-z}{1-az},\qquad
 e^{-m(P)}P/I_P=(1-az)^2.
 \tag{19}
\]
The first nonconstant coefficient of the last polynomial is
\(-2a=-3+\sqrt5\), which is not an integer.
In the other direction,
\[
 e^{m(P)}I_P(z)=\frac{1-a^{-1}z}{1-az}
             =1-\sqrt5\,z+\cdots.
 \tag{20}
\]
Its first nonconstant coefficient is also nonintegral.
Both identities follow by writing
\(P=(1-a^{-1}z)(1-az)\).
This fixed-positive-measure example tests preservation of the arithmetic property; it is not a small-measure family.

Multiplication by an inner factor cannot reduce the boundary absolute value of an analytic f, while division by it changes the coefficients as in (19).
An inner/outer argument therefore cannot claim the integer energy step of C868 merely from the modulus relations.
C296 and C475 retain the appropriate analytic coefficient and finite-compression facts without identifying their real coefficients with an integer Taylor sequence.

<a id="integer-difference-zero-control"></a>
## An integer divided difference sends a zero input to compulsory positive expense

For every integer \(k\ge3\), take the original monic reciprocal cyclotomic polynomial
\[
 P_k(z)=1+z^{2k},\qquad P_k(0)=1,\qquad m(P_k)=0.
\]
Its value at one is two.
The actual integer divided difference
\[
 D_k(z)=\frac{P_k(z)-P_k(1)}{z-1}
       =\frac{z^{2k}-1}{z-1}
       =1+z+\cdots+z^{2k-1}
 \tag{21}
\]
is holomorphic in the disk, has constant coefficient one and coefficient square energy \(2k\ge6\).
It is therefore an eligible integer input for the energy condition in C868 v1.
Any nonnegative \(g\) supplying AM1 for \(D_k\) has
\[
 \int g\ge\gamma>0.
 \tag{22}
\]
Such a majorant exists, for example the construction (7) applied to the polynomial \(D_k\) with denominator one.
Consequently no bound \(\int g\le C m(P_k)\), with finite C and valid for every original input of this divided-difference construction, is possible.

This is a direct failure on a cyclotomic zero object.
It does not exclude a different construction that first removes such objects and supplies a separate cost proof.
In particular it is not evidence against a transfer restricted to irreducible noncyclotomic inputs.
It shows that integer coefficients, constant coefficient one and a new finite energy crossing alone do not preserve the original Mahler expense.

<a id="reciprocal-ratio-comparison"></a>
## The original reversal ratio recovers a weaker nonreciprocal gap and degenerates on the reciprocal class

Let P again be any monic integer polynomial with \(P(0)=1\), and let
\[
 P^*(z)=z^{\deg P}P(1/z),\qquad
 f=P^*/P,\qquad q=I_P,\qquad b=fq.
 \tag{23}
\]
The ratio f is analytic near zero, with integer Taylor coefficients and \(f(0)=1\).
It may have poles elsewhere in the open disk.
It is therefore not automatically an AM1 input; the argument below uses exact finite Taylor identities instead of asserting full-disk analyticity of f.

Real coefficients imply \(|P^*|=|P|\) on the circle.
A circle zero has the same multiplicity in P and \(P^*\), because inversion there is conjugation.
All circle poles of f are consequently removable.
The zeros of q cancel all its possible inside poles, with the full denominator multiplicities.
Thus b and q are analytic on a neighborhood of the closed disk and have modulus one on its boundary.
In particular
\[
 \|b\|_{H^2}\le1,\qquad \|q\|_{H^2}=1,\qquad
 q(0)=e^{-m(P)}.
\]
Coefficient Parseval then gives
\[
 \|1-q\|_{H^2}^2=2(1-e^{-m(P)})\le2m(P).
 \tag{24}
\]

Suppose \(P^*\ne P\).
Let N be the first positive index where the Taylor coefficient c of f is nonzero.
Then \(N\ge1\), \(c\in\mathbb Z\setminus\{0\}\), and the prefix is
\[
 T_N(z)=1+cz^N.
\]
Let \(S_N\) retain coefficients of degrees zero through N.
Since f and its Taylor prefix agree to order N at zero and q is analytic there,
\[
 S_N b=S_N(T_Nq),\qquad
 T_N-S_N b=S_N(T_N(1-q)).
 \tag{25}
\]
These are finite identities even if the full f has poles inside the disk.
The functions b and \(T_N(1-q)\) belong to \(H^2\), and coordinate truncation is contractive there.
Using \(\|T_N\|_\infty\le1+|c|\), (24)--(25) give
\[
 \sqrt{1+c^2}
 \le1+(1+|c|)\sqrt{2m(P)}.
 \tag{26}
\]

For real \(t\ge1\), the function
\[
 r(t)=\frac{\sqrt{1+t^2}-1}{1+t}
\]
has derivative
\[
 r'(t)=\frac{1+(t-1)/\sqrt{1+t^2}}{(1+t)^2}>0.
\]
Thus \(|c|\ge1\) makes its minimum occur at one.
Equation (26) proves
\[
 \boxed{m(P)\ge\frac{(\sqrt2-1)^2}{8}
              \quad\hbox{when }P^*\ne P.}
 \tag{27}
\]
No original degree, root separation or boundary-\(H^2\) assumption on f was inserted.

This is only a comparison of the inexpensive inner-factor mechanism with the arithmetic energy step.
The existing Smyth bound is stronger and already covers the nonreciprocal domain.
For a reducible monic P with \(P(0)=1\) and \(P^*\ne P\), at least one monic irreducible unit factor is nonreciprocal: otherwise reversing all factors and multiplying their constant signs would give \(P^*=P\).
The retained Smyth statement gives total measure at least \(\log\theta_0\) for that factor, and hence for P.
No new Claim or new coverage is needed for (27).

For every reciprocal P in the original difficult class,
\[
 P^*=P,\qquad f\equiv1,\qquad b=q.
 \tag{28}
\]
There is no first nonconstant coefficient and no energy crossing.
This includes reciprocal inputs with positive Mahler measure.
The mechanism therefore degenerates exactly on the class whose missing transfer it was intended to test.
It is not a proof of an unrestricted original-input reduction to C868.

<a id="original-damping-return-boundary"></a>
## Retained outcome and first missing original-input step

The quotient \(P/A\) keeps full-disk analyticity and integer coefficients, and its exact least AM1 expense is (7).
For positive-measure even reciprocal P, every allowed even reciprocal cyclotomic denominator pays at least \(\gamma\), by the complete low-energy classification and C868 v1.
This identifies a uniform expense floor but supplies no uniform upper comparison with \(m(P)\).
Removing only actual cyclotomic divisors is trivial on irreducible noncyclotomic inputs.

Normalized inner/outer factors keep their exact modulus identities but fail integer coefficient preservation on the explicit quadratic.
The actual integer divided difference (21) creates compulsory positive expense from zero original measure.
The reversal-ratio construction uses the original measure in (24) and recovers a weaker already-covered nonreciprocal bound, while becoming identically one on every reciprocal input.

The missing original-input interface is a concrete transformation that simultaneously retains an integer nontrivial energy crossing and supplies a nonnegative Poisson expense bounded above by \(C m(P)\), with C independent of the actual degree.
The formulas and controls above establish failures of the specified shortcuts, not an impossibility theorem for all other transformations.
No positive sequence approaching zero, arbitrary-input Mahler gap, new nonreciprocal coverage or unrestricted G0001 completion is asserted.

The author checks covered every root multiplicity in (4), the original total-measure normalization, the complete radial \(L^1\) passage and continuous-test necessity argument, the minimum-cost identity, all energies one through four in the denominator floor, the explicit loss of integer coefficients, the divided-difference zero control, and the finite Taylor argument without a false analyticity assumption on \(P^*/P\).
The coordinating agent's two proposed deductions retain their actual contribution relationship.
No native numerical experiment, new external-source inspection or independent review of this ledger is claimed.
