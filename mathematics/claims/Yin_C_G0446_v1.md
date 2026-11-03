---
author: Yin
---

# Complete true positive-log tail lower bounds and coefficient-scale accuracy cost

This retains the complete necessary mathematical argument from [the complete original G382 account](../ledger/Yin_L_G0382_v1.md).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P be any nonzero integer polynomial, retain all factors/content/multiplicities, set H=sum|a_j|, m=m(P), M=exp(m), and for every integer N>=1 use precisely

    nu_n=integral_circle(1-|P|^2/H^2)^n dmu,
    T_N=log H-(1/2)sum_(n=1)^N nu_n/n,
    T_N-m=(1/2)sum_(n>N)nu_n/n.

No squarefree or circle-zero exclusion is required for this identity.
For x_P=M^2/H^2 in(0,1] and r_N(x)=(1/2)sum_(n>N)(1-x)^n/n,

    T_N-m>=r_N(x_P)>=(1/4)(1-x_P)^(2N).

The full supporting-line proof uses the original X=|P|²/H² and integrable Y=logX, with

    g_N(y)=r_N(exp y),
    g_N'(y)=-(1-exp y)^N/2,
    g_N''(y)=N exp y(1-exp y)^(N-1)/2>=0.

The bounded derivative proves integrability and justifies the comparison at the finite mean log x_P, including all finite-multiplicity zeros.
For a monomial P=a t^j, M=H and all positive moments/remainders vanish.
For a nonmonomial, the nonzero extreme autocorrelation proves x_P<1.

For every nonmonomial and every0<delta<1/4, the accuracy premise T_N-m<=delta necessarily implies

    N>=log(1/(4delta))/[-2log(1-x_P)]
      >=(1/2)(H²/M²-1)log(1/(4delta)).

This is a necessary window for absolute accuracy of the uncorrected truncation, not a sufficient estimate or a universal obstruction to a corrected lower certificate.
Independently,

    T_N-m>=log(H/M)-H_N/2
           >=(1/2)log[H²/(e M² N)],

where H_N is the harmonic number; the right side may be negative while the actual tail is nonnegative.
For fixed B with M<=B and fixed delta, the necessary window grows at least as a positive delta-dependent multiple of H²/B² minus a constant.
For fixed C>0, if additionally N<=C d with d the actual degree, then H²<=M²[1+2Cd/log(1/(4delta))].
Integer support count k<=H gives k=O(sqrt d) at fixed B,C,delta.
For bounded M and H²/N tending to infinity, the true tail itself tends to infinity.
The fast O(Nd²) arithmetic recurrence retains its full growing bit/live/output costs and does not remove this necessary N.

The accepted fixed-support DS17 statement implies that every hypothetical sequence0<m(P_j)->0 has support count k_j->infinity and H_j->infinity.
No rate forcing H²/d to diverge along every such sequence, explicit sparse gap, actual near-one family or irreducible factor transfer is asserted.
The monomial K1 branch and original unreviewed external foundations remain at their accepted source scope.

For every prime p>=3, the actual full squarefree polynomial

    P_p=(t²-3t+1)(1+t+...+t^(p-1))

has degree p+1, fixed total M=(3+sqrt5)/2 and complete coefficients1,-2, then p-2 copies of-1, then-2,1, so H=p+4.
All cyclotomic roots and coefficients are retained.
For every fixed C>0 and every1<=N<=C(p+1), its true remainder is at least(1/2)log p-O_C(1) and diverges.
Even an arbitrary valid scalar normalization L>=max_circle|P_p| has L>=|P_p1|=p; the same proof/normalized identity gives the same divergence.
This is a reducible fixed-positive-measure cost control, not an irreducible-hard-core or Lehmer counterexample.

