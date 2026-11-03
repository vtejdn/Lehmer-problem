---
author: Yin
---

# Complete exact finite arcsine integer-state recurrence and all costs

This retains the complete necessary mathematical argument from [the complete original G379 account](../ledger/Yin_L_G0379_v1.md).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

For every nonzero integer Laurent polynomial, remove only its monomial shift and preserve all coefficients, content and factors.
A monomial P=a z^j has every positive moment nu_n=0 for n>=1 and is treated directly, with ordinary arcsine initial values at n=0.
Otherwise write P(z)=sum_(j=0)^d a_j z^j with actual span d>=1 and a_0 a_d!=0, set H=sum|a_j|, and let C_0=2,C_1=x,C_(l+1)=x C_l-C_(l-1).
Then the unique integer trace polynomial

    R(x)=H^2-b_0-sum_(l=1)^d b_l C_l(x),
    b_l=sum_(j=0)^(d-l) a_j a_(j+l),
    R(z+z^-1)=H^2-P(z)P(z^-1),
    R=sum_(l=0)^d r_l x^l, r_d=-a_0 a_d!=0

has exact degree d, either leading sign and 0<=R<=H^2 on[-2,2].
For all integers n,k>=0, the arcsine probability integral I[n,k]=integral x^k R(x)^n dx/[pi sqrt(4-x^2)] is an integer, initially I[0,2h]=binom(2h,h), I[0,2h+1]=0.
Its scalar nu_n=I[n,0]/H^(2n) is the exact nonnegative logarithmic moment; odd states may be negative.
The complete bounds are |I[n,k]|<=2^k H^(2n) and 0<=I[n+1,0]<=H^2 I[n,0]<=H^(2n+2).

For every n,j>=0, differentiating x^j sqrt(4-x^2) R(x)^(n+1), taking both vanishing endpoint limits and using its integrable derivative gives the full annihilator

    A_(n,j)=sum_(l=0)^d r_l[
       4(j+(n+1)l)x^(j+l-1)
       -(j+1+(n+1)l)x^(j+l+1)].

Omit the coefficient-zero j=l=0 negative-power term.
For k>d put j=k-d-1 and D_(n,j)=[j+1+(n+1)d]r_d!=0.
Every other exponent lies below k, so the exact signed triangular recurrence is

    I[n,k]=[sum_(l=0)^d 4(j+(n+1)l)r_l I[n,j+l-1]
       -sum_(l=0)^(d-1)(j+1+(n+1)l)r_l I[n,j+l+1]]/D_(n,j).

Compute k=d+1,...,2d and then I[n+1,j]=sum_(l=0)^d r_l I[n,j+l] for0<=j<=d.
Induction identifies every state with the integral and proves every signed division exact.
No division by R, positivity of odd states, monic leading coefficient or exclusion of interior/endpoint/repeated zeros is used.

For N>=1, constructing R costs O(d^2) integer arithmetic operations and computing all moments through N costs O(Nd^2) such operations with O(d) live state integers, versus O(N^2d^2) for the direct growing Laurent convolution.
With W=sum|r_l|<=2^(d+2)H^2, every triangular numerator and its partial sums are bounded by5(n+2)d W 2^(2d)H^(2n), and its divisor by(n+2)d W.
All states, products and divisors therefore have B_N=O((N+1)log(2H)+d+log(N+2)+log(d+1)) bits.
Elementary quadratic multiplication/division gives the conservative O(Nd^2 B_N^2) bit bound and O(d B_N) live-state bits; exact division and growing integer size are paid.
Retaining all scalar numerators costs up to O(N^2 log(2H)) output bits; every full vector adds the degree factor and state overhead.
Six checkpoints and a final vector are a narrower retention scope, not all intermediate states.

