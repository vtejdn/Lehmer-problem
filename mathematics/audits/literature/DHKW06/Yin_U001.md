---
author: Yin
---

# Exact sums of polynomial weights over lattice points

<a id="dhkw06-u001"></a>
<a id="sum"></a>
## Evaluating the first weighted sum

Take a convex bounded rational polytope \(K\) given by binary-encoded rational linear inequalities in a fixed number of variables \(n\).
For a fixed-degree integer polynomial \(f\), the integer \(\sum_{a\in K\cap\mathbb Z^n} f(a)\) is computable in time polynomial in the bit length of the inequalities and the coefficients of \(f\).
In Section 3 of the [journal edition](readme.md#edition), Lemma 3.1 applies the operators \(z_i\partial/\partial z_i\) to the lattice-point generating function to insert polynomial weights.
The proof of Lemma 3.3(i) then evaluates the resulting short rational expression at \(\mathbf 1\) by residue evaluation.
This specialization yields the exact sum even though individual rational summands can have poles there.
An empty set of lattice points contributes zero.

The inspection covers the fixed-degree differential-operator argument and the specialization step used for the first moment.
The short rational representation and its polynomial-time residue evaluation enter as the authors' cited algorithms.
The coefficient application uses the first moment of a nonnegative weight, since its sum is positive exactly when the weight is nonzero at some integer point.
