---
author: Yin
---

# Complete conditional-tail lifting of selected original odd energy and sign flows

Contributor original_law develops the selected-energy and exact full-negative-word flow comparisons below from C170's existing complete original endpoint reduction.
Root proposed testing full conditional-tail randomization and the spectral interface; the two-projection spectrum itself is already proved in C170 and is reused, not claimed anew.
The original word law, its complete normalizer and the actual current-length labels are retained throughout.
This complete author argument is fixed for fresh isolated whole review; its initial assessment is open and no independent review or uniform load bound is claimed.

## Statement

Fix the actual quartic P(t)=t^4-t^3-t^2-t+1, its exterior Salem root beta and neutral conjugate zeta.
For every integer n>=5 put k=n-2, and let Omega_n be ALL returned length-2n ternary words with original digit probabilities1/4,1/2,1/4 before conditioning.
Write a word as eta=(A,theta,C), with both outside tails of length k and four middle digits.
Let w(V)=2^(number of zero digits in V), c_j(a)=sum_(V of length j, V(beta)=a) w(V), and Z=c_(2n)(0).
The complete original law is pi(eta)=w(A)w(theta)w(C)/Z.
Let K=(H_A+H_C)/2 condition on the entire left or right tail, and S eta=-eta.
For every unordered positive nonloop full-word edge q={eta,eta'}, set Q(q)=pi(eta)K(eta,eta') and E(f)=sum_q Q(q)|f(eta)-f(eta')|^2.

Use the actual normalized labels

    y=-beta^-k A(beta), c=C(beta),
    theta(beta)=y-beta^4 c.

Because 1,beta,beta^2,beta^3 are independent over Q, a positive label pair e=(y,c) determines exactly one middle word theta_e.
Let I be precisely the finite set of positive current label pairs, and define

    L_y=c_k(-beta^k y), R_c=c_k(c),
    W_e=L_y R_c w(theta_e), p_e=W_e/Z,
    r_y=sum_(e:y(e)=y) p_e, s_c=sum_(e:c(e)=c) p_e,
    alpha_y(A)=w(A)/L_y, gamma_c(C)=w(C)/R_c,
    mu_e(A,C)=alpha_y(A) gamma_c(C).

Only positive fibers are used, and pi(A,theta_e,C)=p_e mu_e(A,C).
Negation sends e to Se=(-y,-c), preserves p,r,s and sends alpha_y,gamma_c to their full negative-word laws.
The exact label kernel and its energy are

    Kbar(e,e')=1_(y=y') p_(e')/(2r_y)
                 +1_(c=c') p_(e')/(2s_c),
    Qbar({e,e'})=p_e Kbar(e,e'),
    Ebar(g)=sum_(qbar nonloop) Qbar(qbar)|g(e)-g(e')|^2.       (1)

Take ANY function w_sel:I->[0,1] with w_sel(Se)=w_sel(e).
Its unnormalized selected masses are a(eta)=pi(eta)w_sel(e(eta)), abar_e=p_e w_sel(e), and delta=sum_e abar_e.
Define B_full and B_label as the least nonnegative extended-real constants in

    sum_eta a(eta)|f(eta)|^2 <= B_full E(f),    f(S eta)=-f(eta),
    sum_e abar_e |g(e)|^2 <= B_label Ebar(g),   g(Se)=-g(e).    (2)

All real or complex functions are included, and the least constant is infinity if no finite constant exists.
Then

    B_label <= B_full <= max{B_label,2}.                       (3)

In particular uniform boundedness in n of either selected coefficient is equivalent to uniform boundedness of the other, with the same complete selected mass.
No all-function spectral gap or uniform value for B_label is asserted.
The label selection may be a nonclosed subset of a component.

There is also an explicit paid flow lift, retaining the individual terminal word S eta.
For every e with abar_e>0, choose a path law Gamma_e on finitely many positive nonloop label paths from e to Se, allowing the empty path when e=Se.
Let ell be its random length and N_qbar its traversal counts, and set

    m_e=abar_e E_(Gamma_e)(ell+4),
    Lambda_bar_plus4=max_qbar Qbar(qbar)^-1
                         sum_e abar_e E[(ell+4)N_qbar],
    q_A(e)=p_e/(2r_y), q_C(e)=p_e/(2s_c),
    Lambda_refresh=max_e 2(m_e+m_(Se))
                                  /[p_e min{q_A(e),q_C(e)}].  (4)

Set m_e=0 for unselected labels; empty maxima and unused-edge loads are zero.
There are random positive full-word paths eta to S eta at the SAME n, selected with complete source mass a, satisfying

    Lambda_full=max_q Q(q)^-1 sum_eta a(eta) E[length N_q]
        <= max{Lambda_bar_plus4,Lambda_refresh}.              (5)

The construction uses all original tail representations with their complete alpha and gamma laws.
No individual alpha_y(A)^-1 or gamma_c(C)^-1 occurs in (4)--(5).
The quantities q_A and q_C are the actual probabilities in one K step of choosing H_A or H_C, respectively, and retaining label e; their possibly small values are paid explicitly.
If every selected Gamma_e is supported on paths of length at most L>=0, the simpler bound is

    Lambda_refresh <= max_(e selected)
          8 w_sel(e)(L+4) max{r_y,s_c}/p_e.                   (6)

This bound requires sign symmetry of the selection, but no sign-symmetric choice of the path laws.
Formula (5) makes no claim that bounded B_label yields bounded canonical-path load.

For C625's actual selections A_n(R)=E_n intersect {|Z_n|<=R}, where E_n has four zero middle digits, w_sel is label-measurable, sign-symmetric and includes COMPLETE original tails.
At every n covered by C625's current-onset theorem, all its selected labels lie in the zero-word component, so both (2) have finite constants and the paths in (4) exist.
In particular C625 gives a selection of mass at least1/32 at every sufficiently large n, with available label paths of length O(sqrt(n)).
This theorem removes the artificial single-word minimum-conductance bound from that interface, but supplies no uniform bound on B_label, Lambda_bar_plus4 or Lambda_refresh.
C602 applies to (5) with coefficient Lambda_full/4.
Alternatively, a future bound B_label<=B at every sufficiently large n, on selections of mass at least delta0>0, would give original fixed-radius midpoint capture and finite critical mean.
Precisely, for R_*^2=max{1,8B/delta0} the actual midpoint law has mass at least delta0/2 in |Z_n|<=R_*, and mu<=2N(R_*)/delta0 by C204, where N is the actual finite core count.
No such bound, critical-mean branch, finite-graph mixing inference or unrestricted Lehmer conclusion is proved here.
At the digit-work clock all energies divide by n+2 and all coefficients and loads multiply by n+2.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision conditional-lift-registration

| Field | Value |
| --- | --- |
| date | 2026-10-23T19:04 |
| status | open |
| reason | Register the complete selected odd-energy comparison and randomized full-negative-word flow lift with exact original conditional laws and paid endpoint hold costs. C170's existing spectrum is reused, and C625 supplies the all-late positive-mass current-length application. No uniform endpoint coefficient or congestion estimate is supplied, and fresh isolated whole review remains pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact comparison](#statement) | Every n>=5 and complete original quartic word law, positive current incidence support and normalizer, arbitrary sign-symmetric label selection, extended optimal odd coefficients, finite randomized label path laws, exact full negative-word terminal condition, all load constants, C625 current-mass consumer and remaining quantitative and Task limits. |
| argument | [Complete argument](#argument) | Sections 1--4 and formulas 1--12, including complete conditional factors, commuting label expectation, orthogonal tail-noise control, source/target correlation and unordered edge factors, original mass and midpoint capture, zero/empty cases and time rescaling. |
| dependency | [Existing exact original endpoint reduction](Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix) | Actual complete conditional word laws, weighted endpoint incidence, component correspondence and already established half/zero residual spectrum; no new priority or uniform spectral estimate. |
| dependency | [Unique four-digit labels and marks](Yin_C_G0170_v1.md#four-digit-overlap-exact-marks) | Exact middle-word uniqueness, complete label-measurability of the original midpoint and energy at most 4. |
| dependency | [All-late current full-fiber capture](Yin_C_G0625_v1.md#current-length-full-fiber-capture) | Complete zero-middle radius selections with actual original weights, sign symmetry and current-n zero-component membership, under the exact existing onset conditions. |
| dependency | [Positive mass and square-root paths](Yin_C_G0625_v1.md#square-root-current-sign-paths) | Original selected mass at least 1/32 and available O(sqrt(n)) same-n word paths at every sufficiently large n; no existing uniform load estimate is imported. |
| dependency | [Actual partial sign-flow inequality](Yin_C_G0602_v2.md#partial-sign-flow-original-law) | Directed original source mass, unordered edge conductance, randomized length-times-traversal convention and odd-energy coefficient Lambda/4. |
| dependency | [Original fixed-radius capture](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | Finite actual core count and the all-late positive capture implication for the actual critical mean, used only conditionally on a future uniform label coefficient. |
| support | [Existing two-step endpoint transfer](Yin_C_G0514_v2.md#partial-path-weighted-carry-target) | Prior paid transfer of a different all-function left-endpoint inequality, and standard weighted path-Cauchy accounting; not duplicated or used as a supplied load bound. |
| support | [Fixed-hub original load and mass](Yin_C_G0519_v1.md#seed-path-load-and-mass) | Existing original-weight and fixed-hub limitations, distinct from the new complete current-length selections. |
| support | [Original odd component scope](Yin_C_G0552_v2.md#odd-component-exact-theorem) | Self-sign complete-component and odd-energy terminology; finite connectivity is not a uniform coefficient. |

<a id="argument"></a>

<a id="conditional-lift-exact-reuse"></a>

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T19:13 |
| status | proved |
| reason | Adopt the entire exact original conditional-tail selected-energy comparison and randomized full-negative-word lift after reading the full fixed C and isolated whole R830. The optimal extended odd coefficients obey B_label<=B_full<=max(B_label,2), and every original endpoint holding probability, tail law, unordered orientation, source-target correlation and work-clock factor is retained in the paid flow. C625 supplies positive current mass and finite paths, not a uniform label coefficient or load; the unrestricted Task remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact comparison](#statement) | Every n>=5 and complete original quartic word law, positive current incidence support and normalizer, arbitrary sign-symmetric label selection, extended optimal odd coefficients, finite randomized label path laws, exact full negative-word terminal condition, all load constants, C625 current-mass consumer and remaining quantitative and Task limits. |
| argument | [Complete argument](#argument) | Sections 1--4 and formulas 1--12, including complete conditional factors, commuting label expectation, orthogonal tail-noise control, source/target correlation and unordered edge factors, original mass and midpoint capture, zero/empty cases and time rescaling. |
| dependency | [Existing exact original endpoint reduction](Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix) | Actual complete conditional word laws, weighted endpoint incidence, component correspondence and already established half/zero residual spectrum; no new priority or uniform spectral estimate. |
| dependency | [Unique four-digit labels and marks](Yin_C_G0170_v1.md#four-digit-overlap-exact-marks) | Exact middle-word uniqueness, complete label-measurability of the original midpoint and energy at most 4. |
| dependency | [All-late current full-fiber capture](Yin_C_G0625_v1.md#current-length-full-fiber-capture) | Complete zero-middle radius selections with actual original weights, sign symmetry and current-n zero-component membership, under the exact existing onset conditions. |
| dependency | [Positive mass and square-root paths](Yin_C_G0625_v1.md#square-root-current-sign-paths) | Original selected mass at least 1/32 and available O(sqrt(n)) same-n word paths at every sufficiently large n; no existing uniform load estimate is imported. |
| dependency | [Actual partial sign-flow inequality](Yin_C_G0602_v2.md#partial-sign-flow-original-law) | Directed original source mass, unordered edge conductance, randomized length-times-traversal convention and odd-energy coefficient Lambda/4. |
| dependency | [Original fixed-radius capture](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | Finite actual core count and the all-late positive capture implication for the actual critical mean, used only conditionally on a future uniform label coefficient. |
| support | [Existing two-step endpoint transfer](Yin_C_G0514_v2.md#partial-path-weighted-carry-target) | Prior paid transfer of a different all-function left-endpoint inequality, and standard weighted path-Cauchy accounting; not duplicated or used as a supplied load bound. |
| support | [Fixed-hub original load and mass](Yin_C_G0519_v1.md#seed-path-load-and-mass) | Existing original-weight and fixed-hub limitations, distinct from the new complete current-length selections. |
| support | [Original odd component scope](Yin_C_G0552_v2.md#odd-component-exact-theorem) | Self-sign complete-component and odd-energy terminology; finite connectivity is not a uniform coefficient. |
| review | [Independent whole conditional-tail finding](../audits/reviews/Yin_R_G0830_v1.md#conditional-tail-lift-whole-independent-finding) | Entire fixed statement and proof, exact product and label laws, all residual modes and extended zero/infinite cases, every randomized full-negative-word correlation and load factor, C625 consumer and conditional mean scope; all inherited source and historical review boundaries remain unchanged. |

## 1. Exact reuse and the full conditional product law

C170 already proves the weighted endpoint matrix, exact full-word spectrum, half-eigenvalue tail residuals, zero-eigenvalue interaction residuals and equality of complete word and endpoint components in [its Section 3](Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix).
Its Section 4 proves the uniqueness of the four-digit middle word and the exact label-measurability of the midpoint.
The normalized y used here is the bijective coordinate change from C170's left endpoint a=-beta^k y; no endpoint law is changed.
C514v2 already pays all residual word modes when transferring a different two-step LEFT-ENDPOINT all-function inequality in [its Section 6](Yin_C_G0514_v2.md#partial-path-weighted-carry-target).
C519 supplies original fixed-hub conductances and the distinction between selected mass and paid path load, not a growing-family load estimate.
The new statements here concern arbitrary label-measurable partial odd selection and a full-negative-word randomized flow, with explicit within-label prices.
They do not re-register the old spectrum or infer a gap from it.

The return equation is A(beta)+beta^k theta(beta)+beta^(k+4)C(beta)=0.
For each positive pair (y,c), the unique middle polynomial equals y-beta^4c.
Summing w(A)w(theta_e)w(C) over ALL outside representations gives W_e, hence sum_e W_e=Z exactly.
Conditioning on e leaves the independent complete alpha_y and gamma_c laws.
Given the full left word A, the next label under H_A has y fixed and conditional probability p_(e')/r_y, independent of the representation A.
Given that new label, the new right word has complete law gamma_(c').
The analogous assertion holds under H_C with alpha_(y').
Thus K is strongly lumped to (1), including the two contributions on a label self-loop.
For distinct labels sharing y, a full transition fixes the SAME left word and has conductance

    Q({(A,theta_e,C),(A,theta_(e'),C')})
        =Qbar({e,e'}) alpha_y(A) gamma_c(C) gamma_(c')(C').   (7)

For distinct labels sharing c, the symmetric formula has gamma_c(C) alpha_y(A) alpha_(y')(A').
Distinct label pairs cannot share both coordinates.
Within one label, a nonloop edge changing only C has

    Q({(A,theta_e,C),(A,theta_e,C')})
        =p_e q_A(e) alpha_y(A) gamma_c(C) gamma_c(C'),         (8)

and the symmetric formula holds for changing A with p_e q_C(e).
Distinct full words in one label cannot change both tails in one K step.
Every factor in (7)--(8) is the complete original factor, and all denominators are positive on their stated domains.
These formulas are conditional probability identities, not a uniform replacement law on a graph.

<a id="selected-odd-energy-lift"></a>
## 2. Exact paid selected-energy comparison

Let Rf=E_pi[f|e], the orthogonal conditional expectation onto label functions.
For each full word, H_A Rf is a function only of y.
Averaging H_A f over alpha_y while holding e fixed also gives that same function: conditional on y, the fixed left representation is independent of the remaining labels and right representation.
Consequently RH_A=H_A R, and the analogous equality holds for H_C.
Thus R commutes with K, with I-K and, by original sign symmetry, with S.

On ker R, H_A maps into the left-tail functions whose conditional mean at each y is zero.
H_C kills every such function, because conditional on a right word the left-tail distribution is a mixture of the complete alpha_y laws.
Similarly H_A kills the range of H_C within ker R.
The two restricted projections therefore have orthogonal ranges and their sum is an orthogonal projection.
For every h in ker R,

    <h,Kh>=(||H_A h||_2^2+||H_C h||_2^2)/2
              <=||h||_2^2/2,
    E(h)=<h,(I-K)h> >= ||h||_2^2/2.                         (9)

This is the already known half/zero spectral decomposition in a form usable with a nonclosed selection.
For any odd f put g=Rf and h=f-g.
Both are odd, E(f)=Ebar(g)+E(h), and E_pi[h|e]=0.
Since w_sel is label-measurable, the selected cross term also vanishes exactly:

    sum_eta a(eta)|f(eta)|^2
      =sum_e abar_e |g(e)|^2 + E_pi[w_sel |h|^2]
      <= B_label Ebar(g)+||h||_2^2
      <= B_label Ebar(g)+2E(h).                              (10)

If B_label is finite, (10) proves the upper bound (3); if it is infinite the extended-real upper bound is automatic.
Testing (2) only on label functions proves the lower bound, including the case of infinite coefficient.
At a finite state space the infimal finite constant is attained: the inequality is an inequality of finite-dimensional nonnegative quadratic forms, with the numerator vanishing on the denominator's kernel whenever a finite bound exists.
Equivalently (10) may first be applied with any admissible bound and then take its infimum.
Zero selections and empty odd label subspaces are included, with least nonnegative coefficient0.
The proof applies directly to complex functions through orthogonality with conjugates; no real-only extension is left implicit.

<a id="full-negative-word-randomized-lift"></a>
## 3. Randomized paths retaining the exact negative word

For a selected source eta0=(A0,theta_e,C0), remember the two original words A0,C0 and draw a label path from Gamma_e independently of their representations.
Perform the following finite sequence.
First keep e fixed, resample C from the COMPLETE gamma_c law, and then resample A from the COMPLETE alpha_y law.
Next follow the chosen label path, resampling the changing tail from its complete conditional law at every label transition and keeping the other tail exactly fixed.
Finally, at label Se, set C=-C0 and then set A=-A0, leaving the label and its unique middle word fixed.
Every proposed change is a positive K move by (7) or (8), and a proposal that leaves the full word unchanged is removed from the path.
The terminal word is exactly (-A0,-theta_e,-C0)=S eta0.
This is a construction of paths through positive edges, not an assertion that K itself chooses a prescribed label with probability1.
The inverse label-holding probabilities in (4) pay that conditioning.

Conditional on the initial label, the ORIGINAL source words A0,C0 are independent with laws alpha_y,gamma_c because the source mass is abar_e mu_e.
After the first two resamplings, the current tails have product law mu_e and are independent of both stored original words.
Induction along every prescribed label path preserves product law mu at the current label and independence from the stored words: the unchanged tail has the appropriate complete marginal, and the changed tail is a fresh independent draw.
At the final label the current tails are therefore independent of (-A0,-C0), whose joint law is mu_(Se).
During the final C correction the held A has its complete alpha law independently of the old and target C words.
During the final A correction the held -C0 has its complete gamma law independently of the old and target A words.
This checks the required endpoint correlation explicitly; merely sampling an unrelated terminal word from mu_(Se) would not suffice.

For each selected source label the actual length is at most ell+4.
It suffices to bound the expected load using ell+4 and the proposed traversals before deleting identity moves.
For a full nonloop edge projecting to a nonloop label edge, conditional product law and (7) show that its normalized load is exactly the corresponding expression in Lambda_bar_plus4 when computed with this larger length.
Indeed the product alpha/gamma factors in the numerator are the same as those in Q and cancel.
The reverse traversal has the same product factors, so both orientations contribute to the single unordered N_qbar in (4).
Summing over every directed initial source label, with its original abar mass, proves the first part of (5).

For a within-label edge changing C from C1 to C2 while A is fixed, the two distinct words C1,C2 can occur in either order in a refresh or final correction.
Its total weighted proposed traffic is therefore

    2(m_e+m_(Se)) alpha_y(A) gamma_c(C1) gamma_c(C2).         (11)

The term m_e comes from the initial refresh of sources at e, and m_(Se) from the final correction of sources at Se.
Both terms remain present when Se=e; they then refer to the two distinct phases of the same construction.
Division by (8) gives 2(m_e+m_(Se))/(p_e q_A(e)).
The analogous A-changing edge gives the denominator p_e q_C(e).
All full nonloop edges either change their label or have exactly one of these within-label forms, so their maximum is (5), with no addition of disjoint edge classes.
If an entire class has no actual nonloop edges, the displayed maximum remains a valid overestimate.
When both source paths have length at most L, sign symmetry gives m_e+m_(Se)<=2p_e w_sel(e)(L+4), proving (6).
No word atom is bounded below anywhere in this argument.

<a id="current-positive-mass-endpoint-obligation"></a>
## 4. Actual current-length consumer and the remaining paid obligation

C170's exact midpoint mark is constant on each complete label pair.
For the zero-middle event specifically, theta_e=0, y=beta^4c and Z_n=(beta^2c)(zeta), so C625's radius cutoff is also label-measurable.
C625's selected event and its mass use the complete normalizer Z and ALL representations in alpha and gamma, exactly as in the current theorem.
Its actual current-onset assertion puts every selected full word in the zero-word component; C170's complete component correspondence therefore places each selected label in its self-sign zero label component.
A finite path to its negative exists in the actual current label graph.
Projecting the C625 same-n full-word paths and deleting label repetitions provides such label paths with no greater length.
Consequently (4)--(5) apply at every n satisfying C625, including its all-late mass1/32 and O(sqrt(n)) length version.
The possibly very small complete label probabilities p_e and q_A,q_C have not been estimated uniformly.
The new load estimate removes the individual-word exponential minimum used in C625's coarse bound; it does not replace these unestimated endpoint quantities by constants.

Finiteness of B_label for this selection follows by restricting to the finite self-sign zero component.
An odd function has zero component mean because sign preserves the component and its original law.
The finite connected reversible Dirichlet form is positive on its nonconstant subspace, so the selected numerator has a finite bound there; outside this component the selected numerator is zero.
This finite-dimensional fact supplies no n-independent coefficient.
Equation (3) proves that the tail-representation part cannot itself be the source of divergence of the selected odd coefficient.
It does not identify an explicit label flow of uniformly bounded load, nor equate optimal energy constants with the loads of this particular path construction.

For any putative all-late label bound B_label<=B and selected mass delta>=delta0>0, apply (2) to the actual odd label mark g=Z_n.
C170 gives Ebar(Z_n)=E(Z_n)<=4, hence

    sum_eta a(eta)|Z_n(eta)|^2<=4B,
    pi_n{|Z_n|<=R}>=delta0-4B/R^2.                           (12)

Choosing R=R_* gives delta0/2 capture.
The quartic core and its full rank-four Minkowski lattice are unchanged, so C204 gives the stated finite critical-mean conclusion.
For C625's mass1/32 one can take R_*^2=max{1,256B} and mu<=64N(R_*).
This is a conditional consequence only; no new all-late estimate of B has been supplied.
C602 separately transfers the ACTUAL lifted loads (5) to all odd functions and preserves its necessary mass-versus-load obstruction on any hypothetical common divergent D_n subsequence.
In particular the existence of short label paths and complete selected mass alone still does not bound paid load.
The digit-work rescaling follows by multiplying each original edge time by n+2; label and full-word energies and loads have the same rescaling.
No finite screen, new numerical data or external theorem is used in this analytic comparison.
