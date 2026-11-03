---
author: Yin
---
# Sch14-U001: actual 2-ramified Galois fields and their pro-2 scope

Date: 2026-10-20T10:14.
Human record author Yin.
Root supplied the Schmid and Jones source leads for the full D42 arithmetic-family candidate.
The draft_comparison_cleanup AI acquired and read the actual Schmid publisher PDF; the Jones resource was unnecessary for the resulting source interface.

<a id="sch14-u001"></a>
## Read; accepted precise arithmetic realization statements

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Peter Schmid, On2-extensions of the rationals with restricted ramification, Acta Arithmetica163(2)(2014),111--125, DOI10.4064/aa163-2-2. The actual publisher PDF has16 pages, the last blank, with printed111--125 on PDF pages1--15.

Passages: Printed111/PDF1: definition of K_S(G), Q_S, G_S, their2-extension versions and Theorem0. Printed113--114/PDF3--4: complete initial quadratic-field classification, Lemma2.1, Proposition2.2 and its complete proof; the latter identifies the classical pro-2 presentation and states its inherited-proof references.

Inspection: Read the complete named definitions, theorem and proposition, quadratic classification and displayed proofs. Accept the established realization/presentation statement at this exact scope; the classical Markšaitis/Shafarevich/Koch/Gras--Jaulent proofs of the presentation and the later central-extension/class-field calculations were not independently audited.


Source: [publisher artifact](../../../literature/pdf/Sch14--publisher.pdf).
No printed contents table appears in the inspected opening.
The supplied ResearchGate excerpt was only a source lead; the accepted statements were checked against the actual publisher text.

<a id="two-ramified-field-definitions"></a>
### Complete field-class definitions

For a finite set S of rational primes and a finite group G, K_S(G) is the set of normal number fields inside C with Galois group isomorphic to G and unramified at all finite primes outside S.
Ramification at infinite places is allowed.
The maximal algebraic extension of Q with this ramification condition is Q_S, and G_S=Gal(Q_S/Q).
The maximal Galois pro-2 subextension is Q_S(2), with G_S(2)=Gal(Q_S(2)/Q); equivalently G_S(2) is the maximal pro-2 quotient of G_S.
For S={2}, the source calls such number fields2-ramified and writes K_2(G).
Here a finite2-group means a group of order a power of2, and an arbitrary finite2-extension in this use is Galois over Q.
The source does not say that every abstract finite2-group is realizable with this single ramified finite prime.

<a id="quadratic-and-pro-two-realization"></a>
### Exact quadratic classification and actual realizability

The opening of Section2 states that the only quadratic number fields unramified at every finite prime other than2 are

    Q(i), Q(sqrt2), Q(sqrt(-2)).

Each is ramified at2.
The latter local assertion may also be checked directly using the Eisenstein polynomials X^2-2, X^2+2 and, after translation for Q(i), X^2+2X+2.
This classification supplies the source input for the complete-ramification argument now fixed in [C_G181](../../../claims/Yin_C_G0181_v1.md#argument); Schmid does not state that particular subsequent decomposition/inertia proof here.

For any finite2-group G, define

    Omega(G)={(x,y) in G times G:G=<x,y>, y^2=1}.

Theorem0 and Proposition2.2 assert exactly

    K_2(G) is nonempty iff Omega(G) is nonempty,
    |K_2(G)|=|Omega(G)|/|Aut(G)|.

Thus the realization is a theorem about actual number fields with controlled finite ramification, and is not supplied merely by choosing a permutation or abstract group.
The equation y^2=1 permits y=1; the displayed criterion rather than an informal use of “involution” controls all small or cyclic cases.

The proposition's proof uses the established presentation

    Gal(Q_{ {2} }(2)/Q)
      = pro-2 completion of Z * C_2
      = <sigma,tau | tau^2=1> in the pro-2 category.

The element tau can be identified with complex conjugation.
For each pair in Omega(G), the proof constructs a continuous epimorphism sending sigma,tau to x,y.
The fixed field of its kernel is the actual required finite Galois extension.
Two pairs give the same field precisely when they differ by an automorphism of G, giving the counting formula.
The original proof of the pro-2 presentation remains an accepted classical input with the source's explicit references, not a newly audited project argument.

### Exact project scope

The [C_G181 full2-extension condition](../../../claims/Yin_C_G0181_v1.md#statement) uses the quadratic classification for every actual B in this field class.
The full presentation and realization theorem identify that class and permit separately justified structural comparisons.
They do not supply a bounded conjugacy class, central Frobenius lift, original-unit height estimate, bounded inertia quotient or a near-one family without the additional project arguments.
They also do not by themselves prove that the whole field is outside every fixed-radical or previous height domain.
Those are separate applicability obligations; a nonabelian field, large abstract2-group or fixed-positive-measure control is not a Lehmer counterexample.
The separate [C_G183 source interface](../../../claims/Yin_C_G0183_v1.md#pro-two-source-interface) records its later inspection of Proposition2.4 at printed114/PDF4; that additional passage is not included retroactively in this unit's original inspection range.
