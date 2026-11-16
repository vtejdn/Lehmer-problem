---
author: Yin
---

# Review of the two-point Pisot bound and the complete fixed Salem fiber

An agent outside the development of C345v4 reviewed the fixed claim for Yin on 2026-11-16T13:06 UTC.
The assignment identified the claim and its mathematical scope, without development discussion or an earlier verdict.

<a id="pisot-simplex-review"></a>
## Finite inequalities, enumeration and second-order optimum

Both inequalities (1), the exact open simplex (5), its lattice count (2), and the fixed-output lower limit (3) hold under their stated hypotheses.

### The two disk values

Since \(q>1\), the irreducible monic Pisot polynomial is coprime to its reversal, and the exterior reciprocal pair of \(zf+f^*\) is simple by L462v32.
Removing the exterior factor from \(f/f^*\) leaves the product of the disk factors of the \(\deg f-1\) interior conjugates, after reordering the conjugate multiset in the denominator.
It is a holomorphic disk map with \(F(0)=-q/\theta\).
At \(1/\sigma\) the denominator \(f^*\) cannot vanish, because then the reciprocal identity would also force \(f\) to vanish there.
Substitution gives \(F(1/\sigma)=s(s-t)/(ts-1)\) with \(s=\sigma,\ t=\theta\).
Solving the real Schwarz–Pick interval at \(0,1/s\) gives the lower endpoint \(-(qs+t)/(ts+q)\) and upper endpoint \((t-qs)/(ts-q)\).
All denominators are strictly positive.
Multiplying the upper endpoint minus \(F(1/s)\) by \((ts-q)(ts-1)\) gives \(st(s+1)\{\delta(1-1/t)-(T-2)\}\).
Multiplying \(F(1/s)\) minus the lower endpoint by \((ts+q)(ts-1)\) gives \(st(s-1)\{T+2-\delta(1+1/t)\}\).
These identities verify both signs, including when \(F(1/s)\) is negative.

The disk points are distinct, so Schwarz–Pick equality requires an automorphism.
The Blaschke degree exceeds one in all degrees greater than two.
For \(z^2-(q+2)z+q\) the associate is \((z+1)(z^2-3z+1)\), giving \(T=3\), and \((\theta-1)(\theta-q)=\theta\) gives equality in the lower bound on \(\delta\).
For the infimum over all positive constants, any quadratic output has integral trace at least three.
L462v33 gives a Salem trace excess below one as well as convergence of the least excess at prescribed \(q\) to the Salem infimum.
Together with (1) this proves both directions of the infimum assertion.

### Necessity and sufficiency of the residue coordinates

For a monic solution, cancellation of the leading coefficients in \(A=f-P\) leaves the relation \(A=-z^{2m-1}A(1/z)\) in the indicated formal degree.
It gives \(A(1)=0\), and division by \(z-1\) leaves an integral symmetric polynomial in formal degree \(2m-2\).
The integral trace basis for the shifted Laurent polynomial uses \(1\) in degree zero, so it imposes no parity constraint on any of the lower coefficients of \(R\).
The constant of \(f\) is \(1-[x^h]R=q\).
Conversely every \(R\) in (4) gives a monic degree-\(2m\) solution with exactly that constant.
Partial fractions at the distinct \(x_j\) give \(R/H=1-q-\sum_j b_j/(x-x_j)\).

