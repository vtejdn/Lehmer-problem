---
author: Yin
---
# Bil97-U001: fixed rational functions on independent small points

Date: 2026-10-18T12:14.
Human record author Yin.
Root proposed the strict/non-strict graph application and the later own-degree consequence.
The angular_envelope_review AI located and directly read the original paper, checked those applications, and used its printed Theorem5.1 for the direct uniform graph argument below.
Both are contributors to this application account; no independent project review is asserted.
These are standard source consequences with complete local applicability checks, not a new equidistribution theorem or an unrestricted Salem gap.

<a id="bil97-u001"></a>
## Read; accepted source statements and fixed-function application

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Yuri Bilu, Limit distribution of small points on algebraic tori, Duke Mathematical Journal89(3) (1997), 465--476; actual published12-page academic-hosted copy, with printed465 at PDF1.

Passages: Printed465--467/PDF1--3: height, orbit measure, strictness, weak topology, Theorem1.1 and Lemma2.1(d). Printed474--475/PDF10--11: torsion-subvariety convention, complete Theorem5.1 and its adjacent attribution/argument.

Inspection: Selected complete statements and conventions text-read; printed465 and474 also visually inspected to resolve the extracted mathematical symbols. The graph, rational-denominator, strict-subsequence, height and own-degree applications now fixed in C852 were checked at that original inspection scope. Theorem1.1's proof in Sections3--4 and the original Zhang/Bombieri--Zannier proofs were not audited; reading the short Section5 consequence is not a source-wide proof audit.


The [retained primary paper](../../../literature/pdf/Bil97--published.pdf) identifies the edition.
Theorem1.1, Lemma2.1(d) and Theorem5.1 are accepted at this precise statement/applicability scope.
The paper explicitly attributes Theorem5.1 to Zhang and discusses the different Bombieri--Zannier proof; neither original paper is newly inspected here.
The bounded search stopped when the retained primary statement supplied the complete needed result.

<a id="strict-small-points-and-orbit-measures"></a>
### Exact definitions and topology

Fix N>=1 and the torus G_m^N over Qbar.
The source's height of x=(x_1,...,x_N) is the absolute logarithmic projective height of(1:x_1:...:x_N):

    H_N(x)=[K:Q]^(-1) sum_v [K_v:Q_v]
                 max(0,log|x_1|_v,...,log|x_N|_v),

for any number field K containing the coordinates and absolute values extending the usual real/complex or p-adic normalization.
In particular max_i h_abs(x_i)<=H_N(x)<=sum_i h_abs(x_i).
For FIXED N, coordinate heights tend to zero if and only if H_N does.
There is no silent rank-uniform statement when N varies.

The full orbit probability measure is

    mu_x=[K:Q]^(-1) sum_(sigma:K->C) delta_(sigma(x)),

including every complex embedding with its actual multiplicity.
Equivalently it is uniform on the distinct joint Galois orbit, because every such point has the same number of extensions to K.
The source defines weak convergence on (C^*)^N by all bounded continuous test functions on that space, not only functions of the angular coordinates.
The limiting nu_N is Haar probability on the compact unit polycircle (S^1)^N, viewed as a measure on (C^*)^N.

A sequence x_k is STRICT if every proper algebraic subgroup of G_m^N contains only finitely many indexed terms x_k.
This includes disconnected and zero-dimensional subgroups and is weaker than avoidance of every proper closed subvariety.
It is not a condition saying that the relations of each point may be ignored when their exponents vary.
Every tuple with multiplicatively independent coordinates belongs to no proper algebraic subgroup, so a sequence of such tuples is automatically strict.
Here independence means product_i x_i^(a_i)=1, a_i integers, only when every a_i=0; it also excludes torsion-valued nontrivial relations by taking a positive power.

Theorem1.1 states that every strict sequence with H_N(x_k)->0 has mu_(x_k) weakly converging to nu_N.
Lemma2.1(d) says that if all measures in a weakly convergent sequence are supported on one fixed closed subset, their limit is supported there as well.
Only bounded continuous tests, or that fixed-closed-set consequence, are used below; no passage to a singular logarithmic test is assumed.

<a id="torus-bogomolov-complement"></a>
### Exact Bogomolov complement in Theorem5.1

A torsion subvariety in the source is a translate zeta H of a subtorus H by a torsion point zeta.
The trivial zero-dimensional subtorus is allowed, so torsion points themselves are included.
For a Zariski-closed X in G_m^N, define X^* by removing the union of ALL torsion subvarieties contained in X, including zero-dimensional ones and X itself if X is a torsion translate.
The theorem does not assume that X is irreducible.
Its conclusions are that X has finitely many maximal torsion subvarieties and that, whenever X^* is nonempty,

    eta_X=inf_(z in X^*) H_N(z)>0.                    (1)

This is an absolute tuple-height bound, with a constant depending on the fixed X.
No effective numerical value or uniformity over varying X or N is supplied by this selected theorem.

## Project applications and their fixed homes

The complete fixed-rational-function graph, strict/non-strict alternative, height, own-degree/measure and Salem deductions are retained in [C852](../../../claims/Yin_C_G0852_v1.md#statement).
The actual original [R392 finding](../../reviews/Yin_R_G0392_v1.md#fixed-function-applicability-finding) retains its source-versus-project scope; moving the unchanged argument supplies no new proof inspection or mathematical adoption.
The source statements, definitions, edition and original-proof limits above remain the external input.
