---
author: Yin
---

# Fixed-norm residue tests at conductor 6561

<a id="sparse-unit-sieve"></a>
## Exact moment screening at four centers in two unit orbits

Use \(p=3^8=6561,\ n=3280,\ k=\lfloor p/\log p\rfloor=746\), and \(b_j=2\cos(2\pi j/p)\) for \(1\le j\le n\).
For the [surviving third-moment profile](../Yin_J_G0151/readme.md#next-conductor) \(x=-1\), the first two targets are \(K=\sum r_j=3,\ L=\sum b_jr_j=4\).
The next target is \(N=\sum b_j^2r_j=8\).
Here \(r_j=(4-b_j^2)h(b_j)/p\) is negative at the \(k\) smallest nodes and positive at all others.

The original center \(h_0\) uses the [integral cosine-sign construction](../../../ledger/Yin_L_G0464_v8.md#integral-sign-representative).
The selected column counts in ascending scales \(s=1,3,\ldots,2187\) are \(1050,369,123,46,15,6,1,1\).
For a selected column \(a\), its quotient is \(T_a/T_s\) on the grid, with \(s=3^{v_3(a)}\) and \(T_a(z+z^{-1})=z^a+z^{-a}\).
At each scale the alternating center takes these quotients in ascending column order, keeping the first, inverting the second, keeping the third, and continuing in this order.
It retains the factor \(T_s\) exactly when that scale has an odd column count, as in \(h_0\).
Replacing a quotient by its inverse multiplies by an integral totally positive unit, its inverse square.
Both centers have the stated cut and \(\Delta=2^{1502}\), since the exponent is \(\sum_{s:\,\text{odd count}}(s-1)/2\).
The [balanced center](#balanced-center) inverts a further 208 quotients from the alternating choice and retains the same strict signs and resultant.
The fourth center is the balanced center multiplied on the nodes by \(W=T_3^8/T_9^2>0\).
Writing \(A_\ell=2^{3^{\ell-1}t_\ell}\) for its absolute layer norms, the first three centers have \((t_1,\dots,t_8)=(5,4,3,3,2,2,1,0)\).
The correction adds \((6,-2,0,0,0,0,0,0)\), so all new valuations are nonnegative and the total norm exponent changes by \(6-2\cdot3=0\).
The transferred center is integral on each layer, and the denominator has only two-power norm, so the [layer Chinese remainder argument](../../../ledger/Yin_L_G0464_v11.md#layer-valuations-and-orbits) gives integrality in the full order.
Its distinct layer valuations place it in a second positive-unit orbit.

Let \(U_d=2+T_d\), for \(d\) among the 2187 integers from 1 through \(n\) coprime to three.
These factors are totally positive units on the full grid by permutation of the nodes and \(|B(-2)|=1\).
Multiply each center by the empty word, by every single \(U_d\), by all \(U_dU_e\) with \(d\le e\), and by every \(U_fU_dU_e\) with \(f\le d\le e\) and \(f\) among the first sixteen directions.
This counts words indexed by sorted directions, including repetitions.
The number per center is \(1+D+\binom{D+1}{2}+\sum_{i=0}^{15}\binom{D-i+1}{2}=40{,}414{,}134\), with \(D=2187\).

| Center | Parameter words | \(K=3\bmod39367\) | Both targets modulo \(39367\) | \(K=3\) modulo both primes | Integer \((K,L)=(3,4)\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original | 40,414,134 | 969 | 0 | 0 | 0 |
| Alternating | 40,414,134 | 1,011 | 0 | 0 | 0 |
| Balanced | 40,414,134 | 1,017 | 0 | 0 | 0 |
| Balanced multiplied by \(W\) | 40,414,134 | 999 | 0 | 0 | 0 |

Consequently even the first integer moment \(K=3\) has no solutions among these 161,656,536 parameter choices counted with their centers.
No input advances to third-moment, endpoint or whole-measure evaluation in this sieve.

The [finite-field program](p6561.py) verifies that each prime \(q=39367,52489\) admits a root \(\xi\) of exact order \(p\).
It reduces \(b_j\) to \(\xi^j+\xi^{-j}\), computes the center values there and checks the expected signed norm separately on each of the eight layers.
Every cosine denominator is nonzero in these odd characteristics because a zero would force an element of odd order to have a power of order two.
Finite orthogonality gives the reductions of the integer moments by the same weighted evaluations as over \(\mathbb C\).
For either moment let \(G_d=\sum_j w_jT_d(b_j)\), with \(w_j=r_j\) or \(b_jr_j\).
Multiplication by \(U_f\) replaces \(G_d\) by \(2G_d+G_{d+f}+G_{d-f}\), and the moment after multiplying by \(U_dU_e\) is \(2G_0+2G_d+2G_e+G_{d+e}+G_{d-e}\).
The program applies these identities modulo the first prime, then recomputes both moments of every first-moment residue match by direct summation on all 3280 nodes at each prime.
It compares the direct first-prime pair and the second-prime first moment with the frequency calculations.

<a id="protected-node"></a>
## Length needed for positive-unit corrections

The separator \(y=-68/45\) lies strictly between the two sign blocks by the [exact pole count](../Yin_J_G0151/readme.md#next-conductor).
Thus \(V_j=(b_j+68/45)r_j>0\) and the two moments require \(\sum_jV_j=L+68K/45=128/15\).
For \(h_0\) the program encloses \(2^{16374}<V_{1640}<2^{16375}\).
For the alternating center it encloses \(2^{153}<V_{940}<2^{154}\).
It evaluates the selected cosine ratios at the single indicated node using 160-bit Arb real balls and rational arguments to \(\cos(\pi t)\).

Allow any correction step given by a totally positive unit of the form \(T_a^2\) or \((T_a/T_b)^2\), or its inverse, in the full integral grid order.
This includes \(U_d=T_s^2\) for \(2s\equiv d\bmod p\).
At every node \(2/p\le |T_a(b_j)|\le2\), since the distance of \(2\pi aj/p\) from a cosine zero is at least \(\pi/(2p)\), and \(\sin(\pi/(2p))\ge1/p\).
Every step therefore leaves the positive summand at least \(p^{-2}\) times its preceding value.
The strict integer comparisons \(15\cdot2^{16374}>128p^{1290}\) and \(15\cdot2^{153}>128p^{10}\) exclude the two target moments simultaneously for **every** word of length at most 645 from \(h_0\) and every word of length at most 5 from the alternating center, with unrestricted choices and repetition of these generators.
These estimates leave longer corrections and other types of positive unit open.

<a id="balanced-center"></a>
## Magnitude-directed center outside the two short-word tests

Starting from the alternating signs, greedily flip a single selected quotient to decrease \(\sum_j V_j^\alpha\) using all 3280 node values, successively for \(\alpha=0.02,0.05,0.10,0.20,0.40,0.70,1\).
The program tests every flip at each step, breaks relative near-ties by ascending column index and stops the stage when the relative improvement is at most \(10^{-11}\).
The seven stages take 142, 34, 10, 22, 0, 4 and 0 steps, respectively, and the final signs differ from the alternating signs at 208 columns.
The stored integer mask fixes the representative independently of the numerical selection.
At this center 160-bit real-ball evaluations at all the nodes, combined with integrality of \(K,L\), give the unique integers
\[
 K=-1131435017943396285556,\qquad L=2851388676408052152242,\qquad
 45T=45L+68K=51374909218211399433082 .
\]
Thus \(2^{69}<T<2^{70}\), while the alternating center's single positive component already exceeds \(2^{153}\).
Both split-field calculations also recover the reductions of these center integers.
For the transferred center the same real-ball calculation gives \(K=1957492344071963752167247,\ L=393574365815142124636061\), also checked modulo both primes.

Write \(V^{(0)},V^{(1)},V^{(2)}\) for the components at the original, alternating and balanced centers, respectively.
The program verifies the strict ball comparisons
\[
 V^{(0)}_{1640}>64p^{1290}V^{(2)}_{1640},\qquad
 V^{(2)}_{1892}>p^{10}V^{(1)}_{1892},\qquad
 2270280229<V^{(2)}_{1892}<2270280230 .
\]
In the balanced family every word has at most three factors \(U_d\le4\), so its component at node 1640 lies below the applicable lower bound throughout the original center's length-645 ball.
The 1458 directions with \(U_d(b_{1892})\ge1\) are characterized by \(3\min(w,p-w)\le p,\ w=1892d\bmod p\) in \([0,p)\).
Words using only these directions keep the component above the upper bound \(p^{10}V^{(1)}_{1892}\) for the alternating center's length-five ball.
With the same triple anchors as the full balanced search, this subset contains 11,635,690 parameter words outside both previous balls.
Among those words 277 have \(K=3\bmod39367\), none has both target moments modulo 39367, and none has \(K=3\) modulo both primes.
These words are included in the full balanced row.
For arbitrary lengths, every nonnegative product of those 1458 units at the balanced center retains \(V_{1892}>2270280229>128/15\), which alone rules out the two target moments.
The full balanced row also tests directions that shrink this component.

<a id="replay"></a>
## Reproduction

From this directory run the following command using Python, NumPy and python-flint.
The [checked logarithmic floor](../Yin_J_G0148/cuts.py) is imported from J148.

~~~text
python -B p6561.py
python -B p6561.py --select
~~~

The first command uses the stored mask and the second replays the floating-point selection before checking its equality with the stored integer input and running the same certificates.
Both commands were run locally with NumPy 2.3.5 and python-flint 0.9.0.
For additional positive adjustments, see the [fiber screen](fibers.md#fiber-screen) and the [lower-layer control](fibers.md#lower-layer-control).