The reference solution corresponds to \(R_0=(1-q)H\).
Its quadratic \(p_q\) has one root in \((0,1)\) and one above \(q\), and its other factor \(V\) has simple unit roots different from \(-1\).
At \(\zeta=e^{it}\) above \(x_j\), the radial derivative in C345v2 has the sign of \(R(x_j)/H'(x_j)=-b_j\), since \(\sin(t/2),\sin t>0\) and \(\Re(e^{-it/2}p_q(\zeta))=\cos(t/2)(x_j-T)<0\).
Both conjugates enter the disk exactly for \(b_j>0\).
If \(b_j=0\), the original point is still a root at the end of the path, so it cannot be a Pisot solution.
Evaluation at \(-1\) gives
\[
 f(-1)=(-1)^m H(-2)\left(-T-2q+2\sum_j \frac{b_j}{2+x_j}\right).
\]
Here \((-1)^m H(-2)<0\) since \(h=m-1\), giving precisely the strict upper facet in (5) for either parity of \(m\).
Equality on that facet makes \(-1\) a root.

If \(f(-1)>0\), linear interpolation from \(F_0(-1)>0\) stays positive there.
At the other possible circle roots, namely those of \(V\), the path value for a positive parameter is that parameter times a nonzero displacement when all \(b_j\ne0\).
The number of exterior roots is consequently \(1+2\#\{j:b_j<0\}\) on the entire open path to \(f\).
For (5) the sole exterior root is real and positive because \(f(1)=P(1)<0\).
A monic integral factor made entirely of interior roots would have nonzero absolute constant below one, proving irreducibility.
Conversely a Pisot solution has no circle roots and \(f(-1)>0\) since its degree is even, its real roots lie above \(-1\), and the nonreal factors pair conjugately.
The exterior count therefore forces all \(b_j>0\).

I also tested both parities in the finite coefficient box \(-4\le r_i\le4\) for \(q=2,3\), using \(Q=x^2-x-3\) and \(Q=x^3-4x-1\).
For every candidate I evaluated the simplex signs using rational isolating intervals for the inner traces and compared them with a separate test requiring a nonsingular integer Schur–Cohn matrix with one negative eigenvalue and \(f(1)<0\).
Both tests gave respectively \(2,2\) solutions out of 9 for the quadratic trace, and \(1,0\) out of 81 for the cubic trace at the two constants.
These counts refer only to that box.

### Counting and optimization in the whole fiber

The linear part of the coefficient-to-residue map is the evaluation matrix scaled in row \(j\) by \(-1/H'(x_j)\).
Its absolute determinant is \(\Delta/\Delta^2=1/\Delta\), so the lattice point count divides the volume by \(1/\Delta\).
Scaling each coordinate of the standard simplex gives the volume in the claim, including its \(1/h!\).
The bounded-width neighborhood of its boundary has volume \(O_P(q^{h-1})\), which bounds the error in the covolume-weighted count for every translate.
At \(h=1\) this is the bounded endpoint error for an open interval.
In particular the leading term (2) is positive, and the finite fiber is nonempty for all large \(q\).

At the Pisot root the trace argument \(x_\theta>2\) is strictly above all the poles.
The identity \(\theta(x_\theta-T)=(\theta-1)^2-\theta(T-2)\) in the evaluated partial fractions gives (6), with each residue correction positive.
The upper part of (1) gives \(\delta\le T+2\), so \(\theta=q+O_P(1)\) uniformly in the entire fiber.
It follows that \(q/(\theta-1)\to1\) and \(q/(x_\theta-x_j)\to1\) for all fixed \(j\).
The first term in (6) alone gives the lower limit at least \(T-2\) for the minima.

The trace has degree \(m=h+1\) because its quadratic lift has degree \(2m\).
Synthetic division of \(Q\) by \(x-T\) expresses \(1,h_{h-1},\ldots,h_0\) by successive monic integral polynomials in \(T\) of degrees \(0,\ldots,h\), proving their rational independence.
Thus each nontrivial Fourier character of the coefficient translates has mean zero in the limit by a geometric sum.
Equidistribution implies infinitely many visits to the projection of the inverse image of \((0,\epsilon)^h\) under the residue map, an open nonempty set on the coefficient torus.
For each visit a choice of the integral lower coefficients realizes the small positive residues, and the last facet holds automatically when \(q\) is large.
Taking increasing \(q\) and shrinking boxes makes the contribution of the residue terms to \(q(\delta-(T-2))\) tend to zero.
The positive term from \(\theta/(\theta-1)\) tends after that subtraction and scaling to \(T-2\), giving equality in (3) for the lower limit of the minima.
The result keeps the Salem polynomial fixed throughout.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Two-point and simplex finding](#pisot-simplex-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Two-point and simplex finding](#pisot-simplex-review) | [C345v4 statement](../../claims/Yin_C_G0345_v4.md#statement) | Both finite inequalities, strictness, the global infimum, the complete fiber, lattice asymptotic and second-order lower limit. |
| [Two-point and simplex finding](#pisot-simplex-review) | [C345v4 two disk points](../../claims/Yin_C_G0345_v4.md#two-points) | Evaluation and pole cancellation, real Schwarz–Pick endpoints, exact algebraic reductions and equality examples. |
| [Two-point and simplex finding](#pisot-simplex-review) | [C345v4 simplex](../../claims/Yin_C_G0345_v4.md#simplex) | Integral affine coordinates, parity, root motions, endpoint signs, necessary and sufficient inequalities, covolume and boundary error. |
| [Two-point and simplex finding](#pisot-simplex-review) | [C345v4 second order](../../claims/Yin_C_G0345_v4.md#second-order) | Exact identity at the Pisot root, uniform finite-fiber bound, dense translates, positive residues and the optimal fixed-output lower limit. |
| [Two-point and simplex finding](#pisot-simplex-review) | [L462v32 positive return](../../ledger/Yin_L_G0462_v32.md#boyd-return) | Unique simple exterior and interior pair for the positive-constant delay-one construction. |
| [Two-point and simplex finding](#pisot-simplex-review) | [C345v2 root motion](../../claims/Yin_C_G0345_v2.md#inward) | Radial derivative for arbitrary antisymmetric displacement and the possible later circle crossings. |
| [Two-point and simplex finding](#pisot-simplex-review) | [L462v33 envelope](../../ledger/Yin_L_G0462_v33.md#least-excess) | Global limit at large constants, positive quadratic trace bound and comparison with the Salem infimum. |
| [Two-point and simplex finding](#pisot-simplex-review) | [C345v2 original optimum](../../claims/Yin_C_G0345_v2.md#optimum) | Prior fixed-output \(O_P(1/q)\) comparison sharpened by the lower limit. |
