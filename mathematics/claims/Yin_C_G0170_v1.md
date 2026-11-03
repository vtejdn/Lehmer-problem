---
author: Yin
---
# Short-overlap heat baths, exact carry contraction and bounded true-midpoint energy

Date: 2026-10-18T15:19.
Human author Yin.
Root proposed the shorter overlapping-block direction and required every overlap, carry and clock cost.
The entropy_attainment_bridge agent authors the centered operators, algebraic invariant, complete weighted endpoint reduction, exact marked formula and this fixed statement.
Root and entropy_attainment_bridge are contributors; angular_envelope_review supplied only the L282/BSS17 source pointers.
No numerical execution supplies a premise.
This 2026-10-18 author preface precedes the later whole finding; the current selected decision and its R account state the actual adopted scope and unresolved context-isolation relationship.

<a id="statement"></a>
## Complete operator statement

Fix the actual quartic P(t)=1-t-t^2-t^3+t^4, its exterior Salem root beta and one neutral conjugate zeta.
Let O=Z[beta], with the integral basis1,beta,beta^2,beta^3 of this order, without a maximal-order claim.
For integers n>=3 and1<=b<n put N=2n,k=n-b and let pi_N be the complete law of original independent digits eta_j in{-1,0,1}, of probabilities1/4,1/2,1/4, conditioned on sum_(j<N)eta_j beta^j=0.
Define the left tail A={0,...,k-1}, central overlap B={k,...,k+2b-1}, and right tail C={k+2b,...,N-1}.
Let H_A and H_C be conditional expectations given every digit in the indicated tail, and set

    K_(n,b)=(H_A+H_C)/2,
    Z_n=-zeta^-n sum_(j<n)eta_j zeta^j,
    m_n=E_pi_N|Z_n|^2,
    D_(n,b)=<Z_n,(I-K_(n,b))Z_n>_pi_N.

Each resampling changes n+b coordinates, and their overlap has2b coordinates.
The true complex squared modulus uses exactly two unweighted real neutral coordinates.
The chain is reversible and positive and E Z_n=0, with

    D_(n,b)=[E Var(Z_n|A digits)+E Var(Z_n|C digits)]/2,
    0<=D_(n,b)<=min(m_n,b^2).

No global connectivity is assumed.
For the declared digit-work slowdown K^cost=(1-1/(n+b))I+K/(n+b), both its spectral gap and its Dirichlet energy are divided by n+b.
This is a work-accounting clock, not an efficient-sampler or chronological-walk equivalence.

**Algebraic obstruction.** The class of a=sum_(j in A)eta_j beta^j modulo span_Q{beta^k,...,beta^(k+2b-1)} is invariant under both updates.
At b=1 it is nonconstant on actual returned words and gap(K_(n,1))=0 for every n>=3.
At b=2 the overlap powers form an integral basis of O, so this rational and integral quotient obstruction is trivial; connectivity and a quantitative gap remain unproved.

**Exact full-law spectral reduction.** For l>=0 let c_l(x) be the sum of2^(number of zero digits) over ALL l-digit words with endpoint x, with c_0(0)=1 and zero elsewhere.
For n>=5 and1<=b<n define

    W(a,c)=c_k(a)c_k(c)c_(2b)(-beta^-k a-beta^(2b)c),
    S=sum_(a,c)W(a,c)=c_(2n)(0),
    r(a)=sum_c W(a,c), h(c)=sum_a W(a,c),
    M(a,c)=W(a,c)/sqrt(r(a)h(c)),

using exactly the positive-marginal endpoint labels on each side.
Each side has at least two labels.
The top singular value is1, and let rho_(n,b) be the second singular value counted with multiplicity, including another1 for a disconnected graph.
Then the full returned-word chain, including all words in each endpoint fiber, satisfies

    gap(K_(n,b))=(1-rho_(n,b))/2,
    (1-rho_(n,b))m_n<=2b^2.

Its complete components coincide with the components of this weighted endpoint incidence graph.
The rational two-step left-endpoint kernel is T(a,a')=sum_c W(a,c)W(a',c)/(r(a)h(c)), with stationary law r(a)/S and nontrivial top eigenvalue rho_(n,b)^2.
For FIXED b, an additional eventual bound rho_(n,b)<=1-delta,0<delta<=1, implies m_n<=2b^2/delta and finite original critical first-return mean through the accepted actual-quartic midpoint criterion.
No such eventual contraction is asserted.
A supplied m_n>=epsilon n at one tested n forces1-rho_(n,b)<=2b^2/(epsilon n); the converse is not asserted.

**Complete marks at b=2.** For n>=5, each endpoint vertex has at most81 neighbors.
On every edge let x=beta^-k a and let theta_0,...,theta_3 in{-1,0,1} be the unique coordinates of-x-beta^4c.
The actual midpoint is the neutral embedding of

    y_(a,c)=-beta^-2(x+theta_0+theta_1 beta).

Every complete original word in that edge has this same midpoint.
For q=sum_(j=0)^3 a_j beta^j with rational a_j, put s_l=sum_(j=0)^(3-l)a_j a_(j+l) and

    Phi(q)=s_0+s_2+3s_3+u(s_1+s_2+s_3),
    u=(1-sqrt13)/2.

