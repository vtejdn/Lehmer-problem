---
author: Yin
---
# Critical-scale arithmetic and the costs of joint Taylor evaluation

Date: 2026-11-06.
This exploration concerns the unchanged [unrestricted Lehmer contract](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating agent and the alternative_mechanism, bottleneck_diagnosis and external_structural_lead contributors developed the comparisons below as author work for Yin.
The coordinating agent checked the displayed deductions and independently recomputed the specified finite matrices as ordinary development checks.
No formal independent review, new Claim assessment, literature novelty claim or unrestricted positive-gap conclusion is made.

The question is whether small total measure supplies additional arithmetic information at a degree-dependent scale, or whether joint evaluation avoids the costs of the earlier scalar comparisons.
The three tests below retain their original inputs and complete stated costs.
They reuse the accepted statements at their existing review and source-inspection scopes.
The conclusions are useful limitations and conditional continuation points, rather than an assertion that all related mechanisms are impossible.

<a id="degree-scale-abel-test"></a>
## Degree-scale smoothing and the actual integer-trace radius

Let P be monic, irreducible, reciprocal and noncyclotomic in Z[x], of degree d with constant coefficient one.
Assume every positive power of a root preserves degree d.
Write its full roots as alpha_i=exp(ell_i+i theta_i), and put
\[
 m=\sum_i(\ell_i)_+,\qquad H=\max_i|\ell_i|,\qquad
 E_2=\sum_i(\ell_i)_+^2.
\]
All logarithms are natural, and total measure is never divided by degree.
Reciprocity gives radial extrema H and -H and sum_i |ell_i|=2m.

Reuse the [complete tensor object](Yin_L_G0453_v1.md#same-input-tensor-and-mahler-cost) and [contracted comparison](Yin_L_G0453_v1.md#contracted-trace-error-and-finite-tail):
\[
 \beta_{ij}=\alpha_i/\alpha_j^2,\quad
 a_{ij}=\ell_i-2\ell_j,\quad
 z_{ij}=e^{-|a_{ij}|+i(\theta_i-2\theta_j)},
\]
\[
 D_P(x)=\prod_{i,j}(1-x\beta_{ij}),\quad
 B=\tfrac12\sum_{i,j}|a_{ij}|\le3dm,\quad
 K=\sum_{i,j}\log|1-z_{ij}|.
\]
The [original resultant split](../claims/Yin_C_G0001_v1.md#statement) gives
\[
 K=\log|D_P(1)|-B\ge d\log2-B.
\]
Every ordered pair and its multiplicity is retained.
The resultant is nonzero on this nontorsion domain.

For 0<r<1 put
\[
 K_r=\sum_{i,j}\log|1-rz_{ij}|,\qquad C_n=\sum_{i,j}z_{ij}^n.
\]
Conjugation makes C_n real, and K_r=-sum_{n>=1} r^n C_n/n is absolutely convergent.
The factor inequality already used in [C4](../claims/Yin_C_G0004_v1.md#damped-cyclotomic-norm-inequalities) is
\[
 |1-rz|^2-r|1-z|^2=(1-r)(1-r|z|^2)\ge0
 \quad (|z|\le1).
\]
Applying it to all d^2 factors, with r=e^{-t}, proves
\[
 K_{e^{-t}}\ge d\log2-B-\frac{d^2t}{2}.                 \tag{A1}
\]
The absolute bound |C_n|<=d^2 also gives
\[
 \left|\sum_{n>N}\frac{e^{-tn}C_n}{n}\right|
 \le\frac{d^2e^{-t(N+1)}}{(N+1)(1-e^{-t})}.             \tag{A2}
\]
Thus for fixed c>0, t=c/d and N=ceil(d log d/c),
\[
 -\sum_{n=1}^{N}\frac{e^{-cn/d}C_n}{n}
 \ge d(\log2-c/2-3m)-\frac{d+c}{\log d}.              \tag{A3}
\]
Indeed e^{-t(N+1)}<=1/d and 1-e^{-c/d}>=(c/d)/(1+c/d).
For 0<c<2log2, this retains positive linear arithmetic income on a hypothetical sequence with m tending to zero.
The degree-logarithmic bandwidth is sufficient for the absolute estimate (A2); no necessity theorem for the actual signed coefficients is asserted.

The old torsion control P=Phi_{2p}, d=p-1, makes the scale visible:
\[
 K_r=\log(1+r)+(p-2)\log(1+r^p),\qquad
 K_{e^{-c/d}}/d\longrightarrow\log(1+e^{-c})>0.
\]
It remains a torsion control with a power-degree drop, not a near-zero nontorsion sequence.

Writing s_n=sum_i alpha_i^n, the original integer traces are
\[
 u_n=\sum_{i,j}\beta_{ij}^n=s_ns_{2n}\in\mathbb Z,\qquad
 \log D_P(x)=-\sum_{n\ge1}u_nx^n/n
\]
near zero, with the logarithm normalized to zero there.
Its exact Taylor radius is
\[
 R_{\rm raw}=e^{-3H}.                                \tag{A4}
\]
Every beta has modulus at most e^{3H}.
If alpha_i has radial logarithm H, choose alpha_j=alpha_i^{-1}; then beta_ij=alpha_i^3 has modulus e^{3H}.
The corresponding nearest zero of D_P is a nonremovable singularity of its logarithm, since D_P'/D_P has a pole there.
Multiplicity cannot cancel that pole.

The accepted [C855 v2, Part D](../claims/Yin_C_G0855_v2.md#statement) applies on precisely this original domain and gives dE_2>=1/20.
Since E_2<=Hm and E_2<=m^2,
\[
 dH\ge\frac1{20m},\qquad d\ge\frac1{20m^2}.           \tag{A5}
\]
Consequently on any hypothetical near-zero sequence, dH tends to infinity.
For fixed c>0 and m<3/(20c),
\[
 e^{-c/d}>e^{-3H}=R_{\rm raw}.                        \tag{A6}
\]
The smoothing scale retaining the arithmetic income is therefore eventually outside the actual raw Taylor disk.
This excludes the proposed infinite integer-trace substitution at that scale, rather than merely finding a poor sufficient convergence bound.

A finite comparison is still legitimate.
The old contraction calculation, now with the exact H in its exponent, gives
\[
 \left|K_{e^{-t}}+\sum_{n=1}^N e^{-tn}u_n/n\right|
 \le2B\sum_{n=1}^N e^{(3H-t)n}
   +\frac{d^2e^{-t(N+1)}}{(N+1)(1-e^{-t})}.            \tag{A7}
\]
Reciprocity and conjugation identify its actual signed discrepancy as
\[
 u_n-C_n=\sum_{i,j}\sinh(n|a_{ij}|)
                   \cos(n(\theta_i-2\theta_j)).       \tag{A8}
\]
To verify (A8), average the raw sum over the inverse-pair permutation to obtain cosh(na_ij), then subtract exp(-n|a_ij|).
At t=c/d, (A5) makes the positive majorant in (A7) ineffective.
That is not a lower bound for the actual signed error.
An additional cancellation estimate for (A8), or a genuinely different representation retaining arithmetic, is still missing.

<a id="fixed-incidence-energy-test"></a>
## A complementary fixed-incidence test of the new coordinate kernel

Use the actual degree-eight Salem source and degree-24 endpoint construction of [C866 v10](../claims/Yin_C_G0866_v10.md#coordinate-unit-counterexample).
Put z=a_1a_2, ell=log(alpha)>0, and gamma=z^N u, where N>=1 and u is a coordinate unit with exact incidence norm Phi(u)=1.
The retained embedding formulas give, on the four oriented labels of each support {1,j}, j=2,3,4, the logarithms
\[
 x_j,\ x_j,\ -x_j,\ -x_j,\qquad x_j=N\ell+c_j,
 \qquad \sum_{j=2}^4c_j=0.
\]
The other twelve logarithms vanish.
Thus on the 24 labels,
\[
 \sum_T\log^2|\gamma_T|
 =12N^2\ell^2+4\sum_{j=2}^4c_j^2.                    \tag{E1}
\]

Restrict to the strict chamber x_j>0 for every j.
The v10 condition N ell>max_j |c_j| suffices.
The positive labels are exactly the signatures containing a_1, and the negative labels exactly those containing its inverse.
If tau fixes gamma, applying every g in the Galois group to that equality forces tau S_0 and S_0 to have the same membership in every original root.
Thus tau fixes S_0, and the stabilizer is exactly the signature stabilizer H_0.
Since gamma belongs to its fixed field, both inclusions hold and the actual degree is 24.
The same reasoning applies to the baseline u=1.

It follows that
\[
 m(\gamma)=6N\ell,\qquad
 M_2(\gamma)^2=288N^2\ell^2+96\sum_jc_j^2
             =M_2(z^N)^2+96\sum_jc_j^2.              \tag{E2}
\]
Equality holds only when all c_j vanish.
Then every conjugate of u has modulus one, and the retained unit theorem's finite torsion kernel makes u torsion.
The non-torsion kernel used in v10 therefore strictly increases the complete own-degree raw cost within this chamber.
This is a direct test of that construction, not a minimization theorem over other signatures or degree-changing chambers.
If actual degree were D, the label conversion would instead be M_2^2=(D^2/24)sum_T log^2|gamma_T|; no claim outside the strict chamber uses degree 24.

<a id="joint-evaluation-test"></a>
## Actual joint evaluation and the Boolean difference cost

Use the integral germs and private-branch independence of [L445](Yin_L_G0445_v1.md#rotated-radicals).
For an odd prime q and K=Q(zeta_q), write
\[
 U=P_2,\quad F=\sqrt{P_2P_4},\quad F/U=1+2h,\quad
 h\in\mathbb Z[[x]],
\]
\[
 U_j=U(\zeta_q^jx),\quad F_j=F(\zeta_q^jx),\quad
 M_J=\prod_{j\in J}F_j,\quad U_J=\prod_{j\in J}U_j,\quad
 \delta_J=\prod_{j\in J}(F_j-U_j).
\]
Empty products equal one.
All original roots and rotations are retained.
The full 2^q mask family is independent over K(x) on the stated all-power degree-preserving input domain.

Expansion gives mutually inverse polynomial changes of basis
\[
 \delta_J=\sum_{I\subseteq J}(-1)^{|J|-|I|}U_{J\setminus I}M_I,
 \qquad M_J=\sum_{I\subseteq J}U_{J\setminus I}\delta_I. \tag{B1}
\]
They are unitriangular over O_K[x].
The coefficient multiplying M_I has degree d(|J|-|I|), so an ordinary coefficient window of degree less than N can grow to N+qd.
It cannot be treated as the same unweighted finite lattice.

The weighted window with coefficient bound deg a_J<N-d|J| is preserved exactly by (B1).
Indeed a term a_J U_{J\setminus I}M_I has weighted degree at most deg a_J+d(|J|-|I|)+d|I|=deg a_J+d|J|<N, and the inverse expansion has the same property.
The finite monomial bases are related by a unitriangular matrix over O_K.
Its column count and explicitly extracted binary valuation are
\[
 D_N=\sum_{J\subseteq\mathbb Z/q\mathbb Z}(N-d|J|)_+,\qquad
 V_N=\sum_J |J|(N-d|J|)_+.                           \tag{B2}
\]
Indeed
\[
 \delta_J=2^{|J|}U_J\prod_{j\in J}h(\zeta_q^jx)
\]
has integral normalized coefficients.
Every full-column minor is divisible by 2^{V_N}.
Independence ensures that some sufficiently long Taylor evaluation has full column rank, but says nothing about the initial consecutive square minor.

For N>=qd, subset counting gives
\[
 D_N=2^qN-dq2^{q-1},\qquad
 V_N=Nq2^{q-1}-dq(q+1)2^{q-2}.                       \tag{B3}
\]
For fixed d,q this is only a linear explicit valuation contribution as N grows.
It is not an upper bound for the valuation of the residual normalized matrix or for its deeper Smith profile.

Descent to the original unweighted orbit module is a separate issue.
At q=3 its six series are
\[
 (f_0,\ldots,f_5)=(1,F_0,S,T,F_0S,F_0T),\quad
 S=F_1+F_2,\quad T=F_1F_2.
\]
Although
\[
 \delta_{\{1,2\}}=T-U_2F_1-U_1F_2+U_1U_2             \tag{B4}
\]
is Galois invariant and integral, it is not in their Q(x)-span when U_1 differs from U_2.
In the independent full mask basis, every combination of the six unweighted sums has equal coefficients on F_1 and F_2.
Equation (B4) has unequal coefficients -U_2 and -U_1.
Increasing N cannot repair this failure already over Q(x).
Weighted invariant generators require an actual new integral lattice and paid degree/complex-place bounds.

### Exact finite control

Take the already covered quartic of L445:
\[
 P(t)=t^4-t^3-t^2-t+1,\quad
 U=1-3x+x^2-3x^3+x^4,\quad
 V=1-7x-15x^2-7x^3+x^4,\quad F=\sqrt{UV}.
\]
Here U(zeta_3 x) differs from U(zeta_3^2 x), so (B4) applies.
The original reduction is Phi_5, a class already having a positive gap; these calculations supply no near-zero coverage.

Set
\[
 A_{M,N}[n,(i,j)]=[x^{n-j}]f_i,\quad
 0\le n<M,\quad0\le i<6,\quad0\le j<N,
\]
with columns ordered first by i, then j, and negative coefficients zero.
All calculations used exact integer arithmetic.

For reproducibility, F=sum_n a_n x^n is determined by
\[
 a_0=1,\qquad
 a_n=\frac{[x^n](UV)-\sum_{k=1}^{n-1}a_ka_{n-k}}2.
\]
The coefficients of S are (2 if 3 divides n, otherwise -1) times a_n.
If
\[
 r_l(n)=\sum_{\substack{0\le k\le n\\2n-k\equiv l\pmod3}}
                         a_ka_{n-k},
\]
then r_1(n)=r_2(n) and [x^n]T=r_0(n)-r_2(n).
Convolution gives the remaining two series.
The initial a_n for n=0,...,12 are
\[
 (1,-5,-9,-31,-181,-1170,-7956,-55926,-403884,
 -2981160,-22398948,-170776710,-1318075434).
\]

For N=1 the first independent row set is (0,1,2,3,6,9), giving
\[
 B_1=\begin{pmatrix}
1&1&2&1&2&1\\
0&-5&5&5&-5&0\\
0&-9&9&34&-34&0\\
0&-31&-62&-107&-214&-353\\
0&-7956&-15912&-22430&-44860&-53541\\
0&-2981160&-5962320&-8203572&-16407144&-18897595
\end{pmatrix}.
\]
Its determinant is 55528012334250, and positive Smith diagonal is
(1,1,1,1,3,18509337444750).
The first six consecutive rows have rank four, illustrating why nonzero minors must actually be specified.

For N=2, rows 0,...,11 give determinant
9137418592565271196828542796114088088 and positive Smith diagonal
(1,1,1,1,1,1,1,1,3,3,1332672296022,761829247548560213903556).
The dyadic valuations are ten zeros followed by 1 and 2.
In contrast, the rectangular matrices have
\[
 \operatorname{SNF}(A_{14,1})=(1,1,1,1,3,6),
\]
\[
 \operatorname{SNF}(A_{16,2})=(1,1,1,1,1,1,1,1,3,3,6,54).
\]
The last dyadic exponent drops from two to one after additional actual rows are included.
That extra bit in the shortest square minor is therefore not a divisibility property of every minor of the larger evaluation map.
The contributor found the same rectangular diagonals through forty rows; this is a finite observation, not a stabilization theorem.
The coordinating agent separately recomputed B_1 and these three smaller evaluation matrices from the displayed inputs and recurrence.

For the genuine submodule (1,S,T), the first three rows are
\[
 \begin{pmatrix}1&2&1\\0&5&5\\0&9&34\end{pmatrix},
 \qquad\det=125,\qquad\operatorname{SNF}=(1,5,25).
\]
It supplies no dyadic gain.
These finite checks and the paid Boolean calculation do not classify the full joint Smith profile.


<a id="complete-return-test"></a>
## Returning the alternatives to the original positive-gap target

Increasing q together with the window does not rescue the explicit Boolean contribution in the full-window regime N>=qd.
Equations (B2)--(B3) give
\[
 V_N\le qD_N,\qquad D_N\ge2^{q-1}N,\qquad
 \frac{V_N}{D_N^2}\le\frac{2q}{2^qN}
                    \le\frac{2}{2^qd}.              \tag{C1}
\]
Hence this explicit normalized contribution tends to zero along every such unbounded-size regime.
When q,d stay bounded, use the first bound as N grows; when either increases, use the second.
This is not an upper bound for the actual determinant valuations.
It identifies the additional contribution that a deeper joint Smith argument would need.

### Exact rational evaluation bypasses the series but retains denominators

Return to D_P of the first section and put M=d^2.
It is an integer polynomial of degree M, constant term one and leading coefficient one.
Indeed its roots arise from the complete pair spectrum of algebraic units, whose product is one; d is even, so M is even.
Galois invariance of that complete spectrum makes the algebraic-integer coefficients rational, hence integers.
Reciprocity makes the beta multiset inversion invariant and gives
\[
 D_P(x)=x^M D_P(x^{-1}).
\]
For relatively prime integers 0<a<b, set r=a/b and
\[
 Z(a,b)=b^M D_P(a/b)
       =\prod_{i,j}(b\alpha_j^2-a\alpha_i)
       =\operatorname{Norm}_{\mathbb Q(\alpha)/\mathbb Q}
                     \bigl(a^dP(b\alpha^2/a)\bigr).  \tag{C2}
\]
The homogeneous polynomial inside the norm has integer coefficients in alpha.
Every denominator in P(b alpha^2/a) is cancelled by a^d.
The product equality uses product_j alpha_j^{2d}=1.
Thus Z(a,b) is an integer.
It is nonzero: a rational zero of the monic constant-one D_P could only be 1 or -1, outside 0<r<1.
Moreover, for every prime p dividing b, its leading term gives Z(a,b)=a^M modulo p.
Thus gcd(Z(a,b),b)=1, and b^M is the exact reduced denominator, rather than only a clearing bound.

If a and b are odd, then
\[
 a^dP(bX^2/a)\equiv P(X^2)\equiv P(X)^2\pmod2.
\]
Its value at alpha lies in twice the ring of integers of Q(alpha).
Consequently
\[
 2^d\mid Z(a,b),\qquad
 \log|D_P(a/b)|\ge d\log2-d^2\log b.                 \tag{C3}
\]
This really preserves a dyadic income, while charging the entire rational evaluation denominator.
For 1-r<=c/d, b>=d/c; if a,b are odd the difference is at least two and b>=2d/c.
The displayed denominator price therefore exceeds the linear income in the relevant large-degree regime.
This says that (C3) does not supply the desired estimate; it is not an upper bound on the actual arithmetic income of Z.

Reciprocal compression does not reduce that price.
Write k=M/2 and
\[
 D_P(x)=x^kQ(x+x^{-1}),\qquad Q\in\mathbb Z[y],
 \quad\deg Q=k.
\]
The representation follows by pairing reciprocal coefficients and the recurrence for x^j+x^{-j}.
Since
\[
 r+r^{-1}=\frac{a^2+b^2}{ab},\qquad
 \gcd(a^2+b^2,ab)=1,
\]
its homogenized integer is exactly
\[
 (ab)^kQ((a^2+b^2)/(ab))=b^{2k}D_P(a/b)=Z(a,b).
                                                               \tag{C4}
\]
The apparent halving of polynomial degree produces no denominator saving.

For a fixed P put s=v_2(D_P(1)), which is finite by the original nonzero resultant.
If b is odd and v_2(a-b)>s, integrality of the coefficients gives
\[
 D_P(a/b)\equiv D_P(1)\pmod{2^{s+1}}
 \quad\hbox{in }\mathbb Z_2.
\]
It follows that v_2(Z(a,b))=s.
Thus making this rational evaluation arbitrarily close to one in the dyadic metric does not by itself accumulate additional valuation.
This is a fixed-input local statement, not a classification of different rational choices or of growing-prime income.

Exact evaluation also does not identify D_P(r) with the contracted quantity K_r.
Their exact difference is
\[
 \log|D_P(r)|-K_r
 =\sum_{|\beta_{ij}|>1}
   \log\left|\frac{1-r\beta_{ij}}
                    {1-r/\overline{\beta_{ij}}}\right|.          \tag{C5}
\]
At r=1 this becomes B, but no uniform small-measure control of (C5) at the degree scale has been supplied here.
For an actual positive Salem root alpha, D_P has a zero at alpha^{-3}.
Consequently continuing polynomial values beyond the raw disk cannot justify a termwise Taylor identity across the intervening real singularity.
Complex analytic continuation of a logarithm still requires its branch and the explicit correction (C5).

### Outcome and actual continuation boundary

The first test retains a finite contracted certificate at the d-scale and shows why the raw infinite trace substitution fails on the very near-zero domain it was meant to address.
The second identifies a finite genuine evaluation, the boundary cost and a descent obstruction for Boolean differences, while finding only a vanishing normalized explicit contribution.
The third supplies exact rational evaluation and reciprocal normalization formulas but no unpaid arithmetic gain.
The coordinate-kernel comparison separately removes the proposed cost-saving motivation for the particular new v10 chamber.

No original near-zero input class has been newly covered by a positive total-measure bound.
The remaining joint-evaluation question concerns additional Smith divisibility after the explicit factors, on actual nonzero minors of a fully specified descended integral module.
It would have to beat the complete complex-place bound for those same minors, preserve all row/window and original-degree costs, and apply to the needed near-zero inputs.
Independence alone does not guarantee an initial consecutive minor is nonzero.
The finite quartic control, a constant-factor gain or the already counted Boolean factors supplies no such bridge.
The finite signed quantity (A8) remains an alternative unresolved question; this comparison gives no evidence that its required bound is independently easier than the original gap.