A lower certificate T_N-U_N could remain positive after a sufficiently accurate subtraction of a large tail.
These lower bounds on the tail do not rule that out, any full-tail algebraic acceleration, other normalizations on other inputs, rational/oscillatory/root estimators or the separate original H9 Lehmer experiment.
No mathematical program, new source proof, finite computation or Task/E resumption occurs.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:25 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact complete positive logarithmic identity](Yin_C_G0434_v1.md#positive-log-moment-identity) | Only the original full-factor/all-multiplicity series and exact nonnegative remainder; no simple-zero upper-tail condition is imported. |
| dependency | [Exact finite-state arithmetic and bit costs](Yin_C_G0439_v1.md#fast-positive-moment-arithmetic-cost) | Only the actual O(Nd²) arithmetic bound and growing signed bit/live/output costs; no program rerun or lower-tail certificate is supplied by finite evaluation. |
| dependency | [Original fixed-support external input](../audits/literature/DS17/Yin_U002.md#ds17-u002) | Only exact accepted univariate nonzero integer fixed-K positive total gap, with direct monomial branch and original unreviewed proof foundations; no new PDF/source-proof audit. |
| dependency | [Retained original support escape](Yin_C_G0221_v1.md#cyclotomic-support-escape) | Only the already proved fixed-K contradiction for positive measures tending to0, including completion1; no new support-rate estimate. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:28 |
| status | proved |
| reason | Adopt the actual complete SELF check of every derivative/supporting-line/all-multiplicity identity, necessary accuracy/harmonic estimate, fixed/sequence quantifier, complete squarefree padding and scalar-normalization control. Clarify C221 as historical method support at its own domain; the general conclusion follows the explicit DS17 statement locally. Preserve all original SELF, source/no-run and accuracy-versus-subtraction boundaries. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0434_v1.md#positive-log-moment-identity) | Only the original full-factor/all-multiplicity series and exact nonnegative remainder; no simple-zero upper-tail condition is imported. |
| dependency | [Exact accepted input](Yin_C_G0439_v1.md#fast-positive-moment-arithmetic-cost) | Only the actual O(Nd²) arithmetic bound and growing signed bit/live/output costs; no program rerun or lower-tail certificate is supplied by finite evaluation. |
| dependency | [Exact accepted input](../audits/literature/DS17/Yin_U002.md#ds17-u002) | Only exact accepted univariate nonzero integer fixed-K positive total gap, with direct monomial branch and original unreviewed proof foundations; no new PDF/source-proof audit. |
| support | [Exact support](Yin_C_G0221_v1.md#cyclotomic-support-escape) | Historical fixed-support escape method credit at its retained monic/completion domain; the present general-nonzero-integer consequence is explicitly proved locally from DS17-U002, not by extending that prior input. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0650_v1.md#current-coefficient-tail-whole-finding) | Entire exact Statement and Argument and original full Sections1–4/equations1–7, all old whole bindings, precise domains, actual family, useful limits and original author/source checking. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="complete-positive-log-coefficient-tail-cost"></a>
The exact current nonnegative series and all-multiplicity tail are retained in [C434](Yin_C_G0434_v1.md#positive-log-moment-identity), and its unchanged fast recurrence/cost interface in [C439](Yin_C_G0439_v1.md#fast-positive-moment-arithmetic-cost).
The original dated method/reuse/status account remains at L382, and the precise fixed-support consequence is retained in [C221](Yin_C_G0221_v1.md#cyclotomic-support-escape).

<a id="geometric-mean-positive-tail-lower-bound"></a>
## 1. Exact lower bound from the original geometric mean

For0<x<=1 define

    r_N(x)=(1/2)sum_(n>N)(1-x)^n/n,
    x_P=M^2/H^2 in(0,1].                              (2)

For every N>=1,

    T_N-m(P)>=r_N(x_P).                               (3)

Proof.
The original random variable X=|P(e^(i theta))|^2/H^2 belongs to[0,1] and is positive almost everywhere.
Y=log X is integrable with integral Y=2m(P)-2log H=log x_P.
The geometric-series remainder differentiates on0<x<1 to r_N'(x)=-(1-x)^N/(2x).
Hence g_N(y)=r_N(e^y), y<=0, satisfies

    g_N'(y)=-(1-e^y)^N/2,
    g_N''(y)=N e^y(1-e^y)^(N-1)/2>=0.                (4)

The bounded first derivative also proves that g_N(Y) is integrable.
Its tangent at the finite mean log x_P lies below its graph; integrate that supporting-line inequality.
Nonnegative termwise integration in(1) identifies integral g_N(Y) with T_N-m(P), giving(3).
End value x_P=1 gives zero and needs no derivative formula at minus infinity.
No interchange of an uncontrolled signed series is made.
For a monomial M=H and every nu_n=0, so equality holds trivially.
For a nonmonomial the modulus is nonconstant and x_P<1; strictness is not needed below.

This lower bound uses the geometric mean of the ORIGINAL modulus.
Substituting coefficient energy or a selected conjugate for M would be a different estimate and is not done.

<a id="necessary-quadratic-coefficient-scale"></a>
## 2. Explicit accuracy cost and quantifiers

Summing only n=N+1,...,2N in(2) yields

    r_N(x)>=(1/4)(1-x)^(2N).                          (5)

Consequently, for0<delta<1/4 and a nonmonomial P, the accuracy premise T_N-m(P)<=delta implies

    N>=log(1/(4delta))/[-2log(1-x_P)]
      >=(1/2)(H^2/M^2-1)log(1/(4delta)).              (6)

The last step uses -log(1-x)<=x/(1-x).
Every direction and sign is retained; this is NECESSARY for accuracy, not sufficient.
At fixed upper bound M<=B and fixed delta, useful finite accuracy therefore requires N at least a positive delta-dependent multiple of H^2/B^2 minus a fixed constant.
The recurrence's O(Nd^2) count still pays this growing window; faster evaluation does not remove it.

A complementary bound follows directly from0<=nu_n<=1 and H_N<=1+log N:

    T_N-m(P)>=log(H/M)-H_N/2
             >=(1/2)log(H^2/(e M^2 N)).              (7)

The right side may be negative; it is a valid lower estimate, alongside the nonnegative actual remainder.
In particular bounded M, H^2/N tending to infinity forces the true omitted tail to infinity, not merely an inefficient displayed upper bound.

If the finite window is N<=C d and the same fixed delta accuracy is required, (6) forces H^2<=M^2[1+2Cd/log(1/(4delta))].
Since integer coefficients give H>=k, where k is the number of nonzero coefficients, it also forces k=O(sqrt d) when M is bounded.
This condition does not exclude hypothetical near-one inputs with sufficiently sparse support and does not supply an actual near-one family.

The already accepted [DS17 original bounded-support theorem](../audits/literature/DS17/Yin_U002.md#ds17-u002), as used in [L19](../ledger/Yin_L_G0019_v1.md), says each fixed k has a positive gap.
Thus a hypothetical sequence with0<m(P)->0 has k->infinity and H->infinity.
Formula(6) adds the necessary coefficient-scale window for this particular positive-log estimator.
It does not strengthen the unrestricted Mahler bound itself, and the original DS17 proof-inspection limits remain unchanged.

<a id="squarefree-integer-padding-control"></a>
## 3. An actual squarefree noncyclotomic growing-cost control

For a prime p>=3 take

    P_p(t)=(t^2-3t+1)(1+t+...+t^(p-1)).

This is a squarefree integer polynomial: the prime cyclotomic factor has simple circle roots and is disjoint from the two distinct positive off-circle quadratic roots.
Its degree is p+1, total M=(3+sqrt5)/2 is fixed, and the COMPLETE coefficient list is

    1,-2, then p-2 entries equal to-1, then-2,1.

Consequently H=p+4.
Every factor and coefficient is retained; the cyclotomic factor contributes zero measure but affects the actual normalized moments.
For N<=C(p+1), (7) gives a true remainder diverging at least as (1/2)log p-O_C(1).
Accuracy by this normalized truncation cannot be degree-linear on this actual family.
It is reducible and has fixed positive measure, so it is neither an irreducible-hard-core obstruction nor a counterexample to Lehmer.
Its role is to separate a genuine estimator cost from a possibly crude tail proof.

Even replacing H by ANY valid scalar upper normalization L>=max_circle|P_p| does not remove this control: |P_p(1)|=p, so L>=p.
The same proof applies with x=M^2/L^2 and T_N normalized by L, and the same divergence follows at linear windows.
No assertion is made that H is optimal on other inputs or that every determinant method uses such a normalization.
