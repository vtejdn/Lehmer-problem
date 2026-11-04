---
author: Yin
---

# LS05: central cocycles and the restricted Salem coding interface

Date: 2026-10-07.
Bounded source inspection for G0001 by assigned AI ms25_source for Yin.
The coordinator registered this source unit after the scoped checks described below.

<a id="ls05-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Elon Lindenstrauss and Klaus Schmidt, *Symbolic representations of nonexpansive group automorphisms*, Israel Journal of Mathematics 149 (2005), 227--266, DOI 10.1007/BF02772542. Retained preprint: arXiv:math/0409257v2, submitted 18 May 2005 09:35:13 UTC; v1 submitted 15 September 2004 18:05:04 UTC. Exact [LS05.pdf](../../../literature/pdf/LS05.pdf), 33 pages, 358400 bytes. No publisher/preprint byte identity is asserted.

Passages: Printed and PDF pages coincide. Central basis and partial fractions (2.15)--(2.18), p.7; coding map (4.4), p.11; positive-time cocycle (4.8)--(4.10), p.12; skew extension (4.15)--(4.17) and Theorem4.13, p.15; Definition4.14 and proof of (1) implies (2), p.16; beta-shift (5.1)--(5.4), p.21; Theorem6.3, p.25.

Inspection: Retained title, authors, arXiv version, page count and hash checked. Extracted text at the listed locators read; retained pages7,12,15,16,25 rendered and visually inspected. The exact positive-time cocycle coordinate and lift-implies-tightness proof were checked. Remaining equivalence in Theorem4.13 and proof of Theorem6.3 were not fully audited; their exact statements are accepted external comparison inputs under their stated hypotheses. No full-paper audit is claimed.


