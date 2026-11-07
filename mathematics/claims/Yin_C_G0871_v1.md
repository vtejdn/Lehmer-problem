---
author: Yin
---

# An indivisible residue block for each Frobenius orbit in the odd-prime square family

<a id="statement"></a>
## Degree restriction

Let \(p\) be an odd prime, let \(\rho=\operatorname{ord}_p(2)\), and put
\[
 A=(z-1)\Phi_{8p}(z),\quad B=(z+1)\Phi_{4p}(z)^2,\quad H_p=(A^2+B^2)/2.
\]
In any factorization of \(H_p\) into monic irreducibles over the integers, each irreducible factor of \(\overline{\Phi_p}\) in \(\mathbb F_2[z]\) occurs with its full exponent eight in exactly one factor reduction.
The exponent two of \(z+1\) likewise occurs in a single factor reduction.
The polynomial \(H_p\) is squarefree over \(\mathbb Q\).
Every irreducible factor has degree \(8\rho a+\delta\) with \(a\ge1\) and \(\delta\in\{0,2\}\), and precisely one factor has \(\delta=2\).
There are at most \((p-1)/\rho\) factors, so \(H_p\) is irreducible when \(\rho=p-1\).
If the factor is reciprocal and \(\rho\) is odd, its degree has the stronger form \(16\rho a+\delta\) with \(a\ge1\).

<a id="argument"></a>
## Proof by an integral resultant

We use the [odd-prime construction and its endpoint and reduction identities](../ledger/Yin_L_G0458_v4.md#prime-square-family-inputs).
These give a monic integral polynomial with \(H_p(0)=1,\ H_p(1)=2\), and \(\bar H_p=(z+1)^2\overline{\Phi_p}^{\,8}\).
We also use the [exclusion of factors supported only at the binary root one](../ledger/Yin_L_G0458_v4.md#prime-square-residue-degree).
The new argument concerns the allocation of all eight copies of each primitive binary factor.

Set \(D=\mathbb Z[\zeta]\) for a primitive \(p\)-th root \(\zeta\).
Both \(1+\zeta^4\) and \(1+\zeta^2\) are units since their norms are \(\Phi_p(-1)=1\).
The quotient formulas for the cyclotomic inputs give
\[
 H_p(\zeta)=2(u^2+4v^2),\qquad
 u=\frac{\zeta-1}{1+\zeta^4},\quad v=\frac{\zeta+1}{(1+\zeta^2)^2}.
\]
Here \(D/2D=\mathbb F_2[z]/(\overline{\Phi_p})\), a product of fields since \(z^p-1\) is separable in characteristic two.
The element \(\bar u\) is a unit there since \(1\) is not a root of \(\overline{\Phi_p}\).
Multiplication by \(u^2+4v^2\) on the free abelian group \(D\) therefore has odd determinant.
Taking determinants gives
\[
 v_2\!\left(|\operatorname{Res}(\Phi_p,H_p)|\right)=p-1.
\tag{1}
\]

Write \(H_p=\prod_i f_i\), with each appearance of a monic irreducible factor listed separately, and let \(b_i=\deg\gcd(\bar f_i,\overline{\Phi_p})\).
Multiplication by \(f_i(\zeta)\) on \(D/2D\) has kernel dimension \(b_i\) over \(\mathbb F_2\), by the product of fields description.
An integer matrix of rank defect \(b_i\) modulo two has determinant divisible by \(2^{b_i}\), as follows by row elimination modulo two with integer row additions and swaps.
Thus \(v_2(|\operatorname{Res}(\Phi_p,f_i)|)\ge b_i\).
Each binary irreducible divisor of \(\overline{\Phi_p}\) occurs at least once among the \(\bar f_i\).
Adding the inequalities, using multiplicativity and (1), yields \(p-1\ge\sum_i b_i\ge p-1\).
If any primitive binary factor occurred in two appearances, it would contribute its positive degree twice and make the second inequality strict.
Hence every such factor is confined to one appearance, in which its exponent must be eight.
The same indivisibility at \(z+1\) follows separately: two appearances vanishing at one modulo two would give \(4\mid H_p(1)\).
Thus every binary block in \(\bar H_p\) is indivisible between appearances and a repeated rational factor is impossible.

All irreducible binary factors of \(\overline{\Phi_p}\) have degree \(\rho\), since the Frobenius orbit of a primitive \(p\)-th root has that length.
Every actual \(f_i\) contains at least one of them by the cited exclusion.
Counting degrees proves the formula, the bound on the number of factors and the primitive-root case.
If \(\rho\) is odd, inversion exchanges two different Frobenius orbits because \(-1\notin\langle 2\rangle\) modulo \(p\).
A reciprocal \(f_i\) contains both binary blocks in each such pair, which gives the last assertion.

The degree list is necessary and supplies no factor over the integers.
The [height bound and exact sublinear-degree criterion](../ledger/Yin_L_G0458_v4.md#prime-square-sublinear-factor-criterion) retain their own hypotheses, constants and checking scope.

## Assessment history

### Decision integral-block-allocation

| Field | Value |
| --- | --- |
| date | 2026-11-07T15:57 |
| status | proved |
| reason | The complete resultant argument and the precise scope of the factor-degree restriction passed independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Odd-prime block restriction](#statement) | Block allocation, squarefreeness, factor counts and reciprocal degrees for every odd prime. |
| argument | [Integral resultant argument](#argument) | Determinant valuation, rank defects, endpoint and inverse-orbit count. |
| review | [Whole independent finding](../audits/reviews/Yin_R_G1095_v1.md#integral-block-finding) | Complete statement and argument with their local inputs. |

## Current assessment

[Selected decision](#decision-integral-block-allocation)

