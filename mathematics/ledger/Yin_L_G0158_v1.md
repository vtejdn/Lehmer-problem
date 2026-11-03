---
author: Yin
---

# Full weighted-return tests: support density, minimal blocks, and bounded-height loops

Date: 2026-10-09.
Bounded G0001/S_G0007 candidate by the assigned execution_and_deliverables AI for Yin, with the coordinating AI's quartic Salem contribution and the entropy_status AI's actual Lehmer loop construction disclosed below.
This failed-mechanism analysis is self-checked and has the complete independent AI written review and fixed-ledger adoption recorded below.
No numerical computation, word enumeration or new source was used.
No novelty claim or new entropy lower bound is made.

The candidate was to improve complete weighted first-return control by partitioning every actual return relation into minimal zero blocks and using the connectivity forced by the earlier-prefix conditions.
The local reuse check read [L85's complete minimal-block argument](Yin_L_G0085_v1.md#uniform-fixed-moment-energy), [L154's original first-return law](Yin_L_G0154_v1.md#actual-first-return-paths), [L156's complete reentry interface](Yin_L_G0156_v1.md#complete-unit-trace-kernel), and the [fixed quartic Salem input](Yin_L_G0008_v1.md#quartic-projection-obstruction).
The conclusions below isolate the support range that remains to be controlled and test whether first return bounds minimal-block size.
The final actual control tests whether long first returns necessarily have growing quotient height or prime support.
None of these tests supplies the missing estimate for dense connected relations and all omitted reentries.

<a id="full-word-support-tail-bound"></a>
## 1. A complete support-density bound under the original word weights

Use X_0=0, X_(j+1)=alpha X_j+eta_j, with independent digits of probabilities w_0=1/2 and w_1=w_(-1)=1/4.
Let K_n be the number of nonzero digits in a word of length n.
A prescribed word with k nonzero digits has probability 2^(-n-k).
Therefore, before imposing any algebraic endpoint or first-return constraint,

    Pr(K_n=k)=binom(n,k) 2^k 2^(-n-k)
             =2^(-n) binom(n,k).                    (1)

All signs and positions, including dense words, are accounted for.
Since the indicators of nonzero digits are independent fair bits,

    E[4^(-K_n)]=(5/8)^n,
    Pr(K_n<=n/8)<=[(5/8)2^(1/4)]^n=a^n.            (2)

The inequality follows because 4^(-K_n)>=4^(-n/8) on the indicated event.
The random variables K_n and n-K_n have the same distribution, so the same bound holds for K_n>=7n/8.
The inequalities retain their literal real thresholds; no divisibility of n by eight is required.

Let f_n be the actual first-return probability, as in L154.
Split it into f_n^ext and f_n^mid according as K_n<=n/8 or K_n>=7n/8, or instead n/8<K_n<7n/8.
These are disjoint cases and cover every word.
As the first-return event is a subevent of the word events just estimated,

    f_n=f_n^ext+f_n^mid,       f_n^ext<=2a^n,
    sum_(n>d) f_n^ext z^n
      <=2(az)^(d+1)/(1-az),       0<=az<1.           (3)

This is a complete infinite-tail bound on its named subclass.
It does not estimate f_n^mid or replace all first returns by sparse ones.

<a id="actual-salem-middle-density-tail"></a>
## 2. An actual nonvanishing middle-density weighted tail

Set z=4/3 and

    r=az=(5/6)2^(1/4),       r^4=625/648<1.          (4)

For every actual nontorsion algebraic unit of degree d with M<4/3, the retained [L154 complete-tail theorem](Yin_L_G0154_v1.md#complete-weighted-return-tail-lower-bound) gives sum_(n>d) f_n (4/3)^n>=1/3.
The extreme-support contribution in (3) is finite.
It follows that

    sum_(n>d) f_n^mid (4/3)^n
       >=1/3-2r^(d+1)/(1-r).                        (5)

If the middle sum is infinite this assertion is still valid.
The argument only subtracts the finite upper bound in (3), never infinity from infinity.
A negative right side at a small d is allowed and is not claimed to be informative.

In particular, use exactly the already fixed actual Salem inputs

    P_N=t^N(t^3-t-1)+(1-t^2-t^3),
    N=9 modulo 120, N>=129,        d=N+3.             (6)

The [L154 actual-family control](Yin_L_G0154_v1.md#salem-first-return-tail-control) reuses their irreducibility, Salem property, preservation of degree under every positive power, and theta<M(P_N)<4/3, where theta>1 is the plastic root.
Hence the lower limit of the middle-density weighted tail in (5), along this family, is at least 1/3.
The total contribution of the two extreme support ranges tends to zero exponentially in d.

Consequently an estimate confined to the two support ranges in (3) misses an actual nonvanishing part of the weighted first-return law.
This includes any input-independent sparse cutoff K_n<=b(n) with b(n)/n tending to zero: once d is sufficiently large, b(n)<=n/8 for every n>d.
Fixed input-independent support bounds are a special case.
No claim about an arbitrary input-dependent cutoff is needed.
The family stays away from Mahler measure one and does not refute a separately proved smaller exponent or a sufficiently-near-one theorem.
The general conditional assertion (5) uses its literal M<4/3 hypothesis; it does not assert that new near-one inputs exist.
Nor does it identify this middle mass as nonunit reentry: it is a statement about the whole actual first-return law, with no prime-support restriction.

<a id="first-return-minimal-block-connectivity"></a>
## 3. What earlier-prefix avoidance forces, and what it does not

Let alpha be nontorsion and let a nontrivial first-return word have length n>1 and endpoint polynomial

    Q(t)=sum_(j=0)^(n-1) eta_j t^(n-1-j).

Its first and last digits are nonzero.
An initial zero digit would return at time one.
If its last digit were zero, X_n=alpha X_(n-1)=0 would give an earlier return because alpha!=0.

Partition the occupied signed terms of Q(alpha)=0 into inclusion-minimal nonempty zero subsets, as in L85: extract such a subset, remove it, and repeat on the remaining zero relation.
Terms of a height-one polynomial occupy distinct exponents.
There are no one-term blocks, and a two-term block would force alpha^h=+1 or -1 for a nonzero integer h, contrary to nontorsion.
Each block has at least three terms.

Every such partition must have a block crossing each internal cut between exponents c and c+1, for 0<=c<n-1.
Otherwise all blocks lie wholly on one side or the other, and the sum of the high-exponent terms is zero.
Those terms are nonempty because the leading digit is nonzero; after multiplying by alpha^(-(c+1)), they are the state of a proper prefix.
This contradicts first return.
Thus the convex intervals spanned by the blocks cover every internal cut.
This is a necessary condition only; no converse first-return test for an arbitrary chosen partition is asserted.

The condition does not bound the number of terms in a block, even on an actual fixed reciprocal Salem input.
Use the irreducible p(t)=t^4-t^3-t^2-t+1 and its real conjugates beta>1 and beta^(-1) from the fixed quartic input cited above.
For every integer k>=0, direct multiplication gives

    Q_k=p(t) sum_(r=0)^k t^(3r)
       =t^(3k+4)-t^(3k+3)-sum_(r=0)^k t^(3r+2)-t+1. (7)

All displayed exponents are distinct, so Q_k has coefficient height one.
Its quotient sum_(r=0)^k t^(3r) also has height one.
We next check every nonempty proper subset of the occupied signed terms, not just every prefix.

If a subset omits the highest positive term, its only possible positive term is the constant one.
At beta>1, every negative term has magnitude strictly larger than one.
Thus no nonempty such subset sums to zero: it is either the positive constant alone or has a strictly negative sum.

Suppose a subset contains the highest positive term but omits the positive constant.
If its integer polynomial vanished at beta, irreducibility would force divisibility by p and hence vanishing at the conjugate beta^(-1).
At that conjugate, the highest power is positive and strictly smaller than every negative term in absolute value, because all negative exponents are smaller.
A subset with a negative term is strictly negative there, and the highest term alone is positive.
Both cases contradict vanishing.

Finally, a proper subset containing both positive terms must omit at least one negative term.
Evaluating at beta, its sum is strictly positive, since the complete relation is zero.
These cases prove that the entire support in (7) is one minimal zero block, of unbounded size k+5.

Read Q_k's coefficients in descending order.
The word has

    length=3k+5,       number of nonzero digits=k+5,
    probability=2^(-4k-10).                          (8)

No proper nonempty prefix returns: after multiplication by a nonzero power of beta its value is the sum of a proper nonempty subset of the signed terms in (7), which cannot vanish.
The last constant term is nonzero, so every proper prefix omits a term.
All intermediate states are actual, since the complete word returns by (7).
The negative word is a second distinct first return of the same weight.
Their entire family therefore contributes exactly

    sum_(k>=0) 2^(-4k-9) z^(3k+5)
       =z^5/[512(1-z^3/16)],       0<=z<16^(1/3),   (9)

as a convergent nonnegative series, and the identity is also formal.
It is an explicitly specified subseries of the full first-return law; there is no exhaustion claim.
It is increasing on 0<=z<=2 and has value 1/8 at z=2, so throughout that range it is at most 1/8.

This is a fixed degree-four reciprocal Salem input with M=beta, not a new sufficiently-near-one family.
It shows that first return and interval connectivity alone cannot impose bounded block arity, even at fixed degree within this reciprocal class.
It does not refute a separately proved smaller near-one claim or show that high arity is itself costly: this family's full original-law weights are summable in the explicit range (9).
The old irreducibility and Salem classification are reused, not newly audited or enumerated.

<a id="actual-lehmer-bounded-height-long-returns"></a>
## 4. Actual long Lehmer first returns with quotient height one

Reuse the named irreducible degree-ten input and original digit law from [L155](Yin_L_G0155_v1.md#norm-cell-actual-returning-domain), and the quotient-height convention of [L157](Yin_L_G0157_v1.md#return-core-quotient-height-equivalence):

    P(t)=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1,
    P(alpha)=0,              alpha>1.

Irreducibility is reused at its existing fixed scope.
Define

    A(t)=-t^8+t^6+t^3,
    c(t)=1-t^2,
    B(t)=-t^5-t^2+1,
    S_k(t)=sum_(r=0)^(k-1)t^(3r),  S_0=0.

Direct multiplication gives

    (t^3-1)A(t)+c(t)=-(t-1)P(t).                    (10)

For every integer k>=0 put q_k(t)=-(t-1)sum_(r=0)^(k+2)t^(3r), Q_k=Pq_k.
Then

    Q_k=t^(9+3k) A+t^9 c S_k+B.                     (11)

At k=0 the identity is the exact expansion

    Q_0=-(t-1)P(1+t^3+t^6)
       =-t^17+t^15+t^12-t^5-t^2+1=t^9 A+B.         (12)

For general k, use t^(3k)-1=(t^3-1)S_k and (10).
The right side of (11) equals Q_0-(t-1)P t^9 S_k, exactly the defining Q_k.
Reading (11) in descending coefficient order gives three nonoverlapping digit blocks:

    prefix, length 9: (-1,0,1,0,0,1,0,0,0);
    loop, length 3:   (-1,0,1), repeated k times;
    suffix, length 9: (0,0,0,-1,0,0,-1,0,1).          (13)

There is no hidden collision of these blocks' coefficients.
Thus deg Q_k=17+3k, its word length is 18+3k, and it has 6+2k nonzero digits.
The coefficients of q_k are +1 at 3r and -1 at 3r+1, for 0<=r<=k+2.
These positions are disjoint, so the maximum absolute coefficient heights satisfy

    H(Q_k)=H(q_k)=1     for every k>=0.              (14)

The word Q_0 has length 18 and nonzero leading and final digits.
An earlier return at time l would make its nonzero prefix polynomial vanish, forcing l>=11 by minimal-polynomial divisibility.
The remaining suffix, still with a nonzero final digit, would similarly have length at least 11.
That would force 18>=22, a contradiction.
Thus Q_0 is a genuine first return.

Its state after nine digits is x=A(alpha).
From (10),

    (alpha^3-1)x=alpha^2-1,
    x=(alpha+1)/(alpha^2+alpha+1).                  (15)

The loop in (13) makes exactly the transitions

    x -> y=-1/(alpha^2+alpha+1)
      -> alpha y=-alpha/(alpha^2+alpha+1)
      -> x.                                        (16)

These states are nonzero units.
To check this, set C(t)=t^2+t+1.
Reduction modulo C gives P(t)=-t^2.
For its roots omega,omega^2, with omega^3=1 and omega!=1, resultant interchange gives

    Norm_(Q(alpha)/Q)(C(alpha))
      =Res(P,C)=Res(C,P)
      =(-omega^2)(-omega^4)=1.                      (17)

The interchange sign is positive since 10*2 is even.
Thus the algebraic integer C(alpha) is a unit.
Direct evaluation gives Norm(alpha)=1 and Norm(alpha+1)=P(-1)=1, so every state in (16) is a maximal-order unit.

Inserting any number of these nonzero loops at the ninth state of Q_0 preserves all later suffix states and introduces no earlier zero.
The fixed prefix and suffix have no intermediate zero by the first-return proof for Q_0.
Hence every Q_k is a genuine first-return word.
Negating its digits gives a second genuine first return of the same weight.
All states in these words lie in the finite set of Q_0 states together with y and alpha y, and their negatives.
Their nonzero states therefore have one common finite prime-ideal support.
No factorization of that finite set is asserted or needed.

The probability of the specified Q_k word, retaining every zero digit and sign choice, is

    Pr(Q_k)=2^(-24-5k).                              (18)

Different k have different lengths, and the two signs give distinct words.
Their exact nonnegative contribution to the complete F is

    G(z)=sum_(k>=0)2^(-23-5k) z^(18+3k)
        =2^(-23) z^18/(1-z^3/32),
             0<=z<32^(1/3).                        (19)

The series identity is also formal.
In its convergence range F(z)>=G(z).
It is increasing on 0<=z<=2 and satisfies G(z)<=G(2)=1/24.
Thus this subseries does not prove divergence or obstruct a sufficiently small positive weighted exponent.
It does not bound other paths from above.

Its role is precise: arbitrarily long genuine first returns need not have increasing quotient height or new prime ideals.
Charging only those two features leaves this infinite family untreated; equation (19) shows how this particular remaining family can be paid for exactly.
The fixed Lehmer input is not a new near-one family, and no claim of an infinite full returning domain is made.

<a id="connected-return-test-stop-boundary"></a>
## 5. Decision boundary and contribution scope

The present test supplies no estimate for the missing middle-density connected relations.
L85 counts all minimal zero blocks, with explicit shape and partition costs depending on their arities.
Applying that count unchanged here only returns to the retained moment problem; the necessary interval-crossing condition has not paid its costs when the total support is proportional to n.
Bounded-arity truncation also requires a justified weighted error, as the exact control (7)--(9) shows.
Equations (3)--(6) exclude treating the omitted middle-support words as harmless merely because sparse words are controlled.
Equations (10)--(19) separately exclude treating path length alone as a certificate of growing quotient height or prime support.
The latter two fixed controls are explicitly summable; neither asserts that their own contributions defeat a valid full-law upper bound.

The bounded candidate therefore stops here.
A substantive continuation would need a new arithmetic estimate for the complete weighted sum of the dense connected relations, or a full reentry estimate on a proved actual domain.
No further renewal identity, finite-prime reformulation, or generic fixed-order shape estimate is proposed as the missing input.
No unrestricted gap, smaller near-one obstruction, or new positive collision exponent is concluded.

The execution_and_deliverables AI proposed the connected minimal-block test, derived the all-word support tail (1)--(3), its actual Salem middle-density consequence (4)--(6), and the exact necessary cut condition, and assembled this written analysis.
The coordinating AI supplied the concrete quartic Salem family and its two-real-conjugate minimal-block control; the assigned AI checked its finite indices, minimality, first-return guard and weights and wrote (7)--(9).
Old L8/L85/L154/L155/L157 inputs are reused only at their stated fixed scopes.
The entropy_status AI derived the Lehmer construction (10)--(19), including the exact polynomial decomposition, finite-index first-return proof, unit loop, quotient height and full subclass sum.
The coordinating and assembling AIs checked that component as contributors, not independent reviewers.
Author self-check covers every displayed formula (1)--(19) and all actual-domain and weighted-tail qualifiers.
The coordinating AI also read the complete assembled argument as a contributor; this check is separate from the independent review below.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0057_v1.md#complete-independent-written-review-and-adoption), with its original inspected scope and relationship.
