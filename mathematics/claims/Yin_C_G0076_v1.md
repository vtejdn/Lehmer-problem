---
author: Yin
---
# Exact six-digit endpoint heat baths, complete core paths and true-midpoint energy

Date: 2026-10-12T14:25.
Human author Yin.
Fixed extraction under the continuing G0001 instruction.
Rounding-recovery supplied all original D31 mathematics through its complete actual 22:14 freeze.
Root supplied only the broad richer-block question and later read the full body, without supplying a new formula or proof step.
The g0001_matrix_recovery AI separately WHOLE-reviewed that actual original body in R299 and NOW authors this new statement, decision and extraction wrapper.
It is therefore a contributor to this allocated extraction and cannot independently review it.
A different noncontributor must actually inspect this new Claim before adoption.
The complete original history, proof, source/access limits, author checks and freeze follow unchanged.

## Statement

Fix the ACTUAL irreducible Salem quartic P(t)=1-t-t^2-t^3+t^4, its real root beta>1, either neutral conjugate zeta, and u=zeta+zeta^-1=(1-sqrt13)/2.
For EVERY integer n>=7 put N=2n.
Let Omega_n consist of ALL eta in{-1,0,1}^N satisfying sum_(i=0)^(N-1)eta_i beta^i=0.
All original conjugate constraints and earlier visits are retained.
The independent original digit probabilities are1/4,1/2,1/4.
Let z(eta) count zero digits and define

    W_n=sum_(eta in Omega_n)2^z(eta),
    p_(2n)=W_n/4^N, pi_n(eta)=2^z(eta)/W_n,
    Z_n(eta)=-zeta^-n sum_(i=0)^(n-1)eta_i zeta^i,
    m_n=E_pi_n |Z_n|^2.

The complex norm is exactly the sum of TWO unweighted real neutral-coordinate squares.
Global sign symmetry gives E_pi_n Z_n=0.
The all-zero word has conditional mass2^N/W_n.

**A. Exact arbitrary-endpoint conditional operator.**
For0<=j<=N-6 take I_j={j,...,j+5}.
Given the outside digits, set x_j=sum_(r=0)^5 eta_(j+r) beta^r and use the COMPLETE fiber

    F_6(x)={theta in{-1,0,1}^6: sum_r theta_r beta^r=x},
    Z_6(x)=sum_(theta in F_6(x))2^z(theta).

H_j leaves all outside digits fixed and draws theta with probability2^z(theta)/Z_6(x_j).
This includes EVERY endpoint, not only0.
It is precisely conditional expectation given the outside digits in L2(pi_n).
Define ONE auxiliary UPDATE by

    b_N=N-5, S_n=(1/b_N)sum_(j=0)^(N-6) H_j.

Every H_j is a self-adjoint orthogonal projection and S_n is a reversible positive contraction for the original pi_n.
For every complex g,

    D_6,n(g)=<g,(Id-S_n)g>_pi_n
       =(1/b_N)sum_j E_pi_n Var(g | outside I_j)
       =(1/2)sum_(eta,xi)pi_n(eta)S_n(eta,xi)
                                      |g(xi)-g(eta)|^2.

Neither irreducibility nor a positive global gap is part of this conclusion.

**B. Three COMPLETE local fibers and their original probabilities.**
Any same-endpoint six-digit difference is P(t)(a+bt) with integers a,b, whose coefficient vector is

    (a,b-a,-a-b,-a-b,a-b,b).

The following are the entire fibers, not just pairs of exhibited legal alternatives.

1. At the NONZERO endpoint -2beta^3, the only words are

       X=(0,-1,1,-1,1,-1),
       Y=(-1,1,1,-1,-1,0).

   They satisfy Y-X=P(t)(t-1), have block weights2 and2, and the conditional transition probabilities in both directions are1/2.

2. At the NONZERO endpoint -1-beta+beta^2, the only words are

       C0=(-1,0,0,-1,-1,1),
       C1=(-1,-1,1,0,0,0).

   They satisfy C1-C0=-tP, have block weights4 and8, and the forward/reverse probabilities are2/3 and1/3.

3. At endpoint0, the complete fiber is six zeros and the four length-six words +/-P,+/-tP.
   Its weight is64+4*2=72.
   Each signed P followed by0 moves to six zeros with probability8/9, and the reverse probability to each specified signed P word is1/36.

Global sign reflection gives the reflected fibers and the same probabilities.
These are the original conditional probabilities with zero-digit weights; uniform resampling would give a different law.

**C. Every original long core has a complete path to zero.**
Reuse the actual strings

    D=(1,-1,-1,0), B=(-1,1,-1,1,-1), C=(0,-1,-1,1),
    V_m=D B^m C, ell=8+5m,
    D'=(1,-1,-1), B'=(-1,1,1,-1,-1),

where word powers mean CONCATENATION.
For the stated n put

    m=floor((N-8)/5)>=1, p=N-ell in{0,1,2,3,4},
    l=min(2,p), r=p-l<=2,
    eta_n^+=(l zeros) V_m (r zeros), eta_n^-=-eta_n^+.

These are the original C70 words.
Their exact quotient is

    V_m=P Q_m,
    Q_m=1+t^3+t^4(-1+t+t^4)sum_(a=0)^(m-1)t^(5a).

Both eta_n^+ and eta_n^- are connected to zero by explicit S_n paths of EXACTLY J_m=2m+2 nontrivial updates.
All intermediate states of the positive unpadded transport stage are

    W^(a)=D' (B')^a 0 B^(m-a) C, 0<=a<=m.

At index3+5a change0B to B'0 by fiber B.1.
The complete quotient after those m moves is

    Q_m+(t-1)t^3 sum_(a=0)^(m-1)t^(5a)
        =sum_(a=0)^m t^(5a)+t^(5m+3).

