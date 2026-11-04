---
author: Yin
---
# Nonzero invariant components of the true quartic midpoint and persistent update correlations

Date: 2026-10-12T12:30.
Human author Yin.
Internal fixed extraction under the continuing G0001 authorization.
The rounding-recovery agent authored the complete original20:11 D21 and now authors this exact statement/wrapper; it cannot independently review this extraction.
g0001_routes separately whole-reviewed the original proof in R286.
That original finding is support only, not a prospective wrapper review.
The ENTIRE original question, reuse/contribution history, safe checkpoint, proof/tables, source limits and freeze are retained below.
Initial status is proof draft / under review pending another actual extraction review.
No adoption or retirement is performed here.

## Statement

Fix the ACTUAL original Salem quartic

    P(t)=1-t-t^2-t^3+t^4,
    beta>1 its real root, zeta a unit-circle conjugate,
    u=zeta+zeta^-1=(1-sqrt13)/2, u^2=u+3, u<0.

For EVERY integer n>=5 put N=2n and L=2n-4.
Let Omega_n contain ALL original eta in{-1,0,1}^N with full field return F_eta(beta)=0, F_eta=sum_(j=0)^(N-1)eta_j t^j.
The complete original digit law remains1/4,1/2,1/4.
For the actual zero count z(eta), define

    W_n=sum_(eta in Omega_n)2^z(eta),
    Pr(original return at2n)=W_n/4^(2n),
    pi_n(eta)=2^z(eta)/W_n,
    Z_n(eta)=-zeta^-n sum_(j=0)^(n-1)eta_j zeta^j,
    E_pi_n Z_n=0, m_n=E_pi_n|Z_n|^2.

All original conjugate constraints and every prior zero visit remain.
Neutral norm uses exactly TWO unweighted real coordinates.
The unique integer quotient F_eta=P A_eta has L coefficients a_0,...,a_(L-1).
At one auxiliary UPDATE choose one j uniformly and resample a_j from its exact pi_n conditional law given all other quotient coordinates.
If K_j is that conditional expectation, put

    T_n=(1/L)sum_j K_j.

This is the actual C60 reversible self-adjoint positive contraction.
Its graph joins exactly all legal integer changes by a multiple of one shifted P.
Let Pi_n be conditional expectation given its ACTUAL connected component, and H_n=Pi_n Z_n.
Its range is ker(I-T_n); H_n is globally centered.
No componentwise zero-mean assumption is made.

**A. Explicit nonzero-midpoint frozen families at EVERY original length.**
Use the following three original coefficient blocks, with their recorded lengths10,13,18:

    F=(1,-1,0,-1,-1,-1,-1,0,-1,1),
    G=(1,-1,-1,0,-1,1,-1,1,-1,0,-1,-1,1),
    H=(1,-1,-1,0,-1,1,-1,1,-1,-1,1,-1,1,-1,0,-1,-1,1).

They are the accepted internally frozen P-multiple seeds, each with exactly two zeros, beginning(1,-1) and ending(-1,1).
Write n=5k+e, k>=1, e in{0,1,2,3,4}.
Form the following family F_n by choosing each block's global sign independently.
F^a in this table means a concatenated list of blocks, NOT a polynomial power, and F^0 is empty.
Zeros are added only at the two OUTER ends.

| Case | Ordered block list | Leading zeros | Trailing zeros | Number b of blocks | Added zeros s |
| --- | --- | --- | --- | --- | --- |
| e0,k odd | F^k | 0 | 0 | k | 0 |
| e0,k even | H,F^(k-2) | 1 | 1 | k-1 | 2 |
| e1 | F^k | 0 | 2 | k | 2 |
| e2 | G,F^(k-1) | 0 | 1 | k | 1 |
| e3 | G,F^(k-1) | 1 | 2 | k | 3 |
| e4 | H,F^(k-1) | 0 | 0 | k | 0 |

Every word has EXACT original length2n and is a nonzero frozen returned word.
There are exactly2^b DISTINCT words.
The midpoint always lies strictly inside a block; the exact common squared midpoint norm v_n of every family member is:

| Case | v_n |
| --- | --- |
| e0,k odd | 3-2u |
| e0,k even | 2-u if k2; otherwise1 |
| e1 | 1-u if k odd;1 if k even |
| e2 or e3 | 7-3u if k1;1 if k2;1-u if k>=3 odd;1 if k>=4 even |
| e4 | 2-u if k1 or k2;1 if k>=3 odd;1-u if k>=4 even |

Thus1<=|Z_n(eta)|^2=v_n<=7-3u on F_n.
The complete prefix positions, integer P quotients and hand autocorrelations are retained in the proof; no finite graph table is extrapolated.

**B. Exact original probability and nonzero invariant projection.**
Every family member has exactly2b+s zeros and unconditional original probability2^(2b+s)/4^(2n).
With A_n=2^(3b+s),

    Pr_original(F_n)=A_n/4^(2n),
    pi_n(F_n)=A_n/W_n,
    rho_n=v_n A_n/W_n>0.

