---
author: Yin
---

# G0001: the coverage limit of fixed shortness and a companion-lattice test

Current complete proof: [C226](../claims/Yin_C_G0226_v1.md#joint-frobenius-minor-test), adopted at its actual current decision.
The original dated mathematical argument remains below as a fixed historical input; it supplies no Task resumption.

Date: 2026-10-07.
Bounded strategic assessment by assigned AI ms25_source for Yin, using the current S G0001, S G0002 and S G0004 and their retained mathematical inputs.
The coordinating AI requested the exact joint-prime calculation below.
This assessment proposes a next investigation within the existing Task; it changes no Task, strategy record, priority, or completion criterion.
The original displayed calculations have author self-review and a complete coordinator check whose initial review arrangement is unknown, as retained in R513.
No new literature search or computation was used.

<a id="fixed-shortness-coverage-limit"></a>
## Assessment: useful subsidiary results, with a now decisive scope limit

Continuing the current length-six classification by itself does not address the missing unrestricted quantifier.
It has produced useful theorems about positive realizations, essential neutral factors and their arithmetic costs.
But a positive entropy gap on every fixed support or fixed shortness class was already supplied by the accepted DS17 input in [L G0025](Yin_L_G0025_v1.md#bounded-excess-gap).
The new classifications can improve structural information within those classes; they have not placed arbitrary small-measure inputs in one fixed class.

Two distinct coverage obligations remain:

1. A general reduced reciprocal unit need not have a positive uniquely dominant conjugate.
   A primitive nonnegative realization with characteristic polynomial t^z p c, with c cyclotomic, exists exactly in the Perron scope of L G0034.
   Necessity is immediate: its Perron eigenvalue exceeds one and must belong to p, since zeros and roots of unity cannot supply it; primitivity makes it uniquely dominant.
   Neutral padding cannot remove this restriction.
   L G0042's prescribed root M(p) has exact entropy cost log M(M(p)), not automatically m(p).
2. Even on the Perron core, no theorem bounds minimum shortness L(p) or presentation excess E(p) throughout a fixed small-measure window.
   L G0027--28 show that bounded support, bounded length and bounded integral excess are the same boundedness obligation on bounded-measure families.
   Relabelling one as another changes no quantifier.

In particular, the existential assertion that there are some B>1 and some K with L(p)<=K whenever 1<M(p)<B is already Lehmer-equivalent, with the vacuous reverse implication explained in [L G0028](Yin_L_G0028_v1.md#near-one-quantifiers).
A preassigned window such as 1<M(p)<13/10 and an actual input-covering construction are materially more specific obligations; neither is proved.

The latest results make the distinction between repair degree and presentation complexity especially clear:

| Retained result | Actual advance | Remaining coverage boundary |
| --- | --- | --- |
| [L G0047](Yin_L_G0047_v1.md#girth-window-deletion) | Exact all-realization net-trace obstruction to neutral deletion, and a graph girth test. | Passing the test supplies no bounded graph excess through KOR00. |
| [L G0048](Yin_L_G0048_v1.md#positive-length-six-graph) | Primitive no-zero edge-excess-three presentations for the reciprocal length-six normal form. | The normal form is an input restriction. |
| [L G0049](Yin_L_G0049_v1.md#scaled-plastic-repair-bound) | Uniform repair bounds for every coprime scaled-plastic pair, at the whole noncyclotomic quotient scope. | It eliminates one attempted unbounded-repair family. |
| [L G0050](Yin_L_G0050_v1.md#essential-family-measure-obstruction) | Uniform eventual M>4/3 for the whole S_6 offset family. | It excludes that support as an infinite small-core mechanism; no effective cutoff is supplied. |
| [L G0051](Yin_L_G0051_v1.md#power-two-noncyclotomic-repair) | Exact unbounded minimum repair after all neutral factors are removed along powers of two. | These whole quotients have an edge-excess-three completion and face L G0050's measure obstruction; irreducibility is separate. |

Thus unbounded repair degree can coexist with a fixed positive graph budget.
Repair size is not a necessary intermediate bound for proving an entropy gap on that fixed-budget class: the latter already follows from bounded support.
Even an order bound B(e) for every fixed excess e would not bound e on the unrestricted core.
A reduction of dimension that leaves an unbounded initial excess untouched also does not close that direction.
This is the finite-closure check in M W0004 applied to the actual parameters, rather than an objection to the proved local theorems.

<a id="required-arithmetic-bridge"></a>
## The strongest useful bridge and its missing operation

The subsidiary graph results would reach the original gap through an actual, covering descent: for every input in a preassigned small-measure window, produce either a degree-independent positive entropy certificate, or a new noncyclotomic unit with no larger positive Mahler measure and strictly smaller well-founded complexity, with all terminal classes uniformly controlled.
If the input is already Perron, an entropy-neutral operation strictly lowering excess above one absolute threshold would be one concrete implementation.
The operation must act on every input in its claimed class, and terminal coverage must include non-Perron inputs through a separate justified reduction.

L G0014 already supplies such an actual descent when raising to a prime exponent lowers degree.
Its endpoint preserves degree under every map alpha -> alpha^ell with ell prime; the latest graph operations do not continue that descent throughout this endpoint class.
The meaningful remaining alternatives are an unrestricted arithmetic entropy certificate, or a new operation on these actual endpoints.
Another complete classification at L=6 does not itself provide either one.

This does not recommend declaring the length-six theorems irrelevant.
They now serve as controls for an all-excess operation and prevent false claims that divisibility guarantees positive deletion or bounded repair.
Finish the currently bounded classification test, then require a new coverage-changing mechanism before opening another fixed-length classification round.

<a id="joint-frobenius-minor-test"></a>
## One next discriminating task: the actual two-prime mixed-minor surplus

Use the original companion lattice, so the domain no longer requires Perron dominance, bounded shortness, bounded repair, or bounded rank.
Let p be monic irreducible reciprocal noncyclotomic in Z[t], with p(0)=1, degree d>=2, and companion matrix A in GL_d(Z).
In the target test additionally impose the fixed window 1<M(p)<13/10 and deg(alpha^ell)=d for every prime ell, exactly the endpoint condition proved in L G0014.
No stronger assertion for every composite exponent is needed here.
The formulas in this section do not need that power-degree condition; it is needed below when using the retained discriminant-escape implication.

Write Delta=|disc p| and call the discriminant parameter

    D_disc=d/Delta^(1/d).

This D_disc is unrelated to the canonical repair degree D(p).
For ell=2,3 let

    F_ell=p(A^ell).

The complete local proof in [C217v2](../claims/Yin_C_G0217_v2.md#argument) gives F_ell=ell B_ell with B_ell integral and nonsingular.
Frobenius proves integrality.
A zero determinant would give alpha_i^ell=alpha_j for conjugates of p; iteration of a finite-order Galois automorphism would then make alpha_i a root of unity.
Thus

    |det F_2|>=2^d,            |det F_3|>=3^d.                 (1)

These statements retain the actual d powered conjugates even when their degree drops; no degree-loss multiplicity is removed.

The joint determinant has the exact lower floor

    J(p):=det(F_2 F_2^T+F_3 F_3^T) >=13^d.                  (2)

Here is a direct proof, avoiding an additional source input.
If X,Y are positive definite d by d matrices, let lambda_i>0 be the eigenvalues of X^(-1/2)Y X^(-1/2).
Convexity of log(1+exp x) gives

    det(X+Y)^(1/d)
      >=det(X)^(1/d)+det(Y)^(1/d).

Indeed det(X+Y)=det(X) product_i(1+lambda_i), and the geometric mean of the last factors is at least 1+(product_i lambda_i)^(1/d).
Apply this to X=F_2 F_2^T and Y=F_3 F_3^T, and then use (1), giving 4+9=13.

The exact coefficient cost must be retained.
Put N=4d and let V_N have columns t^j mod p for 0<=j<N, as in L G0004.
Let E_ell be the N by d matrix whose j-th column is the coefficient vector of t^j p(t^ell), with 0<=j<d and zero padding.
Both ell=2 and ell=3 fit this window.
Set E=[E_2 E_3], an N by 2d matrix.
Then

    V_N E=[F_2 F_3],           G_N=det(V_N V_N^T).

One entirely integral, explicitly computable upper-comparison cost is

    C(p)=sum_(|I|=|K|=d) det(E[I,K])^2,                     (3)

where I ranges over row subsets of size d and K over column subsets of size d.
Equivalently C(p) is the coefficient of z^d in det(I_(2d)+z E^T E).
Cauchy--Binet followed by Cauchy--Schwarz, first for each K and then summing over K, gives exactly

    J(p)<=G_N C(p).                                         (4)

For clarity, the summand is det((V_N E)[:,K])=sum_I det(V_N[:,I]) det(E[I,K]), and sum_I det(V_N[:,I])^2=G_N.
No independence of the two prime blocks or omission of their mixed minors is assumed.
Also C(p)>=1: E_2 has a unit determinant minor on rows 2d,...,3d-1, since these leading coefficient rows are triangular with diagonal one.
A sharper valid cost is the product of the d largest squared singular values of E; using it would require its full comparison and evaluation, rather than silently dropping (3).

Combine (4) with the retained Vandermonde entropy bound Delta G_N<=N^d exp(2(N-1)m(p)).
This gives the actual sufficient certificate

    m(p) >= [log Delta+log J(p)-log C(p)-d log(4d)]
                 /[2(4d-1)].                              (5)

The precise new test is whether the full arithmetic J(p), after paying the entire coefficient cost C(p), can provide a uniform positive normalized surplus on the stated window.
For example an explicit c>0 and a proof

    Delta J(p)/[(4d)^d C(p)] >= exp(c d)                     (6)

throughout that domain would give m(p)>c/8.
Together with the already proved degree-reducing power descent and the nonreciprocal/unit reductions, this would address the original all-degree gap.
Equation (6) is an unproved, stronger finite certificate target; it is not asserted to follow from Lehmer or from positivity of a finite minor.
It may fail on an actual positive-entropy input without refuting Lehmer.
In particular a failed retained control would reject this specific two-prime cost, not the true entropy inequality (5).

<a id="bare-joint-prime-loss"></a>
## A proved gate: the bare 13^d floor does not remove the degree loss

Inserting only (2) into (5) supplies

    [d log(13/(4 D_disc))-log C(p)]/[2(4d-1)].               (7)

Because C(p)>=1, its numerator is at most d log(13/(4 D_disc)).
Once D_disc>13/4, this particular sufficient bound is nonpositive.
The retained [L G0015](Yin_L_G0015_v1.md#discriminant-escape) proves that any hypothetical sequence preserving degree under every map alpha -> alpha^ell, ell prime, with 0<m(p)->0 must have D_disc->infinity.
Therefore the bare two-prime floor supplies no positive certificate on precisely that hypothetical remaining branch.
This is a failure of the lower estimate obtained from divisibility alone; it is not a counterexample to (6), nor an assertion that a vanishing-entropy sequence exists.

This makes the next investigation concrete: determine whether the actual mixed-minor excess in J(p), using original integer recurrence data, offsets both D_disc and C(p), or prove a structural obstruction to this proposed cost.
Begin with the retained exact controls as checks of the formula, then require an all-degree argument rather than another parameter scan.
A proof of (6), or a properly quantified weaker certificate with the same uniform entropy consequence, is a success.
Recovery only of (7), a per-degree constant, or an assumed bound on D_disc, shortness or expanding-root count is a failure of this mechanism and should close that bounded attempt.

The overlap with earlier work is explicit.
L G0012 supplied the two individual Frobenius maps and identified their coefficient-Gram cost; L G0015 exposed discriminant escape; L G0016 permits a finite choice of a good prime under bounded discriminant and expanding count.
The new proposed test assumes neither of those bounds, keeps mixed minors of two actual prime maps, and must improve their normalized arithmetic gain.
Merely multiplying separate resultant inequalities would repeat the old degree-dependent mechanism.
The elementary floor (2) and the loss calculation (7) already show why a formal stacking argument is insufficient.

<a id="uniform-quantifier-review"></a>
## Research decision and review scope

Keep algebraic entropy primary and affine linear growth secondary.
The proposed computation and inequalities concern h_alg(A)=m(p) for the original companion flow, with no division by degree.
They need neither weighted entropy nor a Shannon-to-collision comparison.
The affine route should receive a separate new all-time estimate only when it retains arithmetic reachability; the known continuous and finite-quotient relaxations in L G0008/L G0011 do not acquire an arithmetic gap by being renamed.

The recommendation is to finish the one bounded length-six diagnostic already in progress, and move the next main effort to the original companion-lattice mixed-minor test above.
This is a proposed change of research attention inside G0001, not a Task change or an assertion of likely success.
Reopen fixed shortness classification as primary work only if it supplies an operation quantified over unbounded complexity or demonstrably enlarges input coverage.

The original formal checks are retained in [R513 author finding](../audits/reviews/Yin_R_G0513_v1.md#historical-minor-author-finding) and [R513 coordinator finding](../audits/reviews/Yin_R_G0513_v1.md#historical-minor-coordinator-finding), with the original2026-10-07 date, exact inspected scope and genuinely unknown coordinator initial arrangement.
The complete current mathematical proof and the exact failure of this proposed finite-window target are in C226; the historical research recommendation above is retained as history.
