---
author: Yin
---

# Deep powered-polynomial congruence: degree and total Mahler costs

Human author Yin.
This project deduction gives the complete precision-budget argument, including the additional precision gained by repeated squaring.
The small-measure-inputs agent developed the original multilevel budget, its quantified consequences and the higher-depth Hankel comparison.
Root supplied the repeated-squaring refinement, which that agent checked and incorporated into the complete proof below.
Both are substantive proof contributors.
The selected decision below owns the assessment and exact independent review evidence.

## Statement

Let \(P\in\mathbb Z[t]\) be monic, irreducible, reciprocal and noncyclotomic, of degree \(d\ge2\) and constant term one.
Let \(\alpha_1,\ldots,\alpha_d\) be all its conjugate roots, and suppose every positive power of a root still has degree \(d\).
Set
\[
 Q_n(t)=\prod_{i=1}^d(t-\alpha_i^n),\qquad
 m=m(P)>0,\qquad
 \Delta=|\operatorname{disc}P|,\qquad
 D=d/\Delta^{1/d},\qquad
 I_n=[\mathbb Z[\alpha_1]:\mathbb Z[\alpha_1^n]].
\]
Thus \(m\) is the total logarithmic Mahler measure, and all degrees, norms and products use the original \(d\) conjugates.
Every \(I_n\) is a finite positive integer under the stated power-stability assumption.
The following conclusions hold.

**A. Simultaneous precision and index budget.**
If an integer \(L\ge1\) satisfies
\[
                         Q_2\equiv Q_4\pmod{2^L},                 \tag{1}
\]
then for all \(1\le r<s\),
\[
                 Q_{2^r}\equiv Q_{2^s}\pmod{2^{L+r-1}}.
\]
For every integer \(k\ge2\),
\[
 \left[L(k-1)+\frac{(k-1)(k-2)}3\right]\log2
 +\frac2{dk}\sum_{r=1}^k\log I_{2^r}
 \le
 \log(kD)+\left(4-\frac4{dk}\right)(2^k-1)m.                      \tag{2}
\]
In particular,
\[
                   L(k-1)\log2\le\log(kD)+4(2^k-1)m.             \tag{3}
\]
There is no squarefree-reduction, unramified-prime or irreducible-modulo-two hypothesis.
The same input and depth must satisfy all these inequalities simultaneously.

**B. A uniform gap for logarithmic-depth inputs.**
For each real \(c>0\), let \(k_c\) be the least integer \(k\ge2\) for which
\[
                              c(k-1)\ge2+\log_2 k.
\]
This integer exists.
If (1) holds with \(L\ge c\log_2d\), then
\[
                      m\ge\delta_c:=
                         \frac{\log2}{4(2^{k_c}-1)}>0.           \tag{4}
\]
For every fixed \(k\ge2\) with positive numerator, the same hypothesis gives the more precise lower bound
\[
             m\ge
              \frac{[c(k-1)-1]\log d-\log k}{4(2^k-1)}.           \tag{5}
\]
Consequently every sequence of the stated inputs with \(d_j\to\infty\), bounded \(m(P_j)\), and any valid depths \(L_j\) in (1) satisfies
\[
                               L_j/\log d_j\longrightarrow0.    \tag{6}
\]
In particular (6) holds on every hypothetical sequence with \(m(P_j)\to0\).
It also holds for the maximum coefficient congruence depth, which is finite.

**C. A joint measure/discriminant restriction.**
Under the congruence hypothesis (1), if \(0<m\le1/4\), put \(k=\lfloor\log_2(1/m)\rfloor\ge2\).
Then
\[
 \log D\ge
 \left[L(k-1)+\frac{(k-1)(k-2)}3\right]\log2-\log k-4.             \tag{7}
\]
The weaker but simpler consequence
\[
               \log D\ge
                 L\log(1/m)-2L\log2-\log k-4                    \tag{8}
\]
retains its explicit growing-\(L\) cost.
No rate of degree growth in terms of \(m\) is assumed, and these restrictions alone do not contradict a near-one sequence.

