---
author: Yin
---
# MS05-U001: exact interlacing and killer-exponent Salem construction

Date: 2026-10-18T14:05.
Human record author Yin.
The entropy_attainment_bridge AI retains the newly inspected source interface needed for the explicit fixed-trace changing-exponent family.
This is source-statement acceptance and selected proof/application checking, not independent review of the source's complete original argument or its quantitative degree theorem.
No source acquisition, numerical program or prime enumeration is performed.

<a id="ms05-u001"></a>
## Read; exact construction interface accepted at the stated proof depth

## Source and inspection

Source edition: James McKee and Chris Smyth, There are Salem numbers of every trace, retained arXiv:math/0308213v2,31March2004, with title-page date19February2004; 12 pages with matching printed/PDF pagination. The published journal edition has different result numbering and is not substituted here.

Passages: Circular-interlacing definition, Lemma4 and Proposition5(a), pages3--4; Proposition6 and torus/coset conventions, page5; Theorem8 statement, page6; Corollary9, h and equation(10), Lemmas10--11, pages8--9; Lemma12 and its complete construction proof, pages9--10; finite-computation limitation, Section8,page10.

Inspection: Direct text reading of the listed statements, definitions and construction proof; visual checks of pages8--9, including page9 in the present inquiry. Lemma10's classification argument and the torsion exclusion, parity, interlacing application, original degree and trace in Lemma12 are checked below. Theorem8/Corollary9 and the interlacing propositions are accepted at their exact primary-statement/applicability scope; no original Mann/Schmidt proof audit, whole-paper audit, or acceptance of the separately optimized degree estimate.


