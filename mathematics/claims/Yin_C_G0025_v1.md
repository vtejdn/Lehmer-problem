---
author: Yin
---

# Exact first-window denominator minimum for flat integer coefficients

Date: 2026-10-11T20:02.
Human author Yin.
Provenance: project deduction under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root supplied the substantive candidate and nearest-coordinate mechanism, and the responsible author reconstructed the complete proof.
The old L237 scalar witness and sufficient condition are explicitly credited; no new witness, novelty or main-theorem designation is asserted.

## Statement

Let P=sum_(j=0)^d p_j t^j be an ACTUAL monic irreducible minimal polynomial of a nontorsion integer unit alpha, d>=2, p_j in{0,+1,-1}, p_d=1, p_0=+/-1, and n the number of its nonzero coefficients.
Use ACTUAL O_0=Z[alpha] and allowed coefficient window[0,d].
For each positive integer q consider ALL rational f in this window with qf integral and f(alpha) a NONZERO actual O_0 integer.
Here q CLEARS each denominator; an individual ACTUAL least denominator may divide q.

**A. Exact individual minimum.**
The minimum over this entire infinite representative class is attained and equals

    ell_n(q)=min_(0<=k<=floor(q/2))
                   [1-2k/q+n k^2/q^2].

Every finite-grid value has an actual admissible attainer.
The proof covers ALL integer shifts of the one-dimensional kernel, q1, fractional part0 and the half-integer endpoint.
Interior equality has exactly one changed nonzero support coefficient; the half-integer equality uses a nonempty proper subset of the support, excluding the two zero-residue scalar multiples.
No bounded representative search is substituted for this infinite-domain minimum.

**B. Necessary packet denominator.**
One has ell_n(q)=1 iff q<=n/2, ell_n(q)<1 iff q>n/2, and ell_n(q)>=1-1/n.
Therefore any first-window rational packet of actual nonzero O_0 integer values with positive normalized weights and energy E<1, in particular any exact complementary packet, MUST have actual COMMON coefficient denominator

    q>n/2, hence q>=floor(n/2)+1.

The converse supplies only an INDIVIDUAL below-one coordinate, already constructed in L237.
It does not supply lag cancellation, a complementary packet at that q or a bound on the final least weight denominator M.
The full first-window capacity satisfies E_d>=1-1/n, and adopted C17 gives its strict upper bound E_d<1.
No exact capacity or attained complementary minimum is asserted.

**C. Applications and actual arithmetic.**
The adopted dense C21/C22 families have n=d+1 and thus require first-window q>=floor((d+1)/2)+1, growing with degree.
Their denominator2 escape at width d+1 is consistent because the kernel then has two polynomial directions.
The ORIGINAL Lehmer polynomial has n=9, so any below-one first-window packet has q>=5 and

    8/9<=E_10(P)<1.

