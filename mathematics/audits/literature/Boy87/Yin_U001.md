---
author: Yin
---

# Degree of a reciprocal algebraic integer's Mahler measure

<a id="boy87-u001"></a>
## The orbit of the exterior conjugates

In §1 of the [published edition](readme.md#edition), printed pages 3–4, Boyd takes a reciprocal algebraic integer of degree \(2h\) with \(\nu\le h\) conjugates outside the unit circle.
Let \(E\) be the set of those conjugates, \(G\) the rational splitting group, and \(u=\pm1\) the sign for which \(M(\alpha)=u\prod_{z\in E}z\).
Immediately before Proposition 1, Boyd proves that
\[
  [\mathbb Q(M(\alpha)):\mathbb Q]=|G\cdot E|.
\]
Among the subsets of size \(\nu\), \(E\) uniquely maximizes the modulus of the product, since every replaced exterior root has modulus greater than one and every replacement has modulus at most one.
The product map on the orbit is equivariant, so all its fibers have the same size as the singleton fiber over \(M(\alpha)\) after multiplication by \(u\).

Boyd also places \(G\) in the signed permutation group on the \(h\) inverse pairs.
Consequently every image of \(E\) chooses \(\nu\) pairs and one member of each, giving the upper bound \(2^\nu\binom h\nu\).
Equality requires transitivity on those choices.
For instance, Boyd's dihedral construction in §2, Theorem 1 on printed page 5, has \(\nu=h-1\) and measure degree dividing the odd integer \(h\).

The [degree calculation for the cubic specialization](../../../ledger/Yin_L_G0462_v183.md#orbits) supplies its own transitivity over \(\mathbb Q^{\rm ab}\) and independence across distinct factors.
In its notation \(h=n_i\) and \(\nu=\ell_i<n_i\), so an unused pair can absorb a parity correction and all orientations of the chosen \(\ell_i\) pairs occur.
For \(\ell_i=n_i\), even flips and alternating permutations preserve sign parity and give two orbits of orientations.
Boyd's orbit identity itself holds at this endpoint as well.
This inspection verifies the selected orbit proof and its hypotheses against printed pages 3–4 and checks the contrasting theorem statement and exterior count on page 5.
