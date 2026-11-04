---
author: Yin
---

<a id="ope26d-u001"></a>
# Ope26d-U001: the entropy-rate dimension formula and its formal-source boundary

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Ope26d; [retained PDF](../../../literature/pdf/Ope26d.pdf).

Passages: Manuscript dated 24 September 2026 at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`; complete Sections 1--6, Theorem 1.1 and corollaries, printed/PDF pp. 1--20; associated Lean module and comparator descriptions at that commit.

Inspection: 2026-10-07, AI reviewers working for human author Yin at his explicit request to acquire and audit OpenAI Math families 153 and 148.
Coordinator completed the whole manuscript proof review and the stated static Lean checks.
A separate agent independently checked the finite-pair/conditional-window bridge with its actual interfaces.
Exact review arrangements and unchecked formal execution are recorded below.


## Assessment and exact statement

**Audited within scope; no mathematical defect found in the manuscript's complete proof of Theorem 1.1 and Section 6 corollaries.**
This is ordinary mathematical review with the established Feng--Hu input explicitly retained.
The formal-source inspection has the separate, narrower status below.

<a id="ope26d-entropy-rate-and-dimension"></a>
Let $\Phi=(\varphi_i)_{i\in\Lambda}$ be a finite nonempty indexed family on $\mathbb R$, $\varphi_i(x)=r_i x+t_i$, with $0<|r_i|<1$, and let $p_i>0$, $\sum_i p_i=1$.
Repeated maps, signed and unequal ratios, and exact overlaps are allowed.
Let $\mu=\sum_i p_i(\varphi_i)_*\mu$ be the unique invariant probability.
For independent $I_j$ of law $p$, define the **complete affine map** $G_n=\varphi_{I_1}\circ\cdots\circ\varphi_{I_n}$, combining probabilities of words that define the same slope and translation.
In base-2 logarithms,
$$h_{\mathrm{RW}}=\lim_n H(G_n)/n=\inf_{n\ge1}H(G_n)/n,\qquad
\chi=-\sum_i p_i\log_2|r_i|>0.$$
Subadditivity proves the limit; $0\le h_{\mathrm{RW}}\le H(p)$.
Theorem 1.1 states
$$\dim_H\mu=\min\{1,h_{\mathrm{RW}}/\chi\}.$$
The source defines lower Hausdorff dimension as the infimum of dimensions of Borel sets of positive measure.
Exact dimensionality makes this equal to the full-mass convention here.
A common change of logarithm base leaves the ratio unchanged.
Address entropy, translation entropy for unequal slopes, algebraic entropy of a discrete abelian flow, and $h_{\mathrm{RW}}$ must not be identified by notation alone.

## Complete manuscript proof review

The coordinator read all six TeX sections, compared the complete extracted PDF and visually checked selected formulas on pp. 2 and 18.
The following checks record the actual mechanism, including its quantitative and conditional interfaces.

1. **Upper bound and exact dimension (pp. 2--4).**
[FH09-U001](../FH09/Yin_U001.md#fh09-u001) checks the only external dimension-theorem input at its exact primary statement.
Passing to a block alphabet of distinct complete maps with combined weights, the law of large numbers for probabilities and contraction slopes gives the covering upper bound $d\le H(G_n)/(n\chi)$ for each fixed block length.
Taking the infimum proves $d\le h/\chi$.
The cases $h=0$ and a single map are included.

2. **Averaged scale entropy (Section 2, pp. 5--9).**
For compactly supported $X$, uniform smoothing yields $\bar H_s(X)=h(X+U_{[0,s]})-\log_2s$.
Signed affine scaling uses $|r|$.
For integer $t/s$, $G_{s,t}=\bar H_s-\bar H_t$ is an averaged conditional grid entropy, between 0 and $\log_2(t/s)$, concave in the law and nondecreasing under convolution.
The comparison with a fixed grid loses at most one bit.
The exact-dimensional entropy upper bound is obtained first on a set with mass $1-\eta$ and uniform ball bounds, then by compact support for the remaining mass.
It does not assume an unproved entropy-dimension limit.

3. **Uniform nonsaturation and two-point gain.**
If $d<1$, $\delta=\inf_{v>0}(1-G_{v,2v}(\mu))>0$.
Small deficit would make a uniform-smoothed law and its translate almost equal in total variation.
For fixed large integer $K$, a common part of $K$ translates then forces $G_{v,Kv}$ close to $\log_2K$.
Stopped self-similarity transfers this to every sufficiently small scale, with a loss independent of $K$; telescoping contradicts the dimension upper bound.
The stopping range uses the minimum contraction modulus and handles negative ratios.
The random-grid information calculation gives, for $0<s<v<t$, a two-point convolution gain at least $\Delta_v-s/v-v/t$.
The fine/coarse boundary errors are explicitly retained.

4. **Finite-law pair bound (Section 3, pp. 9--12).**
Let $c_\ell(\nu)$ be the maximum mass of a submeasure expressible as fair pairs of atoms whose distances lie in $[2^{-\ell},2^{1-\ell})$.
For every finite-support law on $F$, the source bounds $k(H(\nu)-H^0_\rho(\nu))$ by $\log_2|kF|+60000k^4\sum_{2^{-\ell}\le2\rho}c_\ell(\nu)$.
Random nested partitions have between 2 and 8 children and cut density at most $20/\rho_h$.
The exceptional coordinates are independent conditional on parent cells **before** observing their sum.
If $t$ is the sum of exception probabilities, two exceptions have probability at most $t^2$ and at most $t$.
The event determined by the observed sum costs no additional entropy flag.
Thus the entropy charge is linear in $t$.
The symmetric same-cell coupling gives a feasible fair-pair submeasure with the correct factor two.
Summing the geometric scale weights removes the finite isolating depth; no minimum-distance estimate enters the constant.

5. **Conditional block types (Section 4, pp. 12--15).**
Under the contradiction hypothesis $d\chi<h$, choose $\alpha>\chi$ with $d\alpha<h$ and then a block length $b$ so the type cost $m\log_2(b+1)$ is small.
Type counts fix the complete signed slope, and retain the original iid word law conditional on types.
The entropy inequality charges the type information even though types need not be functions of the affine map.
Averaging the unobserved future gives the original invariant measure, so fixed-grid conditional translation entropy is bounded by that of $\mu$ plus one bit.
The atypical contraction-depth event has probability tending to zero and bounded entropy cost per position.
The sumset estimate $|kS|\le(k+1)^{nm^b}$, with $k$ chosen before $n$, and the pair bound yield at least $cn$ expected pair capacity on a finite deterministic interval $[a_n,B_n]$.
Only finiteness of $B_n$ is proved or used.

6. **Conditional gain and disjoint windows (Section 5, pp. 16--19).**
A fixed type environment has a pathwise convolution decomposition of its prefix and tail.
Condition only through the prefix endpoint: selected pairs, their distances and signed slopes are then fixed while the same future tail remains unobserved.
Convexity of $\Delta_v=1-G_{v,2v}$ gives $\mathbb E(\Delta_v(\tau)\mid\mathcal F)\ge\Delta_v(\mathbb E(\tau\mid\mathcal F))\ge\delta$.
It does not require uniform nonsaturation of every quenched tail.
Take the window ratio $M^2$ integral and $M$ large enough to absorb the two-point error $5/M$.
Select any finite number $q$ of block lengths successively, after preceding finite $B_n$ values are known, so $a_{n_i}-A'n_i-1$ exceeds every earlier endpoint.
For each target scale, retained windows are pathwise disjoint because contraction depth is monotone; retention events are measurable under the conditional-gain sigma-algebra.
Each finite band is counted exactly once when target scales are summed.
Stationarity, without independence between windows, yields $\delta c qT/(4D)\le2T\log_2M$, impossible for arbitrary $q$.
This closes the lower bound, including critical and supercritical entropy rates.

7. **Corollaries (Section 6, pp. 19--20).**
With no exact overlaps, complete maps label words injectively and $h=H(p)$.
Equality of maps for distinct words of unequal lengths can be converted to a same-length equality via their two concatenations; if those words commute, their common word powers and strict contraction rule out equal maps unless the words coincide.
The attractor formula uses weights $|r_i|^s$ together with the ordinary covering upper bound.
The homogeneous all-weight and three-map specializations satisfy the same hypotheses.
These are dimension statements and make no assertion of absolute continuity.

## Additional independent check of the critical bridge

The separately assigned source reviewer rederived all of pairs.tex and windows.tex, the used entropy/type interfaces, and visually checked pp. 10, 16 and 18.
It knew the coordinator's prior no-gap verdict but was not supplied its derivations; this was not a blind review.
It did not develop the source argument.
Its independently checked scope is Lemma 3.2, Proposition 4.2, Lemmas 5.1--5.2 and the final count, including the order of finite-band choices.
It found no defect.
It did not separately audit all corollaries, original Feng--Hu proof, or Lean sources.
The detailed retained cross-check follows below; it supplements the complete coordinator review rather than widening its own scope.

## Lean source inspection and execution boundary

At the same fixed commit, lean/docs/148.md and the two ComparatorChallenges descriptions identify the main theorem and its no-overlap corollaries.
All 64 files under lean/OAI/MeasureTheory/SelfSimilar were downloaded.
Static review of Model.lean, Main.lean, EntropyGap.lean and the used definition interfaces confirms that the terminal theorem concerns actual affine composition, collision-merged map entropy, Lyapunov exponent and Hausdorff dimension.
A search of those 64 solution modules found no `sorry`, `admit`, declared `axiom`, `unsafe`, `implemented_by`, `extern`, or `Lean.ofReduceBool`.
This text search is not a kernel or transitive-axiom check.

The main solution is `OAI.EntropyRateDimension.entropy_rate_dimension` in `OAI.MeasureTheory.SelfSimilar.Main`.
The comparator description lists `propext`, `Quot.sound`, `Classical.choice` as permitted axioms and sets `enable_nanoda` to false.
The challenge-side `sorry` is an intentional comparator template, not evidence of a hole in the solution.
The inspected toolchain is Lean v4.34.1 and the pinned mathlib revision is `d13f23b723b8a846827a245b89c10fc7d3f11612`.

**Not locally rebuilt or comparator-verified.**
The installed toolchain list contained v4.24.0, v4.32.1 and v4.32.2, not v4.34.1.
No toolchain installation, lake build, proof export, transitive axiom audit or Comparator execution was performed.
A terminal proof source, permitted-axiom list and absence of the searched words do not establish successful elaboration or semantic equivalence.
The source's formalization claim remains distinct from this local static inspection.
The ordinary manuscript audit is not labeled as formally verified.

## Use for G0001 and remaining boundaries

The result supplies a dimension formula once the exact random-walk entropy is known.
It does not give a degree-independent lower bound for positive algebraic entropy, identify every digit-law entropy with Mahler measure, or turn singularity into a strict dimension drop.
Hence it does not by itself resolve [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).
The separate family153 singularity conclusions are compatible with full Hausdorff dimension.
Applying the formula to a new local entropy mechanism requires its own hypotheses and derivation.

The only non-elementary external dimension input retained by the manuscript proof is the exact-dimensionality theorem checked in FH09-U001.
Historical and survey citations are context rather than adopted proof premises here.
Their priority claims and full proofs were not recursively audited.
No erratum or different edition was substituted for the fixed inspected commit.
These source units do not resume the paused autonomous research run or alter prior mathematical decisions.

## Detailed independent bridge review

## Lemma 3.2: finite-law pair bound

Locators: PDF pp. 9-12, especially equations (3.3)-(3.7) on pp. 10-11; `pairs.tex` lines 37-231.

1. **Random partition geometry.**
   The parent-length ratio to the next scale lies in [2,8].
   A nearest integer N remains in [2,8], and dividing by N puts unperturbed lengths inside the claimed conservative range [.75,1.25] times the next scale.
   Independent internal cut perturbations change each length by at most .2 scale, keeping cuts ordered and all child lengths in [.5,2] scale.
   The cut density is exactly 5/rho_{h+1}=20/rho_h.
   Shared parent cuts are reused for all coordinates in that parent; nothing requires separate cuts for them.

2. **Entropy chain and later cuts.**
   Conditional on a fixed scheme, initial coordinate cell labels are independent and have entropy k H^0_rho(nu).
   Observing the exact sum costs at most log|kF|.
   The refinement chain terminates once all cells isolate atoms; the required J is finite for each finite F but need not be quantitatively bounded.
   Sampling the scheme independently of the samples permits averaging this finite identity.
   Later cuts, conditional on the earlier cuts, are still independent of the sample vector and its sum, so dropping them from the relevant level's conditioning is valid.

3. **Independence is used before observing the sum.**
   Conditional on a tuple of parent cells, coordinates remain independent.
   After the new cuts are fixed, the common threshold a is a deterministic function of those cells, means and cuts.
   Thus exceptional-coordinate events remain independent at precisely the stage used to bound q=P(at least two exceptions)<=sum_{i<j}p_i p_j<=t^2 and q<=t.
   The source never needs these events to be independent after Y is observed.

4. **The entropy flag estimate.**
   On E-complement and B-complement all child labels equal the labels of their means: a changed label needs one deviation of size at least a, and at most k-1 deviations smaller than a/(4k) cannot cancel that below a/2.
   Each coordinate has at most eight child labels.
   The E flag costs h2(q)<=3 sqrt(q)<=3t bits.
   The event B is a function of the already observed sum Y and so has no additional binary-entropy cost.
   Its probability is <=t.
   This yields the claimed linear bound <=9k sum_i p_i; the conditioning direction and half-open boundary cases are valid.

5. **Cut averaging and pair conversion.**
   A union bound over at most 7k cut/mean instances gives probability <=1120 k^2 u/rho_h that a<=4ku.
   This remains valid when a cut is shared by several coordinates; repeated instances merely weaken the bound.
   Jensen yields E|X_i-m_i|<=E|X_i-X_i'| for an independent copy in the same cell.
   Averaging parent cells gives the symmetric same-cell coupling pi_h with both marginals nu.
   Its distance-band portion assigns unordered edge weight 2pi_h(x,y), a feasible fair-pair submeasure; no missing factor two occurs.

6. **No hidden separation-rate dependence.**
   The per-level bound is 20160 k^4 sum_{2^{-ell}<=2rho_h}(2^{-ell}/rho_h)c_ell(nu).
   For fixed ell, the ratio grows by four and is retained only while <=2; its geometric sum is <=8/3.
   Hence 60000 k^4 is a valid C_k.
   The auxiliary separating depth J disappears.
   Singleton F and empty distance bands cause no exceptional case.

### Section 2 and Section 4 interfaces

Locators: PDF pp. 5-9, Lemmas 2.1-2.4; pp. 12-15, Lemma 4.1 and Proposition 4.2.

The averaged entropy identity uses bounded uniform smoothing, so all differential entropies are finite even for atomic laws.
For integer scale ratio N, the two translated grids are nested and G is an averaged conditional entropy.
Conditioning on a mixture label proves concavity in the law; translation invariance then proves monotonicity under convolution.
All uses of this concavity here have ratios 2 or M^2 (the nonsaturation argument also uses an integer K).

For nonsaturation, Delta_v equals the information carried by the fair mixture of X+V_v and its translate by v.
A small deficit implies a small total-variation distance by the explicitly checked binary-entropy curvature bound.
For fixed K, the K translates have common mass tending to one, giving G_{v,Kv} approaching log K.
Stopped self-similarity transfers this to all smaller scales with an additive loss independent of K.
The source's exact-dimensional entropy upper bound contradicts that transfer when d<1.
Signed contractions are handled by the signed scale identity, and the stopping time is uniformly bounded for every fixed target scale.
No separation assumption enters this deduction.

The two-point gain compares information from independently shifted fine and coarse grids.
A fine cell crosses a coarse boundary on a fraction s/v of shifts; adjoining X bounds the coarse gain by v/t.
These give the stated Delta_v-s/v-v/t bound.
Unused grid shifts remain independent, so the information chain rule used here has the stated conditioning.

For block types, counts fix the complete signed slope.
Conditional on the type prefix, translation and complete affine map determine each other even when different addresses collide.
The chain-rule cost is at most n*m*log(b+1), independent of whether the type prefix is a function of the map.
Conditioning only through the prefix endpoint leaves the original future coding law equal to mu, giving E H_s^0(nu_{omega,n})<=H_s^0(mu)+1 through translation comparison and entropy concavity.
The law of large numbers and the linear upper bound on exact entropy permit removal of the high-contraction-depth event without losing the positive linear deficit.

The conditional support satisfies log|kS|<=n*m^b*log(k+1), including arbitrary collisions and negative slopes.
Fixing a sufficiently large k before n makes this smaller than half the amplified deficit.
Applying Lemma 3.2 then gives linear expected pair mass.
For fixed n there are finitely many type prefixes, each producing a finite support, so their nonempty distance bands have a deterministic finite maximum B_n.
This proves Proposition 4.2's exact finiteness assertion; it does not introduce a rate or a uniform bound on B_n.

### Lemma 5.1: the same unobserved future and Jensen direction

Locators: PDF pp. 16-17, equations (5.1)-(5.4); `windows.tex` lines 20-127.

The identity tau_j=(D_{R_j}nu_{shift^j omega,n})*tau_{j+n} is pathwise for a fixed environment.
Under F_{j+n}, the finite prefix law, its pair decomposition, both signed products, and every chosen pair distance are fixed.
A maximizer can be chosen measurably because there are finitely many relevant type prefixes.

For ell=L-ceil(sigma_j), scaling the band gives v/r in [1,4), so r/M<v<Mr and the two-point error is <=5/M.
Reordering pair endpoints handles a negative slope without changing the positive distance v.

Only the future type sequence remains unobserved.
It is independent of F_{j+n}, so the conditional mean of the very same tail used in the pathwise convolution identity is D_{R_{j+n}}mu.
Since G_{v,2v} is concave, Delta_v=1-G_{v,2v} is convex, and Jensen has exactly the required direction:

    E[Delta_v(tau_{j+n}) | F_{j+n}]
      >= Delta_v(D_{R_{j+n}}mu)
      = Delta_{v/|R_{j+n}|}(mu) >= delta.

The pair distance v is fixed under this conditioning, so this is not an illicit Jensen step with a varying functional.
The proof does not assert nonsaturation for each conditional tail.
Concavity of the window gain and nonnegative convolution gain for the normalized residual measure then yield delta/2 times the selected pair capacity.
Zero residual mass is harmless.

### Lemma 5.2 and the finite-band quantifiers

Locators: PDF pp. 17-19, equations (5.5)-(5.11); `windows.tex` lines 129-299.

All constants A>A', D, c, delta and M are fixed before the arbitrary integer q is chosen.
The lengths n_i are selected successively: when choosing n_i, the finitely many earlier B_{n_h} are already fixed, whereas a_n-A'n-1 tends to infinity.
No growth upper bound on B_n is used or needed.
An even integer T is chosen only after these finitely many bands are fixed.

For a fixed environment and target L, x_j=L-ceil(sigma_j) is nonincreasing.
A retained finer-band window ends with x_{j+n_i}>=a_{n_i}-A'n_i-1>B_{n_h} for every coarser band h<i.
A retained coarser start k satisfies x_k<=B_{n_h}, forcing k>j+n_i.
Thus cross-band windows are pathwise disjoint; starts within one band are multiples of its length and also give disjoint half-open windows.
Monotonicity of g_j telescopes all retained gains to at most 2log M.

The retention event is F_{j+n_i}-measurable, exactly the sigma-algebra required in Lemma 5.1.
Multiplying its conditional inequality by the indicator and applying the tower property is therefore legitimate.
For each candidate start, sigma_j<=Dj<=T/2 and T is even, so ceil(sigma_j)<=T/2.
Each integer ell in the band occurs exactly once as L-ceil(sigma_j) for L=1,...,T; a_n>=1 and B_n<T/2 put that target inside the chosen range.
Stationarity supplies the expected cn_i mass at each candidate; independence between distinct windows is not assumed.

There are floor(T/(2Dn_i))+1>=T/(2Dn_i) candidates per band.
Thus the gain lower bound is delta*c*q*T/(4D), while the upper bound is 2T log M.
Canceling the finite positive T bounds the arbitrary q by a constant chosen before q, producing the claimed contradiction.
The same-future conditioning, Jensen direction, endpoint rounding, finite-band order of choices, and absence of a smallest-distance estimate are all explicitly covered by this cross-check.
