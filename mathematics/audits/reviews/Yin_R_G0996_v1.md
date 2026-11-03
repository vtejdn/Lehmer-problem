---
author: Yin
---

# Whole independent review of complete quartic midpoint data and the true-radius lower bound

Human record author Yin.
The review act completed at 2026-10-26T08:58 UTC.
The exact initial target was [C776 v1, decision midpoint-256-open](../../claims/Yin_C_G0776_v1.md#decision-midpoint-256-open), its entire Statement and Complete argument, and its retained native J52 inputs and output.
The reviewer was a separately assigned agent outside the substantive development of that proof and program.
Its supplied mathematical inputs were the fixed C776 statement/proof, the directly needed fixed Claims and J52 native materials, together with the requested review scope.
No D37 development, proof-generation dialogue, persistent memory, proposing-agent mathematical explanation or previous review of this new C776 calculation was read before the initial findings.
The J52 README includes older reviews of the earlier finite calculation; those historical notices were encountered while inspecting the assigned native entrance, but their findings or programs were not used to certify the new computation.
The reviewer supplied no substantive repair of the reviewed mathematics.
A missing explicit selection of the already invoked C526 upper-radius input was identified and communicated after the independent initial inspection; it is a dependency-selection issue, not a new proof step.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [C776 Statement](../../claims/Yin_C_G0776_v1.md#statement) | Entire fixed-quartic original-law statement: full times 1--256, graph counts, exact p128/p256, all four true midpoint quantities, both unsuccessful finite pressure tests, every n>=256 normalized lower bound, strict R>1687/1000 and stated exclusions. |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [C776 Complete argument](../../claims/Yin_C_G0776_v1.md#complete-argument) | All MC1--MC7 reasoning, including the infinite dyadic tail and exact finite native certificates; direct accepted-input interfaces and remaining limsup distinction. |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [C419 integral reverse map](../../claims/Yin_C_G0419_v1.md#argument) | Exact integral bijection of quotient and original returned words, digit negation, reversal, weights and chronological midpoint; no renewed review of unrelated C419 theorems. |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [C559 finite completeness](../../claims/Yin_C_G0559_v1.md#complete-finite-quartic-argument) | Returned prefix/suffix height bound and constants, rational outward strips, actual integer transitions and safe forward/backward pruning, applied at height48 and times through256. |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [C645 complete envelope](../../claims/Yin_C_G0645_v1.md#statement) | Complete original overlap D_m<=G_m for all m, its gamma/kappa constants and valid true-radius use in both mean branches; the invoked product, packing and tail derivation were inspected. |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [C555 dyadic identity](../../claims/Yin_C_G0555_v1.md#dyadic-critical-normalization) | Exact convergent infinite identity at the true exponential return radius and the entropy-limit remainder; no R=beta assumption. |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [C285 moment interpretation](../../claims/Yin_C_G0285_v1.md#diffusive-moment-fixed-scope) | Existing finite-mean subdiffusive conclusion and positive-limsup implication only; four finite values supply neither asymptotic premise. |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [C526 fixed upper radius](../../claims/Yin_C_G0526_v1.md#statement) | Only the already accepted same-quartic R<=beta and true-radius recurrence needed by the final interval and existing moment interpretation; no equality R=beta or mean classification. |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [Original graph program](../../computations/programs/Yin_J_G0052/experiment.py) | The graph, constants, rational strip pruning, state-cap and original-weight functions actually imported at height48; other historical experiment outputs are not re-certified. |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [Author midpoint program](../../computations/programs/Yin_J_G0052/midpoint_continuation.py) | Entire new integer return, backward, midpoint, renewal, rational enclosure and radius-certificate implementation at its declared scope. |
| [Whole C819 finding](#complete-midpoint-native-and-radius) | [Output of the recorded run](../../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Native scope and mathematical payload checked against independent calculation, including all complete return and first-return weights, exact midpoint coefficients, intervals and pressure/radius certificates. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0052/midpoint_continuation.json`; this target locates that original run's computation account. |

<a id="complete-midpoint-native-and-radius"></a>
## Whole finding and necessary dependency selection

No mathematical defect was found in the complete MC1--MC7 proof at its stated fixed-quartic scope.
The independent native calculation agrees exactly with every decisive finite value and certificate.
The resulting true-radius lower bound is supported by a complete all-late analytic argument together with exact p256; it is not an extrapolation of the four observed midpoint ratios.
The final R<=beta endpoint uses the already accepted [C526 Statement](../../claims/Yin_C_G0526_v1.md#statement), whose explicit quartic justification is [Section5](../../claims/Yin_C_G0526_v1.md#quartic-critical-recurrence-and-sextic-approximation).
C776's initial reuse prose already names C526, but its initial decision does not select that exact dependency.
A new adoption should explicitly select this fixed input for that narrow scope.
This review neither supplies a new upper-radius proof nor retrospectively changes C526's accepted evidence.

### MC1: complete returned-path coverage and graph preservation

The C559 coefficient-height argument uses the exact return to replace each neutral prefix by the negative suffix, giving the bound floor(t/2), while retaining both nonneutral places.
The rational constant checks give C0<6/5 and C1<11/30, so every quotient coefficient in every return word with t<=256 has absolute value less than722/15<49.
Integral height therefore puts every such path inside height48, including all initial and terminal zero padding.
Times below the polynomial degree have only the zero relation and cause no exceptional omitted path.
The nonconstant strip coefficient functions -1/gamma, gamma^2-gamma-1 and gamma-1 are increasing on both actual real-embedding brackets, which lie above1/2.
Outward rounding and sign-aware interval evaluation reject only states that cannot satisfy the required strips.
Reachability from zero and reachability of zero remove no zero-to-zero word.
Every retained edge remains a genuine integer digit transition, so an overinclusive strip does not introduce a false algebraic return.
The reached-state cap is100000, not an edge cap; it was respected without enlargement.

The independent checker enumerated71135 strip-allowed lattice points by exact three-coordinate slicing of the fourth-coordinate interval.
It then used original chronological coordinates and separate forward/inverse depth-first searches, finding66777 original-forward states and68211 original-backward states.
Under the exact reverse map the latter is the author's quotient-forward count.
Their intersection has65893 states and114445 directed digit edges, agreeing with the author's returning graph.
The full enclosing box has97^4=88529281 points; neither program substitutes that count for the reached graph.

### MC2: complete weights, midpoint splitting and first returns

The common denominator remains4 per digit, with integer weights1,2,1; no wall or zero-visit renormalization occurs.
The author forward and terminal recurrences compute the two parts of every returned word, so their midpoint product sums to W_(2n).
The independent implementation uses predecessor-gather evolution in original coordinates, with zero at its actual sorted index rather than assuming index0.
It computes all257 weights W_0 through W_256 and a separate terminal evolution through128.
Every terminal zero weight agrees with the corresponding forward return weight, and all four midpoint sums equal W_(2n).
The independent program also counts first-positive returns by killing paths immediately after their first positive visit to zero, instead of deriving them by the author's renewal inversion.
Every resulting first-return weight agrees with the author list, and the full renewal identities hold through256.
The old p16,p32,p64 controls and the displayed exact p128,p256 fractions were checked directly.
All earlier zero visits remain in the complete return weights.

### MC3: actual chronological midpoint and both neutral coordinates

The displayed triangular integer map Psi has integer inverse, obtained recursively from its last coordinate upward.
Direct expansion with beta^4=beta^3+beta^2+beta-1 proves beta Psi(S_e q)-e=Psi(q) for arbitrary q and digit e.
Thus reversing a complete quotient path and negating its digits produces a complete original chronological path with the same probability.
At time2n its midpoint is exactly Psi(q_n), not a forward map applied at a different chronological position.

For u=(1-sqrt13)/2, the identity u^2-u-3=0 yields zeta^2+zeta^-2=u+1 and zeta^3+zeta^-3=u+3.
Expanding the full modulus square gives the author's A,B formula, with both real neutral coordinates retained.
The independent program derives these symmetric powers through V_(k+1)=u V_k-V_(k-1) in Q(sqrt13), starting with V0=2,V1=u, then evaluates the direct original-coordinate norm.
Its two weighted integer coefficients agree with the author's sums at all four times.
The squared rational bracket for sqrt13 is strict, and the enclosure uses the coefficient's sign correctly.
All weighted quotient-coordinate sums are exactly zero; this checks only global midpoint centering and supplies no unproved component-centering premise.

### MC4 and MC4a: finite data and the two distinct unsuccessful tests

The positive midpoint-state counts are159,727,3231,13963 for n16,32,64,128 respectively.
All eight displayed open intervals for D_n and M_n/n were independently recovered with exact rational comparisons.
The last two moment lower endpoints exceed1/5, giving the stated finite M64 and M128 inequalities.
The exact new probabilities are the displayed numerators divided by2^253 and2^504, respectively.
For every1<=t<=256 the independent comparison p_t(1723/1000)^t<1 holds strictly.
Since beta<1723/1000, this proves the stated finite no-crossing result, with the correct inequality direction.

The separately computed first-return list gives the same exact evaluations at861/500 and1723/1000 as the author's renewal list.
Their monotonicity in the positive argument and strict beta bracket give the full stated chain0.948616<sum_(j<=256)f_j beta^j<0.950835<1.
The strict comparisons are valid since f1=1/2>0.
Failure of either finite sufficient test says nothing about an uncomputed later crossing or the first-return tail.
Neither calculation identifies R with beta or chooses a critical-mean branch.

### MC5--MC7: analytically controlled unobserved times

C645 supplies D_m<=1+gamma sqrt(pi(m/2+kappa))+gamma^2(m/2+kappa) for every m>=1, with gamma^2=16beta/(beta-1)^2.
The rational beta lower bound and monotonicity of beta/(beta-1)^2 give gamma^2<53.
The quartic relation gives |1-zeta^2|^2=4-u^2=(1+sqrt13)/2, so sqrt13>7/2 implies kappa<2/3.
For m>=256, the squared square-root comparison follows by the decreasing function1/(2m)+2/(3m^2), checked strictly at256.
The remaining constant1+106/3 is strictly less than m/4 in the same range.
Together these yield G_m<(55/2)m at every such m, without data from any later time.

C555's telescoping identity has the true entropy-limit remainder2^-J log(R^(2^J n)p_(2^J n)), which tends to zero for fixed n.
Its nonnegative infinite sum is therefore exactly -log(R^n p_n).
For every n>=256 all dyadic multiples remain in the valid range of MC5.
Summing the full bounds with sum2^(-j-1)=sum j2^(-j-1)=1 gives -log(R^n p_n)<=log(55n), hence R^n p_n>=1/(55n).
No later p_n is claimed computed, and no finite truncation is substituted for this infinite estimate.
The independent exact rational certificate (55*256)p256(1687/1000)^256<1 then forces R>1687/1000.
The certificate is approximately0.9850152044 for display only; the retained numerator/denominator is the evidence.
The logarithmic entropy bound follows because log is increasing, and the accepted C526 input supplies the upper endpoint R<=beta.

### Moment interpretation and actual remaining scope

C285's finite-mean implication concerns the full actual midpoint law and includes a paid uniform-integrability argument using its exponential/fourth-moment bounds.
Its positive-limsup contrapositive is applicable at this recurrent quartic, but four finite values do not establish that limsup premise.
The new lower-radius estimate does not prove R<beta or R=beta.
It supplies no degree-uniform entropy or Mahler bound, varying near-one family, asymptotic midpoint diffusion, critical mean classification or resolution of G0001.
These exclusions agree with the complete C776 statement.

## Native verification and limits

The retained distinct checker is [reviewer_midpoint_verify.py](../../computations/programs/Yin_J_G0052/reviewer_midpoint_verify.py), with reviewer_midpoint_result.json (`mathematics/computations/outputs/Yin_J_G0052/reviewer_midpoint_result.json`).
It imports no author mathematical function and reads the author JSON only after calculating its own data.
It retains the same polynomial, rational strip enclosures, height48, original weights, declared return/midpoint range and100000 reached-state cap.
The independently implemented slicing, original-coordinate traversal, predecessor-gather evolution, killed first-return recurrence and norm recurrence distinguish this calculation from an author replay.
It shares the fixed mathematical reduction and accepted inputs; this is not a different theorem or formal verification of Python.
No output beyond256, enlarged state cap, unrestricted binary enumeration or new source audit was performed.
The author program was inspected in full but was not rerun as part of this independent check.
Its retained decisive output was reproduced by the independent implementation rather than treated as its own correctness oracle.
Old J52 reviews and old native programs were not relabelled as verification of the new scope.
Accepted fixed inputs were inspected at the invoked interfaces; unrelated theorem sections and their complete transitive source proofs were not recursively re-audited.

From the repository root, the completed standard-library command is:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/reviewer_midpoint_verify.py
```

The command requires the retained author JSON for its explicit comparison after independent computation.
Its generated output is published only after all checks succeed.
This fixed finding supplies whole C776 mathematical/native review evidence, with the explicit C526 selection qualification above; adoption remains the responsible Claim decision.

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.
