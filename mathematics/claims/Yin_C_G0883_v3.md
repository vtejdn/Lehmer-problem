---
author: Yin
---

# Arithmetic lower bounds for the least volume realizing a homological polynomial

<a id="statement"></a>
## Volume and the support of cyclotomic multiples

Let \(P\) be the whole monodromy polynomial of a closed orientable hyperbolic surface bundle, with closed connected orientable fiber and orientation-preserving monodromy.
Define \(\sigma(P)=\min_C |\operatorname{supp}(PC)|\), where \(C\) is a monic product of cyclotomic polynomials with repetitions allowed, including \(C=1\).
This minimum counts nonzero coefficients after collection. [Cyclotomic completions](Yin_C_G0221_v1.md)
Write \(V_{\min}(P)\) for the infimum of volumes of all such realizations.
There is an absolute \(b>0\) such that
\[
                \log\sigma(P)\ \le\ b V_{\min}(P).
\]
More concretely, each realization of volume \(V\) supplies a cyclotomic completion with at most \(\exp(bV)\) nonzero terms.
Its multiplier can be taken to be two geometric sums \((t^{|a|}-1)/(t-1)\), \((t^{|a'|}-1)/(t-1)\), times at most \(b'V\) binomials \(t^{|c|}-1\), with \(a,a',c\ne0\) and \(b'\) absolute.
For \(M(P)>1\), enlarging an absolute constant \(B\) if needed, this entails
\[
              M(P)-1\ \ge\ \exp\{-\exp(\exp(B(1+V_{\min}(P))))\}.
\]
Thus the measured value \(M(P)\) itself gives a lower bound growing at least as a constant times \(\log\log\log(1/(M(P)-1))\) up to an additive constant when this expression is defined and positive.
Also \(\sigma(P)\ge1+\max(R_+,R_-)\), where \(R_\pm\) count positive and negative real zeros respectively, with multiplicity, by applying Descartes' rule of signs to each completed polynomial at \(t\) and at \(-t\).
These statements concern the original polynomial, including irreducible reciprocal strict records via the [mapping-torus realization](Yin_C_G0883_v2.md#mapping-tori).

<a id="columns"></a>
## Clearing one row per core circle

By [Kobayashi and Rieck, Corollary 1.3](../audits/literature/KR11/readme.md), the realization is obtained by Dehn filling a compact link exterior with at most \(K V\) tetrahedra for a universal \(K\).
A bounded number of barycentric subdivisions per simplex, if needed, gives a genuine triangulation at universal multiplicative cost.
Denote its tetrahedron count by \(t_0\).
Use the [cellular filling construction and end minors](Yin_C_G0883_v2.md#bounded-volume) for the fibration character over \(\mathbb Z[t^{\pm1}]\).
The square complementary minor \(B_0\) of \(\partial_2\) has size \(s\le C_0t_0\), since each original simplex contributes boundedly many cells, also on the boundary cylinders.
The end minors are signed Laurent monomials times \(t^a-1,t^{a'}-1\).
Up to a signed Laurent unit, \(\det B_0=P(t)(t^a-1)(t^{a'}-1)/(t-1)^2\).

The potentially long geometric sums occur in the row of the target core edge of each mapping cylinder.
For each such row present in the minor and having nonzero core value \(c\), multiply that row alone by \(t^c-1\).
An old triangle column still contributes at most three signed monomials distributed among its entries.
A prism over a boundary edge has two vertical sides, the old edge, and the path around its own core.
The first three contribute at most three monomials in total and avoid all target-core rows.
Clearing the core entry leaves at most two monomials, since it was a monomial times \((t^{kc}-1)/(t^c-1)\) for a winding number \(k\).
If \(c=0\), the core entry already has at most one monomial with integral coefficient \(\pm k\).
Deleting rows cannot increase these counts.
A determinant term must choose one summand from each column, so the resulting nonzero determinant has at most \(5^s\) monomials even before like exponents are collected.
Up to a signed Laurent unit this determinant is the stated completion of \(P\), giving the claimed multiplier and support estimates independently of the filling coefficients.
For a nonzero norm gap apply [Dobrowolski, Theorem 1](../audits/literature/Dob06/Yin_U001.md#sparse-measure) to the complete determinant.
At \(k\ge2\) terms its multiplicative measure minus one is at least \(\exp(-a_0 3^{\lfloor(k-2)/4\rfloor}k^2\log k)\) with an absolute \(a_0\).
Every added binomial or geometric sum has measure one.
Substituting \(k\le\exp(bV)\) and then taking realizations approaching the infimal volume gives the bound in the statement.

<a id="cyclic-homology"></a>
## What all cyclic homology ranks can force

Suppose \(P\) is monic reciprocal irreducible noncyclotomic of degree \(2g\ge4\) and is not a polynomial in \(t^k\) for \(k>1\).
There is a single closed hyperbolic realization of this whole polynomial which minimizes \(b_1(M_{f^j};\mathbb F_p)\) simultaneously over all realizations, for every prime \(p\) and \(j\ge1\).
The minimum equals \(1+\deg\gcd(\bar P,t^j-1)\), where reduction and gcd are over \(\mathbb F_p\).
In particular the supremum over \(p,j\) of the excess above one divided by \(j\) is at most one for this same realization.
This gives a ceiling for a lower-bound argument based on cyclic mod-\(p\) Betti numbers per covering degree, even allowing the prime and cover to depend on \(P\).

To construct the integral lattice, in \(\mathbb Z[x]/P\) use the basis \(1,x,\ldots,x^{2g-1}\).
Take the doubly infinite integral sequence \(u_k\) satisfying the recurrence with polynomial \(P\), specified by \(u_{-g}=-1\) and \(u_k=0\) for \(-g<k<g\).
The monic and constant coefficients of \(P\) both equal one, so the sequence extends uniquely in both directions and \(u_g=1\).
Reciprocity and uniqueness of the extension give \(u_{-k}=-u_k\).
The form \(\langle x^i,x^j\rangle=u_{j-i}\) descends to the quotient in both variables by the recurrence and reciprocity, and is invariant under multiplication by \(x\).
Its two diagonal \(g\)-by-\(g\) blocks vanish, and its upper right block is triangular with diagonal one.
The form is unimodular alternating and thus has an integral symplectic basis.
In this basis multiplication by \(x\) lifts to a pseudo-Anosov map by the [homological criterion](../audits/literature/MS07/readme.md).
On its cyclic covers the fiber coinvariants modulo \(p\) are precisely \(\mathbb F_p[x]/(\bar P,x^j-1)\).
The additional base-circle summand supplies the asserted first Betti number.

For any other integral homology action with characteristic polynomial \(P\), decompose each \(h\)-primary component over \(\mathbb F_p\) into cyclic blocks of lengths \(a_i\) for a monic irreducible \(h\).
If \(v_h(x^j-1)=t\), that component contributes \(\deg h\sum_i\min(t,a_i)\), at least \(\deg h\min(t,\sum_i a_i)\).
Summing proves the optimality simultaneously, including repeated roots and \(p\mid j\).
This calculation leaves the sizes of torsion groups and invariants of other coverings available for separate tests.

## Assessment history

### Decision volume-from-cyclotomic-support

| Field | Value |
| --- | --- |
| date | 2026-11-27T12:07 |
| status | proved |
| reason | The volume bound and the cyclic homology minimum follow from the checked column count, sparse-polynomial estimate and integral cyclic symplectic model. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Volume bounds](#statement) | Support of a cyclotomic multiple, the Mahler gap and real-root counts for the full polynomial. |
| argument | [Filling determinant](#columns) | Clearing each core row once in a triangulation of linear size. |
| argument | [Cyclic ranks](#cyclic-homology) | One integral realization minimizes all cyclic ranks simultaneously. |
| dependency | [Filling model](Yin_C_G0883_v2.md#bounded-volume) | The end minors and normalized integral torsion of the fibered class. |
| dependency | [Sparse estimate](../audits/literature/Dob06/Yin_U001.md#dob06-u001) | Quantitative bound for the full cyclotomic completion. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1279.md#finding) | All three sections and their source interfaces. |

## Current assessment

[Selected decision](#decision-volume-from-cyclotomic-support)
