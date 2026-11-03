---
author: Yin
---

# G0001: girth, simple cycles and exact neutral-spectrum deletion

The complete current mathematical home is [Yin_C_G0268_v1](../claims/Yin_C_G0268_v1.md#argument), adopted at 2026-10-21T06:39 after the [actual complete current self-check](../audits/reviews/Yin_R_G0532_v1.md#current-complete-exact-deletion-finding).
The original2026-10-07 mathematics and still-needed fixed review input below retain their original scope and date; this is no new research run.


Date: 2026-10-07.
Proof draft and authoring-agent self-review by assigned AI review_matrix_completion for Yin.
The coordinator requested a graph criterion beyond the equitable quotient of [L G0046](Yin_L_G0046_v1.md), using the essential repairs in [L G0039](Yin_L_G0039_v1.md#degree22-small-core-counterexample) and [L G0045](Yin_L_G0045_v1.md#sharp-degree34-control).
No new external source or computation is used.
The only external existence input is the previously accepted [KOR00 statement](../audits/literature/KOR00/readme.md#nettrace-scope), whose original proof remains unreviewed.

The main additional graph information is exact in the interval below twice the girth.
In this interval, every primitive orbit is a simple cycle.
This gives a finite necessary and sufficient deletion test, a simple-cycle budget at fixed edge excess, and an explicit obstruction to deleting the whole bounded-base blocks of [L G0044](Yin_L_G0044_v1.md).
It does not provide a realization with bounded edge excess.

<a id="exact-spectral-deletion"></a>
## Exact meaning of deletion

Let A be a primitive nonnegative integer adjacency matrix with Perron root lambda>1.
Parallel edges are separately labelled, loops are allowed, and row adjacency is used.
Write

    chi_A(t)=t^z q(t),       q(0)!=0,
    e=sum_ij A_ij-dim A.

Let g be the length of a shortest nonempty directed closed walk, equivalently a shortest directed simple cycle.
Let C_n be the number of directed simple cycles of length n, counted up to cyclic rotation and retaining parallel-edge labels.
For any monic polynomial f with nonzero roots alpha_i, put

    b_n(f)=(1/n) sum_(j|n) mu(n/j) sum_i alpha_i^j.

As in L G0034, b_n(q) counts primitive directed periodic orbits of length n, and is a nonnegative integer.
Zero eigenvalues make no contribution.

A cyclotomic divisor d of q is called deletable here if some nonnegative integer matrix B has nonzero characteristic polynomial q/d; arbitrary additional zero eigenvalues are permitted, but no new cyclotomic factors are added.
This concerns exact nonzero spectra.
It does not assert a quotient, a local surgery, a common dimension, an integral conjugacy, or an edge-excess bound.

Write

    d=product_m Phi_m^(h_m),       h_m>=0,
    f_n=b_n(d)=sum_(m: n|m) mu(m/n)h_m.               (1)

Then the following are equivalent:

1. d is deletable in the stated sense.
2. There is such a B which is primitive.
3. For every n>=1, f_n<=b_n(q).

Necessity is the nonnegativity of primitive-orbit counts for any nonnegative integer B.
For sufficiency, q/d is monic integral and has nonzero constant coefficient.
Deleting roots of unity leaves lambda as a positive simple strictly dominant root.
Its normalized net traces are b_n(q)-f_n>=0; multiplying by n gives exactly the unnormalized net traces in KOR00.
That accepted theorem supplies a primitive B with the specified nonzero spectrum and possible zero padding.
Only indices dividing an order appearing in d need to be tested, because f_n=0 elsewhere.
Formula (1) and its integrality are the Euler-coordinate identity of [L G0039](Yin_L_G0039_v1.md).

This equivalence shows why failure of one equitable partition is insufficient to prove an obstruction, but a negative net trace rules out every nonnegative integer realization of the proposed reduced spectrum.
It also shows why adding a replacement repair would change the question.

<a id="simple-cycle-budget"></a>
## The simple-cycle interval and its budget

For every n<2g,

    b_n(q)=C_n,                                      (2)

where C_n=0 for n<g.
Indeed, a closed walk which repeats a vertex other than the identified initial/final vertex splits there into two nonempty closed walks.
Each has length at least g, so the original length is at least 2g.
Therefore every closed walk of length less than 2g is a simple cycle.
A simple cycle is primitive and has exactly n based versions, including the edge labels.
This proves (2), including loops and parallel edges.

There is also the global bound

    sum_n C_n <= product_v outdeg(v) <= 2^e.          (3)

For the first inequality, fix a simple cycle C.
Since the graph is strongly connected, every vertex has a path to C.
At a vertex outside C choose one outgoing edge that decreases the shortest-path distance to C, and on C choose its prescribed outgoing cycle edge.
The resulting choice of one edge at every vertex has C as its unique directed cycle.
Choices produced for different C cannot coincide, because their unique cycles differ.
There are exactly product_v outdeg(v) possible choices.
Every outgoing degree is a positive integer, and a<=2^(a-1) for a>=1.
Multiplication proves the second inequality since sum_v(outdeg(v)-1)=e.

The bound is on simple cycles, not on all primitive periodic orbits at arbitrary lengths.
In the branch-return description of [L G0041](Yin_L_G0041_v1.md#branch-return-budget), the degree-one vertices contribute factors one to the product in (3).
Thus the same bound is controlled by the bounded number and total multiplicity of branching choices; it is insensitive to long delays.

<a id="girth-window-deletion"></a>
## A complete test for factors of order below twice the girth

Suppose every m with h_m>0 satisfies m<2g.
Then d is deletable if and only if

    sum_(m: n|m) mu(m/n)h_m <= 0       for 1<=n<g,
    h_n <= C_n                        for g<=n<2g.   (4)

For n>=2g the correction vanishes.
For g<=n<2g the only multiple of n which is less than 2g is n itself, so f_n=h_n.
For n<g, (2) gives b_n(q)=0.
The exact criterion above now proves (4).

Several consequences follow without a search over presentations.

* If all the orders in a nonconstant d are less than g, d cannot be deleted.
  Take its largest order m: f_m=h_m>0 but b_m(q)=0.
  More generally, this applies to any nonempty subcollection of neutral factors whose orders all lie below g.
* For a single Phi_m with m<2g, deletion is possible precisely when m is a prime power, or m=1, and C_m>=1.
  If m has at least two distinct prime divisors p and r, its correction at n=m/(pr) is +1.
  This index is less than g, so deletion is impossible.
  For m=p^a the only corrections are +1 at m and -1 at m/p, and m/p<g; the criterion reduces to C_m>=1.
  For m=1 there is only the correction +1 at 1, giving the same cycle test.
  Multiplicities of a single eligible factor are bounded by C_m.
* Individual factors need not have the same deletion behavior as their product.
  For example, the positive correction at a short divisor which blocks Phi_m may be cancelled by other cyclotomic factors.
  The cycle product t^m-1 has only the correction f_m=1.
  Whenever it divides q, it is deletable exactly when b_m(q)>=1, and in the interval m<2g this is exactly C_m>=1.

There is an exact cycle-polynomial description of every d passing (4):

    d(t) = product_(g<=n<2g)(t^n-1)^(h_n)
           / product_(1<=n<g)(t^n-1)^(-f_n).         (5)

All displayed exponents are nonnegative integers, with h_n<=C_n.
This is the finite Euler identity for a cyclotomic product; it is an equality of rational functions, whose value is the already specified polynomial d.
Thus each such deletion spends at most one unit of its available simple-cycle count for each positive high-index correction, while its remaining corrections occur at shorter indices with nonpositive sign.
It follows that

    deg d = sum_n n f_n
          <= sum_(g<=n<2g) n h_n
          <= sum_(g<=n<2g) n C_n
          <= (2g-1) product_v outdeg(v)
          <= (2g-1)2^e.                              (6)

This is a bound on deletable neutral degree in a specified relative-order window.
Its dependence on g is explicit.
It is not a bound on all neutral degrees, all orders, or all essential repair budgets at fixed e.

<a id="whole-block-first-obstruction"></a>
## Applying the criterion to an entire arithmetic block

For the block d(t)=Phi_b(t^h), with positive integers b,h, the finite rational identity gives

    d(t)=product_(j|b)(t^(hj)-1)^(mu(b/j)).           (7)

Its correction is therefore mu(b/j) at n=hj for j|b and zero at other indices.
This statement does not require b to be squarefree.
Let rad(b) be the product of its distinct prime divisors and omega(b) their number.
The least index with a positive correction is

    n_+ = h b/rad(b),                     if omega(b) is even,
    n_+ = h b p_min/rad(b),               if omega(b) is odd, (8)

where p_min is the least prime divisor of b; b=1 belongs to the even case and gives n_+=h.
To verify (8), the positive corrections correspond to squarefree divisors b/j with an even number of prime factors.
Their largest product is rad(b) when omega(b) is even, and rad(b)/p_min otherwise.

Consequently, if this whole block divides q and n_+<g, it cannot be deleted into any nonnegative integer realization.
If hb<2g, its deletion is completely decided by checking that every positive-correction index hj satisfies C_(hj)>=1.
Negative corrections impose no further constraint.
This specializes (2) and the exact spectral criterion, without estimating a new graph.

The blocks produced in L G0044 have squarefree bounded b and potentially unbounded h.
For them (8) becomes n_+=h for even omega(b), and n_+=h p_min for odd omega(b).
Thus scalar divisibility of the entire block can fail the positivity test even before questions of coefficient growth or same-excess graph surgery arise.
This does not show that such a failure occurs in every admissible large-order family.
It supplies a concrete graph-orbit test that any proposed deletion must pass.

## Existing controls and the unresolved quantitative bridge

For the degree-22 core in L G0039, q=Phi_6 p has girth seven.
Since 6<7, no nontrivial cyclotomic divisor of q can be deleted.
In particular p has a negative normalized net trace at six and at one, so it has no nonnegative integer realization with only zero padding.
The obstruction concerns all positive realizations, not merely the equitable partitions of that particular graph.

For the degree-34 core in L G0045, q=Phi_10 Phi_12 p has girth thirteen.
Each nonempty subproduct of the two neutral factors has largest order below thirteen, so none is deletable.
This proves inclusion-minimality of that neutral padding directly from girth.
The stronger unique minimum-degree repair statement remains the separately proved result of L G0045; no new minimum-repair conclusion is inferred here.

For the twin-cycle family in L G0046 the girth is n and there are two simple n-cycles.
The neutral divisor t^n-1 has correction +1 only at n.
It therefore passes the spectral test, consistently with the explicit equitable quotient of that material.
That quotient additionally controls edge excess, which KOR00 alone does not do.
No conflict arises between essential low relative orders in the first two examples and redundant unbounded orders in the third.

At bounded edge excess there are at most 2^e simple cycles, but their lengths, the girth and the delays in the return matrix may grow.
The present result does not exclude large essential orders or yield an unbounded essential-order example in the small reciprocal irreducible class.
Nor does passing (4) construct a same-excess presentation: KOR00 may introduce uncontrolled dimension, zero multiplicity and edge count.
The next additional input would have to turn the finite cycle allocation in (5) into an actual positive operation with a controlled graph budget, or exhibit an eligible family whose required positive corrections occur before all available cycles.
Full algebraic entropy is preserved whenever deletion is achieved, since the deleted roots are roots of unity; the Perron logarithm alone is not substituted for that entropy.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0012_v1.md#review-boundary), with its original inspected scope and relationship.
