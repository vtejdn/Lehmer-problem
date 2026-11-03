---
author: Yin
---

# G0001 exploration: structure behind the short orbit-Gram window

Date: 2026-10-06.
Assigned structural investigation for Yin, continuing the same authorized exploration.
This preserves the original structural exploration and unresolved full-core question.
The complete exact structural result now belongs to [C214](../claims/Yin_C_G0214_v1.md#statement), with the actual formal findings in [R506](../audits/reviews/Yin_R_G0506_v1.md); no Task completion or Lehmer solution is recorded.

## 1. Question, reused inputs, and outcome

The unresolved short-window question is whether
\[
R_{2d}(p):=\frac{\Delta(p)G_{2d}(p)}{(2d)^d}>1 \tag{1}
\]
for every monic irreducible reciprocal noncyclotomic unit polynomial \(p\in\mathbb Z[t]\), of degree \(d\).
Here \(V_N\) has columns \(t^j\bmod p\), in the power basis, \(W_N=V_NV_N^{\mathsf T}\), \(G_N=\det W_N\), and \(\Delta(p)=|\operatorname{disc}p|\).
The [complete finite Gram theorem](../claims/Yin_C_G0209_v1.md#gram-lower-certificate) proves
\[
G_N=D_{N-d},\qquad
m(p)\ge\frac{\log R_N(p)}{2(N-1)},\qquad
R_N(p)=\frac{\Delta(p)G_N}{N^d}.
\tag{2}
\]
Its exact finite enumeration and stronger-threshold failures are reused by link, not rerun or enlarged here.
A strict integer surplus in (1) still does not supply the exponential surplus required for a uniform entropy gap.

This segment obtains four structural statements with elementary proofs below:

1. An integral inverse-trace form turns \(\Delta G_N\) into the determinant of an integral matrix with real spectrum, trace \(Nd\), and a precisely identifiable inertia.
   These coarse matrix properties alone do not imply (1).
2. The real-coefficient relaxation of (1) has an explicit counterexample and an arbitrary-degree family of counterexamples.
   Integrality is therefore substantive.
3. There is an explicit irreducible integral reciprocal family of unbounded degree with exponential surplus at \(N=2d\).
   The totally real core also satisfies (1), using the already audited statement of Schinzel's restricted bound.
4. For Salem polynomials, short-window positivity implies \(m(p)>1/(2d)\), using the unique negative trace-form eigenvalue.
   This is a necessary degree-dependent house bound, not a uniform Mahler gap or a converse to (1).

No counterexample or proof of (1) on the full core is obtained.
No new enumeration or numerical experiment is performed in this draft.

The local inputs are (2), its [time-dilation identity](../claims/Yin_C_G0209_v1.md#degree-window-tests), and the [Smy08 restricted-height interface](../audits/literature/Smy08/Yin_U002.md#smy08-restricted-height-gap).
Their existing source-inspection boundaries are unchanged.
The trace-form calculation below is proved directly; its historical attribution has not been settled and no novelty is claimed.

<a id="inverse-trace-orbit"></a>
## 2. The inverse-trace form and the missing matrix constraint

Assume throughout this section that \(p\) is monic, irreducible, reciprocal, and a unit, and has degree \(d>1\).
Then \(p(0)=1\), its roots are distinct and nonzero, and \(K=\mathbb Q(\alpha)\), \(p(\alpha)=0\), has an involution
\[
x\longmapsto x^\dagger,\qquad \alpha^\dagger=\alpha^{-1}.
\]
It is well defined because substitution \(t\mapsto t^{-1}\) preserves the relation \(p(t)=0\).
Its square is the identity.
In the power basis, put
\[
H_{ij}=\operatorname{Tr}_{K/\mathbb Q}(\alpha^{i-j}),
\qquad 0\le i,j<d. \tag{3}
\]
Every power, including a negative power, is an algebraic integer, so \(H\) is integral.
Inversion permutes the conjugates, so \(\operatorname{Tr}(\alpha^k)=\operatorname{Tr}(\alpha^{-k})\) and \(H\) is symmetric.
It represents the real bilinear form
\[
B(x,y)=\operatorname{Tr}_{K/\mathbb Q}(xy^\dagger).
\]

Let \(E=(\alpha_i^j)\), and let \(P\) be the permutation matrix which pairs a root with its inverse.
Then
\[
H=E^{\mathsf T}PE,\qquad |\det H|=|\det E|^2=\Delta(p). \tag{4}
\]
The transpose in this identity is intentional; this is a bilinear trace form, not the positive Hermitian Gram form used in (2).

For \(N\ge d\), define the generally nonsymmetric integral matrix
\[
C_N=HW_N.
\]
Since \(W_N\) is positive definite, \(C_N\) is similar to the real symmetric matrix \(W_N^{1/2}HW_N^{1/2}\).
In particular its spectrum is real, and its numbers of positive and negative eigenvalues agree with the inertia of \(H\).
Moreover,
\[
\operatorname{tr}C_N
=\sum_{j=0}^{N-1}v_j^{\mathsf T}Hv_j
=\sum_{j=0}^{N-1}\operatorname{Tr}(\alpha^j\alpha^{-j})=Nd,
\qquad
|\det C_N|=\Delta(p)G_N. \tag{5}
\]
Thus the question is whether this particular orbit-dependent matrix has geometric mean of eigenvalue magnitudes greater than the arithmetic mean of its signed eigenvalues.

The form \(H\) is positive definite exactly when all conjugates lie on the unit circle.
For that direction, evaluation gives
\(B(x,x)=\sum_i|x(\alpha_i)|^2\) for a real coefficient vector, which is positive unless the vector is zero.
Conversely, if a root lies off the unit circle, assign values 1 and -1 on a real inverse pair, or values 1 on a nonreal conjugate pair and -1 on its inverse conjugate pair.
Assign zero on the other roots.
These values respect complex conjugation, so interpolation at the distinct roots produces a real coefficient vector.
Its value under \(B\) is respectively -2 or -4.
The vector representing 1 has value \(d>0\), so \(H\) is indefinite.
This also handles reciprocal roots of negative real sign.
In the Salem case, exactly one positive real inverse pair is off the circle, so the inertia is \((d-1,1)\).

For a core polynomial, Kronecker's already retained characterization excludes the all-unit-circle case.
Consequently the core corresponds here to an indefinite trace form.
But **integrality, real spectrum, the correct trace, and indefiniteness do not suffice** for (1): for \(d=2\) and every integer \(N\ge3\),
\[
B_N=\operatorname{diag}(-1,2N+1)
\]
is an integral symmetric indefinite matrix with trace \(2N\) and
\[
|\det B_N|=2N+1<N^2.
\]
This is a counterexample only to the relaxed matrix inference.
It is not asserted to equal \(H W_N\) for an integral companion flow.
In particular it does not refute (1).

Some genuine extra structure is visible.
If \(A\) denotes multiplication by \(\alpha\), then
\[
A^{\mathsf T}HA=H,
\qquad
C_N=\sum_{j=0}^{N-1}(A^{\mathsf T})^{-j}
 (Hv_0v_0^{\mathsf T})(A^{\mathsf T})^j. \tag{6}
\]
Each summand is rank one and has trace \(d\).
Any successful matrix approach must use an orbit or cyclic relation such as (6), beyond the invariants in (5).
No determinant bound from (6) is proved here.

## 3. Failure without integrality, and a core family where the certificate works

For the real monic reciprocal polynomial
\[
q_a(t)=t^2-at+1,\qquad a>2,
\]
directly taking the Gram matrix of the coefficient vectors of \(q_a,tq_a\) gives
\[
\Delta(q_a)=a^2-4,\qquad
G_4(q_a)=(a^2+2)^2-4a^2=a^4+4.
\tag{7}
\]
These are identities over the reals; they do not depend on integrality.
Both roots are positive reciprocals and the Mahler measure exceeds 1.
Nevertheless \(\Delta G_4\to0\) as \(a\downarrow2\).
A completely exact witness is \(a=21/10\):
\[
\Delta G_4
=\frac{41}{100}\frac{234481}{10000}
=\frac{9613721}{1000000}<16=4^2.
\]
The roots are distinct, so no zero-discriminant limit is being substituted for an admissible witness.
For every integer \(r\ge1\), the dilation \(q_a(t^r)\) is also squarefree, monic, reciprocal and of degree \(2r\); the established dilation identity, valid here over real coefficients as well, gives
\[
R_{4r}(q_a(t^r))=R_4(q_a)^r<1.
\tag{8}
\]
These examples are outside the integral core.
Clearing denominators changes the primitive polynomial and its Mahler normalization: \(10t^2-21t+10\) has a leading-coefficient contribution.
Thus they are not small-entropy counterexamples for rational flows either.

In contrast, consider the integral family
\[
p_k(t)=t^{2r}-4t^r+1,\qquad r=2^k,\quad k\ge0.
\tag{9}
\]
After replacing \(t\) by \(t+1\), reduction modulo 2 is \(t^{2r}\), while the constant coefficient is \(-2\).
Eisenstein at 2 therefore proves irreducibility for every \(k\).
These are monic reciprocal units, with no unit-circle roots and hence noncyclotomic.
Their degree is \(d=2r\), and the Mahler measure is always \(2+\sqrt3\).
Equation (7) gives for the seed \(q_4\)
\[
\Delta=12,\quad G_4=260,\quad R_4=195.
\]
Consequently
\[
R_{2d}(p_k)=195^r,\qquad
B_{2d}(p_k)=\frac{r\log195}{2(4r-1)}
\longrightarrow\frac{\log195}{8}>0. \tag{10}
\]
This is an unbounded-degree family in the actual core with an exponential surplus and a stable finite certificate.
Its measure \(M(p_k)=2+\sqrt3>2\) is already in an easy large-measure range, and \(m(p_k)=\log(2+\sqrt3)\) is constant; it does not address the remaining small-entropy core.
Its house tends to 1, so it checks that the certificate is measuring Mahler entropy, not confusing it with house.
The family is a concrete application of the already proved dilation mechanism, not a new general entropy theorem.

## 4.
The totally real core is a closed restricted subfamily

For any monic polynomial \(p\), every monic multiplier \(q\) has \(M(q)\ge1\), and Jensen's inequality gives
\[
\|pq\|_2\ge M(pq)=M(p)M(q)\ge M(p).
\]
Apply this to each monic multiplier in the Gram--Schmidt residuals of \(p,tp,\ldots,t^{d-1}p\).
It follows directly, without a limiting Szegő argument, that
\[
G_{2d}=D_d\ge M(p)^{2d}. \tag{11}
\]
This direction is a lower estimate for the determinant; a residual itself remains an upper estimate for the entropy as already recorded in L_G0004.

Suppose now that the core polynomial is totally real.
The retained Schinzel statement gives \(M(p)\ge\phi^{d/2}\), where \(\phi=(1+\sqrt5)/2\).
Since \(\Delta\ge1\), equation (11) gives \(\Delta G_{2d}\ge\phi^{d^2}\).
For every even \(d\ge6\), \(\phi^d>2d\): it holds at \(d=6\), since \(\phi^6=8\phi+5>12\), and the ratio grows upon increasing \(d\) by 2.
Thus (1) holds in these degrees.

The two small cases require no new external input.
For \(d=2\), write \(p=t^2-at+1\).
Integrality and noncyclotomic total reality imply \(|a|\ge3\), and (7) gives \(\Delta G_4\ge5\cdot85=425>16\).

For \(d=4\), write
\[
p(t)=t^4+at^3+bt^2+at+1=t^2Q(t+t^{-1}),
\quad Q(y)=y^2+ay+b-2.
\]
Irreducibility of \(p\) forces irreducibility of \(Q\).
Its roots are real, so its discriminant is a positive nonsquare integer, congruent to 0 or 1 modulo 4, and is therefore at least 5.
Pairing roots through \(t^2-u_it+1\) gives the exact identity
\[
\Delta(p)=|Q(2)Q(-2)|\operatorname{disc}(Q)^2\ge25. \tag{12}
\]
Indeed each within-pair squared difference is \(u_i^2-4\), and the resultant of two different quadratic factors is \((u_i-u_j)^2\).
The factors \(Q(\pm2)\) are nonzero integers because \(p\) has no root \(\pm1\).
Now (11) and Schinzel give
\(\Delta G_8\ge25\phi^{16}>8^4\); for an entirely rational comparison, use \(\phi>3/2\) and \(25(3/2)^{16}>4096\).

The Schinzel theorem is reused only at its already audited statement level; its original proof is not newly inspected.
This closes a known strong-gap subfamily, not the Salem or general reciprocal case.
In particular the totally real argument is not evidence that arbitrary inverse-trace indefiniteness supplies a gap.

<a id="salem-necessary-bound"></a>
## 5. What positivity would force in the Salem case

Let \(p\) be a Salem polynomial, of even degree \(d\ge4\), with two real reciprocal roots \(\tau,\tau^{-1}\), \(\tau>1\), and its other \(d-2\) roots on the unit circle.
Put \(\ell=\log\tau=m(p)\).
Retaining the geometric sums in the Hadamard proof of (2), instead of bounding each individually by its largest term, gives for every \(N\ge d\)
\[
R_N(p)
\le\frac{1}{N^2}
 \left(\sum_{j=0}^{N-1}e^{2j\ell}\right)
 \left(\sum_{j=0}^{N-1}e^{-2j\ell}\right)
=\left(\frac{\sinh(N\ell)}{N\sinh\ell}\right)^2.
\tag{13}
\]
The unit-circle rows contribute exactly \(N^{d-2}\) before division by \(N^d\); no assumption of their mutual orthogonality is made.

Using only (13) and the minimum integer surplus would give the very weak necessary condition that its right side is at least \(1+N^{-d}\).
The inertia from Section 2 gives a substantially stronger condition.
Put
\[
\mathcal K_N=V_N^{\mathsf T}HV_N,
\qquad a_j=e^{j\ell},\quad b_j=e^{-j\ell},\quad0\le j<N.
\]
The nonzero eigenvalues of \(\mathcal K_N\) and \(C_N\) agree, by the elementary equality of nonzero spectra of \(AB\) and \(BA\).
Its inertia is \((d-1,1,N-d)\).
Evaluation at the roots decomposes it as
\[
\mathcal K_N=ab^{\mathsf T}+ba^{\mathsf T}+U_N,
\qquad U_N\ge0. \tag{14}
\]
Here the unit-circle part is the sum of the Hermitian matrices \(w_\zeta w_\zeta^*\), with \((w_\zeta)_j=\zeta^j\); the full sum is real.
The first two terms have nonzero eigenvalues
\[
N\pm T_N,\qquad
T_N=\|a\|\|b\|=\frac{\sinh(N\ell)}{\sinh\ell}.
\]
Indeed \(a^{\mathsf T}b=N\), and a rank-two calculation gives these two eigenvalues.
If \(-\nu\) is the unique negative eigenvalue of \(\mathcal K_N\), the positive semidefinite addition in (14) gives
\[
0<\nu\le T_N-N. \tag{15}
\]
Its other \(d-1\) nonzero eigenvalues are positive and have sum \(Nd+\nu\).
Apply arithmetic--geometric mean to those eigenvalues, and use (5), to obtain, with \(x=\nu/N\),
\[
R_N(p)
\le x\left(\frac{d+x}{d-1}\right)^{d-1}
\le x e^{1+x}. \tag{16}
\]
If \(x\le1/4\), the last expression is at most \(e^{5/4}/4<1\).
Therefore \(R_N(p)>1\) requires \(\nu>N/4\), and hence \(T_N/N>5/4\).
But if \(N\ell\le1\), then
\[
\frac{T_N}{N}
=\frac{\sinh(N\ell)}{N\sinh\ell}
\le\frac{\sinh(N\ell)}{N\ell}
\le\sinh1<\frac54,
\]
a contradiction.
We have proved the conditional implication
\[
R_N(p)>1\quad\Longrightarrow\quad m(p)=\ell>\frac1N;
\qquad
R_{2d}(p)>1\quad\Longrightarrow\quad
\tau>e^{1/(2d)}. \tag{17}
\]
In this derivation integer-valued determinants were not needed: the Salem root configuration, distinctness, and \(N\ge d\) suffice.
The proposed universal positivity statement supplies the arithmetic hypothesis when it is restricted to integral Salem polynomials.

This implication is more informative than extracting the minimum positive integer surplus from (2), but its lower bound still tends to zero with unbounded degree.
It is not a uniform Lehmer gap.
Conversely, a lower bound on \(\ell\) alone does not reverse (13) or (16) or prove (1).
No equivalence between (1) and Lehmer is asserted.
A proof of (1) could contain stronger arithmetic information than these necessary conditions; no degree-independent extraction is established here.
The one-negative-eigenvalue argument is specific to the Salem configuration and is not asserted for general reciprocal polynomials with several off-circle pairs.

## 6. Bounded literature check and continuation boundary

A bounded primary-source check located [Amo97](https://iris.unito.it/retrieve/a4044a17-420a-4465-92d6-e3b72b114e10/Szego.pdf), Francesco Amoroso, *A Remark on a Theorem of Szegő*, The Ramanujan Journal 1(4) (1997), 357--362.
Theorem 1.1 on printed p.359 / PDF p.3 assumes \(FF^*\) squarefree, with \(F^*(z)=z^{\deg F}\overline{F}(1/z)\), and bounds a product of finite prediction errors using \(|\operatorname{disc}(FF^*)|\).
For a real reciprocal core polynomial \(p\), \(p^*=p\), so \(pp^*=p^2\) is not squarefree.
Therefore that displayed theorem cannot be imported directly into the present core.
The paper's introductory report also confirms that finite prediction-error approximation was already studied by Dégot, cited here only through Amo97.
Only these scope/attribution interfaces were checked; no theorem from this source is a premise and no full source audit is claimed.
The2026-10-06 local download failed with HTTP403; there is no retained local PDF.
This acquisition bookkeeping was completed after the mathematical draft was frozen and does not expand its research scope.

The next bounded structural target is to retain the orbit identity (6), or a genuinely integral cyclic-minor constraint, while deriving a useful determinant estimate.
Replacing that structure by trace and inertia has been ruled out as sufficient.
Repeating dilation of a fixed polynomial cannot produce a small-entropy family.
Real-coefficient root clustering is a useful obstruction to analytic relaxations, but it must not be reported as an integral counterexample.
The full-core positivity question and, more strongly, a degree-uniform exponential-surplus estimate remain unresolved here.

The [original author algebra check](../audits/reviews/Yin_R_G0506_v1.md#original-author-algebra-check) retains its original scope and date.
No executable experiment supports a conclusion in this draft, so no new computation artifact or numerical precision claim is present.

The [original combined structural finding](../audits/reviews/Yin_R_G0506_v1.md#original-contributor-structural-finding) retains its complete inverse-trace/family/totally-real inspection and the actual negative-eigenvalue contribution and subsequent bound check.
That reviewer contributed to this complete argument, so its current relationship is self-reviewed; the original independent wording, exact date and no-source/no-rerun boundaries remain readable in R506.
The [current complete C214 finding](../audits/reviews/Yin_R_G0506_v1.md#current-structural-finding) is a separate actual self-review of the registered full statement and argument.
