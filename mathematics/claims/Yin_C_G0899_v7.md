---
author: Yin
---

# Height-one varying Pisot seeds can erase a prescribed sublinear prime-order rate

<a id="statement"></a>
## Exact failure at the seed degree

For each odd prime \(p\) put
\[
 f_p(z)=z^p-\sum_{j=0}^{p-1}z^j,\qquad
 H_{p,N}(z)=z^Nf_p(z)-f_p^*(z).
\]
The seed \(f_p\) is the monic minimal polynomial of a Pisot number and has coefficient height one.
For every integer \(N\ge4\), the polynomial \(H_{p,N}\) has a unique exterior root \(\alpha_{p,N}\), and
\[
                 \frac32<\alpha_{p,N}<2.
\]
Its monic minimal polynomial \(P_{p,N}\) is a Salem polynomial of degree \(d_{p,N}\) satisfying
\[
                 N-11p\le d_{p,N}\le N+p.                    \tag{1}
\]
Use the trace resultant \(B_q(P)\) and common integer modulus \(G_q(P)\) of [C899v5](Yin_C_G0899_v5.md#statement).
If \(p\nmid N\), then
\[
             B_p(P_{p,N})=G_p(P_{p,N})=1,\qquad
 \left|\frac{\log G_p(P_{p,N})}{p-1}-\frac{m(P_{p,N})}{2}\right|
                     >\frac12\log\frac32.                  \tag{2}
\]
The same strict error bound holds with \(B_p\) in place of \(G_p\).

Consequently, let \(N\) tend to infinity through primes, and prescribe any odd primes \(p_N\to\infty\) with \(p_N=o(N)\).
The height-one seeds \(f_{p_N}\) then have degrees \(p_N=o(N)\), the actual Salem degrees satisfy \(d_{p_N,N}/N\to1\), and \(p_N=o(d_{p_N,N})\), while both proposed prime-order rates are identically zero for all sufficiently large \(N\).
Thus sublinear seed degree and bounded coefficient height do not make an arbitrarily prescribed common sublinear prime sequence uniform over those seeds.
More precisely, for a prime delay \(N\) and a seed-degree cap \(3\le R<N\), no odd prime \(q\le R\) gives error less than \(\tfrac12\log(3/2)\) simultaneously for all the seeds \(f_p\) with odd prime \(p\le R\).
Take the member \(f_q\) to see this.

<a id="salem"></a>
## A Salem factor at every stated delay

The [multinacci root calculation](Yin_C_G0021_v1.md#multinacci-local-roots-irreducibility-and-measure) proves that \(f_r=z^r-\sum_{j=0}^{r-1}z^j\) is irreducible for every \(r\ge2\), with one simple root in \((1,2)\) and all its other roots strictly inside the unit disk.
Its classical attribution and the distinction from an uninspected original proof are retained in [Smi11-U001](../audits/literature/Smi11/Yin_U001.md#smi11-u001).
For \(r\ge3\), inspection of the interior coefficients shows that \(f_r\) and \(f_r^*\) are not proportional.

Write \(x=3/2\) and \(A=x^N\).
The finite geometric sums give
\[
 f_r(x)=2-x^r,\qquad f_r^*(x)=4-3x^r,
 \qquad H_{r,N}(x)=(3-A)x^r+2A-4.
\]
For \(r\ge3\) and \(N\ge4\), we have \(A\ge81/16>3\), and therefore
\[
 H_{r,N}(3/2)\le \frac{49}{8}-\frac{11A}{8}
                       \le-\frac{107}{128}<0.
\]
At the other endpoint,
\[
                   H_{r,N}(2)=2^N+2^{r+1}-3>0.
\]
There is a positive exterior root between these endpoints.
The [circle-root argument](../ledger/Yin_L_G0462_v111.md#cofactor) gives at most one exterior root, counting multiplicity, without a large-delay hypothesis: for \(0<s<1\), Rouché's theorem on the unit circle applies to \(z^Nf_r-sf_r^*\), and passage to \(s=1\) preserves that upper bound.
Thus this root is unique and simple.

The anti-reciprocity of \(H_{r,N}\) gives its inverse as the sole interior root.
The polynomial is monic with constant \(-1\).
Every monic irreducible factor therefore has constant of absolute value one, so the factor \(P_{r,N}\) containing the exterior root must also contain its inverse.
It is reciprocal, and the remaining cofactor is cyclotomic by the [same factor argument](../ledger/Yin_L_G0462_v111.md#cofactor).
The degree of \(P_{r,N}\) cannot be two: a reciprocal quadratic unit with a positive root greater than one has the form \(z^2-az+1\) with an integer \(a\ge3\), whose exterior root exceeds two.
Hence \(P_{r,N}\) is a Salem minimal polynomial of degree at least four, and \(m(P_{r,N})=\log\alpha_{r,N}>\log(3/2)\).

<a id="degree"></a>
## Counting the cofactor uniformly, including repeated torsion roots

Here is a uniform variant of the degree estimate in [L462v111](../ledger/Yin_L_G0462_v111.md#cofactor).
Let \(f\) be a nonreciprocal monic Pisot minimal polynomial of degree \(r\), let \(g=f^*\), and suppose \(H=z^Nf-g\) has an exterior root, with \(N>0\).
The torsion calculation there bounds the number of distinct torsion roots of \(H\) by \(10r\), for each individual delay, before any exceptional delays for repetition are removed.
Indeed, its three nonzero cleared-denominator equations have degrees at most \(4r,4r,2r\).
Their nonvanishing follows from the pole at the unique positive exterior root of \(f\); that argument is independent of a lower bound on \(N\).

Put
\[
 D(z)=Nf(z)g(z)+z\bigl(f'(z)g(z)-f(z)g'(z)\bigr).
\]
The direct identity
\[
              D=zfH'-(Nf+zf')H                              \tag{3}
\]
shows that \(\gcd(H,H')\) divides \(D\).
The derivative terms of degree \(2r\) cancel each other, whereas \(Nfg\) has a nonzero term of that degree, so \(D\ne0\) and \(\deg D=2r\).
Every torsion root of multiplicity \(e\) contributes \(e-1\) to this gcd.
Thus the total degree of the cyclotomic cofactor is at most \(10r+2r=12r\), including all multiplicities and all delays under consideration.
Since \(\deg H=N+r\), the exterior minimal factor has degree at least \(N-11r\).
Applying this with \(r=p\) proves (1).

<a id="norm"></a>
## A prime norm leaves no nontrivial trace resultant

Let \(\zeta\) be a primitive \(p\)-th root of unity.
The complete geometric sum vanishes, so
\[
 f_p(\zeta)=1,
 \qquad f_p^*(\zeta)=\zeta^p f_p(\zeta^{-1})=1,
 \qquad H_{p,N}(\zeta)=\zeta^N-1.
\]
If \(p\nmid N\), taking absolute norms in \(\mathbb Q(\zeta)\) gives
\[
       |\operatorname{Res}(H_{p,N},\Phi_p)|=p.
\]
The integer factorization \(H_{p,N}=P_{p,N}C_{p,N}\) therefore shows that the positive integer \(|\operatorname{Res}(P_{p,N},\Phi_p)|\) divides \(p\).
For a reciprocal Salem polynomial the [trace identity](Yin_C_G0899_v5.md#local) makes this integer exactly \(B_p(P_{p,N})^2\).
Its being a square divisor of the prime \(p\) forces \(B_p(P_{p,N})=1\).
The positive integer \(G_p\) divides \(B_p\), so it too equals one.
The root bound now proves (2).

<a id="scope"></a>
## What remains open for a varying seed

The counterexample obstructs uniform recovery at a prime comparable to, or smaller than, an allowed seed degree.
It does not exclude a prime chosen after seeing the seed, a common prime above the seed-degree cap, or a slower increasing seed envelope supplied together with additional arithmetic estimates.
The rate theorem for [every fixed finite seed list](Yin_C_G0899_v6.md#statement) remains unchanged.
The present outputs have measure greater than \(\log(3/2)\), so they neither produce near-one Salem numbers nor obstruct a rate theorem restricted to a sufficiently small Mahler shell.

For bounded seed degree and coefficient height there are finitely many seeds, but this observation and the fixed-list theorem provide no explicit function of the delay for a growing bound.
In particular the [S-unit overlap estimate used in C899v5](Yin_C_G0899_v5.md#overlap) has an input-dependent onset, and the present calculation supplies no effective uniform replacement.
A quantified positive result must state its seed-degree, height and prime-window relationship as well as control its varying arithmetic inputs.

## Assessment history

### Decision varying-seed-prime-obstruction-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-17T18:52 |
| status | open |
| reason | Submit an explicit height-one varying-seed obstruction to uniform recovery at a prescribed sublinear prime, with a degree estimate that retains repeated torsion roots. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact prime-order failure](#statement) | All odd prime seed degrees, all stated delays, the actual Salem factor and its degree, and the quantified uniformity obstruction. |
| argument | [Salem factor](#salem) | Multinacci seed applicability, explicit exterior interval, irreducible reciprocal factor and exclusion of degree two. |
| argument | [Uniform degree](#degree) | Distinct torsion roots and the full excess multiplicity bound at every delay with an exterior root. |
| argument | [Prime norm](#norm) | Exact root-of-unity evaluation, square trace resultant and the trivial common modulus. |
| argument | [Scope](#scope) | The distinction from a seed-dependent prime, a smaller seed envelope and a near-one family. |
| dependency | [Multinacci roots](Yin_C_G0021_v1.md#multinacci-local-roots-irreducibility-and-measure) | Minimality, the Pisot property and the root interval for each degree at least two. |
| dependency | [Circle and torsion calculations](../ledger/Yin_L_G0462_v111.md#cofactor) | The at-most-one exterior-root argument, cyclotomic factorization and the count of distinct torsion roots before removing repetition exceptions. |
| dependency | [Trace resultant](Yin_C_G0899_v5.md#local) | Square norm for a reciprocal polynomial and divisibility of every integer-value gcd by the trace resultant. |

### Decision varying-seed-prime-obstruction-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T19:00 |
| status | proved |
| reason | Accept the independently checked all-delay cofactor bound and varying-seed counterexample with the clarified sufficiently-large-index scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact prime-order failure](#statement) | All odd prime seed degrees, all stated delays, the actual Salem factor and its degree, and the quantified uniformity obstruction. |
| argument | [Salem factor](#salem) | Multinacci seed applicability, explicit exterior interval, irreducible reciprocal factor and exclusion of degree two. |
| argument | [Uniform degree](#degree) | Distinct torsion roots and the full excess multiplicity bound at every delay with an exterior root. |
| argument | [Prime norm](#norm) | Exact root-of-unity evaluation, square trace resultant and the trivial common modulus. |
| argument | [Scope](#scope) | The distinction from a seed-dependent prime, a smaller seed envelope and a near-one family. |
| dependency | [Multinacci roots](Yin_C_G0021_v1.md#multinacci-local-roots-irreducibility-and-measure) | Minimality, the Pisot property and the root interval for each degree at least two. |
| dependency | [Circle and torsion calculations](../ledger/Yin_L_G0462_v111.md#cofactor) | The at-most-one exterior-root argument, cyclotomic factorization and the count of distinct torsion roots before removing repetition exceptions. |
| dependency | [Trace resultant](Yin_C_G0899_v5.md#local) | Square norm for a reciprocal polynomial and divisibility of every integer-value gcd by the trace resultant. |
| review | [Independent review](../audits/reviews/Yin_R_G1114_v104.md#varying-seed-prime-obstruction-whole) | Entire corrected claim, norm and common modulus, multiplicities and asymptotic quantifiers. |

## Current assessment

[Selected decision](#decision-varying-seed-prime-obstruction-reviewed)
