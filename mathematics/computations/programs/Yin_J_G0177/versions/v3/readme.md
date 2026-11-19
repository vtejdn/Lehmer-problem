---
author: Yin
---

# Finding the double factors of a unit and its square on a fixed row

<a id="test"></a>
## All integer exponents for one row

For a nonzero integral row \(A\), its formal width \(b\), and either graph sign, the [program](square_pairs.py) lists every pair consisting of \(n\ge2\) and a Galois orbit of nontorsion units \(\delta\) for which both \(\delta,\delta^2\) have genuine double contact.
The graph is \(A(X^n)+\varepsilon X A_b^*(X^n)\), where \(A_b^*(Y)=Y^b A(1/Y)\).
Both powered numerator values are required to be nonzero.
The [square identity and exponent recovery](../../../../../claims/Yin_C_G0345_v428.md#inverse) reduce all exponents to factoring one polynomial of degree at most \(4b\).
The algorithm tests repeated monic unit factors other than cyclotomic polynomials and carries out the remaining derivative and power tests in their exact rational residue fields.
The output represents \(\delta\) as a polynomial in \(\beta=\delta^n\) and checks the strict coefficient budget independently for each actual pair.

<a id="controls"></a>
## Two rows with the same genuine pair

From the repository root, with Python and SymPy, run

~~~text
python -B mathematics/computations/programs/Yin_J_G0177/versions/v3/square_pairs.py --sign -1 1 166 1211 626 21
python -B mathematics/computations/programs/Yin_J_G0177/versions/v3/square_pairs.py --sign 1 -- -1 -126 -251 334 19
python -B mathematics/computations/programs/Yin_J_G0177/versions/v3/square_pairs.py --sign -1 0 1 0
~~~

Coefficients are in increasing degree and terminal zeros count toward the formal width.
The first two rows have one-norms 2025 and 731, respectively.
Each has exactly one orbit over all exponents, at \(n=2\), with \(\beta^2-7\beta+1=0\) and \(\delta=(1+\beta)/3\).
Consequently \(\delta^2=\beta\) and \(\delta^2-3\delta+1=0\).
In both cases the powered minimum occurs to order two in the square identity, and the original signed row fails the strict size budget.
The third row gives an identically zero square identity and has no genuine pair.
Each command prints the complete result as JSON.
