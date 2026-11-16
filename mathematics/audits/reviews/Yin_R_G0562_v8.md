---
author: Yin
---

# Review of the uniform positive-constant bound on the leading-two Chebyshev path

An agent outside the proof development of C345v8 and L462v52 reviewed both fixed arguments for Yin on 2026-11-16T14:36 UTC.
The assignment supplied the targets without proof-development discussion or prior conclusions on these arguments.
The reviewer had previously checked the three-profile reduction in L462v49 and the location and shapes of the first discrepancy in L462v50.

<a id="chebyshev-path-review"></a>
## The uniform bound

The argument excludes every unbounded sequence of positive constants \(q\) on the stated path and covers both degree parities of the Pisot polynomial.
The bound is qualitative.

### Comparing every positive harmonic

For every fixed \(k\ge1\) and \(l\in\mathbb Z\), \(n\to\infty\) and \(n/h\to0\) put both \(kn+l\) and \(kn+l-1\) between 1 and \(2h\) eventually.
One weak limit on the product of circles suffices for all these pairs, since each \(v^l u^k\) is a fixed continuous test function.
At any atom \(v_0\) of the first marginal \(\tau\), the first discrepancy argument in L462v49 identifies the complex mass of the \(u\)-weighted projection as \(\xi_{v_0}\tau(\{v_0\})\), with \(|\xi_{v_0}|=1\).
The integral of \(|u-\xi_{v_0}|^2\) on that fiber is therefore zero.
Consequently its contribution to the \(k\)-th weighted projection is exactly \(\xi_{v_0}^k\tau(\{v_0\})\), including when mass approached \(v_0\) along nearby points before the weak limit.

For \(m=kn+l\), the positive measure \(2(\omega_q-\alpha\delta_1)\) has \(m\)-th moment \([z^m]J_q-2\alpha\), where \(\alpha\to0\).
The moment of \(\tau\) is \([z^m]J\), and its continuous contribution tends to zero because \(m\to\infty\).
Its atoms give exactly the fixed phases in the \(k\)-th weighted projection, since the extraction fixes \(v_0^n\) for every torsion atom.
After canceling these terms, reflection in the first coordinate turns the remaining \(v^l\) moment into the \(l\)-th Fourier coefficient of \(\sigma c_k\), with the same conditional probability in the \(u\) coordinate for every \(k\).
Multiplication by \(1-v/2\) gives the difference of this coefficient and half the preceding one.
The exact prefix identity through degree \(2h\) makes this the limit of the corresponding integer coefficients of \(B^\sharp-B_\infty\).
Because \(\sigma\) is bounded and \(|c_k|\le1\), Parseval gives square summability for all \(l\in\mathbb Z\).
Thus only finitely many Fourier coefficients of \(H_k=(1-v/2)\sigma c_k\) are nonzero, and \(H_1\ne0\) by the first discrepancy.
Shifting the least exponent in a nonzero \(H_k\) preserves its boundary modulus and gives the integer polynomial with nonzero constant needed in the L462v50 classification.

### Both endpoint exclusions in L462v52

The same conditional probability gives \(|c_{2r}-c_r^2|\le 1-|c_r|^2\) by comparing the integrals of \((u^r-c_r)^2\) and \(|u^r-c_r|^2\).
For \(K=(2-z)/(1-z)\) direct substitution gives \(c_k=0\) or \(\pm v^{d_k}(1-2v)/3\).
The expression extends over \(v=1\), where the density vanishes.
At \(v=-e^{it}\), \(|c_1(-1)|=1\), and \(1-|c_1|^2=O(t^2)\) forces \(c_2\) to be nonzero and its value and first derivative to coincide with those of \(c_1^2\).
The resulting phase derivative equality would give \(d_2-2d_1=2/3\), impossible for integers.

