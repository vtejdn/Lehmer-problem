---
author: Yin
---

# Endpoint constraints and the complete domain of a small exceptional pair

<a id="statement"></a>
## Exact statement and original-input scope

Set \(p=19683\), \(n=9841\), \(k=1990\), and \(b_j=2\cos(2\pi j/p)\) in decreasing order for \(1\le j\le n\).
Let \(B_0=1\), \(B_1=t+1\), \(B_i=tB_{i-1}-B_{i-2}\), \(B=B_n=\prod_j(t-b_j)\), and \(D=B_{n-1}\).
Let \(h\in\mathbb Z[t]\) satisfy
\[
 h(b_j)>0\quad(1\le j\le7851),\qquad
 h(b_j)<0\quad(7852\le j\le9841),\qquad
 \prod_{j=1}^n|h(b_j)|=2^{4391}.
\]
Define
\[
 r_j=(4-b_j^2)h(b_j)/p,\qquad C=Dh\bmod B,\qquad
 Q=(t+2)B+C,\qquad P(z)=z^{n+1}Q(z+z^{-1}).
\]
The remainder \(C\) has degree less than \(n\), so \(Q\) and \(P\) are monic.
Assume the negative-one branch conditions
\[
 K=\sum_jr_j=3,\qquad L=\sum_jb_jr_j=4,\qquad
 N=\sum_jb_j^2r_j=7,\qquad P(-1)>0,\qquad M(P)\le101/100.
\]
Here \(M(P)\) is the complete multiplicative Mahler measure, with every root counted with its original multiplicity.
Write
\[
 U=\sum_jr_j/(2+b_j),\qquad
 (O,V,W)=\left(\sum_jb_j^3r_j,\sum_jb_j^4r_j,\sum_jb_j^5r_j\right).
\]
The applicable [C882v6 conclusion](Yin_C_G0882_v6.md#statement) gives \(U=1\) and
\[
 (O,V,W)\in\mathcal R
 =\{(10,18,27),(11,20,33),(11,20,34),(11,21,36),(11,21,37)\}.
\]
No member of this necessary list is asserted to be realizable.

Put \(x_0=-2\), \(x_i=b_{n+1-i}\), and \(c=x_{1991}=b_{7851}\).
For every choice of one mandatory root \(u_i\in(x_{i-1},x_i)\) for each \(i\ne1991\), remove exactly one copy and write
\[
 Q(t)=\left(\prod_{i\ne1991}(t-u_i)\right)Z(t),\qquad
 Z(t)=(t-s)^2-d,\qquad v_{1,2}=s\pm\sqrt d.
\]
The parameters \(s,d\) are real, and all remaining copies of repeated roots belong to \(Z\).
The claimed necessary conditions, for every such choice and each of the five triples, are the following.

- The actual terminal-interval indicator \(w=\sum_{i\ne1991}\mathbf1_{[u_i,x_i]}\) obeys the seven exact moment identities (5) and the finite endpoint equality (7).
  In those equations \(c\) lies in (1), \(D_j\) is exactly (4), \(m_j=\int_{-2}^2t^jw(t)\,dt\), \(m=m_0\), \(\gamma=2+c\), and \(A=(2+s)^2-d\).
- If \(d\ge0\), both exceptional roots lie in a bounded pole cell, \(0\le d\le4\pi^2/p^2\), and the complete measure is \(M(P)=1\).
  Consequently every original candidate with \(1<M(P)\le101/100\) has \(d<0\) and
  \[
       -6/5<s<-1/3,\qquad s^2/40401-1/10100\le d<0.
  \]
  The real-part bound \(-6/5<s<-1/3\) also holds in the real-pair case under the stated hypotheses.
- The strict first-moment inequalities (11), the density variance inequality (12), all four strict positive-definiteness conditions (15), the strict endpoint inequalities (16) and (18), and both polynomial-minorant inequalities (20) hold.
  Explicitly the stronger endpoint condition is
  \[
  \bigl((2+s)^2-d-(2+c)\bigr)\bigl(3+d-(s-c)^2\bigr)
       >(2+c)(2s+2-c)^2,
  \qquad 3+d-(s-c)^2>0.
  \]
- For every real polynomial \(q\) of degree at most six, both density-aware dual necessary inequalities (21) and (22) hold.
  These quantify over all such polynomials; they are not restricted to a finite list of computed duals.

The displayed conclusions concern the whole polynomial \(P\), with no squarefreeness assumption and no unproved hypothesis that the exceptional roots are nonreal.
They neither exclude all five branches nor prove that any remaining parameter is realizable by a density, an actual root configuration, an integral \(h\), or the specified resultant.
In particular this Claim asserts no new uniform lower bound above one for these residual branches.

<a id="dependencies"></a>
## Inputs, extraction and mathematical boundary

[C882v6](Yin_C_G0882_v6.md#statement) supplies the consequence \(U=1\), the five-triple restriction under \(M(P)\le101/100\), and the exact trace differences for this same original construction.
Its [cut enclosure](Yin_C_G0882_v6.md#relaxation-barrier) supplies the actual \(c=b_{7851}\) in (1).
[C882v8](Yin_C_G0882_v8.md#quadratic-signs) supplies strict signs of the residual quadratic for every allowed mandatory-root selection, including repeated roots; its [root-location conclusion](Yin_C_G0882_v8.md#root-location) supplies the same-component condition for real roots and the pole-gap bound.
The present assumptions are exactly their \(N=7\) input, with the additional complete-measure upper bound, so these inputs apply.
Their finite relaxed models are not proof premises here.

The oriented terminal-interval identity follows the interface in [L464v15](../ledger/Yin_L_G0464_v15.md#oriented-geometry), and the complete pairing, multiplicity and endpoint derivations are given below.
No numerical or interval existence certificate from that ledger is used as a premise.
This argument was extracted on 2026-11-09 from the analytic work in [L464v16](../ledger/Yin_L_G0464_v16.md#analytic-reduction), which now retains the research questions and finite-test boundaries rather than a duplicate proof.
That extraction link is provenance, not a dependency on an assertion left in L.
All new polynomial, density and logarithmic arguments are supplied in this C; no J computation is needed for them.
The finite dual trials and their unresolved parameter cells remain outside this Claim's statement and proof.

<a id="moving-pair"></a>
## Original roots, moments and endpoint value

The residue identity is
\[
 \frac{Q(t)}{B(t)}=t+2+\sum_{j=1}^n\frac{r_j}{t-b_j}.
\]
Its limits on either side of a cell between poles with the same residue sign have opposite signs.
At the left endpoint its value is \(-U=-1\), while its limit as \(t\) approaches the negative-residue pole \(b_n\) from the left is positive infinity.
Thus every allowed cell below contains a root of \(Q\), including the first cell at \(-2\).
Choosing one root in each of those disjoint open cells gives \(n-1=9840\) distinct mandatory roots.
Only one copy of each chosen root is removed; any additional multiplicity remains in the residual real monic quadratic.
This construction works for every allowed root choice and does not assume that \(Q\) is squarefree.
Write \(n=9841\), \(x_0=-2\), \(x_i=b_{n+1-i}\), and \(c=x_{1991}=b_{7851}\).
The inherited enclosure is
\[
 c\in I_c=[-1609663/10^6,-1609662/10^6].
 \tag{1}
\]
Choose one mandatory root \(u_i\in(x_{i-1},x_i)\) for each \(i\ne1991\), and retain the actual indicator
\[
 w(t)=\sum_{i\ne1991}\mathbf1_{[u_i,x_i]}(t).
 \tag{2}
\]
This has \(0\le w\le1\), positive mass, positive-measure complement, and zero occupancy in the cut cell and above \(b_1\).
It also vanishes in a nonempty interval immediately to the right of \(-2\), so all endpoint integrals below are finite.
The two remaining roots have the form
\[
 v_1=s+\sqrt d,\qquad v_2=s-\sqrt d,\qquad s,d\in\mathbb R,
 \qquad Z(t)=(t-s)^2-d.
 \tag{3}
\]
Here \(d\ge0\) describes real roots, including a repeated root, and \(d<0\) describes a nonreal conjugate pair.
The square-root notation is only a symmetric-root parameterization and imposes no choice of a complex branch in the formulas.
Precisely, with \(F(t)=\prod_{i\ne1991}(t-u_i)\), we have \(Q=FZ\) as monic real polynomials, with every original multiplicity preserved.
In particular \(v_1,v_2\) may coincide with each other or with a chosen root.
The strict signs \(Z(-2)>0\) and \(Z(b_j)>0\) are the applicable conclusion of [C882v8](Yin_C_G0882_v8.md#quadratic-signs) for this same choice of \(F\).
They exclude an exceptional root at \(-2\) or at any pole.

The five residual triples inherited from [C882v6](Yin_C_G0882_v6.md#statement) are
\[
 \mathcal R=\{(10,18,27),(11,20,33),(11,20,34),(11,21,36),(11,21,37)\}.
\]
For their trace-difference functional \(\mathcal D\), put \(D_j=\mathcal D(t^j)\), so
\[
 D_0=1,\quad D_1=D_2=D_3=-2,\quad D_4=-10,\quad
 D_5=48-5O,\quad D_6=-44+12O-6V,\quad D_7=-7O+14V-7W-2.
 \tag{4}
\]
Every actual input must satisfy, for \(0\le j\le6\),
\[
 m_j:=\int_{-2}^2t^jw(t)\,dt
 =\frac{2\displaystyle\sum_{\ell=0}^{\lfloor(j+1)/2\rfloor}
    {j+1\choose2\ell}s^{j+1-2\ell}d^\ell-c^{j+1}-D_{j+1}}{j+1}.
 \tag{5}
\]
In particular,
\[
 m_0=2s+2-c,\qquad m_1=s^2+d+1-c^2/2,\qquad
 m_2=2s^3/3+2sd+(2-c^3)/3.
 \tag{6}
\]
For completeness, define the trace difference with multiplicity by
\[
 \mathcal D(f)=\sum_{Q(v)=0}f(v)-\sum_{B(b)=0}f(b).
\]
The factorization \(Q=FZ\) and the pairing with the right poles give
\[
 \mathcal D(f)+f(c)
 =f(v_1)+f(v_2)+\sum_{i\ne1991}(f(u_i)-f(x_i))
 =f(v_1)+f(v_2)-\int_{-2}^2w(t)f'(t)\,dt.
\]
Using \(f(t)=t^{j+1}\) and expanding the symmetric root sum proves (5).
There is no replacement of the exceptional roots by a free positive measure.
The values (4) are the inherited trace differences; equivalently they follow from the formal-logarithm recurrence
\[
 D_j=-j a_j-\sum_{i=1}^{j-1}a_iD_{j-i},\qquad
 (a_0,\ldots,a_7)=(1,2,3,4,7,O,V,W).
\]
Here \(D_0=1\) is the degree difference, so constant terms and repeated roots are included.

To avoid conflict with the original polynomial remainder, define the new scalar abbreviations
\[
 \gamma=2+c,\qquad A=(2+s)^2-d=Z(-2),\qquad m=m_0.
\]
The quadratic signs give \(A>0\).
Evaluating \(Q/B=FZ/B\) at \(-2\), one factor of \(B\) remains unpaired at \(c\).
The other factors have the exact positive ratios \((2+u_i)/(2+x_i)\), giving the root-product identity
\[
 U=\frac{A}{\gamma}\prod_{i\ne1991}\frac{2+u_i}{2+x_i}.
\]
Consequently the original value \(U=1\), as distinct from the strict endpoint sign, requires
\[
 J:=\int_{-2}^2\frac{w(t)}{2+t}\,dt
   =\log\frac A\gamma.
 \tag{7}
\]
For example \(J>0\) already implies \(A>\gamma\).
No polynomial moment identity alone is substituted for (7).

<a id="mahler-domain"></a>
## The complete small-Mahler pair domain

The positive mass and the density cap imply \(0<m<4\), hence
\[
                 (c-2)/2<s<(c+2)/2.
 \tag{8}
\]
The real roots in (3) must lie in one common component of \(\mathbb R\setminus\{-2,b_n,\ldots,b_1\}\), by [C882v8](Yin_C_G0882_v8.md#statement).
The component \((-\infty,-2)\) is impossible, since then \(m=2s+2-c<-2-c<0\).
The component \((b_1,\infty)\) is also impossible, since \(b_1>1\), \(c<0\), and then \(m>2b_1+2-c>4\).
Thus real exceptional roots both lie in one bounded cell inside \((-2,b_1)\).
Their separation satisfies \(2\sqrt d\le4\pi/p\), so
\[
                  0\le d\le4\pi^2/p^2.
 \tag{9}
\]
Every monic trace factor \(t-v\) lifts to \(z^2-vz+1\).
A real trace \(v\in(-2,2)\) gives two unit-circle roots, counted with their full multiplicities.
All mandatory roots already lie in \((-2,2)\), so a real exceptional pair necessarily gives \(M(P)=1\).
This assertion uses every trace root, not merely a bound for the house.
It does not assert that such an integer input exists.
In particular a counterexample with \(1<M(P)\le R\) must have \(d<0\).

For a nonreal pair the two reciprocal exterior radii are equal; write them as \(\rho>1\).
All mandatory pairs have radius one, so the complete measure is \(M(P)=\rho^2\).
Writing one lift as \(\rho e^{i\theta}\) gives
\[
 s=(\rho+\rho^{-1})\cos\theta,\qquad
 \sqrt{-d}=(\rho-\rho^{-1})|\sin\theta|.
\]
The ellipses are nested as \(\rho\) increases, so \(M(P)\le R=101/100\) implies
\[
 \frac{s^2}{40401/10100}+\frac{-d}{1/10100}\le1,
 \qquad
             \frac{s^2}{40401}-\frac1{10100}\le d<0.
 \tag{10}
\]
Conversely this filled-ellipse condition bounds the complete cost of this conjugate pair by \(R\); it is not a sufficient condition for the original integer input.
The larger rectangle \(d\in[-1/10100,0]\) is therefore safe for a subsequent exclusion test of \(1<M(P)\le101/100\), provided its boundary is included.
Combining (9) and (10), every real or nonreal input under consideration has \(|d|<1/10000\).

<a id="density-constraints"></a>
## Density constraints and a uniform rational interval for \(s\)

For any density \(0\le w\le1\) on \([-2,2]\) of mass \(m\), filling the left or right interval of length \(m\) bounds its first moment:
\[
               -2m+m^2/2\le m_1\le2m-m^2/2.
\]
In (2) both inequalities are strict, since there are nonempty occupied terminal intervals separated by nonempty unoccupied gaps.
Substituting (6) gives the useful necessary conditions
\[
        (s-c)^2<3+d,\qquad 3s^2-2cs+d<1.
 \tag{11}
\]
They first imply \(-4/3<s<1/8\).
Indeed, for \(s\le-4/3\) the quadratic \(3s^2-2cs\) is decreasing as \(s\) increases in that range and its minimum over \(c>-161/100\) is greater than \(26/25\) at \(s=-4/3\); adding \(d>-1/10000\) still exceeds one.
For \(s\ge1/8\), the other inequality fails since \(c<-1609/1000\) gives \((s-c)^2>(867/500)^2>3+1/10000\).

A second independent density consequence is
\[
                    m m_2-m_1^2\ge m^4/12.
 \tag{12}
\]
To prove it, extend \(w\) by zero to the real line and set \(\mu=m_1/m\).
Compare it with the indicator of \([\mu-m/2,\mu+m/2]\).
The product of their difference with \((t-\mu)^2-(m/2)^2\) is nonnegative pointwise, because the latter changes sign exactly at the endpoints of this interval.
After integration the mass term cancels, giving \(\int(t-\mu)^2w\ge m^3/12\), which is (12).
This proof does not assume that an arbitrary density is an actual root configuration.

Put \(a=s+2\), so \(m=2a-\gamma\).
The exact left side of (12) after moving \(m^4/12\) to the left is the polynomial
\[
\begin{split}
 V(a,\gamma,d)={}&-a^4+2\gamma a^3-\gamma^2a^2-6a^2+20a
                   +3\gamma^2-10\gamma-9\\
              &+d(\gamma^2-2\gamma a+2a^2-6)-d^2.
\end{split}
 \tag{13}
\]
Thus \(V\ge0\) is necessary.
The same identity can be checked after translation using
\[
 \int(t+2)w=a^2+d+3-\gamma^2/2,
 \qquad
 \int(t+2)^2w=2a^3/3+2ad-\gamma^3/3+10.
\]

Here is a completely rational enclosure proof, without a parameter scan.
The preceding first-moment bounds put \(2/3<a<17/8\), while (1) gives \(0<\gamma-39/100<1/2500\).
On the rectangle \(2/3\le a\le17/8\), \(39/100\le\gamma\le2/5\), \(|d|\le1/10000\), direct differentiation of (13) gives \(|\partial_\gamma V|<40\) and \(|\partial_dV|<20\).
Consequently, with \(V_0(a)=V(a,39/100,0)\),
\[
       |V-V_0|<40/2500+20/10000=9/500<1/50.
\]
Also
\[
 V_0''(a)=-12(a-39/200)^2+(39/100)^2-12<0.
\]
The four exact endpoint values needed for the two tails are
\[
\begin{array}{c|cc}
 a&V_0(a)+1/50&V_0'(a)\\\hline
 4/5&-92821/250000&60039/6250\\
 5/3&-115211/405000&-338189/27000.
\end{array}
\]
Strict concavity makes \(V_0\) increasing on the left tail \(a\le4/5\) and decreasing on the right tail \(a\ge5/3\).
Both tails therefore have \(V<0\) throughout the preliminary interval, contrary to (12).
This proves the uniform necessary enclosure
\[
                         -6/5<s<-1/3.
 \tag{14}
\]
It holds for every one of the five triples, for real and nonreal exceptional pairs, and for the entire cut enclosure (1).
It does not certify any point remaining in this interval.

The density cap also supplies complementary moment tests rather than only ordinary positive-measure tests.
Let \(e_j=\int_{-2}^2t^jdt\), so \(e_j=0\) for odd \(j\) and \(e_j=2^{j+2}/(j+1)\) for even \(j\).
For an actual configuration all four matrices
\[
 [m_{i+j}]_{0\le i,j\le3},\quad [e_{i+j}-m_{i+j}]_{0\le i,j\le3},\quad
 [4m_{i+j}-m_{i+j+2}]_{0\le i,j\le2},\quad
 [4(e_{i+j}-m_{i+j})-(e_{i+j+2}-m_{i+j+2})]_{0\le i,j\le2}
 \tag{15}
\]
are positive definite.
They are Gram matrices against \(w\), \(1-w\), \((4-t^2)w\), and \((4-t^2)(1-w)\), respectively, and each weight is positive on an open interval.
The variance inequality (12) likewise applies to the complementary moments \(4-m\), \(-m_1\), and \(16/3-m_2\).
These are additional necessary conditions; this record does not claim that their simultaneous feasibility reconstructs an indicator, the roots, or an integer input.

<a id="endpoint-rearrangement"></a>
## Two exact endpoint consequences of the density cap

The kernel \(1/(2+t)\) is decreasing, so among densities of mass \(m\) on \([-2,2]\) its smallest integral is obtained by occupying \([2-m,2]\).
For the actual indicator the inequality is strict, yielding
\[
       J>\log\frac4{4-m},\qquad
       A(\gamma-2s)>4\gamma.
 \tag{16}
\]
The second form follows from (7) and \(4-m=\gamma-2s>0\).
It is a condition on the moving pair, not just on the old fixed double-atom witnesses.

Retaining the first moment strengthens (16) without introducing any transcendental parameter test.
Let \(\mu=m_1/m\).
The strict first-moment bounds place the interval \(H=[\mu-m/2,\mu+m/2]\) strictly inside \((-2,2)\).
For the strictly convex kernel \(k(t)=1/(2+t)\), let \(\ell\) be the affine function joining its values at the two endpoints of \(H\).
Convexity gives \(k-\ell\le0\) in \(H\) and \(k-\ell\ge0\) outside \(H\).
Hence \((k-\ell)(w-\mathbf1_H)\ge0\) pointwise.
The two densities have the same mass and first moment, so the affine part cancels upon integration.
Equality would require \(w=\mathbf1_H\) almost everywhere, which is impossible for the separated strict terminal intervals in (2).
It follows that
\[
 J>\log\frac{2+\mu+m/2}{2+\mu-m/2}
   =\log\frac{2m+m_1+m^2/2}{2m+m_1-m^2/2}.
 \tag{17}
\]
Define \(H_-=2m+m_1-m^2/2=3+d-(s-c)^2>0\), using (11).
The original endpoint value and (17) imply the exact polynomial condition
\[
              (A-\gamma)H_->\gamma m^2,
 \quad\text{that is}\quad
 \bigl((2+s)^2-d-(2+c)\bigr)\bigl(3+d-(s-c)^2\bigr)
       >(2+c)(2s+2-c)^2.
 \tag{18}
\]
The centered interval satisfies the same density cap, so (17) is at least as strong as the mass-only bound (16).
Neither inequality asserts existence when it passes.

<a id="endpoint-duals"></a>
## Polynomial endpoint bounds and a density-aware dual

A convenient polynomial minorant uses any quadratic \(a_2(t)=\alpha_0+\alpha_1t+\alpha_2t^2\).
The identity
\[
 \frac1{2+t}-\left[\frac14-(2-t)a_2(t)-(4-t^2)a_2(t)^2\right]
 =\frac{2-t}{2+t}\left(\frac12+(t+2)a_2(t)\right)^2\ge0
 \tag{19}
\]
holds on \((-2,2]\).
Define \(\eta_i=2m_i-m_{i+1}\) for \(0\le i\le2\) and \(B_{ij}=4m_{i+j}-m_{i+j+2}\) for \(0\le i,j\le2\).
Then
\[
 J>m/4-\eta^T\alpha-\alpha^TB\alpha,
 \qquad
 J>m/4+\tfrac14\eta^TB^{-1}\eta
 \tag{20}
\]
for an actual configuration, the second inequality following by the choice \(\alpha=-B^{-1}\eta/2\).
The inverse exists by (15).
The inequality is strict because the squared polynomial in (19) cannot vanish identically on any nonempty open occupied interval: its value at \(t=-2\) before squaring is \(1/2\).
All moments needed in (20) occur in (5).
Evaluation only at a previously fixed value of \(s\) does not establish this inequality's sign over the moving-pair domain.

For any polynomial \(q(t)=\sum_{j=0}^6q_jt^j\), the full density cap gives the more flexible bound
\[
 J\ge\sum_{j=0}^6q_jm_j
          -\int_{-2}^2\left(q(t)-\frac1{2+t}\right)_+dt.
 \tag{21}
\]
Indeed \((k-q)w\ge-(q-k)_+\) pointwise for \(0\le w\le1\).
The positive-part integral is finite because the polynomial is bounded and \(k(t)\to+\infty\) at the left endpoint.
Unlike a global polynomial minorant, (21) allows \(q\) to exceed the kernel on part of the interval and pays the exact excess there.
It directly exploits the density cap that an unrestricted positive-measure relaxation discards.
A related purely polynomial necessary inequality is
\[
                \sum_{j=0}^6q_jm_j\le\int_{-2}^2q(t)_+dt.
 \tag{22}
\]
Fixed rational \(q\), exact root isolation and rigorous integrals can make these finite certificates, but a numerical LP optimum alone cannot do so.


<a id="proof-boundary"></a>
## Exact coverage and unresolved original existence

For \(1<M(P)\le101/100\), the proof gives the five triples, the actual \(c\) in (1), the real-part interval (14), and the nonreal ellipse (10), together with all the moment and endpoint constraints.
The larger closed box \([-6/5,-1/3]\times[-1/10100,0]\times I_c\) is a safe superset for an exclusion certificate.
Its \(d=0\) boundary is retained when testing that superset even though an original positive-measure candidate has \(d<0\).
Strict inequalities for the actual indicators may be relaxed to nonstrict ones when forming such a superset.
Passing any or all of the necessary conditions is not a realization theorem.
In particular neither the integer-coefficient condition nor the nonunit resultant follows from a continuous occupancy model.
The finite symbolic expansion of (13) is directly verifiable from the displayed moments; its coefficients, tail values and derivative bounds are part of the analytic proof rather than an external generated-data premise.

## Assessment history

### Decision endpoint-domain-19683

| Field | Value |
| --- | --- |
| date | 2026-11-09T16:15 |
| status | proved |
| reason | Complete independent review verifies the original-root moment and endpoint identities, full real/nonreal pair domain, density constraints and all stated polynomial duals; no branch realization or new positive Mahler floor is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact necessary-domain statement](#statement) | Every stated original input, all five residual triples, every permitted root selection and all multiplicities. |
| argument | [Inputs and boundary](#dependencies) | Exact applicability of adopted C882v6 and C882v8, with extraction provenance separate from proof premises. |
| argument | [Moving roots and endpoint](#moving-pair) | Oriented terminal intervals, all seven moments and the exact finite logarithmic endpoint value. |
| argument | [Complete measure domain](#mahler-domain) | Real exterior components excluded, complete measure one for real pairs, and the nonreal ellipse with its safe rectangle. |
| argument | [Density constraints](#density-constraints) | Strict first moments, density variance, all four Gram matrices and the rational real-part enclosure. |
| argument | [Endpoint rearrangements](#endpoint-rearrangement) | Strict mass and centered-interval bounds and the exact quartic necessary condition. |
| argument | [Polynomial duals](#endpoint-duals) | Strict quadratic minorants and both density-aware inequalities for every real polynomial of degree at most six. |
| argument | [Coverage boundary](#proof-boundary) | Safe closed exclusion domain, no original realization and no new lower-measure claim. |
| dependency | [Adopted five-triple input](Yin_C_G0882_v6.md#statement) | Exact original hypotheses, U=1, the five remaining triples and trace differences. |
| dependency | [Actual cut enclosure](Yin_C_G0882_v6.md#relaxation-barrier) | The inherited enclosure of c=b7851; relaxed-model existence is not a premise. |
| dependency | [Quadratic signs](Yin_C_G0882_v8.md#quadratic-signs) | Strict signs for every chosen mandatory-root factor with multiplicity retained. |
| dependency | [Residual root location](Yin_C_G0882_v8.md#root-location) | Same-component conclusion and the original pole-gap bound. |
| review | [Independent complete finding](../audits/reviews/Yin_R_G1107_v25.md#endpoint-domain-review) | Entire fixed analytic statement and proof, exact symbolic checks and applicability of adopted dependencies, without any new J premise. |

## Current assessment

[Selected decision](#decision-endpoint-domain-19683)
