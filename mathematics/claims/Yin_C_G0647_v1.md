---
author: Yin
---

# Same-time original tail-count lower bounds and subexponential sign-flow load

The declared analytic question is whether actual finite reaching/continuation words give lower counts on every intermediate label of the current C623/C625 routes, with their full original time and probability cost.
Contributor original_law develops the following quantitative comparison; root selected the missing original-count/congestion problem and required the complete current-length and short-refresh accounting.
C519's fixed-word injection and cubic conductance cancellation are reused, not claimed as new general mechanisms.
The new application is to a growing family of actual routes carrying the ENTIRE C625 square-root event, with complete original mass at least1/32 at every sufficiently large n.
No finite scan or new J is used.

## Statement

Fix P(t)=t^4-t^3-t^2-t+1, its exterior root beta, neutral conjugate zeta and actual order O=Z[beta].
The chronological original kernel K_orig is restricted to its actual zero-to-zero core D: a transition staying in D has probability1/2 for digit0 and1/4 for digit+1 or-1; exits are killed.
For m>=0 write nu_m(x) for the COMPLETE original m-digit endpoint probability, p_m=nu_m(0), p_0=1, and c_m(x)=4^m nu_m(x).
The integer word weight is w(V)=2^(number of zero digits in V), including the empty word.
The separate current returned-word kernel at n>=5 is K_n=(H_A+H_C)/2 on ALL length-2n original returned words eta=(A,theta,C), with tail length k=n-2 and middle length4.
Here H_A and H_C are the complete original conditional resampling kernels given the entire left or right tail.
Its law is pi_n(eta)=w(A)w(theta)w(C)/Z_n, where Z_n=c_(2n)(0), and S eta=-eta.
Use the actual positive current labels e=(y,c), y=-beta^-k A(beta), c=C(beta), with unique middle word theta_e satisfying theta_e(beta)=y-beta^4c.
Put

    alpha_k(y)=c_k(-beta^k y)/c_k(0),
    beta_k(c)=c_k(c)/c_k(0),
    t_k=c_k(0)^2/Z_n,
    p_e=t_k alpha_k(y) beta_k(c) w(theta_e),
    r_y=sum_(e:y(e)=y)p_e, s_c=sum_(e:c(e)=c)p_e,
    Kbar_n(e,e')=1_(y=y')p_(e')/(2r_y)
                        +1_(c=c')p_(e')/(2s_c),
    Qbar_n({e,e'})=p_e Kbar_n(e,e'),
    D_n=p_(2n)/p_n^2.

Every row and column includes ALL original positive labels, including labels outside the chosen routes.
For any finite label collection whose left labels have actual continuation words y->0 of length at most an integer T and whose right labels have actual reaching words0->c of length at most T, if k>=T>=0 then

    4^-T<=alpha_k(y),beta_k(c)<=1.                         (1)

Every positive nonloop label edge with both ends in this collection obeys the SAME-CURRENT-LENGTH bound

    Qbar_n>=4^(-3T)/(131072 D_n).                          (2)

A zero-middle source label in the collection has original half-kernel holding probabilities

    q_A(e)=p_e/(2r_y)>=4^-T/32,
    q_C(e)=p_e/(2s_c)>=4^-T/32.                            (3)

No time shift has been suppressed in (1): a fixed word of length ell<=T is concatenated with ALL remaining k-ell returns, its probability at least4^-ell is paid, and actual monotonicity p_(k-ell)>=p_k is used.

All logarithms below are natural.
For the application use C623/C625's fixed accepted A_D,B_D>0 and exact constants

    g1=beta^-3(beta-1),
    C_neu=(1+2/|Im zeta|)/|g1(zeta)|,
    P0=130909, G=16P0+55,
    A_rad=2C_neu, B_rad=24+2sqrt(13)(P0+2),
    A_len=G*C_neu/sqrt(13), B_len=5G/sqrt(13)+26,
    U=2A_D A_rad sqrt(log128), W=A_D B_rad+B_D,
    N_sqrt=max{5,ceil(((U+sqrt(U^2+4(W+2)))/2)^2)}.

For EVERY integer n>=N_sqrt put

    r_n=2sqrt(n log128),
    R_n=A_rad r_n+B_rad,
    T_n=max{3,ceil(A_D R_n+B_D)},
    L_n=ceil(4A_len sqrt(n log128)+2B_len).

One has T_n<=n-2=k and L_n>=7.
Let M_n be the COMPLETE set of current labels with theta_e=0 and rho(c)=|c(zeta)|<=r_n, and let A_n be the union of all their complete original word fibers.
No matching trim is applied.
Its actual original mass satisfies

    delta_n=pi_n(A_n)=16/Z_n
       sum_((beta^4c,c) in M_n)c_k(-beta^(k+4)c)c_k(c)
        >=1/32.                                         (4)

There are randomized positive K_n paths gamma_eta from EVERY selected eta to its own full negative S eta, at that SAME n, with actual FULL-WORD length at most L_n.
For unordered original nonloop edges q, set Q_n(q)=pi_n(u)K_n(u,v) and define the complete directed-source load

    Lambda_n=max_q Q_n(q)^-1
         sum_eta pi_n(eta)1_(A_n)(eta) E[length(gamma_eta)N_q].

The construction pays the separate components

    Lambda_interlabel<=131072 D_n 4^(3T_n)L_n^2,
    Lambda_short_refresh<=896*4^T_n,
    Lambda_n<=131072 D_n 4^(3T_n)L_n^2
             <=131072 G_n 4^(3T_n)L_n^2.                 (5)

Here G_n is the fully original C645 bound

    B=1/(beta-1), S_real=beta B, kappa=1/|1-zeta^2|,
    h_n=n/2+kappa,
    G_n=1+4sqrt(pi B S_real h_n)+16B S_real h_n,
    C_star=G_1, D_n<=G_n<=C_star n.

Every use of G_n in (5) follows AFTER the independently proved conductance lower bound (2); no endpoint lower bound is inferred from C645's upper profile.
For explicit fixed constants put

    C_T=max{3,W+1},
    L_star=4A_len sqrt(log128)+2B_len+1,
    C_flow=131072 C_star 4^(3C_T)L_star^2,
    c_flow=3U log4.

Then EVERY n>=N_sqrt satisfies the fully paid subexponential estimate

    Lambda_n<=C_flow n^2 exp(c_flow sqrt(n)).              (6)

Consequently, for every real or complex odd function f on the full original word space,

    sum_(eta in A_n)pi_n(eta)|f(eta)|^2
       <=(Lambda_n/4) sum_q Q_n(q)|f(u_q)-f(v_q)|^2.       (7)

At the digit-work clock the load in BOTH expressions (5) and in (6) is multiplied by n+2, and the energy in (7) is divided by n+2.
The paths have at most L_n auxiliary updates and at most(n+2)L_n units in the declared digit-work clock; the short-path refreshes have been included in these actual full-word length bounds.
The result is an all-late positive-mass, same-current-length comparison with a generally growing coefficient.
It proves no uniform load, actual critical-mean branch, unrestricted spectral gap or Lehmer conclusion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision growing-route-paid-load-registration

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:04 |
| status | open |
| reason | Register the complete actual same-time lower-tail-count and full-row conductance comparison on the growing C623/C625 route family, covering the entire original square-root event of mass at least 1/32. The long/short lifts retain the exact full negative word and actual full length at most L_n; both load expressions and the O(n^2 exp(c sqrt(n))) consequence pay every original word, normalizer and clock cost. The coefficient remains nonuniform and no mean branch or final Task conclusion is supplied; fresh whole review remains pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact growing-route theorem](#statement) | Complete fixed-quartic original digit/count law, same k>=T injection, all full label marginals, cubic conductance and holding constants, every n>=N_sqrt, all intermediate endpoint coverage, entire mass1/32 selection, exact negative full word, actual full lengths, both paid load bounds, explicit subexponential constants, odd complex energy and digit-work scope. |
| argument | [Complete six-section proof](#argument) | Sections 1--6 and formulas 1--13, exact reuse, actual legal-word injections with remaining returns and monotonicity, complete row/column weight256 and factor131072, current T_n onset, compression without a congestion claim, short-refresh price896 and true length bound, D_n/G_n substitution only after a lower-conductance proof, all constants and limitations. |
| support | [Existing complete fixed-word injection](Yin_C_G0519_v1.md#seed-complete-count-comparison) | Existing actual word plus complete remaining-return mechanism, reused with the explicit growing witness length T_n rather than a new fixed-seed or free-padding claim. |
| support | [Existing cubic count cancellation](Yin_C_G0519_v1.md#seed-original-conductance) | Existing full-neighbor denominator and cubic count mechanism; its old fixed-hub mass and reflected-kernel scope are not substituted for the present full label chain. |
| dependency | [Original return monotonicity](Yin_C_G0169_v1.md#endpoint-collision-monotonicity) | Complete binary-difference law gives p_(k-ell)>=p_k and p_k>=p_n with all lengths and empty-return cases retained. |
| dependency | [Every actual intermediate route label](Yin_C_G0623_v1.md#whole-z0-finite-route) | Both left/right zero-middle and excursion labels lie in the strict actual core, have radius below R(c), and admit actual reaching/continuation words of length at most A_D R(c)+B_D; same current-n paths and sign reversal retain these bounds. |
| dependency | [Paid affine route radius](Yin_C_G0625_v1.md#neutral-coordinate-affine-onset) | Actual R(c)<=A_rad rho(c)+B_rad and inherited length constants, with both trace coefficients and original neutral embedding paid. |
| dependency | [Exact current square-root event](Yin_C_G0625_v1.md#statement) | Full original mass1/32, exact N_sqrt and L_n, same-current-length sign paths, all original tail representations and complete return normalizer. |
| dependency | [Complete original label law](Yin_C_G0627_v2.md#conditional-lift-exact-reuse) | Exact conditional product fibers, all full row/column masses and original half-kernel conductances; no uniform graph probability. |
| dependency | [Paid short-path lift](Yin_C_G0627_v2.md#full-negative-word-randomized-lift) | Original four-refresh construction on ell<4, exact source-terminal correlation and complete unordered-edge load accounting. |
| dependency | [Exact long lift and mixed path formula](Yin_C_G0631_v1.md#alternating-shortening-and-short-path-scope) | Clique compression preserves vertices/current support, exact long alternating lift and fully paid mixed-length numerator and short refresh formula; no compression-congestion monotonicity or unrestricted zero-length lift. |
| dependency | [Original linear overlap bound](Yin_C_G0645_v1.md#gaussian-core-sum-linear-overlap) | Actual D_n<=G_n<=C_star n used only after deriving the current conductance lower bound and upper load; no lower count inferred from an upper endpoint profile. |
| dependency | [Original odd sign-flow inequality](Yin_C_G0602_v2.md#partial-sign-flow-original-law) | Full sign-symmetric subprobability, randomized actual length-times-traversal load, exact Lambda/4 coefficient for real or complex odd functions and digit-work conversion. |


### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:16 |
| status | proved |
| reason | Adopt the entire same-current-time count and growing-route theorem after main reading of complete C647 and isolated whole R855. All actual word injections, complete marginal weights, intermediate endpoint onsets, source mass at least1/32, full negative-word lifts and short refreshes are paid. Both D_n and G_n load bounds and the explicit C_flow n^2 exp(c_flow sqrt(n)) consequence retain actual full lengths and all n+2 digit-work costs. The growing coefficient gives no uniform load, critical-mean branch, spectral gap or unrestricted Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact growing-route theorem](#statement) | Complete fixed-quartic original digit/count law, same k>=T injection, all full label marginals, cubic conductance and holding constants, every n>=N_sqrt, all intermediate endpoint coverage, entire mass1/32 selection, exact negative full word, actual full lengths, both paid load bounds, explicit subexponential constants, odd complex energy and digit-work scope. |
| argument | [Complete six-section proof](#argument) | Sections 1--6 and formulas 1--13, exact reuse, actual legal-word injections with remaining returns and monotonicity, complete row/column weight256 and factor131072, current T_n onset, compression without a congestion claim, short-refresh price896 and true length bound, D_n/G_n substitution only after a lower-conductance proof, all constants and limitations. |
| support | [Existing complete fixed-word injection](Yin_C_G0519_v1.md#seed-complete-count-comparison) | Existing actual word plus complete remaining-return mechanism, reused with the explicit growing witness length T_n rather than a new fixed-seed or free-padding claim. |
| support | [Existing cubic count cancellation](Yin_C_G0519_v1.md#seed-original-conductance) | Existing full-neighbor denominator and cubic count mechanism; its old fixed-hub mass and reflected-kernel scope are not substituted for the present full label chain. |
| dependency | [Original return monotonicity](Yin_C_G0169_v1.md#endpoint-collision-monotonicity) | Complete binary-difference law gives p_(k-ell)>=p_k and p_k>=p_n with all lengths and empty-return cases retained. |
| dependency | [Every actual intermediate route label](Yin_C_G0623_v1.md#whole-z0-finite-route) | Both left/right zero-middle and excursion labels lie in the strict actual core, have radius below R(c), and admit actual reaching/continuation words of length at most A_D R(c)+B_D; same current-n paths and sign reversal retain these bounds. |
| dependency | [Paid affine route radius](Yin_C_G0625_v1.md#neutral-coordinate-affine-onset) | Actual R(c)<=A_rad rho(c)+B_rad and inherited length constants, with both trace coefficients and original neutral embedding paid. |
| dependency | [Exact current square-root event](Yin_C_G0625_v1.md#statement) | Full original mass1/32, exact N_sqrt and L_n, same-current-length sign paths, all original tail representations and complete return normalizer. |
| dependency | [Complete original label law](Yin_C_G0627_v2.md#conditional-lift-exact-reuse) | Exact conditional product fibers, all full row/column masses and original half-kernel conductances; no uniform graph probability. |
| dependency | [Paid short-path lift](Yin_C_G0627_v2.md#full-negative-word-randomized-lift) | Original four-refresh construction on ell<4, exact source-terminal correlation and complete unordered-edge load accounting. |
| dependency | [Exact long lift and mixed path formula](Yin_C_G0631_v1.md#alternating-shortening-and-short-path-scope) | Clique compression preserves vertices/current support, exact long alternating lift and fully paid mixed-length numerator and short refresh formula; no compression-congestion monotonicity or unrestricted zero-length lift. |
| dependency | [Original linear overlap bound](Yin_C_G0645_v1.md#gaussian-core-sum-linear-overlap) | Actual D_n<=G_n<=C_star n used only after deriving the current conductance lower bound and upper load; no lower count inferred from an upper endpoint profile. |
| dependency | [Original odd sign-flow inequality](Yin_C_G0602_v2.md#partial-sign-flow-original-law) | Full sign-symmetric subprobability, randomized actual length-times-traversal load, exact Lambda/4 coefficient for real or complex odd functions and digit-work conversion. |
| review | [Independent entire growing-route finding](../audits/reviews/Yin_R_G0855_v1.md#growing-route-load-whole-independent-finding) | Complete statement and Sections1--6, all same-k and empty-word cases, full131072 conductance and896 refresh constants, every intermediate label/current onset, original mass and terminal word, actual length, both load expressions, exact constants, odd real/complex energy and work clock; prior C645 and upstream source scopes retained. |

<a id="argument"></a>

<a id="growing-route-count-reuse"></a>
## 1. Exact reuse and the new growing-route scope

[C519 Section1](Yin_C_G0519_v1.md#seed-complete-count-comparison) already obtains complete same-time endpoint counts by concatenating fixed actual words with every remaining-length return, using original monotonicity.
Its [Section2](Yin_C_G0519_v1.md#seed-original-conductance) already pays the cubic count factors and the complete middle-word denominator on a FIXED seed.
The present proof reuses those mechanisms with a growing paid witness length T_n, rather than claiming another fixed-hub result.
[C169](Yin_C_G0169_v1.md#endpoint-collision-monotonicity) supplies p_(m+1)<=p_m for the full original digit law.
The same binary autocorrelation gives nu_m(z)<=p_m for every z, as used in C519.

[C623 Section6](Yin_C_G0623_v1.md#whole-z0-finite-route) bounds BOTH left and right intermediate label radii and provides actual reaching/continuation words of length at most A_D R(c)+B_D.
[C625](Yin_C_G0625_v1.md#neutral-coordinate-affine-onset) bounds R(c) by A_rad rho(c)+B_rad, and its exact square-root onset supplies the complete mass and path lengths used here.
[C627v2](Yin_C_G0627_v2.md#conditional-lift-exact-reuse) owns the full label/word laws, including every original conditional denominator.
[C631](Yin_C_G0631_v1.md#alternating-shortening-and-short-path-scope) supplies clique compression and the already proved paid mixture of exact long alternating lifts with short-path refreshes.
[C645](Yin_C_G0645_v1.md#gaussian-core-sum-linear-overlap) supplies only the final upper bound for the original D_n, after the actual lower-count proof below is complete.
No known1/n return order, finite-word injection principle, topology-only gap or existing lift is registered again in isolation.

<a id="same-time-complete-tail-count-injection"></a>
## 2. Same-time lower counts with all word and time costs

For a right label c choose one ACTUAL chronological word0->c of length ell_c<=T and probability q_c>=4^-ell_c.
Appending that fixed word to every original return of length k-ell_c is a probability-preserving concatenation of disjoint digit positions before conditioning.
Different earlier return words give different complete words.
Thus

    K_orig^k(0,c)>=p_(k-ell_c)q_c
                    >=4^-T p_k.                         (8)

For a left label y choose one ACTUAL continuation word y->0 of length ell_y<=T and probability q_y>=4^-ell_y.
Follow it by every original zero-to-zero return of length k-ell_y, obtaining

    K_orig^k(y,0)>=q_y p_(k-ell_y)
                    >=4^-T p_k.                         (9)

The comparison p_(k-ell)>=p_k is exactly C169's monotonicity; it neither sets the fixed word's probability to1 nor changes the length k.
The case ell=k leaves p_0=1, and ell=0 causes no exception.
Reversing the chronological digit order identifies K_orig^k(0,c)=nu_k(c) while preserving every original word weight.
The same convention gives K_orig^k(y,0)=nu_k(-beta^k y).
Therefore (8)--(9), divided by p_k and multiplied by the matching4^k factors for integer counts, give the lower part of (1).

For the upper part, write the original ternary endpoint as the difference of two independent fair-binary endpoints.
Its probability is a full binary autocorrelation, so Cauchy--Schwarz gives nu_k(z)<=nu_k(0)=p_k for every z.
This is used only as an UPPER bound and as the existing input to monotonicity, not reversed to manufacture a lower bound.
All lower counts have already been obtained by the concrete injections (8)--(9).
The fixed words are witnesses for a lower count; the eventual flow uses ALL representations in the full fibers, not just those witnesses.

<a id="growing-patch-full-label-conductance"></a>
## 3. Complete row and column denominators and original conductance

Let Theta be the81 four-digit ternary words and w(theta)=2^(zero count).
Their TOTAL original integer weight is

    sum_(theta in Theta)w(theta)=(1+2+1)^4=256.           (10)

For fixed y each positive right neighbor c corresponds to a different middle polynomial theta=y-beta^4c.
The basis1,beta,beta^2,beta^3 makes its word unique, so the complete row satisfies

    r_y=t_k alpha_k(y) Z_y,
    Z_y=sum_(c current neighbor)beta_k(c)w(theta_(y,c))<=256.

This includes every original neighbor, not only the selected collection; unsupported terms may simply be zero.
Similarly s_c=t_k beta_k(c) Z'_c with Z'_c=sum_y alpha_k(y)w(theta_(y,c))<=256.
No reflected or induced subgraph denominator is used.

For distinct labels (y,c),(y,c') in the collection, the exact heat-bath conductance is

    Qbar=t_k alpha_k(y) beta_k(c) beta_k(c')
                    w(theta)w(theta')/(2 Z_y)
          >=t_k 4^(-3T)/512.                            (11)

For a column edge the remaining product is beta_k(c)alpha_k(y)alpha_k(y') and the same inequality follows.
The lower power is cubic because the shared tail factor cancels once against its COMPLETE marginal; the half-kernel factor2 is retained.
Finally the full normalization and the original time comparison are

    t_k=c_k(0)^2/c_(2k+4)(0)
        =p_k^2/[256 p_(2n)]
        >=p_n^2/[256 p_(2n)]
        =1/(256 D_n), n=k+2,                            (12)

using p_k>=p_n from monotonicity.
Combining512 and256 gives131072=2^17 and proves (2).
Every chronological index and factor4^4 is retained in (12).

At a zero-middle source, w(theta)=16, and its ACTUAL probabilities of choosing a specified half-kernel and retaining the label are

    q_A(e)=p_e/(2r_y)=16 beta_k(c)/(2 Z_y)>=4^-T/32,
    q_C(e)=p_e/(2s_c)=16 alpha_k(y)/(2 Z'_c)>=4^-T/32.

These are (3), with no conditional probability rescaled to one.

<a id="all-intermediate-label-current-onset"></a>
## 4. Every intermediate endpoint is covered at the SAME n

For source c in C625's square-root window, rho(c)<=r_n.
C623 gives its route and the sign-reversed counterpart, with EVERY zero-middle and excursion label of both endpoint types in the actual core and of neutral radius less than R(c).
Its proof explicitly includes common labels of the forms beta^4q+u and q-beta^-4u for legal four-digit u, adding the full radius cost4.
C625's affine bound is R(c)<=A_rad rho(c)+B_rad<=R_n.
The same bound holds for -c because C623 has R(-c)=R(c).
Consequently each right label on either route has an actual reaching word of length at most A_D R_n+B_D, and each left label has an actual continuation word of that same bound.
This covers all intermediates, not just the initial and final zero-middle states.

For n>=N_sqrt the defining quadratic inequality gives

    n-U sqrt(n)-(W+2)>=0,
    k=n-2>=U sqrt(n)+W=A_D R_n+B_D.

Also n>=5 gives k>=3.
Since k is an integer, k>=T_n=max{3,ceil(A_D R_n+B_D)}.
There is thus enough room for each injection in Section2 at this very tail length k; no later length is used to establish a current count.
Apply (1)--(3) to the finite union of all labels used by these routes, with T=T_n.
It is finite because the current selection and each chosen route are finite; no enumeration or bound on its cardinality is needed.

For each source label choose one of the C623/C625 sign routes, project to labels, remove successive equal labels and apply C631's row/column clique compression.
The resulting path depends only on the source label, is alternating and has length ell<=L_n.
Compression introduces no new vertices, so EVERY endpoint count needed for its edges still satisfies the bounds just proved.
Shortcut edges may differ, but (2) applies to every positive edge joining vertices in this collection.
No unproved claim that compression decreases congestion is used.

C625's complete original mass computation gives (4), including the unique middle zero-word weight16 and the full Z_n denominator.
The radius event is sign-symmetric and includes every source-tail representation at each retained label.
We use this whole event, not the smaller matching-trim event of C627v2.
Its mass is therefore at least1/32 for every stated n, independently of the critical-mean branch.

<a id="paid-short-refresh-and-subexponential-full-flow"></a>
## 5. Actual full-word length, both load terms and their constants

Use C631's exact lift for ell>=4 and C627's four-refresh lift for ell<4, as assembled in C631's mixed-length formula.
Both retain the own-source terminal word S eta exactly and average over complete original tail laws.
They apply because the selected source is label-measurable and its word fibers retain their complete product distributions.
No negative source is replaced by an unrelated word at the same endpoint.

For long paths the full-word length is exactly ell.
For short paths it is at most ell+4<=7, after removing any identity proposals.
Here B_len=5G/sqrt(13)+26>26, so L_n>=ceil(2B_len)>52 and in particular L_n>=7.
Thus the ACTUAL full-word length is at most L_n in BOTH cases.
This check is made before using L_n as a full-path cost.

For an unordered inter-label edge, the C631 mixed-load numerator is

    sum_e p_e 1_(M_n)(e) E[(ell+4*1_(ell<4))N_edge].

Its length factor is at most L_n by the preceding bound, its traversal count is at most ell<=L_n, and the complete selected source mass is at most1.
The numerator is therefore at most L_n^2.
Dividing by the independently proved current conductance lower bound (2) gives the first line of (5).
This calculation uses the full original mass, not a uniform distribution on paths or labels.

For short-path refreshes put

    m_e_short=p_e 1_(M_n)(e) E[(ell+4)1_(ell<4)].

At a selected label m_e_short<=7p_e.
Sign symmetry gives p_(Se)=p_e and keeps Se selected, hence m_e_short+m_(Se)_short<=14p_e.
At every unselected label both source terms are zero.
C631's complete within-label load formula and (3) give

    Lambda_short_refresh
      <=max_(e selected)2(14p_e)/[p_e(4^-T_n/32)]
      =896*4^T_n.                                      (13)

The constant896 includes both source/terminal contributions, both unordered orientations and the true half-kernel holding cost.
No symmetry of the chosen path laws is required.
Every full nonloop edge is either inter-label or within-label, so the total load is bounded by the MAXIMUM of the two displayed prices, not their sum.
Since D_n>=1, T_n>=0 and L_n>=1, the first price131072 D_n 4^(3T_n)L_n^2 is at least the second896*4^T_n.
This proves the first total bound in (5).
Only now use the adopted original overlap bound D_n<=G_n from C645 to obtain the second expression in (5).
This is a valid substitution into an already proved upper LOAD bound; it is not a lower endpoint estimate deduced from an upper profile.

For (6), the exact definitions give

    T_n<=U sqrt(n)+C_T,
    L_n<=L_star sqrt(n),
    G_n<=C_star n.

The first inequality follows from ceil(x)<=x+1 and the separate max with3; the second uses sqrt(n)>=1.
Substitution into the FULL second bound of (5) gives exactly C_flow n^2 exp(c_flow sqrt(n)).
The constants are fixed by the stated actual quartic and inherited actual-word onset constants; they are not optimized.
The original complete sign-flow inequality C602 applies to these paths and source mass, proving (7) for real and complex odd f.
Multiplying the nonloop clock price by n+2 multiplies both load expressions by n+2 and divides the corresponding energy by n+2, without changing the source law or terminal word.

<a id="same-time-lower-count-scope-boundary"></a>
## 6. Exact improvement and the remaining unproved bridge

The new assertion is a completely paid all-late ORIGINAL positive-mass sign flow with subexponential-in-n load, and thus a corresponding bound for all selected odd functions.
Its counts and all path intermediates are realized at the same current n, with the complete denominators retained.
The return words in the injections cost4^-T_n; the growth T_n=O(sqrt(n)) has not been hidden.
This improves C625's coarse exp(Cn) single-word conductance estimate, while reusing C519's existing injection/cancellation mechanism at its true growing cost.
C519's fixed-hub mass limitation is unchanged: the present mass comes from C625's growing COMPLETE radius event, not a fixed seed or a padded collection of selected words.

The factor4^(3T_n) grows, and none of the bounds proves a uniform odd coefficient or paid load.
C645 controls only the D_n factor after this actual lower-count construction; it does not remove the witness-word cost.
C631's necessary original congestion lower bounds and the unresolved finite/infinite mean alternatives remain compatible with the present upper estimate.
The new theorem does not select a critical-mean branch, prove a uniform spectral gap or complete the original unrestricted Lehmer Task.
A further bridge would have to improve the paid lower-count/congestion mechanism itself, rather than erase its time cost or reverse an upper estimate.
