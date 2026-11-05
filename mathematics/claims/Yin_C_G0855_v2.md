---
author: Yin
---

# All-root slit capacity and a uniform Mahler p=2 floor

This version strengthens the p=2 question in [C855 v1](Yin_C_G0855_v1.md#statement) from a restricted radial-support consequence to the universal raw p=2 bound stated below.
The argument was developed for Yin on 2026-11-05 by the authoring research agent, with the coordinating agent independently obtaining the same radius optimization as a contributor to the development.
The [selected assessment](#decision-whole-independent-review-2026-11-04) adopts the complete new proof through the separate independent R1086 finding.
No novelty, optimal-constant, or unrestricted total Mahler-gap claim is made.

## Revision scope and retained version

[C855 v1](Yin_C_G0855_v1.md#retained-argument) remains the exact home of its restricted Dobrowolski/support estimates, finite-degree qualification and Salem comparison.
That version has no selected assessment; this version neither silently adopts it nor supplies a retrospective review of its argument.
Its numerical Dobrowolski premise is not required for the new proof.
The new capacity, descent and finite-place arguments below establish their own complete chain.
The original total logarithmic Mahler measure remains the target of [G0001](../tasks/Yin_T_G0001_v1.md#contract); its unrestricted positive gap is not a conclusion of this Claim.

## Statement

All logarithms are natural.
For a nonzero algebraic number \(\alpha\), let \(K=\mathbb Q(\alpha)\), \(d=[K:\mathbb Q]\), and use absolute values extending the usual rational ones.
Define
\[
 \mathcal M_2(\alpha)=d\left(
   \sum_{v\in M_K}\frac{[K_v:\mathbb Q_{v_0}]}d
                    |\log|\alpha|_v|^2\right)^{1/2},
\]
where \(v_0\) is the underlying rational place.
For units, this is \((d\sum_{i=1}^d\log^2|\alpha_i|)^{1/2}\), with all original embeddings counted, including both members of every nonreal pair.

**A. Universal raw p=2 bound.**
Every \(\alpha\in\overline{\mathbb Q}^{\times}\) that is not a root of unity satisfies
\[
                       \mathcal M_2(\alpha)\ge1/\sqrt{10}.
\]
Every nonunit satisfies the stronger bound \(\mathcal M_2(\alpha)\ge\log2\).
In C231's degree-lowering ordinary norm construction, with \(L=\mathbb Q(\alpha^n)\), \(e=[K:L]\), \(\gamma=\operatorname{Norm}_{K/L}(\alpha)\), and \(f=[L:\mathbb Q(\gamma)]\), units satisfy exactly
\[
                    \mathcal M_2(\gamma)=\mathcal M_2(\alpha)/f.
\]

**B. The precise FM13 operator-norm consequence.**
Use FM13's arithmetic set \(\mathcal S=\mathcal R\cap\mathcal P\cap\mathcal U\), with its retained 2013 definitions of representability, projection irreducibility and algebraic-unit functions.
For every nonzero \(f_\alpha\in\mathcal S\), and a representative of its minimal degree, one has
\[
           \|f_\alpha\|_{m,2}
           =d(f_\alpha)\|f_\alpha\|_2\ge1/\sqrt{10}.
\]
No operator-norm floor on the whole rationally divisible unit space, or reversal of the source's general upper comparison with the raw degree norm, is asserted.

**C. Original-root contour and the same Hankel determinants.**
Let \(P\) be a monic irreducible reciprocal noncyclotomic integer polynomial of degree \(d\), with constant term one and roots \(\alpha_i\), and suppose every positive power of a root has degree \(d\).
Put \(P_n(x)=\prod_i(1-\alpha_i^n x)\), \(u_i=\log|\alpha_i|\), \(m=\sum_i(u_i)_+\), and \(E_2=\sum_i(u_i)_+^2\).
For an odd prime \(q\), a primitive \(q\)-th root \(\zeta\), and a full orbit \(O\) of nonempty subsets of \(\mathbb Z/q\mathbb Z\) under \(\operatorname{Gal}(\mathbb Q(\zeta)/\mathbb Q)\), define
\[
 D_J(x)=\prod_{j\in J}P_2(\zeta^jx),\quad
 N_J(x)=\prod_{j\in J}P_4(\zeta^jx),\quad
 G_J(x)=\sqrt{N_J(x)/D_J(x)},\quad G_J(0)=1,
\]
\[
 f(x)=\sum_{J\in O}G_J(x)=\sum_{n\ge0}a_nx^n,\qquad
 S=\bigcup_{J\in O}J,\qquad s=|S|,\qquad
 \Delta_h=\det(a_{i+j+1})_{0\le i,j<h}.
\]
For \(t\ge0\), let \(K_t\) be the disk of radius \(e^{-t}\), with radial slits to every \(\zeta^j\alpha_i^2\) and \(\zeta^j\alpha_i^4\) lying outside that disk, for all \(i\) and \(j\in S\).
Then
\[
 \limsup_{h\to\infty}h^{-2}\log|\Delta_h|
 \le\log\operatorname{cap}K_t\le\Phi_s(t),
\]
where zero determinants have logarithm \(-\infty\) and
\[
 \Phi_s(t)=-t+2s\sum_i\left(
    \log\cosh\frac{(t+2u_i)_+}{2}
   +\log\cosh\frac{(t+4u_i)_+}{2}\right).
\]
Every neutral or contracting endpoint and every used rotation is included according to this definition.
The following paid bounds hold:
\[
 \Phi_s(0)\le5sE_2,\qquad
 \inf_{t\ge0}\Phi_s(t)\le10sE_2-\frac1{2ds},
\]
\[
 \inf_{t\ge0}\Phi_s(t)
       \le5sE_2-\frac{(1-3sm)^2}{2ds}
                         \quad\hbox{if }3sm<1.
\]
Under the complete arithmetic and approximation-rank hypotheses of [C860 v4 Part C](Yin_C_G0860_v4.md#statement), with its residual-depth gain \(a>0\) and actual pole-rank slope \(K_{\rm pole}>0\), the same determinants satisfy
\[
              \frac{a\log2}{2K_{\rm pole}}
                        \le\inf_{t\ge0}\Phi_s(t).
\]
This is a conditional strengthening of the complex comparison, not a supply of masks, centers or extra rank reduction.

**D. Square-mass and conditional total-Mahler consequences.**
For the original \(P\) in C, the unrotated integral germ \(\sqrt{P_2P_4}\) gives
\[
         0\le\inf_{t\ge0}\Phi_1(t),\qquad dE_2\ge1/20.
\]
It also gives \(10dE_2\ge(1-3m)^2\) when \(m<1/3\).
For any fixed \(C>0\), the exact additional condition \(dE_2\le Cm^2\) therefore gives both
\[
                 m\ge\frac1{\sqrt{20C}},\qquad
                 m\ge\frac1{3+\sqrt{10C}}.
\]
No uniform such concentration condition on all putative near-one inputs is claimed.
A Salem polynomial has \(E_2=m^2\), so its concentration ratio \(dE_2/m^2=d\) remains unbounded with degree.

## Sources and proof interfaces

[Dim19, arXiv:1912.12545v1](../literature/pdf/Dim19.pdf), Section 3 on printed pp. 12--13 and Section 4 on pp. 13--15, supply the capacity normalization and the determinant mechanism.
The present author text-read those complete selected passages from the available original, including the proof outline of Theorem 4 and Corollary 5, and the Theorem 1 application on pp. 15--16.
In that convention the Green function at infinity is \(g_K(z)=\log|z|-\log\operatorname{cap}K+o(1)\), and capacity equals transfinite diameter and the leading coefficient of the normalized exterior Riemann map.
The contour argument below supplies the relevant determinant estimate directly, using those standard capacity identities.
This is not an inspection of the entire Dim19 proof or of the original Bertrandias and Dubinin sources.

The [published Calegari--Dimitrov--Tang Theorem 2.0.1, printed p. 635](https://www.math.uchicago.edu/~fcale/papers/UDC.pdf#page=9) was checked at statement and applicability scope.
Its expanding-map hypothesis remains necessary for that theorem, but is not used below.
The [published van Ittersum--Ringeling--Zudilin paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8B96145B989139A2E44CF7ABE8D4EA92/S0004972721000654a.pdf/hedgehogs_in_lehmers_problem.pdf), Section 2, printed pp. 237--239, was checked for its unrestricted geometric question and Theorems 3--4.
This is the 2022 journal edition; the earlier L445 link refers to the preprint's numbering.
Its small-product hedgehogs neither provide an original integral conjugate set nor bound the radial concentration defined below.

Local reuse included C857 v2, C858, C860 v4, L445, and the previously restricted [C855 v1 p=2 argument](Yin_C_G0855_v1.md#statement) with [FM13's exact normalization](../audits/literature/FM13/Yin_U001.md#p-two-and-classical-gap-boundary).
A bounded search by radial slits, capacity, squared logarithmic root norms and the Lp Lehmer question found no verified theorem already supplying the specific estimate below.
That search outcome gives no novelty or priority claim, and the 2010 author PDF found for Fili--Miner is not substituted for the retained 2013 source unit.


The proof uses the following actual fixed interfaces.
[C231 Part D](Yin_C_G0231_v1.md#all-positive-power-existence-descent) supplies ordinary relative-norm degree descent and the equal-modulus embedding fibers; the new square-norm identity is proved here.
[C858](Yin_C_G0858_v1.md#all-place-hankel-budget) supplies the original branch noncollision, nonrationality, finite elementary-divisor comparison and shifted Kronecker criterion, at its adopted scope.
[C860 v2](Yin_C_G0860_v2.md#statement) supplies the original congruence \(P_4-P_2\in4\mathbb Z[x]\); the resulting square-root integrality is proved directly below.
[C860 v4](Yin_C_G0860_v4.md#statement) supplies only the stated optional finite-place coefficient and its paid pole-rank hypotheses.
[Smy08 U002](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number) supplies the accepted nonreciprocal lower bound, without a newly audited 1971 source proof.
[FM13 U001](../audits/literature/FM13/Yin_U001.md#restricted-arithmetic-set) supplies the exact 2013 definitions and the operator identity only on the arithmetic set \(\mathcal S\), at its retained statement and applicability scope.
The capacity identities accepted from the selected Dim19 passages, the direct contour calculation, and every new deduction below are separate from those fixed arithmetic inputs.

<a id="argument"></a>
## Complete argument

### A disk and one radial slit

For \(r>0\), \(v\ge0\) and \(\theta\in\mathbb R\), let
\[
 K(r,v,\theta)=\{z:|z|\le r\}\cup
       \{s e^{i\theta}:r\le s\le r e^v\}.
\]
Then
\[
 \operatorname{cap}K(r,v,\theta)
                  =r\cosh^2(v/2).                         \tag{SC1}
\]
To verify the constant, rotation and scaling reduce to \(r=1\), \(\theta=0\).
The Joukowski map \(J(z)=z+z^{-1}\) maps the exterior of the unit disk conformally onto the complement of \([-2,2]\), with expansion \(J(z)=z+O(z^{-1})\) at infinity.
Removing the slit \([1,e^v]\) removes the additional interval \([2,e^v+e^{-v}]\) from the image.
The resulting interval has length \(2+e^v+e^{-v}=4\cosh^2(v/2)\).
An interval of length \(\ell\) has capacity \(\ell/4\), as follows from the inverse Joukowski map with its leading coefficient.
Composition at infinity therefore proves (SC1), including \(v=0\).

### The common disk makes the logarithmic comparison valid

Let \(K_1,\ldots,K_N\) each be the closed disk of radius \(r\) together with one radial slit, and let \(K=\bigcup_\nu K_\nu\).
Repeated directions and zero-length slits are allowed.
These sets have connected complements and regular boundaries for the exterior Dirichlet problem.
They are radial star sets, so their complements in the Riemann sphere are simply connected; after inversion their complements are disks with finitely many inward radial slits that can be contracted toward zero.
Let \(g_\nu\) and \(g\) be their Green functions with pole at infinity, extended continuously by zero to the boundaries, and put \(g_0(z)=\log(|z|/r)\) on \(|z|>r\).
By comparison with the disk, \(0\le g_\nu\le g_0\) outside \(K_\nu\).
For completeness, the upper inequality follows by applying the maximum principle to the bounded harmonic difference \(g_\nu-g_0\), which is nonpositive on the boundary and extends harmonically across infinity on the Riemann sphere.
No sign at infinity has to be assumed: infinity is an interior point of that bounded harmonic comparison.

On the common exterior \(\Omega=\widehat{\mathbb C}\setminus K\), set
\[
 H=\sum_{\nu=1}^N(g_0-g_\nu)-(g_0-g).
\]
Every boundary point belongs to at least one \(K_\nu\) and, when approached from \(\Omega\), has \(g_\nu=0\) for that index.
Since \(g=0\) there and all other \(g_0-g_\nu\) are nonnegative, one has \(H\ge0\) on the boundary.
The logarithmic terms cancel at infinity, so \(H\) is bounded and harmonic on \(\Omega\), including infinity as a removable point.
The minimum principle on this domain in the sphere gives \(H(\infty)\ge0\), or
\[
 \log\frac{\operatorname{cap}K}{r}
       \le\sum_{\nu=1}^N\log\frac{\operatorname{cap}K_\nu}{r}.
                                                               \tag{SC2}
\]
Thus (SC2) is a proved comparison for hulls with this common disk, not an assertion of unrestricted subadditivity of logarithmic capacity.

### All original roots and every used rotation

Let \(P\) be the monic irreducible reciprocal noncyclotomic power-stable unit input of C858, of degree \(d\), with its complete original list of roots \(\alpha_1,\ldots,\alpha_d\).
Write
\[
 u_i=\log|\alpha_i|,\qquad
 m=\sum_{i=1}^d(u_i)_+,\qquad
 E_2=\sum_{i=1}^d(u_i)_+^2,
 \qquad (x)_+=\max(x,0).                                    \tag{SC3}
\]
Every complex embedding is counted, including both members of a nonreal pair.
Reciprocity implies that the multiset \(\{u_i\}\) is symmetric under negation and that \(\sum_i u_i^2=2E_2\).

Let \(O\) be a full Galois orbit of nonempty rotation masks, let \(S=\bigcup_{J\in O}J\), and put \(s=|S|\).
For \(t\ge0\), set \(r=e^{-t}\), and form \(K_t\) from the disk \(|z|\le r\) by adding radial slits to every point
\[
             \zeta^j\alpha_i^2,\quad \zeta^j\alpha_i^4,
                  \qquad i=1,\ldots,d,\ j\in S,             \tag{SC4}
\]
whose modulus is greater than \(r\).
Endpoints already in the disk add no slit.
The multiset of slit lengths, with harmless repeated slits retained in the upper bound, consists of \((t+2u_i)_+\) and \((t+4u_i)_+\) for each \(j\in S\).
Equations (SC1)--(SC2) give the complete estimate
\[
 \log\operatorname{cap}K_t\le\Phi_s(t):=
 -t+2s\sum_{i=1}^d
 \left\{\log\cosh\frac{(t+2u_i)_+}{2}
       +\log\cosh\frac{(t+4u_i)_+}{2}\right\}.              \tag{SC5}
\]
In particular, a neutral root contributes both of its positive-length terms when \(t>0\).
Contracting roots are retained whenever their powered endpoints lie outside the chosen disk.
No branch endpoint has been discarded according to whether it contributes to \(m\).

The same germ \(f(x)=\sum_{J\in O}G_J(x)\) as in C858 is single-valued and holomorphic after \(x=1/z\) on \(\widehat{\mathbb C}\setminus K_t\).
Indeed each rational radicand has all its zeros and poles in (SC4), is nonzero and holomorphic on that simply connected exterior, and equals one at infinity.
Its unique square root based at infinity therefore extends there.
All finitely many mask products extend on the same domain, so taking their sum does not introduce a hidden sheet-degree multiplier.
The denominators, branch points and every used rotation have already been included in \(K_t\).
Constants bounding this fixed-input sum on a contour may depend on its orbit and degree; their logarithms occur only to linear order in the Hankel size below.

### The capacity bound applies to the same shifted Hankel determinants

Let \(f(x)=\sum_{n\ge0}a_nx^n\) be any germ with the preceding exterior continuation, and let \(\Delta_h=\det(a_{i+j+1})_{0\le i,j<h}\).
For a positively oriented analytic Jordan curve \(\Gamma\) enclosing \(K_t\) within the continuation domain,
\[
 a_{n+1}=\frac{1}{2\pi i}\int_\Gamma f(1/z)z^n\,dz.
\]
Expanding determinants and permuting the integration variables gives the finite identity
\[
 \Delta_h=\frac1{h!(2\pi i)^h}
  \int_{\Gamma^h}\prod_{\ell=1}^h f(1/z_\ell)
          \prod_{j<k}(z_k-z_j)^2\,dz_1\cdots dz_h.          \tag{SC6}
\]
This can also be checked directly by multiplying the two Vandermonde determinants, expanding both permutations, and integrating each monomial.
Let
\[
 \delta_h(\Gamma)=
   \max_{z_1,\ldots,z_h\in\Gamma}
          \prod_{j<k}|z_k-z_j|^{2/(h(h-1))}
\]
for \(h\ge2\), and let \(A_\Gamma=\operatorname{length}(\Gamma)\sup_\Gamma|f(1/z)|/(2\pi)\).
Taking absolute values in (SC6) yields
\[
 |\Delta_h|\le\frac{A_\Gamma^h}{h!}
                 \delta_h(\Gamma)^{h(h-1)}.
\]
By the transfinite-diameter identity retained above,
\[
 \limsup_{h\to\infty}\frac{\log|\Delta_h|}{h^2}
                       \le\log\operatorname{cap}\Gamma.
\]
Zero determinants have logarithm \(-\infty\).
For precision about the last contour limit, the normalized exterior Riemann map of \(K_t\) sends \(|w|>1\) onto its exterior and has leading coefficient \(c=\operatorname{cap}K_t\).
Its image of \(|w|=R>1\) is an analytic Jordan curve \(\Gamma_R\) with capacity \(Rc\), by the same leading-coefficient characterization.
Using these curves and letting \(R\downarrow1\) proves
\[
 \limsup_{h\to\infty}\frac{\log|\Delta_h|}{h^2}
                 \le\log\operatorname{cap}K_t\le\Phi_s(t)
                    \quad\hbox{for every }t\ge0.           \tag{SC7}
\]
This is a fixed-input limit in \(h\); no estimate uniform in a changing polynomial is needed for the contour constants to disappear.

### Return to the integral original input and the finite-place budget

For the C858 orbit sum, retain its supplied all-place integrality and nonrationality, or the corresponding centered hypotheses of C860 v4.
The same shifted leading Hankel determinants are nonzero for infinitely many \(h\) by the accepted Kronecker criterion.
If the actual approximation ranks and depths give quadratic valuation coefficient \(a/(2K_{\rm pole})\), as in C860 v4, then integer nonzero determinants and (SC7) give
\[
 \frac{a\log2}{2K_{\rm pole}}
                  \le\inf_{t\ge0}\Phi_s(t).                \tag{SC8}
\]
All original approximation-rank, center and descent hypotheses are unchanged in this implication.
In particular, the upper bound does not provide an all-place mask or improve \(K_{\rm pole}\) by itself.

There is also an unconditional version of this analytic comparison on the stated original input.
Take the single unrotated integral germ
\[
                  F(x)=\sqrt{P_2(x)P_4(x)},\qquad F(0)=1.
\]
Its integrality follows from the [retained original congruence](Yin_C_G0860_v2.md#statement) \(P_4-P_2\in4\mathbb Z[x]\): write \(P_4=P_2+4W\), so \(F=P_2\sqrt{1+4W/P_2}\), where \(W/P_2\in x\mathbb Z[[x]]\).
For every integer \(n\ge1\), the factorial formula gives
\[
 4^n\binom{1/2}{n}
   =2(-1)^{n-1}
      \left\{\binom{2n-2}{n-1}-\binom{2n-2}{n}\right\}
      \in\mathbb Z.
\]
Thus substitution proves the asserted formal integrality directly.
This is the square-root integrality mechanism attributed to Dim19 Proposition 2.2 in the retained L445 source comparison.
Power-stability and positive height exclude collisions among the squared and fourth-powered roots as in C858.
Its simple branch points make it nonrational.
Thus its infinitely many nonzero shifted leading Hankel determinants are nonzero integers, and the same proof, now with \(s=1\), gives
\[
                         0\le\inf_{t\ge0}\Phi_1(t).         \tag{SC9}
\]
This step uses all original roots of the one polynomial and does not assert arithmetic realizability of a freely chosen radial configuration.

### Explicit radial square-mass consequences

The elementary inequality \(\log\cosh x\le x^2/2\) and
\((t+cu)_+^2\le t^2+2ctu_++c^2u_+^2\), valid for \(t,c\ge0\), imply
\[
 \Phi_s(t)\le -t+s\left(\frac d2t^2+3mt+5E_2\right).
                                                               \tag{SC10}
\]
At \(t=0\) this gives the useful bound \(\Phi_s(0)\le5sE_2\le5sm^2\), in place of the elementary disk cost \(4\log H\).
If \(3sm<1\), choosing \(t=(1-3sm)/(ds)\) gives
\[
 \inf_{t\ge0}\Phi_s(t)
          \le5sE_2-\frac{(1-3sm)^2}{2ds}.                  \tag{SC11}
\]
Consequently (SC9) implies \(10dE_2\ge(1-3m)^2\) when \(m<1/3\).
For any supplied constant \(C>0\), the exact original-input condition
\[
                           dE_2\le C m^2                  \tag{SC12}
\]
would therefore imply the total Mahler gap
\[
                          m\ge\frac1{3+\sqrt{10C}}.         \tag{SC13}
\]
Inputs with \(m\ge1/3\) already satisfy (SC13).
Condition (SC12) bounds the concentration of the actual radial logarithms; having many nonzero radial coordinates alone does not imply it.

Reciprocity gives a second, unconditional square-mass estimate on this input class.
For \(t,a\ge0\), direct consideration of \(a\le t\) and \(a>t\) proves
\[
                   (t+a)_+^2+(t-a)_+^2\le2t^2+2a^2.
\]
Pairing the original \(u_i\) with \(-u_i\), including zero coordinates, in (SC5) gives
\[
 \Phi_s(t)\le -t+s\left(\frac d2t^2+10E_2\right),\qquad
 \inf_{t\ge0}\Phi_s(t)\le10sE_2-\frac1{2ds}.              \tag{SC14}
\]
Here the minimizing choice is \(t=1/(ds)\).
Equations (SC9) and (SC14) give
\[
 dE_2\ge\frac1{20},\qquad
 \left(d\sum_i u_i^2\right)^{1/2}\ge\frac1{\sqrt{10}},      \tag{SC15}
\]
and (SC12) would also give \(m\ge1/\sqrt{20C}\).
The raw square norm in (SC15) uses the original degree and all embeddings.
Its relation to the FM13 Mahler operator outside the restricted arithmetic set is not silently identified; see the exact boundary in [FM13 U001](../audits/literature/FM13/Yin_U001.md#restricted-arithmetic-set).

The finite-place strengthening (SC8) adds its positive left side to the requirements in (SC11) and (SC14), with the same \(s,d,E_2\) and actual \(K_{\rm pole}\).
For example, (SC14) gives \(10sE_2\ge1/(2ds)+a\log2/(2K_{\rm pole})\).
The selected whole review includes these consequences and their exact classical capacity interfaces.
The present construction supplies no bound (SC12) on a covering family of putative near-one inputs, no universal upper determinant cost proportional to \(m/d\), and no unrestricted positive total Mahler gap.
For a Salem input \(E_2=m^2\), the concentration ratio in (SC12) is \(d\), so the original missing total-measure issue remains visible.

<a id="raw-p-two-norm-descent"></a>
### Norm descent of the raw p=2 quantity

The following extension completes the raw p=2 statement at every actual algebraic degree.
It uses the actual [C231 all-power norm descent](Yin_C_G0231_v1.md#all-positive-power-existence-descent), rather than assuming that taking an arbitrary positive power decreases the relevant quantity.
For any nonzero algebraic number \(\alpha\) with \(K=\mathbb Q(\alpha)\) and \(d=[K:\mathbb Q]\), define the raw quantity in the retained FM13 normalization by
\[
 \mathcal M_2(\alpha)=d\left(
   \sum_{v\in M_K}\frac{[K_v:\mathbb Q_{v_0}]}{d}
                    |\log|\alpha|_v|^2\right)^{1/2}.
                                                               \tag{SC16}
\]
Here \(v_0\) is the underlying rational place, and the absolute values extend the ordinary rational absolute values.
For an algebraic unit, every finite-place term vanishes and
\[
             \mathcal M_2(\alpha)^2
                     =d\sum_{i=1}^d\log^2|\alpha_i|.        \tag{SC17}
\]
For a complex place the local degree two gives exactly the two original embeddings in (SC17).

### The exact square-norm change in C231's descent

Let \(\alpha\) be a nonzero nontorsion algebraic unit for which an integer \(n\ge1\) lowers degree.
Set
\[
 L=\mathbb Q(\alpha^n),\qquad e=[K:L]>1,\qquad
 \gamma=\operatorname{Norm}_{K/L}(\alpha),\qquad
 f=[L:\mathbb Q(\gamma)].
\]
C231 proves that \(\gamma\) is a nontorsion algebraic unit,
\(\deg\gamma=d/(ef)<d\), and \(\gamma^n=(\alpha^n)^e\).
For each complex embedding \(\tau:L\hookrightarrow\mathbb C\), its \(e\) extensions \(\sigma:K\hookrightarrow\mathbb C\) have a common modulus \(r_\tau=|\sigma(\alpha)|\), since their \(n\)-th powers coincide.
The ordinary relative norm therefore satisfies \(|\tau(\gamma)|=r_\tau^e\).
Every embedding of \(\mathbb Q(\gamma)\) occurs exactly \(f\) times among the embeddings of \(L\).
Consequently
\[
 \begin{split}
 \sum_{\gamma'}\log^2|\gamma'|
   &=\frac{e^2}{f}\sum_{\tau:L\hookrightarrow\mathbb C}
                                      \log^2r_\tau
     =\frac e f\sum_{\sigma:K\hookrightarrow\mathbb C}
                                      \log^2|\sigma(\alpha)|,\\
 \mathcal M_2(\gamma)^2
   &=\frac1{f^2}\mathcal M_2(\alpha)^2.                     \tag{SC18}
 \end{split}
\]
This compares the raw quantities at their respective actual degrees; it introduces no normalized relative norm or uncharged radical.
Repeating C231's strictly degree-lowering construction terminates at a power-stable nontorsion unit \(\beta\), with
\[
                    \mathcal M_2(\beta)\le
                    \mathcal M_2(\alpha).                  \tag{SC19}
\]
No algorithm for deciding the all-positive-power condition is claimed.

### Reciprocal and nonreciprocal endpoints

If the endpoint \(\beta\) is reciprocal, (SC15) gives
\(\mathcal M_2(\beta)\ge1/\sqrt{10}\).
If it is nonreciprocal, use the already accepted [Smyth input and its source-proof limit](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number): \(m(\beta)\ge\log\theta_0\), where \(\theta_0>1\) is the real root of \(x^3-x-1\).
For any unit of degree \(D\), the product formula and Cauchy--Schwarz give
\[
 \mathcal M_2(\beta)\ge\sum_{i=1}^D|\log|\beta_i||
                                  =2m(\beta).
\]
Since \(\theta_0>5/4\) and \(\log(5/4)>1/5\), the nonreciprocal bound is larger than \(2/5>1/\sqrt{10}\).
Together with (SC19), this proves
\[
       \mathcal M_2(\alpha)\ge\frac1{\sqrt{10}}
              \quad\text{for every nontorsion algebraic unit }\alpha.
                                                               \tag{SC20}
\]
Reciprocity need not be preserved during norm descent, because the endpoint alternatives have both been covered.

### The finite-place floor for a nonunit

If a nonzero algebraic number \(\alpha\) is not an algebraic unit, at least one finite place \(v\) of \(K\) has nonzero additive valuation.
Write its ramification and residue degrees over a rational prime \(p\) as \(e_v,f_v\).
For the integer-valued valuation \(\operatorname{ord}_v\), the stipulated normalization is
\[
        \log|\alpha|_v=-\frac{\operatorname{ord}_v(\alpha)}{e_v}
                                      \log p.
\]
Its single contribution to (SC16), with \([K_v:\mathbb Q_p]=e_vf_v\), gives
\[
 \mathcal M_2(\alpha)^2
     \ge\frac{df_v}{e_v}\operatorname{ord}_v(\alpha)^2
                          (\log p)^2
     \ge(\log2)^2,                                         \tag{SC21}
\]
because \(e_v\le d\), \(f_v\ge1\), and the nonzero integer valuation has square at least one.
This argument includes nonintegral algebraic numbers and either sign of the finite valuation.
Since \(\log2>1/2>1/\sqrt{10}\), (SC20)--(SC21) give the proposed uniform raw bound
\[
 \mathcal M_2(\alpha)\ge\frac1{\sqrt{10}}
       \quad\left(\alpha\in\overline{\mathbb Q}^{\times}
                    \text{ not a root of unity}\right).   \tag{SC22}
\]
The positive constant is not claimed optimal.

### Exact FM13 and total-Mahler interfaces

For the chosen original representative, \(\mathcal M_2(\alpha)\) is precisely FM13's \(m_2(\alpha)=\deg(\alpha)h_2(\alpha)\), using all places.
For a nonzero element \(f_\alpha\) of the retained arithmetic set \(\mathcal S=\mathcal R\cap\mathcal P\cap\mathcal U\), choose its representative of minimal degree \(d(f_\alpha)\).
The accepted [FM13 Proposition 4.5 interface](../audits/literature/FM13/Yin_U001.md#restricted-arithmetic-set) then identifies
\[
       \|f_\alpha\|_{m,2}
       =d(f_\alpha)\|f_\alpha\|_2
       =\mathcal M_2(\alpha)\ge\frac1{\sqrt{10}}.            \tag{SC23}
\]
Equations (SC22) and (SC23) are the two equivalent positive-floor formulations of the source's p=2 assertion, at its retained Theorem 4 statement/applicability scope.
The decomposition theorem and its original proof are not newly independently audited here.
No positive floor is asserted for the Mahler operator norm on the whole rationally divisible unit space, and its general upper comparison with the raw degree norm has not been reversed.

This statement strengthens the previously retained restricted-support p=2 result, while remaining logically weaker than the original p=1 Lehmer Task.
On units the original total logarithm is \(m=\frac12\sum_i|\log|\alpha_i||\), whereas (SC22) controls a degree-weighted square norm.
A uniform bound of that square norm by a fixed multiple of the total logarithm is still missing on the unrestricted arithmetic inputs.
The original-root concentration condition (SC12) supplies exactly such a restricted comparison in the reciprocal case; the number of nonzero coordinates alone does not.
All of (SC1)--(SC23), including the norm-descent extension and exact source limits, are covered by the selected independent whole finding.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T21:03 |
| status | proved |
| reason | Adopt complete A--D and SC1--SC23 after independent R1086: the all-root slit-capacity and shifted-Hankel comparison, universal raw Mahler p=2 floor 1/sqrt(10), exact ordinary-norm descent, nonunit floor and FM13 operator consequence only on its restricted arithmetic set. Classical source inputs retain their inspected scope. The total p=1 gap still requires additional arithmetic or concentration control; G0001 remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, all nonzero nontorsion algebraic numbers in the raw bound, exact restricted operator identity, original-root capacity and separately conditional total-Mahler consequences. |
| argument | [Complete argument](#argument) | All SC1--SC23: single slit, common-disk Green comparison, complete branch continuation, determinant capacity limit, integer nonrational input, optimization, norm descent and finite-place normalization. |
| dependency | [Ordinary norm descent](Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Actual degree, unit/nontorsion preservation and equal-modulus embedding fibers in the terminating all-power existence descent. |
| dependency | [Original branches and Hankel criterion](Yin_C_G0858_v1.md#all-place-hankel-budget) | Original noncollision/private branches, finite elementary-divisor implication and shifted leading-Hankel criterion at retained BNZ22 scope. |
| dependency | [Original modulo-four congruence](Yin_C_G0860_v2.md#statement) | Only P4-P2 in 4 Z[x] for the same original reciprocal input; square-root integrality is proved directly in this argument. |
| dependency | [Optional finite-place strengthening](Yin_C_G0860_v4.md#statement) | Only complete Part C supplied-center hypotheses, same original orbit sum, actual positive slope and all-level determinant valuation coefficient. |
| support | [FM13 normalization and restricted set](../audits/literature/FM13/Yin_U001.md#fm13-u001) | Retained 2013 all-place normalization, minimal representative degree, R/P/U definitions, Proposition 4.5 and Theorem 4 at their stated source-inspection limits. |
| support | [Nonreciprocal threshold](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only the accepted nonreciprocal algebraic-integer bound used at the norm-descent endpoint, without a new audit of the 1971 proof. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1086_v1.md#raw-p2-whole) | Complete A--D/SC1--SC23, exact accepted capacity/arithmetic/source interfaces, restricted operator scope, preservation of unassessed v1 and the original p=1 Task boundary. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
