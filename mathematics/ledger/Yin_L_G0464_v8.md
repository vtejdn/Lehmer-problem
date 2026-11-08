---
author: Yin
---

# Integral realization and norm cost of cuts at conductors \(3^m\)

For the [odd-grid construction](Yin_L_G0464_v5.md#odd-grid-product), the full grid at \(p=3^m\) admits every prescribed sequence of residue signs at a normalized resultant cost at most \(\sqrt2\).
The layer norms also give a lower bound for arbitrary integral inputs that excludes bounded resultants when a nonempty negative block approaches the left endpoint.
A delegated agent derived and self-checked this construction for Yin's [small-shell investigation](../tasks/Yin_T_G0001_v1.md#decision-resume-small-shell-2026-11-08).

<a id="three-power-cost"></a>
## The cost of a specified sign pattern

Fix \(m\ge2,\ p=3^m,\ n=(p-1)/2,\ b_j=2\cos(2\pi j/p)\) for \(1\le j\le n\), and \(B=B_n,\ D=B_{n-1}\) in the odd-grid notation.
Set \(T_a(z+z^{-1})=z^a+z^{-a}\).
The nodes of exact order \(3^\ell\) form layer \(\ell\), of size \(d_\ell=3^{\ell-1}\), for \(1\le\ell\le m\).
Write \(\eta_\ell\in\{0,1\}\) for the parity of the number of requested negative residues in that layer and set \(\eta_0=0\).
For any integer \(a\) there is an explicit \(h\in\mathbb Z[t]\) of precisely the requested signs on the nodes such that, for
\[
 C=\operatorname{rem}_B(Dh),\qquad Q=(t-a)B+C,\qquad
 \Delta=|\operatorname{Res}(B,Q)|,
\]
one has
\[
  \Delta=2^E,\qquad
  E=\sum_{\substack{0\le e<m\\ \eta_{e+1}\ne\eta_e}}\frac{3^e-1}{2}
    <\frac n2 .
\]
Indeed \(r_j=C(b_j)/B'(b_j)=\nu_jh(b_j)\), where \(\nu_j=4\sin^2(2\pi j/p)/p>0\).
Also \(D\) has absolute resultant one with \(B\), since \(|D(b_j)|=|1+\exp(2\pi i j/p)|\) and evaluation of \(1+z+\cdots+z^{p-1}\) at \(-1\) gives one upon pairing conjugates.
The construction below uses one square matrix of bits and ordinary integral products.

<a id="cosine-sign-basis"></a>
## The cosine signs on the full grid

Encode a negative value by one over \(\mathbb F_2\).
On layer \(\ell\) let \(V_\ell\) be the space of bit vectors, indexed by the invertible residues modulo \(3^\ell\) up to sign.
For \(\ell\ge2\) write \(I\) for pulling a vector back to the three lifts of each index and \(N\) for summing a vector on those three lifts.
Then \(NI=1\), and \(V_\ell=IV_{\ell-1}\oplus W_\ell\), where \(W_\ell=\ker N\).
Set \(W_1=V_1\), with no lower layer.

The signs \(v_{\ell,u}\) of \(T_u\) on layer \(\ell\), as \(u\) runs through the invertible classes modulo \(3^\ell\) up to sign, form a basis of \(V_\ell\).
These are signs of real circular units, for which the [prime-power sine-signature description](../audits/literature/DDK19/Yin_U001.md#sine-signatures) gives the general setting.
Here the specific spanning assertion follows directly.
On the lowest layer \(T_u=-1\).
On each triple of lifts the trace values for invertible \(u\) solve \(X^3-3X-y=0\), where \(y\) is the corresponding lower-layer value.
Their product is \(y\) and their sum is zero, so \(Nv_{\ell,u}=v_{\ell-1,u}\) and the three signs are mixed.
In particular \(v_{\ell,1}+INv_{\ell,1}\) is a nonzero element of \(W_\ell\) in the span of the translates of \(v_{\ell,1}\), because \(IN\) sums the three translations by the kernel of the restriction to the lower layer.

Multiplication by two cyclically permutes the \(d_\ell\) indices.
Indeed \(4=1+3\) and cubing an integer \(v>1\) congruent to \(1\) modulo \(3\) increases the \(3\)-adic valuation of \(v-1\) by exactly one, by binomial expansion.
It follows that \(2\) has order \(2\cdot3^{h-1}\) modulo every \(3^h\), and generates the quotient by signs as well.
In the cyclic shift representation over \(\mathbb F_2\), \(W_\ell\) for \(\ell\ge2\) is irreducible.
To see this, \(V_\ell\) is the regular module \(\mathbb F_2[X]/(X^{d_\ell}-1)\), and the lower component corresponds to the roots of \(X^{d_{\ell-1}}-1\).
The complementary roots have exact order \(3^{\ell-1}\), have no multiplicities, and form a single orbit under the Frobenius square by the order just computed.
Thus their common factor \(\Phi_{3^{\ell-1}}\) is irreducible.
The nonzero difference on a triple therefore generates \(W_\ell\), and the norm images of the translates span \(V_{\ell-1}\) by induction.
This proves spanning, hence the basis assertion by the number of vectors.

The \(n\) columns consisting of the signs of \(T_a\) on the **full** grid, \(1\le a\le n\), also form a basis.
For the proof, transform any full vector with layers \(s_\ell\) into layers \(s_\ell+I s_{\ell-1}\), taking the lower term to be zero at \(\ell=1\).
This transformation is invertible by recursion.
Group the columns by \(a=3^e u\), taking \(u\) up to sign modulo \(3^{m-e}\).
They vanish as bits on \(\ell\le e\), where their actual values are two.
On \(\ell>e\) their transformed bits are
\[
 I^e\big(v_{\ell-e,u}+I v_{\ell-e-1,u}\big)\ \in\ I^e W_{\ell-e},
\]
again with the lower term zero at layer one.
For each \(\ell\) the spaces \(I^e W_{\ell-e}\), \(0\le e<\ell\), are precisely its direct-sum decomposition.
For a fixed \(e\), taking the successive norms of a vector in \(V_{m-e}\) and the displayed differences gives an isomorphism onto the direct sum of the \(W_h\) for \(1\le h\le m-e\), by \(NI=1\).
The top vectors \(v_{m-e,u}\) form a basis and descend to the indicated \(v_{h,u}\).
Thus the columns with this \(e\) generate exactly their summands at all levels, proving the full assertion.

<a id="integral-sign-representative"></a>
## A product with only one possible norm payment at each scale

Solve the full bit system for the desired signs by Gaussian elimination.
The sign bit of column \(a\) at node \(j\) is one exactly when the least nonnegative residue of \(aj\) modulo \(p\) lies strictly between \(p/4\) and \(3p/4\).
For each selected column write \(a=3^eu\) up to sign modulo \(p\), choosing a positive odd representative \(u\bmod 3^{m-e}\).
Since \(T_u(X)\) is odd for odd \(u\), \(J_u(X)=T_u(X)/X\) is an integral polynomial with \(J_u(2)=1\).
On the grid the column's actual value is \(T_{3^e}(b_j)J_u(T_{3^e}(b_j))\).
The second factor has absolute norm one on each layer, as the numerator and denominator there are conjugates for \(\ell>e\) and both two for \(\ell\le e\).
For each \(e\) let \(\epsilon_e\) be the parity of the number of selected columns in the group.
Take
\[
 h(t)=\prod_{e=0}^{m-1}T_{3^e}(t)^{\epsilon_e}
       \prod_{\text{selected }(e,u)}J_u(T_{3^e}(t)).
\]
Removing an even power of a nonzero cosine preserves every sign.
The group factor \(T_{3^e}\) has absolute layer norm \(2^{d_\ell}\) for \(\ell\le e\) and signed layer norm \(-1\) for \(\ell>e\), by the cubic product, its odd repetition count and the lowest value \(-1\).
The \(J_u\) factors all have positive signed layer norms, so \(\eta_\ell=\sum_{e<\ell}\epsilon_e\bmod2\).
This proves the formula for \(E\) since \(\sum_{\ell\le e}d_\ell=(3^e-1)/2\) and \(\sum_{e<m}(3^e-1)/2=n/2-m/2\).

<a id="arbitrary-input-lower-bound"></a>
## A lower bound for every integral input with those signs

Every integral remainder \(C\) with nonvanishing node values has the form \(Dh\bmod B\) for integral \(h\), since multiplication by \(D\) on \(\mathbb Z[t]/B\) has determinant \(\pm1\).
Let \(A_\ell>0\) be the absolute layer norm of this \(h\), so \(\Delta=\prod_\ell A_\ell\).
For every \(\ell\) the signed norm is congruent to \(h(2)\) modulo three.
Indeed the monic layer trace polynomial reduces to \((t-2)^{d_\ell}\) modulo three, by lifting to \(\Phi_{3^\ell}(z)\equiv(z-1)^{2d_\ell}\) and using \(z(t-2)=(z-1)^2\).
Reduction of the norm gives \(h(2)^{d_\ell}\equiv h(2)\).
If \(3\mid h(2)\), it follows that \(\Delta\ge3^m=p\).

Otherwise \(A_\ell^2\equiv1\bmod 3^\ell\).
In fact for a primitive \(3^\ell\)-th root \(\xi\), the ring
\(\mathbb Z[\xi]/(h(\xi+\xi^{-1}))\) has size \(A_\ell^2\) by the determinant of multiplication, and three is invertible in it.
For \(0<j<3^\ell\), \(1-\xi^j\) divides a power of three in \(\mathbb Z[\xi]\), since the product over the primitive roots of the order of \(\xi^j\) of one minus the root equals three.
Thus multiplication by \(\xi\) gives orbits of size \(3^\ell\) on all nonzero elements of the quotient.
This proves the congruence, including the one-element quotient.
The two possible square roots of one modulo \(3^\ell\) are \(1,-1\), and their reductions modulo three differ.
Write \(\delta=0\) if \(h(2)\equiv1\bmod3\) and \(\delta=1\) if \(h(2)\equiv-1\bmod3\).
Since the signed norm is \((-1)^{\eta_\ell}A_\ell\), the full bound is
\[
       \Delta\ \ge\ \prod_{\ell:\,\eta_\ell\ne\delta}(3^\ell-1).
\]
In particular the patterns realizable by a unit are exactly those for which all \(\eta_\ell\) coincide, by this necessity and the integral product above.
For example the all-positive pattern is realized by \(h=1\).

For a terminal block of \(k\) negatives in decreasing \(b_j\) order, the distances from the angle \(\pi\) are \(\pi d/p\) for \(d=1,3,\ldots,2k-1\).
Let \(K_i=\lfloor k/3^i+1/2\rfloor\), the number of these \(d\)'s divisible by \(3^i\).
The layer of order \(3^{m-i}\) contains \(K_i-K_{i+1}\) negatives.
For \(k>0\) some layer count is odd.
If all were even, then \(K_m=0\) would imply all \(K_i\) even, while the balanced ternary digits \(K_i-3K_{i+1}\in\{-1,0,1\}\) would all be zero.
This would give \(k=K_0=0\).
Every layer with a negative contains a \(d\le2k-1\), so its order \(p/\gcd(p,d)\) is at least \(L=p/(2k-1)\).
When \(L>3\), the largest power of three strictly below \(L\) is at least \(L/3\) and is the order of an entirely positive layer.
For \(\delta=0\) use an odd-count layer, and for \(\delta=1\) use that positive layer.
Together with the divisible-by-three case, this gives the uniform lower bound
\[
                      \Delta\ge L/3-1\qquad(L>3).
\]
Thus any nonempty terminal block with \(k=o(p)\) forces \(\Delta\to\infty\) at conductors \(3^m\), including when the exceptional traces are real.

<a id="small-norm-terminal-block"></a>
## Terminal blocks and complete exterior cost

For \(m\ge3\), the cut \(k=\lfloor p/\log p\rfloor\) has \(1\le k<n\), satisfies the required [endpoint exponent](Yin_L_G0464_v5.md#endpoint-index-exponent) as \(m\to\infty\), and its prescribed signs are realized with \(\Delta^{1/n}<\sqrt2\), below the [necessary shrinking-shell ceiling](Yin_L_G0464_v6.md#norm-ceiling).
For large \(m\) its bottom layer is positive, so the parity argument guarantees a genuine nonunit.
For a second explicit choice let \(k=3^{m-s}\), \(1<s<m\).
Then \(K_i=3^{m-s-i}\) up to \(i=m-s\), and \(K_i=0\) afterwards.
Only layer \(s\) has odd negative count, so the construction gives exactly
\[
                   \Delta=2^{(3^{s-1}-1)/2+(3^s-1)/2}
                          =2^{2\cdot 3^{s-1}-1}.
\]
For sufficiently large \(m\), taking \(s=\lceil\log_3 m\rceil\) gives \(k/p\) comparable to \(1/\log p\) and \(\Delta\) polynomially bounded in \(p\).
More slowly diverging \(s=o(m)\) also gives \(k/p\to0,\ \log k/\log p\to1,\ \Delta^{1/n}\to1\).

For each of these cuts and any fixed \(a=2x,\ x\in\{-2,-1,0,1,2\}\), a positive unit enforces the strict endpoint and gives an explicit family whose whole measure can be evaluated asymptotically.
Replace \(h\) by \(h(t)(2+t)^d\), which preserves all signs and the resultant because \(|B(-2)|=1\).
Write \(r_j=\nu_jh(b_j)(2+b_j)^d\) and \(A=r_1\).
Choose the least nonnegative integer \(d\) satisfying
\[
 A\ge p^2+64,\qquad
 \sum_{j>1}|r_j|\le A/p,\qquad
 \sum_{j>1}\frac{|r_j|}{2+b_j}\le A/8.
\]
This index exists because \(h(b_1)>0,\ 2+b_1>1\) and each other base \(2+b_j\) is strictly smaller and positive.
Now \(Q(-2)/B(-2)=-2-a-\sum r_j/(2+b_j)\le 2-A/8<0\).
At \(t=\sqrt A\,w\), the rational function \(Q(t)/(B(t)\sqrt A)\) converges locally uniformly away from zero to \(w+1/w\) as \(m\to\infty\).
Indeed the first residue term is \(1/(w-b_1/\sqrt A)\), and the sum of the remaining absolute numerator weights after scaling is at most \(1/p\).
Small disjoint circles about \(i,-i\) therefore contain one rescaled zero each by Rouché's theorem.
The original pair is \(q,\bar q\) with \(q/\sqrt A\to i\) in the upper half-plane.
The [same-sign gaps and left endpoint](Yin_L_G0464_v1.md#positive-resolvent) already give \(n-1\) distinct real roots in \((-2,2)\), accounting for every other trace root.
Consequently the whole lift \(P=z^{n+1}Q(z+z^{-1})\) satisfies
\[
              M(P)=|\lambda|^2=(1+o(1))A\longrightarrow\infty,
       \qquad \lambda+\lambda^{-1}=q,\quad|\lambda|>1 .
\]
This choice of \(d\) realizes the required cut, endpoint, coefficient \(a\) and norm budget simultaneously, and shows the exterior cost of that choice.
Whether another choice of magnitudes in these signature classes can satisfy the complete shrinking-shell condition remains open.