For the six rows of the first table, A_n is respectively2^(3k),2^(3k-1),2^(3k+2),2^(3k+1),2^(3k+3),2^(3k).
Each family vertex is a singleton component, so H_n=Z_n there.
Consequently

    ||H_n||_(pi_n)^2>=rho_n
        >=2^(3floor(n/5)-1)/W_n
        >=2^(3floor(n/5)-1-4n)>0,
                              EVERY n>=5.

The first rho_n is the EXACT family contribution to the squared projection norm, not the value of the entire projection or a classification of all components.
The final bound uses W_n<=4^(2n).
Global sign symmetry pairs different singleton components with opposite means and does not imply zero means inside each component.

**C. Persistent stationary UPDATE correlations and averages.**
Fix n>=5 and start the auxiliary T_n chain X_t in the EXACT original return-conditioned law pi_n.
For every integer update time t>=0,

    R_n(t)=E[conj(Z_n(X_0)) Z_n(X_t)]
          =<Z_n,T_n^t Z_n>_(pi_n)
          >=||H_n||^2>=rho_n,
    lim_(t->infinity)R_n(t)=||H_n||^2>0.

These correlations are real and nonnegative and equal the sum of the two real-coordinate autocovariances.
The all-t lower bound uses positivity of T_n, not reversibility alone.
The fixed-n series sum_(t>=0)R_n(t) diverges.
For EVERY positive integer J the stationary update average is globally centered and satisfies

    E|J^-1 sum_(t=0)^(J-1)Z_n(X_t)|^2
      =J^-2[J R_n(0)+2 sum_(s=1)^(J-1)(J-s)R_n(s)]
      >=||H_n||^2>=rho_n.

The variable t counts replacements of a COMPLETE returned word; it is not original chronological time n.
No uniform-in-n convergence rate or interchange of these clocks is asserted.

**D. Failure on the midpoint-generated invariant space.**
The finite equation

    (I-T_n)g=Z_n

has NO complex-valued solution on Omega_n for every n>=5.
At least one of the two real-coordinate equations fails; both cannot be solved simultaneously.
Let

    V_n=span_R{T_n^j Re Z_n,T_n^j Im Z_n:j>=0}.

This finite-dimensional invariant space consists of globally centered functions and contains Re H_n and Im H_n.
At least one is nonzero, has positive variance and has zero Dirichlet energy.
Hence

    inf_(g in V_n,Var_pi_n g>0)
       <g,(I-T_n)g>/Var_pi_n g=0,
                              EVERY n>=5.

Thus restricting to the invariant space generated by the TRUE midpoint does not itself restore a positive comparison constant; the obstruction is not merely an unrelated frozen observable.

**E. Exact residual and scope limit.**
Orthogonality gives

    m_n=||H_n||^2+||Z_n-H_n||^2.

For each fixed n, the component-centered equation (I-T_n)g=Z_n-H_n DOES have a finite solution, obtained by division by1-lambda on the eigenspaces with lambda<1.
No uniform inverse bound, eigenvalue estimate, efficient algorithm or control of all component means is supplied.
A componentwise variance argument must separately estimate ||H_n||^2; declaring it zero is refuted by B.

The displayed family lies in a fixed neutral annulus and its conditional mass may be small.
Its coarse paid lower bound decays exponentially; it does not prove growing midpoint variance, a positive diffusive limsup, bounded total variance, a nonvanishing frozen proportion, an original chronological critical-mean branch or a Mahler gap.
No alternative dynamics, enlarged local moves, new graph enumeration or changed probability law is introduced.
The result concerns this exact fixed quartic, actual return law and auxiliary conditional-resampling operator, and leaves unrestricted G0001 unresolved.

