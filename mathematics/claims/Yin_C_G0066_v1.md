---
author: Yin
---
# Complete sign-product packets and the original-root amplitude-balance obstruction

Date: 2026-10-12T12:20.
Human author Yin.
Fixed extraction under the continuing G0001 authorization.
g0001_routes authored the original D20 mathematics and now authors this exact statement/wrapper.
Root independently whole-reviewed the complete original20:09 body in R285.
That original finding is support only and does not inspect this new extraction; a different actual statement/interface review remains required.
The ENTIRE original candidate, proof, hand controls, histories, source boundaries and freeze are retained below.
No adoption or draft retirement is performed.

## Statement

Let P be an ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, with original degree d>=2, field K=Q(alpha), monogenic order O0=Z[alpha], ALL original conjugates beta_i=r_i z_i with r_i>0 and |z_i|=1, and total logarithmic Mahler measure m=m(P)>0.
Neither reciprocity nor flat coefficients are assumed.

Choose an integer r>=1, positive integers h_j and NONZERO integer amplitudes a_j,b_j for1<=j<=r.
Keep all2^r sign labels epsilon in{-1,+1}^r with their FINAL indexed weights omega_epsilon=2^(-r), even if different labels produce equal polynomials.
Define

    F_epsilon(t)=product_j(a_j+epsilon_j b_j t^(h_j)),
    T=sum_j h_j, M=2^r, U=T m/d,
    A_j=a_j²+b_j², S=product_j A_j,
    G_j(t)=a_j²-b_j² t^(2h_j),
    R_j=Res(P,G_j),
    D_epsilon=Norm_(K/Q)(F_epsilon(alpha)),
    v_j=a_j²b_j²/A_j² in(0,1/4].

This is the complete independent-sign PRODUCT family; unequal amplitudes do not mean unequal sign probabilities.
Repeated and overlapping frequencies are allowed.
Nonproduct sign weights, arbitrary mixtures or coordinate transformations are not silently included.

**A. Actual complementary packet and exact full arithmetic gate.**
Every F_epsilon(alpha) is a NONZERO actual O0 integer.
Every polynomial has nonzero constant and degree-T coefficients, so its actual width and the actual common union width are exactly T.
The complete circle identity and all signed norm copies are

    (1/M)sum_epsilon |F_epsilon(z)|²=S for |z|=1,
    (1/M)sum_epsilon ||F_epsilon||_2²=S,
    product_epsilon D_epsilon
       =product_j R_j^(2^(r-1)).

All D_epsilon and R_j are nonzero signed integers, using the original field and degree.
Define the raw integer packet's income and full surplus

    I=(1/(dM))sum_epsilon log|D_epsilon|,
    sigma=I-(1/2)log S.

Then

    I=sum_j log|R_j|/(2d),
    sigma=sum_j sigma_j,
    sigma_j=log|R_j|/(2d)-(1/2)log A_j,
    sigma>0 iff product_j |R_j|>S^d.

The last equivalence is an EXACT finite integer-resultant positivity test, not a proof of positive income uniformly over inputs.
Moreover sigma/T=sum_j(h_j/T)(sigma_j/h_j): product formation cannot improve surplus per physical width beyond the best constituent in that same packet.
It does not ensure a constituent with a uniform absolute margin when r grows.

**B. An all-input original-root deficit.**
Define the ACTUAL damped moments

    D_h=(1/d)sum_i exp(-2h|log r_i|) z_i^(2h).

They are real by conjugate pairing and have absolute value at most1.
This symbol D_h denotes a root moment, distinct from the indexed signed norms D_epsilon.
Put

    L_j=1-2v_j(1+Re D_(h_j)).

For every stated input and packet, with NO small-measure assumption, 0<L_j<=1 and

    sigma<=U+(1/4)sum_j log[1-2v_j(1+Re D_(h_j))]
          <=U-(1/2)sum_j v_j(1+Re D_(h_j)).

Thus actual positive full surplus NECESSARILY satisfies

    sum_j v_j(1+Re D_(h_j))<2U.

More generally sigma>=eta>0 implies that sum is at most2(U-eta).
Passing this spectral test is not sufficient for positivity; the exact arithmetic gate in A remains essential.
All original roots, radial damping and original exponents are retained, with no assumed preservation of the degree of alpha^(2h).
The damped sums may equivalently be written, after conjugate pairing, with beta_i^(2h) on |beta_i|<=1 and beta_i^(-2h) on |beta_i|>1.

