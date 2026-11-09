---
author: Yin
---

# Whole odd-grid prefix bounds and compatible cut lengths

<a id="scope"></a>
## Scope and relation to the previous versions

This version gives a project deduction for the full odd cyclotomic grid \(b_j=2\cos(2\pi j/p)\).
The grid is different from the original Chebyshev grid in [v2](Yin_C_G0881_v2.md#statement).
The reverse implication here bounds the entire Mahler measure from an exact prefix; it does not transfer v2's finite rigidity statement or selected assessment to this new grid or rational profile.
All proofs needed for this new analytic implication are supplied below.
The [selected assessment](#decision-odd-grid-prefix) adopts these implications after complete independent review, leaving actual integer supply unresolved.

<a id="statement"></a>
## Prefix upper bound, positive cut constraint and fixed real obstruction

Use the [real input domain](#original-domain), with \(p=2n+1\) odd, \(n\ge2\), \(x\in\{-2,-1,0,1,2\}\), a strict terminal negative block of size \(1\le\kappa<n\), and the strict left endpoint condition (2).
For every integer \(2\le L\le n+1<p\), agreement through coefficient index \(L\) with
\[
                    P_{*,x}(z)=\frac{(1-xz+z^2)^2}{(1-z)^2(1+z)}
\]
is equivalent to the affine coordinate conditions (6).
Under that agreement, the complete polynomial, with all factors and multiplicities retained, satisfies
\[
 1\le M(P)\le
 \bigl(8\lfloor L/2\rfloor+8\bigr)^{2/\lfloor L/2\rfloor}.
\]
This statement includes real and nonreal residual quadratic roots and requires no prior upper bound on \(M(P)\).

For \(x=0\), independently of the endpoint condition, the strict single-cut signs and the same coordinate prefix imply, for every integer \(m\ge2\) with \(2m+3\le L\),
\[
 2+c<
 \frac{8m-4}{(8m^3+24m^2+4m+6)/3}
\]
for every separator \(b_{n-\kappa+1}<c<b_{n-\kappa}\).
Thus along any such inputs with \(L\to\infty\) the angular-midpoint separator satisfies \((2+c)L^2\le12+o(1)\).
If also \(\kappa/p\to0\), then \(\limsup \kappa L/p\le\sqrt3/\pi\).

At \(p=401,\ n=200,\ \kappa=3,\ x=0\), no real coefficient input has the strict cut signs and this prefix through any index \(L\) with \(83\le L\le201\).
In particular the proposed length \(L=140\), which would imply \(M(P)<6/5\), is infeasible already over the reals.
The endpoint condition, integrality and any resultant budget are unnecessary for this obstruction.

<a id="original-domain"></a>
## Original input and multiplicities

Let \(p=2n+1\) be odd, \(n\ge2\), fix \(x\in\{-2,-1,0,1,2\}\), and take the full decreasing grid
\[
 b_j=2\cos(2\pi j/p),\qquad
 B=B_n=E_n+E_{n-1},\qquad D=B_{n-1},
\]
where \(E_{-1}=0,E_0=1,E_1=t,E_{i+1}=tE_i-E_{i-1}\), and \(B_m=E_m+E_{m-1}\) for \(m\ge0\), so \(B_0=1\).
Let
\[
 h=\sum_{i=0}^{n-1}a_iE_i\in\mathbb R[t],\qquad
 C=Dh\bmod B,\qquad Q=(t-2x)B+C,\qquad
 P(z)=z^{n+1}Q(z+z^{-1}).                                  \tag{1}
\]
The coefficients of \(P\) are real; when all \(a_i\) are integers, \(P\) is a monic integer polynomial with constant coefficient one.
Use \(\nu_j=(4-b_j^2)/p\) and \(r_j=\nu_jh(b_j)\).
Assume that the first \(n-\kappa\) residues are strictly positive and the last \(\kappa\) strictly negative, where \(1\le\kappa<n\), and require
\[
                          Q(-2)/B(-2)<0.                  \tag{2}
\]
Since \(B(-2)=(-1)^n\) and \(P(-1)=(-1)^{n+1}Q(-2)\), (2) is equivalent to \(P(-1)>0\).
All original multiplicities are retained.

The trigonometric identity
\[
 B_n(2\cos\theta)=\frac{\sin(p\theta/2)}{\sin(\theta/2)}
\]
and differentiation at its roots give \(D(b_j)/B'(b_j)=(4-b_j^2)/p\).
Partial fractions therefore yield
\[
                  Q(t)/B(t)=t-2x+\sum_j\frac{r_j}{t-b_j}.
\]
On every same-sign gap the two one-sided pole limits have opposite signs, so at least one root lies in that gap.
There are \(n-2\) such gaps.
Since \(r_n<0\), the limit of \(Q/B\) at \(b_n\) from the left is positive infinity.
Together with (2), this gives a further root between \(-2\) and \(b_n\).
This is the general same-sign-gap mechanism also used in [L464v1](../ledger/Yin_L_G0464_v1.md#positive-resolvent).
There are \(n-1\) such disjoint intervals and hence \(n-1\) distinct chosen roots \(u_i\) in \((-2,2)\).
Remove one copy of each chosen root from \(Q\).
The remaining factor is a real monic quadratic with roots \(v_1,v_2\), including multiplicity.
It has either two real roots or one nonreal conjugate pair.
Its roots may coincide with each other or with a chosen root, but the removal does not discard that remaining multiplicity.

For each \(v_i\), choose a root \(\lambda_i\) of \(z^2-v_i z+1\) with modulus \(\rho_i\ge1\).
All chosen \(u_i\) lift to the unit circle.
Therefore the complete original measure is
\[
                               M(P)=\rho_1\rho_2.          \tag{3}
\]
No nonreal assumption is made in (3).

<a id="prefix-coordinates"></a>
## Exact affine coordinates for the five integer profiles

Set
\[
 P_{*,x}(z)=\frac{(1-xz+z^2)^2}{(1-z)^2(1+z)}.
\]
For an integer \(L\) satisfying
\[
                              2\le L\le n+1<p,             \tag{4}
\]
prefix agreement means \(P-P_{*,x}=O(z^{L+1})\) at zero.
This includes coefficients indexed from zero through \(L\).

The recurrence implies
\[
                 E_iD\bmod B=B_{n-i-1}\qquad(0\le i<n).
\]
For \(i=0\) this is \(D=B_{n-1}\), and for \(i=1\) it follows from \(tB_{n-1}=B_n+B_{n-2}\).
Applying the recurrence gives the remaining indices through \(i=n-1\), where the remainder is \(B_0=1\).
No value of \(B_{-1}\) is used.
Consequently
\[
 C=\sum_{i=0}^{n-1}a_iB_{n-i-1},
\]
and the full odd-grid lift gives the exact polynomial identity
\[
 (1-z)P=(1-2xz+z^2)(1-z^p)
              +\sum_{i=0}^{n-1}a_i(z^{i+2}-z^{p-i}).        \tag{5}
\]
The first reflected tail exponent is \(n+2\), and the baseline correction begins at \(p\).
Both lie beyond the range in (4).
Since
\[
 (1-z)P_{*,x}=\frac{(1-xz+z^2)^2}{1-z^2}
 =1-2xz+(x^2+3)z^2-4xz^3+(x^2+4)z^4-4xz^5+\cdots,
\]
the prefix condition is exactly
\[
 a_0=x^2+2,\qquad
 a_i=-4x\ \text{for odd }i,\qquad
 a_i=x^2+4\ \text{for even }i\ge2,
                    \qquad 0\le i\le L-2.                 \tag{6}
\]
All later coefficients remain free reals in the analytic statement, or free integers when integrality is required.
In particular \(a_1=-4x\) when \(L\ge3\), and \(a_2=x^2+4\) when \(L\ge4\).
In the affine moment notation \(K=a_0,\ N=K+a_2\), matching through index 4 requires \(N=2x^2+6\).
Thus \(x=0\) requires \(N=6\), and \(x=-1\) requires \(N=8\).
An \(x=-1,\ N=7\) input does not have this length-4 prefix.

<a id="newton-baseline"></a>
## The baseline Newton sums require \(j<p\)

For a monic reciprocal polynomial with constant coefficient one, write \(s_j(P)\) for the sum of the \(j\)-th powers of all roots, including multiplicity.
The low-order formal logarithm gives
\[
                  s_j(P)=-j[z^j]\log P(z).
\]
Thus prefix agreement determines these sums for \(1\le j\le L\).
Let \(T_j\) denote the trace Chebyshev polynomial,
\(T_j(z+z^{-1})=z^j+z^{-j}\).
The two reciprocal roots associated with \(1-xz+z^2\) have trace \(x\).
The numerator and denominator of \(P_{*,x}\) therefore give
\[
                    s_j(P)=2T_j(x)-2-(-1)^j.              \tag{7}
\]
For every \(x\in\{-2,-1,0,1,2\}\), one has \(|T_j(x)|\le2\).
This also follows immediately by writing \(x=2\cos\theta\).
The full lift \(z^nB(z+z^{-1})=(1-z^p)/(1-z)\) has precisely the nontrivial \(p\)-th roots of unity.
For \(1\le j<p\), their \(j\)-th power sum is \(-1\), even when \(p\) is composite.
This restriction matters: at a positive multiple of \(p\) the sum is \(p-1\).
Using (4), the trace difference therefore satisfies
\[
 \mathcal D(T_j):=\sum_{Q(q)=0}T_j(q)-\sum_{\ell=1}^nT_j(b_\ell)
                  =s_j(P)+1=2T_j(x)-1-(-1)^j,
                       \qquad 1\le j\le L.                \tag{8}
\]
In particular \(|\mathcal D(T_j)|\le6\).
There is no omitted factor of two: each trace root contributes exactly the two reciprocal powers \(T_j(q)\).

<a id="paired-variation"></a>
## Disjoint intervals remove the degree cost

Match each chosen root \(u_i\) to the right pole of its interval, including the root in the left endpoint interval.
These \(n-1\) poles are distinct.
Exactly one pole \(b_*\), the smallest pole with positive residue, remains unpaired.
The matching intervals have disjoint interiors and lie in \([-2,2]\).

For any real polynomial \(f\),
\[
 \mathcal D(f)=
       \sum_{\text{matched }(u,b)}(f(u)-f(b))
             +f(v_1)+f(v_2)-f(b_*).
\]
Hence
\[
 |f(v_1)+f(v_2)|
 \le|\mathcal D(f)|+|f(b_*)|
                    +\operatorname{Var}_{[-2,2]}(f).       \tag{9}
\]
The variation term bounds the sum over all matched intervals at once.
It is not multiplied by their number.

For \(f=T_j\), one has \(|T_j(b_*)|\le2\) and
\[
 \operatorname{Var}_{[-2,2]}(T_j)
     =\int_0^\pi 2j|\sin(j\theta)|\,d\theta=4j.
\]
Combining (8)--(9) yields the degree-independent bound
\[
                |T_j(v_1)+T_j(v_2)|\le4j+8,
                         \qquad 1\le j\le L.              \tag{10}
\]

<a id="whole-measure-upper"></a>
## A uniform upper bound for both exceptional-root types

Put \(q=\lfloor L/2\rfloor\ge1\).

If \(v_1,v_2\) are nonreal, they are conjugate.
Their exterior lifts may be written \(\rho e^{\mathrm i\theta}\) and \(\rho e^{-\mathrm i\theta}\), with \(\rho>1\), and
\[
 T_j(v_1)+T_j(v_2)
       =2(\rho^j+\rho^{-j})\cos(j\theta),\qquad M(P)=\rho^2.
\]
At least one of \(|\cos(q\theta)|\) and \(|\cos(2q\theta)|\) is at least \(1/2\).
Indeed, if the first is smaller, \(\cos(2q\theta)=2\cos^2(q\theta)-1<-1/2\).
For the corresponding \(j\in\{q,2q\}\), (10) gives
\[
                  \rho^j+\rho^{-j}\le4j+8\le8q+8.
\]
As \(j\ge q\),
\[
                              M(P)\le(8q+8)^{2/q}.         \tag{11}
\]

If \(v_1,v_2\) are real, let \(\rho=\max(\rho_1,\rho_2)\).
If \(\rho=1\), the measure is one.
Otherwise at least one trace is outside \([-2,2]\), and at the even frequency \(2q\) its Chebyshev value is at least \(\rho^{2q}\).
The other real trace has Chebyshev value at least \(-2\) when it lies in \([-2,2]\), and at least \(2\) otherwise.
Thus (10) implies
\[
                 \rho^{2q}\le8q+10,\qquad
                 M(P)\le\rho^2\le(8q+10)^{1/q}.            \tag{12}
\]
Since \(8q+10\le(8q+8)^2\), the same bound (11) covers this case too.
The argument includes repeated real roots and coincident chosen and remaining roots.

Therefore every input satisfying (1)--(6) obeys
\[
 \boxed{\quad
 1\le M(P)\le
 \bigl(8\lfloor L/2\rfloor+8\bigr)^{\,2/\lfloor L/2\rfloor}.
 \quad}                                                    \tag{13}
\]
No prior bounded-measure assumption or degree-dependent error term is used.
In particular, along actual noncyclotomic integer inputs with \(L\to\infty\), the complete measure satisfies
\[
                   0<\log M(P)=O(\log L/L)\longrightarrow0.
\]
The conditional existence of those inputs remains the arithmetic problem.

<a id="prefix-cut-compatibility"></a>
## A positive test bounds the compatible prefix length

For this section and the two following sections, specialize to \(x=0\).
Let \(d\alpha(t)=dt/(\pi\sqrt{4-t^2})\) on \((-2,2)\).
For the exact prefix coordinates (6), orthogonality on the full odd grid gives
\[
 \sum_jr_j f(b_j)=\int_{-2}^2 t^2 f(t)\,d\alpha(t)
                       \quad(\deg f\le L-2).              \tag{14}
\]
To verify this, it suffices to use \(f=E_i\).
The right side equals 2 for \(i=0\), zero for odd \(i\), and 4 for positive even \(i\).
The latter identities follow directly from
\(E_{2r}(2\cos\theta)=1+2\sum_{\ell=1}^r\cos(2\ell\theta)\)
and \(t^2=2+2\cos(2\theta)\).
For completeness the required discrete orthogonality holds for every odd \(p\), including composite \(p\).
Put \(\theta_\ell=2\pi\ell/p\).
For \(0\le s\le2n-2=p-3\), doubling the half grid and using the sine formula for \(E_s\) gives
\[
 \sum_{j=1}^n\nu_jE_s(b_j)
 =\frac1p\sum_{\ell=0}^{p-1}
       \bigl(\cos(s\theta_\ell)-\cos((s+2)\theta_\ell)\bigr)
 =\begin{cases}1,&s=0,\\0,&1\le s\le2n-2.\end{cases}
\]
The term at \(\ell=0\) is zero before separating the two cosines.
No nonzero frequency in this range is a multiple of \(p\).
Using the polynomial product identity
\[
          E_iE_j=\sum_{r=0}^{\min(i,j)}E_{i+j-2r}
                    \quad(0\le i,j<n)
\]
therefore proves \(\sum_\ell\nu_\ell E_i(b_\ell)E_j(b_\ell)=\delta_{ij}\).
This quadrature identity itself depends only on the grid and holds for every choice of the profile parameter \(x\).
Consequently the left side of (14), for \(f=E_i\), equals \(a_i\).
The range \(L-2\le n-1\) is ensured by (4).
This supplies the general-conductor argument directly, without extrapolating the fixed-conductor chart in [L462v9](../ledger/Yin_L_G0462_v9.md#affine-moments).

Take any separator \(c\) in the strict sign gap, so \((b_j-c)r_j>0\).
For an integer \(m\ge2\), define the integer polynomial
\[
 g_m(t)=m+1+\sum_{i=1}^m(m+1-i)(-1)^iT_i(t).                \tag{15}
\]
If \(L\ge2m+3\), then (14) applies to \((t-c)g_m(t)^2\), and positivity requires
\[
 0<\sum_j(b_j-c)r_jg_m(b_j)^2
     =\mathcal A_m-(2+c)\mathcal B_m,                       \tag{16}
\]
where
\[
 \mathcal B_m=\int t^2g_m(t)^2\,d\alpha(t),\qquad
 \mathcal A_m=\int (t+2)t^2g_m(t)^2\,d\alpha(t).
\]
The sum is strictly positive because \(g_m\) has degree \(m<n\) and cannot vanish at all \(n\) distinct nodes.

Both constants have simple finite-sum formulas:
\[
 \boxed{\qquad
 \mathcal A_m=8m-4,\qquad
 \mathcal B_m=\frac{8m^3+24m^2+4m+6}{3}.
 \qquad}                                                   \tag{17}
\]
For a direct derivation, put \(z=e^{\mathrm i\theta}\).
The Laurent coefficients of \(g_m(z+z^{-1})\) are
\((-1)^r(m+1-|r|)\) for \(|r|\le m\).
Let
\[
 C_j=\sum_{r\in\mathbb Z}
        (m+1-|r|)_+(m+1-|r-j|)_+,
\]
where \(x_+=\max(x,0)\).
The coefficient of \(z^j\) in \(g_m^2\) is \((-1)^jC_j\).
Summing the integer arithmetic progressions gives
\[
 C_0=\frac{(m+1)(2m^2+4m+3)}3,\qquad
 C_j=C_0-(m+1)j^2+\frac{j^3-j}{2}
                  \quad(j=1,2,3;\ m\ge2).
\]
Arcsine integration is the constant Laurent coefficient.
Thus
\[
 \mathcal B_m=2(C_0+C_2),\qquad
 \mathcal A_m=4C_0-6C_1+4C_2-2C_3,
\]
which proves (17).

Consequently every compatible input with \(L\ge2m+3\) must satisfy the exact necessary condition
\[
                2+c<\frac{8m-4}{(8m^3+24m^2+4m+6)/3}
                            \sim\frac3{m^2}.               \tag{18}
\]
This uses real positivity alone, so an integer search cannot overcome its failure.

<a id="fixed-compatibility-test"></a>
## The proposed conductor-401 test is already impossible over the reals

The proposed first upper-measure target used
\[
                  p=401,\quad n=200,\quad \kappa=3,
                  \quad x=0,\quad L=140.
\]
If it had an actual strict input, (13), with \(q=70\), would give
\[
                    M(P)\le568^{1/35}<6/5.
\]
The last inequality is an exact integer comparison:
\[
                 6^{35}-568\cdot5^{35}
                      =65973229805948225794283176>0.
\]
This attractive upper bound does not establish compatibility of the prefix and cut.

Take \(c=-799/400\).
It lies strictly between \(b_{198}\) and \(b_{197}\).
For an elementary check, \(b_{197}=-2\cos(7\pi/401)\), \(b_{198}=-2\cos(5\pi/401)\), and the usual bounds \(3<\pi<22/7\) give
\[
 \cos(7\pi/401)
  <1-\frac12(21/401)^2+\frac1{24}(21/401)^4
  <799/800,
\]
\[
 \cos(5\pi/401)>1-\frac12(110/2807)^2>799/800.
\]
All remaining comparisons are rational.

Already \(m=40\), requiring only \(L\ge83\), gives from (17)
\[
                  \mathcal B_{40}=183522,\qquad
                  \mathcal A_{40}=316.
\]
But \(2+c=1/400\), so (16) would read
\[
                   0<316-\frac{183522}{400}
                        =-\frac{28561}{200}<0.             \tag{19}
\]
This contradiction rules out every real coefficient vector with the stated strict signs and prefix length at least 83.
It covers the proposed length 140 before any integer, endpoint or norm filter is used.

This is an exact obstruction over the real coefficient domain.
Its finite arithmetic checks consist of the displayed convolution sums, rational separator comparisons and integer power comparison.

<a id="growing-scale"></a>
## What remains compatible for the zero profile as conductor and block grow

At the angular midpoint of a terminal block of \(\kappa\) nodes,
\[
                  c=-2\cos(2\pi\kappa/p),\qquad
                  2+c=4\sin^2(\pi\kappa/p).
\]
Taking \(m=\lfloor(L-3)/2\rfloor\) in (18), for growing \(L\), gives
\[
                          (2+c)L^2\le12+o(1).              \tag{20}
\]
If \(\kappa/p\to0\), a necessary asymptotic consequence is
\[
                 \limsup\frac{\kappa L}{p}
                                      \le\frac{\sqrt3}{\pi}. \tag{21}
\]
A cut remaining away from \(-2\) permits only bounded prefix length.

For \(\kappa/p\asymp1/\log p\), (21) permits at most \(L=O(\log p)\).
This necessary condition alone does not exclude choosing \(L\asymp\log p\) with a sufficiently small constant.
If actual noncyclotomic integer inputs at that length existed, (13) would still give the very slow but sufficient rate
\[
                    \log M(P)
                       =O(\log\log p/\log p)\longrightarrow0.
\]
Neither (18) nor (21) proves those inputs exist.

<a id="integer-corollary"></a>
## Conditional consequence for noncyclotomic integer supply

If a sequence of inputs in the five-profile upper statement has integer coefficients, matching lengths \(L\to\infty\), and complete lifts which are not products of cyclotomic polynomials, then
\[
                        0<\log M(P)=O(\log L/L)\to0.
\]
Here \(P\) is monic with constant coefficient one, so the zero-root and leading-coefficient alternatives do not occur.
The strict lower inequality uses precisely Kronecker's measure-one characterization with arbitrary products and multiplicities, retained in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), printed p.322.
Only that theorem statement is reused; no new inspection of its original proof is asserted.
The upper bound itself does not depend on Kronecker's theorem.
The existence of this integer sequence, or an actual positive count in each required strict shell, is not established here.

## Assessment history

### Decision odd-grid-prefix

| Field | Value |
| --- | --- |
| date | 2026-11-09T15:32 |
| status | proved |
| reason | Complete independent review verifies the five-profile whole-measure bound, zero-profile positive cut constraint and exact conductor-401 real obstruction; integer supply and arbitrary-radius positive counts remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact odd-grid statement](#statement) | All stated odd conductors, five profiles, complete-root upper bound, zero-profile compatibility inequality and fixed real obstruction. |
| argument | [Original domain](#original-domain) | Strict signs and endpoint, all mandatory roots and original multiplicities. |
| argument | [Exact coordinates](#prefix-coordinates) | Full lift identity and all permitted prefix indices for five profiles. |
| argument | [Newton baseline](#newton-baseline) | Complete reciprocal power sums and the essential frequency range below p. |
| argument | [Disjoint pairing](#paired-variation) | Degree-independent variation bound with the actual unpaired pole. |
| argument | [Complete measure bound](#whole-measure-upper) | Real and nonreal residual quadratic roots, with no prior measure bound. |
| argument | [Positive cut constraint](#prefix-cut-compatibility) | General odd-grid orthogonality and exact zero-profile finite convolution. |
| argument | [Fixed real obstruction](#fixed-compatibility-test) | Rational separator and exact contradiction for conductor 401 and matching lengths 83 through 201. |
| argument | [Growing scales](#growing-scale) | Necessary cut-length asymptotics and conditional logarithmic-length return. |
| argument | [Integer consequence](#integer-corollary) | Conditional convergence for actual noncyclotomic integer inputs, without an existence assertion. |
| dependency | [Kronecker characterization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | The measure-one characterization in the height-normalization section, with products and multiplicities, used only for the conditional strict lower bound; original proof not re-audited. |
| review | [Independent complete finding](../audits/reviews/Yin_R_G1107_v24.md#odd-grid-prefix-review) | Entire fixed C argument, exact arithmetic and external-statement applicability at their stated scopes. |

## Current assessment

[Selected decision](#decision-odd-grid-prefix)
