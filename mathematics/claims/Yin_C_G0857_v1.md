---
author: Yin
---
# Binary rotation masks and high-precision units with long residue periods

This project deduction concerns the first residue layer of the rotated-radical mechanism for the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
It fixes the cyclic-mask classification and the separation construction developed in D11, without adopting D11's distinct complex-disk argument or any unreviewed deduction from L445.
The mathematical author is Yin; the radical-route subagent developed the argument under the main agent's research assignment.
The selected decision below owns the assessment and exact review evidence.

## Statement

Let \(q\) be an odd prime, let \(k\) be a finite field of characteristic two containing a primitive \(q\)-th root \(\xi\), and let \(r\in k(x)\).
Write \(\wp(v)=v^2+v\), \(r_j(x)=r(\xi^jx)\), and
\[
 K_q(r)=\{e\in\mathbb F_2^q:\sum_{j=0}^{q-1}e_jr_j\in\wp(k(x))\}.
\]
Then the following conclusions hold.

1. Under the identification of \(\mathbb F_2^q\) with \(\mathbb F_2[z]/(z^q-1)\), the kernel \(K_q(r)\) is the ideal of one monic divisor \(g\mid z^q-1\).
   Its dimension is \(q-\deg g=\epsilon+tf\), where \(f=\operatorname{ord}_q(2)\), \(\epsilon\in\{0,1\}\), and \(0\le t\le(q-1)/f\).
   This assertion has no restriction on pole multiplicities of \(r\).
   If \(f=q-1\), the only kernels are zero, the span of the full mask, the even-weight subspace, and the entire mask space.
   The even-weight case holds exactly when all \([r_j]\) are the same nonzero Artin--Schreier class, and the entire-space case holds exactly when \([r]=0\).

2. Suppose additionally that \(r\) is proper, has no pole at zero, and has only simple finite poles.
   Then \([r]=0\) is equivalent to \(r=0\), and equality of two rotation classes is equivalent to equality of the corresponding rational functions.
   If \(f=q-1\) and a nonempty proper mask belongs to \(K_q(r)\), either \(r=0\) or \(r(\xi x)=r(x)\ne0\).
   In the latter case the degree of the reduced denominator of \(r\) is a positive multiple of \(q\).
   In particular, for \(r=\overline W/\overline U\) with \(\overline U(0)\ne0\), \(\overline U\) squarefree of degree \(d\ge1\), \(\deg\overline W<d\), and \(\gcd(\overline U,\overline W)=1\), such a proper mask requires \(q\mid d\) and \(q\le d\).

3. For every \(n=2^a\), \(a\ge1\), and every integer \(L\ge3\), there are infinitely many monic irreducible reciprocal \(P\in\mathbb Z[t]\) of degree \(d=2n\), with constant term 1, such that all positive powers of a root have degree \(d\), \(m(P)>\log2\), and the reduction \(Q=\overline P\) is irreducible with every root of order \(N=2^n+1\).
   For \(P_b(x)=\prod_{i=1}^d(1-\alpha_i^b x)\), these inputs satisfy \(P_4\equiv P_2\pmod{2^L}\).
   With \(U=P_2\), \(W=(P_4-P_2)/4\), and the square root of constant term 1, one has
   \[
   F=\sqrt{P_2P_4}\in\mathbb Z[[x]],\qquad
   F/U\equiv1\pmod{2^{L-1}}.
   \]
   Therefore \(\overline W=0\), and \(K_q(\overline W/\overline U)=\mathbb F_2^q\) at every odd rotation prime.
   Nevertheless, for any positive integers \(a_1,\ldots,a_k\) with \(Q\mid\prod_i(t^{a_i}-1)\), at least one \(a_i\) is divisible by \(N\), so \(\sum_i a_i/d\ge(2^n+1)/(2n)\to\infty\).

The construction in part 3 separates plentiful masks and arbitrary prescribed finite precision from the short binary scalar-period and bounded-ratio binomial-cover hypotheses.
Its large measure does not supply a near-one family, a new Mahler gap, or the missing small-measure input for the rotated-radical strategy.
No claim that all first-layer relations are cyclotomic controls, that primes with \(\operatorname{ord}_q(2)=q-1\) are available in an unbounded prescribed range, or that the repeated-pole case satisfies the simple-pole conclusions is made.

