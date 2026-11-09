---
author: Yin
---

# Higher integer moments and a uniform whole-measure gap for the negative-one branch

<a id="statement"></a>
## Statement and retained scope

Use the exact conductor, cut, signs and integral construction of [C882v3](Yin_C_G0882_v3.md#statement), with
\[
 p=19683,\quad n=9841,\quad k=1990,\quad
 b_j=2\cos(2\pi j/p),\quad B=\prod_{j=1}^n(t-b_j),\quad D=B_{n-1}.
\]
Let \(h\in\mathbb Z[t]\) be positive at the first 7851 nodes and negative at the last 1990 nodes, with \(\prod_j|h(b_j)|=2^{4391}\).
Set
\[
 r_j=(4-b_j^2)h(b_j)/p,\qquad C=Dh\bmod B,\qquad
 Q=(t+2)B+C,\qquad P=z^{n+1}Q(z+z^{-1}).
\]
Assume \(K=\sum r_j=3\), \(L=\sum b_jr_j=4\), and \(P(-1)>0\).
The inherited endpoint conclusion is \(U=\sum r_j/(2+b_j)=1\), and the inherited necessary second residue moments are \(N=\sum b_j^2r_j\in\{7,8,9,10\}\).
Write
\[
 O=\sum b_j^3r_j,\qquad V=\sum b_j^4r_j,\qquad W=\sum b_j^5r_j.
\]
These are integers, as are all coefficients in the Laurent expansion of the integral rational function \(C/B\) at infinity.
No additional agreement with an arcsine moment profile is assumed.

For \(N=8\), the complete multiplicative Mahler measure satisfies
\[
                         M(P)>23/20.
\]
This holds for every permitted \(h\), and does not require deciding whether the two exceptional trace roots are real or nonreal.
It is weaker than the \(6561\) lower bound \(2209/1600\), whose extension to this case remains unresolved.
The existing \(N=9,10\) conclusions remain at [C882v3](Yin_C_G0882_v3.md#whole-measure), while the different \(x=2\) branch remains at [C882v4](Yin_C_G0882_v4.md#statement).

For \(N=7\), the following table is necessary.
Every displayed interval includes its endpoints.
No entry is asserted to be realizable, and no uniform complete-measure gap for this row is established here.

| \(O\) | \(V\) | Necessary \(W\) |
| ---: | ---: | --- |
| 10 | 17 | 25,26 |
| 10 | 18 | 26,27,28 |
| 11 | 19 | 30,31,32 |
| 11 | 20 | 32,33,34,35 |
| 11 | 21 | 36,37 |
| 12 | 22 | 39,40 |
| 12 | 23 | 42,43 |

<a id="positive-moments"></a>
## Positive moment matrices without profile matching

Take \(y=-161/100\), which lies in the sign-changing gap by the [exact recurrence calculation](Yin_C_G0882_v3.md#argument).
The weights
\[
             \mu_j=(2-b_j)(b_j-y)h(b_j)/p
\]
are strictly positive at every node.
Put \(s_a=\sum b_j^a\mu_j\).
The identity \(r_j=(2+b_j)(2-b_j)h(b_j)/p\), together with \(U=1,K=3,L=4\), gives
\[
\begin{aligned}
 s_0&=261/100,&s_1&=361/100,&s_2&=N-78/100,\\
 s_3&=O-39N/100+156/100,\\
 s_4&=V-39O/100+78N/100-312/100,\\
 s_5&=W-39V/100+78O/100-156N/100+624/100.
\end{aligned}
\]
Every moment matrix below is strictly positive definite: its quadratic form sums a positive weight times the square of a nonzero polynomial of degree at most two over 9841 distinct nodes.
The localizing factors \(2+b_j\), \(2-b_j\), and \(4-b_j^2\) are also strictly positive.

The two matrices \((2s_{i+j}\mathbin\pm s_{i+j+1})_{i,j=0}^1\) imply
\[
 \frac{(2s_1+s_2)^2}{2s_0+s_1}-2s_2
 <s_3<
 2s_2-\frac{(2s_1-s_2)^2}{2s_0-s_1}.
\]
After substituting the displayed moments, this gives
\[
\begin{array}{c|c|c}
 N&\text{strict interval for }O&\text{integer possibilities}\\ \hline
7&(162239/17660,\ 209121/16100)&10,11,12\\
8&(236958/22075,\ 16)&11,12,13,14,15.
\end{array}
\]

The matrices \((s_{i+j})_{i,j=0}^2\) and \((4s_{i+j}-s_{i+j+2})_{i,j=0}^1\) give
\[
 \frac{s_2^3-2s_1s_2s_3+s_0s_3^2}{s_0s_2-s_1^2}
 <s_4<
 4s_2-\frac{(4s_1-s_3)^2}{4s_0-s_2}.
\]
All denominators are positive by the same strict positive definiteness.
For the only sixth-degree case needed below, \(N=8,O=14\), this implies
\[
       72698481/2906050<V<241321/8050,
       \qquad V\in\{26,27,28,29\}.
\]
For \(N=7\), the resulting possibilities are
\[
 O=10:\ V=17,18;\qquad
 O=11:\ V=19,20,21;\qquad
 O=12:\ V=22,23,24.
\]

For each sign \(\varepsilon\in\{1,-1\}\), set
\[
 A_\varepsilon=
 \begin{pmatrix}2s_0+\varepsilon s_1&2s_1+\varepsilon s_2\\
 2s_1+\varepsilon s_2&2s_2+\varepsilon s_3\end{pmatrix},\qquad
 v_\varepsilon=\binom{2s_2+\varepsilon s_3}{2s_3+\varepsilon s_4}.
\]
The positive definite matrices \((2s_{i+j}+\varepsilon s_{i+j+1})_{i,j=0}^2\) imply the strict bounds
\[
 v_+^{\mathsf T}A_+^{-1}v_+-2s_4<s_5
 <2s_4-v_-^{\mathsf T}A_-^{-1}v_-.
\]
Substitution supplies explicit rational lower and upper bounds on the integer \(W\).
The additional norm inequality in the next section removes \((O,V)=(12,24)\) and gives exactly the \(N=7\) table in the statement.
The [integer and rational program](../computations/programs/Yin_J_G0151/negative_one_higher.py) evaluates these displayed formulas and enumerates all integers strictly between their endpoints.

<a id="higher-norm"></a>
## An integral positive weight and its range across conductors

Let \(g(t)=(t-1)(t-2)\).
The weights \((b_j-y)r_jg(b_j)^2\) are strictly positive.
On a primitive layer of order \(3^\ell\), use the factorization \(h=2^{t_\ell}f_\ell\), the normalized-trace integrality, the exponent constraint and the parities proved in [C882v3](Yin_C_G0882_v3.md#argument).
The polynomial
\[
      (4-b^2)(100b+161)(b-1)^2(b-2)^2f_\ell(b)
\]
has positive values at all layer embeddings.
For \(\ell>1\), the absolute norms of \(b-1\), \(b-2\), and \(4-b^2\) are respectively \(1,3,3\).
For \(\ell=1\), the only node is \(-1\), and the polynomial factor has value \(3\cdot61\cdot36=6588\).
The integral normalized traces therefore have lower bounds
\[
                (6588,355,139,114,103,102,101,101,101).
\]
Minimizing \(\sum d_\ell2^{t_\ell}\) times these weights over the inherited exponent and parity constraints gives 1781643.
The exact minimum is attained by the exponent vector \((5,4,3,2,2,2,2,1,0)\), and the same exhaustive dynamic program and integer-root tests used in C882v3 verify it.
Consequently
\[
 \begin{split}
 I&=W-\frac{439}{100}V+\frac{167}{50}O
       +\frac{893}{100}N-\frac{1049}{25}\\
  &\ge\gamma:=\frac{1781643}{1968300}=\frac{593881}{656100}.
 \end{split}
\]
For the \(N=7\) enumeration, intersect the strict moment-matrix interval for \(W\) with
\[
 W\ge\gamma+\frac{439}{100}V-\frac{167}{50}O
            -\frac{893}{100}N+\frac{1049}{25}.
\]
For example, \((O,V)=(12,24)\) has a moment-matrix upper bound less than \(45.379\), whereas this norm bound is greater than \(45.635\), leaving no integer.

The same polynomial weight gives a conductor-independent conditional obstruction to simultaneous matching of the first six residue moments.
For any sign cut with separator \(y\), expansion gives
\[
 \sum(b_j-y)r_jg(b_j)^2
 =W-(6+y)V+(13+6y)O-(12+13y)N+(4+12y)L-4yK.
\]
At the negative-one arcsine target \((K,L,N,O,V,W)=(3,4,8,12,26,40)\), the right side equals \(-40-22y\).
It is negative whenever \(y>-20/11\), contradicting positivity.
This observation concerns simultaneous moment matching, not a Mahler threshold by itself.
In particular, it cannot be substituted for the complete-root argument below.
For logarithmic cuts at unbounded conductors, the separators tend to \(-2\), so the condition \(y>-20/11\) eventually fails.
This weight therefore does not alone give a bound uniform over an unbounded conductor sequence.
The choice of a quadratic positive weight was developed in collaboration with the main agent's target Hankel calculation; neither calculation is an independent review of this argument.

<a id="whole-measure"></a>
## Root pairing and a certificate for the complete measure

Let \(b_*=b_{7851}\), the smallest positive-residue pole.
The rational recurrence from C882v3 gives 7851 poles above \(y=-161/100\) and 7850 poles above \(z=-1006/625\).
Hence \(y<b_*<z\).
The second count, as well as the first, is checked by the native rational program.

There is at least one real root of \(Q\) in every interval whose endpoint residues have the same sign.
This follows from the opposite infinite limits of \(Q/B=t+2+\sum_jr_j/(t-b_j)\) at those endpoints.
There is also a root in \((-2,b_n)\), since \(Q(-2)/B(-2)=-U=-1\) and the limit from below at the negative-residue pole \(b_n\) is positive infinity.
Choose one root in each of these disjoint intervals and pair it with that interval's right pole.
There are \(n-1\) chosen roots, all in \((-2,2)\); the only unpaired pole is \(b_*\).
Denote the remaining two trace roots, with multiplicity, by \(v_1,v_2\).

For a real polynomial \(f\), write
\[
 \mathcal D(f)=\sum_{Q(v)=0}f(v)-\sum_{B(b)=0}f(b),\qquad
 V_-(f)=\int_{-2}^2\max(0,-f'(t))\,dt.
\]
Each chosen root lies to the left of its paired pole, and the corresponding intervals are disjoint.
Summing the integrals of \(f'\) over these intervals gives
\[
        \sum_{i=1}^2\operatorname{Re} f(v_i)
        \ge\mathcal D(f)+f(b_*)-V_-(f).
\]
The two remaining lifted reciprocal pairs have exterior radii \(\rho_1,\rho_2\ge1\).
All chosen trace roots lift to the unit circle, so the complete measure is exactly \(M(P)=\rho_1\rho_2\).

Use \(T_j(z+z^{-1})=z^j+z^{-j}\), and let \(f=\sum_{j=1}^d c_jT_j\).
If \(M(P)\le R\), compare each \(v_i=\rho_i e^{i\theta_i}+\rho_i^{-1}e^{-i\theta_i}\) with \(2\cos\theta_i\).
Then
\[
 \sum_{i=1}^2\operatorname{Re}f(v_i)
 \le2\max_{[-2,2]}f+
       \sum_{j=1}^d|c_j|(R^j+R^{-j}-2).
\]
Indeed the radial error for \(T_j\) is bounded by \(\rho_i^j+\rho_i^{-j}-2\), and the sum of these two nonnegative quantities is at most \((\rho_1\rho_2)^j+(\rho_1\rho_2)^{-j}-2\).
The last inequality follows by writing \(\rho_i^j=e^{a_i}\), \(a_i\ge0\), and using \(\cosh(a_1+a_2)-1\ge(\cosh a_1-1)+(\cosh a_2-1)\).
This covers both real and nonreal exceptional roots.

Let \(D_j=\mathcal D(t^j)\).
There is one more root of \(Q\) than of \(B\), so \(D_0=1\).
Expansion of \(Q/(tB)=1+2/t+3/t^2+4/t^3+N/t^4+O/t^5+V/t^6+\cdots\) yields
\[
\begin{aligned}
 D_1=D_2=D_3&=-2,\\
 D_4&=18-4N,\\
 D_5&=10N-5O-22,\\
 D_6&=-6N+12O-6V-2,\\
 D_7&=-7O+14V-7W-2.
\end{aligned}
\]
In particular, the constant terms of the even \(T_j\) contribute through \(D_0=1\).

Set \(R=23/20\).
For each possible \(O\) with \(N=8\), choose the following integer Chebyshev coefficients.
The omitted sixth coefficient is zero.

| \(O\) | \((c_1,c_2,c_3,c_4,c_5,c_6)\) | Strict lower bound for the certificate margin |
| ---: | --- | ---: |
| 11 | \((2383,-2971,2189,-1400,1057,0)\) | 6544 |
| 12 | \((2975,-2801,2206,-1407,612,0)\) | 2562 |
| 13 | \((3157,-2865,2246,-1319,413,0)\) | 53 |
| 14 | \((673,-2441,3300,-1307,-1292,988)\) | 386 |
| 15 | \((0,0,2275,-3347,-4378,0)\) | 11815 |

The certificate margin is a rigorous lower bound for
\[
 \mathcal D(f)+\min_{[y,z]}f-V_-(f)
       -2\max_{[-2,2]}f
       -\sum_{j=1}^d|c_j|(R^j+R^{-j}-2).
\]
For \(O=14\), use the worst permitted value \(V=29\).
Since the coefficient of \(D_6\) is \(988>0\), decreasing \(V\) only increases \(\mathcal D(f)\), so this same certificate applies to \(V=26,27,28\).
Every margin is positive, contradicting the two root-pairing inequalities if \(M(P)\le23/20\).

<a id="rational-certificates"></a>
## Exact polynomial enclosure and reproduction

The margin bounds are checked with rational arithmetic, without root finding or an assumed numerical extremum.
For a polynomial \(q\) of degree \(d\) on a rational interval \([a,b]\), write \(q(a+(b-a)u)=\sum_{j=0}^d A_ju^j\).
Its degree-\(d\) Bernstein coefficients are
\[
       \beta_i=\sum_{j=0}^i A_j\frac{\binom{i}{j}}{\binom{d}{j}}.
\]
The Bernstein basis is nonnegative and sums to one on \(0\le u\le1\), so \(\min_i\beta_i\le q\le\max_i\beta_i\).
Apply this to \(f'\) on each of the 1024 equal rational subintervals of \([-2,2]\).
If its Bernstein lower bound is nonnegative, that interval contributes zero to \(V_-(f)\), and its maximum of \(f\) is its right endpoint value.
If its Bernstein upper bound is nonpositive, the negative variation is exactly \(f(a)-f(b)\), and the maximum is its left endpoint value.
Otherwise, bound the negative variation by \((b-a)\max(0,-\min_i\beta_i)\), and bound the maximum of \(f\) by its own Bernstein upper bound.
The maximum of these interval bounds bounds \(\max_{[-2,2]}f\), while their variation bounds add.
An independent Bernstein lower bound for \(f\) on \([y,z]\) supplies the cut term.
Every coefficient, interval endpoint, trace difference and radial cost is rational.

Running `python mathematics/computations/programs/Yin_J_G0151/negative_one_higher.py` uses only the standard library and verifies all five strict integer margin bounds, the cut brackets, the layer norm bound and the complete necessary moment tables stated here.
Its optional `--explore` mode uses SciPy to search sampled linear programs; those outputs are explicitly exploratory and supply no certificate or realizability claim.
The fixed certificates above do not call or depend on that mode.

## Assessment history

### Decision negative-one-higher-19683

| Field | Value |
| --- | --- |
| date | 2026-11-09T12:20 |
| status | proved |
| reason | Independent inspection and separate rational computations verified every higher-moment restriction and the complete-measure bound for all N=8 inputs, retaining the unresolved N=7 and larger-threshold questions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Negative-one higher moments](#statement) | All stated hypotheses, the full N=8 Mahler bound and necessary N=7 integer table. |
| argument | [Positive moment matrices](#positive-moments) | Strict localized matrices and complete integer intervals without additional profile matching. |
| argument | [Higher norm weight](#higher-norm) | Every layer valuation, exact trace bound and limited moving-cut consequence. |
| argument | [Complete root measure](#whole-measure) | Every trace root, exact cut bracket, constant trace term and five fixed coefficient vectors. |
| argument | [Rational certificates](#rational-certificates) | Exact Bernstein bounds and all five positive margins at 23/20. |
| dependency | [Inherited integer chamber](Yin_C_G0882_v3.md#statement) | Exact signs and norm, U=1 and N in 7 through 10. |
| dependency | [Integral layer inputs](Yin_C_G0882_v3.md#argument) | Separator, normalized traces, valuation constraints and exhaustive minimization. |
| dependency | [Complete pairing](../ledger/Yin_L_G0464_v12.md#pairing) | Disjoint real intervals and both exceptional exterior radii. |
| review | [Independent negative-one finding](../audits/reviews/Yin_R_G1107_v10.md#negative-one-higher-19683) | Entire new statement and proof, all default exact program paths and necessary direct interfaces. |

## Current assessment

[Selected decision](#decision-negative-one-higher-19683)
