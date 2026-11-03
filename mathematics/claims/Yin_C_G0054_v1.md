---
author: Yin
---
# Finite modular rounding with exact zero repair and complete arithmetic costs

Date: 2026-10-12T10:13.
Human author Yin.
Internal fixed extraction under the continuing G0001 instruction.
Root supplied the modular-lift candidate, the original author supplied the informal recursion/coefficient candidate, and the recovery author reconstructed the complete D7 proof.
The ENTIRE original author account is retained below.
g0001_routes independently whole-reviewed that original proof in R261 and NOW authors this new fixed statement/wrapper; this contributor cannot independently review the present extraction.
A separate actual extraction finding remains required before adoption.

## Statement

Let P be the ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, original degree d>=2, K=Q(alpha) and O0=Z[alpha].
Reciprocity is NOT assumed.
Let A_T be the complete integer remainder matrix in the actual power basis for allowed window[0,T], T>=0.
Fix an integer q>=2 and residues c_i in{0,...,q-1} with A_T c=0 modulo q.
Independently sample B_i in{0,1} with Pr(B_i=1)=x_i=c_i/q, and let the rational coefficient vector f=x-B.
Keep every positive-probability indexed atom with its actual probability lambda_a.
Put

    V=diag(x_i(1-x_i)), S=Tr V,
    Z={a:A_T f_a=0}, N={a:A_T f_a!=0},
    p0=sum_(a in Z)lambda_a.

**A. Actual finite repair, all lags and exact success criterion.**
For EVERY finite integer k>=1 use independent copies f^(1),...,f^(k), with

    I_j=1_{A_T f^(1)=...=A_T f^(j-1)=0}, I_1=1,
    Y_k=sum_(j=1)^k I_j f^(j)+I_(k+1) epsilon e0,
    Pr(epsilon=+1)=Pr(epsilon=-1)=1/2,
    h_k=sum_(j=0)^(k-1)p0^j.

Retain the complete indexed stopping tree: a first nonzero leaf at depth j has weight product_(l=1)^j lambda_(a_l); each terminal sign leaf has weight(product_(l=1)^k lambda_(a_l))/2.
All final weights are positive rational and sum1.
EVERY final value Y_k(alpha) is a NONZERO actual O0 integer.
The COMPLETE coefficient mean and second moment are

    E Y_k=0,
    E(Y_k Y_k^T)=h_k V+p0^k e0 e0^T,
    E_k=h_k S+p0^k>0.

Consequently every positive and negative aggregate lag vanishes and E_k is the actual constant circle covariance.
This is an actual finite packet, not only a PSD condition or a closed-hull limit.
For nonzero c, p0<1 and

    h_k=(1-p0^k)/(1-p0),
    1-E_k=h_k(1-S-p0),
    lim_(k->infinity)E_k=S/(1-p0).

Thus E_k<1 for SOME finite k if and only if S+p0<1, in which case EVERY finite k succeeds.
Recursion cannot rescue a failed one-step energy test.
The limit is only a limit of numerical finite energies.
For c0, Y_k is the equiprobable constant pair+/-1 and E_k=1.
The p0=0 case has only depth-one leaves.

**B. ACTUAL coefficient denominator, FINAL weights, support and full norms.**
For nonzero c set Q=q/gcd(q,c_0,...,c_T), and let s be the number of nonzero c_i.
The complete retained packet has ACTUAL least coefficient denominator q_k=Q for EVERY finite k.
Its ACTUAL indexed least FINAL weight denominator and copy counts satisfy

    M_k=lcm_b denominator(omega_b),
    M_k divides 2 Q^(s k),
    n_b=M_k omega_b in Z_{>0}, sum_b n_b=M_k.

For c0, q_k=1 and M_k=2.
Equal leaves or values are not merged in these assertions.
The exact union of occupied coefficient positions is {i:V_ii>0}, together with0 when p0>0.
If its endpoints are r,t, ONE common monomial gives physical width T_phys=t-r<=T.
For nonzero c, coefficient heights of the unshifted integer numerators F_b=QY_b are at most Q(k+1); the number of indexed leaves is at most sum_(j=1)^k 2^(s j)+2^(s k+1).

For a in N retain the full SIGNED degree-d norm D_a=Norm_K(f_a(alpha)) in Z minus{0}, and put

    B_norm=(1/d)sum_(a in N)lambda_a log|D_a|>=0.

A stopping leaf ending in a has value f_a(alpha), and a terminal sign leaf has value epsilon and norm epsilon^d.
The total stopping weight ending in a is h_k lambda_a.
Therefore

    Lambda_k=(1/d)sum_b omega_b log|Norm_K(Y_b(alpha))|
             =h_k B_norm,
    Res(P,F_b)=Q^d D_b,
    product_b Res(P,F_b)^(n_b)=Q^(d M_k)product_b D_b^(n_b),
    S_int=Q^2 E_k,
    I_k=log Q+Lambda_k,
    I_k-(1/2)log S_int=Lambda_k-(1/2)log E_k
                       <=(T_phys/d)m(P).

The formula with Q applies to the nonzero-c case; c0 has the explicit constant unit packet above.
All original roots, contents and positive copies remain.
In particular positive content g_b contributes g_b^d to Res(P,F_b), with g_b^d dividing Q^d D_b; contents need not be1 or divide Q.
The common monomial multiplies each D_b by nu^-r and the complete signed product by nu^(-r M_k), where nu=Norm_K(alpha)=(-1)^d P(0) in{+1,-1}.
Absolute incomes are unchanged.
Coefficient denominator and FINAL weight denominator are distinct; no extra log Q penalty remains after both exact costs are charged.