For \(K=(2-z)(1+z)\), subtracting the separate atom at \(-1\) leaves the continuous density stated in L462v52 and \(c_k=0\) or \(\pm v^{d_k}(2-v^{-1})/(3-x)\).
At \(v=e^{it}\) one has \(1-|c_1|^2=(2-x)^2/(3-x)^2=O(t^4)\), hence \(c_2\) is nonzero and \(c_2/c_1^2=1+O(t^4)\) near \(t=0\).
The continuous local phase of this ratio must vanish through degree three.
Expansion of the logarithm gives \(\Im\log(2-e^{-it})=t-t^3+O(t^5)\).
Multiplication by a signed integral monomial changes the constant and linear phase terms only.
The cubic coefficients of \(c_2\) and \(c_1^2\) are therefore \(-1\) and \(-2\), which excludes this second profile.

### The remaining profile at three circle points

For \(K=2-z\), the density \(\sigma=2(4-x)/|2-v|^2\) is strictly positive and the factor converting \(H_r\) to \(c_r\) is \((2-v^{-1})/(4-x)\).
I checked these identities and the preceding two formulas by rational simplification on substituting \(v^{-1}=\bar v\).
The resulting moments are continuous functions of \(v\).
For each matrix size they form a positive semidefinite Toeplitz matrix almost everywhere, hence everywhere by continuity and positivity of the marginal density on open arcs.
With \(c_0=1\) and \(c_{-r}=\overline{c_r}\), the Herglotz theorem now gives a circle probability at every evaluation point.

At \(v=-1\), the common factor is \(1/2\), and either allowed binomial has modulus two.
If \(c_r\) comes from a binomial, the variance inequality forces \(c_{2r}(-1)=c_r(-1)^2\) of modulus one.
Thus \(c_{2r}\) must also come from a binomial.
Smoothness and nonnegativity of \(1-|c_r|^2\) give a double zero or higher there, so the local first phase derivatives agree for \(c_{2r}\) and \(c_r^2\).
At \(v=-e^{it}\) the numerator \(2+e^{-it}\) contributes \(-1/3\).
The two binomials contribute \(1/2\) and \(1\), giving residues \(1/6\) and \(2/3\) modulo one after allowing the integral monomial.
Doubling either gives \(1/3\) modulo one, impossible for \(c_{2r}\).
This argument eliminates binomials for every positive \(r\).

