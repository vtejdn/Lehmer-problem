---
author: Yin
---

# Independent whole review of the actual endpoint-product and linear doubling-overlap bounds

Date and human record author: 2026-10-23T21:45; Yin.
The exact target is [C645v1](../../claims/Yin_C_G0645_v1.md), with its [linear-overlap registration](../../claims/Yin_C_G0645_v1.md#decision-linear-overlap-registration), complete Statement and Sections 1--5 of the argument.
The inspected physical v1 was open at this review.
This review supplies evidence only and neither selects adoption nor changes the Task or execution state.

## Arrangement and coverage

A separate agent outside this proof's substantive development received the fixed target path, operational scope and applicable repository rules.
No D37, author development discussion, mathematical development summary, other-agent inventory or earlier R finding was read for this review.
Fixed mathematical materials and their necessary input interfaces were inspected directly.
Assessment histories and review links embedded in those fixed materials were visible; no previous R conclusion was substituted for checking the present argument.
The reviewer contributed no repair and did not edit C645 or its inputs.

The review reconstructs every positive assertion in the target: the full original endpoint profile, two-factor product identity, actual-core summation, all-n and asymptotic constants, true-radius normalization, finite dyadic remainder, and the exact limitations concerning mass and congestion.
It checks all selected dependency/support interfaces at the scopes declared below.
It is not a recursive proof or source audit of every theorem contained in those supporting materials.
No native computation is needed or used.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#linear-overlap-whole-independent-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C645v1 statement](../../claims/Yin_C_G0645_v1.md#statement) | Entire fixed-quartic statement for every n>=1 and x in O, complete original counts, all constants, limiting quantifiers, true radius, finite J remainder and all nonconclusions. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C645v1 argument](../../claims/Yin_C_G0645_v1.md#argument) | Complete Sections 1--5 and equations (1)--(10), all original-law/input applications, singular early lengths, actual-core Gaussian sum and exact dyadic time accounting. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C432v1 endpoint profile](../../claims/Yin_C_G0432_v1.md#complete-neutral-covariance-profile) | Original full endpoint MGF, actual deterministic covariance and singular-case applicability; directly rechecked the specialization used here. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C419v1 original endpoint MGF](../../claims/Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Entire finite Fourier/absolute-value/subset-expansion/zero-digit-removal proof used for the endpoint bound, with the complete p_n factor and original probabilities. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C602v2 actual-core packing](../../claims/Yin_C_G0602_v2.md#neutral-packing-and-load-lower-bound) | Used integer-norm separation and all-radius actual-core packing, rederived with both real embeddings and the neutral pair; later mass/load arguments in that section are not imported as a conclusion. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C204v1 actual midpoint product](../../claims/Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse) | Complete original midpoint orientation, core support, full return normalization and product identity; rederived by splitting unconditioned original words. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C555v1 true-radius dyadic identity](../../claims/Yin_C_G0555_v1.md#dyadic-critical-normalization) | Exact entropy convention, nonnegative weighted dyadic telescope, fixed-n limit and chronological observation times; rechecked locally, without identifying R with beta or using its older polynomial remainder as the new estimate. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C285v1 phase and moment interface](../../claims/Yin_C_G0285_v1.md#midpoint-proxy-explicit-linear-scale) | Existing finite geometric phase bound rechecked; midpoint proxy/moment claims inspected only as the stated reuse/comparison boundary, without adding a new moment conclusion. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C432v1 prior polynomial order](../../claims/Yin_C_G0432_v1.md#degree-cost-reduced-original-core-norm) | Existing unit/q=2 E_n and entropy interface checked to confirm that order 1/n for a_n was already available; no new whole audit of its grid/operator proof is claimed. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C627v2 comparison](../../claims/Yin_C_G0627_v2.md#statement) | Exact full original conditional-tail/label conventions and unresolved cross-label load inspected as comparison, not as an input proving an upper congestion bound. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C631v1 alternating lift](../../claims/Yin_C_G0631_v1.md#statement) | Exact same-current-length lift and necessary lower label-load statement checked at their stated interface; no upper load bound or whole re-review of the lifting proof is claimed. |
| [Whole finding](#linear-overlap-whole-independent-finding) | [C204v1 mean boundary](../../claims/Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | Accepted finite-mean/all-late bounded-overlap criterion and its distinction from a linear bound; its finite-branch convergence and common null-subsequence passages were also read, without recursively auditing their source chain. |

## Obligations and decisive verification

### 1. Exact endpoint law and early singular covariance

Every digit probability is retained.
For an n-word the original probability is 2^z/4^n, so c_n sums all representations with their integer weights and p_n>=2^-n>0.
The fixed neutral conjugate is nonreal; in particular zeta^2 is not one, so kappa is finite and h_n>0.

The used C419 proof was checked directly.
Fourier orthogonality for the integer power-basis endpoint gives the finite product of cos^2 factors.
Taking absolute values uses |cos^2(x-iy)|=cos^2(x)+sinh^2(y).
For each subset J of selected sinh terms, the original event with all digits in J zero gives p_n>=2^(-|J|)p_(J-complement).
Summing the nonnegative subset expansion gives the product of cosh factors; log cosh t<=t^2/2 gives the stated MGF bound.
Thus the denominator is the same complete original p_n, and no conditional independence is introduced.

Specialize the endpoint linear functional to u dot (Re(x(zeta)),Im(x(zeta))).
On the fixed endpoint event it is deterministic, giving equation (6) with C_n=sum v_j v_j^t.
Each v_j is a unit vector, and explicitly

    C_n=(n/2)I+(1/2)[[Re s_n,Im s_n],[Im s_n,-Re s_n]],
    s_n=sum_(j=0)^(n-1)zeta^(2j).

The second matrix has eigenvalues plus/minus |s_n|, so the operator-norm deviation is |s_n|/2.
The exact geometric sum bounds |s_n| by 2/|1-zeta^2|, giving C_n<=h_n I for every n>=1.
Choosing u=z/h_n gives exponent -|z|^2/(2h_n).
No inverse of C_n is taken, so n=1 and every singular case remain covered.
An unsupported endpoint has probability zero and satisfies the same inequality.

Multiplication by beta^n stays in O and acts at the neutral embedding by the unit complex factor zeta^n.
It preserves rho(x), so both normalized endpoint factors have the same exponential upper bound.
Their product has exponent -rho(x)^2/h_n.
This multiplies two deterministic inequalities, without assuming the endpoint factors are independent after conditioning.

### 2. Complete midpoint support and count normalization

Split the original unconditioned 2n-word into independent polynomials U,V, with return condition U+beta^n V=0.
Original sign symmetry gives equation (8).
A positive summand has both a legal n-step path from zero to x and a legal n-step continuation from x to zero, after the ordinary chronological reversal of iid coefficients.
Hence x belongs to the actual zero-to-zero core.
Earlier zero visits and every possible endpoint representation remain in the summand.

The x=0 term divided by p_n^2 equals one.
This proves D_n>=1 at every positive n.
The identity

    (4^(-2n)c_(2n)(0))/(4^(-n)c_n(0))^2
       =c_(2n)(0)/c_n(0)^2

checks the integer-count normalization exactly, with equal n,n half lengths.
No unknown R occurs in this identity.

For any actual core state, its finite path from zero bounds the stable real embedding strictly by sum_(j>=0)beta^-j=S_real.
Its finite continuation to zero bounds the expanding embedding strictly by sum_(j>=1)beta^-j=B.
Thus the strict strips used for the packing argument are consistent with the actual original core; equality of that core with all strip order points is unnecessary here.

### 3. Actual-core packing and the Gaussian integral

For distinct x,y in the actual quartic order, v=x-y is a nonzero algebraic integer.
Its norm is a nonzero integer and equals v_+ v_- times |v(zeta)|^2.
The two strict core strips therefore imply

    1<=|Norm(v)|<4 B S_real |v(zeta)|^2,
    |v(zeta)|>1/(2sqrt(B S_real))=d_0.

The disks of radius d_0/2 centered at different neutral images are disjoint.
For rho<=r they lie inside radius r+d_0/2, yielding N(r)<=(1+2r/d_0)^2=(1+gamma r)^2.
This also proves finiteness of every bounded-radius core subset by applying the area estimate to arbitrary finite subsets.
The argument includes r=0 and uses the actual conjugate pair, not one real neutral coordinate.

The layer identity is nonnegative.
Since O is countable, monotone summation/integration applies without a prior integrability assumption.
For h>0 the three integrals after expansion are

    integral_0^infinity (2r/h)exp(-r^2/h)dr=1,
    integral_0^infinity (4gamma r^2/h)exp(-r^2/h)dr
       =gamma sqrt(pi h),
    integral_0^infinity (2gamma^2 r^3/h)exp(-r^2/h)dr
       =gamma^2 h.

Their finite sum gives exactly G_n at h=h_n, and also establishes convergence of the comparison series.
The actual midpoint sum itself has finite support.
Every factor and the square-root coefficient in equation (10) is correct.

For n>=1, h_n<=n h_1 and sqrt(h_n)<=n sqrt(h_1).
Together with 1<=n these prove G_n<=G_1 n=C_star n at every stated length.
Since h_n/n tends to 1/2 and sqrt(h_n)/n tends to zero,

    G_n/n -> gamma^2/2=8 B S_real.

This proves the limsup assertion, without asserting that D_n/n has a limit.

### 4. True entropy and all-n normalized returns

The original concatenation inequality p_(n+m)>=p_n p_m makes -log p_n subadditive.
Its finite exponential rate h is the infimum of -log p_n/n, with 0<=h<=log 2.
Consequently R=exp(h) is the actual original return radius and 0<a_n=R^n p_n<=1.
This verifies the normalization interface independently of any assumed value of R.

The exact relation log D_m=log a_(2m)-2log a_m telescopes to

    H_(n,J)=-log a_n+2^-J log a_(2^J n).

For fixed n, the last term tends to zero because it equals n times log a_N/N at N=2^J n.
Thus H_n=-log a_n, and D_m>=1 makes every summand nonnegative.
No unproved recurrence, mean classification or polynomial lower bound is required for this telescope.

The two weighted sums are exactly one:

    sum_(j>=0)2^(-j-1)=1,
    sum_(j>=0)j 2^(-j-1)=1.

Using D_(2^j n)<=C_star 2^j n gives H_n<=log(C_star n)+log 2.
Exponentiation proves 1/(2 C_star n)<=a_n<=1, including n=1.

Set A=8 B S_real.
For every epsilon>0 the deterministic envelope gives some N_epsilon with D_m<=(A+epsilon)m for every m>=N_epsilon.
For every n>=N_epsilon this bound applies simultaneously to all its dyadic multiples.
The same weighted sum then gives n a_n>=1/[2(A+epsilon)] for all such n.
Taking liminf in n and then epsilon down to zero yields 1/(16 B S_real).
This uses an all-late estimate, not a selected subsequence or an exchange of unrelated n-dependent onsets.

### 5. Finite observation remainder and exact scope

For every n>=1 and integer J>=1,

    sum_(j>=J)2^(-j-1)=2^-J,
    sum_(j>=J)j 2^(-j-1)=(J+1)2^-J.

The nonnegative omitted dyadic tail is therefore at most

    2^-J[log(C_star n)+(J+1)log 2]
       =2^-J log(2^(J+1)C_star n).

This checks every factor of two and the J+1 in epsilon_(n,J).
The exponential bracket has the correct direction because H_n lies between H_(n,J) and H_(n,J)+epsilon_(n,J).
Its largest observed overlap is D_(2^(J-1)n), whose numerator requires p_(2^J n), exactly the claimed largest original return time.
The estimate for unseen times is analytic; none of their numerical values is assumed.
For each fixed n and this fixed quartic the remainder tends to zero; no uniformity over varying fields or phases is claimed.

C432's existing E_n=C_non[2+sqrt(2pi n)]^2 at this two-real-dimensional neutral pair already gives a normalized-return lower bound of order 1/n.
C645 correctly does not claim that polynomial order or a midpoint moment theorem as new.
C285's distinct midpoint proxy is not substituted for the endpoint covariance.
The proof uses no lower diffusion estimate and no independence of the neutral coordinates.

C204's finite-mean branch yields a finite limit for D_n, while its infinite-mean branch supplies a common subsequence on which D_n diverges.
An upper bound proportional to n is compatible with either branch and implies neither.
C627 and C631 have complete original conductance factors which can involve small intermediate endpoint counts.
An upper bound on endpoints or D_n does not give a positive lower bound for those factors.
In particular substituting an upper bound for D_n into a necessary lower load bound cannot produce an upper load bound.

## Input, source and verification limits

The supporting local mathematical passages named in the binding table were actually read.
C419's consumed elementary MGF argument, C432's profile specialization, the norm/packing step, original midpoint product and true-radius dyadic algebra were rechecked at their used scopes.
C432's full grid/operator construction is an accepted comparison for already existing polynomial order, not a whole argument newly audited here.
C285's remaining projection estimates and C627/C631's full lifting proofs were not re-audited because this theorem imports no new positive conclusion from them.
C204's fixed critical recurrence and finite/infinite-mean statements are used only at their accepted comparison scope; its classical Markov/source proof chain was not recursively audited.
The original quartic and its conjugate/order conventions remain the specified fixed input.

No prior R verdict is relabelled or broadened.
This review verifies the exact local reuse and mathematical applicability just stated; it makes no global novelty survey or claim that every external source in the dependency graph was inspected.
The local proof needs only elementary finite Fourier algebra, geometric sums, integer norms, plane-disk area comparison, nonnegative integration and the existing subadditive entropy normalization.
No missing external assertion was identified as a premise of equations (1)--(5).

No native program, enumeration, finite screen or numerical endpoint approximation was introduced or run.
The exact bounds were checked analytically, so there is no unseen empirical extrapolation or generated-output premise.
No formal proof-assistant verification, uniform near-one result, upper congestion theorem or Task-completion audit is claimed.

<a id="linear-overlap-whole-independent-finding"></a>
## Whole independent finding

No mathematical gap was found in the complete C645v1 statement, Sections 1--5, their constants, selected-input applications or stated quantifiers.
The every-n product/overlap envelope, limsup D_n/n<=8 B S_real, every-n normalized-return lower bound, liminf n a_n>=1/(16 B S_real), and explicit finite dyadic remainder are supported at precisely the fixed original-quartic scope.
The mean branch and uniformly paid inter-label congestion remain unresolved exactly as stated.
This R supplies independent review evidence; adoption remains a separate C decision.
