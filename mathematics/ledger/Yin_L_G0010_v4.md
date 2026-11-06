---
author: Yin
---

# A cyclotomic auxiliary bounds every integral completion of the Pell moment prefix

Date: 2026-11-05.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating agent proposed the circle auxiliary and exterior-root budget; the responsible delegate checked the complete argument, endpoint cases, source applicability and leading-coefficient extension below.
This is ordinary author exploration and checking, not independent review, a new Claim assessment or Task completion.

<a id="pell-prefix-auxiliary-scope"></a>
## Question and relation to the previous versions

[L10 v2](Yin_L_G0010_v2.md#integer-near-psd-three-moment-construction) gives an integer prefix \(s_0=d,s_1=a,s_2=1\) whose three-by-three Toeplitz matrix has a negative eigenvalue tending to zero.
Its small-total-measure reciprocal root model is not an integer polynomial.
[L10 v3](Yin_L_G0010_v3.md#pell-integral-completion-and-measure-price) gives a monic integer reciprocal completion of this prefix and proves that this particular completion pays divergent total logarithmic Mahler measure.
The question here is whether every monic integer completion of that same prefix must pay divergent total measure.

The answer is yes, by the explicit cyclotomic auxiliary below.
The new bound allows reducible polynomials, repeated roots and zero roots, without any reciprocal or unit hypothesis.
It supplies a quantitative arithmetic price for this prefix, rather than an input-uniform restriction that covers the unresolved near-zero irreducible domain.
The distinct formal-ghost analysis, explicit completion and angular control of v3 remain at their original addresses.

The related [C1 trace error](../claims/Yin_C_G0001_v1.md#integer-trace-low-mode-question), [C4 cyclotomic norm comparison](../claims/Yin_C_G0004_v1.md#damped-cyclotomic-norm-inequalities), and [C570 angular and coefficient-energy statement](../claims/Yin_C_G0570_v1.md#coefficient-energy-fixed-scope) were inspected at their actual scopes.
They retain related resultant, radial and angular mechanisms; the local comparison did not locate the particular harmonic-plus-\(\Phi_6\) bound proved here.
This is no claim that the auxiliary-function method is new or that the same inequality is absent from the literature.
C1 and C570 already exclude the Pell ratio in an irreducible small-total-measure sequence, whereas the present direct inequality applies to every monic integer completion.

<a id="cyclotomic-two-trace-bound"></a>
## Exact domain and resulting certificate

Let \(P\in\mathbb Z[X]\) be monic of degree \(d\ge0\), with all roots \(\alpha_1,\ldots,\alpha_d\) counted with their full multiplicities.
Put
\[
 s_j=\sum_{i=1}^d\alpha_i^j\quad(j=1,2),\qquad
 m=m(P)=\sum_{i=1}^d\log^+|\alpha_i|,
 \qquad L(P)=3s_1-s_2-2d.
\tag{1}
\]
Here \(\log^+0=0\), and an empty root list has empty sums.
The two power sums are integers by the Newton identities, including in degrees zero and one.
Define
\[
 g(t)=6\sinh t+2\sinh(2t)+t\qquad(t\ge0).
\tag{2}
\]
Then
\[
                         L(P)\le g(m(P)).
\tag{3}
\]
Every logarithm is natural, and \(m\) is total logarithmic Mahler measure, without division by \(d\).

Since \(L(P)\in\mathbb Z\), a positive \(L(P)\) gives \(g(m(P))\ge1\).
The function \(g\) is continuous and strictly increasing on \([0,\infty)\), with \(g(0)=0\) and \(g(t)\to\infty\), so this restricted class has \(m(P)\ge g^{-1}(1)>0\).
The condition \(L(P)>0\) is not asserted for every noncyclotomic input.

<a id="phi-six-circle-auxiliary"></a>
## Circle inequality and its disk extension

Set
\[
 Q(z)=z^2-z+1=\Phi_6(z),\qquad
 H(z)=\Re(3z-z^2)-2+\tfrac12\log|Q(z)|.
\tag{4}
\]
Give \(H\) the extended value \(-\infty\) at a zero of \(Q\).
For \(z=e^{i\theta}\) and \(x=\cos\theta\),
\[
 Q(z)=z(2x-1),\qquad
 \Re(3z-z^2)-2=-(1-x)(1-2x).
\tag{5}
\]
Consequently \(H(z)\le0\) on the unit circle is equivalent to
\[
                  \log|2x-1|\le2(1-x)(1-2x)
                  \qquad(-1\le x\le1).
\tag{6}
\]

For \(1/2<x\le1\), put \(y=2x-1\in(0,1]\).
The right-hand side of (6) is \(-y(1-y)\), and the elementary logarithmic inequality gives
\[
                   \log y\le y-1=-(1-y)\le-y(1-y).
\tag{7}
\]
The last inequality uses \(0<y\le1\), and at \(x=1\) it gives equality.
For \(-1\le x<1/2\), put \(y=1-2x\in(0,3]\).
The right-hand side of (6) is \(y(1+y)\), and
\[
                         \log y\le y-1\le y(1+y),
\tag{8}
\]
where the final difference is \(y^2+1>0\).
The endpoint \(x=-1\) is included in this second interval.
At the remaining endpoint \(x=1/2\), \(Q(z)=0\) and the extended logarithmic inequality holds directly.
This proves (6) on the entire circle.

Apply the maximum modulus principle to the entire function
\[
                         G(z)=\exp(6z-2z^2-4)Q(z).
\tag{9}
\]
Away from the two zeros of \(Q\), \(\log|G(z)|=2H(z)\), while \(G=0\) at those zeros.
Thus (6) gives \(|G(z)|\le1\) on the unit circle, and continuity on the closed disk and the maximum modulus principle give
\[
                          H(z)\le0\qquad(|z|\le1).
\tag{10}
\]
In particular \(H(0)=-2\); no inverse or logarithm of a root equal to zero is needed.

The precise source input is Jacob Shapiro, [Complex Analysis with Applications](https://web.math.princeton.edu/~js129/PDFs/teaching/MAT330_spring_2023/MAT330_Lecture_Notes.pdf), MAT330 Spring 2023 notes, typeset 14 May 2023, existing bibliography key Sha23.
The responsible delegate directly text-read the retained [Sha23 PDF](../literature/pdf/Sha23.pdf), printed/PDF pages 87--89, including Corollary 7.52 on page 88 and its proof on page 89.
That corollary states that a nonconstant holomorphic function cannot attain a modulus maximum in the interior of its domain.
The function in (9) is entire and nonconstant, and its modulus attains a maximum on the compact closed unit disk, so that maximum is on the boundary.
These are exactly the hypotheses and conclusion used in (10).
This is inspection of the stated interface and adjacent displayed proof, not an audit of the complete lecture notes or all proof dependencies.
The inequalities (5)--(8), the choice of \(G\), and the rootwise budget below are the present author calculations.

<a id="phi-six-exterior-budget"></a>
## Exterior comparison and the complete root budget

For \(|z|=r>1\), put \(w=1/z\).
The reciprocal identity
\[
                              Q(z)=z^2Q(1/z)
\]
and the fact that neither \(z\) nor \(w\) is a zero of \(Q\) give
\[
 H(z)-H(1/z)
       =\Re\bigl(3(z-1/z)-(z^2-1/z^2)\bigr)+\log r.
\tag{11}
\]
Write \(z=re^{i\theta}\).
Then
\[
\begin{aligned}
 H(z)
 &\le3(r-r^{-1})\cos\theta-(r^2-r^{-2})\cos(2\theta)+\log r\\
 &\le3(r-r^{-1})+(r^2-r^{-2})+\log r\\
 &=g(\log r).
\end{aligned}
\tag{12}
\]
The first inequality uses (10) at \(1/z\).
The signs in (12) come from the actual \(1/z=r^{-1}e^{-i\theta}\), not an unsupported replacement of roots by conjugates.

The function \(g\) is superadditive on nonnegative arguments.
Indeed, for \(a,b\ge0\),
\[
 \sinh(a+b)=\sinh a\cosh b+\cosh a\sinh b
                         \ge\sinh a+\sinh b,
\tag{13}
\]
and the same calculation applies to \(2a,2b\), while the linear term adds exactly.
Induction therefore gives
\[
                       \sum_i g(t_i)\le g\!\left(\sum_i t_i\right)
                       \qquad(t_i\ge0).
\tag{14}
\]
The empty-sum case also holds because \(g(0)=0\).

First suppose that \(P\) and \(Q\) have no common root.
The full resultant is the nonzero integer
\[
                  \operatorname{Res}(P,Q)=\prod_{i=1}^d Q(\alpha_i),
\]
so its absolute value is at least one.
Using (4), the reality of \(s_1,s_2\), (10), (12) and (14), obtain
\[
\begin{aligned}
 L(P)+\tfrac12\log|\operatorname{Res}(P,Q)|
 &=\sum_{i=1}^d H(\alpha_i)\\
 &\le\sum_{|\alpha_i|>1}g(\log|\alpha_i|)\\
 &\le g(m(P)).
\end{aligned}
\tag{15}
\]
Every original root and its multiplicity occurs in the equality.
Roots in the closed unit disk contribute nonpositively, including zero roots.
Dropping the nonnegative resultant term proves (3) in this case.

For a general monic integer \(P\), divide out the maximal power \(Q^k\) and write \(P=Q^kP_0\).
The polynomial \(Q=\Phi_6\) is monic and irreducible over \(\mathbb Q\), so a common root implies this factor, and division leaves \(P_0\in\mathbb Z[X]\) monic.
The polynomial \(P_0\) has no common root with \(Q\), including when \(P_0=1\).
For the two roots of each copy of \(Q\),
\[
                    s_1(Q)=1,\qquad s_2(Q)=-1,\qquad
                    L(Q)=3-(-1)-4=0,\qquad m(Q)=0.
\tag{16}
\]
Power sums and degrees add under products, and logarithmic Mahler measure is additive.
Hence
\[
                         L(P)=L(P_0),\qquad m(P)=m(P_0).
\tag{17}
\]
Apply (15) to \(P_0\) to finish the proof.
There is no appeal to a zero resultant or to an undefined cancellation of logarithms.

<a id="all-pell-completions-measure-price"></a>
## The price for every completion of the Pell prefix

Use precisely the integer pairs in [L10 v2](Yin_L_G0010_v2.md#integer-near-psd-three-moment-construction):
\[
 d\ge32,\quad a\ge23,\quad d\ \hbox{even},\quad a\ \hbox{odd},
 \qquad 2a^2=d^2+d+2,
\tag{18}
\]
with \(d,a\to\infty\) along its displayed recurrence.
Let \(P\) be any monic integer polynomial of degree \(d\) whose complete root multiset satisfies \(s_1=a\) and \(s_2=1\).
This class is nonempty by [v3's explicit reciprocal completion](Yin_L_G0010_v3.md#pell-integral-completion-and-measure-price).
The present argument does not impose reciprocity, irreducibility, distinct roots or a unit constant coefficient on \(P\).

Put \(\kappa=3/\sqrt2-2>0\).
Then
\[
             L(P)=3a-1-2d>\kappa d-1>0,
\tag{19}
\]
because (18) gives \(a>d/\sqrt2\) and \(d\ge32\).
For every \(t\ge0\),
\[
 6\sinh t\le3e^t\le3e^{2t},\qquad
 2\sinh(2t)\le e^{2t},\qquad t\le e^{2t},
\]
so
\[
                              g(t)\le5e^{2t}.
\tag{20}
\]
Combining (3), (19) and (20) gives
\[
 m(P)\ge\tfrac12\log\frac{3a-1-2d}{5}
       >\tfrac12\log\frac{\kappa d-1}{5}
       =\tfrac12\log d-O(1).
\tag{21}
\]
In particular the total measure tends to infinity for every sequence of monic integer completions along these Pell pairs.
A negative right-hand side for an initial pair does not affect the inequality or its divergent asymptotic conclusion.

The stronger lower bound for the particular six-term completion in v3 remains valid at its original scope.
Equation (21) supplies a weaker rate for a much larger class: it excludes every integer completion with small total measure, rather than only the previously constructed completion.
It also proves that v2's nonintegral small-measure root model cannot be replaced by a monic integer polynomial while preserving the same degree and first two power sums and keeping its total measure small.
No numerical root computation or classification of the remaining coefficients is involved.

<a id="leading-coefficient-scope-note"></a>
## Leading-coefficient scope note

The same numerical inequality (3) holds for every nonzero integer polynomial, although \(L(P)\) need not then be an integer.
To see this, let \(c\ne0\) be its leading coefficient and strip all factors \(Q\) as in (16)--(17), which leaves \(c,L,m\) unchanged.
For the remaining polynomial put \(S=\sum_i\log^+|\alpha_i|\), so \(m(P)=\log|c|+S\).
Since \(Q\) has degree two, the resultant formula and the same rootwise argument give
\[
 L(P)+\tfrac12\log|\operatorname{Res}(P,Q)|-\log|c|
       =\sum_i H(\alpha_i)\le g(S).
\]
The nonzero integer resultant, \(\log|c|\ge0\), (14), and \(g(t)\ge t\) imply
\[
 L(P)\le g(S)+\log|c|
       \le g(S)+g(\log|c|)
       \le g(m(P)).
\tag{22}
\]
Constants are included by empty sums.
The zero polynomial is excluded because its logarithmic Mahler measure is not the finite root-list quantity used here.
The integer-positive-\(L\) certificate above was stated for monic polynomials, not for arbitrary rational power sums.

<a id="low-trace-certificate-return-boundary"></a>
## Why this does not cover the original near-zero domain

Consider actual monic irreducible polynomials of nontorsion algebraic units, with full degree \(d\), total measure \(m\), and roots \(\alpha_i=r_i e^{i\theta_i}\).
The already retained [C570 angular bound](../claims/Yin_C_G0570_v1.md#uniform-powered-angular-coherence), applied with the fixed window \(T=2\), gives
\[
 \left|\frac1d\sum_i e^{in\theta_i}\right|
       \le\varepsilon(2m/d)\longrightarrow0
       \qquad(n=1,2)
\tag{23}
\]
along a hypothetical sequence with \(m\to0\).
Its actual powered-degree multiplicities and original unit hypotheses remain in force.
The already retained [C1 radial error](../claims/Yin_C_G0001_v1.md#integer-trace-low-mode-question) gives
\[
 \left|s_n-\sum_i e^{in\theta_i}\right|
                   \le2n e^{nm}m\qquad(n=1,2).
\tag{24}
\]
Divide (24) by \(d\) and combine it with (23).
For those genuine inputs,
\[
                     s_1/d\to0,\qquad s_2/d\to0,\qquad
                     L(P)/d\to-2.
\tag{25}
\]
Thus the positive-\(L\) certificate is eventually unavailable precisely in this possible near-zero regime.
The Pell prefix instead has \(s_1/d\to1/\sqrt2\); under a small-total-measure hypothesis (24) would transfer this to a nonzero first angular average.
For completions whose total measure grows, the untruncated trace ratio alone does not imply that their radial projections have the same angular bias.

The auxiliary therefore settles the arithmetic price of the selected near-positive moment test, without providing unrestricted input coverage, a contradiction to a genuine near-zero sequence or a strict counterexample to the original Task.
Neither the full ghost congruences nor the integer resultant here supplies the missing universally useful certificate.
No further parameter search or new strategy is justified by this particular bound alone.

The author check covered both circle intervals and all endpoints, the entire-function disk argument and actual source hypotheses, the exterior reciprocal identity, superadditivity with the complete root budget, nonzero integer resultants, repeated \(\Phi_6\) removal, zero and constant cases, the Pell constants, leading-coefficient costs and the actual irreducible return.
No independent review, new Claim adoption or native mathematical computation is claimed.
