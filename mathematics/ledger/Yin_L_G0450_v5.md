---
author: Yin
---

# Moving sparse mixed maps: a uniform height asymptotic and the sublinear-factor criterion

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating contributor selected the moving family and its complete coefficient cost.
The construction contributor developed the integral Mobius height identity and relative-orbit asymptotic; the source contributor checked its field, place-weight, equidistribution and positivity interfaces.
The computation contributor completed the four assigned exact factorizations and full-root diagnostics in J142.
These are ordinary author-development checks, not an independent project review, a new Claim assessment or a resolution of the Task.

<a id="moving-map-scope"></a>
## Question and fixed predecessors

The [fixed cubic backward-tree obstruction](Yin_L_G0450_v4.md#cubic-allpass-height-floor) has a constant depending on its fixed rational map.
Here the map itself changes with n, so that obstruction supplies no uniform height floor.
[V3](Yin_L_G0450_v3.md#mixed-allpass-revision-scope), [v2](Yin_L_G0450_v2.md#fixed-source-proliferation-revision) and [v1](Yin_L_G0450_v1.md#scope-and-factor-proliferation-assessment) retain their distinct norm, parity, Blaschke and radical-substitution arguments.
The current input at n=3 is the first fixed-cubic layer already computed in [J141](../computations/programs/Yin_J_G0141/readme.md); larger n here are not deeper iterates of that cubic.

The [positive-factor bridge](Yin_L_G0450_v1.md#positive-factor-counterexample-bridge) gives a sufficient route through bounded complete measure and an unbounded number of positive factors within the same output.
For the present family, the height calculation below gives a sharper equivalence: extracting positive measures tending to zero is exactly the problem of finding actual factors of degree o(n).
Neither that degree condition nor unbounded factor count has been established.
All measures m are total logarithmic Mahler measures, and h is absolute logarithmic Weil height, with [m(f)=deg(f)h(beta)](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) for an irreducible integer polynomial f with root beta.

<a id="moving-map-actual-inputs"></a>
## Complete integer inputs and the fixed-field fiber

Fix the Lehmer polynomial and odd integers n>=3:
\[
 P_L(z)=z^{10}+z^9-z^7-z^6-z^5-z^4-z^3+z+1,\qquad
 g_n(z)=z^n-z-1,\qquad g_n^*(z)=1-z^{n-1}-z^n,
\]
\[
 R_n=g_n^*/g_n,\qquad
 F_n(z)=g_n(z)^{10}P_L(R_n(z)).                         \tag{M1}
\]
The source is irreducible of degree ten, has constant one and endpoint values P_L(1)=-1 and P_L(-1)=1, and is Salem with real root lambda>1.
These are the same fixed-source properties used in [v4](Yin_L_G0450_v4.md#cubic-allpass-actual-polynomials).

There is no common root of g_n and g_n*.
Indeed their sum is -z(1+z^(n-2)); a common root is nonzero and satisfies z^(n-2)=-1.
Substitution in g_n then gives z^2+z+1=0.
A cube root of unity cannot have a power equal to -1, giving a contradiction.
In particular g_n has no root on the unit circle, since its real coefficients would then make that root common with g_n*.
The map R_n therefore has no pole on the circle and preserves it.

Direct homogeneous evaluation in (M1) gives
\[
 \deg F_n=10n,\qquad \operatorname{lc}F_n=F_n(0)=1,
 \qquad F_n(1)=-1,\quad F_n(-1)=1.                    \tag{M2}
\]
For the leading and constant coefficients use P_L(-1)=1; for the endpoints use g_n(1)=g_n*(1)=-1 and g_n(-1)=-1, g_n*(-1)=1.
Reversal interchanges g_n and g_n*, so reciprocity of P_L gives reciprocity of F_n.
Thus F_n is primitive, and all its irreducible factors can be chosen monic with constant coefficient plus or minus one.

No root beta of F_n is a root of unity.
First, g_n(beta) cannot vanish: at a zero of g_n, homogeneous evaluation gives F_n(beta)=g_n*(beta)^10, which is nonzero by coprimality.
If beta were a root of unity, alpha=R_n(beta) would be a root of P_L, and every conjugate of beta would be on the circle.
The nonvanishing denominator and circle-preservation property then put every conjugate of alpha on the circle, contradicting its conjugate lambda>1.
Consequently every actual irreducible factor has positive measure by the accepted Kronecker characterization.
The complete coefficient cost is uniformly bounded:
\[
 0<m(F_n)\le\log\|F_n\|_1
 \le \log\bigl(9\cdot3^{10}\bigr).                    \tag{M3}
\]
There are nine nonzero source coefficients of absolute value one, and both g_n and g_n* have coefficient one-norm three.
The estimate retains all homogeneous terms and makes no subtraction of denominator or radial cost.

Fix alpha=lambda, K=Q(alpha), d=[K:Q]=10, and put
\[
 u=(1+\alpha)^{-1},\qquad a=1-u=\alpha/(1+\alpha).
\]
Since alpha and 1+alpha are units, u and a are units in O_K.
For any actual irreducible factor of F_n, a conjugate root beta can be chosen so that R_n(beta)=alpha.
Then K is a subfield of L=Q(beta), and
\[
 q_{n,u}(z)=z^{n-1}(z+u)-(az+1),\qquad
 q_{n,u}(\beta)=0,\qquad
 \beta^{n-1}=T_u(\beta),\quad
 T_u(z)=\frac{az+1}{z+u}.                              \tag{M4}
\]
The denominator in this last expression cannot vanish at a root, as follows also from the unit determinant below.
Every actual factor degree is d[L:K], hence a multiple of ten.

The original fiber is g_n* - alpha g_n=-(1+alpha)q_(n,u).
Its leading factor has norm N_(K/Q)(-(1+alpha))=P_L(-1)=1, so the exact polynomial identity is
\[
                         F_n=N_{K/\mathbb Q}(q_{n,u}). \tag{M5}
\]
The leading factors at individual embeddings are not separately free; their total logarithmic cost is zero because their norm is one.
The full degree-n fiber has relative root product one, since n is odd and q_(n,u) has constant -1.
This supplies a genuine torsion full-fiber norm, not a formula for the relative norm of an arbitrary proper factor.

<a id="moving-map-integral-mobius-height"></a>
## Integral Mobius matrix and the exact height identity

The fixed matrix representing T_u is
\[
 A=\begin{pmatrix}a&1\\1&u\end{pmatrix},\qquad
 \det A=au-1=-\frac{\alpha^2+\alpha+1}{(\alpha+1)^2}.    \tag{M6}
\]
For a primitive cube root omega, direct reduction gives P_L(omega)=-omega^2 and P_L(omega^2)=-omega.
Therefore
\[
 N_{K/\mathbb Q}(\alpha^2+\alpha+1)
       =P_L(\omega)P_L(\omega^2)=1.
\]
The numerator in (M6) is an algebraic-integer unit, and hence A belongs to GL_2(O_K).
At every finite place of any extension of K, both A and A^(-1) have integral entries.
Applying the maximum norm to A and its inverse proves equality of the maximum norms before and after applying A.
Thus the projective height difference for T_u has exactly zero finite-place contribution; no finite denominator cost is omitted.

For each of the d embeddings sigma:K into C, define
\[
 \psi_\sigma(z)=
 \log\max\{|(\sigma a)z+1|,\ |z+\sigma u|\}
       -\log\max\{1,|z|\}.                            \tag{M7}
\]
The two numerator linear forms have no common zero because det A is nonzero.
The function extends continuously to the Riemann sphere, with value log max(1,|sigma a|) at infinity.
In particular it is bounded, including at the pole of the affine fractional expression.

Write r=[L:K] and use the complete relative orbit at sigma,
\[
 \nu_{\beta,\sigma}
  =\frac1r\sum_{\tau:L\hookrightarrow\mathbb C,\ \tau|_K=\sigma}
                        \delta_{\tau\beta}.
\]
Each of the ten embeddings of K is counted once; the two embeddings belonging to a complex place thus have their usual combined weight.
The finite-place identity and (M4) give the exact equality
\[
 (n-2)h(\beta)=h(T_u(\beta))-h(\beta)
       =\frac1d\sum_\sigma\int\psi_\sigma\,d\nu_{\beta,\sigma}. \tag{M8}
\]
This is a full-height equality for the actual root, not a selected real-root estimate.

For every finite z, the numerator maximum in (M7) is at most max(1+|sigma a|,1+|sigma u|) max(1,|z|), and the resulting bound for psi_sigma also holds at infinity by continuity.
Consequently the fixed finite constant
\[
 C=\frac1d\sum_\sigma
        \log\max\{1+|\sigma a|,\ 1+|\sigma u|\}
\]
gives the uniform bound
\[
                         0<h(\beta)\le\frac{C}{n-2}.  \tag{M9}
\]
Strict positivity uses the already proved absence of zero and roots of unity.

<a id="moving-map-uniform-asymptotic"></a>
## Relative equidistribution and the positive limiting constant

Apply the inspected [BR06 Theorem 2.3](../audits/literature/BR06/Yin_U001.md#br06-galois-small-point-equidistribution) with the fixed base field k=K and phi(z)=z^2.
For this map canonical height is ordinary height, and the archimedean canonical measure is normalized Haar measure mu_T on the unit circle.
The theorem therefore applies to complete K-relative Galois orbits at every archimedean place.
The separately printed Theorem 2.4 uses Q-orbits; changing its printed base field without the Theorem 2.3 interface is unnecessary.

Choose any odd sequence n_j tending to infinity and any actual irreducible factor at each n_j.
Choose a conjugate root beta_j above the fixed alpha as in (M4).
After making n_j distinct, the beta_j are distinct: the same nonzero root at two exponents in (M4) would satisfy beta^(n_i-n_j)=1, contradicting the absence of roots of unity.
By (M9), their ordinary heights tend to zero.
BR06 then gives
\[
                    \nu_{\beta_j,\sigma}\ \Longrightarrow\ \mu_T
\]
at each fixed embedding, with the conjugate embedding handled by complex conjugation.
Since every psi_sigma is continuous on the compact sphere, (M8) yields
\[
 (n_j-2)h(\beta_j)\longrightarrow E,\qquad
 E=\frac1d\sum_\sigma\int_{\mathbb T}\psi_\sigma\,d\mu_T. \tag{M10}
\]
No entire fiber has been substituted for one irreducible factor's complete relative orbit.

The constant E is strictly positive.
On the unit circle the second term in (M7) vanishes, and the first maximum is at least |z+sigma u|.
Jensen's formula and the fact that u is a unit give
\[
 E\ \ge\ \frac1d\sum_\sigma\log^+|\sigma u|
       \ =\ h(u)\ >0.                                \tag{M11}
\]
For the last strict inequality, the actual real embedding has 0<u=(1+lambda)^(-1)<1.
Since the product of the moduli of all its conjugates is |N_(K/Q)u|=1, at least one other conjugate has modulus greater than one.
The same positive constant E works for every actual factor of every F_n in the asymptotic assertion.

Indeed if convergence were not uniform over factors, a fixed positive error and a sequence of exponents with violating factors would contradict the preceding arbitrary-sequence argument.
Thus, with beta_f any root of f,
\[
 \sup_{\substack{f\mid F_n\\f\ {\rm irreducible}}}
       |(n-2)h(\beta_f)-E|\longrightarrow0.             \tag{M12}
\]
There is no effective error rate asserted, and no need to assume irreducibility of F_n or of an entire K-fiber.

<a id="moving-map-sublinear-factor-criterion"></a>
## Exact remaining factor question and complete measure

For all actual irreducible factors, uniformly as odd n tends to infinity,
\[
              m(f)=\frac{\deg f}{n-2}\bigl(E+o(1)\bigr). \tag{M13}
\]
It follows that, along any sequence of these actual factors with n tending to infinity,
\[
                      m(f)\longrightarrow0
              \quad\Longleftrightarrow\quad
                      \frac{\deg f}{n}\longrightarrow0. \tag{M14}
\]
The forward implication uses E>0, and the reverse implication uses the same uniform bounded error.
Such factor degrees would necessarily tend to infinity: otherwise (M9), bounded degree and Northcott finiteness would contradict the distinctness of the selected roots.
Thus the unresolved target is an actual sequence of degrees growing to infinity but sublinear in n, rather than a bounded-degree root family.

Counting every multiplicity and using the exact degree sum 10n in (M2), uniformity also gives
\[
                             m(F_n)\longrightarrow10E>0. \tag{M15}
\]
The entire output does not approach zero.
It is possible for its individual factors to do so only through (M14), and no existence of such factors follows from (M15).

Unbounded positive-factor count remains a sufficient route: a least-degree factor has degree at most 10n/r_+(F_n).
It is not necessary for (M14); even a bounded number of factors could include one with sublinear degree and another carrying almost all the degree.
Neither a collection of new factors across distinct n nor height decay by itself supplies (M14).

There is a further necessary fixed-field norm constraint.
For a selected root beta above alpha put gamma=N_(L/K)beta.
It is an O_K-unit and, by the height inequality for a product of its r relative conjugates,
\[
                      h(\gamma)\le r h(\beta)
                                  \le\frac{rC}{n-2}.  \tag{M16}
\]
If r=o(n), the right side tends to zero.
Northcott finiteness in the fixed field K implies that gamma is eventually a root of unity.
The chosen field K is a subfield of R, so these roots of unity are exactly plus and minus one.
Accordingly an eventual sublinear factor of the monic K-fiber must have constant coefficient plus or minus one.
Equivalently, if eta_K is the minimum positive height of a nontorsion O_K-unit, then gamma not in {1,-1} forces r>=eta_K(n-2)/C.
Such eta_K>0 exists by Northcott finiteness, and no effective value is asserted.
The entire fiber already has relative norm one; this condition does not exclude proper sublinear factors and does not turn the mixed norm formula into a no-cancellation equality.

<a id="moving-map-factorization-sources"></a>
## Ordinary reversal, field restriction and inspected factorization sources

The ordinary degree-n reversal satisfies
\[
 q_{n,u}^*=-q_{n,1-u},\qquad
 q_{n,u}+q_{n,u}^*=(2u-1)z(z^{n-2}+1).                \tag{M17}
\]
Since u is not 1/2, a common root of q_(n,u) and its ordinary reversal would give z^(n-2)=-1 and then z^2+z+1=0, again impossible.
Thus these polynomials are coprime over K and there is no ordinary reciprocal K-factor.

For the large-gap template z^N c(z^(-1))+d_0(z), take
\[
 c(z)=1+uz,\qquad d_0(z)=-(az+1),\qquad N=n.
\]
Their constants are nonzero, c is not plus or minus d_0, and gcd(c*,d_0)=1 because au-1 is nonzero.
Moreover
\[
             -\frac{d_0(z)}{c(z^{-1})}
                  =\frac{z(az+1)}{z+u}                \tag{M18}
\]
has a simple zero at zero.
Hence it is not a p-th power for any prime p, or a nonzero constant times a fourth power, even over the algebraic closure of K.
The elementary Capellian obstruction is absent.

This matching does not supply an applicable irreducibility theorem over K.
The [SSS18 v1 source](../audits/literature/SSS18/readme.md), printed pp.1--3 including Theorem 1.2, explicitly works over Q.
The present coefficient field has signature (2,4), so it is neither totally real nor a CM field under the already retained [Kroneckerian-field convention](../audits/literature/Smy08/Yin_U002.md#smy08-kroneckerian-field).
The [Schinzel official introduction excerpt](../audits/literature/Sch00/readme.md), printed pp.5--6, describes the relevant Chapter 6 scope through Kroneckerian fields, meaning totally real or CM fields, and non-self-inversive lacunary factors.
That excerpt was read, but the full statement of the cited Theorem 74 was not obtained or checked.
It is therefore a source-domain warning, not an adopted theorem about this fiber or a claim to have exhausted possible later extensions.

<a id="moving-map-self-inversive-convention"></a>
**Definition (complex self-inversive polynomial).**
For a degree-s complex polynomial p with nonzero constant coefficient, write p*(z)=z^s p(1/z) and let the bar on p conjugate its coefficients.
The polynomial is self-inversive when p*=c bar(p) for a complex constant c with |c|=1.
This is the usual complex-coefficient convention used in the comparison here, distinct from ordinary reciprocal equality up to a scalar without coefficient conjugation.

The self-inversive distinction is substantive here.
The involution tau of K sending alpha to alpha^(-1) sends u to 1-u and gives q_(n,u)*=-tau(q_(n,u)).
At the eight nonreal embeddings, |sigma alpha|=1 and conjugation sends sigma u to 1-sigma u, so the corresponding complex fiber is self-inversive.
At the two real embeddings it is not, as follows also from the ordinary-reversal coprimality.
Passing to the totally real trace field fixes tau but gives the relative norm q_(n,u)tau(q_(n,u))=-q_(n,u)q_(n,u)*, which is reciprocal.
It does not remove the reciprocal-factor issue.

The bounded source comparison also reread [AS18 v3](../audits/literature/AS18/readme.md), printed pp.1--5, and [Fil22 v1](../audits/literature/Fil22/readme.md), printed pp.1--4.
The first retains a free variable in its proved function-field statement, while its rational one-variable counterpart is presented as a conjecture in that edition.
The second gives a statement for the nonreciprocal part over integer coefficients, with further bivariate hypotheses.
Neither inspected statement supplies a lower bound proportional to n for all actual K-fiber factor degrees, or a construction of a sublinear factor.
The earlier [source comparison](Yin_L_G0450_v2.md#delayed-factorization-source-boundary) retains their precise earlier use and limitations.
No original Schinzel proof, whole-book theorem audit or exhaustive literature-absence claim is made.

<a id="moving-map-finite-evidence-and-next-input"></a>
## Finite evidence and the next substantive input

[J142](../computations/programs/Yin_J_G0142/readme.md) constructed and factored exactly n=5,7,9,13 over ZZ.
Each complete output is irreducible, noncyclotomic and has multiplicity one, with degrees 50,70,90,130 and r_+=1.
The product-back, complete degree, unit, reciprocity and endpoint checks passed.
Its complete 50-digit root diagnostics give uncertified measures approximately 3.17356, 2.83802, 2.87393 and 2.82960 respectively.
These numerical values are not premises of (M1)--(M18), not certified enclosures and not evidence of all-n irreducibility.
The n=3 result is reused at its existing J141 home.

The coordinating contributor read the native J142 program and its complete report and checked the exact output classifications and full root-list counts.
The mathematical height argument received an ordinary cross-check of finite places, all archimedean weights, continuity at poles and infinity, complete relative orbits, uniformity and strict positivity.
The construction contributor subsequently read the complete saved argument, including the sublinear-factor equivalence and the fixed-field norm constraint, with no substantive defect found.
This does not constitute an independent formal review or an audit of the BR06 proof.

The construction has bounded complete measure, a positive whole-measure limit, and a precise remaining small-factor criterion.
The next useful algebraic input would either produce an actual sublinear-degree K-factor with its full integer output, or establish a proportional lower degree bound for all actual factors.
Increasing the finite scan without such a mechanism is not selected.
The constant-one full relative norm and the ordinary nonreciprocity over K identify useful interfaces, but neither resolves the remaining factor question.
