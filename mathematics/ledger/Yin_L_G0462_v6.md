---
author: Yin
---

# Integer residuals, exact factor diagnostics and Galois-permuted nonunit filters

<a id="scope"></a>
## The bounded strategic question

The [unrestricted Task](../tasks/Yin_T_G0001_v1.md#contract) still requires a uniform positive whole-measure gap or actual integer polynomials with arbitrarily small strictly positive logarithmic Mahler measure.
For a discrete sampling law, the counterexample direction can instead be established by proving positive probability for every strict shell \(1<M(P)<1+\varepsilon\).
The previous [topological and rotating-shear exploration](Yin_L_G0462_v5.md#scope) retains those constructions, their probability laws and their actual limitations.
This continuation asks for an arithmetic supply of inputs beyond a fixed unit orbit, with the entire resultant and Mahler costs accounted for.

The moving linear-cut square proposal below has a complete obstruction in the separately retained [C880v3](../claims/Yin_C_G0880_v3.md#statement), whose own assessment governs use.
The Galois-filter proposal below specifies the arithmetic law; [J154](../computations/programs/Yin_J_G0154/readme.md) owns its subsequent finite execution and exact results.
No new near-one polynomial, positive small-shell count or asymptotic sequence was found in this bounded exploration.

<a id="integer-residual"></a>
## An exact integer residual interface and its local failure

Let \(J\) be the symmetric integral tridiagonal matrix with off-diagonal entries one and diagonal entries zero except for the last entry \(-1\).
Its characteristic polynomial is the full odd-grid polynomial \(B_n\), and the Chebyshev coefficient basis identifies multiplication by \(t\) with \(J\), as in the [moment ellipsoid](Yin_L_G0464_v10.md#moment-ellipsoid).
Write \(T=J+2I\).
For the candidate
\[
             h(t)=(r(t+2)-1)v(t)^2,\qquad r\ge2,
\]
represent \(v\bmod B_n\) by its integer coefficient vector \(\mathbf v\) in that basis and put
\[
                         \mathbf w=(rT-I)\mathbf v.
\]
If \(K=\sum_j r_j\) and \(L=\sum_j b_jr_j\) are the first two residue moments, exact quadrature gives
\[
 K=\mathbf v^{\mathsf T}\mathbf w,\qquad
 L+2K=\mathbf v^{\mathsf T}T\mathbf w,\qquad
 \|\mathbf w\|^2=r(L+2K)-K.
 \tag{1}
\]
Conversely, \(\mathbf w=(rT-I)\mathbf v\), the prescribed \(K=\mathbf v^{\mathsf T}\mathbf w\), and the last identity recover the prescribed second moment.
For the surviving profile \(x=-1\), the necessary targets \(K=3,L=4\) become
\[
                    \mathbf v^{\mathsf T}\mathbf w=3,\qquad
                    \|\mathbf w\|^2=10r-3.
 \tag{2}
\]
This gives a short integer residual sphere with the explicit image-lattice condition \(\mathbf w\in(rT-I)\mathbb Z^n\), not a proof that the sphere has a suitable point.

The determinant of \(T\) is one.
Conjugating by alternating diagonal signs turns it into the path matrix with diagonal \(2,\ldots,2,1\) and off-diagonal \(-1\).
The inverse of that conjugated matrix has entries \(\min(i,j)\), with \(1\le i,j\le n\).
Thus \(T^{-1}\) is integral and is obtained by undoing those alternating signs.
For the integer vector \(\mathbf u=T\mathbf v\), (2) is equivalently
\[
 r\|\mathbf u\|^2-\mathbf u^{\mathsf T}T^{-1}\mathbf u=10,\qquad
 \mathbf u^{\mathsf T}T^{-2}\mathbf u
          -r\mathbf u^{\mathsf T}T^{-1}\mathbf u=-3,
 \qquad
 \mathbf w=r\mathbf u-T^{-1}\mathbf u.
 \tag{3}
\]
The equivalence is exact over the integer lattice.

A compactly supported local construction already fails.
If the first and last entries of \(\mathbf v\) vanish, write its coefficient list as a nonzero integer polynomial \(V(z)\).
Zero-padding the tridiagonal product gives the Laurent polynomial
\[
                  W(z)=[r(z+z^{-1})+2r-1]V(z)
\]
without discarded boundary coefficients, and its coefficient-square sum is exactly \(\|\mathbf w\|^2\).
The quadratic \(rz^2+(2r-1)z+r\) has both roots on the unit circle and Mahler measure \(r\).
Jensen's inequality and Parseval therefore give
\[
                   \|\mathbf w\|^2\ge M(W)^2
                             =r^2M(V)^2\ge r^2.
\]
For (2), this is impossible for \(r\ge10\).
This local argument leaves boundary-supported vectors open.

The full-family [norm obstruction](../claims/Yin_C_G0880_v3.md#norm-bound) then closes that boundary escape as well.
The integer linear factor alone contributes a norm root asymptotically at least \(r\), while multiplying by a nonzero integer square cannot lower its norm.
Consequently this family has no shrinking positive whole-measure sequence.
The obstruction is caused by the forced integer linear divisor, not by the square representation itself.
The same norm calculation would also apply to an arbitrary integer cofactor positive on the entire grid; that extension is an observation about the argument, not a change to the fixed C880v3 statement.
No further residual scan in this linear-factor family is warranted.

<a id="factor-feedback"></a>
## What the exact factor diagnostics change

The additional [J153 factor diagnostics](../computations/programs/Yin_J_G0153/readme.md#factor-diagnostics) recomputed the same 72 labelled matrices and exact characteristic polynomials before rational factorization.
Within its 48 positive outputs, eight have a nonreciprocal noncyclotomic factor and 40 have only reciprocal noncyclotomic factors.
The minimum is exactly the square of the plastic constant.
Its full factorization and the proof of that equality belong to J153.

That special factorization does not explain every positive output.
J153 also identifies single irreducible reciprocal cores of degrees \(20,44,44,92\) at the explicit labels \((12,2,2),(24,2,0),(24,2,7),(48,2,1)\).
Hence a uniform exclusion by decomposition into nonreciprocal factors is already false for this ensemble.
The low-rank perturbation of a long rotation can still have a large irreducible reciprocal component.
Neither small perturbation rank nor small house controls its complete exterior-root cost.

A next structural analysis of that model must keep the number of active sites growing.
A fixed number of local defects can lead to a bounded-support specialization, and the [fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) must be checked for any such proposed reduction.
The present evidence gives no reason to enlarge the random sample window before obtaining an exact mechanism that controls all expanding roots.

<a id="galois-filter-law"></a>
## A nonunit integer supply with an explicit norm budget

For the next arithmetic test take \(p=3^m\), \(m\ge3\).
Set \(s=2\) when \(m=3\), and \(s=\lceil\log_3m\rceil\) when \(m\ge4\), and let the negative terminal block have length
\[
                           \ell_p=3^{m-s}.
\]
These choices satisfy \(1<s<m\).
Use the exact representative \(h_{0,p}\) from the [integral sign construction](Yin_L_G0464_v8.md#integral-sign-representative) with this cut and its prescribed construction, without an additional unit multiplier.
The [terminal-block norm formula](Yin_L_G0464_v8.md#small-norm-terminal-block) gives
\[
 \Delta_{0,p}=|\operatorname{Res}(B,h_{0,p})|
       =2^{\,2\cdot3^{s-1}-1},\qquad
                 \Delta_{0,p}^{1/n}\longrightarrow1.
 \tag{4}
\]
Here \(\ell_p/p\to0\) and \(\log\ell_p/\log p\to1\).
The initial test uses exactly
\[
 (p,m,s,\ell_p)=(27,3,2,3),(81,4,2,9),(243,5,2,27),(729,6,2,81).
\]
All four initial representatives have \(\Delta_{0,p}=32\).
These cuts differ from the earlier floor-\(p/\log p\) windows.

Let
\[
 F(z)=z^{10}+z^9-z^7-z^6-z^5-z^4-z^3+z+1,\qquad \mu=M(F).
\]
Its [retained irreducible Salem classification](../claims/Yin_C_G0226_v1.md#lehmer-joint-prime-control) supplies the absence of torsion roots and the unique positive expanding root \(\mu\).
For \(j\ge0\), define \(T_j\) by \(T_j(z+z^{-1})=z^j+z^{-j}\).
For every \(k\) coprime to \(p\), put
\[
 V_k(t)=T_{5k}(t)+T_{4k}(t)-T_{2k}(t)-T_k(t)-1,\qquad
                    z^{-5k}F(z^k)=V_k(z+z^{-1}).
 \tag{5}
\]
These are actual integer polynomials; their remainders modulo \(B\) may be used without changing their grid values.
No \(V_k\) vanishes at any grid point.

Let \(G_p=(\mathbb Z/p\mathbb Z)^\times/\{\pm1\}\), with each class represented by an integer \(1\le k\le(p-1)/2\).
One-filter inputs use
\[
             h=h_{0,p}V_k^2,\qquad k\in G_p.
\]
Two-filter inputs use
\[
             h=h_{0,p}(V_kV_l)^2,\qquad (k,l)\in G_p^2.
 \tag{6}
\]
Repeated indices and repeated output polynomials are allowed.
All grid signs agree exactly with \(h_{0,p}\).
The filters are unrestricted integer elements rather than units of the trace order.

Multiplication by any such \(k\) permutes the full odd grid, including all imprimitive nodes.
Thus
\[
 N_p=|\operatorname{Res}(B,V_1)|
       =|\operatorname{Res}(B,V_k)|\in\mathbb Z_{>0},
 \qquad
 N_p^2=|\operatorname{Res}(F,z^p-1)|,
 \tag{7}
\]
where the second equality uses reciprocal pairing and \(|F(1)|=1\).
For \(d\) filters, with multiplicities included, the exact whole resultant is
\[
                   \Delta_{p,d}=\Delta_{0,p}N_p^{2d}.
 \tag{8}
\]
Applying the already inspected [Dim16 logarithmic-form interface](../audits/literature/Dim16/Yin_U001.md#dim16-reported-bound) to the fixed nontorsion roots of \(F\) on the circle, while treating its two off-circle roots directly, gives
\[
 \log|\operatorname{Res}(F,z^p-1)|=p\log\mu+O(\log p).
\]
Every fixed root has Weil height \(\log\mu/10<1\), so this uses precisely the existing bounded-height scope.
Equations (4), (7) and (8) give
\[
             N_p^{1/n}\longrightarrow\mu,\qquad
             \Delta_{p,d}^{1/n}\longrightarrow\mu^{2d}.
 \tag{9}
\]

The norm budget genuinely permits one and two such filters.
Indeed
\[
 F(19/16)=\frac{330753263801}{1099511627776}>0,\qquad F(1)=-1
\]
and the unique expanding root give \(\mu<19/16\).
Consequently
\[
                  \mu^4<\frac{130321}{65536}
                            <2\exp(-2^{-22}).
\]
This is below the necessary [shrinking-shell ceiling](Yin_L_G0464_v6.md#norm-ceiling).
It is not a sufficient condition for a small Mahler measure of the output.
There is also a precise limit to adding more filters:
\[
 F(7/6)=-\frac{13481789}{60466176}<0,\qquad
           \mu>7/6,\qquad \mu^6>(7/6)^6>2.
\]
Thus any fixed \(d\ge3\) in the same construction is excluded from a shrinking sequence by that ceiling.
More generally an unbounded filter count is also excluded by (7)--(9) for large \(p\).
The one- and two-filter experiment cannot be extended by adding arbitrarily many copies of this same seed at no cost.

<a id="exact-support-test"></a>
## The next discriminating test and probability accounting

For each stated \(p\), each one-filter index or ordered two-filter pair, and each \(x\in\{-2,-1,0,1,2\}\), form
\[
 C=\operatorname{rem}_B(B_{n-1}h),\quad
 Q=(t-2x)B+C,\quad P=z^{n+1}Q(z+z^{-1}).
\]
This supplies genuine monic reciprocal integer polynomials before any moment or root test.
For a fixed \(p\) and filter count \(d=1,2\), choose uniformly from \(G_p^d\times\{-2,-1,0,1,2\}\).
Every labelled outcome has mass \(1/(5|G_p|^d)>0\).
A countable mixture assigning positive mass to every selected \(p\) and both filter counts preserves every such atom.

The intended shell event includes the strict endpoint \(Q(-2)/B(-2)<0\) and \(1<M(P)<1+\varepsilon\).
The sign conditions are already automatic.
An eventual shrinking sequence in this chamber must satisfy the exact first two moment targets
\[
                     K=x^2+2,\qquad L=-4x.
 \tag{10}
\]
The first bounded test is the complete joint support and multiplicity table of \((K,L)\) over the prescribed one- and two-filter indices, not a random subsample or a larger conductor exclusion table.
The native J154 traversal uses unordered two-filter pairs; its reported histogram has unordered multiplicities, while the ordered probability law here assigns multiplicity two to an off-diagonal pair and one to a diagonal pair.
Both conventions have the same support and the same zero-hit event.
For a symmetric cyclic Laurent representative \(H(z)=\sum_{j\bmod p}H_jz^j\) of \(h(z+z^{-1})\), exact grid summation gives
\[
                          K=H_0-H_2,\qquad L=H_1-H_3.
\]
Hence the test can use exact integer cyclic convolutions and requires no approximate evaluation at algebraic nodes.
The Galois action expresses the same functions as correlations on the finite multiplicative group, which may expose structural congruences or a count formula.
The number of labelled moment hits is the missing arithmetic output; the norm calculation above supplies no lower bound for it.

Immediately test each actual moment hit against the exact endpoint condition and certify its complete Mahler measure.
The chamber interlacing identifies all but the two exceptional trace roots as real and inside \((-2,2)\), but the remaining roots still need full certified treatment.
A valid shrinking mechanism must explain why those complete positive costs approach zero across changing \(p\).
A finite moment hit, a cyclotomic output or a decrease of the house alone supplies no such explanation.

If a certified strict-shell hit is found, its atom gives an explicit positive probability at that particular shell.
For every \(\varepsilon>0\), positive probability still requires a hit at a suitable conductor with a correspondingly small complete cost.
Neither equidistribution of Galois indices nor a large number of labelled inputs proves this rare-event existence.

If the exact joint support misses all five targets throughout the four declared conductors, stop enlarging this one- and two-filter window until a structural reason predicts a new target.
That finite absence would reject the present initial allocation, not prove a uniform impossibility for the model.
If moment hits occur but all fail the endpoint or retain a positive full cost, analyze their exact common structure before extending the range.
A positive count with a scalable full-cost bound would justify expansion; a further finite necessary sieve by itself would not.
