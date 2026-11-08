# Mossinghoff's table of small Mahler measures by exterior root count

The selected [author's data table](https://github.com/mossinghoff/Mahler-Measure-Database/blob/main/BestByRootCount_200.txt) is dated May 31, 2026.
The [local original](../../../literature/pdf/Mos26/BestByRootCount_200.txt) gives the degree, multiplicative measure, exterior root count and first half of the reciprocal coefficients in each row.
The degree-ten row with one exterior root and the degree-18 row with two were inspected for the [finite calibrations](../../../computations/programs/Yin_J_G0144/readme.md).
The degree-18 input and its total measure bounds are independently reproducible from the rational certificate there.
The table describes known examples and its numerical entries supply reference values for the controls.

<a id="complete-small-cores"></a>
## The degree-44 range in the full small-measure table

The [author's full list](https://github.com/mossinghoff/Mahler-Measure-Database/blob/7e3798516710370a758e16eb5de6bccbee98bb6a/AllSmallMeasures_200.txt) dated May 31, 2026 displays the leading half of each reciprocal coefficient vector and chooses one sign substitution.
The header reports completeness for primitive irreducible noncyclotomic polynomials of measure below 1.3 through degree 44, as in [Mossinghoff, Rhin and Wu](https://doi.org/10.1080/10586458.2008.10128872).
The 944 rows within that degree range in the [native table](../../../literature/pdf/Mos26/AllSmallMeasures_200.txt) were consumed by the [cyclotomic completion census](../../../computations/programs/Yin_J_G0149/readme.md#core-coverage).
The program restores substitutions, both signs and reducible inputs locally.
The source's exhaustive irreducible classification is an external input at its reported degree limit.
