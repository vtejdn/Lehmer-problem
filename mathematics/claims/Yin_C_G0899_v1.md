---
author: Yin
---

# Large prime factors of primitive cyclic resultants in a linear window

<a id="statement"></a>
## An elementary sieve for the primes dividing the return

Let \(P\in\mathbb Z[z]\) be primitive of degree \(d\), without roots of unity, and let \(m(P)=\log M(P)>0\).
Fix \(A\ge1\) and \(0<\delta<e^{-1/(2A)}/3\).
For all sufficiently large \(d\), a positive proportion of integer orders \(Ad\le j\le2Ad\) are composite and satisfy both
\[
              \log D_j(P)\ge c_{A,\delta}d\,m(P),
        \qquad
              \ell\mid D_j(P)\ \Longrightarrow\ \ell>d^\delta
              \quad\text{for every rational prime }\ell ,
\]
where \(D_j(P)=|\operatorname{Res}(P,\Phi_j)|\).
The proportion and the positive constant are independent of the coefficients, multiplicities and factorization of \(P\).
In particular one may take \(A=1\) and \(\delta=1/5\).
Every exponent below \(1/3\) works at some fixed linear scale \(A\).

For a positive integer \(n\), write \(n_{>x}=\prod_{\ell>x}\ell^{v_\ell(n)}\), the product over rational primes.
Put \(C_j(P)=|\operatorname{Res}(P,z^j-1)|\).
For either choice \(V_j=D_j,C_j\), a uniform positive Lehmer gap for algebraic units is equivalent to the following single-order assertion:
there is an absolute \(c>0\) such that every nontorsion algebraic unit of sufficiently large degree \(d\), with minimal polynomial \(P\), has some \(d\le j\le2d\) with \(\log (V_j(P))_{>d^{1/5}}\ge cd\).
One may require \(j\) composite in this assertion.
The gap and the single-order assertion are both unresolved.

<a id="orders"></a>
## Orders containing one large prime

