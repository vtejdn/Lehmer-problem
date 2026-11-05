---
author: Yin
---
# Independent whole review of fixed componentwise Pade precision, pole rank and family certificate

Review act: 2026-11-04T23:00.
The human record author is Yin.
This is a separately organized whole-proof agent review of the fixed [C0860 v7 statement](../../claims/Yin_C_G0860_v7.md#statement) and [complete argument](../../claims/Yin_C_G0860_v7.md#argument), including LC1--LC13, PR1--PR8, FP1--FP7 and the constant-ratio boundary example.
The reviewer did not participate in substantive proof development and received no proof-generation dialogue, development notes, proposing-agent mathematical explanation or prior verdict on this candidate.
The fixed candidate and directly necessary fixed inputs were read.
The candidate's contributor paragraphs were visible but supplied no review evidence.
The exact obligations and initial mathematical findings were formed before consulting R1076 v5.
No rolling Draft, numerical probe or temporary development material was consulted, and no substantive proof repair was supplied.
The candidate had no selected assessment during this review.

## Earlier findings and accepted-input limits

[R1076 v1](Yin_R_G1076_v1.md#precision-budget-whole), [v2](Yin_R_G1076_v2.md#mask-depth-whole), [v3](Yin_R_G1076_v3.md#fixed-center-whole), [v4](Yin_R_G1076_v4.md#pade-minimum-rank-whole) and [v5](Yin_R_G1076_v5.md#bad-reduction-whole) remain the complete fixed homes of their earlier findings, exact inputs, relationships, dates and adoption scopes.
The new same-topic review neither replaces those records nor transfers their conclusions to this candidate.
After forming the initial findings, the reviewer read R1076 v5 to preserve those boundaries.
Its preceding single-radical and bad-reduction findings do not supply the present multiple-component precision or rank conclusion.

The directly checked project interfaces were C0860 v5's exact Pade identities and formal shifted-rank convention, C0860 v2's adopted original modulo-four congruence, C0858's geometric branches and finite Hankel comparison, C0857 v2's cyclotomic residue-factor normalization, and C0855 v2 Part C's original all-root contour.
The relevant proofs and hypotheses were checked at those uses.
The good-reduction minimum of C0860 v5, the bad-reduction estimates of v6 and the center-supply classification of C0857 are not premises of v7.

The complete current [ESS02 source unit](../literature/ESS02/Yin_U001.md#ess02-u001) was read.
Its accepted input is Theorem 1.1 in Evertse--Schlickewei--Schmidt, *Linear equations in variables which lie in a multiplicative group*, Annals of Mathematics (2) 155 (2002), 807--836, as retained in arXiv:math/0409604v1.
The exact statement, nondegeneracy condition and tuple-group rank scope at printed pp. 807--808 and 810 are reused at the unit's existing statement-and-applicability inspection depth.
No new original-PDF inspection, Subspace Theorem proof audit or recursive audit of its foundations was performed.
The minimal-block and finite-fiber specialization in the present candidate was checked directly.

The formal rank convention retains C0860 v5's Par88/BR10 source limits, including the polynomial part and no bounded-operator assertion.
The Pade/Cayley mechanism retains its Kou11 attribution without relying on the two excluded intermediate source recurrences.
The original modulo-four congruence retains C0860 v2's Dimitrov v1 Lemma 2.1 scope.
The cyclotomic integer-ring input retains C0857 v2's Bel17 statement scope.
The BNZ22 shifted leading-Hankel criterion and C0855 v2's capacity identities retain their recorded source-inspection limits.
None of these original sources was newly re-audited.
The inspected project erratum was empty.

<a id="componentwise-pade-whole"></a>
## Whole fixed-family finding

**Finding:** no unresolved mathematical gap was found in the entire C0860 v7 statement and proof under its supplied fixed-input hypotheses and accepted-source limits.
The general number-field valuation lemma, the geometric pole-rank theorem with independent component indices, the common-index exact leading precision and rank, the family minimum and counting certificate, and the original determinant/contour consequence are supported.
The explicit finite, exact and asymptotic claims are distinguished below.
This review makes no Claim assessment or Task-completion decision.

The initial obligations were the fraction-field valuation and derivative argument, fixed-number-field scalar estimate, all geometric pole cases and possible cancellations, exact ESS hypotheses, all-place arithmetic descent, finite exceptional indices, unrestricted minimization within the stated family, and return to the same original determinants.
No missing step was supplied as a substantive repair.

### LC1--LC2: the valuation is on the correct field

A nonzero coefficient-bounded series over the discrete local value group has an attained minimum coefficient valuation.
After multiplying by scalars to make both minima zero, reduction to the residue power-series domain proves multiplicativity.
This gives a well-defined valuation on the fraction field of the integral power-series ring.
Every bounded series belongs to that fraction field after scalar normalization.

Differentiation multiplies coefficients by nonnegative integers, so it cannot lower this valuation on bounded series.
For a fraction \(P/Q\), the quotient numerator has valuation at least \(v(P)+v(Q)\), and division by \(Q^2\) proves LC2.
The field embeds in \(K_{\mathfrak p}((x))\), but the valuation need not equal an infimum of Laurent-coefficient valuations for unbounded expansions.
The displayed inverse of \(2x+x^2\) correctly illustrates that distinction.
No boundedness assertion about the inverses of the \(w_j\) is used later.

### LC3--LC13: fixed inputs prevent a linear extra cancellation depth

The recursion LC5 is the product rule for the derivatives of \(A_jw_j^n\).
It has degree at most \(i\) in the exponent parameter and leading coefficient \(\ell_j^i\).
The leading coefficient of its determinant is therefore the stated Vandermonde product.
If two \(\ell_j\) agreed, the quotient of the corresponding \(w_j\) would have zero formal derivative.
Its Laurent coefficients are in \(K\), so characteristic zero would make it a constant in \(K\), contrary to LC3.
This argument also covers \(M=1\), where the determinant is one.

The \(U_{hj}\) recursion clears exactly the denominator \(w_j^h\) in the derivative ratio \(\partial^h(w_j^n)/w_j^n\).
Leibniz's formula then gives LC8 with integral bounded series coefficients, since \(h\le i\le M-1\).
The product \(B\) is nonzero, and a nonzero coefficient polynomial \(Q\in K[X]\) exists because \(B\Delta(X)\) is nonzero.
Outside the finite integer-root set of \(Q\), the coefficient comparison gives LC10 with the displayed inequality direction.

After one integer clears the algebraic denominators of \(Q\), its nonzero field norm is a nonzero rational integer.
The archimedean product grows at most polynomially in the positive integer \(n\).
All local contributions above two are nonnegative, and the selected one is exactly \([K_{\mathfrak p}:\mathbb Q_2]v_{\mathfrak p}(cQ(n))\) with the chosen normalization.
Thus LC11 is valid even when \(K\) is ramified.
The fixed number field is essential; the proof does not replace algebraic coefficients by arbitrary local-field coefficients.

LC2 gives nonnegative valuation for every evaluated matrix entry and hence for its cofactors.
Cramer's rule bounds the valuation of a summand below by \(v(F_n)-v(\Delta(n))\), which is precisely the rearranged upper bound LC12.
The invertible system also excludes \(F_n=0\).
Selecting a summand with minimum \(v(w_j)=a\), and combining with the elementary lower bound, proves the first assertion of LC4 for all sufficiently large positive integers.

Each \(1-w_j^n\) has valuation zero and an integral power-series inverse.
The difference \(E_n-F_n\) has depth at least \(2an+\min_jv(A_j)\).
Because \(a>0\), this exceeds the logarithmic-error upper bound for \(F_n\) for every sufficiently large \(n\), so the ultrametric equality gives \(v(E_n)=v(F_n)\).
The assertion holds on the whole eventual odd subsequence and leaves only finitely many exceptional indices.
It gives no effective or uniform bound for that exceptional range.

### PR1--PR7: geometric independence and the exact ESS use

Power-stability excludes root-of-unity quotients among distinct conjugates, since a common positive power would collapse the degree.
A squared and fourth-powered conjugate cannot agree up to a root of unity, because their positive absolute heights differ by a factor of two.
Consequently all rotated squared and fourth-powered root positions are simple and private over \(\mathbb C\), not just over the original coefficient field.

Parity at these private positions proves independence of the rotation square classes after extension of constants.
Division by a rational square changes none of them.
For two distinct nonempty masks, both radicands and their quotient remain nonsquares, so their common quadratic extension is biquadratic.
The elementary \(a+b y_J\) calculation checks the necessary field-degree assertion directly.

Each \(y_J\), and hence its Cayley function \(w_J\), is nonconstant.
The two sign automorphisms separately invert the corresponding \(w\).
Applying them to a putative monomial relation modulo constants forces each exponent to vanish.
This proves multiplicative independence modulo \(\mathbb C^\times\), in particular excluding the constant-ratio failure relevant to LC3.

A nonzero Laurent-polynomial relation exists on the common transcendence-degree-one curve.
After equal monomials are collected, its exponent vectors are distinct and its coefficients are fixed and nonzero.
At a simultaneous torsion point, choose a minimal vanishing block.
The block has at least two terms and gives the normalized equation PR7.

The tuple group \(\mu_\infty^{|B|-1}\) has rank zero and is permitted by the retained ESS statement even though it is not finitely generated.
The coefficient field is characteristic zero, the coefficients are fixed and nonzero, and the normalized solution is nondegenerate by the minimal-block/complement argument.
The one-variable case and repeated coordinate values are allowed.
ESS therefore gives finitely many tuples for each of finitely many blocks.

For a fixed tuple, any nonanchor exponent difference is nonzero and defines a nonconstant meromorphic monomial by the established independence.
Its specified fiber on the smooth projective curve is finite.
Taking the finite union proves the required torsion-point finiteness and then the finite projected set \(E_{JL}\).
This is a direct application of the accepted ESS theorem, not reliance on an additional torus torsion theorem or on an effective bound.

### PR8 and PR2--PR4: every pole case and bounded cancellation

The even/odd binomial expansion gives PR8 with the normalization \(2^n y\).
The removable value at \(y=0\) is \(n/2^{n-1}\), and the value at \(y^2=1\) is one.
For odd \(n\), the nontrivial \(n\)-th roots of unity exclude both \(w=1\) as a denominator zero and \(w=-1\).
Inversion pairs correspond to \(y\) and \(-y\), giving exactly \(t\) distinct finite nonzero roots of \(q_t\), all simple.
C0860 v5's coprimality excludes numerator cancellation there.
For \(t=0\), the map is constant and there are no such roots.

At a preimage of a denominator root, pole order is exactly the local multiplicity of \(R_J\), at most its fixed degree \(\delta_J\).
This includes critical points and infinity.
At \(R_J=0\) and \(R_J=\infty\), the Pade map has the finite nonzero values \(1/n\) and \(n\), so no omitted radicand branch pole contributes a growing order.
Composition has total pole degree \(t_J\delta_J\).

A pole shared by two components lifts to simultaneous torsion on their common curve, irrespective of the two approximation indices.
Changing either square-root sign merely inverts a root of unity.
All such intersections lie in the one fixed finite set supplied for the pair.

Adjoining all center zeros and poles and infinity gives a fixed finite exceptional set.
Outside it, a component's Pade pole is private, multiplication by its center preserves its order, and its principal part cannot cancel in the sum.
At each exceptional point the composition's pole order is bounded by \(\delta_J\); a fixed center adds at most its fixed pole order.
Thus the lost total pole degree is uniformly bounded over all index choices.
The sum-of-pole-orders upper bound gives the other side of PR2.
The formal shifted Hankel rank equals total projective pole degree, including the polynomial part, because the rational functions are regular at zero.

There are \(2d|J|\) original finite branch points of odd valuation.
Each remains a zero or pole of odd nonzero order after division by \(H_J^2\).
The total zero and pole degrees both equal \(\delta_J\), giving \(\delta_J\ge d|J|\).
No zero-count assumption after reduction modulo two or additive-rank assumption before the pole analysis enters this proof.
Equivariance is unnecessary for the geometric independent-index assertion and is not asserted to hold for arbitrary index choices.

### FP1--FP3: arithmetic normalization on the supplied original functions

The original modulo-four congruence gives \(N_J/D_J\in1+4x\mathcal O_K[[x]]\).
For \(r\ge1\), the exact valuation of \(4^r\binom{1/2}{r}\) is \(s_2(r)\), and these rational numbers have no odd-prime denominator.
Their substitution proves algebraic integrality of each \(G_J\).
The complete equivariant orbit sum therefore has integer coefficients.
The geometric character argument also proves its nonrationality without an uncentered modulo-eight hypothesis.

Each center is a supplied integral power-series unit at every place above two.
Thus \(R_J\) is integral there, and the nontrivial branch class ensures \(R_J-1\ne0\).
Discreteness makes each positive depth finite and attained.
The accepted cyclotomic integer ring and squarefree residue polynomial make all these places unramified, so the normalized depths are integers.

The square root \(y_J=G_J/H_J\) is the unique branch with constant one.
At the selected place, put \(\lambda_J=v_{\mathfrak p}(R_J-1)\).
The binomial expansion at depth at least three gives \(y_J-1\) divisible by \(2^{\lambda_J-1}\).
Therefore \((1+y_J)/2\) is an integral unit, and the exact identity FP2 gives \(v_{\mathfrak p}(w_J)=\lambda_J-2\).
The full orbit and Galois transitivity on places carry a globally minimizing pair to every chosen place while keeping its mask in the orbit.
Thus the minimum depth of the \(w_J\) is the same positive integer \(a\) at every place.

The \(G_J\) have valuation zero because they are integral with constant one.
The \(w_J\) are nonzero integral series in \(xK[[x]]\), and their pairwise ratios are nonconstant.
All hypotheses of LC4 are therefore supplied with \(A_J=G_J\).
The exact error identity has the factor \(-2\), giving depth \(a(2t+1)+1+O(\log(t+2))\).
The componentwise lower bound applies at every index and makes the excess \(e_t\) nonnegative.

The even/odd Pade identities give integral numerators and denominator units after substituting each \(R_J\); multiplication by the supplied center preserves integrality.
Common indices and equivariance make the sum a rational function over \(\mathbb Q\).
Local coefficientwise valuations of the error series with rational coefficients agree with \(v_2\).
This proves the claimed descent and FP3, with \(\Delta>0\) and constants depending only on the fixed input and centers.
No good-reduction minimum or existence of such centers on every original input is used.

### FP4--FP7: the family minimum and complete determinant return

At every precision the family is nonempty by its guaranteed depth, so its nonnegative integer ranks attain a minimum.
Each finite-index depth is finite because an identically zero error would make the nonrational original \(f\) rational.
This removes the only possible obstruction from a permanently exact exceptional approximant.

The displayed ceiling choice supplies the upper rank bound with leading coefficient \(\Delta/(2a)\).
A minimizing index is \(O(s+1)\) by the matching linear growth of its rank.
For large \(s\) it leaves the finite exceptional depth range.
The eventual precision upper bound then gives the lower rank bound with error \(O(\log(s+2))\).
No monotonicity of individual ranks or depths is assumed.

The family profile implies that only \(O(h)\) precision levels can contribute to \(B_h^{\rm fam}\).
On this range, the positive-part function is one-Lipschitz, so replacing the rank profile by its linear term costs \(O(h\log(h+2))\).
The remaining arithmetic triangle has leading coefficient \(a/\Delta\).
This proves the exact leading coefficient of the family's counting certificate.

At each precision, the chosen approximant has an integral finite Hankel matrix of rational rank at most \(r_s^{\rm fam}\).
C0858's finite elementary-divisor argument applies to that approximation and the same original shifted matrix.
It may be applied separately at each level and then summed; the approximants need not be coherent across levels.
This yields the exact inequality \(v_2(\mathcal D_h(f))\ge B_h^{\rm fam}\).

The original integer \(f\), its nonrationality and the accepted shifted Kronecker criterion give infinitely many nonzero integer determinants.
Their logarithms have lower quadratic coefficient \(a\log2/\Delta\).
C0855 v2 Part C applies to this identical germ, original powered roots, full used rotation union and determinant shift.
Its contour includes neutral and contracting endpoints as specified there, and artificial center poles do not alter the original germ.
For each fixed contour parameter, its upper bound therefore gives FP7; taking the infimum preserves that inequality.
The input and contour are fixed before the Hankel-size limit, and no changing-input uniformity is required.

### Boundary example and excluded conclusions

For the displayed \(y=\sqrt{1+2^{a+2}x}\), the Cayley function has exact coefficientwise depth \(a\).
For odd \(n\), the two terms with \(w\) and \(-w\) sum exactly to \(2w^{2n}/(1-w^{2n})\), of depth \(2an+1\).
Their quotient is constant and their Cayley radicals are inverses in one quadratic field.
The example therefore demonstrates the need for LC3 without contradicting the original private-square-class situation.

The result establishes the fixed common-index family's asymptotic minimum, not the minimum over all rational approximants.
Its exact leading certificate is a lower-bound mechanism, not equality or an upper bound for actual determinant valuations.
Centers varying with the approximation index, changing polynomials or orbits, uniform constants, arbitrary joint approximants and a near-one arithmetic supply remain outside the theorem.
The original unrestricted positive total logarithmic Mahler gap is unresolved.
This is an independent mathematical text review, not formal verification, numerical certification or a novelty audit.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [C0860 v7 statement](../../claims/Yin_C_G0860_v7.md#statement) | Complete statement, supplied original hypotheses, LC and PR generality, exact and asymptotic family conclusions, determinant inequality, contour consequence and exclusions. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [C0860 v7 complete argument](../../claims/Yin_C_G0860_v7.md#argument) | Entire LC1--LC13, PR1--PR8, FP1--FP7, boundary control, fixed-input constants, source interfaces and scope limits. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Coefficientwise valuation lemma](../../claims/Yin_C_G0860_v7.md#coefficientwise-valuation-lemma) | Fraction-field valuation, derivatives, determinant, fixed-number-field norm bound, Cramer isolation and eventual first-harmonic equality. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Componentwise pole rank](../../claims/Yin_C_G0860_v7.md#componentwise-pole-rank) | Geometric square classes, ESS torsion specialization, denominator roots, branch/infinity cases, independent indices and bounded center/cancellation losses. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Supplied original orbit application](../../claims/Yin_C_G0860_v7.md#supplied-original-orbit-application) | All-place depth normalization, exact Pade error, arithmetic descent, positive rank slope and original branch-degree cost. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Complete family certificate](../../claims/Yin_C_G0860_v7.md#componentwise-family-profile) | Family minimum, finite exceptions, all-level elementary-divisor sum, exact leading certificate and original all-root contour return. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Constant-ratio boundary](../../claims/Yin_C_G0860_v7.md#nonconstant-ratio-boundary) | Exact odd-index cancellation example and its exclusion by the original distinct-square-class hypotheses. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Accepted Pade normalization](../../claims/Yin_C_G0860_v5.md#pade-integrality) | Exact even/odd identities, integral unit substitution, normalized error, coprimality and composition degree; no good-reduction optimality imported. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Formal rational rank and source scope](../../claims/Yin_C_G0860_v5.md#exact-inputs-and-source-scope) | Polynomial-inclusive shifted Hankel rank over characteristic-zero fields and retained Par88/BR10/Kou11 limits; no new original-source audit. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Original modulo-four input](../../claims/Yin_C_G0860_v2.md#statement) | Only the adopted original P4 minus P2 divisibility by four and its retained Dimitrov v1 source scope. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Original branches and finite Hankel inputs](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) | Geometric private branches, same-germ nonrationality, all-level finite elementary-divisor lemma and BNZ22 shifted criterion; no uncentered modulo-eight premise imported. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Cyclotomic residue normalization](../../claims/Yin_C_G0857_v2.md#all-place-mask-kernel) | Accepted integral cyclotomic ring, squarefree modulo-two factors and all-place unramified normalization; no mask classification or center supply imported. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [ESS02 complete source unit](../literature/ESS02/Yin_U001.md#ess02-u001) | Current complete unit read; accepted Theorem 1.1, characteristic-zero field, nonzero coefficients, nondegeneracy and finite-rank tuple-group scope, with original-proof and source-edition limits retained. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [ESS exact counting statement](../literature/ESS02/Yin_U001.md#ess-exact-counting-bound) | Rank-zero all-torsion tuple group, allowed lack of finite generation, one-variable case and repeated coordinates; new minimal-block/finite-fiber deduction checked in v7. |
| [Whole componentwise Pade finding](#componentwise-pade-whole) | [Original all-root contour](../../claims/Yin_C_G0855_v2.md#statement) | Accepted Part C only, identical original function, all used rotations and roots, shifted determinants, fixed-input contour limit and Phi bound; no p=2 or norm-descent conclusion imported. |
