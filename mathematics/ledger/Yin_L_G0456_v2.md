---
author: Yin
---

# Chebyshev rounding and the complete binary-product correction test

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The construction agent developed the signed binary-product correction, its exact formula and the bounded computation, and assembled this account.
The coordinating agent supplied the four-pair modulo-two screen.
The bottleneck-diagnosis contributor supplied and checked the complete cyclotomic-degree argument and the factorwise return through the accepted binary theorem.
The assembling agent checked those formulas and the original-degree accounting.
These are ordinary author-development contributions and checks, not an independent project review or a new Claim assessment.

<a id="binary-product-revision-scope"></a>
## Retained inputs and the changed construction

[V1](Yin_L_G0456_v1.md#chebyshev-rounding-scope-and-reuse) remains fixed.
Its [complete Chebyshev rounding calculation](Yin_L_G0456_v1.md#nearest-chebyshev-integer-rounding), [positive real target](Yin_L_G0456_v1.md#positive-real-target-cyclotomic-rounding), [bounded-energy repair](Yin_L_G0456_v1.md#bounded-energy-integer-repair) and [six-term endpoint-kernel completion](Yin_L_G0456_v1.md#integer-endpoint-kernel-correction) retain their complete arguments and limits.
This version does not duplicate those proofs.
The present correction replaces the constant endpoint-kernel coefficient by a changing binary-product sign pattern.
Its natural cyclotomic completion has a growing number of terms, so the particular six-term argument no longer applies.
The question is whether this different actual integer output can have positive total logarithmic Mahler measure tending to zero.

The complete source scope of [L454](Yin_L_G0454_v1.md#arithmetic-realization-scope) and the accepted [DS17 support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001), as applied through [C221](../claims/Yin_C_G0221_v1.md#controlled-entropy-completion), remain as recorded in v1.
They motivate the construction but supply no automatic all-parameter exclusion of the new family.

The new exclusion instead uses [C864 v2 Part A](../claims/Yin_C_G0864_v2.md#statement), the already selected original-window theorem for a supplied reflected binary auxiliary with at most four pairs.
[C139's equation (15)](../claims/Yin_C_G0139_v1.md#argument) identifies the exact dependence of its auxiliary constant on the original-degree window.
The accepted [Kronecker normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) identifies the zero-measure factors.
These inputs retain their existing mathematical and source-review scopes.
No general Lehmer conclusion is inferred from their application to this one construction.

<a id="binary-product-correction-construction"></a>
## Exact construction and positive measure

Retain C_j(t)=2T_j(t/2) for j>=1 and the integer second-kind polynomials
\[
 S_0(t)=1,\qquad S_1(t)=t,\qquad
 S_j(t)=tS_{j-1}(t)-S_{j-2}(t).
\]
Use the exact identities
\[
 C_j(z+z^{-1})=z^j+z^{-j},\qquad
 S_j(z+z^{-1})=\sum_{\nu=0}^{j}z^{j-2\nu}.
 \tag{B1}
\]

The parameter domain is
\[
                         r\ge2,\qquad k=2^r,\qquad a=k/2.
\]
Define
\[
 B_r(s)=\prod_{i=0}^{r-1}(1-s^{2^i}),\qquad
 E_r(s)=B_r(s)+2s^a-2s^{a+1}
       =\sum_{j=0}^{k-1}\varepsilon_js^j.
 \tag{B2}
\]
Every coefficient of B_r is 1 or -1: binary expansion gives one choice of factors for each exponent j from 0 to k-1, with sign (-1) raised to the number of selected factors.
The coefficients at a and a+1 are respectively -1 and 1.
The modification in (B2) reverses these two signs, so every epsilon_j is still 1 or -1.
Both indices lie in [0,k-1] because r>=2.

Put
\[
 Q_r(t)=C_{2k}(t)-\sum_{j=0}^{k-1}
                  \varepsilon_jS_{2k-1-2j}(t),\qquad
 P_r(z)=z^{2k}Q_r(z+z^{-1}).
 \tag{B3}
\]
All second-kind indices in (B3) are positive.
The polynomial Q_r is monic integral of degree 2k, since the correction has degree at most 2k-1.
Consequently P_r is monic reciprocal integral of degree 4k, with constant coefficient one.

The factor (1-s)^r divides B_r(s).
For r>=2, equation (B2) therefore gives
\[
 E_r(1)=0,\qquad E_r'(1)=-2.
\]
Since S_m(2)=m+1,
\[
 \begin{aligned}
 Q_r(2)
 &=2-\sum_j\varepsilon_j(2k-2j)\\
 &=2-\bigl(2kE_r(1)-2E_r'(1)\bigr)=-2.
 \end{aligned}
 \tag{B4}
\]
Thus Q_r has an actual real root greater than 2, by its monicity and the intermediate value theorem.
The reciprocal quadratic belonging to that trace root has an exterior root, and
\[
                            m(P_r)>0.                 \tag{B5}
\]
This positive-measure statement requires no irreducibility assumption.

For r>=4, the factor (1-s)^r also makes the first three moments of the coefficients of B_r vanish.
The recurrence in (B1) gives
\[
 S_m'(2)=\frac{m(m+1)(m+2)}6,\qquad C_{2k}'(2)=4k^2.
\]
These identities follow by differentiating the recurrence, with the displayed initial values.
Applying them to (B3), the binary-product part contributes zero and the two modified signs contribute 2(k-1)^2.
Hence
\[
                        Q_r'(2)=4k^2-2(k-1)^2>0
                        \qquad(r\ge4).                \tag{B6}
\]
This favorable endpoint derivative does not control the total escape of the remaining roots.

<a id="binary-product-exact-completion"></a>
## Full polynomial and its growing natural completion

Equation (B1) gives the exact full polynomial
\[
 P_r(z)=z^{4k}+1-
        \sum_{j=0}^{k-1}\varepsilon_j
        \sum_{\nu=0}^{2k-1-2j}z^{4k-1-2j-2\nu}.
 \tag{B7}
\]
Multiplying each finite geometric sum by z^2-1 yields
\[
 \begin{aligned}
 (z^2-1)P_r(z)
 ={}&z^{4k+2}-z^{4k}+z^2-1\\
   &-\sum_{j=0}^{k-1}\varepsilon_j
        \bigl(z^{4k+1-2j}-z^{2j+1}\bigr).
 \end{aligned}
 \tag{B8}
\]
The four even exponents and the two groups of k odd exponents are pairwise disjoint.
Every displayed coefficient is nonzero.
Thus this particular cyclotomic completion has exactly 2k+4 terms.
This does not claim that every other cyclotomic completion has growing support.

For a useful closed form, put
\[
                  R_r(z)=\prod_{i=1}^{r-1}(1-z^{2^{i+1}}).
\]
Reciprocity of the product B_r gives
\[
 B_r(s^{-1})=(-1)^rs^{-(k-1)}B_r(s).
\]
Using B_r(z^2)=(1-z^2)R_r(z) in (B8), and then inserting the two modified coefficients, gives
\[
 \boxed{
 P_r(z)=z^{4k}+1
       -z\bigl(1-(-1)^rz^{2k+2}\bigr)R_r(z)
       -2\bigl(z^{3k-1}+z^{k+1}\bigr).}
 \tag{B9}
\]
The two modified signs can alternatively be checked through
S_m-S_{m-2}=C_m at m=k-1.
Formula (B9) retains the entire output, not just its exterior real root.

<a id="binary-product-finite-computation"></a>
## Bounded exact construction and whole-measure diagnostics

The native program and reproducible outputs are retained in [J139](../computations/programs/Yin_J_G0139/readme.md).
The exact constructions (B7) and (B9), reciprocal symmetry, P_r(1)=-2, the eight-term modulo-two auxiliary below, and its exact multiplicity at one were checked for r=2,3,4,5,6,7.
The program also multiplies every completed exact factorization back into the input.

For r=2 through 6, SymPy factor_list completed the following exact factorizations.
For r=7 an initial factorization attempt was stopped without a result; the retained bounded program does not repeat it.
Its completed numerical calculation uses full-polynomial shifted FFT integrals.

| r | deg P_r | Completed factorization | Whole logarithmic measure diagnostic |
| --- | --- | --- | --- |
| 2 | 16 | Phi_6 times one irreducible degree-14 noncyclotomic factor | 0.3016217691 |
| 3 | 32 | One irreducible factor | 0.6481143071 |
| 4 | 64 | One irreducible factor | 0.9091520618 |
| 5 | 128 | One irreducible factor | 1.1067986808 |
| 6 | 256 | One irreducible factor | 1.2994745332 |
| 7 | 512 | No completed factorization | Shifted integrals 1.4565018718 and 1.4563868759 |

The r<=6 displayed measures use all noncyclotomic factors and their multiplicities with double-precision roots; exact cyclotomic factors contribute zero.
The program additionally records two direct circle-integral diagnostics for each such input.
The r=7 numbers use respectively 262144 and 1048576 offset samples of the full polynomial.
All floating values lack certified error bounds.
They are not accepted numerical inequalities, counterexamples, or proof inputs for the all-parameter result below.
The diagnostics suggest increasing total cost in the tested range despite the endpoint behavior (B4)--(B6).

<a id="binary-product-four-pair-filter"></a>
## The exact four-pair binary auxiliary

Let
\[
 \begin{aligned}
 T&=4k+4,\\
 V(z)&=1+z+z^4+z^{2k+1}+z^{2k+3}
            +z^{4k}+z^{4k+3}+z^{4k+4}.
 \end{aligned}
 \tag{B10}
\]
Reduction of (B9) modulo two gives
\[
                  V(z)=(1+z^4)P_r(z)\pmod2.          \tag{B11}
\]
Indeed, in F_2[z],
\[
 \prod_{i=1}^{r-1}(1+z^{2^{i+1}})
            =\frac{1+z^{2k}}{1+z^4},
\]
where the quotient is a polynomial.
Substitution in (B9) gives (B11) by direct expansion.

The four disjoint reflected pairs in (B10) have lower exponents
\[
                         0,\ 1,\ 4,\ 2k+1.
\]
They are distinct and strictly less than T/2=2k+2 for k>=4.
Thus (B10) is an actual four-pair binary auxiliary of full span T.
Its span has not yet been compared with the degree of a positive irreducible factor.
That missing comparison must be supplied rather than assuming that P_r is irreducible or replacing a factor's degree by 4k.

<a id="binary-product-positive-factor-degree"></a>
## A uniform positive-factor degree proportion

The same reduction can be written
\[
 \overline P_r(z)
 =(z+1)^{2k-4}
 \left[(z+1)^{2k+4}+z(1+z^{2k+2})\right].
 \tag{B12}
\]
Here the bar denotes coefficientwise reduction modulo two.
For z=1+t, the bracket in (B12) equals
\[
 t^2+t^3+t^{2k}+t^{2k+1}+t^{2k+2}+t^{2k+3}+t^{2k+4}.
\]
Its order at t=0 is exactly two, because k>=4.
Consequently
\[
 \operatorname{ord}_{z+1}\overline P_r=2k-2=2(k-1).
 \tag{B13}
\]
This is not a power of two when k=2^r and r>=2.
Equivalently,
\[
 \overline P_r=(z+1)^{2k-2}H_r,\qquad
             \deg H_r=2k+2,\qquad H_r(1)=1.           \tag{B14}
\]

Equation (B4) gives P_r(1)=-2, so Phi_1 does not divide P_r.
Suppose Phi_(2^b) divides P_r for some b>=1.
The monic integer quotient A then satisfies
\[
                  A(1)=P_r(1)/\Phi_{2^b}(1)=-1.
\]
Its reduction does not vanish at one.
Since
\[
              \overline{\Phi_{2^b}}=(z+1)^{2^{b-1}},
\]
this would force the order in (B13) to equal 2^(b-1), a contradiction.
Thus no pure-power-of-two cyclotomic polynomial divides P_r.

Every remaining cyclotomic index has the form 2^b m with m>1 odd.
All roots of its reduction have exact odd multiplicative order m, and therefore differ from one.
For clarity, z^m-1 is squarefree in characteristic two when m is odd, and its cyclotomic factors partition roots by exact order.
The usual identities for Phi_(2^b m) reduce it to a positive power of Phi_m in characteristic two, which preserves the set of roots.
These facts retain repeated factors but introduce no root at one.

Let Z_r be the product of every cyclotomic factor of P_r, with its actual multiplicity.
Its reduction is coprime to z+1 and divides the quotient H_r in (B14).
Monicity preserves degrees under reduction, so
\[
                         D_0:=\deg Z_r\le2k+2.       \tag{B15}
\]
The polynomial P_r is monic with constant coefficient one.
Every monic irreducible integer factor is therefore an algebraic-unit polynomial.
By the accepted Kronecker statement, each noncyclotomic irreducible factor has positive total logarithmic Mahler measure.
The total degree of these positive factors, with multiplicities, satisfies
\[
                         D_+=4k-D_0\ge2k-2.         \tag{B16}
\]
This argument covers every r>=2 and does not use the finite factorizations in J139.

<a id="binary-product-complete-original-return"></a>
## Factorwise original-degree return and a uniform floor

For the already accepted constants of C864 v2 (BP1), define
\[
                         \kappa_{\rm bin}=\Gamma_{\rm bin}(1)>0.
\]
This symbol is unrelated to the capacity parameter in v1.
C139 equation (15) writes
\[
               g(K,S,C,\eta)=h_*(K,S,\eta)/C,
\]
where h_* retains that theorem's fixed absolute source constant and does not depend on C.
Consequently every term in C864's minimum scales by 1/C, giving
\[
                  \Gamma_{\rm bin}(C)=\kappa_{\rm bin}/C.
 \tag{B17}
\]
More explicitly,
\[
 \kappa_{\rm bin}
 =\min\left\{
 h_*(6,6,\eta_3),\ K_0\,6^{-64},\
 h_*(8,8,\eta_2),\ K_0\,8^{-64},\
 \frac{\log2}{2L_*}
 \right\},
\]
using exactly C864's eta_2, eta_3, K_0 and L_*.
No numerical value or broader source-review scope is asserted.

Let f be an actual positive irreducible factor of P_r, of degree e, and let alpha be one of its roots.
The polynomial V-(1+z^4)P_r has even integer coefficients by (B11).
Therefore
\[
 \frac{V(\alpha)}2\in\mathbb Z[\alpha]
                  \subseteq\mathcal O_{\mathbb Q(\alpha)}.
 \tag{B18}
\]
The value may be zero, as explicitly permitted by C864 v2 Part A.
The actual auxiliary span remains T, and its original-degree window constant for this factor is C=T/e.
C864 v2 Part A and (B17) give
\[
                          m(f)>\kappa_{\rm bin}e/T.
 \tag{B19}
\]
No reciprocity, squarefree-reduction or power-degree-preservation assumption is made on f.

Summing (B19) over every positive factor with its multiplicity, and then using (B16), proves
\[
 \boxed{
 m(P_r)>\kappa_{\rm bin}\frac{D_+}{T}
       \ge\kappa_{\rm bin}\frac{2k-2}{4k+4}
       \ge\frac{3\kappa_{\rm bin}}{10}>0
       \qquad(r\ge2).}
 \tag{B20}
\]
The last inequality uses k>=4.
The full auxiliary span has been charged separately against each factor's actual degree.
The necessary positive-degree proportion comes from the complete cyclotomic argument, not an irreducibility assumption or a finite observation.

<a id="binary-product-outcome-and-limits"></a>
## Outcome and limits

The proposed sign modification produces a genuine integer reciprocal unit polynomial with positive measure and a natural cyclotomic completion of growing support.
Nevertheless the entire r>=2 family has the uniform positive floor (B20), so it cannot provide a positive-to-zero sequence.
This is a complete failure diagnosis for the displayed construction, rather than merely an inadequate sufficient upper estimate.
The mathematical exclusion is independent of all floating computations and of finite irreducibility checks.

The reason is specific: the signs disappear modulo two, leaving a four-pair auxiliary, while the exact value at one and the residual multiplicity prevent cyclotomic factors from absorbing most of the degree.
Growing ordinary support alone does not avoid that combined arithmetic mechanism.
The result neither classifies other corrections nor supplies a uniform gap on unrestricted original inputs.
No further parameter scan of this same family is needed for its proposed counterexample purpose.
