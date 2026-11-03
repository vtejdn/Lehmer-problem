---
author: Yin
---
# Rum13-U001: exact compact-set Fekete–Szegö input and local discs

Date: 2026-10-20T11:48.
Human record author Yin.
The delegated source reader performed this selected primary-source inspection for the residual-singleton existence inquiry.
Root supplied the proposed application and the simpler finite-bad-place disc construction.
This is author-side source work, not independent review of a project existence proof.

<a id="rum13-u001"></a>
## Read; the stated external input is accepted with its actual proof-inspection limit

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Robert Rumely, The Fekete–Szegö Theorem with Local Rationality Conditions on Algebraic Curves, arXiv:1203.1213v1, 6 March 2012, 451-page early author manuscript. The bibliography key Rum13 identifies the same-work 2013 book family; this inspection is of the explicitly earlier manuscript, not the published book.

Passages: Definitions 0.1–0.2 and Theorem 0.3, printed vi/PDF 6; capacity conventions and variants, printed 1–10/PDF 23–32, especially Theorem 1.6 printed 6–7/PDF 28–29; basic assumptions printed 62–63/PDF 84–85; Definition 3.8 and Theorem 3.9 with its displayed proof, printed 70–72/PDF 92–94; canonical-distance comparison printed 74–75/PDF 96–97, equations (3.22)–(3.27); single-pole energy, nonpolarity and Green conventions printed 77–81/PDF 99–103, and Lemma 3.21 with its complete displayed proof printed 81–82/PDF 103–104.

Inspection: Direct text reading of these named statements, conventions and displayed local-parametrization and monotonicity proofs. The long global and local patching proof of the Fekete–Szegö theorem was not reviewed. Theorem 3.9's existence of parametrizations, the canonical-distance comparison, and Green-function properties and monotonicity retain the earlier capacity theory cited by this primary source; those ancestor proofs were not independently audited.


The [actual manuscript](../../../literature/pdf/Rum13--arxiv-v1.pdf) and [complete supplied contents](../../../literature/contents/Rum13--arxiv-v1.md) identify the inspected edition.
The author's official publication page explicitly describes this manuscript as an early draft of the published book.
No statement-by-statement equivalence with the unavailable 2013 edition is asserted.
In particular, the primary theorem below is the early manuscript's actual Theorem 1.6, not an inference from QY26's citation of the published theorem number.

<a id="compatible-berkovich-adelic-set"></a>
## Definition: compatible Berkovich adelic set

Let K be a global field, C/K a smooth geometrically integral projective curve, and X a nonempty finite Galois-stable set of geometric points in C(Kbar).
For a nonarchimedean place v, C_v^an here is the Berkovich curve over the completed algebraic closure C_v; at an archimedean place it is the complex Riemann surface.
Choose a projective embedding and its closure model over the valuation ring.
A local compact set E_v is X-trivial when the model has good reduction, the geometric points of X have distinct specializations, and E_v consists of all analytic points whose specialization avoids those specializations.
Equivalently, it is the Berkovich closure of the classical complement of the open spherical balls B(x,1)^− around x in X.

A compact Berkovich adelic set E=(E_v)_v compatible with X has each E_v compact, nonpolar and disjoint from X, and has E_v X-trivial for all but finitely many v.
Nonpolar means positive local capacity.
The set is K-rational when each E_v is stable under all continuous automorphisms of C_v fixing K_v.
This stability is a condition on the complete local set, not a requirement that every disc center be K_v-rational.
The classical compatibility convention additionally describes the local sets as bounded away from X; compactness and disjointness give that separation in the compact Berkovich formulation.

<a id="cantor-capacity-normalization"></a>
## Definition and normalization: Cantor capacity

Choose a finite normal extension L/K over which all points x_1,...,x_m of X are rational and the source's fixed global uniformizing parameters at those points.
The local Green matrix has diagonal entries the single-pole Robin constants and off-diagonal entries the Green functions evaluated at the other pole.
In the classical convention the global matrix is [L:K]^(-1) times the sum over all places w of L of Gamma(E_w,X) log(q_w), exactly as on printed page 2.
In the Berkovich convention of printed page 6 the nonarchimedean factor log(q_w) is already absorbed into the local Green functions and is omitted from those terms of the sum.
Archimedean factors retain the source's normalized absolute values and place conventions.
These are two matching normalizations, not permission to omit a place or degree weight.
All but finitely many local matrices vanish for the compatible X-trivial sets with the fixed global parameters.
The product formula makes the global matrix independent of a change of those global uniformizers, and the normalized sum is independent of the chosen splitting extension.

