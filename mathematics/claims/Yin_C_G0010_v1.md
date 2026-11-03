---
author: Yin
---

# Rational complementary Laurent lifts with original values and complete costs

Date: 2026-10-11T17:29.
Human author: Yin.
Provenance: mixed project deductions and the explicitly accepted external inputs below.
Internal reusable-result organization under [G0001](../tasks/Yin_T_G0001_v1.md#decision-weekly-resume-2026-10-11); no manuscript main-theorem designation or objective change.

## Statement

Fix an actual monic irreducible self-reciprocal nontorsion integer-unit polynomial P of degree d>=2, K=Q(alpha), sigma(alpha)=alpha^-1, and a full sigma-stable order O containing alpha and alpha^-1.
Given nonzero actual O-unit targets a_j and positive rational normalized weights lambda_j with sum lambda_j a_j sigma(a_j)=E in Q, 0<E<1, then for every eta>0 there is a finite rational Laurent bundle V_b and strictly positive normalized rational weights omega_b with exact constant covariance E', E<E'<min(1,E+eta).
Every original coordinate retains its exact target a_j before common monomial normalization; added coordinates have value+1 or-1, and original weight ratios remain unchanged.

For TOTALLY REAL F=Q(alpha+alpha^-1), the same structural conclusion holds for arbitrary nonzero targets a_j in K, without integrality or inverse assumptions.
This registration keeps that extension at the old L392 formal domain; the nonreal/nonunit combination requires its separate new interface review.

For integer targets, after one actual common monomial and coefficient denominator q, the original full resultants are q^d Norm_K(a_j), added full resultants are+q^d, exact covariance is q^2 E', and I=log q+(1/d)sum_original omega_j log|Norm_K(a_j)|.
All actual contents and final weight multiplicities are retained.
For unit targets I=log q and q^2 E'>=1.
For every exact constant-covariance bundle with nonzero resultants and common union width T, I<=(1/2)log(q^2 E')+(T/d)m(P); hence the surplus is paid by the original window.
This inequality is proved directly below, with no small-height restriction.

For the fixed genuine-Salem packet whose distinguished trace-unit target is epsilon_0^N, r=|rho_0(epsilon_0)|>1 and weight w_0, arbitrary admissible independent monomial twists retain |f_0(beta)f_0(beta^-1)|=r^(2N).
Exact covariance E_c gives Tm(P)>=2Nlog r+log(w_0/E_c).
Without constant covariance, full rational coefficient energy A>=w_0 r^(2N)/(beta^T sum_(k=0)^T beta^(-2k)).
In the lift use the FINAL weight lambda_0/Z_r and FINAL energy E', not the preliminary ones.
No uniform dimension/height/denominator or gap is concluded.

## Current assessment
[Selected decision](#decision-initial)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-11T17:29 |
| status | open |
| reason | Register the exact reusable statement and its actual complete fixed argument. Historical whole reviews retain their original L scopes; adoption of this extraction and its selected dependency interfaces awaits a separate current finding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only the explicitly registered conclusions and domains above. |
| argument | [Argument](#argument) | Actual reasoning retained below, with the stated assembly and exclusions. |
| dependency | [Unit field profiles](Yin_C_G0009_v1.md#statement) | Only the genuine-Salem existence corollary and fixed cone packet application; the general conditional lift does not require profile existence. |
| dependency | [Classical Gram attribution](../audits/literature/GL06/Yin_U001.md#gl06-u001) | Known normalized Gram construction attributed at its checked source scope; explicit rational positivity and LDL are proved in the retained argument. |


## Argument

The complete L390 construction below proves the general reciprocal unit-target implication.
The separately retained L392 Section4 supplies exactly its nonzero-target extension on the totally real trace domain stated above.
The complete L389 account supplies the fixed-packet cost inequalities, using the same original roots and common union width.
The genuine-Salem profile availability used in L390's corollary is supplied by the profile Claim linked in the decision; its old L references in the retained history record ancestry, not a proof left outside C.

### Direct exact-covariance window inequality

For finite polynomials F_b of degree at most T, positive normalized weights omega_b and constant sum_b omega_b |F_b(z)|^2=S on |z|=1, each squared modulus is subharmonic on the disk.
The maximum principle applied to their sum gives sum_b omega_b |F_b(z)|^2<=S for |z|<=1.
Apply the same argument to t^T F_b(t^-1); real rational coefficients ensure unchanged circle covariance.
Therefore at every complex z, sum_b omega_b |F_b(z)|^2<=S max(1,|z|)^(2T).
For each original root alpha_i, concavity gives sum_b omega_b log|F_b(alpha_i)|<=(1/2)log S+Tlog max(1,|alpha_i|).
Sum over ALL d roots and divide by d.
Monicity and nonzero full resultants give I<=(1/2)log S+(T/d)m(P).
This reconstructs the exact-complementarity branch of L318 locally; L318 is attribution/extraction ancestry for this branch, not an unprovided proof dependency.
The two-root packet bound follows by applying the same estimates separately at beta and beta^-1 and multiplying; the coefficient bound is the full coefficient Cauchy--Schwarz calculation retained in L389.

### Complete L390 author account

## Rational complementary Laurent bundles from exact positive unit profiles

Date: 2026-10-12.
Authored by the paraunitary researcher AI for Yin.
Root supplied the substantive complete core candidate: second-order profile correction, positive damping, rational Toeplitz/Gram sums of squares and paired nonvanishing unit-coordinate repair.
Root is not an independent whole reviewer.
This distinct draft was allocated before development.
No native mathematical program, scan, solver or new J was used; prior fixed mathematics is untouched.

## Assigned question and result

Given an exact rational normalized constant field profile E with 0<E<1 on an original irreducible monic reciprocal nontorsion integer-unit input, construct a finite rational Laurent bundle with exact constant circle covariance at energy arbitrarily close above E, preserving all supplied original unit values and giving every added coordinate a nonzero actual unit value.
The proof below establishes this implication without a Salem or totally-real-trace hypothesis.
In the genuine Salem subclass, combination with L388 characterizes existence of some positive-surplus exact complementary unit bundle by the existence of an actual negative-full-norm unit.
That sign equivalence is NOT asserted outside the genuine Salem subclass.
No uniform degree, coefficient, denominator or Mahler-gap bound follows.

<a id="complementary-unit-lift-reuse-and-domain"></a>
## 1. Fixed inputs, recognized Gram source and exact domain

[L388's actual-order field-profile theorem](../ledger/Yin_L_G0388_v1.md#positive-rational-field-profile-construction) supplies rational positive weights and exact relative-unit profiles when an actual negative-full-norm unit exists.
Its result is only in the trace field.
[L372's sign obstruction](../ledger/Yin_L_G0372_v1.md#mixed-signed-unit-constant-obstruction) supplies the converse obstruction for constant profiles below one if all selected full norms are positive.
[L380](../ledger/Yin_L_G0380_v1.md#structural-factorization-costs-and-next-gate) retains the polynomial-versus-field and residual-projection distinctions.
[L318's finite Poisson/reversal estimate](../ledger/Yin_L_G0318_v1.md#polynomial-poisson-majorant) supplies the original-root degree expense used below.
These are exact fixed inputs, not an adoption of a new uniform gap.

The [same L318 account](../ledger/Yin_L_G0318_v1.md#common-filter-cancellation-obstruction) already has the unprojected complementary pair 1+t^h,1-t^h at equal weights, exact energy 2 and complete income log|Res(P,t^(2h)-1)|/(2d).
Its degree-linear near-one surplus tends to -log(2)/2 by the full cyclic-cost theorem.
Thus generic existence of complementary integer bundles is not new here.
The changed construction preserves ACTUAL unit-valued coordinates, including every added coordinate, so after scalar clearing their full norms are all +/-q^d.
It starts from an actual constant field profile and gives the precise sign/existence criterion and finite construction below.
The earlier binomial obstruction, its complete resultant and its near-one scope remain unchanged.

A bounded local search by positive Laurent polynomial, rational sum of squares, Toeplitz Gram and Fejer--Riesz found related fixed Gram arguments and [L22's rational LDL construction](../ledger/Yin_L_G0022_v1.md#neutral-rational-symmetric-realization), but no already retained version of the new unit-preserving completion.
The standard Gram construction is explicitly present in Jeffrey S. Geronimo and Ming-Jun Lai, [Factorization of Multivariate Positive Laurent Polynomials](https://arxiv.org/pdf/math/0503133), arXiv:math/0503133v1, 7 March 2005, 19 pages.
The author read Section 2's Fourier quadratic-form positivity on p.3, the exact entries p_(k-j)/(m+1-|j-k|) on p.5, and their perturbative positivity argument on pp.6--7.
The journal record is Journal of Approximation Theory 139(1--2)(2006),327--345, DOI 10.1016/j.jat.2005.09.010; the inspected pagination is the preprint's.
Canonical inspected-source navigation is [GL06-U001](../audits/literature/GL06/Yin_U001.md#gl06-u001), with the retained v1 artifact and its exact depth.
No novelty is claimed for that Gram mechanism.
The local univariate bound below is checked directly, and rational LDL replaces a complex square root or spectral factor.
No uninspected multivariate factorization theorem, coefficient-field descent, source numerical algorithm or whole-paper audit is invoked.

The now fixed [L389 packet cost](../ledger/Yin_L_G0389_v1.md#exact-covariance-distinguished-product-width-bound) was also read.
It charges actual width/energy on the same original L388 unit packet and does not supply a covariance construction.
The present repair must still pay its finite bound using the final, changed weights and energy; the comparison is recorded in Section 6.

Fix the ORIGINAL monic irreducible reciprocal nontorsion integer-unit polynomial P in Z[t], alpha=t mod P, K=Q(alpha), F=Q(alpha+alpha^-1) and sigma(alpha)=alpha^-1.
Here reciprocity is P(t)=t^d P(t^-1).
Its constant coefficient is 1, its degree is even d=2s>=2, and Norm_K(alpha)=1.
An odd-degree self-reciprocal irreducible polynomial would have root -1 and be torsion, so that case is excluded by the stated domain.
The reciprocal involution is nonidentity because alpha is nontorsion.
No total reality of F, unique exterior inverse pair or circle-root hypothesis is used in the lifting proof.
Let O be a full sigma-stable order containing alpha and alpha^-1.
The latter unit containment is an explicit normalization guard.
The theorem is not stated for an arbitrary smaller order without it.
Put R=Q[t,t^-1], and a*(t)=a(t^-1).
For the actual P,

    B=P P*=t^-d P^2,
    B(e^(i theta))=|P(e^(i theta))|^2>=0.

Suppose actual O-units u_1,...,u_k and strictly positive rational weights lambda_j are given with

    sum_j lambda_j=1,
    sum_j lambda_j u_j sigma(u_j)=E in Q, 0<E<1.    (1)

Choose rational Laurent representatives f_j with f_j(alpha)=u_j, and put G=sum_j lambda_j f_j f_j*.
All coefficients are real rational, G*=G, G>=0 on the whole circle, and G(alpha)=E.
Equality modulo the whole P preserves every original conjugate.
For existence and the later degree bound, one may choose the ordinary power-basis representatives of degree at most d-1; this choice preserves the original residues, not an unrelated pre-existing circle covariance.

**Theorem 1.** Under precisely this general reciprocal domain and supplied profile (1), for every real eta>0 there is a finite family of rational Laurent polynomials V_b and strictly positive rational weights omega_b summing to one such that their complete circle covariance is a constant E' with E<E'<min(1,E+eta).
Every supplied u_j remains exactly the value at alpha of its corresponding original coordinate; every added coordinate has value +1 or -1.
All original weight ratios are preserved, though their total mass decreases after the additional weights are normalized.
The identity is exact in R and at every original conjugate.
Sections 2--5 prove this statement; Sections 6--7 retain its complete arithmetic and degree costs.

<a id="second-order-original-quotient-correction"></a>
## 2. A second-order correction with unchanged original values

Because P is the actual minimal polynomial and alpha is nonzero, G-E is divisible by P in R.
Define

    x=(G-E)/E, c=1-x/2, g_j=c f_j,
    G_1=sum_j lambda_j g_j g_j*=c^2G.

Both x and c are self-star, and c(alpha)=1.
Direct multiplication gives

    G_1-E=E[(1+x)(1-x/2)^2-1]
          =E x^2(x-3)/4.                           (2)

Thus P^2 divides G_1-E in the Laurent ring.
Since B=t^-d P^2 differs by an invertible Laurent monomial,

    h_0=(G_1-E)/B belongs to R,
    h_0*=h_0, G_1=E+B h_0.                         (3)

This is polynomial divisibility before any evaluation, not division of a zero numerical value.
It covers every original root simultaneously.
The self-star assertion follows from (3) and the domain property of R.
If the error vanishes identically take h_0=0.
Each g_j still has its exact unit value u_j, and G_1 remains an actual positive-weight square sum on the entire circle.
No division by P at a circle root is used.

<a id="strict-positive-damped-remainder"></a>
## 3. Exact damping and strict positivity, including circle roots

Let H_P be the sum of absolute coefficients of the ORIGINAL P, and let K_0 be the sum of absolute Laurent coefficients of h_0.
These are finite, with H_P>=1 and K_0>=0 rational.
On the circle h_0<=K_0, so G_1<=E+K_0 B.
Put

    epsilon=1/(2H_P^2), S=1-epsilon B,
    1/2<=S<=1 on the circle,
    choose integer N>=1 with 2N epsilon E>K_0.       (4)

The range follows from |P|<=H_P.
All coefficients of S are rational, S*=S, and S(alpha)=1.
Set v_j=S^N g_j.
The exact remaining error is

    E-sum_j lambda_j v_j v_j*=B h,
    h=E epsilon sum_(a=0)^(2N-1)S^a-h_0 S^(2N).     (5)

The displayed finite sum proves directly that h is a rational self-star Laurent polynomial; it also defines it at every zero of B.
For B>0 on the circle, the elementary inequality (1-y)^(-2N)>=1+2Ny for 0<=y<=1/2 gives

    h>=S^(2N){ E[(1-epsilon B)^(-2N)-1]/B-K_0 }
      >=(2N epsilon E-K_0)2^(-2N)=:delta>0.          (6)

For example the elementary inequality follows because the derivative of (1-y)^(-2N)-1-2Ny is nonnegative and its value at zero is zero.
The set B>0 is dense on the circle since P is a nonzero polynomial.
Continuity of the Laurent polynomial h extends the same bound to all circle zeros.
Equivalently (5) gives h=2N epsilon E-h_0 when B=0.
Thus there is no exceptional zero, multiplicity or sign gap in (6).
Every v_j(alpha)=u_j, exactly.

<a id="rational-positive-laurent-gram-lemma"></a>
## 4. A strictly positive rational Laurent polynomial has a rational weighted-square representation

**Lemma.** Let h=sum_(l=-L)^L h_l t^l in R with h*=h and h>=delta>0 on the circle, where delta is a known positive rational lower bound.
Set C=2sum_(l=1)^L l|h_l|, with the empty sum zero.
Choose an integer M>L with M-L>C/delta.
Define the M-by-M rational symmetric matrix

    Q_ij=h_(j-i)/(M-|j-i|), 0<=i,j<M,
    h_l=0 for |l|>L.                               (7)

Then Q is positive definite, and there are d_a>0 rational and p_a in Q[t], degree at most M-1, such that h=sum_(a=1)^M d_a p_a p_a*.

*Proof.* For z=(1,t,...,t^(M-1))^T, exactly M-|l| pairs have j-i=l.
Hence z*Qz=h as a Laurent identity.
Put T_ij=h_(j-i).
Its finite Fourier quadratic form gives T>=delta I: for any complex vector b, integrate h(t)|sum_j b_j t^-j|^2 on the circle.
The result is b^*Tb, and the lower bound is delta sum|b_j|^2 by Fourier orthogonality.

Write Q=T/M+Delta.
Its diagonal error vanishes, and for 0<|j-i|<=L the error entry is |j-i|h_(j-i)/[M(M-|j-i|)].
Thus every absolute row sum is at most C/[M(M-L)].
Symmetry and 2|b_i b_j|<=|b_i|^2+|b_j|^2 give

    |b^*Delta b|<=C/[M(M-L)] ||b||^2,
    Q>=[delta-C/(M-L)] I/M>0.                       (8)

These are complete finite coefficient estimates, not an asymptotic spectral theorem.
The case L=0 is included with M=1.

Rational Gaussian elimination gives Q=L_0 diag(d_a)L_0^T with L_0 rational unit lower triangular and all d_a positive rational.
At each step the positive pivot and positive-definite Schur complement follow from the same quadratic form, so no square root is needed.
Setting p=L_0^T z gives

    h=sum_(a=1)^M d_a p_a p_a*, d_a>0.              (9)

Every p_a is a nonzero rational polynomial of degree at most M-1.
This is precisely the rational weighted-square representation required here.
It does not claim a single rational spectral factor or factorization without the displayed positive rational weights.

<a id="nonzero-unit-residue-completion"></a>
## 5. Repairing zero residues and normalizing the exact covariance

Apply the lemma to the strictly positive h in (5)--(6), and put H_a=P p_a.
Then H_a(alpha)=0 and H_a H_a*=B p_a p_a*.
Equations (5) and (9) give the exact constant completion

    sum_j lambda_j v_j v_j*+sum_a d_a H_a H_a*=E.   (10)

The H_a are not admissible unit-income coordinates: their original resultant is zero.
They are not retained as if they had unit values.

Choose ANY rational r>0, and replace each such coordinate by

    K_(a,+)=H_a/r+1, K_(a,-)=H_a/r-1,
    raw weight d_a r^2/2 for each sign.

The new original values are exactly +1 and -1, both actual O-units.
Direct expansion cancels the cross terms and gives

    (d_a r^2/2)(K_(a,+)K_(a,+)*+K_(a,-)K_(a,-)*)
         =d_a H_a H_a*+d_a r^2.                    (11)

Let D_sos=sum_a d_a>0 and Z_r=1+D_sos r^2.
The original raw weights have sum one and the added weights have sum D_sos r^2.
Divide ALL weights by Z_r.
The resulting strictly positive rational weights omega_b sum to one, every coordinate V_b is rational Laurent with a nonzero actual O-unit residue, and

    sum_b omega_b V_b V_b*=E_r,
    E_r=(E+D_sos r^2)/(1+D_sos r^2),
    E<E_r<1, E_r-E=(1-E)D_sos r^2/(1+D_sos r^2).   (12)

The original k coordinate residues remain exactly u_j before common monomial normalization; their relative weights remain in the ratios lambda_j.
The added 2M residues are the displayed signed units.
For every prescribed positive tolerance, a sufficiently small positive rational r makes E_r less than E plus that tolerance.
This is an exact identity at each finite r, not an approximate covariance limit.
It does not assert that every desired rational output energy can be hit exactly by rational r.

This proves the lifting theorem for every supplied field profile (1).
All zero-residue auxiliary coordinates have been replaced; none supplies spurious norm income.
No coefficient-field extension, numerical positivity check or irrational square root was used.

<a id="original-norm-denominator-and-degree-costs"></a>
## 6. Complete original integer costs and finite construction sizes

Choose one common Laurent monomial t^m so all coordinates have nonnegative exponents, and then the ACTUAL least common positive scalar denominator q making F_b=q t^m V_b integral.
Because alpha and alpha^-1 belong to the specified order, every new residue alpha^m V_b(alpha) is still an actual O-unit.
This changes the original labels by a common unit monomial; it does not erase that normalization.
Norm_K(alpha)=1 and the original degree d is even, so the full signed resultants are

    Res(P,F_j)=q^d Norm_K(u_j) for the original labels,
    Res(P,F_(a,+))=Res(P,F_(a,-))=+q^d.

All are nonzero and contain EVERY original conjugate.
The added minus-one value has norm (-1)^d=+1, not a fabricated negative unit.
Every original negative unit keeps its actual full sign.
The complete circle identity and norm income are

    sum_b omega_b F_b F_b*=q^2 E_r,
    I=(1/d)sum_b omega_b log|Res(P,F_b)|=log q,
    I-(1/2)log(q^2 E_r)=-(1/2)log E_r>0.            (13)

The weighted positive-lag correlations all vanish exactly.
Individual coefficient contents remain in the integer auxiliaries; removing one would change its full norm and energy and is not done.
If M_w is the ACTUAL least common weight denominator and m_b=M_w omega_b, their complete copied signed norm product is q^(d M_w) product_b Norm_K(V_b(alpha))^(m_b).
Scalar coefficient denominator q, weight denominator M_w and Gram dimension M are separate quantities.

Every integral F_b is nonzero and has squared coefficient norm at least one.
Thus q^2 E_r>=1, a necessary elementary denominator cost.
In particular q must grow if a sequence of these exact energies tends to zero.
This is the familiar integral-energy constraint, not a new free normalization.
As r tends to zero at fixed earlier construction, some coordinate coefficients and the weight denominator can grow even if q happens to stay fixed.

There are explicit finite support costs.
With the initial ordinary degree-at-most-d-1 representatives, G,x,c have support radius at most d-1; g_j has support in [-(d-1),2(d-1)].
From (3), h_0 has support radius at most 2d-3, with h_0=0 included.
Damping gives v_j support in [-Nd-d+1,Nd+2d-2], and h in (5) has radius L<=2Nd+2d-3.
The Gram choice M>L+C/delta and the d_a/p_a are actual construction data.
Each added K coordinate has degree at most d+M-1.
Therefore a common polynomial window may be chosen with

    T<=max{2Nd+3d-3, Nd+2d+M-2},
    number of coordinates = k+2M.                  (14)

The actual common union width can be smaller; equality is not claimed.
The damping requirement N>K_0/(2epsilon E), the possibly tiny delta=(2N epsilon E-K_0)2^(-2N), the Gram size, rational LDL pivots, final r, all coefficient denominators and all weight denominators remain paid.
These formulas prove finite existence, not a useful uniform bound or an efficient algorithm.
No computation of these quantities for a specific input has been performed.

For a genuine Salem packet supplied by L388, L389's finite distinguished-root-product inequality remains applicable.
If its distinguished unit is epsilon_0^n with |rho_0(epsilon_0)|=R_0>1 and original weight lambda_0, the final repair has weight lambda_0/Z_r on that same residue and energy E_r.
Consequently its actual width obeys Tm(P)>=2n log R_0+log[lambda_0/(Z_r E_r)]=2n log R_0+log[lambda_0/(E+D_sos r^2)].
Here n is the unit-packet exponent, separate from the damping exponent N.
The new coordinates and changed normalization do not remove this cost; neither the old weight lambda_0 nor the old energy E is silently substituted into the final bundle's inequality.

<a id="exact-covariance-sign-criterion-and-window-boundary"></a>
## 7. Genuine-Salem sign criterion and the general original degree expense

**Corollary, genuine Salem only.** Restrict to a genuine Salem input d>=4 and combine Theorem 1 with L388 for the SAME actual sigma-stable order containing alpha and alpha^-1.
If an actual negative-full-norm unit exists, L388 supplies (1) at any positive rational E.
Choose E arbitrarily small, then choose rational r so E_r is only slightly larger.
Thus there exist finite exact constant-covariance rational Laurent unit bundles with normalized energies arbitrarily close to zero.
Conversely any such bundle of energy below one evaluates to a constant field profile below one, so L372 forces at least one actual negative-full-norm unit.
This is an existence equivalence at the stated GENUINE SALEM unit/order scope.
It is not universal negative-unit availability, a two-coordinate paraunitary classification or a uniform-gap theorem.
Outside the Salem subclass this draft adopts only the conditional lifting from the supplied profile (1), not L388's profile existence or L372's full-sign necessity.
In particular no sign conclusion is transplanted to multiple exterior trace places or nonreal trace fields.

A complete necessary window cost remains throughout the GENERAL reciprocal domain of Section 1, even in the exact constant case.
Use the actual common polynomial window [0,T] and original degree d.
The accepted elementary L318 Poisson/reversal estimate applied to each F_b and summed with these SAME weights gives, at every original root alpha_i, including nonreal exterior roots when present,

    sum_b omega_b |F_b(alpha_i)|^2
       <=q^2 E_r max(1,|alpha_i|)^(2T).

Finite weighted logarithmic concavity and the complete original resultants in (13) then give

    log q <= log q+(1/2)log E_r+(T/d)m(P),
    -(1/2)log E_r <= (T/d)m(P).                     (15)

There is no small-height or equidistribution hypothesis in this direct exact-constant specialization: the aggregate Poisson majorant is the constant q^2 E_r.
All original roots and the common degree window are retained.
Hence T>=d log(1/E_r)/(2m(P)).
Arbitrarily low energies force a growing window even for fixed P; on a hypothetical near-one family a fixed positive surplus would demand an unbounded T/d unless a genuine gap were separately established.
Existence from L388 and this construction supplies no missing uniform control of that expense.

The resulting explicit integer auxiliaries have exact full covariance in their own right.
Orthogonal least-energy residual projection may change that covariance, so it is not silently applied.
The theorem closes the field-profile-to-some-Laurent-bundle existence interface by allowing finitely many additional unit coordinates and changed normalized weights.
It is not a replacement of L318's already existing binomial complementarity by a new name: its additional obligation is the prescribed original unit norm income, repaired even on the formerly zero-residue coordinates.
It leaves the quantitative degree/height/denominator, residual and near-one coverage questions at their actual scopes.

## 8. Complete author self-check and pending review

The author checked the general original irreducible/reciprocal nontorsion-unit domain, even degree including d=2, and B=t^-d P^2; evaluation at all original roots and the actual-order monomial guard; every coefficient in the second-order error (2); Laurent divisibility and self-star quotients including h_0=0; damping range, positive integer N, exact finite geometric-sum quotient and the uniform lower bound at zeros of P; all Toeplitz/Gram index orientations, diagonal multiplicities, rational entries, strict row-error estimate, constant-h case and rational positive LDL; every zero-residue H coordinate and its inadmissible norm before repair; the paired cross-term cancellation, exact +/-1 values, positive rational raw/final weights and E<E_r<1; unchanged original values before monomial normalization; all full signed original norms, added minus-one sign, common q, actual contents, weight multiplicities and coefficient energy; all explicit finite support/dimension bounds and their lack of uniformity; the exact sign-existence equivalence ONLY in the genuine Salem subclass using L388/L372; and the general original-root Poisson/log degree cost without a falsely inherited small-height, real-trace or single-exterior-pair assumption.
Root explicitly requested and contributed the broader-domain interface check before freeze.

The source screen located the exact classical Gram construction and did not claim it as new.
The univariate bound and rational LDL argument are complete locally, reusing L22's algebraic coefficient-field method.
No complex coefficient spectral factor, rational-descent theorem, multivariate factorization result, uninspected numerical algorithm or full-source proof audit is adopted.
Root supplied the substantive candidate, and this is author self-review.
Separate whole noncontributor review and coordinator fixed retention remain pending.
No native mathematical program, scan, solver or new J occurred; G0001 remains active and unrestrictedly unresolved.

<a id="complementary-unit-lift-entire-author-freeze"></a>
## Entire author freeze

2026-10-11T16:22.
The complete author body, Sections 1--8 and equations (1)--(15), Theorem 1 on the general reciprocal nontorsion-unit domain, strict rational Gram lemma, genuine-Salem-only sign corollary, source/reuse and root contribution disclosure, all original unit residues/norms, second-order divisibility and zero-safe positivity, paired nonzero repair, exact weight/energy normalization, explicit dimension/support/denominator costs, L389's correctly renormalized packet price, and general original-root width lower bound are frozen after complete author self-check.
The scoped material check passed.
No native mathematical program, scan, solver or new J occurred.

The author is stopped; whole noncontributor review and coordinator fixed retention remain pending.
Root's substantive core and domain clarification are not an independent review.
G0001 remains active and unrestrictedly unresolved.

### Complete L389 author account

## Original window and coefficient costs of concentrating trace-unit packets

Date:2026-10-12.
Authored by integer_symbol_review AI for Yin under continuing G0001 weekly authorization.
This distinct responsible draft was allocated before substantive derivation.
Root supplied the substantive candidate: a distinguished trace-unit power preserves its product at the two original real embeddings under independent signed monomial twists; fixed-window Poisson/reversal and coefficient Cauchy--Schwarz impose quantitative width or energy costs.
Root is a contributor and cannot serve as the independent whole reviewer of this account.
No native mathematical program, scan or new J was used.

<a id="trace-packet-cost-reuse-and-conditional-input"></a>
## 1. Reuse, current packet and actual scope

This account concerns the CURRENT new [D2 field-profile construction, now fixed in L388](../ledger/Yin_L_G0388_v1.md#negative-unit-profile-entire-author-freeze), whole author freeze2026-10-11T15:58, especially its [actual trace-unit directions](../ledger/Yin_L_G0388_v1.md#actual-order-units-in-every-log-cone), [positive rational profiles](../ledger/Yin_L_G0388_v1.md#positive-rational-field-profile-construction) and [weight asymptotics and costs](../ledger/Yin_L_G0388_v1.md#rational-weight-denominators-and-original-costs).
That rolling address was reused for the distinct argument and inherits no retired D2 evidence.
Its entire saved argument was read before this cost derivation.
The packet was then pending whole noncontributor review; the completed [R214 whole finding](../audits/reviews/Yin_R_G0214_v1.md#negative-unit-rational-profile-whole-finding) now supports the unchanged fixed L388 account.
This locator/status maintenance preserves the cost mathematics and its00:05 author freeze.
Pending-input wording below records the initial review boundary; the packet dependency is now resolved at R214's actual scope.
The finite estimates hold for every actual packet satisfying their stated hypotheses.
This author neither supplies that packet proof nor claims an independent review of it.

[L318's polynomial Poisson majorant](../ledger/Yin_L_G0318_v1.md#polynomial-poisson-majorant) already proves the positive-kernel inside-disk square bound and the fixed-window reversal for exterior roots.
Its [complete weighted theorem](../ledger/Yin_L_G0318_v1.md#weighted-integral-bundle-bound) explicitly retains common window T, all original conjugates and exact aggregate covariance.
[L377's two-real-root width argument](../ledger/Yin_L_G0377_v1.md#independent-twist-width-four-obstruction) already applies that same inside/reversal bound to independently twisted original residues.
[L372's common-twist energy bounds](../ledger/Yin_L_G0372_v1.md#new-quartic-mixed-unit-identity), equation(15), already use coefficient Cauchy--Schwarz at BOTH original real embeddings and V_+=beta^(2T)V_-.
These exact passages were read before deriving the present application.
No new maximum principle, general analytic theorem, spectral factorization or novelty claim is introduced.

The [existing ABR01 selected inspection](../audits/literature/ABR01/readme.md#selected-poisson-attribution) is the inherited classical-method attribution.
This author read that account and L318's self-contained finite kernel calculation, not a fresh PDF.
D2's new actual-order Dirichlet input stays at its own recorded source scope and pending whole-review boundary; it is not needed to prove the finite inequalities for an already supplied packet here.
No full unit-group theorem or regulator bound is imported into these cost calculations.

Let alpha=beta>1 be a genuine Salem number, P its original monic irreducible polynomial, d=2s>=4, K=Q(alpha), sigma(alpha)=alpha^-1, and F=Q(tau), tau=alpha+alpha^-1.
The original real roots are beta,beta^-1, and

    m=m(P)=log beta>0, Norm_K(alpha)=1.               (1)

Let O be the actual sigma-stable full order used by the packet, B=O intersection F, and rho_0 the trace embedding tau->beta+beta^-1.
Suppose the packet includes, for an integer N>=1,

    u_0(N)=epsilon_0^N, epsilon_0 in B^times,
    r=|rho_0(epsilon_0)|>1, ell=log r>0,
    a_00(N)=r^(2N), weight w_0(N)>0.                 (2)

Other labels can be any actual packet units with positive weights w_j summing to1.
The finite estimates only need the distinguished label(2); no cancellation assumption on the other labels is used.
For the current D2 construction, fix its positive rational target E, negative-unit relative value c_0<0, and the finitely many chosen trace units.
Then its claimed packet asymptotics give

    w_0(N)->w_* =(-c_0)/(1-c_0)>0                    (3)

as integers N tend to infinity.
Fixed input, chosen units and fixed E are essential to this use of(3).

<a id="independent-twists-common-window-and-full-costs"></a>
## 2. Independent twists, common window and all scalar costs

Let H_j in Q[t,t^-1] be arbitrary rational Laurent representatives with

    H_j(alpha)=delta_j alpha^(k_j) u_j(N),
    delta_j in{1,-1}, k_j in Z.

All independent k_j are allowed in the finite analytic inequalities.
Let[L,U] be the ACTUAL union of their coefficient supports and T=U-L>=0.
Normalize by ONE common monomial f_j=t^(-L)H_j in Q[t], so deg f_j<=T.
This preserves every coefficient squared norm and every circle square.
Different effective spans of individual labels cannot replace the common union width T.

Because epsilon_0 lies in the trace field, its values at the two original real embeddings agree.
The independent sign, its own alpha power and the common normalization cancel in their product.
Thus

    |f_0(beta) f_0(beta^-1)|=r^(2N)=a_00(N).        (4)

This includes negative exponents and negative rho_0(epsilon_0), since the original trace-unit power occurs twice.
No signed cancellation with another packet label can reduce this positive absolute product.

D2 allows a general full order O, not necessarily one containing alpha.
Consequently an arbitrary alpha^k twist or common monomial normalization need not preserve membership in O^times.
The bounds hold for every displayed representative regardless.
If a later construction requires every twisted target to remain an actual O-unit, restrict to its admissible twists, or assume alpha is an O-unit, as in O=Z[alpha,alpha^-1].
Every alpha power remains an algebraic unit and has full norm1 in K, so the full norm and product identities below do not require that additional order-membership assertion.

Let q be the ACTUAL least positive common scalar coefficient denominator of the normalized rational representatives, and put F_j=q f_j in Z[t].
No nonconstant polynomial denominator is allowed in this class.
Then

    |F_0(beta)F_0(beta^-1)|=q^2 r^(2N),
    Norm_K(F_j(alpha))=q^d Norm_K(u_j(N)).

Here the sign delta_j has norm1 because d is even, and all signed monomial shifts have norm1.
In the D2 packet the positive directions have full norm+1 and its negative direction has full norm-1, so every complete original resultant is respectively+q^d or-q^d.
No trace-degree or selected-root product replaces those full norms.
If the integer content of F_j is b_j, the nonzero integral primitive resultant gives b_j|q; all contents are retained.
Dividing them out separately would alter the evaluation, energy and covariance data and is not performed.

For rational weights let M be their least common denominator and m_j=Mw_j positive integers.
Then sum m_j=M, and the complete signed resultant product is q^(dM) product_j Norm_K(u_j)^(m_j).
In D2 it is q^(dM)(-1)^(m_-).
The weight denominator M and coefficient denominator q are different actual objects.
Both can vary with N and neither is silently identified with the prescribed rational E.

<a id="exact-covariance-distinguished-product-width-bound"></a>
## 3. Exact constant covariance imposes a finite width bound

Assume in addition the ACTUAL full-circle identity

    sum_j w_j |f_j(exp(i theta))|^2=E>0
                      for every real theta.        (5)

This is not supplied by field interpolation alone.
If the packet's relative-norm field profile equals the prescribed E, then any constant in(5) is forced to be that same E: evaluate at an original circle conjugate of the genuine Salem input, where rational real coefficients turn reversal into complex conjugation and signed monomial twists have relative norm1.
Thus an exact covariance cannot choose a different constant while retaining these residues and weights.

The reused L318 Poisson bound gives sum_j w_j|f_j(z)|^2<=E for |z|<=1.
Apply it also to t^T f_j(t^-1).
At the TWO original real roots,

    w_0 |f_0(beta^-1)|^2<=E,
    w_0 |f_0(beta)|^2<=E beta^(2T).

Multiplying these inequalities and taking the nonnegative square root, then using(4), gives

    w_0 r^(2N)<=E beta^T,
    Tm >=2N ell+log(w_0/E).                          (6)

There is no division by d in this two-real-root inequality; m=log beta is the ORIGINAL total Salem measure.
In the original normalized radial-cost convention it reads (T/d)m>=[2N ell+log(w_0/E)]/d.
No replacement by the trace degree s is made.
The right side of(6) may be negative for a particular small N; the finite inequality remains valid and yields a nontrivial positive width floor when that right side is positive.

All q factors cancel only AFTER charging them: for the integral F_j, the two right sides are q^2 E and q^2 E beta^(2T), while the distinguished product is q^2 r^(2N).
Their resulting inequality is w_0 q^2 r^(2N)<=q^2 E beta^T, exactly(6).
If integer multiplicities are used, the same inequality is m_0 q^2 r^(2N)<=Mq^2 E beta^T; divide by Mq^2.
No choice of a growing scalar denominator or weight denominator removes this width price while w_0 stays bounded away from zero.

<a id="coefficient-energy-bound-without-covariance"></a>
## 4. A finite coefficient-energy bound without constant covariance

For any representatives in Section2, regardless of their circle autocorrelations, define their COMPLETE weighted rational coefficient energy

    A=sum_j w_j ||f_j||_2^2,
    V_T=sum_(k=0)^T beta^(-2k),
    V_+=sum_(k=0)^T beta^(2k)=beta^(2T)V_T.

Coefficient Cauchy--Schwarz, including every coefficient position in the common window, gives

    |f_0(beta)|<=||f_0||_2 sqrt(V_+),
    |f_0(beta^-1)|<=||f_0||_2 sqrt(V_T).

Multiply and use(4).
Since every weighted squared coefficient norm is nonnegative,

    A>=w_0 ||f_0||_2^2
     >=w_0 r^(2N)/(beta^T V_T)
     >=w_0(1-beta^-2) r^(2N) beta^-T.                (7)

The last direction follows from V_T=(1-beta^(-2(T+1)))/(1-beta^-2)<=1/(1-beta^-2), with beta>1.
The exact first bound retains the full finite geometric sum; the weaker last expression is convenient for fixed-input asymptotics.
T=0 and all padded endpoints are covered.
No constant covariance, residual projection, optimum, or cancellation of signs is assumed in(7).

For cleared integer polynomials, A_int=sum_j w_j||F_j||_2^2=q^2 A.
Their distinguished product is q^2 r^(2N), so the same proof gives A_int>=w_0 q^2 r^(2N)/(beta^T V_T).
For integer weight copies, the complete coefficient energy is sum_j m_j||F_j||_2^2=Mq^2 A.
Dividing by the actual Mq^2 yields exactly(7).
This explicitly preserves both denominators and every auxiliary content.
Field values may cancel at the exterior trace place, but these coefficient-square terms cannot.

If(5) does hold, Parseval gives A=E.
Equation(6) is the stronger constant-covariance application; the coarser energy floor(7) alone is not used to assert covariance.
Both are necessary bounds, with no assertion of simultaneous attainment.

<a id="fixed-input-large-power-linear-window-cost"></a>
## 5. Fixed-input and fixed-E large-power consequences

Now condition on the D2 packet and its claimed(3).
For the FIXED field, order, chosen units and prescribed rational E>0, choose N_1 such that w_0(N)>=w_*/2 for every N>=N_1.
If exact covariance(5) is realized by a sequence of representatives of widths T_N, equation(6) gives

    T_N m>=2N ell+log[w_*/(2E)],
    liminf_(N->infinity) T_N/N>=2ell/m>0.            (8)

More generally, without constant covariance, suppose only that their actual weighted coefficient energies satisfy A_N<=A_* for one fixed finite A_*>0.
Equation(7) gives

    T_N m>=2N ell
              +log[w_*(1-beta^-2)/(2A_*)],
    liminf_(N->infinity) T_N/N>=2ell/m>0.            (9)

Thus the positive rational field profiles in this particular large-power construction cannot be realized with bounded energy and sublinear-in-N common windows, even with independent signed monomial twists.
For T_N=o(N), the unconditional finite bound further gives

    liminf_(N->infinity) log A_N/N>=2ell.             (10)

These are fixed-input statements.
The constants beta,m,ell,w_*,N_1, the chosen units, weights and their denominators depend on that input and on the fixed target E.
D2's proof does not supply uniform control as E tends to zero or as the field/input varies toward total measure zero.
In particular1-beta^-2 can vanish and the selected log-unit/lattice data can vary in a joint limit.
No such joint limit is taken here.
The finite inequalities remain valid for actual supplied parameters, but do not by themselves establish a uniform near-one obstruction, construction or Mahler gap.

<a id="trace-packet-cost-entire-author-freeze"></a>
## 6. Outcome and author self-check

This account reuses the already retained Poisson/reversal and two-real-root coefficient inequalities to charge the distinguished direction of the new field-profile packet.
Its finite conclusions(6)--(7) hold for any actual packet satisfying the explicit hypotheses, without assuming D2's existence proof.
Applying them through N->infinity uses D2's pending positive-weight construction and(3), so(8)--(10) remain conditional on that exact packet until its whole review.
Root's supplied core is substantive; neither root acceptance nor this author self-check is independent whole review.

The author self-check covers the original Salem real pair and total measure; actual trace-unit values and even powers; independent signs and signed exponents; one ACTUAL union window and common normalization; the general-order versus alpha-unit twist boundary; every q^2 and M factor; signed full q^d norms and integer contents; the distinction between prescribed field E, actual full-circle covariance E and coefficient energy A; both inside/reverse bounds; multiplication/square-root/log directions in(6); both coefficient Cauchy--Schwarz inequalities, V_+=beta^(2T)V_T and the finite geometric-sum direction in(7); T=0 and nonpositive finite width floors; exact-covariance A=E versus arbitrary A; and fixed-input/fixed-E/nonzero limiting weight quantifiers versus an unproved joint near-one claim.

No native mathematical program, scan, solver or J occurred.
Scoped material validation passed for D3 and the exact current D2 input; it verifies structure and locators, not mathematical correctness.
The complete Sections1--6/equations(1)--(10) are frozen at2026-10-11T16:05 for a separate whole noncontributor review.

No exact Laurent-covariance existence, least-energy residual covariance, uniform height/denominator/window bound or unrestricted G0001 completion is asserted.

### L392 nonzero-target interface, at its stated totally real domain

<a id="arbitrary-nonzero-value-rational-lifting-extension"></a>
## 4. Precise extension of L390 to arbitrary nonzero target values

**Structural extension.** For the selected original P and reciprocal involution, suppose any nonzero targets a_1,...,a_k in K and positive rational weights lambda_j summing to1 satisfy sum lambda_j a_j sigma(a_j)=E in Q with0<E<1.
For every real eta>0 there is a finite rational Laurent family V_b with strictly positive rational weights omega_b summing to1 and exact constant covariance E' satisfying E<E'<min(1,E+eta).
Each original coordinate retains value a_j EXACTLY before common monomial normalization; every added coordinate has value+1 or-1.
Original weight ratios are preserved.
No original target inverse or integrality is needed for this structural statement.
Integrality is an additional premise for the norm-income lower bound in Section5.

Here is the complete changed interface to the accepted L390 construction.
Choose ordinary rational representatives f_j of degree at most d-1.
Put G=sum lambda_j f_j f_j*, where f*(t)=f(t^-1), and let B_P=P P*=t^-d P^2.
The equality G(alpha)=E uses the field profile and star evaluation as sigma, not target unit status.
The kernel of Laurent evaluation at alpha is generated by the ACTUAL minimal P.
Therefore

    x=(G-E)/E, C=1-x/2, g_j=C f_j,
    C(alpha)=1,
    G_1=sum lambda_j g_j g_j*=C^2G,
    G_1-E=E x^2(x-3)/4=B_P h_0,
    h_0 in Q[t,t^-1], h_0*=h_0.                    (6)

These are the same finite identities as L390.
P^2 divisibility follows before evaluation, including the h_0=0 case.
On the circle G_1 is a nonnegative weighted square sum for arbitrary rational real f_j.
Let H_P be the full coefficient absolute sum of original P, K_0 the Laurent coefficient absolute sum of h_0, epsilon=1/(2H_P^2), S=1-epsilon B_P, and choose an integer D>=1 with2D epsilon E>K_0.
Then1/2<=S<=1 on the circle and S(alpha)=1.
With v_j=S^D g_j,

    E-sum lambda_j v_j v_j*=B_P h,
    h=E epsilon sum_(a=0)^(2D-1)S^a-h_0 S^(2D),
    h>=delta=(2D epsilon E-K_0)2^(-2D)>0.           (7)

L390's elementary derivative inequality for(1-y)^(-2D) proves the bound where B_P>0.
The displayed finite Laurent sum defines it at every circle zero of P as well, where h=2D epsilon E-h_0; continuity or this exact value gives the same bound.
Every v_j(alpha)=a_j, since both correcting factors evaluate to1.
No target inverse is used.

The complete L390 rational Gram lemma now applies to this self-star h and positive rational delta.
With support radius L_h and C_h=2sum_(l=1)^(L_h)l|h_l|, choose integer M>L_h with M-L_h>C_h/delta.
Its normalized rational Gram entries h_(j-i)/(M-|j-i|), positive Fourier/row-error estimate and rational LDL give h=sum_(a=1)^M d_a p_a p_a*, d_a>0 rational and deg p_a<=M-1.
This is exactly the previously proved lemma at its actual hypotheses, with no new spectral factor or coefficient-field descent.

The temporary H_a=Pp_a have ZERO original values and cannot supply income.
Replace each by H_a/r+1,H_a/r-1 at raw weights d_a r^2/2 for any small rational r>0.
They have exact nonzero values+1,-1.
Cross terms cancel, adding the old H_a square and constant d_a r^2.
If D_sos=sum d_a>0, then

    Z_r=1+D_sos r^2,
    omega_j=lambda_j/Z_r for original coordinates,
    omega_(a,+)=omega_(a,-)=d_a r^2/(2Z_r),
    sum_b omega_b V_b V_b*=E'=(E+D_sos r^2)/Z_r,
    E<E'<1, E'-E=(1-E)D_sos r^2/Z_r.                (8)

A sufficiently small positive rational r gives the stated eta tolerance.
Every finite r gives an EXACT Laurent identity, with all original nonzero values retained and all temporary zero-value coordinates removed.
This proves the new structural extension.
The unit assumption in L390 was needed for its later exact income simplification, not any step just reconstructed.



## Extraction operation and preserved history

2026-10-11T17:29: reusable mathematical registration extracts L390, L389 and L392 Section4; direct exact-covariance inequality from the L318 branch, with historical R292/R291/R294 coverage retained.
Fixed L originals and R findings are preserved.
The complete author accounts below retain their original freezes, contribution disclosures, corrections, comparisons and historical pending statements.
The present decision controls current assessment; copied historical pending prose is not an alternative selection.
Current hypotheses and proof selections above delimit the adopted candidate.
Original proof/source inspection is not expanded by relocation.
Complete-body preservation is checked separately.
No native execution or new mathematical computation accompanies this operation.
