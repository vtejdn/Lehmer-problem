---
author: Yin
---
# Exact linear Hankel valuations from a nonrational residue layer

This fixed result concerns actual local valuations of the original shifted leading Hankel determinants.
It complements [C858 v1](Yin_C_G0858_v1.md#decision-whole-independent-review-2026-11-04), whose separate supplied modulo-eight divisibility theorem and adopted review retain their exact scope.
The coordinating research agent developed the argument for Yin, and the selected assessment adopts its independent whole review at the stated scope.
Neither v1's conditional approximation premise nor an unreviewed working Draft is a premise below.

## Statement

**A. A first nonrational residue layer.**
Let p be a prime, k>=0 an integer, A(x)=sum_(n>=0)a_n x^n in Z_p[[x]], and suppose

    A(x)=a_0+p^k B(x), B in Z_p[[x]], B(0)=0.

Assume Bbar is not rational over F_p(x).
For h>=1 put Delta_h(A)=det(a_(i+j+1))_(0<=i,j<h), and set v_p(0)=infinity.
Then

    v_p(Delta_h(A))>=kh for all h,
    v_p(Delta_h(A))=kh for infinitely many h,                 (HV1)
    liminf_(h->infinity,Delta_h(A)!=0) v_p(Delta_h(A))/h=k,
    liminf_(h->infinity,Delta_h(A)!=0) v_p(Delta_h(A))/h^2=0.

The equality subsequence is part of the conclusion, not a supplied approximation or a numerical observation.

**B. The actual nonzero dyadic class.**
Let P be monic, irreducible, reciprocal and noncyclotomic in Z[t], with degree d>=2, constant term one, and every positive power of a root still of degree d.
Use all original roots alpha_i to define P_n(x)=product_i(1-alpha_i^n x), U=P_2, V=P_4 and G=sqrt(V/U), with G(0)=1.
Write

    r=overline((V-U)/4)/Ubar in F_2(x),

and let c be its normalized reduced Artin--Schreier representative as in C857 v2.
If c!=0, the integer coefficients of the same original G satisfy

    v_2(Delta_h(G))>=h for all h,
    v_2(Delta_h(G))=h for infinitely many h,                  (HV2)

and the two liminf assertions in Part A hold with k=1.
No squarefreeness of Pbar is required.
For squarefree Pbar this is the nonzero branch of C860 v8; its retained Lehmer control is one actual example, not a supplied near-one sequence.

**C. Good odd primes.**
For the same original input, put

    T=2 disc(U) disc(V) Res(U,V),

which is a nonzero integer.
For each prime p not dividing T, infinitely many h satisfy

    v_p(Delta_h(G))=0.                                     (HV3)

The exceptional set and the equality subsequences can depend on P.
The result does not assert a common infinite subsequence for different primes, an upper bound at every index, a bound on the sum over all prime valuations, or any equality for the zero dyadic class.
In particular it does not resolve G0001 or rule out arithmetic using other matrices, selected subsequences or additional primes.

## Exact inputs and source scope

[C857 v2](Yin_C_G0857_v2.md#reduced-representative) supplies the original modulo-four congruence and the normalized rational Artin--Schreier reduction, including its nonzero-class obstruction to a rational solution.
[C860 v8](Yin_C_G0860_v8.md#argument) supplies only the comparison with its squarefree nonzero branch and actual Lehmer control; its minimum-rank theorem is not used to infer an upper bound on actual valuations.
The noncollision argument retained in [C855 v3](Yin_C_G0855_v3.md#the-mesh-estimate-uses-the-actual-integral-squared-polynomial) and [C860 v7](Yin_C_G0860_v7.md#componentwise-pole-rank) gives the needed original power-stable simple roots and nonzero cross-resultant, with the same proof restated below at the general original-input scope.

The only external rationality input is the exact criterion already accepted at [C858 v1's source interface](Yin_C_G0858_v1.md#preparation-and-exact-remaining-inputs): for a formal series over a field, all sufficiently large leading Hankel determinants vanish if and only if the series is rational.
The source is [BNZ22, arXiv:2205.02145v3](../literature/pdf/BNZ22.pdf), Section2.2, printed/PDF pp.4--6, definition, Lemma2.1 and Corollaries2.2--2.3.
For the present characteristic-p use the author additionally read those actual retained passages: Section2.2 explicitly takes k to be an arbitrary field, while the characteristic-zero restriction begins only in Section2.3.
This verifies applicability of the already accepted field-valued criterion; no later D-finite theorem or characteristic-zero differentiation argument is used.
The original complete paper and its external inputs are not newly audited, and no independent source-proof review is asserted.
The finite shifted convention is checked explicitly in the argument below.

## Argument

### The scalar factor and the exact equality subsequence

For every h, each entry of the shifted coefficient Hankel matrix of A is p^k times the corresponding entry for B, since the constant coefficient a_0 does not occur.
Factoring p^k from all h rows gives the exact identity

    Delta_h(A)=p^(kh) Delta_h(B).                            (HV4)

The latter determinant belongs to Z_p, proving the all-index lower bound.
Now Bbar/x belongs to F_p[[x]] because B(0)=0, and it is nonrational because multiplication by x cannot change rationality.
The h-square leading Hankel matrix of this series has entries bbar_(i+j+1), so its determinant is precisely the reduction of Delta_h(B).
The accepted field-valued Kronecker criterion implies that this determinant is nonzero for infinitely many h.
For those h, Delta_h(B) is a p-adic unit and (HV4) gives the equality in (HV1), including nonvanishing of Delta_h(A).
The linear liminf is k because all nonzero determinants have quotient at least k and infinitely many have equality.
The quadratic quotient is nonnegative, and along the equality subsequence it is k/h, which tends to zero.
This proves Part A without assuming an infinite rational-approximation profile or a characteristic-zero field.

### The original dyadic residue is genuinely nonrational

The original congruence V-U in 4Z[x] and U(0)=1 give

    V/U=1+4W/U, W=(V-U)/4 in Z[x], W(0)=0.

The normalized binomial expansion is coefficientwise well defined because W/U has zero constant term.
For j>=1 the rational number 4^j binomial(1/2,j) is an even integer: its denominator is a power of two and its two-adic valuation is the number of ones in the binary expansion of j, which is at least one.
Consequently G=1+2H with H in Z[[x]], H(0)=0.
Squaring gives H+H^2=W/U and hence

    Hbar+Hbar^2=r.                                         (HV5)

If c!=0, the adopted normalized Artin--Schreier reduction excludes a rational solution of (HV5).
Thus Hbar is nonrational over F_2(x), whether or not Ubar has repeated poles.
Part A with p=2,k=1,A=G,B=H proves (HV2) and its actual valuation liminf statements.
This argument does not call on the separate modulo-eight premise of C858 v1, which is not present in this branch.
The specific squarefree control comparison follows from the exact c!=0 computation retained in C860 v8 and is not used for the general proof.

### Good odd reduction and its distinct index sets

Power stability makes the d original squared roots distinct and likewise the fourth-powered roots.
No squared root can equal a fourth-powered root: their positive absolute Weil heights would be 2h_abs(alpha) and 4h_abs(alpha), respectively.
These facts prove that U and V are squarefree and coprime over Q, so T is a nonzero integer.
Their leading and constant coefficients are one, so reduction at any prime preserves degree and the constant-one power-series denominator.
For p not dividing T, Ubar and Vbar are squarefree and coprime over F_p and its algebraic closure.
Thus Vbar/Ubar has simple zeros and poles, and cannot be the square of a rational function over F_p(x): every zero or pole of a rational square has even order.

The already established integral identity G^2=V/U reduces at this p.
If Gbar were rational, its square would give the forbidden rational square representation, so Gbar is nonrational.
Therefore B=G-1 has B(0)=0 and Bbar nonrational.
Part A with k=0 proves (HV3).
Only the finitely many prime divisors of T are excluded.
Each use of the criterion produces an infinite set for its own prime; it supplies no intersection statement between these sets.

### Consequence and exact limitations

For every input in Part B and every eta>0, a lower estimate v_2(Delta_h(G))>=eta h^2 for all sufficiently large h with nonzero determinant is impossible, because (HV2) supplies arbitrarily large h with valuation h.
Likewise at each good odd prime, a strictly positive all-late quadratic valuation lower bound is impossible by (HV3).
These are statements about the actual original leading determinants, stronger at these scopes than a vanishing quadratic coefficient in a selected rational-approximation certificate.
They do not control other primes at the same index, all valuations at all indices, the zero dyadic class, a modified determinant sequence, or a selected subsequence avoiding the equality indices.
The original unrestricted positive total-Mahler gap remains unresolved.

## Assessment history

### Decision whole-independent-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T00:21 |
| status | proved |
| reason | Adopt complete A--C/HV1--HV5 after independent R1074 v3: a nonrational first residue layer gives infinitely many exact linear actual Hankel valuations, the nonzero original dyadic class needs no squarefree reduction, and each good odd prime has infinitely many unit determinants. The field-valued Kronecker criterion and original shifted indexing were checked at their exact source scope. Separate prime subsequences are not synchronized and total finite-place contributions remain uncontrolled; no unrestricted Mahler-gap conclusion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire A--C, exact equality subsequences, both liminf assertions, original nonzero dyadic class, good odd primes and all stated index/prime/Task boundaries. |
| argument | [Complete argument](#argument) | All HV1--HV5, exact row factor, finite-field shifted criterion, integral binomial expansion, rational AS obstruction and general original noncollision. |
| dependency | [Original reduced AS class](Yin_C_G0857_v2.md#reduced-representative) | Normalized reduction and nonzero-class rational obstruction, including repeated poles; no squarefree premise is imported. |
| dependency | [Original modulo-four congruence](Yin_C_G0860_v2.md#statement) | Only the accepted original divisibility and polynomial conventions at retained Dimitrov source scope. |
| dependency | [Accepted field-valued Kronecker criterion](Yin_C_G0858_v1.md#preparation-and-exact-remaining-inputs) | BNZ22 v3 Section 2.2, printed/PDF pp.4--6, Corollary 2.3 over an arbitrary field; actual positive-characteristic and shifted-index applicability checked directly, without using v1's separate modulo-eight premise. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1074_v3.md#actual-hankel-residue-whole) | Complete current statement/argument, actual BNZ22 passage reading, source limits and no shared-prime-index or total-valuation assertion. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-05)