**C. Nonflat first-window coefficient test, including its zero-margin boundary.**
Put T=d, P=sum_(i=0)^d p_i t^i, a_i=|p_i| on nonzero positions, H=max a_i>=2, L1=sum a_i and L2=sum a_i^2.
For EVERY integer q>H use the equivalent signed-bit law

    f=P/q-sum_(i:p_i!=0) sign(p_i)B_i t^i,
    Pr(B_i=1)=a_i/q independently.

Its only zero-valued atom is P/q, so

    S=L1/q-L2/q^2,
    p0=product_(i:p_i!=0)(1-a_i/q),
    Delta=(3L2-L1^2)/2,
    E_1=S+p0<=1-Delta/q^2.

Every finite tree has ACTUAL q_k=q and physical union width d.
If Delta>0 then for every finite k,

    E_k<=1-h_k Delta/q^2<1.

If Delta=0 one still has E_1<1 and hence all finite E_k<1: there are at least three nonzero coefficients and the strict three-bit event has positive probability.
No positive Delta/q^2 margin is asserted at Delta0.
If Delta<0 the displayed sufficient bound decides nothing by itself; the exact criterion remains S+p0<1.

**D. Flat case and the COMPLETE diagonal obstruction.**
If instead H=1 and q>=2, the same signed law has TWO zero atoms P/q and(1/q-1)P, with

    p0=(1-1/q)^n+q^-n,
    S=n(q-1)/q^2,

where n is the number of nonzero coefficients.
Both masses are retained.
At first window, the accepted C29 theorem implies E_k>=1 for every finite k.
More generally it excludes strict-below-one energy for this diagonal repair applied to ANY first-window modular codeword on an actual flat P.
This concerns the diagonal coefficient covariance class only; C17's full first-window E_d<1 uses nonzero off-diagonal entries with canceling lag sums.
No wider-window obstruction is asserted.

**E. Fixed-input large-q limitation, uniform in finite depth.**
For EVERY FIXED nonflat P in C, as integers q->infinity,

    p0=1-L1/q+(L1^2-L2)/(2q^2)+O_P(q^-3),
    1-E_1=Delta/q^2+O_P(q^-3),
    1-S/(1-p0)=Delta/(L1 q)+O_P(q^-2).

Single-bit values have absolute full norm1; all remaining nonzero bit values form a fixed finite set with maximum log norm C_P.
Thus

    0<=B_norm<=C_P (L1^2-L2)/(2 d q^2),
    0<=Lambda_k<=B_norm/(1-p0)=O_P(q^-1),
    E_k=1+O_P(q^-1),
    Lambda_k-(1/2)log E_k=O_P(q^-1),

UNIFORMLY over ALL finite k>=1.
Constants may depend on P.
This rules out obtaining a fixed positive surplus merely by increasing q on one fixed input; it does not classify jointly varying inputs/codewords/windows or refute C50's necessary growing-q domain.

**F. Exact q4 control with the content exception retained.**
For ACTUAL P=t^2-3t+1,q4, one has H3,L1=5,L2=11,Delta4,

    S=9/16, p0=9/64, E_1=45/64,
    E_k=(36/55)(1-(9/64)^k)+(9/64)^k,
    q_k=4, T_phys=2, M_k=2*64^k.

At depth1 the seven nonempty bit sets {0},{1},{2},{0,1},{0,2},{1,2},{0,1,2} have signed norms1,1,1,-1,9,-1,4 and respective weights3,27,3,9,1,9,3 divided by64.
The empty set is repaired by P/4+/-1 with weight9/128 each and norm1.
Hence M_1=128 and

    product_b Res(P,F_b)^(128 omega_b)=4^256*9^2*4^6,
    Lambda_1=(log9+3log4)/128,
    S_int=45/4,
    I_1=log4+Lambda_1.

The {0,2} numerator is-3(1+t+t^2), CONTENT3, full resultant144.
The six other bit numerators and both repair numerators are primitive.
Both negative-norm types have even multiplicity18, explaining the positive signed product.
The original all-primitive author error and its18:00 correction are retained in the full proof.
C20's accepted optimum1/3 is smaller than both45/64 and the recursive limit36/55; no new optimum, near-one family or unrestricted gap is claimed.

