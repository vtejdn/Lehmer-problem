---
author: Yin
---

# A degree-free Green-energy barrier and its forcing boundary

The current complete mathematical proof is retained in [C308](../claims/Yin_C_G0308_v1.md#argument).
The original mathematical text below remains the fixed old input,with its original date and exact old review bindings.

Date: 2026-10-07.
Bounded direct derivation by the assigned review_matrix_completion AI agent for Yin.
This note tests the analytic cost of the Green inverse in the exact defect classification of [L G0107](Yin_L_G0107_v1.md#rounded-defect-residue-class).
No source, computation or novelty claim is involved.

Let P be a real monic polynomial of degree d>=1 with |P(0)|=1 and no root on the unit circle.
Write M=M(P)>1 and m=log M.
Its coefficients need not be integral for the first analytic theorem.
On bilateral square-summable sequences use (Sx)_j=x_(j+1), and let delta be any unit impulse.
Since P has no circle zero, P(S) is invertible on l2.
Fourier isometry gives the impulse energy

    E_P=||P(S)^(-1)delta||_2^2
       =integral_0^1 |P(exp(2pi it))|^(-2) dt.          (1)

The location of the impulse does not change its energy.

<a id="unit-green-energy-floor"></a>
## A sharp-order lower bound depending only on Mahler measure

The direct bound is

    E_P>=1/(M^2-M^(-2))=1/(2sinh(2m)).                (2)

In particular, E_P>=(1+o(1))/(4m) as m decreases to zero, in the conditional sense of applying to any sequence of polynomials in this domain.
No existence of an integral near-one sequence is asserted.

Here are the outer factor and every normalization needed for (2).
List all roots beta with multiplicity, and define

    O(z)=M product_(|beta|>1)(1-z/beta)
             product_(|beta|<1)(1-conjugate(beta)z).

On the unit circle, |O|=|P|, and O has no zero on the closed disk.
Moreover O(0)=M.
The product of the moduli of all roots is |P(0)|=1, so the inside-root product is M^(-1).
Consequently the leading coefficient satisfies |O_d|=M^(-1).
The conjugate pairs make O a real polynomial, although the proof below permits complex coefficients in O.

Set f=O/M, c=f_d, and use the conjugate reversal

    f^*(z)=z^d conjugate(f(1/conjugate(z))).

Then f_0=1, |c|=M^(-2), f^*_0=conjugate(c), and f^*_d=1.
Define a weighted inner product linear in its first argument by

    <u,v>_w=integral u(z) conjugate(v(z)) |O(z)|^(-2) dt,
    z=exp(2pi it).

Because 1/O is analytic on a disk larger than the closed unit disk, its power series is absolutely convergent there.
Taking constant Fourier coefficients therefore proves

    <f,z^j>_w=0          for 1<=j<=d,
    <f^*,z^j>_w=0        for 0<=j<=d-1,
    ||f||_w^2=||f^*||_w^2=M^(-2)=:v,
    <f,1>_w=v.                                        (3)

For example, the first integrand simplifies to z^(-j)/(M conjugate(O(z))), whose Fourier powers are strictly negative.
The second simplifies to z^(d-j)/(M O(z)), whose powers are strictly positive.
This proves the two orthogonality assertions with their exact orientations.

Put g=f-c f^*.
Its degree is at most d-1, and g_0=1-|c|^2.
Since the constant coefficient of f^* is conjugate(c), (3) gives <f,f^*>_w=c v.
Thus

    ||g||_w^2=v(1-|c|^2),
    <g,1>_w=v.                                        (4)

Cauchy--Schwarz applied to (4) yields

    v^2<=v(1-|c|^2)||1||_w^2
           =v(1-|c|^2)E_P.

Substituting v=M^(-2) and |c|=M^(-2) proves (2).
This is a finite weighted-polynomial calculation, not an imported prediction or Toeplitz-limit theorem.
Hyperbolicity ensures the inverses and the strict |c|<1 domain; for a monic constant-unit polynomial the absence of circle roots also excludes M=1.

<a id="quadratic-green-energy-control"></a>
## An exact integral control outside the small-measure region

For each integer T>=3 take

    P_T(t)=t^2-Tt+1,
    lambda=(T+sqrt(T^2-4))/2,
    beta=lambda^(-1).

This is an irreducible hyperbolic monic unit polynomial: T^2-4 lies strictly between (T-1)^2 and T^2 for T>=3.
Its Mahler measure is lambda>2.
Direct substitution in the recurrence gives

    w_j=-beta^|j|/sqrt(T^2-4),
    P_T(S)w=delta_(-1).

Indeed the recurrence vanishes except at the crossing j=-1, where T-2beta=sqrt(T^2-4).
Summing the geometric squares gives

    E_(P_T)=(1+beta^2)/[(T^2-4)(1-beta^2)]
           =T/(T^2-4)^(3/2),
    1/(M(P_T)^2-M(P_T)^(-2))
           =1/[T sqrt(T^2-4)].                         (5)

The ratio of the exact energy to (2) is T^2/(T^2-4), tending to one as the integer T tends to infinity.
Thus the multiplicative constant one in (2) cannot be increased uniformly over this integral hyperbolic-unit domain.
This sharpness control lies at large Mahler measure, and does not establish sharpness as m tends to zero.

<a id="forcing-numerator-and-rounding-boundary"></a>
## Why impulse energy is not an admissible-defect energy bound

For any nonzero finitely supported forcing z, choose a Laurent polynomial Z representing its Fourier transform; its exponent orientation and any monomial shift do not affect the modulus integrals.
Then

    ||P(S)^(-1)z||_2^2
        =integral |Z(exp(2pi it))|^2/|P(exp(2pi it))|^2 dt.  (6)

The numerator is essential.
It may suppress precisely the circle regions where |P| is small.
For example, z=P(S)delta is a nonzero finite integer forcing when P is integral, and its response is exactly delta with energy one.
This forcing has zero residue in the L G0107 quotient and violates the strict rounding cube.
It is deliberately not an admissible nonzero multiplier example.
The numerator can cancel the denominator completely; the impulse proof of (2) supplies no lower bound of that form for general Z.
This example by itself is not a counterexample to every possible extension of (2).

There is a weaker bound that does apply to every nonzero integer forcing.
Clear a monomial from Z and let M(Z) denote its usual polynomial Mahler measure.
Jensen's circle identity and the arithmetic/geometric mean inequality give

    ||P(S)^(-1)z||_2^2>=M(Z)^2/M(P)^2>=M(P)^(-2).       (7)

The first inequality allows circle zeros of Z: their logarithmic singularities are integrable.
The second uses the nonzero integral leading coefficient of Z and its root factorization.
Consequently, for an actual rounded integral trace defect e_theta=P(S)^(-1)z_theta of L G0107,

    ||e_theta||_2^2>=M(P)^(-2),
    c_P(theta)=product_j cos(pi e_(theta,j))
                 <=exp[-pi^2/(2M(P)^2)].               (8)

The cosine factors are positive because every |e_(theta,j)|<1/2, and the logarithmic bound is applied first to finite products and then to their convergent limit.
This is another upper cap on Fourier amplitude, not a positive lower bound on that amplitude.
It may be combined with the previously retained coefficient- and circle-norm caps by taking the minimum.

In particular, M(P)<=2 implies c_P(theta)<=exp(-pi^2/8)<1/2, uniformly over all nonzero integral multipliers.
The strict numerical comparison already follows from pi>3 and log2<1.
This applies on the small-measure target interval without selecting a short polynomial multiple or estimating its coefficient norm.

There is a direct consequence for the exact envelope in [L G0109](Yin_L_G0109_v1.md#optimizing-convolution-fourier-tests).
That record proves that k^2 g(c^k) is nonincreasing in the positive integer k whenever 0<c<=1/2.
Taking the supremum in (8) over integral multipliers therefore shows, throughout the hyperbolic unit domain M(P)<=2,

    sup_(k>=1) k^2 g(c_opt(P)^k)=g(c_opt(P)).            (9)

Thus k=1 is already the strongest test in that particular convolution-Fourier upper envelope, over the entire stated target interval.
This closes that specific optimization possibility, not all uses of convolution measures or all possible entropy-deficit estimates.
It still supplies no positive lower estimate for c_opt(P), and no Mahler gap.

The actual admissible class is still exactly

    Phi(z) in 2P'(alpha)O_K minus {0},
    ||P(S)^(-1)z||_infinity<1/2,

as proved in L G0107.
Neither (2) nor (7) produces a forcing satisfying these two conditions with bounded response energy.
Nor does (2) establish that every such response has energy of order 1/m: the admissible numerator can depend on P and cancel its spectral peaks.
The established restriction is that a single uncorrected Green impulse already has diverging l2 cost in any hypothetical near-one sequence, whereas cancellation and arithmetic residue conditions remain additional work for any rounding or short-forcing construction.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0032_v1.md#contribution-and-actual-review), with its original inspected scope and relationship.
