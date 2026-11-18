---
author: Yin
---

# Quadratic sequences on a fixed arithmetic progression

<a id="tao10-u001"></a>
## Character criterion and one differencing step

The [author's HTML edition](readme.md#edition), Section 1, gives the [character criterion in Proposition 1](../../../literature/pdf/Tao10/equidistribution-20100328.html#weyl), the [linear test in Exercise 5](../../../literature/pdf/Tao10/equidistribution-20100328.html#equiva), and [Corollary 5 on differences](../../../literature/pdf/Tao10/equidistribution-20100328.html#vdc-eq).
Corollary 6, immediately following Remark 2, gives the polynomial result on the integer line.
I checked these passages for the positive-index quadratic application and the order of limits in the differencing proof.

Let \(x(v)=u v^2+w v+b\) in \(\mathbb R^h/\mathbb Z^h\), with \(n\cdot u\) irrational for every nonzero \(n\in\mathbb Z^h\).
For a fixed positive lag \(t\), the difference of the phase \(n\cdot x(v)\) has linear coefficient \(2t(n\cdot u)\), so its character average tends to zero by the geometric sum.
Corollary 5 on positive indices takes the long-sample limit with a fixed number of shifts, then lets that number grow.
Proposition 1 turns the resulting vanishing of every nontrivial character average into Haar equidistribution.
Replacing the index by \(v_0+Mv\), \(M\ge1\), multiplies the quadratic coefficient by \(M^2\), preserving this hypothesis.
Thus each nonempty open box is visited infinitely often for every fixed such progression.

In the [square-constant inverse](../../../ledger/Yin_L_G0462_v170.md#squares), rational independence of \(1,e_1,\ldots,e_h\) gives the required irrational scalar coefficients at each fixed Salem input.
The application allows the lower degree cutoff to depend on that input and on the chosen box.
The inspected qualitative argument supplies no common cutoff as these data vary.
