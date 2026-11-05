---
author: Yin
---
# Exact joint rational-rank profile for coprime blocks and the original squarefree-reduction dichotomy

This project deduction determines the minimum rank over all rational approximants to the stated products and applies it to the original unrotated radical under squarefree reduction.
The precision-varying-approximants contributor developed the complete proof for Yin; the coordinating main agent contributed the requested original-input and scope checks.
The [selected assessment](#decision-whole-independent-review-2026-11-04) adopts the complete statement and argument after the [independent whole finding R1076 v7](../audits/reviews/Yin_R_G1076_v7.md#coprime-block-profile-whole).
The original unrestricted positive total logarithmic Mahler gap remains unresolved.

The complete earlier conclusions, arguments, source limits and adopted assessments remain at their exact fixed homes: [v1](Yin_C_G0860_v1.md#decision-whole-independent-review-2026-11-04), [v2](Yin_C_G0860_v2.md#decision-whole-independent-review-2026-11-04), [v4](Yin_C_G0860_v4.md#decision-whole-independent-review-2026-11-04), [v5](Yin_C_G0860_v5.md#decision-whole-independent-review-2026-11-04), [v6](Yin_C_G0860_v6.md#decision-whole-independent-review-2026-11-04), and [v7](Yin_C_G0860_v7.md#decision-whole-independent-review-2026-11-04).
In particular the fixed-binomial result, single-radical good- and bad-reduction bounds, and fixed componentwise trace-family theorem retain their distinct scopes.
None of their reviews is transferred to the new proof.
No rolling Draft, unreviewed center-supply construction, numerical probe, or new unadopted contour theorem is a mathematical premise.

## Statement

**A. Products with pairwise coprime residual denominators.**
Let \(i\) range over a nonempty finite set and suppose
\[
 \begin{gathered}
 D_i,E_i\in\mathbb Z_2[x],\quad D_i(0)=1,\quad E_i(0)=0,\quad
 f_i=\deg D_i\ge1,\quad \deg E_i\le f_i,\\
 F_i=\overline D_i,\quad \deg F_i=f_i,\quad
 \gcd(\overline E_i,F_i)=1,\quad \gcd(F_i,F_j)=1\ (i\ne j),\\
 \lambda_i\in\mathbb Z,\quad\lambda_i\ge3,\quad a_i=\lambda_i-2,\quad
 Y=\prod_i\sqrt{1+2^{\lambda_i}E_i/D_i},
 \end{gathered}
\]
with every square root normalized to one at zero.
For an integral rational series \(T\in\mathbb Q_2(x)\cap\mathbb Z_2[[x]]\), let \(\rho(T)\) be its shifted coefficient-Hankel rank.
Let \(r_s(Y)\) be the minimum of this rank subject to \(Y-T\in2^s\mathbb Z_2[[x]]\), for each integer \(s\ge1\).
Then
\[
 r_s(Y)=\sum_i f_i\max\left(0,
             \left\lceil\frac{s-a_i-1}{2a_i}\right\rceil\right).
\]
The same exact minimum holds if the approximants must have coefficients in \(\mathbb Q\).
For fixed data,
\[
 r_s(Y)=\frac{s}{2}\sum_i\frac{f_i}{a_i}+O(1),\qquad
 \sum_{s\ge1}(h-r_s(Y))_+=\gamma h^2+O(h),\qquad
 \gamma=\left(\sum_i\frac{f_i}{a_i}\right)^{-1}.
\]
Multiplying \(Y\) by a fixed rational integral unit whose inverse is integral changes \(r_s\) by at most the multiplier's rank and leaves the leading coefficient \(\gamma\) unchanged.
All competitors, including precision-dependent rational centers and coefficients in \(\mathbb Q_2\), are included; component-rank additivity is proved rather than assumed.

**B. The original squarefree-reduction dichotomy.**
Let \(P\in\mathbb Z[t]\) be monic, irreducible, reciprocal and noncyclotomic, of degree \(d\ge2\) and constant term one, and suppose every positive power of a root retains degree \(d\).
Use all its original roots to define \(P_n(x)=\prod_j(1-\alpha_j^n x)\), \(U=P_2\), \(V=P_4\), and \(G=\sqrt{V/U}\), normalized by \(G(0)=1\).
Assume \(\overline P\) is squarefree, and write \(\overline P=\prod_iF_i\) into distinct monic irreducibles of degrees \(f_i\).
If \(V\equiv U\pmod8\), let \(U_i,V_i\in\mathbb Z_2[x]\) be the unique degree-\(f_i\), constant-one factors of \(U,V\) reducing to \(F_i\), and set
\[
 \lambda_i=v_2(V_i-U_i)\ge3,\qquad a_i=\lambda_i-2.
\]
All these depths are finite, and Part A applies to \(G\) with \(D_i=U_i\) and \(E_i=(V_i-U_i)/2^{\lambda_i}\).
If \(V\not\equiv U\pmod8\), then instead
\[
                     r_1(G)=0,\qquad r_s(G)=+\infty\quad(s\ge2).
\]
Here \(+\infty\) denotes the empty rational-approximation class.
In this squarefree class the canonical Artin--Schreier center of C857 v2 is one, and its zero-class condition is exactly \(V\equiv U\pmod8\).
The complete proof also retains a small-measure Lehmer control in the nonzero-class branch; it does not supply a near-one sequence in the zero-class branch.

**C. Exact depth budget and the same original contour.**
In the finite-profile branch of Part B,
\[
 v_2\operatorname{Res}(U,V)=\sum_i f_i\lambda_i,\qquad
 \gamma\le\frac{v_2\operatorname{Res}(U,V)-2d}{d^2},\qquad
 \gamma\log2\le\frac{\log(d/2)+(12-6/d)m(P)}d.
\]
For the same original shifted leading Hankel determinants and the original-root slit function \(\Phi_1\) of C855 v2,
\[
 \gamma\log2\le\inf_{\tau\ge0}\Phi_1(\tau)\le5E_2,\qquad
 m(P)\ge\sqrt{\gamma\log2/5},\qquad
 E_2=\sum_{|\alpha_j|>1}\log^2|\alpha_j|.
\]
The coefficient \(\gamma\) is the exact leading coefficient of the all-level rational-approximation certificate for this particular germ.
It is not an upper bound on actual Hankel valuations, and the stated bound on \(\gamma\) does not exclude further arithmetic information or a better use of the actual contour.
Neither repeated reduction after recentering nor a sum of several original mask radicals is covered by the minimum-rank theorem.

## Exact inputs and source scope

| Role | Exact input and use |
| --- | --- |
| Adopted project dependency | [C860 v5 integral Padé identities](Yin_C_G0860_v5.md#pade-integrality), [normalized rational-denominator lemma](Yin_C_G0860_v5.md#integral-rational-denominator), and [single-factor minimum proof](Yin_C_G0860_v5.md#minimum-rational-rank): the explicit scaled odd Padé approximants, their exact normalized error and denominator reduction, and normalization of arbitrary rational competitors over \(\mathbb Q_2\). Its retained Kou11 and formal-rank source scopes are unchanged. |
| Adopted project dependency | [C857 v2 canonical Artin--Schreier representative](Yin_C_G0857_v2.md#reduced-representative) and [C860 v2 original modulo-four input](Yin_C_G0860_v2.md#statement): only the actual original \(P_4-P_2\) divisibility and the simple-pole consequence of the retained canonical decomposition. |
| Adopted project dependency | [C860 v4 original resultant budget](Yin_C_G0860_v4.md#coherent-center-precision-budget), especially (H7): nonvanishing and the full-original-degree upper bound, with its C860 v1 Vandermonde/source interface unchanged. |
| Adopted project dependency | [C858](Yin_C_G0858_v1.md#all-place-hankel-budget): original nonrationality, finite elementary-divisor comparison, and infinitely many nonzero shifted leading Hankel determinants at its accepted source scope. |
| Adopted project dependency | [C855 v2](Yin_C_G0855_v2.md#statement), Part C: the same original single-mask contour, determinant shift and \(\Phi_1(0)\le5E_2\), without any later contour theorem. |
| Local lifting attribution and context | [C241's complete-ring proof](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) and [The26b-U004](../audits/literature/The26b/Yin_U004.md#the26b-u004): existing Hensel mechanism and classical attribution, while the exact coprime coefficient-lifting map needed here is completely proved below; no new source theorem or source-proof inspection is claimed. |
| Fixed control only | [C399](Yin_C_G0399_v1.md#statement) and [C251](Yin_C_G0251_v1.md#j10-complete-exponent-profile-proof): the actual original Lehmer input and its squarefree mod-two factors, at retained mathematical/native-evidence scope, with no fresh historical run. The new \(U,V\) identities are proved by displayed polynomial expansion. |

<a id="argument"></a>
## Complete argument

### A product theorem with arbitrary rational competitors

Fix a nonempty finite collection of polynomials and integers satisfying
\[
 \begin{gathered}
 D_i,E_i\in\mathbb Z_2[x],\qquad D_i(0)=1,\quad E_i(0)=0,
 \qquad f_i=\deg D_i\ge1,\quad \deg E_i\le f_i,\\
 F_i=\overline D_i,\qquad \deg F_i=f_i,\qquad
 \gcd(\overline E_i,F_i)=1,\qquad
 \gcd(F_i,F_j)=1\quad(i\ne j),\\
 \lambda_i\ge3,\qquad a_i=\lambda_i-2,\qquad
 R_i=1+2^{\lambda_i}E_i/D_i,\qquad
 y_i=\sqrt{R_i},\quad y_i(0)=1,\qquad Y=\prod_i y_i.
                                                               \tag{CB1}
 \end{gathered}
\]
The degree and coprimality conditions imply that \(\overline E_i\ne0\), that \(E_i/D_i\) is reduced, and that each factor satisfies C860 v5's good-reduction hypotheses with degree \(f_i\).
Use its shifted Hankel rank \(\rho(T)=\max(\deg A,\deg B)\) for a nonconstant reduced rational function \(T=A/B\), and rank zero for a constant.
For each integer \(s\ge1\), define
\[
 \begin{split}
 r_s(Y)&=\min\{\rho(T):T\in\mathbb Q_2(x)\cap\mathbb Z_2[[x]],
                         \ Y-T\in2^s\mathbb Z_2[[x]]\},\\
 k_i(s)&=\max\left(0,
                \left\lceil\frac{s-a_i-1}{2a_i}\right\rceil\right).
 \end{split}
\]
Then the exact joint minimum is
\[
                     r_s(Y)=\sum_i f_i k_i(s).                \tag{CB2}
\]
No restriction to products, functions of a fixed residual, fixed centers, rational coefficients in \(\mathbb Q\), or a predetermined denominator is imposed on the competitors.

For the upper bound, write \(A_{i,t}=P_{i,t}/Q_{i,t}\) for C860 v5's odd Padé approximant to \(y_i\).
Its exact identities give
\[
 \begin{gathered}
 P_{i,t},Q_{i,t}\in\mathbb Z_2[x],\quad
 P_{i,t}(0)=Q_{i,t}(0)=1,\quad
 \deg P_{i,t},\deg Q_{i,t}\le f_it,\\
 \overline P_{i,t}=\overline Q_{i,t}=F_i^t,\qquad
 \sigma_i(t)=a_i(2t+1)+1,\\
 y_i-A_{i,t}\in2^{\sigma_i(t)}\mathbb Z_2[[x]],\qquad
 \overline{(y_i-A_{i,t})/2^{\sigma_i(t)}}
                   =(\overline E_i/F_i)^{2t+1}.
                                                               \tag{CB3}
 \end{gathered}
\]
By definition \(\sigma_i(k_i(s))\ge s\), including the case \(k_i(s)=0\).
The product of these approximants differs from \(Y\) by an element of \(2^s\mathbb Z_2[[x]]\), by telescoping the product and using integrality of every other factor.
Its numerator and denominator degrees are at most \(\sum_i f_i k_i(s)\).
This proves the upper bound in (CB2), without an assumption that those product degrees survive cancellation.

For the lower bound, fix an arbitrary competing \(C/B\) of rank \(r\).
The [integral-denominator lemma](Yin_C_G0860_v5.md#integral-rational-denominator) gives a reduced representation with
\[
 C,B\in\mathbb Z_2[x],\qquad B(0)=1,\qquad
                    \deg C,\deg B\le r.
                                                               \tag{CB4}
\]
Fix an index \(i\) with \(k_i=k_i(s)>0\), set \(t=k_i-1\), and compare with
\[
 T^{(i)}=A_{i,t}\prod_{j\ne i}A_{j,k_j(s)}=P^{(i)}/Q^{(i)},
 \qquad \sigma=\sigma_i(t)<s,
                                                               \tag{CB5}
\]
where the displayed polynomial numerator and denominator are the un-cancelled products from (CB3).
The other factors have already reached precision \(s\).
Consequently
\[
 Y-T^{(i)}
 =(y_i-A_{i,t})\prod_{j\ne i}y_j
   +A_{i,t}\left(\prod_{j\ne i}y_j-
                         \prod_{j\ne i}A_{j,k_j(s)}\right)
\]
has exact depth \(\sigma\), and after division by \(2^\sigma\) its reduction is \((\overline E_i/F_i)^{2t+1}\).
Indeed the second summand is divisible by \(2^s\), while every \(y_j\) reduces to one.
This identifies the leading error before any putative cancellation among product terms; all higher cross terms are contained in the second summand and vanish in this reduction.
Since \(Y-C/B\) is divisible by \(2^s\), the same reduction holds for \(C/B-T^{(i)}\).
The polynomial
\[
             H^{(i)}=(C Q^{(i)}-B P^{(i)})/2^\sigma
\]
has integral coefficients, because its Taylor coefficients are those of the integral series \(B Q^{(i)}(C/B-T^{(i)})/2^\sigma\).
Reducing this polynomial identity gives
\[
 \overline H^{(i)}=
 \frac{\overline B\,\overline E_i^{\,2t+1}
                   \prod_{j\ne i}F_j^{k_j(s)}}{F_i^{t+1}}.
                                                               \tag{CB6}
\]
The other displayed factors are coprime to \(F_i\), so polynomiality forces \(F_i^{k_i(s)}\mid\overline B\).
This argument is repeated with different comparisons (CB5) but the same arbitrary denominator \(B\).
Pairwise coprimality therefore gives
\[
                 \prod_i F_i^{k_i(s)}\mid\overline B.
                                                               \tag{CB7}
\]
Since \(\overline B(0)=1\), this polynomial is nonzero and its degree is at least \(\sum_i f_i k_i(s)\).
Together with (CB4), this proves the lower bound and completes (CB2).
Thus degree additivity is a conclusion of the separate residue-pole constraints, not an assumption about arbitrary joint rational approximants.

For fixed data put
\[
 c=\frac12\sum_i\frac{f_i}{a_i},\qquad
 \gamma=\left(\sum_i\frac{f_i}{a_i}\right)^{-1}.
\]
Equation (CB2) gives the full profile and its consequence
\[
 r_s(Y)=cs+O(1),\qquad
       \sum_{s\ge1}(h-r_s(Y))_+=\gamma h^2+O(h).
                                                               \tag{CB8}
\]
The second formula follows by comparison with the arithmetic progression \(cs\); only \(O(h)\) precision levels contribute, and the fixed bounded rank error changes their sum by \(O(h)\).
Both constants may depend on all the fixed input data.
For a fixed rational multiplier \(S\) with \(S,S^{-1}\in\mathbb Z_2[[x]]\), the same multiplication/division argument as C860 v5 gives \(|r_s(SY)-r_s(Y)|\le\rho(S)\), so the leading coefficient \(\gamma\) is unchanged.

The minimum can also be realized with coefficients in \(\mathbb Q\).
For any integral polynomial representation \(A/B\) attaining the upper bound at precision \(s\), replace each coefficient by an ordinary integer in its residue class modulo \(2^s\), retaining \(B(0)=1\).
The new polynomials have no larger degrees, their denominators remain integral power-series units, and their quotient differs from \(A/B\) by an element of \(2^s\mathbb Z_2[[x]]\).
The lower bound already applies to this smaller class, so its minimum equals (CB2).
This finite coefficient approximation is independent of any number-field or fixed-family logarithmic-cancellation argument.

### Exact factor lifting for the original squarefree-reduction input

Let \(P\) satisfy C857 v2's original hypotheses: it is monic, irreducible, reciprocal and noncyclotomic, has degree \(d\) and constant term one, and every positive power of a root still has degree \(d\).
Put \(U=P_2\), \(V=P_4\), and suppose for this paragraph that \(\overline P\) is squarefree and
\[
                              V\equiv U\pmod8.
                                                               \tag{CB9}
\]
The characteristic-two root-power identity gives \(\overline U=\overline V=\overline P\).
Write its factorization into distinct monic irreducibles as \(\overline P=\prod_i F_i\), with \(f_i=\deg F_i\) and \(\sum_i f_i=d\).
Every \(F_i(0)=1\), since the original constant term is one.
There are unique normalized factorizations
\[
 U=\prod_i U_i,\qquad V=\prod_i V_i,
 \qquad U_i,V_i\in\mathbb Z_2[x],\qquad
 U_i(0)=V_i(0)=1,\quad \deg U_i=\deg V_i=f_i,
 \quad \overline U_i=\overline V_i=F_i.
                                                               \tag{CB10}
\]
Moreover \(U_i\equiv V_i\pmod8\) for every \(i\).

Here is a complete coefficient-lifting proof, recording the constant normalization and congruence stability needed in this application.
Start with any degree-\(f_i\) binary lifts of \(F_i\), with constant term one.
At precision \(2^n\), correct the \(i\)-th factor by \(2^n C_i\), where \(\deg C_i\le f_i\) and \(C_i(0)=0\).
The correction equation modulo two is the linear map
\[
 (\overline C_i)_i\longmapsto
                    \sum_i\overline C_i\prod_{j\ne i}F_j
                                                               \tag{CB11}
\]
from a space of dimension \(\sum_i f_i=d\) to the polynomials of degree at most \(d\) with zero constant term, also of dimension \(d\).
Its kernel is zero: reduction modulo \(F_i\) forces \(F_i\mid\overline C_i\), and the degree bound and zero constant term then force \(\overline C_i=0\).
Thus (CB11) is an isomorphism and supplies a unique next correction for any required coefficient error.
Iterating and using completeness of \(\mathbb Z_2\) proves existence and uniqueness in (CB10).
The same recursion proves that congruent target polynomials modulo \(2^N\) have congruent normalized factors modulo \(2^N\).
Taking \(N=3\) gives the final assertion.
Leading coefficients remain units because their reductions are the monic \(F_i\).
This is the usual coprime Hensel factor lifting, proved here with the actual degree and normalization constraints.
The existing [C241 complete-ring lifting proof](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) and [The26b-U004's classical Hensel attribution](../audits/literature/The26b/Yin_U004.md#the26b-u004) provide the local source context; no uninspected general factorization theorem or extra source-proof scope is imported.

For each block set
\[
 \lambda_i=v_2(V_i-U_i),\qquad
 D_i=U_i,\qquad E_i=(V_i-U_i)/2^{\lambda_i}.
                                                               \tag{CB12}
\]
The integer \(\lambda_i\) is finite, since otherwise \(U\) and \(V\) would share the factor \(U_i=V_i\), contrary to their original nonzero cross-resultant in C860 v4.
It is at least three by (CB9)--(CB10).
The polynomial \(\overline E_i\) is nonzero, has degree at most \(f_i\), and has zero constant term.
It is therefore not divisible by the irreducible polynomial \(F_i\): a multiple of \(F_i\) of degree at most \(f_i\) is either zero or has nonzero constant term.
This proves \(\gcd(\overline E_i,F_i)=1\), so every condition in (CB1) is now verified for actual factors of the original \(P_4/P_2\).
The product of the normalized square roots equals the original normalized radical \(G=\sqrt{V/U}\), by squaring and using its constant term one.
Consequently (CB2) and (CB8) give its exact minimum rational-rank profile, with no extra supplied good-reduction assumption after (CB9) and squarefreeness.
The local coefficients lie in \(\mathbb Q_2\); a number-field description of all these factors is unnecessary.
The preceding coefficient-rounding argument supplies rational approximants to the same original integral germ at each finite precision.

### The Artin--Schreier alternative and the scope of recentering

For this original squarefree-reduction input, \(r=\overline{(V-U)/4}/\overline U\) is proper and has only simple poles after cancellation.
The canonical decomposition in C857 v2 therefore has \(h=0\) and \(c=r\).
In particular
\[
            c=0\quad\Longleftrightarrow\quad V\equiv U\pmod8.
                                                               \tag{CB13}
\]
Thus C857's canonical rational centers do not enlarge (CB9) in this reduction class: the canonical center is one.

If (CB9) fails, the exact alternative is stronger than failure of a particular Padé family.
The scaled-binomial integrality from C860 gives \(G=1+2H\) with \(H\in\mathbb Z_2[[x]]\), and squaring yields
\[
                 \overline H^{\,2}+\overline H=r.
                                                               \tag{CB14}
\]
A nonzero proper rational function with only simple poles cannot be \(z^2+z\) for any rational \(z\in\mathbb F_2(x)\): a pole of \(z\) gives an even-order pole of \(z^2+z\), while absence of finite poles makes \(z\) a polynomial and properness makes its Artin--Schreier image constant.
The constant possibility is zero here because \(r(0)=0\).
If an integral rational \(T\) satisfied \(G-T\in4\mathbb Z_2[[x]]\), then \((T-1)/2\) would be an integral rational series whose reduction is \(\overline H\), contradicting (CB14) and this pole test.
Reduction is legitimate by C860 v5's integral normalized-denominator lemma, applied to \((T-1)/2\).
Writing the minimum of an empty approximation class as \(+\infty\), one obtains
\[
                 r_1(G)=0,\qquad r_s(G)=+\infty\quad(s\ge2)
                         \quad\hbox{when }c\ne0.
                                                               \tag{CB15}
\]
This includes rational centers depending on the requested precision.
The same argument excludes any fixed integral rational unit center \(S\), normalized by \(S(0)=1\), for which \(G^2/S^2\equiv1\pmod8\): its normalized square root would give \(G/S\equiv1\pmod4\), hence a forbidden rational approximation \(G\equiv S\pmod4\).
No analogous conclusion is asserted when \(\overline P\) has repeated factors; then the nonzero canonical \(h\), additional center poles and C860 v6's bad-reduction phenomena remain genuine possibilities.

Squarefree reduction is compatible with actual small reciprocal measure, but does not supply (CB9).
For example, the original Lehmer polynomial has the adopted [degree-ten Salem and measure data](Yin_C_G0399_v1.md#statement) and the retained [two distinct degree-five mod-two factors](Yin_C_G0251_v1.md#j10-complete-exponent-profile-proof).
For its exact coefficients, the elementary identity \(P_2(x)=P_{\rm even}(x)^2-xP_{\rm odd}(x)^2\), where \(P(t)=P_{\rm even}(t^2)+tP_{\rm odd}(t^2)\), gives
\[
 \begin{split}
 U&=1-x-x^3+x^4-x^5+x^6-x^7-x^9+x^{10},\\
 V&=U-4x^4-4x^6.
 \end{split}                                                    \tag{CB16}
\]
These displayed identities can be checked directly by polynomial expansion and are not premises taken from an unretained numerical probe.
They place this particular small-measure input in (CB15), not in (CB2).
No sequence approaching measure zero, and no near-one sequence satisfying (CB9), is supplied by this control.

### Exact depth budget and the original complex return

Under (CB9), multiplicativity of resultants in the complete factorizations (CB10) gives
\[
                  v_2\operatorname{Res}(U,V)
                              =\sum_i f_i\lambda_i.
                                                               \tag{CB17}
\]
Indeed, for \(i\ne j\) the reduction of \(\operatorname{Res}(U_i,V_j)\) is \(\operatorname{Res}(F_i,F_j)\ne0\), so the cross-block factors are units.
For the matching block, evaluating \(V_i=U_i+2^{\lambda_i}E_i\) at the \(f_i\) roots of \(U_i\) shows that its resultant is \(2^{f_i\lambda_i}\) times a unit.
The remaining unit consists of the unit leading coefficient of \(U_i\) to a nonnegative power and \(\operatorname{Res}(U_i,E_i)\), which is a unit by \(\gcd(F_i,\overline E_i)=1\).
This also verifies that neither a lower degree of \(E_i\) nor the constant-term normalization changes the valuation.

With \(a_i=\lambda_i-2\), Cauchy--Schwarz and (CB17) imply
\[
 \gamma=\left(\sum_i\frac{f_i}{a_i}\right)^{-1}
       \le\frac{\sum_i f_i a_i}{d^2}
       =\frac{v_2\operatorname{Res}(U,V)-2d}{d^2}.
                                                               \tag{CB18}
\]
The original resultant is a nonzero integer, and the already adopted C860 v4 estimate (H7) is
\(\log|\operatorname{Res}(U,V)|\le d\log(2d)+(12d-6)m(P)\).
Consequently
\[
               \gamma\log2
                \le\frac{\log(d/2)+(12-6/d)m(P)}{d}.
                                                               \tag{CB19}
\]
The exact weighted coefficient \(\gamma\) can exceed the coefficient obtained by using only \(\min_i a_i\), so the local splitting is a constructive precision improvement when block depths differ.
It cannot be replaced by a uniform dimension-free positive coefficient merely by choosing different rational approximants to this same \(G\): (CB2) already minimizes over all of them, and (CB19) tends to zero on any hypothetical near-one sequence of unbounded degree.
This is a statement about the all-level rational-approximation certificate, not an upper bound on the actual Hankel determinant valuation.

The original germ \(G\) has integral coefficients and is nonrational at C858's adopted original-input scope.
Its infinitely many nonzero shifted leading Hankel determinants \(\mathcal D_h(G)\) obey the same finite elementary-divisor bound, now with the exact ranks (CB2).
Combining (CB8) with the [C855 v2 original-root contour](Yin_C_G0855_v2.md#statement), using the invariant single mask \(\{0\}\) and slit count one, gives
\[
 \liminf_{\mathcal D_h(G)\ne0}
       h^{-2}\log|\mathcal D_h(G)|\ge\gamma\log2,
 \qquad
       \gamma\log2\le\inf_{\tau\ge0}\Phi_1(\tau)\le5E_2,
 \qquad
                m(P)\ge\sqrt{\gamma\log2/5}.
                                                               \tag{CB20}
\]
Here \(E_2=\sum_{|\alpha_i|>1}\log^2|\alpha_i|\) uses all original conjugates and \(m(P)\) is the unrestricted total logarithmic Mahler measure.
If (CB9) fails, (CB15) instead makes this particular approximation certificate exactly \(h\), with zero quadratic coefficient.
The exact ranks do not imply asymptotic equality for the determinant valuations, optimality among non-rational-matrix divisibility arguments, or an obstruction to better use of the actual complex contour.
They also do not settle the genuinely joint approximation problem for a sum of several original mask radicals, or the repeated-reduction input after canonical recentering.
Those are the remaining original-input routes; no unrestricted positive total gap or counterexample follows here.

## Current assessment
[Selected decision](#decision-whole-independent-review-2026-11-04)

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T23:53 |
| status | proved |
| reason | Adopt complete A--C and CB1--CB20 after independent R1076 v7: the exact minimum over all Q2 and Q rational approximants for the stated coprime blocks, original squarefree-reduction dichotomy, normalized Hensel realization, exact weighted resultant budget and same-germ contour return. The original degree and total measure are retained. This fixes the rational-approximation certificate rather than actual determinant valuations; repeated reduction, several-mask traces and unrestricted G0001 remain unresolved. All preceding versions and source/evidence limits remain at their exact scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | All A--C, arbitrary rational competitors, exact rank at every precision, Q2/Q equality, fixed multiplier comparison, both original squarefree branches, actual depth budget and exact limitations. |
| argument | [Complete argument](#argument) | Entire CB1--CB20, one-block-low polynomial comparisons, simultaneous denominator divisibility, constant-one lifting and congruence stability, nonzero AS branch, original control and full determinant/contour accounting. |
| dependency | [Single-block Padé identities](Yin_C_G0860_v5.md#pade-integrality) | Actual integral approximants, exact leading error and denominator reductions, including index zero and retained source limits. |
| dependency | [Arbitrary rational denominator normalization](Yin_C_G0860_v5.md#integral-rational-denominator) | Every integral Q2-rational competitor and its degree bounds; no restriction to a chosen approximant family. |
| dependency | [Canonical AS reduction](Yin_C_G0857_v2.md#reduced-representative) | Proper simple-pole specialization and canonical center only on the original squarefree input. |
| dependency | [Original congruence](Yin_C_G0860_v2.md#statement) | Accepted modulo-four divisibility and original polynomial conventions, at retained Dimitrov scope. |
| dependency | [Original resultant budget](Yin_C_G0860_v4.md#coherent-center-precision-budget) | Full original nonzero resultant and H7, preserving all degree, discriminant and source costs. |
| dependency | [Original Hankel inputs](Yin_C_G0858_v1.md#all-place-hankel-budget) | Original nonrationality, finite elementary-divisor constraints and shifted leading-Hankel criterion at retained BNZ22 scope. |
| dependency | [Same original contour](Yin_C_G0855_v2.md#statement) | Only Part C and the singleton-mask original germ, complete roots, determinant shift and Phi_1(0) upper bound; no newer cut theorem is a premise. |
| dependency | [Lehmer control](Yin_C_G0399_v1.md#statement) | Actual degree-ten Salem polynomial and accepted measure only, with no historical native rerun. |
| dependency | [Squarefree control factors](Yin_C_G0251_v1.md#j10-complete-exponent-profile-proof) | Exact two distinct mod-two factors at retained native-evidence scope; the displayed powered polynomial identities are checked directly. |
| support | [Classical lifting attribution](../audits/literature/The26b/Yin_U004.md#the26b-u004) | Existing source context only; the exact factor-lifting map is proved directly, without importing an uninspected factorization theorem. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1076_v7.md#coprime-block-profile-whole) | Entire A--C/CB1--CB20, exact source and control limits, direct finite algebra check and no unrestricted gap or actual determinant equality. |