<a id="argument"></a>
## Complete argument

<a id="binary-cyclic-mask"></a>
## The cyclic structure of the first binary relation space

Author development for Yin, 2026-11-04T16:15.
Let \(q\) be an odd prime, let \(k\) be a finite field of characteristic two containing a primitive \(q\)-th root \(\xi\), and put \(V=k(x)/\wp(k(x))\), where \(\wp(v)=v^2+v\).
This quotient is an \(\mathbb F_2\)-vector space; no \(k\)-linear structure is asserted.
For \(r\in k(x)\), write \(r_j(x)=r(\xi^jx)\) and let
\[
 K_q=\{(e_0,\ldots,e_{q-1})\in\mathbb F_2^q:
                  \sum_j e_j[r_j]=0\text{ in }V\}.
\]
The substitution \(\tau f(x)=f(\xi x)\) preserves \(\wp(k(x))\), has order \(q\), and takes \([r_j]\) to \([r_{j+1}]\).
Thus the map \(\mathbb F_2[z]/(z^q-1)\to V\) sending \(z^j\) to \([r_j]\) is a module homomorphism when \(z\) acts as \(\tau\).
Its kernel is an ideal, so \(K_q=(g)\) for a unique monic divisor \(g\mid z^q-1\), with \(\dim K_q=q-\deg g\).
For completeness, take the inverse image of the kernel in the Euclidean ring \(\mathbb F_2[z]\); its monic generator divides \(z^q-1\), and the residues of \(g,zg,\ldots,z^{q-\deg g-1}g\) form the indicated basis.
This argument requires no restriction on the pole multiplicities of \(r\) and therefore also applies to repeated reduction factors.

Let \(f=\operatorname{ord}_q(2)\).
The nontrivial \(q\)-th roots have Frobenius orbits of length \(f\), so every irreducible factor of \(\Phi_q\) over \(\mathbb F_2\) has degree \(f\).
Indeed a root \(\omega\ne1\) returns under the \(a\)-fold Frobenius exactly when \(q\mid2^a-1\); its orbit product has coefficients fixed by squaring and hence in \(\mathbb F_2\), and any polynomial over \(\mathbb F_2\) vanishing at \(\omega\) vanishes at the whole orbit.
Since \(z^q-1\) is squarefree, it follows that
\[
 \dim K_q=\epsilon+tf,
 \qquad \epsilon\in\{0,1\},\quad 0\le t\le(q-1)/f.
\]
When \(f=q-1\), the only possible dimensions are \(0,1,q-1,q\).
The one-dimensional possibility is the span of \(1+z+\cdots+z^{q-1}\), corresponding precisely to the full mask.
The \((q-1)\)-dimensional possibility is \((z+1)\), the even-weight masks; it occurs exactly when all \([r_j]\) are the same nonzero class.
The full kernel occurs exactly when \([r_0]=0\).
Consequently a nonempty proper mask at such a prime forces either equality of all classes or their common vanishing.
No assertion about infinitely many such primes, or a suitable such prime in a logarithmic interval, is used.

Suppose now that \(r\) is proper, has no pole at zero, and has only simple finite poles, as in part 2.
A nonzero pole of \(v\) of order \(a\) gives \(v^2+v\) a pole of order \(2a\), so a proper rational function with at most simple poles is in \(\wp(k(x))\) only when it is zero.
The same applies to a difference of two of the \(r_j\).
Thus common zero classes mean \(r_0=0\), while equal classes mean actual equality \(r_0(\xi x)=r_0(x)\).
If this invariant rational function is nonzero, its finite poles are nonzero and form disjoint orbits of length \(q\).
Its reduced denominator therefore has degree divisible by \(q\), at least \(q\).
In the specialization \(r=\overline W/\overline U\) of part 2 with \(\gcd(\overline U,\overline W)=1\), the denominator degree is \(d\), so proper masks beyond the full mask require \(q\mid d\) and \(q\le d\).
With cancellation, these conditions concern the reduced denominator, not all of \(\overline P\).
For repeated reduction factors one cannot replace equality of Artin--Schreier classes by equality of rational functions using this simple-pole argument.

