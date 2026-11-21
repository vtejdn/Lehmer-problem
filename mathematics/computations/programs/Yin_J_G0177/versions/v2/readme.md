---
author: Yin
---

# A width-nine octic witness below the full cutoff at prime seventeen

<a id="census"></a>
## All odd primes through 251 for one Salem seed

Fix \(P=X^8-X^5-X^4-X^3+1\).
Among the 53 odd primes \(3\le p\le251\), only \(p=17\) admits nonzero coprime integral rows \(U,V\) of degree at most nine with \(P^2\mid U(X^p)+XV(X^p)\), \(UU^\iota\ne VV^\iota\) and \(H=\max(\|U\|_1,\|V\|_1)\le2^p\), where \(\iota(Y)=1/Y\).
Its exact minimum is \(91\,698<131\,072\).
Thus the [finite minimum allowing every seed](../../../../../claims/Yin_C_G0345_v408.md#statement) at width nine and \(p=17\) is at most \(91\,698\).
The table gives an attaining pair for the specified octic in ascending coefficient order.

| Row | Coefficients |
| --- | --- |
| \(U\) | \(-618,-3483,-2652,-18660,-7272,-14106,-22068,5644,-13470,3725\) |
| \(V\) | \(840,1329,-4420,-7980,-44,-31290,8004,-23052,228,-2751\) |

The individual signed coefficient vectors can fit the necessary box even when a genuine pair is unavailable.
The table counts all nonzero signed vectors of one-norm at most \(2^{p+1}\), identifying a vector and its negative.
The adjacent ranks give the dimensions of their rational spans.

| Prime | Plus count | Plus rank | Minus count | Minus rank | Genuine costs among the tested representatives |
| ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 1 | 1 | 0 | 0 | None |
| 7 | 1 | 1 | 0 | 0 | None |
| 17 | 3 | 2 | 11 | 2 | \(91\,698,\ 114\,378\) |
| All other tested primes | 0 | 0 | 0 | 0 | None |

At \(p=17\), nine of the 33 combinations have matching coefficient parities, two give actual cost at most \(2^{17}\), and both pairs are coprime with nonzero reflected determinant.
At 51 primes at least one sign already fails the necessary Euclidean bound \(\lambda_{1,\varepsilon}\le 2^{p+1}\).
At \(p=3\) both signs meet that Euclidean bound, but the minus sign fails the one-norm test.
The two independent short directions in each plane at \(p=17\) show that the [eventual one-direction restriction](../../../../../ledger/Yin_L_G0462_v255.md#bounds) has not yet taken effect there.
This finite range leaves open the behavior of the cutoff for arbitrarily large primes.

<a id="minima"></a>
## Exact minima before the cutoff

The search determined the least genuine uncapped cost for the specified seed at **each** of the 53 primes, including an attaining pair for each.
The table gives the first seven values.

| \(p\) | 3 | 5 | 7 | 11 | 13 | 17 | 19 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(H_{p,9}(P)\) | 22 | 275 | 845 | 23,767 | 4,370,042 | 91,698 | 199,466,038 |

At the same \(p=17\), the [degree-eight signed-line formula](../../../../../ledger/Yin_L_G0462_v242.md#lines) gives \(H_{17,8}(P)=13\,902\,464\).
The extra coefficient position permits the displayed width-nine witness to fall below the cutoff.
For every tested prime \(19\le p\le251\), the exact minima obey \(H_{p,9}(P)^4>2^{5p}\).
The source computes this last comparison with integers.

<a id="method"></a>
## Saturated signed lattices and exhaustive mixing

Use formal reversal \(A^*(Y)=Y^9 A(1/Y)\) and the [integer-kernel and plane enumeration](../../readme.md#method) with the single octic input and row width nine.
For each sign \(\varepsilon\), the ten columns are the remainders \(X^{pi}+\varepsilon X^{p(9-i)+1}\bmod P^2\) in the 16-dimensional monomial basis.
At every tested prime both rational nullspaces have dimension two.
The calculation saturates each lattice by imposing the integer coordinate congruences and applies unimodular Gauss reduction.
For each returned basis \(u,v\) the program independently checks both remainder equations and the gcd one of all \(2\)-by-\(2\) coordinate minors, which certifies saturation in its rational plane by Smith normal form.

Put \(a=u\cdot u,\ b=u\cdot v,\ c=v\cdot v\).
The reduction gives \(0<a\le c,\ 2|b|\le a\).
For \(iu+jv\) with \(|j|=1\), completing the square shows that \(i=0\) is a minimizing choice and the squared length is at least \(c\).
For \(|j|\ge2\), the squared length is at least \(4(c-b^2/a)\ge3c\).
Thus \(u,v\) realize the two Euclidean successive minima, with squares \(a,c\).
The output supplies both vectors, both squared minima and the off-diagonal Gram entry for every sign and prime.

At any trial ceiling \(T\), each genuine pair has nonzero signed components \(A=U+V^*, C=U-V^*\) of one-norm at most \(2T\).
The program enumerates the full Euclidean ellipse of that radius in each integral plane and filters by the one-norm, using integer square roots for all coefficient limits.
Choosing one sign per vector suffices, since the alternative choices negate the pair or exchange its two formally reversed rows up to sign.
Removing a common power of \(Y\) after that exchange preserves the degree cap, cost and double divisibility.
The mixed rows are integral exactly when \(A,C\) have matching coefficient parities.
The program checks their actual costs, autocorrelation differences and ordinary rational polynomial gcds, and rechecks each stored witness against the original remainder columns.

For the uncapped minimum the trial ceiling is the sum of the one-norms of the two reduced first vectors, one from each plane.
The computation found a genuine witness inside this ceiling for every input, and it compared all candidates that could improve the smallest cost.
Consequently each stored minimum is global for that seed, width and prime.
The largest product of the two candidate counts for this search was \(9\cdot565=5\,085\) at \(p=109\).
The separate test at \(T=2^p\) records every passing representative, including both at \(p=17\).

<a id="reproduction"></a>
## Reproducing the certificates

Run the [standard-library Python program](octic_nine.py) from the repository root.
It reuses the [original kernel and search routines](../../minimum.py) and requires no generated input.

~~~text
python mathematics/computations/programs/Yin_J_G0177/versions/v2/octic_nine.py
~~~

Compare the generated `outputs/Yin_J_G0177/versions/v2/results.json` in the computations directory with the fixed result.
Python 3.14.3 produced the [53 per-prime records and single width-eight control](../../inputs/versions/v2/results.json).
Each record includes the two signed reduced bases, a cutoff decision with candidate counts, the uncapped enumeration ceiling and counts, and the least cost with its genuine rows.
