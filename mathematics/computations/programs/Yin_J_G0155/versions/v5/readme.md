---
author: Yin
---

# Certifying the exclusion of a nonreal cubic at the fourth coefficient

<a id="enumeration"></a>
## The finite calculation

The [cubic sign-factor argument](../../../../../claims/Yin_C_G0896_v2.md#integer-prediction) reduces the question to the integer cubics \(G(t)=At^3+Bt^2+Ct+D\) and integer coordinate continuations specified below.
For [Yin's Lehmer Task](../../../../../tasks/Yin_T_G0001_v1.md#contract) the construction contributor ran the [exact interval enumeration](cubic_prediction.py) on 2026-11-16.
It excludes all the continuations without imposing a degree bound on the original polynomial.
The [independent arithmetic review](../../../../../audits/reviews/Yin_R_G1107_v71.md#cubic-enumeration-review) reran the outward-rounded enumeration and checked its table against a direct Toeplitz calculation.

Use \(1\le A\le3,\ |B|\le21,\ |C|\le49,\ 1\le D\le38\).
Retain negative discriminant and the strict signs \(G(-2)<0<G(-3/2)\), so the sole real root \(y\) is in this interval.
The computation tests all these coefficient tuples, including imprimitive or reducible cubics if they satisfy the conditions.
For the nonreal trace root \(q\), the elementary symmetric coefficients give \(\Re q=(-B/A-y)/2\) and \(|q|^2=-D/(Ay)\).
With \(S=(|q+2|+|q-2|)/2\), the larger modulus of its reciprocal lifts is \(\lambda=(S+\sqrt{S^2-4})/2\).
Indeed for \(q=z+z^{-1}\) the two distances are \(|z\pm1|^2/|z|\), whose sum is \(2(|z|+|z|^{-1})\).
This gives \(M=A\lambda^2\).
Keep every interval comparison compatible with \(M\le -12-8y\).

The table gives the first order \(k\) at which no moment branch remains and the largest number of retained branches at any order from one up to \(k-1\).
The initial coordinates are \(a_0=2,a_1=0,a_2=4\).

| \(A\) | \(B\) | \(C\) | \(D\) | Empty order | Largest count |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | -1 | -3 | 4 | 26 | 18 |
| 1 | -1 | -3 | 5 | 27 | 25 |
| 1 | 0 | -2 | 2 | 2 | 1 |
| 1 | 0 | -2 | 3 | 21 | 6 |
| 1 | 1 | -1 | 1 | 27 | 16 |
| 2 | -3 | -7 | 11 | 1 | 0 |
| 2 | -2 | -7 | 9 | 4 | 1 |
| 2 | -1 | -6 | 6 | 1 | 0 |
| 2 | 1 | -4 | 2 | 1 | 0 |
| 2 | 1 | -4 | 3 | 1 | 0 |
| 2 | 2 | -3 | 1 | 26 | 14 |
| 2 | 3 | -1 | 1 | 1 | 0 |

<a id="reproduction"></a>
## Covering all integer continuations

The program runs with Python's standard library from the repository root.

~~~text
python -B mathematics/computations/programs/Yin_J_G0155/versions/v5/cubic_prediction.py
~~~

Root bisection evaluates the integer cubic after clearing the positive denominator exactly.
All computed real intervals have integer endpoints in units of \(2^{-192}\).
Products enclose the four corner products, reciprocals enclose both endpoints with the denominator separated from zero, and square roots use integer square roots with the upper endpoint rounded upwards.
The underlying radicands used for the measure are nonnegative by their geometric formulas.

At each branch the prior error \(e\), predicted moment \(v\), and the offset \(b=-a_{k-3}-y(a_k-a_{k-2})\) are enclosed by intervals.
The next moment is \(c_k=a_{k+1}+b\).
If the upper endpoint of \(e(e-M)\) is negative the branch is empty.
Otherwise the program adds and subtracts an upper bound on its square root to the interval for \(v-b\) and visits every integer in that closed range.
For each visited integer it encloses the updated error and predictor using the [projection formulas](../../../../../claims/Yin_C_G0896_v2.md#integer-prediction).
An updated error excludes a branch only when its upper endpoint lies strictly below the lower endpoint of \(M\).
Survival at order 30 would raise an error and withhold a completed exclusion for that input.
All twelve inputs exhausted their branches before this limit.
