---
author: Yin
---

# Integer Gram boundary cokernels and actual shift costs

Current complete mathematical home: [C393v1](../claims/Yin_C_G0393_v1.md#statement).
The dated allocation, adoption and continuation descriptions below retain the original research/check context and supply no Task/E resumption.

Date: 2026-10-11.
Root coordinating AI for Yin fixes this restricted exploration under the continuing G0001 weekly authorization after complete separately organized noncontributor review in [the responsible R](../audits/reviews/Yin_R_G0190_v1.md#whole-boundary-shift-finding).
Adoption covers the exact complete retained author body below, its declared hypotheses, original costs, actual failures, source boundaries and review limits.
No unrestricted gap or Task completion is asserted.

<a id="third-coupling-batch-fixed-scope"></a>
## Fixed scope and preserved account

The entire original author account and later author review notices follow, with only heading depth and navigation relocated.
Allocation-era pending or unrun statements remain historical; the linked fixed R supersedes pending review only at its actual inspected scope.
Proposed enormous finite expressions remain UNRUN; a known-measure comparison is not a newly executed certificate.
No canonical Claim, uniform near-one estimate or new allowance is created.
Continued research uses a separate responsible draft.

## Complete retained account

## Actual boundary vectors and shift relations in integer Toeplitz Gram cokernels

## Question, contribution and scope

Under renewed G0001 research, continue [L363](Yin_L_G0363_v1.md#cokernel-denominator-identity): for a monic unit polynomial P of degree d, its extreme autocorrelation is+/-1.
Root supplied the observation that finite banded Gram row recurrences should generate the integer cokernel by at most the first min(d,n) coordinate classes.
That observation alone controls a largest Smith invariant rather than the order of the ACTUAL boundary vector b_n, which equals the minimal optimizer normalizer k_n.
The assess_bv19b_current AI agent for Yin must test the full boundary relations and whether any induced shift is justified before using that vector as a cyclic generator.

This draft is allocated before substantive derivation.
Seek an exact actual-input relation between k_n, the Gram determinant and the boundary class, or a precise failed-transfer control on an irreducible noncyclotomic unit input.
Do not infer that an ambient coordinate shift descends through the finite Gram relations.
No theorem, computation, J, source acquisition or independent review is asserted at creation.
Root owns Task/strategy/execution state; this agent owns only the argument in this home.

<a id="gram-boundary-setting"></a>
## 1. Complete banded Gram object and the actual boundary vector

Let P(t)=sum_(i=0)^d a_i t^i be an integer polynomial of degree d>=1 with a_d=1 and a_0=+/-1.
Define

    c_h=sum_i a_i a_(i+h),    c_(-h)=c_h,
    c_h=0 for |h|>d,         c_d=a_0 a_d=+/-1.

Indices outside0,...,d contribute zero.
Write

    T_n=(c_(i-j))_(0<=i,j<n),    D_n=det T_n,
    b_n=(c_1,...,c_n)^T,        A_n=Z^n/T_n Z^n.

This is the full coefficient Gram matrix for |P|^2, with every original coefficient and scalar content retained.
It is positive definite.
D_n is its positive integer determinant, and the denominator of the degree<=n predictor q(0)=1 is the order of the ACTUAL class[b_n] in A_n: its other coefficients are-T_n^(-1)b_n.
This direct normal-equation observation is the same exact interface proved in [L363](Yin_L_G0363_v1.md#cokernel-denominator-identity), not a new definition of the normalizer.
Denote that order by k_n.

The bounded local screen read the actual full Toeplitz/residual account [L4](Yin_L_G0004_v1.md#degree-window-tests), [L359](Yin_L_G0359_v1.md#integer-multiplier-variational-formula), and [L9's already retained radical family](Yin_L_G0009_v1.md).
The first-d-generator observation was supplied by root; the full boundary presentation, commutator obstruction, selected-vector index and calculations below were developed by this assigned agent.
No claim of historical novelty is made for elementary band elimination, Smith interpretation or the known radical construction.

<a id="full-boundary-presentation"></a>
## 2. Exact dimension-d presentation with both boundaries retained

Let V=Z^d have standard basis f_0,...,f_(d-1).
Define vectors E_j in V for every j>=-d by

    E_j=0 for j<0,    E_j=f_j for0<=j<d,
    c_d E_(j+d)=-sum_(h=-d)^(d-1)c_h E_(j+h),   j>=0.      (1)

Since c_d=+/-1, this recursively defines integral vectors and pays the entire left zero boundary.
For n>=d put

    B_n=[E_n E_(n+1) ... E_(n+d-1)],
    beta=(c_1,...,c_d)^T in V.

**Theorem 1.** For every n>=d,

    A_n is isomorphic to V/B_n Z^d,
    [e_j] maps to[E_j] for0<=j<n,
    [b_n] maps to[beta],
    |det B_n|=D_n.                                        (2)

Here e_j denotes the actual standard coordinate vector in Z^n.
Thus the full Gram cokernel needs at most d generators, while the responsible boundary vector is the SAME primitive vector beta at every such n.
No shift action on this quotient is presumed.

**Proof.** Full recurrence(1) says sum_(h=-d)^d c_h E_(j+h)=0 for j>=0.
In V/B_nZ^d, the vectors E_n,...,E_(n+d-1) vanish, as do negative E_j.
Hence for0<=j<n the truncated sum sum_(i=0)^(n-1)c_(i-j)E_i also vanishes.
These are exactly the columns of T_n.
Sending e_j to E_j therefore gives a homomorphism A_n to V/B_nZ^d, surjective because the first d images are a basis.

Conversely in A_n put F_j=[e_j] for0<=j<n and F_j=0 for j<0 or j>=n.
The actual column relations give sum_(h=-d)^d c_h F_(j+h)=0 for0<=j<n.
Starting from F_0,...,F_(d-1), the same unit-leading recurrence determines each F_d,...,F_(n+d-1).
Induction therefore identifies them with the images of E_d,...,E_(n+d-1) under f_i->[e_i].
In particular the right boundary E_n,...,E_(n+d-1) maps to zero, so the inverse homomorphism is well defined.
The two maps are inverse on generators.
The finite cardinality of A_n is D_n, so B_n has full rank and absolute determinant D_n.
Finally b_n has coefficients c_(j+1), which vanish for j>=d; its image is sum_(j=0)^(d-1)c_(j+1)f_j=beta.
This proves every part of(2).

For n<d, the first min(d,n)=n coordinate classes already generate A_n without any reduction.
Thus root's at-most-min(d,n) generator observation holds in all sizes.
It is a cardinality/rank fact about the full group, not yet an estimate on k_n.

<a id="selected-element-index"></a>
## 3. An exact lower-dimensional index measures the missed group part

Because the last coordinate c_d is a unit, beta is primitive in V.
For d>=2 define the integral surjection

    pi_beta:V -> Z^(d-1),
    pi_beta(x)_i=x_i-(c_(i+1)/c_d)x_(d-1), 0<=i<d-1.       (3)

Its kernel is exactly Z beta: the last coordinate determines an integer multiple because c_d=+/-1.
Theorem1 consequently gives

    A_n/<[b_n]> is isomorphic to Z^(d-1)/pi_beta(B_n)Z^d,
    D_n/k_n=[Z^(d-1):pi_beta(B_n)Z^d].                    (4)

This quotient is finite.
In ordinary integer-matrix language, the index on the right is the gcd of all(d-1)-row maximal minors of the explicit(d-1)-by-d matrix pi_beta(B_n).
One can read this either from integer row/column elimination or the already recognized Smith-module interface.
The [Hun74 module audit](../audits/literature/Hun74/Yin_U005.md#hun74-u005) records the invariant-factor classification at its actual scope; no original-source re-audit or stronger theorem estimate is needed here.

For d=1, V/Z beta is zero and(4) has index1; therefore k_n=D_n for every n>=1.
For d>=2, primitivity of beta alone does not make the index1.
This is the explicit missing subgroup cost.
In the cofactor notation of L363 it is exactly the full cofactor gcd g_n=D_n/k_n, now expressed through the complete band-boundary matrix rather than an unspecified primitive scale.

<a id="truncated-shift-failure"></a>
## 4. The natural truncated coordinate shift usually is not an endomorphism

Let S_n e_j=e_(j+1) for j<n-1 and S_n e_(n-1)=0.
For n>=2 define

    u=(c_1,...,c_(n-1),0)^T,
    v=(0,c_(n-1),...,c_1)^T.

A complete entry calculation gives

    S_n T_n-T_n S_n=v e_(n-1)^T-e_0 u^T.                  (5)

All interior entries cancel; the first row and last column are the two finite-boundary defects.
Thus S_n descends to A_n if and only if

    c_h[e_0]=0 for1<=h<=n-1,    and[v]=0 in A_n.          (6)

Indeed T_n S_n already has columns in T_nZ^n; descent is equivalent to the commutator columns belonging there.
For columns j<n-1 those are-c_(j+1)e0; the last column is v.
This is a criterion for the actual finite lattice, not a formal infinite convolution identity.

**Theorem 2.** For n>=d+1, S_n descends to A_n if and only if A_n is trivial.
In particular it never descends for the present nonmonomial monic-unit input.

If S_n descends, (6) includes c_d[e0]=0.
Since c_d=+/-1, [e0]=0.
Its successive induced images are[e1],...,[e_(n-1)], so all classes vanish.
The converse is automatic for a trivial quotient.
To see that the present A_n is nontrivial, finite prediction gives D_n as a product of coefficient residual energies.
The first residual is||P||_2^2>=2, and every subsequent residual is at least M(P)^2>=1 by coefficient Parseval/Jensen and q(0)=1.
Hence D_n>=2.
This uses only the exact finite residual mechanism already read in L4/L359; no quantitative limit is needed.

The theorem concerns S_n with its specified zero right boundary.
It does not rule out a different cyclic or boundary-adjusted map on a particular input.
Such a map must separately preserve the actual relation lattice, as the next control illustrates.

<a id="irreducible-radical-cokernel-control"></a>
## 5. An actual irreducible noncyclotomic family with constant normalizer

Use the already retained family in L9:

    r=2^j, j>=0,
    P_r(t)=t^(2r)-4t^r+1,    d=2r.                        (7)

Its irreducibility is transparent after t->t+1: modulo2 the polynomial becomes t^(2r), and its constant coefficient is-2, not divisible by4.
Eisenstein at2 proves actual degree2r.
Its roots consist of r roots of2+sqrt3 and r roots of2-sqrt3.
They are reciprocal with no circle roots, so these are irreducible reciprocal nontorsion units.
Their COMPLETE total Mahler measure is the fixed2+sqrt3, even as r grows.
This construction and measure statement are known local reuse, not a new near-one family.

The only nonzero autocorrelations are

    c_0=18,    c_r=-8,    c_(2r)=1.

At Gram size n=d=2r, residue classes modulo r give r identical blocks

    H=[[18,-8],[-8,18]],    det H=260.                    (8)

The gcd of its entries is2 and its positive Smith factors are2,130.
This also follows directly by integer Euclidean row/column operations.
Therefore

    A_(2r) is isomorphic to (Z/2 direct-sum Z/130)^r,
    D_(2r)=260^r.                                        (9)

The complete b_(2r) is nonzero only at coordinates r-1 and2r-1; it is(-8,1) in ONE residue block and zero in all the others.
The exact solution is

    H^(-1)(-8,1)^T=(-136,-46)^T/260
                     =(-34/65,-23/130)^T.

Thus its order, and hence the actual minimal predictor normalizer, is

    k_(2r)=130.                                          (10)

This denominator uses both coordinates; cancelling a2 in the second coordinate incorrectly would change it.
In the full predictor the coefficients are

    q_(2r)(t)=1+(34/65)t^r+(23/130)t^(2r),
    Q_(2r)(t)=130+68t^r+23t^(2r).

The active degree<=2r residue chain has three coefficients; all other chains have zero optimizer coefficients.
Multiplication retains the complete product

    P_r Q_(2r)=130-452t^r-119t^(2r)-24t^(3r)+23t^(4r),
    ||P_r Q_(2r)||_2^2=236470,
    r_(2r)=236470/130^2=1819/130.

As a direct determinant check, the three-by-three active block has determinant3638, so D_(2r+1)=3638*260^(r-1) and D_(2r+1)/D_(2r)=3638/260=1819/130.
The full cofactor gcd is consequently

    g_(2r)=D_(2r)/k_(2r)=260^r/130.                       (11)

These are symbolic coefficient and integer-matrix identities, not an executed parameter scan.
They show exponential determinant/cofactor cancellation even for actual irreducible noncyclotomic units.
The individual normalizer stays constant at this degree-scale window.
The conclusion is separate from L363's fixed-input k_n->infinity as n tends to infinity: here the input itself changes with r.

The first-d generator bound is sharp on this actual family.
Modulo2, the entire T_(2r) is zero, so A_(2r)/2A_(2r) is F_2^(2r) and requires exactly2r=d generators.
The missing quotient by[b] has cardinality260^r/130, in agreement with(4), rather than1.

For a small fully written check of the boundary formula, at r=1,d=n=2 one gets

    E_2=(-18,8)^T,    E_3=(-136,46)^T,
    beta=(-8,1)^T,    pi_beta(x0,x1)=x0+8x1.

The projected boundary row is(46,232), of gcd2.
Formula(4) gives D_2/k_2=2, hence k_2=130 exactly.
The group itself is noncyclic of cardinality260.
At the even smaller n=1, the actual group is Z/18 and b_1=-8 has order9; no endomorphism orbit of this b_1 can generate the whole cyclic group, since endomorphisms preserve its even subgroup.
These are distinct window controls and are not conflated.

<a id="justified-cyclic-shift-control"></a>
## 6. Even a genuinely generating shift orbit does not force growing k

On the n=2r control define the CYCLIC shift R e_j=e_(j+1 mod2r), and put X=R^r.
Then X^2=I and the full Gram matrix is

    T_(2r)=18I-8X.

It commutes with R, so this R DOES descend to an automorphism of A_(2r).
The truncated S_(2r) is a different map.
It fails to descend even at this n=d window: applying S to the last-block relation18e_(r-1)-8e_(2r-1) gives18e_r.
In the first block H^(-1)(0,18)^T=(36/65,81/65)^T is not integral, so18e_r is not in the relation lattice.

For the descending cyclic map, the actual boundary vector has the precise form

    b=R^(r-1)(-8+X)e_0.

Moreover

    (18I-8X)(9I+4X)=130I,
    (-8+X)(-8-X)=63I,
    63*97=1+47*130.

Thus130 kills A_(2r), and(-8+X) is invertible on it, with inverse97(-8-X).
R itself is invertible.
Consequently the actual R-orbit of b generates exactly the same group as the R-orbit of e0, namely all of A_(2r).
This is a justified shift-orbit generation theorem on an actual irreducible noncyclotomic family, not an assumed action or an arbitrary group surrogate.

Nevertheless b's INDIVIDUAL additive order is still130 while the group cardinality is260^r and its minimal number of additive generators isd=2r.
Module cyclicity under an operator therefore does not identify an additive element order with the full group size.
Any denominator inference from that module generation must pay the complete orbit length/dimension or additional arithmetic structure.
The example supplies no opposing near-one estimate.

<a id="gram-cokernel-outcome"></a>
## 7. Outcome, obligations and self-check

Root's generator-count scout is now completed by the exact both-boundary presentation(1)--(2).
The actual normalizer is the order of one fixed primitive boundary vector beta, with its missed group part measured exactly by the lower-dimensional index(4).
The natural zero-truncated shift cannot descend at any n>=d+1 for these nontrivial Gram cokernels.
A separately checked cyclic shift can descend and even generate the full cokernel from b, but the irreducible noncyclotomic family(7)--(11) shows that this still allows constant k and exponentially growing determinant at moving degree-scale windows.

This rules out a specific proposed shortcut from raw Toeplitz integrality, at-most-d generators or uncharged shift-orbit generation to a growing unavoidable normalizer.
It does not rule out a theorem using small TOTAL original Mahler measure, actual cofactor-gcd restrictions or a uniform approximation error.
The control has fixed total m=log(2+sqrt3)>0, and individual roots approaching the circle do not make it a near-one sequence.
No uniform gap, near-one coverage, complete cokernel classification for other inputs, or restriction on every conceivable boundary-adjusted operator is asserted.

Author self-check covered full band indices and signs, both zero boundaries, the mutually inverse presentation maps including n=d, primitive beta and quotient index, d=1, the exact commutator and its n>=d+1 threshold, nontrivial determinant proof, actual irreducibility and complete root/Mahler scope of the reused family, residue-block indexing for b and predictor, BOTH reduced denominators, coefficient product/energy and determinant ratio, sharp mod2 generator count, distinction between truncated and cyclic shifts, and the exact operator inverse for the actual b-orbit.
No code, numerical experiment, continued program or J was used.
The complete bounded account is self-checked and ready for noncontributor review.
