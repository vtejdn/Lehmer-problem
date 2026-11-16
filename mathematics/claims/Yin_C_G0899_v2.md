---
author: Yin
---

# The part of a primitive resultant carried by primes at which the residue order equals the sampled order

<a id="statement"></a>
## Exact orders on a positive proportion of the linear window

Let \(P\) be the monic minimal polynomial of a nontorsion algebraic unit of degree \(d\), with positive logarithmic Mahler measure \(m(P)\le1\).
Fix \(A\ge1\) and \(0<\delta<e^{-1/(2A)}/3\).
Put \(D_j=|\operatorname{Res}(P,\Phi_j)|\) and define
\[
       T_j(P)=\sum_{\substack{\ell>d^\delta\\ \ell\nmid j}}
                     v_\ell(D_j)\log\ell ,
\]
where \(\ell\) runs over rational primes.
For a positive proportion of composite \(j\in[Ad,2Ad]\), uniformly over \(P\) as \(d\to\infty\),
\[
        T_j(P)=(1+o(1))\log D_j
              \quad\text{and}\quad \log D_j\gg_{A,\delta}d\,m(P).
\]
Each contributing prime has a root of \(P\bmod\ell\) of multiplicative order exactly \(j\) in a finite field of characteristic \(\ell\).
Other roots of the same polynomial modulo that prime may have different orders.

In particular take \(A=1,\delta=1/5\).
A uniform positive Lehmer gap for nontorsion units is equivalent to the existence of an absolute \(c>0\) such that every sufficiently large-degree nontorsion unit with \(m(P)\le1\) has one \(d\le j\le2d\) with \(T_j(P)\ge cd\).
The witness may be required to be composite.
The theorem produces a lower bound proportional to \(d\,m(P)\); finding a degree-proportional lower bound independent of \(m(P)\) is open.

<a id="local"></a>
## A local calculation at a prime dividing the order

Write \(j=u\ell^a\) with \(a\ge1\) and \(\ell\nmid u\).
For each primitive \(u\)-th root \(\xi\) in an algebraic closure of \(\mathbb F_\ell\), let \(h_\xi\ge0\) be its multiplicity as a root of \(P\bmod\ell\).
If every such \(h_\xi<\varphi(\ell^a)\), then exactly
\[
                         v_\ell(D_j)=\sum_{\xi}h_\xi .                  \tag{1}
\]
In a finite unramified extension of \(\mathbb Q_\ell\) containing the \(u\)-th roots of unity, each \(\xi\) has a unique lift \(\tilde\xi\) of order \(u\) by the simple roots of \(z^u-1\) and Hensel lifting.
Every primitive \(j\)-th root has a unique expression \(\tilde\xi\lambda\) with \(\lambda\) a primitive \(\ell^a\)-th root.
With \(v_\ell(\ell)=1\), \(v_\ell(\lambda-1)=1/\varphi(\ell^a)\), as follows by Eisenstein's criterion for \(\Phi_{\ell^a}(1+z)\).
In the expansion \(P(\tilde\xi+z)=\sum c_s z^s\), the coefficient \(c_{h_\xi}\) is a unit and all lower coefficients belong to \(\ell\) times the unramified integer ring.
At \(z=\tilde\xi(\lambda-1)\), the term of index \(h_\xi\) has valuation \(h_\xi/\varphi(\ell^a)<1\).
All lower terms have valuation at least one, and all higher terms have strictly higher valuation by integrality.
This computes the valuation of each evaluation, including \(h_\xi=0\).
Summing over the \(\varphi(\ell^a)\) lifts of each \(\xi\) in the cyclotomic resultant proves (1).

<a id="discriminant"></a>
## Controlling exceptional multiplicities across the whole window

