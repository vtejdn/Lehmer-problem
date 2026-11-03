---
author: Yin
---
# A three-rotation determinant screen before the two-shear grid

Root authors this additional analytic screen before any J102 calculation is run.
The changed arithmetic family was adopted in [C157v3](../../../claims/Yin_C_G0157_v3.md#decision-whole-reviewed-2026-10-18), through its complete R541 review, before either finite determinant screen was run.
This record supplies a circle comparison, not an original-field integrality theorem.
The original finite grid remains the fallback only when this screen does not decide the input.

## Reuse and the changed first stage

The accepted [C157v2](../../../claims/Yin_C_G0157_v2.md#statement) and [J101](../Yin_J_G0101/record.md#two-set-correction) control a different one-shear form.
[The original Schur comparison, retained in C587](../../../claims/Yin_C_G0587_v2.md#schur-residual-screen) permits the previously retained F component to change its effective coefficient through cross terms, but does not give the determinant comparison below.
A bounded local search for three rotations, circle Hadamard bounds and residue determinants found no matching complete screen in the existing G-line C/L/D materials.
The finite Hadamard inequality and residue-class Fourier decomposition are standard elementary tools; no novelty is claimed.

<a id="three-rotation-screen"></a>
## Exact analytic statement

Let E,F_0,G be the original centered real Laurent polynomials for one fixed reciprocal input, with their actual denominators72,800,30375.
Let mu be normalized circle Haar measure, omega=exp(2pi i/3), and put

    V(z)=[ E(z)          F_0(z)          G(z);
           E(omega z)    F_0(omega z)    G(omega z);
           E(omega^2 z)  F_0(omega^2 z)  G(omega^2 z) ].

For any real s,t, any real q>0 and b>=2, define

    B(z)=q(E(z)+sG(z))^2+q^(-1)(F_0(z)+tG(z))^2+bG(z)^2.

If det V is not identically zero, then

    integral log B dmu
       >=(log2+2 integral log abs(det V) dmu)/3.       (1)

Indeed multiply each row of V by the same real matrix that maps (E,F_0,G) to

    (sqrt(q)(E+sG), (F_0+tG)/sqrt(q), sqrt(b)G).

This matrix has determinant sqrt(b), and its three squared row norms are B(z),B(omega z),B(omega^2 z).
The finite Hadamard inequality therefore gives their product at least b abs(det V(z))^2.
One elementary proof is Gram--Schmidt on the three rows: the absolute determinant is the product of orthogonal residual lengths, each no greater than the original row length; dependent rows make the determinant zero.
Taking logarithms outside the finite zero sets and integrating gives three identical left integrals by Haar rotation invariance.
Use b>=2 to obtain (1).
All logarithms are integrable: G is a nonzero Laurent polynomial and B>=2G^2, while a nonzero Laurent determinant has only finitely many circle zeros with finite multiplicity.
The screen is inconclusive when det V is identically zero; no logarithm of that zero polynomial is taken.

## Exact rational reduction to one ordinary integer polynomial

Write the three centered functions as f_j(z)=sum_n c_(j,n)z^n, and decompose every integer exponent, including negative ones, uniquely as n=3k+r with r in{0,1,2}.
Set

    R_(j,r)(u)=sum_k c_(j,3k+r)u^k,
    W(u)=det [R_(j,r)(u)]_(j=1,2,3;r=0,1,2).

The exact matrix factorization is

    V(z)=D_omega diag(1,z,z^2) R(z^3)^T,
    (D_omega)_(ell,r)=omega^(ell*r).

The three-by-three Vandermonde determinant has absolute value3sqrt3, so

    abs(det V(z))=3sqrt3 abs(W(z^3)) on the circle,
    integral log abs(det V) dmu=(3/2)log3+m(W).        (2)

The monomial z^3 has modulus one, and z to z^3 preserves normalized Haar measure.
There is no assertion that W is monic or integral.

For the actual fixed defects let L=972000 and instead form the residue matrix of the INTEGER Laurent polynomials

    L E=-13500 z^(-3d)H23,
    L F_0=-1215 z^(-5d)H25,
    L G=-32 z^(-15d/2)H35.

Its determinant is L^3 W.
Strip its least Laurent power to obtain a nonzero ordinary integer polynomial K with nonzero constant coefficient.
No content or leading coefficient is discarded.
Then m(W)=m(K)-3log L, and (1)--(2) give the explicit bound

    I_(s,t,q,b)>=log3+[log2+2m(K)-6log L]/3.          (3)

Consequently a certified

    m(K)-3log L>=log2-(3/2)log3                       (4)

excludes I<log2 for ALL real s,t,q>0 and b>=2 on this one original input.
A failure of (4) supplies neither a successful parameter nor an attained minimum.
This whole-family circle comparison does not enlarge the rational domain of any algebraic norm theorem.

## Declared finite evaluation and fallback

The first stage uses exactly the same two J97 inputs already declared in the J102 entrance.
Construct the three integer centered Laurent polynomials, all nine residue polynomials and their six-term determinant by exact integer arithmetic.
If the determinant vanishes identically, report that exact failure and proceed to the already declared finite grid for that input.
Otherwise certify the complete Mahler measure of K by squarefree factorization and all distinct complex root balls, retaining every multiplicity and the exact leading coefficient.
Use256-bit working precision with at most one512-bit escalation, a1e-30 root-radius target and a300-second bound per input.
Propagate outward balls through (3) and compare the lower bound with log2 and the operational log2-1/16 target.
If (4) is certified, the whole two-shear family is excluded below log2 on that input and its fallback parameter grid is not run.
If the weaker lower bound is certified strictly above log2-1/16, the operational target is already excluded for the whole family and that input likewise does not proceed to a parameter grid; this weaker finding does not exclude every positive Haar saving.
If neither comparison succeeds within these limits, the existing finite grid and selected-witness protocol applies only to surviving inputs.
The independent checker must reconstruct the exact residue determinant separately and check all root counts, coefficient/scalar bindings and reported comparisons.
The completed [actual finite results](readme.md#certified-results) now certify both determinant screens and their independent reconstructions.
Both inputs stop before the fallback grid: the quartic misses the operational1/16 target, while Lehmer cannot achieve any positive Haar saving in this family.
No parameter samples or direct integrals were evaluated; the finite computation used only the declared exact determinants and complete-root Jensen certificates.