At index5m+2 the last six digits are C0.
Use B.2 to remove the last t^(5m+3) quotient term, leaving m+1 disjoint consecutive copies of P followed by three zeros.
Erase those P blocks right to left, using B.3 at indices5a for a=m,...,0.
There are m transports, one cap change and m+1 erasures.

Add the SAME original l,r padding to every state, shifting every interval start by l.
Every selected interval lies inside the original N positions, including n7,m1.
Negating every state gives the negative path.
Before reaching zero the first nonzero digit at position l is+1 on the positive path and-1 on the negative path.
Each path has distinct intermediate states, and the two paths meet ONLY at zero.
Thus this old C70 pair is not a closed component for S_n.
No statement about all other components follows.

**D. Full original masses, exact event probability and paid path energy.**
Put v_n=|Z_n(eta_n^+)|^2=|Z_n(eta_n^-)|^2.
For n modulo5 equal0,1,2,3,4, respectively,

    v_n=5-2u, 2-u, 7-3u, 7-3u, 2-u,
    2-u<=v_n<=7-3u.

Each initial word has2+p zeros, original unconditional probability2^(2+p)/4^N and conditional mass

    w_n=2^(2+p)/W_n, rho_n=2w_n v_n.

Every transport state has that same weight.
The cap gives zero count3+p; after a erasures it is3+p+5a, reaching N at a=m+1.
Every path-state conditional mass is at least w_n.
From either specified initial word, the event selecting every displayed interval and alternative in the next J_m updates has EXACT probability

    p_path=b_N^(-J_m) (1/2)^m (2/3) (8/9)^(m+1)>0.

Other selected intervals may realize the same state transition, so this is a lower bound for following only the state path or hitting zero by J_m.
Starting in the signed pair under pi_n separately costs2w_n.

For EVERY complex g, the original Dirichlet form satisfies

    D_6,n(g)>=w_n/[2b_N J_m]
       *[|g(eta_n^+)-g(0)|^2+|g(eta_n^-)-g(0)|^2].

In particular

    D_6,n(Z_n)>=rho_n/[2b_N J_m],
    8(2-u)2^(-2N)<=rho_n<=(7-3u)2^(7-N).

The paths are edge-disjoint and every edge conductance is at least w_n/(2b_N), which supplies the displayed constant by Cauchy--Schwarz.
The pair's paid quantity tends to zero exponentially.
Its existence supplies no uniform probability fraction, global mixing-time estimate or chronological diffusive growth.

**E. Strict old-graph enlargement and all-n true-midpoint update energy.**
Let T_n be the ACTUAL C60 uniformly chosen single-quotient-coordinate operator, with N-4 sites.
Then for every complex g,

    D_6,n(g)>=(N-4)/[2(N-5)] <g,(Id-T_n)g>_pi_n.

Every old edge is a new edge, and the inclusion is strict: the first transport out of an original old-frozen core changes two adjacent quotient coordinates.
Five-digit original-outside conditioning is exactly the old one-quotient conditional partition; the comparison assigns each old interval to a containing six-digit interval, using each at most twice.
It compares averaged conditional variances and pays BOTH clocks.
Because the old global gap is zero, this inequality supplies no positive new global gap.

With C_star=5+sqrt13, for EVERY n>=7,

    C_star/[1024(N-5)]<=D_6,n(Z_n)<=38/(N-5).

The lower bound uses the exact old C60 two-coordinate energy.
For the upper bound only the five intervals j=n-5,...,n-1 cross the midpoint.
With a=n-j, equality of FULL endpoints bounds the conditional diameter by2min(a,6-a).
Half the squared diameter gives2min(a,6-a)^2, whose five values sum to38.
This is the arbitrary-endpoint C45 bound at one complex neutral place.
It makes no zero-endpoint or zero-conditional-mean assumption.
If every six-digit interval is instead updated at unit rate, multiply BOTH energy bounds by N-5.
The result concerns auxiliary-update energy, not an upper bound on m_n.

**F. Precisely conditional spectral and chronological consequences.**
Define the real global Rayleigh gap

    lambda_6,n=inf_(Var_pi_n(g)>0)D_6,n(g)/Var_pi_n(g)
                in[0,1].

Then

    lambda_6,n m_n<=D_6,n(Z_n)<=38/(N-5).

An ADDITIONAL eventual lower bound lambda_6,n>=c/(N-5) for some c>0 would imply m_n<=38/c eventually, hence original full-state tightness using the fixed nonneutral strips and actual rank-four Minkowski lattice.
C60's unchanged original-law tightness interface would then give finite original chronological critical first-return mean.
This premise, global irreducibility and that mean classification are NOT proved here.

Conversely a supplied value m_n>=epsilon n implies lambda_6,n<=38/[epsilon n(N-5)] at that same n.
Small gap does not imply diffusive variance growth.
The proved paths place only the specified signed cores and zero in one component; other components, their original masses, all conditional means and uniform mixing remain unresolved.
The C64/C68/C70 obstructions retain their own specified operators.

The construction uses exactly the uniform six-original-digit arbitrary-endpoint heat bath.
It contains no free full-word refresh, reweighted path law, global spectral lower estimate, varying-input transfer or unrestricted G0001 solution.
All new finite fiber, path, projection and variance arguments are retained in full below.
Classical heat-bath/Gibbs-sampler naming retains the existing LP17 partial indexed-text and unavailable-full-book limits; no external mixing theorem or new source proof is adopted.