Year, journal, volume, pages and DOI were verified against the author's [institutional publication record](https://cris.huji.ac.il/en/publications/symbolic-representations-of-nonexpansive-group-automorphisms/).
Version dates were checked against the [arXiv record](https://arxiv.org/abs/math/0409257).
The [fixed v2 PDF](https://arxiv.org/pdf/math/0409257v2) was downloaded with normal TLS on 2026-10-07 and retained without overwrite in the verified flat external store.
The initial version-bearing filename was normalized to LS05.pdf without changing bytes; no duplicate remains in the library.
The PDF's 2021 rendering timestamp is not its mathematical version date.

A 34-page author file, coding050329.pdf, supplied the initial locator; it was not retained or adopted.
Every formula below was rechecked in the selected 33-page v2.
No full comparison of these two versions is claimed.

## Exact central coordinate

The source takes R_1=Z[u,u^(-1)] and an irreducible nonhyperbolic, noncyclotomic polynomial f.
The compact group X_f is the dual of R_1/(f), with automorphism alpha_f induced by u.
A monic unit polynomial gives the corresponding toral automorphism.
Write Omega^0 for the unit-circle roots.

For (S w)_l=w_(l+1), the finite-dimensional real central space W_f^0=ker f(S) in l_infinity(Z,R) is spanned by real and imaginary parts of w(omega)_l=omega^l.
The shift is a supremum-norm isometry.
The torus reduction rho is injective on W_f^0, with dense central image.
The extension below uses the noncompact vector-space topology, not a compact quotient of that space.

The partial fractions on p.7 give b_omega/f_m=1/f'(omega).
Thus the central vector in (2.17) is

    w^(Delta0)_l=sum_(omega in Omega^0)
                               omega^(l-1)/f'(omega).

The one-sided Green sequences w^(Delta+) and w^(Delta-) differ by this vector.
The coding map xi_bar^* in (4.4) uses w^(Delta-) for nonnegative digit indices and w^(Delta+) for negative ones.
For n>0, source (4.8) is

    d(n,v)=S^n xi_bar^*(v)-xi_bar^*(S^n v)
          =sum_(j=0)^(n-1) v_j S^(n-j)w^(Delta0).      (1)

Consequently the coefficient of (omega^l)_l is exactly

    omega^(n-1)/f'(omega)
                       sum_(j=0)^(n-1) v_j omega^(-j). (2)

Equation(2) is a direct substitution into the checked source formulas.
It is a rotated digit partial sum, with a nonzero coefficient and no omitted bounded coboundary remainder.
Real vectors have conjugate-paired coefficients.
Only the positive-time branch of (4.8) is used here; no negative-time index check is claimed.

## An invariant central lift requires uniform tightness

The skew extension of (4.16) is

    S_tilde(v,w)=(S v, S w+d(1,v))                     (3)

on l_infinity(Z,Z) x W_f^0.
For a shift-invariant probability nu on the digit space, Theorem4.13 asserts equivalence of:

1. An S_tilde-invariant probability lift with digit marginal nu exists.
2. For every epsilon>0, one compact C_epsilon in W_f^0 contains d(n,v) with probability greater than 1-epsilon for each n in Z.
3. There is a Borel b into W_f^0 such that d(1,v)=b(Sv)-S b(v) for nu-almost every v.

In condition2, the same compact set works at every time; it need not contain all times on one common event.
Definition4.14 calls these measures weakly d-bounded.
Its stronger d-bounded condition requires one compact set containing the whole cocycle orbit almost surely.

The necessary implication1 to2 has an elementary proof on p.16, checked here.
Choose a central ball carrying lift probability greater than 1-epsilon/2.
Invariance makes the initial and time-n endpoint balls overlap with probability greater than 1-epsilon, without independence.
The cocycle identity and the shift isometry then bound ||d(n,v)|| by twice the radius.
The proof of the remaining equivalence uses further cocycle theory and has not been re-audited.

Thus failure of uniform tightness of any coordinate in (2) excludes this source's invariant probability lift.
A probabilistic proof for iid digits is a separate local deduction; the source is not said to state that deduction explicitly.

## The Salem entropy statement restricts both measure and digits

For a Salem number beta>1 with minimal polynomial f, Theorem6.3 assumes that nu is a weakly d-bounded shift-invariant probability on the two-sided beta-shift V_beta.
The corrected Borel map xi_b^* from Theorem4.13 is then countable-to-one nu-almost everywhere; its image mu is alpha_f-invariant, singular to Haar, and

    h_nu(S)=h_mu(alpha_f).                              (4)

This is the entropy of that restricted symbolic law.
It is not an identification of the Shannon rate of unrestricted binary algebraic sums with a toral factor.
The countability, singularity and full entropy proof of Theorem6.3 were not audited here.

Source (5.3)--(5.4) requires every one-sided tail in V_beta to be lexicographically bounded by the distinguished expansion e_beta^* of one.
When 1<beta<2, using the alphabet {0,1} does not remove this restriction.
Choose L such that sum_(j=1)^L beta^(-j)>1.
Admissible one-sided evaluations lie in [0,1], so L consecutive ones form a forbidden block.
Fair binary iid inputs contain that block almost surely by independent disjoint trials, and therefore give V_beta measure zero.
This is a direct applicability check, not exclusion of all binary symbolic laws.

The source consequently supplies an exact central cocycle interface and a restricted entropy theorem.
It does not supply the missing central correction for the original fair binary law, identify its h_1 with (4), or prove a uniform Lehmer gap.
The [hyperbolic bridge](../../../claims/Yin_C_G0303_v1.md#coding-entropy-scope-and-costs) cannot be extended merely by omitting the central condition.
The [c0 obstruction](../../../claims/Yin_C_G0316_v1.md#unit-circle-c0-integer-forcing) does not forbid the source's nondecaying central state.

## Actual search and review boundaries

The title, author and arXiv ID were checked before selecting this single original paper.
A targeted search also located an author survey, which was not selected.
Search stopped after obtaining the exact bridge.
Historical open questions are not reported as verified current status.

The assigned agent checked the source identities, coordinate substitution, lift-implies-tightness proof and beta-shift applicability boundary above.
No whole-paper proof audit, new mathematical computation or source-unit allocation occurred.

The coordinator independently read the complete unit and the retained source text at pp.7,11--12,15--17,21,25, and visually checked pp.7,12,15.
It verified the partial fractions, positive-time coefficient, necessary lift-to-tightness proof, exact theorem hypotheses and beta-shift evaluation bound.
The author institutional and arXiv records were checked directly, and the retained PDF hash was independently matched.
The matrix agent separately inspected retained pp.7,12,15,16,25 and the source shift definition, and independently verified the exact central coordinate, finite-dimensional norm interface and necessary theorem applicability.
Neither check audits the hard converse or the entire entropy-preservation proof.
The assess agent independently checked the local forbidden-all-ones-block argument under the stated tail-evaluation premise, without claiming an original-source reread.

The actual fair-sign and fair-bit failure of tightness is proved in [C G0319](../../../claims/Yin_C_G0319_v1.md#ls05-central-cocycle-iid-interface).
This local result does not turn the source's restricted entropy theorem into a representation for the unrestricted digit law.