At \(v=i\), every remaining nonzero moment is \((2+i)/4\) times a fourth root of unity.
The real and imaginary parts multiplied by four are integers at all positive, zero and negative indices.
Each sequence is the Fourier–Stieltjes transform of a finite complex measure by combining the probability \(\lambda_i\) with its reflected measure.
I checked the locally compact hypothesis and the integer-valued transform conclusion in [Sanders's published Corollary 12.4](https://link.springer.com/article/10.1007/s00041-020-09732-y).
On the discrete integers its finite coset representation contains congruences and possibly singletons, giving a common eventual period \(D\) for both parts.
Averages on \(Dl+a\) converge by the geometric sum to \(\int_{u^D=1}u^a\,d\lambda_i\).
For \(a=0\) this is real and nonnegative, while all four allowed nonzero moments are nonreal.
Thus \(\lambda_i(\{u:u^D=1\})=0\) and every residue class has eventual value zero.
Only finitely many \(c_r(i)\) are nonzero, which makes the entire \(H_r\) sequence finitely supported in \(r\) because each nonzero Laurent monomial is nonzero at \(i\).
This use of Sanders is at statement and application scope.

At \(v=1\), the surviving values of \(c_r(1)\) are \(0,\pm1/2\).
Fourier uniqueness gives \(2\lambda_1\) a finite continuous even density of mean two with integer Laurent coefficients, nonnegative everywhere by positivity of the measure.
The finite integer mean-two theorem in C403v1 allows at most one nonzero positive frequency.
Frequency one survives since \(H_1\) is a nonzero monomial, and every other nonzero \(H_r\) would also survive at one.
Thus all moments of order \(r\ge2\) vanish identically, forcing \(|c_1(v)|\le1/2\) from the minimum of \(1+2\Re(c_1(v)\bar u)\).
But \(4|c_1|^2-1=(4-x^2)/(4-x)^2>0\) at each \(-2<x<2\).
This excludes the final candidate.

Every sequence with \(q\to\infty\) would have supplied a subsequential candidate among these three, so the constants are uniformly bounded.
Both parities enter the same trace argument under the exact inverse construction.
Finally \(2/(\theta-q)=q+\theta^{-1}-H'_q(0)\le q+3\) gives the claimed positive lower bound for the excess.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Uniform path bound](#chebyshev-path-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Uniform path bound](#chebyshev-path-review) | [C345v8 statement](../../claims/Yin_C_G0345_v8.md#statement) | The full path in both degree parities, bounded constants and the uniform excess consequence. |
| [Uniform path bound](#chebyshev-path-review) | [Continuous moment fibers](../../claims/Yin_C_G0345_v8.md#fibers) | Continuous representatives at every index, Toeplitz positivity at each point and existence of the fiber probabilities there. |
| [Uniform path bound](#chebyshev-path-review) | [Binomial exclusion](../../claims/Yin_C_G0345_v8.md#binomials) | Saturation at minus one, second moments and phase derivatives for every harmonic. |
| [Uniform path bound](#chebyshev-path-review) | [Specialization](../../claims/Yin_C_G0345_v8.md#specialization) | Discrete-group integer transforms, progression means, finite support, mean-two classification and the final strict inequality. |
| [Uniform path bound](#chebyshev-path-review) | [Two endpoint profiles](../../ledger/Yin_L_G0462_v52.md#exclusions) | Both excluded limiting profiles in the inverse construction. |
| [Uniform path bound](#chebyshev-path-review) | [Every harmonic](../../ledger/Yin_L_G0462_v52.md#harmonics) | Simultaneous limits, atomic phases, reflection, disintegration, two-sided integer coefficients and allowed Laurent shapes. |
| [Uniform path bound](#chebyshev-path-review) | [Endpoint slopes](../../ledger/Yin_L_G0462_v52.md#slopes) | Explicit densities, variance order, incompatible linear derivative at minus one and cubic phase at one. |
| [Uniform path bound](#chebyshev-path-review) | [First discrepancy](../../ledger/Yin_L_G0462_v49.md#departure) | Fixed atomic phases, canceled first weighted projection and nonzero first discrepancy. |
| [Uniform path bound](#chebyshev-path-review) | [Three candidate profiles](../../ledger/Yin_L_G0462_v49.md#exclusions) | Exhaustion of subsequential limits on this path. |
| [Uniform path bound](#chebyshev-path-review) | [Sublinear departure](../../ledger/Yin_L_G0462_v50.md#window) | Availability of \(kn+l\) and the preceding index in the exact Taylor range. |
| [Uniform path bound](#chebyshev-path-review) | [Polynomial shapes](../../ledger/Yin_L_G0462_v50.md#shapes) | All three lists after shifting the least exponent of a nonzero integer Laurent polynomial. |
| [Uniform path bound](#chebyshev-path-review) | [Integer Fourier–Stieltjes transforms](../literature/San20/Yin_U001.md#fourier-stieltjes) | Locally compact Corollary 12.4 and its application on the infinite discrete group of integers. |
| [Uniform path bound](#chebyshev-path-review) | [Mean-two classification](../../claims/Yin_C_G0403_v1.md#integer-mean-two-classification) | Finite even nonnegative symbol with integer Laurent coefficients and constant two. |
| [Uniform path bound](#chebyshev-path-review) | [Pisot excess](../../ledger/Yin_L_G0462_v36.md#second) | Exact derivative formula and the bound \(2/(q+3)\) for the second branch. |
| [Uniform path bound](#chebyshev-path-review) | [Inverse simplices](../../ledger/Yin_L_G0462_v43.md#inverse) | Reconstruction in both degree parities, including the odd-degree equality face. |
