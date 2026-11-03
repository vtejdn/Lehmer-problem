---
author: Yin
---

# Finite-energy certificates for tunable Salem transition products

Date: 2026-10-08.
Direct G0001 derivation by the coordinating Codex AI for Yin.
The assigned entropy_status AI and coordinator independently identified the dyadic improvement below during the same exploration; its role on that part is a collaborator, not independent reviewer.
This record studies the finite-energy search of L G0130.
It gives explicit feasible witnesses, improves that search's energy budget, and bounds the actual L G0129 Salem transition product through finite energy certificates with a computable window cutoff.
It does not compute an optimum, supply a new transition lower bound, or assert a degree-uniform Mahler gap.
Completed independent review is recorded at the end.

## Domain and the earlier finite problem

Let P be the monic irreducible minimal polynomial of an algebraic unit alpha, with positive logarithmic Mahler measure and q>0 central conjugates.
Count both members of each complex pair.
Put d=deg P, h=d-q>0 and

    rho=max(max_stable |beta|, max_expanding |beta|^(-1)),
    lambda=-log rho>0,  b_0=1/16.

There are both stable and expanding roots.
Use the explicit height constant C_P of [L G0123](Yin_L_G0123_v1.md#polynomial-height-central-approximation): for every 0<epsilon<=1 there is nonzero theta in Z[alpha] with

    max_central |sigma(theta)|<epsilon,
    H=max_sigma |sigma(theta)|<=C_P epsilon^(-q/h).       (1)

In particular C_P>=1 and H>=1.
For R>=0 let I_R={-R,...,R+d}, M_R=2R+d+1, and use exactly [L G0130's finite rational energy problem](Yin_L_G0130_v1.md#finite-rational-energy-coercivity):

    K_R={x in [-1/2,1/2]^(I_R):
         (P(S)x)_j is an integer for -R<=j<=R,
         (P(S)x)_0 !=0},
    E_R=min_(x in K_R) sum_(j in I_R) x_j^2.              (2)

There E_R is nondecreasing and tends to infinity, with infinity allowed for an empty feasible set.
The construction here shows that in the present positive-Mahler unit domain no K_R is empty, and their divergence is no faster than an explicit logarithmic bound.
The cyclotomic control P=t+1 in L G0130 has different hypotheses and can have linear growth; no conflict is implied.

<a id="logarithmic-finite-energy-witnesses"></a>
## Explicit logarithmic upper bound

For every integer R>=0,

    E_R <= a_P log M_R + b_P,                            (3)
    a_P=q/(4h lambda),
    b_P=25/32
        +[log(16d C_P)+(q/h)log(16q)]/(2lambda)
        +3rho^2/[64(1-rho^2)].

All constants are determined by the fixed polynomial.
They are not bounded uniformly as the degree, root geometry or Mahler measure varies.
For a Salem polynomial, h=2 and lambda=m=log M(P), so a_P=(d-2)/(8m); this dependence must not be suppressed.

Fix R, write M=M_R and choose (1) with

    epsilon=1/(16q sqrt M),
    J=ceil(log(16dH)/lambda).                            (4)

For all integers j write u_j,v_j,w_j for the stable, expanding and central weighted traces of theta alpha^j.
Their sum is an integer.
Let e_j be the nearest-integer error of 2(u_j+w_j).
As in [L G0125](Yin_L_G0125_v1.md#transition-defect-compactness),

    |e_j|<1/2,  z=P(S)e is integer-valued,
    e_j=-2v_j for j<-J,
    e_j=2u_j+2w_j for j>J.                               (5)

Here are the guards needed without any product lower bound.
A rounding tie would force the algebraic integer u_j+w_j to be an odd integer divided by four, which is impossible.
For |j|>J the relevant hyperbolic trace is bounded by b_0 rho^(|j|-J), and |w_j|<=q epsilon<=b_0.
Hence the expressions in (5) lie strictly in the rounding interval.
Each homogeneous tail satisfies P(S), so z has support in [-J-d,J].

Moreover z is nonzero.
Otherwise e is a bounded bilateral homogeneous solution and is a sum of central modes only: the distinct-root Vandermonde representation excludes all hyperbolic modes from a bounded bilateral solution.
Its negative tail in (5) tends to zero, so another Vandermonde argument makes every central coefficient zero.
Thus e=0.
The negative identity in (5) then makes the expanding trace eventually zero; the distinct reciprocal expanding roots force all its coefficients sigma(theta) to vanish.
This contradicts theta!=0 and injectivity of each field embedding.

Choose k with z_k!=0.
The restriction of (e_(j+k)) to I_R lies in K_R.
For its energy, the core has at most 2J+1 coordinates, each with square at most 1/4.
The entire negative tail contributes at most 4b_0^2 rho^2/(1-rho^2).
On the positive part of this translated window use (2u+2w)^2<=8u^2+8w^2.
The hyperbolic part contributes at most 8b_0^2 rho^2/(1-rho^2), and at most M central terms contribute at most 8M q^2 epsilon^2=1/32.
Consequently

    sum_(j in I_R) e_(j+k)^2
       <=(2J+1)/4+12b_0^2 rho^2/(1-rho^2)+1/32.          (6)

This bound holds for any translating k; no assumed location of the chosen defect is needed.
By (1) and (4),

    J <= 1+[log(16d C_P)+(q/h)log(16q)
                        +(q/(2h))log M]/lambda.         (7)

Substitution into (6) proves (3), with 3/4+1/32=25/32 and 12b_0^2=3/64.
Feasibility of every K_R also follows.
Together with L G0130 this gives E_R tending to infinity but bounded above by a_P log(2R+d+1)+b_P for every R.

This construction proves existence using the finite coefficient-box selection of L G0123.
It is not an executed coefficient search or an evaluation of E_R.
Its real algebraic witness need not be the rational minimizing point used in the earlier exact algorithm.

<a id="dyadic-collapse-energy-budget"></a>
## A logarithmic budget suffices in the effective collapse search

Keep the explicit tail-energy constant E_P of L G0125 and L G0130.
For rational 0<c<1, let k>=1 be the least integer with 2^k c>=1.
It is determined by finite exact rational comparisons.
Then

    -2log c/pi^2 <= (2log2/pi^2)k < k/6.                 (8)

For the strict bound, log2<3/4 and pi>3 imply 12log2<9<pi^2.
Obtain a rational upper bound E_bar>=E_P from the same algebraic root-isolation procedure as L G0130, and choose an integer

    B>=1,  B>E_bar+k/6.                                  (9)

Run precisely the finite rational search for the first R with E_R>4B and put

    delta=min(1/(16q),1/(4q M_R)).                        (10)

This still terminates by E_R tending to infinity.
It has the same proved consequence as the earlier search: every nonzero integral theta with all central conjugates at most delta, and every admissible transition window J, satisfy C(theta,J)<c.

For completeness, if C(theta,J)>=c, the earlier rounding construction provides e,h with nonzero integer P(S)e,

    ||h||_2^2<=E_P-2log c/pi^2<B,
    ||e-h||_infinity<=2q epsilon,
    |e_j|<1/2.                                          (11)

Translate a nonzero defect to zero.
If epsilon<=delta, its energy on I_R is less than

    [sqrt B+2q epsilon sqrt M_R]^2
       <=[sqrt B+1/(2sqrt M_R)]^2<4B.                   (12)

The last inequality uses B>=1.
This contradicts E_R>4B.
All other guards are unchanged, in particular q epsilon<=1/16 and the actual admissible-window conditions of L G0125.
There is no new height restriction.
Choosing the least integer B allowed by (9) replaces the earlier convenient sufficient budget E_P+2/c by O_P(log(1/c)).
The older larger budget remains valid in its fixed record.

## What the witness bound does and does not imply about cost

For any energy parameter B>=1, every successful certificate E_R>4B necessarily satisfies, by (3),

    M_R > exp((4B-b_P)/a_P).                             (13)

In particular a bound E_R>=c_P R for all large R with c_P>0 is impossible in this domain.
The finite search has an exponential lower bound on its necessary window size as a function of B for fixed P, when the exponent in (13) is positive.
This says nothing about the complexity of alternative collapse proofs or algorithms.

For the particular output (10), (13) also implies

    delta < exp((b_P-4B)/a_P)/(4q).                       (14)

This bounds the value returned by this sufficient-certificate scheme, not the largest mathematically valid transition modulus.
The dyadic choice (9) is important: inserting the old 2/c budget into (13) and calling the resulting exponential-in-1/c scale intrinsic would be incorrect.
Equations (8)--(12) remove that unnecessary energy loss.

There is still no explicit lower growth estimate for E_R in this positive-Mahler unit domain, no upper bound on the terminal R, and no uniform-in-degree threshold.
No simultaneous compatibility or incompatibility of all L G0129 guards with its actual C_delta>=16m target follows just from (3) or (13).
The following sections instead use that precise enlarged window to derive an actual-product upper test.
The needed arithmetic product lower bound and full G0001 objective remain open.

<a id="tunable-salem-finite-energy-envelope"></a>
## A finite-energy upper certificate for the actual tunable Salem product

Use a hypothetical Salem input in the exact domain of L G0129: P is its monic irreducible polynomial, degree d, q=d-2>0, and 0<m=log(alpha)<=1/32.
Put rho=exp(-m).
For any integer N>=1, take a nonzero integral multiplier theta with all central conjugates bounded by

    epsilon_N=kappa/sqrt(N),  kappa=sqrt(m)/(16q).

Let H>=1 bound all conjugate moduli.
There is no polynomial-height assumption in this section.
Keep the actual L G0129 choices

    delta_tail=sqrt(m(1-rho^2))/16,
    J=ceil(log(dH/delta_tail)/m),
    C_delta=product_(j=-J)^(-1)|cos(2pi v_j)|
              product_(j=0)^J|cos(2pi(u_j+w_j))|.          (A1)

The subscript on delta_tail distinguishes it from a central-smallness modulus.
This J is the enlarged tunable window; the shorter fixed-tail window cannot be substituted.
Every factor is nonzero by the algebraic integer rounding argument below, so 0<C_delta<=1.

For R>=0 use exactly the finite rational problem E_R of L G0130, on I_R={-R,...,R+d}, with M_R=2R+d+1.
Any nonnegative finite certified lower bound L_R<=E_R may replace E_R throughout the bounds below.
Define

    T_m=m rho^2/(32d^2),
    a_(R,N)=sqrt(m M_R/(64N)),
    e_R=sqrt(E_R),  x_+=max(x,0).

The actual transition product satisfies

    C_delta <= min{1, exp[-(pi^2/2)
                     (((e_R-a_(R,N))_+)^2-T_m)]}.       (A2)

The minimum with one is necessary: when the energy lower bound is too weak, the exponential displayed here can exceed one.
Equivalently the right side is exp[-(pi^2/2) (((e_R-a_(R,N))_+)^2-T_m)_+].
With a certified lower bound L_R, replace e_R by sqrt(L_R); monotonicity makes the resulting upper bound weaker but valid.
An infinite E_R would already contradict the feasible restriction constructed in the proof; in this domain every E_R is finite.

Here is a complete derivation independent of an entropy inequality.
There is exactly one stable and one expanding conjugate.
The definition of J gives H rho^J<=delta_tail/d, whence for every r>=1

    |u_(J+r)|, |v_(-J-r)| <= (delta_tail/d) rho^r.        (A3)

Also |w_j|<=q epsilon_N=sqrt(m)/(16sqrt(N))<=1/16.
Let e_j be the nearest-integer error of 2(u_j+w_j).
A rounding tie would make the algebraic integer u_j+w_j an odd integer divided by four; therefore |e_j|<1/2.
Because P(S)(u+w)=0, P(S)e is an integer sequence.
The integer trace identity and (A3) identify

    e_j=-2v_j for j<-J,
    e_j=2u_j+2w_j for j>J.                              (A4)

Indeed delta_tail<=1/16, so both doubled tail expressions have modulus at most 1/4 and remain strictly within the rounding interval.
This supplies all rounding guards for every N>=1; no Fourier-noise guard or lacunary-frequency condition is being assumed.

Set h_j=e_j-2w_j 1_(j>J).
On the core, the product in (A1) is exactly product_(j=-J)^J cos(pi e_j).
Since -log cos(pi x)>=pi^2 x^2/2 for |x|<1/2,

    sum_(j=-J)^J e_j^2 <= -2log(C_delta)/pi^2.

The two tails of h are -2v_j and 2u_j.
Summing their squared geometric bounds in (A3) gives

    sum_(|j|>J) h_j^2
       <= 8 delta_tail^2 rho^2/[d^2(1-rho^2)]
        = T_m.

Consequently

    ||h||_2^2 <= -2log(C_delta)/pi^2+T_m,
    ||e-h||_infinity <= 2q epsilon_N
                      = sqrt(m)/(8sqrt(N)).             (A5)

The integer defect P(S)e has support in [-J-d,J] and is nonzero, by the same finite-tail and homogeneous-mode argument as L G0125.
For clarity, if it were zero, boundedness on both half-lines would eliminate every hyperbolic mode from the distinct-root recurrence.
The remaining central modes tend to zero on the negative tail by (A4); the Vandermonde argument makes all their coefficients vanish.
Then e=0 and v_j=0 for j<-J.
Here v_j is the single expanding embedding coefficient times alpha^j, so its coefficient would vanish, contradicting theta!=0 and injectivity of that embedding.

Translate e and h together to put a nonzero defect at zero.
The restriction of the translated e to I_R is feasible for L G0130's problem, irrespective of the original location of the defect.
The global norm and error bounds (A5) imply

    sqrt(E_R) <= ||e|_(I_R)||_2
       <= sqrt(-2log(C_delta)/pi^2+T_m)+a_(R,N).         (A6)

Thus ((e_R-a_(R,N))_+)^2 <=-2log(C_delta)/pi^2+T_m.
Rearrangement and C_delta<=1 prove (A2).
This uses a global l2 comparison for h, not the false claim that the persistent-central-tail sequence e itself is in l2.

## The resulting finite exclusion of the linear transition target

Let

    B_m=-2log(16m)/pi^2+T_m.                            (A7)

It is positive because 0<16m<=1/2.
For any R such that E_R>B_m, the strictly finite condition

    N > m M_R/[64(sqrt(E_R)-sqrt(B_m))^2]               (A8)

forces C_delta<16m.
More generally, the same claim follows with any certified finite L_R>B_m substituted for E_R.
If instead one assumes C_delta>=16m, (A5)--(A6) give the necessary condition

    E_R <= (sqrt(B_m)+sqrt(m M_R/(64N)))^2,              (A9)

which directly contradicts (A8).
Equality at the threshold in (A8) is not asserted to give a strict exclusion.

Every m,d,N cost is present: T_m retains the scalar Salem tails and the 1/d factor in J, while M_R=2R+d+1 is the complete recurrence window.
For a fixed input, L G0130 ensures an R with E_R>B_m exists.
The upper estimate (A2) and exclusion (A8) hold separately for each input without transferring a fixed-P asymptotic assertion across a varying near-one family.
They supply no degree-uniform bound on R.

This is a direct finite-energy restriction on the actual product; it does not require any of the additional L G0129 entropy/noise/time guards (17).
It can therefore exclude that product target even at windows before those guards hold.
When applying it to L G0129's contradiction scheme, both that scheme's own guards and its actual enlarged transition product must still be used.

## Fully rational sufficient implementation of the threshold

No numerical optimization is executed here.
The following finite procedure shows that the new condition has an exact certificate version.
Choose rational 0<c<=16m and rational mu>=m; root isolation and certified logarithms permit such choices for a fixed input.
One may always use mu=1/32 in the stated conditional domain.
Let k>=1 be the least integer with 2^k c>=1 and set

    B_bar=k/6+mu/(32d^2).                               (A10)

The elementary dyadic estimate -2log(c)/pi^2<k/6 and rho^2<1 give B_m<B_bar.
Search the exact finite rational problems until

    E_R>4 B_bar.                                      (A11)

L G0130 proves termination.
It suffices to certify a rational lower bound L_R>4B_bar instead of computing the exact optimum.
If N>=1 and

    N>=mu M_R/(64 B_bar),                             (A12)

then a_(R,N)<=sqrt(B_bar), and C_delta>=16m would imply E_R<(sqrt(B_bar)+sqrt(B_bar))^2=4B_bar, contradicting (A11).
Thus (A10)--(A12), apart from the initial certified parameter bounds, involve only rational inequalities and integer enumeration.
The strict energy comparison removes any issue at equality in (A12).

If rational 8m<c<16m is chosen and mu=1/32 is used, the energy budget is logarithmic in 1/m, with the d term retained.
The earlier weak-admissibility tail constant proportional to 1/m is not needed for the actual tunable Salem window.
The new N threshold is linear in M_R, because the l2 error on M_R coordinates is controlled directly.
Neither improvement is a bound on the size of the first successful R or an assertion that the exact finite rational optimization is practical.

No estimate C_delta>=16m is established, and no such Salem input is presumed to exist.
These upper certificates alone do not exclude every hypothetical input or prove a uniform Mahler gap.


<a id="finite-energy-candidate-window-cutoff"></a>
## A finite exhaustive window range for this upper-certificate family

For the same fixed Salem P and fixed integer N>=1, the family (A2) over all integers R>=0 has a computable finite candidate range for every nontrivial upper bound.
Choose a real M_cap>=max(3,d+1) with

    a_P log M_cap+b_P <= m M_cap/(64N).                  (B1)

This can be obtained by doubling integers: use certified rational upper bounds a_bar>=a_P, b_bar>=b_P, a positive rational lower bound m_low<=m, and stop at a strict certified comparison

    a_bar log M_cap+b_bar < m_low M_cap/(64N).           (B2)

The logarithm divided by M tends to zero, so the doubling procedure terminates.
Root isolation and certified logarithms provide the constant bounds at any fixed input.
This cutoff retains its actual dependence on m and P; it does not avoid an unknown small-m cost.

Since a_P,b_P>0 and log M>1 for M>=3,

    d/dM [(a_P log M+b_P)/M]
        =[a_P-a_P log M-b_P]/M^2<0.                    (B3)

Thus for every R with M_R>=M_cap, (3) and (B1)--(B3) give

    E_R <= a_P log M_R+b_P <= m M_R/(64N)=a_(R,N)^2.

For every such R the right side of (A2) is exactly one.
The same is true if E_R is replaced by any smaller certified lower bound.
It follows that every nontrivial certificate from (A2), including every certificate that makes its upper bound strictly below 16m, must occur among the finitely many indices

    R>=0 with 2R+d+1<M_cap.                              (B4)

This is an exhaustive finite range only for the stated finite-energy upper-envelope test.
One can compute its finitely many exact rational E_R values by L G0130 and approximate the corresponding analytic bounds to arbitrary accuracy.
Strict exclusions admit certified comparison; no universally terminating exact decision procedure for every possible transcendental equality at a boundary is asserted.
The fully rational sufficient conditions (A10)--(A12) avoid that comparison issue whenever they succeed.

Neither (B4) nor a failure of every test there supplies an actual product lower bound.
They do not exhaust all Fourier arguments, all choices of multiplier, or all possible mathematical upper certificates.
No optimization, coefficient enumeration or search over this finite range has been run in this derivation.

## Contributions and review

The coordinator derived the feasible witnesses, all constants in (3)--(7), the cost implication (13)--(14), and assembled the full proof, the actual-product inversion in (A2), and finite cutoff (B1)--(B4).
The entropy_status AI derived the specialized tunable-tail energy estimate, finite target threshold and rational implementation (A1)--(A12), and checked their complete proof as a contributor.
It independently noticed the dyadic budget refinement during development and supplied the sharper k/6 constant; the coordinator had also identified the dyadic improvement.
These are collaborator checks.
The coordinator also read and checked the complete specialized contribution, every constant and both rational parameter guards, and explicitly retained the precise L G0129 window.

On 2026-10-08, the separately assigned execution_and_deliverables AI for Yin independently read and checked the complete final proof: (1)--(14), (A1)--(A12), and (B1)--(B4).
It had received an outline and progress reports, so the review was not blind, but it contributed no proof mechanism or numerical evidence.
It directly read the used L G0123 coefficient-box construction, L G0125 rounding/nonzero-defect and tail interfaces, L G0130 finite rational optimization/coercivity, L G0115 rigidity, and the exact L G0129 enlarged Salem window.

The review verified the algebraic-integer no-tie condition, nonzero defect without any product lower bound, every translated-window tail and core coefficient in a_P,b_P, dyadic k/6 budget, sufficient-scheme versus intrinsic-modulus distinction, exact scalar Salem tail energy, actual-product positive-part/minimum inversion, strict target exclusion, certified lower-bound substitution, rational sufficient implementation, and the positivity, monotonicity, certified doubling and exhaustive scope of the finite candidate cutoff.
It identified one parameter-cost wording issue: O(log(1/m)) must use c comparable to m and bounded mu.
The final text explicitly chooses 8m<c<16m and mu=1/32, and the reviewer checked that correction in the merged proof.
No substantive defect or missing domain hypothesis remained after the complete reread.

This is full independent written-proof review, not an executed energy optimization, coefficient search, source-original audit or formal proof.
The coordinator accepted this bounded refinement for fixed-ledger preservation under the current G0001 instruction on 2026-10-08.
The Task and its full unrestricted objective remain unresolved.
