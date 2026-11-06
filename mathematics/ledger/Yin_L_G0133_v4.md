---
author: Yin
---

# Reciprocal cyclotomic quotients: short local limits and persistent boundary separation

Date: 2026-11-05.
Prepared for Yin by the coordinating agent and the assigned three_block agent during the G0001 exploration.
The coordinator proposed the local-compactness test, the zero-free, unit-circle-root route to classifying the limits, and the varying zero-model formulation of the remaining estimate.
The assigned agent checked that route, connected eventual integer-coefficient agreement to exact finite Fourier agreement and the L133 v2 boundary gap, and prepared this account.
This is ordinary joint author-side exploration, not an independent review, an accepted Claim or a new strategy adoption.

<a id="inputs-and-scope"></a>
## Inputs and scope

[L133 v3](Yin_L_G0133_v3.md#three-block-integral) supplies the complete three-block family, its logarithmic-integrability argument and the exact Jensen cost.
Its [integer-prefix estimate](Yin_L_G0133_v3.md#integer-prefix-estimate) supplies the interior Poisson bound and the finite coefficient-energy restriction used here.
[L133 v2](Yin_L_G0133_v2.md#cyclotomic-boundary-log-gap) supplies uniform boundary-log separation for distinct monic cyclotomic products, allowing constant coefficients of either sign, arbitrary degrees and multiplicities.
The present argument connects those two retained results; neither their original proofs nor their actual review scope is replaced or enlarged.
The exact return from a hypothetical positive vanishing-cost sequence to integral reciprocal polynomials remains in [L133 v3](Yin_L_G0133_v3.md#original-polynomial-return) and is not repeated here.

Suppose there were a sequence of the v3 inputs A0_j,B0_j, each monic reciprocal cyclotomic with constant coefficient1 and even degrees 2a_j,2b_j, such that

    f_j=B0_j/A0_j,       epsilon_j=m_2(F_j)>0,
    epsilon_j -> 0.

No such positive sequence is constructed or assumed to be already known.
The following are necessary consequences of this hypothesis, not a proof that it is consistent.
All circle integrals use normalized Haar measure.

<a id="short-local-limits"></a>
## Local compactness and the exact necessary limit candidates

For every 0<R<1 the v3 Poisson bound gives

    sup_(|z|=R)|f_j(z)|<=2exp(epsilon_j(1+R)/(1-R)).          (1)

This is bounded uniformly in j because epsilon_j tends to zero.
Write f_j(z)=sum_(k>=0)c_(j,k)z^k, where c_(j,k) are integers and c_(j,0)=1.
The coefficient bound obtained from (1) and Parseval makes each fixed sequence c_(j,k) bounded, hence valued in a finite set of integers.
A diagonal subsequence therefore makes every fixed coefficient eventually constant.

This diagonal convergence is locally uniform, not just formal.
For 0<r<R<1, a common bound M_R in (1) gives |c_(j,k)|<=M_R R^(-k), so the tails on |z|<=r are uniformly bounded by M_R sum_(k>K)(r/R)^k.
The tail tends to zero as K tends to infinity.
Thus, after relabelling the subsequence, f_j converges locally uniformly to an analytic f_infinity with integer Taylor coefficients and constant coefficient1.
Taking the limit at each point in (1) gives |f_infinity(z)|<=2 throughout the disk.

The limit is also zero-free in the disk, as in Hurwitz's nonvanishing alternative.
In this family that step follows directly from the same Poisson kernel without importing a further source theorem.
Fix 0<r<R<1 and choose a common positive C_R bounding log|f_j| on |z|=R by (1).
Since f_j is zero-free in the disk, log|f_j| is harmonic and has value0 at the origin.
The nonnegative harmonic function C_R-log|f_j| has circle mean C_R on radius R.
The maximum of the radius-r Poisson kernel for that circle is (R+r)/(R-r), so

    log|f_j(z)|>=-2C_R r/(R-r)       for |z|<=r.

The limit is consequently bounded away from zero on every smaller disk.

Parseval and |f_infinity|<=2 give a total coefficient square energy at most4.
Integer coefficients make f_infinity a polynomial.
For a nonconstant such polynomial, every nonzero coefficient has absolute value1, because its constant coefficient already contributes1 and any other coefficient of absolute value at least2 would force energy at least5.
In particular its leading coefficient is1 or -1.
It has no root inside the disk, and the modulus of its root product is the absolute value of the ratio of its constant and leading coefficients, namely1.
Every root therefore lies on the unit circle.

Writing d=deg f_infinity, real coefficients and unit-circle roots imply

    f_infinity*(z)=eta f_infinity(z),
    f_infinity*(z)=z^d f_infinity(1/z),
    eta=leading coefficient of f_infinity,   eta in {1,-1}.

Indeed complex conjugation and inversion preserve the same root multiset, and comparison of constant coefficients fixes eta.
This recovers reciprocal or antireciprocal symmetry of the limit without passing the varying degrees through the limit.

Energy4 would force |f_infinity|^2=4 almost everywhere on the circle.
That is impossible for a nonconstant polynomial with nonzero constant and leading coefficients, since the Fourier coefficient of |f_infinity|^2 at its extreme lag is nonzero.
The only possible constant polynomial here is1.
At energy3, eta=1 forces the trinomial 1+sigma z^h+z^(2h), with sigma in {1,-1}, whose modulus is3 at z^h=sigma.
For eta=-1, antireciprocal symmetry pairs every nonzero coefficient with its negative and forces a central coefficient to vanish, so an odd number of nonzero coefficients is impossible.
Both energy3 cases are therefore excluded.
The complete necessary list is

    f_infinity=1, or f_infinity=1+z^h, or f_infinity=1-z^h,
    where h>=1.                                             (2)

There is no parity restriction on h in this local argument.
Monicity and even degree of the input blocks were not silently passed to the limit.
Conversely, (2) is only a necessary candidate list: it does not establish that the minus sign, odd h, or any candidate at all can arise from a positive sequence epsilon_j->0.
The exact zero-measure inputs from v3 realize some of these local limits, but they do not supply the hypothetical positive sequence.

<a id="exact-fourier-escape"></a>
## Exact finite Fourier agreement with a persistent L1 gap

Put

    u_j(theta)=log|f_j(exp(i theta))|,
    u_infinity(theta)=log|f_infinity(exp(i theta))|.

These are integrable and have mean0.
For u_j this follows from the cyclotomic quotient; for u_infinity it follows directly from (2).
The logarithmic Poisson passage established in v3 applies to both, including all boundary zeros and poles.

Take the analytic logarithms L_j=log f_j and L_infinity=log f_infinity in the disk, normalized to have constant term0.
For each k>=1, the coefficient of z^k in a formal logarithm is determined by the first k Taylor coefficients of its argument with constant coefficient1.
Their eventual equality along the selected subsequence makes these logarithm coefficients eventually equal as well.
For a positive integer k, the kth Fourier coefficient of u_j is half the kth Taylor coefficient of L_j; negative indices are their conjugates and the zeroth coefficient is0.
Consequently, for every fixed integer K>=0 there is j(K) such that

    Fourier_k(u_j-u_infinity)=0
    for all |k|<=K and all j>=j(K).                          (3)

This is eventual exact agreement, rather than only coefficient convergence.

Nevertheless the L1 difference has a fixed positive lower bound.
Choose the monic cyclotomic associate H of f_infinity by

    H=1                if f_infinity=1,
    H=1+z^h            if f_infinity=1+z^h,
    H=z^h-1            if f_infinity=1-z^h.

Each H is a monic cyclotomic product, with constant coefficient1 or -1, and |H|=|f_infinity| on the circle.
Thus A0_j H and B0_j satisfy the actual hypotheses of L133 v2; no even-degree or positive-constant restriction is needed for that two-block result.
They are distinct.
In the first two cases equality would give f_j=f_infinity and hence epsilon_j=0 by the v3 Jensen formula and |f_infinity|<=2 on the circle.
In the third case their constant coefficients are -1 and1, respectively, so equality is impossible.
The positive-sequence hypothesis therefore permits the v2 separation bound for every j:

    ||u_j-u_infinity||_L1
      =norm_L1(log|B0_j/(A0_j H)|)
      >=2log(theta_0)>0,                                    (4)

where theta_0 is the real root greater than1 of t^3-t-1.
This use retains v2's total boundary-log conclusion and its accepted Smyth and fixed-pair Lawton inputs; it asserts neither a new source-proof audit nor a bound on individual factors.

Equations (3)-(4) identify the precise missing boundary control.
Every fixed Fourier window of the residual is eventually zero, but its L1 norm remains bounded below.
Interior normal-family compactness and eventual integer-coefficient stability therefore cannot by themselves give the L1 convergence that would contradict (4).
An additional argument forcing that convergence, or assigning a uniform arithmetic cost to this residual with arbitrarily large Fourier gaps, would be needed to exclude the hypothetical positive sequence.

<a id="pole-free-zero-control"></a>
## Why this failure is not specifically a pole-concentration mechanism

Consider the exact zero-measure inputs

    A0_n=1,       B0_n=1+z^(2n),       f_n=1+z^(2n).

They satisfy the original monic reciprocal, constant1, even-degree cyclotomic hypotheses and have epsilon_n=0 by v3.
They have no poles, converge locally uniformly to1, and have every fixed nonconstant Taylor coefficient eventually zero.
Yet their boundary logarithms have the same absolute-value distribution for every n under the measure-preserving covering z->z^(2n).
Their L1 norms are therefore the fixed positive number norm_L1(log|1+z|), not a sequence tending to zero.
Their logarithms are even uniformly integrable because these distributions agree, so uniform integrability alone does not supply the missing L1 convergence.
Their nonzero Fourier coefficients occur only at multiples of2n, so their discrepancy from the local limit moves outside every fixed Fourier window.

This supplies an exact pole-free illustration of the failure of local compactness to control boundary L1 behavior.
It is not a positive-measure counterexample sequence and does not show that any of the candidates in (2) can occur for epsilon_j>0 tending to zero.
Boundary poles and narrow logarithmic peaks remain possible features of a hypothetical positive sequence, but they are not the only issue identified by the compactness argument.
The quantitatively necessary obstruction is (3)-(4): persistent boundary-log separation beyond every fixed Fourier window.
To accommodate these exact zero controls, a boundary approximation from small nonnegative epsilon must at least allow a varying zero-measure model q_j=1 or q_j=1+z^(2h_j), with h_j>=1, rather than require L1 convergence to one fixed local limit.
If such models could be chosen with norm_L1(log|f_j|-log|q_j|)->0, the v2 gap applied to B0_j and A0_j q_j would force their exact equality for all sufficiently large j, contradicting positive epsilon_j.
No theorem supplying this varying-model approximation is proved here, and the necessary local-limit candidates remain those in (2).
This refines the missing estimate after L133 v3 without producing a uniform Mahler gap, a positive vanishing-measure sequence or a new adopted strategy for G0001.
