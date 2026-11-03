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

Inspection: Selected complete statements and conventions text-read; printed465 and474 also visually inspected to resolve the extracted mathematical symbols. The graph, rational-denominator, strict-subsequence, height and own-degree applications below were checked. Theorem1.1's proof in Sections3--4 and the original Zhang/Bombieri--Zannier proofs were not audited; reading the short Section5 consequence is not a source-wide proof audit.


The [retained primary paper](../../../literature/pdf/Bil97--published.pdf) identify the edition.
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

<a id="fixed-rational-function-height-gap"></a>
### Direct fixed rational-function consequence

Fix an integer r>=1 and a nonzero rational function F in Q(X_1,...,X_r).
Suppose F is not a root of unity times a Laurent monomial; since F is rational over Q, the excluded functions are precisely

    F(X)=+/- product_i X_i^(a_i), a_i in Z.           (2)

The zero exponent vector in(2) includes the constants+1 and-1.
There exist positive constants delta_F,c_F such that for every multiplicatively independent x in(Qbar^*)^r with max_i h_abs(x_i)<=delta_F, whenever F(x) is defined and nonzero,

    h_abs(F(x))>=c_F.                                (3)

Both constants are uniform over the tuples and their field degrees, but depend on the fixed function and fixed r.
Consequently every sequence of such independent tuples with maximum coordinate height tending to zero has a positive lower limit of the output height.

Write F=A/B with nonzero coprime rational Laurent polynomials, and let X be the Zariski closure in G_m^(r+1) of its graph on A(x)B(x)!=0.
It is irreducible of dimension r, defined over Q, and contained in the fixed hypersurface A(x)-y B(x)=0.
For example, primitivity and degree one in y show that this is the graph component; closure adds no other irreducible component.
Clearing fixed rational denominators changes this equation by a nonzero scalar only.
Every actual Galois conjugate of a valid graph point remains a valid graph point, because A and B are rational and their nonzero values remain nonzero under embeddings.

Every graph point with independent x lies in X^*.
Indeed let a torsion translate T inside X contain that point and project T to the first r coordinates.
If its image is a proper torsion translate, a nonzero integer character takes a root-of-unity value at x, contradicting independence.
Otherwise that projection is surjective, so dim T>=r; since T is contained in the irreducible dimension-r graph closure, T=X.
Such a torsion graph has a character relation

    x^a y^b=zeta, b!=0,

because its projection to x is dominant.
It follows that F^b X^a=zeta as a rational-function identity.
The Laurent polynomial ring over Qbar is a unique factorization domain; the valuation of this identity at every nonunit irreducible factor makes F a scalar times a Laurent monomial.
Its rational scalar is a root of unity and therefore is+1 or-1, contradicting the hypothesis.
This also covers zero-dimensional torsion translates: their projected x is a torsion point and cannot be independent.

If admissible graph points exist, X^* is nonempty and(1) applies to every one of them.
If no such point exists, assertion(3) is vacuous.
The exact local height comparison gives

    eta_X<=H_(r+1)(x,F(x))
          <=sum_i h_abs(x_i)+h_abs(F(x)).             (4)

Thus one can take delta_F=eta_X/(2r), c_F=eta_X/2.
In fact along any admitted small-height sequence, liminf h_abs(F(x_k))>=eta_X.
There is no coefficient-denominator saving or omission of finite places in(4).

### Check of the proposed strict/non-strict alternative

Suppose for contradiction that independent x_k have coordinate heights tending to zero and h_abs(F(x_k))->0.
Their lifted graph points then have H_(r+1)->0 by(4)'s upper inequality.
If the lifted sequence is strict, Theorem1.1 and Lemma2.1(d) put full polycircle Haar measure on the fixed graph hypersurface.
That is impossible: a nonzero Laurent polynomial cannot vanish almost everywhere on the polycircle, by orthogonality of its finitely many characters.

If the lifted sequence is not strict, the DEFINITION supplies one fixed proper algebraic subgroup containing an infinite subsequence.
Choose a nontrivial ambient integer character that is identically one on that proper subgroup to obtain one fixed relation x_k^a F(x_k)^b=1 on that subsequence.
The exponent b is nonzero because every x_k is independent.
After reversing all exponents if necessary, take b>0 and clear the fixed denominator to get x_k^a A(x_k)^b-B(x_k)^b=0.
The base sequence is still strict and small, so Bilu and the same fixed-closed-set argument make this Laurent polynomial identically zero.
The resulting rational identity again forces exactly the excluded functions(2).
No common character is selected from merely varying pointwise dependencies; the fixed infinite subsequence is supplied only by failure of strictness.
This verifies the proposed alternative without needing it in addition to the direct Theorem5.1 application.

The rational case must not be justified by claiming that every rational function of unit modulus on the circle is a monomial.
For example (X-2)/(2X-1) has unit modulus on S^1 and is nonmonomial.
The fixed graph in one additional coordinate, not its modulus-only image, is the relevant closed set.

<a id="fixed-function-own-degree-divergence"></a>
### Nonconstant functions: actual own degree and total measure

Now require F to be NONCONSTANT, while retaining fixed r and rational coefficients.
For every independent x_k with max_i h_abs(x_(k,i))->0 and defined nonzero y_k=F(x_k),

    [Q(y_k):Q]->infinity.                             (5)

