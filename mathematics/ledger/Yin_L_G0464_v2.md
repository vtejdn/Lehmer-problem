---
author: Yin
---

# Rational limits for integer trace polynomials with a moving sign change

The [original moving-cut test](Yin_L_G0462_v2.md#central-sign-test) bounds three moments without bounding unsigned residue mass.
This gives a restriction on entire coefficient distributions in the probabilistic search, even if the cuts move through irrational points.

<a id="rational-prefix"></a>
## Rationality on passing to a coefficient limit

Use the single strictly negative then strictly positive residue transition and left endpoint sign of [L462 v2](Yin_L_G0462_v2.md#central-sign-test).
In particular \(B,Q\) are monic integral of degrees \(n,n+1\), \(Q/B=t-a+\sum_i r_i/(t-b_i)\), and the simple poles are strictly inside \([-2,2]\).
Write \(t=z+z^{-1}\), \(B^*=z^nB(t)\), \(P=z^{n+1}Q(t)\), and \(F=P/B^*=zQ(t)/B(t)\).
Thus \(F\) is holomorphic in the open disk, has integral Taylor coefficients and \(F(0)=1\).
For \(M(P)\le2\) every sequence of such \(F\)'s has a subsequence converging locally uniformly to a rational function.
Every coefficient limit is of this form.
If \(M(P)\to1\), each limit is a quotient of products of cyclotomic polynomials with its sign chosen to give constant coefficient one.
The statement permits two real exceptional roots as well as a conjugate pair.

Choose a separator \(c\) in the transition gap and set \(k=\sum r_i\), \(l=\sum b_i r_i\).
The three trace power sums in the [matching calculation](Yin_L_G0462_v2.md#central-sign-test) bound \(a,k,l\) uniformly.
Consequently the positive measure \(\mu=\sum_i(b_i-c)r_i\delta_{b_i}\) has total mass \(l-ck=O(1)\).
Pass to a subsequence with \(a,k\) fixed, \(c\to c_*\) and \(\mu\) converging weakly on \([-2,2]\) to a finite positive measure \(\mu_*\).
The division \((t-c)Q/B=(t-c)(t-a)+k+\int(t-b)^{-1}\,d\mu(b)\) gives
\[
 (1-cz+z^2)F(z)
 =(1-cz+z^2)(1-az+z^2)+kz^2+
       \frac{z^3}{1-z^2}K_\mu(z),\qquad
 K_\mu(z)=\int\frac{1-z^2}{1-bz+z^2}\,d\mu(b).
\]
The kernels and denominators are uniformly regular on every smaller closed disk as \(b,c\) vary in the trace interval.
Weak convergence therefore gives local uniform convergence of \(F\) to the same expression with \(c_*,\mu_*\); for example, expand the kernels on a slightly larger disk to get a uniform tail bound.
For \(b=\xi+\bar\xi\), \(|\xi|=1\), the integrand in \(K_\mu\) is half the sum of \((1+\xi z)/(1-\xi z)\) and \((1+\bar\xi z)/(1-\bar\xi z)\).
Thus \(K_{\mu_*}\) has nonnegative real part, and its Cayley transform \((K_{\mu_*}-1)/(K_{\mu_*}+1)\) is bounded by one in modulus.
It follows that \(K_{\mu_*}\) is a quotient of bounded holomorphic functions, also for zero mass.
Such quotients form a field and include rational functions, so the limiting \(F_*\) has bounded characteristic.
Its coefficients are limits of integers and hence are integers, individually eventually constant along the subsequence.
By [David G. Cantor, Theorem 1, p. 365](../audits/literature/Can63/Yin_U001.md#cantor-rationality), \(F_*\) is rational.
The theorem is used for its published statement, without claiming a new audit of its proof.

<a id="cyclotomic-prefix"></a>
## Why a shrinking shell leaves only cyclotomic rational limits

Every zero of \(P\) in the open disk has modulus at least \(1/M(P)\) by reciprocity and monicity; \(B^*\) has no open-disk zeros.
If \(M(P)\to1\), the functions \(F\) are eventually zero-free on each smaller disk.
The limit has constant coefficient one, so Hurwitz's theorem makes \(F_*\) zero-free throughout the disk.
Hence \(F_*^{-1}\) is also holomorphic there and its Taylor series is integral.

For clarity, any rational function \(f\) holomorphic in the disk with integral Taylor coefficients has a denominator that is a product of cyclotomics up to sign.
Let \(V\) be the rational span of all shifts of the sequence of its coefficients.
Rationality gives finite Hankel rank over \(\mathbb C\), hence also over \(\mathbb Q\) because the entries are rational.
Thus finitely many coordinate evaluations embed \(V\) into \(\mathbb Q^h\), and the lattice of integral sequences in \(V\) is a subgroup of \(\mathbb Z^h\) spanning \(V\).
The shift preserves this finitely generated lattice, so it has an integral matrix in a lattice basis.
For each \(\varepsilon>0\) the coefficients and each of their fixed shifts are \(O_\varepsilon((1+\varepsilon)^j)\) at coordinate \(j\), by analyticity in the disk.
In the chosen evaluation coordinates this bounds the growth of the powers of the shift on a basis and bounds its spectral radius by one.
Its nonzero eigenvalues and all their conjugates are therefore algebraic integers of modulus at most one and so roots of unity by Kronecker's theorem.
The matrix inverse \((I-z\,\mathrm{shift})^{-1}\) supplies a denominator \(\det(I-z\,\mathrm{shift})\) for \(f\) by evaluating the generating series of the shifted coefficient vectors at coordinate zero.
Applying this to \(F_*\) and its inverse proves the asserted classification, with the constant fixed by \(F_*(0)=1\).

<a id="prefix-law"></a>
## Consequence for discrete probability laws

On the original Chebyshev grid \(B=U_{d-1}(t/2)\), \(d=n+1\), one has \(B^*=(1-z^{2d})/(1-z^2)\).
As \(d\to\infty\), every limit of the original polynomials \(P\) is therefore \(F_* /(1-z^2)\).
In a shrinking shell all such limits are again cyclotomic quotients.
In particular suppose that a sequence of probability laws is supported on these integer polynomials, with degrees tending uniformly to infinity and \(1<M(P)\le1+\varepsilon_j\), \(\varepsilon_j\to0\).
In the topology of coefficientwise convergence, every subsequential weak limit of these laws is purely atomic.
Indeed local uniform boundedness as above bounds each integer coefficient by a constant depending only on its position, after multiplying by \(B^*\), which is uniformly bounded on smaller disks.
The resulting product of finite coordinate sets is compact and metrizable.
The intersection of the closures of the unions of supports over tails has full mass under any such weak limit, by the closed-set inequality.
Every point in that intersection is a limit of inputs from unbounded indices and hence a quotient of cyclotomics, a countable set.
This rules out a diffuse limit law on fixed original coefficient positions for this chamber.
A sequence can still share increasingly long prefixes with a single rational limit while its noncyclotomic contribution moves to higher coefficients.
No bound on the first differing coefficient, vanishing of the finite-degree event, or resolution of the unrestricted probability question follows here.

<a id="boundary-phase"></a>
## Locating the cut from a cyclotomic prefix

There is an additional constraint linking the stable coefficients to the limit \(c_*\) of the actual separators.
For \(t\) in the upper half-plane choose \(z+z^{-1}=t\) with \(|z|<1\), and put \(R(t)=F_*(z)/z\).
The limiting division above gives
\[
 (t-c_*)R(t)-(t-c_*)(t-a)-k=\int\frac{d\mu_*(b)}{t-b}.
\]
The imaginary part of the right side is nonpositive.
At any interior \(u=2\cos\theta\), \(0<\theta<\pi\), where \(F_*\) is regular at \(\zeta=e^{-i\theta}\), approach \(u\) from the upper half-plane.
The disk branch tends to \(\zeta\), so \((u-c_*)\operatorname{Im}(F_*(\zeta)/\zeta)\le0\).

Suppose \(M(P)\to1\) and \(c_*\) is interior but not a trace of a root of unity.
The cyclotomic quotient \(F_*\) has neither pole nor zero above \(c_*\).
Continuity on both sides of that point then forces \(F_*(\zeta)/\zeta\) to be real there.
Write \(D=\deg(\mathrm{numerator})-\deg(\mathrm{denominator})\); reversal of each cyclotomic factor gives \(F_*(1/z)=\sigma z^{-D}F_*(z)\), \(\sigma\in\{1,-1\}\).
Reality at this nontorsion \(\zeta\) gives \(1=\sigma\zeta^{2-D}\), whence \(D=2,\sigma=1\).
Thus \(F_*(z)/z\) is invariant under \(z\mapsto1/z\); it is a real rational function of \(t\), since \(z\) satisfies \(z^2-tz+1=0\) over \(\mathbb R(t)\).
This forces the Cauchy transform above to be rational in \(t\), with possible poles only at traces of the finitely many roots of unity that are poles of \(F_*\).
At infinity the transform is proper.
Consequently \(\mu_*\) is a finite atomic measure supported on those traces: at a real pole \(v\), dominated convergence in \(i\eta\int(v+i\eta-b)^{-1}d\mu_*(b)\) gives its mass and rules out a higher pole.
Subtract those atoms; the residual rational transform has no poles and tends to zero at infinity, so all its moments vanish, giving the zero residual measure by polynomial approximation.
This assertion is about the weighted measure in the limit, with no rate for a shrinking neighborhood of the cut.

There is a concrete test even without assuming \(M(P)\to1\).
Suppose \(M(P)\le2\) on the Chebyshev grid, \(d\to\infty\), and the first nonconstant nonzero coefficient of \(P\) tends to infinity in index.
Then \(P\to1\) coefficientwise, hence \(F_*=1-z^2\).
For every interior \(u\) as above, \(\operatorname{Im}(F_*(\zeta)/\zeta)=2\sin\theta>0\).
The boundary inequality requires \(u\le c_*\) for every \(u<2\), and therefore every subsequential cut limit is \(2\).
In particular a construction that puts its entire perturbation at growing exponents must push the change of sign to the right endpoint; it cannot realize a nontrivial interior moving cut.

<a id="torsion-limits"></a>
## On the original Chebyshev grid every limiting separator is a torsion trace

For this additional step, proposed by agent-S, suppose \(d\to\infty\) and choose the angular midpoint in each transition gap.
Changing the separator to this point changes its location by at most the maximal Chebyshev mesh, which tends to zero.
Write \(n=d-1\) and \(\mu_i=(b_i-c)r_i>0\).
Using the same derivative product as in the [original resultant calculation](Yin_L_G0464_v1.md#angular-midpoint-resultant), but now with no division by the exceptional-root distances, gives
\[
     \prod_{i=1}^n\mu_i
       = |B(c)|\,|\operatorname{Res}(B,Q)|\,\frac{d^2}{(2d)^n}.
\]
In particular \(n(\prod \mu_i)^{1/n}\ge (d-1)/(2d)\), since \(|B(c)|\ge1\) and strict residues give a nonzero integral resultant.
This argument does not require the two exceptional trace roots to be nonreal.
Every nonempty open subinterval of \((-2,2)\) contains a closed subinterval \(I\) of positive length strictly inside it.
The fraction \(\alpha_d\) of grid points in \(I\) tends to a number in \((0,1)\) by uniform spacing in angle.
Writing \(T_d=\sum\mu_i=O(1)\) and \(m_I=\sum_{b_i\in I}\mu_i\), two applications of arithmetic-geometric mean give
\[
 n\Big(\prod\mu_i\Big)^{1/n}
 \le (m_I/\alpha_d)^{\alpha_d}
          \big((T_d-m_I)/(1-\alpha_d)\big)^{1-\alpha_d}.
\]
Thus \(\liminf m_I>0\), and the closed-set inequality for weak convergence gives \(\mu_*(I)>0\).
Every weak limit of these weighted measures has full support on \([-2,2]\).
This contradicts the finite atomic consequence above whenever \(c_*\) is interior and not a torsion trace.
Therefore every separator accumulation point on a shrinking-shell sequence in this chamber, endpoints included, is \(2\cos(2\pi r)\) for some rational \(r\).
These traces form a dense countable set, and the proof supplies no speed of convergence or bound on the denominators over different sequences.
If the shrinking measures are strictly positive (\(0<\log M(P)\to0\)), the [fixed algebraic weight condition](../claims/Yin_C_G0880_v2.md#moving-cut) also requires \(|c-c_*|\sum|r_i|\to\infty\) along any subsequence with this fixed limit.
