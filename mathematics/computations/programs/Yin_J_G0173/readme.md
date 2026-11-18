---
author: Yin
---

# First half-mass exponents for Mossinghoff's 72 small Salem numbers

<a id="exponents"></a>
## Exact exponents in source rank order

For each Salem number \(\sigma\) in the June 1, 2026 table, \(e(\sigma)\) is the least \(k\ge1\) for which the fixed input \(\sigma^k\) admits the [half-mass construction](../../../claims/Yin_C_G0345_v392.md#statement).
The entries in each line run from the first indicated rank through the last.

| Mossinghoff ranks | Least exponents |
| --- | --- |
| 1–12 | 31, 511, 127, 127, 31, 73, 33, 1025, 17, 257, 5, 63 |
| 13–24 | 513, 1, 127, 257, 31, 17, 17, 8191, 127, 2047, 17, 8193 |
| 25–36 | 205, 171, 5, 32767, 32769, 127, 4097, 129, 32767, 3, 511, 5 |
| 37–48 | 1, 1025, 511, 8388607, 31, 9, 129, 2049, 16385, 131073, 43, 63 |
| 49–60 | 65537, 255, 129, 8191, 89, 524289, 1398101, 9, 37449, 5, 31, 127 |
| 61–72 | 65, 255, 127, 1025, 129, 31, 15, 257, 257, 8191, 819, 127 |

Lehmer's polynomial at rank 1 has \(Q(0)=3,\ Q'(0)=4\) and its sole binary order is \(31\) with trace weight \(5\).
The largest least exponent is \(2^{23}-1=8\,388\,607\), at rank 40 of degree 46.
Of the 68 odd-constant rows, 15 attain the [sharp bound](../../../claims/Yin_C_G0345_v392.md#least) \(2^{\deg(P)/2}+1\), including rank 54 of degree 38.
Ranks 60 and 69 have \(Q(0)\equiv2\bmod4\) and \(Q'(0)\) odd, giving first exponents 127 and 257 respectively.
Rank 69 attains the second bound \(2^{\deg(P)/2-1}+1\).
Only ranks 14 and 37 admit exponent one.

<a id="window"></a>
## Powered values that stay below the catalogue cutoff

For each entry, exact signs at \(7/6\) and \(49/37\) give \(7/6<\sigma<49/37\), using the unique exterior real root of its monic Salem polynomial.
Since \((7/6)^2>49/37\), any admissible power from these inputs remaining below \(49/37\) has exponent one.
The two outputs are rank 14 of degree 20, displayed as \(1.253330650201\), and rank 37 of degree 24, displayed as \(1.291741425715\).
Their respective trace data are \((Q(0),Q'(0))=(-4,-5)\) and \((4,11)\).
Exact signs at \(9/7\) separate the first from the second.

Mossinghoff reports completeness for \(\sigma<1.3\) through degree 44.
There are 46 entries in that range, as checked by exact signs at \(13/10\).
The one further listed entry below \(1.3\) has degree 46.
Using the source's stated completeness, ranks 14 and 37 are consequently **all** admissible powered values below \(1.3\) from Salem inputs of degree at most 44, since \(1<\sigma\le\sigma^k<1.3\) forces the original input into that range.
Rank 14 gives the exact minimum powered value among admissible choices in these degrees.
For unrestricted degree the table lists known examples, and the behavior of \(e(\sigma)\log\sigma\) along a hypothetical sequence approaching one remains open. [Mossinghoff's fixed source table](https://github.com/mossinghoff/Mahler-Measure-Database/blob/27df0451b18cf711c9ff2a5dacbc46eec33a15a4/SalemList.txt)

<a id="method"></a>
## Exact binary orders and integral parity

The program reads the rank, degree, displayed decimal and complete leading-through-center coefficient list for every data line of [the registered Mos26b original](../../../literature/pdf/Mos26b/SalemList.txt), and reflects the coefficient list to obtain \(P\).
The displayed decimals label the inputs.
For \(P=z^sQ(z+z^{-1})\), the integral values \(Q(0),Q'(0)\) follow from the center coefficient and the constant and linear coefficients of \(C_j(z+z^{-1})=z^j+z^{-j}\).
For \(j>0\) even these are \(2(-1)^{j/2},0\), and for \(j\) odd they are \(0,j(-1)^{(j-1)/2}\).

Every residue order divides \(2^f-1\) or \(2^f+1\) for some \(1\le f\le s\), by Frobenius on an inverse pair.
The program lists all positive divisors of those integers.
For each candidate \(n\), it computes \(\deg\gcd(\bar P,z^{bn}-1)/2\) over \(\mathbb F_2\), where \(b\) is a power of two at least \(\deg P\).
Since \(n\) is odd and \(z^{bn}-1=(z^n-1)^b\), this counts all trace weights with order dividing \(n\), including their full multiplicities.
Subtracting the already determined proper-divisor weights gives \(w_n\).
Their sum is checked against \(s\).
The [least-exponent criterion](../../../claims/Yin_C_G0345_v392.md#least) selects the answer from these weights and the integral parity.
As a separate arithmetic check, the computation author factored each of the 72 binary polynomials into irreducibles with SymPy, stripped prime divisors from \(2^{\deg g}-1\) by modular powering at each factor \(g\), and recomputed the integral traces from Chebyshev polynomials.
All weights, both trace coefficients and all least exponents agreed.
The Salem identification and the claimed completeness in the indicated degree range come from the source.

<a id="reproduction"></a>
## Source and reproduction

The source is Michael J. Mossinghoff's *Small Salem Numbers*, dated June 1, 2026, in the author's Mahler Measure Database.
The native table used here is the revision uploaded July 2.
Its header gives the search window \(49/37\), the lower complete range and the positive Salem orientation of the listed polynomials. [Fixed author revision](https://github.com/mossinghoff/Mahler-Measure-Database/blob/27df0451b18cf711c9ff2a5dacbc46eec33a15a4/SalemList.txt)

If the ignored source store is empty, recover that revision from the repository root with the first command.
Run the [standard-library Python program](least_exponents.py) with the second.

~~~sh
curl --fail --location --create-dirs --output mathematics/literature/pdf/Mos26b/SalemList.txt https://raw.githubusercontent.com/mossinghoff/Mahler-Measure-Database/27df0451b18cf711c9ff2a5dacbc46eec33a15a4/SalemList.txt
python mathematics/computations/programs/Yin_J_G0173/least_exponents.py
~~~

The [generated table](../../outputs/Yin_J_G0173/least_exponents.tsv) gives the integral trace data, every positive exact-order weight and the least exponent for each source rank.