The separately investigated J88 finite denominator9 family does not exclude ALL denominator9 packets, nor does this necessary q>=5 imply existence at q9.
All least-denominator/gcd reductions, primitive contents, full signed original norms/resultants and final packet q/M/width costs remain in the complete proof.
The monomial-valued individual witnesses cannot alone form a reciprocal below-one complementary packet: evaluation of constant covariance at an original reciprocal root pair gives E=1.
Half-endpoint subset patterns are not silently included in that unit-witness comparison.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-11T20:02 |
| status | open |
| reason | Register the complete03:59 author theorem and exact individual/packet distinction, with current adopted family and C17 interfaces. Separate whole and actual extraction review are pending. No author construction or prior scalar review substitutes for those checks. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual flat-coefficient minimalP/O_0, ALL q and individual representatives at first allowed windowd; exact minimum, necessary packet denominator and applications only. |
| argument | [Argument](#argument) | Complete03:59 D20 author freeze, every division/kernel/sign/endpoint/equality, actual arithmetic and individual-versus-packet boundary. |
| dependency | [Exact actual-residue packet domain](Yin_C_G0016_v1.md#statement) | Finite rational and formal-real conventions for the capacity comparison; the individual minimum is locally proved over all rational representatives. |
| dependency | [Strict monogenic first-window theorem](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | Individual actual P is irreducible and nontorsion, so FULL E_d<1, without a construction or uniform deficit. |
| dependency | [Adopted dense multinacci input](Yin_C_G0021_v1.md#statement) | Its actual minimal polynomial has n=d+1; only the stated denominator application and width comparison. |
| dependency | [Adopted genuine Salem input](Yin_C_G0022_v1.md#statement) | Its actual minimal polynomial, of degree divisible by6, has all coefficients+/-1; only the denominator application and same-input one-extra-power boundary. |
| dependency | [Fixed original-Lehmer control](../ledger/Yin_L_G0055_v1.md#lehmer-joint-prime-control) | ONLY the actual original degree10 irreducible Salem/nontorsion polynomial identity for partC and its C17 application; no cyclic-return calculation, source-proof audit or new native execution is imported. |
| dependency | [Generic-monic complete-root charged inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Applied ONLY to actual complementary packets with their true q/M, signed original resultants, contents and union width; no such inequality is inferred from an isolated individual minimizer. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-11T20:13 |
| status | proved |
| reason | Adopt the completed separate noncontributor finding for this exact registered scope and selected fixed argument. Complete original histories, current repairs, source inspection limits and all costs remain; no uniform efficiency, unrestricted gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual flat-coefficient minimalP/O_0, ALL q and individual representatives at first allowed windowd; exact minimum, necessary packet denominator and applications only. |
| argument | [Argument](#argument) | Complete03:59 D20 author freeze, every division/kernel/sign/endpoint/equality, actual arithmetic and individual-versus-packet boundary. |
| dependency | [Dependency](Yin_C_G0016_v1.md#statement) | Finite rational and formal-real conventions for the capacity comparison; the individual minimum is locally proved over all rational representatives. |
| dependency | [Dependency](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | Individual actual P is irreducible and nontorsion, so FULL E_d<1, without a construction or uniform deficit. |
| dependency | [Dependency](Yin_C_G0021_v1.md#statement) | Its actual minimal polynomial has n=d+1; only the stated denominator application and width comparison. |
| dependency | [Dependency](Yin_C_G0022_v1.md#statement) | Its actual minimal polynomial, of degree divisible by6, has all coefficients+/-1; only the denominator application and same-input one-extra-power boundary. |
| dependency | [Dependency](../ledger/Yin_L_G0055_v1.md#lehmer-joint-prime-control) | ONLY the actual original degree10 irreducible Salem/nontorsion polynomial identity for partC and its C17 application; no cyclic-return calculation, source-proof audit or new native execution is imported. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Applied ONLY to actual complementary packets with their true q/M, signed original resultants, contents and union width; no such inequality is inferred from an isolated individual minimizer. |
| review | [Current finding](../audits/reviews/Yin_R_G0790_v1.md#c25-first-window-denominator-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |


### Decision current-joint-minor-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:52 |
| status | proved |
| reason | Select C226#lehmer-joint-prime-control as the complete current responsible home of the identical retained L55 original degree10 irreducible Salem/nontorsion control, at exactly the already used identity and original power-basis scope. The complete original control, accepted MS26 premise and source-depth limits were actually read. This is a same-content interface adoption; mathematical status, statement/proof and selected finding remain, with no new independent inspection or cyclic-return calculation. Old dated decisions and R bindings retain the original L55 address and inspection facts. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual flat-coefficient minimalP/O_0, ALL q and individual representatives at first allowed windowd; exact minimum, necessary packet denominator and applications only. |
| argument | [Argument](#argument) | Complete03:59 D20 author freeze, every division/kernel/sign/endpoint/equality, actual arithmetic and individual-versus-packet boundary. |
| dependency | [Dependency](Yin_C_G0016_v1.md#statement) | Finite rational and formal-real conventions for the capacity comparison; the individual minimum is locally proved over all rational representatives. |
| dependency | [Dependency](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | Individual actual P is irreducible and nontorsion, so FULL E_d<1, without a construction or uniform deficit. |
| dependency | [Dependency](Yin_C_G0021_v1.md#statement) | Its actual minimal polynomial has n=d+1; only the stated denominator application and width comparison. |
| dependency | [Dependency](Yin_C_G0022_v1.md#statement) | Its actual minimal polynomial, of degree divisible by6, has all coefficients+/-1; only the denominator application and same-input one-extra-power boundary. |
| dependency | [Dependency](Yin_C_G0226_v1.md#lehmer-joint-prime-control) | ONLY the actual original degree10 irreducible Salem/nontorsion polynomial identity for partC and its C17 application; no cyclic-return calculation, source-proof audit or new native execution is imported. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Applied ONLY to actual complementary packets with their true q/M, signed original resultants, contents and union width; no such inequality is inferred from an isolated individual minimizer. |
| review | [Review](../audits/reviews/Yin_R_G0790_v1.md#c25-first-window-denominator-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |


### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:33 |
| status | proved |
| reason | Adopt the separately assigned isolated complete mathematical inspection of this actual fixed statement and entire selected argument. Its recorded initial finding preceded all old target verdicts and substantive target-development context was not shared. Preserve the exact current mathematical domain, complete proof, source-depth and native-execution limits, all earlier findings and their original relationships, and every arithmetic and physical-window charge. No new uniform construction, optimality or Task/E resumption is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual flat-coefficient minimalP/O_0, ALL q and individual representatives at first allowed windowd; exact minimum, necessary packet denominator and applications only. |
| argument | [Argument](#argument) | Complete03:59 D20 author freeze, every division/kernel/sign/endpoint/equality, actual arithmetic and individual-versus-packet boundary. |
| dependency | [Dependency](Yin_C_G0016_v1.md#statement) | Finite rational and formal-real conventions for the capacity comparison; the individual minimum is locally proved over all rational representatives. |
| dependency | [Dependency](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | Individual actual P is irreducible and nontorsion, so FULL E_d<1, without a construction or uniform deficit. |
| dependency | [Dependency](Yin_C_G0021_v1.md#statement) | Its actual minimal polynomial has n=d+1; only the stated denominator application and width comparison. |
| dependency | [Dependency](Yin_C_G0022_v1.md#statement) | Its actual minimal polynomial, of degree divisible by6, has all coefficients+/-1; only the denominator application and same-input one-extra-power boundary. |
| dependency | [Dependency](Yin_C_G0226_v1.md#lehmer-joint-prime-control) | ONLY the actual original degree10 irreducible Salem/nontorsion polynomial identity for partC and its C17 application; no cyclic-return calculation, source-proof audit or new native execution is imported. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Applied ONLY to actual complementary packets with their true q/M, signed original resultants, contents and union width; no such inequality is inferred from an isolated individual minimizer. |
| review | [Isolated complete current finding](../audits/reviews/Yin_R_G0790_v1.md#current-flat-denominator) | Complete current fixed statement and entire selected argument, actual required mathematical interfaces and all quantifier, source and execution limits; initial independent reconstruction precedes old target verdict comparison. |

## Argument

The COMPLETE03:59 D20 frozen author account follows, unchanged apart from first-title depth and final whitespace.
All actual membership, monic division, one-dimensional-kernel, nearest-coordinate and endpoint arguments are physically present.
L237's old sufficient scalar witness is ancestry, not an unproved premise replacing the new all-representative lower bound.
C21/C22 are actually adopted inputs for their family applications; the historical initial C22 candidate reading and pre-freeze refresh remain distinct.
No source intake or native mathematical program was needed.

## Exact denominator obstruction in the first coefficient window

Context: unchanged [G0001](../tasks/Yin_T_G0001_v1.md#contract), [C16 actual capacity domain](Yin_C_G0016_v1.md#statement), [C17 first-window existence](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree).
Human author Yin; multinacci_source_intake AI in an AUTHOR role.
Root supplied the substantive candidate formula and proof mechanism; this author must verify all endpoints, actual residue/denominator guards and implications.
No independent review is asserted.

## Question and scope

At the FIRST allowed windowT=d, for ACTUAL monic irreducible nontorsion integer-unit P with coefficients0,+/-1 and n nonzero coefficients, determine the minimum INDIVIDUAL squared coefficient energy among rational f with qf integral and actual Af a nonzero integer residue in O_0=Z[alpha].
Test the proposed finite formula min_(0<=k<=floor(q/2))[1-2k/q+n k^2/q^2].
A packet consequence, if proved, is a NECESSARY actual common denominator q>n/2 for complementary E<1; an individual below-one coordinate would not imply a complementary packet at that q.
Full signed norms, contents, actual q/M and width remain.
This is not a full capacity optimizer, input-uniform deficit or Lehmer gap.

## Pre-development boundary

The responsible mathematical home is allocated before sustained derivation.
Bounded current reuse is in progress.
No native mathematical program, enumeration, solver or new J is authorized or run for this assignment.
Substantive reasoning and all useful failed implications belong here.

<a id="first-window-denominator-reuse"></a>
## 1. Reuse and the precise changed claim

The responsible author read the exact adopted [C14 monogenic short-width statement](Yin_C_G0014_v2.md#short-width-power-order-obstruction), [C16 rational actual-residue domain](Yin_C_G0016_v1.md#integer-moment-domain-and-energy) and [C17 first-window existence](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree).
Their premises distinguish actual O_0 coordinates from a norm floor, allowed support from actual width, rational coordinate denominators from final weight denominators, and individual representatives from a complementary bundle.
C14 gives E>=1 below widthd, but does not give the denominator-dependent individual minimum AT widthd.
C16/C17 define the whole first-window packet problem without a finite residue or denominator cutoff.

The already adopted [C21 dense multinacci family](Yin_C_G0021_v1.md#statement) and registered [C22 genuine-Salem family](Yin_C_G0022_v1.md#statement) have n=d+1.
Their first-window whole-lattice lower bound d/(d+1) and one-power escape are retained at their own actual review scopes; C22 was a proof draft under review at the initial screen.
A pre-freeze refresh checked its2026-10-11T19:52 organized-reviewed decision and exact [R790 extraction scope](../audits/reviews/Yin_R_G0790_v1.md#c22-salem-first-window-extraction-finding), so the final family application invokes that adopted statement rather than treating the earlier candidate as a resolved premise.
The denominator statement proved below applies to these coefficient shapes with their actually proved irreducibility.
No new review of either family proof is claimed here.

Most directly, [L237 already proves](../ledger/Yin_L_G0237_v1.md#scalar-sign-deep-floor-control) that F_q=P-p_0q has coefficient squared energy q^2-2q+B and positive scalar coefficient-energy surplus exactly when q>B/2, with B=sum p_j^2.
For the present0,+/-1 coefficients B=n.
The below-one single-coordinate construction and its q>n/2 SUFFICIENCY are therefore old.
L237's [Euclidean projection](../ledger/Yin_L_G0237_v1.md#monomial-projection-uniform-margin) also supplies monomial-valued low-energy representatives in a larger window; it does not establish the present complete first-window denominator minimum or exact lag cancellation.
The changed assertion is a lower bound over ALL allowed first-window rational representatives whose denominators divide a specifiedq, hence a NECESSARY denominator obstruction for EVERY complementary packet.

The bounded screen also inspected L233's strict dyadic small-integer-energy classification, C15's q/M and near-floor boundary, and C20's different non-flat quadratic control.
Their arbitrary-width period, discrete numerator-energy and coefficient-a>=3 settings do not assert this all-q first-window formula for flat coefficients.
Directory/glob searches by q>B/2, q>n/2, nearest-coordinate and first-window denominator phrases found only the L237 scalar witness and unrelated rounding passages in L280/L284/L292; no matching complete minimum was retained.
This is not an exhaustive novelty/priority search.
The proof below needs only monic division, the actual power-basis uniqueness and elementary integer-coordinate distances.
No new external theorem, source intake, native mathematical program or J is used.

Root supplied the substantive formula and its nearest-coordinate proof candidate.
The present author reconstructed the complete division/sign/fractional-endpoint argument, equality conditions, actual-denominator/content accounting and packet implications.
These are AUTHOR contributions, not independent review.

<a id="first-window-denominator-exact-statement"></a>
## 2. Exact statement and clearing-versus-least denominator

Let

    P(t)=sum_(j=0)^d p_j t^j,
    p_j in{0,+1,-1}, p_d=1, p_0 in{+1,-1},
    n=#{j:p_j!=0}>=2.                              (1)

P is the ACTUAL monic irreducible minimal polynomial of a nontorsion integer unit alpha, degree d>=2, and O_0=Z[alpha].
Fix an integer q>=1.
The individual class consists of ALL f in Q[t] supported in[0,d] such that qf has integer coefficients and f(alpha) is a NONZERO actual O_0 element.
The requirement is denominator DIVIDINGq, not necessarily actual least denominatorq.
The unique integer residue vector is Af, A=[I_d,-p_low].
Write ||f||^2=sum_(j=0)^d f_j^2.

**Theorem.** The minimum over this entire individual class exists and is

    ell_n(q)=min_(0<=k<=floor(q/2))
                 [1-2k/q+n k^2/q^2].             (2)

For q1 the only displayed index is0, giving1.
The minimum is over this explicit finite grid, but the original representative class is infinite; the proof below establishes the lower bound for every member and supplies an actual admissible attainer for every grid value.
No finite coefficient search or integer-lattice cutoff is being substituted.

In particular

    ell_n(q)=1  iff q<=n/2,
    ell_n(q)<1 iff q>n/2,
    ell_n(q)>=1-1/n>0.                            (3)

For any positive normalized packet of these rational coordinates, its weighted coefficient energy is at least ell_n(q), whether or not its lags vanish.
Therefore an EXACT complementary packet at the first allowed window with E<1 and ACTUAL least common coefficient denominator q must satisfy

    q>n/2, hence q>=floor(n/2)+1.                  (4)

This is necessary, not a sufficient condition for a complementary packet at thatq.
The final weight denominator M is separate, and no bound on M follows.
No full capacity optimizer, input-uniform gap or q-attainment theorem is asserted.

<a id="first-window-denominator-monic-fraction-reduction"></a>
## 3. Complete monic division and fractional reduction

Let F=qf in Z[t], deg F<=d.
Monic division at this exact endpoint gives

    F=R+kP, deg R<d, R in Z[t], k=F_d in Z.

Its value is R(alpha), so f(alpha)=R(alpha)/q.
Actual membership in O_0 means that this value has a UNIQUE integer coefficient vector in the basis1,alpha,...,alpha^(d-1).
Hence EVERY coefficient of R is divisible byq.
This uses actual monogenic membership; a large norm or membership only in an overorder would not imply it.
Write R=qR_0.
Then

    f=R_0+(k/q)P, R_0 in Z[t], deg R_0<d.         (5)

Conversely (5) with R_0 nonzero has the required actual nonzero integer residue.
More generally, after changing k by an integer multiple ofq, the compensating integral polynomial may have degree d; still f=z+theta P with z integral of degree<=d and Af=Az.
This does not enlarge the allowed coefficient window.

Take the residue a of k moduloq in{0,...,q-1} and absorb the integer part into z.
If a>q/2, replace f by-f and absorb one further integer multiple ofP; its fractional part becomes(q-a)/q.
Global sign preserves energy, denominator-divisibility and the nonzero integer residue condition.
Thus it suffices to consider

    f=z+theta P,
    z in Z^(d+1), theta=k/q,
    0<=k<=floor(q/2).                              (6)

The rational kernel of A in this coefficient window is EXACTLY QP: a rational polynomial of degree<=d vanishing at alpha is a scalar multiple of its actual degree-d minimal polynomial.
Its integer part is ZP, because p_d=1.
Consequently the nonzero-value condition is precisely Az!=0, not merely z!=0.
In particular it implies z!=0.
This exact rank/kernel fact handles all possible multiples ofP and is used again at the half-integer endpoint.

<a id="first-window-denominator-nearest-coordinate-proof"></a>
## 4. Every fractional class, including both endpoints

First theta0 makes f an integer polynomial.
Its nonzero value excludes the zero polynomial, so ||f||^2>=1, attained exactly by signed monomials in[0,d].
Their values are nonzero integer units.
This proves the grid value at k0 without treating the forbidden zero-residue polynomial as an attainer.

Now0<theta<1/2.
At each nonzero coefficient p_j, set u_j=p_j z_j in Z.
Its contribution is(u_j+theta)^2.
Its unique nearest-integer choice is u_j0, contributing theta^2.
For u_j!=0,

    (u_j+theta)^2-theta^2>=1-2theta,               (7)

with equality exactly at u_j=-1.
Indeed u_j>=1 gives at least1+2theta, while u_j=-m,m>=1 gives m^2-2mtheta; subtracting1-2theta leaves(m-1)(m+1-2theta)>=0, strictly positive when m>1.
At a zero coefficient p_j0, the nearest integer is z_j0 and any change contributes at least1, strictly larger than1-2theta.

Taking every nearest choice would give z0 and f=theta P, whose residue is ZERO and is forbidden.
Since an admissible z is nonzero, at least one coordinate changes.
Every change has nonnegative cost and any nonzero change costs at least1-2theta.
Thus

    ||f||^2>=n theta^2+1-2theta.                  (8)

This bound includes every integer coefficient vector, not just nearest candidates; excluding the other zero-residue vectors z=mP cannot weaken it.
It is attained by choosing ANY nonzero P coefficient j and setting

    f=theta P-p_j t^j,
    f(alpha)=-p_j alpha^j!=0.                    (9)

This actual integer unit lies in O_0.
Equality in(8), at the interior fractional part, requires exactly one changed NONZERO P coordinate by(7), and no other change; thus(9) gives all equality representatives AFTER the sign/fractional normalization(6).

At theta1/2, possible only for evenq, each nonzero coefficient contributes at least1/4 and each zero coefficient contributes at least0.
Hence ||f||^2>=n/4, which is also1-2theta+n theta^2.
The nearest choices at each nonzero coefficient are f_j=p_j/2 or-p_j/2, and zero coefficients remain0.
Let J be the subset of coefficients choosing the minus sign; then

    f=(1/2)P-sum_(j in J)p_jt^j,
    f(alpha)=-sum_(j in J)p_jalpha^j.             (10)

The value is zero EXACTLY for the empty subset or the full nonzero support: the associated integer coefficient vector z=-sum_(j in J)p_jt^j can be a scalar multiple ofP only when all its nonzero-coordinate ratios are the same, here either0 or-1.
Because n>=2, a nonempty PROPER subset exists, giving a nonzero actual integer value and attaining n/4.
These proper-subset nearest patterns give all endpoint minimizers.
They need not all be units; no unit-norm claim is made for them.
A one-coordinate subset gives the unit witness(9).

For every grid k, the corresponding admissible representative has exactly the stated energy; conversely all admissible representatives were reduced to one such fractional class and obey its bound.
This proves the entire finite formula(2), with both endpoints and its asserted minimum attainment.
Global sign may be undone to recover the original representatives.

<a id="first-window-denominator-packet-threshold"></a>
## 5. The exact threshold, scalar inventory and packet consequences

For k>=1, the grid value minus1 is

    (k/q)(n k/q-2).

If q<=n/2 then n/q>=2, so every such value is at least1; k0 attains1.
If q>n/2, n>=2 implies q>=2 and k1 is allowed.
Its value1-2/q+n/q^2 is strictly below1.
This proves both directions in(3).
Completing the square gives

    1-2theta+n theta^2
      =1-1/n+n(theta-1/n)^2>=1-1/n.               (11)

The lower bound is an INDIVIDUAL coefficient-energy bound.
It is sharp across all positive clearing denominators, since q=n,k1 and(9) attain1-1/n.
It is not an assertion that a complementary packet attains that value.
Weighted averaging proves(4) for any real or rational positive normalized weights on rational coordinates; lag cancellation is only needed to identify this average with the constant covariance E.
Since the actual least common denominator clears every coordinate, it is a validq in the theorem.
If a packet is initially Laurent-supported in a common interval of widthd, one common integral monomial shift places it in[0,d], preserving coefficient denominators, energy, covariance and actual O_0 membership because alpha is a unit.
The first-window consequence therefore has the same actual-width convention as C14/C17.

For q>n/2, the explicit k1 witness in(9) has ACTUAL least denominatorq: at least one nonzero P coefficient is unchanged by the one-coordinate subtraction, leaving coefficient+/-1/q.
Its actual union width isd, since both endpoints remain nonzero for q>=2.
This proves that an INDIVIDUAL below-one coordinate exists with actual denominatorq exactly under that threshold, matching L237's old j0 scalar construction.
Its existence is not a complementary bundle or an attainment result for E_d.

For a general k>0 in(9), let g=gcd(k,q), q_0=q/g, k_0=k/g.
The actual least denominator is q_0, and the primitive actual numerator is

    F_0=k_0P-q_0 p_jt^j,
    content(F_0)=gcd(k_0,q_0)=1.                  (12)

The content identity follows from one untouched nonzero coefficient k_0 and the changed coefficient p_j(k_0-q_0); n>=2 guarantees the untouched coefficient.
At theta1/2 the one-coordinate witness has actual denominator2; general endpoint proper-subset patterns also have actual denominator2 and primitive coefficients+/-1.
The specified clearingq must not be confused with these least denominators.

Let eta=Norm(alpha)=(-1)^d p_0 in{+1,-1}.
Every original root is retained in the complete signed values

    Norm(-p_jalpha^j)=(-p_j)^d eta^j,
    Res(P,F_0)=(-q_0p_j)^d eta^j.                 (13)

With nominal numerator qf before dividing contentg, its content isg and its signed resultant is(-qp_j)^d eta^j; dividing by g^d produces(13).
There is no discarded root, selected factor or maximal-order norm substitution.
The general endpoint patterns may have varying nonunit norms and require their own complete original norm accounting if used in a future packet.

For ANY actual complementary rational packet in the theorem's domain, let q be its ACTUAL common coefficient denominator, M its ACTUAL final weight denominator, m_b=M omega_b, D_b=Norm(f_b(alpha)) a nonzero signed integer.
Its full costs remain

    Res(P,qf_b)=q^dD_b,
    product_b Res(P,qf_b)^m_b=q^(dM)product_bD_b^m_b,
    S=q^2E,
    I=log q+(1/d)sum_b omega_b log|D_b|,
    I-(1/2)log S=(1/d)sum_b omega_b log|D_b|
                    -(1/2)log E <=m(P).          (14)

The last inequality uses the complete [C10 exact-covariance window argument](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) ONLY when the packet actually exists and has its paid original widthd.
An isolated witness(9) has no constant-covariance premise, so(14) is NOT applied to it alone.
A common monomial shift adds its explicit unit norms and preserves their absolute income; all original signed factors still remain.
No bound on M, all D_b, height or an input-uniform positive surplus follows from the denominator obstruction.

<a id="first-window-denominator-applications-and-limits"></a>
## 6. Dense families, original Lehmer and the one-power boundary

The dense multinacci coefficient shape of C21 has n=d+1.
Every ACTUAL first-window complementary packet of energy below1 must therefore have

    q>=floor((d+1)/2)+1.                           (15)

The same application holds for C22's now adopted genuine-Salem coefficient shape, with its actual irreducibility supplied at that material's exact statement/review scope.
For its d=6r inputs the bound becomes q>=d/2+1.
Thus the coefficient denominator is necessarily unbounded along either dense first-window family.
This complements the old d/(d+1) whole-lattice lower bound; formula(11) recovers that same energy floor when n=d+1 and does not claim it new as a family result.

By contrast their known one-extra-power packets at widthd+1 have q2,M2,E1/2.
There is no inconsistency: the proof of(5) and the one-dimensional kernel reduction use EXACTLY the first allowed window[0,d].
At T=d+1 the kernel contains both P andtP, and(2)/(15) are not asserted.
The width change can therefore remove this particular denominator obstruction.
No universal larger-window construction follows.

For the ACTUAL original Lehmer polynomial, whose retained target-domain identity and irreducible Salem premise are explicit in [C226 retained L55 control](Yin_C_G0226_v1.md#lehmer-joint-prime-control), with ascending coefficients

    [1,1,0,-1,-1,-1,-1,-1,0,1,1],

n9, so a first-windowT10 packet below1 MUST have actual q>=5.
Independently, averaging(11) over the full rational packet class gives the original-input capacity interval

    8/9<=E_10(P)<1,                               (16)

where the strict upper bound is adopted C17 and is not a new constructive witness.
No claim of equality at8/9 is made.
The [D18/J88 exact finite-family result](Yin_C_G0024_v1.md#lehmer-first-window-exact-finite-family-result) at denominator-dividing9, selected ternary residues, five representative offsets and energy cap4 is separately author-frozen.
Its finite minimum1 does NOT exclude ALL denominator9 packets, and the present necessary q>=5 does NOT prove a denominator9 packet exists.

Finally, the explicit individual minimizers cannot simply be combined and called a complementary solution.
For a reciprocal P, every one-coordinate witness(9) has values-p_jalpha_i^j at ALL original roots, including alpha and alpha^-1.
Their product at that reciprocal pair is1.
Evaluating any hypothetical constant-covariance bundle consisting entirely of these witnesses at alpha therefore gives E=sum_b omega_b=1.
This is the already retained cyclic-unit obstruction in its simplest direct form, not a new global unit classification.
It exhibits concretely why the individual sufficiency direction is not packet sufficiency.
The half-endpoint proper-subset patterns need not be such unit monomials, so they are not silently included in this special comparison.

The new outcome is the complete first-window denominator-dependent INDIVIDUAL minimum and the resulting necessary packet coefficient cost.
It supplies neither a complementary construction at the threshold, nor exact packet infimum/attainment, nor a near-one sequence, nor an unrestricted Lehmer gap.

This coefficient formula is specific to the ACTUAL monogenic order and coefficients0,+/-1.
In an overorder the remainder of qf need not be coefficientwise divisible byq in the original power basis; C14 already records that distinction.
Coefficients of larger magnitude change the nearest-coordinate problem.
No extension to either case is asserted.
The function ell_n(q) is indexed by a clearing denominator; monotonicity in its numerical size is not asserted, since the actual fractional grids for unrelated integers are not nested.

<a id="first-window-denominator-complete-author-freeze"></a>
## 7. Complete author self-check and freeze

2026-10-11T19:59.
The author reconstructed and checked the ENTIRE Sections1--7, theorem, equations(1)--(16), reuse/attribution and limitations.
The check includes actual degree-d minimality and monogenic membership, the leading coefficient in monic division, coefficientwise divisibility rather than a norm surrogate, rational/integer kernel exactly QP/ZP, arbitrary integer multiples and the global-sign/fractional reduction, q1 and floor(q/2), forbidden zero-residue nearest representatives, all integer coordinate changes and the strict interior equality case, zero-P coefficient changes, both half-integer nearest choices and the nonempty proper-subset guard, and every existence/minimum quantifier over the full infinite representative class.

The theorem's clearing-denominator class is kept distinct from actual least individual/common denominators.
The threshold proof covers q<=n/2 including equality, q>n/2 with admissible k1 and q>=2, n>=2 and all endpoint shapes.
The complete-square floor, positive real/rational weighted averaging, Laurent common shifts, exact first-window kernel dimension and absence of a T=d+1 transfer were checked.
The actual denominator/contentgcd formulas and untouched-coordinate guard, every original signed unit norm/resultant, nominal versus primitive numerators, final M/m_b/q^d costs and the exact-covariance-only use of the analytic inequality remain explicit.
No packet is inferred from a single low-energy coordinate, including the credited old L237 construction.

Family applications use C21 and the now adopted exact C22 statement; their own proof/review scopes are not re-audited or expanded.
The original Lehmer n9/q>=5 and full capacity lower8/9 are distinguished from C17's strict upper1, from an unknown capacity optimizer and from D18/J88's separately frozen finite-screen minimum1.
The simple reciprocal evaluation obstruction is checked only for the specified monomial-valued unit witnesses, not arbitrary endpoint-pattern or independent-unit packets.
Overorder/non-flat exclusions, no-nested-grid monotonicity assertion, no norm-inventory/weight-denominator bound and no unrestricted-gap conclusion were checked.

Root supplied the substantive formula/proof candidate and is an author contributor.
This is the responsible author's complete self-check, not independent review.
The scoped material check passed before this paragraph and is repeated on the final changed file; it checks structure and locators, not mathematics.
No native mathematical program, solver, enumeration, source intake or new J was run.

The COMPLETE current D20 is author-frozen for separately organized whole noncontributor review and later root registration/adoption.
No further author mathematical work is pending under this assignment.
G0001 remains active and unrestrictedly unresolved.


## Registration and preservation operation

2026-10-11T20:02: retain the complete2026-10-11T19:59 author freeze as the actual selected argument.
A separate noncontributor is checking the whole account and will inspect this actual registered statement and dependencies before adoption.
Working-draft retirement requires whole preservation and incoming-reference maintenance.
This register creates no complementary optimizer, new execution baseline or unrestricted Task completion.

## Retained finite-investigation locator maintenance

2026-10-11T20:17: the original D18 finite-comparison link now reaches the SAME preserved author subsection in C24 before retirement.
Its original as-of-writing author/review history is unchanged; current acceptance is separately selected in C24.
No native check or older review scope is retroactively extended.
