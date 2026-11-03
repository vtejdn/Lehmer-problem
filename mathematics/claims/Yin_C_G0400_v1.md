---
author: Yin
---

# Exact conditional Salem return strip, fixed boundary states and geometric core growth

This retains the complete elementary deduction and every hypothesis/proof from [L170](../ledger/Yin_L_G0170_v1.md#exact-salem-return-strip).
The narrow co-return premise is an explicit arithmetic input, supplied here only by the two complete fixed-input Claims.
The coordinator authored the original greedy strip extension, exact necessary/sufficient strip identity, two-state boundary observation and two-sided lattice count.
The original00:22 inspection, its disclosed but unspecified proposed-strengthening explanation, actual inputs and independent-isolation uncertainty remain in [R69](../audits/reviews/Yin_R_G0069_v1.md#exact-strip-growth-review).
The same-minute original-Lehmer nonzero-state wording reread has its own targeted scope and known shared-chain relationship; it is not another whole corrected-chain inspection.
No new computation or source-proof audit is needed for these deductions.
Task/E execution remains paused.

## Statement

Let beta be a Salem unit with1<beta<2, reciprocal irreducible polynomial of degree d>=4, and actual order O=Z[beta].
For every x in O put x_+=x(beta),x_-=x(beta^(-1)),B=1/(beta-1),S=beta B.
Use precisely the original operations x->beta x+eta with eta in{-1,0,1}, and let D be the actual states on finite zero-to-zero words, including the empty word.
Assume that every actual x in O with abs(x_+)<=1 and abs(x_-)<=S has a finite original-digit continuation to zero, with no bound or prior reachability condition on its other embeddings.
Then

    D={x in O:abs(x_+)<B,abs(x_-)<S}.

This is equality with the actual discrete algebraic set, without a condition on neutral embeddings and without replacing O by a projected closure.
For every actual x with abs(x_+)<B and abs(x_-)<=S, a finite greedy prefix with eta=-sign(x_+) while abs(x_+)>1 enters the assumed co-return domain.
The reciprocal lattice involution T=beta^(-1)sigma, sigma(beta)=beta^(-1), converts the continuation of T(x) into an original-digit path from zero to x.
The finite geometric sums for reachability and continuation force both strip inequalities to be strict.

For each fixed input P(t)=t^4-t^3-t^2-t+1 and P(t)=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1, the complete C396 and Lehmer Claim proofs respectively establish the exact narrow co-return premise.
For these two polynomials P(1)=-1, hence P(t)+1=(t-1)Q_1(t) with Q_1 integral and (beta-1)Q_1(beta)=1.
Consequently B belongs to O and has real coordinates(B,-S); its negative has(-B,S).
By injectivity of either real embedding, +/-B are the only actual order elements on any of the four closed natural-strip boundary lines.
Replacing both strict strip inequalities by weak ones adds exactly these two states, neither of which is in D.
This boundary conclusion is restricted to these two fixed P(1)=-1 inputs; the general strip equality has only the stated Salem and narrow co-return hypotheses.

Write r=(d-2)/2, take the r upper unit-circle conjugates zeta_j and put rho(x)^2=sum_(j=1)^r abs(x(zeta_j))^2.
For D_R={x in D:rho(x)<=R}, there exist constants c,C,R_0>0 depending on this input such that for every real R>=R_0,

    c R^(d-2)<=abs(D_R)<=C(R+1)^(d-2).

The upper bound uses separation balls in the full real embedding lattice and a cylinder of fixed widths in the two real coordinates.
The lower bound uses all(N+1)^d actual power-basis elements, O((N+1)^2) half-open real cells of widths1 and beta, and distinct within-cell differences with abs(x_+)<1,abs(x_-)<beta.
Their coefficients have magnitude at most N and rho<=d sqrt(r) N.
Taking N=floor(R/(d sqrt(r))) proves the lower bound for every sufficiently large R, rather than a selected subsequence.
This gives fixed-input growth of order R^2 for the quartic and R^8 for the original Lehmer unit.
It concerns states rather than words or their probabilities; no local-limit theorem, equidistribution, spectral, degree-uniform or Mahler-gap inference is included.
The numerical L_R+25 timing and hitting bounds in the two narrow-domain Claims keep their original narrow-real-strip and bounded-radius hypotheses.
This exact open-strip identity does not extend those bounds automatically.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T17:12 |
| status | open |
| reason | Retain the complete conditional exact-strip/growth theorem, both actual fixed-input premise interfaces and every necessary elementary proof with precise boundaries. Actual complete current whole self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact conditional strip, boundaries and growth](#statement) | Entire general conditional exact-strip and two-sided growth theorem and complete proof: actual Salem unit1<beta<2/reciprocal irreducible degree d>=4/order/original digits and explicit unrestricted-neutral narrow co-return premise, finite greedy sign-fixed recurrence/invariant strip and reciprocal reversed-negated reachability, strict finite-prefix/continuation necessities and actual discrete-set equality, both fixed-polynomial applicability inputs and P(1)=-1 order inverse/only two excluded boundary states, full-lattice separation upper count and full coefficient-box/half-open-cell/difference lower count with all sufficiently large real R and input-dependent positive constants, every rho/r/d exponent and state-versus-word/probability/no-uniformity boundary. |
| argument | [Complete retained proof](#argument) | Entire general conditional exact-strip and two-sided growth theorem and complete proof: actual Salem unit1<beta<2/reciprocal irreducible degree d>=4/order/original digits and explicit unrestricted-neutral narrow co-return premise, finite greedy sign-fixed recurrence/invariant strip and reciprocal reversed-negated reachability, strict finite-prefix/continuation necessities and actual discrete-set equality, both fixed-polynomial applicability inputs and P(1)=-1 order inverse/only two excluded boundary states, full-lattice separation upper count and full coefficient-box/half-open-cell/difference lower count with all sufficiently large real R and input-dependent positive constants, every rho/r/d exponent and state-versus-word/probability/no-uniformity boundary. |
| dependency | [Complete fixed-quartic co-return theorem](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Only actual original-digit co-return for every x in Z[beta] with abs(x_+)<=1 and abs(x_-)<=S for P=t^4-t^3-t^2-t+1, no neutral bound; this supplies the conditional premise at that input without extending its explicit timing domain. |
| dependency | [Complete original-Lehmer co-return theorem](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | Only actual original-digit co-return for every x in Z[beta] with abs(x_+)<=1 and abs(x_-)<=S for the fixed original Lehmer polynomial, no neutral bound; this supplies the conditional premise at that input without extending its explicit timing domain. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T17:16 |
| status | proved |
| reason | Adopt after actual complete current mathematical self-check of the entire exact statement, every necessary proof and all declared fixed input/certificate interfaces. No substantive mathematical defect or missing hypothesis was found. All actual order/original-digit/domain/timing-or-counting/source/native limits remain explicit; retained executions are reused without a new run. Current whole self-review does not close any historical unknown independent arrangement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire general conditional exact-strip and two-sided growth theorem and complete proof: actual Salem unit1<beta<2/reciprocal irreducible degree d>=4/order/original digits and explicit unrestricted-neutral narrow co-return premise, finite greedy sign-fixed recurrence/invariant strip and reciprocal reversed-negated reachability, strict finite-prefix/continuation necessities and actual discrete-set equality, both fixed-polynomial applicability inputs and P(1)=-1 order inverse/only two excluded boundary states, full-lattice separation upper count and full coefficient-box/half-open-cell/difference lower count with all sufficiently large real R and input-dependent positive constants, every rho/r/d exponent and state-versus-word/probability/no-uniformity boundary. |
| argument | [Exact retained argument](#argument) | Entire general conditional exact-strip and two-sided growth theorem and complete proof: actual Salem unit1<beta<2/reciprocal irreducible degree d>=4/order/original digits and explicit unrestricted-neutral narrow co-return premise, finite greedy sign-fixed recurrence/invariant strip and reciprocal reversed-negated reachability, strict finite-prefix/continuation necessities and actual discrete-set equality, both fixed-polynomial applicability inputs and P(1)=-1 order inverse/only two excluded boundary states, full-lattice separation upper count and full coefficient-box/half-open-cell/difference lower count with all sufficiently large real R and input-dependent positive constants, every rho/r/d exponent and state-versus-word/probability/no-uniformity boundary. |
| dependency | [Exact retained dependency](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Only actual original-digit co-return for every x in Z[beta] with abs(x_+)<=1 and abs(x_-)<=S for P=t^4-t^3-t^2-t+1, no neutral bound; this supplies the conditional premise at that input without extending its explicit timing domain. |
| dependency | [Exact retained dependency](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | Only actual original-digit co-return for every x in Z[beta] with abs(x_+)<=1 and abs(x_-)<=S for the fixed original Lehmer polynomial, no neutral bound; this supplies the conditional premise at that input without extending its explicit timing domain. |
| review | [Complete actual current whole self finding](../audits/reviews/Yin_R_G0603_v1.md#current-exact-strip-growth-finding) | Entire general conditional exact-strip and two-sided growth theorem and complete proof: actual Salem unit1<beta<2/reciprocal irreducible degree d>=4/order/original digits and explicit unrestricted-neutral narrow co-return premise, finite greedy sign-fixed recurrence/invariant strip and reciprocal reversed-negated reachability, strict finite-prefix/continuation necessities and actual discrete-set equality, both fixed-polynomial applicability inputs and P(1)=-1 order inverse/only two excluded boundary states, full-lattice separation upper count and full coefficient-box/half-open-cell/difference lower count with all sufficiently large real R and input-dependent positive constants, every rho/r/d exponent and state-versus-word/probability/no-uniformity boundary. Actual whole relationship is self-reviewed; original whole and targeted scopes remain separately retained at their genuine relationships. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T17:57 |
| status | proved |
| reason | Adopt the new complete isolated whole finding after autonomous reconstruction before old substantive target findings. All exact original domains, complete finite proof interfaces, retained execution boundaries, timing/growth quantifiers and every source/full-law limitation were checked. Original R69 UNKNOWN/SELF and targeted item3 clarification remain at their actual historical scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire general conditional exact-strip and two-sided growth theorem and complete proof: actual Salem unit1<beta<2/reciprocal irreducible degree d>=4/order/original digits and explicit unrestricted-neutral narrow co-return premise, finite greedy sign-fixed recurrence/invariant strip and reciprocal reversed-negated reachability, strict finite-prefix/continuation necessities and actual discrete-set equality, both fixed-polynomial applicability inputs and P(1)=-1 order inverse/only two excluded boundary states, full-lattice separation upper count and full coefficient-box/half-open-cell/difference lower count with all sufficiently large real R and input-dependent positive constants, every rho/r/d exponent and state-versus-word/probability/no-uniformity boundary. |
| argument | [Complete selected argument](#argument) | Entire general conditional exact-strip and two-sided growth theorem and complete proof: actual Salem unit1<beta<2/reciprocal irreducible degree d>=4/order/original digits and explicit unrestricted-neutral narrow co-return premise, finite greedy sign-fixed recurrence/invariant strip and reciprocal reversed-negated reachability, strict finite-prefix/continuation necessities and actual discrete-set equality, both fixed-polynomial applicability inputs and P(1)=-1 order inverse/only two excluded boundary states, full-lattice separation upper count and full coefficient-box/half-open-cell/difference lower count with all sufficiently large real R and input-dependent positive constants, every rho/r/d exponent and state-versus-word/probability/no-uniformity boundary. |
| dependency | [Exact accepted input](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Only actual original-digit co-return for every x in Z[beta] with abs(x_+)<=1 and abs(x_-)<=S for P=t^4-t^3-t^2-t+1, no neutral bound; this supplies the conditional premise at that input without extending its explicit timing domain. |
| dependency | [Exact accepted input](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | Only actual original-digit co-return for every x in Z[beta] with abs(x_+)<=1 and abs(x_-)<=S for the fixed original Lehmer polynomial, no neutral bound; this supplies the conditional premise at that input without extending its explicit timing domain. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0607_v1.md#whole-strip-growth-independent-finding) | Entire exact current Statement and complete selected proof with all fixed/general domain guards, finite-code/input/retained-run interfaces, quantitative bounds, source and probability/near-one limitations. |

## Complete retained argument

<a id="argument"></a>

<a id="exact-salem-return-strip"></a>
### General conditional statement

Let beta be a Salem unit with 1<beta<2 and reciprocal irreducible polynomial of degree d>=4.
Let O=Z[beta], x_+=x(beta), x_-=x(beta^(-1)), B=1/(beta-1) and S=beta B.
Use precisely the operations x -> beta*x+eta with eta in {-1,0,1}.
Suppose every actual x in O with |x_+|<=1 and |x_-|<=S has a finite continuation to zero.
Then the actual zero-to-zero return core is exactly

    D={x in O: |x_+|<B, |x_-|<S}.                 (1)

No condition on the unit-circle embeddings is present in (1).
In particular this is an equality with an actual discrete algebraic strip, not with its real projection or closure.
The fixed quartic narrow co-return theorem is fully proved in [C396](Yin_C_G0396_v1.md#quartic-infinite-core-theorem), and the complete original-Lehmer theorem is fully proved in [the responsible Lehmer Claim](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem).
The actual original exact-strip/growth inspection and its stated context remain in [R69](../audits/reviews/Yin_R_G0069_v1.md#exact-strip-growth-review), without inferring review isolation from its title.

### Proof of exactness

First extend the co-return premise to every actual state satisfying |x_+|<B and |x_-|<=S.
If |x_+|<=1, the premise applies directly.
Otherwise put u=|x_+| and choose eta=-sign(x_+).
As long as u>1,

    u'=beta*u-1>0,   u'<u,

because beta>1 and u<B.
The sign does not change during those steps.
The scalar recurrence is u_k=B+beta^k(u_0-B) while this rule continues.
It cannot stay above one indefinitely, since u_0-B<0.
At the first time u_k<=1 it is still positive.
Every original digit preserves |x_-|<=S because beta^(-1)S+1=S.
The finite prefix ends in the narrow co-return domain; its neutral coordinates may have increased but remain finite.
Appending the assumed continuation proves generalized co-return.
The proof never requires the neutral radius to stay below its initial value during this greedy prefix.

The reciprocal automorphism sigma(beta)=beta^(-1) preserves O.
The map T=beta^(-1)sigma is an additive involution with

    T(x)_+=x_-/beta,   T(x)_-=beta*x_+.

If y reaches zero with eta_1,...,eta_n, then y=-sum eta_i beta^(-i), so the reversed negated word takes zero to T(y).
For x in the right-hand side of (1), both x and T(x) satisfy generalized co-return.
A zero continuation of T(x) therefore yields reachability of x from zero, and x's own continuation completes a true return.
This proves sufficiency.

For necessity, a state x reached from zero in a digits satisfies

    |x_-|<=sum_(j=0)^(a-1) beta^(-j)
           =S(1-beta^(-a))<S

when a>0; the empty word gives x=0 and the same strict strip membership.
A continuation from x to zero in b>0 digits gives

    |x_+|<=sum_(j=1)^b beta^(-j)
           =B(1-beta^(-b))<B;

if b=0 then x=0.
Every actual returning state thus lies in the displayed open strip.
This proves (1), including the strict boundaries.

For both fixed polynomials P(t)=t^4-t^3-t^2-t+1 and P(t)=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1, P(1)=-1.
Indeed P(t)+1=(t-1)Q_1(t) for Q_1 in Z[t], so evaluation at beta gives (beta-1)Q_1(beta)=1.
Therefore beta-1 is an algebraic unit and B belongs to O.
Its two real values are B and -S.
The states +/-B are actual lattice points on the boundary, but neither can lie in D by the necessity just proved.
Injectivity of either real embedding shows that these are the only actual O elements on any of the four boundary lines of the closed natural strip.
Thus replacing both strict inequalities by weak ones adds exactly these two states for these two fixed inputs.
This last observation is not needed for (1).

<a id="return-core-neutral-growth"></a>
### A quantitative geometric consequence at fixed input

Write r=(d-2)/2, z_j=x(zeta_j), and rho(x)^2=sum_(j=1)^r |z_j|^2.
Under the same co-return premise, let D_R={x in D:rho(x)<=R}.
There are input-dependent constants c,C,R_0>0 such that

    c R^(d-2)<=|D_R|<=C(R+1)^(d-2)  for R>=R_0.    (2)

For the upper bound, the full embedding of O in R^d is a lattice.
Choose a positive radius epsilon so the Euclidean epsilon-balls about distinct lattice points are disjoint.
Balls about points of D_R lie in a cylinder whose first two coordinate widths are fixed (enlarged by 2epsilon) and whose neutral radius is at most R+epsilon.
Comparing d-dimensional volumes proves the upper estimate.
This uses the complete embedding, not a discreteness claim for the two-real projection.

For the lower bound, use the (N+1)^d distinct coefficient-box elements sum_(i=0)^(d-1) a_i beta^i, a_i in {0,...,N}.
Their two real values lie in a rectangle of side lengths O(N).
Partition into half-open cells of widths 1 and beta.
Some cell contains at least c_0(N+1)^(d-2) distinct elements.
Subtract a selected element from every other element in this cell.
The resulting states have |x_+|<1 and |x_-|<beta, so they belong to D by reciprocal co-return, since beta<2 implies beta<S and 1<B.
Each difference has power-basis coefficients of magnitude at most N; hence every neutral modulus is at most dN and rho<=d sqrt(r) N.
Taking N=floor(R/(d sqrt(r))) and adjusting constants yields the lower bound for every sufficiently large R.
Distinctness survives subtraction.

For the original degree-ten Lehmer input, (2) gives growth of order R^8; for the quartic it gives order R^2.
The constants are fixed-input constants.
This statement quantifies state counts, not counts of words or their original probabilities.
It does not imply a return-probability estimate, a degree-uniform bound, or a positive Mahler gap.
No probabilistic local limit theorem or spectral conclusion is assumed.

## Contribution and fixed-input boundary

The original coordinator's greedy, reciprocal, boundary and counting contributions are retained in full.
The old source/native/review inputs remain fixed in L170, R69 and the two premise Claims.
These elementary deductions neither execute a new certificate nor prove narrow co-return for an arbitrary Salem input.
The original Task/E lifecycle is unaffected.