**D. The higher-depth version of the elementary Hankel comparison.**
Independently of (1), keep the exact input \(P\) above, put \(U=Q_2\), \(V=Q_4\), and let \(H=\max_i|\alpha_i|>1\).
Let \(q\) be an odd prime, \(\zeta\) a primitive \(q\)-th root of unity, \(K=\mathbb Q(\zeta)\), and \(O\) a full Galois orbit of a nonempty subset \(I\subseteq\mathbb Z/q\mathbb Z\).
For \(J\in O\), set
\[
 D_J(x)=\prod_{j\in J}U(\zeta^jx),\qquad
 N_J(x)=\prod_{j\in J}V(\zeta^jx),\qquad
 G_J=(N_J/D_J)^{1/2},
\]
where the square root has constant coefficient one.
Suppose every \(J\in O\) satisfies the global coefficient condition
\[
                      N_J-D_J\in2^\lambda\mathcal O_K[x],
                            \qquad\lambda\ge3.                 \tag{9}
\]
Here \(\lambda\) is an integer and is not presumed equal to the original congruence depth \(L\).
Put
\[
 a=\lambda-2,\qquad B=d|I||O|,\qquad
 f=\sum_{J\in O}G_J=\sum_{n\ge0}b_nx^n,\qquad
 \mathcal H_h=(b_{i+j+1})_{0\le i,j<h},\qquad
 \mathcal D_h=\det\mathcal H_h.
\]
The series \(f\) has integer coefficients and is nonrational.
For every \(h\ge1\),
\[
 \begin{split}
 v_2(\mathcal D_h)
 &\ge(a+1)h+a\sum_{r\ge1}\max(h-rB,0)\\
 &=(a+1)h+a\left(\ell h-\frac{B\ell(\ell+1)}2\right),
 \qquad \ell=\left\lfloor\frac{h-1}{B}\right\rfloor.              \tag{10}
 \end{split}
\]
The valuation of zero is infinity.
The original elementary disk estimate then gives
\[
               \log H\ge\frac{(\lambda-2)\log2}{8B},\qquad
               m\ge\frac{(\lambda-2)\log2}{8d|I||O|}.             \tag{11}
\]

**E. Scope of the inherited-precision comparison.**
If the depth in (9) is inherited only from (1), so that \(\lambda=L\ge3\), then on every hypothetical near-one sequence the lower-certificate value in (11) is at most
\[
                    \frac{L\log2}{8d}
                        =o\!\left(\frac{\log d}{d}\right)\to0.   \tag{12}
\]
A uniform positive value of this particular certificate would instead require \(\lambda-2\) to be bounded below by a positive multiple of \(B\).
The logarithmic original-depth class already has the uniform gap in B.
Thus raising only the original full-polynomial congruence depth cannot repair the degree loss of this elementary disk comparison on an uncovered near-one class.
This is a statement about the displayed certificate, not an upper bound for the actual Mahler measure or for every possible determinant method.
Mask-specific cancellation producing \(\lambda>L\), a smaller true approximation rank, and a different complex estimate remain outside this comparison.

## Exact dependencies and comparison scope

