---
author: Yin
---

# Exact Galois-filter supply on slow ternary cuts

<a id="scope"></a>
## Question and scope

Test actual integral inputs obtained by multiplying the [low-norm sign representative](../../../ledger/Yin_L_G0464_v8.md#integral-sign-representative) by one or two squared Galois conjugates of the Lehmer trace polynomial.
For \(p=3^m\), set \(s=\max\{2,\lceil\log_3m\rceil\}\) and \(k=3^{m-s}\), using only \(1<s<m\).
The completed finite window is \(p=27,81,243,729\), with respective cuts \(k=3,9,27,81\).
These are the [slow terminal cuts](../../../ledger/Yin_L_G0464_v8.md#small-norm-terminal-block), not the earlier cuts \(\lfloor p/\log p\rfloor\).

Let \(n=(p-1)/2\), \(b_j=2\cos(2\pi j/p)\), \(B=\prod_j(t-b_j)\), \(D=B_{n-1}\), and \(\nu_j=(4-b_j^2)/p\).
The baseline \(h_{0,p}\) is the deterministic sign-column solution produced by the existing [J150 solver](../Yin_J_G0150/moments.py), with the same ascending pivot rule and the parity payments of L464 v8.
No positive-unit adjustment or endpoint-forcing power is added.
Write \(T_i(z+z^{-1})=z^i+z^{-i}\), and use
\[
 V_a=T_{5a}+T_{4a}-T_{2a}-T_a-1,\qquad
 A_p=\{1\le a\le n:\gcd(a,p)=1\}.
\]
The tested integer inputs are
\[
 h=h_{0,p}V_a^2\quad(a\in A_p),\qquad
 h=h_{0,p}(V_aV_b)^2\quad(a,b\in A_p,\ a\le b).
\]
Thus repeated filters are included, and swapping the two filters is not counted twice.
The double-filter table and histogram use these unordered multiplicities.
To recover the ordered law in [L462 v6](../../../ledger/Yin_L_G0462_v6.md#exact-support-test), an off-diagonal pair has multiplicity two and a diagonal pair has multiplicity one; the present histogram is not that ordered probability distribution.
The support and the absence of target hits are the same under either convention.
For every input, compute the exact joint moments
\[
 K=\sum_j\nu_jh(b_j),\qquad L=\sum_jb_j\nu_jh(b_j),
\]
and test every target \((K,L)=(x^2+2,-4x)\), \(x=-2,-1,0,1,2\).
These are necessary tests before forming \(Q=(t-2x)B+Dh\bmod B\) and its complete reciprocal lift.

<a id="cyclic-arithmetic"></a>
## Files and exact cyclic arithmetic

[galois_filters.py](galois_filters.py) owns the complete traversal and reproducible joint distributions.
Its only retained source-program dependency is the sign solver and low-dimensional comparison in [J150 moments.py](../Yin_J_G0150/moments.py).
It uses symmetric length-\(p\) integer words in
\(\mathbb Z[z]/(1+z+\cdots+z^{p-1})\), normalizing by subtracting the coefficient at index \(n\) from every coefficient.
The resulting two middle coefficients vanish, so the word represents the integral trace polynomial
\[
                 h(t)=w_0+\sum_{j=1}^{n-1}w_jT_j(t).
\]
Subtracting a constant word does not change values at the nontrivial \(p\)-th roots.
Multiplication uses exact cyclic convolution after shifting each word to nonnegative entries.
Byte packing chooses a radix strictly larger than \(p\) times the product of both coefficient ranges, so no coefficient carry occurs.
Reduction modulo the radix raised to \(p\), minus one, folds the ordinary convolution cyclically; normalization then removes the added constant word.

For a selected sign column \(a=3^eu\), the baseline program forms \(T_a/T_{3^e}\) in this integral quotient.
The identity
\[
 (z^d+z^{-d})\sum_{j=0}^{p/\gcd(p,d)-1}(-1)^jz^{(2j+1)d}=2
\]
on the cyclic quotient supplies twice its inverse.
The program checks this identity, exact divisibility by two in every quotient, and multiplication back by \(T_{3^e}\).
Replacing an even number of cosine factors by one preserves their nonzero signs; the retained sign solver checks every node's exact sign bit.

For a symmetric word the root-of-unity sum gives
\[
                         K=w_0-w_2,\qquad L=w_1-w_3.
\]
Indeed, the vanished trivial-character term permits summation over all \(p\)-th roots, and the factor \(4-b^2=2-z^2-z^{-2}\) extracts these coefficient differences.
Every \(V_a^2\) is retained as an exactly collected sparse cyclic word.
The single-filter words are constructed completely; the two-filter moment pairs are extracted by sparse correlation before any full second multiplication.
No modular rejection, floating-point approximation or sampled parameter choice omits a label.

<a id="norm-and-controls"></a>
## Exact norms and local verification

The baseline norm formula gives
\[
 |\operatorname{Res}(B,h_{0,p})|=2^{\,2\cdot3^{s-1}-1}=32
\]
throughout this finite window.
The program independently computes the integer resultant of the reconstructed baseline polynomial with \(B\) at all four conductors and checks that value.
Let \(N_p=|\operatorname{Res}(B,V_1)|\).
Multiplication by a unit modulo \(p\) permutes all nonzero trace classes, including the imprimitive ones, so every \(V_a\) has this same norm.
The exact values are:

| \(p\) | \(N_p\) |
| ---: | ---: |
| 27 | 1 |
| 81 | 163 |
| 243 | 3113425999 |
| 729 | 43277631155108742057426611 |

In particular every filter is nonzero at every node, and squaring preserves the baseline's strict signs.
The resulting whole input norms are \(32N_p^2\) for one filter and \(32N_p^4\) for two, also when \(a=b\).
The filters at 27 are units; they are nonunits at each of the other tested conductors.
As an additional representation check, the program reconstructs \(V_a^2\) and computes its resultant directly at the first, middle and last Galois labels for each conductor, obtaining \(N_p^2\) in all cases.

At \(p=27\), the baseline word agrees exactly with the original J150 polynomial-construction implementation.
All nine single-filter polynomials and all 45 double-filter polynomials are also reconstructed independently by ordinary FLINT polynomial composition and reduction modulo \(B\), rather than by cyclic word multiplication.
For all 45 pairs, the coefficients of \(C=Dh\bmod B\) give the same \(K,L\) as both the full cyclic word and the sparse correlation.
These are author-level local checks of the program and its mathematical representation; they are not an independent project proof review.

<a id="finite-results"></a>
## Results and limits

The complete finite traversal found no joint two-moment hit at any of the five target profiles.
Within each single-filter or double-filter traversal, every computed joint pair \((K,L)\) is distinct.

| \(p\) | \(k\) | Single-filter labels | Double-filter labels | Single joint hits | Double joint hits |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 27 | 3 | 9 | 45 | 0 | 0 |
| 81 | 9 | 27 | 378 | 0 | 0 |
| 243 | 27 | 81 | 3321 | 0 | 0 |
| 729 | 81 | 243 | 29646 | 0 | 0 |

At 27 the only input with \(K\in\{2,3,6\}\) is the double filter \((a,b)=(2,5)\), giving \((K,L)=(2,9)\).
The profile with \(K=2\) requires \(L=0\), so this input fails the second moment.
At each of 81, 243 and 729, every tested \(K\) exceeds 6.
For instance, the smallest single- and double-filter \(K\) at 81 are respectively 440694762156419 and 9112789263427.
The corresponding minima at 243 have 87 and 84 decimal digits; at 729 they have 357 and 351 decimal digits.
The low norm of this particular representative therefore does not supply the required small moments, even after all of the specified single or double Galois filters.

No input passed the two moments, so no strict endpoint or complete Mahler-measure computation was run or needed in this finite test.
The program retains any future moment hit for those separate tests; it does not claim a certificate for an unexecuted root-finding path.
For any probability law supported on one of these finite tested label sets, the event of hitting one of the five prescribed joint moment targets has probability zero.
This statement does not concern arbitrary low-measure polynomials outside those necessary-moment targets.
The computation excludes neither other sign representatives in the same norm classes, additional positive-unit adjustments, other filters, nor an unbounded conductor sequence.
It supplies no positive-probability result for arbitrarily small strict Mahler shells.

<a id="reproduction"></a>
## Running the finite traversal

Run from the repository root with Python, python-flint, SymPy and NumPy.
The executed environment used Python 3.14.7, python-flint 0.9.0, SymPy 1.14.0 and NumPy 2.5.4.
NumPy is imported by the retained J150 dependency; the new traversal itself uses integer arithmetic and FLINT integer polynomials.

~~~text
python -B mathematics/computations/programs/Yin_J_G0154/galois_filters.py
~~~

The default command traverses the full four-conductor window, without requiring any generated input.
The explicit option `--conductors 27 81` selects those complete smaller conductor cases and does not claim the others.
The files `mathematics/computations/outputs/Yin_J_G0154/galois_filters_<p>.json` are regenerated local outputs.
Each contains the exact baseline word, sign columns, filter norm, full label set, every joint \((K,L)\) pair with its count, first-moment hits and any joint hits.
The files are written only after the corresponding conductor traversal and its checks complete.
No random seed, floating precision or previous output is used by this exact screen.

<a id="related-controls"></a>
## Further controls and review

The [independent baseline finding](../../../audits/reviews/Yin_R_G1107_v11.md#galois-filter-finite-review) checks the model, norm budget, complete finite label coverage and the stated probability scope.
The [balanced controls](balanced.md#scope) separately own the two adjusted bases, the conductor-81 unit descent, both complete filtered supports and the conductor-27 whole-measure enclosure, checked by the [separate independent finding](../../../audits/reviews/Yin_R_G1107_v11.md#balanced-control-review).
The [radius-two unit window](unit_ball.md#results) covers all 2813 exponent labels at the final conductor-81 base, with [independent review](../../../audits/reviews/Yin_R_G1107_v12.md#unit-ball-review).
The [integer-square search](low_energy_shell.md#partial-result) reached its node cap before exhausting the ball of energy at most six.
Its [independent prefix review](../../../audits/reviews/Yin_R_G1107_v12.md#low-energy-prefix-review) confirms the exact visited prefix and incomplete status; it supplies no exclusion for the unvisited branches.
The separate [complete ball at energies one and two](two_energy_shell.md#scope) excludes both energies for every integer square multiplier of that fixed base.
Its 2084-node complete traversal has a [separate independent finding](../../../audits/reviews/Yin_R_G1107_v12.md#two-energy-review), without extending the energy-six result.
