---
author: Yin
---
# Full-surplus bounds for arbitrary correlated flat-bit laws with one common marginal

Date: 2026-10-12T11:35.
Human author Yin.
Root authored the entire original D16 proof and its dated FINAL-weight correction.
g0001_review_recovery independently reviewed the original19:18 whole scope in R273 and actual19:31 corrected whole scope in R274, and NOW authors this new fixed statement/wrapper.
The extractor is a contributor to this new material and cannot independently review its actual extraction.
The complete corrected body, original freeze, negative denominator finding and dated correction are preserved below.
Initial status is proof draft / under review, pending another noncontributor's actual statement/preservation/interface review.

## Statement

Let P(t)=sum_(i=0)^d c_i t^i be the ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, ORIGINAL degree d>=2, with c_i in{0,+1,-1}, c_0 in{+1,-1}, c_d=1.
Write I={i:c_i!=0}, n=|I|>=3, sigma_i=c_i on I and m=m(P)=sum_beta log max(1,|beta|), summing over ALL original conjugates.
All values and norms belong to O0=Z[alpha] and the ORIGINAL field Q(alpha).
Reciprocity is not assumed.

Choose ANY rational0<p<1, shared by the entire law, and ANY rational probability vector(w_B) over ALL subsets B of I such that

    sum_B w_B=1,
    sum_(B containing i)w_B=p for EVERY i in I.

Zero masses are omitted.
All subset sizes and arbitrary correlations are allowed.
Put

    f_B=pP-sum_(i in B)sigma_i t^i.

Replace EACH positive empty or full atom by f_B+1 and f_B-1 at half its original mass, retaining all proper nonempty atoms.
Arbitrary finite positive rational splitting of identical final labels is allowed, with its ACTUAL indexed final weights retained.

**A. Actual nonzero packet and exact lag criterion.**
The only zero values f_B(alpha) before repair are B empty and B=I.
Thus all final values are nonzero actual O0 integers, with the two repaired values +/-1.
The final weights are positive rational numbers summing1, and every global coefficient mean is zero.
Define

    b_ij=Pr(i,j in B),
    a_h=sum_(i<j in I,j-i=h)sigma_i sigma_j.

The final packet is complementary, with every positive coefficient lag zero, IF AND ONLY IF

    sum_(i<j in I,j-i=h)sigma_i sigma_j b_ij=p^2 a_h
                                  for EVERY h=1,...,d.

These conditions are imposed on the ACTUAL probability law, not on hypothetical moments whose realizability is assumed.
Pair repair adds only(w_empty+w_I)e0e0^T to the raw second-moment matrix.
Negative lags follow by symmetry and higher lags vanish.

**B. Complete energy and exact success.**
Put

    X_ex=sum_(B:|B|>=2)(|B|-1)w_B, tau=w_empty+w_I,
    E=sum_b omega_b||f_b||_2^2,

where b now indexes EVERY actual final label, including repair signs and any declared splitting.
Then

    w_empty=1-np+X_ex,
    0<E=np(1-p)+tau=1-np^2+X_ex+w_I.

In particular, for a realized complementary law, E<1 IF AND ONLY IF X_ex+w_I<np^2.
Full-subset probability contributes(n-1)w_I inside X_ex AND an additional w_I through repair.
No zero mass is dropped, and no conditional renormalization is used.

**C. Actual arithmetic, splitting and complement symmetry.**
Write the selected original p=a/q in lowest terms,0<a<q.
EVERY final atom has ACTUAL least coefficient denominatorq, primitive integer numerator F_b=q f_b, nonzero constant and degree-d coefficients, and physical width EXACTLY d.
Let M be the ACTUAL least common denominator of the complete final indexed weight list, and let k_b=M omega_b in Z_(>0), so sum_b k_b=M.
If r clears the original aggregate w_B, the canonical repaired representation BEFORE additional label splitting has denominator M_unsplit dividing2r.
After arbitrary additional splitting, recompute M from the actual split weights; no bound from aggregate r alone is asserted.

For every final label retain the complete SIGNED original norm

    D_b=Norm_(Q(alpha)/Q)(f_b(alpha)) in Z minus{0}.