| Role | Input and exact use |
| --- | --- |
| Dependency | [C231 powered index and degree convention](Yin_C_G0231_v1.md#powered-order-index): every \(Q_n\) is the full original powered polynomial, and power stability gives its squarefreeness and the exact discriminant identity \(|\operatorname{disc}Q_n|=\Delta I_n^2\). |
| Dependency | [C231 mixed-power nonvanishing](Yin_C_G0231_v1.md#mixed-power-resultant-identities): distinct positive exponents have nonzero full cross resultants for a nonzero nontorsion input. |
| Dependency and established-mechanism attribution | [C219 direct finite Vandermonde proof](Yin_C_G0219_v1.md#finite-prime-discriminant-gap) identifies the already retained Mat96 determinant mechanism; all finite Vandermonde/Hadamard steps used here are explicitly given below. Its [discriminant escape](Yin_C_G0219_v1.md#discriminant-escape) supplies \(D\to\infty\), hence \(d\to\infty\), on a hypothetical vanishing-measure power-stable sequence. |
| Dependency | [C858 all-place series and rank comparison](Yin_C_G0858_v1.md#all-place-hankel-budget), together with its [Cauchy-radius argument](Yin_C_G0858_v1.md#cauchy-radius-cost): integrality and nonrationality of the same trace series under the weaker depth-three hypothesis, the finite elementary-divisor/rank implication, infinitely many nonzero shifted leading determinants, and the exact original holomorphic radius. The higher-depth truncation and level count are proved below. |
| Comparison only | [C232 multilevel certificates](Yin_C_G0232_v2.md#statement): related finite multilevel notation and the distinct floor-only optimization problem. No optimization theorem or mathematical assessment of that family is a premise of this proof. |
| Comparison only | [C857 large-period full-mask construction](Yin_C_G0857_v1.md#large-period-full-mask): arbitrary prescribed finite precision is available on certain large-measure inputs; this supplies no near-one instance of (1) or (9). |
| Task reduction only | [C231 existence descent](Yin_C_G0231_v1.md#all-positive-power-existence-descent): a hypothetical unrestricted vanishing sequence may be reduced to the power-stable reciprocal core, without preserving the original polynomial, residue data or discriminant. All conditions in this Claim must then be checked on the same reduced input. |

No new external source theorem, native computation, numerical certification, or original-source proof audit is used.
The inherited source-inspection limits of C219 and C858 are unchanged.
All direct dependencies are fixed materials; the original Draft is not part of the logical chain.

<a id="argument"></a>
## Complete argument

<a id="squaring-precision-gain"></a>
### Repeated squaring gains one coefficient digit at each step

For a monic degree-\(d\) polynomial \(A\), let \(\mathcal P_2(A)\) denote the monic polynomial whose roots are the squares of all its roots, with multiplicities.
With an auxiliary variable \(s\),
\[
              \mathcal P_2(A)(s^2)=(-1)^d A(s)A(-s).              \tag{13}
\]
Indeed the right side is \(\prod_i(s^2-\beta_i^2)\) when \(A(s)=\prod_i(s-\beta_i)\).
It belongs to \(\mathbb Z[s^2]\) when \(A\in\mathbb Z[t]\), so no division by two is involved in reading its coefficients as a polynomial in \(s^2\).

If monic degree-\(d\) polynomials satisfy \(A=R+2^vE\) with integer \(v\ge1\) and \(E\in\mathbb Z[t]\), then
\[
 A(s)A(-s)-R(s)R(-s)
 =2^v\{E(s)R(-s)+R(s)E(-s)\}
       +2^{2v}E(s)E(-s).                                      \tag{14}
\]
Writing \(F(s)=E(s)R(-s)\), the bracket is \(F(s)+F(-s)\), which belongs to \(2\mathbb Z[s^2]\).
The remaining product belongs to \(\mathbb Z[s^2]\), and \(2v\ge v+1\).
After the common sign in (13), this proves
\[
             A\equiv R\pmod{2^v}
             \quad\Longrightarrow\quad
             \mathcal P_2(A)\equiv\mathcal P_2(R)\pmod{2^{v+1}}.  \tag{15}
\]
This elementary coefficient identity needs no separability or local-field hypothesis.

Starting from \(Q_2\equiv Q_4\pmod{2^L}\), induction gives
\[
                 Q_{2^r}\equiv Q_{2^{r+1}}
                              \pmod{2^{L+r-1}}\qquad(r\ge1).
\]
Summing consecutive differences proves the asserted congruence for every \(r<s\), since the later differences have at least the first difference's precision.
This is the actual source of the extra term in (2).

<a id="multilevel-precision-budget"></a>
### Complete finite Vandermonde comparison

Power stability makes every \(Q_{2^r}\) monic, integral and squarefree of degree \(d\).
Its total Mahler logarithm is \(2^r m\), since
\(\log^+|\alpha_i^{2^r}|=2^r\log^+|\alpha_i|\) at every original root.
C231 gives
\[
                    |\operatorname{disc}Q_{2^r}|=\Delta I_{2^r}^2.
\]
For \(r<s\), write \(Q_{2^s}=Q_{2^r}+2^{L+r-1}E_{r,s}\) with integral \(E_{r,s}\).
Evaluation at the \(d\) roots of \(Q_{2^r}\) gives the integer divisibility
\[
                 2^{d(L+r-1)}
                     \mid\operatorname{Res}(Q_{2^r},Q_{2^s}).   \tag{16}
\]
Explicitly the resultant equals \(2^{d(L+r-1)}\operatorname{Res}(Q_{2^r},E_{r,s})\).
The full cross-exponent nonvanishing in C231 ensures these integers are nonzero.
Together with within-level squarefreeness, this shows that all \(kd\) nodes in the levels \(2,4,\ldots,2^k\) are distinct.

Let \(W\) be their Vandermonde matrix, with columns indexed by zero through \(kd-1\).
Its determinant product yields exactly
\[
 |\det W|^2
 =\left(\prod_{r=1}^k|\operatorname{disc}Q_{2^r}|\right)
  \left(\prod_{1\le r<s\le k}
         |\operatorname{Res}(Q_{2^r},Q_{2^s})|^2\right).
\]
The discriminant and resultant lower bounds therefore give
\[
 |\det W|^2\ge
 \Delta^k\left(\prod_{r=1}^k I_{2^r}^2\right)
 2^{\,2d\sum_{r=1}^{k-1}(k-r)(L+r-1)}.                          \tag{17}
\]
The elementary finite sums are
\[
 \sum_{r=1}^{k-1}(k-r)=\frac{k(k-1)}2,\qquad
 \sum_{r=1}^{k-1}(k-r)(r-1)=\frac{k(k-1)(k-2)}6.                 \tag{18}
\]

For a row with node \(\beta\), its squared Euclidean norm is
\[
 \sum_{j=0}^{kd-1}|\beta|^{2j}
       \le kd\max(1,|\beta|)^{2(kd-1)}.
\]
Hadamard's inequality, applied to these actual rows, gives
\[
 |\det W|^2
 \le(kd)^{kd}
     \exp\left(2(kd-1)\sum_{r=1}^k2^r m\right)
 =(kd)^{kd}\exp\left(2(kd-1)(2^{k+1}-2)m\right).                \tag{19}
\]
Taking logarithms of (17)--(19), dividing by \(dk\), inserting (18), and moving
\(\log\Delta/d\) to the right proves (2).
The radial coefficient is
\(2(kd-1)(2^{k+1}-2)/(dk)=(4-4/(dk))(2^k-1)\).
All index terms and the additional precision term are nonnegative, so dropping them and increasing that coefficient to four proves (3).
At \(k=2\), the extra precision term vanishes and the sharper index-free bound is
\[
                          L\log2\le\log(2D)+(12-6/d)m.          \tag{20}
\]
The higher-depth income in (17) is counted through disjoint pair-resultant factors of one determinant.
No prime-power ratio has been substituted for a valuation, and no discarded surplus is upper-bounded.

<a id="logarithmic-depth-gap"></a>
### Quantified gap and near-one consequences

Since \(\Delta\) is a nonzero integer, \(D\le d\).
Under \(L\ge c\log_2d\), inequality (3) consequently gives
\[
              4(2^k-1)m\ge[c(k-1)-1]\log d-\log k.              \tag{21}
\]
The integer \(k_c\) in B exists because \(c(k-1)-\log_2k\to\infty\).
For \(k=k_c\) and \(d\ge2\), the right side of (21) is at least
\[
            [1+\log_2k_c]\log2-\log k_c=\log2,
\]
which proves (4).
Keeping the right side unchanged proves (5).

Now let \(d_j\to\infty\) while \(m_j\) remains bounded.
For each \(c>0\), choose a fixed \(k\ge2\) with \(c(k-1)>1\).
If \(L_j\ge c\log_2d_j\) along an infinite subsequence, (21) forces \(m_j\to\infty\) along that subsequence, a contradiction.
Thus eventually \(L_j<c\log_2d_j\) for every \(c>0\), proving (6).
For a sequence with \(m_j\to0\), the applicable C219 discriminant-escape theorem gives \(D_j\to\infty\) and hence \(d_j\to\infty\), so the preceding argument applies.
Alternatively the uniform constants (4), for every \(c>0\), directly exclude those logarithmic-depth subsequences.
The maximum depth of \(Q_2-Q_4\) is finite because this difference is nonzero: equality would contradict C231's cross-exponent nonvanishing.
All valid smaller depths obey the same bounds.

For C, \(k=\lfloor\log_2(1/m)\rfloor\ge2\) gives \(2^km\le1\), so the rightmost radial term in (2) is at most four.
Dropping only the index term and rearranging proves (7).
Also \(k-1\ge\log_2(1/m)-2\).
Dropping the nonnegative quadratic precision term from (7) and applying this inequality proves (8).
The remainder \(2L\log2\) is explicitly retained when \(L\) grows.
No exchange between a fixed-input limit and a growing-degree limit appears in these deductions.

<a id="higher-depth-hankel-comparison"></a>
### Rational approximation at every precision level

For a reciprocal degree-\(d\) unit polynomial with constant term one, inversion permutes its roots and their product is one.
Consequently
\[
              Q_n(x)=\prod_i(1-\alpha_i^n x),
\]
so D uses exactly the C858 radicands and original analytic radius.
Condition (9), with \(\lambda\ge3\), implies C858's depth-three hypothesis.
That Claim therefore supplies the integrality and nonrationality of the same series \(f\), its holomorphy on \(|x|<H^{-4}\), and infinitely many nonzero shifted leading Hankel determinants.
These input facts are not transferred to a different trace or mask.

For the changed precision bound, write \(A_J=(N_J-D_J)/2^\lambda\).
Then \(A_J\in\mathcal O_K[x]\), \(A_J(0)=0\), and
\[
              G_J=(1+2^\lambda A_J/D_J)^{1/2}.
\]
For \(n\ge1\), the exact binomial valuation is
\[
 v_2\left(2^{\lambda n}\binom{1/2}{n}\right)
       =(\lambda-1)n-v_2(n!)
       =(\lambda-2)n+s_2(n)
       =an+s_2(n)\ge an+1,                                    \tag{22}
\]
where \(s_2(n)\) is the number of ones in the binary expansion of \(n\).
The factorial identity follows by summing \(\lfloor n/2^j\rfloor\), or directly from the binary expansion.
The valuations in (22) concern rational coefficients and hence hold simultaneously at every prime above two.

For each integer \(s\ge1\), put
\[
                   r_s=\max\left(0,\left\lfloor\frac{s-2}{a}\right\rfloor\right),
                   \qquad b_s=Br_s.
\]
Truncate each binomial expansion after \(n=r_s\).
If \(r_s=0\), the same valuation bound shows that the omitted terms vanish modulo \(2^s\); otherwise every omitted \(n\ge r_s+1\) satisfies \(an+1\ge s\).
Each truncation has denominator \(D_J^{r_s}\), with numerator and denominator degrees at most \(r_s\deg D_J\).
The common product denominator over \(J\in O\) has degree at most \(b_s\) and constant term one.
Because the orbit is full and the truncation rule is common, its coefficients and the summed numerator are Galois invariant and algebraic integral, hence in \(\mathbb Z\).
The same all-place congruence descends to
\[
              f-R_s\in2^s\mathbb Z[[x]],\qquad
              R_s=A_s/Q_s,\quad
              \deg A_s,\deg Q_s\le b_s,\quad Q_s(0)=1.           \tag{23}
\]
In particular \(R_s\) has integer formal coefficients.

The shifted rational series \((R_s-R_s(0))/x\) has numerator degree less than \(b_s\) and denominator degree at most \(b_s\).
Its coefficient recurrence makes its finite shifted Hankel matrices have rank at most \(b_s\) over \(\mathbb Q_2\).
When \(b_s=0\), the shifted series is zero.
Thus the original \(\mathcal H_h\) is congruent modulo \(2^s\) to an integral matrix of rank at most \(b_s\).
The finite elementary-divisor argument proved in C858 then gives
\[
                 v_2(\mathcal D_h)\ge\sum_{s\ge1}\max(h-b_s,0).  \tag{24}
\]
There are \(a+1\) initial indices \(s=1,\ldots,a+1\) with \(b_s=0\).
For each positive \(r\), exactly \(a\) subsequent indices have \(b_s=rB\).
This proves the first formula in (10).
Only \(1\le r\le\ell=\lfloor(h-1)/B\rfloor\) contribute positive terms, so the finite arithmetic sum proves its second formula.
For fixed input and masks, its quadratic coefficient as \(h\to\infty\) is \(a/(2B)\).

<a id="higher-depth-disk-cost"></a>
### The original complex cost and the inherited-precision restriction

Fix \(0<\rho<H^{-4}\) and put \(M_\rho=\max_{|x|=\rho}|f(x)|\).
The original Cauchy estimate gives \(|b_n|\le M_\rho\rho^{-n}\).
Factoring \(\rho^{-i}\) from row \(i\) and \(\rho^{-(j+1)}\) from column \(j\), and applying Hadamard to the remaining matrix, gives
\[
              \log|\mathcal D_h|
                   \le-h^2\log\rho+h\log M_\rho+\frac h2\log h  \tag{25}
\]
whenever \(\mathcal D_h\ne0\).
These determinants are integers, so (10) gives
\(\log|\mathcal D_h|\ge v_2(\mathcal D_h)\log2\).
Along their infinitely many nonzero indices, divide both bounds by \(h^2\), let \(h\to\infty\), and then let \(\rho\) increase to \(H^{-4}\).
The result is
\[
                             \frac{a\log2}{2B}\le4\log H.
\]
Since \(\log H\le m\), this proves (11).
The input, orbit and radius are fixed before the Hankel-size limit, and the original total Mahler normalization is unchanged.

If (9) is obtained merely by substituting \(\zeta^jx\) into (1) and multiplying the resulting congruences, it is valid with \(\lambda=L\).
A product may have a still higher actual precision, but that is a separate arithmetic fact, not supplied by this inherited argument.
When \(\lambda=L\), \(B=d|I||O|\ge d\) and (6) give
\[
        \frac{(L-2)\log2}{8B}\le\frac{L\log2}{8d}
                           =o\left(\frac{\log d}{d}\right)\to0
\]
on a hypothetical near-one sequence, proving (12).
If the displayed lower-certificate values were bounded below by \(\eta>0\), one would instead need
\(\lambda-2\ge8\eta B/\log2\).
For inherited precision this lies far beyond the logarithmic original-depth class already covered by (4).
The conclusion concerns this particular all-place rank and elementary disk assembly.
It neither estimates the best possible mask depth nor rules out another analytic or rank mechanism.

## Limits and operation scope

The actual new retained result is the repeated-squaring precision budget and its uniform logarithmic-depth consequence, together with the exact higher-depth comparison for the same C858 construction.
The complete finite argument is included here; no conclusion from C232's separate optimization problem is invoked.
C857's high-precision examples are a comparison outside the small-measure range, not evidence for near-one supply.
No original input is replaced after a congruence, index or mask condition has been imposed.

Ordinary author checking covered the sign in (13), the integral even-coefficient gain in (14), the weighted pair count (18), all original-root and norm factors in (17)--(19), the fixed-\(c\) constant, the growing-\(L\) remainder, all-place rational descent, the \(a+1\) initial rank-zero levels, and the original order of analytic limits.
This is an account of proof development, not a formal review finding.
The theorem supplies no unrestricted input-coverage statement, near-one family, or resolution of the unrestricted Lehmer Task.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T17:12 |
| status | proved |
| reason | Adopt the complete original-powered precision budget, logarithmic-depth family gap, bounded-measure precision restriction and higher-depth Hankel comparison after independent R1076. Original depth and additional mask-specific depth remain distinct; no unrestricted near-one coverage or G0001 completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E with original total measure, all-power stability, supplied global congruences, all k and c quantifiers, exact constants and certificate boundaries. |
| argument | [Complete argument](#argument) | All repeated-squaring, full Vandermonde/index/Hadamard, quantified asymptotic, rational descent and disk-comparison steps. |
| dependency | [Original powered orders](Yin_C_G0231_v1.md#powered-order-index) | Exact same-degree order-index and discriminant identity for each selected power. |
| dependency | [Mixed-power nonvanishing](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Nonzero resultants and distinct powered roots at the supplied original input. |
| dependency | [Discriminant escape](Yin_C_G0219_v1.md#discriminant-escape) | Only the accepted implication that a power-stable vanishing-positive-measure sequence has D and hence d tending to infinity. |
| dependency | [Original Hankel interface](Yin_C_G0858_v1.md#all-place-hankel-budget) | Same trace nonrationality, elementary-divisor count and exact shifted Kronecker convention, with the selected source-inspection limits. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1076_v1.md#precision-budget-whole) | Whole A--E statement, argument and direct interfaces, with actual source/native and unrestricted-Task limits. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