**C. Small-measure total balance and primitive-amplitude height.**
Use the precisely accepted angular-bound function

    c0=log(2)/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0) log sqrt(c0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0.

Under the ADDITIONAL hypotheses

    0<2U<=h0, delta(U)=epsilon(2U)+4U<1,

one has |D_h|<=delta(U) for EVERY h<=T and

    sigma<=U+(1/4)sum_j log[1-2(1-delta(U))v_j]
          <=U-[(1-delta(U))/2]sum_j v_j.

Consequently sigma>0 forces

    sum_j v_j<2U/[1-delta(U)].

For the primitive amplitude height and ratio

    H_j=max(|a_j|,|b_j|)/gcd(|a_j|,|b_j|),
    x_j=min(|a_j|,|b_j|)/max(|a_j|,|b_j|),

the same positive-surplus packet must satisfy

    sum_j x_j²<8U/[1-delta(U)],
    sum_j H_j^(-2)<8U/[1-delta(U)].

If all H_j<=H, necessarily H²>r[1-delta(U)]/(8U).
If all x_j>=xi>0, then

    sigma<=U-[(1-delta(U))/2] r xi²/(1+xi²)².

For any fixed C>0 and ANY hypothetical sequence of actual inputs with m(P)->0, packets of this class at T<=C d eventually satisfy the small-measure conditions.
Every such POSITIVE-surplus packet must have sum_j v_j=O_C(m(P)).
Bounded primitive-amplitude families cannot give positive surplus there; uniformly nondegenerate ratios give strictly NEGATIVE surplus eventually, even with arbitrarily growing r.
Increasing factor count spends the same total balance budget rather than creating a separate allowance per factor.
No such input sequence, positive packet or surviving high-bias construction is asserted to exist.

**D. Actual q, FINAL indexed M, contents and legal rational rescalings.**
The raw integer construction has actual least coefficient denominator q=1 and actual FINAL indexed-weight denominator M=2^r, each copy multiplicity1.
Its complete signed copied resultant is exactly A's product.
Every output content is retained.
Common integer amplitude factors multiply both the full norm income and one-half log energy by the same logarithmic scalar and cannot change sigma or v_j; their factors are not dropped from the actual signed products.

The same balance and surplus conclusions extend to ONE common positive rational rescaling f_epsilon=c F_epsilon PROVIDED EVERY f_epsilon(alpha) remains a NONZERO element of the ACTUAL O0.
Norm divisibility alone is not a membership test.
Let q_star be the ACTUAL least coefficient denominator after this operation, H_epsilon=q_star f_epsilon in Z[t], and D'_epsilon=Norm(f_epsilon(alpha)) the full signed nonzero integer norms.
Then

    E=c²S,
    Lambda=(1/(dM))sum_epsilon log|D'_epsilon|=log c+I,
    Lambda-(1/2)log E=sigma,
    Res(P,H_epsilon)=q_star^d D'_epsilon,
    product_epsilon Res(P,H_epsilon)
       =q_star^(dM)product_epsilon D'_epsilon.

The q_star, denominator of c before cancellation and FINAL indexed M are not identified.
Every actual numerator content and signed norm remains.
Nonzero rational-amplitude products reduce to integer-amplitude products times a common rational scalar by clearing each factor; the extension applies exactly when their final actual values satisfy the same O0 condition.
It does not declare all rational amplitudes admissible.

A single common monomial shift preserves energy, coefficient denominator, indexed weights, actual width and absolute norms because alpha is an actual O0 unit, while its signed norm powers remain in the copied product.
Independent shifts of different atoms are not part of this width assertion.
Any later merging or positive splitting of labels requires recalculation of the actual FINAL indexed denominator and copy exponents; M=2^r describes the declared raw indexed construction, not arbitrary postprocessing.

This result treats a specified factorized complementary family at arbitrary coefficient energy, including any legal common integral-value rational normalization.
It supplies the exact finite gate and new necessary amplitude budget; it does not supply uniform positive arithmetic income.
The older balanced-pair negative limit is credited, not improved by a relabeled constant.
General nonfactorized packets, nonproduct sign weights, arbitrary tailored transformations and unrestricted G0001 remain outside its conclusion.
No new native calculation or source theorem is a premise.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T12:20 |
| status | open |
| reason | Register the precise independent-sign product family, full norm-copy identity, exact arithmetic positivity gate, all-input original-root deficit and conditional small-measure total amplitude/height budget, with complete original costs. Entire20:09 D20 is retained. R285 whole-reviewed that original body only; the original author also wrote this new wrapper, which requires a separate actual review before adoption. No successful uniform lower-income construction or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, actual general unit input, complete indexed product family, actual signed norms/width, all-input versus conditional small-measure conclusions, true q/FINAL M and legal rational rescaling limits. |
| argument | [Entire retained original proof](#argument) | Complete20:09 D20 allocation/candidate/reuse history, Sections1--7/equations1--17, exact hand controls, source/role boundaries, all costs and final freeze. |
| dependency | [Original-root finite Poisson/reversal bound](../ledger/Yin_L_G0318_v1.md#polynomial-poisson-majorant) | Exact finite polynomial bound for G_j at ALL original conjugates, with degree2h_j, its negative lag and radial damping; inherited attribution only, no source-scope enlargement. |
| dependency | [Actual powered angular estimate](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | ONLY partC: accepted epsilon at original cutoff2T and height2U, all actual powered-degree multiplicities, with retained Pri11/Dim19 acceptance limits. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0285_v1.md#biased-sign-product-whole-independent-finding) | Entire original20:09 D20 proof and exact direct interfaces/controls. It does not inspect this new statement/wrapper or prospectively adopt it. Finding relationship: self-reviewed. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T12:43 |
| status | proved |
| reason | Adopt the complete original whole R285 and separate actual extraction R289v2, whose dated correction repairs literal square-encoding defects while preserving v1. Exact complete sign-product arithmetic and the necessary total amplitude budget are proved at their stated input and small-measure scopes; the high-bias possibility remains unproved, and no uniform gap follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, actual general unit input, complete indexed product family, actual signed norms/width, all-input versus conditional small-measure conclusions, true q/FINAL M and legal rational rescaling limits. |
| argument | [Entire retained original proof](#argument) | Complete20:09 D20 allocation/candidate/reuse history, Sections1--7/equations1--17, exact hand controls, source/role boundaries, all costs and final freeze. |
| dependency | [Original-root finite Poisson/reversal bound](Yin_C_G0600_v1.md#polynomial-poisson-majorant) | Exact finite polynomial bound for G_j at ALL original conjugates, with degree2h_j, its negative lag and radial damping; inherited attribution only, no source-scope enlargement. |
| dependency | [Actual powered angular estimate](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | ONLY partC: accepted epsilon at original cutoff2T and height2U, all actual powered-degree multiplicities, with retained Pri11/Dim19 acceptance limits. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0285_v1.md#biased-sign-product-whole-independent-finding) | Entire original20:09 D20 proof and exact direct interfaces/controls. It does not inspect this new statement/wrapper or prospectively adopt it. Finding relationship: self-reviewed. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0289_v2.md#c66-sign-product-actual-extraction-finding) | Entire actual statement, complete retained original body and precise direct interfaces separately inspected after allocation, preserving earlier review scopes and corrections. Finding relationship: self-reviewed. |

## Registration and complete preservation

The ENTIRE original20:09 D20 body follows, with only duplicate front matter represented once, its first title demoted from one hash to two, and line endings/separating terminal blank space normalized.
Every original candidate, mathematical formula, hand check, anchor, historical status, contribution, source limit and freeze is retained.
Existing ../claims/ and ../ledger/ links remain valid from the Claim directory, so no locator rebasing is needed.

The [original D20 freeze](#biased-sign-product-entire-author-freeze) is extraction ancestry and the complete preservation target, not an additional missing proof.
The old [L318 balanced-pair/common-filter failure](Yin_C_G0600_v1.md#common-filter-cancellation-obstruction), [L168 actual cyclic UPPER cost](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost), and the C62/C63 comparisons remain at their original credited roles.
No lower arithmetic income is inferred from an upper-cost theorem.
No inherited source-proof scope is enlarged.

The original author also writes this wrapper and cannot independently review it.
R285 is original whole support; a separate actual extraction/interface finding and responsible adoption decision are still required.
Complete-body comparison and scoped material checks verify preservation/structure only.
No adoption, D retirement or new native mathematical execution accompanies this registration.

## Argument


## Complete biased-sign product packets and their original-root balance budget

Date: 2026-10-12T12:01.
Human author Yin.
New AUTHOR inquiry by g0001_routes under root-coordinated continuing G0001.
Root gave only the broad absolute-degree-multiple/full-surplus question, not this class, formulas or proof.
This author selects the independent-sign product family and develops its complete arithmetic and quantitative obstruction here.
No new native mathematical program or source acquisition is planned.

## Bounded reuse and changed question

The author read [C62](Yin_C_G0062_v1.md#statement) and [C63](Yin_C_G0063_v1.md#statement) at their actual flat E<1 first/fixed-extra-window scopes, including the fact that neither covers all E>=1 packets or all degree-proportional windows.
The author is C63's wrapper contributor and separately reviewed C62; those roles supply no independent review of this new work.
[L318's common-filter and balanced-binomial failure](Yin_C_G0600_v1.md#common-filter-cancellation-obstruction) already gives the exact pair1+/-t^h with its negative degree-linear near-one surplus.
[L318's original-root Poisson/reversal calculation](Yin_C_G0600_v1.md#polynomial-poisson-majorant) and [signed weighted inequality](Yin_C_G0600_v1.md#weighted-integral-bundle-bound) are accepted interfaces.
[L168](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost) is an UPPER cyclic-product cost, not an arithmetic lower income or gap theorem.
Those old conclusions are not claimed anew.

A bounded Claim/ledger screen for tensor, Hadamard, biased/amplitude, product packets and binomial mechanisms found the old balanced pair, common-filter obstruction, minimum-energy binomial classification and arithmetic paraunitary transformations.
It did not locate an all-amplitude independent-sign product balance budget.
One initial PowerShell brace-style path search failed without supplying mathematical evidence; the actual directory/glob search was then used.
This is bounded reuse, not a literature-wide novelty claim.
Root's current short-row universally integral paraunitary inquiry is a different construction and is not a premise.

The present class is allowed to have integer coefficient energy GREATER than one.
It changes the class behind the recent below-one first-window barriers.
The candidate is not claimed to solve G0001: it will either identify a genuine arithmetic gate or close this more flexible factorized recipe with a precise necessary condition.

<a id="biased-sign-product-author-domain"></a>
## 1. Responsible candidate, exact domain and planned discriminator

Fix an ACTUAL monic irreducible nontorsion integer-unit minimal polynomial P of original degree d>=2, alpha a root, K=Q(alpha), O0=Z[alpha], all original roots beta_i and total measure m=m(P)>0.
No reciprocity or flatness is imposed.
Choose a positive integer r, positive integers h_j and nonzero integer amplitudes a_j,b_j for1<=j<=r.
The complete INDEXED family has2^r labels epsilon in{-1,+1}^r and

    F_epsilon(t)=product_(j=1)^r(a_j+epsilon_j b_j t^(h_j)),
    omega_epsilon=2^(-r), T=sum_j h_j.

All labels are retained even if some polynomials happen to coincide.
The work will keep the actual O0 values, full signed original resultants, actual common physical width T, q and FINAL indexed weight denominator distinct.
It will not divide by an amplitude and silently assume the resulting residue remains integral.

Proposed exact algebra: averaging the squared modulus over independent signs on the circle gives constant S=product_j(a_j²+b_j²).
Complete norm multiplication should yield

    product_epsilon Norm(F_epsilon(alpha))
       =product_j Res(P,a_j²-b_j² t^(2h_j))^(2^(r-1)),
    surplus=sum_j {log|Res(P,a_j²-b_j² t^(2h_j))|/(2d)
                            -(1/2)log(a_j²+b_j²)}.

These formulas require the nonzero original-value and endpoint proofs below.
The proposed new discriminator uses the ACTUAL original damped moments

    D_h=(1/d)sum_i exp(-2h |log|beta_i||)
                          (beta_i/|beta_i|)^(2h),
    v_j=a_j² b_j²/(a_j²+b_j²)².

Applying the old Poisson/reversal lemma to each PRODUCT polynomial a_j²-b_j²t^(2h_j), before treating the factors as an alleged arithmetic gain, suggests a per-factor upper deficit proportional to v_j(1+Re D_(h_j)).
In a genuinely small-total-measure regime the accepted powered angular bound makes Re D_h close to0 uniformly in h<=T.
If valid, positive full surplus forces the SUM of all amplitude balances to be small.
This would cover arbitrarily many factors and input-adapted unequal amplitudes, including repeated/overlapping frequencies; it is stronger than merely restating the negative limit of a single fixed balanced pair.

No proof claim is accepted at this allocation.
The remaining work is to establish all local identities and the precise log bound, ensure its argument is positive, formulate the finite exact resultant positivity criterion, distinguish sign-indexed M from coalesced labels and any optional integral normalization, and state the small-measure/large-amplitude consequences with every quantifier.
Every failed strengthening and source boundary will remain in this responsible D.
No native run is authorized or needed for the proposed hand calculation.

<a id="biased-sign-product-exact-packet"></a>
## 2. Complete packet identity, original nonvanishing and exact arithmetic gate

The following establishes the allocation candidate without deleting or aggregating any label.
Put

    A_j=a_j²+b_j²>0,
    G_j(t)=a_j²-b_j² t^(2h_j),
    R_j=Res(P,G_j),
    D_epsilon=Norm_(K/Q)(F_epsilon(alpha)),
    M=2^r, S=product_j A_j, U=T m/d.                 (1)

Every factor a_j+epsilon_j b_j alpha^(h_j) is nonzero.
If it were zero, alpha^(h_j) would be rational.
It and its inverse are algebraic integers since alpha is an integer unit, so this rational number would be+/-1.
That would make alpha torsion, a contradiction.
Thus every D_epsilon and every R_j is a nonzero SIGNED integer.
Every F_epsilon has a nonzero constant coefficient product_j a_j and nonzero leading coefficient product_j epsilon_j b_j at degree T.
Hence EACH polynomial has actual width T, and so does their common union; no degree cancellation is hidden by repeated or overlapping h_j.

On the unit circle, average successively over the independent signs:

    2^(-r)sum_epsilon |F_epsilon(z)|²
       =product_j [(|a_j+b_j z^(h_j)|²
                         +|a_j-b_j z^(h_j)|²)/2]
       =product_j A_j=S.                            (2)

This proves every aggregate lag is zero.
Fourier constant coefficients give the complete actual coefficient energy 2^(-r)sum ||F_epsilon||²=S even when different subsets of exponents coincide.
Independence is over the finite sign labels; no independence of roots or frequencies is assumed.

Full multiplicativity of the original field norm gives

    product_epsilon D_epsilon
       =product_j R_j^(2^(r-1)).                    (3)

Indeed each sign of each factor occurs exactly2^(r-1) times in the product over all labels, and the product of the two factors is G_j.
Monicity of P identifies its resultant with the full norm of G_j(alpha); no leading sign, root factor or degree is omitted.
For r1 the exponent is1, and for larger r its actual even multiplicity is retained rather than removing a possible negative R_j by assertion.

Define the raw integer packet's original normalized income and full surplus by

    I=(1/(dM))log|product_epsilon D_epsilon|,
    sigma=I-(1/2)log S.

Then

    I=sum_j log|R_j|/(2d),
    sigma=sum_j sigma_j,
    sigma_j=log|R_j|/(2d)-(1/2)log A_j.             (4)

In particular the following is an EXACT necessary and sufficient arithmetic positivity test for this complete finite family:

    sigma>0 iff product_j |R_j| > S^d.             (5)

Both sides of(5) are positive integers defined by the ORIGINAL P.
This is a finite exact resultant comparison, not a test of one embedding, a substitute prime list or a claim that positivity actually occurs uniformly.
No computation of it is performed in this inquiry.
It exposes all factors and actual degrees that a later bounded experiment would have to declare.

One also has sigma/T=sum_j(h_j/T)(sigma_j/h_j), so product formation cannot improve surplus per unit physical width beyond the best constituent pair in that same packet.
At least one constituent has positive surplus whenever the product does.
This elementary reduction does not imply that one factor retains a uniform absolute margin if r grows; it is only the stated width-weighted identity.

<a id="biased-sign-product-original-root-deficit"></a>
## 3. Exact original-root deficit, before any small-measure estimate

For each original root write beta_i=r_i z_i with r_i>0 and |z_i|=1.
Because P has real integer coefficients, complex roots occur with their conjugates.
Define the actual damped moment and the scale-invariant amplitude balance

    D_h=(1/d)sum_(i=1)^d exp(-2h|log r_i|) z_i^(2h),
    v_j=a_j² b_j²/A_j² in(0,1/4].                 (6)

The moment is real by conjugate pairing, although Re D_h will be retained in formulas to keep its origin explicit.
Its absolute value is at most1.
It uses ALL ORIGINAL d roots and the ORIGINAL exponent h; a smaller degree of alpha^(2h) is not silently substituted.

Apply L318's accepted finite Poisson/reversal lemma to the actual polynomial G_j=a_j²-b_j²t^(2h_j).
Its energy is a_j^4+b_j^4 and its only nonzero positive-lag autocorrelation is -a_j²b_j² at lag2h_j.
At each original root it gives

    |G_j(beta_i)|²/max(1,r_i)^(4h_j)
       <=a_j^4+b_j^4
           -2a_j²b_j² exp(-2h_j|log r_i|) Re z_i^(2h_j).

Average this inequality over the original roots.
Write

    L_j=1-2v_j(1+Re D_(h_j)).                     (7)

The averaged right side is A_j² L_j.
The averaged left side is STRICTLY positive, because every actual G_j(beta_i) is nonzero.
Therefore L_j>0.
Also Re D_h>=-1 gives L_j<=1.
This supplies the positivity needed before taking its logarithm, even in the limiting-looking case v_j=1/4; no zero logarithm is used as a finite bound.

For u_j=h_j m/d, the exact original norm and Jensen give

    log|R_j|/d
       =2u_j+(1/d)sum_i log[|G_j(beta_i)|/max(1,r_i)^(2h_j)]
       <=2u_j+(1/2)log(A_j² L_j).

After dividing by2 and subtracting(1/2)log A_j,

    sigma_j<=u_j+(1/4)log L_j.

Sum all factors, noting sum u_j=U.
Since log(1-x)<=-x for0<=x<1, equations(6)--(7) prove the ALL-INPUT estimate

    sigma<=U+(1/4)sum_j log[1-2v_j(1+Re D_(h_j))]
          <=U-(1/2)sum_j v_j(1+Re D_(h_j)).       (8)

There is no small-m hypothesis for(8).
It refines the old generic exact-complementarity price sigma<=U by retaining the NEGATIVE autocorrelation of the product of each pair's full original values.
The new factor-specific deficit is not obtained merely by applying that generic price to the original packet and renaming it.

Thus actual positive surplus in this family NECESSARILY obeys the finite spectral test

    sum_j v_j(1+Re D_(h_j))<2U.                   (9)

More generally sigma>=eta>0 implies the same left side is at most2(U-eta).
The exact sufficient-and-necessary arithmetic gate remains(5); passing(9) alone is not sufficient.
The damped moments in(9) are actual algebraic root expressions: after conjugate pairing their sums can be written using beta_i^(2h) for |beta_i|<=1 and beta_i^(-2h) for |beta_i|>1.
No probabilistic phase law or unweighted sample is substituted.
This gives a second, necessary, precisely specified finite test if a future declared exact computation is useful.

<a id="biased-sign-product-small-measure-budget"></a>
## 4. Uniform balance budget at absolute degree-multiple width

For the small-measure corollary use ONLY the already accepted actual-original-root angular estimate retained in L318/L229.
Its constants and function are

    c0=log(2)/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0) log sqrt(c0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0.

On that retained domain epsilon is increasing and tends to0 at0.
It bounds every original angular moment through a chosen integer frequency cutoff H when u=H m/d.
No powered-degree equality is required; the accepted proof already pays the actual degree escape.
This author uses that established statement and does not claim a new audit of its Pri11/Dim19 source proofs.

Assume now

    0<2U=2T m/d<=h0,
    delta(U)=epsilon(2U)+4U<1.                    (10)

Apply the angular bound at H=2T.
The original unit relation gives sum_i|log r_i|=2m.
For every h<=T,

    |D_h|
      <=|(1/d)sum_i z_i^(2h)|
          +(1/d)sum_i [1-exp(-2h|log r_i|)]
      <=epsilon(2U)+4h m/d<=delta(U).            (11)

The second line uses1-exp(-x)<=x and includes all original roots.
Thus(8) yields

    sigma<=U+(1/4)sum_j log[1-2(1-delta(U))v_j]
          <=U-[(1-delta(U))/2]sum_j v_j.          (12)

The new log arguments are positive because v_j<=1/4 and delta(U)>=0; each is at least1/2.
Since delta(U)<1, positivity of the ACTUAL full surplus forces

    sum_j v_j < 2U/[1-delta(U)].                 (13)

This statement covers arbitrarily many factors, arbitrary nonzero INTEGER amplitudes chosen as a function of P, and arbitrary repeated/overlapping positive frequencies with their ACTUAL total width T.
It is a sum budget rather than a separate free allowance for each factor.
It preserves the full norm gate(5) and does not turn the accepted upper cyclic/analytic cost into lower arithmetic income.

In particular, fix C>0 and consider ANY hypothetical sequence of actual inputs with m(P)->0 and any packets of this class at T<=C d.
Then U<=C m tends to0, conditions(10) hold eventually, and every packet with positive full surplus must have sum_j v_j=O_C(m).
No existence of such inputs or packets is asserted.
This corollary says more about THIS construction than the generic bound sigma<=C m: every nontrivial factor must spend part of a vanishing combined amplitude-balance budget.

<a id="biased-sign-product-height-and-failed-escape"></a>
## 5. Integer-height consequences and the failed many-factor repair

For each factor define its primitive amplitude pair by dividing |a_j|,|b_j| by their positive integer gcd, and let

    H_j=max(|a_j|,|b_j|)/gcd(|a_j|,|b_j|)>=1,
    x_j=min(|a_j|,|b_j|)/max(|a_j|,|b_j|) in(0,1].

These quantities are scale-invariant.
Since the smaller primitive amplitude is a positive integer, x_j>=1/H_j.
Moreover

    v_j=x_j²/(1+x_j²)²>=x_j²/4>=1/(4H_j²).

Consequently under(10), EVERY positive-surplus packet in this family satisfies

    sum_j x_j² < 8U/[1-delta(U)],
    sum_j H_j^(-2) < 8U/[1-delta(U)].             (14)

If all primitive amplitude heights are at most one common H, then

    H² > r[1-delta(U)]/(8U).                     (15)

Thus a bounded primitive-amplitude family cannot give even POSITIVE surplus along m->0 at T<=C d.
If the number of factors grows, its required largest permitted amplitude scale grows at least as sqrt(r/U) in the precise sense(15).
This is not a lower bound on every coefficient of every output polynomial, and a single very large amplitude does not by itself make the construction successful.
The more informative necessary condition is the sum of inverse squares in(14), not a claim that only the maximum matters.

If instead each factor has a uniformly nondegenerate ratio x_j>=xi>0, monotonicity of x²/(1+x²)² on0<x<=1 gives

    sigma<=U-[(1-delta(U))/2]
                     r xi²/(1+xi²)².             (16)

Hence arbitrary tensor multiplication of such factors has strictly negative full surplus for all sufficiently small m at bounded T/d, even if r grows; increasing r makes this upper deficit larger.
This is the failed repair mechanism: many fully paid sign factors cannot compensate for one another merely by duplicating the old complementary identity.
To evade this particular obstruction, their amplitudes must become increasingly unbalanced with the total squared ratios in(14) tending to0.
The resulting coefficients, full norm products and physical width still have to satisfy the exact arithmetic gate(5).

For the old balanced pair a_j=+/-b_j, v_j=1/4.
The present inequality is NOT advertised as a sharper estimate than L318/L168's old single-pair limit -log2/2.
It is deliberately broader: input-adapted biases, all factors at once and explicit height/total-balance costs.
No new universal binomial existence result, fixed-positive-measure calibration or improvement of a known Mahler lower bound is claimed.

<a id="biased-sign-product-complete-costs"></a>
## 6. Actual order, true q, FINAL M, signed copies and rational rescalings

For the raw integer packet in Sections1--5, every value lies in the actual O0, the ACTUAL coefficient denominator is q=1, the ACTUAL FINAL indexed denominator is M=2^r, and every copy multiplicity is1.
The complete signed copied resultant is exactly(3).
The energy is S, every content remains in every polynomial/resultant, and the full income and surplus are(4).
No least denominator attached to coalesced distinct values replaces the indexed M used in this product.
If a later operation merges identical labels, its new weights and actual denominator must be recalculated; none of the formula's multiplicities may be retained by assumption.

A common integer amplitude factor c_j in(a_j,b_j) multiplies every full output F_epsilon by c=product c_j.
Its complete norm is multiplied by c^d per label and its energy by c².
Therefore its income changes by log c and the one-half log energy by the same amount.
It cannot change the surplus or the balance v_j.
This explains why(14)--(15) use primitive amplitude ratios without silently making the actual output polynomials primitive or dropping their content factors.

The conclusions also survive ONE common positive rational rescaling f_epsilon=c F_epsilon, PROVIDED that EVERY actual f_epsilon(alpha) is still a NONZERO element of the actual O0.
This is an explicit full-coordinate membership requirement; divisibility of norms alone does not prove it.
Define q_star as the ACTUAL least coefficient denominator of this rescaled packet and H_epsilon=q_star f_epsilon in Z[t].
Keep its complete signed integer norms D'_epsilon=Norm(f_epsilon(alpha)).
Then

    E=c² S,
    Lambda=(1/(dM))sum_epsilon log|D'_epsilon|
           =log c+I,
    Lambda-(1/2)logE=sigma,
    Res(P,H_epsilon)=q_star^d D'_epsilon,
    product_epsilon Res(P,H_epsilon)
        =q_star^(dM) product_epsilon D'_epsilon.  (17)

Here the first expression for Lambda means the usual(1/d) weighted sum with weights1/M; equivalently it is(1/(dM)) times the unweighted sum of the M logarithms.
q_star is not identified with the denominator of c before cancellation, with M or with any pre-splitting denominator.
Every actual numerator content and signed norm remains in(17).
Negative common scalars can be absorbed into signs; their actual signed norm powers must likewise be retained.

More generally a product packet with nonzero RATIONAL amplitudes can be cleared factor by factor to the displayed integer-amplitude family times one common rational scalar.
If its final values meet that actual O0 condition, the same surplus and scale-invariant balance bounds therefore apply.
This extension is a proved scaling observation, not an assertion that arbitrary rational amplitudes automatically give integral residues.
It includes possible legitimate below-one normalizations without waiving any integer-value hypothesis or creating norm income by division.

A single common monomial shift preserves widths, energy, coefficient denominator, final indexed weights and absolute norms because alpha is an actual unit.
Its full signed Norm(alpha) power remains in every copied norm if values are recorded before shifting.
The construction itself already has common interval[0,T] with both endpoints attained.
Shifting individual atoms separately is not part of the class analyzed here and does not preserve the asserted physical-width accounting by decree.

<a id="biased-sign-product-boundaries-and-freeze"></a>
## 7. What is proved, what failed and the remaining arithmetic test

The result is the exact full family identity(2)--(5), the all-input actual-root deficit(8)--(9), its small-measure TOTAL balance budget(12)--(13), and the consequent ratio/height constraints(14)--(16), with all costs in(17).
It is a necessary quantitative obstruction for a defined construction class at T<=C d, together with an exact necessary-and-sufficient finite resultant positivity test.
It does not supply that missing lower arithmetic income uniformly.
No bound here implies positivity from spectral admissibility, and no new same-exponent A(n)>=eta d witness is asserted.

The initial idea of repairing the old balanced binomial pair by multiplying many sign factors fails precisely when their total amplitude balance does not shrink as in(13).
Simply increasing factor count, repeating frequencies, changing common scalar content or legally dividing into integral values does not bypass the theorem.
Arbitrarily unbalanced primitive amplitudes are a genuine remaining loophole to THIS obstruction, not an established successful construction.
General nonfactorized complementary packets, correlated nonproduct sign weights and arbitrary rational orthogonal mixing of coordinates are outside this class.
Root's distinct universally integral short-row paraunitary problem is neither repeated nor used as a premise.

The locally derived sign average, norm-copy factorization, finite Jensen estimate, ratio monotonicity and rescaling arithmetic require no new external theorem.
Classical Poisson attribution and the powered angular/source scopes remain exactly the accepted upstream L318/L229 ones.
L168's upper cyclic cost was read and credited solely to avoid relabeling the old balanced failure as arithmetic lower income.
No new literature-wide novelty or source-proof completion is claimed.
No native mathematical program, scan, optimizer or J was needed or run; any future exact resultant test would first need its own declared finite J scope.

Author self-check covers actual nontorsion-unit nonvanishing, every original conjugate and signed norm, degree endpoints and repeated frequencies, all2^r positive indexed labels, actual q1/M2^r, coefficient energy despite exponent collisions and full copied signs; G_j's negative autocorrelation and all Poisson/reversal normalizers, Jensen's factor1/2 and the resulting factor1/4 in the surplus, positivity of each L_j, real damped moments and no smaller powered-degree substitution; original unit radial sum2m, cutoff2T and delta=epsilon(2U)+4U, both necessary inequality directions, ratio/height scaling and arbitrary growing r; all contents, rational amplitudes, actual integral rescaling and least q_star versus M, common monomial signs and the exact limited class.
This is AUTHOR checking, not independent review.
A separately organized whole noncontributor review is required before fixed extraction or adoption.

### Exact hand check of signs, repeated frequencies and the finite gate

For a transparent check only, take the actual irreducible unit polynomial P=t²-3t+1 (discriminant5), alpha=(3+sqrt5)/2, d2.
Its positive total measure is log alpha; it is NOT a near-one family and does not satisfy the tiny regime(10).
With r1,h1,a=b1, the two original norms are Norm(1+alpha)=5 and Norm(1-alpha)=-1, since the roots have sum3 and product1.
Thus R=-5, S2, M2, q1 and sigma=(1/4)log(5/4)>0, exactly as(3)--(5) require.
The finite gate is5>2².
No new binomial existence or quantitative gap is inferred.

With TWO identical such factors, repeated h values give four INDEXED polynomials and norms25,-5,-5,1.
The two mixed-sign polynomials coincide, but both labels remain: their complete product is625, matching R1²R2²; S4, M4 and sigma=(1/2)log(5/4).
This checks the copied multiplicity and energy formulas with an actual exponent collision.
It supplies no advantage in surplus per width, consistently with(4).
As an unequal-amplitude check on the same original input, a2,b1,h1 gives norms11,-1 and S5, so the gate11>25 fails.
Bias is not in itself a sufficient source of positive income.
All these are exact symbolic multiplications performed by hand, not a native computation or an input scan.

### Exact accepted interfaces and final author freeze

The small-measure statement uses [L229's actual all-frequency angular bound](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence), equations3--4 at its adopted original-unit scope, and [L318's finite Poisson/reversal identity](Yin_C_G0600_v1.md#polynomial-poisson-majorant).
Both actual passages were read; their inherited source-theorem acceptances are not enlarged.
Equation8 itself requires only the latter finite polynomial inequality and the displayed local derivation, not the angular-source corollary.
Positive splitting of labels, like merging, must use its recalculated ACTUAL final indexed M and copy exponents if carried out later; the raw construction's exact M2^r is not a universal postprocessing denominator bound.

<a id="biased-sign-product-entire-author-freeze"></a>
Freeze the ENTIRE allocation/candidate/reuse history and Sections1--7/equations1--17, the exact hand checks, all original norms/weights/width/denominator costs, source limits and failed/surviving mechanisms at 2026-10-12T12:09.
The author supplied and checked the new formulas, so these are not independently reviewed results.
Scoped material validation passed for this D and the three directly inspected ledgers with checked4; that is structural validation only.
Root owns independent-review assignment and any later adoption.
No target outside this D, shared navigation, source register or native program was changed by this author inquiry.
Development now stops on this frozen body pending a separately organized whole noncontributor review.
