---
author: Yin
---

# An exact finite-section barrier for short integer forcing

Date: 2026-10-07.
Bounded direct derivation by the assigned review_matrix_completion AI agent for Yin.
The argument reuses the explicit outer factor of L G0111 and turns its impulse estimate into an exact polynomial variational problem.
No source, computation or novelty claim is involved.

Let P be a real monic polynomial of degree d with |P(0)|=1, no unit-circle root, and M=M(P)>1.
Put m=log M.
For a finitely supported forcing z let Z denote its Laurent Fourier polynomial, and let

    E(Z)=||P(S)^(-1)z||_2^2
        =integral_(unit circle) |Z|^2/|P|^2.

Multiplication of Z by a monomial does not affect E(Z).
The exponent span is its highest exponent minus its lowest exponent after zero coefficients have been omitted.
In the arithmetic application P is the irreducible minimal polynomial of a hyperbolic algebraic unit, and Z has integer coefficients.

<a id="exact-short-forcing-variational-problem"></a>
## The exact optimum before the polynomial degree reaches d

Use the outer polynomial from [L G0111](Yin_L_G0111_v1.md#unit-green-energy-floor):

    O(t)=M product_(|beta|>1)(1-t/beta)
             product_(|beta|<1)(1-conjugate(beta)t),
    f=O/M,   c=f_d,   v=M^(-2).

Then |O|=|P| on the circle, f_0=1 and |c|=M^(-2)<1.
Define f^*(t)=t^d conjugate(f(1/conjugate(t))) and the inner product linear in its first argument by

    <U,V>_w=integral U conjugate(V) |P|^(-2).

The direct constant-Fourier-coefficient proof in L G0111 gives

    f perpendicular to t,...,t^d,
    f^* perpendicular to 1,...,t^(d-1),
    ||f||_w^2=||f^*||_w^2=v,
    <f,1>_w=v,  <f,f^*>_w=c v.                       (1)

Set

    Q_*(t)=(f(t)-c f^*(t))/(1-|c|^2).

Its leading term cancels, its constant term is one, and it is perpendicular to t,...,t^(d-1).
Thus

    deg Q_*<=d-1,   Q_*(0)=1,
    ||Q_*||_w^2=v/(1-|c|^2)
               =1/(M^2-M^(-2))=:B(m).                 (2)

For every complex polynomial Z of degree at most d-1, put b=Z(0).
The polynomial Z-b Q_* has zero constant term, so it is orthogonal to Q_*.
Consequently the exact Pythagorean identity is

    E(Z)=|b|^2 B(m)+||Z-b Q_*||_w^2.                  (3)

In particular,

    min_(deg Z<=d-1, Z(0)=1) E(Z)=B(m),               (4)

and Q_* is the unique minimizer.
Positivity of the circle weight proves uniqueness.
This is an attained finite-section variational equality, not only an estimate for one impulse.
For real P the polynomial Q_* is real, so (4) is also the exact minimum over real polynomials.
Its coefficients are not asserted integral, and its response is not asserted to lie in the open rounding cube.

<a id="integer-span-and-energy-cost"></a>
## Consequence for all integer forcings of span less than d

If Z is a nonzero integer Laurent polynomial of exponent span less than d, shift its lowest exponent to zero.
The resulting polynomial has degree at most d-1 and nonzero integer constant term b, hence |b|>=1.
Equations (3)--(4) give

    E(Z)>=B(m)=1/(2sinh(2m)).                          (5)

This conclusion does not require the open-cube condition or the specified multiplier residue.
It therefore applies, in particular, to every such short forcing that belongs to the relaxed class of [L G0110](Yin_L_G0110_v1.md#relaxed-residue-amplitude-equivalence).
The square-cost residue conversion in that record can enlarge the exponent span; it does not circumvent (5) while preserving short span.

For any fixed C>0, a forcing of span less than d and E(Z)<=C necessarily satisfies

    m>=(1/2) asinh(1/(2C)).                            (6)

Equivalently, whenever 0<m<(1/2)asinh(1/(2C)), every nonzero integer forcing with energy at most C must have exponent span at least d.
This is a restriction on the geometry of a proposed construction, not a proof that such a long forcing exists.
It applies even before testing whether its response lies in the rounding cube.

In particular all binomials 1-t^n with 1<=n<d obey (5).
Their spectral numerator can cancel some peaks, but it cannot have uniformly bounded response energy along any hypothetical hyperbolic integral-unit sequence with m tending to zero.
The statement does not cover delays n>=d.
Nor does it assume such a near-one sequence exists.

Identity (3) identifies the extra arithmetic cost precisely at each fixed input: among short polynomials the continuous optimum is Q_*, and an integer numerator pays its weighted squared distance from b Q_*.
No uniform lower bound for that additional distance, or integral approximation achieving it, has been proved.

<a id="short-binomial-open-cube-control"></a>
## A binomial with a genuine open-cube response outside the target region

The short mechanism is not impossible for all inputs.
Take the actual hyperbolic unit P=t^2-3t+1, with lambda=(3+sqrt5)/2 and beta=lambda^(-1).
The Green sequence retained in L G0107 and L G0111 is

    w_j=-beta^|j|/sqrt5,   P(S)w=delta_(-1).

For z=delta_(-1)-delta_(-2), the Laurent numerator is Z=1-t and the response is e_j=w_j-w_(j+1).
Directly,

    ||e||_infinity=(1-beta)/sqrt5=1/(lambda+1)<1/2,
    ||e||_2^2=2(3-2)/(3^2-4)^(3/2)=2/(5sqrt5)<1.       (7)

For the energy, the geometric sums give ||w||_2^2=3/(5sqrt5) and <w,S w>=2/(5sqrt5), so ||w-S w||_2^2=2(||w||_2^2-<w,S w>) as stated.
Its residue 1-alpha is nonzero, and the forcing is nonzero integral; hence this really belongs to the relaxed open-cube class.
It is not asserted to have the prescribed integral-multiplier residue before the square-cost conversion.

Here f=(1-beta t)^2, c=beta^2, and the exact optimizer is Q_*=1-(2/3)t.
Thus (3) also checks the strict excess of the integer binomial above B(m)=1/(3sqrt5).
The coefficient -2/3 displays the distinction between a real variational minimizer and an integer forcing.
The measure lambda>2 places this entire control outside the near-one target; it is not a counterexample there.

## Scope and actual review

The new restriction is the exact degree-d finite-section optimum and its integer-span consequence, not a new sufficient gap hypothesis.
A uniformly bounded-energy construction near m=0 must use exponent span at least d, regardless of how it later solves the cube or residue constraints.
No statement rules out long sparse forcings, or promises useful energy or rounding margin for them.

The assigned agent checked the reused orthogonality orientations, unique optimum and exact residual identity, integer Laurent shift, energy-to-m conversion, and the genuine quadratic open-cube control.

The coordinator independently read and checked the complete actual (1)--(7), including weighted-projection orientation and uniqueness, real-versus-integer scope, the nonzero lowest Laurent coefficient, the direction of the asinh bound, the exact quadratic cube margin 1/(lambda+1), energy 2/(5sqrt5), optimizer 1-(2/3)t, and the outside-core limitation.
It found no mathematical defect.
It selected the problem and requested scope clarifications, but did not contribute the proof mechanism; this is a complete independent mathematical review.

The assess_shortness_route agent independently read and checked the complete final (1)--(7), including the linear-first inner product, the cross term c v, cancellation of the highest and constant coefficients in Q_*, orthogonality, the exact norm and Pythagorean identity for complex Z, uniqueness, the integer Laurent lowest-coefficient guard, span and asinh quantifiers, and the residue-conversion scope.
It checked both geometric sums in the quadratic example, its exact open-cube margin and energy, Q_*=1-(2/3)t, and B(m)=1/(3sqrt5).
It found no defect and did not treat the continuous optimizer as integral or cube-admissible.

| Review | Relationship |
| --- | --- |
| Assigned-agent derivation checks | self-reviewed |
| Coordinator complete written proof review (1)--(7) | independently reviewed |
| assess_shortness_route complete written proof review (1)--(7) | independently reviewed |

No source, computation, identifier allocation or fixed-material edit was made by the assigned agent or formed part of either review.

Before allocation, ms25_source also independently checked the complete (1)--(7), including the exact weighted optimum, complex Pythagorean identity, integer span and asinh consequences, and the actual quadratic cube, energy and optimizer.
It found no defect.
This is additional complete independent coverage and does not replace the two reviews above.
