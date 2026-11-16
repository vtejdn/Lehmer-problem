---
author: Yin
---

# One-sided isolation of atom masses for positive measures with integer Fourier coefficients

<a id="statement"></a>
## The mass at the identity

Let \(M\) be fixed and let \(\nu\) range over positive measures of mass at most \(M\) supported on a finite group of roots of unity of arbitrary order.
Suppose \(\int v^k\,d\nu(v)\in\mathbb Z\) for every integer \(k\).
The set of values of \(\nu(\{1\})\) contains no infinite strictly increasing sequence.
In particular for any real \(a\) there is an \(\eta(M,a)>0\) for which none of these masses lies in \((a-\eta(M,a),a)\).

<a id="cosets"></a>
## Inverting signed cosets

Consider a sequence of the measures with support in \(\mu_{N_n}=\{v:v^{N_n}=1\}\).
On \(\mathbb Z/N_n\mathbb Z\) the integer-valued function \(k\mapsto\int v^k\,d\nu_n(v)\) has normalized Fourier coefficients equal to the nonnegative point masses, so its Fourier algebra norm is at most \(M\).
By [Sanders's finite abelian theorem](../audits/literature/San20/Yin_U001.md#san20-u001) it is the sum of a bounded number of signed indicators of congruences \(k\equiv r_i\bmod d_i\) with \(d_i\mid N_n\).
Pass to a subsequence with fixed number of terms \(s\) and fixed signs \(\epsilon_i\).
Fourier inversion gives, for \(\xi\in\mu_{N_n}\),
\[
 \nu_n(\{\xi\})=\sum_{i:\xi^{d_i}=1}\frac{\epsilon_i\,\xi^{-r_i}}{d_i}.
 \tag{1}
\]
In particular only the signs and denominators influence the mass at the identity.

<a id="isolation"></a>
## The contribution of growing denominators

Every sequence of positive integers has a constant subsequence or a subsequence tending to infinity.
Make this choice simultaneously for each \(d_i\) and every ratio \(d_i/\gcd(d_i,d_l)\), with ordered pairs \(i,l\).
Group two indices together when both ratios for the pair are bounded.
This is an equivalence relation since it is equivalent, after the extraction, to a fixed rational ratio \(d_i/d_l\).
In a class write \(D=\gcd_i d_i\), taking the gcd over that class alone.
The ratios \(d_i/D=k_i\) are fixed positive integers, as follows by clearing the denominators of the fixed ratios and removing their common gcd.
The class contributes \(b/D\) to the mass at the identity, where \(b=\sum_i\epsilon_i/k_i\).

We show \(b\ge0\) whenever \(D\to\infty\).
For fixed \(\eta>0\), a fraction bounded below independently of \(n\) of the points \(\xi\in\mu_D\) satisfy \(|\xi^{-r_i}-1|<\eta\) for every member of the class.
Indeed partition the product of its unit circles into a fixed number of boxes of coordinate diameter less than \(\eta\).
Take a box containing at least the average number of images of points, counted with multiplicity, and divide all corresponding points by one of them.
For any foreign index \(l\), the fraction of \(\mu_D\) in \(\mu_{d_l}\) is \(\gcd(D,d_l)/D\).
After a further simultaneous extraction this fraction either tends to zero or has bounded reciprocal.
In the second case \(d_l/D\to\infty\), since a bounded subsequence of \(d_l/D\) would keep both indices relative to \(\gcd(D,d_l)\) bounded, and would put \(l\) in the same class as each \(k_iD\).
Thus one may choose a point of the boxes' difference set avoiding all the vanishing fractions, and each remaining foreign contribution to (1) there has absolute value \(o(1/D)\).
At that point the real part of the class contribution is at most \((b+s\eta)/D\).
If \(b<0\), choose \(\eta\) with \(b+s\eta<0\).
Equation (1) would then give a negative real mass for large \(n\), a contradiction.

On the extracted subsequence the classes with fixed denominators contribute a constant, and the growing classes contribute a nonnegative sum tending to zero.
An increasing sequence would converge strictly from below to that same constant, which is impossible.
Any sequence approaching \(a\) strictly from below has a strictly increasing subsequence, giving the stated one-sided interval.

## Assessment history

### Decision atom-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T13:38 |
| status | open |
| reason | Submit the one-sided isolation result with no bound on the order of the cyclic support. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Atom masses](#statement) | Fixed mass bound and arbitrary finite torsion support. |
| argument | [Coset inversion](#cosets) | Uniform number of terms and their atomic weights. |
| argument | [Denominator classes](#isolation) | Positivity on simultaneous phase neighbourhoods and the sign of each growing class. |
| dependency | [Sanders's theorem](../audits/literature/San20/Yin_U001.md#san20-u001) | Signed-coset representation on finite abelian groups with length bounded in terms of the Fourier algebra norm. |

### Decision atom-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T13:53 |
| status | proved |
| reason | Adopt the one-sided isolation theorem after independent review of the coset inversion, subgroup intersections and use of positivity. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Atom masses](#statement) | Fixed mass bound and arbitrary finite torsion support. |
| argument | [Coset inversion](#cosets) | Uniform number of terms and their atomic weights. |
| argument | [Denominator classes](#isolation) | Positivity on simultaneous phase neighbourhoods and the sign of each growing class. |
| dependency | [Sanders's theorem](../audits/literature/San20/Yin_U001.md#san20-u001) | Signed-coset representation on finite abelian groups with length bounded in terms of the Fourier algebra norm. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v6.md#atom-isolation-review) | All finite cyclic groups, the stated Fourier norm, sign of every growing class and the one-sided conclusion. |

## Current assessment

[Selected decision](#decision-atom-reviewed)