This conclusion also holds for the monomials in(2); it does not require(3).
Here is the complete elementary height and finiteness argument.

Clear the rational coefficients and a common Laurent monomial so that F=P/Q with nonzero integer ordinary polynomials.
Put C=max(||P||_1,||Q||_1)>=1 and let D_i be the maximum degree in X_i of these two polynomials.
The local triangle inequality at infinite places, and the ultrametric inequality with integral coefficients at finite places, give

    h_abs(F(x))=h(P(x):Q(x))
       <=log C+sum_i D_i h_abs(x_i).                 (6)

All C,D_i are fixed and no output integrality is assumed.
The product formula justifies the projective rescaling from(P(x):Q(x)) to(1:F(x)).
Thus y_k have bounded absolute height.

If their own degrees were bounded along an infinite subsequence, they would take only finitely many values.
For completeness, a primitive integer minimal polynomial of degree n<=B and height at most H has

    |a_(n-j)|<=binomial(n,j) exp(nH)<=2^B exp(BH).

Hence only finitely many such integer polynomials, and consequently finitely many roots, occur.
This is the elementary coefficient form of the standard Northcott finiteness fact; it is verified here rather than importing a new source proof.
Choose a further subsequence with y_k=y_0 and let q(Y) in Z[Y] be its nonzero minimal polynomial, of degree s.
The expression

    Q(X)^s q(P(X)/Q(X))

is a fixed rational polynomial vanishing on that subsequence.
It is nonzero because a nonconstant rational function cannot satisfy a nonzero polynomial over the constant field: factoring q over Qbar would otherwise make one factor F-c identically zero.
Its rational coefficients ensure that every full Galois orbit of x_k is in its zero set.
Bilu applied to the base tuples again contradicts nonzero polynomial vanishing on full Haar measure.
This proves(5), including the possibility of an initially unbounded degree sequence with a bounded-degree subsequence.

Combining(3) and(5), for NONCONSTANT F outside(2), the output's own TOTAL logarithmic Mahler measure satisfies

    m_own(F(x_k))=[Q(F(x_k)):Q] h_abs(F(x_k))
                    ->infinity.                     (7)

The degree is the actual minimal-polynomial degree of the output.
The measure includes its primitive leading-coefficient contribution when the output is not integral; neither the degree nor that contribution is replaced by the input degree.
No rate or explicit universal lower constant is supplied.

### Constants, monomials, domain and fixedness boundaries

The identically zero function is excluded, and zero or undefined evaluations are outside(3)--(7).
For a fixed reduced nonzero numerator or denominator, independent tuples with coordinate heights tending to zero eventually avoid its zero set by the same base Bilu argument.
The explicit domain restriction nevertheless remains part of the statement.

For F=c in Q^*, the height and own measure are the fixed numbers h_abs(c) and m_own(c)=h_abs(c), since the degree is one.
They are zero for c=+/-1 and positive for every other nonzero rational c; for example F=2 has measure log2.
Thus CONSTANTS do not satisfy the divergence conclusion and must not be listed only as torsion exceptions.

For F=c X^a with c in Q^*, height inequalities give

    |h_abs(F(x))-h_abs(c)|<=sum_i |a_i|h_abs(x_i).

Therefore its height tends to h_abs(c).
If a!=0 and c is not+/-1, both(3) and(7) apply.
If c=+/-1, the height tends to zero and(3) is correctly excluded, although(5) still holds for a!=0.
Whether its own measure grows then requires separate arithmetic of those monomials.

All functions, coefficients, exponent supports and r are fixed before the input sequence varies.
There is no asserted uniformity over varying rational functions, growing support/rank, growing coefficient denominators, or an auxiliary chosen from the current minimal polynomial.
In particular the input-dependent projection symbols of C158 are not fixed F and are not disposed of by this statement.

### Salem consumer and contribution boundary

For a fixed number r of roots chosen from distinct inverse pairs of genuine Salem inputs, the classical [L_G176 independence argument](../../../ledger/Yin_L_G0176_v1.md#salem-joint-phase-density), with its [Dub23 attribution](../Dub23/readme.md), supplies multiplicative independence.
The same modulus proof includes a selected real-pair representative: send that chosen root to the real exterior root and all other selected pairs to circle roots.
If original total measures stay bounded while original degrees d tend to infinity, every selected coordinate has h_abs=m(alpha)/d tending to zero.
Thus every fixed NONCONSTANT rational pattern outside(2) has diverging OWN total measure by(7), without a normal-trace, subdegree or Galois-group hypothesis.
Unbounded d alone is insufficient unless m(alpha)/d tends to zero; bounded original total measure is one sufficient condition.

Any combination with a separate theorem about monomials in several Salem roots must retain that theorem's own acceptance, support and single-root exceptions.
This unit does not adopt the separate C165 candidate or independently review it.
For nonconstant fixed patterns, the remaining torsion-monomial cases require that separate analysis; all nonzero rational constants remain a different, explicitly bounded-output case.
The conclusion is an obstruction for these fixed auxiliary patterns, not a positive gap for the original Salem numbers or a theorem about moving projection coefficients.
