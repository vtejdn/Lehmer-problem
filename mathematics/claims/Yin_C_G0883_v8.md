---
author: Yin
---

# Which sparse cyclotomic multiples occur before capping a fiber?

<a id="cycles"></a>
## Recovering the proposed boundary periods from the cofactor

Let \(f\) be an orientation-preserving pseudo-Anosov homeomorphism of a closed orientable surface of genus \(g\ge2\), and let \(P\) be its characteristic polynomial on \(H_1\).
Write a proposed monic cyclotomic cofactor as \(C=\prod_{n\ge1}\Phi_n^{c_n}\) with finite support.
Put \(e_n=c_n+\mathbf1_{n=1}\) and define
\[
                 m_h=\sum_{j\ge1}\mu(j)e_{jh}\qquad(h\ge1).
\]
The cofactor has the form of the homology lost in capping a nonempty set of boundary circles if and only if every \(m_h\ge0\).
In that case the proposed boundary permutation has exactly \(m_h\) cycles of length \(h\), and this cycle profile is unique.
Indeed \(e_n=\sum_{n\mid h}m_h\) by finite Möbius inversion.
These are exactly the multiplicities in \((x-1)C=\prod_h(x^h-1)^{m_h}\).
The kernel of capping is the oriented boundary permutation module modulo the sum of the boundary circles. [Capping calculation](Yin_C_G0883_v5.md#hironaka)
In particular the number of cycles is \(e_1\), and the number of boundary circles is \(\deg C+1\).
Suppose the closed polynomial \(P\) is irreducible and noncyclotomic with \(M(P)\le19/16\), and the open polynomial modulo a prime is divisible by \(x^N\pm1\) with \(\deg P\le2N\).
Then the [overlap bound](Yin_C_G0904_v6.md#boundary) gives \(\sum_h m_h\gcd(h,N)>N/40\) for these uniquely determined lengths.

<a id="orbits"></a>
## Actual periodic orbits certified by the closed polynomial

Compute \(L_n=2-\sum_{P(\alpha)=0}\alpha^n\), counting roots with multiplicity, and set
\[
              b_h=\frac1h\sum_{j\mid h}\mu(h/j)L_j .
\]
Every such \(f\) has at least \(\max(0,b_h)\) distinct orbits of least period \(h\).
Consequently \(0\le m_h\le\max(0,b_h)\) for every \(h\) is sufficient to realize \(PC\) on a punctured fiber and recover the same closed \(f\) on capping.
For the [closed homological realizations](Yin_C_G0883_v2.md#mapping-tori), both mapping tori are hyperbolic.

Here is the local index calculation allowing either orientation behavior of the invariant foliations.
A point with \(k\) unstable prongs has \(k\) stable prongs, with \(k=2\) at a regular point.
At a point of least period \(a\), the first return permutes the \(k\) unstable prongs by a cyclic rotation of order \(q\mid k\).
An iterate fixing the point has index \(1-k\) when it fixes the prongs and index \(1\) otherwise. [Lefschetz formula and local index calculation, pp. 114–116](https://www.numdam.org/article/AIF_2011__61_1_105_0.pdf#page=11)
For a direct verification, take an oriented disk coordinate \(w\) with flat coordinate \(z=w^{k/2}\) up to sign and choose the expanding axis to be real.
The return is a lift of \((\Re z,\Im z)\mapsto(\lambda\Re z,\lambda^{-1}\Im z)\), \(\lambda>1\), with a rotation by \(2\pi j/k\) in \(w\).
This local model can be read on a sufficiently small circle wherever the sign of the flat coordinate changes.
Changing \(\lambda\) to \(\lambda^s\) for \(s\in(0,1]\) deforms the return without a fixed point on the circle.
For \(j\ne0\bmod k\), the angular displacement of the stretch in \(w\) has absolute value less than \(\pi/k\), so the deformation extends to \(s=0\) as a nontrivial rotation of index one.
For \(j=0\bmod k\) the infinitesimal displacement on \(w=re^{i\theta}\) has direction \(e^{i(1-k)\theta}\), since \(\dot z=(\log\lambda)\bar z\) and \(\dot w/w=(2/k)\dot z/z\).
Its winding number is \(1-k\), giving the other index.

The Lefschetz fixed point formula therefore counts the contribution of this single orbit to \(L_n\) as
\[
                   a\,\mathbf1_{a\mid n}-ak\,\mathbf1_{aq\mid n}.
\]
After Möbius inversion and division by \(h\), its contribution to \(b_h\) is \(\mathbf1_{h=a}-(k/q)\mathbf1_{h=aq}\).
Summing over the finitely many orbits fixed by the relevant iterates proves the lower bound and integrality of \(b_h\).
Choose the certified number of disjoint orbits for each length and puncture the surface at all their points.
The same invariant measured foliations give a pseudo-Anosov map on the punctured surface, with an old regular point becoming a two-pronged puncture.
Truncating the punctures gives boundary circles with the selected permutation, and capping recovers the original closed mapping class.
The homology exact sequence gives the full polynomial \(PC\), including any extension between the quotient and kernel.
The orbit test is sufficient and can undercount periodic orbits.
Puncturing a known closed realization gives no bound for the drilled volume in terms of the support of \(PC\).

<a id="lehmer"></a>
## The least number of open coefficients for the degree-ten record

Take the actual record \(L=x^{10}+x^9-x^7-x^6-x^5-x^4-x^3+x+1\).
The smallest support of \(LC\) among all boundary cofactors is **six**.
It is attained on a hyperbolic open bundle which caps to a closed bundle with whole polynomial \(L\).
Indeed \(b_1=2-\operatorname{tr} f_*=3\), since the coefficient of \(x^9\) is one and a [closed realization exists](Yin_C_G0883_v2.md#mapping-tori).
Two fixed points give \(C=x-1\) and
\[
               (x-1)L=x^{11}-x^9-x^8+x^3+x^2-1 .
\]
Thus a polynomial with nine occupied positions caps exactly from one with six. [Degree-ten identity](Yin_C_G0904_v5.md#finite)

For the lower bound let \(t=\sum_h m_h\).
The two positive roots of \(L\) and the root \(1\) of multiplicity \(t-1\) in \(C\) force at least \(t+2\) terms by Descartes' rule, giving the claim for \(t\ge4\).
For \(t\le3\) normalize the constant coefficient of \(LC\) to one.
Its coefficients through degree three are those of
\[
          (1+2x+2x^2+x^3+O(x^4))\prod_h(1-x^h)^{m_h},
\]
by the expansion of \(L/(1-x)\).
If \(m_1=0\), the linear coefficient is two and the quadratic one is \(2-m_2\).
When \(m_2=2\), the cubic coefficient is \(-3-m_3\).
If \(m_1=1\), the linear coefficient is one and the quadratic one is \(-m_2\).
When \(m_2=0\), the cubic coefficient is \(-1-m_3\).
If \(m_1=2\), the quadratic and cubic coefficients are \(-1-m_2\) and \(-1-m_3\).
If \(m_1=3\), the linear and quadratic coefficients are both \(-1\).
Thus at least three of the initial four positions are occupied.
Reciprocity up to sign gives another three at the far end, disjoint since \(\deg(LC)\ge10\).
In particular the five-term completion \(\Phi_6 L=x^{12}-x^7-x^6-x^5+1\) cannot be an open homological polynomial capping to \(L\).
For this particular cofactor inversion already gives \(m_3=-1\).

<a id="partial"></a>
## Five-term open polynomials on a fixed two-cusped parent

For comparison, the other variable sign of the same record does admit an actual five-term open polynomial.
More generally take the [Hironaka fibers](Yin_C_G0883_v5.md#hironaka) with \(a=1,\ b=3u,\ u\ge2\).
On the original two cusps the boundary cycles have lengths \(1,3\).
Fill only the cusp carrying the length-one cycle along its fiber boundary.
The capped point has \(3b\) prongs, so the remaining punctured monodromy is pseudo-Anosov.
The one-cusped manifold is hyperbolic and has volume strictly less than the original fixed two-cusped exterior by hyperbolic Dehn filling.
Its remaining three boundary circles form one cycle.
The homological kernel of their final capping has polynomial \(\Phi_3\).
By the closed polynomial calculation, the whole open polynomial after the first filling and the whole closed polynomial after the second are respectively
\[
       F_b=x^{2b}+x^{b+1}-x^b+x^{b-1}+1,\qquad P_b=F_b/\Phi_3 .
\]
The latter filling also gives a hyperbolic bundle, with capped points of \(b/3\ge2\) prongs.
At \(b=6\) it gives exactly \(P_b=L(-x)\), and \(F_b\) has five terms.
For \(j<b-1\), the coefficients of \(P_b\) equal those of \(1/\Phi_3=(1-x)/(1-x^3)\).
Hence the closed support has at least \(2\lfloor(b-1)/3\rfloor\) terms although the open support always has five.
These examples have uniformly bounded volume and a uniform measure gap when the measure exceeds one, by the [five-term bound](../audits/literature/Dob06/Yin_U001.md#sparse-measure).
Realizing an arbitrary new record from a comparably economical open parent still requires such a parent or an independent volume bound for that construction.

## Assessment history

### Decision capping-periods

| Field | Value |
| --- | --- |
| date | 2026-11-28T07:47 |
| status | proved |
| reason | Möbius inversion determines the boundary profile and the local fixed point indices give sufficient orbits. Counting the end coefficients proves the minimum for the given sign of the degree-ten record. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Boundary periods](#cycles) | Algebraic criterion and uniqueness of the cycle profile. |
| argument | [Orbit certificate](#orbits) | Lefschetz inversion, local indices and exact capping. |
| argument | [Lehmer minimum](#lehmer) | Six terms are necessary and attainable for the given polynomial. |
| argument | [Partial fillings](#partial) | Five-term open family, volume and the other sign of the degree-ten record. |
| dependency | [Closed realization](Yin_C_G0883_v2.md#mapping-tori) | Existence for the irreducible record. |
| dependency | [Hironaka fibers](Yin_C_G0883_v5.md#hironaka) | Capping action, prongs, boundary periods and polynomial. |
| dependency | [Cyclotomic overlap](Yin_C_G0904_v6.md#boundary) | Necessary overlap with the stated measure and degree bounds. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1296.md#finding) | Four sections including the corrected scope of the modular overlap test. |

## Current assessment

[Selected decision](#decision-capping-periods)