The theorem constructs finite admissible packets under its exact modular/energy tests and records their full price.
It does not produce an input-uniform suitable codeword, positive deficit, positive full surplus or unrestricted G0001 completion.
Classical Bernoulli-rounding and paired-repair attribution remain at their exact recorded scopes; no source probability-tail theorem is imported.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T10:13 |
| status | open |
| reason | Register the complete finite modular stopping construction, exact arithmetic costs, first-window success/flat boundaries, fixed-input uniform-in-finite-depth limit and exact q4 control. Entire original proof and contribution/source/error-correction history are retained. R261 covers only the original18:00 whole author account; this new statement/wrapper requires separate noncontributor actual extraction review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F with general original-unit/order domain, all finite trees, actual q/M/full norms and every stated success/failure/uniformity boundary. |
| argument | [Entire retained proof](#argument) | ENTIRE original D7 Sections1--8/equations1--21, starting scope, source/recovery/contribution history, actual18:00 content correction and whole freeze. |
| dependency | [Finite nonzero-integer moment domain](Yin_C_G0016_v1.md#statement) | Exact finite rational admissibility and all lag equations; construction is supplied directly, not inferred from PSD alone. |
| dependency | [Complete flat first-window obstruction](Yin_C_G0029_v1.md#statement) | All actual first-window diagonal coefficient covariances have energy at least1; no full-domain or wider-window extension. |
| dependency | [Full original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | SAME final weights, full nonzero signed resultants and actual physical common width, in its general monic domain. |
| support | [Old paired repair](Yin_C_G0043_v2.md#chebyshev-damping-gram-repair-and-width) | Elementary paired +/-1 replacement credited at its actual role; current finite probabilities and recursion proved locally. |
| support | [Necessary coefficient-denominator boundary](Yin_C_G0050_v1.md#statement) | General original-unit q-growth and complete q-versus-M/surplus distinction, as a consistency comparison only. |
| support | [Full first-window existence](Yin_C_G0017_v1.md#statement) | Accepted full E_d<1 comparison, distinct from the restricted diagonal obstruction. |
| support | [Actual quadratic optimum](Yin_C_G0020_v1.md#statement) | Accepted a3,T2 optimum1/3 comparison only; all present q4 arithmetic is independently local. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0261_v1.md#modular-rounding-whole-independent-finding) | Original18:00 D7 whole proof only. The same reviewer's present wrapper contribution bars a self-supplied independent actual extraction verdict. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T10:27 |
| status | proved |
| reason | Adopt the separately performed actual noncontributor extraction/interface finding together with the exact original whole-author and applicable native-review scopes. Preserve all original source/contribution/correction history and finite costs. No uniform surplus, uncomputed-time growth, expanded native domain or unrestricted Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F with general original-unit/order domain, all finite trees, actual q/M/full norms and every stated success/failure/uniformity boundary. |
| argument | [Entire retained proof](#argument) | ENTIRE original D7 Sections1--8/equations1--21, starting scope, source/recovery/contribution history, actual18:00 content correction and whole freeze. |
| dependency | [Finite nonzero-integer moment domain](Yin_C_G0016_v1.md#statement) | Exact finite rational admissibility and all lag equations; construction is supplied directly, not inferred from PSD alone. |
| dependency | [Complete flat first-window obstruction](Yin_C_G0029_v1.md#statement) | All actual first-window diagonal coefficient covariances have energy at least1; no full-domain or wider-window extension. |
| dependency | [Full original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | SAME final weights, full nonzero signed resultants and actual physical common width, in its general monic domain. |
| support | [Old paired repair](Yin_C_G0043_v2.md#chebyshev-damping-gram-repair-and-width) | Elementary paired +/-1 replacement credited at its actual role; current finite probabilities and recursion proved locally. |
| support | [Necessary coefficient-denominator boundary](Yin_C_G0050_v1.md#statement) | General original-unit q-growth and complete q-versus-M/surplus distinction, as a consistency comparison only. |
| support | [Full first-window existence](Yin_C_G0017_v1.md#statement) | Accepted full E_d<1 comparison, distinct from the restricted diagonal obstruction. |
| support | [Actual quadratic optimum](Yin_C_G0020_v1.md#statement) | Accepted a3,T2 optimum1/3 comparison only; all present q4 arithmetic is independently local. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0261_v1.md#modular-rounding-whole-independent-finding) | Original18:00 D7 whole proof only. The same reviewer's present wrapper contribution bars a self-supplied independent actual extraction verdict. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0262_v1.md#c54-modular-rounding-actual-extraction-finding) | Actual fixed statement, complete original preservation and present mathematical/computation interfaces, inspected separately from the original whole scope. |

## Registration and preservation

Date: 2026-10-12T10:13.
The assigned extractor retains the ENTIRE original D7 author account after only its short front matter is removed, its first title is demoted once, exact relative Claim links are rebased, and terminal whitespace is normalized.
Every proof, source-attribution/pending-resolution account, failed implication, content correction, contribution/recovery history and original freeze remains.
Historical pending-review language is not the present Claim assessment.
The [RT87 passage account](../audits/literature/RT87/readme.md#independent-bernoulli-rounding-attribution) is ordinary attribution only and is not a selected proof or Review-binding target.
No tail theorem, original source proof or full-source audit is asserted.
The extractor's R261 stays independent at its original scope; this new wrapper is the extractor's substantive contribution and requires a distinct noncontributor actual review.

## Argument

## Independent modular rounding with exact zero-residue repair

Date: 2026-10-12T09:21.
Human author Yin.
New bounded AUTHOR inquiry under the current G0001 continuation.
Root supplies the modular independent-lift candidate.
This newly allocated D inherits no older address's authority.

## Starting question and actual costs

For a codeword in the full actual modulo-q remainder kernel, investigate the independent integer lifts c_i or c_i-q with mean-zero coefficient sampling.
Their diagonal second moment may solve all lag equations, but some whole polynomial samples can have ZERO actual field residue and are forbidden.
Construct an exact treatment of every such atom and its final weight, or prove a precise failure condition.
Do not discard zero residues without restoring the complete covariance, assume PSD implies finite nonzero-integer realization, or return to a fixed-q near-one construction excluded at C50's recorded scope.

The actual original order/degree, arbitrary growing coefficient denominator q, physical common window, all lag constraints, FINAL rational weights and least denominator, contents, signed full original norms and every copy must remain.
Any native computation first requires a responsible declared J and root coordination.
No theorem, review, construction success or native program is asserted at allocation.
All substantive work continues here.

## Initial reuse

The current C50 statement, C16 finite nonzero-integer moments and C29 first-window diagonal obstruction were inspected.
Existing C10/C43 paired nonzero-value repair, the actual C20 quadratic optimum and local rounding/zero-atom searches will be followed before substantial proof investment.
Root's suggested sampling is a candidate, not an established covariance or nonzero-residue theorem.

<a id="modular-rounding-recovery-and-reuse"></a>
## 1. Dated recovery, exact reuse and contribution limits

2026-10-12T09:55.
The replacement AUTHOR contributor read the actual saved file: it contained only the allocation and initial reuse paragraphs above.
The former author's informal recursion, coefficient criterion and flat-case observations reached this author through root's handoff; they were not a previously saved or independently checked proof.
This dated continuation preserves that original content and reconstructs the whole candidate below.
Root supplied the independent modular-lift mechanism, the preceding author supplied the recursion and proposed coefficient criterion, and the present author supplies the complete reconstruction, exact stopping-tree/denominator/norm accounting and limitations.
All three are substantive contributors.
None of them is an independent reviewer of this account.

The precise retained inputs read here are [C16](Yin_C_G0016_v1.md#statement), for actual nonzero integer residues, finite rational packets and every aggregate lag; [C29](Yin_C_G0029_v1.md#statement), for the entire first-window diagonal-covariance obstruction on flat minimal polynomials; [C50](Yin_C_G0050_v1.md#statement), for necessary coefficient-denominator growth in hypothetical small-measure linear windows; and [C10](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality), for the complete original-root expense.
The [C43 paired repair](Yin_C_G0043_v2.md#chebyshev-damping-gram-repair-and-width) already replaces zero-valued polynomials by pairs with values +1 and -1.
The present use is its elementary two-square mechanism, with the original finite probabilities retained exactly.
[C20](Yin_C_G0020_v1.md#statement) supplies a fixed quadratic comparison, not a premise for the new construction.
Existing accepted proofs are invoked at these exact interfaces; no earlier review is extended to this draft.

Bounded directory searches in Claims, ledgers, source units and the bibliography for independent/randomized rounding, Bernoulli rounding, zero atoms and the candidate coefficient quantities found the existing covariance and paired-repair mechanisms but no registered matching rounding attribution.
Some broad Bernoulli hits concern unrelated convolution or operator results.
One Windows wildcard-path invocation failed before the corrected directory/glob search; it supplied no evidence.
The known independent Bernoulli-rounding step triggered a primary-source search.
Raghavan--Thompson, *Randomized rounding: A technique for provably good algorithms and algorithmic proofs*, Combinatorica 7 (1987), 365--374, DOI 10.1007/BF02579324, was located at the [author-hosted ten-page PDF](https://www.cs.auckland.ac.nz/~cthombor/Pubs/RandomRounding/RandomRounding1987.pdf).
Equation (1.1), printed p.366/PDF p.2, is the identified scalar-rounding locator.
At this continuation's initial save only the primary search extraction and PDF identity had been available; actual primary-passage verification and root-coordinated acquisition remain explicitly pending until a later dated source note.
No concentration theorem, source proof, novelty or priority claim is used.
All finite probability identities below are proved directly.

**Source resolution, 2026-10-12T10:00.**
Root acquired the actual ten-page author scan through canonical source registration and personally rendered/visually read PDF pages 1--2, including printed p.366 equation (1.1).
This author read the resulting [RT87 exact passage account](../audits/literature/RT87/readme.md#independent-bernoulli-rounding-attribution), which records the actual identity and inspection depth.
The preceding pending wording is retained as the history of the initial save; its attribution/acquisition obligation is now resolved at that precise scope.
This author did not independently render the scan.
The source is classical Bernoulli-rounding attribution only, with no imported probability-tail, optimization or zero-repair theorem and no project-review binding.

<a id="modular-rounding-finite-construction"></a>
## 2. Finite modular law and repair of every zero atom

Let P be the ACTUAL monic irreducible minimal polynomial of a nontorsion integer unit alpha, of original degree d>=2, with K=Q(alpha) and actual O0=Z[alpha].
No reciprocity is imposed.
Fix an allowed coefficient window [0,T], T>=0, and let A=A_T be its integer d-by-(T+1) remainder matrix in the actual power basis.
Thus Af is integral and nonzero exactly when the rational polynomial f has nonzero value in O0.
Every column of A is nonzero, since alpha^i is a nonzero field element.
Let q>=2 be an integer and take c=(c_0,...,c_T), with 0<=c_i<q and Ac=0 modulo q.
Set

    x_i=c_i/q, v_i=x_i(1-x_i),
    V=diag(v_0,...,v_T), S=sum_i v_i.

Independently choose B_i in {0,1}, with probabilities Pr(B_i=1)=x_i, and set f_i=x_i-B_i.
Deterministic zero coordinates can be omitted from the index set.
The resulting finite set of indexed atoms has positive rational probabilities lambda_a after zero-probability choices are discarded.
Each q f_i is c_i or c_i-q, and

    E f=0, E(f f^T)=V,
    Af=Ac/q-AB in Z^d.                              (1)

The mean follows from E B_i=x_i.
Independence gives E f_i f_j=0 for i!=j, and the two-point calculation gives E f_i^2=x_i(1-x_i).
This proves EVERY lag cancellation, including repeated index differences, but (1) alone is not admissible: some complete atoms can have Af=0.

Write Z={a:Af_a=0}, N={a:Af_a!=0}, and

    p0=sum_(a in Z)lambda_a.

For every a in N keep f_a with probability lambda_a.
For every a in Z replace f_a by BOTH f_a+e_0 and f_a-e_0, with probability lambda_a/2 each.
Their actual values are +1 and -1.
Pointwise averaging gives

    [(f+e_0)(f+e_0)^T+(f-e_0)(f-e_0)^T]/2
       =f f^T+e_0 e_0^T.

The repaired finite law therefore has mean zero, diagonal second moment V+p0 e_0 e_0^T and exact constant Laurent covariance

    E_1=S+p0.                                       (2)

All its atoms have nonzero actual integral values.
No zero atom was discarded, no conditional renormalization was performed, and its weights still sum to one.
The notation E_1 denotes coefficient energy and hence the circle covariance constant, while p0 is a probability; neither is a field norm.

<a id="modular-rounding-finite-recursion"></a>
## 3. Finite stopping recursion, all covariances and exact success test

Fix a FINITE integer k>=1.
Use independent copies f^(1),...,f^(k) of the complete original law.
Start at zero, add a fresh copy only while the cumulative actual residue is zero, and stop adding copies at the first nonzero residue.
If every one of the k copies used has zero residue, add an independent equiprobable +e_0 or -e_0.
This is a finite tree, not an infinite law or a closure point.

More explicitly, put

    I_j=1_{Af^(1)=...=Af^(j-1)=0}, I_1=1,
    I_(k+1)=1_{Af^(1)=...=Af^(k)=0},
    Y_k=sum_(j=1)^k I_j f^(j)+I_(k+1) epsilon e_0,
    Pr(epsilon=+1)=Pr(epsilon=-1)=1/2.               (3)

Whenever a copy is reached, all previous actual values are zero.
Thus the first nonzero copy supplies the final residue without cancellation by a prefix.
The remaining branch has final value epsilon.
This proves admissibility of every final atom directly in the original order.

For l>j, condition on the first l-1 copies.
The vector I_j f^(j) and the scalar I_l are then fixed, whereas the fresh f^(l) has mean zero.
Hence every cross second moment between different increments vanishes.
The last signed correction likewise has conditional mean zero, so its cross terms vanish even though I_(k+1) depends on all earlier copies.
Also Pr(I_j=1)=p0^(j-1).
Therefore, with

    h_k=sum_(j=0)^(k-1)p0^j,

the COMPLETE coefficient second moment and energy are

    E(Y_k Y_k^T)=h_k V+p0^k e_0 e_0^T,
    E_k=h_k S+p0^k.                                (4)

All off-diagonal entries are zero, so every aggregate positive lag vanishes in the original allowed window, with no condition on distinct exponent differences.
This proves an actual finite member of C16's nonzero-integer moment hull rather than substituting a PSD relaxation.

For nonzero c, p0<1.
Indeed p0=1 would imply Af=0 for every atom and therefore

    0=E[(Af)(Af)^T]=A V A^T.

Taking traces gives sum_i v_i ||A e_i||_2^2=0.
Every summand is nonnegative and every column is nonzero; hence every v_i=0, and 0<=c_i<q forces c=0, a contradiction.
Thus for nonzero c,

    h_k=(1-p0^k)/(1-p0),
    1-E_k=h_k(1-S-p0),
    lim_(k->infinity)E_k=S/(1-p0).                  (5)

The limit in (5) is a numerical limit of finite energies, not an asserted admissible infinite packet.
In particular E_k<1 for some finite k if and only if E_1=S+p0<1, and then every finite k has this property.
RECURSION CANNOT REPAIR FAILURE OF THE ONE-STEP ENERGY TEST.
When E_1<1 the finite deficits increase to 1-S/(1-p0).
When c=0, every base atom is zero and the final law is simply +/-1 with equal weights, E_k=1; formula (4) remains valid and the fraction in (5) is not used.

<a id="modular-rounding-all-finite-costs"></a>
## 4. Actual denominators, support, contents, signed norms and every copy

Keep the complete indexed stopping tree.
A leaf that stops at depth j consists of a_1,...,a_(j-1) in Z and a_j in N; it has polynomial sum_l f_(a_l) and FINAL weight product_l lambda_(a_l).
A terminal repaired leaf consists of k labels in Z and a sign epsilon; it has polynomial sum_l f_(a_l)+epsilon e_0 and FINAL weight (product_l lambda_(a_l))/2.
These are the actual normalized weights omega_b.
No repeated values or equal polynomials are merged in the stated packet.

For nonzero c define

    Q=q/gcd(q,c_0,...,c_T).

Every base atom has exactly these same coefficient fractions modulo Z, so its ACTUAL least coefficient denominator is Q.
Every final sum has denominator dividing Q.
At least one positive-weight nonzero atom exists and occurs already as a depth-one leaf for every k; its denominator is Q.
Therefore the ACTUAL least common coefficient denominator of the complete finite packet is

    q_k=Q,                                         (6)

not merely a divisor bound.
The equality depends on keeping the actual tree's depth-one leaves, not on an arbitrary replacement with the same covariance.
For c=0 it is q_k=1.

Let s be the number of indices with 0<c_i<q.
Every base probability has denominator dividing Q^s.
If M_k is the ACTUAL least denominator of all FINAL indexed weights, then

    M_k=lcm_b denominator(omega_b),
    M_k divides 2 Q^(s k), n_b=M_k omega_b in Z_{>0},
    sum_b n_b=M_k.                                 (7)

This is a finite bound, not an assertion that the upper bound is least or that M_k stays bounded as k varies.
Combining equal leaves would change the indexed least denominator and must be accounted for separately.
For p0=0 there are only depth-one leaves, so unnecessary zero-tree levels add no copies or weights.

Formula (4) identifies the exact union of nonzero coefficient positions: it is {i:v_i>0}, together with position 0 if p0>0.
This follows because a second-moment diagonal entry is positive exactly when some positive-weight leaf has a nonzero coefficient there.
Write r for its least position and t for its greatest, and T_phys=t-r.
One COMMON monomial shift t^(-r) puts every polynomial into [0,T_phys], with T_phys<=T.
It changes every field value by the same unit alpha^(-r); no independent shift or padded endpoint is charged as physical width.
In the nonzero-c case |(Y_k)_i|<=k+1, hence the integer numerators F_b=Q Y_(k,b) have coefficient heights at most Q(k+1).
There are at most 2^s original atoms and at most sum_(j=1)^k 2^(s j)+2^(s k+1) indexed final leaves; this crude finite count is not used as a uniform bound.

For a in N, set u_a=f_a(alpha) and retain its FULL SIGNED original degree-d norm D_a=Norm_K(u_a), a nonzero integer.
A nonzero stopping leaf ending in a has value u_a EXACTLY, regardless of its preceding zero-valued polynomials.
A terminal repaired leaf has value epsilon and signed norm epsilon^d.
No zero prefix is assigned a nonzero norm or included in a logarithm.
Define the unconditioned base norm income

    B_norm=(1/d)sum_(a in N)lambda_a log|D_a|>=0.

The total FINAL weight of all leaves ending in a is h_k lambda_a, while terminal repaired mass is p0^k.
Consequently

    Lambda_k=(1/d)sum_b omega_b log|Norm_K(Y_(k,b)(alpha))|
             =h_k B_norm.                          (8)

These are full original norms, with no deleted contracting, circle or exterior conjugates.
For the unshifted numerators,

    Res(P,F_b)=Q^d D_b,
    product_b Res(P,F_b)^(n_b)
        =Q^(d M_k) product_b D_b^(n_b),
    S_int=Q^2 E_k,
    I_k=log Q+Lambda_k,
    I_k-(1/2)log S_int=Lambda_k-(1/2)log E_k.        (9)

Here D_b=D_a or epsilon^d according to the leaf.
One may group equal norm types only with their full integer multiplicities; M_k h_k lambda_a is an integer because it is the sum of all n_b ending in a.
The constant-sign terminal groups have total multiplicities M_k p0^k/2 each when p0>0, again integers because they are sums of their leaves.
The common monomial normalization multiplies every signed D_b by nu^(-r), nu=Norm_K(alpha)=(-1)^d P(0) in {+1,-1}; the COMPLETE copied product then acquires nu^(-r M_k).
Absolute incomes do not change.
These signs are retained rather than automatically set to +1 on a general nonreciprocal input.

If g_b is the positive integer content of F_b, the primitive part is not silently substituted.
The exact identity Res(P,F_b)=g_b^d Res(P,F_b/g_b)=Q^d D_b keeps every content and its divisibility g_b^d | Q^d D_b.
Contents need not be one or divide Q.
Equation (9) uses the original numerators and every copy, not a primitive-content discount.
Applying the accepted C10 inequality to this ACTUAL finite complementary packet after the one common shift gives

    Lambda_k-(1/2)log E_k <= (T_phys/d)m(P).        (10)

All q, M, norm and width data in (10) are those of this same packet.
In particular a growing denominator is not an additional uncancelled log Q penalty after the exact identities (9).

<a id="modular-rounding-first-window-criterion"></a>
## 5. First-window coefficient criterion and all zero events

Now set T=d and P(t)=sum_(i=0)^d p_i t^i.
Put a_i=|p_i|, sigma_i=sign(p_i) on nonzero positions, n=number of nonzero coefficients, and

    H=max_i a_i, L1=sum_i a_i, L2=sum_i a_i^2.

Assume H>=2 and choose ANY integer q>H.
Independently sample B_i with success probability a_i/q at each nonzero position and define

    f(t)=P(t)/q-sum_(i:p_i!=0) sigma_i B_i t^i.
                                                            (11)

For positive p_i these are the original modular choices; for negative p_i the same law uses the residue c_i=q-a_i and the complementary Bernoulli bit.
Thus (11) is exactly a law from Section 2, with c=P modulo q, and it has mean zero and

    S=L1/q-L2/q^2.                                  (12)

Its actual value is minus the signed bit polynomial, hence is an actual order integer.
To classify EVERY zero atom, if f(alpha)=0 then the signed bit polynomial vanishes at alpha and has degree at most d.
Minimality forces it to be hP for some rational h.
Its leading coefficient is B_d in {0,1}, since P is monic, so h=0 or 1.
If h=0 every bit is zero.
If h=1, coefficient comparison gives B_i=a_i at all nonzero positions, impossible when some a_i>=2.
Consequently the sole zero atom is P/q and

    p0=product_(i:p_i!=0)(1-a_i/q).                 (13)

The event has positive probability.
Some nonzero atoms exist, for example selecting just one bit gives value -sigma_i alpha^i, an actual unit.
The leading coefficient of every base atom is 1/q or 1/q-1, so q_k=q in every finite tree.
Since p_0 and p_d are nonzero and q>H, both end positions have positive variance; the ACTUAL union width is exactly d.
In particular none of the first-window cost is removed by a support convention.

Define

    Delta=(3 L2-L1^2)/2.

To bound (13), let R=sum_i B_i.
The elementary pointwise inequality

    1_{R>=1} >= R-R(R-1)/2

holds for every nonnegative integer R: check R=0,1,2 directly, and for R>=3 the right side is at most zero.
Taking expectations gives

    1-p0 >= L1/q-sum_(i<j)a_i a_j/q^2.

Together with (12) and 2 sum_(i<j)a_i a_j=L1^2-L2, this yields

    E_1=S+p0 <= 1-Delta/q^2.                        (14)

Therefore if Delta>0 every q>H gives a complete finite rational nonzero-integer complementary packet in the first window with

    E_k <= 1-h_k Delta/q^2 <1, k>=1.               (15)

No native search or experiment is needed for (14).
It is a sufficient coefficient test, not an equivalence: Delta<=0 does not by itself refute E_1<1.
The EXACT criterion remains S+p0<1 from (5) and (12)--(13).
Since any nontorsion irreducible integer-unit polynomial of degree>=2 has at least three nonzero coefficients (a unit binomial t^d+/-1 has only roots of unity), the pair-count inequality is actually strict here: the positive-probability event R=3 makes it strict.
This also gives E_1<1 when Delta=0, without asserting the positive explicit margin Delta/q^2 in that boundary case.

If instead H=1, the h=1 event IS possible and must be retained.
For q>=2 the two zero atoms are P/q and (1/q-1)P, with total probability

    p0=(1-1/q)^n+q^(-n), S=n(q-1)/q^2.            (16)

The repaired and recursively repaired covariances are still diagonal.
The adopted COMPLETE C29 theorem therefore gives E_k>=1 for every finite k and every q.
This conclusion also excludes any other first-window modular codeword handled by this diagonal construction, not just (11).
It neither says the full C16 first-window optimum is one nor applies to wider windows.
C17's accepted unrestricted strict-below-one result necessarily uses nonzero off-diagonal entries whose lag sums cancel.
Omitting the second zero atom in (16) would contradict the actual residue requirement and is not an allowable simplification.

<a id="modular-rounding-fixed-input-limits"></a>
## 6. Recursion, growing denominators and the remaining uniform gap

For a FIXED nonflat P in Section 5, finite product expansion as integer q tends to infinity gives

    p0=1-L1/q+(L1^2-L2)/(2q^2)+O_P(q^(-3)),
    1-E_1=Delta/q^2+O_P(q^(-3)),
    1-S/(1-p0)=Delta/(L1 q)+O_P(q^(-2)).           (17)

The constants are allowed to depend on this fixed actual polynomial.
If Delta>0, (5) shows that even arbitrarily large finite k can amplify the one-step deficit only to the last quantity in (17), which tends to zero.
Thus merely sending q to infinity on one input does not yield a fixed positive deficit.

The full norm income also stays in this fixed-input scale.
A bit set of cardinality one has value -sigma_i alpha^i and absolute full norm one.
There are only finitely many other bit sets; their nonzero norms have some finite fixed maximum logarithm C_P.
The probability of at least two successful bits is at most sum_(i<j)a_i a_j/q^2, since 1_{R>=2}<=R(R-1)/2.
Zero bit sets are excluded before taking logarithms.
Hence

    0<=B_norm<=C_P (L1^2-L2)/(2 d q^2),
    0<=Lambda_k<=B_norm/(1-p0)=O_P(q^(-1)).        (18)

Uniformly over ALL finite k, (4)--(5) place E_k between 1 and S/(1-p0), so E_k=1+O_P(q^(-1)) and

    Lambda_k-(1/2)log E_k=O_P(q^(-1)).             (19)

This fixed-input statement charges full norms and has no unproved uniform bound on C_P, L1, L2 or H across different inputs.
It neither constructs a small-measure sequence nor obstructs every jointly varying growing-denominator scheme.
The accepted C50 necessity q->infinity in hypothetical small-measure linear windows therefore remains intact.
To obtain an input-uniform Mahler gap from the present mechanism one would still have to supply actual suitable codewords/windows, control their complete zero-residue probabilities and keep the FULL surplus in (10) uniformly positive as the input varies.
The coefficient sufficient condition alone does not supply any of those unrestricted selection assertions.

<a id="modular-rounding-hand-quadratic-control"></a>
## 7. Exact hand control and comparison with the existing optimum

For the actual P=t^2-3t+1, take q=4.
This polynomial is irreducible because its discriminant 5 is not a rational square, and its larger root is greater than one; it is an actual nontorsion unit polynomial.
Here (a_0,a_1,a_2)=(1,3,1), H=3, L1=5, L2=11 and Delta=4.
Thus

    S=9/16, p0=9/64, E_1=45/64<1,
    E_k=(36/55)(1-(9/64)^k)+(9/64)^k.              (20)

The bound (14) gives E_1<=3/4; the actual 45/64 is strictly smaller because triples have positive probability.
The only zero bit set is empty, with polynomial P/4.
Its two repaired leaves P/4+1 and P/4-1 have weights 9/128 each, values +1 and -1, and norms +1 and +1.
For the other seven bit sets U, the value is -sum_(i in U)sigma_i alpha^i.
With alpha^2=3alpha-1, the full signed norms and FINAL weights are as follows; these are hand algebraic equalities, not computational output.

| Bit set U | Actual value | Full signed norm | FINAL weight |
| --- | --- | --- | --- |
| {0} | -1 | +1 | 3/64 |
| {1} | alpha | +1 | 27/64 |
| {2} | -alpha^2 | +1 | 3/64 |
| {0,1} | alpha-1 | -1 | 9/64 |
| {0,2} | -1-alpha^2=-3alpha | +9 | 1/64 |
| {1,2} | alpha-alpha^2=1-2alpha | -1 | 9/64 |
| {0,1,2} | -1+alpha-alpha^2=-2alpha | +4 | 3/64 |

The binary norm formula Norm(m+n alpha)=m^2+3mn+n^2 verifies every row.
For this exact indexed one-step packet q_1=4 and M_1=128, because all weights divide 128 and 9/128 occurs.
Its integer numerator for bit set U is P-4 sum_(i in U)sigma_i t^i.
Six of the seven such numerators are primitive: either an endpoint coefficient is 1, or U={0,1,2} and the middle coefficient is 1.
The exception U={0,2} has numerator -3(1+t+t^2), of content THREE; its full resultant is 16*9=144, retaining the content factor 3^2.
The two repaired numerators are P+4 and P-4, with coefficient contents one.
All numerators have actual union width two.
Their full resultants are 4^2 times the displayed signed norms; the copied complete product is

    product_b Res(P,F_b)^(128 omega_b)=4^256 9^2 4^6.

The two negative-norm types each have multiplicity 18, so the overall sign in this control is positive; no negative factors were discarded.
Moreover

    Lambda_1=(log 9+3 log 4)/128,
    S_int=45/4,
    I_1=log4+Lambda_1,
    I_1-(1/2)log S_int=Lambda_1-(1/2)log(45/64)
         <=m(P)=log((3+sqrt5)/2).                 (21)

This checks the same original d=2 and T_phys=2 in (10).
The already adopted C20 exact unrestricted first-window optimum is 1/3 for this polynomial, strictly better than 45/64 and even the recursion's limiting 36/55.
This example validates arithmetic bookkeeping and the finite construction; it is not a new optimum, a near-one sequence, or a new fixed low-measure bound.

For every finite depth k in this SAME fixed example, the terminal repaired leaf has weight 9^k/(2*64^k), already in lowest terms.
The denominator upper bound (7) is 2*4^(3k)=2*64^k, so the ACTUAL indexed denominator is exactly M_k=2*64^k.
This is an explicit example of growing FINAL weights despite fixed actual coefficient denominator q_k=4 and fixed physical width two; their different roles cannot be interchanged.

**Author correction before freeze, 2026-10-12T10:00.**
The first saved version of Section 7 said that all seven bit numerators were primitive merely because their endpoints were 1 or -3.
That inference failed when BOTH endpoints were -3.
Direct coefficient inspection gives the exceptional numerator -3(1+t+t^2) for U={0,2}, and the preceding paragraph has been corrected with its content 3 and full resultant 144.
No energy, weight, field norm or copied-product value changes.
This records the actual author error and repair; it is not an independent review finding.
No other earlier account is silently replaced.

<a id="modular-rounding-entire-author-freeze"></a>
## 8. Complete author self-check, frozen scope and handoff

The responsible author checked the actual order/power-basis membership, all positive-probability atoms and both zero/nonzero residues; mean-zero independent coordinates and every lag; finite stopping-tree probabilities, conditional cross terms and terminal signed repair; the p0=0 and c=0 endpoints and proof that nonzero c forces p0<1; the exact one-step success equivalence and finite-versus-infinite distinction; ACTUAL q_k=Q via retained depth-one leaves, least FINAL M_k versus its upper bound, actual support and one common shift; full original signed norms, every copied multiplicity, numerator contents, monomial norm signs and the C10 input; the unique nonflat zero event versus both flat zero events; every inequality direction in the pair count and Delta criterion; fixed-P limits including the full norm-income bound; and every rational number, signed norm, content and copied factor in the quadratic hand control.
The content error and its actual correction are retained immediately above.

The complete Sections 1--8 and equations (1)--(21), with source and contribution history, are AUTHOR-FROZEN at 2026-10-12T10:00 for a separately organized whole noncontributor review.
This is a complete proof draft with author self-check, not independent acceptance or a new C assessment.
Root, the preceding author and this recovery author all contributed; none can supply the whole independent review.
The earlier material check passed for the then-current D7 and is repeated after this freeze; it validates structure and locators, not these proofs.

No native mathematical program, solver, enumeration or new J was used.
The unrestricted G0001 contract remains unresolved.
The next local action is the separately organized whole review of this exact frozen body and then any root-controlled registration/adoption; further construction would require a genuinely changed selection or covariance mechanism at the boundaries in Sections 5--6.
