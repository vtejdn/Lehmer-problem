---
author: Yin
---
# Gent21-U001: the normalized square norm of algebraic integers

Date: 2026-10-18T12:59.
Human record author Yin.
Root supplied the source lead after independently finding a finite convex-variance argument.
The entropy_attainment_bridge AI inspects only the selected source definitions and elementary results below.
This is not an audit of the paper's main capacity, algorithmic or enumeration theorems.

<a id="gent21-u001"></a>
## Audited within scope: normalized square norm and the strict indecomposability threshold

## Source and inspection

[Source and edition notes](readme.md).

Source edition: D. M. H. van Gent, Indecomposable algebraic integers, arXiv:2111.00499v1; side stamp31October2021, manuscript date2November2021; 43 pages, with printed and PDF page numbers equal.

Passages: Definition3.1 on page5; Definition4.1 and Lemma4.3 on page8; Lemma4.4 on pages8--9; Lemma7.2 and Definitions7.3,7.6 on page14; Lemma7.7, Proposition7.8, Theorem7.9 and Remark7.10 on pages14--15; Proposition8.1 on page16.

Inspection: Direct retained-primary text reading of these statements and their displayed elementary proofs; visual inspection of pages8,14,15,16. The page9 continuation of Lemma4.4 was text-read. The AMGM and Kronecker external inputs retain the boundaries below; no complete-paper or original Kronecker-proof audit.


The exact [retained v1 source](../../../literature/pdf/Gent21--arxiv-v1.pdf) and its [contents](../../../literature/contents/Gent21--arxiv-v1.md) identify the inspected version.
No later edition or publication is substituted for this identified version.

<a id="normalized-algebraic-square-norm"></a>
### Definitions and field normalization

Write Qbar for an algebraic closure of Q and Zbar for its ring of algebraic integers.
For z in Qbar, the source's normalized absolute norm and square norm are

    N(z)=abs(Norm_(Q(z)/Q)(z))^(1/[Q(z):Q]),
    q(z)=(1/[Q(z):Q]) sum_(sigma:Q(z)->C)|sigma(z)|^2.

Set N(0)=q(0)=0.
The symbol q is a squared Euclidean norm, not a logarithmic height or Mahler measure.
For any finite number field K containing z, both formulas may instead be averaged over ALL embeddings of K, with denominator [K:Q].
This is Lemma7.2: every embedding of Q(z) has exactly [K:Q(z)] extensions, so the repeated fibers cancel exactly.
In particular a common finite Galois field can be used without changing q or N.

For x,y in Qbar and any finite K containing them, Remark7.10 gives

    <x,y>=(1/[K:Q]) sum_(sigma:K->C)
                        sigma(x) conjugate(sigma(y)).

This is a positive definite REAL Q-bilinear inner product: embeddings pair under complex conjugation, and the expression is independent of K by the same constant-fiber argument.
Its square norm is q(x)=<x,x>, and the parallelogram identity follows by summing the complex scalar identity, as in Lemma7.4.
Multiplication by -1 and Galois conjugation preserve q directly by the formula.
No infinite-dimensional Hilbert-space completion is needed for the finite conjugate calculations that motivate this unit.

<a id="algebraic-square-norm-minimum"></a>
### Complete elementary lower bound

Lemma7.7 applies AMGM to the squared absolute conjugates and gives

    q(z)>=N(z)^2,

with equality exactly when all absolute conjugates of z are equal; the source calls this property uniform in Definition7.6.
For every NONZERO algebraic integer z, its own field norm is a nonzero rational integer.
Therefore

    q(z)>=abs(Norm_(Q(z)/Q)(z))^(2/[Q(z):Q])>=1.   (1)

This verifies the whole proof of the lower bound needed for z and for differences of distinct algebraic integers.
It requires neither that z be a unit nor that it be nontorsion.
The elementary finite AMGM inequality is used as such; no proof from the source's separate analysis reference is required.

