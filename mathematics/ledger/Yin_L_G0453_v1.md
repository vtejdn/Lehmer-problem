---
author: Yin
---

# Same-input tensor traces, radial contraction and complete doubling tails

Date: 2026-11-05.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The responsible delegate developed and checked this bounded comparison after the coordinating agent selected the joint ghost/resultant question.
This is author work and ordinary checking, not independent review, a new Claim assessment or a uniform Mahler-gap theorem.

<a id="tensor-ghost-doubling-scope"></a>
## Question, reuse and responsible scope

Can the same original polynomial's complete integer ghost congruences, positive and negative frequency moment constraints, and doubling resultant force a new paid restriction on its mixed logarithmic correlation?
The complete ghost equivalence itself is already retained in [L10 v3](Yin_L_G0010_v3.md#all-prime-ghost-equivalence) and is not reproved here.
The new comparison separates the raw product spectrum, where integer traces live, from its exact radial contraction, where the boundary Fourier coefficients live.

The complete all-pair integrality, non-torsion, original resultant and multiplicity accounting are already supplied by [C477](../claims/Yin_C_G0477_v1.md#full-ratio-orbits).
Its [same-resultant identity](../claims/Yin_C_G0477_v1.md#symmetrized-mixed-resultant-identity) retains the degree-d original norm and degree-2d original auxiliary at the doubling prime, while charging every one of the d-squared pair labels.
Those existing conclusions are reused, not recreated as a new arithmetic theorem.
[C1](../claims/Yin_C_G0001_v1.md#doubling-exact-radial-angular-split) owns the exact radial/angular split and its compulsory linear angular income.
[C4](../claims/Yin_C_G0004_v1.md#growing-band-resultant-localization) already gives an actual finite-band estimate and a complete Abel-tail requirement with the original radial damping retained.
[C215](../claims/Yin_C_G0215_v1.md#argument) supplies the actual reciprocal moment, inertia and integer-minor constraints, rather than constraints on freely chosen matrices.

The nearby [L174](Yin_L_G0174_v1.md#salem-arithmetic-fixed-scope) concerns the exact positive-Salem dyadic identity, its primitive plastic-family energy and doubling-auxiliary construction.
Its complete current positive-Salem identity is [C408](../claims/Yin_C_G0408_v1.md#salem-exact-damped-mixed-identity), and the fixed-positive-measure plastic-family calculation is [C409](../claims/Yin_C_G0409_v1.md#complete-plastic-mixed-energy-limit).
Those specialized results are not superseded by the present all-reciprocal comparison.
[L397](Yin_L_G0397_v1.md#statement) is the fixed full-Frobenius symmetrization inquiry now retained in C477.
Neither its Galois-class accounting nor L174's specialized family calculations already contain the raw-versus-contracted ghost comparison and the two controls below.
The present record therefore owns this distinct bounded compatibility test while linking those adequate existing arguments.

The outcome is an exact same-input tensor representation, an explicit contraction expense, a cyclotomic control with a completely computed linear boundary tail, and a nontorsion power-stable quartic with negative first mixed trace.
The cyclotomic control is outside the nontorsion endpoint domain, and the quartic has fixed positive total measure.
Neither is a near-zero sequence or a counterexample to the unrestricted Task.

<a id="same-input-tensor-and-mahler-cost"></a>
## The tensor polynomial has the old arithmetic and the exact radial measure

Let P be the monic irreducible reciprocal polynomial of a nontorsion algebraic unit, of original degree d.
Its constant coefficient is one, d is even, and its full root multiset is closed under inversion and conjugation.
Write
\[
 \alpha_i=e^{\ell_i+i\theta_i},\qquad
 m=m(P)>0,\qquad s_n=\sum_i\alpha_i^n=s_{-n},
\]
so that \(\sum_i\ell_i=0\), \(\sum_i|\ell_i|=2m\), and \(|\ell_i|\le m\).
The intended endpoint additionally preserves degree under every positive integer power.
The identities in this section do not require that extra property and retain all original pair multiplicities.

For the integer companion matrix A of P, put
\[
 D_P(t)=\det(I-t(A\otimes A^2))
       =\prod_{i,j}(1-t\alpha_i\alpha_j^2).
\tag{1}
\]
The equality follows by diagonalizing the separable companion matrix over a splitting field and taking the tensor eigenbasis.
Reciprocity lets us reindex the second root list by inversion, so the same product is
\[
 D_P(t)=\prod_{i,j}(1-t\beta_{ij}),
 \qquad \beta_{ij}=\alpha_i/\alpha_j^2.
\tag{2}
\]
C477's complete pair-orbit result supplies integrality and nontorsion of this full ratio multiset, with every repeated ratio retained.
Indeed, the ratios in (2) are the inverses of C477's doubling ratios after interchanging the two ordered labels; inversion preserves the integral-unit and nontorsion conclusions.
Equivalently, the determinant in (1) displays its integer coefficients directly.
The polynomial has degree \(d^2\), constant coefficient one and leading coefficient one, since the original root product is one and d is even.
It is reciprocal, because the full \(\beta_{ij}\) multiset is closed under inversion.

The full-root resultant convention gives
\[
 |D_P(1)|=|\operatorname{Res}(P,P^{[2]})|
 \ge2^d.
\tag{3}
\]
This is the existing Frobenius floor, not an extra factor supplied by tensorization.
No pair degree is substituted for the original field degree.
In particular, the degree-\(d^2\) tensor polynomial does not mean that the original auxiliary \(P(X^2)\), of degree \(2d\), has changed degree.

Put \(a_{ij}=\ell_i-2\ell_j=\log|\beta_{ij}|\).
The product formula for Mahler measure and the zero sum of these logarithms give
\[
 m(D_P)=\sum_{i,j}\max(0,a_{ij})
       =\frac12\sum_{i,j}|a_{ij}|
       =B_{\rm rad}\le3dm.
\tag{4}
\]
Every original pair is included in both sides.
Thus C1's exact angular energy can also be written
\[
 K=\log|D_P(1)|-m(D_P).
\tag{5}
\]
In particular \(K\ge d\log2-3dm\), exactly C1's existing lower bound.
The tensor packaging identifies an evaluation-minus-measure quantity on one genuine integral polynomial; it supplies no new upper estimate for that quantity.

Its raw power sums are exactly
\[
 u_n=\operatorname{tr}((A\otimes A^2)^n)
     =s_ns_{2n}=\sum_{i,j}\beta_{ij}^n.
\tag{6}
\]
They satisfy complete integer ghost congruences because they are traces of this actual integer matrix.
This joint arithmetic is automatic from the original matrix and supplies no sign assertion for \(u_n\).
Since \(|\beta_{ij}|\le e^{3m}\), one has the absolutely convergent identity
\[
 \log|D_P(r)|=-\sum_{n\ge1}\frac{r^n u_n}{n}
       \qquad(0\le r<e^{-3m}).
\tag{7}
\]
The stated radius is a sufficient one; it is not asserted optimal for each input.
Equation (7) supplies no unrestricted substitution \(r=1\).

<a id="contracted-trace-error-and-finite-tail"></a>
## The contracted spectrum and its explicit comparison price

Define
\[
 z_{ij}=e^{-|a_{ij}|+i(\theta_i-2\theta_j)},\qquad
 C_n=\sum_{i,j}z_{ij}^n.
\tag{8}
\]
Conjugation symmetry makes \(C_n\) real, so this is precisely C1's cosine coefficient with the original pair-dependent damping.
If \(|\beta_{ij}|\le1\), then \(z_{ij}=\beta_{ij}\).
If \(|\beta_{ij}|>1\), then \(z_{ij}=1/\overline{\beta_{ij}}\).
These contracted coefficients are not asserted integral and are not the raw ghost sequence in (6).

For each \(0<r<1\),
\[
 K_r=\sum_{i,j}\log|1-rz_{ij}|
    =-\sum_{n\ge1}\frac{r^n C_n}{n}.
\tag{9}
\]
The series is absolutely convergent because \(|C_n|\le d^2\).
The per-input limit \(K=\lim_{r\uparrow1}K_r\) exists: there are finitely many factors, and a factor can equal zero at the endpoint only if \(\beta_{ij}=1\), excluded by the original nonzero mixed resultant.
This justifies the complete Abel limit without claiming absolute convergence of the boundary series or a uniform family limit.

For \(a>0\), the elementary inequality
\[
 e^{na}-e^{-na}=2\sinh(na)\le2na e^{na}
\]
and \(a_{ij}\le3m\) give
\[
 |u_n-C_n|
 \le\sum_{a_{ij}>0}2n a_{ij}e^{n a_{ij}}
 \le2n e^{3nm}B_{\rm rad}.
\tag{10}
\]
The middle positive logarithm sum is exactly (4).
Thus for \(q=re^{3m}<1\),
\[
 |K_r-\log|D_P(r)||\le
 2B_{\rm rad}\sum_{n\ge1}q^n
 =\frac{2B_{\rm rad}q}{1-q}
 \le\frac{6dmq}{1-q}.
\tag{11}
\]
This couples the arithmetic and contracted quantities on one input while paying the actual radial comparison.
It loses uniformity as q approaches one.

There is also a finite statement valid for every \(0<r<1\) and integer \(N\ge1\), without requiring \(re^{3m}<1\):
\[
 \left|K_r+\sum_{n=1}^N\frac{r^n u_n}{n}\right|
 \le 2B_{\rm rad}\sum_{n=1}^N(re^{3m})^n
      +\frac{d^2r^{N+1}}{(N+1)(1-r)}.
\tag{12}
\]
The first term is (10) summed over the finite band.
For the remaining contracted series, use \(|C_n|\le d^2\) and \(1/n\le1/(N+1)\).
This is an explicit paid bound, not a useful degree-uniform boundary estimate.

C4's existing growing-band result compares the actual \(C_n\) with angular products and retains a different expense,
\(4N(N+1)L^2+6Ndm\), where \(L=\log\|P\|_{\mathbb T}\).
Its complete tail lower bound already forces the omitted band to carry linear income in its stated coefficient-growth class.
Neither (11) nor (12) removes that remaining band or improves its original-input coverage.
One must not transfer the raw integer congruences to \(C_n\), or replace (9) by (7) outside its proved convergence domain.

<a id="cyclotomic-full-ghost-and-linear-tail-control"></a>
## A cyclotomic control with complete arithmetic, positivity and exact tail

Let p be any odd prime, set \(d=p-1\), and take
\[
 P(X)=\Phi_{2p}(X)=\frac{X^p+1}{X+1}.
\tag{13}
\]
Its roots are \(\alpha_j=-\zeta_p^j\), \(1\le j\le p-1\).
This is an integral reciprocal polynomial, so all its integer ghost congruences and its initialized finite polynomial recurrence hold.
Every Toeplitz matrix from arbitrary integer frequency indices is positive semidefinite:
for any finite coefficients \(v_a\), its quadratic form is
\[
 \sum_{j=1}^{p-1}\left|\sum_a v_a\alpha_j^a\right|^2\ge0.
\tag{14}
\]
This explicitly includes positive and negative frequencies.

The product spectrum in (1) consists of \(-\zeta_p^{\,i+2j}\) for nonzero i and j modulo p.
For residue zero there are \(p-1\) ordered pairs, since \(i=-2j\) remains nonzero.
For any nonzero residue there are \(p-2\) pairs, because the unique forbidden choice \(j=i_{\rm target}/2\) would force the other index to zero.
Consequently
\[
 D_P(t)=(1+t)^{p-1}
          \prod_{k=1}^{p-1}(1+t\zeta_p^k)^{p-2}
       =(1+t)(1+t^p)^{p-2}.
\tag{15}
\]
The degrees sum to \(1+p(p-2)=(p-1)^2=d^2\).
There are no coincident-root omissions.

Here \(m=0\), \(B_{\rm rad}=0\), and the raw and contracted spectra agree.
Formula (15) therefore gives, including its finite endpoint,
\[
 K_r=\log(1+r)+(p-2)\log(1+r^p),\qquad
 K_1=(p-1)\log2=d\log2.
\tag{16}
\]
In particular the full mixed resultant is nonzero and saturates the \(2^d\) floor.
For each fixed \(0<r<1\), \(K_r\to\log(1+r)\) as p tends to infinity, while the boundary value is linear in d.
If \(r=e^{-c/p}\), for a fixed \(c>0\), then
\[
 K_r/d\longrightarrow\log(1+e^{-c})>0.
\tag{17}
\]
This identifies a concrete smoothing scale on this control rather than interchanging the two limits.

The complete Fourier tail can be read without an asymptotic estimate.
The geometric sum of the p-th roots gives
\[
 s_n=(-1)^n
 \begin{cases}p-1,&p\mid n,\\-1,&p\nmid n.\end{cases}
\tag{18}
\]
Since p is odd, \(s_{2n}\) has the same bracket without the sign, so for every \(N<p\),
\[
 -\sum_{n=1}^N\frac{s_ns_{2n}}n
    =\sum_{n=1}^N\frac{(-1)^{n+1}}n,
 \qquad 0<\sum_{n=1}^N\frac{(-1)^{n+1}}n\le1.
\tag{19}
\]
Subtracting this finite sum from the per-input Abel limit in (16) gives the exact tail
\[
 \mathcal T_N=-\lim_{r\uparrow1}\sum_{n>N}\frac{r^n s_ns_{2n}}n
             =d\log2-\sum_{n=1}^N\frac{(-1)^{n+1}}n
             \ge d\log2-1.
\tag{20}
\]
One may take \(N=d=p-1\).
Thus even a degree-linear initial band misses nearly all the boundary floor on this control.

This is a boundary test of the proposed sufficient information, not an input to the nontorsion endpoint theorem.
All roots of (13) are torsion.
Their p-th powers equal -1, so the original degree drops to one; all-positive-power degree preservation fails.
The same example does preserve degree under powers of two, since its squared roots have exact order p, but that weaker property does not repair the missing endpoint hypothesis.
Full ghost congruences and full positive moment matrices alone therefore permit the exact linear doubling energy; excluding this control requires genuine nontorsion or endpoint information beyond those two predicates.
No perturbation of (13) with small positive integral total measure is constructed.

<a id="negative-quartic-original-endpoint-control"></a>
## A genuine power-stable reciprocal unit with a negative mixed trace

For a separate control inside the actual nontorsion endpoint domain, take
\[
 P_-(X)=X^4+X^3-X^2+X+1.
\tag{21}
\]
The positive-sign Salem seed \(P_+(X)=X^4-X^3-X^2-X+1\) and its squared polynomial already appear in [L445](Yin_L_G0445_v1.md#first-binary-layer).
Here \(P_-=P_+(-X)\).
The following direct checks establish the negative control's exact domain and costs; no table or numerical experiment is a premise.

Modulo two, \(P_-\) becomes \(X^4+X^3+X^2+X+1\).
It has no linear factor over \(\mathbb F_2\).
The only monic irreducible quadratic over \(\mathbb F_2\) is \(X^2+X+1\), and division gives remainder \(X+1\).
Thus this quartic reduction is irreducible, proving irreducibility of \(P_-\) over \(\mathbb Q\).
It is monic, reciprocal and has constant coefficient one.

Put \(T=X+X^{-1}\).
Then
\[
 P_-(X)=X^2(T^2+T-3).
\tag{22}
\]
The trace roots \(t_\pm=(-1\pm\sqrt{13})/2\) satisfy
\(-5/2<t_-<-2\) and \(1<t_+<2\).
The first gives a negative real reciprocal pair \(-\lambda,-\lambda^{-1}\), with
\[
 \lambda>1,\qquad
 \lambda+\lambda^{-1}=(1+\sqrt{13})/2,
\tag{23}
\]
and the second gives two distinct unit-circle roots.
There is exactly one root outside the unit circle, and
\[
 m(P_-)=\log\lambda>0.
\tag{24}
\]
This positive total measure is fixed throughout the example.

Every positive power preserves the original degree four.
Indeed, a degree drop would give distinct conjugates with root-of-unity quotient.
By irreducibility, a splitting-field automorphism can carry the first conjugate to the unique outside root.
It would then carry the other to a distinct root of the same outside modulus, a contradiction.
This is the same elementary unique-outside-root argument used in the inspected [C857 construction](../claims/Yin_C_G0857_v1.md#large-period-full-mask), with its domain verified directly here.

Newton initialization gives
\[
 s_1=-1,\qquad s_2=3,\qquad s_1s_2=-3.
\tag{25}
\]
Thus complete integer ghost conditions, the original recurrence, reciprocity, all-power degree preservation and C215's actual moment identities do not imply a universal nonnegative sign for the individual products \(s_ns_{2n}\).
This says nothing about a rule additionally requiring sufficiently small total measure.

The squared full-root polynomial and its normalized Frobenius remainder are exact:
\[
 P_-^{[2]}(X)=X^4-3X^3+X^2-3X+1,
 \qquad
 H(X)=\frac{P_-^{[2]}(X)-P_-(X)}2
      =-2X^3+X^2-2X.
\tag{26}
\]
For a direct verification, \(t^2+t-3=0\) gives the squared trace \(u=t^2-2=1-t\); its two values have sum three and product minus one, yielding (26).
At an original root \(\alpha\), \(H(\alpha)=\alpha^2(1-2t)\).
The trace field is \(F=\mathbb Q(\sqrt{13})\), and the original field has degree two over F by (22) and quartic irreducibility.
Consequently
\[
 \operatorname{Norm}_{F/\mathbb Q}(1-2t)
 =1-2(t_++t_-)+4t_+t_-=-9,
\]
\[
 |\operatorname{Res}(P_-,H)|=81,\qquad
 |\operatorname{Res}(P_-,P_-^{[2]})|
       =2^4\cdot81=6^4.
\tag{27}
\]
The unit factor \(\operatorname{Norm}(\alpha^2)\) is one.

The radial list is \(m,-m,0,0\), irrespective of the signs of the two real roots, so C1's count gives \(B_{\rm rad}=10m\).
The full angular energy is therefore
\[
 K=4\log6-10\log\lambda>0.
\tag{28}
\]
For the strict sign, (23) gives \(1<\lambda<2\), since \((1+\sqrt{13})/2<5/2=2+1/2\).
Hence the right side of (28) is greater than
\(4\log6-10\log2=\log(81/64)>0\).
This retains the entire resultant and radial cost rather than extrapolating the negative first product to the whole sum.
No growing family, arbitrarily small measure, universal tail sign or improved lower gap is inferred.

<a id="tensor-contraction-return-boundary"></a>
## First unsupported bridge and author-check limits

The tensor polynomial places all raw mixed traces on one genuine integer object, with original multiplicities intact, but its integer ghost congruences are automatic.
The actual boundary coefficients require radial contraction, and (10)--(12) are the explicit price of comparing that object with its raw arithmetic.
The cyclotomic control satisfies full ghost arithmetic and every signed-index positive moment constraint while placing linear income beyond a degree-linear initial band.
Its torsion and power-drop defects are essential, so it is not a counterexample inside the selected endpoint domain.
The negative quartic is an actual reciprocal nontorsion endpoint and excludes a universal termwise nonnegative mixed-trace rule, but only at its fixed positive total measure.

The remaining unsupported step is an estimate on the complete contracted boundary tail for actual small-total-measure nontorsion inputs, using original arithmetic and endpoint information with the d-squared pair population, radial comparison and full remainder paid.
C477's original-field normalization, C4's complete tail requirement and C215's moment constraints remain in force.
No conditional independence, probabilistic rarity, separate congruence feasibility or finite truncation replaces that joint estimate.
This bounded comparison supplies no additional uniform income and no proof or counterexample for the unrestricted Lehmer objective.

The reuse search inspected C1, C4, C215, C231, C477 and its L397 input, the relevant S5 Fourier allocation, L10 v3, L174 and its current C408/C409 proof homes, L445 and C857's unique-outside-root argument.
It compared the exact damping, degree and measure scopes before retaining the new tensor/contraction calculation and explicit controls.
All new calculations use finite linear algebra, finite root sums, elementary series on their stated convergence domains and the retained Mahler/resultant conventions.
No new external theorem, external-source acquisition, native mathematical program or numerical experiment is used.
The delegate directly checked tensor eigenvalues, reciprocal reindexing, measure and trace normalization, the contraction bound, complete finite and Abel tails, cyclotomic multiplicities, quartic irreducibility, all-power degree preservation, norm factors and every stated domain exclusion.
These checks have their actual author-development relationship and are not a formal or independent review.
