---
author: Yin
---

# Complete original doubling overlaps and radius-free sufficient mean certificates

The current complete proof is retained from [L293](../ledger/Yin_L_G0293_v1.md).
The original 2026-10-10T05:25 reverse-inference repair and 2026-10-10T05:27 domain repair remain in that fixed original record and [R776](../audits/reviews/Yin_R_G0776_v1.md#doubling-overlap-complete-independent-review).
This registration uses the corrected complete argument and makes no new research claim.

<a id="statement"></a>
## Complete statement

Use the ORIGINAL independent digits eta in{-1,0,1} with probabilities1/4,1/2,1/4.
For ANY nonzero algebraic integer alpha with actual order O=Z[alpha], define S_n=sum_(j<n)eta_j alpha^j, mu_n(x)=Pr(S_n=x), p_n=mu_n(0),p_0=1, h=lim_n -log p_n/n,R=exp h and a_n=R^n p_n.
The full original zero-to-zero process supplies first-return probabilities f_n, U(z)=sum p_n z^n and F(z)=sum f_n z^n, with U=1/(1-F) below R.
One has1<=R<=2 and0<a_n<=1.
For positive n only, put D_n=p_(2n)/p_n^2>=1; it contains no unknown R and has exact finite identities

    p_(2n)=sum_(x in O)mu_n(x)mu_n(alpha^n x),
    D_n=sum_x[mu_n(x)/p_n][mu_n(alpha^n x)/p_n]
       =sum_x M_n(x)M_n(alpha^n x)/M_n(0)^2
       =M_(2n)(0)/M_n(0)^2.

Here B_n(y) is the complete count of fair binary words with endpoint y and M_n(x)=sum_y B_n(y)B_n(y-x), so mu_n=M_n/4^n.
All multiplicities and at most3^n midpoint states are retained; positive terms lie in the actual core without a full-strip hypothesis.
No feasible uniform enumeration bound is asserted.

For n>=1,J>=1 set H_(n,J)=sum_(j=0)^(J-1)2^(-j-1)log D_(2^j n).
Then

    log a_n=-H_(n,J)+2^-J log a_(2^J n),
    H_n=sum_(j>=0)2^(-j-1)log D_(2^j n)=-log a_n<infinity.

For ACTUAL ALGEBRAIC UNITS only, let q be the full neutral real Minkowski dimension and C_non>=1 the actual full nonneutral-place constant of C432.
With E_N=C_non[2+sqrt(2pi N)]^q and epsilon_(n,J)=2^-J log E_(2^J n), one has

    exp[-H_(n,J)-epsilon_(n,J)]<=a_n<=exp[-H_(n,J)],
    0<=H_n-H_(n,J)<=epsilon_(n,J).

The largest original return observation is2^J n, and all degree/q/C_non costs remain.
The displayed remainder is fixed-input convergent and is not asserted for nonunits without another premise.

If there are N0>=1 and a FINITE C with D_n<=C for EVERY n>=N0, then F(R)=1 and the complete critical first-return mean mu_R=sum_j jR^j f_j<=C<infinity.
Recurrence is a conclusion.
For units the accepted exact criteria then give full variational attainment and bounded continuous critical dual convolution with norm mu_R.
A complete all-late H_n<=log C bound is also sufficient.
A finite overlap list is neither premise.
Only IF F(R)=1 does the extended consequence limsup_n D_n>=mu_R follow.
Critical transience, and separately infinite recurrent mean, each forces unbounded D_n; unbounded D_n alone classifies neither recurrence, mean nor attainment.
If D_n tends to1, then R=2 and every returned word is all zero, excluding this limit at any actual input with a nontrivial original height-one relation.

For phi=(1+sqrt5)/2, its complete original five-state law has

    F_phi(z)=z/2+(z^3/32)/(1-z^2/8),
    U_phi(z)=(32-4z^2)/(32-16z-4z^2+z^3),
    p_1=1/2,p_2=1/4,p_3=5/32,p_4=3/32,
    D_1=1,D_2=3/2.

For every r=2^k,k>=0, beta_r=phi^(1/r) has ACTUAL irreducible minimal t^(2r)-t^r-1 of degree2r, with complete TOTAL m=log phi fixed positive and no neutral root.
For every l>=1,

    p_(rl)(beta_r)=p_l(phi)^r,
    D_(rl)(beta_r)=D_l(phi)^r,
    h(beta_r)=h(phi),R(beta_r)=R(phi).

There is no1/r entropy factor.
For every1<=n<=r, D_n(beta_r)=1, while D_(2r)(beta_r)=(3/2)^r.
Its actual core is the finite product D_core(phi)^r, with finite mean mu_(beta_r)=mu_phi^r,1<mu_phi<infinity, stationary zero mass mu_phi^-r and the same full convolution norm.
Thus each fixed member has finite mean while no common finite all-late overlap constant exists across the family, even with input-dependent onsets.
This family is nonreciprocal, fixed positive total measure and not a near-one or Salem counterexample.
The original unsupported reverse implication and undefined D_0 wording were corrected in the original review round at their real dates; neither is adopted here.
No new program, external theorem, pointwise renewal limit, actual quartic mean classification or Mahler gap is asserted.

## Complete argument

<a id="argument"></a>

<a id="doubling-overlap-reuse"></a>
### 1. Changed finite object and exact reused premises

The exact adopted scope of [C546](Yin_C_G0546_v1.md#statement) was read.
L289 separates the complete periodic diagonal t_n from its zero-avoiding part: only their difference c_n counts rooted cycles visiting zero.
Its period-three control excludes treating the full periodic diagonal as a rooted return.
The new object here starts directly from a zero-rooted word of length2n and marks its midpoint, so the full return condition is imposed before an arithmetic sum is formed.

The local screen also read [C479 complete first-return/attainment interface](Yin_C_G0479_v1.md#critical-excursion-attainment-condition), [L240's separate bounded-convolution criterion](../ledger/Yin_L_G0240_v1.md#critical-convolution-bounded-density-test), [C526](Yin_C_G0526_v1.md#actual-critical-return-fixed-scope), the actual golden full series in [C372](Yin_C_G0372_v1.md#finite-prime-core-golden-ratio-control), and [C493 complete radical core and critical product formulas](Yin_C_G0493_v1.md#radical-actual-core-product).
L255's full original operator expense supplies a paid finite remainder estimate below.
The earlier L5 radical degree proof and digit product are reused, not claimed as new.
These exact local inputs suffice.
No new external theorem, renewal limit theorem, source acquisition or novelty claim is needed or made.
In particular no pointwise renewal asymptotic is silently assumed.

Let alpha be a nonzero algebraic integer, O=Z[alpha], and let the independent ORIGINAL digits have probabilities mu(0)=1/2, mu(+/-1)=1/4.
Write

    S_n=sum_(j=0)^(n-1) eta_j alpha^j,
    mu_n(x)=Pr(S_n=x), p_n=mu_n(0), p_0=1,
    h=lim -log p_n/n, R=exp(h), a_n=R^n p_n.          (1)

Concatenation gives p_(n+m)>=p_n p_m.
Consequently0<a_n<=1 and1<=R<=2, with the actual exponent and no degree normalization.
This is the existing L201 original-word convention.
The actual zero-to-zero core and the complete first-return series F(z)=sum f_n z^n are used, with U(z)=sum p_n z^n=1/(1-F(z)) below R.
Nonunits are permitted in the finite word and renewal parts; unit-only operator and stationary conclusions will be marked separately.

Define the finite doubling overlap

    D_n=p_(2n)/p_n^2 >=1, n>=1.                       (2)

There is no unknown R in this observable.
Its full unweighted state sum and every probability will be retained.
This D_n denotes an overlap here, not the ideal index denoted by D_n in L289.

All present new deductions are by structural_research for Yin.
The coordinator supplied the broad question only.
The simultaneous D157 endpoint-profile argument is not read or used.
No program or J is needed for the exact examples below.

<a id="actual-original-midpoint-overlap"></a>
### 2. The complete actual midpoint and integer-fiber identity

Split a chronological returned word of length2n into two consecutive length-n words.
The first endpoint x has law mu_n, since reversing iid digits does not change their law.
The last endpoint equals alpha^n x plus an independent displacement.
Digit-sign symmetry gives

    p_(2n)=sum_(x in O) mu_n(x) mu_n(alpha^n x),
    D_n=sum_(x in O) [mu_n(x)/p_n][mu_n(alpha^n x)/p_n]. (3)

Only finitely many terms occur, at most3^n.
Every positive term automatically has x in the ACTUAL zero-to-zero core, with a path of length n in both directions.
No real-strip completeness premise, fractional module, stationary approximation or finite quotient has entered.
Paths visiting zero before or after the midpoint remain included exactly once.
The x=0 term is one after normalization and proves D_n>=1 directly.
This is not the periodic fixed-point sum t_n of L289 and does not require deleting unidentified zero-avoiding cycles.

There is a full integer-fiber version.
Let B_n(y) be the number of fair binary words with sum_(j<n) epsilon_j alpha^j=y, epsilon_j in{0,1}.
Define

    M_n(x)=sum_y B_n(y)B_n(y-x).

The difference of two independent fair binary words is exactly the original digit law, so mu_n(x)=M_n(x)/4^n and

    D_n=sum_x M_n(x)M_n(alpha^n x)/M_n(0)^2
        =M_(2n)(0)/M_n(0)^2.                         (4)

All multiplicities in the integer relation fibers survive.
The finite support and integer arithmetic make(4) exactly computable in principle; no feasible bound independent of n,d or input is claimed.
A full list of binary endpoints can itself have2^n words, and no such enlarged computation is performed here.
Replacing the fibers by parity ranks, uniformly weighted distinct endpoints or independently chosen congruence classes would change(4).

The individual normalized factors in(3) are at most one by the original binary-autocorrelation maximum-atom argument.
Their SUM of products, however, need not be near one or bounded across inputs.
This is the new arithmetic overlap whose long-time control is needed below.

<a id="dyadic-critical-normalization"></a>
### 3. Exact dyadic normalization with its complete finite remainder

For n>=1 and integer J>=1 put

    H_(n,J)=sum_(j=0)^(J-1) 2^(-j-1) log D_(2^j n).

Telescoping the definition(2) gives the exact equality

    log a_n=-H_(n,J)+2^(-J) log a_(2^J n).            (5)

Because log a_N/N tends to zero at the actual entropy, the final term tends to zero for each fixed n as J tends to infinity.
Every term in H is nonnegative, so

    H_n:=sum_(j>=0)2^(-j-1)log D_(2^j n)
        =-log a_n < infinity.                       (6)

Thus the finite original doubling overlaps recover the complete critical normalized return without presupposing R.
Equation(6) is an algebraic telescoping identity plus the existing entropy limit, not a new convergence theorem for the renewal sequence.
It keeps arbitrarily late chronological observations: an infinite series is not declared a finite certificate.

For an ACTUAL ALGEBRAIC UNIT, [C432](Yin_C_G0432_v1.md#statement) supplies the full original operator estimate with

    E_N=C_non[2+sqrt(2pi N)]^q,
    E_N^(-1)<=a_N<=1.                                (7)

Here q is the complete real neutral dimension, and C_non is its stated product of nonneutral state-count constants.
Both depend on the actual input and must remain.
Applying(7) to the last term of(5) gives a finite bracket

    exp[-H_(n,J)-epsilon_(n,J)]<=a_n<=exp[-H_(n,J)],
    0<=H_n-H_(n,J)<=epsilon_(n,J),
    epsilon_(n,J)=2^(-J)log E_(2^J n).               (8)

The largest original time read in this expression is2^J n; it includes p_(2^J n) and its complete return mass.
For fixed input and fixed n, epsilon tends to zero as O_P((J+log(n+1))/2^J).
No varying-input convergence is asserted without the displayed q and C_non.
No bare finite p_n lower bound for entropy is being used: the FULL operator expense is the proof of(7).
The definition of H_(n,J) itself applies to nonunits, but this specific remainder estimate is not extended to them without a substitute premise.

<a id="bounded-doubling-critical-mean-test"></a>
### 4. A radius-free sufficient upper certificate for the critical mean

Here is a new useful direction of control.
Suppose for the original law that there are N0>=1 and a FINITE constant C such that

    D_n<=C for EVERY n>=N0.                          (9)

Then C>=1.
For n>=N0 every dyadic successor also meets(9), so(6) gives H_n<=log C and hence

    a_n>=1/C for every n>=N0.                        (10)

It follows that U(Ru)=sum a_n u^n diverges as u increases to1, so F(R)=1.
Thus critical recurrence is a CONCLUSION, not an extra hypothesis for this implication.
With b_j=R^j f_j now a probability distribution, elementary renewal gives

    V(u):=(1-F(Ru))/(1-u)
        =sum_(j>=1)b_j(1+u+...+u^(j-1))
        increases to mu_R=sum j b_j.                (11)

Since V(u)=1/[(1-u)sum a_n u^n], (10) implies V(u)<=C u^(-N0).
Passing to the limit proves

    F(R)=1 and mu_R<=C<infinity.                     (12)

No pointwise renewal limit, Tauberian theorem or interchange of signed endpoint series is used.
The proof only sums nonnegative terms and uses the exact renewal relation already fixed.
For units L201/L232 now imply actual variational attainment, and L240 identifies a bounded continuous dual convolution with exact norm mu_R.
In that application(9) is a sufficient concrete FINITE-TIME arithmetic overlap bound for those conclusions, valid at all late times.
It is not a statement that a finite list of D_n values supplies(9).

One may weaken(9) to H_n<=log C for all sufficiently large n, thereby allowing occasional large individual D_n if their COMPLETE dyadic costs are bounded.
This is still an infinite-time obligation.
A useful explicit consequence without any new assumption is

    limsup_(n->infinity) D_n >= mu_R
                                  if F(R)=1,        (13)

where infinity is allowed.
If the limsup is finite L, apply(9)--(12) with C=L+epsilon eventually, then decrease epsilon to zero.
If the limsup is infinite the assertion is automatic.
In particular infinite critical mean forces unbounded original D_n.
Critical transience also forces unbounded D_n, by the recurrence conclusion of(12).
An unbounded observed family therefore does NOT distinguish null recurrence from transience; finite critical derivatives can occur in the latter case, as L201 already records.
No converse to(12), or exact limit of D_n for an arbitrary infinite core, is asserted here.

If D_n tends to one, the same argument gives F(R)=1 and mu_R<=1.
As every excursion has length at least one, this forces b_1=1 and all other b_j=0.
Since f_1=1/2, necessarily R=2 and every returned word is all zero.
Thus an actual input with a nontrivial original height-one relation cannot have D_n tending to one.
This consequence has no degree normalization and is distinct from a uniform positive entropy bound.

For the actually recurrent quartic, the mean lower bounds in L289 turn(13) into a necessary limsup lower bound greater than3/2; that is a reuse consequence, not this round's decisive example.
The new discriminator below shows why even a completely flat degree-scale initial profile gives no uniform control of the later overlap.

<a id="radical-delayed-overlap-control"></a>
### 5. An actual nontorsion family with delayed exponential overlap

Let phi=(1+sqrt5)/2.
Its complete five-state core and forward first-return series are retained in L5/L157:

    F_phi(z)=z/2+(z^3/32)/(1-z^2/8),
    U_phi(z)=(32-4z^2)/(32-16z-4z^2+z^3).            (14)

These are the FULL original probabilities, not a truncated kernel.
In particular f_1=1/2, f_2=0, f_3=1/32, f_4=0.
Direct renewal therefore gives

    p_1=1/2, p_2=1/4, p_3=5/32, p_4=3/32,
    D_1(phi)=1, D_2(phi)=3/2.                        (15)

For r=2^k, k>=0, let beta_r=phi^(1/r).
L5 proves that P_r(t)=t^(2r)-t^r-1 is its ACTUAL irreducible minimal polynomial of degree d_r=2r.
The norm-minus-one induction doubles the field degree at each square root; no neutral padding or presumed irreducibility is used.
The complete total Mahler measure is M(P_r)=phi: there are r expanding roots of modulus phi^(1/r), and the other r roots have modulus phi^(-1/r).
Thus each input is an actual nontorsion algebraic unit, with NO unit-circle conjugate, fixed positive total measure log phi<log2 and expanding individual moduli tending to one.
This is not a family of decreasing total Mahler measures and not a Salem family.

The exact independent residue-class digit decomposition of L5/L206 gives, for every integer l>=1,

    p_(r l)(beta_r)=p_l(phi)^r,
    D_(r l)(beta_r)=D_l(phi)^r,
    h(beta_r)=h(phi), R(beta_r)=R(phi).               (16)

The unchanged entropy is essential: the r residue classes exactly cancel the factor r in chronological time.
There is NO1/r entropy factor.
For every n with2n<=d_r, minimal degree says that every length2n original return word is all zero, so p_(2n)=2^(-2n) and p_n=2^(-n).
Consequently

    D_n(beta_r)=1 for EVERY1<=n<=r=d_r/2,
    D_(2r)(beta_r)=(3/2)^r=(3/2)^(d_r/2).            (17)

This is a complete all-r symbolic control, using only the four exact base probabilities(15).
No numerical scan, finite-height restriction or J is needed.
It refutes the proposed inference that a perfectly flat initial doubling profile through half the actual degree yields an input-uniform overlap bound.
At time equal to the actual degree the full original overlap is already exponentially large in that degree.
It also rules out any degree-independent bound for all inputs in this fixed-positive-total-measure class.
It does not refute such a bound on a separately specified sufficiently-small-total-measure or actual Salem subclass.

The mean and attainment boundaries are equally concrete.
In(14), F_phi is strictly increasing before its first positive pole sqrt8, starts at zero and has F_phi(2)=3/2>1.
Its unique root F_phi(R_phi)=1 therefore lies below2 and is the positive singularity of the nonnegative U_phi series.
This identifies the actual critical radius; the derivative is finite there.
Nontrivial excursions have positive critical mass, so

    1<mu_phi=R_phi F_phi'(R_phi)<infinity.

The base core is finite and irreducible, and its critical mean is this finite value.
L206's genuine-core product and full attainment theorem then give

    D_core(beta_r)=D_core(phi)^r,
    mu_(beta_r)=mu_phi^r,
    pi_(beta_r)(0)=mu_phi^(-r).                       (18)

Here D_core denotes the actual state set, not the overlap(2).
Thus the exponentially large overlap in(17) occurs on finite, positively recurrent critical cores, NOT as evidence of infinite critical mean at any fixed member.
Their bounded critical dual convolution norms also grow as mu_phi^r by L240.
Even if the onset N0 is permitted to depend on r, a putative common eventual overlap constant C would have to satisfy C>=mu_phi^r by(12); hence no such common finite C exists on this family.
The already retained radical mean product is reused; the new conclusion is its coexistence with the exact early plateau and later original-overlap spike.
Fixed-input boundedness, varying-degree uniformity and observed finite-time size are three different assertions.

<a id="doubling-overlap-costs-and-next-gate"></a>
### 6. What the changed mechanism supplies and what remains

Equations(3)--(4) replace the complete periodic diagonal by an automatically rooted, fully original-law midpoint overlap.
Equations(5)--(8) expose its entire dyadic time expense and give an actual finite bracket at unit inputs.
Most importantly, an eventual uniform bound for this actual arithmetic overlap proves finite critical mean and attainment by(9)--(12), without knowing R or assuming pointwise renewal asymptotics.
The unknown radius has canceled from every finite observable, while all field/order constraints and original word weights remain.

This identifies a concrete next arithmetic task: bound the full products of normalized integer relation fibers in(4), uniformly over all late n at a FIXED actually recurrent input, or prove that those full overlaps are unbounded.
The former proves recurrence and finite mean at once.
Unboundedness rules out the proposed eventual-C certificate; by the present argument alone it does not classify recurrence, critical mean or attainment, even if recurrence is separately known.
A bound for individual factors, a fixed finite quotient, the zero-avoiding periodic mass, or finitely many early D_n values does not discharge it.
Existing polynomial-in-time norm/covariance expenses are useful for the remainder in(8) but do not themselves provide the constant C in(9).

The exact family(17)--(18) is a strong calibration before seeking an input-uniform theorem: even actual fixed-total-measure, nonunit-circle unit inputs can have a growing perfectly free initial window and an exponential overlap at the next degree scale.
Any uniform proposal must explicitly exclude, pay for or structurally distinguish that behavior.
The full near-one total-measure regime, the original quartic's finite-versus-infinite mean and a Salem-only overlap estimate remain open.
No L289 avoidance term was silently estimated, and no hypothesis about D157's separate profile question entered the proof.
The full near-one and actual quartic mean questions remain unresolved.



## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:58 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C432 full covariance expense](Yin_C_G0432_v1.md#statement) | Unit-only all-time actual counting-core estimate and full q/C_non cost. |
| dependency | [C479 first-return attainment](Yin_C_G0479_v1.md#critical-excursion-attainment-condition) | Complete original renewal/finite-mean criterion at its exact actual-unit scope. |
| dependency | [C493 radical product](Yin_C_G0493_v1.md#radical-actual-core-product) | Actual relative-degree order/core/return products and both directions of finite-mean attainment. |
| dependency | [C212 actual golden radicals](Yin_C_G0212_v1.md#statement) | Full golden carry core and genuine dyadic irreducibility/rate equality, with fixed positive total measure. |
| dependency | [C372 exact golden full series](Yin_C_G0372_v1.md#finite-prime-core-golden-ratio-control) | Complete original forward first-return generating function, not a finite truncation. |
| dependency | [Original full convolution criterion](../ledger/Yin_L_G0240_v1.md#critical-convolution-bounded-density-test) | Fixed accepted whole-order dual criterion with norm RFprime+1-F; recurrent finite-mean specialization only. |
| support | [Original complete proof and repairs](../ledger/Yin_L_G0293_v1.md#doubling-overlap-reuse) | Original Sections1--6/equations1--18, author check, 2026-10-10T05:25 directional repair,2026-10-10T05:27 positive-l domain repair and old R192 fixed inputs/verdicts remain. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:14 |
| status | proved |
| reason | Adopt the complete retained theorem at its exact hypotheses, full costs and negative limits after actual whole current SELF of the published Statement and entire Argument; no independent arrangement or research resumption is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C432 full covariance expense](Yin_C_G0432_v1.md#statement) | Unit-only all-time actual counting-core estimate and full q/C_non cost. |
| dependency | [C479 first-return attainment](Yin_C_G0479_v1.md#critical-excursion-attainment-condition) | Complete original renewal/finite-mean criterion at its exact actual-unit scope. |
| dependency | [C493 radical product](Yin_C_G0493_v1.md#radical-actual-core-product) | Actual relative-degree order/core/return products and both directions of finite-mean attainment. |
| dependency | [C212 actual golden radicals](Yin_C_G0212_v1.md#statement) | Full golden carry core and genuine dyadic irreducibility/rate equality, with fixed positive total measure. |
| dependency | [C372 exact golden full series](Yin_C_G0372_v1.md#finite-prime-core-golden-ratio-control) | Complete original forward first-return generating function, not a finite truncation. |
| dependency | [Original full convolution criterion](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test) | Fixed accepted whole-order dual criterion with norm RFprime+1-F; recurrent finite-mean specialization only. |
| support | [Original complete proof and repairs](../ledger/Yin_L_G0293_v1.md#doubling-overlap-reuse) | Original Sections1--6/equations1--18, author check, 2026-10-10T05:25 directional repair,2026-10-10T05:27 positive-l domain repair and old R192 fixed inputs/verdicts remain. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0745_v1.md#doubling-overlap-whole-self) | The complete current Statement and entire Argument, every selected dependency interface and all original failed-scope/source/native limits. |


### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:00 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire Argument after the actual isolated whole review completed2026-10-22T20:49 UTC, with all original domains, costs, failed/negative scopes, source depth and finite-evidence limits retained. The dated original reviews and current SELF findings keep their actual inputs and relationships; this decision neither backfills old review acts nor resumes research. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C432 full covariance expense](Yin_C_G0432_v1.md#statement) | Unit-only all-time actual counting-core estimate and full q/C_non cost. |
| dependency | [C479 first-return attainment](Yin_C_G0479_v1.md#critical-excursion-attainment-condition) | Complete original renewal/finite-mean criterion at its exact actual-unit scope. |
| dependency | [C493 radical product](Yin_C_G0493_v1.md#radical-actual-core-product) | Actual relative-degree order/core/return products and both directions of finite-mean attainment. |
| dependency | [C212 actual golden radicals](Yin_C_G0212_v1.md#statement) | Full golden carry core and genuine dyadic irreducibility/rate equality, with fixed positive total measure. |
| dependency | [C372 exact golden full series](Yin_C_G0372_v1.md#finite-prime-core-golden-ratio-control) | Complete original forward first-return generating function, not a finite truncation. |
| dependency | [Original full convolution criterion](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test) | Fixed accepted whole-order dual criterion with norm RFprime+1-F; recurrent finite-mean specialization only. |
| support | [Original complete proof and repairs](../ledger/Yin_L_G0293_v1.md#doubling-overlap-reuse) | Original Sections1--6/equations1--18, author check, 2026-10-10T05:25 directional repair,2026-10-10T05:27 positive-l domain repair and old R192 fixed inputs/verdicts remain. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0776_v1.md#current-dyadic-overlap) | The complete current fixed Statement and entire Argument, all necessary mathematical interfaces and actual finite-evidence checks at2026-10-22T20:49 UTC; independently reviewed in the disclosed isolated arrangement, without native discovery/reviewer reruns. |