Singleton norms have sign(-sigma_i)^d Norm(alpha)^i and absolute value1; the two repaired values have norms1 and(-1)^d.
Proper larger subsets may have nonunit norms.
With ALL original roots and actual copies,

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(k_b)=q^(dM)product_b D_b^(k_b),
    Lambda=(1/d)sum_b omega_b log|D_b|>=0,
    S_int=sum_b omega_b||F_b||_2^2=q^2E,
    I_income=(1/(dM))log|product_b Res(P,F_b)^(k_b)|
            =logq+Lambda.

After the lag criterion in A holds, the same-packet C10 inequality gives

    I_income-(1/2)logS_int=Lambda-(1/2)logE<=m.

All signs, original norm degrees, contents and copies remain; content1 is proved for this family.
No upper bound on actual q or arbitrary-split M is asserted.

Complementation B to I minus B together with p to1-p maps the complete repaired packet to its global negative with labels and repair signs permuted.
It preserves E, lag cancellation, actual q, actual indexed M and Lambda; each signed norm changes by(-1)^d and the copied signed product by(-1)^(dM).
Therefore the energy/full-surplus bounds may reduce to0<p<=1/2.
The original p>1/2 laws are included through this exact symmetry.

**D. All original norm income is charged.**
Every proper nonempty subset of size s>=2 satisfies

    0<=log|Norm_(Q(alpha)/Q)(sum_(i in B)sigma_i alpha^i)|/d
        <=log s+m<=(s-1)(log2+m).

Consequently

    0<=Lambda<=(log2+m)[X_ex-(n-1)w_I]
                  <=(log2+m)X_ex.

The full subset is excluded from THIS norm sum because its actual repaired values are units; its full energy charge in B remains.
All larger proper subsets and all original conjugates are included.
Under success E<1,

    Lambda<(log2+m)np^2,
    0<1-E=np^2-X_ex-w_I<=np^2.

These formulas also apply after any declared identical-label splitting.

**E. Uniform full-surplus barrier for growing support.**
Suppose n>=5 and E<1.
After the actual complement reduction to p<=1/2, define

    r_n=(1-sqrt(1-4/n))/2,
    z_n=n r_n^2=r_n/(1-r_n) in(0,1).

Raw variance implies np(1-p)<1, hence p<r_n and np^2<z_n.
Every realized complementary law in this family therefore satisfies

    0<Lambda-(1/2)logE
        <=z_n(log2+m)-(1/2)log(1-z_n)

and also the coarser bound

    Lambda-(1/2)logE<=4(log2+m)/n+2/(n-4).

The first upper bound tends to0 as n tends to infinity with m bounded, since z_n~1/n.
This is uniform over the ACTUAL rational common p, every correlation pattern, all subset sizes and all rational final indexed weights.
It controls the FULL arithmetic surplus, including every nonunit norm, not just energy.
The weak inequality does not claim attainment at its endpoint.

The packet/energy/arithmetic/norm identities remain true at n3 and n4.
Those values are excluded from this square-root/logarithmic growing-support estimate: n3 has no real stated root and n4 would give z4=1.
This theorem does not assume that a sequence of actual inputs with growing support and bounded measure exists.

**F. Special marginal and exact limits.**
If p=1/q with integerq>=2, every successful law has q>=n-1, for ALL n>=3, without any subset-size cutoff.
It follows that

    Lambda-(1/2)logE
        <=[n/(n-1)^2](log2+m)
           -(1/2)log[1-n/(n-1)^2].

At fixed n and bounded m, successful laws with q tending to infinity have full surplus O(q^-2), using the finer bound np^2=n/q^2 before rounding.
This does not assert the exact optimum of the narrower pair-supported family.

For consistency only, the old explicit original quartic P=t^4-t^3-t^2-t+1 seven-label law at p1/4 has n5, X_ex1/4 and zero empty/full mass, recovering E15/16 and the known Lambda=log3/64.
No new finite optimum or native experiment is supplied by this control.

