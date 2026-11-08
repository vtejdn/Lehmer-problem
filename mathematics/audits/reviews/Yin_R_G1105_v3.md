---
author: Yin
---

# Independent review of rational coefficient limits and the boundary phase

<a id="prefix-rigidity-review"></a>
## Rationality, atomic laws and the separator

At 2026-11-08T02:11 UTC a separately assigned agent for Yin reviewed the four sections of L464 v2 named below, from rational compactness through the boundary-phase test.
The reviewer took no part in developing these arguments and received the fixed text and dependency locators without development dialogue or author explanation.
The earlier [fixed-weight review](Yin_R_G1105_v2.md#weighted-lift-review) concerned the matching and weighted-mass input.
The reviewer rederived that input and checked the four deductions directly.

**Compactness and Cantor's theorem.**
Each of the \(n-2\) same-sign pole gaps gives a real zero by the opposite one-sided limits, and the left endpoint sign gives a zero before the first pole.
Assign each selected zero to the right endpoint of its interval.
One pole and two trace roots remain, counted with multiplicity.
For a reciprocal pair above any trace root, its larger radius \(R\) satisfies \(1\le R\le M(P)\), so both remaining traces have modulus at most \(R+R^{-1}\le5/2\) when \(M(P)\le2\).
The matched intervals have disjoint interiors, bounding their total contribution to each power-sum difference by the variation of \(t^h\) on \([-2,2]\), for \(h=1,2,3\).
Expansion of \(\log(Q/(tB))\) through order three then bounds \(a,k,l\) as stated, without a restriction on the reality or multiplicity of the exceptional roots.
Monic division gives integral \(a\), and \(k\) is the coefficient of \(t^{n-1}\) in the integral proper numerator.
Thus bounded \(a,k\) can be fixed along a subsequence.

I checked the identity by substituting \((t-c)/(t-b)=1+(b-c)/(t-b)\) in the secular function.
The resulting weights \((b_i-c)r_i\) are nonnegative for every allowed choice of separator and sum to \(l-ck\).
Their weak subsequential limit is finite and positive in the sense of measures, permitting the zero measure.
On \(|z|\le s<1\), each factor \(1-bz+z^2\) has modulus at least \((1-s)^2\), also when \(b=\pm2\).
This bound holds for the separator factor as well, and weak convergence against the resulting compact family of continuous kernels gives locally uniform convergence.
The averaged Cayley kernels have nonnegative real part, so \(w=(K-1)/(K+1)\) satisfies \(|w|\le1\).
Writing \(K=(1+w)/(1-w)\) gives bounded holomorphic numerator and denominator even when \(K=0\).
The field of bounded-characteristic functions therefore contains the limit of \(F\).
Local uniform convergence makes each integral coefficient eventually constant, and every coefficientwise limit has a locally uniform subsequence with the same coefficients.
Cantor's definition on printed p. 362 and Theorem 1 on p. 365 apply exactly to this holomorphic function with integral Taylor series.
The [published article](https://www.ias.edu/sites/default/files/Cantor%20-%20Power%20series%20with%20integral%20coefficients.pdf) and [source unit](../literature/Can63/Yin_U001.md#cantor-rationality) agree on the hypotheses.

**Cyclotomic classification.**
Reciprocity and monicity give \(|\alpha|\ge M(P)^{-1}\) at every zero in the disk, and \(F(0)=1\) rules out the identically zero alternative in Hurwitz's theorem.
The analytically invertible limit has an integral reciprocal Taylor series by the unit constant coefficient.
For either series, rationality gives finite rank of its shift space by the coefficient recurrence, with any finite initial transient included.
Finite coordinate evaluations inject the rational shift space into a finite-dimensional rational vector space.
The lattice of integral sequences embeds in the corresponding integer lattice and spans the shift space because the original shifts are integral.
The shift acts integrally on this lattice.
For a fixed lattice basis, Cauchy estimates at any \(s<1\) give \(O_s(s^{-j})\) for the evaluated entries of its \(j\)-fold shift, since each basis vector is a fixed linear combination of shifts of the original sequence.
This bounds the spectral radius by one, and every conjugate of each nonzero eigenvalue is also an eigenvalue of the integral matrix.
Kronecker's theorem now applies, while zero eigenvalues contribute a unit factor to \(\det(I-zS)\).
Evaluation of the resolvent at the original sequence gives a denominator of this form.
Applying the argument to both series leaves only cyclotomic factors in the reduced numerator and denominator, with the constant multiplier fixed by \(F_*(0)=1\).

**Limit laws.**
On the stated Chebyshev grid, \(P=F(1-z^{2d})/(1-z^2)\), so along \(d\to\infty\) the limits of \(P\) are \(F_* /(1-z^2)\).
The compactness estimate gives finitely many integer possibilities at each fixed coordinate for the tail with \(M(P)\le2\).
For each tail, the closure of its union of supports has mass one under any subsequential weak limit by the closed-set inequality.
Their intersection also has mass one, and metrizability lets one approximate each of its points by allowed inputs from indices tending to infinity.
The uniform degree and shrinking-shell hypotheses thus apply to this approximating sequence.
Every point of the intersection is a cyclotomic quotient and these form a countable set, which gives pure atomicity.
The order of this argument matters because the closure of an arbitrary countable set can be uncountable.

**Boundary phase.**
For \(z=r e^{-i\theta}\), \(0<r<1\) and \(0<\theta<\pi\), one has \(\operatorname{Im}(z+z^{-1})=(r^{-1}-r)\sin\theta>0\).
Taking \(r\uparrow1\) in the Cauchy-transform identity gives the stated inequality at every regular boundary point, with the indicated lower semicircle and sign.
On both sides of an interior nontorsion cut the rational limit has neither pole nor zero sufficiently near that cut.
The sign inequality forces \(F_*(\zeta)/\zeta\) to be real at the cut, and conjugation followed by reversal gives \(1=\sigma\zeta^{2-D}\).
A nonzero exponent would make \(\zeta\) torsion even for \(\sigma=-1\), so \(D=2\) and \(\sigma=1\).
The invariant rational function lies in \(\mathbb R(t)\), the fixed field of the nontrivial involution in the quadratic extension \(\mathbb R(z)/\mathbb R(z+z^{-1})\).
Each finite pole of the resulting proper Cauchy transform lifts to a pole of \(F_*\), also at a ramified endpoint if that endpoint is a pole.
For a putative pole \(v\), the kernel \(i\eta/(v+i\eta-b)\) has modulus at most one and tends to the indicator of \(\{v\}\).
This excludes higher poles and identifies each residue with its positive atom.
After subtracting those atoms the rational transform vanishes by properness, and uniqueness of moments on the compact interval gives zero residual measure.

As a boundary check, the test quotient \(1+z^3\) has imaginary part \((1-u)\sin\theta\) after division by \(\zeta\) on that semicircle.
It satisfies the boundary inequality for \(c_*=1\) with \(D=3\), demonstrating the need for the nontorsion hypothesis in the phase deduction alone.
Its realization as a limit in the chamber is outside this test.
For the claimed long constant prefix, the exact Chebyshev multiplier gives \(F_*=1-z^2\) and the imaginary part becomes \(2\sin\theta>0\).
Every subsequential cut limit is consequently \(2\), already under \(M(P)\le2\).

The four deductions pass with the stated strict two-block and endpoint assumptions and their additional grid or shrinking-shell hypotheses where indicated.
Cantor's rationality theorem, Hurwitz's theorem and Kronecker's theorem were used as external results without an independent review of their proofs.
The findings concern coefficientwise laws and the limiting weighted measure, with no estimate for a first differing coefficient, finite-degree event probability or concentration rate.
Coverage ends at the long-prefix endpoint test.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Prefix rigidity](#prefix-rigidity-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Prefix rigidity](#prefix-rigidity-review) | [Rational compactness](../../ledger/Yin_L_G0464_v2.md#rational-prefix) | Matching input, positive weighted mass, normal family and Cantor's rationality theorem for every coefficient limit. |
| [Prefix rigidity](#prefix-rigidity-review) | [Cyclotomic limit](../../ledger/Yin_L_G0464_v2.md#cyclotomic-prefix) | Shrinking shell, integral shifts and the cyclotomic classification of both numerator and denominator. |
| [Prefix rigidity](#prefix-rigidity-review) | [Coefficient laws](../../ledger/Yin_L_G0464_v2.md#prefix-law) | Chebyshev multiplier, uniform degree escape and pure atomicity of subsequential weak limits on coefficient space. |
| [Prefix rigidity](#prefix-rigidity-review) | [Boundary phase](../../ledger/Yin_L_G0464_v2.md#boundary-phase) | Half-plane sign, nontorsion interior cut, atomic weighted limit and the long constant-prefix endpoint test. |