## Current assessment
[Selected decision](#decision-independent-current-whole-review-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T14:25 |
| status | open |
| reason | Register the exact original six-digit arbitrary-endpoint operator, complete fibers, all-n>=7 long-core annihilation paths and original probabilities, fully paid path/clock comparison, midpoint energy and precisely conditional gap/mean interface. The ENTIRE original 22:14 D31 is retained. R299 whole-reviewed that original body; its reviewer now authors this new wrapper, so an actual different-noncontributor extraction review is required before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F with the fixed original quartic/law, n>=7, all exact paths, weights, clocks, quantitative constants and unresolved global/chronological scope. |
| argument | [Entire retained original body](#argument) | Complete allocation/reuse/candidate, Sections1--7/Theorems1--2/equations1--17, sources/access, roles, author checking and actual22:14 freeze. |
| dependency | [C60 original law and energy](Yin_C_G0060_v1.md#statement) | Exact returned law, unique integer quotient, original conditional operator with N-4 sites and C_star/[512(N-4)] lower midpoint energy in TWO unweighted real coordinates. |
| dependency | [C60 conditional finite-mean interface](Yin_C_G0060_v1.md#quartic-local-gap-necessary-price) | Eventual bounded TRUE midpoint second moment implies full actual-state tightness through fixed strips/lattice, then the accepted original chronological finite-mean implication. No positive lower gap is assumed as a result. |
| dependency | [C70 actual cores and midpoint](Yin_C_G0070_v1.md#statement) | Original D B^m C identity, all-n>=7 padding, old frozen status, complete v_n and original pair probabilities; its reflection operator is distinct from this new six-digit dynamics. |
| dependency | [C45 all-endpoint diameter](Yin_C_G0045_v1.md#statement) | Part A's actual two-neutral-coordinate endpoint diameter/conditional-variance interface only; no unweighted overlapping certificate or total midpoint upper covariance bound is imported. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0299_v1.md#six-digit-whole-independent-finding) | Entire actual22:14 D31 and its used interfaces were directly reconstructed before this wrapper was written. This finding does not inspect or adopt the new statement/wrapper. Referenced finding relationship: self-reviewed. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T14:31 |
| status | proved |
| reason | Adopt original whole R299 and separate actual extraction R405. The complete original-law arbitrary-endpoint six-digit operator, all-n long-core annihilation paths, full original probabilities and paid update-energy bounds are fixed. Global irreducibility, uniform spectral lower bound and chronological mean/diffusion conclusions remain unproved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F with the fixed original quartic/law, n>=7, all exact paths, weights, clocks, quantitative constants and unresolved global/chronological scope. |
| argument | [Entire retained original body](#argument) | Complete allocation/reuse/candidate, Sections1--7/Theorems1--2/equations1--17, sources/access, roles, author checking and actual22:14 freeze. |
| dependency | [C60 original law and energy](Yin_C_G0060_v1.md#statement) | Exact returned law, unique integer quotient, original conditional operator with N-4 sites and C_star/[512(N-4)] lower midpoint energy in TWO unweighted real coordinates. |
| dependency | [C60 conditional finite-mean interface](Yin_C_G0060_v1.md#quartic-local-gap-necessary-price) | Eventual bounded TRUE midpoint second moment implies full actual-state tightness through fixed strips/lattice, then the accepted original chronological finite-mean implication. No positive lower gap is assumed as a result. |
| dependency | [C70 actual cores and midpoint](Yin_C_G0070_v1.md#statement) | Original D B^m C identity, all-n>=7 padding, old frozen status, complete v_n and original pair probabilities; its reflection operator is distinct from this new six-digit dynamics. |
| dependency | [C45 all-endpoint diameter](Yin_C_G0045_v1.md#statement) | Part A's actual two-neutral-coordinate endpoint diameter/conditional-variance interface only; no unweighted overlapping certificate or total midpoint upper covariance bound is imported. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0299_v1.md#six-digit-whole-independent-finding) | Entire actual22:14 D31 and its used interfaces were directly reconstructed before this wrapper was written. This finding does not inspect or adopt the new statement/wrapper. Referenced finding relationship: self-reviewed. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0794_v2.md#c76-six-digit-actual-extraction-finding) | Complete ACTUAL registered statement, entire preserved original and all exact interfaces separately checked after allocation by a noncontributor; earlier whole review retains its original scope. Referenced finding relationship: unknown. |


### Decision independent-current-whole-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:10 |
| status | proved |
| reason | The current finding is SELF because its initial complete argument input included author-validation conclusions beyond the necessary derivation. Adopt the separately organized current fixed-target finding after complete statement and retained-argument inspection, including late extensions, actual costs, controls, necessary mathematical interfaces and source limits, while excluding credited comparison scopes first separately checked after old-review exposure. The initial mathematical conclusion was formed at 2026-10-22T22:47 UTC before old-target review comparison. The finding records the exact interface and later credited-comparison reading sequence. Preserve fixed mathematics, historical decisions, all non-review premises and their scopes; retain earlier findings in their original homes at their actual recorded relationships and checking scopes. This selects current review evidence and supplies no new research, Task completion or execution resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement: statement](#statement) | Entire A--F with the fixed original quartic/law, n>=7, all exact paths, weights, clocks, quantitative constants and unresolved global/chronological scope. |
| argument | [Argument: argument](#argument) | Complete allocation/reuse/candidate, Sections1--7/Theorems1--2/equations1--17, sources/access, roles, author checking and actual22:14 freeze. |
| dependency | [Dependency: statement](Yin_C_G0060_v1.md#statement) | Exact returned law, unique integer quotient, original conditional operator with N-4 sites and C_star/[512(N-4)] lower midpoint energy in TWO unweighted real coordinates. |
| dependency | [Dependency: quartic-local-gap-necessary-price](Yin_C_G0060_v1.md#quartic-local-gap-necessary-price) | Eventual bounded TRUE midpoint second moment implies full actual-state tightness through fixed strips/lattice, then the accepted original chronological finite-mean implication. No positive lower gap is assumed as a result. |
| dependency | [Dependency: statement](Yin_C_G0070_v1.md#statement) | Original D B^m C identity, all-n>=7 padding, old frozen status, complete v_n and original pair probabilities; its reflection operator is distinct from this new six-digit dynamics. |
| dependency | [Dependency: statement](Yin_C_G0045_v1.md#statement) | Part A's actual two-neutral-coordinate endpoint diameter/conditional-variance interface only; no unweighted overlapping certificate or total midpoint upper covariance bound is imported. |
| support | [Recorded original finding](../audits/reviews/Yin_R_G0299_v1.md#six-digit-whole-independent-finding) | Entire actual22:14 D31 and its used interfaces were independently reconstructed before this wrapper was written. This finding does not inspect or adopt the new statement/wrapper. Finding relationship: self-reviewed. |
| review | [Current SELF finding](../audits/reviews/Yin_R_G0794_v2.md#g76-current-independent) | Complete current mathematical statement and retained proof, including all late extensions, paid arithmetic, useful controls and accepted necessary interfaces at their exact scopes; exclude post-initial credited comparison scopes identified by the finding; initial conclusion 2026-10-22T22:47 UTC, then old-finding comparison; actual interface and credited-comparison reading limits are disclosed in the finding. |

## Registration and complete preservation

The [original entire D31 freeze](#six-digit-entire-author-freeze) is extraction ancestry rather than another proof dependency.
The ENTIRE body follows after removing only duplicate author/framework front matter, demoting its first title by one hash, and normalizing line endings and terminal/separating blank lines.
Every original paragraph, formula, explicit anchor, candidate status, reuse/failure/source/access limit, contribution and freeze remains.
Original ../claims/ and ../audits/ links remain valid from this Claim directory and require no rebasing.
No proof passage is replaced by a summary.

Rounding-recovery remains the original proof author.
R299 records the fresh matrix collaborator's actual noncontributor WHOLE review of that original body.
The same collaborator NOW authors this new extraction wrapper and is a contributor to the new artifact.
Root's broad assignment and full reading supplied no D31 proof step; root may arrange or perform a separately disclosed actual extraction review.
Historical pending-review prose in the retained body remains historical; this new initial decision states the extraction's present pending review.

The [LP17 ordinary attribution account](../audits/literature/LP17/readme.md#finite-conditional-resampling-attribution) remains partial indexed method naming with unavailable complete second-edition acquisition.
It is not made a canonical review binding or accepted external mixing premise.
Structural validation and literal preservation are not mathematical acceptance.
This registration performs no adopted decision, D retirement or native mathematical run.

## Argument

## Six-digit endpoint heat baths dissolve the primitive quartic cores

Date: 2026-10-12T14:03.
Human author Yin.
AUTHOR inquiry by rounding-recovery under the original G0001 continuation.
Root supplied only the broad request for a richer original-law block heat bath after C68/C70, not the six-digit replacement, path or quantitative estimates below.
All new construction and derivation are this author's.
No native mathematical computation, new J or external source is proposed.

## Bounded reuse and actual question

The actual C60 original-law conditional operator and midpoint energy, C64 old single-site freezing, C68 midpoint invariant component, C70 full long-core/returned-interval-reflection obstruction, and C45 arbitrary-endpoint fiber locality/covariance barrier were read.
These results remain true for their specified update/certificate classes.
C70 explicitly leaves arbitrary endpoint-conditioned block heat baths outside its theorem; C45 already treats arbitrary endpoints for a different within-block lower covariance certificate and forbids promoting its bound to an upper total covariance bound.
A targeted local search for block resampling, arbitrary endpoints, bounded blocks and long cores found those interfaces but no retained six-digit path from the C70 cores to the all-zero returned word.
This is a bounded reuse observation, not a priority assertion.

The classical heat-bath/Gibbs-sampler attribution and its LIMITED partial indexed-source access are retained in the existing LP17 account.
Finite conditional-expectation/detailed-balance calculations will be proved locally; no external mixing theorem or positive gap is imported.

## Candidate to verify directly here

Keep the ORIGINAL fixed Salem quartic P=1-t-t^2-t^3+t^4, original digits(-1,0,1) of probabilities(1/4,1/2,1/4), every lengthN=2n full-field returned word, exact conditional weights2^z/W_n and the actual neutral midpoint.
Choose uniformly one of the N-5 original intervals of length6 and resample its digits from their COMPLETE conditional law given all digits outside it.
Every arbitrary endpoint fiber is included, not only zero-sum blocks or sign flips.

The local words (0,-1,1,-1,1,-1) and(-1,1,1,-1,-1,0) differ by P(t)(t-1).
They appear to be the ENTIRE common-endpoint six-digit fiber, of equal original weight.
This allows the leading zero of C70's core D B^m C to move through all m repeated blocks.
After m moves its quotient should be1+t^5+...+t^(5m)+t^(5m+3).
One further local removal of the last P term, followed by right-to-left deletion of the m+1 disjoint P blocks, would reach the all-zero word in2m+2 legal moves.
Proposed exact conditional probabilities are1/2 for each transport,2/3 for the cap removal and8/9 for each final block deletion.
Every original zero weight and the actual chosen-block clock must be charged.

The intended output is a fully paid path and connectivity for these SPECIFIED long cores, plus exact reversible original-law dynamics and useful quantitative upper/lower midpoint-update energy.
It must not assert global irreducibility, a positive mixing lower bound, chronological diffusion or a Mahler gap from the existence of these paths.
Complete substantive proof and useful failures will remain in this responsible draft.

<a id="six-digit-original-law-operator"></a>
## 1. Exact original law and arbitrary-endpoint six-digit kernel

Use the ACTUAL irreducible Salem quartic P(t)=1-t-t^2-t^3+t^4, its real root beta>1, either neutral conjugate zeta, and u=zeta+zeta^-1=(1-sqrt13)/2.
For EVERY integer n>=7 set N=2n and let Omega_n contain ALL eta in{-1,0,1}^N with F_eta(beta)=0, where F_eta=sum_(i=0)^(N-1)eta_i t^i.
The original independent digit probabilities are1/4,1/2,1/4.
With z(eta) its number of zeros, use

    W_n=sum_(eta in Omega_n)2^z(eta),
    Pr(original return at N)=W_n/4^N,
    pi_n(eta)=2^z(eta)/W_n,
    Z_n(eta)=-zeta^-n sum_(i=0)^(n-1)eta_i zeta^i,
    m_n=E_pi_n |Z_n|^2.                                (1)

The complex modulus is the sum of squares of TWO unweighted real neutral coordinates.
Every original return and every earlier visit is retained.
Global sign symmetry gives E_pi_n Z_n=0, and the all-zero word belongs to Omega_n with weight2^N.

For j=0,...,N-6 let I_j={j,...,j+5}.
Given eta, put x_j=sum_(r=0)^5 eta_(j+r) beta^r and define its COMPLETE six-digit endpoint fiber and weight

    F_6(x)={theta in{-1,0,1}^6: sum_r theta_r beta^r=x},
    Z_6(x)=sum_(theta in F_6(x))2^z(theta).

Let H_j resample the six digits from probability2^z(theta)/Z_6(x_j), leaving every outside digit fixed.
This includes ALL endpoints x_j, not only0.
Since beta^j is a unit, preserving x_j is exactly the condition for keeping the whole return with those outside digits.
Equality at beta implies the full original polynomial relation, hence all conjugate returns are preserved as well.
Define one UPDATE by

    S_n=(1/(N-5))sum_(j=0)^(N-6) H_j.                  (2)

Every H_j is exactly conditional expectation in L2(pi_n) given the digits outside I_j.
To verify the conditional weights, factor2^z(eta)=2^z(outside)2^z(inside); the outside factor and W_n are constant on its fiber.
Detailed balance has the symmetric common factor2^z(outside)2^z(theta)2^z(theta')/[W_n Z_6(x_j)].
Thus H_j is a self-adjoint orthogonal projection and S_n is a reversible positive contraction for the ORIGINAL law.
For a complex function g, with conditional variance E|g-Eg|^2,

    D_6,n(g)=<g,(Id-S_n)g>_pi_n
       =(1/(N-5))sum_j E_pi_n Var(g | outside I_j)
       =(1/2)sum_(eta,xi)pi_n(eta)S_n(eta,xi)
                                      |g(xi)-g(eta)|^2. (3)

All sums are finite and all positive-probability transitions are reversible.
No assertion of irreducibility follows from(2)--(3).
The [C60 finite conditional-resampling proof](Yin_C_G0060_v1.md#quartic-local-operator-and-energy) and [LP17 attribution-only account](../audits/literature/LP17/readme.md#finite-conditional-resampling-attribution) are reused at their actual scope.
The latter still records unavailable full-book acquisition and partial indexed-text inspection; no source-completeness or new mixing theorem is implied.

<a id="six-digit-three-exact-fibers"></a>
## 2. Three complete fibers with their original weights

For any two six-digit words with the same endpoint, their polynomial difference is divisible by the ACTUAL monic quartic P.
Its degree is at most5, so the integer quotient is a+bt.
Conversely such a difference preserves the endpoint if its new digits remain legal.
The complete six coefficients of P(a+bt) are

    (a,b-a,-a-b,-a-b,a-b,b).                            (4)

Monic division justifies INTEGER a,b, not a fractional or bounded-quotient guess.
The following fiber classifications use every integer possibility in(4).

**Transport fiber.**
Define

    X=(0,-1,1,-1,1,-1),
    Y=(-1,1,1,-1,-1,0).

Their difference Y-X=P(t)(t-1).
More explicitly their common actual endpoint is -2beta^3: reducing X(t)=-t+t^2-t^3+t^4-t^5 by P gives -2t^3.
This endpoint is NONZERO.
For a legal alternative X+P(a+bt), positions2 and3 force a+b=0.
Position0 gives -1<=a<=1, and position4 gives -1<=a<=0.
The remaining positions allow both a0 and a=-1 and no others.
The resulting quotients(a,b) are(0,0),(-1,1), giving EXACTLY X,Y.
Both have one zero and original block weight2, so

    F_6(-2beta^3)={X,Y}, H_j(X,Y)=H_j(Y,X)=1/2.        (5)

The notation H_j(X,Y) means the actual conditional block probability with any legal fixed outside word and this endpoint.
For globally negated words the reflected fiber and identical probabilities apply.

**Cap fiber.**
Define

    C0=(-1,0,0,-1,-1,1),
    C1=(-1,-1,1,0,0,0).

Their difference is -tP and their common endpoint is -1-beta+beta^2, nonzero by degree<4.
In a legal C0+P(a+bt), position0 gives a>=0, position5 gives b<=0, and position1 gives a-b<=1.
Hence(a,b) is one of(0,0),(1,0),(0,-1).
Position3 excludes(1,0), and the remaining two are legal.
This is the ENTIRE fiber.
The original weights are4 and8, respectively, so

    H_j(C0,C1)=2/3, H_j(C1,C0)=1/3.                   (6)

**Zero fiber.**
For a length-six word of endpoint0, (4) applies relative to the zero word.
The first and last coefficients force a,b in{-1,0,1}, and the middle coefficients force both |a+b|<=1 and |a-b|<=1.
Thus the only possibilities are(0,0),(+1,0),(-1,0),(0,+1),(0,-1).
These are the zero word and the four words +/-P, +/-tP in length6.
The zero word has weight64 and each other word has weight2.
Consequently

    Z_6(0)=72,
    H_j(P followed by0, six zeros)=8/9,
    H_j(six zeros, P followed by0)=1/36.                (7)

The same values hold for the negative P word.
These are exact original conditional probabilities, not chosen symmetric edge weights.
The zero counts change on(6)--(7), so replacing those fibers by uniform resampling would change the original law.

<a id="six-digit-long-core-annihilation-path"></a>
## 3. A complete short-block path from each long core to zero

Reuse ONLY the exact original C70 family and its original probability/midpoint conclusions.
Write

    D=(1,-1,-1,0), B=(-1,1,-1,1,-1), C=(0,-1,-1,1),
    V_m=D B^m C, ell=8+5m, m>=1,
    B'=(-1,1,1,-1,-1), D'=(1,-1,-1).

Powers of words here mean CONCATENATION.
The [C70 complete polynomial identity](Yin_C_G0070_v1.md#long-frozen-core-identities) is

    V_m=P Q_m,
    Q_m=1+t^3+t^4(-1+t+t^4)sum_(r=0)^(m-1)t^(5r).

For our N=2n choose m=floor((N-8)/5), p=N-ell in{0,1,2,3,4}, l=min(2,p), r=p-l<=2.
The positive original word eta_n^+ has l leading zeros, core V_m and r trailing zeros; eta_n^-=-eta_n^+.
These are C70's original words, not new words inferred from a finite table.

**Theorem 1.**
For EVERY n>=7, both eta_n^+ and eta_n^- are connected to the all-zero word by S_n transitions.
There is an explicit path of EXACTLY

    J_m=2m+2                                             (8)

nontrivial updates.
Each move changes at most six consecutive original digits and preserves the original full field return.
The paths for the two signs are disjoint except at the all-zero endpoint.
Thus the signed long-core pair is NOT a closed component for this operator, even though C70 proves its closed-component obstruction for every cap in the different returned-interval reflection dynamics.

**Proof and complete states.**
First work with the unpadded positive core.
For a=0,...,m, let

    W^(a)=D' (B')^a 0 B^(m-a) C.

It starts at W^(0)=V_m.
For each a<m replace the six-digit substring0B by B'0 at core index3+5a, using(5).
The resulting word is exactly W^(a+1).
All other digits remain unchanged, all digits are legal, and each difference is t^(3+5a)P(t)(t-1).
Each state has precisely two zeros, so all have the SAME original weight.
This lists every intermediate state explicitly, not only the endpoints of a proposed path.

After m transports, the quotient has changed by(t-1)t^3 sum_(a=0)^(m-1)t^(5a).
Expanding the retained Q_m and canceling the telescoping -t^3+t^8 terms gives the EXACT final quotient

    Q_m+(t-1)t^3 sum_(a=0)^(m-1)t^(5a)
       =sum_(a=0)^m t^(5a)+t^(5m+3).                   (9)

The last six digits of W^(m), starting at index5m+2, are C0.
Apply(6), whose quotient change is -t^(5m+3).
The new quotient is sum_(a=0)^m t^(5a); hence the resulting length-ell word is m+1 disjoint consecutive copies of the five-digit coefficient word P=(1,-1,-1,-1,1), followed by THREE zeros.
Its total zero count is now3, one more than before.
This agrees both with the local cap replacement and the global polynomial identity.

Now erase the rightmost remaining P block, then the next rightmost, until all m+1 blocks are erased.
At each step the block P is followed by a zero, so use exactly the length-six zero fiber(7) starting at index5a, a=m,m-1,...,0.
Each erasure increases the zero count by5 and changes the quotient by -t^(5a).
After m+1 erasures the word is all zero.
There were m transports, one cap move and m+1 erasures, proving(8).
The entire list of padded states is obtained by adding the original l leading and r trailing zeros.
All specified interval starts are shifted by l; each remains in0,...,N-6, including the cap interval which ends exactly at the core's last digit.

Negate every state for the negative path.
The global law and all three conditional probabilities are sign symmetric.
Before its final zero state, every positive path word has first nonzero digit+1 at position l: transport and cap moves occur later, and P blocks are erased right to left.
Every negative path word has first nonzero digit-1 at that same position.
The two paths are therefore disjoint except at zero.
Within either path the moving-zero position distinguishes the transport states, the cap changes the total zero count by1, and subsequent erasures increase it by5; all displayed consecutive states are distinct.
This proves the theorem.

The path uses genuinely nonzero-endpoint moves in(5)--(6).
It is not a rephrasing of a sign reversal on a returned interval.
Its local quotient changes use two adjacent coefficients for the transports and an old single coefficient for the cap and erasures; feasibility depends on the actual intermediate words, which the proof retains.

<a id="six-digit-path-probability-and-paid-energy"></a>
## 4. Original probabilities and a paid path inequality

Keep p,l,r,m from Section3 and put b_N=N-5, J_m=2m+2.
The [C70 actual midpoint calculation](Yin_C_G0070_v1.md#long-frozen-all-length-midpoints) supplies Z_n(eta_n^-)=-Z_n(eta_n^+) and the common nonzero squared modulus v_n.
For n modulo5 equal0,1,2,3,4, respectively,

    v_n=5-2u, 2-u, 7-3u, 7-3u, 2-u.

Thus2-u<=v_n<=7-3u.
No larger-degree or varying-input statement is inferred from this fixed quartic.
Each of the two initial words has exactly2+p zero digits, ORIGINAL unconditional probability2^(2+p)/4^N, and conditional mass

    w_n=2^(2+p)/W_n,
    rho_n=2w_n v_n=v_n 2^(3+p)/W_n.                    (10)

The m transports keep the zero count2+p.
The cap move increases it to3+p.
After a of the final P-block erasures the zero count is3+p+5a.
At a=m+1 this is N, as required for the all-zero word.
In particular every state on either path has pi_n mass at least w_n.
These exact original weights are not replaced by uniform vertex weights.

Given either initial word, the event that the next J_m updates select the displayed interval at each step and take the displayed alternative has EXACT probability

    p_path=b_N^(-J_m) (1/2)^m (2/3) (8/9)^(m+1)>0.     (11)

Some state transitions may also be produced by other selected intervals; (11) specifies the interval choices as part of the event and is a valid lower bound for following the state path or hitting zero by J_m.
The probability of starting at either original signed word under pi_n is2w_n.
Thus no statement about that path may silently discard the factor w_n.
The small explicit bound in(11) does not bound a global mixing time from above by O(n), nor does it prove a slow-mixing lower bound.

For EVERY complex function g on Omega_n, the exact reversible Dirichlet form obeys

    D_6,n(g)>= w_n/[2b_N J_m]
      *[|g(eta_n^+)-g(0)|^2+|g(eta_n^-)-g(0)|^2].      (12)

Indeed each selected path edge has actual forward transition probability at least1/(2b_N), by(5)--(7), and its starting pi_n mass is at least w_n.
Its unoriented conductance pi_n(x)S_n(x,y) is therefore at least w_n/(2b_N).
Detailed balance identifies both orientations.
Formula(3) is the sum of conductance times squared difference over unoriented edges.
The two paths share no edge, so keep all their edges in that nonnegative sum.
Cauchy--Schwarz along each J_m-edge path bounds the sum of squared edge differences below by the squared endpoint difference divided by J_m.
This proves(12), with no general network theorem or mixing assumption.

For the TRUE midpoint g=Z_n, Z_n(0)=0 and its endpoint norms are v_n, so(12) gives the fully paid bound

    D_6,n(Z_n)>=rho_n/[2b_N J_m].                       (13)

This is an explicit path contribution, not a lower bound on m_n independent of the original pair's mass or a classification of the full communicating graph.
In fact the elementary inequalities2^N<=W_n<=4^N give

    8(2-u)2^(-2N)<=rho_n<=(7-3u)2^(7-N).               (14)

Thus this particular pair's paid contribution tends to0 exponentially, despite its bounded nonzero midpoint.
The path resolves the old closed-component obstruction for this pair, but does not turn its tiny original mass into a uniform proportion.
Every bound retains N=2n, the original zero weights and the complete field return.

<a id="six-digit-comparison-and-actual-midpoint-energy"></a>
## 5. Genuine enlargement and all-n midpoint-update energy

**Theorem 2.**
Let T_n be the ACTUAL C60 uniform single-quotient-coordinate operator, with N-4 sites.
For every complex g on Omega_n,

    D_6,n(g)>=(N-4)/[2(N-5)] <g,(Id-T_n)g>_pi_n.       (15)

Every edge of the old graph is an edge of the new graph.
The inclusion is STRICT on these original words, since the six-digit transport in(5) changes two quotient coordinates and leaves an old-frozen word.
Nevertheless(15) does not prove a positive global gap, because the old global gap is0.

For C_star=5+sqrt13 and EVERY n>=7, the TRUE midpoint satisfies

    C_star/[1024(N-5)] <= D_6,n(Z_n) <=38/(N-5).         (16)

This is ONE uniformly chosen six-digit interval per update.
If each such interval is updated at unit rate, multiply both sides by N-5.
These are auxiliary-update energy bounds, not chronological variance growth.

**Proof of the comparison.**
Let J_j={j,...,j+4},0<=j<=N-5, be a five-digit interval.
On the full returned state space, conditioning on all original digits outside J_j is EXACTLY the same partition as fixing every quotient coefficient except a_j.
In one direction a change delta t^j P changes no digit outside J_j.
In the other, a difference supported in J_j that vanishes at beta is t^j times a polynomial of degree at most4 vanishing at beta, so monicity and minimality force an integer scalar multiple of t^j P.
Thus the five-digit conditional kernel is precisely C60's K_j, including its original conditional weights.

If J_j is contained in I_a, conditioning outside I_a reveals fewer coordinates than conditioning outside J_j.
The finite conditional-variance identity, or the norm monotonicity of these nested conditional-expectation projections, gives

    E Var(g | outside J_j)<=E Var(g | outside I_a).

This is an averaged statement; a pointwise fiber inequality is not presumed.
For j=0,...,N-6 use I_j, and for the last j=N-5 use I_(N-6).
Every I is used at most twice.
Summing gives sum_j E Var_5,j<=2sum_a E Var_6,a.
Divide by their actual respective clocks N-4 and N-5 to get(15).
Each old legal transition belongs to one of these larger fibers and has positive conditional probability there.
The explicit initial-core transport has quotient change(t-1)t^(l+3), so it is not an old single-coordinate edge and witnesses strict enlargement.

The [C60 original midpoint energy](Yin_C_G0060_v1.md#statement) gives <Z_n,(Id-T_n)Z_n>>=C_star/[512(N-4)] in the two-real-coordinate convention of(1).
Equation(15) proves the lower bound in(16).

For the upper bound, a block entirely to the left of the midpoint has a fixed endpoint and hence a fixed contribution to Z_n; a block entirely to the right does not affect Z_n.
Only j=n-5,...,n-1 can contribute, exactly five valid six-digit intervals for n>=7.
In such a block put a=n-j in{1,2,3,4,5}.
For two conditional words, the change in Z_n is the neutral evaluation of their left digit differences.
Each difference has absolute value at most2, so its modulus is at most2a.
Because the FULL block endpoints agree, the same change is minus the right contribution and has modulus at most2(6-a).
Thus the conditional diameter is at most2min(a,6-a), for every arbitrary endpoint and outside word.
Taking half the mean squared distance of two independent conditional copies gives conditional variance at most2min(a,6-a)^2.
This is the exact two-neutral-coordinate elementary specialization of [C45's all-endpoint fiber bound](Yin_C_G0045_v1.md#statement), not an assumption of endpoint0 or zero conditional mean.
The five bounds sum to2(1+4+9+4+1)=38.
Averaging by N-5 proves the upper bound in(16).

The operator uses overlapping intervals as a normalized random update.
It does not add their lower covariance certificates without their clock weights, so it does not violate C45's disjoint-collection restriction or its mesoscopic barrier.
Equation(16) controls the update energy; it is not an upper bound on the entire original midpoint variance m_n.

<a id="six-digit-quantitative-gap-boundary"></a>
## 6. The remaining quantitative question is explicit

Define the actual global Rayleigh gap of S_n by

    lambda_6,n=inf_(Var_pi_n(g)>0)
           D_6,n(g)/Var_pi_n(g),

using real g; it lies in[0,1].
Apply it to the real and imaginary parts of the globally centered TRUE midpoint and add.
The consequence is

    lambda_6,n m_n<=D_6,n(Z_n)<=38/(N-5).              (17)

If some ADDITIONAL constant c>0 and n0 supplied lambda_6,n>=c/(N-5) for every n>=n0, then(17) would imply m_n<=38/c eventually.
The unchanged original-law tightness/critical-mean interface in C60 would then give its same finite-mean implication.
Neither such a gap lower bound nor global irreducibility is proved here.
Even a proof of irreducibility for each finite n would only supply a positive input-dependent gap and would not discharge this uniform bound.

Conversely, a supplied original diffusive lower value m_n>=epsilon n would force lambda_6,n<=38/[epsilon n(N-5)] at that n.
This is an UPPER gap price implied by variance growth, not a derivation of variance growth from a small gap.
The known C64/C68/C70 zero-gap or slow-pair arguments apply to their specified operators and remain correct; their exhibited closed components are not automatically components of the different S_n.
The path in Theorem1 proves that the C70 pair and zero lie in the SAME S_n component.
It says nothing about components disjoint from those paths, other frozen words, their total original mass, or a full spectral lower bound.

The free global refresh which resamples the entire returned word is not used.
Nor is any distribution changed to make a proposed path more likely.
The complete six-digit conditional laws are explicit finite fibers and preserve the original process.
The new progress is the verified richer local move, full annihilation path for every long core, exact original probabilities and nonzero-endpoint updates, with the actual update-energy scale(16).
The unresolved next step is a proof or refutation of a quantitative comparison for THIS enlarged operator or the midpoint-relevant component/observable, with the remaining original conditional means and masses paid.

<a id="six-digit-source-limits-and-author-check"></a>
## 7. Sources, exact scope and author checking

The original fixed input, full return law, quotient normalization and old one-site energy are accepted C60/C64 material.
The long-core identities, original midpoint and paid pair mass are accepted C70 material.
C68's invariant conclusion and C70's reflection conclusion are retained at their old operators; no correction to them is proposed.
C45 already treats every endpoint for its lower covariance certificate; the six-digit heat bath and transport/annihilation path are a different dynamical construction.
The bounded reuse screen found no retained version of this actual path or its complete fiber probabilities, without making a priority claim.

Classical finite heat-bath/Gibbs-sampler and Dirichlet naming is attributed through the existing LP17 account.
Its bounded acquisition exception and partial indexed-text observations remain explicit; no full book inspection, external mixing theorem or new source acceptance is claimed.
Detailed balance, projections, the three complete fibers, the path and every comparison used here are checked by finite local arguments.
Original source-proof limits of accepted inputs are unchanged.

The author checked every integer(a,b) fiber inequality, NONZERO transport/cap endpoints, original counts2/4/8/64 and all normalizers, both signs, all m>=1 including the first overlapping-end case, all n>=7 paddings and actual interval starts, every intermediate word/quotient and both terminal stages, exact path length and conditional event clock, original masses and disjoint paths, edge conductance and the factor1/2, actual complex midpoint norm and all five crossing intervals, equivalence of the old quotient partition with original five-digit conditioning, the averaged direction of nested conditional variance, both update clocks, and the distinction between energy, gap, chronological time and diffusive conclusions.
No native mathematical program, enumeration, J or new source acquisition was used.
The root supplied only the broad task, while the present author supplied all new formulas, path and estimates.
This is an author proof draft awaiting an actual whole noncontributor review, not an independent finding, adoption or G0001 completion.

<a id="six-digit-entire-author-freeze"></a>
## Entire-author freeze

Date: 2026-10-12T14:14.
Freeze the COMPLETE allocation/reuse/candidate history and Sections1--7/Theorems1--2/equations(1)--(17), including the exact all-n path, all original probabilities, paid path inequality, actual-midpoint energy bounds, precise conditional gap interface and source/access/contribution limits.
This is a complete AUTHOR proof draft for separate whole noncontributor review.
Its new operator is exactly the uniform six-original-digit arbitrary-endpoint heat bath(2); no global irreducibility or positive gap lower bound is included in the theorem.
The author supplied the new mathematics; root supplied the broad research question only.
The scoped check of this draft and actual C60/C70/C45 inputs returned checked4, and saved text is pure ASCII with no U+864F or replacement characters.
Those are structural/encoding checks, not independent proof review.
No native mathematical program, J, source acquisition, adoption or retirement was performed.