The cyclic-code identification is standard, not a project novelty claim.
The inspected primary course notes [Pedro Martins Rodrigues, Cyclic Codes, Notes VIII of the 2020--2021 Coding Theory and Combinatorics course, Section 1.1, Theorem 7, Propositions 8--9 and Lemma 10, PDF pages 2--4](https://www.math.tecnico.ulisboa.pt/~pmartins/CTC/CTC21Notes8.pdf#page=2) give the ideal correspondence, generator divisor and dimension statement used as attribution here; the application and its proof are given above.
The local search by Artin--Schreier, binary masks, rotation poles and cyclic codes found L445's pole test and the existing arithmetic constructions, but no retained version of this mask-module statement in that selected scope.
This is not an exhaustive novelty search.

<a id="large-period-full-mask"></a>
## Full mask spaces do not force a short binary binomial cover

The following construction tests the proposed implication from plentiful masks to the previously covered C244/C135 classes.
For every \(n=2^a\) with \(a\ge1\), put \(N=2^n+1\) and \(d=2n\).
There is a reciprocal irreducible polynomial \(Q\in\mathbb F_2[t]\) of degree \(d\) whose roots all have order \(N\).
To see this, choose an element \(u\) of order \(N\) in \(\mathbb F_{2^{2n}}^*\).
Existence follows from the cyclicity of the multiplicative group, and \(N\mid2^{2n}-1\).
The standard primitive-element fact was checked in [Fields and Cyclotomic Polynomials, Theorem 19 and Corollary 20, printed/PDF pages 16--17](https://e.math.cornell.edu/people/belk/numbertheory/CyclotomicPolynomials.pdf#page=16).
Here \(2^n\equiv-1\pmod N\), and the order of 2 modulo \(N\) divides the power of two \(2n\) but does not divide \(n\).
It is therefore exactly \(2n\).
The Frobenius orbit of \(u\) has length \(d\), giving the claimed irreducible \(Q\); inversion is its \(n\)-fold Frobenius, proving reciprocity.
Its constant term is 1 and its roots are simple.

There is a monic reciprocal polynomial \(Q_*\in\mathbb Z_2[t]\) reducing to \(Q\), with constant term 1, whose root set is stable under squaring and consists of roots of unity of order \(N\).
Here are the local details, reusing the simple-root lifting and finite-order Frobenius construction in [C241](../claims/Yin_C_G0241_v1.md#direct-etale-frobenius-lift).
For any monic integer lift \(Q_0\) of \(Q\), the ring \(\mathcal O=\mathbb Z_2[t]/(Q_0)\) is the degree-\(d\) unramified complete ring in that construction, with residue field \(\mathbb F_{2^d}\) and a Frobenius lift \(\sigma\) of order \(d\).
Hensel lifting applied to \(t^N-1\), whose derivative is a unit at \(u\), gives a unique \(\beta\equiv u\pmod2\) with \(\beta^N=1\).
Its order is exactly \(N\) by reduction.
Both \(\sigma\beta\) and \(\beta^2\) are roots of \(t^N-1\) reducing to \(u^2\), so uniqueness gives \(\sigma\beta=\beta^2\).
Define \(Q_*\) as the product of \(t-\beta^{2^j}\) for \(0\le j<d\).
Its coefficients are fixed by \(\sigma\) and lie in \(\mathbb Z_2\): a fixed element has residue in \(\mathbb F_2\), and repeatedly subtracting 0 or 1 and dividing by 2 gives its convergent binary expansion in \(\mathbb Z_2\).
The roots pair under inversion because \(2^n\equiv-1\pmod N\); hence the product is reciprocal with constant term 1.
Squaring permutes the roots, so the powered polynomials satisfy \((Q_*)_2=(Q_*)_4=Q_*\).
Only the general local lifting construction of C241 is used here, not its nontorsion norm conclusion.

Fix any integer \(L\ge3\) and choose a monic reciprocal \(P_0\in\mathbb Z[t]\), of degree \(d\) and constant term 1, coefficientwise congruent to \(Q_*\pmod{2^L}\).
For a positive integer \(T\), put
\[
 P_T(t)=P_0(t)+2^LT(t^{d-1}+t).
\]
Reduction modulo 2 is the irreducible \(Q\), so \(P_T\) is irreducible over \(\mathbb Q\).
Choose \(T\) so large that
\[
 2^LT(2^{d-1}-2)>
                  \sum_{j=0}^d |[t^j]P_0|\,2^j.
\]
On \(|t|=2\), the added term then strictly dominates \(P_0\).
[Rouche's theorem, Corollary 7.44, printed page 83 of the Princeton MAT330 Spring 2023 notes](https://web.math.princeton.edu/~js129/PDFs/teaching/MAT330_spring_2023/MAT330_Lecture_Notes.pdf#page=83), gives exactly \(d-1\) roots of \(P_T\) inside that circle, since \(t^{d-1}+t=t(t^{d-2}+1)\) has that many there.
There is exactly one root outside, so \(m(P_T)>\log2\) and the input is nontorsion.
All positive powers preserve its degree: if distinct conjugates had a root-of-unity quotient, an automorphism taking the first to the unique outside root would take the second to another root of the same modulus, a contradiction.
Thus these are actual irreducible reciprocal power-stable integer units, not merely modular models.

The coefficients of a powered polynomial are integral polynomials in those of its original polynomial, for example from the characteristic polynomial of the powered integral companion matrix.
Therefore \((P_T)_2\equiv(P_T)_4\equiv Q_*\pmod{2^L}\).
In particular \(\overline W=0\), and \(r_j=0\) for every rotation prime and every \(j\).
The whole space \(\mathbb F_2^q\) survives as masks, including every proper mask.
More strongly, writing \(U=(P_T)_2\) and \((P_T)_4-U=2^LA\), one has
\[
 \frac{\sqrt{U(P_T)_4}}{U}
       =\sqrt{1+2^LA/U}\equiv1\pmod{2^{L-1}}.
\]
The normalized series is well defined because \(U(0)=1\) and \(A(0)=0\).
For the term with index \(j\ge1\) in its binomial expansion, the 2-adic coefficient valuation is
\[
 Lj+v_2\binom{1/2}{j}
       =(L-1)j-v_2(j!)=(L-2)j+s_2(j)\ge L-1,
\]
where \(s_2(j)\) is the number of ones in the binary expansion of \(j\).
Thus any prescribed finite approximation precision is available in this construction.

On the other hand, any binary binomial cover
\[
 Q\mid\prod_{i=1}^k(t^{a_i}-1)
\]
must have \(N\mid a_i\) for at least one \(i\), by evaluating at the root \(u\) of exact order \(N\).
Consequently \(\sum_i a_i\ge N\) and
\[
 \frac{\sum_i a_i}{d}\ge\frac{2^n+1}{2n}\longrightarrow\infty.
\]
This excludes a uniformly bounded total exponent-to-degree ratio, regardless of how the number of factors is chosen.
In particular neither the short scalar-period hypothesis of [C244](../claims/Yin_C_G0244_v1.md#balanced-scalar-congruence-gap) nor the bounded-ratio binary-binomial-cover hypothesis of [C135v2](../claims/Yin_C_G0135_v2.md#statement) is forced by a full first-layer mask space, even on actual power-stable reciprocal inputs.
The construction has large measure by design and supplies no near-one family or new Mahler gap.
It separates the binary relation condition from those two sufficient coverage hypotheses; it does not show that the latter fail on small-measure inputs or that no other known gap criterion applies.
The next useful question is the paid analytic and coefficient cost of high-precision lifts in the actual small-measure range, rather than whether full first-layer kernels automatically imply the old short-period controls.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T16:27 |
| status | proved |
| reason | Adopt the complete cyclic-mask classification and actual high-precision long-period construction after independent R1074 F1. The constructed inputs have large Mahler measure; no near-one supply, alternative-prime exclusion or unrestricted gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire stated theorem, with all supplied hypotheses, quantifiers and comparison limitations. |
| argument | [Complete argument](#argument) | Entire fixed argument through its final consequences and source/application boundaries. |
| dependency | [Local lifting input](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Complete unramified local-ring Hensel and Frobenius construction at the exact use specified in the argument. |
| support | [Scalar comparison](Yin_C_G0244_v1.md#balanced-scalar-congruence-gap) | Binary short-period hypothesis comparison only; no all-prime failure assertion. |
| support | [Binomial-cover comparison](Yin_C_G0135_v2.md#statement) | Full reduction-divisibility and total-exponent cost hypotheses only. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1074_v1.md#binary-masks-whole) | Complete exact statement and argument, including source and comparison interfaces at the finding's stated depth. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