Choose constants \(1/2<\beta<\alpha<1\) with \(3\delta<\beta\) and \(\log(\alpha/\beta)>1/(2A)\).
This is possible since \(e^{-1/(2A)}>1/2\) for \(A\ge1\).
Choose \(\gamma>\delta\) with \(2\gamma+\delta<\beta\).
Consider the integers \(j\in[Ad,2Ad]\) divisible by a prime \(r\) between \(d^\beta\) and \(d^\alpha\).
There is at most one such prime per order since \(d^{2\beta}>2Ad\) eventually.
These \(j\) are composite, and their number is
\[
                         Ad\big(\log(\alpha/\beta)+o(1)\big).
\]
Indeed each prime contributes \(Ad/r+O(1)\) multiples and the accumulated endpoint error is \(O(d^\alpha)=o(d)\).
For the reciprocal-prime sum one needs only \(\sum_{p\le X}(\log p)/p=\log X+O(1)\).
For integer \(X\) this follows by expanding \(\log(X!)\) over prime powers, dropping \(O(X)\) in the floor errors by the [elementary Chebyshev bound](../ledger/Yin_L_G0462_v54.md#all-units), and bounding the terms of power at least two by \(X\sum_p(\log p)/(p(p-1))=O(X)\).
Stirling's estimate or integral comparison then gives the formula, and partial summation over the indicated interval yields \(\log(\alpha/\beta)+O(1/\log d)\).

Discard primes \(r\) for which some rational prime \(\ell\le d^\delta\) has multiplicative order at most \(d^\gamma\) modulo \(r\).
These rational primes differ from \(r\).
Every discarded \(r\) divides the product of the integers \(\ell^k-1\) for primes \(\ell\le d^\delta\) and \(1\le k\le d^\gamma\).
Its logarithm is at most \(O(d^{2\gamma}\sum_{\ell\le d^\delta}\log\ell)=O(d^{2\gamma+\delta})\).
Since \(\log r\ge\beta\log d\), there are \(O(d^{2\gamma+\delta}/\log d)\) discarded primes \(r\).
They affect \(O_A(d^{1-\beta})\) orders each and hence \(o(d)\) orders altogether.

<a id="residues"></a>
## The cost in degree of each remaining small prime

For each remaining \(j\), its distinguished prime \(r\) satisfies \(\operatorname{ord}_r(\ell)>d^\gamma\) for all primes \(\ell\le d^\delta\).
If such an \(\ell\) divides \(D_j(P)\), write \(j=u\ell^k\), \(\ell\nmid u\).
The [cyclotomic reduction identity](../ledger/Yin_L_G0462_v54.md#cyclotomic-clearing) gives a common root of \(\Phi_u\) and \(P\) in an algebraic closure of \(\mathbb F_\ell\), of multiplicative order exactly \(u\).
The implication holds even when the leading coefficient of \(P\) vanishes modulo \(\ell\), since \(\Phi_j\) is monic and the resultant is the product of evaluations at its roots up to sign.
Primitivity ensures that \(P\) is a nonzero polynomial after reduction.
The common root belongs to an irreducible factor of this reduction of degree \(f\), with \(u\mid\ell^f-1\).
Since \(r\mid u\), one has \(f\ge\operatorname{ord}_r(\ell)>d^\gamma\).

For fixed \(\ell\), at most \(d^{1-\gamma}\) distinct irreducible factors of \(P\bmod\ell\) have degree this large.
The roots of each factor have one order \(u\), so it can account for at most two indices \(j=u\ell^k\) in a closed dyadic interval.
This includes all powers of \(\ell\) in \(j\) and does not bound the \(\ell\)-adic valuation when an incidence occurs.
Over all primes \(\ell\le d^\delta\) the total number of affected orders is \(O(d^{1+\delta-\gamma})=o(d)\).

We therefore retain \(Ad(\log(\alpha/\beta)+o(1))\) orders with no small prime divisor of \(D_j\).
The [linear-window estimate](../ledger/Yin_L_G0462_v70.md#linear) loses at most \(d/2+o(d)\) orders for \(\log D_j=(1+o(1))\varphi(j)m(P)\).
There is a fixed positive margin because \(A\log(\alpha/\beta)>1/2\).
The [bounded mean of \(j/\varphi(j)\)](../ledger/Yin_L_G0462_v54.md#exceptional-orders) permits discarding the \(O_A(\eta d)\) orders with \(\varphi(j)<\eta d\) for a sufficiently small fixed \(\eta>0\).
This proves the asserted positive proportion and size simultaneously.

<a id="criterion"></a>
## Large prime divisors remove the exceptional power-substitution orders

If \(m(P)\) has a uniform positive lower bound, apply the result just proved with \(A=1,\delta=1/5\).
All prime factors of \(D_j\) are then included in its large-prime part, and \(D_j\mid C_j\).
Either choice of \(V_j\) yields the required inequality for a positive proportion of composite orders.

Conversely fix the monic minimal polynomial \(Q\) of an arbitrary nontorsion unit of degree \(D\).
For every sufficiently large prime \(p\), \(Q(z^p)\) is the minimal polynomial of a nontorsion unit of degree \(d=Dp\) by the [irreducible power-substitution argument](../ledger/Yin_L_G0462_v60.md#lifts).
If \(d\le j\le2d\) and \(p\mid j\), write \(j=kp\) with \(D\le k\le2D\).
The power map on primitive roots, or on all roots, gives \(V_{kp}(Q(z^p))\) equal to a positive integral power of \(V_k(Q)\).
The latter are finitely many fixed nonzero integers, independent of \(p\).
For large \(p\) their prime factors are all below \(d^{1/5}\), so these exceptional orders contribute zero large-prime logarithm.
At every remaining \(j\), raising roots to the \(p\)-th power permutes the chosen orbit and \(V_j(Q(z^p))=V_j(Q)\).
For fixed \(Q\) the [same fixed-polynomial estimates](../ledger/Yin_L_G0462_v60.md#lifts) give \(\log D_j(Q)/\varphi(j)\to m(Q)\) and \(\log C_j(Q)/j\to m(Q)\).
Hence a witness of large-prime logarithm at least \(cd\) implies \(m(Q)\ge c/2\), since both normalizing denominators are at most \(2d\).
This proves the converse even for a single witness with no restriction on its order other than membership in the interval.

## Assessment history

### Decision large-prime-return-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:11 |
| status | open |
| reason | Register the sieve for the rational prime divisors of primitive resultants and the single-order equivalence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Prime factors and equivalence](#statement) | Positive proportion, polynomial cutoff, and both forms of the single-order criterion. |
| argument | [Order primes](#orders) | Prime sum and simultaneous removal of small multiplicative orders. |
| argument | [Finite field degrees](#residues) | Factor count, dyadic multiplicity, geometric loss and size of the primitive resultant. |
| argument | [Single-order test](#criterion) | Elimination of low-order power-substitution witnesses by the prime cutoff. |
| dependency | [Linear approximation](../ledger/Yin_L_G0462_v70.md#linear) | Primitive relative asymptotics after at most one deleted order per nonreal conjugate pair plus a density-zero set. |
| dependency | [Prime count](../ledger/Yin_L_G0462_v54.md#all-units) | Elementary Chebyshev estimates used in the prime sums. |
| dependency | [Cyclotomic reduction](../ledger/Yin_L_G0462_v54.md#cyclotomic-clearing) | Multiplicative order after reduction in the order characteristic. |
| dependency | [Totient mean](../ledger/Yin_L_G0462_v54.md#exceptional-orders) | Removing small totients from a positive-density set. |
| dependency | [Power substitutions](../ledger/Yin_L_G0462_v60.md#lifts) | Irreducibility, exact orbit sampling, and the fixed-polynomial limit. |

### Decision large-prime-return-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:19 |
| status | proved |
| reason | Adopt the sieve and the two single-order equivalences after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Prime factors and equivalence](#statement) | Positive proportion, polynomial cutoff, and both forms of the single-order criterion. |
| argument | [Order primes](#orders) | Prime sum and simultaneous removal of small multiplicative orders. |
| argument | [Finite field degrees](#residues) | Factor count, dyadic multiplicity, geometric loss and size of the primitive resultant. |
| argument | [Single-order test](#criterion) | Elimination of low-order power-substitution witnesses by the prime cutoff. |
| dependency | [Linear approximation](../ledger/Yin_L_G0462_v70.md#linear) | Primitive relative asymptotics after at most one deleted order per nonreal conjugate pair plus a density-zero set. |
| dependency | [Prime count](../ledger/Yin_L_G0462_v54.md#all-units) | Elementary Chebyshev estimates used in the prime sums. |
| dependency | [Cyclotomic reduction](../ledger/Yin_L_G0462_v54.md#cyclotomic-clearing) | Multiplicative order after reduction in the order characteristic. |
| dependency | [Totient mean](../ledger/Yin_L_G0462_v54.md#exceptional-orders) | Removing small totients from a positive-density set. |
| dependency | [Power substitutions](../ledger/Yin_L_G0462_v60.md#lifts) | Irreducibility, exact orbit sampling, and the fixed-polynomial limit. |
| review | [Independent review](../audits/reviews/Yin_R_G1114_v66.md#large-prime-return-review) | Sieve exponent range, uniformity, local factor count and the fixed-base obstruction to exceptional witnesses. |

## Current assessment

[Selected decision](#decision-large-prime-return-reviewed)
