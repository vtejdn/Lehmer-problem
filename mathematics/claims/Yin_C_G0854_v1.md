---
author: Yin
---

# All-index cyclic-norm bounds and an entropy-dependent finite threshold

## Statement

For a nontorsion algebraic unit alpha of degree d>=2 and 0<m=log M(P)<=1, there is an absolute numerically uncalibrated kappa>=1 such that K=kappa d^4 log(2d) gives n m-K log(2n)<=log|Res(P,t^n-1)|<=n m+d log2 for every n>=1.
With x=K/m and N=ceil(8x log(8x)), every n>=N has log C_n>=nm/2 and (log C_n-d log2)/n>=m/4.
The exponent-one guard, original-root normalization, constant and nonuniformity limits are retained below.

## Source and original checking boundary

The exact accepted external estimate (1) is [Dim16 equation9.1](../audits/literature/Dim16/Yin_U001.md#dim16-reported-bound), applied separately at algebraic degree d and Weil height m/d.
The original 2026-10-07 source and project-specialization checks are retained at [Dim16 U001](../audits/literature/Dim16/Yin_U001.md#dim16-u001).
They do not audit the original Baker--Wustholz proof, calibrate kappa or inspect Dim16's main multivariable theorem.
No Current assessment is selected for this newly organized fixed account.
Placement preserves the existing argument and actual earlier checking scopes; it supplies no new mathematical adoption, review relationship, source reading or Task/E authority.

## Retained argument

<a id="dim16-cyclic-all-index"></a>
## Direct all-index specialization for the near-one unit domain

Let alpha be a nontorsion algebraic unit with monic irreducible polynomial P, degree d>=2 and 0<m=log M(P)<=1.
Set

    C_n=|Res(P,t^n-1)|=|Norm_(Q(alpha)/Q)(alpha^n-1)|,
    K=kappa d^4 log(2d),

where kappa>=1 may be enlarged from (1).
Then, for every n>=1,

    n m-K log(2n) <= log C_n <= n m+d log 2.                    (2)

To prove this, normalize each complex conjugate alpha_i separately:

    z_i=alpha_i        if |alpha_i|<=1,
        alpha_i^(-1)   if |alpha_i|>1.

Thus |z_i|<=1, and all d normalized numbers remain nontorsion, have degree d and have Weil height m/d.
Inverting selected roots does not require a common splitting-field degree in (1): apply that one-number statement separately to each z_i.
Directly,

    C_n=exp(nm) product_i |1-z_i^n|.                            (3)

For n>=2, (1) and max(h(z_i),1/d)=1/d give a total logarithmic loss at most kappa d^4 log d log n, which is bounded by the loss in (2).
The upper bound follows from |1-z_i^n|<=2.
No root on the unit circle is omitted.
For n=1, C_1 is a nonzero integer, so log C_1>=0; also K log 2>=m on the stated domain.
This proves the remaining lower-bound case without applying log b at b=1.

<a id="dim16-polynomial-threshold"></a>
## A finite threshold, and its limitation

Define

    x=K/m,
    N=ceil(8x log(8x)).                                        (4)

Then every integer n>=N satisfies

    log C_n >= n m/2,
    [log C_n-d log 2]/n >= m/4.                                (5)

Here x>=1 and K>=d log 2.
Since x log(8x)>=1,

    N<=9x log(8x),
    2N<=18x log(8x)<=144x^2<=(8x)^4.

Consequently K log(2N)<=4K log(8x)<=Nm/2.
The function log(2t)/t decreases for t>=2, so the same relative error bound holds for every n>=N.
Also N>=4x>=4d log 2/m, hence subtracting d log 2 costs at most nm/4.
This proves (5).

In particular the bound has order

    N=O((d^4 log(2d)/m) log(d^4 log(2d)/m))

on 0<m<=1, with an absolute but numerically uncalibrated constant from the external statement.
This is a bound polynomial in d and 1/m up to the displayed logarithms, and it pays the archimedean d log 2 cost explicitly.
It is not a numerically certified search cutoff until an explicit valid kappa is supplied.
No numerical transcendence-constant optimization was attempted.

The conclusion controls every sufficiently large n.
By contrast, the independently proved [finite prime witness](Yin_C_G0260_v1.md#finite-cyclic-norm-prime-witness) finds at least one prime exponent with a smaller degree dependence for each fixed positive lower entropy threshold, and requires no logarithmic-form theorem.
The two conclusions have different quantifiers.
Both certify a positive fraction of the input's m; neither establishes a common positive lower bound for m in the first place.
In particular (4) grows as m decreases, and (5)'s guaranteed lower certificate also decreases.
No bound on the arithmetic prime factors of C_n follows.
