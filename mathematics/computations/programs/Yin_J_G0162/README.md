---
author: Yin
---

# Exhausting trace denominator prefixes on a Chebyshev path

<a id="prefix-certificate"></a>
## Exact exclusion for the unit divisor

For \(C_h=2U_h(x/2)-U_{h-1}(x/2)\) and \(b=1\), no monic integer denominator \(B\) passes the positive-constant Pisot inverse test in degrees \(74\le h\le90\).
The main researcher selected the benchmark \(h=74,q=77\) for [Yin's Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract).
The construction contributor performed the complete integer enumeration on 2026-11-16.
The [positive moment and reciprocity argument](../../../ledger/Yin_L_G0462_v53.md#moments) proves that every admissible denominator must survive each level tested.

From the repository root, run the [certificate program](prefix.py) with Python 3.9 or newer.
The author run used Python 3.14.3 and the standard library.

~~~text
python -B mathematics/computations/programs/Yin_J_G0162/prefix.py
python -B mathematics/computations/programs/Yin_J_G0162/prefix.py --first 74 --last 90
~~~

The first command uses the endpoint masses for \(q=77\) alone.
At index 75, 1,461 prefixes pass the moment tests, of which 64 satisfy both endpoint conditions.
Starting at that index, the respective survivor counts after enforcing both endpoints and then appending the reciprocal coefficients are
\[
64,59,56,50,47,44,41,40,36,35,32,31,27,26,23,22,18,17,14,13,9,8,5,4,0.
\]
The last zero is at index 99.

The second command uses a common positive correction at \(1,-1\) throughout the interval, so its free-prefix counts can be larger.
Here \(q=h+3\), the endpoint test is at index \(m=h+1\), and the first empty index is always within \(2h-1\), the last index required for strict positivity.

| \(h\) | Free prefixes through \(m\) | Passing both endpoints | First empty index |
| ---: | ---: | ---: | ---: |
| 74 | 1673 | 64 | 99 |
| 75 | 1698 | 70 | 101 |
| 76 | 1726 | 66 | 102 |
| 77 | 1744 | 70 | 103 |
| 78 | 1768 | 67 | 105 |
| 79 | 1781 | 71 | 106 |
| 80 | 1806 | 68 | 107 |
| 81 | 1829 | 75 | 109 |
| 82 | 1845 | 72 | 110 |
| 83 | 1862 | 77 | 111 |
| 84 | 1891 | 73 | 113 |
| 85 | 1904 | 77 | 114 |
| 86 | 1919 | 72 | 115 |
| 87 | 1943 | 78 | 117 |
| 88 | 1955 | 76 | 118 |
| 89 | 1968 | 81 | 119 |
| 90 | 1985 | 79 | 121 |

The program extends each prefix by every integer allowed by the [strict determinant interval](../../../ledger/Yin_L_G0462_v53.md#recursion).
At index \(m\) it also opens a branch for the corresponding degree when both endpoint tests hold.
That branch appends the already determined mirror coefficients until it becomes empty or reaches the last necessary moment.
A surviving prefix at the last moment would require a separate inverse test.
