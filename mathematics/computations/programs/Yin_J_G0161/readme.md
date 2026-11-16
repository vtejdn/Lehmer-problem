---
author: Yin
---

# A Graeffe certificate for four phases of the plastic polynomial

<a id="four-phase-certificate"></a>
## Complete measure for the 31 exponents

For \(f(z)=z^3-z-1\), \(g(z)=1-z^2-z^3\) and every integer \(-3\le k\le27\), the polynomial
\[
             V_k(z)=z^{4\max(k,0)}f(z)^4-z^{4\max(-k,0)}g(z)^4
\]
satisfies \(M(V_k)>41/20\).
The computation for [Yin's Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract) uses the complete multiplicative measure, including the absolute leading coefficient.
The main researcher supplied the family and interval, and the construction contributor certified all 31 cases with exact integer coefficients on 2026-11-16.

Write each coefficient array in ascending powers.
For \(C(z)=E(z^2)+zO(z^2)\), the [Graeffe transform in J144](../Yin_J_G0144/pilot.py) computes \(G(C)(z)=E(z)^2-zO(z)^2\).
Indeed \(G(C)(z^2)=C(z)C(-z)\), so \(G(C)\) has the squared roots with multiplicities and its absolute leading coefficient is the square of that of \(C\).
Thus \(M(G(C))=M(C)^2\) even for odd degree or a nonunit leading coefficient.
At \(k=0\), cancellation in \(f^4-g^4\) gives degree eleven, leading coefficient \(-4\) and constant coefficient zero.
All other inputs have degree \(D=4|k|+12\).

The elementary symmetric expansion gives \(|[z^j]C|\le\binom Dj M(C)\) for every polynomial of degree \(D\), since each root product times its absolute leading coefficient is at most \(M(C)\).
Apply this to \(C=G^8(V_k)\), where \(G^8\) denotes eight iterations.
The table records the exact integer floor of
\[
       \frac{|[z^j]G^8(V_k)|\,20^{256}}{\binom Dj\,41^{256}}
\]
or its minimum over the indicated set.
Both floors exceed one, proving the strict bound.

| Exponents | Number of inputs | Index \(j\) | Minimum floor | Attaining exponent |
| --- | ---: | ---: | ---: | ---: |
| \(1\) | 1 | 1 | 2 | \(1\) |
| \(-3\le k\le27,\ k\ne1\) | 30 | 3 | 1264 | \(-2\) |

From the repository root, run the [certificate program](four_phase.py) with Python 3.
The author run used Python 3.14.3 and the standard library.

~~~text
python -B mathematics/computations/programs/Yin_J_G0161/four_phase.py
~~~
