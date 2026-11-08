---
author: Yin
---

# Conductor-6561 unit corrections and quotients of Salem seeds

At 2026-11-08T07:10 UTC an independent agent for Yin recorded the checks of the original and alternating conductor-6561 centers, the continuous order-27 fiber test and the Salem quotient argument.
The reviewer took no part in developing these inputs and received the selected paths and scope without their development dialogue, author explanations or earlier verdicts.
The coordinating reviewer received development updates about two further centers and a lower-layer example while this inspection was under way.
A separate reviewer outside their development checked these additions from the fixed programs and statements without those updates and returned the findings at 2026-11-08T07:09 UTC.

<a id="sparse-sieve-review"></a>
## Parameter words and protected nodes

I checked the two centers against the [integral sign construction](../../ledger/Yin_L_G0464_v8.md#integral-sign-representative).
Inverting any of its quotient units preserves the signs and layer norms, because the change is an inverse square.
The selected column counts on the eight scales give odd counts precisely at \(3,9,81,729,2187\), whose \((s-1)/2\) sum is \(1502\).
The primitive directions number \(D=2187\), and multiplication by each direction permutes the full grid up to sign.
For the triples with least direction of zero-based rank \(i\), the remaining sorted pair has \(\binom{D-i+1}{2}\) possibilities, including repeats.
Summing this expression over \(0\le i<16\) and adding the pairs, singles and empty word gives \(40\,414\,134\) parameter preimages per center.
No injectivity of the word-to-unit or unit-to-polynomial map enters the count.

The trace recurrence reduces the integral evaluations at a primitive \(6561\)st root in either splitting field.
The denominator \(6561\) is invertible there, and a vanishing cosine trace would give a power of the odd-order root equal to \(-1\).
I checked the normalization \(T_0=2\) and the pair expansion by \(T_dT_e=T_{d+e}+T_{d-e}\), including \(d=e\).
For a separate complete count I used another primitive root at both primes, the sign columns from J150, and collected the signed multiplicities of all \(T_a\) in each center before evaluation.
With the half-trace transform \(H_s=\frac12\sum_j w_jT_s(b_j)\), I applied successive translations for the prefix and took \(2H_0+2H_e\) for the last factor \(2+T_e\).
I screened both first-prime moments this way and recomputed the second-prime first moment of each candidate by direct node products.
Both this count and the supplied program gave respectively \(969\) and \(1011\) first-prime \(K\)-matches for the original and alternating center, zero first-prime joint matches and zero two-prime \(K\)-matches.
Thus the exact integer first-moment count already vanishes in both enumerated families, under every weighting of their parameter words.

The separator puts \((b_j+68/45)r_j>0\) at every node, and the target budget for their sum is exactly \(128/15\).
The 160-bit real-ball replay gave the claimed lower powers of two at nodes \(1640\) and \(940\), respectively.
For every cosine trace the absolute value is in \([2/p,2]\) by the odd-grid distance from a cosine zero and the chord bound for sine.
Consequently each allowed positive square or inverse square, of a trace or quotient of traces, is at least \(p^{-2}\) at that node.
The two strict integer comparisons establish the exclusions through lengths \(645\) and \(5\) for simultaneous target moments.
The argument concerns generator length and requires every step to be a unit of the indicated form in the full order.

<a id="additional-centers"></a>
## Two additional centers and a restricted set of directions

The separate reviewer ran the four-center program with its selector and matched the fixed mask, with 208 set bits, after the seven floating-point selection stages.
The mask specifies the exact third center independently of how it was found.
For the fourth center \(W=T_3^8/T_9^2\) changes the layer valuations by \((6,-2,0,0,0,0,0,0)\), giving the nonnegative vector \((11,2,3,3,2,2,1,0)\).
The change in the total norm exponent is \(6-2\cdot 3=0\), and the altered order-nine norm separates the fourth center from the positive-unit orbit of the first three.
Layerwise integrality and the two-power denominator give full-order integrality by the cited Chinese remainder argument.
The coordinated replay and the separate review both recovered the displayed exact \(K,L\) at the two centers.
Here integrality permits unique-integer recovery from the real balls, and the reductions at both splitting primes agree.

For the third and fourth center respectively, each full enumeration gave \(1017\) and \(999\) first-prime \(K\)-matches among \(40\,414\,134\) parameter words.
Neither enumeration retained a first-prime joint match or a two-prime \(K\)-match.
At the third center the condition \(3\min(w,p-w)\le p,\ w=1892d\bmod p\), selects exactly those directions whose unit value at node \(1892\) is at least one.
Intersecting the full family's sixteen triple anchors with the 1458 selected directions leaves ten anchors, so the \(11\,635\,690\) resulting parameter words are included in the full third-center count.
They have \(277\) first-prime \(K\)-matches and zero first-prime joint or two-prime \(K\)-matches.
The upper factor \(4^3\) at node \(1640\) and the lower factor one at node \(1892\), together with the strict ball comparisons, put these words outside the two earlier protected balls.
At arbitrary length a product of nonnegative powers of the 1458 units still has \(V_{1892}>2270280229\), enough to exclude simultaneous \(K=3,L=4\).
The finite first-moment exclusion has only the enumerated scope.
The isolated inspection found that the former single-node helper would return the alternating-center value if called separately with index three.
The fourth-center moment and sieve paths actually used in the replay had applied \(W\) explicitly and correctly.
The resulting helper repair was outside that reviewer's replay.

<a id="fiber-distortion-review"></a>
## Necessary variation inside an order-27 fiber

For an arbitrary totally positive integral unit \(u\) in the original orbit, restriction and restriction of its inverse give norm one on each primitive layer.
Thus the three entries of \(\log u\) at order nine have sum zero.
The two order-nine log vectors of \(U_1,U_2\) span this plane since their two-by-two minors are nonzero.
This gives unique **real** exponents \(d,e\), including for units outside the subgroup they generate.
The three individual positive mass limits yield a bounded triangle because its three normals sum to zero and span the plane.
I directly recomputed its pairwise vertices, whose extrema lie strictly inside the outward-rounded rectangle \([-7,8]\times[530,545]\).

Let \(S=279936/5\) and form the three groups of order-27 nodes by their image under \(T_3\).
Each group contains three nodes, and the product of the geometric means \(g_F\) of the normalized unit values is one by the order-27 norms of \(u,U_1,U_2\).
The mass of a group is at least \(g_F\sum_{j\in F}A_j/D_*\); multiplying the three bounds and applying arithmetic-geometric mean proves the lower bound \(V/D_*\) for their sum.
At a hit this sum is strictly less than \(S\) since every omitted mass is positive.

With 224-bit Arb I evaluated products of powers directly and recovered the 75 integral pairs below the order-nine budget and the unique minimum \(16822209.23568485\ldots\) of the stated lower sum at \((0,533)\).
Separately, using 192-bit balls and endpoint values of each positive power along each axis, I obtained 4969 retained closed cells among the \(120^2\) squares of side \(1/8\).
The smallest lower quotient of the fiber bound by \(S\) in this second calculation was \(238.3752798\ldots\), in the cell with lower corner \((2/8,4262/8)\).
This confirms \(D_*>238\) as a necessary condition for all units in the stated orbit, with the strict comparison following already from \(V/S\ge238\) and the omitted positive masses.
A factor of the form \(v(T_3)\) that is a totally positive full-grid unit is constant at order nine, where \(T_3=-1\), so its value there is one by its layer norm.
At order 27 it is constant on each fiber, giving \(D_*=1\) after removal of the \(U_1,U_2\) powers, even with additional unit factors equal to one on both orders.
The exclusion applies to this entire family without limiting its remaining exponents.

<a id="lower-layer-word"></a>
## Exact costs for an adjustment on four low layers

The separate reviewer ran the fixed fiber program and independently reconstructed the displayed adjustment in \(\mathbb Q[X]/(T_{q/3}(X)+1)\) at \(q=3,9,27,81\).
For a monic separable layer polynomial \(F\), the leading coefficient at degree \(\deg F-1\) of \(vF'\bmod F\) equals \(\operatorname{Tr}(v)\) by interpolation at its roots.
Exact rational arithmetic this way gave \(45\) times the first three layer masses as \(2208,4272,12960\), hence total mass \(432<S\).
At order \(81\) the exact ratio lies strictly between \(2^{704}\) and \(2^{705}\), so this single layer exceeds the full budget.
The check establishes the result for the fixed word; selection by least-squares fitting was not independently reconstructed.

<a id="salem-quotients-review"></a>
## Full measure of Salem quotients

For embeddings fixing \(\lambda\), the images of \(\mu\) are distinct because \(\lambda,\mu\) generate the compositum.
If two twisted quotients after extension had the same image, a common positive power of the corresponding \(\mu_i,\mu_j\) would coincide.
Transporting \(\mu_i\) to \(\mu>1\) in its normal closure forces the transported \(\mu_j\) to have the same modulus, which uniquely identifies that conjugate.
Thus all nonprincipal images in the fiber are distinct conjugates of the quotient, of modulus at least \(\lambda^a\).
Applying the calculation also to the inverse unit gives the maximum in (1) without counting all compositum embeddings as distinct roots.

I used the [fixed-field Salem generator theorem at its recorded scope](../literature/Smy15/Yin_U001.md#smy15-u001).
If the two positive seed fields coincide, the exponent of their common generator in the quotient is \(ai-bj\), and a nonzero exponent gives full measure at least the generator, also with a root-of-unity twist.
Different fields give at least \(A\) for seeds in \([A,B]\) since some relative degree exceeds one.
Conversely, for each Salem number \(\tau\downarrow1\) with \(A\tau^2<B\), the two indicated adjacent powers are distinct Salem seeds in the interval and give \(\tau\) with trivial twist and unit exponents.
Distinct conjugates remain distinct under positive powers by the same normal-closure argument, including conjugate pairs on the unit circle.
This yields positive probability in every shell \(1<M<1+\epsilon\) under a law charging every indicated choice, with no quantitative lower probability as \(\epsilon\downarrow0\).

For the three-arm progression I checked the substitution \(n=N+1\) into [C578](../../claims/Yin_C_G0578_v1.md#plastic-tree-all-root-cost) and the cyclotomic-order argument in [L462 v3](../../ledger/Yin_L_G0462_v3.md#minus-delay-progression), taking the fixed all-root and minimal-vanishing-relation inputs at their stated scopes.
Here \(\gcd(N+2,N+362)=\gcd(10,360)=10\), and the compositum degree is a multiple of the least common multiple even when the fields intersect.
The exponent in (2) is at least \(36\) at \(N=8\) and diverges, while the increasing positive roots have a common finite limit.
The whole progression therefore assigns zero mass to \(1<M<\lambda_8\) for every sampling law on the specified powers and twists.

For the [equal-degree construction](../../ledger/Yin_L_G0462_v3.md#same-degree-radicals), taking the actual base degrees \(D/h,D/k\) gives relative degrees at least \(h/g,k/g\), respectively.
Every conjugate of \(\gamma^\ell\) has exactly \(r=[\mathbb Q(\gamma):\mathbb Q(\gamma^\ell)]\) preimages among the conjugates of \(\gamma\), by separability in the field tower.
This proves \(\ell m(\gamma)=r m(\gamma^\ell)\) for these algebraic units and yields precisely (3) after division.
Since \(r\ge1\) and both subset differences contain a prime, the bound forces \(r/g\to0\) and \(g\to\infty\) along any such positive near-one sequence.
This is a necessary degree constraint on aligned radical quotients.
The generator theorem, the earlier three-arm root theorem and the earlier radical irreducibility inputs were used at their recorded scope without a new proof audit of their external dependencies.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Sparse sieve](#sparse-sieve-review) | independently reviewed |
| [Additional centers](#additional-centers) | independently reviewed |
| [Fiber distortion](#fiber-distortion-review) | independently reviewed |
| [Low-layer example](#lower-layer-word) | independently reviewed |
| [Salem quotients](#salem-quotients-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Sparse sieve](#sparse-sieve-review) | [J152 counted words](../../computations/programs/Yin_J_G0152/readme.md#sparse-unit-sieve) | Original and alternating centers, exact parameter counts and moment conclusions. |
| [Sparse sieve](#sparse-sieve-review) | [J152 word-length bound](../../computations/programs/Yin_J_G0152/readme.md#protected-node) | Both protected values, allowed generators and maximal asserted lengths. |
| [Sparse sieve](#sparse-sieve-review) | [J152 split-field program](../../computations/programs/Yin_J_G0152/p6561.py) | Full replay, separate enumeration and the real-ball protected-node checks. |
| [Additional centers](#additional-centers) | [J152 four-center counts](../../computations/programs/Yin_J_G0152/readme.md#sparse-unit-sieve) | Two additional centers, layer transfer and both full counts. |
| [Additional centers](#additional-centers) | [J152 balanced center](../../computations/programs/Yin_J_G0152/readme.md#balanced-center) | Exact seed values, two node comparisons, restricted words and arbitrary nonnegative powers. |
| [Additional centers](#additional-centers) | [J152 selector and sieve](../../computations/programs/Yin_J_G0152/p6561.py) | Four-center replay with the selector, residue tests, restricted anchors and finite counts. |
| [Fiber distortion](#fiber-distortion-review) | [J152 order-27 test](../../computations/programs/Yin_J_G0152/fibers.md#fiber-screen) | Full positive-unit orbit, integer exponent pairs, continuous triangle and pullback exclusion. |
| [Fiber distortion](#fiber-distortion-review) | [J152 fiber program](../../computations/programs/Yin_J_G0152/fibers.py) | Nine- and twenty-seven-layer evaluations, outward bounds and full real subdivision. |
| [Low-layer example](#lower-layer-word) | [J152 control word](../../computations/programs/Yin_J_G0152/fibers.md#lower-layer-control) | Fixed correction and first four layer masses. |
| [Low-layer example](#lower-layer-word) | [J152 control evaluation](../../computations/programs/Yin_J_G0152/fibers.py) | Replay and separate exact quotient-ring traces. |
| [Salem quotients](#salem-quotients-review) | [L462 v4 embedding fibers](../../ledger/Yin_L_G0462_v4.md#cross-field-fibers) | Distinct conjugates, same-field generators and the full-support interval equivalence. |
| [Salem quotients](#salem-quotients-review) | [L462 v4 progression](../../ledger/Yin_L_G0462_v4.md#adjacent-ratios) | Adjacent exponential measure cost and strict-shell exclusion on the whole progression. |
| [Salem quotients](#salem-quotients-review) | [L462 v4 aligned radicals](../../ledger/Yin_L_G0462_v4.md#aligned-radical-test) | Relative degrees, exact power multiplicity and necessary common-part loss. |
