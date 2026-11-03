---
author: Yin
---

# Complete excess-three Salem family and exact all-index neutral repair

This retains the entire original2026-10-07 all-parameter proof, with exact finite evidence as corroboration and no length-six enumeration premise.

## Statement

Put f=t^3−t−1, h=1−t^2−t^3 and q_N=t^N f+h.
For every integer N>3, q_N=p_N c_N with p_N the Salem minimal polynomial and c_N the square-free cyclotomic product given in the complete table below.
For every positive integer N the only cyclotomic factors of q_N are Phi2 when N=0mod2, Phi8 when N=7mod8, Phi12 when N=10mod12, Phi18 when N=14mod18 and Phi30 when N=21mod30, each once.
For N>=2 the explicit positive binary graph has dimension N+3, N+6 arrows, characteristic polynomial q_N and determinant of absolute value1; it is primitive and has Frobenius and edge excess3.
For N>=16 the Salem root obeys theta<tau_N<4/3, the tau_N are distinct and converge to theta, every positive power preserves degree, and E(p_N)=3,L(p_N)=6.
The cyclotomic degree is at most12, hence deg p_N>=N−9.
For every N>3, the only possible negative normalized net trace is b_2(p_N)=−1 exactly when N=10mod12.
The canonical repair is then t^2−1 of degree2, and the least-degree repair is Phi2 of degree1; otherwise both repairs are1 of degree0.
These bounded repair and excess controls coexist with unbounded degree and long free digit windows at a strictly positive limiting entropy, and imply no near-one family or unrestricted Mahler gap.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:06 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every integer N>3 for the exact Salem/cyclotomic factorization and all-index canonical/minimum repair, every positive N for the complete square-free cyclotomic table, N>=2 for the exact primitive graph, and N>=16 for E=3/L=6, distinct Salem numbers, interval and all-power degree preservation. |
| argument | [Argument](#argument) | Complete simple-cycle determinant and primitivity, Rouche/reciprocity/Kronecker/root-height proof, all five root-of-unity eliminations/residues/repeated-root remainders, finite-primitive-orbit all-index repair and exact degree-one optimum, source-separated E/L and rational-interval argument. |
| dependency | [Original sparse Salem family](Yin_C_G0222_v1.md#sparse-salem-delay-family) | The exact cubic, root interval/distinctness/convergence/all-positive-power preservation and finite-time digit-window arguments, without importing its old unspecified construction threshold. |
| dependency | [Excess-two construction and lower bound](Yin_C_G0234_v1.md#argument) | E>=2/L>=5 for reciprocal noncyclotomic units and exact E2/L5 relation, not a length6 source classification. |
| dependency | [Exact Salem E2 branch](Yin_C_G0247_v1.md#argument) | Complete accepted thirteen-number branch and seventeen polynomials; only exact separating intervals and the finite branch are used. |
| dependency | [Primitive-cycle net traces](Yin_C_G0240_v1.md#finite-nettrace-repair) | Integral Euler exponents and exact canonical repair convention, with all-index nonnegative graph traces proved locally here. |
| dependency | [Exact retained identities](../computations/programs/Yin_J_G0002/readme.md#results-and-limits) | Existing exact elimination/residue/repeated-root identities, finite graph/net-trace controls and source-group rational interval separation; no new replay claimed. |
| support | [Kronecker and Lehmer source](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted unit-circle Kronecker criterion and exact standard Lehmer polynomial identity at their recorded original source scope. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:15 |
| status | proved |
| reason | The complete retained current statement and all written proof parts were actually checked in the selected whole constructor self finding, with native evidence reused at its real scope. Source, all-index/finite, degree/entropy, zero and conditional limits remain explicit; no isolated review, new execution or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every integer N>3 for the exact Salem/cyclotomic factorization and all-index canonical/minimum repair, every positive N for the complete square-free cyclotomic table, N>=2 for the exact primitive graph, and N>=16 for E=3/L=6, distinct Salem numbers, interval and all-power degree preservation. |
| argument | [Argument](#argument) | Complete simple-cycle determinant and primitivity, Rouche/reciprocity/Kronecker/root-height proof, all five root-of-unity eliminations/residues/repeated-root remainders, finite-primitive-orbit all-index repair and exact degree-one optimum, source-separated E/L and rational-interval argument. |
| review | [Actual complete self finding](../audits/reviews/Yin_R_G0524_v1.md#current-complete-excess-three-family-finding) | Entire current statement and every retained argument/interface at the exact selected scope; actual constructor self-review. |
| dependency | [Original sparse Salem family](Yin_C_G0222_v1.md#sparse-salem-delay-family) | The exact cubic, root interval/distinctness/convergence/all-positive-power preservation and finite-time digit-window arguments, without importing its old unspecified construction threshold. |
| dependency | [Excess-two construction and lower bound](Yin_C_G0234_v1.md#argument) | E>=2/L>=5 for reciprocal noncyclotomic units and exact E2/L5 relation, not a length6 source classification. |
| dependency | [Exact Salem E2 branch](Yin_C_G0247_v1.md#argument) | Complete accepted thirteen-number branch and seventeen polynomials; only exact separating intervals and the finite branch are used. |
| dependency | [Primitive-cycle net traces](Yin_C_G0240_v1.md#finite-nettrace-repair) | Integral Euler exponents and exact canonical repair convention, with all-index nonnegative graph traces proved locally here. |
| dependency | [Exact retained identities](../computations/programs/Yin_J_G0002/readme.md#results-and-limits) | Existing exact elimination/residue/repeated-root identities, finite graph/net-trace controls and source-group rational interval separation; no new replay claimed. |
| support | [Kronecker and Lehmer source](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Accepted unit-circle Kronecker criterion and exact standard Lehmer polynomial identity at their recorded original source scope. |

## Argument

<a id="excess-three-family"></a>
### Statement and retained interfaces

Put `f(t)=t^3−t−1`, `h(t)=f*(t)=1−t^2−t^3`, and

\[
q_N(t)=t^Nf(t)+h(t)
      =t^{N+3}-t^{N+1}-t^N+1-t^2-t^3.
\]

For every `N>3`, this is a Salem minimal polynomial `p_N` times the square-free cyclotomic product `c_N` specified below.
For every `N>=16`:

1. `theta<tau_N<4/3`, where `theta` is the real root of `f` and `tau_N` the Salem root.
   The `tau_N` are distinct, tend to `theta`, and have all-power degree preservation, as in [L G0020](Yin_C_G0222_v1.md#sparse-salem-delay-family).
2. `E(p_N)=3` and `L(p_N)=6`.
   There is an explicit primitive nonnegative **unimodular** `(N+3)`-dimensional matrix with characteristic polynomial exactly `q_N`, with `N+6` entries equal to 1 and all other entries 0.
3. For the canonical repair in [L G0034](Yin_C_G0240_v1.md#finite-nettrace-repair), `a_j=max(0,−b_j(p_N))`, one has

   ```
   product_j (t^j−1)^(a_j) = t^2−1  if N=10 mod12,
                              1     otherwise.
   ```

In particular the negative-index cutoff is at most two and the canonical repair degree is at most two, although `deg p_N` tends to infinity.
The repair assertion already holds for every `N>3`.

The least degree of any cyclotomic factor making all net traces nonnegative is in fact one in the first case, attained by `Phi_2=t+1`, and zero otherwise.
This sharpening was proposed by the coordinator and checked by the assigned agent below.

The assertion `E=3,L=6` uses only the established excess/shortness interface of [L G0033](Yin_C_G0234_v1.md), together with the accepted exact Salem length-five classification [MS26-U001](../audits/literature/MS26/Yin_U001.md#ms26-u001).
It does not use any unaudited length-six enumeration.

### An explicit primitive matrix of excess three

Take a three-vertex core with arrows

```
a0 -> a1,  a1 -> a2,  a2 -> a0,  a2 -> a1.
```

Its simple cycles have lengths two and three, both based at `a1`, and its characteristic polynomial is `f`.
Take a disjoint positive `N`-cycle on `b0,...,b_(N−1)`, and add just

```
b_(N−2) -> a2,    a1 -> b0.
```

This construction is valid for every `N>=2`.
All arrows have weight 1; the two new positions are distinct and absent from the base graph.
Use the convention that an arrow `j->i` is the matrix entry `A_ij`.

The only mixed simple cycles use both new arrows.
The segment inside the `N`-cycle runs from `b0` to `b_(N−2)` and has `N−2` edges; the segment from `a2` to `a1` is either the direct edge or the two-edge route through `a0`.
Thus their lengths are `N+1` and `N+2`.
The only pairs of disjoint simple cycles are the full `N`-cycle together with either core cycle.
Consequently the directed-cycle expansion gives

\[
\begin{aligned}
\det(I-uA_N)
 &=(1-u^2-u^3)(1-u^N)-u^{N+1}-u^{N+2}\\
 &=1-u^2-u^3-u^N-u^{N+1}+u^{N+3}
  =q_N(u).
\end{aligned}
\]

The graph has `N+3` vertices and `N+6` arrows, giving Frobenius and nonnegative edge excess both equal to three.
Since `q_N` is reciprocal and has constant coefficient 1, its characteristic polynomial is exactly `q_N(t)`, and `det A_N=(-1)^(N+3)`.
No zero eigenvalue is added.

The graph is strongly connected.
At `a1` there are return cycles of lengths two and three, so every length at least two is available as a return walk.
Fix paths from each vertex to `a1` and from `a1` to each vertex.
Choosing a common total length larger than every sum of these fixed lengths plus two gives a walk of that length for every ordered pair.
Hence a common matrix power is strictly positive: `A_N` is primitive.

This construction supersedes the coordinator's preliminary excess-four graphs; they are not needed as theorem dependencies.
For `N>3` it directly gives an admissible realization for `E(p_N)`, once the factorization below is established.

### The Salem factor exists for all N greater than three

The cubic `f` is irreducible by the rational-root test; its discriminant is `−23`.
Its real root `theta>1` and the moduli of its two nonreal roots are `theta^(−1/2)<1`, as already checked in L G0020.
In particular `f` has no unit-circle root.

For `epsilon>0`, on `|t|=1` one has

```
|(1+epsilon)t^N f(t)| > |h(t)| = |f(t)|.
```

Rouche's theorem shows that `(1+epsilon)t^N f+h` has exactly `N+2` roots inside the circle and one outside.
Passing to `epsilon=0` shows that `q_N` has at most one root strictly outside, counting multiplicity.
Since `q_N(1)=-2` and it is monic, there is a positive real root greater than one, so it is the unique expanding root and is simple.
Reciprocity gives its inverse, and every other root is on the circle.

For `N>3` the coefficient height is one.
Leading-term domination for `|t|>=2` shows that every root has modulus less than two.
The irreducible factor containing the expanding root must contain the unique contracting root: all irreducible monic factors have constant coefficient a unit, so otherwise its root-product modulus would exceed one.
It cannot be quadratic, since a quadratic reciprocal integer unit with an expanding positive root has integer trace at least three and root at least `(3+sqrt(5))/2>2`.
It therefore has a unit-circle conjugate and is a Salem minimal polynomial.
The other factors are cyclotomic by Kronecker.

This direct argument removes the unspecified construction threshold from the old family's statement, without enlarging a source adoption.
The previous exact calculations

```
q_N(theta)<0,
q_N(4/3)=((4/3)^N−85)/27>0 for N>=16
```

now give the claimed interval for all `N>=16`.
L G0020's arguments for distinctness, convergence and all-power preservation apply unchanged.

<a id="family-cyclotomic-factors"></a>
### Complete cyclotomic factor table

For every positive `N`, the cyclotomic factors of `q_N` are exactly the following, each with multiplicity one:

| Factor | Condition |
| --- | --- |
| `Phi_2` | `N=0 mod2` |
| `Phi_8` | `N=7 mod8` |
| `Phi_12` | `N=10 mod12` |
| `Phi_18` | `N=14 mod18` |
| `Phi_30` | `N=21 mod30` |

Here and below `c_N` is the product of those factors whose conditions hold.
The proof is an explicit root-of-unity elimination, with no large-order search assumption.
Let `zeta` be a primitive `d`th root which is a zero of `q_N`.
Then `f(zeta)h(zeta)!=0` and `zeta^N=−h(zeta)/f(zeta)`.

The following are Galois conjugates of `zeta`: `−zeta` if `4|d`, `zeta^2` if `d` is odd, and `−zeta^2` if `d=2 mod4`.
This follows by checking that the associated exponents are coprime to `d`.
Eliminating `zeta^N` from the two vanishing equations gives the following exact polynomial identities.
Write `P_L` for the retained irreducible Lehmer polynomial, which has no root of unity.

| Case | Eliminating polynomial, factored |
| --- | --- |
| `4|d`, `N` even | `f(t)h(−t)−h(t)f(−t)=−2t Phi_12(t)` |
| `4|d`, `N` odd | `f(t)h(−t)+h(t)f(−t)=2 Phi_1(t) Phi_2(t) Phi_8(t)` |
| `d` odd | `h(t)^2 f(t^2)+h(t^2)f(t)^2=2t P_L(t)` |
| `d=2 mod4`, `N` even | `h(t)^2 f(−t^2)+h(−t^2)f(t)^2=−2t Phi_1(t) Phi_2(t)^3 Phi_18(t)` |
| `d=2 mod4`, `N` odd | `−h(t)^2 f(−t^2)+h(−t^2)f(t)^2=2 Phi_12(t) Phi_30(t)` |

The case restrictions leave only `d=2,8,12,18,30`.
For each, reducing `t^N f+h` modulo `Phi_d` gives precisely the residue in the first table.
It is enough to verify that one residue: if both `r` and `s` work, then `zeta^r=zeta^s`, so `r=s modd`.

A repeated cyclotomic root would also satisfy

\[
N=\frac{t(h'f-hf')}{hf}\quad\text{at }t=\zeta.
\]

The remainders of this rational function modulo the five cyclotomic polynomials are respectively

```
d= 2: −1,
d= 8: −4t^3+4t−5,
d=12: −2t^3+4t−2,
d=18: −6t^5+3t^4+3t^2+3t−4,
d=30: −3t^6−t^5+2t^4+t^3+2t^2+4t−2.
```

The first would require `N=-1`; each other remainder is nonconstant of degree below `deg Phi_d`, and so cannot equal an integer at a primitive `d`th root.
This proves square-freeness of the cyclotomic part.

The degree of `c_N` is at most 12.
For even `N`, only `Phi_2` and at most one of `Phi_12,Phi_18` occur; the latter two congruences are incompatible modulo six.
For odd `N`, only `Phi_8,Phi_30` occur.
In particular `deg p_N=N+3−deg c_N>=N−9`, giving explicit degree escape.

<a id="family-repair"></a>
### Exact canonical repair: only a possible negative b_2

For a nonnegative integral adjacency matrix, the normalized net trace `b_j` counts primitive closed-walk orbits of length `j`.
Indeed ordinary trace counts based closed walks, uniquely obtained by repetition of a primitive orbit, giving `s_m=sum_(j|m) j b_j`.
Thus all `b_j(q_N)` are nonnegative.
The plastic core is a subgraph, so also

```
b_j(q_N)>=b_j(f)  for every j.
```

Equivalently the original series observation is

\[
q_N(u)=(1-u^2-u^3)(1-u^N R(u)),\qquad
R(u)=1+\frac{u+u^2}{1-u^2-u^3}\in\mathbb Z_{\ge0}[[u]].
\]

For a series `C` with nonnegative integral coefficients and zero constant coefficient, the Euler exponents of `1−C` count primitive cyclic words in a graded alphabet and are nonnegative.
Expanding `−log(1−C)` groups words by their primitive cyclic period; a repeated orbit contributes its standard `1/m` logarithmic coefficient.
Only finitely many letters or words occur at each total degree.
This independently explains the same inequality.

Cyclotomic Euler exponents satisfy

```
b_j(Phi_d)=mu(d/j) if j divides d, and 0 otherwise.
```

Applying this identity to the exact factor table shows that positive `b_j(c_N)` can occur only at

```
j in {2,3,5,8,12,18,30}.
```

At each of these indices the plastic core has at least one primitive orbit.
For indices two and three use the two core cycles.
For five and eight use the cyclic words `AB` and `ABB` in return excursions of lengths two and three.
For 12,18,30 use `AAABB`, `AAABBBB`, `AAABBBBBBBB`.
A cyclic word consisting of one nonempty A-block and one nonempty B-block is primitive: a proper power would have more than two changes of letter around the circle.
Thus `b_j(f)>=1` at all seven indices, and `b_2(f)=1` exactly.

Every positive `b_j(c_N)` is at most one, except possibly `j=2`.
At `j=3` the two potential positive contributions, from `Phi_18` and `Phi_30`, cannot coexist because their congruences have opposite parity.
At `j=2` the value is two precisely when both `Phi_2` and `Phi_12` occur, namely `N=10 mod12`; `Phi_30` cannot coexist with either.
All other indices have no more than one positive contribution.

Since `b_j(p_N)=b_j(q_N)−b_j(c_N)`, negativity is therefore impossible except at `j=2` in that one congruence class.
In that class `N>=10`, so the coefficients through degree two of `q_N(u)` equal those of `1−u^2−u^3`, and `b_2(q_N)=1`.
Hence `b_2(p_N)=-1` exactly.
This proves the asserted complete canonical repair, including all indices and all parameters, rather than an experimentally observed cutoff.

The canonical recipe need not minimize repair degree.
If `N=10 mod12`, the factor table gives `c_N=Phi_2 Phi_12` exactly, since the other congruences are incompatible.
Now `b_1(q_N)=0` and `b_1(c_N)=-1`, so `b_1(p_N)=1`.
Multiplication by `Phi_2` changes only `b_1` and `b_2`, by `−1` and `+1` respectively, removing the single negative net trace while leaving all others nonnegative.
A degree-zero repair cannot remove `b_2=-1`; hence degree one is minimal.
Outside this congruence class, no repair is needed and degree zero is minimal.

### Exact complexity and consequence for the original question

The graph proves `E(p_N)<=3`, and `q_N` proves `L(p_N)<=6` for `N>3`.
For `N>=16`, its Salem number lies in `(theta,4/3)`, where `theta>33/25` because `f(33/25)=-313/15625<0`.
The accepted 13-number classification contains no number in `(33/25,4/3)`; this separation is also an exact comparison of the retained rational trace intervals, not a rounding inference.
Thus `L(p_N)!=5` and `E(p_N)!=2`.
Their reciprocal noncyclotomic lower bounds are five and two respectively, so `L(p_N)=6`, `E(p_N)=3`.

This family therefore exhibits unbounded algebraic degree, all-power degree preservation and the long free digit windows of L G0020, alongside uniformly bounded exact shortness, graph excess and canonical repair.
Neither a growing dimension nor that finite-time entropy obstruction forces the negative-index cutoff or repair degree to grow.
The limiting entropy is `log(theta)>0`; nothing here controls a hypothetical sequence with entropy tending to zero.
The canonical degree-two repair is not claimed to have the same explicit graph as the different completion `c_N` used above.
