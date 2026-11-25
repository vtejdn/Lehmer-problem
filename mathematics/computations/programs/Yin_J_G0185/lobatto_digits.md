---
author: Yin
---

# Exact degree lifting for interlacing trace polynomials

<a id="results"></a>
## A trillion trace degrees at the first nonunit norm

Use the [coefficient bounds and pole congruences](../../../claims/Yin_C_G0345_v887.md#statement) with \(q=40,\ p=41\), trace degree \(23\le n\le10^{12}\) and reciprocal degree \(D=2n\).
At each depth the [sieve](lobatto_digits.py) keeps each compatible prefix and its degree residue, discarding classes with no even degree in the interval.
The two counts in each column are the retained prefixes and the even degrees they represent.

| Depth | Exact Chebyshev extrema | Total angular displacement at most \(1/512\) |
| ---: | ---: | ---: |
| 1 | 2 / 2439024390 | 3 / 3658536585 |
| 2 | 22 / 16359306 | 51 / 37923847 |
| 3 | 274 / 124253 | 867 / 393127 |
| 4 | 996 / 996 | 4003 / 4003 |
| 5 | 16 / 16 | 55 / 55 |
| 6 | 0 / 0 | 0 / 0 |

For a prefix through position \(k-1\), write \(D=d+hM^{k-1}\) with the known representative \(0\le d<M^{k-1}\).
In the two rings modulo \(|b|^{k+1}\), \(b=q,-p\), the factors \((1+b)^{M^{k-1}}\) equal \(1+u_b|b|^k\) with \(u_b\) invertible modulo \(|b|\).
The known prefix evaluation at \(d\) already equals \(L^2\bmod |b|^k\).
After adding digit \(c_k\), dividing the error by \(|b|^k\) gives a linear equation in \(h\bmod |b|\) and \(c_k\).
The program combines the two solutions for \(h\) by Chinese remaindering, and advances the period from \(M^{k-1}\) to \(M^k\).
At these depths each admissible range of digits has width less than \(M\), so different prefixes have different residues.
The two calculations use only integer arithmetic and can be run from the root with Python 3.

~~~sh
python -B mathematics/computations/programs/Yin_J_G0185/lobatto_digits.py
python -B mathematics/computations/programs/Yin_J_G0185/lobatto_digits.py --perturbed --depth 8
~~~

Interlacing at substantially different angles or a different signed norm can fall outside both tests.
