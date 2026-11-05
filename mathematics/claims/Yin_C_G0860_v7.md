---
author: Yin
---
# Exact leading rank and precision of fixed componentwise Padé traces

This project deduction completes the leading rank and precision calculation for the fixed componentwise Padé family, with supplied arithmetic hypotheses on the actual original orbit.
The [v4 fixed-binomial theorem](Yin_C_G0860_v4.md#statement), [v5 exact single-radical Padé and good-reduction theorem](Yin_C_G0860_v5.md#pade-statement), and [v6 bad-reduction bound and original control](Yin_C_G0860_v6.md#bad-reduction-statement) remain at their complete fixed homes and their respective [v4](Yin_C_G0860_v4.md#decision-whole-independent-review-2026-11-04), [v5](Yin_C_G0860_v5.md#decision-whole-independent-review-2026-11-04), and [v6](Yin_C_G0860_v6.md#decision-whole-independent-review-2026-11-04) selected assessments.
The earlier [v1](Yin_C_G0860_v1.md#statement) and [v2](Yin_C_G0860_v2.md#statement) statements, proofs and actual assessments are likewise preserved.
None of those reviews is transferred to the present new proof.

The joint-Padé precision contributor developed the general derivative-matrix and Gauss-valuation argument for Yin.
The coordinating agent contributed its fraction-field and Cramer checks, the pairwise torsion mechanism and the direct rank-zero ESS specialization.
The precision-varying-approximants contributor completed the geometric pole-rank argument and the family-profile assembly.
The precision contributor checked the supplied-center generalization as a contributor, and the coordinating agent read both complete component proofs as a contributor.
Those development checks are distinct from this version's selected independent whole assessment.
No rolling Draft, unreviewed center-supply construction or numerical probe is a mathematical premise.

## Statement

Let \(P\in\mathbb Z[t]\) be monic, irreducible, reciprocal and noncyclotomic, of degree \(d\ge2\) and constant term one, and suppose every positive power of a root retains degree \(d\).
Use all original roots \(\alpha_i\) and put \(P_n(x)=\prod_i(1-\alpha_i^nx)\).
Fix an odd prime \(q\), a primitive \(q\)-th root \(\zeta\), \(K=\mathbb Q(\zeta)\), and a full Galois orbit \(O\) of a nonempty mask \(I\subseteq\mathbb Z/q\mathbb Z\).
For \(J\in O\), define
\[
 D_J=\prod_{j\in J}P_2(\zeta^jx),\qquad
 N_J=\prod_{j\in J}P_4(\zeta^jx),\qquad
 G_J=\sqrt{N_J/D_J},\quad G_J(0)=1.
\]
Supply fixed rational centers \(H_J\in K(x)\), regular at zero with \(H_J(0)=1\), such that \(\sigma(H_J)=H_{\sigma J}\) for every Galois automorphism and \(H_J,H_J^{-1}\) are integral power series at every place above two.
Define
\[
 R_J=G_J^2/H_J^2,\qquad \delta_J=\deg R_J,\qquad
 \Delta=\sum_{J\in O}\delta_J,\qquad
 \lambda=\min_{J\in O,\,\mathfrak p\mid2}
                       v_{\mathfrak p}(R_J-1)\ge3,
 \qquad a=\lambda-2.
\]
The valuations are coefficientwise series valuations, normalized by \(v_{\mathfrak p}(2)=1\).
The finite exact minimum \(\lambda\) and all center hypotheses are supplied on these actual functions, rather than asserted to exist on every near-one input.
For \(t\ge0\), let
\[
 \begin{split}
 p_t(Z)&=2^{-2t}\sum_{j=0}^t\binom{2t+1}{2j}Z^j,\\
 q_t(Z)&=2^{-2t}\sum_{j=0}^t\binom{2t+1}{2j+1}Z^j,
 \qquad\pi_t=p_t/q_t,\\
 f&=\sum_{J\in O}G_J,\qquad
 \mathcal T_t=\sum_{J\in O}H_J\pi_t(R_J).
 \end{split}
\]
Then \(f\in\mathbb Z[[x]]\) is nonrational, and every \(\mathcal T_t\) belongs to \(\mathbb Q(x)\cap\mathbb Z_2[[x]]\).
Let \(\rho\) denote the formal shifted Hankel rank, including the polynomial part of a rational function.
For all sufficiently large \(t\),
\[
 \begin{split}
 d_t:=v_2(f-\mathcal T_t)
     &=a(2t+1)+1+e_t,
       \qquad0\le e_t\le C\log(t+2),\\
 \rho_t:=\rho(\mathcal T_t)&=\Delta t+O(1),
       \qquad\delta_J\ge d|J|.
 \end{split}
\]
The lower precision \(d_t\ge a(2t+1)+1\) holds for every \(t\ge0\).
All constants fix \(P,q\), the finite orbit and the rational centers.
In particular \(d_t/\rho_t\to2a/\Delta\).

For the minimum restricted to this common-index family,
\[
 r_s^{\rm fam}=\min\{\rho_t:t\ge0,\ d_t\ge s\},
\]
one has
\[
 r_s^{\rm fam}=\frac{\Delta}{2a}s+O(\log(s+2)),\qquad
 B_h^{\rm fam}:=\sum_{s\ge1}(h-r_s^{\rm fam})_+
       =\frac a\Delta h^2+O(h\log(h+2)).
\]
Here \((u)_+=\max(u,0)\).
For the original shifted leading Hankel determinants \(\mathcal D_h(f)\), the finite elementary-divisor comparison gives \(v_2(\mathcal D_h(f))\ge B_h^{\rm fam}\).
The coefficient \(a/\Delta\) is the exact leading coefficient of this supplied-family counting certificate.
It is not an upper bound or asymptotic equality for the actual determinant valuation, and \(r_s^{\rm fam}\) is not the minimum over all rational approximants.
With \(b=|\bigcup_{J\in O}J|\), the unchanged original all-root contour gives
\[
                   \frac{a\log2}{\Delta}
                         \le\inf_{\tau\ge0}\Phi_b(\tau).
\]

The proof also supplies the complete general number-field valuation lemma (LC1)--(LC13) and the purely geometric rank theorem (PR1)--(PR4).
The latter allows independent component indices for fixed centers, without asserting rational descent for arbitrary index choices.
No good-reduction assumption is required.
No sharp unrestricted rational-approximation rank, uniformity across varying data, near-one arithmetic supply or positive total Mahler gap is claimed.

## Exact inputs and source limits

[C860 v5's explicit Padé normalization](Yin_C_G0860_v5.md#pade-integrality), at its selected assessment linked above, supplies the exact polynomials, formal error identity and rational-map degree; its good-reduction minimum is not invoked.
[C858's private original branches and finite Hankel argument](Yin_C_G0858_v1.md#all-place-hankel-budget), at its [selected assessment](Yin_C_G0858_v1.md#decision-whole-independent-review-2026-11-04), supplies original square-class independence, the same-germ nonrationality, all-level elementary-divisor comparison and the shifted leading-Hankel criterion at its retained BNZ22 scope.
The original modulo-four congruence is the exact adopted input of [C860 v2](Yin_C_G0860_v2.md#statement), with its [selected assessment](Yin_C_G0860_v2.md#decision-whole-independent-review-2026-11-04); integrality of the present germs is checked below.
[C857 v2's residue-factor calculation](Yin_C_G0857_v2.md#all-place-mask-kernel), at its [selected assessment](Yin_C_G0857_v2.md#decision-whole-independent-review-2026-11-04), reuses the accepted integral cyclotomic ring and squarefree modulo-two decomposition, giving the unramified all-place normalization used here.
No Artin--Schreier mask or center-supply conclusion is imported from that Claim.

The only external theorem needed for simultaneous torsion finiteness is [ESS02 Theorem 1.1](../audits/literature/ESS02/Yin_U001.md#ess-exact-counting-bound), read in its complete current source unit for this application.
Its accepted finite-rank tuple-group statement includes the rank-zero group of all torsion tuples, even though that group is not finitely generated.
Its original Subspace Theorem proof and other cited foundations remain outside the retained statement-and-applicability inspection.
The new minimal-block specialization and finite-fiber argument are proved here.
No additional Laurent or torus Manin--Mumford theorem, or new source-original audit, is assumed.

The final contour interface is only [C855 v2 Part C](Yin_C_G0855_v2.md#statement), at its [selected assessment](Yin_C_G0855_v2.md#decision-whole-independent-review-2026-11-04), for the same function, roots, rotations and determinants.
No unreviewed draft proposition is used to supply the centers, residual depths, geometric contour or rank bounds.
The bounded reuse searches found the preceding precise interfaces; their use and the present direct proofs make no novelty or priority claim.

<a id="argument"></a>
<a id="coefficientwise-valuation-lemma"></a>
## A coefficientwise valuation lemma over a fixed number field

Let \(K\) be a number field, let \(\mathfrak p\mid2\), and normalize its valuation by \(v_{\mathfrak p}(2)=1\).
Write \(\mathcal O_{\mathfrak p}\) for the valuation ring of the completion \(K_{\mathfrak p}\).
For a nonzero bounded power series \(F\in K_{\mathfrak p}[[x]]\), define
\[
 v(F)=\min_{r\ge0}v_{\mathfrak p}([x^r]F).
                                                               \tag{LC1}
\]
The minimum exists because the value group is discrete and the coefficient valuations are bounded below.
Reduction after scalar normalization shows \(v(FG)=v(F)+v(G)\): the product of two nonzero series over the residue field is nonzero.
Thus (LC1) extends to a valuation on
\[
                  \mathscr F=\operatorname{Frac}
                              (\mathcal O_{\mathfrak p}[[x]])
\]
by \(v(P/Q)=v(P)-v(Q)\).
This fraction-field valuation is used even when the Laurent expansion of \(P/Q\) has unbounded coefficients.
For example, the inverse of \(2x+x^2\) has valuation zero in this field, although its Laurent coefficients at zero are not bounded below in valuation.
No coefficientwise infimum of that inverse is substituted for \(v\).

Let \(\partial=d/dx\).
For every bounded series \(P\), multiplication of its coefficients by nonnegative integers gives \(v(\partial P)\ge v(P)\), with \(v(0)=+\infty\).
For a fraction, the quotient rule then gives
\[
 v\!\left(\partial\frac P Q\right)
 =v\!\left(\frac{P'Q-PQ'}{Q^2}\right)
 \ge v(P)-v(Q)=v(P/Q).
                                                               \tag{LC2}
\]
Consequently every iterated derivative is nonexpansive for this valuation on \(\mathscr F\).

Fix nonzero series
\[
 A_1,\ldots,A_M\in K[[x]]\cap\mathcal O_{\mathfrak p}[[x]],
 \qquad
 w_1,\ldots,w_M\in xK[[x]]\cap\mathcal O_{\mathfrak p}[[x]],
\]
and assume
\[
 a=\min_jv(w_j)>0,
 \qquad w_i/w_j\notin K\quad(i\ne j).
                                                               \tag{LC3}
\]
All these series and the number field are fixed while the positive integer \(n\) varies.
Put
\[
 F_n=\sum_{j=1}^M A_jw_j^n,
 \qquad
 E_n=\sum_{j=1}^M\frac{A_jw_j^n}{1-w_j^n}.
\]
Then, for every sufficiently large positive integer \(n\), both series are nonzero and
\[
                 v(F_n)=an+O(\log(n+2)),
 \qquad
                 v(E_n)=v(F_n)=an+O(\log(n+2)).
                                                               \tag{LC4}
\]
The constants and the finite exceptional range may depend on all the fixed input data.
The assertion therefore applies on the entire sufficiently large odd subsequence, not only along a selected block or subsequence.

### A fixed derivative matrix isolates each summand

Set \(b_j=A_j'/A_j\) and \(\ell_j=w_j'/w_j\), as elements of \(\mathscr F\).
Define polynomials in an indeterminate \(X\), with coefficients in \(\mathscr F\), by
\[
 M_{0j}(X)=1,
 \qquad
 M_{i+1,j}(X)=\partial M_{ij}(X)
                         +(b_j+X\ell_j)M_{ij}(X).
                                                               \tag{LC5}
\]
For \(0\le i\le M-1\), these satisfy
\[
 M_{ij}(n)=\frac{\partial^i(A_jw_j^n)}{A_jw_j^n},
 \qquad
 \deg_XM_{ij}\le i,
 \qquad
 [X^i]M_{ij}=\ell_j^i.
                                                               \tag{LC6}
\]
Let \(\mathcal M(X)=(M_{ij}(X))_{0\le i\le M-1,\,1\le j\le M}\) and \(\Delta(X)=\det\mathcal M(X)\).
Its leading coefficient at degree \(M(M-1)/2\) is
\[
 [X^{M(M-1)/2}]\Delta(X)
                    =\prod_{i<j}(\ell_j-\ell_i)\ne0.
                                                               \tag{LC7}
\]
Indeed \(\ell_i=\ell_j\) would imply \(\partial(w_i/w_j)=0\).
The field \(\mathscr F\) embeds in \(K_{\mathfrak p}((x))\), and the particular ratios have Laurent coefficients in \(K\); in characteristic zero a Laurent series with zero derivative is constant in \(K\).
This contradicts (LC3), so \(\Delta(X)\) is a nonzero polynomial.

The fixed denominators in \(\Delta\) can be cleared without treating the inverses of the \(w_j\) as bounded series.
For each \(j\), define
\[
 U_{0j}(X)=1,
 \qquad
 U_{h+1,j}(X)=w_j\partial U_{hj}(X)
                       +(X-h)w_j'U_{hj}(X).
\]
Induction gives \(U_{hj}\in(K[[x]]\cap\mathcal O_{\mathfrak p}[[x]])[X]\) and
\[
       \frac{\partial^h w_j^n}{w_j^n}=w_j^{-h}U_{hj}(n).
\]
Leibniz's rule therefore shows that each entry
\[
 A_jw_j^{M-1}M_{ij}(X)
   =\sum_{h=0}^i\binom ih A_j^{(i-h)}
                          w_j^{M-1-h}U_{hj}(X)
                                                               \tag{LC8}
\]
has bounded integral series coefficients in the same number field \(K\).
In particular, with the fixed nonzero series
\[
                         B=\prod_{j=1}^M A_jw_j^{M-1},
\]
one has \(B\Delta(X)\in(K[[x]]\cap\mathcal O_{\mathfrak p}[[x]])[X]\).
Because this polynomial is nonzero, some fixed Taylor coefficient is a nonzero scalar polynomial
\[
                  Q(X)=[x^r](B\Delta(X))\in K[X].
                                                               \tag{LC9}
\]
For every integer \(n\) outside the finite set of integer roots of \(Q\),
\[
              v(\Delta(n))\le v_{\mathfrak p}(Q(n))-v(B).
                                                               \tag{LC10}
\]
This follows by first taking the coefficientwise valuation of the bounded series \(B\Delta(n)\), where comparison with its \(x^r\) coefficient is legitimate.

Choose a fixed positive integer \(c\) clearing the algebraic denominators of the finitely many coefficients of \(Q\), so \(cQ\in\mathcal O_K[X]\).
For \(Q(n)\ne0\), its norm \(N_{K/\mathbb Q}(cQ(n))\) is a nonzero rational integer.
At the archimedean embeddings its absolute value is at most \(C(n+1)^{[K:\mathbb Q]\deg Q}\), for a fixed \(C\).
All valuations above two of \(cQ(n)\) are nonnegative; the contribution of the selected place to the two-adic valuation of this norm is \([K_{\mathfrak p}:\mathbb Q_2]v_{\mathfrak p}(cQ(n))\).
The norm estimate thus gives
\[
                 v_{\mathfrak p}(Q(n))
                         \le C_0+C_1\log(n+2).
                                                               \tag{LC11}
\]
Together with (LC10), this bounds \(v(\Delta(n))\) above by \(O(\log(n+2))\).
This is exactly where coefficients in a fixed number field are used.
No analogous bound is asserted here for arbitrary coefficients in \(\mathbb Q_2\) or \(K_{\mathfrak p}\).

For each positive integer \(n\), (LC2) and (LC6) give \(v(M_{ij}(n))\ge0\), hence all cofactors of \(\mathcal M(n)\) have nonnegative valuation.
Differentiating the sum \(F_n\) through order \(M-1\) gives
\[
 \mathcal M(n)
   \begin{pmatrix}A_1w_1^n\\\vdots\\A_Mw_M^n\end{pmatrix}
       =\begin{pmatrix}F_n\\\partial F_n\\\vdots\\
                        \partial^{M-1}F_n\end{pmatrix}.
\]
Cramer's rule and (LC2) consequently yield, whenever \(Q(n)\ne0\),
\[
           v(F_n)\le v(A_j)+nv(w_j)+v(\Delta(n))
                    \quad(1\le j\le M).
                                                               \tag{LC12}
\]
The same invertible system proves \(F_n\ne0\) at these integers.
Choose a \(j\) with \(v(w_j)=a\) for the upper bound, and use the direct lower bound
\[
                        v(F_n)\ge an+\min_jv(A_j).
\]
Equations (LC10)--(LC12) prove the first part of (LC4), including the finite exceptional range.

Finally, each denominator \(1-w_j^n\) has valuation zero, and
\[
 E_n-F_n=\sum_j\frac{A_jw_j^{2n}}{1-w_j^n},
 \qquad
 v(E_n-F_n)\ge2an+\min_jv(A_j).
                                                               \tag{LC13}
\]
Since \(a>0\), this lower bound is strictly larger than the proved upper bound for \(v(F_n)\) when \(n\) is sufficiently large.
The ultrametric equality then gives \(v(E_n)=v(F_n)\), completing (LC4).
Thus later denominator harmonics cannot cancel the detected first harmonic at asymptotically large indices.

<a id="componentwise-pole-rank"></a>
## Exact leading componentwise rank

### Exact statement for the actual original masks

Use the original monic irreducible reciprocal noncyclotomic power-stable \(P\) of degree \(d\), the odd rotation prime \(q\), the field \(K=\mathbb Q(\zeta_q)\), and the original \(N_J,D_J,G_J\) of C858/C860.
Let \(\mathcal I\) be any fixed finite collection of distinct nonempty masks.
In particular it may be one complete Galois orbit \(O\).
For each \(J\in\mathcal I\), supply a fixed rational center \(H_J\in K(x)\), regular at zero with \(H_J(0)=1\), and put
\[
 R_J=\frac{N_J}{D_JH_J^2},\qquad
 y_J=G_J/H_J,\qquad y_J^2=R_J,\qquad y_J(0)=1,
 \qquad\delta_J=\deg R_J.
                                                               \tag{PR1}
\]
The degree is the reduced rational-map degree in the original variable.
Each \(R_J\) is nonconstant.
Ranks are formal shifted Hankel ranks, equivalently rational pole degrees over an algebraic closure of the coefficient field; for a rational trace the same rank is obtained over \(\mathbb Q_2\).
No finite-place divisibility condition is needed for the following complex rank assertion.

Let \(p_t,q_t\) be exactly the degree-\(t\) odd Padé polynomials of C860 v5 (P1), and put \(\pi_t=p_t/q_t\).
For any nonnegative integer indices \(t_J\), define
\[
       \mathcal F_{\boldsymbol t}
                =\sum_{J\in\mathcal I}H_J\pi_{t_J}(R_J).
\]
Then the formal shifted Hankel rank satisfies
\[
 \boxed{\displaystyle
       \rho(\mathcal F_{\boldsymbol t})
             =\sum_{J\in\mathcal I}\delta_Jt_J+O(1).}
                                                               \tag{PR2}
\]
The bounded term depends on the fixed original input, masks and centers, but is uniform over all choices of the indices.
The independent-index assertion is geometric; arbitrary index choices on a Galois orbit need not give a rational trace.
In particular, with a common index \(t\),
\[
       \rho(\mathcal F_t)=\kappa t+O(1),
       \qquad \kappa=\sum_{J\in\mathcal I}\delta_J.
                                                               \tag{PR3}
\]
Moreover
\[
             \delta_J\ge d|J|,\qquad
             \kappa\ge d\sum_{J\in\mathcal I}|J|.
                                                               \tag{PR4}
\]
For one full orbit this last lower bound is \(d|I||O|\).
The centers in this theorem may have arbitrarily large degrees, but must remain fixed while the approximation indices vary.

### Geometric independence survives extension of constants

For each rotation position \(j\), the rational function
\(P_4(\zeta_q^jx)/P_2(\zeta_q^jx)\) has original simple zeros and poles private to that position.
C858's power-stability argument gives this noncollision over \(\mathbb C\), not merely over \(K\).
Parity of those valuations makes all these rotation square classes independent in \(\mathbb C(x)^\times/\mathbb C(x)^{\times2}\).
Multiplication or division by the square \(H_J^2\) does not change a mask's square class.
Thus for distinct nonempty masks \(J,L\), each of \(R_J,R_L,R_J/R_L\) is a nonsquare in \(\mathbb C(x)\).
In particular the relevant quadratic fields remain distinct and nontrivial after extending constants to \(\mathbb C\).

The common field
\[
                  \mathbb C(x)(y_J,y_L)
\]
is biquadratic.
For an elementary check, if \(R_L\) became a square in \(\mathbb C(x)(y_J)\), write its square root as \(a+b y_J\).
Squaring and comparing the coefficient of \(y_J\) gives \(2ab=0\).
The alternatives would make either \(R_L\) or \(R_L/R_J\) a square in \(\mathbb C(x)\), both impossible.
There are therefore sign automorphisms which invert one \(y\)-sign and leave the other fixed.

On the smooth projective curve of this common field, define
\[
                  w_J=\frac{1-y_J}{1+y_J},\qquad
                  w_L=\frac{1-y_L}{1+y_L}.
                                                               \tag{PR5}
\]
These are nonconstant meromorphic functions.
The sign automorphism for \(y_J\) sends \(w_J\) to \(w_J^{-1}\) and fixes \(w_L\).
Suppose \(w_J^u w_L^v=c\) for integers \(u,v\) and a nonzero complex constant \(c\).
Apply that automorphism and divide the two identities to obtain \(w_J^{2u}=1\).
Nonconstancy forces \(u=0\).
Applying the other sign automorphism then forces \(v=0\).
Thus \(w_J,w_L\) are multiplicatively independent modulo constants.
This geometric independence is essential; distinct field names before extension of constants would not by themselves be an adequate substitute.

### Simultaneous torsion is finite by the accepted ESS theorem

Here is the complete specialization needed for each pair.
Let \(f,g\) be nonconstant meromorphic functions on a fixed irreducible smooth projective complex curve, and assume \(f^u g^v\) is nonconstant whenever \((u,v)\ne(0,0)\).
Then only finitely many points at which both functions are finite and nonzero can have both \(f\) and \(g\) roots of unity.

Because the function field has transcendence degree one, choose a nonzero Laurent-polynomial relation
\[
                 \sum_{e=(a_e,b_e)\in A}
                          c_e f^{a_e}g^{b_e}=0,
                    \qquad c_e\in\mathbb C^\times,
                                                               \tag{PR6}
\]
with a finite set of distinct exponent pairs.
Collect equal monomials first and remove zero coefficients.
At a simultaneous torsion point every term is nonzero.
There is a nonempty subset \(B\subseteq A\), of size at least two, whose evaluated terms sum to zero and have no vanishing nonempty proper subsum.
There are only finitely many possible subsets \(B\).

Choose an anchored exponent \(e_0\in B\), and divide that block relation by \(-c_{e_0}f^{a_{e_0}}g^{b_{e_0}}\).
The resulting equation is
\[
 \sum_{e\in B\setminus\{e_0\}}
       \left(-\frac{c_e}{c_{e_0}}\right)
       f^{a_e-a_{e_0}}g^{b_e-b_{e_0}}=1.                  \tag{PR7}
\]
Its tuple of variable values lies in
\(\Gamma=\mu_\infty^{\,|B|-1}\subset(\mathbb C^\times)^{|B|-1}\).
Every element of this group is torsion, so its multiplicative rank is zero.
It need not be finitely generated, which is allowed by the exact accepted ESS statement.
All coefficients in (PR7) are fixed and nonzero.
Minimality of the block makes the solution nondegenerate: a zero subsum omitting the anchor is prohibited directly, and one containing the anchor would have a prohibited nonempty complement.
The case \(|B|=2\) is also covered, with one variable.
Repeated values of different tuple coordinates cause no problem for that theorem.

ESS therefore permits only finitely many tuples for each fixed block.
For one such tuple, choose any \(e\ne e_0\).
It fixes the value of
\[
                         f^{a_e-a_{e_0}}g^{b_e-b_{e_0}},
\]
which is a nonconstant meromorphic function by the assumed independence.
A nonconstant meromorphic function on a projective curve has a finite fiber at any specified value: its difference from that value has isolated zeros and is not identically zero.
Thus only finitely many curve points yield the selected tuple.
Taking the finite union over tuples and blocks proves the asserted simultaneous-torsion finiteness.
No effective bound, uniformity in the curve or additional external torsion theorem is used.

Apply this argument to (PR5).
For each pair \(J,L\), the projections to the \(x\)-line of their simultaneous torsion points form one fixed finite set \(E_{JL}\).

### Padé poles, including branch and infinity cases

Fix \(t\ge0\) and put \(n=2t+1\).
The exact formula for the Padé denominator is
\[
            q_t(y^2)=
              \frac{(1+y)^n-(1-y)^n}{2^n y},              \tag{PR8}
\]
with its removable value at \(y=0\).
That value is \(n/2^{n-1}\ne0\); the value at \(y^2=1\) is one.
For finite \(y\ne0,\pm1\), its vanishing is equivalent to
\[
                \left(\frac{1-y}{1+y}\right)^n=1.
\]
The excluded root \(w=1\) gives \(y=0\) and is not a denominator zero.
The value \(w=-1\) would correspond to \(y=\infty\), and cannot occur among odd-order \(n\)-th roots.
The remaining \(n-1\) roots are paired by \(w\leftrightarrow w^{-1}\), corresponding to \(y\leftrightarrow-y\).
Each pair gives one distinct finite nonzero value of \(y^2\).
Since \(q_t\) has degree \(t=(n-1)/2\), these are exactly its \(t\) roots, all simple.
For \(t=0\) the set is empty.
The numerator is nonzero at every denominator root, by the coprimality already proved in C860 v5.

Consequently the poles of \(\pi_t(R_J)\) are precisely the pullbacks of those finite denominator roots under \(R_J\).
A zero or pole of \(R_J\) itself contributes no such pole: \(\pi_t(0)=1/n\) and \(\pi_t(\infty)=n\) are finite and nonzero.
At a preimage of a denominator root, the pole order equals the local multiplicity of the rational map \(R_J\).
It is at most \(\delta_J\), independently of \(t\), including at critical points and at \(x=\infty\).
The total pole degree is exactly \(t\delta_J\), by multiplication of rational-map degrees.

Suppose a point is a Padé pole of both \(\pi_{t_J}(R_J)\) and \(\pi_{t_L}(R_L)\).
Their radicand values there are finite and nonzero denominator roots.
A lift to the common biquadratic curve then has \(w_J\) and \(w_L\) roots of unity, of orders dividing \(2t_J+1\) and \(2t_L+1\), respectively.
Changing either lift sign only inverts a root of unity.
Thus the point belongs to \(E_{JL}\).
This argument does not require equal approximation indices.
It covers all moving-pole intersections with one finite set per pair.

### Counting the poles which survive the sum

Let \(E\) be the union of all \(E_{JL}\), all zeros and poles of all fixed centers \(H_J\), and the point infinity.
It is finite and independent of every index.
Outside \(E\), every pole of a summand \(H_J\pi_{t_J}(R_J)\) is a Padé pole private to that summand.
Its center is finite and nonzero there, so multiplication preserves its pole order.
The other summands are holomorphic at that point.
Its entire principal part, and hence its pole order, survives in \(\mathcal F_{\boldsymbol t}\).

At each point of \(E\), the pole order of \(\pi_{t_J}(R_J)\) is at most \(\delta_J\).
Multiplication by the fixed center can add at most its fixed pole order.
These quantities do not grow with \(t_J\), even when the point is a pole for infinitely many indices.
In particular the polynomial part represented by a pole at infinity has only a bounded contribution there.
Since the Padé composition has total pole degree \(t_J\delta_J\), all but a bounded part of that degree lies outside \(E\).
Summing the surviving private poles gives the lower estimate
\[
                    \rho(\mathcal F_{\boldsymbol t})
                       \ge\sum_Jt_J\delta_J-O(1).
\]
For the upper estimate, pole orders of a sum are at most the sums of the component pole orders, and multiplying a rational function by \(H_J\) increases its degree by at most \(\rho(H_J)\).
Therefore
\[
                    \rho(\mathcal F_{\boldsymbol t})
                       \le\sum_Jt_J\delta_J+\sum_J\rho(H_J).
\]
Every summand is regular at zero because \(H_J(0)=R_J(0)=1\).
The formal shifted Hankel rank is its total rational pole degree on the projective line, with infinity included, as in the adopted C860 rank convention.
This proves (PR2)--(PR3), without assuming that ranks add before the pole analysis.

For (PR4), the original \(N_J/D_J\) has \(2d|J|\) distinct finite branch points of odd valuation.
Dividing by \(H_J^2\) changes each valuation by an even integer, so every one remains a zero or pole of nonzero odd order of \(R_J\).
If \(p\) of these points are poles and \(z\) are zeros, then \(p+z=2d|J|\).
The total pole and zero degrees of \(R_J\) are both \(\delta_J\), so \(\delta_J\ge p\) and \(\delta_J\ge z\).
Hence \(\delta_J\ge d|J|\), proving the stated complete original-degree cost.

<a id="supplied-original-orbit-application"></a>
<a id="componentwise-family-profile"></a>
## Supplied fixed centers and the exact leading family certificate

Use the original input, full Galois orbit \(O\), field \(K=\mathbb Q(\zeta_q)\), and germs \(G_J\) of (PR1).
Supply fixed centers \(H_J\in K(x)\), regular at zero with \(H_J(0)=1\), such that
\[
 \sigma(H_J)=H_{\sigma J}
 \quad(\sigma\in\operatorname{Gal}(K/\mathbb Q)),
 \qquad
 H_J,H_J^{-1}\in\mathcal O_{K_{\mathfrak p}}[[x]]
                    \quad(\mathfrak p\mid2).
\]
Put
\[
 R_J=G_J^2/H_J^2,\qquad
 \lambda=\min_{\substack{J\in O\\\mathfrak p\mid2}}
                         v_{\mathfrak p}(R_J-1)\ge3,
 \qquad a=\lambda-2,\qquad
 \delta_J=\deg R_J,\qquad \Delta=\sum_{J\in O}\delta_J.
                                                               \tag{FP1}
\]
These are supplied hypotheses on the actual original functions.
The depth is finite: \(R_J=1\) would make \(G_J=H_J\) rational, contrary to its original odd branch valuations.
The cyclotomic field of odd prime conductor is unramified above two; equivalently its integral cyclotomic residue polynomial is squarefree.
Thus the depths in (FP1), with \(v_{\mathfrak p}(2)=1\), are integers, and the indicated minimum is attained.

Set
\[
 y_J=G_J/H_J,\qquad
 w_J=\frac{1-y_J}{1+y_J},\qquad
 f=\sum_{J\in O}G_J,\qquad
 \mathcal T_t=\sum_{J\in O}H_J\pi_t(R_J),\quad n=2t+1.
\]
The original congruence \(P_4\equiv P_2\pmod4\) gives \(N_J/D_J\in1+4x\mathcal O_K[[x]]\).
For every \(r\ge1\), \(v_2(4^r\binom{1/2}{r})=s_2(r)\ge1\), and these binomial coefficients have only powers of two in their denominators.
Here \(s_2(r)\) is the number of ones in the binary expansion of \(r\).
Thus every \(G_J\) has algebraic-integral coefficients, and the complete Galois orbit sum \(f\) has integer coefficients.
At each place, the normalized binomial expansion gives
\(y_J\equiv1\pmod{2^{v_{\mathfrak p}(R_J-1)-1}}\).
Hence \((1+y_J)/2\) is an integral power-series unit and
\[
       w_J=-\frac{R_J-1}{(1+y_J)^2},\qquad
       v_{\mathfrak p}(w_J)
                        =v_{\mathfrak p}(R_J-1)-2.
                                                               \tag{FP2}
\]
Equivariance and transitivity of the Galois action on the places above two imply
\[
                  \min_{J\in O}v_{\mathfrak p}(w_J)=a
                      \quad\text{for every }\mathfrak p\mid2.
\]
In detail, an entry and place attaining the global minimum in (FP1) can be carried to the specified place, while its mask stays in the full orbit.
Every \(G_J\) is integral there and has valuation zero because its constant coefficient is one.
All coefficients of these series remain in the fixed number field \(K\).

The geometric square-class argument in (PR5) excludes constant ratios \(w_J/w_L\) for distinct masks.
Apply (LC4) with \(A_J=G_J\) and the exact Padé identity
\[
        f-\mathcal T_t
              =-2\sum_{J\in O}\frac{G_Jw_J^n}{1-w_J^n}.
\]
The Padé normalization and the supplied integral centers make every \(\mathcal T_t\) integral at all places above two.
The full equivariant sums have rational coefficients; hence \(\mathcal T_t\in\mathbb Q(x)\cap\mathbb Z_2[[x]]\), and their local coefficientwise valuations agree with \(v_2\).
Therefore, for every sufficiently large \(t\),
\[
 d_t:=v_2(f-\mathcal T_t)
       =a(2t+1)+1+e_t,\qquad
              0\le e_t\le C\log(t+2),\qquad
 \rho_t:=\rho(\mathcal T_t)=\Delta t+O(1).
                                                               \tag{FP3}
\]
The lower precision \(d_t\ge a(2t+1)+1\) holds for every \(t\ge0\), by the componentwise normalized error formula.
The rank statement is (PR3), with \(\delta_J\ge d|J|\).
All constants fix the input, orbit and centers.
In particular \(d_t/\rho_t\to2a/\Delta\).

Define the minimum rank restricted to this common-index family by
\[
 r_s^{\rm fam}
       =\min\{\rho_t:t\ge0,\ d_t\ge s\},\qquad s\ge1.
                                                               \tag{FP4}
\]
This is not the minimum over all rational approximants.
The set is nonempty because the guaranteed precision tends to infinity.
Also \(d_t<\infty\) for every finite \(t\): the original sum \(f\) is nonrational by the private-square-class argument, whereas \(\mathcal T_t\) is rational.
Thus no finite exceptional approximation index has infinite precision.

The exact family profile is
\[
                 r_s^{\rm fam}
                       =\frac{\Delta}{2a}s+O(\log(s+2)).
                                                               \tag{FP5}
\]
For the upper bound, choose
\[
             t=\max\!\left(0,
                       \left\lceil\frac{s-a-1}{2a}\right\rceil
                        \right).
\]
It reaches the requested precision and gives
\(r_s^{\rm fam}\le\Delta s/(2a)+O(1)\).
Choose any index attaining the minimum in (FP4).
The rank estimate in (FP3) and this upper bound imply that this minimizing index is \(O(s+1)\).
For sufficiently large \(s\), it lies beyond the finite exceptional range of the precision estimate, because every depth at an exceptional index is finite.
The upper bound on \(d_t\) now gives
\[
                   s\le2at+O(\log(s+2)),
\]
and hence \(r_s^{\rm fam}\ge\Delta s/(2a)-O(\log(s+2))\).
This proves (FP5), without assuming that individual ranks or depths increase monotonically.

For the elementary-divisor counting certificate of this family, put
\[
                B_h^{\rm fam}
                      =\sum_{s\ge1}\max(h-r_s^{\rm fam},0).
\]
Then
\[
       B_h^{\rm fam}
               =\frac a\Delta h^2+O(h\log(h+2)),
       \qquad
       \lim_{h\to\infty}\frac{B_h^{\rm fam}}{h^2}
                         =\frac a\Delta.                  \tag{FP6}
\]
To check the sum, set \(c=\Delta/(2a)>0\).
Equation (FP5) implies \(r_s^{\rm fam}\ge cs/2\) for all sufficiently large \(s\).
Only \(O(h)\) terms can therefore contribute.
On that range the positive-part function is one-Lipschitz, and replacing \(r_s^{\rm fam}\) by \(cs\) changes the sum by \(O(h\log(h+2))\).
The remaining arithmetic triangle satisfies
\(\sum_{s\ge1}\max(h-cs,0)=h^2/(2c)+O(h)\), proving (FP6).

Let \(\mathcal D_h(f)\) be the original shifted leading Hankel determinants.
C858's finite elementary-divisor argument applies at every attained family precision, so
\[
                       v_2(\mathcal D_h(f))\ge B_h^{\rm fam}.
\]
Equation (FP6) identifies the exact leading coefficient of this particular lower-bound certificate.
It is not an asymptotic equality or upper bound for the actual determinant valuations.
It is also not a lower bound on the minimum rank among all rational approximants.
The original all-root contour therefore retains the paid consequence
\[
               \frac{a\log2}{\Delta}
                    \le\inf_{\tau\ge0}\Phi_b(\tau),
                 \qquad b=\left|\bigcup_{J\in O}J\right|,
                                                               \tag{FP7}
\]
using the same original function and infinitely many nonzero determinants.
No constants are asserted to be uniform across changing polynomials, centers, fields or orbits.
Centers varying with the approximation index and genuinely different joint approximants remain outside the theorem.

<a id="nonconstant-ratio-boundary"></a>
## Necessity of the nonconstant-ratio hypothesis

The nonconstant-ratio hypothesis cannot simply be dropped.
For an integer \(a\ge1\), take \(y=\sqrt{1+2^{a+2}x}\), \(y(0)=1\), and \(w=(1-y)/(1+y)\in x\mathbb Q[[x]]\), whose exact two-adic depth is \(a\).
Set \(w_1=w\), \(w_2=-w\) and \(A_1=A_2=1\).
For odd \(n\),
\[
 \frac{w^n}{1-w^n}+\frac{(-w)^n}{1-(-w)^n}
                      =\frac{2w^{2n}}{1-w^{2n}},
\]
whose depth is \(2an+1\).
The corresponding Cayley radicals are inverses and generate the same quadratic field, so this control violates the original distinct-square-class condition.
It is not an original-input counterexample to (FP3).

## Scope and limits

The proofs establish the fixed-input common-index family profile and its stated preliminary lemmas.
All quantities use the original degree, conjugates, variable and total logarithmic Mahler target.
Centers or orbits varying with the approximation index, arbitrary joint rational approximants and a uniform near-one supply remain outside this result.
The exact leading certificate is a lower-bound mechanism, not an upper bound on actual Hankel divisibility.
No unrestricted Lehmer conclusion has been obtained.

## Current assessment
[Selected decision](#decision-whole-independent-review-2026-11-04)

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T23:01 |
| status | proved |
| reason | Adopt the complete statement and LC1--LC13, PR1--PR8, FP1--FP7 after independent R1076 v6. The fixed number-field derivative argument bounds extra precision logarithmically, the geometric/ESS argument pays the exact leading sum of component pole degrees, and their combination determines the common-index family's rank profile and elementary-divisor certificate. The centers and all-place depth remain supplied hypotheses. Earlier fixed scopes and source-proof limits are unchanged; neither arbitrary joint approximants nor an upper bound on actual determinant valuations or unrestricted G0001 completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Supplied fixed original orbit and centers, general LC/PR conclusions, exact leading precision and rank, family minimum and certificate, same-input contour return and all exclusions. |
| argument | [Complete proof](#argument) | All LC1--LC13, PR1--PR8, FP1--FP7 and constant-ratio control, including all fixed-input, number-field, geometric, valuation and finite-exception conditions. |
| dependency | [Exact Pade identities and rank convention](Yin_C_G0860_v5.md#pade-integrality) | Normalized even/odd identities, integral unit substitution, coprimality and map degree; no good-reduction minimum imported. |
| dependency | [Original modulo-four input](Yin_C_G0860_v2.md#statement) | Only P4 minus P2 divisibility by four for the same original polynomial, at retained source scope. |
| dependency | [Original branches and finite Hankel inputs](Yin_C_G0858_v1.md#all-place-hankel-budget) | Geometric square classes, same-germ nonrationality, all-level finite elementary-divisor comparison and accepted shifted leading-Hankel criterion, without an uncentered modulo-eight premise. |
| dependency | [Cyclotomic all-place normalization](Yin_C_G0857_v2.md#all-place-mask-kernel) | Integral cyclotomic ring and squarefree residue-factor/unramified normalization only; no mask classification or center-supply premise. |
| dependency | [Same original contour](Yin_C_G0855_v2.md#statement) | Only Part C for the identical germ, determinant shift, original branch endpoints and rotation union, at fixed-input capacity scope. |
| support | [ESS02 canonical source](../audits/literature/ESS02/Yin_U001.md#ess02-u001) | Accepted Theorem 1.1 for characteristic-zero fields and finite-rank tuple groups, including rank-zero torsion groups without finite generation, at retained statement/applicability and original-proof limits. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1076_v6.md#componentwise-pade-whole) | Complete statement and all LC/PR/FP deductions, exact accepted interfaces, boundary example, fixed family scope and original-task limits. |