## Current assessment
[Selected decision](#decision-independent-current-whole-review-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T12:30 |
| status | open |
| reason | Register the explicit all-n nonzero-midpoint frozen families, exact original mass and positive invariant projection, persistent stationary update correlations, insoluble uncentered equation and zero midpoint-generated comparison constant. Entire original20:11 D21 is retained. R286 whole-reviewed that original body only; the original D21 author also writes this wrapper, so a separate actual extraction review is required. No chronological diffusion/mean or unrestricted Task conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E for EVERY original n>=5 at the actual fixed quartic, full original unequal-probability law, explicit templates/probabilities and exact auxiliary-update/component boundaries. |
| argument | [Entire retained author account](#argument) | COMPLETE original20:11 D21 question/reuse/roles,20:02 safe checkpoint, Sections1--8/equations1--16, every prefix/autocorrelation/template/mass table, source limit, self-check and freeze. |
| dependency | [C60 complete original-law operator](Yin_C_G0060_v1.md#statement) | Exact integer quotient, original pi_n/midpoint, conditional-expectation K_j, uniform-site T_n and self-adjoint positive contraction. No parity-nonclosure or positive-gap premise is used. |
| dependency | [C64 exact seeds](Yin_C_G0064_v1.md#quartic-three-frozen-return-blocks) | ONLY F/G/H original digit arrays, exact integer P products and complete corrected local freezing certificate. No native graph counts or original all-n template is needed for the new midpoint placement. |
| dependency | [C64 safe concatenation and outer padding](Yin_C_G0064_v1.md#quartic-frozen-concatenation-and-padding) | Arbitrary independent seed signs, all crossing windows and at most two zeros per outer end; no unrestricted zero-padding principle. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0286_v1.md#quartic-invariant-midpoint-whole-independent-finding) | ENTIRE actual original20:11 D21 and precise accepted inputs. It does not inspect or adopt this new statement/wrapper. Referenced finding relationship: self-reviewed. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T12:43 |
| status | proved |
| reason | Adopt original whole R286 and separate actual extraction R386. The complete original-law frozen family gives a paid nonzero invariant component of the actual midpoint and the exact update-correlation/Poisson-equation obstruction. Centered residual solvability is fixed-n only; no chronological diffusion, uniform inverse estimate or unrestricted gap follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E for EVERY original n>=5 at the actual fixed quartic, full original unequal-probability law, explicit templates/probabilities and exact auxiliary-update/component boundaries. |
| argument | [Entire retained author account](#argument) | COMPLETE original20:11 D21 question/reuse/roles,20:02 safe checkpoint, Sections1--8/equations1--16, every prefix/autocorrelation/template/mass table, source limit, self-check and freeze. |
| dependency | [C60 complete original-law operator](Yin_C_G0060_v1.md#statement) | Exact integer quotient, original pi_n/midpoint, conditional-expectation K_j, uniform-site T_n and self-adjoint positive contraction. No parity-nonclosure or positive-gap premise is used. |
| dependency | [C64 exact seeds](Yin_C_G0064_v1.md#quartic-three-frozen-return-blocks) | ONLY F/G/H original digit arrays, exact integer P products and complete corrected local freezing certificate. No native graph counts or original all-n template is needed for the new midpoint placement. |
| dependency | [C64 safe concatenation and outer padding](Yin_C_G0064_v1.md#quartic-frozen-concatenation-and-padding) | Arbitrary independent seed signs, all crossing windows and at most two zeros per outer end; no unrestricted zero-padding principle. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0286_v1.md#quartic-invariant-midpoint-whole-independent-finding) | ENTIRE actual original20:11 D21 and precise accepted inputs. It does not inspect or adopt this new statement/wrapper. Referenced finding relationship: self-reviewed. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0794_v2.md#c68-invariant-midpoint-actual-extraction-finding) | Entire actual statement, complete retained original body and precise direct interfaces separately inspected after allocation, preserving earlier review scopes and corrections. Referenced finding relationship: unknown. |


### Decision independent-current-whole-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:10 |
| status | proved |
| reason | The current finding is SELF because its initial complete argument input included author-validation conclusions beyond the necessary derivation. Adopt the separately organized current fixed-target finding after complete statement and retained-argument inspection, including late extensions, actual costs, controls, necessary mathematical interfaces and source limits, while excluding credited comparison scopes first separately checked after old-review exposure. The initial mathematical conclusion was formed at 2026-10-22T22:44 UTC before old-target review comparison. The finding records the exact interface and later credited-comparison reading sequence. Preserve fixed mathematics, historical decisions, all non-review premises and their scopes; retain earlier findings in their original homes at their actual recorded relationships and checking scopes. This selects current review evidence and supplies no new research, Task completion or execution resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement: statement](#statement) | Entire A--E for EVERY original n>=5 at the actual fixed quartic, full original unequal-probability law, explicit templates/probabilities and exact auxiliary-update/component boundaries. |
| argument | [Argument: argument](#argument) | COMPLETE original20:11 D21 question/reuse/roles,20:02 safe checkpoint, Sections1--8/equations1--16, every prefix/autocorrelation/template/mass table, source limit, self-check and freeze. |
| dependency | [Dependency: statement](Yin_C_G0060_v1.md#statement) | Exact integer quotient, original pi_n/midpoint, conditional-expectation K_j, uniform-site T_n and self-adjoint positive contraction. No parity-nonclosure or positive-gap premise is used. |
| dependency | [Dependency: quartic-three-frozen-return-blocks](Yin_C_G0064_v1.md#quartic-three-frozen-return-blocks) | ONLY F/G/H original digit arrays, exact integer P products and complete corrected local freezing certificate. No native graph counts or original all-n template is needed for the new midpoint placement. |
| dependency | [Dependency: quartic-frozen-concatenation-and-padding](Yin_C_G0064_v1.md#quartic-frozen-concatenation-and-padding) | Arbitrary independent seed signs, all crossing windows and at most two zeros per outer end; no unrestricted zero-padding principle. |
| support | [Recorded original finding](../audits/reviews/Yin_R_G0286_v1.md#quartic-invariant-midpoint-whole-independent-finding) | ENTIRE actual original20:11 D21 and precise accepted inputs. It does not inspect or adopt this new statement/wrapper. Finding relationship: self-reviewed. |
| review | [Current finding](../audits/reviews/Yin_R_G0794_v2.md#g68-current-independent) | Complete current mathematical statement and retained proof, including all late extensions, paid arithmetic, useful controls and accepted necessary interfaces at their exact scopes; exclude post-initial credited comparison scopes identified by the finding; initial conclusion 2026-10-22T22:44 UTC, then old-finding comparison; actual interface and credited-comparison reading limits are disclosed in the finding. Finding relationship: self-reviewed. |

## Registration and complete preservation

The ENTIRE original20:11 D21 body follows unchanged except for representing duplicate front matter once, demoting its first title one level, and normalizing line endings/separating terminal whitespace.
All mathematical text, explicit anchors, formulas, tables, candidate/safe-checkpoint history, source/access limits, actual contributions and freeze are retained.
Existing relative links remain valid from the Claim directory.
A direct complete-body comparison accompanies this extraction; the original D21 remains until root separately performs any actual consumer maintenance and retirement.

C60's ordinary LP17 attribution retains its partial access and unavailable full-book artifact limits, as stated in the original body.
No new source-original theorem, complete-book inspection or native reproduction is asserted.
C64's accepted seed proof is reused at the specified narrow scope; J92's full graph outputs are not a premise for the new templates or spectral conclusions.
The extracting AI is the original author and cannot independently review this new wrapper.
R286 is original whole support only.
This operation makes no adoption or retirement and runs no mathematical native program.

2026-10-12T12:32 extraction check: direct comparison of the ENTIRE actual D21 source and retained body returned equality after only the stated normalization, with23,271 characters,243 lines and8 explicit anchors each.
The scoped C68/D21/R286 check passed with checked3.
This establishes preservation and structure, not an independent wrapper verdict.

## Argument

## Nonzero invariant midpoint components in the original quartic replacement dynamics

Date: 2026-10-12T12:02.
Human author Yin.
New AUTHOR inquiry under the continuing G0001 authorization.
Root supplied only the broad request to test a genuinely observable/component-sensitive escape from the global zero-gap obstruction.
The rounding-recovery author selects and develops every candidate formula here; root supplies no mathematical step and may later independently review it.
No native mathematical program, source acquisition or new execution allowance is planned.
This new draft does not alter the original frozen-word proof, its experiment or C64's scope.

## Selected question and bounded reuse

The actual [C60 operator](Yin_C_G0060_v1.md#statement) preserves the complete original returned law but has the [C64 all-n frozen-word obstruction](Yin_C_G0064_v1.md#statement).
Both current selections are adopted.
A tempting observable-specific escape is that global sign symmetry might nevertheless make the TRUE neutral midpoint have mean zero on every connected component, allowing a componentwise inversion or positive bound on the invariant subspace generated by that observable.
This draft tests that precise assertion, rather than repeating an abstract total-variance identity or calling a small gap diffusion.

The author read the full actual C60 and C64 inputs and the earlier D15 seed/padding proof, of which this author was a contributor.
The new contribution is a DIFFERENT placement of those established seeds so that every n>=5 has positive original probability of an isolated word with a NONZERO chronological midpoint, together with exact prefix norms and a quantitative invariant-component obstruction.
No new seed search or enlarged graph table is used.
A bounded local search for component means, invariant midpoint, persistent correlation and a midpoint linear-equation obstruction was performed in current G Claims/ledgers; no matching current theorem was located.
This bounded reuse check is not a novelty claim.
The original-law/full-field/midpoint and auxiliary-update clocks stay distinct.

## Intended discriminating outcome

For every n>=5, construct an explicit finite family F_n of frozen original return words, each with |Z_n|^2>=1, and retain its exact original mass.
If Pi_n denotes orthogonal projection onto functions constant on the ACTUAL connected components and H_n=Pi_n Z_n, then F_n would give ||H_n||^2>0.
The target is an explicit paid lower bound on this fixed-space projection, on stationary UPDATE-time midpoint correlations and on update-time averages, and a proof that the finite equation (I-T_n)g=Z_n has no solution.
No implication to original chronological diffusion, bounded midpoint variance, critical-mean branch or unrestricted Mahler gap is proposed.
All substantive calculations continue below.

<a id="quartic-invariant-midpoint-domain"></a>
## 1. Actual law, operator and component projection

Fix P(t)=1-t-t^2-t^3+t^4, its original real root beta>1 and neutral conjugate zeta on the unit circle.
Put

    u=zeta+zeta^-1=(1-sqrt13)/2, u^2=u+3, u<0.

For n>=5 let Omega_n be ALL eta in{-1,0,1}^(2n) whose original polynomial F_eta(beta)=0.
Every such word has the unique integer quotient F_eta=P A_eta, with L=2n-4 coefficients a_0,...,a_(L-1).
Keep the ORIGINAL digit probabilities1/4,1/2,1/4 and all conjugate returns.
With z(eta) the zero count,

    W_n=sum_(eta in Omega_n)2^z(eta),
    p_(2n)=W_n/4^(2n), pi_n(eta)=2^z(eta)/W_n,
    Z_n(eta)=-zeta^-n sum_(j=0)^(n-1)eta_j zeta^j.
                                                            (1)

Sign reversal preserves pi_n and changes Z_n to-Z_n, so E_pi_n Z_n=0.
No uniform returned-word law or selected finite endpoint box is substituted.

At each UPDATE choose one quotient site uniformly and resample it from its exact pi_n conditional law.
If K_j is this conditional expectation then T_n=(1/L)sum_j K_j.
These are the actual C60 operators.
For completeness, every K_j is an orthogonal conditional-expectation projection in the finite space L2(pi_n); it is self-adjoint, positive semidefinite and preserves pi_n.
Thus T_n is a self-adjoint positive contraction with all eigenvalues in[0,1].
Every allowed value of the selected coordinate has positive conditional probability.
The underlying undirected graph therefore joins EXACTLY all legal changes by an integer multiple of a single shifted P.

Let C_n(eta) denote its ACTUAL connected component, and let Pi_n be conditional expectation given C_n.
Its range consists of component-constant functions.
This range equals ker(I-T_n): the identity

    <g,(I-T_n)g>=(1/L)sum_j E_pi_n Var(g | a_-j)

is nonnegative, and it vanishes precisely when g is constant on every legal resampling fiber, hence on every graph component.
The reverse implication is immediate.
Consequently

    H_n=Pi_n Z_n

is the orthogonal fixed-space part of the TRUE midpoint, globally centered but not assumed centered component by component.
The following explicit construction, not this generic projection identity alone, decides whether H_n vanishes.

<a id="quartic-nonzero-midpoint-seeds"></a>
## 2. Existing frozen seeds and their original values

Reuse the three C64 blocks, with ascending original digits and actual lengths10,13,18:

    F=(1,-1,0,-1,-1,-1,-1,0,-1,1),
    G=(1,-1,-1,0,-1,1,-1,1,-1,0,-1,-1,1),
    H=(1,-1,-1,0,-1,1,-1,1,-1,-1,1,-1,1,-1,0,-1,-1,1).
                                                            (2)

Their exact original integer quotients, also rechecked by multiplication, are

    F=P(1+t^2+t^3+t^5),
    G=P(1+t^3-t^4+t^5+t^8),
    H=P(1+t^3-t^4+t^5+t^8-t^9+t^10+t^13).
                                                            (3)

Each block has exactly two zero digits, is palindromic, starts(1,-1), ends(-1,1) and is internally frozen.
The exact criterion is that every five-digit window has both+1 and-1 among p_r eta_(j+r), where p=(1,-1,-1,-1,1).
It tests ALL possible integer changes, because their legal interval is -1-min_r(p_r eta_(j+r))<=delta<=1-max_r(p_r eta_(j+r)).
The complete corrected29-cell certificate in C64 proves the internal assertion.
This is a credited accepted seed fact, not another claimed new enumeration.

Independent sign choices on successive blocks and their concatenation preserve return and freezing.
The four seam windows see two opposite nonzero digits at positions(1,2) or(2,3), where the P multipliers are both-1.
Adding at most two zeros at EACH OUTER end creates only the same two signed positions, so remains frozen; arbitrary padding is not allowed.
These are precisely the accepted C64 concatenation/padding operations.
Every resulting original word remains a full P-multiple in the original field, with no missing conjugate or changed digit law.

The original C64 templates sometimes put the midpoint BETWEEN whole return blocks, giving Z_n=0.
The next sections instead choose explicit placements for all five residue classes and both parity cases of floor(n/5), and evaluate every possible cut.
This is the actual changed mathematical obligation; the old existence of frozen words alone does not prove it.

## Current safe checkpoint

2026-10-12T12:02.
The new question, exact full-law/operator interface and reused seed mechanism are saved directly in this responsible draft.
The following planned construction, exact midpoint norm table and fixed-space/correlation conclusions are NOT yet an adopted theorem or a frozen full proof.
The author will continue after the separately assigned C65 extraction review; no new native run is needed.


<a id="quartic-frozen-prefix-exact-norms"></a>
## 3. Exact nonzero prefix norms at every cut that will be used

For a block B of length ell_B from(2), define its neutral prefix

    A_(B,s)=sum_(j=0)^(s-1) B_j zeta^j,
                     0<=s<=ell_B.

Every block is palindromic and its full value is zero at zeta.
Its suffix of length ell_B-s is the reverse of its prefix of that length.
Since |zeta|=1, these facts give

    |A_(B,s)|^2=|A_(B,ell_B-s)|^2.                 (4)

Indeed the full-return identity makes prefix and suffix sums opposite, up to the suffix's unit phase; reversing a real coefficient string on the circle also changes only a unit phase and complex conjugation.
No modulus comparison between different embeddings is used.

Here are ALL prefix positions that occur in the construction below, with exact squared norms:

| Block | Prefix length s | Squared neutral norm |
| --- | --- | --- |
| F | 1 or9 | 1 |
| F | 4 or6 | 1-u |
| F | 5 | 3-2u |
| G | 7 | 7-3u |
| G | 12 | 1 |
| H | 9 or14 | 2-u |
                                                            (5)

For a direct hand verification set C_j=zeta^j+zeta^-j.
The recurrence C_(j+1)=u C_j-C_(j-1), C_0=2,C_1=u, and u^2=u+3 give

    C_2=u+1, C_3=u+3, C_4=3u+2, C_5=4u+6,
    C_6=7u+10, C_7=13u+15, C_8=21u+29.

If a finite real coefficient string has autocorrelations c_j=sum_i a_i a_(i+j), its squared value at zeta is c_0+sum_(j>=1)c_j C_j.
The following short COMPLETE autocorrelation lists, including zero entries, prove every nonsymmetric case needed:

| Prefix | Coefficients | (c_0,c_1,...), through its last possible lag |
| --- | --- | --- |
| F,4 | (1,-1,0,-1) | (3,-1,1,-1) |
| F,5 | (1,-1,0,-1,-1) | (4,0,1,0,-1) |
| G,6 | (1,-1,-1,0,-1,1) | (5,-1,0,0,-2,1) |
| H,4 | (1,-1,-1,0) | (3,0,-1,0) |
| H,9 | (1,-1,-1,0,-1,1,-1,1,-1) | (8,-4,3,-2,0,1,-1,2,-1) |

For example the last row gives8-4C_1+3C_2-2C_3+C_5-C_6+2C_7-C_8=2-u.
The G,6 row gives5-C_1-2C_4+C_5=7-3u.
Symmetry(4) supplies F,6; F,9; G,7; G,12 and H,14.
Prefix length1 is the coefficient1.
Thus every entry of(5) is verified without a numerical root or program.
Since u<0, all these squared norms are at least1 and at most7-3u.

<a id="quartic-all-n-nonzero-midpoint-frozen-family"></a>
## 4. Every n has a frozen family whose TRUE midpoint is nonzero

Write n=5k+e with k>=1 and e in{0,1,2,3,4}.
In the following table each block independently takes either sign.
F^a denotes a consecutive list of a blocks, not a polynomial power; a0 means an empty list.
Zeros are added only at the two OUTER ends.
Let b be the number of blocks and s the total number of added zeros.

| Case | Ordered block list | Leading zeros | Trailing zeros | b | s |
| --- | --- | --- | --- | --- | --- |
| e0,k odd | F^k | 0 | 0 | k | 0 |
| e0,k even | H,F^(k-2) | 1 | 1 | k-1 | 2 |
| e1 | F^k | 0 | 2 | k | 2 |
| e2 | G,F^(k-1) | 0 | 1 | k | 1 |
| e3 | G,F^(k-1) | 1 | 2 | k | 3 |
| e4 | H,F^(k-1) | 0 | 0 | k | 0 |
                                                            (6)

Call the resulting set F_n.
In the second row k is even and at least2, so no negative block count occurs.
Its total length is18+10(k-2)+2=10k.
The other lengths are respectively10k,10k+2,13+10(k-1)+1=10k+4,13+10(k-1)+3=10k+6, and18+10(k-1)=10k+8.
Thus EVERY row has exactly the original length2n, with no surrogate clock.

Every outer padding is within the safe two-per-end range of Section2.
Each sign choice is therefore a legal returned frozen word.
The boundaries are fixed and each block starts with its chosen sign, so all2^b choices are DISTINCT.
No representative, conjugate or original zero-digit probability is removed.

The midpoint is located after the first n ORIGINAL coefficients.
Remove the leading padding count and completed blocks before the cut.
The remaining prefix position is exactly as follows:

| Case in(6) | Block cut and prefix length |
| --- | --- |
| e0,k odd | F,5 |
| e0,k even | H,9 if k2; otherwise F,1 |
| e1 | F,6 if k odd; F,1 if k even |
| e2 or e3 | G,7 if k1; G,12 if k2; F,4 if k>=3 odd; F,9 if k>=4 even |
| e4 | H,9 if k1; H,14 if k2; F,1 if k>=3 odd; F,6 if k>=4 even |
                                                            (7)

To check all larger-k cases explicitly: the second row leaves5k-1-18=5k-19 after H, congruent1 modulo10 for even k>=4.
The e1 row cuts F^k at5k+1, with residues6 or1.
The e2/e3 rows both reach block-list position5k+2 after removing leading zeros; beyond G the residual is5k-11, congruent4 for odd k and9 for even k.
The e4 residual after H is5k-14, congruent1 or6.
The displayed k1/k2 cases are obtained before passing the initial longer block.
Every residual is strictly inside an existing block.
The k1 and k2 cases cover n5 through14 and require no finite native verification.

All whole blocks below the cut have value zero at EVERY original root.
In particular their contributions at zeta vanish.
Hence the actual Z_n is, up to one unit phase and the sign of the cut block, just A_(B,s_cut) from(7).
Formula(5) gives one number v_n, independent of all block signs, such that

    |Z_n(eta)|^2=v_n for EVERY eta in F_n,
    1<=v_n<=7-3u.                                 (8)

The exact v_n is obtained by the two tables; no untested all-n pattern is inferred from J92.
Unlike the original C64 templates, these templates ALWAYS cut a nonzero prefix.
They do not create a large-radius family: all of these midpoints remain in a fixed neutral annulus.

<a id="quartic-invariant-midpoint-paid-lower-bound"></a>
## 5. Exact original mass and a positive fixed-space projection

Each word of F_n has exactly2b+s zeros, since each seed has two and block supports do not overlap.
Its original unconditional probability is2^(2b+s)/4^(2n).
There are exactly2^b words, so with

    A_n=2^(3b+s)

the EXACT family probabilities are

    Pr_original(F_n)=A_n/4^(2n),
    pi_n(F_n)=A_n/W_n.                             (9)

For the six rows of(6), A_n is respectively2^(3k),2^(3k-1),2^(3k+2),2^(3k+1),2^(3k+3),2^(3k).
Thus A_n>=2^(3k-1).
These formulas retain the complete return normalizer W_n; replacing it by the number of words, a selected fiber or a free probability would be incorrect.

Each word of F_n is a singleton component.
Therefore H_n(eta)=Z_n(eta) on that entire family, and(8)--(9) imply

    ||H_n||_(pi_n)^2
       >=rho_n:=v_n A_n/W_n
       >=2^(3floor(n/5)-1)/W_n>0,
                         EVERY n>=5.              (10)

Here rho_n is the EXACT contribution of F_n to the squared projection norm, not a claim to compute the whole projection norm or all components.
Since the integer weights of ALL ternary length2n words sum to4^(2n), one also has W_n<=4^(2n) and the entirely explicit weaker bound

    ||H_n||^2>=2^(3floor(n/5)-1-4n).               (11)

The full global mean of H_n is zero, inherited from Z_n.
This does not contradict(10): global sign reversal pairs distinct singleton components with opposite nonzero means.
It never implied a zero mean within each component.
The new quantitative conclusion refutes that componentwise-centering assertion for EVERY actual n>=5.

<a id="quartic-persistent-update-correlation-obstruction"></a>
## 6. Actual stationary update correlations and the finite linear equation

Fix any n>=5 and start the auxiliary T_n chain X_t at its EXACT pi_n stationary law.
The index t counts local REPLACEMENT UPDATES, whereas n is the original chronological midpoint length.
Define

    R_n(t)=E[conj(Z_n(X_0)) Z_n(X_t)]
          =<Z_n,T_n^t Z_n>_(pi_n), t=0,1,2,... .

Because T_n is a finite self-adjoint positive contraction, orthogonal diagonalization splits Z_n into its fixed part H_n and eigencomponents with0<=lambda<1.
Thus the displayed correlation is real and nonnegative, is the sum of the two real-coordinate autocovariances, and satisfies

    R_n(t)>=||H_n||^2>=rho_n for EVERY t>=0,
    lim_(t->infinity)R_n(t)=||H_n||^2>=rho_n>0.
                                                            (12)

Positivity of T_n, supplied by its exact conditional-expectation construction, is used for the ALL-t lower bound; reversibility alone would not exclude negative eigenvalues.
The limit uses only finite spectral decomposition, with n fixed, and asserts no uniform-in-n rate.
In particular sum_(t>=0)R_n(t) diverges for EACH fixed n>=5 despite the globally zero observable mean.

For every positive integer J, the stationary update average has mean zero and

    E|J^-1 sum_(t=0)^(J-1) Z_n(X_t)|^2
       =J^-2[J R_n(0)+2 sum_(s=1)^(J-1)(J-s)R_n(s)]
       >=||H_n||^2>=rho_n.                        (13)

The coefficient sum in brackets is J+2 sum_(s=1)^(J-1)(J-s)=J^2.
This is an exact stationary-law calculation, not an assumption of independent updates.
Averaging updates therefore cannot erase the actual component mean.
It says nothing about averaging over different original chronological lengths.

The finite linear equation

    (I-T_n)g=Z_n                                  (14)

has NO complex-valued solution on Omega_n.
Indeed Pi_n(I-T_n)=0, while Pi_n Z_n=H_n!=0 by(10).
Equivalently its inner product with H_n gives0=||H_n||^2, a contradiction.
At least one of the two real-coordinate equations fails as well; both cannot be solved simultaneously.
Every function here is automatically square integrable because the state set is finite and pi_n is strictly positive.

This obstruction remains even after restricting attention to the observable-generated real space

    V_n=span_R{T_n^j Re Z_n,T_n^j Im Z_n:j>=0}.

It is finite dimensional and consists of globally mean-zero functions.
The limits of T_n^j Re Z_n and T_n^j Im Z_n are respectively Re H_n and Im H_n, so both belong to V_n, which is a closed finite-dimensional subspace.
At least one is nonzero.
It has positive variance and zero Dirichlet energy, proving the precise restricted obstruction

    inf_(g in V_n,Var_pi_n g>0)
        <g,(I-T_n)g>/Var_pi_n g=0,
                         EVERY n>=5.              (15)

Thus ignoring all observables unrelated to the true midpoint does not by itself restore a positive comparison constant for this dynamics.
This is stronger than invoking an unspecified slow mode: the obstruction lies in the invariant space actually generated by the two midpoint coordinates and has the explicit original-probability contribution(10).

<a id="quartic-component-centering-limits"></a>
## 7. What a componentwise replacement would still have to control

There is a precise finite residual after subtracting the ACTUAL component means.
Orthogonality gives

    m_n=||Z_n||^2=||H_n||^2+||Z_n-H_n||^2.         (16)

The equation (I-T_n)g=Z_n-H_n DOES have a solution for each fixed n: on each eigencomponent with lambda<1, divide the corresponding coefficient by1-lambda and take zero on the fixed space.
This is a finite algebraic existence argument, not a bound on the solution or an algorithm with a uniform numerical cost.
No estimate on the nontrivial eigenvalues, on the whole component means or on the second term of(16) is supplied.

Any useful componentwise variance comparison must therefore separately price ||H_n||^2; declaring it zero from global symmetry is false by(10).
The new lower bound does not make that term grow with n.
The explicit family's squared midpoints are bounded by7-3u, and its original conditional mass may be small.
The lower bound(11) decays exponentially and is a paid obstruction, not a diffusive lower bound or a nonvanishing stationary proportion.
No upper bound on the actual total m_n, no growing lower bound, no original critical-mean decision and no uniform Mahler conclusion follows.

No alternative chain, enlarged local move set, irreducibility assertion, changed digit law or new native graph domain is introduced.
The result identifies a concrete failed observable-specific escape from the all-n frozen-word mechanism: for this EXACT original-law operator, the actual midpoint itself has a nonzero fixed component at every n>=5, with fully paid probabilities and persistent update correlations.
A different successful route would need a genuinely new estimate of the component contribution or a different explicitly justified dynamics; neither is presumed here.

<a id="quartic-invariant-midpoint-entire-author-freeze"></a>
## 8. Complete author check, source scope and frozen handoff

2026-10-12T12:11.
The author checked the actual current adopted C60/C64 interfaces, complete original digit and quotient law, all field returns and neutral normalization; the inherited corrected seed certificate and exact safe concatenation/padding operations; all three displayed integer P products, palindrome reversal on the unit circle, every coefficient of the five autocorrelation rows and C_2 through C_8 reductions; all six length templates, every k1/k2 endpoint and odd/even cut residue; distinctness and sign count, total zero counts, unconditional probability and the full W_n denominator; singleton component means and nonzero global-centered projection; finite self-adjoint positivity, the all-update-time bound and fixed-n limit, exact time-average covariance coefficients, finite linear-equation obstruction and the closed observable-generated subspace; the component-centered residual solution and the absence of any uniform inverse estimate, variance-growth or chronological-mean inference.
These are author checks, not independent review.

The C60 operator retains its classical conditional-resampling/Dirichlet naming and the exact [LP17 partial attribution account](../audits/literature/LP17/readme.md#finite-conditional-resampling-attribution).
Its unavailable full-book artifact and limited indexed passage inspection are not promoted to full source coverage here.
This author did not acquire or render a new source.
The new fixed-space and correlation consequences use explicitly given finite conditional expectations and elementary finite-dimensional orthogonal diagonalization; no external mixing, gap, convergence-rate or original-source theorem is imported.
The seed facts are credited to C64, and the new templates/prefix calculations and original-probability obstruction are proved directly above.
No novelty or priority is asserted.

The rounding-recovery agent is the sole substantive author of this new mathematics under human Yin.
Root supplied only the broad task and execution coordination, not the candidate, formulas, proof steps or corrections.
Earlier author/reviewer relationships at C60/C64 remain disclosed antecedent work and do not independently review D21.
The intervening R284 v1 review of unrelated C65 was a separate noncontributor activity; it supplies no mathematical input here.

Freeze the ENTIRE actual D21: allocation/reuse/question, Sections1--8/equations(1)--(16), original20:02 safe-checkpoint history, every table, source/contribution boundary and all stated limits.
Whole noncontributor review must inspect this complete actual body before any adoption; no fixed C or independent acceptance is asserted here.
No new mathematical native run, new J or altered J92 output occurred.
The scoped material check before this freeze passed with checked1 and is repeated on the complete body; it verifies structure only.
