---
author: Yin
---

# Arithmetic first-return rarity and finite Perron profile escape

Date: 2026-10-10.
Fixed retention under the coordinating AI for Yin's instruction, after its complete noncontributor review of D49.
The authoring arithmetic agent performs this mechanical retention.
This is not an independent review of its own proof, a C acceptance, or Task completion; G0001 remains active and unresolved.

<a id="finite-profile-escape-fixed-scope"></a>
## Adopted scope

The [finite critical-return theorem](#finite-critical-return-profile) bounds stationary mass at zero using the complete original arithmetic first-return mass bound and an explicitly normalized finite Doob chain.
The [reciprocal Salem interface](#reciprocal-prime-profile-amplitude) converts this to a positive right Perron coordinate bound on prime sets invariant under the field involution.
The [small-measure theorem](#small-measure-profile-escape) and following word-ball estimates retain every degree, measure, finite-core and auxiliary-probability hypothesis.
They force a necessary mass-escape pattern but give no uniform spectral contradiction.
No full infinite critical-return normalization or original-law mean estimate is asserted.

The complete proof and original author-checking/contribution account follow.
Their earlier pending status records the drafting stage and is superseded by this fixed adoption statement.
Any later extension from Salem inputs to general reciprocal units is a separate theorem and is not silently included in this version.

<a id="retained-finite-profile-escape-argument"></a>
## Preserved D49 proof and original checking scope

## Arithmetic first-return rarity forces finite Perron profiles away from zero

Date: 2026-10-10.
New arithmetic/operator inquiry by resultant_research for Yin, after fixed retention of [L177](Yin_L_G0177_v1.md).
The question is how genuine non-torsion relation structure constrains low-energy finite Perron profiles.
This draft combines the complete degree-dependent first-return mass bound already proved in L154 with a finite critically tilted chain; it does not infer any full-infinite critical-return identity or uniform gap.
The coordinating agent assigned the direction and supplied none of the derivation below.
No program is planned.

### Responsible inputs and scope

Use [L154's complete original first-return law and mass bound](Yin_L_G0154_v1.md#uniform-small-unweighted-return-tail), [L157's exact finite-prime restricted cores](Yin_L_G0157_v1.md#finite-prime-return-core), [L173's radius exhaustion](Yin_L_G0173_v1.md#finite-prime-spectral-exhaustion), and [L177's exact Perron energy](Yin_L_G0177_v1.md#finite-prime-near-one-size-cost).
The original matrices and original return laws always use eta in{-1,0,1} with weights(1/4,1/2,1/4).
A finite auxiliary Doob chain below is explicitly normalized and is not substituted for that law.
The intended output is a necessary quantitative profile-escape theorem, not a restatement of finite-prime approximation as a lower entropy bound.

<a id="finite-critical-return-profile"></a>
### 1. Exact finite critical normalization and the arithmetic mean-return bound

Let alpha be a nontorsion algebraic unit of degree d>=3 and let D_S be a nontrivial finite-prime restricted core, with original killed matrix K=K_S.
Its graph is strongly connected by the actual definition in L157.
Write r=r(K) and h=-log r.
L177 gives1/2<r<1.
Let v and w be positive right and left Perron vectors, respectively, and define the auxiliary stochastic matrix and stationary probability

    Q(x,y)=K(x,y)v(y)/(r v(x)),
    pi(x)=w(x)v(x)/sum_y w(y)v(y).                     (1)

Both assertions follow by the two Perron equations; no boundary probabilities of K have been renormalized in the original problem.
For any zero-to-zero word of length n, the v factors telescope, so its Q probability is exactly r^(-n) times its original probability.
If f_n^S denotes the original restricted first-return mass, its Q first-return distribution is consequently

    q_n=f_n^S r^(-n),
    q_1=1/(2r),  sum_(n>=2)q_n=b:=1-1/(2r)>0.        (2)

The normalization sum_n q_n=1 and finite mean hold because Q is a finite irreducible chain.
Here is also the needed mean formula without an unstated infinite-chain recurrence assumption.
From every state there is a positive-probability path to zero of bounded finite length; a minimum of those finitely many probabilities gives a geometric block bound for the hitting time.
The first positive return time tau from zero therefore has finite mean.
Its expected occupation numbers before tau satisfy mu Q=mu by shifting the time index in the finite-expectation sum: the initial and final states are both zero.
Moreover mu(0)=1.
The unique normalized stationary distribution is pi, so

    E_Q tau=1/pi(0).                                 (3)

This is proved only for the finite auxiliary chain.
No normalization at a full infinite operator's critical radius is being assumed.

L154 supplies the complete original-law bound

    f_n=0 for2<=n<=d,
    sum_(n>=2) f_n <=T_d,
    T_d=d 2^(-d)[1+8/(3(d-2))].                      (4)

Restricted first-return events form a subset of these actual events, so the same bounds hold for f_n^S.
Put a=sum_(n>=2)f_n^S, which is positive for a nontrivial core.
On nontrivial excursions, let nu_n=q_n/b be the normalized Q law.
Then, with every term nonnegative and finite first moment,

    a/b=E_nu exp(-h n),
    E_nu n >= log(b/a)/h >= log(b/T_d)/h.              (5)

The inequality is Jensen for the convex function exp(-h n); it retains the exact original-to-auxiliary exponential factor.
Also E_nu n>=d+1 by(4).
Substitution in(3) gives the precise profile bound

    1/pi(0) >= 1/(2r)
       +b max{d+1, log(b/T_d)/h}.                    (6)

In particular, if b>T_d,

    pi(0)<=h/[b log(b/T_d)].                         (7)

The discarded positive one-step contribution only weakens this last inequality.
The maximum in(6) keeps the bound useful and positive even when the logarithm in(5) is negative.
This is a new consequence for finite Perron profiles of the already retained arithmetic return rarity, not a new proof of(4).

<a id="reciprocal-prime-profile-amplitude"></a>
### 2. On reciprocal prime cores this controls the right eigenvector itself

Now let beta in(1,2) be Salem, and let sigma be the involutive automorphism of Q(beta) taking beta to beta^(-1).
Choose the finite set S of maximal-order prime ideals invariant under sigma.
Such sets remain cofinal: enlarge any finite set to S union sigma(S), and apply the same operation to an increasing exhaustion.

The additive involution T(x)=beta^(-1)sigma(x) preserves O=Z[beta] and the S-unit domain, because beta is a unit and sigma permutes S.
An original edge x->y=beta*x+eta reverses to T(y)->T(x) with digit-eta.
Thus every restricted closed word transforms to another restricted closed word, D_S is preserved by T, and with U the corresponding coordinate permutation,

    K_S^T=U K_S U,  U^2=I,  U(0)=0.                  (8)

For a positive right Perron vector v with ||v||_2=1, Uv is a positive left Perron vector.
Put c=<v,Uv>, so0<c<=1 by Cauchy--Schwarz.
Formula(1) at the fixed point zero gives

    pi(0)=v(0)^2/c,  hence v(0)^2<=pi(0).            (9)

Combining(6) or(7) with(9) is therefore a statement about the actual positive l2-normalized finite Perron profile, rather than only a stationary product of unrelated left and right eigenvectors.
Prime invariance is an explicit hypothesis here; it is not silently assumed for every finite S.

<a id="small-measure-profile-escape"></a>
### 3. An explicit d/m scale for hypothetical near-one Salem approximants

Suppose d>=12 and0<m=log(beta)<=log(4/3)/2.
Let S be sigma-invariant and large enough that

    r(K_S)>=exp(-2m).                               (10)

Such finite sets exist, and all sufficiently large sets in the symmetrized L173 exhaustion work: its limiting radius exp(-h_2) is at least exp(-m), which is strictly greater than exp(-2m).
This uses the existing inequality h_2<=m and the correct below-to-above direction of radius approximation.

For such a core, h=-log r<=2m and r>=3/4, so b>=1/3.
For every d>=12,

    T_d<=(13/9)d 2^(-d),
    (13/3)d<=2^(d/2),
    log(1/(3T_d))>=d log2/2.                         (11)

The first estimate already holds for d>=8.
For the second, d=12 gives52<=64, and increasing d by one multiplies the right side by sqrt2 while the left side grows by a factor at most13/12<sqrt2.
Hence the second estimate holds for all later integers.
Equations(7), (9) and(11) prove

    pi(0)<=12m/(d log2),
    v(0)^2<=12m/(d log2),
    E_Q tau>=d log2/(12m).                           (12)

All constants and the degree restriction are explicit.
These are conditional necessary properties of hypothetical small-measure Salem approximants, not a construction or an exclusion of those inputs.
Their finite sizes may be arbitrarily large.
The expected return time in(12) belongs to the displayed auxiliary critically tilted chain; it is not an original-law expected-return assertion.

### 4. Every bounded restricted-word neighborhood carries little profile mass

Define B_L(S) to be the states reachable from zero by at most L positive K_S edges, retaining the actual restricted paths.
It is not defined by ambient short paths that could leave D_S.
On every positive edge x->y, the right Perron equation gives

    v(y)<=r v(x)/K_S(x,y)<=4r v(x).

Choose a shortest restricted word to each state in B_L(S).
At most3^l such states have chosen length l.
Thus

    sum_(x in B_L(S))v(x)^2
       <=v(0)^2 sum_(l=0)^L [3(4r)^2]^l
       <=[(48^(L+1)-1)/47] pi(0).                    (13)

For the cores in Section3, put C_L=(48^(L+1)-1)/47.
The bound becomes

    sum_(x in B_L(S))v(x)^2<=C_L 12m/(d log2).        (14)

In particular, on any hypothetical family satisfying the stated near-one hypotheses, every fixed restricted-word radius has asymptotically zero mass.
If such a ball is to carry at least one half of the profile norm squared, it is necessary that

    L>=log_(48)(1+47d log2/(24m))-1.                  (15)

The estimate is deliberately a safe coarse count, with original edge probabilities kept.
It is not a claim of optimal distance growth.

For a fixed input, any fixed finite list of actual returning states and specified zero-to-state paths can be included in a sufficiently large restricted core: append one actual return path for each state and collect the finitely many prime divisors of all nonzero intermediate states.
Symmetrizing that finite prime set preserves inclusion.
This observation can be used when a test requires the selected local words inside D_S.
It does not make every ambient path restricted for an arbitrary already chosen S.

<a id="arithmetic-profile-boundary"></a>
### 5. Relation to the exact energy obstruction

For the original normalized right profile, L177 gives

    1-r(K_S)=sum_({x,y})H_S(x,y)|v(x)-v(y)|^2
                             +sum_x delta_x v(x)^2,
    H_S=(K_S+K_S^T)/2.

Together with(12)--(14), this says that a near-one finite Perron profile must simultaneously have low edge/boundary energy and avoid every bounded restricted-word neighborhood of the origin.
The new ingredient is the actual degree-dependent rarity of every nontrivial original first return, transferred through a fully normalized finite chain.
It is more than a statement that each finite matrix has integral4K, but it is still compatible with escaping mass on a growing state set.

There is consequently no contradiction or uniform forbidden spectral neighborhood here.
A new arithmetic input would have to prevent those genuine eigenprofiles from escaping while their edge energy is small, or derive a full-kernel estimate that already includes that escape.
The origin cannot be given an input-independent mass lower bound merely because every finite core is strongly connected through it: equations(12)--(14) show precisely how such a lower bound would have to overcome the existing long-return mechanism.
Nor may one infer F(exp(h_2))=1 for the full infinite return series by importing the finite normalization in(2); that limit has not been justified and is not needed.

### 6. Checking and contribution boundary

The assigned arithmetic agent derived and self-checked(1)--(15), including finite hitting-time integrability, stationary occupation normalization, the exact tilt sign, the original/auxiliary probability distinction, the restricted-event inclusion into L154, the small-degree/logarithm guard, prime-involution covariance, positive left/right normalization, cofinal approximation direction, and the distinction between restricted and ambient word balls.
The coordinating agent assigned the conceptual continuation and received an early checkpoint but supplied none of this proof.
The underlying original all-degree mass bound is exactly the older L154 theorem, not newly claimed here.
Standard finite Perron and elementary convexity facts are used; no new external theorem or numerical experiment is adopted.
No J is needed.
Complete independent mathematical review and fixed adoption are pending, and unrestricted G0001 remains unresolved.







<a id="finite-profile-escape-retention-record"></a>
## Retention and contribution boundary

The resultant_research AI derived D49's finite normalization, mean-return/profile estimates and word-ball consequences.
Its complete2026-10-10 author self-check remains in [R80](../audits/reviews/Yin_R_G0080_v1.md#finite-profile-original-author-check-finding), covering all(1)--(15) and its exact listed finite/domain/probability obligations.
On2026-10-10 the coordinating AI checked the complete frozen D49 Sections1--6/equations(1)--(15), finding no mathematical defect.
Its exact input is the original [retained finite-profile argument](#retained-finite-profile-escape-argument): original killed law versus finite auxiliary Doob law, hitting/occupation/Jensen normalization and log guards, Salem invariant-prime reversal/cofinality, d12/small-measure constants, restricted-word balls/finite-list inclusion and exact energy/escape limits.
It assigned the broad research question and received author progress summaries, shared context and an early checkpoint, but supplied none of these derivations.
The actual initial target-mathematical contents of those additional inputs remain unestablished, so the original whole relationship is unknown.

The original dated fixed-retention instruction above followed that noncontributor check.
The authoring arithmetic agent implemented the restricted adoption and retired D49; this was neither C acceptance nor Task completion.
The [later R660 whole finding](../audits/reviews/Yin_R_G0660_v1.md#isolated-finite-profile-whole-finding) is a new2026-10-22 inspection of C435v1 and an explicit comparison of the entire old mathematical, probability, source and contribution scope.
It does not change the original adoption date or attribute an isolated arrangement to the old reviewer.
No J or numerical calculation belongs to this proof-only result.