For a real m by m matrix Gamma and the probability simplex P^m, write

\[
 \operatorname{val}(\Gamma)=\sup_{s\in P^m}\inf_{r\in P^m}s^{T}\Gamma r,
 \qquad \gamma(E,X)=\exp(-\operatorname{val}(\Gamma(E,X))).
\]

The source's global Green matrix is symmetric and Galois-stable.
Its off-diagonal entries are nonnegative; finite local energies on the nonpolar compact sets give finite matrix entries.
The [QY26 closed-point convention](../QY26/Yin_U002.md#closed-point-cantor-capacity) uses Galois orbit averages of this geometric-point matrix.
That convention and its normalization must be matched in any application; this source unit does not substitute an unweighted sum of arbitrary local capacities.

<a id="compact-set-fekete-szego-lrc"></a>
## Exact external theorem: early-manuscript Theorem 1.6

Let K,C,X,E be as in the compatible-set definition, with E K-rational.
Let S be a finite set of places containing every archimedean place and such that E_v is X-trivial outside S.
Assume gamma(E,X)>1.
At every v in S impose the following additional local forms.

1. If K_v is complex, E_v is a finite union of compact sets, each the closure of its complex interior and with piecewise smooth boundary.
2. If K_v is real, E_v is conjugation-stable and a finite union of pieces, each either a set of the preceding complex type or a compact connected subset of C_v(R).
3. If v is nonarchimedean, E_v is stable under Aut_c(C_v/K_v) and is a finite union of pieces, each either a strict closed Berkovich affinoid, or a compact classical set of the form C_v(F_w) intersect B(a,r) for a finite separable extension F_w/K_v.

Then infinitely many alpha in C(K^sep) have all their global K-conjugates in E_v for every place v.
This conclusion is containment in E itself.
No neighborhood enlargement is required in this version.
The theorem does not require all geometric poles in X to be real.
The entire local set must still be compact and nonpolar, and strict supercritical capacity is required.

Theorem 1.6 is accepted here as an established external theorem at its exact stated scope.
Its lengthy patching proof is not independently checked in this record.
The early manuscript's introductory Theorem 0.3 explicitly includes finite unions of closed balls among the permitted nonarchimedean classical sets; Theorem 1.6 provides the compact Berkovich version used here.
Theorems 1.2–1.3 were also read to distinguish neighborhood and interior variants, but this unit's selected existence input is Theorem 1.6.

<a id="small-local-disc-interface"></a>
## Local disc and kernel interfaces

Definition 3.8 calls an open spherical ball isometrically parametrizable if a convergent power-series map from an open disc is an onto isometry in an affine patch.
A closed ball is so parametrizable when it lies in a larger such open ball.
Theorem 3.9 says that for every nonarchimedean v there is R_v>0, depending on the fixed projective embedding, such that every open ball of radius at most R_v is isometrically parametrizable.
For good reduction R_v may be taken to be 1.
If the chosen center belongs to C(F_w), where F_w is a complete extension of K_v in C_v, the parametrization can be chosen over F_w.
The theorem also identifies the points over any further complete extension through that parametrization.
The additional displayed isometry and field-of-definition proof was read in full; the theorem's original existence input is explicitly attributed there to Rumely's earlier capacity monograph.

For the intended finite-place application this permits a positive-radius closed disc strictly inside a sufficiently small analytic coordinate neighborhood of an algebraic local point.
A radius in the local algebraic value group gives the strict closed-disc form in Theorem 1.6(C1).
A finite union of its local Galois conjugates can satisfy the required setwise invariance.
The consuming proof must still establish that all its specified rational coordinates have absolute value at most 1 on those discs and that the discs avoid X.
The source theorem does not itself construct the residual curve's local points.

Equations (3.22)–(3.23) write the canonical kernel as

\[
 [z,w]_a=\frac{((z,w))_v}{((z,a))_v((w,a))_v},
 \qquad C_v^{-1}\|z,w\|_v\le ((z,w))_v\le C_v\|z,w\|_v .
\]

On the archimedean surface this compares it, up to fixed positive bounded factors, to the metric
\[
 \rho_a(z,w)=\frac{\|z,w\|_v}{\|z,a\|_v\|w,a\|_v}.
\]
The metric assertion is stated on printed page 75 with its earlier construction referenced there.
For fixed b different from a, rho_a(b,z) tends to infinity as z tends to a.
Changing the chosen single-pole normalization multiplies the kernel and its capacity by a fixed positive constant; it does not change this divergence.
The earlier proof of the metric and canonical-distance comparison was not re-audited.
The [selected QY26 arc argument](../QY26/Yin_U002.md#arc-capacity-and-exhaustion) records the actual lower bound needed from this interface.

<a id="single-pole-robin-and-green-monotonicity"></a>
## Definition and accepted interface: single-pole Robin constant and Green function

For a compact set H disjoint from a pole a, fix the source's uniformizer-normalized canonical distance [z,w]_a.
For probability measures nu on H set I_a(nu)=integral integral -log_v([z,w]_a) dnu(z)dnu(w), V_a(H)=inf_nu I_a(nu), and gamma_a(H)=q_v^(-V_a(H)).
The normalized natural-log convention replaces V_a by V_a log(q_v) and writes gamma_a=exp(-V_a).
The archimedean formulas used for the real arcs below use this natural-log convention.
The empty set has Robin constant infinity.
A compact set is nonpolar when one such probability measure has finite energy; this property is independent of the pole outside the set.
Printed page 79 states positive inner capacity for a set containing a nonempty local analytic open set, a nonempty open subset of C_v(F_w) for a finite local extension, or a nondegenerate archimedean continuum.
Consequently an actual positive-radius small disc supplies a nonpolar set, whereas a finite collection of centers alone does not.

For nonpolar compact H let mu_(H,a) be its equilibrium probability measure and let u_H(z,a)=integral -log_v([z,w]_a) dmu_(H,a)(w).
The source's Green function is G(z,a;H)=V_a(H)-u_H(z,a).
The existence and uniqueness of the equilibrium measure are retained external facts cited on printed page 80, not new project proofs.
Proposition 3.20 states G>=0, continuity away from H and the pole, and vanishing on a union of archimedean continua.
Equation (3.36) recovers V_a from G by subtracting its normalized pole singularity.
For H contained in H' with the pole outside H', Lemma 3.21 gives G(z,a;H)>=G(z,a;H') for every z.
The displayed proof and its explicit references to the author's earlier capacity theory were read.
Robin monotonicity V_a(H)>=V_a(H') also follows immediately from the inclusion of the two classes of probability measures in its infimum definition.
Thus a fixed initial nonpolar compact set gives upper bounds for all its later Green entries and Robin constants when the local sets increase.
These standard interfaces are accepted at this exact scope, with their ancestor-proof limit preserved.

## Source search and application boundary

The local bibliography and audit directories had no adequate Rumely unit for this theorem.
The source follow-up therefore checked the arXiv author manuscript and the author's official publication page, which identified it as an earlier version of the 2013 book.
The AMS book page did not supply readable full published text in this search; no comparison to its entire theorem proof or errata is claimed.
The search stopped after the identified primary manuscript supplied the exact compact-set theorem and needed local conventions.

For the [G0001 inquiry](../../../tasks/Yin_T_G0001_v1.md), this source can accept specified finite unions of strict local discs at a finite set of bad places and the standard X-trivial sets elsewhere.
A proof using that option must establish a single finite exceptional set outside which the projective curve has good reduction, X has distinct specializations, and all chosen coordinate functions extend regularly over the complement.
It must also prove actual positive-capacity local sets, global capacity greater than 1, and the passage from every local conjugate lying in the sets to the claimed integer or unit coordinates.
Those are project obligations; they are not discharged by this source-account acceptance.
No algebraic residual triple, total-real point, norm counterexample, or uniform Mahler conclusion is adopted here.