The original finite evidence is exactly J86's four fixed coefficient lists through n64, all1235 full-state equalities and960 exact signed divisions, and the single original Lehmer input through n1024 with six scalar checkpoints and11 final entries.
The latter has10240 exact divisions/extended bounds,11275 stored-state bounds,1025 scalar bounds,1024 monotonicity checks, max numerator/divisor6513/14bits and1954 final scalar decimal digits with denominator9^2048.
Original direct convolution reaches only64; the original R281 separately implemented recurrence supplies the retained1024 verification at its actual historical scope.
The new whole self-review records one fresh original-domain read-only reconstruction, including all saved mathematical counters, without changing native bytes or asserting historical runtimes anew.
No derivative sum, local radius, complementary modulus, tail/logarithmic enclosure, positive Mahler lower certificate, useful uniform cutoff, additional input/depth or research Task completion follows.
AZ90 supplies selected classical method attribution only; no unseen theorem, source algorithm or external complexity bound is a premise.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:00 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact complete positive logarithmic identity](Yin_C_G0434_v1.md#positive-log-moment-identity) | Only the actual nonnegative moment normalization, all integer factors and distinction between finite moments and the separately paid full tail. |
| support | [Classical total-derivative attribution](../audits/literature/AZ90/Yin_U001.md#az90-u001) | Only the exact recorded selected original pp1–4 method/boundary attribution; no source-wide proof, algorithm/order or complexity theorem is invoked. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:04 |
| status | proved |
| reason | Adopt the actual complete SELF finding of every signed finite-state formula, all endpoint/domain/bit/output costs and the original bounded proof/program/data scopes, including one direct original-domain read-only reconstruction matching all saved mathematical values and counters. No tail/Mahler certificate, fresh isolation, source proof or new input/depth follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0434_v1.md#positive-log-moment-identity) | Only the actual nonnegative moment normalization, all integer factors and distinction between finite moments and the separately paid full tail. |
| support | [Exact support](../audits/literature/AZ90/Yin_U001.md#az90-u001) | Only the exact recorded selected original pp1–4 method/boundary attribution; no source-wide proof, algorithm/order or complexity theorem is invoked. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0642_v1.md#current-finite-arcsine-whole-finding) | Entire current Statement and Argument, full original whole and author-check scope, every original J86 mathematical field/counter at its actual bounded domain, source and negative limits. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="complete-finite-arcsine-integer-state"></a>
The exact current positive-log definition and full tail boundary are retained in [C434](Yin_C_G0434_v1.md#positive-log-moment-identity).
The dated original reading and execution account below remains a historical account, including pending-review language; current adoption is a separate actual decision.

<a id="fast-positive-moment-reuse-and-attribution"></a>
## 1. Responsible inputs and attribution boundary

The complete [D24 positive-moment proof, fixed in L378](../ledger/Yin_L_G0378_v1.md#positive-log-moment-identity), independently reviewed in [R202](../audits/reviews/Yin_R_G0202_v1.md#positive-log-whole-finding), fixes the intended nu_n, original H, exact constant term and lower-tail boundary.
[L358](../ledger/Yin_L_G0358_v1.md#single-haar-moment-lower-certificate) and [J84](../computations/programs/Yin_J_G0084/readme.md) retain the four ORIGINAL polynomial controls and their earlier Chebyshev computation; their old Chebyshev moments are not the new positive moments.
The actual J84 main.py CASES table and computation rules were directly read.
The new comparison uses those exact polynomials, not their old numerical output as an oracle.

A bounded local search found related integration-by-parts and arcsine contexts but no matching finite positive-moment state.
A primary context screen directly read Gert Almkvist and Doron Zeilberger, *The method of differentiating under the integral sign*, [author-hosted23-page PDF](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimPDF/duis.pdf), introduction and total-derivative elimination on pp.1--4.
The source's own header identifies J.Symbolic Computation10(1990),571--591; no independently reconciled final-page metadata or full-source proof audit is claimed.
It explains constructing integral relations by integration by parts and eliminating total derivatives.
This is classical method context only, now recorded at [AZ90-U001](../audits/literature/AZ90/Yin_U001.md#az90-u001).
No holonomic existence theorem, automatic telescoping algorithm, unseen recurrence-order result or source complexity bound is invoked.
The complete actual boundary/triangular proof follows below.
No historical novelty is claimed.

Root supplied the core integral identity and the d+1-state candidate.
The exact signed coefficient formula, integer divisibility, arithmetic/bit/output accounting and bounded implementation/check design below are developed here.
This author-side work and later author-side program checks need a separate whole noncontributor review.

<a id="arcsine-integer-state-domain"></a>
## 2. Exact integer polynomial and arcsine state

Let P(z)=sum_(j=0)^d a_j z^j be a nonmonomial integer polynomial after stripping a monomial, with actual span d>=1 and a_0 a_d!=0.
Keep H=sum|a_j| and B(z)=P(z)P(z^-1).
Symmetry gives the UNIQUE integer polynomial

    R(x)=H^2-b_0-sum_(l=1)^d b_l C_l(x),
    b_l=sum_(j=0)^(d-l) a_j a_(j+l),
    C_l(z+z^-1)=z^l+z^-l,
    R(z+z^-1)=H^2-B(z),
    deg R=d, r_d=-a_0 a_d!=0.                     (1)

The integer polynomials in(1) satisfy C_0=2,C_1=x and C_(l+1)=x C_l-C_(l-1), which proves their monic integral triangular form and the coefficient-norm bound used below.

Write R=sum_(l=0)^d r_l x^l and W=sum|r_l|.
Its leading coefficient may have either sign.
On x in[-2,2],0<=R(x)<=H^2.
The pushforward of Haar probability under x=2cos theta is

    dmu_A(x)=dx/[pi sqrt(4-x^2)] on(-2,2).

For all integers n,k>=0 define

    I[n,k]=integral_(-2)^2 x^k R(x)^n dmu_A(x),
    I[0,2h]=binom(2h,h), I[0,2h+1]=0,
    nu_n=I[n,0]/H^(2n).                            (2)

The initial formula follows from the constant term of(z+z^-1)^k; this also proves that EVERY I[n,k] is an integer, since x^k R(x)^n has integer coefficients.
Odd states need not be positive.
The useful exact bounds are

    |I[n,k]|<=2^k H^(2n),
    0<=I[n+1,0]<=H^2 I[n,0]<=H^(2n+2).             (3)

These bounds use the actual nonnegative circle function, not coefficientwise positivity.
A monomial P=a z^j instead has R=0 and nu_n=0 for n>=1 and is handled directly, without assigning the zero polynomial a false degree.

<a id="triangular-integration-by-parts-reduction"></a>
## 3. Full triangular reduction and state update

For integers n,j>=0 differentiate x^j sqrt(4-x^2)R(x)^(n+1) on(-2,2).
Its endpoint values tend to zero, and its derivative is a polynomial divided by sqrt(4-x^2), hence integrable.
Integrating first on compact interior intervals and taking endpoint limits gives

    0=integral R(x)^n A_(n,j)(x)dmu_A(x),
    A_(n,j)=sum_(l=0)^d r_l [
       4(j+(n+1)l)x^(j+l-1)
       -(j+1+(n+1)l)x^(j+l+1)].                    (4)

The term at j=l=0 in the first sum is zero and is OMITTED; no moment of exponent-1 is introduced.
No division by R is used, so interior or endpoint zeros and repeated roots of R cause no singularity or missing hypothesis.

For k>d set j=k-d-1>=0 and

    D_(n,j)=[j+1+(n+1)d]r_d!=0.

The coefficient of x^k in(4) is-D_(n,j), and all other exponents are below k.
Therefore

    I[n,k]=D_(n,j)^-1 [
       sum_(l=0)^d 4(j+(n+1)l)r_l I[n,j+l-1]
       -sum_(l=0)^(d-1)(j+1+(n+1)l)r_l I[n,j+l+1]
                              ],                 (5)

again omitting the zero negative-exponent term.
The denominator is signed and nonzero for every n>=0.
The identity determines every higher I[n,k] successively from I[n,0],...,I[n,d].
In particular compute k=d+1,...,2d, corresponding to j=0,...,d-1.
Then

    I[n+1,j]=sum_(l=0)^d r_l I[n,j+l], 0<=j<=d.    (6)

Equations(5)--(6) are the complete rational linear d+1-state recurrence.
Their starting vector is(2).
Correctness by induction follows from the exact integral identity: triangular reduction recovers actual moments at n, then(6) gives actual moments at n+1.
Since all those moments are integers, EACH signed division in(5) is exact.
An integer implementation can and must assert zero remainder; no rational-state denominator need be retained.
This integrality is a consequence of the actual arcsine functional, not of an assumed monic R or positive numerator.

<a id="fast-positive-moment-arithmetic-cost"></a>
## 4. Full arithmetic, bit and retention costs before implementation

Autocorrelation and the integer Chebyshev basis construct(1) in O(d^2) integer arithmetic operations.
At each n, d triangular reductions use O(d) terms each, and d+1 state updates use d+1 terms each.
Thus all moments through N cost O(Nd^2) integer arithmetic operations with O(d) live state integers.
Constructing a dense symbolic transition matrix is unnecessary.
This improves the direct growing-Laurent convolution's O(N^2d^2) arithmetic count, without making bit cost independent of N.

The recurrence temporarily needs k<=2d.
Equation(3) bounds those states by2^(2d)H^(2n).
The elementary ||C_l||_1<=2^(l+1) bound and sum_(l=-d)^d|b_l|<=H^2 give

    W<=2^(d+2)H^2.

For0<=j<d, the absolute numerator of(5) is bounded by

    5(n+2)d W 2^(2d)H^(2n).                        (7)

Its denominator has modulus at most(n+2)d W.
Intermediate state-update sums have the same scale without the n d factor.
Thus all signed states, products, numerator partial sums and divisors through N have bit size

    B_N=O((N+1)log(2H)+d+log(N+2)+log(d+1)).        (8)

Integer exact division is still a paid operation.
With elementary quadratic multiplication/division, a conservative bit-operation upper bound is O(Nd^2 B_N^2); the arithmetic-operation statement does not claim constant-time big integers.
Live mathematical state storage is O(d B_N) bits.
Source polynomial coefficients and output metadata have their own smaller fixed input costs.

Retaining ALL nu_n as unreduced numerator I[n,0] plus the known H requires up to O(N^2 log(2H)) output bits; writing every denominator separately does not avoid that growth.
Retaining every full d+1 state through N has an additional d factor and degree overhead.
A larger run can instead retain named checkpoints and its final complete state, making its narrower retention explicit, while the reproducible program checks all intermediate exact divisions and scalar bounds.
No permanent mathematical hash substitutes for necessary data.

## 5. Bounded execution plan and limits

Before any code run, allocate one responsible new J with exactly the four original J84 coefficient lists and the main proof above.
The first declared stage is n=0,...,64, comparing the new integer recurrence against an INDEPENDENT direct Laurent convolution of Z=H^2-P(z)P(z^-1).
Compare not only CT Z^n but all stored I[n,k],0<=k<=d, by direct constant terms of(z+z^-1)^k Z^n.
Retain exact input coefficients, H, R, all finite states and positive-moment numerators; preserve actual check counts and any failed assertion.
Use standard-library integers only and a30second process cap for this complete four-input comparison.

The responsible [J86](../computations/programs/Yin_J_G0086/readme.md) was allocated with this complete scope before implementation or execution.
At initial implementation its recurrence and independent Laurent reference were author-inspected and unrun; the subsequent exact execution facts are recorded below.
The runtime was read as CPython3.12.14.

Only after that stage passes, execute ONE further recurrence-only Lehmer run through n=1024 with its own30second process cap.
Retain exact scalar checkpoints at n=0,64,128,256,512,1024, the final full d+1-state vector, arithmetic/check counts and runtime facts.
Check all signed exact divisions and the scalar positivity/monotonicity/size assertions at every n, but do not claim independent direct-convolution verification beyond64.
No different input, second larger N, parameter search or retry with a weakened check is included.

No tail modulus b, local radius, derivative S or certified logarithmic enclosure is computed by these stages.
Therefore an exact fast positive moment is NOT a positive finite lower Mahler certificate.
D24's full analytic tail and all original coefficient/degree costs remain required.
The recurrence works for arbitrary nonzero integer inputs at its stated domain, but the executed evidence will cover only the four declared cases and single additional Lehmer depth.
Separate whole mathematical/program review is pending.

<a id="fast-positive-moment-execution-outcome"></a>
## 6. Exact bounded author execution and remaining review

The two predeclared [J86](../computations/programs/Yin_J_G0086/readme.md) stages were actually executed once each, in order, on2026-10-11 before the 2026-10-11T14:42 closeout check, with the current saved programs and exact standard-library integers.
The complete comparison payload (`mathematics/computations/outputs/Yin_J_G0086/comparison.json`) retains all state vectors n0--64 and all four original input/H/R lists.
The independent direct original-Laurent algorithm shares no trace-polynomial or integration-by-parts reduction code.
All1,235 full-state equalities passed, along with960 exact signed divisions and the scalar/Fourier/state bounds.
In particular both signs of r_d occur among the controls.

The first three exact R polynomials in ascending coefficients are[2,1],[8,-2,-1],[16,6,-1].
For the original Lehmer input H=9 and

    R=[72,-24,14,70,9,-64,-23,20,9,-2,-1].

The single additional Lehmer1024 payload (`mathematics/computations/outputs/Yin_J_G0086/lehmer1024.json`) passed all10,240 signed divisions,10,240 extended-state size bounds,11,275 stored-state size bounds,1,025 scalar range bounds and1,024 normalized monotonicity bounds.
Its n64 overlap matches the independently checked data.
It retains scalar checkpoints0,64,128,256,512,1024 and the final full11-state vector, with original positive moment denominator9^(2n).
No independent direct-convolution agreement beyond64 is asserted.
The recorded maximum numerator/divisor lengths were6,513/14bits.
Both worker/supervisor elapsed times were below one second on these runs, with actual values and separate30second hard caps in J86.
No further input/depth or failed/retried mathematical run occurred.

The mathematical benefit is the proved reduction of the arithmetic recurrence from quadratic to linear dependence on N at fixed d, with full bit/output costs in(7)--(8), and a bounded actual implementation discriminator.
The exact moments do not establish tail constants or a positive Mahler lower certificate.
No old J84 output, root approximation, floating arithmetic or huge scan supplies hidden acceptance.
Root's core derivation is disclosed; these checks are author-side and whole separate mathematical/program scrutiny remains pending.

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0086](../computations/programs/Yin_J_G0086/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
