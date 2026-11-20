---
author: Yin
---

# Finite prime-exponent checks for the Salem family approaching two

<a id="traces"></a>
## The first failing trace congruence

For \(F_n=X^n+1-\sum_{i=1}^{n-1}X^i\), let \(s_t\) be the sum of the \(t\)-th powers of its roots.
Among \(4\le n\le39\) and primes \(n\le p\le37\), the [finite reduction](../../../claims/Yin_C_G0345_v680.md#remaining) needs a \(j\) with \(s_{pj}\ne s_j\bmod p^2\) for every pair.
Run `python mathematics/computations/programs/Yin_J_G0181/prime_traces.py` from the repository root.
The [program](prime_traces.py) applies Newton's identities to the descending coefficients of \(F_n\) through the index \(2p\), reducing each integer sum modulo \(p^2\).
It prints the counts for the first successful \(j\in\{1,2\}\) and the eight pairs requiring \(j=2\).
Of the 162 pairs, 154 fail the congruence at \(j=1\), and every remaining pair fails at \(j=2\).
The [independent review](../../../audits/reviews/Yin_R_G0562_v817.md#finding) checked all the pairs by multiplication in the power basis.
