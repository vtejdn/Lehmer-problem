---
author: Yin
---

# Complete finite midpoint radial profiles and the actual signed lower-moment diagnostic

Human author Yin.
The original_law_continuation contributor developed MP1--MP4 and the native profile calculation.
Root read the complete saved mathematics and new native program before fixing this initially OPEN candidate.
The [D2 supplement](../drafts/Yin_D_G0002.md#complete-original-midpoint-profile-256) is provenance only.
The declared finite scope is unchanged from adopted C776, and its old program/output and original reviews remain intact.
Independent whole mathematical/native review and separate adoption are required for this supplement.

## Statement

Fix the actual quartic P=t^4-t^3-t^2-t+1, exterior root beta, neutral conjugate zeta and COMPLETE original bridge law of adopted C776, with independent digits of probabilities1/4,1/2,1/4 and no deleted zero visits or endpoint fibers.
For n in{16,32,64,128} put Y_n=|X_n(zeta)|^2/n conditioned on X_(2n)=0.
The complete deterministic height48, total time<=256 and100000 reached-state cap are unchanged.
The exact fourth moments, median and90-percent quantiles, six radial tail probabilities and signed coefficient intervals in the explicitly displayed tables of this material all hold, with rational OPEN interval endpoints except the exact median1/16 at n16.
The quantile convention is the least radial mark whose cumulative original weight is at least the specified probability.
Tail events use >=, including exact threshold equality.
Every field comparison and moment is computed in Q(sqrt13) before enclosure, with zero omitted mass in this finite scope.

In particular Pr(Y_n>=1/10)>1/2 for n64 and128.
For EACH of the four declared n,

    E[Y_n 1_(Y_n>=1)]<(1/10)E[Y_n],
    E[Y_n 1_(Y_n>=2)]<(3/1000)E[Y_n].

Thus more than90 percent of each observed second moment is supplied by Y_n<1 and more than99.7 percent by Y_n<2.
These are finite assertions about the actual full profiles, not an asymptotic tail or diffusion theorem.

The genuine C300 signed original coefficient mathcal_B_n and real-place companion T_n agree EXACTLY with MP4 and satisfy

    E[Y_n]=T_n/n-sqrt13 mathcal_B_n/(nW_(2n)),
    |T_n|<BS<430500/130321.

All native signs, weights and both real neutral coordinates are retained in this identification.
The finite negative signed ratios do not imply mathcal_B_n<=-epsilon nW_(2n) at arbitrarily large n.
No uniform positive tail lower bound, positive asymptotic midpoint moment, Gaussian law, critical-mean classification, strict R<beta or R=beta, varying near-one bound or unrestricted G0001 conclusion is asserted.

## Complete argument and exact finite tables

### Exact original law and algebraic comparisons

Put Y_n=|X_n(zeta)|^2/n under the COMPLETE original law conditioned on X_(2n)=0, and retain the actual graph, forward weights F_n(q), terminal weights B_n(q) and W_(2n) of C776 MC1--MC3.
The original digit law remains1/4,1/2,1/4; no original word, earlier zero visit, endpoint fiber or coordinate is deleted.
Reusing that complete deterministic height argument gives zero omitted return mass for this unchanged scope.
The new program imports the unchanged experiment.py graph helpers and midpoint_continuation.py coordinate/mark functions, never their main functions or old output files.
It rebuilds the same graph and integer forward/backward weights and checks its graph counts and exact p64,p128,p256 against the fixed values.
Thus reproduction does not require an already generated old output.

Write the exact neutral square at q as

    r(q)^2=(A(q)+B(q)sqrt13)/2,
    w_n(q)=F_n(q)B_n(q), W=sum_q w_n(q)=W_(2n).

Squaring in the real quadratic field gives the complete fourth moment

    E[Y_n^2]=[sum_q w_n(q)(A(q)^2+13B(q)^2)
             +sqrt13 sum_q w_n(q)2A(q)B(q)]/[4n^2 W].     (MP1)

The two integer sums and both resulting rational field coefficients are retained in the output.
The program also checks E[Y_n^2]>=E[Y_n]^2 by exact quadratic-field sign, rather than by rounded decimals.

For a positive rational threshold t=a/b in lowest terms, with b>0, the event Y_n>=t is EXACTLY

    b A(q)-2na+b B(q)sqrt13>=0.                         (MP2)

For rational x,y the sign of x+y sqrt13 is computed without any approximation as follows.
If y=0 use the sign of x; if x=0 use the sign of y; if x and y have the same nonzero sign use that common sign.
When their signs differ, use sign(x) sign(x^2-13y^2), obtained by multiplying by x-y sqrt13, whose sign is then sign(x).
The norm is nonzero in this last case because sqrt13 is irrational.
This covers equality at rational thresholds as well as zero states and retains the requested non-strict >= event.
Every threshold probability is the exact rational sum of its complete integer weights divided by W.
The same event weights retain the exact first-moment contribution E[Y_n 1_(Y_n>=t)].
Rational enclosures are produced only after these exact memberships and weighted sums are decided.

For the median and90-percent quantile, the program groups equal pairs(A,B), orders them by this same exact sign comparison, and takes the least mark whose cumulative weight is at least the desired fraction of W.
Equality of quadratic values is equality of both rational coefficients, so no distinct radial marks are accidentally merged by a numerical tolerance.
Each output quantile includes its exact Q(sqrt13) value, the mass strictly below it and the mass at or below it, with the former strictly smaller than the requested probability and the latter at least that probability.
The unchanged rational bracket for sqrt13 is used only to enclose the resulting exact field elements.

### Complete finite fourth moments and radial masses

The following open intervals have rational decimal endpoints and enclose the complete fourth moments E[|X_n(zeta)|^4]/n^2.
The median at n16 is exactly1/16; every other displayed quantile is enclosed in the indicated open rational interval.

| n | E[Y_n^2] | Median of Y_n | 90-percent quantile of Y_n |
| ---: | --- | --- | --- |
|16|(0.061732,0.061733)|1/16|(0.475346,0.475347)|
|32|(0.079301,0.079302)|(0.103211,0.103212)|(0.340885,0.340886)|
|64|(0.098866,0.098867)|(0.170442,0.170443)|(0.562933,0.562934)|
|128|(0.105968,0.105969)|(0.162630,0.162631)|(0.537130,0.537131)|

The following entries are open rational intervals for the COMPLETE probabilities Pr(Y_n>=t), not empirical samples or masses of selected representative states.

| n | t=1/20 | t=1/10 | t=1/5 | t=1/2 | t=1 | t=2 |
| ---: | --- | --- | --- | --- | --- | --- |
|16|(0.547766,0.547767)|(0.443721,0.443722)|(0.421337,0.421338)|(0.056828,0.056829)|(0.006894,0.006895)|(0.000118,0.000119)|
|32|(0.657545,0.657546)|(0.637166,0.637167)|(0.350770,0.350771)|(0.079645,0.079646)|(0.014030,0.014031)|(0.000101,0.000102)|
|64|(0.822607,0.822608)|(0.633273,0.633274)|(0.310902,0.310903)|(0.130928,0.130929)|(0.010925,0.010926)|(0.000157,0.000158)|
|128|(0.816225,0.816226)|(0.577449,0.577450)|(0.386639,0.386640)|(0.107237,0.107238)|(0.012949,0.012950)|(0.000215,0.000216)|

In particular Pr(Y_n>=1/10)>1/2 for n64 and128, by integer weight comparisons.
For EVERY one of these four declared n, the exact quadratic-field comparisons also prove

    E[Y_n 1_(Y_n>=1)] < (1/10)E[Y_n],
    E[Y_n 1_(Y_n>=2)] < (3/1000)E[Y_n].                 (MP3)

Consequently more than90 percent of each observed second moment is supplied by Y_n<1, and more than99.7 percent by Y_n<2.
These are finite statements about the actual complete profiles, making precise the exclusion of an explanation based only on the farthest observed radial tails.
They do not establish a limit shape, a Gaussian law, monotonicity of the quantiles, or any uniform tail lower bound at later times.

### Direct connection to the existing lower-moment analytic interface

The [C285 complete lower-moment test](Yin_C_G0285_v1.md#diffusive-lower-moment-null-test) already shows that positive limsup E[Y_n] implies infinite critical mean, with a paid positive tail bound from its all-n fourth-moment estimate.
Its [finite-mean theorem](Yin_C_G0285_v1.md#whole-midpoint-moments-and-localization) implies E[Y_n^p]->0 for every fixed p>0, in particular both E[Y_n] and E[Y_n^2]->0, under the finite-mean hypothesis.
The new tables are finite measurements of these actual quantities; their positive values supply none of the required infinitely-many-n premises.
Equally, a positive lower bound for Pr(Y_n>=1/10) on an unbounded sequence would suffice, since E[Y_n]>=(1/10)Pr(Y_n>=1/10).
The observed probability greater than1/2 at two times cannot be promoted to such a sequence.

More arithmetically, use the actual [C300 two-integer diagnostic](Yin_C_G0300_v1.md#integer-midpoint-moment-diagnostic), not the deterministic covariance proxy.
For original coordinates x=a_0+a_1 beta+a_2 beta^2+a_3 beta^3, define s_l=sum_j a_j a_(j+l), A_0=s_0+s_2+3s_3 and B_0=s_1+s_2+s_3.
The present integer mark uses A=2A_0+B_0 and B=-B_0.
Thus C300's genuine signed coefficient and its real-place companion are

    mathcal_B_n=sum_q w_n(q)B_0(Psi(q))=-sum_q w_n(q)B(q),
    T_n=[sum_q w_n(q)A(q)-sqrt13 sum_q w_n(q)B(q)]/(2W),
    E[Y_n]=T_n/n-sqrt13 mathcal_B_n/(nW),
    |T_n|<BS<430500/130321.                              (MP4)

The full reciprocal-fiber product of C300 and the present forward/backward quotient product describe the same original midpoint state by C423/C776's bijection.
The first equality therefore retains the original signed integer numerator rather than renaming an unrelated scalar diagnostic.
The bound on T_n is the actual two-real-strip bound; the native output independently checks that its exact field enclosure lies strictly inside the displayed rational interval.
It does not treat x_+x_- as a nonnegative squared norm.

The exact rational ratios mathcal_B_n/(nW) lie in these open rational intervals:

| n | mathcal_B_n/(nW) |
| ---: | --- |
|16|(-0.040071,-0.040070)|
|32|(-0.049122,-0.049121)|
|64|(-0.059066,-0.059065)|
|128|(-0.063001,-0.063000)|

The precise analytic target is C300's already established condition mathcal_B_n<=-epsilon nW for a fixed epsilon>0 at arbitrarily large n, with every actual endpoint and original word weight retained.
MP4 identifies which complete signed count must be estimated; the present finite signs and magnitudes do not prove that condition.
The inspected [C300 original block minorization](Yin_C_G0300_v1.md#quartic-uniform-positive-covariance) explicitly bounds a fixed-diameter disjoint-block certificate by2L^2 and retains the factor p_(2m) in growing centered-block minorization.
The inspected [C45 complete-fiber boundary](Yin_C_G0045_v1.md#complete-fiber-reuse-and-scope) also excludes its specified small-support full-fiber covariance certificates from giving diffusion; it leaves nonzero-endpoint means and genuinely larger-support estimates separate.
C673's paid translation-copy expense is unchanged.
Accordingly a subsequent analytic attempt must estimate this actual signed endpoint sum, or the covariance of actual nonzero-endpoint conditional means with adequate support, rather than summing unpriced local copies or replacing the original law by a Gaussian proxy.
No such new uniform estimate is asserted here.

### Reproduction and current limits

Run from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/midpoint_profile.py
```

Only the Python standard library and the two explicitly named same-group source imports are used.
The default output is the separate midpoint_profile.json under this J group's existing output home; --output selects an explicit alternative.
The script writes its canonical output only after completing the declared graph, recurrences, exact memberships, moments, signed coefficients and quantile checks.
It checks the original graph counts, fixed complete returns, midpoint product totals, nonnegative radial marks, tail nesting, second/fourth-moment inequality, exact quantile brackets, real-strip mean bound and MP3.
Terminal decimals are labeled display-only; every mathematical decision uses integers, rational numbers or the exact sign rule above.
The original reviewed MC program/output and preceding MC section are unmodified by this supplement.
No new longer time, enlarged state cap, independent review, mean classification or unrestricted Task conclusion is claimed.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision midpoint-profile-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T09:22 |
| status | open |
| reason | Fix the same-scope complete MP1--MP4 radial-profile supplement, exact fourth moments/threshold probabilities/quantiles and tail contributions, and the actual C300 signed coefficient connection. Independent mathematical/native review remains outstanding. The finite profiles show substantial mass at the observed scaled radii but supply no unbounded sequence or original critical-mean decision. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete finite profile statement](#statement) | Exact four midpoint times, complete original law, all finite tables and >= threshold convention, quantiles, tail-moment inequalities, signed original coefficient and real-place bound, with every asymptotic exclusion. |
| argument | [Complete MP1--MP4 and finite tables](#complete-argument-and-exact-finite-tables) | Same finite coverage, exact quadratic-field signs/moments/grouped quantiles, full original weight sums, strict data/certificate tables, exact C300 interface and remaining lower-moment limits. |
| dependency | [Adopted complete original midpoint law](Yin_C_G0776_v1.md#decision-whole-reviewed-2026-10-26) | Same fixed quartic/full original graph, height48 finite completeness, exact reverse map/neutral mark, original weights and time scope, verified complete returns and positive midpoint supports. |
| dependency | [Adopted actual signed moment diagnostic](Yin_C_G0300_v1.md#decision-complete-retained-proof-adoption) | Integer-midpoint diagnostic, real-place companion and exact signed lower-moment implication; original block bounds retain their paid scope. |
| support | [Adopted moment interpretation](Yin_C_G0285_v1.md#decision-sufficient-projection-home) | Existing finite-mean subdiffusive moments and positive-limsup/null-mean test with all required infinite-time premises; no premise supplied by finite tables. |
| support | [Actual complete-fiber limitation](Yin_C_G0045_v1.md#complete-fiber-reuse-and-scope) | Existing small-support full-fiber covariance limitation, not a prohibition on every larger-support method. |
| support | [Paid chronological-copy constraint](Yin_C_G0673_v1.md#decision-whole-reviewed-2026-10-24) | Existing original-time translation scale and actual Doob/stationary costs, retained for the analytic next-step interpretation. |
| support | [New native profile program](../computations/programs/Yin_J_G0052/midpoint_profile.py) | Entire same-scope exact author fourth/tail/quantile/signed-coefficient implementation, with explicit original graph and mark source imports. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | All original weighted field sums, rational probabilities, exact quantiles/cumulative masses, strict moment and signed-coefficient certificates; generated evidence requiring independent check. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/midpoint_profile.json`; this target locates its run account. |
| support | [Existing graph helper](../computations/programs/Yin_J_G0052/experiment.py) | Unchanged exact graph, rational strips and100000 cap, reused only atheight48. |
| support | [Existing mark helper](../computations/programs/Yin_J_G0052/midpoint_continuation.py) | Unchanged integral original-coordinate and Qsqrt13 neutral-mark functions imported by the new program; no old main/output execution required. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T09:46 |
| status | proved |
| reason | Root read the complete fixed MP1--MP4 statement/proof and whole independent mathematical/native R999 and adopts the four complete original-law radial profiles and actual signed coefficient diagnostic without substantive repair. The independently reconstructed integer and quadratic-field payloads support every finite table and strict contribution inequality. No unbounded-time sequence, critical-mean branch, equality or strict inequality R versus beta, or unrestricted Task conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete finite profile statement](#statement) | Exact four midpoint times, complete original law, all finite tables and >= threshold convention, quantiles, tail-moment inequalities, signed original coefficient and real-place bound, with every asymptotic exclusion. |
| argument | [Complete MP1--MP4 and finite tables](#complete-argument-and-exact-finite-tables) | Same finite coverage, exact quadratic-field signs/moments/grouped quantiles, full original weight sums, strict data/certificate tables, exact C300 interface and remaining lower-moment limits. |
| dependency | [Adopted complete original midpoint law](Yin_C_G0776_v1.md#decision-whole-reviewed-2026-10-26) | Same fixed quartic/full original graph, height48 finite completeness, exact reverse map/neutral mark, original weights and time scope, verified complete returns and positive midpoint supports. |
| dependency | [Adopted actual signed moment diagnostic](Yin_C_G0300_v1.md#decision-complete-retained-proof-adoption) | Integer-midpoint diagnostic, real-place companion and exact signed lower-moment implication; original block bounds retain their paid scope. |
| support | [Adopted moment interpretation](Yin_C_G0285_v1.md#decision-sufficient-projection-home) | Existing finite-mean subdiffusive moments and positive-limsup/null-mean test with all required infinite-time premises; no premise supplied by finite tables. |
| support | [Actual complete-fiber limitation](Yin_C_G0045_v1.md#complete-fiber-reuse-and-scope) | Existing small-support full-fiber covariance limitation, not a prohibition on every larger-support method. |
| support | [Paid chronological-copy constraint](Yin_C_G0673_v1.md#decision-whole-reviewed-2026-10-24) | Existing original-time translation scale and actual Doob/stationary costs, retained for the analytic next-step interpretation. |
| support | [New native profile program](../computations/programs/Yin_J_G0052/midpoint_profile.py) | Entire same-scope exact author fourth/tail/quantile/signed-coefficient implementation, with explicit original graph and mark source imports. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | All original weighted field sums, rational probabilities, exact quantiles/cumulative masses, strict moment and signed-coefficient certificates; generated evidence independently reconstructed in R999 at the same finite scope. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/midpoint_profile.json`; this target locates its run account. |
| support | [Existing graph helper](../computations/programs/Yin_J_G0052/experiment.py) | Unchanged exact graph, rational strips and100000 cap, reused only atheight48. |
| support | [Existing mark helper](../computations/programs/Yin_J_G0052/midpoint_continuation.py) | Unchanged integral original-coordinate and Qsqrt13 neutral-mark functions imported by the new program; no old main/output execution required. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G0999_v1.md#complete-profile-and-signed-diagnostic) | Entire fixed statement and MP1--MP4, every finite table, exact non-strict events/grouped quantiles, actual original reciprocal-fiber signed coefficient and real companion, independent native reconstruction and retained analytic boundaries. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0052](../computations/programs/Yin_J_G0052/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
