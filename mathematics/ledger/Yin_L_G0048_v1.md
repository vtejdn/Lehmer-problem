---
author: Yin
---

# G0001: reciprocal length-six graphs and their neutral block types

The complete current mathematical home is [Yin_C_G0269_v1](../claims/Yin_C_G0269_v1.md#argument), adopted at 2026-10-21T06:39 after the [actual complete current self-check](../audits/reviews/Yin_R_G0532_v1.md#current-complete-length-six-finding).
The original2026-10-07 mathematics and still-needed fixed review input below retain their original scope and date; this is no new research run.


Date: 2026-10-07.
Direct derivation by assigned AI assess_shortness_route for Yin.
The coordinating AI checked the positive graph construction and requested its inclusion.
The assigned AI review_matrix_completion supplied the final scalar-division control and independently checked the sign argument.
The coordinator supplied the unbounded essential-block family; the separate reviewer independently checked it and derived its exact negative net-trace budget, and the coordinator checked the ensuing repair bounds.
The complete proof has been checked at the review scopes recorded below.

<a id="reciprocal-length-six-presentation"></a>
## Scope and conclusions

Let p be a monic irreducible reciprocal unit polynomial with a positive uniquely maximal-modulus root lambda>1 and 1<M(p)<theta_0, where theta_0 is the positive root of x^3-x-1.
Suppose that q=p c, with c a monic cyclotomic product, satisfies

    q*=q,       q(0)=1,       ||q||_1=6.                       (1)

The condition q*=q is explicit.
A completion of a reciprocal p can instead be anti-reciprocal when c contains Phi_1 with odd multiplicity; those completions are addressed separately below.
We do not infer (1) from L(p)=6 without checking this sign.

Then q has the form

    q=t^D+1-t^a-t^(D-a)-t^b-t^(D-b),
    1<=a<=b<=D/2,       gcd(D,a,b)=1,       b>=2.             (2)

The four negative terms count coefficient units, not necessarily four distinct exponents.
There is a primitive nonnegative integral unimodular matrix with characteristic polynomial exactly q, dimension D, and nonnegative edge excess three.
If b<D/2 it has only zero-one entries and Frobenius excess three.
If b=D/2, the construction has one entry two, edge excess three, and Frobenius excess five.
No zero padding is needed.
This does not bound D-deg p or the cyclotomic repair degree.

For a cyclotomic factor Phi_m of q, either m divides 30, or q contains an entire factor of one of the forms

    t^g+1,             Phi_6(t^g)=t^(2g)-t^g+1,              (3)

with g>=1 and respectively m/gcd(m,g)=2 or 6.
In a sequence with unbounded m, the corresponding g is unbounded.
This is an arithmetic constraint on possible neutral factors, not an automatic operation deleting them at edge excess three.

One exact family identity below deletes a Phi_6(t^g) block while preserving length six and, within the stated core scope, permits a positive realization at the same edge excess.
A separate reciprocal primitive-graph family shows that simple scalar division may increase coefficient length without bound even at edge excess three.
A further explicit family has an entire high-order block no nonconstant part of which can be deleted into any nonnegative exact residual realization.
Its quotient has bounded Mahler measure, canonical budget 2g, and optimized repair degree exactly g when g is a power of two at least four.
The quotient may be reducible and is not asserted to have Mahler measure below theta_0.
These missing hypotheses are substantive: the general small-core neutral reduction question remains unresolved.

Only the directly proved interfaces in [L G0044](Yin_L_G0044_v1.md#minimal-vanishing-order) and [L G0045](Yin_L_G0045_v1.md#five-root-vanishing-classification), and the necessary net-trace deletion criterion in [L G0047](Yin_L_G0047_v1.md#girth-window-deletion) are reused.
No length-six Salem list, new external theorem, numerical search or novelty assertion is used.

## The sign normal form, including repeated coefficients

Write D=deg q.
The monic leading and constant coefficients contribute two units of coefficient length, leaving four interior units.
Reciprocity pairs the coefficients at j and D-j.
In even degree the central coefficient is therefore even, since every other contribution to length is even.
Consequently the total absolute mass of the negative interior coefficients is even.

If that negative mass is at most two, evaluate q at t=exp(u)>1 and divide by t^(D/2).
The endpoint contribution is 2cosh(Du/2).
A negative pair of total mass two has magnitude 2cosh((D/2-j)u), strictly less than the endpoint contribution.
A central coefficient -2 has magnitude two, also strictly smaller.
All remaining contributions are nonnegative.
Thus q(t)>0, contrary to q(lambda)=0.
The negative interior mass must be four: all interior coefficients are negative.

Four negative units in a reciprocal polynomial can always be listed as two reciprocal pairs, producing (2) before the gcd and b restrictions.
This includes a=b (a pair of coefficients -2), b=D/2 (a central -2), and a=b=D/2 (a central -4).
In particular q(1)=-2, independent of these coincidences.
The last case has q=t^(2a)-4t^a+1 and Mahler measure 2+sqrt(3), so it cannot occur in the small core, though the displayed normal form itself includes it.

If g_0=gcd(D,a,b)>1, then q(t)=Q(t^(g_0)).
All the distinct numbers lambda epsilon, for epsilon in the g_0-th roots of unity, would be roots of q of modulus lambda>1.
They cannot belong to c, and hence are conjugates of p.
This contradicts the uniquely dominant conjugate.
Therefore g_0=1.
This is the same precise unique-core use as in L G0045; global support gcd one is not a claim about proper vanishing subsums.

If b=1 then a=1.
At any positive root lambda>1, (2) gives

    lambda^(D-1)(lambda-2)=2lambda-1>0,

also when D=2 and the central coefficients coincide.
Hence lambda>2, contradicting M(p)<theta_0<2.
Thus b>=2 in the stated core scope.

<a id="six-term-positive-graph"></a>
<a id="positive-length-six-graph"></a>
## A positive primitive graph for every such reciprocal completion

Take disjoint positive directed cycles of lengths a and D-a, with vertices u_0,...,u_(a-1) and v_0,...,v_(D-a-1).
Add three arrows, counting multiplicity:

    u_0 -> v_0,
    v_(b-2) -> u_0,
    v_(D-b-2) -> u_0.                                   (4)

Both return indices lie between zero and D-a-1, because 2<=b<=D/2 and a<=b.
Their positions are distinct unless b=D/2, when there are two parallel arrows in that position.
All added arrows connect the two different cycles and are absent from the base cycles, even if a=1.
The graph has D vertices and D+3 arrows with multiplicity, giving edge excess three.
The sole entry two in the parallel case contributes two additional units to Frobenius excess, explaining the stated value five rather than three.

Its simple directed cycles are the two base cycles, of lengths a and D-a, and the two mixed cycles through u_0, of lengths b and D-b.
The mixed cycles use the common arrow u_0->v_0; when their return positions coincide they are counted as two choices of labelled parallel edge.
A simple cycle cannot first traverse the u base cycle and then leave u_0, since that would repeat u_0.
Nor can it travel beyond its chosen return vertex and then return to it by making a full v cycle without repeating vertices.
This exhausts the possibilities.

Only the two base cycles are vertex-disjoint.
Their product gives the positive constant term in the characteristic polynomial; each of the four single cycles gives its negative term.
Thus the determinant cycle expansion gives exactly (2), including repeated-coefficient cases.
The constant coefficient one shows det A=(-1)^D, so A is unimodular.

The graph is strongly connected: every u vertex reaches u_0 and enters the v cycle, and every v vertex can reach a return arrow to u_0.
Its closed-walk period is the gcd of the four simple-cycle lengths, namely gcd(D,a,b)=1.
Equivalently, decompose closed walks into simple cycles to see that these lengths generate the period gcd.
A finite strongly connected graph of period one is primitive.
It follows that A is a positive primitive realization of q, with m(A)=m(p), because c is cyclotomic.

This supplies the presentation asserted in the statement.
It neither constructs a quotient for an arbitrary neutral factor nor identifies Frobenius excess with nonnegative edge excess when entries exceed one.

<a id="six-term-neutral-block-dichotomy"></a>
## A complete decomposition alternative for high-order unit roots

Expand each nonzero coefficient of q into signed unit terms.
There are exactly six such terms, counting multiplicities.
At a root of unity zeta of order m, absorb the signs into the roots of unity.
The resulting vanishing sum either is minimal or splits into minimal components.

If it is minimal, the original rational-coefficient relation among the distinct monomials is also minimal: any vanishing proper subset of monomials would give a proper vanishing subset of the six unit terms.
The rational relative-order theorem of L G0044 and the global support gcd one imply m divides P_s, where s<=6 is the number of distinct monomials.
In particular m divides 30.

Otherwise the only possible minimal-component sizes are 2,3,5,6, because L G0045 excludes size four and a nonzero singleton cannot vanish.
The partitions of six into such proper component sizes are therefore exactly 2+2+2 and 3+3.
The components are respectively three opposite pairs or two regular triangles.
Repeated coefficients have not been discarded in this argument; they are represented by repeated unit terms.

For a component I, let g_I be the gcd of the differences of its original exponents, before absorbing signs.
This gcd is positive.
Indeed two opposite signed unit terms in the polynomial cannot have the same exponent, since all units at a collected exponent have the same sign; similarly a minimal triangle cannot consist entirely of the same signed unit.
Set g=gcd_I g_I and b=m/gcd(m,g).
The exact subgroup identity from L G0044 gives

    b=lcm_I [m/gcd(m,g_I)].                              (5)

For an opposite pair, the original root ratio is 1 or -1, so its order is 1 or 2.
For a regular triangle, the signed ratios have order three; undoing the original signs makes the group of original ratios have order 3 or 6.
It cannot have order one or two, since three signed units then cannot sum to zero.
Thus the first partition type gives b in {1,2}, and the second gives b in {3,6}.

The component polynomials are t^(r_I)F_I(t^g), with integer F_I, and F_I(zeta^g)=0.
The element zeta^g has exact order b, so each F_I is divisible by Phi_b and hence

    Phi_b(t^g) divides q(t).                             (6)

This argument remains valid when copies of one monomial are assigned to different components: the component polynomials still have integer coefficients and sum to q.
It does not require disjoint supports of those component polynomials.

Finally q(1)=-2 rules out b=1, since Phi_1(1)=0, and b=3, since Phi_3(1)=3 cannot divide -2.
It leaves exactly b=2 or b=6, proving (3).
This is a restriction arising from the specific component sizes; it is not a claim that evaluating at 1 excludes every odd composite base order.
Since m=b gcd(m,g)<=6g, an unbounded m in this alternative forces g to be unbounded.

<a id="controlled-phi6-deletion"></a>
## One exact block deletion with controlled scalar and graph complexity

Use distinct names for two trinomials:

    F(x)=x^5-x^4-1,       H(x)=x^3-x-1.

Direct multiplication gives

    F(x)=Phi_6(x)H(x).

Because Phi_6 is reciprocal, F*(x)=Phi_6(x)H*(x), with reciprocity taken in the respective degrees five and three.
Consequently, for N,g>=1,

    [t^N F(t^g)+F*(t^g)] / Phi_6(t^g)
       =t^N H(t^g)+H*(t^g).                            (7)

Both the numerator and quotient are monic reciprocal polynomials of coefficient length six: each has positive endpoint coefficients and four negative interior coefficient units, allowing coincident exponents.
Their degrees are N+5g and N+3g.
The neutral factor in (7) has degree 2g and includes primitive roots of order 6g, so its orders and degree can grow without changing the coefficient length.

If the numerator is an eligible q=p c in (1), the quotient is another completion of exactly the same p and has the same Mahler measure.
Its support gcd is gcd(N,g), which must be one by the uniquely dominant core.
Its normal-form parameter b is at least two by the same small-core argument above.
Both polynomials therefore admit the positive primitive edge-excess-three realizations of (4).
This is an actual entropy-neutral algebraic replacement, with a fresh graph realization at the same edge budget and with dimension lowered by 2g.
It does not assert an equitable quotient or a graph surgery relating the two particular matrices.

No existence of infinitely many eligible small-core numerators in this identity is asserted.
The implication is conditional on that input, and does not replace the general deletion obligation for other block patterns.

<a id="scalar-division-positive-graph-obstruction"></a>
## Scalar division can still have unbounded cost within positive graphs

For n>=2, consider the family supplied by review_matrix_completion:

    Q_n(t)=t^(2n+1)+1-t^(n+2)-t^(n+1)-t^n-t^(n-1).

It is in the normal form with D=2n+1, a=n-1 and b=n.
All four negative exponents are distinct.
Its support gcd is one, b>=2, and hence the graph above gives a primitive zero-one unimodular presentation of dimension 2n+1 and edge excess three.
Also Q_n(1)=-2, so it has a positive real root greater than one.

Despite this positive presentation, direct division gives

    Q_n(t)/(t+1)
       =sum_(j=0)^(2n) (-1)^j t^j - t^(n-1)(t^2+1).     (8)

Multiplication by t+1 proves the identity: the alternating sum gives t^(2n+1)+1, and the other product gives the four consecutive negative terms.
If n is even, the two altered coefficients were -1 and become -2, so the quotient length is 2n+3.
If n is odd, they were +1 and become zero, so the length is 2n-1.
In either case it is unbounded, although ||Q_n||_1=6 and its positive graph excess stays three.

This strengthens the broad scalar-division warning in L G0044 to the reciprocal positive primitive graph class.
It still does not show that the quotient lacks a different positive graph of bounded excess, nor that the deleted factor is essential.
The example deletes the fixed factor Phi_2, so it is not an unbounded-order counterexample.
No unique irreducible noncyclotomic core or M<theta_0 is asserted.
In particular it does not refute the existential small-core conjecture.

<a id="unbounded-essential-block-family"></a>
## Unbounded essential orders and repair degrees in an explicit broader family

The coordinating AI supplied the following exact family.
For g>=3 put

    D=7g,       a=2g+1,       b=3g+1,

    q_g(t)=t^(7g)+1-t^(2g+1)-t^(5g-1)
                       -t^(3g+1)-t^(4g-1).              (9)

The inequalities 1<=a<=b<D/2 hold, and gcd(a,b)=1 because their difference is g and gcd(2g+1,g)=1.
Thus (4) gives a primitive zero-one unimodular graph with 7g vertices, 7g+3 arrows and edge excess three.
Its four distinct simple-cycle lengths are

    2g+1,       5g-1,       3g+1,       4g-1.

Its girth is therefore gamma=2g+1.
In particular b_j(q_g)=0 for 1<=j<=2g.
These assertions follow directly from the complete cycle description above, not from a finite graph scan.

Let

    S_6(x)=x^6-x^5+x^4-x^3+x^2-x+1,
    r_g(t)=S_6(t^g)-t^(2g+1)-t^(4g-1).

Since (x+1)S_6(x)=x^7+1, direct multiplication gives

    q_g(t)=(t^g+1)r_g(t).                               (10)

Every cyclotomic order in t^g+1 divides 2g and does not divide g, so all these orders are at most 2g<gamma; the block includes Phi_(2g).
If d is any nonconstant cyclotomic divisor of t^g+1, take the largest order m in d, with multiplicity h_m>0.
No larger multiple of m occurs in d, so b_m(d)=h_m.
But b_m(q_g)=0 because m<gamma.
Hence

    b_m(q_g/d)=-h_m<0.

This rules out every nonnegative integer matrix with nonzero characteristic polynomial q_g/d, irrespective of dimension, additional zero eigenvalues or edge budget.
It is exactly the necessary direction of L G0047's criterion; no KOR00 sufficiency theorem is needed.
Thus no nonconstant part of this explicit high-order neutral block is deletable while retaining exactly the other nonzero spectrum.

There is also a quantitative repair consequence for the entire quotient r_g, without assuming it irreducible.
Define D(r_g) and R_*(r_g) by the same canonical negative-net-trace budget and minimum cyclotomic repair degree as before, applied to this whole polynomial.
The identity

    t^g+1=(t^(2g)-1)/(t^g-1)

gives net-trace corrections -1 at g, +1 at 2g and zero elsewhere.
Since both indices are below the girth,

    b_g(r_g)=1,       b_(2g)(r_g)=-1,

and every other b_j(r_g) equals the nonnegative graph count b_j(q_g).
Consequently

    D(r_g)=2g.                                          (11)

Any cyclotomic repair of r_g must contribute positively at index 2g.
Thus at least one factor Phi_m in it has order divisible by 2g; its degree is at least phi(2g), since phi is nondecreasing under divisibility.
The original block t^g+1, of degree g, is a repair back to q_g.
Therefore

    phi(2g)<=R_*(r_g)<=g.                               (12)

For the subsequence g=2^k with k>=2, phi(2g)=g and hence R_*(r_g)=g exactly.
This proves unbounded optimized repair degree without an asymptotic estimate for the totient.
Every repair also contains an order at least 2g, so allowing a different cyclotomic repair does not create a bounded-order choice for this broader family.

The polynomial r_g is monic, reciprocal, has constant coefficient one and degree 6g, and retains the graph's positive simple strictly dominant root after the roots of t^g+1 are deleted.
It is a reciprocal Perron unit polynomial in this explicit sense, not an asserted irreducible minimal polynomial.
Its Mahler measure is uniformly bounded: q_g has six distinct unit coefficients for g>=3, so Jensen--Parseval gives

    1<M(r_g)=M(q_g)<=sqrt(6).                            (13)

The strict lower inequality follows from the positive Perron root greater than one, which exists because q_g(1)=-2.
Thus unbounded actual repair degree already occurs with bounded Mahler measure and a length-six completion having a primitive edge-excess-three realization.

The missing target hypotheses are explicit.
Neither irreducibility of r_g nor M(r_g)<theta_0 has been proved; r_g may retain additional cyclotomic or noncyclotomic factors.
A chosen irreducible factor cannot inherit (11)--(12) without accounting for the net traces of all other factors.
Different repairs are allowed in (12), but the bounds concern the whole r_g.
This does not refute the irreducible small-core question.
It identifies this precise family and its factorization/measure conditions as a concrete next arithmetic test.

<a id="anti-reciprocal-boundary"></a>
## The anti-reciprocal boundary

If q=p c instead has q*=-q and ||q||_1=6, its constant coefficient is -1.
Its central coefficient is zero, and the four interior units form two antisymmetric pairs, allowing repetition of a pair.
Write

    q=t^D-1+epsilon(t^(D-a)-t^a)
                +delta(t^(D-b)-t^b),
    1<=a<=b<D/2,       epsilon,delta in {1,-1}.

For t=exp(u)>1, divide by t^(D/2).
The endpoint contribution is 2sinh(Du/2), and the two other contributions are 2epsilon sinh((D/2-a)u) and 2delta sinh((D/2-b)u).
Since each interior frequency is strictly smaller than D/2, a positive root forces epsilon=delta=-1.
Such a root also requires D>2(a+b): if D<=2(a+b), then D/2 is at least the sum of the two interior frequencies, and sinh(v+w)>sinh(v)+sinh(w) for positive v,w makes the expression strictly positive.
Thus the anti-reciprocal normal form is

    q=t^D-1-t^(D-a)+t^a-t^(D-b)+t^b,
    D>2(a+b).                                           (14)

The uniquely dominant core again forces gcd(D,a,b)=1.
The same six-unit-term decomposition gives either m|30 or a full Phi_b(t^g) block with b in {1,2,3,6}.
But here q(1)=0: bases one and three cannot be excluded by the previous value-at-one argument.
No positive graph or controlled deletion for all cases of (14) is proved here.

Accordingly the concrete advances are the full positive graph for the reciprocal sign in (1), the two possible high-order neutral block types there, the exact replacement (7), and the bounded-Mahler family (9)--(13) with unbounded essential repair.
The latter rules out a general bounded-repair assertion for whole possibly reducible Perron unit polynomials.
A conclusion for the irreducible small core still requires resolving the stated factorization and measure hypotheses, together with the separate anti-reciprocal boundary; no general bounded-excess reduction in that target scope has been proved.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0013_v1.md#review-boundary), with its original inspected scope and relationship.