Let \(E_\ell=\sum_{\xi:\,h_\xi>0}(h_\xi-1)\), now summing over all distinct roots of \(P\bmod\ell\).
Then \(E_\ell\le v_\ell(|\operatorname{disc}P|)\).
Indeed multiplication by \(P'\) on the integral algebra \(\mathbb Z[z]/P\) has determinant the discriminant up to sign.
Its reduction has kernel dimension \(\deg\gcd(\bar P,\bar P')\), which is at least \(E_\ell\), also in inseparable reductions.
The integer elementary divisors of the multiplication matrix show that this dimension is at most the valuation of the nonzero determinant.
The complex Vandermonde determinant and Hadamard's row bound give
\[
        \sum_\ell E_\ell\log\ell\le\log|\operatorname{disc}P|
            \le d\log d+2(d-1)m(P).
\]
Indeed each root \(\alpha\) gives a row of norm at most \(\sqrt d\max(1,|\alpha|)^{d-1}\).

Discard an order \(j\) if for some \(\ell>d^\delta\) dividing \(j\) a root of order \(j/\ell^{v_\ell(j)}\) has multiplicity at least \(\varphi(\ell^{v_\ell(j)})\).
Such a root contributes at least \(\ell-2\) to \(E_\ell\) and it can affect at most two indices in the closed dyadic interval, because its order is fixed and successive indices differ by a factor \(\ell\).
For \(\ell>d^\delta\), \(\sum E_\ell=O_\delta(d)\) by the discriminant bound and \(m(P)\le1\).
Consequently only \(O_\delta(d^{1-\delta})=o(d)\) orders were discarded.

For each remaining \(j\), apply (1) to each prime \(\ell>d^\delta\) dividing \(j\).
The number of distinct primitive \(u\)-th roots is \(\varphi(u)\le j/\ell\).
The weighted contribution of the first copy of each root to these valuations is bounded above by
\[
                \sum_{\substack{\ell\mid j\\\ell>d^\delta}}
                       (j/\ell)\log\ell
                  \le j d^{-\delta}\log j .
\]
The remaining copies contribute a nonnegative error whose sum over all remaining orders is at most \(2\sum_\ell E_\ell\log\ell\), since each root at each prime has at most two relevant indices.
Thus, outside another \(O_{A,\delta}(d^{\delta/2}\log d)=o(d)\) orders, the total logarithm from primes \(\ell>d^\delta\) dividing \(j\) is \(O_{A,\delta}(d^{1-\delta}\log d+d^{1-\delta/2})\).
This is \(o(d\,m(P))\) uniformly by the [degree-dependent Mahler bound](Yin_C_G0147_v5.md#argument).

<a id="transfer"></a>
## From unrestricted prime divisors to exact residue order

The [large-prime sieve](Yin_C_G0899_v1.md#statement) supplies a positive proportion of composite \(j\) with \(\log D_j\gg_{A,\delta} d\,m(P)\) and no prime divisor at most \(d^\delta\).
On these orders the only logarithm omitted from \(T_j\) comes from primes dividing \(j\).
Removing the two density-zero sets above gives the relative estimate in the statement.
When \(\ell\nmid j\), the roots of \(\Phi_j\bmod\ell\) have exact order \(j\) by separability of \(z^j-1\); divisibility of the resultant forces a common root with \(P\bmod\ell\).

Under a positive Lehmer gap the estimate just proved gives the requested single witness at \(A=1,\delta=1/5\).
For the converse fix \(Q\) of a nontorsion unit with \(m(Q)\le1\) and apply the hypothesis to the [irreducible power substitutions](../ledger/Yin_L_G0462_v60.md#lifts) \(Q(z^p)\) for primes \(p\to\infty\), which retain \(m(Q)\).
Since \(T_j\le\log (D_j)_{>d^{1/5}}\), the [single-order power-substitution argument](Yin_C_G0899_v1.md#criterion) gives \(m(Q)\ge c/2\) for each such \(Q\).
All units outside this test range already have \(m(Q)>1\), proving the equivalence for the full unit problem.

## Assessment history

### Decision exact-order-income-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:16 |
| status | open |
| reason | Register the large-prime exact-order contribution and the discriminant estimate removing primes that divide the sampled order. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact residue orders](#statement) | Uniform positive proportion for minimal unit polynomials of measure at most one in logarithmic units, and a single-order unrestricted-gap equivalence. |
| argument | [Local valuation](#local) | Unramified lifts, multiplicities below the ramification threshold, and the exact valuation. |
| argument | [Total multiplicity](#discriminant) | Rank defect, discriminant, exceptional order count and summed valuation error. |
| argument | [Transfer and equivalence](#transfer) | Intersection with the sieve, actual residue orders and both implications. |
| dependency | [Mahler lower estimate](Yin_C_G0147_v5.md#argument) | The power-saving error is negligible relative to the total logarithmic measure scale. |
| dependency | [Positive-proportion sieve](Yin_C_G0899_v1.md#statement) | Large primitive return whose prime divisors all exceed the power cutoff. |
| dependency | [Single-order converse](Yin_C_G0899_v1.md#criterion) | Fixed base values at the resonant orders and convergence at the other orders. |
| dependency | [Irreducible substitutions](../ledger/Yin_L_G0462_v60.md#lifts) | Fixed base measure in the same bounded-measure test class. |

### Decision exact-order-income-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:19 |
| status | proved |
| reason | Adopt the exact residue-order valuation theorem and its uniform-gap equivalence after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact residue orders](#statement) | Uniform positive proportion for minimal unit polynomials of measure at most one in logarithmic units, and a single-order unrestricted-gap equivalence. |
| argument | [Local valuation](#local) | Unramified lifts, multiplicities below the ramification threshold, and the exact valuation. |
| argument | [Total multiplicity](#discriminant) | Rank defect, discriminant, exceptional order count and summed valuation error. |
| argument | [Transfer and equivalence](#transfer) | Intersection with the sieve, actual residue orders and both implications. |
| dependency | [Mahler lower estimate](Yin_C_G0147_v5.md#argument) | The power-saving error is negligible relative to the total logarithmic measure scale. |
| dependency | [Positive-proportion sieve](Yin_C_G0899_v1.md#statement) | Large primitive return whose prime divisors all exceed the power cutoff. |
| dependency | [Single-order converse](Yin_C_G0899_v1.md#criterion) | Fixed base values at the resonant orders and convergence at the other orders. |
| dependency | [Irreducible substitutions](../ledger/Yin_L_G0462_v60.md#lifts) | Fixed base measure in the same bounded-measure test class. |
| review | [Independent review](../audits/reviews/Yin_R_G1114_v69.md#exact-orders) | Local ramification threshold, total discriminant charge, two exceptional sets, and both directions at degree-linear order. |

## Current assessment

[Selected decision](#decision-exact-order-income-reviewed)
