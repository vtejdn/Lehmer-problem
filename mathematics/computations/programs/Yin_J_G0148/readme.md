---
author: Yin
---

# A prescribed moving cut for units and norm-$p$ numerators

<a id="prescribed-cut"></a>
## Two numerator families on the same prime grid

For every prime $23\le p\le67$, put $n=(p-1)/2$, $k=\lfloor p/\log p\rfloor$ (natural logarithm), and $r=n-k$.
Use the [J146 circular units](../Yin_J_G0146/readme.md#unit-law) in $\mathbb Q(\zeta_p)^+$, where $b_j=\zeta_p^j+\zeta_p^{-j}$ decrease for $1\le j\le n$ and $B=\prod_j(t-b_j)$.
The target is $k$ negative residues at the smallest poles and $r$ positive residues at the largest.
Choose the full parameter box
\[
 U=s\prod_{j=2}^n u_j^{e_j},\qquad
 s\in\{-1,1\},\quad e_j\in\{-1,0,1\},\qquad
 C(b_1)\in\{U,(2-b_1)U\},\qquad
 a=2x,\quad x\in\{-2,-1,0,1,2\}.
\]
Here $C$ is the unique integral representative of degree below $n$, $Q=(t-a)B+C$, and $P=z^{n+1}Q(z+z^{-1})$ is the original monic reciprocal polynomial of degree $p+1$.
At all embeddings $2-b_j>0$, so this multiplier preserves every sign.
The absolute resultant $\Delta=|\operatorname{Res}(B,Q)|$ is respectively $1$ and $p$, since $|N(U)|=1$ and $\prod_j(2-b_j)=B(2)=p$.
In particular the norm-$p$ choice has $\Delta^{1/n}\to1$ as the prime grows and so fits the asymptotic [resultant ceiling](../../../ledger/Yin_L_G0464_v6.md#norm-ceiling).
The strict left endpoint is $Q(-2)/B(-2)=-P(-1)<0$.

<a id="finite-box"></a>
## Exact counts and whole-measure exclusions

In the table each paired entry lists the unit count first and the norm-$p$ count second.
Words count the parameter choices $(s,e)$ for each family meeting the requested residue signs before choosing $x$.
The chamber column counts $(s,e,x)$ after the strict endpoint test.
The next column counts chamber atoms whose coefficients through $z^2$ match the [limiting profile for their own $x$](../../../ledger/Yin_L_G0464_v5.md#only-left-endpoint).

| $p$ | $k$ | Signature rank | Words per family | Chamber atoms | Match through $z^2$ |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 23 | 7 | 11 | 128 | 75 / 10 | 0 / 0 |
| 29 | 8 | 11 | 0 | 0 / 0 | 0 / 0 |
| 31 | 9 | 15 | 256 | 106 / 13 | 2 / 0 |
| 37 | 10 | 18 | 256 | 121 / 30 | 2 / 0 |
| 41 | 11 | 20 | 512 | 248 / 30 | 11 / 4 |
| 43 | 11 | 21 | 4 | 6 / 3 | 0 / 0 |
| 47 | 12 | 23 | 4 | 6 / 3 | 0 / 0 |
| 53 | 13 | 26 | 4 | 6 / 4 | 0 / 0 |
| 59 | 14 | 29 | 16,384 | 10,392 / 4,978 | 46 / 0 |
| 61 | 14 | 30 | 4,096 | 2,968 / 1,811 | 23 / 0 |
| 67 | 15 | 33 | 16,384 | 7,550 / 4,582 | 31 / 0 |
| Total | | | 38,028 | 21,478 / 11,464 | 115 / 4 |

Every one of the 21,478 unit chamber atoms has $M(P)>29/20$.
Every one of the 11,464 norm-$p$ chamber atoms has $M(P)>12/5$.
The coefficients of the corresponding limiting profile through $z^3$ are $1,1-2x,x^2-2x+4,x^2-6x+4$.
No chamber atom matches all four coefficients.
These are complete exclusions for the specified box, strict chamber and shifts.
They give zero mass to $1<M(P)\le6/5$ there and leave larger exponents, other numerators and other conductors open.

<a id="paired-example"></a>
## A unit and a nonunit at the same cut

At $p=43$ take $x=1$ and $U=u_2^{-1}u_{21}^{-1}$.
Both inputs have eleven negative residues and ten positive ones.
The unit has $P(-1)=3$ and $1.46<M(P)<1.47$.
The norm-43 input has $P(-1)=1$ and $2.40<M(P)<2.43$.
For a direct check of the unit used here, $u_2=b_1$ and $u_n b_n=-1$ since $2n=p-1$, so $b_1 U=-b_n$.
The program checks this identity on the actual cyclic coefficient vector and checks both rational measure windows on the original lifts.

<a id="reproduction"></a>
## Reproduction and certification

Run the [census](cuts.py) from this directory with Python 3.11 or later and the standard library.
The only repository dependency is the integer [Graeffe map](../Yin_J_G0144/pilot.py).
The default command prints the complete table, including the cubic-prefix and below-threshold counts, and checks the paired example.

~~~text
python -B cuts.py
~~~

For the signature matrix, the sign bit at pole $b_l$ of $u_j$ is $\lfloor 2jl/p\rfloor\bmod2$ and the column for $-1$ consists of ones.
The numerator target has bit $((l-1)\bmod2)\mathbin{\mathrm{XOR}}[l>r]$, accounting for the sign of $B'(b_l)$.
The program checks the integer $k$ against exact rational bounds enclosing the correctly rounded decimal logarithm and solves the resulting binary system.
At $p=29$ the rows with one-based indices $1,2,3,4,5,7,10,12$ sum to zero on every generator and to one on this target.
Thus the prescribed cut is impossible there for arbitrary integer exponents in these generators, also after multiplying by $2-b_1$.
Every other prime in the table has full signature rank.

For every solution, a zero parity means exponent zero and a one means each of $-1,1$ in turn.
Products are computed by cyclic convolution in $\mathbb Z[\zeta_p]$, representing $u_j$ by $\sum_{h=0}^{j-1}\zeta_p^{j-1-2h}$ and its inverse by the same sum with length $j^{-1}\bmod p$ and variable $\zeta_p^j$.
Subtracting the common coefficient at $\pm n$ from every cyclic coefficient gives the symmetric Laurent representative $W$ supported in $[-n+1,n-1]$.
This represents the unique trace remainder of degree below $n$, so the program tests the endpoint on the integer lift
\[
       (1-2xz+z^2)\Phi_p(z)+z^{n+1}W(z).
\]
For a candidate upper bound $R>1$, the [reciprocal Newton bound](../Yin_J_G0146/readme.md#four-conductors) gives necessary inequalities $|s_h|\le p-1+R^h+R^{-h}$.
For any surviving input after $d$ Graeffe squarings, the new coefficients $c_j$ satisfy
\[
  \max_j\frac{|c_j|}{\binom{p+1}{j}}\le M(P)^{2^d}
    \le\left(\sum_jc_j^2\right)^{1/2}.
\]
All measure decisions compare rational thresholds by integer arithmetic, including the strict lower and upper bounds in the paired example.
An undecided threshold raises an error.
The computation developer executed and self-checked the stated finite scope.
Direct sums of the unreduced cyclic coefficients reproduced all 128 unit words at 23 and all four each at 43 and 53.
For the paired example, fraction-free determinants of the multiplication maps on the real trace order gave signed norms (-1) and (-43).
