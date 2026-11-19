---
author: Yin
---

# Exact costs of five signed coefficients at a quadratic unit and its square

<a id="costs"></a>
## The least width and the next width

Let \(\delta=(3+\sqrt5)/2\), or more generally let \(c>1\) be a real quadratic reciprocal unit of integer trace \(T\equiv3\pmod{1009}\), with \(T\ge3\).
In the first case take \(c=\delta\).
Fix a formal width \(b\), a five-element set \(I\subseteq\{0,\ldots,b\}\) and a sign \(\varepsilon=\pm1\).
We seek an integer row \(A(Y)=\sum_{j\in I}a_jY^j\) whose graph \(A(X^n)+\varepsilon X^{nb+1}A(X^{-n})\) has double zeros at \(c,c^2\) and satisfies \(A(c^n)A(c^{2n})\ne0\).
At all sufficiently large \(n\) the listed supports give exactly one rational line, genuine at both nodes.
For its primitive integral generator let \(\rho=\lim_{n\to\infty}\log\|A\|_1/(n\log c)\).
Both signs have the rates in the table.

| Width \(b\) | Support \(I\) | Raw minimum and maximum \(z\)-degrees | \(\rho\) |
| ---: | --- | --- | ---: |
| 4 | All five positions | \(2,22\) | 8 |
| 5 | Omit \(0\) or \(5\) | \(5,25\) | 8 |
| 5 | Omit \(1\) or \(4\) | \(3,27\) | 10 |
| 5 | Omit \(2\) or \(3\) | \(2,28\) | 11 |
| \(6\le b\le12\) | \(\{0,1,2,3,b\}\) | \(3,6b-3\) | \(3b-5\) |

The [small-support bound](../../../../../claims/Yin_C_G0345_v446.md#statement) makes five the fewest possible positions at every fixed width \(b\ge4\).
At width four \(8\log c\) is therefore the least genuine rate among all rows.
At width five it is the least rate among five-position rows.
For every width tending to infinity, with no support bound, the square pair has sharp rate \(3\log c\) by the [signed-row theorem for powers of one unit](../../../../../claims/Yin_C_G0345_v434.md#statement).

For each tabulated \((b,I)\), every \(d\ge1\) and \(u\ge0\) multiply the normalized rate \(\rho\) by \(d\) at width \(db+2u\) on support \(dI+u\).
Indeed \(A(Y)=Y^u B(Y^d)\) identifies the signed graph there with \(X^{nu}\) times the signed graph of \(B\) of width \(b\) at exponent \(dn\).
The substitution preserves primitivity and the one-norm and multiplies both tested numerator values by nonzero powers of \(c\).
In particular every fixed width \(b\ge4\) admits a five-position line of rate \(8\log c\), by translating a width-four example for even \(b\) and a width-five endpoint omission for odd \(b\).

<a id="certificate"></a>
## Characteristic-zero division and a finite-field coprimality certificate

Use indeterminates \(C,x,z\) in place of \(c,n,c^n\), respectively.
In column \(j\), the two rows for \(k=1,2\) are the value and Euler derivative
\[
 V_{kj}=z^{kj}+\varepsilon C^kz^{k(b-j)},\qquad
 E_{kj}=jx z^{kj}+\varepsilon C^k((b-j)x+1)z^{k(b-j)} .
\]
Let \(D_j\) be their signed maximal minors in the four-row order \(V_1,E_1,V_2,E_2\), omitting one column at a time in increasing order of \(I\).
The [program](square_circuits.py) expands all five determinants in \(\mathbb Z[C,x,z]\), reads the lowest and highest \(z\)-degrees \(l,h\) across the tuple, and divides each minor exactly by \(z^l(z-1)^4\).
Write \(H_j\) for these quotients and \(D=h-l-4\).
Under \(C=384,\ x=7\) in \(\mathbb F_{1009}\), the five \(H_j\) are nonzero, have gcd one and attain maximum degree \(D\).
At \(z=2\) the two sums \(\sum_jH_jz^{kj}\) are nonzero in every case.
For example, at width four the residues of these sums in node order are \((274,526)\) for the negative sign and \((8,132)\) for the positive sign.

Since \(384^2-3\cdot384+1\equiv0\pmod{1009}\), the modular substitution factors through \(\mathbb Z[c,x]\) for every indicated trace.
The reduced tuple over \(\mathbb Q(c)(x)[z]\) also has gcd one.
Indeed choose a member attaining degree \(D\) after the substitution and invert its leading coefficient.
In the quotient by this member, the products of the other members with \(1,z,\ldots,z^{D-1}\) span the whole quotient after reduction, by the finite-field gcd.
A nonvanishing \(D\)-rowed minor of their coefficient matrix lifts, proving the same spanning statement over \(\mathbb Q(c)(x)\).
Consequently the tuples over \(\mathbb Q(c)[x,z]\) have no further common factor of positive \(z\)-degree, and their \(z\)-exponents have spread \(D\).
Any common factor in \(x\) alone can be cancelled without changing this spread.

Every tested numerator sum and every coordinate remains nonzero as a polynomial after \(C=c\).
At \(x=n,z=c^n\) its highest surviving \(z\)-power dominates all lower ones for large \(n\), since its coefficient is a nonzero polynomial in \(n\).
The nonzero cofactors yield a one-dimensional kernel on all five positions, and the two numerator tests prove genuineness.
The signed graph is reciprocal up to sign, so at these specializations it also has double contact at the inverse nodes.
The equations thus specify the same kernel as divisibility by the squared product of the two rational minima, making this line rational.

Apply the [one-parameter projective height calculation](../../../../../ledger/Yin_L_G0462_v257.md#height) to this coprime tuple with the single unit \(c\).
The two real embeddings send \(c\) to \(c\) and \(c^{-1}\), so their archimedean contributions together give \(nD\log c/2+O(\log n)\).
The common finite divisor after specialization has logarithmic cost \(o(n)\) by the cited calculation.
The resulting absolute projective height is the log maximum norm of the primitive integral generator, within \(\log5\) of its log one-norm.
Thus \(\rho=D/2\).

Run the following command from the repository root with Python and SymPy.
It prints both signs for every five-position support through width five and the indicated support at each width from six through twelve, including the two numerator residues for each row.

~~~text
python -B mathematics/computations/programs/Yin_J_G0177/versions/v4/square_circuits.py
~~~
