---
author: Yin
---

# Exact search for six-term positive-constant Pisot trace lifts

<a id="six-term-search"></a>
## Enumeration of all endpoint divisors and monic denominators

For [Yin's Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract), the construction contributor ran the [coefficient search](search.py) on 2026-11-16.
The input is \(h\ge2,\ 1\le d<e\le h,\ a,b\in\{-1,1\}\) and a positive divisor \(u\) of \(2(h+1)+a(h+1-d)+b(h+1-e)\).
This divisor sets \(q=1+C(2)/u\) and \(B(2)=-u\).
The [necessary positive moments and exact endpoint inequalities](../../../ledger/Yin_L_G0462_v63.md#certificate) apply to both parity choices in the inverse and prove the completeness of the integer enumeration.
The reciprocal lift has free integer coefficients through the center \(h+1\).
The determinant interval at each step includes every positive definite extension.
At the center both endpoints are tested and the remaining coefficients are forced by reciprocity.
Reaching \(2h-1\) invokes a rational signed-remainder test for all positive residues, with exact reconstruction if successful.
All counts are exact integers.

From the repository root use the following commands.
The author run used Python 3.14.3 and SymPy 1.14.0.
The threshold-77 enumeration through the indicated range ends before the optional SymPy test.

~~~text
python -B mathematics/computations/programs/Yin_J_G0163/search.py --last 22
python -B mathematics/computations/programs/Yin_J_G0163/search.py --first 23 --last 24
python -B mathematics/computations/programs/Yin_J_G0163/search.py --first 25 --last 26
python -B mathematics/computations/programs/Yin_J_G0163/search.py --first 19 --last 19 --verbose
python -B mathematics/computations/programs/Yin_J_G0163/search.py --benchmark
python -B mathematics/computations/programs/Yin_J_G0163/search.py --first 2 --last 2 --q-min 10
~~~

The first value of \(h\) with \(q\ge77\) is 19.
The free count includes each moment-positive prefix through the center, summed separately over the qualifying parameter and divisor choices.
The deepest index is the largest index attained after imposing both endpoints.

| \(h\) | Cases | Free prefixes | Both endpoints | Deepest index | Reaching \(2h-1\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 through 18 | 0 | 0 | 0 | — | 0 |
| 19 | 2 | 632 | 10 | 26 | 0 |
| 20 | 12 | 3487 | 181 | 29 | 0 |
| 21 | 30 | 9580 | 241 | 30 | 0 |
| 22 | 56 | 19527 | 830 | 33 | 0 |
| 23 | 90 | 33881 | 884 | 34 | 0 |
| 24 | 132 | 54910 | 2085 | 36 | 0 |
| 25 | 180 | 80624 | 1810 | 36 | 0 |
| 26 | 235 | 115842 | 4415 | 39 | 0 |

There are 737 parameter and divisor choices through \(h=26\), with 318,483 free prefixes and 10,456 endpoint matches.
Every qualifying divisor equals one.
The sign pair \((1,-1)\) occurs once at \(h=25\) and ten times at \(h=26\), and the other 726 cases have sign pair \((1,1)\).

<a id="benchmark"></a>
## A second exact check of the specified \(q=77\) example

For \(h=19,\ d=1,\ e=3,\ a=b=1,\ u=1\), the 320 positive prefixes through index 20 give just one endpoint match.
Its coefficient vector consists of \(1\), eighteen zeros, and two entries \(-1\).
It gives \(B(x)=2T_{20}(x/2)-x-1\).
The positivity test excludes the forced extension at index 21.
The benchmark command reconstructs \(C,B\) over \(\mathbb Q\), checks squarefreeness of \(C\), and counts their real roots in \((11/10,23/20)\) by exact rational polynomial arithmetic.
There is exactly one root of \(C\), with \(C(11/10)>0>C(23/20)\), while \(B(11/10)<0\) and \(B\) has no root there.
Thus \(-2B(y)/C'(y)<0\) at this root, directly violating the inverse criterion.
The other qualifying \(h=19\) case has \(d=1,\ e=2,\ q=78\).
Its 312 free prefixes give nine endpoint matches, of which none extends through index 27.

The last command exercises actual reconstruction on the only \(h=2\) case with \(q\ge10\).
It returns two Pisot polynomials with \(q=10\), including the [explicit positive-residue control](../../../ledger/Yin_L_G0462_v63.md#benchmark).
The finite negative search gives no exclusion in untested degrees or for other coefficients in the sparse lift.
