---
author: Yin
---

<a id="cha03-u001"></a>
# Chang's moment inequality for prime valuations

<a id="dimension"></a>
## Multiplicative dimension

For a nonempty finite set \(A\) of positive rationals, use all primes appearing in its numerators or denominators to form the exponent vector \((v_p(a))_p\) of each \(a\in A\).
Chang defines the multiplicative dimension as the dimension over \(\mathbb R\) of the affine span of these vectors.
Multiplication of \(A\) by a positive rational translates the exponent vectors after including any new prime coordinates and preserves the dimension.
Proposition 9 uses the fact that \(m\) coordinates separate the elements of \(A\) when this dimension is \(m\), by an injective coordinate projection on the affine span. [Published edition, pp. 947–948](readme.md#edition)

<a id="valuation-estimate"></a>
## The one-prime estimate and iteration

For an integer \(h\ge1\) use the \(L^{2h}\) norm for Lebesgue probability on \([0,1]\).
Write \(e(x)=e^{2\pi i x}\).
For a prime \(p\), take finite nonnegative linear combinations \(F_j\) of \(e(nx)\) with positive integral \(n\) and \(v_p(n)=j\).
Proposition 6, (1.7), gives
\[
       \left\|\sum_j F_j\right\|_{2h}^2
                \le (2h^2-h)\sum_j\|F_j\|_{2h}^2 .
\]
For \(R\) distinct primes, Proposition 8, (1.15), replaces \(j\) by the joint valuation vector and raises the same constant to the power \(R\).
For a finite set of positive integers of multiplicative dimension \(m\), Proposition 9, (1.16), applies the resulting bound with singleton components and constant \((2h^2-h)^m\) in the squared norm.
The sixth moment uses \(h=3\) and constant \(15\) at each prime. [Published edition, pp. 945–948](readme.md#edition)

<a id="minimum-ties"></a>
## Counting the minimum when more than two indices are tied

The first displayed equality on p. 946 counts selected pairs at the minimum valuation.
For \(h\ge2\) and a single nonzero component \(F_j\), its three terms give \(2\binom h2+h^2=2h^2-h\) copies of \(\int|F_j|^{2h}\).
Thus this line gives an upper bound under the stated nonnegative-coefficient hypothesis.
To verify the inequality needed in Proposition 6, expand the even moment and use orthogonality.
Every contributing equality of sums has at least two of its \(2h\) positions at the least valuation, since division by the least power of \(p\) excludes a unique minimum modulo \(p\).
Count a tuple once for each possible pair of tied positions to obtain an upper bound, and enlarge each class by dropping the minimum requirement while retaining equality of the two valuations.
This enlargement is valid for nonnegative Fourier coefficients.
At a fixed pair of positions and valuation \(j\), the resulting integral in absolute value is at most \(\int |F_j|^2|\sum_lF_l|^{2h-2}\).
Hölder and the \(\binom{2h}{2}\) possible pairs give (1.7), after division when \(\|\sum_lF_l\|_{2h}>0\).
The case \(h=1\) also follows directly by orthogonality.
Iteration yields (1.15), and coefficientwise absolute values majorize an even moment when the original coefficients have signs or phases.
This inspection checks the valuation inequalities, the definition and the projection used in (1.16) in the published edition.
The [independent comparison with the printed displays](../../reviews/Yin_R_G0562_v110.md#valuation-occupancy) also gives a four-frequency counterexample to the middle vanishing condition in (1.11) and the singleton equality case for the strict sign printed in (1.16).

<a id="product-doubling"></a>
## Dimension from a small product set

Let \(A\) be a nonempty finite set of positive integers and \(AA=\{aa':a,a'\in A\}\).
The argument on pp. 948–949 gives \(\operatorname{mult.dim}(A)\le\alpha\) when \(|AA|<\alpha |A|\) and \(\alpha<\sqrt{|A|}\).
In Proposition 11 on p. 949 the first left-hand side is printed as \(|A|^2\).
The proof takes \(A_1=\log A\) in the cited Freiman dimension bound, so \(|A_1+A_1|=|AA|\) is the cardinality required by that argument.
The proper progression containing \(\log A\) has at most \(\alpha\) generators in \(\log\mathbb Q_{>0}\), whence exponentiation and prime-valuation coordinates bound the affine dimension as in (1.19)–(1.20).
Proposition 12 immediately below uses \(|A^2|\) with the exponent inside the cardinality signs.
The stated Freiman input is accepted here at statement scope, without using a bound for the size of the progression or auditing the other sum-product theorems. [Published edition, pp. 948–949](readme.md#edition)
