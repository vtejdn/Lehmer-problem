---
author: Yin
---

# Degree lifting for two families of movable interlacing nodes

<a id="census"></a>
## Integer census at height forty

The [moment bound](../../../claims/Yin_C_G0345_v888.md#moments) constrains the coefficients of \(F_V=(1-z^2)S/(A V)\).
The [program](grid_moment_digits.py) forms the integer kernel \([z^j](1-M^2z^2)/(A(Mz)V(Mz))\).
It convolves this kernel with the existing prefix of \(S(Mz)\) and uses the fact that the new digit changes the result by \(M^j\).
For the exact prefix it retains \(-2<[z^j]F_V\le2\), and for the perturbed prefix it retains \(|[z^j]F_V|\le9/4\).
It uses the [two local lifts](lobatto_digits.py) at 40 and \(-41\) to enumerate even degrees \(46\le D=2n\le2\cdot10^{24}\).
The conditions \(n\ge23\) and \(j\le10\) suffice for both intervals.

The table counts distinct prefixes with at least one degree in range.
From depth eight each prefix represents exactly one even degree, since \(1640^8>2\cdot10^{24}\).

| Depth | Exact, \(e=1\) | Exact, \(e=2\) | Perturbed, \(e=1\) | Perturbed, \(e=2\) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 2 | 2 | 3 | 3 |
| 2 | 8 | 8 | 15 | 15 |
| 3 | 32 | 32 | 75 | 75 |
| 4 | 128 | 128 | 375 | 375 |
| 5 | 512 | 512 | 1875 | 1875 |
| 6 | 2048 | 2048 | 9375 | 9375 |
| 7 | 8192 | 8192 | 46875 | 46875 |
| 8 | 1277 | 1221 | 9005 | 8925 |
| 9 | 2 | 6 | 27 | 39 |
| 10 | 0 | 0 | 0 | 0 |

Run from the repository root with Python 3 and either endpoint power.
Omit the last flag for exact prescribed grid coefficients.

~~~sh
python -B mathematics/computations/programs/Yin_J_G0185/grid_moment_digits.py --endpoint-power 1 --perturbed
python -B mathematics/computations/programs/Yin_J_G0185/grid_moment_digits.py --endpoint-power 2 --perturbed
~~~