The bounds concern centered binary representatives with ONE shared fractional coefficient pP, common bit marginals and the stated paired-unit repair in the actual original first window.
They are not an upper bound for full capacity and do not cover unequal marginals, separate p_B values at individual atoms, larger alphabets, different representative families, wider windows or an additional mixture theorem.
No capacity lower-bound improvement, positive uniform Mahler gap or unrestricted G0001 completion follows.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:35 |
| status | open |
| reason | Register the complete corrected all-subset/common-marginal packet identities, actual arithmetic, complete norm-income bound and growing-support full-surplus barrier. R274 covers the corrected original proof only, and its reviewer now authors this wrapper. Another noncontributor must inspect the actual extraction before adoption. The original R273 post-splitting denominator defect and dated correction are retained. No full-capacity bound or unrestricted Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, actual original flat unit/order, all rational correlated laws, complete repairs/energy/arithmetic and precise uniform/special-marginal bounds and exclusions. |
| argument | [Complete retained proof](#argument) | ENTIRE actual19:31 corrected D16, original allocation, Sections1--7/equations1--13, original19:18 freeze and dated split-denominator correction/counterexample. |
| dependency | [C10 complete original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Same actual complementary rational packet, all full signed original-degree resultants, actual FINAL weights/copies and physical widthd. |
| support | [C25 original flat-residue context](Yin_C_G0025_v1.md#statement) | Prior actual first-window/order and empty/full zero patterns only; arbitrary-p classification and all new formulas are proved in the retained body. |
| support | [C54 exact paired-repair antecedent](Yin_C_G0054_v1.md#statement) | Existing +/-1 repair with retained zero mass only; independent-rounding hypotheses are not imported. |
| support | [C58 old explicit quartic](Yin_C_G0058_v1.md#statement) | ONLY PartF seven-label original quartic control and split-denominator counterexample data; its new restricted optimum theorem is not a premise. |
| support | [Original whole negative finding](../audits/reviews/Yin_R_G0273_v1.md#all-subset-original-split-denominator-finding) | Complete original19:18 checking and the fixed original post-splitting denominator defect; not overwritten as a pass. |
| support | [Corrected original whole finding](../audits/reviews/Yin_R_G0274_v1.md#all-subset-corrected-whole-finding) | ENTIRE actual19:31 corrected original body only. Its reviewer is now this new wrapper's author and cannot provide its independent extraction verdict. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:45 |
| status | proved |
| reason | Adopt the separately performed corrected whole R274 and actual extraction R277 findings, retaining R273 original negative scope and the complete dated FINAL-weight correction. The all-subset common-marginal surplus theorem has its stated restricted representative domain; no full-capacity or unrestricted gap conclusion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, actual original flat unit/order, all rational correlated laws, complete repairs/energy/arithmetic and precise uniform/special-marginal bounds and exclusions. |
| argument | [Complete retained proof](#argument) | ENTIRE actual19:31 corrected D16, original allocation, Sections1--7/equations1--13, original19:18 freeze and dated split-denominator correction/counterexample. |
| dependency | [C10 complete original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Same actual complementary rational packet, all full signed original-degree resultants, actual FINAL weights/copies and physical widthd. |
| support | [C25 original flat-residue context](Yin_C_G0025_v1.md#statement) | Prior actual first-window/order and empty/full zero patterns only; arbitrary-p classification and all new formulas are proved in the retained body. |
| support | [C54 exact paired-repair antecedent](Yin_C_G0054_v1.md#statement) | Existing +/-1 repair with retained zero mass only; independent-rounding hypotheses are not imported. |
| support | [C58 old explicit quartic](Yin_C_G0058_v1.md#statement) | ONLY PartF seven-label original quartic control and split-denominator counterexample data; its new restricted optimum theorem is not a premise. |
| support | [Original whole negative finding](../audits/reviews/Yin_R_G0273_v1.md#all-subset-original-split-denominator-finding) | Complete original19:18 checking and the fixed original post-splitting denominator defect; not overwritten as a pass. |
| support | [Corrected original whole finding](../audits/reviews/Yin_R_G0274_v1.md#all-subset-corrected-whole-finding) | ENTIRE actual19:31 corrected original body only. Its reviewer is now this new wrapper's author and cannot provide its independent extraction verdict. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0277_v1.md#c61-common-marginal-actual-extraction-finding) | Entire actual statement, completely retained argument/history and current direct interfaces, separately inspected after allocation by a noncontributor. Finding relationship: self-reviewed. |

## Registration and complete preservation

Date: 2026-10-12T11:35.
The actual corrected D16 body below is retained in full, with only its repeated author front matter removed, its first title demoted once and terminal whitespace normalized.
Existing valid relative links are preserved.
No proof paragraph, original condition, coefficient/weight cost, larger-subset/full-subset term, sign, source/reuse history, original freeze or dated negative-finding correction is removed.

The initial Claim has not been adopted.
The extractor's completed R273/R274 findings keep their original scopes, while authoring this new wrapper prevents an independent self-review of its actual extraction.
Root will arrange another noncontributor's actual statement/body/interface review.
No new native run, source intake, mathematical proof correction, decision on another material or draft retirement accompanies registration.

## Argument

## Full-surplus barrier for arbitrary correlated flat-bit laws with a common marginal

Date: 2026-10-12T11:11.
Human author Yin.
Root AUTHOR continuation under the unchanged G0001 weekly instruction.
Root supplies this new all-subset/common-marginal counting candidate; no sibling has contributed its formulas.
No native mathematical program, solver or new source is planned.
All substantive argument belongs here.

## Bounded reuse and exact changed question

Root has read the entire original pair-supported proof now retained in [C58](Yin_C_G0058_v1.md#argument), its separate whole finding R267 and the relevant [C25](Yin_C_G0025_v1.md#statement), [C29](Yin_C_G0029_v1.md#statement), [C54](Yin_C_G0054_v1.md#statement) interfaces.
C58's actual extraction is currently under separate root review; this inquiry needs none of its new theorem as a premise, only its fully specified example for comparison.
C25 already identifies empty/full flat subsets as the zero representatives; C54 keeps all repaired zero mass.
A bounded current G-Claim/ledger screen found no full arbitrary-subset common-marginal surplus theorem.
This is a bounded reuse observation, not a novelty claim.

Allow EVERY subset of the n nonzero positions of an actual flat monic irreducible nontorsion integer-unit P, with ANY rational joint distribution and ANY common rational marginal p in(0,1).
Use actual representatives f_B=pP-sum_(i in B)p_i t^i and pair-repair BOTH empty and full zero-residue atoms by f_B+/-1 at half their original mass.
Require all actual lags to cancel, retaining exact coefficient denominator, FINAL weights, contents, original norms and physical width d.
Larger subsets and arbitrary correlations are explicitly allowed.

## Candidate identity and uniform limitation

By complementing all bits, replacing p with1-p and changing the sign of all representatives, energy and absolute norm income are unchanged; reduce to p<=1/2.
Let X=sum_(|B|>=2)(|B|-1)w_B, and w_I be the full-subset mass.
Marginals give E|B|=np and w_empty=1-np+X.
The repaired energy should be EXACTLY E=1-np^2+X+w_I.
Thus successful E<1 forces X+w_I<np^2.
Only proper subsets of size at least2 have potentially nonunit norm.
The original-root bound log|Norm(sum subset)|/d<=log|B|+m(P), followed by log s<=(s-1)log2, bounds ALL norm income by (log2+m(P))X.
Meanwhile raw variance np(1-p)<1 forces p<r_n=(1-sqrt(1-4/n))/2 for n>=5.
Consequently n p^2<z_n=n r_n^2~1/n, so the FULL surplus is bounded by z_n(log2+m(P))-(1/2)log(1-z_n), tending to0 at bounded measure and unbounded support n.
If correct, simply allowing larger subsets while retaining common-marginal binary representatives cannot repair the uniform-gain failure.

Every identity, complement and endpoint case, exact rational q/FINAL M, original nonzero norm, signed products and all-lag requirement must be proved below.
No full capacity impossibility, variable-per-atom coefficient residue class, unequal marginals, larger integer alphabet or mixture theorem is claimed.
This is developing author work, unreviewed and unadopted.


<a id="all-subset-common-marginal-domain"></a>
## 1. Complete declared family and exact finite realization

Let P(t)=sum_(i=0)^d c_i t^i be the ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, d>=2, c_i in{0,+1,-1}, c_0=+/-1, c_d=1.
Let I={i:c_i!=0}, n=|I|>=3 and sigma_i=c_i on I.
The n>=3 assertion follows because a monic unit binomial has only roots of unity.
All residues are in O0=Z[alpha], all norms are Norm_(Q(alpha)/Q) of original degree d, and m=m(P)=sum_beta log max(1,|beta|).
Reciprocity is not assumed.

Choose ANY common rational marginal 0<p<1 and ANY probability vector w_B>=0 on ALL subsets B of I, with rational entries and

    sum_B w_B=1, sum_(B containing i)w_B=p for EVERY i in I.
                                                            (1)

Zero masses are omitted; arbitrary finite positive splitting of identical labels is allowed and its FINAL weights are charged.
The common p belongs to the entire law, not an individually chosen p_B.
No independence, size cutoff, exchangeability, pairwise sign constraint or particular joint-law generator is imposed.
Set

    f_B(t)=pP(t)-sum_(i in B)sigma_i t^i.             (2)

For each positive empty or full B, replace f_B by f_B+1 and f_B-1 with half that atom's actual mass each.
All other atoms remain unchanged.
This exact paired repair retains normalization and mean; no zero-value mass is discarded or conditionally renormalized.

The actual value of (2) is minus its signed subset sum, an O0 integer.
It vanishes EXACTLY for B empty or B=I: if a degree<=d signed-subset polynomial vanishes at alpha, it is a real/rational multiple of the monic minimal P; its coefficient ratios at the original support are all0 or1, forcing either the empty or full subset.
In particular no proper nonempty atom is invalid and each repaired value is+/-1.
This supplies an ACTUAL finite rational packet before any lag condition, with no moment-hull or PSD realizability assumption.

For i!=j in I put b_ij=Pr(i,j in B), and define original autocorrelations a_h=sum_(j-i=h)sigma_i sigma_j.
Before repair, coefficient means are zero and second moments are

    X_ii=p(1-p),
    X_ij=sigma_i sigma_j(b_ij-p^2).

Zero-coefficient positions remain zero.
Repair adds ONLY (w_empty+w_I)e0e0^T, since each paired cross term cancels even though the original zero-valued polynomial need not have zero coefficient vector.
Therefore the final packet is complementary if and only if

    sum_(i<j in I,j-i=h)sigma_i sigma_j b_ij=p^2 a_h
                       for EVERY h=1,...,d.        (3)

Negative lags follow by symmetry; higher ones vanish by support.
The subsequent theorem applies to EVERY actual law satisfying (1)--(3), not to arbitrary proposed second moments whose distribution has not been realized.

<a id="all-subset-energy-counting-identity"></a>
## 2. Cardinality excess controls the complete repaired energy

Write s(B)=|B| and

    X_ex=sum_(B:s(B)>=2)(s(B)-1)w_B>=0,
    w_I=Pr(B=I), tau=w_empty+w_I.

The symbol X_ex is a scalar cardinality excess, not the coefficient matrix X.
The common marginals give E s(B)=np.
On the other hand E s(B)=Pr(B nonempty)+X_ex, so

    w_empty=1-np+X_ex,
    E=n p(1-p)+tau
       =1-n p^2+X_ex+w_I.                          (4)

Here E is the ACTUAL final weighted coefficient energy, constant circle covariance when (3) holds.
It is positive because every final coefficient vector is nonzero.
Formula(4) includes BOTH repaired zero types; full-subset mass contributes (n-1)w_I inside X_ex and one MORE w_I through repair.
A proof that omitted the full subset from either count would be incorrect.

Thus exact success is the inequality

    E<1 iff X_ex+w_I<n p^2.                        (5)

This is a criterion for an already realized complementary law; it does not assert that a law with arbitrary chosen X_ex exists or solves (3).
In particular allowing large subsets costs s-1 units of excess per occurrence.
Larger subsets may solve different lag equations, but their probability is charged by the same identity.

<a id="all-subset-complement-and-denominators"></a>
## 3. Complement symmetry and exact original q, contents, width and FINAL copies

Complement every subset and put p'=1-p.
Its marginals are p', its rational probabilities are w'_C=w_(I\C), and

    p'P-sum_(i in I\B)sigma_i t^i=-f_B.

Empty and full repair pairs map to the negatives of the corresponding old pairs, with the two signs permuted.
Thus the complete repaired packets agree up to global negation and label permutation.
Energy, complementarity, coefficient-denominator leastness, indexed FINAL weight denominator and absolute norm income are unchanged.
Original signed norms change by(-1)^d for each label and the copied signed product by(-1)^(dM); these signs are retained if this symmetry is actually performed.
It is therefore legitimate for the energy/surplus bounds to reduce to

    0<p<=1/2.                                     (6)

For exact arithmetic write the ORIGINAL selected p=a/q in lowest terms, 1<=a<=q-1, gcd(a,q)=1.
Each nonempty proper atom has numerator

    F_B=aP-q sum_(i in B)sigma_i t^i.

Because both a selected and an unselected support position exist, its nonzero coefficient magnitudes include a and q-a.
Their gcd is1, proving content1.
Every such coefficient is coprime to q, proving ACTUAL coefficient denominator q.
Empty repair numerators aP+/-q are primitive because nonconstant support coefficients have magnitude a while the constant term is a c0+/-q, coprime with a.
Full repairs have numerators (a-q)P+/-q and the same gcd argument.
Their leading coefficients a or a-q are coprime to q.
Hence EVERY final atom has actual coefficient denominator q and primitive numerator.

All constant and degree-d coefficients are nonzero: ordinary coefficients are signed a or a-q, and repaired constant coefficients have absolute base a or q-a strictly less than q.
Therefore EVERY final atom and the complete union have actual physical width d.
The complement transformation changes a to q-a in lowest terms and preserves q; it does not replace the actual degree or order.

Let omega_b be the actual FINAL positive rational weights after both repairs and any declared splitting, M their least common denominator, k_b=M omega_b positive integers summing M.
For the canonical repaired representation BEFORE any additional positive splitting, if r clears the original aggregate w_B, its least denominator M_unsplit divides2r; this is only an upper clearing bound, not equality.
After arbitrary additional splitting, recompute the ACTUAL FINAL M from those split weights; it need not divide2r and no bound in terms of r alone is asserted.
Let D_b be the full SIGNED original norm of each final value.
For singleton subsets the absolute norm is1, with actual sign (-sigma_i)^d Norm(alpha)^i.
For repaired labels the signs are1 and(-1)^d.
Proper larger subsets have nonzero signed integer norms with no unit restriction.
Then exactly

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(k_b)=q^(dM)product_b D_b^(k_b),
    Lambda=(1/d)sum_b omega_b log|D_b|>=0,
    S_int=sum_b omega_b||F_b||^2=q^2E,
    I_income=logq+Lambda,
    I_income-(1/2)logS_int=Lambda-(1/2)logE<=m.       (7)

The last step is the accepted C10 direct generic monic inequality after (3), with actual T=d and the SAME final weights.
Every signed factor, actual coefficient denominator, FINAL copy and original conjugate remains.
Contents are proved1 in this declared family; they are not removed by convention.
No uniform upper bound on q or M is asserted.

<a id="all-subset-complete-norm-income"></a>
## 4. Complete original norm income is also controlled by excess

For a nonempty proper subset of cardinality s>=2 and every original conjugate beta,

    |sum_(i in B)sigma_i beta^i|
         <=s max(1,|beta|)^d.

Multiplication over ALL d original conjugates gives

    0<=log|Norm(sum_(i in B)sigma_i alpha^i)|/d
          <=log s+m.

The lower bound uses actual nonzero integrality, not a norm surrogate.
For every integer s>=2 one has s<=2^(s-1), by induction from2 and s+1<=2s.
Hence log s<=(s-1)log2; also m<=(s-1)m because m>=0.
Singletons and repairs contribute zero absolute logarithmic income.
Therefore

    0<=Lambda
       <=(log2+m) sum_(2<=s(B)<=n-1)(s(B)-1)w_B
       =(log2+m)[X_ex-(n-1)w_I]
       <=(log2+m)X_ex.                             (8)

This includes EVERY nonunit residue in the law and all original roots.
The full-subset term is subtracted because it was repaired to units, not assigned a forbidden norm zero.
Any label splitting preserves these weighted quantities.
Under success (5),

    Lambda<(log2+m)n p^2,
    0<1-E=n p^2-X_ex-w_I<=n p^2.                  (9)

No assumption on the signs or individual sizes of nonunit norms is made beyond their complete integer product bound.
Thus adding their income does not evade the combinatorial energy budget.

<a id="all-subset-common-marginal-uniform-barrier"></a>
## 5. A quantitative all-law barrier when support grows

Assume n>=5 and a successful member E<1, with (6).
Since E=n p(1-p)+tau and tau>=0, one has n p(1-p)<1.
The function p(1-p) is strictly increasing on(0,1/2), so

    p<r_n=(1-sqrt(1-4/n))/2,
    n p^2<z_n=n r_n^2=r_n/(1-r_n)<1.               (10)

The endpoint p=1/2 is impossible here because its raw energy is n/4>1.
The identity for z_n uses n r_n(1-r_n)=1.
It is positive and less than1 since r_n<1/2.
Combining (8)--(10) yields the COMPLETE full-surplus estimate, valid for every realized law satisfying (1)--(3) and E<1:

    0<Lambda-(1/2)logE
       <=(log2+m)z_n-(1/2)log(1-z_n).              (11)

The stated weak inequality follows from strictly stronger intermediate bounds and avoids claiming any endpoint optimizer.
In particular z_n tends to0: rationalizing gives r_n=2/[n(1+sqrt(1-4/n))], so n r_n^2~1/n.
Along ANY sequence of such flat inputs with n->infinity and bounded m(P), the FULL surplus of EVERY successful common-marginal bit law tends to0, uniformly over its actual p, all correlations, all subset sizes and all rational final weights.
The same conclusion holds for any hypothetical near-one sequence whose support grows, without asserting that such a sequence exists.

A simple elementary coarser bound is available for n>=5.
From p<=1/2 and n p(1-p)<1 obtain p<2/n, hence n p^2<4/n.
Equations(8)--(9) and-log(1-z)<=z/(1-z) give

    Lambda-(1/2)logE
       <=4(log2+m)/n+2/(n-4).                     (12)

This bound is looser but has no square root.
Both (11) and(12) control FULL arithmetic surplus, not energy alone.
They do not claim the full C16 capacity has this bound, since other packets may use different fractional multiples of P at different atoms, unequal marginals, larger integer alphabets or different representatives.
Nor do they rule out a successful bounded-support subclass.

The energy identity(4), all-lag criterion(3), costs(7) and norm bound(8) remain valid for n3,4.
No formula involving sqrt(1-4/n) is asserted for n3, and n4's endpoint would give z4=1, unsuitable for a finite logarithmic bound.
Those cases are explicitly outside the growing-support theorem, rather than handled by an invalid denominator.

<a id="all-subset-restricted-comparisons"></a>
## 6. Relation to the pair family and exact controls

For the special marginal p=1/q, where q is integer and q>=2, the raw-energy condition alone forces every successful law to have q>=n-1, for ALL n>=3.
Indeed n(q-1)<q^2.
For2<=q<=n-2 and n>=4, the concave polynomial n(q-1)-q^2 is nonnegative: its endpoint values are n-4>=0 at q2 and n-4>=0 at q=n-2.
The interval is empty at n3.
Thus no such q is successful.
This argument imposes NO subset-size restriction.

Then (9) gives0<1-E<=n/(n-1)^2.
For all n>=3 this upper bound is below1, so (8) yields the further exact-family bound

    Lambda-(1/2)logE
       <=[n/(n-1)^2](log2+m)
          -(1/2)log[1-n/(n-1)^2].                 (13)

At fixed n and bounded m, every successful q tending to infinity has full surplus O(q^-2), using the unrounded n/q^2.
This generalizes the pair-family vanishing mechanism to arbitrary subsets at that same marginal, but does not claim its exact pair optimum, which requires the additional lag/edge structure in C58.

As a finite algebraic consistency control only, use C58's already explicit actual quartic seven-label law at p1/4,n5.
It has pair mass X_ex=4/16=1/4 and no full or empty mass.
Formula(4) gives1-5/16+4/16=15/16, exactly its known energy.
Its known full norm income log3/64 satisfies(8); this inquiry does not recalculate a new optimum or run a native test.
More generally if a bit law has only empty/singletons/pairs, then X_ex is its total pair probability, so with C58 notation X_ex=G/q^2,w_I0, (4) reduces to1-(n-G)/q^2 as it must.

This changed theorem closes a previously plausible escape WITHOUT claiming a wider impossibility: permitting arbitrary larger subsets alone, while keeping one shared fractional coefficient pP and common bit marginals p and paired-unit repair, cannot provide a positive uniform full surplus in the stated growing-support bounded-measure regime.
It does not obstruct mixing distinct p_B at individual atoms, noncentered representative families, other rounding alphabets or wider windows.
A convex mixture of separately complementary members is a different quantitative operation and is not used here as a new capacity theorem.
The exact arithmetic-income versus physical-width target for unrestricted G0001 remains open.

<a id="all-subset-common-marginal-author-freeze"></a>
## 7. Complete author self-check and review handoff

Root checked the complete arbitrary rational joint-law domain, actual flat unit/minimal polynomial and all n bounds; exact two zero residues and paired repair of BOTH; zero coefficient means, signed pair moments and every lag; cardinality identity including the full-subset double charge; complement symmetry and full signed product; primitive-content and true-q proofs for proper/empty/full labels and p0=-1; both physical endpoints, FINAL weight lcm and every original norm/resultant copy; norm income with full-subset removal and all original roots; monotonic root bound, all strict/weak endpoints, n3/n4 exclusions, n>=5 uniform limit and coarse bound; the entire p1/q successful-q condition, fixed-n q-asymptotic and exact old quartic consistency control.
No unproved realization, new source, native computation, mathematical digest or formal assistant is a premise.
No author defect was found; independent review remains separate.

The ENTIRE original allocation and Sections1--7/equations1--13, full source/reuse/contributor history, every actual cost and scope limit are AUTHOR-FROZEN at 2026-10-12T11:18.
Root is the sole new mathematical contributor and cannot independently review this theorem.
A separate whole noncontributor must inspect its actual complete scope before any adoption; a later Claim wrapper also requires an actual extraction review.
The unrestricted Task is active and unresolved; no weekly allowance is restarted here.


<a id="all-subset-final-splitting-correction"></a>
## Dated FINAL-weight correction and corrected complete freeze

2026-10-12T11:31.
The [R273 original whole finding](../audits/reviews/Yin_R_G0273_v1.md#all-subset-original-split-denominator-finding) found that Section3's original sentence `If r clears the original w_B, then M divides2r; this is only an upper clearing bound, not equality.` wrongly applied its bound after arbitrary additional positive label splitting.
Referenced finding relationship: self-reviewed.
The original sentence is preserved here as the exact rejected scope.
In the old quartic law, aggregate r16 and splitting the1/4 singleton into1/12+1/6 yield actual FINAL M48, which does not divide32.
Actual q4, every lag, energy15/16 and full weighted norm income are unchanged.

The active sentence now restricts M_unsplit | 2r to the canonical two-zero paired repair BEFORE additional splitting.
After splitting, the actual FINAL M is recomputed from the complete actual weights with no bound in terms of aggregate r alone.
Every copied-product formula throughout already uses that true FINAL M; no energy, income or asymptotic proof changes.
Root owns this correction; the original R273 negative finding remains at its original scope and is not converted to a pass.

Freeze the ENTIRE corrected body including the original allocation, Sections1--7/equations1--13, original19:18 freeze and this dated counterexample/correction.
A separate complete corrected-body finding is required before adoption.
No native program, new source, new allowance or unrestricted Task conclusion accompanies this repair.
