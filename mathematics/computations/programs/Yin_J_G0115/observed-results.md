# Original retained weighted-collision observations

The following is the complete execution account and table actually retained from L_G0005 on 2026-10-06.
It is historical evidence, not a new run or newly reconstructed stdout.


The code below enumerates the probability mass function using exact integer reduction modulo a monic polynomial.
It checks the full five-state carry matrix against direct digit enumeration for $0\le n\le20$, and the radical product formulas for $r=1,2,4,8$ and $0\le n\le16$.
It also retains cyclotomic and nonunit controls.
These computations test the formulas at finite lengths; the all-length lower bound comes from the displayed positive-vector proof.

Execution: the exact embedded block below ran successfully on 2026-10-06 in the current Windows/PowerShell workspace, using Python 3.13.15, with exit code 0.
All return-probability equalities for $n=0,\ldots,20$ and all radical factorization equalities for $r=1,2,4,8$ and $n=0,\ldots,16$ passed.
The rational positive-vector inequalities also passed.
The returned integer transition matrix was

$$
4P=\begin{pmatrix}
2&1&1&0&0\\
0&0&0&1&0\\
0&0&0&0&1\\
1&2&0&0&0\\
1&0&2&0&0
\end{pmatrix}.
$$

| Parameter/control | Length | Support | Exact collision probability | Finite $a_n/n$ (bits) |
| --- | ---: | ---: | --- | ---: |
| $\varphi$ | 16 | 4180 | $5119/16777216$ | 0.7298971068 |
| $\varphi^{1/2}$ | 16 | 7744 | $3249/16777216$ | 0.7708887482 |
| $\varphi^{1/4}$ | 16 | 20736 | $81/1048576$ | 0.8537593748 |
| $\varphi^{1/8}$ | 16 | 65536 | $1/65536$ | 1 |
| $1$ | 16 | 17 | $300540195/2147483648$ | 0.1773135805 |
| Primitive cube root of unity | 16 | 102 | $4490385/134217728$ | 0.3063495178 |
| Root of $t^8-2$ | 16 | 65536 | $1/65536$ | 1 |

The finite values in the last column remain upper bounds for their respective limiting $h_2$.
In particular, the differing radical values at fixed length do not contradict equality of their asymptotic rates.

Additional reproduction, 2026-10-06: after updating the reproduction command to this permanent ledger path, the coordinator extracted and executed the retained Python block with CPython 3.14.7 from repository root.
All exact carry and radical-product assertions passed; the golden and eighth-root collision fractions matched the retained table.
The original author execution used CPython 3.13.15.
Neither run upgrades the finite tables to a uniform gap theorem.
