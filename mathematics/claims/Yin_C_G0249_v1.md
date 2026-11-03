---
author: Yin
---

# Exact minimum cyclotomic repair and the small degree22 reciprocal control

This owns the entire original2026-10-07 finite-optimization and actual-unit proof, preserving its signed-correction and exact evidence boundaries.

## Statement

For monic irreducible p in Z[t] with constant±1 and a positive strictly dominant root lambda>1, write b_n for its integral normalized net traces, a_n=max(0,−b_n) and D=sum n a_n.
The canonical product of(t^n−1)^a_n is the unique least-degree repair among nonnegative cycle products.
For arbitrary cyclotomic products c=product Phi_m^e_m, e_m>=0 with finite support, the exact correction is f_n=sum_(n divides m)mu(m/n)e_m, its inverse is e_d=sum_(d divides n)f_n, and deg c=sum n f_n.
If D=0 the degree minimum is0 uniquely at c=1; otherwise the true minimum over all cyclotomic repairs is exactly the finite integer program below with1<=m,n<=2D^2,phi(m)<=D, degree<=D and every divisor constraint.
Every repair has degree at least max_(b_n<0)phi(n)(−b_n), without adding those separate bounds.

For the explicit q=t^24−t^17−t^12−t^7+1=Phi6 p and degree22 p below, the positive primitive24-vertex graph has26 edges and no closed walk of length below7.
Its exact b_1,...,b_6 for p are(−1,1,1,0,0,−1), all later b_n are nonnegative, the canonical repair has degree7 and the unique least-degree repair is Phi6 of degree2.
The explicit GF2 and real-embedding argument proves p irreducible of degree22; every positive power preserves degree.
The exact rational Sturm data prove eight unit-circle trace pairs and exactly three expanding conjugates of p.
Its total measure obeys1<M(p)<=lambda^3<(12/11)^3<13/10<theta0, while E(p)=2 and L(p)=5.
The two displayed completion lengths are20 for the degree29 canonical completion and5 for q of degree24.
These values do not imply a uniform relation among minimum degree, length, graph excess, binary interior or weighted entropy; the example is not Salem and does not refute Lehmer.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:07 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All Perron-unit inputs and finite cyclotomic multiplicities, exact signed correction coordinates and finite minimum-degree program with B=2D^2/all constraints, plus the complete irreducible degree22 unit control, exact unique Phi6 optimum and three-expanding/small-measure/all-power-degree scope. |
| argument | [Argument](#argument) | Complete Mobius inversions/degree identity, canonical-cycle uniqueness, totient cutoff and finite-program equivalence, pointwise lower bound; full graph positivity, polynomial/mod2/field/Sturm/trace/root and rational Mahler proof with every exact native control and no scan-to-universal inference. |
| dependency | [Complete repair input](Yin_C_G0240_v1.md#finite-nettrace-repair) | Integral net traces and eventual positivity for the exact Perron-unit domain, canonical cycle correction and its finite feasibility. |
| dependency | [Reciprocal excess lower bounds](Yin_C_G0234_v1.md#excess-two-equivalence) | E>=2 and L>=5, applied only after actual irreducibility/reciprocity/noncyclotomy is proved. |
| dependency | [Degree-preserving convex obstruction](Yin_C_G0239_v1.md#power-stable-canonical-obstruction) | Only the interpretation excluding the entire canonical convex body for the proved degree22 three-expanding unit; no interior or weighted-entropy theorem. |
| dependency | [Exact degree22 evidence](../computations/programs/Yin_J_G0003/readme.md#results-and-limits) | Retained full coefficient/multiplication/GF2/rational-sign/trace/bound data and positive-rescaled Sturm sequence with16-field alternate reconstruction; no new replay or floating-point root claim. |
| support | [Separate Salem branch](Yin_C_G0247_v1.md#excess-two-salem-classification) | Comparison only; none of the unit example, irreducibility, exact root count or Mahler proof depends on MS26 classification. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:15 |
| status | proved |
| reason | The complete retained current statement and all written proof parts were actually checked in the selected whole constructor self finding, with native evidence reused at its real scope. Source, all-index/finite, degree/entropy, zero and conditional limits remain explicit; no isolated review, new execution or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All Perron-unit inputs and finite cyclotomic multiplicities, exact signed correction coordinates and finite minimum-degree program with B=2D^2/all constraints, plus the complete irreducible degree22 unit control, exact unique Phi6 optimum and three-expanding/small-measure/all-power-degree scope. |
| argument | [Argument](#argument) | Complete Mobius inversions/degree identity, canonical-cycle uniqueness, totient cutoff and finite-program equivalence, pointwise lower bound; full graph positivity, polynomial/mod2/field/Sturm/trace/root and rational Mahler proof with every exact native control and no scan-to-universal inference. |
| review | [Actual complete self finding](../audits/reviews/Yin_R_G0524_v1.md#current-complete-minimum-repair-finding) | Entire current statement and every retained argument/interface at the exact selected scope; actual constructor self-review. |
| dependency | [Complete repair input](Yin_C_G0240_v1.md#finite-nettrace-repair) | Integral net traces and eventual positivity for the exact Perron-unit domain, canonical cycle correction and its finite feasibility. |
| dependency | [Reciprocal excess lower bounds](Yin_C_G0234_v1.md#excess-two-equivalence) | E>=2 and L>=5, applied only after actual irreducibility/reciprocity/noncyclotomy is proved. |
| dependency | [Degree-preserving convex obstruction](Yin_C_G0239_v1.md#power-stable-canonical-obstruction) | Only the interpretation excluding the entire canonical convex body for the proved degree22 three-expanding unit; no interior or weighted-entropy theorem. |
| dependency | [Exact degree22 evidence](../computations/programs/Yin_J_G0003/readme.md#results-and-limits) | Retained full coefficient/multiplication/GF2/rational-sign/trace/bound data and positive-rescaled Sturm sequence with16-field alternate reconstruction; no new replay or floating-point root claim. |
| support | [Separate Salem branch](Yin_C_G0247_v1.md#excess-two-salem-classification) | Comparison only; none of the unit example, irreducibility, exact root count or Mahler proof depends on MS26 classification. |

## Argument

### Scope and exact arithmetic coordinates

Let p be monic irreducible in Z[t], with p(0)=+1 or -1 and a positive root lambda>1 strictly greater in modulus than every other root.
With the conventions of L G0034, write

    s_n(p)=sum_(alpha root of p) alpha^n,
    b_n(p)=(1/n) sum_(j|n) mu(n/j) s_j(p).

These normalized net traces are integers, are additive under polynomial multiplication, and are positive for all sufficiently large n.
We use L G0034's proof of these facts.
A repair is a monic cyclotomic product c, possibly 1 or with repeated factors, for which b_n(pc)>=0 for every n>=1.
Set

    a_n=max(0,-b_n(p)),
    c_can=product_n (t^n-1)^(a_n),
    D=deg c_can=sum_n n a_n.

The finite product c_can is feasible.
Among products product_n(t^n-1)^(h_n) with all h_n nonnegative integers, it is the unique repair of minimum degree: the n-th factor changes only b_n, by h_n, so every feasible h_n must satisfy h_n>=a_n.
This statement does not extend to all cyclotomic products.

Indeed, if

    c=product_(m>=1) Phi_m^(e_m),       e_m>=0,

with finitely many nonzero e_m, the exact correction is

    f_n=b_n(c)=sum_(m: n|m) mu(m/n)e_m.                 (1)

To prove (1), use the finite rational factorization

    Phi_m(t)=product_(n|m)(t^n-1)^(mu(m/n))

and add the net-trace contributions; equivalently use the reciprocal formal Euler products in L G0034.
Negative exponents in this identity are permitted as rational identities and do not mean that c itself has a negative cyclotomic multiplicity.
Conversely,

    e_d=sum_(n: d|n) f_n,                              (2)
    deg c=sum_m phi(m)e_m=sum_n n f_n.                  (3)

Equation (2) follows by summing (1) and applying the divisor identity for mu; equation (3) uses sum_(n|m) n mu(m/n)=phi(m).
Thus a feasible correction can have negative f_n at indices where p already has a positive b_n.
The canonical repair deliberately avoids such transfers.

<a id="finite-minimum-repair-program"></a>
### An exact finite minimum-degree problem

If D=0, c=1 is the unique degree-minimizing repair.
Suppose D>=1 and put B=2D^2.
The true minimum degree among all cyclotomic repairs is the minimum of the following finite integer problem:

    variables: e_m in Z_(>=0), for 1<=m<=B with phi(m)<=D;

    minimize:  sum_m phi(m)e_m;

    subject to: sum_m phi(m)e_m<=D,
                b_n(p)+sum_(m: n|m) mu(m/n)e_m>=0
                for every 1<=n<=B.                    (4)

The variables automatically satisfy e_m<=floor(D/phi(m)).
Thus the search set is finite, and (4) characterizes the minimum exactly, without a relaxation or an unproved integrality property.

Here is the order cutoff.
For every positive integer m,

    phi(m)^2 >= m/2.                                  (5)

For a prime power ell^a, the ratio phi(ell^a)^2/ell^a is ell^(a-2)(ell-1)^2.
This is at least one for every odd prime and every a>=1.
For ell=2 its smallest value is 1/2, attained at a=1.
Multiplying over the prime factors proves (5), including m=1.
Any factor in a repair of degree at most D therefore has order m<=2D^2.
Every negative original index satisfies n<=D, since its positive integer contribution n a_n is part of D.
Consequently, for n>B the correction is zero and the original b_n(p) is nonnegative.
This proves both directions of the exact truncation in (4).

It is necessary to impose all constraints in (4), including originally nonnegative indices.
A proposed collection of cyclotomic factors may repair the original negative indices while producing new negatives at divisors of its orders.
Checking only the support of a_n is not a feasibility test.

A cheap lower bound, sometimes sharp, is

    deg c >= max_(n: b_n(p)<0) phi(n)(-b_n(p)).         (6)

For a fixed such n, (1) gives -b_n(p)<=f_n<=sum_(m: n|m)e_m.
If n divides m then phi(n)<=phi(m), as follows prime by prime from the product formula for phi.
Therefore deg c>=phi(n) sum_(m: n|m)e_m, proving (6).
The maximum over separate indices is valid; their bounds cannot in general be added, since one cyclotomic factor can affect several indices.

This is a finite optimization after the original polynomial's canonical D has been determined.
It supplies no degree-independent bound on D, on the resulting matrix dimension, on edge excess, or on algebraic entropy.
The [Salem-specific degree cutoff](Yin_C_G0250_v1.md#degree-only-repair-budget) can be used to determine D in that class; it is not needed for the example below.

<a id="degree22-small-core-counterexample"></a>
### A repair of degree two where the canonical repair has degree seven

Define

    q(t)=t^24-t^17-t^12-t^7+1,
    p(t)=t^22+t^21-t^19-t^18+t^16-t^14-t^13+t^11
         -t^9-t^8+t^6-t^4-t^3+t+1.

Exact multiplication gives

    q=Phi_6 p,              Phi_6=t^2-t+1.             (7)

We first prove all net-trace signs without an infinite numerical search.
Take the directed graph with vertices u_0,...,u_6 and v_0,...,v_16.
Include the forward cycle through all u vertices, the forward cycle through all v vertices, and the two cross arrows

    u_6 -> v_0,             v_4 -> u_0.

All edge weights are +1.
Its simple directed cycles have lengths 7, 17 and 12.
Only the 7- and 17-cycles are disjoint.
Expanding det(tI-A) by disjoint directed cycles gives exactly q.
There are 24 vertices and 26 edges.
The graph is strongly connected, and the 7- and 12-cycles through u_0 have coprime lengths, so A is primitive.
Its normalized net traces b_n(q) count primitive directed periodic orbits and are nonnegative for every n.
There is no nonempty directed closed walk of length below 7, hence b_n(q)=0 for 1<=n<=6.

By (1), the only nonzero corrections from Phi_6 are

    b_1(Phi_6)=1,     b_2(Phi_6)=-1,
    b_3(Phi_6)=-1,    b_6(Phi_6)=1.

Thus

    (b_1(p)...,b_6(p))=(-1,1,1,0,0,-1),
    b_n(p)=b_n(q)>=0 for every n>=7.                  (8)

The canonical repair is

    c_can=(t-1)(t^6-1)=Phi_1^2 Phi_2 Phi_3 Phi_6,
    deg c_can=7.

In contrast, c=Phi_6 repairs all indices by (7), and has degree two.
It is the unique degree-minimizing repair.
Every repair has degree at least phi(6)=2 by (6).
At degree two the only available cyclotomic orders are 1,2,3,4,6, and only order 6 can change b_6.
Therefore the entire degree budget must be spent on one copy of Phi_6.
In particular the correction simultaneously removes the negative b_1 and b_6, spending the available positive b_2 and b_3.
No arbitrary integer net-trace sequence is being presented as an algebraic-unit spectrum.

Coefficient length also differs in this example:

    deg(p c_can)=29,       ||p c_can||_1=20;
    deg(p Phi_6)=24,       ||p Phi_6||_1=5.

These are values of the two displayed completions, not a general relation between minimum repair degree and minimum coefficient length.

### Exact irreducibility and Perron properties

Define C_0(y)=2, C_1(y)=y, C_j(y)=y C_(j-1)(y)-C_(j-2)(y).
Then C_j(t+t^(-1))=t^j+t^(-j).
The trace identity is

    C_12(y)-C_5(y)-1=(y-1)Q(y),

    Q(y)=y^11+y^10-11y^9-11y^8+43y^7+43y^6
         -69y^5-70y^4+35y^3+40y^2+4y-1,

    p(t)=t^11 Q(t+t^(-1)).                            (9)

For a reproducible mod-2 irreducibility certificate, encode a binary polynomial sum a_i y^i by the integer sum a_i 2^i.
The reduction of Q has code 4073.
The successive remainders of y^(2^j) modulo this polynomial, for j=1,...,11, have codes

    4, 16, 256, 944, 1909, 791, 908, 549, 1336, 596, 2.

In particular Q mod 2 divides y^(2^11)-y.
Its values at 0 and 1 are both 1.
Since 11 is prime, every irreducible factor of a divisor of y^(2^11)-y has degree 1 or 11; the linear factors have been excluded.
Hence Q mod 2, and therefore Q over Q, is irreducible of degree 11.

Also Q(0)=-1 and Q(1)=5, so Q has a real root y_0 in (0,1).
The primitive matrix above has a simple positive spectral radius lambda.
Since q(1)=-1 and q(t) tends to positive infinity, q has a real root greater than one and therefore lambda>1.
Its other roots have strictly smaller modulus.
By (7), lambda is a root of p.
Let y=lambda+lambda^(-1).
Equation (9) and irreducibility of Q give [Q(y):Q]=11.
The field Q(y) has a real embedding sending y to y_0, under which y^2-4 is negative.
Consequently y^2-4 is not a square in Q(y).
The quadratic t^2-yt+1 is irreducible over Q(y), and

    [Q(lambda):Q]=22.

Thus p itself is the minimal polynomial of lambda.
It is monic reciprocal with constant coefficient one, and lambda is its unique conjugate of maximal modulus.

For completeness this last property gives degree preservation under every positive power.
Put L=Q(lambda), K=Q(lambda^k).
Every embedding of K into C has [L:K] extensions.
The extensions of the identity embedding send lambda to roots z of p satisfying z^k=lambda^k and hence |z|=lambda.
Uniqueness of the maximal-modulus conjugate forces z=lambda, leaving exactly one extension.
Thus [L:K]=1 for every k>=1.
This is the same field-fiber criterion as [the retained L17 field-fiber proof](Yin_C_G0220_v1.md#reciprocal-discriminant-family).

### An exact upper bound inside the small reciprocal core

For t>1,

    q(t)/t^12
      =(t^(7/2)-t^(-7/2))(t^(17/2)-t^(-17/2))-1.

The product is strictly increasing from zero to infinity.
Hence q has exactly one positive root above one.
The exact evaluation

    q(12/11)=18502323789625876807201
             /9849732675807611094711841 >0

implies lambda<12/11.
The following table supplies eight disjoint sign changes of Q in (-2,2); all displayed rational values are exact.

| a | b | Q(a) | Q(b) |
| --- | --- | --- | --- |
| -2 | -31/16 | -1 | 14120013278129/17592186044416 |
| -19/16 | -9/8 | 5041040784485/17592186044416 | -2317867217/8589934592 |
| -11/16 | -5/8 | -50562228931/17592186044416 | 2987333803/8589934592 |
| -5/16 | -1/4 | 2692471637939/17592186044416 | -1028365/4194304 |
| 1/16 | 1/8 | -10314936859375/17592186044416 | 1497634633/8589934592 |
| 17/16 | 9/8 | 40018870499009/17592186044416 | -2912590367/8589934592 |
| 3/2 | 25/16 | -2783/2048 | 15041332398809/17592186044416 |
| 29/16 | 15/8 | 24923802664949/17592186044416 | -14288048777/8589934592 |

Each real trace root in (-2,2) gives two distinct roots of p on the unit circle.
Thus at least 16 of p's 22 roots lie on the unit circle.
Reciprocity leaves at most three roots outside that circle, counted with multiplicity.
Each has modulus at most lambda by primitivity, so

    1<M(p)<=lambda^3<(12/11)^3=1728/1331<13/10<theta_0, (10)

where theta_0 is the positive root of x^3-x-1.
The last comparison follows because (13/10)^3-13/10-1<0 and x^3-x-1 is strictly increasing for x>=1.
This proves the requested small-Mahler scope without a floating-point root computation.

The exact rational Sturm certificate in J G0003 (`mathematics/computations/outputs/Yin_J_G0003/verification.json`) determines the entire trace-root pattern without invoking a Salem classification.
For the sequence beginning with Q,Q' and successive negative Euclidean remainders, its variation counts are

    V(-infinity)=10,  V(-2)=10,  V(2)=2,  V(+infinity)=1.

The retained sequence rescales each polynomial by a positive rational to a primitive integer polynomial; all endpoint signs are preserved.
Q is irreducible in characteristic zero, hence squarefree, and Q(-2) and Q(2) are nonzero.
Sturm's theorem therefore gives exactly eight roots in (-2,2), one in (2,infinity), none below -2, and two nonreal roots.
Under (9), each of the eight interior trace roots gives two unit-circle roots; the real trace root above two gives one reciprocal positive pair.
Each nonreal trace root gives two reciprocal roots off the unit circle, with exactly one outside: a unit-circle root would have real trace in [-2,2], and the two roots have product one.
Thus p has exactly three expanding conjugates, one positive real and a nonreal conjugate pair.

The graph above is unimodular, has Frobenius excess two, and gives a coefficient-length-five cyclotomic completion of p.
The reciprocal noncyclotomic lower bounds in [L G0033](Yin_C_G0234_v1.md#excess-two-equivalence) imply E(p)=2 and L(p)=5.
In particular p is not Salem.
This is consistent with [L G0036](Yin_C_G0247_v1.md#excess-two-salem-classification), whose Salem members have minimal degree at most 20, but none of the root-count, repair, irreducibility or Mahler-bound conclusions here requires that classification or its MS26 source scope.

### Changed next action and boundaries

The canonical finite cycle repair is an existence certificate, and it should not be used as a minimum-complexity completion even in the small reciprocal, all-power-degree-preserving Perron class.
For a concrete input, compute the finite signed cyclotomic correction problem (4), retaining all divisor constraints.
The lower bound (6) can sometimes certify the optimum without enumerating the full search set; it certifies the example above.

This example also supplies an actual unit control for the multiple-expanding excess-two branch left open by L G0036, with expanding real dimension three and M<theta_0.
Its all-power degree preservation rules out the canonical binary convex cover by [L G0035](Yin_C_G0239_v1.md#canonical-convex-classification).
Neither that failure nor its very short positive graph presentation determines whether the binary attractor has positive volume, and neither is a lower bound for weighted digit entropy.
The graph entropy log(lambda) is strictly smaller than the algebraic entropy log M(p) here, since two further conjugates expand.
A repair minimizes neither this entropy discrepancy nor the dimension or zero padding in the external realization theorem.