The [retained primary manuscript](../../../literature/pdf/MS05.pdf) is the one identified by the [existing source account](readme.md).
The prior arbitrary-trace exterior-root screen is separately retained at [C_G8](../../../claims/Yin_C_G0008_v1.md#arbitrary-trace-construction-measure-screen).
Neither record is relabeled as a whole proof audit by this more detailed source unit.

<a id="ms05-circular-interlacing"></a>
## Circular interlacing and the exact construction theorem used

The source calls a pair p,q circularly interlacing when they are relatively prime real polynomials with positive leading coefficients, all their zeros lie on the unit circle, and their zeros strictly alternate when the circle is traversed.
They consequently have the same degree and no multiple zero.
For every positive integer k, p(z^k),q(z^k) again interlace; in particular z^k-1 and z^k+1 do so.

Proposition6 states that a finite sum of fractions q_i/p_i from such pairs, after reduction, is again q/p from a circularly interlacing pair.
The proof passes to x=z+z^-1 and positive partial fractions as in Lemma4.
The required preservation is for the rational sum after cancelling common factors, not for the uncancelled product denominator with repeated roots.
Positive scalar factors in the fractions do not change the alternating-root condition.

The part of Proposition5 used here is the following complete conditional statement.
If p,q are circularly interlacing integer polynomials and p is monic, then

    S(z)=(z^2-1)p(z)-zq(z)

is the minimal polynomial of a Salem number, or of a reciprocal quadratic Pisot number, possibly times a cyclotomic polynomial, PROVIDED

    p(1)=0,
    OR q(1)=0 and 2p(1)-q'(1)<0.

These are alternatives; the application below uses p(1)=0.
The possible cyclotomic product and possible quadratic exception must be excluded separately before S is called an actual Salem minimal polynomial.
The unrelated Pisot construction in Proposition5(b) is not an input here.
The selected primary statements and their applicability are accepted as established external inputs; their original proofs are not assigned a new independent whole-review verdict.

<a id="ms05-torsion-coset-exponent"></a>
## Torsion cosets, common exponents and the explicit bound

Write G_m^s=(C^*)^s.
An r-dimensional subtorus H is an algebraic subgroup parametrized by monomials t^E, where E is an integer matrix of rank r and t ranges over(C^*)^r.
A torsion coset is omega H, where every coordinate of omega is a root of unity.
A positive integer K is an exponent of that coset if it is a multiple of its order in G_m^s/H, equivalently omega^K belongs to H.
It need not kill each coordinate of a chosen representative omega.
If a coordinate is constant on the coset, however, its value is a K-th root of unity.
A maximal torsion coset contained in a variety V is one not properly contained in another torsion coset contained in V; zero-dimensional cosets are allowed.
This agrees with the torsion-translate convention in [Bil97](../Bil97/Yin_U001.md#torus-bogomolov-complement), with the additional exponent convention made explicit here.

For a Q-defined variety V in G_m^s, let its exponent support be the union of the integer exponent vectors with nonzero coefficient in its specified defining equations.
Let N be that support's size, Delta its Euclidean diameter, and Pi_N the product of the rational primes at most N.
Theorem8 states that each maximal torsion coset of codimension k has an exponent m Pi_N for some positive integer

    m<=Delta^(2k) k^(k/2).

For the present application, Corollary9 supplies the common exponent

    K=Pi_N lcm(1,...,floor(Delta^(2s) s^(s/2))).

Replacing the final floor by a ceiling, or replacing N by an upper bound, gives a permitted common multiple and hence also a common exponent.
The source's lcm notation with a real upper endpoint means the positive integers up to that endpoint; the ceiling convention is a conservative explicit adaptation.
Theorem8/Corollary9 are accepted at this exact source-statement and applicability scope, with the Q-defined variety and support data retained.
Their general lattice argument and Mann/Schmidt inputs are not newly proof-audited.

<a id="ms05-hypersurface-and-killer"></a>
## The actual hypersurface and its source killer exponent

Use q for the source's number n of powered coordinates, to distinguish it from RY26's n=q-1.
For q>=2 define, on(C^*)^(q+1),

    h_q(x_0,x_1,...,x_q)
      =2(x_0^2-1)product_(i=1)^q(x_i-1)
        -x_0 sum_(j=1)^q(x_j+1)product_(i!=j)(x_i-1).

This is the complete polynomial defining the variety; no denominator is used to define its zero set.
Where every x_i!=1 for i>=1, equation(10) is

    h_q/[2x_0 product_(i=1)^q(x_i-1)]
       =x_0-x_0^-1-(1/2)sum_(i=1)^q (x_i+1)/(x_i-1).

Lemma10 says that the only maximal torsion cosets on h_q=0 with x_0 nonconstant are

    B_ij={x_i=x_j=1},    1<=i<j<=q,

with all other coordinates free; these have dimension q-1.
For the checked proof, a point of h_q=0 cannot have exactly one powered coordinate equal to1, since its corresponding summand is then the only nonzero one.
Two such coordinates put the point in B_ij.
For a hypothetical remaining coset with x_0 nonconstant and no powered coordinate identically1, choose a monomial one-parameter specialization avoiding all the finitely many relevant exponent hyperplanes, and reverse its sign so the x_0 exponent is positive.
As the parameter tends to infinity, x_0-x_0^-1 is unbounded, while each of the other fractions has a finite limit.
This contradicts equation(10) and checks the displayed classification argument at its stated torus parametrization.

For this hypersurface the support diameter is sqrt(q+4), the ambient dimension is q+1, and its support size is at most3*2^q.
The source's Lemma11 uses3*2^q in its bound; the present use needs only the upper bound, since some middle coefficients can cancel for even q.
Applying the retained common-exponent statement gives the explicit sufficient choice

    K_q=(product_(p prime,p<=3*2^q) p)
         lcm(1,...,ceil((q+4)^(q+1)*(q+1)^((q+1)/2))).   (1)

This K_q is even.
It kills the constant-x_0 values of all maximal torsion cosets and is sufficient whether or not it is the smallest possible killer exponent.
No optimization of K_q, logarithmic estimate for its size or claimed smallest possible Salem degree is needed.

<a id="ms05-arbitrary-distinct-prime-construction"></a>
## Exact construction interface and why the other primes may vary

Fix an EVEN q>=2.
Let K be an even common exponent as above, set k_1=K, and let k_2,...,k_q be ANY distinct rational primes not dividing K.
All exponents are at least2 and are pairwise coprime.
Then the source's construction and the checked applicability below give

    h_q(t,t^(k_1),...,t^(k_q))=2(t-1)^(q-1)P(t),
    P in Z[t] monic irreducible,
    P is the actual Salem minimal polynomial,
    deg P=2+sum_i k_i-(q-1),
    trace(P)=1-q/2.                                  (2)

There is NO additional cyclotomic factor in(2).
In the source Lemma12 the primes are initially chosen to be the smallest eligible ones.
Inspection of its proof shows that this minimality is used only for its separate degree upper bound; the following torsion, integrality and interlacing argument works for every distinct eligible choice.
This explicit quantifier clarification is the application check made here, not an attribution of a new optimized degree theorem to the source.

Let omega be a root of unity with h_q(omega,omega^(k_1),...,omega^(k_q))=0.
If two powered coordinates equal1, pairwise coprimality forces omega=1.
Otherwise Lemma10 puts the point on a maximal torsion coset with constant x_0, whose value omega is killed by K.
Then omega^(k_1)=1 supplies one powered coordinate equal to1, while exactly one is impossible on h_q=0.
Thus omega=1 is the only possible root of unity.

At t=1, the second part of h_q has exact order q-1, with nonzero leading coefficient

    -2(sum_j product_(i!=j) k_i).

The first part has order q+1, so the multiplicity of t=1 is exactly q-1.
Modulo2, every summand in the second part reduces to the same product, and the number q of summands is even.
Hence every coefficient of h_q is even, and monic division by(t-1)^(q-1) gives P in Z[t].

More explicitly, the reduced denominator for the positive rational sum is

    p(t)=product_i(t^(k_i)-1)/(t-1)^(q-1),
    q_0(t)/p(t)=(1/2)sum_i(t^(k_i)+1)/(t^(k_i)-1).

Pairwise coprimality makes p monic with simple circle zeros, and its only common denominator root is t=1 before reduction.
The parity just checked makes q_0 integral; positive residues prevent cancellation with p.
Proposition6 supplies circular interlacing, and p(1)=0 permits Proposition5(a).
The numerator(t^2-1)p-tq_0 is exactly P.
The root-of-unity exclusion removes its cyclotomic product; its actual degree is greater than2, excluding the reciprocal quadratic Pisot alternative.
This proves that the interface yields the actual irreducible Salem polynomial rather than an unspecified factor of a larger numerator.

The leading terms of h_q are2t^(2+sum k_i)-q t^(1+sum k_i).
Dividing by2(t-1)^(q-1) gives the stated degree and trace1-q/2.
No additional numerical-degree bound is asserted for arbitrary choices of the primes.
The source's final smallest-prime estimate and its prime-counting inputs are outside this unit's accepted numerical conclusions.

<a id="ms05-four-exponent-specialization"></a>
## Four powered coordinates and the RY26 notation match

Set q=4 in(1)--(2).
Then

    K_4=(product_(p prime,p<=48) p)
         lcm(1,...,ceil(8^5*5^(5/2))),
    h_4(t,t^K,t^a,t^b,t^c)=2(t-1)^3P(t),
    deg P=K+a+b+c-1,       trace(P)=-1,             (3)

for any distinct primes a,b,c coprime to this K.
This is exactly the displayed killer formula in RY26 equation(7.2) at its n=3, after identifying q=n+1 and renaming its distinguished x to x_0.
RY26's explicit formula was also read visually on page23, as retained in its [existing source unit](../RY26/Yin_U001.md#ry26-u001); no additional RY26 unit is necessary for this same parameter substitution.
The applicability in(3) is independently supplied by the identified MS05 statements and the proof checks above, rather than by inferring an extension from RY26's abstract.

The [existing RY26 exterior-root computation](../RY26/Yin_U001.md#exterior-root-measure-expense) supplies the separate bounded-measure interval for this fixed q; it is not repeated here.
Its n>=10^4 hypothesis is needed for its stronger every-large-degree prime-representation theorem, not for the individual four-exponent construction(3).
No all-large-degree conclusion follows from merely choosing arbitrary eligible primes.

## Accepted use and limits

The circular-interlacing statements, common torsion-coset exponent bound and construction interface above are accepted for this exact source use after checking their version, hypotheses and applicability.
The source itself is an established published construction; this acceptance does not assert independent auditing of its general torsion-coset theorem, underlying Mann/Schmidt inputs, the journal edition, or every quantitative estimate.
The chosen prime schedule, separated coefficient blocks, Gram obstruction and projection question belong to their separate project material; none is a theorem attributed to MS05.

Section8's reported finite computations replace the killer exponent by2 for particular prime tuples, and explicitly leave the corresponding general cyclotomic-freedom question unresolved.
Those computations do not replace K in(1) or certify an arbitrary varying-prime family with distinguished exponent2.
No small killer exponent, uniform projection bound, actual coherence growth or near-one family is supplied by this source unit.

<a id="original-moving-exponent-reviewer-reading"></a>
## Distinct original moving-exponent reviewer inspection

Retained 2026-10-22T01:16.
The original angular_envelope_review agent separately text-read the retained math/0308213v2 primary PDF on printed/PDF pages3--6 and8--10 and visually checked page9, as expressly reported in R547.
This is distinct from the entropy_attainment_bridge source-author occurrence above, whose complete selected Lemma12 proof/Lemmas10--11/Corollary9/interlacing reading and pages8--9 visual scope already supply the adequate author account.
The reviewer reconstructed the specific torsion classification, arbitrary eligible-prime application, exact factor removal and construction interfaces; general interlacing/exponent statements and original Mann/Schmidt proofs retain their declared external-premise and uninspected-proof boundaries.
No individual old reading minute is recorded; the source-unit22:05 registration, L40221:55 document and R54722:10 whole completion are not replacement reading minutes.
Current maintenance reads this adequate occurrence record and opens no PDF or new source passage, acquires no artifact and gives no whole-source or journal-edition equivalence verdict.