Proposition7.8 additionally identifies the equality range: for algebraic-integer z, q(z)<=1 precisely when z=0 or z is a root of unity.
For nonzero z, (1) and equality in AMGM force every conjugate to have modulus1; the source then invokes Kronecker's theorem.
That last classification uses the already retained [Smy08 Kronecker normalization input](../Smy08/Yin_U001.md#smy08-height-normalization) at its actual accepted source scope.
No original Kronecker proof is re-audited here, and the classification is not needed for (1).
Theorem7.9 summarizes that Zbar with q is a Hilbert lattice with minimum square norm1, attained by1.
The convention P(Lambda)=inf{q(v):0!=v in Lambda} is the one in Definition3.1 on page5; the recall immediately before Theorem7.9 on page15 drops the inf symbol typographically.
The theorem and its proof use the scalar infimum, not the displayed set in that recall.

<a id="algebraic-indecomposability"></a>
### Indecomposability and the exact threshold

Definition4.1 calls a pair (b,c) a decomposition of a lattice element a when a=b+c and <b,c>>=0.
It is trivial if b=0 or c=0.
A nonzero element is indecomposable when it has only these two trivial ordered decompositions.
This is an inner-product condition; it does not mean the absence of all additive identities.

Lemma4.3 rewrites the condition as q(b)+q(c)<=q(a), using q(a)=q(b)+q(c)+2<b,c>.
Lemma4.4 then proves that 0<q(a)<2P(Lambda) implies indecomposability: a nontrivial decomposition would have q(a)>=q(b)+q(c)>=2P(Lambda).
The source also permits equality q(a)=2P(Lambda) when the infimum P(Lambda) is not attained; that extra case is irrelevant for Zbar, where the minimum1 is attained.

Thus the strict part of Proposition8.1 says

    a in Zbar, 0<q(a)<2 => a is indecomposable.     (2)

The entire short proof of (2) is covered by the preceding checks.
At q(a)=2 the same proposition says that a is decomposable exactly when it is a sum of two roots of unity; such a pair is orthogonal, unique up to order, and each member has degree at most2 over Q(a).
Its printed proof uses the equality classification in Proposition7.8 and the elementary fact that two unit vectors with a fixed nonzero sum are determined up to interchange.
That endpoint was read and checked at these stated dependencies; it is not used to replace the STRICT condition in (2).

### Applicability and attribution boundary

The selected definitions, (1) and (2) are accepted source inputs at the exact proof depth just recorded.
For any finite set of algebraic integers in one field, their nonzero differences satisfy (1), and all conjugates of a fixed input have identical q.
These facts provide the classical normalized-lattice context for the project's bounded convex-combination inquiry.
The selected passages do NOT state the exact arbitrary rational convex-hull assertion being developed by root and loglog_cyclic_review; that finite variance deduction must be retained and credited in its own responsible project account.
Indecomposability by itself is not silently redefined as a convex-hull classification.
No automatic nonzero integral point, original Mahler gap, independent review of a contributed project proof, or novelty claim is supplied by this unit.

<a id="original-conjugate-combination-reviewer-reading"></a>
## Original complete conjugate-combination reviewer reading

Retention recorded 2026-10-21T23:58.
The original [R_G395 whole reviewer](../../reviews/Yin_R_G0395_v1.md#conjugate-combination-whole-independent-finding), distinct from entropy_attainment_bridge's source-author inspection and root's lead, directly text-read the retained identified Gent21 primary pages14--16 for the normalized square norm, constant common-field fibers, nonzero-integral AMGM lower bound and related strict q<2 threshold.
That original occurrence is stated in R_G395's actual complete account; it is separate from that source author's broader selected-definition and visual pages8,14,15,16 inspection.
No separate individual source-reading minute is supplied.
The2026-10-18T13:05 R_G395 whole finding and21:00 L399 document date are different events and do not create such a minute.
The reading concerns these exact normalized-norm and elementary interfaces; it is no complete-paper, main capacity/algorithm/enumeration or original Kronecker-proof audit.
The local hull and quantitative logarithmic deductions remain local proofs, rather than an external theorem copied from the strict indecomposability statement.
The original whole review arrangement remains UNKNOWN for its actual earlier target-context boundary; this source reading is neither erased by that uncertainty nor a certificate of isolation.
The present construction read the adequate existing U and recorded this preserved occurrence; it claims no new PDF reading, acquisition or source version.
