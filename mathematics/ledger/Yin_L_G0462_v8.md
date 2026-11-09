---
author: Yin
---

# Local moment abundance and the missing integer count for paired filters

<a id="scope"></a>
## The actual supply and the question tested

The [paired supply](Yin_L_G0462_v7.md#paired-filter-supply) gives positive integral multipliers at every conductor \(p=3^m\), with a paid full resultant.
It does not give a small-moment count or a positive small-Mahler-shell probability.
This exploration asks whether actual finite-label averaging or local representation densities can supply that missing count.
It retains an elementary local calculation for the entire conductor-81 paired family and a bounded dyadic test for the fixed pair \((1,2)\).
These are exploratory deductions for separate review, not an independent review or a new Claim assessment.

The [completed three-base energy-six computation](../computations/programs/Yin_J_G0154/energy_six.md#complete-result) gives relevant feedback at exactly its recorded scope.
The original base has six classes at energy six, none with \(K=2,L=0\).
The single-filter base has one class with those moments, but its lifted polynomial has \(P(-1)=-104\).
The paired \((1,2)\) base has no nonzero integer vector at energy at most six.
Those finite computations remain separate from the local argument below.
In particular, a local solution of the two moments need not give an integer solution, a strict endpoint or a whole-measure bound.

<a id="fixed-inputs"></a>
## Matrices, labels and all five targets

Use \(p=81\), \(n=40\), and the full trace order \(\mathcal O=\mathbb Z[t]/B_{40}\).
Let \(J\) be the symmetric integer Jacobi matrix with off-diagonal entries one, diagonal entries zero except for the final entry \(-1\).
Its characteristic polynomial is
\[
 B_{40}(t)=E_{40}(t)+E_{39}(t),
\]
where \(E_0=1,E_1=t,E_{i+1}=tE_i-E_{i-1}\) are the monic second-kind Chebyshev polynomials.
The [integer moment representation](Yin_L_G0464_v10.md#moment-ellipsoid) uses the associated monic Chebyshev basis.

Fix the [balanced base](../computations/programs/Yin_J_G0154/balanced.md)
\[
 h_*=h_{0,81}U_2^6U_1^{-1}(T_3/T_{15})^2,\qquad U_a=2+T_a,
\]
whose absolute full resultant is \(32\).
For indices \(k,l\) coprime to \(81\), each identified under \(a\sim-a\), put
\[
 V_a=T_{5a}+T_{4a}-T_{2a}-T_a-1,\qquad
 u_{k,l}=q_{k,l}V_kV_l,\qquad h_{k,l}=h_*u_{k,l}.
\]
Here \(q_{k,l}\) is any integral unit making \(u_{k,l}\) positive at every grid point.
Existence and the independence of its positive square class from this choice are established by the [signed-unit interface](Yin_L_G0462_v7.md#signed-unit-rectification).
There are 27 available indices and 378 unordered pair labels with repetition, without any assertion that these are 378 different square classes.

The [signed norm calculation](../computations/programs/Yin_J_G0154/signed_filters.md#layer-norms) gives \(|\operatorname{Res}(B_{40},V_a)|=163\).
Therefore every such pair, including \(k=l\), satisfies
\[
 H=h_{k,l}(J),\qquad |\det H|=32\cdot163^2.                 \tag{1}
\]
Both \(H\) and \(JH\) are symmetric integer matrices.
For an integer coordinate vector \(v\), the two moments and the chosen energy are
\[
 K(v)=v^{\mathsf T}Hv,\qquad L(v)=v^{\mathsf T}JHv,\qquad
 E(v)=3K(v)+2L(v)=v^{\mathsf T}(3I+2J)Hv.                 \tag{2}
\]
The five prescribed targets are:

| Profile \(x\) | \(K=x^2+2\) | \(L=-4x\) | \(E=3K+2L\) |
| ---: | ---: | ---: | ---: |
| \(-2\) | 6 | 8 | 34 |
| \(-1\) | 3 | 4 | 17 |
| 0 | 2 | 0 | 6 |
| 1 | 3 | \(-4\) | 1 |
| 2 | 6 | \(-8\) | 2 |

The local calculations permit every square-root vector.
They impose neither a unit condition nor nonvanishing on every characteristic-zero conductor component.
Those additional restrictions, the strict endpoint and the complete Mahler measure remain separate.

<a id="odd-prime-pencils"></a>
## Every odd-prime pencil has high rank

For \(0\le i<40\), the vector \(J^ie_1\) is supported on the first \(i+1\) coordinates and has coefficient one in coordinate \(i+1\).
Consequently \(e_1,Je_1,\ldots,J^{39}e_1\) is a basis over every field.
Thus \(J\) is cyclic over every field.
For any scalar \(\lambda\), its \(\lambda\)-eigenspace has dimension at most one.
Equivalently,
\[
 \operatorname{rank}(aI+bJ)\ge39
       \quad\hbox{whenever }(a,b)\ne(0,0).                 \tag{3}
\]
This includes repeated roots of the characteristic polynomial; separability is not needed.

Let \(q\) be an odd prime.
By (1), \(H\bmod q\) is invertible unless \(q=163\).
At \(163\), its nullity is at most two.
Indeed, in the integer Smith normal form, each invariant factor divisible by \(163\) contributes at least one to the valuation two of the determinant.
The rank inequality for a product and (3) now give
\[
 \operatorname{rank}_{\mathbb F_q}((aI+bJ)H)\ge37
       \quad\hbox{for every }(a,b)\ne(0,0).                \tag{4}
\]
For \(q\ne163\) the stronger lower bound 39 holds, but (4) suffices uniformly.

<a id="odd-prime-count"></a>
## Every joint target has a nonsingular odd-prime solution

For arbitrary \(K,L\in\mathbb F_q\), define
\[
 N_q(K,L)=
 \#\{v\in\mathbb F_q^{40}:
          v^{\mathsf T}Hv=K,\ v^{\mathsf T}JHv=L\}.
\]
Take a nontrivial additive character \(\psi\) of \(\mathbb F_q\).
Fourier inversion gives
\[
 N_q(K,L)=q^{-2}\sum_{a,b\in\mathbb F_q}\psi(-aK-bL)
       \sum_{v\in\mathbb F_q^{40}}
          \psi\!\left(v^{\mathsf T}(aI+bJ)Hv\right).       \tag{5}
\]
For a symmetric matrix of rank \(r\) in odd characteristic, diagonalization separates \(40-r\) zero variables and \(r\) nonzero one-variable quadratic sums.
Each nonzero one-variable sum has absolute value \(q^{1/2}\).
For completeness, its squared absolute value is
\[
 \sum_{x,y\in\mathbb F_q}\psi(c(x^2-y^2))
 =\sum_{u,w\in\mathbb F_q}\psi(cuw)=q,\qquad c\ne0,
\]
using the invertible substitution \(u=x-y,w=x+y\).
Hence the absolute value of the inner sum in (5) is \(q^{40-r/2}\).
The zero pencil contributes \(q^{38}\), and (4) bounds all the other terms, so
\[
             |N_q(K,L)-q^{38}|<q^{43/2}.                  \tag{6}
\]

The Jacobian of the two moment polynomials has rows \(2(Hv)^{\mathsf T}\) and \(2(JHv)^{\mathsf T}\).
It has rank less than two exactly when \(y=Hv\) and \(Jy\) are linearly dependent.
Such a \(y\) is either zero or belongs to an eigenspace of \(J\) over \(\mathbb F_q\).
There are at most 40 eigenvalues, with at most \(q-1\) nonzero vectors in each eigenspace by cyclicity.
Each \(y\) has at most \(q^2\) preimages under \(H\).
Thus the number of singular vectors, whether or not they satisfy the targets, is at most
\[
                       q^2(1+40(q-1)).                   \tag{7}
\]
For every \(q\ge3\), the lower bound for \(N_q\) from (6) exceeds (7).
One explicit comparison is
\[
 q^{-38}\bigl(q^{38}-q^{43/2}-q^2(1+40(q-1))\bigr)
 >1-q^{-33/2}-40q^{-35}>0.                                 \tag{8}
\]
The last two subtracted terms sum to less than one already at \(q=3\) and decrease thereafter.

Every joint target therefore has a nonsingular solution modulo every odd prime.
This conclusion holds for all 378 conductor-81 pair labels and for arbitrary targets, not only the five rows of the table.
No enumeration of pair labels or finite-field vectors was used.

To see the lift explicitly, suppose \(v_s\) solves the two targets modulo \(q^s\) and has Jacobian rank two modulo \(q\).
For \(v_{s+1}=v_s+q^sw\), the two errors modulo \(q^{s+1}\) are corrected by the surjective linear map
\[
 w\longmapsto
 2\bigl((Hv_s)^{\mathsf T}w,(JHv_s)^{\mathsf T}w\bigr)
       \pmod q.
\]
There are exactly \(q^{38}\) corrections for each required pair of error digits.
This constructs compatible solutions in \(\mathbb Z_q^{40}\).
If \(N_{q^s}\) counts all solutions of the two congruences, it also gives
\[
 \liminf_{s\to\infty}q^{-38s}N_{q^s}
 \ge1-q^{-33/2}-40q^{-35}>0.                               \tag{9}
\]
Equation (9) is a positive local density lower bound; no local-to-global inference is made.
The normalization counts representations per expected dimension 38, not probability under the ambient Haar measure on \(\mathbb Z_q^{40}\).
The exact first quadratic equation already defines a Haar-null set, since a nonzero polynomial has a zero set of measure zero by induction on variables, the finite number of roots in one variable and Fubini's theorem.
Thus positive normalized local density is not positive ambient probability for the exact equations, and supplies no positive probability for the original integer Mahler event.

<a id="dyadic-threshold"></a>
## A mod-eight count suffices above an explicit threshold

For the same \(H\), (1) gives \(v_2(\det H)=5\), so
\[
                   \dim_{\mathbb F_2}\ker H\le5.           \tag{10}
\]
Also \(J\bmod2\) is invertible: \(B_{40}(0)=1\).
For \(y\ne0\) over \(\mathbb F_2\), dependence of \(y,Jy\) therefore forces \(Jy=y\).
The eigenspace for eigenvalue one has dimension at most one by cyclicity.
There are consequently at most two possible \(y\), including zero, with this dependence.
Each has at most \(2^5\) preimages under \(H\), so there are at most \(2^6\) bad parity vectors \(v\bmod2\).

Each parity vector has \(4^{40}\) lifts modulo eight.
Therefore at most
\[
                              2^{86}                       \tag{11}
\]
vectors modulo eight have \(Hv,JHv\bmod2\) dependent.
For any fixed integer targets, let
\[
 N_8(K,L)=
 \#\{v\in(\mathbb Z/8\mathbb Z)^{40}:
          v^{\mathsf T}Hv=K,\ v^{\mathsf T}JHv=L\bmod8\}.
\]
If
\[
                              N_8(K,L)>2^{86},             \tag{12}
\]
at least one solution has \(Hv,JHv\bmod2\) independent.

This condition uses the Jacobian divided by two, not the ordinary Jacobian modulo two, which is always zero.
Starting from such a solution modulo \(2^3\), suppose \(v_s\) solves the two targets modulo \(2^s\), \(s\ge3\).
Put \(v_{s+1}=v_s+2^{s-1}w\).
For either symmetric matrix \(A=H\) or \(A=JH\),
\[
 v_{s+1}^{\mathsf T}Av_{s+1}
 =v_s^{\mathsf T}Av_s+2^s(Av_s)^{\mathsf T}w
        +2^{2s-2}w^{\mathsf T}Aw.                          \tag{13}
\]
The final term vanishes modulo \(2^{s+1}\).
The independence modulo two lets the two linear terms correct the two required error digits.
This step preserves the two quadratic values modulo \(2^s\), while it only guarantees that the vector itself is preserved modulo \(2^{s-1}\).
In particular, it need not preserve the original vector class modulo eight at the first step.
The new vector remains congruent to the old vector modulo four, so the independence persists.
The vectors converge 2-adically because their successive differences are divisible by \(2^{s-1}\), and their limit solves both exact targets in \(\mathbb Z_2\).
Thus (12) is a sufficient dyadic solvability criterion.
It is not a necessary condition and is not an integer existence criterion.

<a id="fixed-dyadic-test"></a>
## The fixed dyadic test uses only pair \((1,2)\)

The selected test fixes the conductor-81 input returned by signed_filters.construct([1, 2]), whose [input certificate](../computations/programs/Yin_J_G0154/paired_control.md#input-certificate) specifies the rectifier, full resultant and matrices.
Use precisely its \(H\) and \(JH\), or an exactly verified simultaneous integral unimodular congruence of those two forms.
Compute \(N_8(K,L)\) for the five target rows above.
No other pair, conductor, unit descent or energy enumeration is part of this test.

Let \(\zeta_8=\exp(2\pi i/8)\).
For \(a,b\in\{0,\ldots,7\}\), compute the 64 complete quadratic sums
\[
 S_8(a,b)=
 \sum_{v\in(\mathbb Z/8\mathbb Z)^{40}}
       \zeta_8^{\,v^{\mathsf T}(aH+bJH)v}.
\]
Then
\[
 N_8(K,L)=\frac1{64}\sum_{a,b\bmod8}
                 \zeta_8^{-aK-bL}S_8(a,b).                \tag{14}
\]
One set of 64 sums supplies all five counts.
All operations can be exact in \(\mathbb Z[\zeta_8]\), with the final counts checked to be nonnegative integers.
A quadratic-block elimination implementation must preserve the full sums, including degenerate blocks and all powers-of-two factors.
This definition does not require enumerating \(8^{40}\) vectors.

The mathematical stopping outcomes are explicit:

- If \(N_8=0\), the specified target has no dyadic solution.
- If \(N_8>2^{86}\), (13) proves dyadic solvability and the odd-prime result proves solvability at every finite prime.
- If \(0<N_8\le2^{86}\), the count alone leaves lifting unresolved.
  A further singular-lifting analysis would be a separate test, not an inference of impossibility.

The present exploration records the contract, not an execution or result of (14).
In particular, no entry of the five-target count table is asserted here.
The separate native record owns the [exact joint counts](../computations/programs/Yin_J_G0154/dyadic_support.md#joint-counts), their [dyadic lifting application](../computations/programs/Yin_J_G0154/dyadic_support.md#lifting), and the [real feasibility and global integer boundary](../computations/programs/Yin_J_G0154/dyadic_support.md#real-and-global-boundary).
Combined with the existing paired \(E\le6\) integer exclusion, a successful dyadic certificate for the targets at energies one, two or six would demonstrate a gap between local solvability and global integer representation in this actual input.
It would not make its empty low-energy integer shell nonempty.
The targets at energies 17 and 34 are not excluded by that finite computation.

<a id="actual-label-average"></a>
## Actual label averages have a discrete scale

At general \(p=3^m\), there are \(a_p=\varphi(p)/2=3^{m-1}\) possible Galois indices modulo sign.
The unordered \(d\)-filter labels with repetition number
\[
                    A_{p,d}=\binom{a_p+d-1}{d}=O(n^d)
\]
for each fixed \(d\), where \(n=(p-1)/2\).
The [norm budget](Yin_L_G0462_v7.md#paired-filter-supply) permits the retained even-filter candidates \(d=2,4\); it does not establish small moments.
Using every label counts multiplicities when several labels define the same square class.

Let \(J_p\) be the analogous \(n\)-dimensional Jacobi matrix, choose the retained slow-cut base \(h_0\), and put \(H_\lambda=(h_0u_\lambda)(J_p)\) for the positive rectified filter of each label.
For each label \(\lambda\), let \(X_\lambda\) be the cardinality of any specified subset of integer square-root vectors satisfying one of the five joint moment targets.
The subset may additionally require nonvanishing, the strict endpoint and \(1<M(P)<1+\varepsilon\).
The count is finite: for a separator \(c\) in the fixed sign gap, each target lies in the positive definite solid ellipsoid
\[
 v^{\mathsf T}G_{\lambda,c}v\le S_0,\qquad
 G_{\lambda,c}=(J_p-cI)H_\lambda,\qquad S_0=L-cK.
\]
Nonpositive \(S_0\) has no nonzero solution.
For the angular midpoint, the [complete ellipsoid bound](Yin_L_G0464_v10.md#moment-ellipsoid) gives \(S_0\le20\), \(|B(c)|\ge1\), and
\[
 \operatorname{vol}\{y:y^{\mathsf T}G_{\lambda,c}y\le S_0\}
       \le(40\pi e/n)^{n/2}.                               \tag{15}
\]
The determinant estimate only uses the nonzero integer full resultant, which remains at least one after the positive integral filter.
Summing (15) over polynomially many labels and the five targets gives
\[
 5A_{p,d}(40\pi e/n)^{n/2}
       =\exp\!\left(-\tfrac12n\log n+O(n)\right)\longrightarrow0. \tag{16}
\]

Under the actual uniform label law,
\[
                \mathbb E X_\lambda\in A_{p,d}^{-1}
                                      \mathbb Z_{\ge0}.    \tag{17}
\]
Thus a positive mean is at least \(1/A_{p,d}\).
A positive continuous average much smaller than this cannot simply be assigned to the actual mean.
More precisely, suppose a positive volume proxy \(W_p\) is bounded above by \(5(40\pi e/n)^{n/2}\).
There cannot be fixed constants \(c_1,c_2>0\) such that \(c_1W_p\le\mathbb E X_\lambda\le c_2W_p\) for all sufficiently large conductors.
The lower bound would make the mean positive, while \(A_{p,d}c_2W_p\to0\) and the upper bound would eventually put it strictly below \(1/A_{p,d}\), contradicting (17).
This rejects that two-sided volume-comparability ansatz; it does not determine whether the actual count is zero or has exceptional positive spikes.
Equations (15)--(17) do not prove emptiness.
The [existing volume obstruction](Yin_L_G0449_v1.md#uniform-volume-and-lattice-obstruction) explicitly permits integer points in sets of shrinking volume, and the [local mass comparison](Yin_L_G0449_v2.md#thin-shell-stratum-comparison) does not repair that transfer.

For a nonnegative count on the finite label space, the elementary second-moment inequality would give
\[
 \Pr(X_\lambda>0)\ge
          \frac{(\mathbb E X_\lambda)^2}{\mathbb E X_\lambda^2}
\]
once an actual positive first moment is established.
No such lower bound is supplied by the volume, the norm ceiling or the local calculation above.
Moreover, changing a rectifier by a positive unit square induces an integral unimodular change of every square-root vector, preserving both moments and the reconstructed \(h\).
It therefore does not randomize the complete count within a fixed positive-unit orbit.

<a id="genus-transfer-gap"></a>
## A genus average would still need a realization map

A possible theta comparison could average representation counts over a genus of positive definite integral quadratic lattices, meaning lattices locally isometric over \(\mathbb R\) and every \(\mathbb Z_q\).
Even if a positive weighted average over such a genus were supplied, it would only force representation in some member of that genus.
It would not identify that member with one of the actual paired inputs.
The obstruction is not resolved by changing the weights or observing positive local densities.

The actual input carries both \(H\) and the integral self-adjoint endomorphism \(J\), with its specified characteristic polynomial and trace-order action.
A scalar energy theta series forgets the second moment and this marked action.
A successful transfer would have to preserve or recover that integral structure, identify the relevant lattices with allowed principal-element square families, and retain the prescribed joint target.
No coverage, positive-fraction realization or bound on the contribution of omitted lattice classes is established.
This is a conditional comparison of averaging domains; no external genus-average identity or prime-element counting theorem is used as support for the local proof or for integer existence.

<a id="probability-boundary"></a>
## What a positive local count would leave unresolved

The [light-tail and full-support analysis](Yin_L_G0464_v9.md#positive-support) already separates positive mass on actual integer inputs from a continuous favorable region.
The present paired family changes the supplied square classes, but neither a finite-prime solution nor a positive genus mean establishes a positive integer count in those classes.
After an integer joint-moment hit, nonvanishing on the original grid, the strict endpoint and the full Mahler measure still have to be checked.
The completed single-filter energy-six hit shows concretely that the endpoint can fail after the moments and unit condition succeed.

The useful next distinction is now narrow.
All odd-prime joint obstructions have been removed analytically for the conductor-81 paired family.
The fixed mod-eight test decides a sufficient dyadic condition for pair \((1,2)\) without a new large real ellipsoid traversal.
If it succeeds, future positive-count work must address the actual global integer representation and the subsequent endpoint and whole-measure conditions.
No arbitrary-radius strictly positive Mahler-shell probability is proved.
