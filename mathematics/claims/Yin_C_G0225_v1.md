---
author: Yin
---

# Complete opposite-pair classification and controlled deletion for reciprocal length six

This retains the complete original2026-10-07 proof by review_matrix_completion for Yin from [L53](../ledger/Yin_L_G0053_v1.md), with the coordinator's prospective-pattern contribution and original review roles preserved separately.

## Statement

Let

    q=t^D+1-t^a-t^(D-a)-t^b-t^(D-b),
    1<=a<=b<=D/2, gcd(D,a,b)=1,

with integer parameters and four negative labelled coefficient units, allowing repeated exponents.
At a root of unity suppose these six signed units admit a partition into three opposite pairs, and let g be the gcd of the original within-pair exponent differences.
Every such difference is nonzero for an actual matching.
The fifteen labelled matchings consist of nine order-two/g=1 cases and the following two general types, up to the stated reflections and relabelling.
In both types zeta^g=-1, and the stated parameter conditions are also sufficient for the matching at every root of t^g+1.

TypeI has pairs(0,D),(u,v),(D-u,D-v), where

    D=Lg, v-u=Kg, L>K>=1 odd, gcd(L,K)=1,
    0<u<(L-K)g, gcd(u,g)=1.

Writing x=t^g and S_j(x)=(x^(j+1)+1)/(x+1) for even j, its exact quotient is

    q/(t^g+1)=S_(L-1)(x)-(t^u+t^((L-K)g-u))S_(K-1)(x).

TypeII pairs the two endpoints to the same reciprocal pair; choose its representative a as the exponent paired with0, and reflect the other pair so0<b<D/2.
Its exact parameters and quotient are

    a=2rg, D=2b+Lg, r>=1, L>=1 odd,
    gcd(2r,L)=1, gcd(b,g)=1, 2rg<2b+Lg,
    q/(t^g+1)=T_(2r-1)(x)(1-t^(2b)x^(L-2r))-t^b S_(L-1)(x),
    T_(2r-1)(x)=(1-x^(2r))/(1+x).

The two-variable display may be Laurent, while the actual specialized exponent D-a is positive.
For integer g>=2, TypeI L=3,K=1 and TypeII r=1,L=1 each give an explicit coprime length-five quotient, a primitive zero-one unimodular realization of edge excess2, and full entropy preservation with dimension reduced by g.
Thus these cases cannot witness minimum cyclotomic coefficient length exactly6.
For every such g>=2 graph, deleting t^g+1 into an arbitrary nonnegative integer realization of exactly the other nonzero spectrum, with zero padding allowed, is equivalent to b_(2g)(q)>=1.
All TypeII r=1 cases and all TypeI L-K=2 cases satisfy that criterion, with complete simple-cycle or primitive-concatenation witnesses.
Those broader spectral deletions have no claimed edge-excess bound.
No matching with an equal-exponent same-sign pair is included; no triangular/minimal-six classification, general K=1 restriction, higher-pattern measure bound or unrestricted completion theorem is inferred.

