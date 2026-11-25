---
author: Yin
---

# An exact enumeration of irrational coefficient traces in degree twelve

<a id="quadratic-base"></a>
## Question and scope

For a cubic half polynomial \(X^3-aX^2+a'X-1\), put \(t=a+a'\) and \(p=aa'\).
This computation checks whether a totally real quadratic base, an irrational \(t\), and marked exterior modulus \(R\le(1+\sqrt5)/2\) satisfy the necessary conditions derived in the [quadratic-base box](../../../claims/Yin_C_G0901_v150.md#box).
The marked root may have either real sign after the constant is normalized to \(-1\).

## Files

The [enumerator](quadratic_cubic_halves.py) contains the complete finite input ranges and sign tests.
It uses only Python's standard library and reports counts to standard output.

## Reproduction

From the checkout root run

~~~text
python -B mathematics/computations/programs/Yin_J_G0193/quadratic_cubic_halves.py
~~~

For each positive fundamental quadratic discriminant \(5\le D_0\le90\), write \(T_2=2t=T+k\sqrt{D_0}\) and \(P_2=2p=P+l\sqrt{D_0}\).
The program tests \(-5\le T\le12,\ 0\le P\le19,\ |k|,|l|\le4,\ k\ne0\) and the two parity conditions for the full ring of integers.
It also imposes \(4k^2D_0<361,\ l^2D_0<121,\ -5<T_2<13,\ -6<T_2'<12\), with primes denoting quadratic conjugation.
The squared-difference test is \(0<D_4=T_2^2-8P_2<16,\ D_4'<0\).
The nonsplit triple requires \(P_2'<18\) and
\[
            (P_2')^2+36P_2'+12T_2'P_2'-2(T_2')^3-108<0 .
\]
The last expression is four times the cubic discriminant at that embedding.
The final marked test requires \(\sqrt{D_4}<n/d_0\), with the positive numerator and denominator specified below.

| Marked trace | \(n\) | \(d_0\) |
| --- | ---: | ---: |
| \(T_2>-4\) | \(5(337-26T_2)\) | \(546\) |
| \(T_2<-4\) | \(21(26T_2+129)\) | \(130\) |

It checks \(n>0\) and \(n^2>d_0^2D_4\).
Every sign is computed in the ordered quadratic field with integers: for opposite nonzero signs of \(A,B\), the sign of \(A+B\sqrt{D_0}\) is \(\operatorname{sgn}(A)\operatorname{sgn}(A^2-D_0B^2)\).
Consequently no approximate quadratic embeddings or root-finding tolerances enter the enumeration.

## Results and limits

The run returned 40 tuples before the final marked test and none after it.
The following counts list all nonzero groups before that last test.

| \(D_0\) | 5 | 8 | 12 | 13 | 17 | 21 | 24 | 28 | 29 | 33 | 37 | 40 | 41 | 44 | 53 | 57 | 61 | 69 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Count | 8 | 6 | 3 | 4 | 3 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

The remaining rational coefficient traces are classified in the [analytic rational-trace result](../../../claims/Yin_C_G0901_v146.md#rational).
This enumeration addresses quadratic bases at the stated exterior-root threshold; the explicit all-degree height bound has a separate proof.
