---
author: Yin
---
# Whole review of arbitrary-exponent harmonic-cost capture

Date: 2026-10-15T09:13.
Human record author Yin.
Root separately assigned g_bridge_audit to review the ACTUAL fixed C132 v1, whose new geometric-chain argument was authored by root.
This reviewer authored the earlier C129 squarefree two-point/tensor mechanism and contributed several cited arithmetic background materials.
That antecedent contribution is explicitly disclosed: this is not a claim of independence from all previous project mathematics.
The reviewer supplied no chain coercivity estimate, dominant-coordinate split, tail bound, constant, endpoint repair or proof step for C132.
The squarefree account had left prime powers outside its proved scope; the new chain argument was first read by this reviewer in actual fixed C132.

This is a separately organized whole review, not blind.
Root's task description and requested checks, the preceding shared G0001 context and the C129 provenance were visible.
No C132 draft-generation dialogue, author proof explanation or earlier C132 review was consulted before the initial reconstruction.
Starting from the actual statement, the reviewer reconstructed all22 formulas, then checked the exact direct arithmetic interfaces.
Root's later correction of the comparison-only C108 anchor was inspected in the actual fixed text and verified at the target; it changes no mathematics.
This R covers the whole actual C132 v1 statement, Sections2--7, responsible question/reuse account, author freeze, fixed organization and initial decision dated17:10.
The exact initial arrangement supports the separate fixed-text inspection of the new chain argument.
The selected whole finding also covers tensorization, capacity substitution and residual-bucket transfer actually supplied by this reviewer in C129 and explicitly reused and expanded by C132.
Those are relevant substantive proof ingredients, not an unrelated earlier author role; rederiving them in C132 rather than listing C129 as a theorem premise does not remove that contribution.
The whole finding is therefore self-reviewed, while retaining the actual separate new-chain checks at their recorded scope.
Original dates, mathematical checks and exact binding scopes remain unchanged, with no new review performed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole prime-power finding](#prime-power-harmonic-whole-independent-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole prime-power finding](#prime-power-harmonic-whole-independent-finding) | [C132 actual Statement](../../claims/Yin_C_G0132_v1.md#statement) | Entire A--C: uniform chain bound with explicit constants, arbitrary exponents and correlated capacities, paid strong/weak forms and original-window capture. |
| [Whole prime-power finding](#prime-power-harmonic-whole-independent-finding) | [C132 actual complete Argument](../../claims/Yin_C_G0132_v1.md#argument) | All Sections2--7 and22 numbered formulas, complete finite boundaries, tensor and original-weight normalization, interval-union cost and conditional full norm. |
| [Whole prime-power finding](#prime-power-harmonic-whole-independent-finding) | [L159 actual capacities](../../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Complete occurring good-prime root counts, w_o<=phi(o), individual-root counting and orbit restrictions; no artificial inventory realization. |
| [Whole prime-power finding](#prime-power-harmonic-whole-independent-finding) | [L74 full original norm](../../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | All original lifted roots, good-prime initial depth at least1 including ell2, and exact total valuation at the same captured integer time. |
| [Whole prime-power finding](#prime-power-harmonic-whole-independent-finding) | [L168 finite original income](../../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Fixed eta*d income at n<=Cd, full original-field norm and possible powered-degree drop, with inherited Pri11 applicability/inspection limits. |

<a id="prime-power-harmonic-whole-independent-finding"></a>

## Whole finding

**PASS at the full declared scope.**
C132 v1 proves the length-independent geometric-chain estimate, its tensor consequence for arbitrary finite prime exponents and arbitrary correlated capacity arrays, and the stated original-time capture and conditional norm consequence.
No mathematical or direct-dependency correction is required.
The complete proof is present in this artifact; acceptance does not depend on treating the reviewer's earlier C129 as already accepted.
C129 is credited for provenance, while its mechanisms are actually rederived in the new domain.

The reciprocal-prime cost remains explicit and may diverge with an unrestricted prime pool.
The same-scale and fixed-number-of-intervals consequences are valid automatic specializations.
The theorem does not establish actual good-prime coverage, an unrestricted weak moment bound, or a Mahler gap.
This R recommends adoption; the responsible Claim decision, not this review, owns that adoption.

### 1. Constants, finite chain positivity and the coarse regime

For0<s<1, q=2/(2-s) lies strictly between1 and2, its conjugate q'=2/s exceeds2, and c=1-2^(s-1) lies strictly between0 and1/2.
Thus rho_0=c/8<1/16, while rho_max=2^(-s/2)>1/sqrt2; both are strictly below1 and rho_0<rho_max.
A_s,B_s,C_s are positive finite constants for each fixed s, with no assertion of uniformity as s approaches an endpoint.

The proposed vectors v_j have squared norm1 by the exact finite geometric sum.
For i<=j their coordinates through i scale by rho^(j-i), proving the Gram identity K(i,j)=rho^abs(i-j).
This establishes PSD, including every boundary row and arbitrary finite e.
At rho=0 the separately defined identity matrix gives PSD directly, so no0^0 ambiguity is used.

The off-diagonal row sum is at most2rho/(1-rho).
Summing2abs(x_i x_j)<=x_i^2+x_j^2 against the symmetric nonnegative entries proves the absolute off-diagonal form bound in equation7 for signed vectors.
Counting-measure norm monotonicity gives norm2<=normq.
For rho>=rho_0, B_s rho^(q') is at least2rho_max/(1-rho_max), so equation8 follows with no dependence on e.
It covers rho=rho_0 and rho=rho_max as well as their interior.

### 2. Large-tail branch of the new chain argument

For small rho, entrywise positivity permits replacing x by abs(x), after which normalizing sum x_i^q=1 and choosing a largest coordinate is legitimate because the vector is finite and nonzero.
Write A for that coordinate and t=1-A^q.

If A^q<=1/2, then sum x_i^2<=A^(2-q)sum x_i^q<=2^((q-2)/q)=2^(s-1)=1-c.
Also rho<=c/8<1/2 gives2rho/(1-rho)<=4rho<=c/2.
The off-diagonal contribution is at most4rho sum x_i^2<=c/2.
Thus the complete form is at most1-c/2, proving equation9.
This is the actual deficit used to absorb the whole row error, not an assumption that a particular coordinate dominates.
Equality A^q=1/2 lies in this valid branch and the next branch alike.

### 3. Small-tail branch, deleted position and exact maximization

If A^q>=1/2, then0<=t<=1/2.
The tail norm satisfies norm2^2<=t^(2/q).
Since2/q=2-s>1, (1-t)^(2/q)<=1-t and t^(2/q)<=2^(s-1)t.
Adding gives the full diagonal bound1-ct in equation10.
This includes t=0 and the shared endpoint t=1/2.

Removing the largest coordinate leaves a principal submatrix, with the original index distances; no relabeling makes its entries larger.
Its row sums are bounded by the same geometric row estimate.
Thus its off-diagonal form is at most4rho norm2(tail)^2<=4rho t<=(c/2)t, exactly equation11.
The unused middle position creates no additional interaction or length charge.

For the largest-tail term, Holder bounds the q'-power sum of the geometric coefficients by2rho^(q')/(1-rho^(q')), since each positive distance occurs at most twice.
At rho<=rho_max one has rho^(q')<=1/2, so the q'-root is at most4^(1/q')rho<=2rho.
The outside factor2A and A<=1 give4rho t^(1/q), proving equation12.
The interaction is zero directly at rho=0.

The remaining form is at most1-(c/2)t+4rho t^(1/q).
Substituting r=t^(1/q) and maximizing over all r>=0 enlarges the domain.
Differentiation gives r_*=[8rho/(qc)]^(1/(q-1)) and maximum(q-1)(c/2)[8rho/(qc)]^(q'), exactly A_s rho^(q').
For rho=0 the maximum is0.
There is no requirement that r_* lie in the original interval.
Equations8,9,13 and homogeneity therefore prove the full quadratic estimate uniformly in e.
When e=0, t=0 and the form is simply the square of its only coordinate, also covered.

### 4. PSD duality and tensor dimensions

The quadratic bound extends to signed real vectors by the nonnegative entries.
The PSD Gram form then gives abs(y^T Kx)^2<=(y^TKy)(x^TKx).
Using the established quadratic bound on each factor and taking square roots retains the constant1+C_s rho^(q'), not its square root.
Finite Holder duality over normq(y)=1 proves the lq-to-lq' operator bound.
Entrywise positivity by itself would not justify this step; actual PSD was proved separately in Section2.

For equation14, raising the displayed mixed norms to power q reduces the claim to the triangle inequality in l^(q'/q), which is a genuine norm because q'/q>1.
The direction is therefore l^(q')_j(l^q_i)<=l^q_i(l^(q')_j).
Applying the first operator, exchanging in precisely this direction, and applying the second yields equation15 with product AB and no counting-measure dimension factor.
Induction applies to arbitrarily many finite prime coordinates, even when their lengths differ.
The input array can be arbitrarily correlated; this is an operator tensor, not an independent input law.

The exponent-vector identity gcd(a,b)^s/(ab)^(s/2)=product_p p^(-s abs(v_p(a)-v_p(b))/2) holds at every pair of full exponents.
Each factor is the just-proved chain at rho_p=p^(-s/2)<=rho_max, with rho_p^(q')=1/p.
Tensorization yields D_s(Q), independent of every exponent bound e_p.
A final Holder inequality supplies the quadratic form in equation17.

### 5. Original capacity, zeros and the paid strong form

The exact lcm*gcd=ab identity turns the original energy into the G_s quadratic form at z_a=w_a/a^(s/2).
Since q-1=sq/2, its q power is w_a(w_a/a)^(q-1)<=w_a under w_a<=phi(a)<=a.
At w_a=0 the term is interpreted directly as0.
Summing and using2/q=2-s proves the actual W^(2-s) bound, without dividing by a layer mass or invoking a product law for w.

For unrestricted nonnegative f, the same calculation at w_a=phi(a)f(a) gives z_a^q=phi(a)f(a)^q[phi(a)/a]^(q-1)<=phi(a)f(a)^q, requiring no f<=1 assumption.
This proves precisely the finite paid strong form.
The product cost is bounded by exp(C_s sum_p1/p) using log(1+x)<=x, not by a prime-independent constant.

The L396 counterfamily and C104 product-profile result were compared at their actual scopes.
L396's global strong failure is consistent with this retained divergent-prime cost.
C104 has a different domain and sharper universal product-profile constant; C132 does not claim that constant for correlated inventories.
The empty prime pool gives the one-point tensor, W=w1<=1 and W^2<=W^(2-s).
The all-zero array gives the trivial energy bound and is properly excluded only from normalized densities.
Every operator and array is finite; no infinite-prime or infinite-chain convergence is asserted.

### 6. Original triple buckets and automatic finite-scale costs

For a pair with L=lcm(a,b)<=X, the exact third-label quotient r=c/gcd(c,L) satisfies lcm(c,L)=Lr.
Every label in one quotient bucket divides the actual integer Lr<=X, so its entire weight is at most H_X; at most floor(X/L) quotients are possible.
Combining with the original total W proves the min bound in equation19.
For L>X the left side is0.
The inequality min(1,z)<=z^s is valid for every z>=0 and0<s<1, including H_X=0.

Multiplying by the ORIGINAL ordered pair weights and summing gives equation20.
No repeated labels are omitted, and no separate-time incomes are averaged.
Positive delta_X forces H_X>0; rearrangement yields H_X>=(delta_X/D_s)^(1/s)W^2/X.
The hypotheses X<=CW and the explicit harmonic-cost upper bound then give equation6 with exponent-C_s L/s and factor1/C in the stated direction.

For real P>=2, b=floor P>=2 and floor(2P)<=2b+1.
Summing1/n under the integral from n-1 to n yields the harmonic bound log(floor(2P)/b)<=log(5/2), including missing primes and the empty pool.
A union of r such intervals costs at most r times this bound by nonnegativity, with any overlaps only overcounted.
The resulting constant is uniform only for fixed r.
There is no claim that arbitrary multi-scale support receives a bounded cost.
If a displayed capture fraction exceeds1 the parameter premises are inconsistent; taking its minimum with1 is harmless.

### 7. Direct arithmetic interfaces and full original norm

The reviewer reread actual L159 and L74 at the declared anchors.
For a good prime, squarefree reduction counts individual original roots, each full order group has w_o<=phi(o), and no further residue-degree multiplier is required.
Arbitrary exponents in the ORDER are permitted and are different from powers of the local good prime.
C132 retains complete selected occurring groups and does not assert that a formal capacity array is realized by a polynomial.

With W>=gamma*d and X<=C*d, the capture bound gives at least exp(-C_s L/s)delta^(1/s)gamma^2*d/C original selected roots at ONE integer n<=X.
At a good local prime ell, each captured root has normalized valuation at least1; L74 also covers ell2 and retains any deeper contributions.
All other original roots contribute nonnegatively.
Their total is exactly v_ell of the full original-field norm, so multiplying by log ell>=log2 gives the displayed eta without an extra orbit factor.

Nontorsion makes the resultant nonzero.
Its absolute value is a positive integer, and the norm remains in Q(alpha) even if alpha^n has smaller degree.
The auxiliary t^n-1 has original degree n<=Cd, content1 and squared coefficient norm2.
L168's exact finite-income criterion accepts any fixed positive eta at that same original time, retaining its powered-degree tower and existing Pri11 statement/applicability boundary.
It does not require the crude income-minus-dlog2 bound to be positive.
Thus equation22 and the conditional strict Mahler consequence are valid, without automatic coverage or an asserted near-one realization.

### 8. Completeness, provenance and remaining scope

The author explicitly rederives all internal finite norm and tensor steps, so the earlier C129 is provenance rather than an unresolved theorem premise.
The reviewer's antecedent authorship does not supply independent review of C129; its separate [R798 original squarefree-tensor](Yin_R_G0798_v1.md#squarefree-tensor-whole-independent-finding) finding remains its own evidence with its current unknown relationship.
Here the new chain argument and the actual whole arbitrary-exponent consumer were reconstructed from the fixed text, with no repair supplied.
The initial isolation facts for the new chain do not turn the whole finding, which also covers this reviewer's reused substantive mechanisms, into independent review.

The comparison-only C108 locator was checked after root corrected it to the actual nested-slice-continuation-statement anchor in C108v2.
That repair changes neither an input nor a mathematical assertion.
The declared direct dependency table covers L159,L74,L168, the actual external arithmetic interfaces used in Section7.
Known Holder, PSD Cauchy--Schwarz and finite Minkowski mechanisms are correctly stated and proved or expanded where needed; no uninspected new external theorem was introduced.
Existing Pri11 source-proof inspection is not upgraded.

The entire claimed finite and conditional scope passes.
Arbitrary prime exponents have been admitted at the paid harmonic-support cost, but diverging harmonic support, automatic original good-prime mass/density coverage and unrestricted G0001 remain open.
No native computation, numerical certificate, formal verification or Task completion is claimed.
No target file was edited by this reviewer.