## Current assessment
[Selected decision](#decision-current-complete-proof-homes)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:39 |
| status | open |
| reason | Register the exact complete matching, factorization and controlled/spectral deletion theorem; actual current full statement/proof/interface checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All labelled matchings, repeated coefficients, precise TypeI/II converse domains, specialized positivity, g>=2 controlled graph reductions and exact broader spectral-deletion witnesses and limitations. |
| argument | [Complete retained argument](#argument) | Entire fifteen-match classification, parity/gcd elimination, both full factorizations, both coprime length-five constructions, g>=2 boundary and actual primitive-orbit witnesses. |
| dependency | [Length-five positive graph](../ledger/Yin_L_G0045_v1.md#uniform-repair-bounds) | Exact primitive zero-one unimodular graph for coprime t^(2n)+1-t^n-t^k-t^(2n-k), edge excess2 and repeated endpoint boundaries; no sharp degree34 computation. |
| dependency | [Exact nonzero-spectrum criterion](../ledger/Yin_L_G0047_v1.md#exact-spectral-deletion) | Necessary primitive-orbit nonnegativity and accepted KOR00 sufficiency for positive strictly dominant integral spectra, zero padding permitted and no dimension/excess bound. |
| dependency | [Six-term primitive graph](../ledger/Yin_L_G0048_v1.md#positive-length-six-graph) | Full labelled simple-cycle graph once g>=2 implies the required b>=2 condition; parallel and repeated coefficient cases retained. |
| support | [General K1 measure boundary](Yin_C_G0224_v1.md#general-k1-measure-corollary) | Only the already adopted full-delay measure reduction at K=1, without extending its central-offset exact repair or asserting finiteB empty. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:48 |
| status | proved |
| reason | Adopt the exact complete retained matching/deletion theorem after actual whole current self-review of every original matching, converse, graph and spectral interface; all integer/gcd/positivity boundaries and limitations are explicit, with no substantive proof repair or new independent-review assertion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All labelled matchings, repeated coefficients, precise TypeI/II converse domains, specialized positivity, g>=2 controlled graph reductions and exact broader spectral-deletion witnesses and limitations. |
| argument | [Complete retained argument](#argument) | Entire fifteen-match classification, parity/gcd elimination, both full factorizations, both coprime length-five constructions, g>=2 boundary and actual primitive-orbit witnesses. |
| dependency | [Length-five positive graph](../ledger/Yin_L_G0045_v1.md#uniform-repair-bounds) | Exact primitive zero-one unimodular graph for coprime t^(2n)+1-t^n-t^k-t^(2n-k), edge excess2 and repeated endpoint boundaries; no sharp degree34 computation. |
| dependency | [Exact nonzero-spectrum criterion](../ledger/Yin_L_G0047_v1.md#exact-spectral-deletion) | Necessary primitive-orbit nonnegativity and accepted KOR00 sufficiency for positive strictly dominant integral spectra, zero padding permitted and no dimension/excess bound. |
| dependency | [Six-term primitive graph](../ledger/Yin_L_G0048_v1.md#positive-length-six-graph) | Full labelled simple-cycle graph once g>=2 implies the required b>=2 condition; parallel and repeated coefficient cases retained. |
| support | [General K1 measure boundary](Yin_C_G0224_v1.md#general-k1-measure-corollary) | Only the already adopted full-delay measure reduction at K=1, without extending its central-offset exact repair or asserting finiteB empty. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0513_v1.md#current-pairing-deletion-finding) | Exact current statement, complete retained proof and every selected dependency interface; self-reviewed, with old dated reviews and their inputs kept separate. |

### Decision current-complete-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:42 |
| status | proved |
| reason | Use the adequate complete same-object C homes for current dependencies; exact scopes, original proof, all other selections and old R bindings remain unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All labelled matchings, repeated coefficients, precise TypeI/II converse domains, specialized positivity, g>=2 controlled graph reductions and exact broader spectral-deletion witnesses and limitations. |
| argument | [Complete retained argument](#argument) | Entire fifteen-match classification, parity/gcd elimination, both full factorizations, both coprime length-five constructions, g>=2 boundary and actual primitive-orbit witnesses. |
| dependency | [Length-five positive graph](Yin_C_G0263_v1.md#uniform-repair-bounds) | Exact primitive zero-one unimodular graph for coprime t^(2n)+1-t^n-t^k-t^(2n-k), edge excess2 and repeated endpoint boundaries; no sharp degree34 computation. |
| dependency | [Exact nonzero-spectrum criterion](Yin_C_G0268_v1.md#exact-spectral-deletion) | Necessary primitive-orbit nonnegativity and accepted KOR00 sufficiency for positive strictly dominant integral spectra, zero padding permitted and no dimension/excess bound. |
| dependency | [Six-term primitive graph](Yin_C_G0269_v1.md#positive-length-six-graph) | Full labelled simple-cycle graph once g>=2 implies the required b>=2 condition; parallel and repeated coefficient cases retained. |
| support | [General K1 measure boundary](Yin_C_G0224_v1.md#general-k1-measure-corollary) | Only the already adopted full-delay measure reduction at K=1, without extending its central-offset exact repair or asserting finiteB empty. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0513_v1.md#current-pairing-deletion-finding) | Exact current statement, complete retained proof and every selected dependency interface; self-reviewed, with old dated reviews and their inputs kept separate. |

## Complete retained argument

<a id="argument"></a>

Original proof date:2026-10-07.

<a id="fifteen-pairing-classification"></a>
## Scope and the fifteen matchings

Write

    q(t)=t^D+1-t^a-t^(D-a)-t^b-t^(D-b),
    1<=a<=b<=D/2,             gcd(D,a,b)=1.                 (1)

The four negative terms are labelled coefficient units.
They may share exponents.
At a root of unity zeta, suppose the six signed units are partitioned into three opposite pairs.
This is the three-pair alternative of L G0048; a minimal six-term relation or two triangular components is outside this statement.

Let g be the gcd of all within-pair differences of original exponents, before absorbing signs.
A valid opposite pair cannot have two equal exponents: opposite signs at an equal exponent would require a collected coefficient with both signs, whereas all four interior units are negative and the two endpoint units positive.
Thus all the pair differences used below are nonzero.
The original ratios have orders one or two, and at least one pair has equal coefficient signs.
The resulting whole block has base two, so zeta^g=-1.
The case distinctions below prove this directly rather than assuming it.

Call the negative labels A,A',B,B', with exponents a,D-a,b,D-b.
There are precisely fifteen matchings:

| Placement of the endpoint units | Number | Outcome |
| --- | ---: | --- |
| Endpoints paired together; remaining pairs AA', BB' | 1 | Order two, g=1 |
| Endpoints paired together; remaining pairs AB,A'B' or AB',A'B | 2 | Type I below |
| Endpoints paired separately to the two members of one reciprocal pair | 4 | Type II below |
| Endpoints paired separately to members of different reciprocal pairs | 8 | Order two, g=1 |

For the first row, the root equations are

    zeta^D=-1,       zeta^(D-2a)=zeta^(D-2b)=-1.

Hence zeta^(2D)=zeta^(2a)=zeta^(2b)=1.
The global gcd in (1) forces zeta^2=1; the first equation excludes zeta=1.
Therefore D is odd and the component gcd gcd(D,2a,2b) is one.

For the last row, let the zero endpoint be paired with exponent u, and the D endpoint with exponent v from the other reciprocal pair.
The remaining negative exponents are D-u,D-v.
The equations give

    zeta^u=1,       zeta^(D-v)=1,       zeta^(v-u)=-1.

Thus zeta^v=zeta^D=-1.
Since reflecting or swapping the two representatives preserves gcd(D,u,v)=1, all three doubled powers give zeta^2=1 and hence order two.
The component gcd is exactly gcd(u,D-v,v-u)=gcd(D,u,v)=1.

These arguments retain repeated labels.
If equal exponents would make a required equal-sign pair vanish, its equation becomes 1=-1 and that particular matching does not occur.
If different labelled reciprocal pairs happen to coincide, the global-gcd argument still applies to the last row; labels have not silently been identified or discarded.

<a id="endpoint-pair-normal-form"></a>
## Type I: the endpoint pair and two crossing negative pairs

By reflecting one representative and then ordering the representatives, the two matchings in the second row can both be written with negative exponents

    u, v, D-u, D-v,       0<u<v<D,

and opposite pairs (0,D), (u,v), (D-u,D-v).
Put

    g=gcd(D,v-u),       D=L g,       v-u=K g.

The equations are zeta^D=zeta^(v-u)=-1.
Since gcd(L,K)=1, zeta^g has order dividing two and cannot equal one.
Consequently

    zeta^g=-1,       L,K are positive odd integers,
    L>K,            gcd(L,K)=1,
    0<u<(L-K)g,     gcd(u,g)=1.                           (2)

The last gcd is exactly the global condition in (1).
Conversely, all the conditions in (2) give a valid opposite-pair decomposition at every root of t^g+1, with component gcd exactly g.

For an even integer j>=0 define

    S_j(x)=x^j-x^(j-1)+...-x+1=(x^(j+1)+1)/(x+1).

With x=t^g, the polynomial and its exact quotient are

    q=t^(Lg)+1-(t^u+t^((L-K)g-u))(1+t^(Kg)),

    q/(t^g+1)
      =S_(L-1)(x)-(t^u+t^((L-K)g-u)) S_(K-1)(x).          (3)

In the originally sorted convention of (1), the two cases are respectively g=gcd(D,b-a), with D/g and (b-a)/g odd, and g=gcd(D,D-a-b), with D/g and (D-a-b)/g odd.
Reflecting b to D-b converts the second case to (2).
Neither matching occurs when its displayed difference is zero.

Formula (3) is a two-parameter family in the odd coprime integers L,K, with further integral delay parameters g,u.
The case K=1 has an alternating-kernel quotient, but the matching argument does not justify imposing K=1 in general.
At K=1 write L=2r+1; the full range is 0<u<2rg with gcd(u,g)=1.
The coordinated [general-delay measure corollary](Yin_C_G0224_v1.md#general-k1-measure-corollary) treats all those offsets for r>=2,g>=3, reducing any small-measure sequence with growing g to a finite, unspecified set of fixed kernels.
It does not prove that set empty.
Its exact D=2g repair argument remains restricted to the central-offset slice u=(r-1)g+h, 1<=h<g/2; reflecting that slice does not exhaust all offsets.
Neither the measure corollary nor the matching argument supplies a uniform quotient coefficient bound as L or K grows, and K>1 is outside that corollary.

<a id="same-reciprocal-pair-normal-form"></a>
## Type II: each endpoint paired to one member of the same reciprocal pair

Choose the representative a to be the exponent paired with the zero endpoint; its partner is D-a and is paired with the D endpoint.
This a need not be the smaller member of its reciprocal pair.
Reflect the remaining pair, if needed, so that 0<b<D/2.
The root equations are

    zeta^a=1,                 zeta^(D-2b)=-1.

Set g=gcd(a,D-2b).
On writing a=A g and D-2b=L g with gcd(A,L)=1, the order of zeta^g divides gcd(A,2L)=gcd(A,2).
The second equation excludes order one.
Therefore A is even and L is odd.
Write A=2r.
The exact parameters are

    a=2r g,             D=2b+L g,
    r>=1,               L>=1 odd,
    gcd(2r,L)=1,        gcd(b,g)=1,
    2r g<2b+L g.                                         (4)

The second gcd follows because gcd(D,a,b)=gcd(b,g gcd(2r,L)).
Conversely, (4) gives exactly this matching at every root of t^g+1, with component gcd g.
Swapping the two reciprocal pairs and choosing either orientation accounts for all four matchings in the third row.

The factorization pattern is

    q=(1-t^(2r g))(1-t^(2b+(L-2r)g))
                          -t^b(1+t^(Lg)).

Define T_(2r-1)(x)=1-x+x^2-...-x^(2r-1)=(1-x^(2r))/(1+x).
The quotient is

    q/(t^g+1)
      =T_(2r-1)(x)(1-t^(2b)x^(L-2r))-t^b S_(L-1)(x),
    x=t^g.                                               (5)

The exponent L-2r in this two-variable notation may be negative.
The actual t-exponent 2b+(L-2r)g=D-a is strictly positive by (4), so (5) is an ordinary polynomial identity after specialization.
Treating the two-variable expression as Laurent is legitimate and does not change this positivity condition.

The natural fixed-pattern Laurent polynomial here has variables x=t^g and y=t^b.
There are two independent pattern parameters r,L.
This is a different family from (3); its measure or short-completion properties cannot be inferred from a result for the K=1 case of Type I.

<a id="controlled-length-five-reductions"></a>
## Two actual reductions to coefficient length five

The least Type I parameters are L=3,K=1.
Equation (3) becomes

    q/(t^g+1)=t^(2g)+1-t^g-t^u-t^(2g-u),
    0<u<2g,       gcd(u,g)=1.                            (6)

For g>=2, u!=g.
Put n=g and k=min(u,2g-u).
Then 1<=k<n and gcd(n,k)=1.
Formula (6) is precisely the primitive length-five positive graph family t^(2n)+1-t^n-t^k-t^(2n-k) from L G0045.
It gives a primitive zero-one unimodular matrix of dimension 2g and edge excess two.

The least Type II parameters r=1,L=1 give

    q/(t^g+1)=t^(2b)+1-t^g-t^b-t^(2b-g),
    b>g/2,       gcd(b,g)=1.                             (7)

For g>=2 one has b>=2 and b!=g.
Set n=b and k=min(g,2b-g).
Again 1<=k<n and gcd(n,k)=1, so the same length-five graph gives a primitive zero-one unimodular realization of dimension 2b and edge excess two.

Thus in both subfamilies the full neutral deletion preserves every noncyclotomic factor and total algebraic entropy, reduces dimension by g, reduces coefficient length from six to five, and improves the available positive graph edge excess from three to two.
No irreducibility assumption is needed for these exact operations.
If an input is a cyclotomic completion of an eligible irreducible core, it therefore supplies a shorter completion of that same core.
These subfamilies cannot witness a core whose minimum cyclotomic coefficient length is exactly six.
The restriction g>=2 avoids the coincident degree-two quotient t^2-3t+1 at g=1; no high-order case is lost by recording this boundary.

<a id="sufficient-spectral-deletions"></a>
## Some further deletions are feasible without a complexity estimate

The graph consequences in this section concern g>=2.
In those cases the sorted normal form automatically has b>=2, as required by the positive graph of L G0048.
Indeed b=1 would give a=b=1.
Its Type I differences are zero or D-2, and gcd(D,D-2) is at most two; the required odd quotients exclude the value two.
Its Type II gcds are gcd(1,D-2) or gcd(D-1,D-2), both one.
The other nine matchings already have g=1.
Thus no g>=2 pairing is lost by the graph hypothesis.

The correction of t^g+1 is -1 at g and +1 at 2g, and zero elsewhere.
Therefore for any primitive graph realizing q, the exact spectral criterion of L G0047 says

    q/(t^g+1) has a nonnegative integer realization
       if and only if b_(2g)(q)>=1.                       (8)

Additional zero eigenvalues are allowed in this equivalence, and sufficiency uses the accepted KOR00 statement through L G0047.
It is not a same-excess construction.

Every Type II case with r=1 passes (8): a=2g is one of the graph's simple-cycle lengths.
Hence the whole block is spectrally deletable for every allowed odd L in that subfamily, even though only L=1 above gives the controlled length-five replacement.

Every Type I case with L-K=2 also passes (8).
Among the four simple-cycle lengths are u and 2g-u.
In the general positive graph one of these, the smaller, is a base cycle; the other is a mixed cycle through its distinguished branch vertex.
Traverse each once.
The resulting closed walk has length 2g and uses the mixed cycle's cross edge exactly once, so it cannot be a nontrivial repetition.
It is a primitive orbit.
This proves b_(2g)(q)>=1 without an assumption that each individual length equals 2g.
At g>=2 the two short lengths are distinct, because u=g would contradict gcd(u,g)=1.
The coincident g=1 case can also be checked directly with labelled edges, but is unnecessary for the growing-block use.

Outside these sufficient cases, divisibility by t^g+1 alone decides neither (8) nor the complexity of a possible positive realization.
Girth and the simple-cycle criterion of L G0047 remain available for a concrete pattern.
No claim is made that all other cases are essential or that the two displayed controlled replacements exhaust every possible shorter completion.