Then Phi(q)=|q(zeta)|^2 in the specified neutral embedding.
Writing ybar_a=sum_c W(a,c)y_(a,c)/r(a) and ybar_c=sum_a W(a,c)y_(a,c)/h(c), the entire true moment and update energy are

    m_n=S^-1 sum_(a,c)W(a,c)Phi(y_(a,c)),
    D_(n,2)=m_n-(2S)^-1[sum_a r(a)Phi(ybar_a)+sum_c h(c)Phi(ybar_c)],
    0<=D_(n,2)<=min(m_n,4).

Thus the same complete integer edge table supplies every component's original mass, conditional midpoint mean and second moment, with no omitted conditional means or within-edge variance.
Finite graph connectivity or a Rayleigh UPPER gap certificate does not establish a uniform gap, diffusion, a critical-mean classification or a Mahler gap.

<a id="argument"></a>
## Complete argument and reuse boundaries

<a id="short-overlap-reuse-and-question"></a>
## Actual question and reuse

Use the complete original quartic returned law and true complex midpoint in [C76](Yin_C_G0076_v1.md#statement), with the frozen six-digit boundary in [C80](Yin_C_G0080_v1.md#statement).
The adopted [C169](Yin_C_G0169_v1.md#statement) gives a uniform gap for two all-but-one resamplings, but its midpoint energy remains comparable to the unknown moment.
The [complete midpoint theorem](Yin_C_G0204_v1.md#midpoint-capture-fixed-scope), retained from the inspected L329 input, supplies the actual critical-mean interface and [L332](../ledger/Yin_L_G0332_v1.md#diffusive-moment-fixed-scope) supplies the genuine diffusive-moment obstruction.
[L335](../ledger/Yin_L_G0335_v1.md#integer-midpoint-moment-diagnostic) already gives the exact two-integer marked partition, and [L353](../ledger/Yin_L_G0353_v1.md#general-conditioning-amplification) already gives the complete original endpoint-conditioned covariance and amplification formula.
Those formulas are not recreated as new work.
The finite-rank interface at the complete current [C517 home](Yin_C_G0517_v1.md#actual-finite-tail-space-rank) is a comparison for the overlap invariant; it does not establish mixing or change the original weights.

The changed goal is a conditional operator whose true midpoint energy is bounded by the overlap alone, independently of the total word length.
Its unresolved quantitative condition will be an explicitly specified weighted finite carry contraction, rather than an unspecified global sampler gap.
The first overlap with no forced rational-rank invariant has a separately retained bounded finite protocol; no numerical result is a premise of this theorem.

<a id="short-overlap-operator-and-energy"></a>
## 1. Complete blocks and an overlap-only midpoint energy bound

Fix P(t)=1-t-t^2-t^3+t^4, its exterior root beta and one neutral conjugate zeta.
For integers n>=3 and 1<=b<n put N=2n and k=n-b.
The exact spectral formula below will use n>=5; the two-digit invariant will also cover n=3,4.
Split the positions into the left tail A={0,...,k-1}, middle B={k,...,k+2b-1} and right tail C={k+2b,...,2n-1}.
Let H_A be conditional expectation given EVERY left-tail digit and H_C conditional expectation given EVERY right-tail digit, in the complete returned law pi_N.
Thus H_A resamples B union C, H_C resamples A union B, and both blocks have length n+b with overlap2b.
Set

    K_(n,b)=(H_A+H_C)/2,
    Z_n=-zeta^-n sum_(j<n)eta_j zeta^j,
    m_n=E_pi_N |Z_n|^2,
    D_(n,b)=<Z_n,(I-K_(n,b))Z_n>_pi_N.             (1)

The full original weights are used on every complete same-endpoint conditional fiber.
Each H is a self-adjoint positive conditional-expectation projection, so K is a reversible positive Markov contraction, without an assumed global gap or connectivity.
Global sign reversal gives E Z_n=0.
The ordinary conditional-variance identity gives

    D_(n,b)=[E Var(Z_n | A digits)
                   +E Var(Z_n | C digits)]/2 <= b^2.       (2)

For the first term, the negative left-half expression for Z_n has its A-tail contribution fixed, and its remaining contribution is the sum of b neutral digit terms.
That random remainder has modulus at most b.
Its conditional variance is at most its conditional second moment, hence at most b^2.
For the second term use the equally exact right-half expression

    Z_n=sum_(j=n)^(2n-1)eta_j zeta^(j-n),

which follows from the full original return at zeta.
Its C-tail contribution is fixed and only the b right-middle digits remain.
This proves(2) without a zero-endpoint assumption, without discarding either conditional mean, and without replacing the original law by a Gaussian or uniform fiber.
The estimate concerns two actual resamplings; it is not a sum of unpaid overlapping lower certificates.

The declared digit-work clock is

    K_(n,b)^cost=(1-1/(n+b))I+K_(n,b)/(n+b).        (3)

It has one expected resampled coordinate per tick, with both its gap and its Dirichlet energy divided by n+b.
This is not a claim of an efficient exact sampler or equality with the original chronological process.
The Poincare ratio for the original moment is unchanged by this simultaneous clock division.

<a id="short-overlap-algebraic-invariant"></a>
## 2. A decisive obstruction at a two-digit overlap

Let a=sum_(j in A)eta_j beta^j and put

    V_(n,b)=span_Q{beta^k,...,beta^(k+2b-1)}.

The class of a in Q(beta)/V_(n,b) is invariant under BOTH resamplings.
Indeed H_A keeps a fixed.
An H_C update keeps the right tail fixed and changes the other two endpoint contributions by opposite amounts, so the change in a belongs to V_(n,b).
The dimension of V_(n,b) is min(2b,4), by the independence of consecutive powers up to the actual degree and invertibility of beta.
The finite-span distinction is consistent with the already retained L282 comparison; no bounded-digit filling or mixing conclusion is inferred from a rank calculation.

For b=1 the invariant is NONCONSTANT on the actual returned support for every n>=3.
Take the all-zero word and the legal returned word with polynomial t^(n-2)P(t).
The latter fits the length2n window and has left-tail endpoint beta^(n-2), because A ends at n-2.
This endpoint is not in span_Q{beta^(n-1),beta^n}: otherwise1 would lie in span_Q{beta,beta^2}, contradicting the degree4 minimal polynomial.
Both words have strictly positive original conditional probability.
A centered indicator of an invariant class therefore has positive variance and zero Dirichlet energy, giving

    gap(K_(n,1))=0 for every n>=3.                 (4)

This is a macroscopic-update obstruction, distinct from the frozen six-digit family of C80.
It does not assert that the true midpoint itself is constant on each component, or classify its moment or critical mean.

At b=2 the four consecutive overlap powers form an integral basis of Z[beta], because beta is a unit.
Thus both this rational-span invariant and its analogous integral quotient invariant are trivial.
This removes only the forced algebraic obstruction; it does NOT prove connectivity or a uniform gap for the constrained weighted graph.
The four-digit overlap is the first centered overlap not already rejected by(4).

<a id="short-overlap-exact-carry-matrix"></a>
## 3. Exact endpoint reduction with every original multiplicity

For l>=0 and a in O=Z[beta], let c_l(a) be the sum of2^(number of zero digits) over ALL l-digit ternary words with endpoint a=sum_(j<l)eta_j beta^j.
Set c_0(0)=1 and c_0(a)=0 otherwise.
Thus Pr(endpoint a)=4^-l c_l(a), and all sums below have finite support.
Use a for the left-tail endpoint in its own positions0,...,k-1, and c for the right-tail endpoint after shifting its positions down by k+2b.
The complete integer joint weight of these two endpoint labels under full return is

    W_(n,b)(a,c)=c_k(a)c_k(c)
                   c_(2b)(-beta^-k a-beta^(2b)c),
    S=sum_(a,c) W_(n,b)(a,c)=c_(2n)(0),
    r(a)=sum_c W_(n,b)(a,c), h(c)=sum_a W_(n,b)(a,c).       (5)

The middle endpoint equation is a+beta^k u+beta^(k+2b)c=0.
Its unique required value is u=-beta^-k a-beta^(2b)c, proving(5) by independence of the three original digit blocks before conditioning.
No powers of4 are omitted: the total length is2k+2b=2n, so they cancel exactly after division by S.
Remove only zero-marginal endpoint labels; every remaining r(a),h(c) is positive.
The normalized endpoint incidence matrix is

    M(a,c)=W_(n,b)(a,c)/sqrt(r(a)h(c)).             (6)

Its leading singular value is1, with unit singular vectors sqrt(r/S) and sqrt(h/S).
Let rho_(n,b) be its second singular value, counted with multiplicity, including another singular value1 when the bipartite graph is disconnected.
For n>=5 and1<=b<n, both sides have at least two positive endpoint labels: a shifted signed P crossing either tail boundary supplies a nonzero label as well as zero.
Thus this definition has no one-state exception in the stated domain.

The complete returned-word heat bath has exactly

    gap(K_(n,b))=(1-rho_(n,b))/2.                 (7)

Here is the full finite reduction.
Conditional on a left-tail WORD, the law of a right-tail word depends on the first word only through its endpoint a, and similarly in the opposite direction.
Within a fixed endpoint, the word law retains its original weight divided by c_k(a).
A function of the left-tail word with conditional mean zero at each a is therefore killed by H_C and fixed by H_A, so it is an eigenfunction of K with eigenvalue1/2.
The corresponding right-tail residual space has the same property; these two residual spaces are orthogonal.
On the endpoint-function spaces, the conditional map from one side to the other is precisely M after weighting coordinates by sqrt(r/S) and sqrt(h/S).
For a singular pair with value s in(0,1), lift its two unit vectors to endpoint functions f and g.
They satisfy H_A g=s f, H_C f=s g, H_A f=f and H_C g=g.
Consequently f+g and f-g have eigenvalues(1+s)/2 and(1-s)/2 for K.
A singular value0 supplies eigenvalue1/2 on the corresponding nonconstant one-sided space.
A singular value1 gives a common function of both tails and eigenvalue1; the first such function is constant, and further ones record the graph components.
The orthogonal complement of both tail-function spaces is killed by both projections.
These spaces exhaust the finite space through the singular-vector decomposition, proving(7).
This is the finite elementary two-projection argument; the existing [BSS17-U001](../audits/literature/BSS17/Yin_U001.md#bss17-u001) provides classical attribution and is not an original-law or mixing theorem.
No generic two-projection representation is being assumed to bound rho.

Equivalently the two-step left-endpoint transition is the rational matrix

    T(a,a')=sum_c W(a,c)W(a',c)/(r(a)h(c)),        (8)

reversible for r(a)/S, whose nontrivial top eigenvalue is rho^2.
Thus all original word multiplicities are preserved in a smaller sparse object; singular values of an unweighted adjacency matrix would describe a different chain.
Every connected component of this endpoint graph corresponds exactly to a complete returned-word component, because words with the same endpoint have the same positive neighboring fibers and each complete conditional fiber is resampled.
Connectivity is only the finite statement rho<1, not a uniform contraction as n grows.

Combining(2) and(7) gives the genuinely changed conditional target

    (1-rho_(n,b)) m_n <=2b^2.                    (9)

For any FIXED b, an additional eventual bound rho_(n,b)<=1-delta with delta>0 would imply m_n<=2b^2/delta, and hence finite original critical mean through L329 and the fixed nonneutral strips.
At b=2 the required moment bound is m_n<=8/delta.
Conversely a supplied m_n>=epsilon n forces1-rho_(n,b)<=2b^2/(epsilon n), without a converse diffusion implication.
Unlike C169's energy comparable to the unknown moment, the new upper energy bound is independent of n.
The uniform carry contraction remains unproved.

<a id="four-digit-overlap-exact-marks"></a>
## 4. The first unobstructed overlap has a complete sparse marked formula

Fix b=2 and n>=5, so k=n-2.
The four powers1,beta,beta^2,beta^3 form the integral basis of O=Z[beta] used here; no maximal-order identification is asserted.
Hence c_4(u) is zero unless the four coordinates of u lie in{-1,0,1}; in that case there is exactly ONE middle word theta=(theta_0,...,theta_3), and c_4(u)=2^z(theta).
Each positive left endpoint has at most3^4=81 right neighbors, and the same bound holds in the other direction.
For an edge(a,c), put x=beta^-k a and let theta be the four coordinates of-x-beta^4 c.
The actual midpoint algebraic integer is

    y_(a,c)=-beta^-2[x+theta_0+theta_1 beta],
    Z_(a,c)=y_(a,c)(zeta).                         (10)

All outer words in this endpoint pair give the same true midpoint, because evaluation at every conjugate depends only on their algebraic endpoints and the unique middle word.
Thus there is no missing within-pair midpoint variance.

For q=a_0+a_1 beta+a_2 beta^2+a_3 beta^3 with rational coordinates, use the old L335 exact neutral-square map

    Phi(q)=s_0+s_2+3s_3+u(s_1+s_2+s_3),
    s_l=sum_(j=0)^(3-l)a_j a_(j+l),
    u=(1-sqrt13)/2.                                (11)

It equals |q(zeta)|^2 and belongs to Q(sqrt13), with the specified real embedding.
The other trace embedding is not another squared Euclidean norm.
Let ybar_a=sum_c W(a,c)y_(a,c)/r(a), and ybar_c=sum_a W(a,c)y_(a,c)/h(c).
The entire true moment and update energy are then

    m_n=S^-1 sum_(a,c) W(a,c)Phi(y_(a,c)),
    D_(n,2)=m_n-(2S)^-1
                 [sum_a r(a)Phi(ybar_a)+sum_c h(c)Phi(ybar_c)],
    0<=D_(n,2)<=min(m_n,4).                         (12)

These exact algebraic quantities retain all endpoint-conditioned means.
The same integer edge table gives every component's original mass and its exact conditional midpoint mean and second moment.
A disconnected graph must not be reported as a midpoint obstruction without checking those marked component quantities.
Formula(12) is a new sparse evaluation interface for this operator, not a new definition or proof of L335's original marked partition.
The latter supplies an independent half-word check of S and m_n.

The separate [J106 native protocol](../computations/programs/Yin_J_G0106/record.md) owns its six finite inputs, programs, resource constraints and any eventual computational findings.
The present analytic theorem does not depend on a numerical result.

## Current assessment
[Selected decision](#decision-isolated-short-overlap-review-20261023)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T15:19 |
| status | open |
| reason | Register the complete shorter-overlap operator and original weighted carry reduction, overlap-only midpoint energy, all-length two-digit invariant, exact four-digit marks and explicitly conditional critical-mean criterion for actual whole review. No numerical outcome or uniform contraction is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete operator statement](#statement) | General n>=3 operator and clock, b1 obstruction n>=3, exact spectral reduction n>=5 and first unobstructed b2 marked graph; all full weights and conditional conclusions. |
| argument | [Full original-weight proof](#short-overlap-operator-and-energy) | Complete Sections1--4 and formulas1--12, including the full-word/endpoint decomposition, invariant, singular multiplicities, exact marks and all scope boundaries. |
| dependency | [C76 original law](Yin_C_G0076_v1.md#statement) | Actual quartic, original ternary weights and neutral midpoint conventions only; the new lengths/operators are proved directly, not imported from the old n>=7 local theorem. |
| dependency | [L329 critical-mean interface](../ledger/Yin_L_G0329_v1.md#midpoint-capture-fixed-scope) | A genuinely established bounded original midpoint moment yields tightness and finite critical mean at this recurrent quartic; the required uniform contraction remains additional. |
| dependency | [L335 exact neutral square](../ledger/Yin_L_G0335_v1.md#integer-midpoint-moment-diagnostic) | Original-order coordinate formula in the specified Q(sqrt13) embedding and complete marked-partition convention; no sign is borrowed from the other trace embedding. |
| support | [C169 changed-scale comparison](Yin_C_G0169_v1.md#statement) | All-but-one uniform gap has energy comparable to an unknown moment; no gap is transferred to the new shorter overlap. |
| support | [C80 frozen six-digit scope](Yin_C_G0080_v1.md#statement) | Different old local operator, with its own components and masses retained; not a proof of the new invariant. |
| support | [L332 true diffusion boundary](../ledger/Yin_L_G0332_v1.md#diffusive-moment-fixed-scope) | Actual moment versus linear proxy and conditional diffusion/mean distinctions, not a new lower moment premise. |
| support | [L353 full conditioning cost](../ledger/Yin_L_G0353_v1.md#general-conditioning-amplification) | Complete original weights and conditional means are retained; no unpaid overlapping lower-certificate sum is used. |
| support | [L282 finite span comparison](../ledger/Yin_L_G0282_v1.md#actual-finite-tail-space-rank) | Finite rank differs from limiting rank and does not imply bounded-digit filling or mixing. |
| support | [BSS17-U001 attribution](../audits/literature/BSS17/Yin_U001.md#bss17-u001) | Classical two-projection representation at its retained statement/applicability scope; the needed finite singular-pair proof is supplied locally without a source mixing theorem. |

### Decision retained-mean-interface

| Field | Value |
| --- | --- |
| date | 2026-10-20T22:12 |
| status | proved |
| reason | Adopt the complete shorter-overlap original-law theorem through actual whole R556 review. The overlap-only energy, all-length b1 obstruction, full-word weighted spectral reduction and b2 exact marks are proved; the eventual uniform carry contraction remains an explicit additional hypothesis, so no critical-mean classification is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete operator statement](#statement) | General n>=3 operator and clock, b1 obstruction n>=3, exact spectral reduction n>=5 and first unobstructed b2 marked graph; all full weights and conditional conclusions. |
| argument | [Full original-weight proof](#short-overlap-operator-and-energy) | Complete Sections1--4 and formulas1--12, including the full-word/endpoint decomposition, invariant, singular multiplicities, exact marks and all scope boundaries. |
| dependency | [C76 original law](Yin_C_G0076_v1.md#statement) | Actual quartic, original ternary weights and neutral midpoint conventions only; the new lengths/operators are proved directly, not imported from the old n>=7 local theorem. |
| dependency | [Retained critical-mean interface](Yin_C_G0204_v1.md#midpoint-capture-fixed-scope) | A genuinely established bounded original midpoint moment yields tightness and finite critical mean at this recurrent quartic; the required uniform contraction remains additional. |
| dependency | [L335 exact neutral square](../ledger/Yin_L_G0335_v1.md#integer-midpoint-moment-diagnostic) | Original-order coordinate formula in the specified Q(sqrt13) embedding and complete marked-partition convention; no sign is borrowed from the other trace embedding. |
| support | [C169 changed-scale comparison](Yin_C_G0169_v1.md#statement) | All-but-one uniform gap has energy comparable to an unknown moment; no gap is transferred to the new shorter overlap. |
| support | [C80 frozen six-digit scope](Yin_C_G0080_v1.md#statement) | Different old local operator, with its own components and masses retained; not a proof of the new invariant. |
| support | [L332 true diffusion boundary](../ledger/Yin_L_G0332_v1.md#diffusive-moment-fixed-scope) | Actual moment versus linear proxy and conditional diffusion/mean distinctions, not a new lower moment premise. |
| support | [L353 full conditioning cost](../ledger/Yin_L_G0353_v1.md#general-conditioning-amplification) | Complete original weights and conditional means are retained; no unpaid overlapping lower-certificate sum is used. |
| support | [L282 finite span comparison](../ledger/Yin_L_G0282_v1.md#actual-finite-tail-space-rank) | Finite rank differs from limiting rank and does not imply bounded-digit filling or mixing. |
| support | [BSS17-U001 attribution](../audits/literature/BSS17/Yin_U001.md#bss17-u001) | Classical two-projection representation at its retained statement/applicability scope; the needed finite singular-pair proof is supplied locally without a source mixing theorem. |
| review | [Whole shorter-overlap finding](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Complete actual fixed statement, Sections1--4, all twelve formulas, initial declarations and used original-law/critical-mean/source interfaces; noncontribution is recorded but inherited substantive development context remains unknown; native evidence is not an analytic premise. |


### Decision current-complete-moment-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:48 |
| status | proved |
| reason | Maintain the same already selected midpoint/control interface at its complete current C285 proof home. The original statement, full proof, old decisions and actual R inputs remain unchanged; no new lower-moment premise or broader review is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete operator statement](#statement) | General n>=3 operator and clock, b1 obstruction n>=3, exact spectral reduction n>=5 and first unobstructed b2 marked graph; all full weights and conditional conclusions. |
| argument | [Full original-weight proof](#short-overlap-operator-and-energy) | Complete Sections1--4 and formulas1--12, including the full-word/endpoint decomposition, invariant, singular multiplicities, exact marks and all scope boundaries. |
| dependency | [C76 original law](Yin_C_G0076_v1.md#statement) | Actual quartic, original ternary weights and neutral midpoint conventions only; the new lengths/operators are proved directly, not imported from the old n>=7 local theorem. |
| dependency | [Retained critical-mean interface](Yin_C_G0204_v1.md#midpoint-capture-fixed-scope) | A genuinely established bounded original midpoint moment yields tightness and finite critical mean at this recurrent quartic; the required uniform contraction remains additional. |
| dependency | [L335 exact neutral square](../ledger/Yin_L_G0335_v1.md#integer-midpoint-moment-diagnostic) | Original-order coordinate formula in the specified Q(sqrt13) embedding and complete marked-partition convention; no sign is borrowed from the other trace embedding. |
| support | [C169 changed-scale comparison](Yin_C_G0169_v1.md#statement) | All-but-one uniform gap has energy comparable to an unknown moment; no gap is transferred to the new shorter overlap. |
| support | [C80 frozen six-digit scope](Yin_C_G0080_v1.md#statement) | Different old local operator, with its own components and masses retained; not a proof of the new invariant. |
| support | [Complete true diffusion boundary](Yin_C_G0285_v1.md#diffusive-moment-fixed-scope) | Actual moment versus linear proxy and conditional diffusion/mean distinctions, not a new lower moment premise. |
| support | [L353 full conditioning cost](../ledger/Yin_L_G0353_v1.md#general-conditioning-amplification) | Complete original weights and conditional means are retained; no unpaid overlapping lower-certificate sum is used. |
| support | [L282 finite span comparison](../ledger/Yin_L_G0282_v1.md#actual-finite-tail-space-rank) | Finite rank differs from limiting rank and does not imply bounded-digit filling or mixing. |
| support | [BSS17-U001 attribution](../audits/literature/BSS17/Yin_U001.md#bss17-u001) | Classical two-projection representation at its retained statement/applicability scope; the needed finite singular-pair proof is supplied locally without a source mixing theorem. |
| review | [Whole shorter-overlap finding](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Complete actual fixed statement, Sections1--4, all twelve formulas, initial declarations and used original-law/critical-mean/source interfaces; noncontribution is recorded but inherited substantive development context remains unknown; native evidence is not an analytic premise. |


### Decision current-complete-lower-fiber-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:36 |
| status | proved |
| reason | Maintain the same already selected original-law, endpoint-conditioned covariance or signed-square input at its complete current C300 proof home. The selected statement and proof, old decisions and actual old Review inputs remain unchanged; no new diffusive premise or broader review is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete operator statement](#statement) | General n>=3 operator and clock, b1 obstruction n>=3, exact spectral reduction n>=5 and first unobstructed b2 marked graph; all full weights and conditional conclusions. |
| argument | [Full original-weight proof](#short-overlap-operator-and-energy) | Complete Sections1--4 and formulas1--12, including the full-word/endpoint decomposition, invariant, singular multiplicities, exact marks and all scope boundaries. |
| dependency | [C76 original law](Yin_C_G0076_v1.md#statement) | Actual quartic, original ternary weights and neutral midpoint conventions only; the new lengths/operators are proved directly, not imported from the old n>=7 local theorem. |
| dependency | [Retained critical-mean interface](Yin_C_G0204_v1.md#midpoint-capture-fixed-scope) | A genuinely established bounded original midpoint moment yields tightness and finite critical mean at this recurrent quartic; the required uniform contraction remains additional. |
| dependency | [L335 exact neutral square](Yin_C_G0300_v1.md#integer-midpoint-moment-diagnostic) | Original-order coordinate formula in the specified Q(sqrt13) embedding and complete marked-partition convention; no sign is borrowed from the other trace embedding. |
| support | [C169 changed-scale comparison](Yin_C_G0169_v1.md#statement) | All-but-one uniform gap has energy comparable to an unknown moment; no gap is transferred to the new shorter overlap. |
| support | [C80 frozen six-digit scope](Yin_C_G0080_v1.md#statement) | Different old local operator, with its own components and masses retained; not a proof of the new invariant. |
| support | [Complete true diffusion boundary](Yin_C_G0285_v1.md#diffusive-moment-fixed-scope) | Actual moment versus linear proxy and conditional diffusion/mean distinctions, not a new lower moment premise. |
| support | [L353 full conditioning cost](../ledger/Yin_L_G0353_v1.md#general-conditioning-amplification) | Complete original weights and conditional means are retained; no unpaid overlapping lower-certificate sum is used. |
| support | [L282 finite span comparison](../ledger/Yin_L_G0282_v1.md#actual-finite-tail-space-rank) | Finite rank differs from limiting rank and does not imply bounded-digit filling or mixing. |
| support | [BSS17-U001 attribution](../audits/literature/BSS17/Yin_U001.md#bss17-u001) | Classical two-projection representation at its retained statement/applicability scope; the needed finite singular-pair proof is supplied locally without a source mixing theorem. |
| review | [Whole shorter-overlap finding](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Complete actual fixed statement, Sections1--4, all twelve formulas, initial declarations and used original-law/critical-mean/source interfaces; noncontribution is recorded but inherited substantive development context remains unknown; native evidence is not an analytic premise. |

### Decision current-complete-finite-pressure-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:54 |
| status | proved |
| reason | Maintain only the previously selected finite-real-span comparison support at its complete same-object C517 home, without bounded-digit filling, connectivity or mixing. The exact statement/proof, state, other input tuples, old decisions and actual original Review inputs remain unchanged; no broader theorem or new review is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | General n>=3 operator and clock, b1 obstruction n>=3, exact spectral reduction n>=5 and first unobstructed b2 marked graph; all full weights and conditional conclusions. |
| argument | [Exact argument](#short-overlap-operator-and-energy) | Complete Sections1--4 and formulas1--12, including the full-word/endpoint decomposition, invariant, singular multiplicities, exact marks and all scope boundaries. |
| dependency | [Exact dependency](Yin_C_G0076_v1.md#statement) | Actual quartic, original ternary weights and neutral midpoint conventions only; the new lengths/operators are proved directly, not imported from the old n>=7 local theorem. |
| dependency | [Exact dependency](Yin_C_G0204_v1.md#midpoint-capture-fixed-scope) | A genuinely established bounded original midpoint moment yields tightness and finite critical mean at this recurrent quartic; the required uniform contraction remains additional. |
| dependency | [Exact dependency](Yin_C_G0300_v1.md#integer-midpoint-moment-diagnostic) | Original-order coordinate formula in the specified Q(sqrt13) embedding and complete marked-partition convention; no sign is borrowed from the other trace embedding. |
| support | [Exact support](Yin_C_G0169_v1.md#statement) | All-but-one uniform gap has energy comparable to an unknown moment; no gap is transferred to the new shorter overlap. |
| support | [Exact support](Yin_C_G0080_v1.md#statement) | Different old local operator, with its own components and masses retained; not a proof of the new invariant. |
| support | [Exact support](Yin_C_G0285_v1.md#diffusive-moment-fixed-scope) | Actual moment versus linear proxy and conditional diffusion/mean distinctions, not a new lower moment premise. |
| support | [Exact support](../ledger/Yin_L_G0353_v1.md#general-conditioning-amplification) | Complete original weights and conditional means are retained; no unpaid overlapping lower-certificate sum is used. |
| support | [Exact support](Yin_C_G0517_v1.md#actual-finite-tail-space-rank) | Finite rank differs from limiting rank and does not imply bounded-digit filling or mixing. |
| support | [Exact support](../audits/literature/BSS17/Yin_U001.md#bss17-u001) | Classical two-projection representation at its retained statement/applicability scope; the needed finite singular-pair proof is supplied locally without a source mixing theorem. |
| review | [Exact review](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Complete actual fixed statement, Sections1--4, all twelve formulas, initial declarations and used original-law/critical-mean/source interfaces; noncontribution is recorded but inherited substantive development context remains unknown; native evidence is not an analytic premise. |

### Decision isolated-short-overlap-review-20261023

| Field | Value |
| --- | --- |
| date | 2026-10-23T01:22 |
| status | proved |
| reason | Add the newly performed isolated whole mathematical review of the complete shorter-overlap theorem. Preserve the proved statement, selected Sections 1--4, all current dependency/support tuples and the original unknown-relationship account at its actual historical scope. The eventual contraction remains additional; no critical-mean classification or Task completion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | General n>=3 operator and clock, b1 obstruction n>=3, exact spectral reduction n>=5 and first unobstructed b2 marked graph; all full weights and conditional conclusions. |
| argument | [Exact argument](#short-overlap-operator-and-energy) | Complete Sections1--4 and formulas1--12, including the full-word/endpoint decomposition, invariant, singular multiplicities, exact marks and all scope boundaries. |
| dependency | [Exact dependency](Yin_C_G0076_v1.md#statement) | Actual quartic, original ternary weights and neutral midpoint conventions only; the new lengths/operators are proved directly, not imported from the old n>=7 local theorem. |
| dependency | [Exact dependency](Yin_C_G0204_v1.md#midpoint-capture-fixed-scope) | A genuinely established bounded original midpoint moment yields tightness and finite critical mean at this recurrent quartic; the required uniform contraction remains additional. |
| dependency | [Exact dependency](Yin_C_G0300_v1.md#integer-midpoint-moment-diagnostic) | Original-order coordinate formula in the specified Q(sqrt13) embedding and complete marked-partition convention; no sign is borrowed from the other trace embedding. |
| support | [Exact support](Yin_C_G0169_v1.md#statement) | All-but-one uniform gap has energy comparable to an unknown moment; no gap is transferred to the new shorter overlap. |
| support | [Exact support](Yin_C_G0080_v1.md#statement) | Different old local operator, with its own components and masses retained; not a proof of the new invariant. |
| support | [Exact support](Yin_C_G0285_v1.md#diffusive-moment-fixed-scope) | Actual moment versus linear proxy and conditional diffusion/mean distinctions, not a new lower moment premise. |
| support | [Exact support](../ledger/Yin_L_G0353_v1.md#general-conditioning-amplification) | Complete original weights and conditional means are retained; no unpaid overlapping lower-certificate sum is used. |
| support | [Exact support](Yin_C_G0517_v1.md#actual-finite-tail-space-rank) | Finite rank differs from limiting rank and does not imply bounded-digit filling or mixing. |
| support | [Exact support](../audits/literature/BSS17/Yin_U001.md#bss17-u001) | Classical two-projection representation at its retained statement/applicability scope; the needed finite singular-pair proof is supplied locally without a source mixing theorem. |
| review | [Exact review](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Complete actual fixed statement, Sections1--4, all twelve formulas, initial declarations and used original-law/critical-mean/source interfaces; noncontribution is recorded but inherited substantive development context remains unknown; native evidence is not an analytic premise. |
| review | [Fresh isolated review](../audits/reviews/Yin_R_G0803_v1.md#fresh-short-overlap-whole-finding) | Complete mathematical statement and Sections 1--4, all formulas (1)--(12), exact domains, original weights, word-space spectrum, midpoint marks, conditional means and clock costs; initial findings preceded old-review comparison, with later current-source-home coordination explicitly disclosed. |

## Historical assessments

<a id="decision-whole-reviewed-2026-10-18"></a>

### Historical assessment whole-reviewed-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T15:24 |
| status | proved |
| review-status | independently reviewed |
| reason | Adopt the complete shorter-overlap original-law theorem through actual whole R556 review. The overlap-only energy, all-length b1 obstruction, full-word weighted spectral reduction and b2 exact marks are proved; the eventual uniform carry contraction remains an explicit additional hypothesis, so no critical-mean classification is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete operator statement](#statement) | General n>=3 operator and clock, b1 obstruction n>=3, exact spectral reduction n>=5 and first unobstructed b2 marked graph; all full weights and conditional conclusions. |
| argument | [Full original-weight proof](#short-overlap-operator-and-energy) | Complete Sections1--4 and formulas1--12, including the full-word/endpoint decomposition, invariant, singular multiplicities, exact marks and all scope boundaries. |
| dependency | [C76 original law](Yin_C_G0076_v1.md#statement) | Actual quartic, original ternary weights and neutral midpoint conventions only; the new lengths/operators are proved directly, not imported from the old n>=7 local theorem. |
| dependency | [L329 critical-mean interface](../ledger/Yin_L_G0329_v1.md#midpoint-capture-fixed-scope) | A genuinely established bounded original midpoint moment yields tightness and finite critical mean at this recurrent quartic; the required uniform contraction remains additional. |
| dependency | [L335 exact neutral square](../ledger/Yin_L_G0335_v1.md#integer-midpoint-moment-diagnostic) | Original-order coordinate formula in the specified Q(sqrt13) embedding and complete marked-partition convention; no sign is borrowed from the other trace embedding. |
| support | [C169 changed-scale comparison](Yin_C_G0169_v1.md#statement) | All-but-one uniform gap has energy comparable to an unknown moment; no gap is transferred to the new shorter overlap. |
| support | [C80 frozen six-digit scope](Yin_C_G0080_v1.md#statement) | Different old local operator, with its own components and masses retained; not a proof of the new invariant. |
| support | [L332 true diffusion boundary](../ledger/Yin_L_G0332_v1.md#diffusive-moment-fixed-scope) | Actual moment versus linear proxy and conditional diffusion/mean distinctions, not a new lower moment premise. |
| support | [L353 full conditioning cost](../ledger/Yin_L_G0353_v1.md#general-conditioning-amplification) | Complete original weights and conditional means are retained; no unpaid overlapping lower-certificate sum is used. |
| support | [L282 finite span comparison](../ledger/Yin_L_G0282_v1.md#actual-finite-tail-space-rank) | Finite rank differs from limiting rank and does not imply bounded-digit filling or mixing. |
| support | [BSS17-U001 attribution](../audits/literature/BSS17/Yin_U001.md#bss17-u001) | Classical two-projection representation at its retained statement/applicability scope; the needed finite singular-pair proof is supplied locally without a source mixing theorem. |
| review | [Whole shorter-overlap finding](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Complete actual fixed statement, Sections1--4, all twelve formulas, initial declarations and used original-law/critical-mean/source interfaces; nonblind noncontributor review, with native evidence not an analytic premise. |
