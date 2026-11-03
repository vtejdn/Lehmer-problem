---
author: Yin
---

# Complete quartic midpoint data through time256 and a true return-radius lower bound

Human author Yin.
The original_law_continuation contributor developed the native calculation and MC1--MC7 analytic reduction.
Root read the complete saved mathematics, new native program and exact fixed interfaces before registering this initially OPEN candidate.
The [D2 development](../drafts/Yin_D_G0002.md#complete-original-midpoint-256) is provenance only; complete necessary reasoning is retained here.
The native program, exact outputs and reproducibility remain in the existing coherent J52 computation group.
Previous J52 reviews do not cover this new computation or radius bound.
No new external theorem or finite extrapolation is used.

## Statement

Fix the ACTUAL irreducible Salem quartic P(t)=t^4-t^3-t^2-t+1, its exterior root beta and a unit-circle conjugate zeta.
Retain its full original zero-to-zero core and chronological independent digit law with probabilities1/4,1/2,1/4 at-1,0,1, including all earlier zero visits and every word representation.
Let p_t be the complete original return probability, f_t the complete first-positive-return probability, R the true exponential return radius, h_2(beta)=logR, and

    D_n=p_(2n)/p_n^2,
    M_n=E[|X_n(zeta)|^2 given X_(2n)=0].

The deterministic height48 graph and integer recurrences in MC1--MC3 compute the COMPLETE original returns for every1<=t<=256 with zero omitted return mass.
The exact new return values are

    p128=241348810511898190541699791270635467354265589/2^253,
    p256=264543412341747108848944040326875358997077741567393090275411759418849446982212078897310231/2^504.

The complete weighted midpoint quantities lie in the following OPEN intervals with rational decimal endpoints:

| n | Positive midpoint states | D_n | M_n/n |
| ---: | ---: | --- | --- |
|16|159|(2.211245,2.211246)|(0.144025,0.144026)|
|32|727|(3.728176,3.728177)|(0.176933,0.176934)|
|64|3231|(8.004156,8.004157)|(0.212920,0.212921)|
|128|13963|(18.166305,18.166306)|(0.227137,0.227138)|

In particular M64>64/5 and M128>128/5.
The moments are computed exactly in Q(sqrt13) before the certified interval enclosure and retain both real neutral coordinates.
For EVERY t=1,...,256 one has p_t(1723/1000)^t<1 and hence p_t<beta^(-t).
The distinct finite first-return test satisfies

    0.948616<sum_(j=1)^256 f_j beta^j<0.950835<1.

Neither finite failure asserts a converse about later times, the true equality R=beta or a critical mean branch.

The following UNCONDITIONAL fixed-input radius bound follows from the exact p256 and the paid infinite-time estimate:

    R^n p_n>=1/(55n) for EVERY integer n>=256,
    R>1687/1000,
    h_2(beta)>log(1687/1000),
    1687/1000<R<=beta<1723/1000.

The n>=256 assertion uses the full existing all-n overlap bound and infinite dyadic identity, not measured later returns.
No positive limiting midpoint ratio, finite/infinite critical mean, R=beta or R<beta, degree-uniform entropy bound, varying near-one family or unrestricted G0001 conclusion is asserted.

## Complete argument

### Question and exact reused inputs

The discriminating quantities are the COMPLETE chronological midpoint moment M_n=E[|X_n(zeta)|^2 given X_(2n)=0] and the radius-free doubling overlap D_n=p_(2n)/p_n^2 for the actual quartic P=t^4-t^3-t^2-t+1.
The digit probabilities remain 1/4,1/2,1/4 at -1,0,1.
Every earlier zero visit, complete word representation and both real neutral coordinates remain included.
No conditional block component is replaced by a connected surrogate, and no component mean is inferred from the globally zero mean.

The local reuse screen read the actual [C204 mean/tightness theorem](Yin_C_G0204_v1.md#midpoint-capture-fixed-scope), [C285 lower-moment discriminator](Yin_C_G0285_v1.md#diffusive-moment-fixed-scope), [C300 signed moment and small-block limits](Yin_C_G0300_v1.md#statement), [C555 dyadic identity](Yin_C_G0555_v1.md#dyadic-critical-normalization), [C645 complete product envelope](Yin_C_G0645_v1.md#statement), C559/J52 finite completeness and the C675/C703/C731/C745 failed comparisons.
The fixed [C526 true-radius and recurrence input](Yin_C_G0526_v1.md#statement) supplies the same quartic's established R<=beta; its C579 companion interface does not infer a critical mean from R<beta, individual singular critical factors or one subcritical convolution.
The existing C285 implication is reused: a positive limsup M_n/n forces infinite critical mean, whereas finite mean forces M_n/n to zero.
This calculation does not reprove that implication or infer its limsup premise from four times.
The actual quotient-state reversal used below is [C419's complete integral map](Yin_C_G0419_v1.md#argument).
These existing arguments supply the complete method; no new external theorem or source attribution is required by the finite algebra and rational comparisons below.

### Complete finite law and exact midpoint mark

Write q=(q_0,q_1,q_2,q_3) for consecutive quotient coefficients, with zero initial state, and set

    S_e(q)=(q_1,q_2,q_3,-q_0+q_1+q_2+q_3+e),
    w_0=2, w_(-1)=w_1=1.

The integer path weight is the product of these w_e; its original probability at time t is that weight divided by 4^t.
The [C559 complete deterministic bound](Yin_C_G0559_v1.md#salem-complete-quotient-height-tail), with its already certified C_0<6/5 and C_1<11/30, gives

    ht(E/P)<6/5+(11/30)floor(t/2)<=6/5+(11/30)128
             =722/15<49                         for t<=256.       (MC1)

Since the height is integral, every original returned path of length at most256 stays inside height48.
The original J52 outward rational real-strip screens remove only impossible actual core points, and its forward/backward reachability removal preserves every zero-to-zero path inside the box.
Thus its height48 graph contains EVERY original returned word at every t<=256, not merely an approximation with a small omitted mass.
It has 68211 forward-reached states and 65893 states that can return inside the graph, below the retained100000 reached-state cap.
There are114445 directed digit edges; the cap counts reached states rather than edges.
The enclosing Cartesian box has88529281 points; these are not all enumerated or substituted for the actual returning graph.

Let F_t(q) be the complete forward integer weight from zero to q in t steps, and B_t(q) the complete terminal integer weight from q to zero in t steps, in this unchanged finite graph.
Their exact recurrences use w_e at every digit, with no killed-mass renormalization.
Put W_t=F_t(0).
For n in{16,32,64,128}, splitting every complete returned word at its actual middle gives

    sum_q F_n(q)B_n(q)=W_(2n),
    p_t=W_t/4^t,
    D_n=W_(2n)/W_n^2.                                  (MC2)

The forward and terminal recurrences separately agree at zero for every time through128.
The complete values p16,p32,p64 agree exactly with all three previously retained J52 controls.
Renewal inversion fweight_t=W_t-sum_(1<=j<t)fweight_j W_(t-j) produces nonnegative integers at every t<=256, retaining rather than deleting the earlier visits already present in W_t.
The output retains the entire W_t and first-return integer-weight lists, not only the four displayed observations.

The exact integral reverse-original state map is

    Psi(q)=a_0+a_1 beta+a_2 beta^2+a_3 beta^3,
    (a_0,a_1,a_2,a_3)=(-q_0+q_1+q_2+q_3,
                        -q_1+q_2+q_3,-q_2+q_3,-q_3).

It obeys beta Psi(S_e q)-e=Psi(q).
Consequently reversal of the complete quotient word, with digit negation, gives the original chronological process and takes its central state to Psi(q_n).
Reversal and digit negation preserve the full original word probability.
The implementation checks the displayed linear identity on zero and all four basis vectors for all three digits; the full original-law justification is C419's integral bijection, not that finite check alone.

For s_l=sum_(0<=j<=3-l)a_j a_(j+l) and u=zeta+zeta^(-1)=(1-sqrt13)/2, the quartic identity u^2-u-3=0 gives

    |Psi(q)(zeta)|^2=s_0+s_2+3s_3+u(s_1+s_2+s_3)
                    =(A(q)+B(q)sqrt13)/2,
    A(q)=2(s_0+s_2+3s_3)+s_1+s_2+s_3,
    B(q)=-(s_1+s_2+s_3).

Indeed zeta^2+zeta^(-2)=u+1 and zeta^3+zeta^(-3)=u+3, so expanding the squared modulus proves every term and retains both neutral coordinates.
Therefore the exact true midpoint moment is

    M_n=[sum_q F_n(q)B_n(q)A(q)
              +sqrt13 sum_q F_n(q)B_n(q)B(q)]/[2W_(2n)].       (MC3)

Both integer sums and the rational coefficients of1,sqrt13 are preserved in the native output.
There is no floating-point value in MC1--MC3 or in the decisive comparisons.
The rational bracket3605551275463989/10^15<sqrt13<3605551275463990/10^15 is certified by squaring and is used with the correct sign of the sqrt13 coefficient.
The complete weighted sum of every quotient coordinate is exactly zero, checking the actual global midpoint centering without asserting centering in an arbitrary update component.

### Exact finite outcomes and the unsuccessful finite crossing test

The following open intervals have rational decimal endpoints and enclose the complete quantities, using MC3 and the certified root bracket.
The number of positive midpoint states counts states with F_n(q)B_n(q)>0, not graph vertices chosen without their original weights.

| n | Positive midpoint states | D_n | M_n/n |
| ---: | ---: | --- | --- |
|16|159|(2.211245,2.211246)|(0.144025,0.144026)|
|32|727|(3.728176,3.728177)|(0.176933,0.176934)|
|64|3231|(8.004156,8.004157)|(0.212920,0.212921)|
|128|13963|(18.166305,18.166306)|(0.227137,0.227138)|

In particular M64>64/5 and M128>128/5 hold with exact rational certificates.
The newer complete return values are

    p128=241348810511898190541699791270635467354265589 / 2^253,
    p256=264543412341747108848944040326875358997077741567393090275411759418849446982212078897310231 / 2^504.       (MC4)

The output stores the equivalent exact numerator/denominator pairs.
For EVERY t=1,...,256 the integer/rational test proves

    p_t(1723/1000)^t<1,

and beta<1723/1000 implies p_t<beta^(-t) throughout this entire finite range.
Thus no time in the computed range supplies the strict-pressure sufficient crossing described in the preceding section.
This finite failure neither proves R=beta nor rules out a later crossing.
The root coordinator separately proposed checking the stronger finite first-return certificate sum_(j<=256)f_j beta^j>1, which is not excluded merely because all individual p_t tests fail.
The complete renewal coefficients give the exact monotone bracket

    0.948616<sum_(j<=256)f_j(861/500)^j
       <sum_(j<=256)f_j beta^j
       <sum_(j<=256)f_j(1723/1000)^j<0.950835<1.          (MC4a)

The exact endpoint fractions are preserved in the output and the rational comparisons are checked directly.
Thus this distinct finite sufficient certificate also fails in the declared range, with no inference about the uncomputed first-return tail or the eventual strict-pressure question.

### A new unconditional true-radius lower bound from the complete p256

The existing C645 bound is D_m<=G_m=1+gamma sqrt(pi(m/2+kappa))+gamma^2(m/2+kappa), where gamma^2=16beta/(beta-1)^2 and kappa=1/sqrt((1+sqrt13)/2).
The actual beta>861/500 gives gamma^2<53 by an exact rational comparison, since beta/(beta-1)^2 decreases for beta>1.
Also sqrt13>7/2 gives kappa<2/3.
Using pi<4, for every m>=256 one has

    gamma sqrt(pi(m/2+kappa))
        <sqrt(212(m/2+2/3))<3m/4,
    1+106/3< m/4,
    G_m<53m/2+3m/4+m/4=(55/2)m.                         (MC5)

For the square-root comparison, divide by m^2 and observe that1/(2m)+2/(3m^2) decreases; the displayed inequality is already strict at m=256 by rational arithmetic.
The other comparison is immediate at256 and remains strict thereafter.
The exact C555/C645 infinite dyadic identity, with its already proved convergence, now yields for every n>=256

    -log(R^n p_n)=sum_(j>=0)2^(-j-1)log D_(2^j n)
       <=sum_(j>=0)2^(-j-1)log((55/2)2^j n)
       =log(55n),
    R^n p_n>=1/(55n).                                  (MC6)

Here sum2^(-j-1)=sum j2^(-j-1)=1; all unobserved later D values are controlled analytically by MC5, not silently treated as measured data.
The complete p256 of MC4 satisfies the exact rational certificate

    (55*256)*p256*(1687/1000)^256<1.

Together with MC6 this proves the candidate unconditional bound

    R>1687/1000,
    h_2(beta)>log(1687/1000),
    1687/1000<R<=beta<1723/1000.                         (MC7)

The certificate product itself is stored as an exact fraction in J52's output.
This improves the previous lower bound2^(5/8) for this fixed original quartic, while leaving the actual R=beta question and critical mean unresolved.
It supplies no new degree-uniform entropy or Mahler estimate and no substitute for a genuine all-late or subsequential lower midpoint bound.

### Remaining discriminating step

The finite moment values increase on this selected dyadic list and exceed1/5 at its last two points, supporting further investigation of the actual C285 lower-moment condition.
The precise unproved target remains a fixed epsilon>0 and an unbounded sequence n_j with M_(n_j)>=epsilon n_j, using the complete original law.
The unchanged C300 signed-integer criterion is an exact possible analytic consumer of MC3; neither an upper projection proxy nor a finite extrapolation supplies its missing lower sign/ratio estimate.
A useful next computational discriminator is the SAME exact midpoint/overlap calculation at a longer declared scale, retaining a proved full-path cutoff and the original integer weights, together with actual midpoint tail masses to distinguish a broad diffusive profile from rare high-radius contributions.
No longer scale or new state cap is selected or executed by this record.
The finite values, MC7 and all native author checks require a separate independent whole native/reduction inspection before adoption.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision midpoint-256-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T08:49 |
| status | open |
| reason | Fix the complete original-law finite midpoint calculation and MC1--MC7 true-radius lower-bound reduction, with exact native inputs and zero omitted mass through256. Separate independent whole mathematical/native inspection is required. Finite rising moments and failed pressure tests do not classify the critical mean, decide R=beta or give a uniform Lehmer result. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact finite data and true-radius bound](#statement) | Fixed actual quartic/full original law, complete1--256 returns, all four true midpoint moments and intervals, exact p128/p256, both failed finite crossing tests, all-n normalized bound and strictR>1687/1000, with all exclusions. |
| argument | [Complete MC1--MC7 reduction](#complete-argument) | Deterministic finite coverage, actual forward/backward weights, original reverse map and neutral quadratic mark, exact finite outcomes/renewal tests, all-tail G_m estimate and dyadic certificate, precise remaining limsup boundary. |
| dependency | [Adopted original integral reversal](Yin_C_G0419_v1.md#decision-complete-isolated-whole-adoption) | Exact quotient-state to original chronological bridge map and original complete-weight bijection, not a conditional component-centering surrogate. |
| dependency | [Adopted full-path height and graph method](Yin_C_G0559_v1.md#decision-complete-isolated-whole-adoption) | Deterministic all-return quotient height C0+floor(t/2)C1, certified constants, original rational core-strip screens and zero-return graph preservation; no later review transferred to the new256 computation. |
| dependency | [Adopted all-n product envelope](Yin_C_G0645_v1.md#decision-whole-reviewed-2026-10-23) | Complete D_m<=G_m with actual gamma/kappa and both neutral dimensions, true-radius normalization and analytically paid unobserved dyadic tail, valid in either critical-mean branch. |
| dependency | [Adopted dyadic identity](Yin_C_G0555_v1.md#decision-isolated-whole-review-adoption-20261022) | Exact convergent infinite dyadic identity H_n=-log(R^n p_n), actual entropy radius and every original chronological observation; no finite extrapolation. |
| support | [Original unchanged graph implementation](../computations/programs/Yin_J_G0052/experiment.py) | Exact integer graph, rational outward strips, retained100000 reached-state cap and earlier complete controls, inspected for the newheight48 invocation. |
| support | [New complete native midpoint calculation](../computations/programs/Yin_J_G0052/midpoint_continuation.py) | Entire author exact integer forward/backward/renewal calculation, full original midpoint mark, rational enclosures and radius certificates at declared scope; not an independent implementation of the original graph. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Complete return/first-return lists, all exact midpoint Q(sqrt13) sums and enclosures, graph scope, old controls and decisive rational certificates; independently reproducible generated data, not its own correctness oracle. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/midpoint_continuation.json`; this target locates its run account. |
| support | [Existing midpoint interpretation](Yin_C_G0285_v1.md#diffusive-moment-fixed-scope) | Only the already fixed positive diffusive-limsup implication; its unproved limsup premise is not inferred from four finite observations. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T09:07 |
| status | proved |
| reason | Root read complete MC1--MC7, the author native program, exact fixed interfaces and full independent R996, and adopts the finite complete original midpoint data and strict true-radius bound R>1687/1000. The independent original-coordinate slice/graph/predecessor/killed-return/norm calculation exactly reproduced all decisive native data and certificates. Explicitly select the already invoked C526 upper-radius/recurrence input for R<=beta as identified in review; this supplies no new proof step or mean inference. Infinite unseen dyadic times are paid analytically. Four finite moments and failed finite crossing tests do not classify the critical mean, decide R=beta/R<beta or resolve G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact finite data and true-radius bound](#statement) | Fixed actual quartic/full original law, complete1--256 returns, all four true midpoint moments and intervals, exact p128/p256, both failed finite crossing tests, all-n normalized bound and strictR>1687/1000, with all exclusions. |
| argument | [Complete MC1--MC7 reduction](#complete-argument) | Deterministic finite coverage, actual forward/backward weights, original reverse map and neutral quadratic mark, exact finite outcomes/renewal tests, all-tail G_m estimate and dyadic certificate, precise remaining limsup boundary. |
| dependency | [Adopted original integral reversal](Yin_C_G0419_v1.md#decision-complete-isolated-whole-adoption) | Exact quotient-state to original chronological bridge map and original complete-weight bijection, not a conditional component-centering surrogate. |
| dependency | [Adopted full-path height and graph method](Yin_C_G0559_v1.md#decision-complete-isolated-whole-adoption) | Deterministic all-return quotient height C0+floor(t/2)C1, certified constants, original rational core-strip screens and zero-return graph preservation; no later review transferred to the new256 computation. |
| dependency | [Adopted all-n product envelope](Yin_C_G0645_v1.md#decision-whole-reviewed-2026-10-23) | Complete D_m<=G_m with actual gamma/kappa and both neutral dimensions, true-radius normalization and analytically paid unobserved dyadic tail, valid in either critical-mean branch. |
| dependency | [Adopted dyadic identity](Yin_C_G0555_v1.md#decision-isolated-whole-review-adoption-20261022) | Exact convergent infinite dyadic identity H_n=-log(R^n p_n), actual entropy radius and every original chronological observation; no finite extrapolation. |
| support | [Original unchanged graph implementation](../computations/programs/Yin_J_G0052/experiment.py) | Exact integer graph, rational outward strips, retained100000 reached-state cap and earlier complete controls, inspected for the newheight48 invocation. |
| support | [New complete native midpoint calculation](../computations/programs/Yin_J_G0052/midpoint_continuation.py) | Entire author exact integer forward/backward/renewal calculation, full original midpoint mark, rational enclosures and radius certificates at declared scope; not an independent implementation of the original graph. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Complete return/first-return lists, all exact midpoint Q(sqrt13) sums and enclosures, graph scope, old controls and decisive rational certificates; independently reproducible generated data, not its own correctness oracle. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/midpoint_continuation.json`; this target locates its run account. |
| support | [Existing midpoint interpretation](Yin_C_G0285_v1.md#diffusive-moment-fixed-scope) | Only the already fixed positive diffusive-limsup implication; its unproved limsup premise is not inferred from four finite observations. |
| dependency | [Established same-quartic upper radius and recurrence](Yin_C_G0526_v1.md#statement) | Only the actual fixed-quartic R<=beta and true-radius recurrence already invoked in the proof; no equality or finite/infinite-mean classification. |
| review | [Independent whole native and radius finding](../audits/reviews/Yin_R_G0996_v1.md#complete-midpoint-native-and-radius) | Entire statement and MC1--MC7, all finite original paths/weights/moments/renewal tests, distinct native reconstruction, exact rational data, full analytic infinite tail and narrow C526 selection, with all asymptotic and source limits. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0052](../computations/programs/Yin_J_G0052/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
