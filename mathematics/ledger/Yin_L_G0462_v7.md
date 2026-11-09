---
author: Yin
---

# Positive nonsquare multipliers from signed-unit rectification

<a id="scope"></a>
## Why changing the integer square class is the next question

The [previous filter proposal](Yin_L_G0462_v6.md#galois-filter-law) used positive square multipliers with a paid resultant budget.
Its [finite Galois tests](../computations/programs/Yin_J_G0154/readme.md#finite-results), [balanced controls](../computations/programs/Yin_J_G0154/balanced.md), and [radius-two unit window](../computations/programs/Yin_J_G0154/unit_ball.md#results) found no joint moment hit on their stated scopes.
The [complete energy-one and energy-two enumeration](../computations/programs/Yin_J_G0154/two_energy_shell.md#scope) now excludes those energies for every integer square multiplier of the specified conductor-81 base \(h_*\).
The energy-six traversal remains incomplete.

A different positive-unit multiple of that base cannot evade the complete two-energy conclusion.
The [square-class calculation](Yin_L_G0464_v10.md#positive-squares) proves that every totally positive unit of the full trace order is an integer unit square.
The associated Gram matrices change by integral unimodular congruence.
A new relevant input must leave that integer square-multiple domain, or address a still-unresolved target within it.

The comparison below examines additive positive multipliers, a conductor-layer patch, and sign rectification of unsquared nonunits.
The third operation supplies explicit new square classes at a smaller norm cost than the earlier separately squared filters.
It supplies no small-moment theorem, near-one polynomial or arbitrary-radius positive-probability estimate.

<a id="sum-of-squares-cost"></a>
## Adding two full-support squares costs at least two

Let \(B\) be the full odd-grid polynomial of degree \(n\), and let \(a,b\in\mathbb Z[t]\) be nonzero at every grid point.
Then
\[
 |\operatorname{Res}(B,a^2+b^2)|^{1/n}
 \ge|\operatorname{Res}(B,a)|^{2/n}+|\operatorname{Res}(B,b)|^{2/n}
 \ge2.                                                        \tag{1}
\]
For the first inequality, put \(A_j=a(b_j)^2>0\), \(B_j=b(b_j)^2>0\), and let \(A,B\) denote their respective geometric means.
Weighted arithmetic-geometric mean with weights \(A/(A+B)\) and \(B/(A+B)\) gives
\[
 \frac{A_j+B_j}{A+B}
 \ge(A_j/A)^{A/(A+B)}(B_j/B)^{B/(A+B)}.
\]
Multiplication over \(j\) proves (1).
The last inequality uses the nonzero integer resultants.

Thus \(h=h_0(a^2+b^2)\), with both summands nonzero throughout the grid, forces the full resultant root to be at least two, since \(|\operatorname{Res}(B,h_0)|\ge1\).
The [strict shrinking-shell ceiling](Yin_L_G0464_v6.md#norm-ceiling) excludes a growing-conductor near-one sequence of such inputs in the strict chamber.
This does not cover arbitrary sums having zero components.
On an irreducible conductor layer, a summand either vanishes identically or is nonzero at every conjugate node.
The same argument applies separately to the active summands on that layer.
Using zero divisors to avoid the full-grid bound leaves the integral gluing cost unresolved.

<a id="layer-patch-cost"></a>
## An automatic positive patch on the top layer also has a large cost

Write \(p=3^m\), \(q=3^{m-1}\), \(n=(p-1)/2\), and \(n_0=(q-1)/2\).
Let \(B_0\) be the full odd-grid polynomial for \(q\), and let
\[
                        F_m=1+T_q,\qquad B=B_0F_m.
\]
The integral multiplier
\[
                              u=1+B_0^2v^2                     \tag{2}
\]
equals one on every lower layer and is strictly positive on the top layer.
Suppose \(v\) is nonzero modulo \(F_m\).
At each lower-layer node \(b\), one has \(T_q(b)=2\), hence \(F_m(b)=3\).
Therefore
\[
 |\operatorname{Res}(F_m,B_0)|=3^{n_0},\qquad
 \operatorname{Norm}(u)
 \ge|\operatorname{Res}(F_m,B_0v)|^2
 \ge3^{2n_0}.                                                  \tag{3}
\]
The last step uses the nonzero integer top-layer norm of \(v\).
Consequently
\[
                   \liminf\operatorname{Norm}(u)^{1/n}
                                   \ge3^{2/3}>2.
\]
An integral nonvanishing base cannot reduce this norm cost.
If \(v\) vanishes modulo \(F_m\), (2) is instead the identity at every node and effects no change.

This rejects the nontrivial automatically positive square patch (2).
It does not reject arbitrary integral Chinese-remainder constructions, patches supported on different layers, or unsquared signed patches subsequently corrected by a unit.
The calculation identifies the cost of this particular gluing factor.

<a id="signed-unit-rectification"></a>
## Rectifying the signs of an unsquared filter

Take the full order \(\mathcal O_p=\mathbb Z[t]/B_{(p-1)/2}\), with \(p=3^m\).
The [unit-signature calculation](Yin_L_G0464_v10.md#positive-squares) says that a sign vector is realized by a unit exactly when its negative-sign parities agree on all \(m\) primitive conductor layers.
For an integer element \(W\) nonzero on the grid, a unit \(q\) satisfying
\[
                            q(b_j)W(b_j)>0\quad\hbox{for all }j \tag{4}
\]
therefore exists exactly when all signed layer norms of \(W\) have the same sign.
The unit has the same sign vector as \(W\), and changes no absolute layer norm.

Any two units rectifying the same \(W\) have a totally positive quotient.
That quotient is an integer unit square.
Thus the square class of the positive multiplier is independent of the rectifier.
A different rectifier can improve magnitudes without changing this square class.
The distinction concerns square classes and principal ideals in the order; no change in an ideal class group is asserted.

Use the fixed Lehmer polynomial and trace form
\[
 \begin{split}
 F(z)&=z^{10}+z^9-z^7-z^6-z^5-z^4-z^3+z+1,\\
 V(t)&=t^5+t^4-5t^3-5t^2+4t+3,\qquad z^{-5}F(z)=V(z+z^{-1}).
 \end{split}
\]
The [retained Salem classification](../claims/Yin_C_G0226_v1.md#lehmer-joint-prime-control) makes \(V\) nonzero at every torsion trace.
For \(k\) coprime to \(p\), put \(V_k=T_{5k}+T_{4k}-T_{2k}-T_k-1\).
Multiplication by \(k\) permutes each conductor layer, so every \(V_k\) has the same signed layer norms
\[
                          A_i=\operatorname{Res}(1+T_{3^{i-1}},V).
\]
The [exact native calculation](../computations/programs/Yin_J_G0154/signed_filters.md#layer-norms) gives
\[
 A_1=A_2=A_3=-1,\quad A_4=-163,\quad A_5=-19100773,\quad
 A_6=13900324327287389.                                        \tag{5}
\]
Layers seven and eight have negative and positive signs, respectively.
The complete exact integers, degree-five recurrence and unreduced low-layer checks belong to the native evidence.

The first five layers admit single-filter rectification.
In particular \(p=81\) and \(243\) permit positive multipliers \(q_kV_k\) without squaring the filter.
For every \(m\ge6\), the conflicting first and sixth layer signs make single-filter unit rectification impossible for this fixed seed, regardless of later layers.
This is an exact obstruction, not failure of a numerical sign search.

<a id="paired-filter-supply"></a>
## Pairing filters removes the layer-parity obstruction

For any \(k,l\) coprime to \(p\), the product \(W=V_kV_l\) has signed norm \(A_i^2>0\) on every layer.
All layer parities are even.
Criterion (4) supplies a signed unit \(q_{k,l}\) making
\[
                              u_{k,l}=q_{k,l}V_kV_l>0          \tag{6}
\]
at every grid point.
This supplies an actual integral positive multiplier at every conductor \(3^m\).
A deterministic rectifier is obtained by solving the finite signature system in the signed-unit columns used by the native program.
Different pairs need not define different square classes.
For \(k=l\), the product is already a square and \(q=1\) is permitted.

Let \(N_p=|\operatorname{Res}(B,V)|\), and \(\mu=M(F)\).
The [full cyclic-norm identity](Yin_L_G0462_v6.md#galois-filter-law) gives
\[
 N_p^2=|\operatorname{Res}(F,z^p-1)|,\qquad N_p^{1/n}\longrightarrow\mu.
\]
For an admissible single rectified filter, its positive norm is \(N_p\).
For the paired construction,
\[
 \operatorname{Norm}(u_{k,l})=N_p^2,\qquad
                \operatorname{Norm}(u_{k,l})^{1/n}\longrightarrow\mu^2<2.
                                                                    \tag{7}
\]
The pair therefore costs the same norm power as one earlier squared filter, not the fourth power of two separately squared filters.
Multiplying a slow-cut representative with norm root tending to one preserves this limit.
It is below the necessary strict-shell budget but supplies no upper bound for the output polynomial's whole Mahler measure.

The same parity argument applies to any even number \(d\) of these unsquared Galois filters, with multiplier norm \(N_p^d\) and limiting norm root \(\mu^d\).
The [exact seed bounds](Yin_L_G0462_v6.md#galois-filter-law) put both \(\mu^2\) and \(\mu^4\) below the strict ceiling, while \(\mu^6>2\) excludes any fixed even \(d\ge6\) from a shrinking sequence in this chamber.
The four-filter version is only an algebraic supply observation; no moment-support calculation or candidate search for it was performed.

The pair resolves the single-filter parity obstruction at the level of integer supply across all conductors.
Choosing useful magnitudes, attaining the integer moment targets, imposing the strict endpoint and controlling the exceptional roots remain unresolved.

<a id="concrete-81"></a>
## A definite new conductor-81 square class

The [single-filter certificate](../computations/programs/Yin_J_G0154/signed_filters.md#rectifier) constructs
\[
 q=-\prod_{a\in A}\frac{T_a}{T_{3^{v_3(a)}}},\qquad
 A=\{6,10,11,12,13,17,18,23,25,28,29,30,34,37,38\}
\]
as an integral unit in \(\mathcal O_{81}\).
It verifies an integer inverse and certifies \(u=qV_1>0\) at all 40 nodes.
Its exact norm is 163, so it cannot be an integer square, whose norm would be the square of an integer.

From the fixed balanced base
\[
                    h_*=h_{0,81}U_2^6U_1^{-1}(T_3/T_{15})^2,
                          \qquad U_a=2+T_a,
\]
put \(h_{\rm new}=h_*u\).
It has the same nine-node negative block and norm \(32\cdot163=5216\).
Since \(h_*\) is nonzero on every component, \(h_{\rm new}=h_*v^2\) would imply \(u=v^2\), a contradiction.
The old complete energy-one and energy-two exclusion therefore does not by itself settle the new square-multiple family.
For a multiplier \(v\) nonzero on every component, \(|\operatorname{Norm}(uv^2)|=163|\operatorname{Norm}(v)|^2\) is not an integer square, so \(h_*uv^2\) cannot belong to the old family \(h_*w^2\).
Square multipliers vanishing on some components can instead give overlap between the two families; no disjointness is asserted for them.

The canonical rectifier is not already well balanced.
Its exact moments and energy are
\[
 K=21027435559692867443,\quad L=815499961442697404,\quad
                         2L+3K=64713306601963997137.
\]
They miss every prescribed target, and no whole measure was computed for this non-hit.
The same native program also rectifies \(V_1V_2\).
Its positive multiplier has norm \(163^2\) but is nonsquare, as shown by explicit odd-divisibility witnesses modulo \(163^2\).
This demonstrates that paired rectification need not return to the old square class even when its total norm is a square.
Its full coefficients, unbalanced moments and modular witnesses stay in the [native certificate](../computations/programs/Yin_J_G0154/signed_filters.md#nonsquare).

<a id="next-test"></a>
## The fixed bounded test and the probability boundary

The selected bounded test uses exactly the single-filter conductor-81 input.
Form \(H_{\rm new}=h_{\rm new}(J)\) and \(G_{\rm new}=(2J+3I)H_{\rm new}\).
The strict signs make \(G_{\rm new}\) positive definite.
An exact unimodular reduction changes coordinates within this new square-multiple domain, without identifying it with the old domain.
Enumerate only \(0<\mathbf v^{\mathsf T}G_{\rm new}\mathbf v\le2\) under a declared node/time cap.
For an actual leaf, compute its first moment, then check nonvanishing at the grid, the strict endpoint and the complete Mahler measure for a target hit.
An incomplete traversal gives no emptiness conclusion.
A complete failure rejects only these two targets in this new square-multiple domain, not all rectified filters.

The importable native call signed_filters.construct([1]) reconstructs this input without generated JSON.
The [separate native result](../computations/programs/Yin_J_G0154/nonsquare_control.md#complete-result) owns the completed traversal and its exact coverage; the present section retains the test's mathematical definition and limits.
That ordinary research computation and any formal review are separate from this strategic development.

No arbitrary-radius positive-probability estimate is established.
A law on these explicit integer inputs gives positive mass to each selected input, and a finite law on verified unit words gives explicit label weights.
It has positive small-shell probability only after an actual complete-measure hit or a genuine positive count has been established.
A new square class, available Galois indices, a norm budget below two, and a favorable continuous logarithmic region do not establish that discrete event.

Signed-unit rectification changes the arithmetic domain while retaining a controlled resultant.
The two automatic-positive alternatives pay too much norm in the stated forms.
The fixed single-input test has its separate result above, while the paired construction remains an all-conductor integer supply whose moment and whole-measure return is unresolved.
