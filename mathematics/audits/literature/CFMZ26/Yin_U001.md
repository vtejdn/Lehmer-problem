---
author: Yin
---

# CFMZ26-U001: exact original collision law and a finite complete-return certificate

<a id="cfmz26-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Cheng, Fang, Ma and Zhang, arXiv:2610.09902v1, 7 October 2026; the [retained original HTML](../../../literature/pdf/CFMZ26/arxiv-v1.html).
Public preprint, with no journal-publication assertion.

Passages: Introduction equations (1.1)--(1.3), Lemma 2.3, Theorem 2.4, Corollary 2.5, Lemma 3.1, Appendix B Lemma B.1, Proposition B.2 and Theorem B.3; Appendix C statements and Appendix D reproducibility description.

Inspection: On 2026-10-26, salem_collision_literature directly checked the exact original-law conversion and the complete proofs of Lemma 2.3, Theorem 2.4, Corollary 2.5, Lemma 3.1 and Appendix B. The main strict-drop proof was read as a separate critical input; this unit does not accept that proof or the quantitative finite certificates. The quantitative source programs and witness arrays have not been executed or verified.


## Exact process and dimension convention

<a id="original-collision-and-energy-dimension"></a>
**Definition.**
Fix the exterior root beta of P(X)=X^4-X^3-X^2-X+1 and r=beta^(-1).
The source also treats the distinct polynomial X^4-2X^3+X^2-2X+1; only its first parameter is used here.
For independent fair signs epsilon_j in {-1,1}, set X_n=sum_(j<n)epsilon_j r^j and let nu_r be the law of the infinite sum.
After merging equal atoms, Q_n=Pr(X_n=X_n')=sum_x Pr(X_n=x)^2, where the prime denotes an independent copy, and Q_0=1.
The source defines rho=lim_n Q_n^(1/n) and G(t)=sum_(n>=0)t^n Q_n.
Its correlation dimension is the energy threshold

    D2(nu)=sup({0} union {s in (0,1): I_s(nu)<infinity}),
    I_s(nu)=integral integral |x-y|^(-s) dnu(x)dnu(y).

These definitions use exact collisions, natural logarithms and the full two-sign law.
There is no counting of approximate equality in Q_n.

Put U_j=(epsilon_j-epsilon_j')/2.
Multiplication by beta^(n-1) and reversal of the iid sequence give exactly

    Q_n=Pr(sum_(j<n)U_j beta^j=0),
    Pr(U_j=0)=1/2, Pr(U_j=+1)=Pr(U_j=-1)=1/4.

Thus source Q_n equals the COMPLETE project p_n, rho=1/R and G(t)=U(t) for the original process in [C_G526](../../../claims/Yin_C_G0526_v1.md#statement).
Sign normalization, reversal and multiplication are bijections and preserve every word probability and multiplicity.
They impose no extra avoidance condition at intermediate times.

## Checked collision-to-dimension interface

Theorem 2.4 gives D2(nu_r)=log(R)/log(beta).
This equality is accepted here at the stated fixed-quartic scope after checking its proof; no general Shannon-to-Renyi equality is used.
For distinct finite atoms the algebraic norm gives separation at least 2(beta-1)r^n/n^2.
Consequently the full near-collision probability at scale r^n is at most a fixed multiple of (1+n^2)Q_n.
This comparison concerns distinct atoms after coincident words are merged.
An energy-shell sum proves convergence for s<log(R)/log(beta).
For the reverse inequality, repeating one exact colliding block yields an energy lower bound growing as (beta^(sk)Q_k)^m whenever beta^(sk)Q_k>1.
These two arguments prove the equality and the equivalence

    R<beta  iff  D2(nu_r)<1  iff  beta^n p_n>1 for some n>=1.

Lemma 3.1 independently identifies Q_n as the Haar integral of the product cos^2(pi y_j) over the companion four-torus.
Expansion of each factor gives coefficients (1,2,1)/4; Haar integration keeps precisely polynomial words divisible by P.
The four first coordinate characters form an integral basis, so their zero relation is equivalent to evaluation at beta being zero.
This is the actual original weighted law, with no new auxiliary probability measure.

## Checked finite supersolution mechanism

<a id="complete-return-supersolution"></a>
**Definition.**
For P=X^4-AX^3+BX^2-AX+1 define

    M(x0,x1,x2,x3)=(x1,x2,x3,-x0+A x1-B x2+A x3),
    e=(0,0,0,1), Z_(n+1)=M Z_n+U_n e,
    L_z(x)=(z^3-Az^2+Bz-A)x0+(z^2-Az+B)x1+(z-A)x2+x3,
    Omega={x in Z^4: |(beta-1)L_beta(x)|<1},
    Omega_J={x in Omega: 0<max_j|x_j|<=J}.

Here A=1,B=-1 for the project quartic.
The source's coordinate map satisfies L_beta(Mx+ue)=beta L_beta(x)+u and is injective, hence Pr_0(Z_n=0)=p_n.
This is an integral coordinate realization, not an assumption equating quotient height with original power-basis height.
The nonnegative characteristic function of the difference law gives Pr_y(Z_m=0)<=p_m for every initial state y.
The complement of Omega is forward invariant and cannot return to zero.

Let F be a finite sign-symmetric subset of Omega_J containing +/-e and closed under all successors that stay in Omega_J.
Extend an even nonnegative w on F by value 1 at zero and at exits from the cube that remain in Omega, and by value 0 outside Omega.
If, for every x in F,

    w(x)>=(t/4)(wtilde(Mx-e)+2wtilde(Mx)+wtilde(Mx+e)),
    c=(t/2)(1+w(e))<1,

then Appendix B proves the COMPLETE original bound U(t)<=1/(1-c).
The proof stops at either the first return or first cube exit, pays every retained exit with terminal value 1, and bounds the remaining return probability by p_(n-k).
Induction on truncated first-stop transforms proves the supersolution comparison.
Induction on truncated generating sums then proves the displayed global bound.
No finite-box killing is substituted for the full process and no unknown tail is set to zero.
This analytic criterion is accepted at the stated scope after the complete selected proof check.

## Concrete unchecked witnesses and exact remaining obligations

For P1 the source's Theorem C.1 asserts U(68883/40000)<105, where 68883/40000=1.722075.
Proposition C.2 supplies 455137 sign representatives at height 180, denominator 2^80, claimed minimum integer residual 2791379258189148576, and initial numerator 181660711014187729550784.
The full state and supersolution arrays are essential evidence; the printed initial numerator or residual alone does not certify their universal inequalities.
The cited verification release is [Zenodo version 1.0](https://doi.org/10.5281/zenodo.23179204), with archive Quartic-Salem-Verification-v1.0.zip.
The API metadata and archive identity were inspected, but the archive and its native checks are not adopted by this unit.
If that certificate is verified, the already adopted recurrence U(R)=infinity in C_G526 upgrades U(t)<infinity to the strict inequality R>t.
No such stronger numerical radius is adopted here before that witness check.

Theorem 1.1 asserts strict correlation-dimension drop for both quartics; Appendix A asserts an explicit upper deficit for P1.
The exact-law conversion above establishes their applicability, but this unit leaves the separate critical proof and quantitative verification obligations explicit.
Neither those radius assertions nor Appendix B classifies the derivative F'(R), the critical first-return mean, or linear growth of the conditioned neutral midpoint.
In particular, the open derivative g'(R) in [C_G785](../../../claims/Yin_C_G0785_v1.md#statement) is not a theorem of this source.

## Bounded search and reuse boundary

The 2026-10-26 search first checked C_G526/C568/C819/C_G785/C836/C837 and the existing Ope26c, Var25, BV20 and Li26 source interfaces.
The earlier Var25 record is a dated statement of an open question; Ope26c's singularity theorem does not itself imply a collision-entropy deficit.
Primary queries combined Salem Bernoulli convolution with collision entropy, Renyi entropy, Lq dimension, local limit theorem and return probability, followed by critical-mean and positive-recurrence variants.
They located this exact fixed-quartic source and its [Shannon sequel](../CFMZ26b/Yin_U001.md#cfmz26b-u001).
No applicable critical-mean or original conditioned-bridge theorem was found in this bounded screen.
That negative outcome establishes neither nonexistence nor novelty.
The decisive continuation is verification of the exact source proof and finite witnesses, rather than replacing the fixed parameter by an almost-everywhere statement or transferring Shannon lower bounds without their entropy-order loss.
