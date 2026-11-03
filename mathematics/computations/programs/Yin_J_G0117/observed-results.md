# Original retained quartic carry observations

## 9. Exact finite control and scope of verification

The formulas above are direct all-length arguments.
The embedded check below independently enumerates the quartic digit law modulo its monic polynomial, compares it to the actual quotient modulo 2, and checks the stated block bound at finite lengths.
It also verifies the cyclotomic truncation counterexample using exact rational numbers.
The finite checks do not prove the general operator comparison or any uniform gap.

Execution: the exact embedded block ran on 2026-10-06 in the current Windows/PowerShell workspace, using Python 3.13.15, with exit code 0.
Every quartic assertion for $0\le n\le16$ and every cyclotomic truncation assertion for $0\le n\le64$ passed.
The retained output rows are:

| $n$ | Quartic support | Exact $q_n$ | Exact $\bar q_n$ modulo 2 | Block upper bound |
| ---: | ---: | --- | --- | --- |
| 0 | 1 | $1$ | $1$ | $1$ |
| 2 | 4 | $1/4$ | $1/4$ | $3/4$ |
| 4 | 16 | $1/16$ | $1/16$ | $9/16$ |
| 8 | 222 | $41/8192$ | $1/16$ | $81/256$ |
| 12 | 2888 | $57/131072$ | $1/16$ | $729/4096$ |
| 16 | 35662 | $5339/134217728$ | $1/16$ | $6561/65536$ |

The quotient plateau and block estimate were proved above for all applicable lengths; the table is only a finite check and illustrates that the block estimate is deliberately weak.
