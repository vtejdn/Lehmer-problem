---
author: Yin
---

# Disjoint local energy, exact multi-field repair and complete ramification controls

The entire mathematical argument of [L73](../ledger/Yin_L_G0073_v1.md#dk25-assigned-local-energy), dated2026-10-07, is retained below.
The already retained source analysis stays in DK25-U001, while this claim owns the separate partition repair and complete local coverage/diagnostic proofs.

## Statement

Let alpha be a nonzero algebraic integer of degree d>=2 with monic irreducible P and polynomial discriminant Delta.
For each prime p partition the original root indices into disjoint blocks I_j, with n_j=|I_j|, inside actual finite local fields K_j of ramification e_j and residue size q_j in one common algebraic closure.
Then

    v_p(Delta)>=sum_j(n_j^2/q_j-n_j)/e_j,
    B_p=max(0,sum_j(n_j^2/q_j-n_j)/e_j),
    h(alpha)>=sum_p B_p logp/(2d^2)-logd/(2d).

Only finitely many B_p are positive.
Assign each root to precisely its generated field Q_p(alpha_i), and let m_K count assigned roots while s_K counts all roots belonging to K.
Disjoint pair counting and weighted Cauchy give

    v_p(Delta)>=max(0,d^2/sum_K(e_K q_K)-sum_K(m_K/e_K))
                >=max(0,d^2/sum_K(e_K q_K)-sum_K(s_K/e_K)).

This proves the original numerical RHS of DK25 Theorem1.5 without its faulty overlapping-count or duplicated-valuation identities.
The corresponding safe Corollary1.6 uses assigned m_K throughout its quadratic expression; the original full-membership-count corollary is not adopted or asserted false.
For beta=alpha^a of distinct degree delta and s actual conjugates in K of degree n_K and residue size q, the exact finite source interface gives

    m(P_alpha)>=d logq [s^2/(q+1)-s]/(2a n_K delta^2)
                  -d logdelta/(2a delta).

All power and degree costs remain explicit; a sublinear count at exponent1 does not by itself yield a fixed gap after a proportional-to-d exponent.
The complete odd-d>=3 unit family P_d=(t+1)^d-2 has a d-fold root mod2 but

    |disc P_d|=d^d 2^(d-1),
    v_2(disc P_d)=d-1,
    M(P_d)>=3^((d/3-1)/2) -> infinity.

Its tame local splitting ramification is d, individual difference valuations are1/d, and a=2^ceil(log2 d) satisfies d<=a<2d and t^a=1 in the full reduced quotient.
The single-prime coarse energy gives no uniform positive bound; the complete discriminant with the original Mahler inequality does give m(P_d)>=log2/2.
This diagnostic refutes only an unjustified quadratic 2-adic energy inference, without constructing a near-one family or proving arbitrary-input coverage.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:36 |
| status | open |
| reason | Register the entire retained original proof with explicit statement and exact existing interfaces; current whole review and any adoption follow separately. This performs no source acquisition, native execution or research resumption and claims no independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Complete assigned local energy/unchanged Theorem1.5 RHS, safe assigned Corollary1.6, exact powering costs and full shifted-Eisenstein diagnostic. |
| argument | [Complete argument](#argument) | Entire original disjoint pair counting, weighted Cauchy, source/power comparisons and all irreducibility/local ramification/discriminant/measure/scalar calculations. |
| dependency | [Retained finite source interface](../audits/literature/DK25/Yin_U001.md#dk25-u001) | Actual generated-field/full-membership definitions and proof defects, complete finite single-field inequality and direct Mahler/Hadamard proof at the recorded original reading depth; original Corollary1.6 is not adopted. |
| support | [Integral scalar norm comparison](Yin_C_G0244_v1.md#scalar-collapse-root-matrix-interface) | The diagnostic family has an actual full-quotient scalar identity after linear powering, with the separate nontorsion norm route; no new numerical margin is recertified. |
| support | [Ramified valuation boundary](Yin_C_G0254_v1.md#ramified-valuation-capture) | Precise conditional valuation-depth versus residue-multiplicity boundary; no extra coverage theorem is supplied. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:40 |
| status | proved |
| reason | Adopt the entire disjoint-assignment repair, finite source/power comparison and full shifted-Eisenstein diagnostic after actual whole current self-review. The original Theorem1.5 RHS and assigned-only corollary remain exact; the original corrected single-prime conclusion is precision restoration with actual rereading, without a substantive repair or new independent review claim. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete assigned local energy/unchanged Theorem1.5 RHS, safe assigned Corollary1.6, exact powering costs and full shifted-Eisenstein diagnostic. |
| argument | [Argument](#argument) | Entire original disjoint pair counting, weighted Cauchy, source/power comparisons and all irreducibility/local ramification/discriminant/measure/scalar calculations. |
| dependency | [Dependency](../audits/literature/DK25/Yin_U001.md#dk25-u001) | Actual generated-field/full-membership definitions and proof defects, complete finite single-field inequality and direct Mahler/Hadamard proof at the recorded original reading depth; original Corollary1.6 is not adopted. |
| support | [Support](Yin_C_G0244_v1.md#scalar-collapse-root-matrix-interface) | The diagnostic family has an actual full-quotient scalar identity after linear powering, with the separate nontorsion norm route; no new numerical margin is recertified. |
| support | [Support](Yin_C_G0254_v1.md#ramified-valuation-capture) | Precise conditional valuation-depth versus residue-multiplicity boundary; no extra coverage theorem is supplied. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0527_v1.md#current-assigned-energy-finding) | Entire exact current statement, complete retained proof and every selected interface, self-reviewed; original findings retain their actual old inputs and scopes. |

## Complete retained argument

<a id="argument"></a>

<a id="dk25-assigned-local-energy"></a>
### Disjoint local blocks

Let alpha be a nonzero algebraic integer with monic irreducible polynomial P of degree d>=2, roots alpha_i, and discriminant Delta.
For each prime p under consideration, choose a partition of the root indices into blocks I_j, and finite local fields K_j containing all alpha_i for i in I_j, inside one fixed algebraic closure of Q_p.
Write n_j=|I_j|, e_j=e(K_j/Q_p), q_j=|residue field K_j|.
The same field may be used more than once, although merging identical-field blocks can give a stronger estimate.
Empty blocks may be discarded.

Within block j let n_(j,x) count the roots reducing to x.
Every such pair has normalized difference valuation at least1/e_j.
All conjugates are integral, so all other pair contributions to v_p(Delta) are nonnegative.
Pairs retained in different blocks are disjoint.
It follows that

    v_p(Delta)>=sum_j (1/e_j) sum_x n_(j,x)(n_(j,x)-1)
               >=sum_j (n_j^2/q_j-n_j)/e_j.             (1)

In particular define

    B_p=max(0,sum_j (n_j^2/q_j-n_j)/e_j).

For any finite set of primes, and hence over all primes with
positive B_p,

    log|Delta|>=sum_p B_p log p,
    h(alpha)>=1/(2d^2) sum_p B_p log p-log d/(2d).      (2)

There are only finitely many positive terms, since (1) forces p to divide Delta when B_p>0.
This proof counts root pairs inside a single common splitting closure.
It never adds separate valuations of the same rational discriminant.

### Theorem1.5 retains its numerical statement

For each p let Q_(p,alpha) be the source's set of actual fields Q_p(alpha_i).
Assign root i precisely to its generated field, and put

    m_K=#{i:Q_p(alpha_i)=K},
    s_K=#{i:alpha_i in K}.

Then sum_K m_K=d and m_K<=s_K, even for nested fields.
Weighted Cauchy--Schwarz gives

    sum_K m_K^2/(e_K q_K)>=d^2/sum_K e_K q_K.

Combining with(1),

    v_p(Delta)>=max(0,d^2/sum_K e_K q_K-sum_K m_K/e_K)
                >=max(0,d^2/sum_K e_K q_K-sum_K s_K/e_K).

The final inequality replaces assigned counts by larger full membership counts only in a **subtracted** term.
Substitution into(2) yields exactly the RHS printed in DK25 Theorem1.5.
Thus the invalid intermediate source identities have a complete repair; no change to the theorem's numerical constant is needed.

The corresponding safe version of Corollary1.6 is

    h(alpha)>=1/2 sum_p max(0,
          1/d^2 sum_K (m_K^2/q_K-m_K) log(q_K)/[K:Q_p])
          -log d/(2d).                                (3)

Here the m_K are assigned counts.
Replacing them throughout(3) by s_K would also enlarge the positive quadratic terms and is not justified by m_K<=s_K.
The original Corollary1.6 is therefore not adopted.
No counterexample to its complete statement is claimed merely from the proof defect.

### What the source changes, and what it does not

For one fixed local field, the exact single-field source bound proved in the audit needs only about sqrt(d log d) actual local conjugates to force an absolute lower bound on m(P).
This is weaker than requiring a fixed positive fraction **at exponent1**.
It does not establish that such conjugates exist.

There is also an important distinction from the unramified modular-collision route.
If p does not divide disc P, all d roots have distinct reductions.
Consequently at most q of them can lie in an integral local field with residue field F_q; for units at most q-1.
For fixed q, that number cannot reach sqrt(d log d) in unbounded degree.
The source's growing local count may use p dividing disc P, including order-index effects; field-unramifiedness alone does not imply p is prime to disc P.

Applying the source to beta=alpha^a does not erase exponent cost.
Let delta=deg beta, let s count beta's **distinct** conjugates in K, and n_K=[K:Q_p].
Since h(beta)=a h(alpha), the exact finite inequality gives

    m(P_alpha)>=d log q/(2a n_K delta^2)
                    * (s^2/(q+1)-s)
                 -d log(delta)/(2a delta).              (4)

Even when delta=d, a proportional to d and s of order sqrt(d log d) make this certificate only of order log(d)/d; they do not yield a fixed positive gap.
For fixed q,n_K and delta=d, a sufficient threshold for a prescribed gap epsilon requires s^2 to dominate a*d+d*log d.
When a is proportional to d this is again a linear count.
If the powered degree drops, equation(4), not d=delta by convention, must be used.

Thus this source supplies an alternative conditional criterion and a precise failure test for an attempted power transfer.
It supplies neither a=O(d) scalar coverage nor a positive fraction of low-degree residues at that cost.
The bounded search found no source that supplies that missing quantifier; this is a report of this search, not a literature nonexistence claim.
No second new source was selected.

### A ramification diagnostic on actual irreducible units

High multiplicity in P mod p cannot alone be counted as a quadratic discriminant-energy gain.
For odd d>=3, set

    P_d(t)=(t+1)^d-2.

It is irreducible because translating by1 gives the Eisenstein polynomial u^d-2.
Its constant term is-1, so every root is an algebraic unit.
It is nontorsion: one complex conjugate is `2^(1/d) exp(i*pi*(d-1)/d)-1`, whose modulus exceeds1.
Modulo2, the sole reduced root1 has multiplicity d.
Yet the translated binomial discriminant gives

    |disc P_d|=d^d 2^(d-1),
    v_2(disc P_d)=d-1                 (d odd).           (5)

The tame local splitting field has ramification index d: adjoining the d-th roots of unity is unramified at2, and adjoining 2^(1/d) is totally ramified of degree d.
Distinct root differences have valuation1/d.
Hence the actual energy is d-1, exactly as(5), despite the d-fold residue collision.
This family is a scope control, not a small-Mahler counterfamily.
Indeed at least d/3-1 of the d-th roots of unity have arguments between2pi/3 and4pi/3.
For r=2^(1/d)>1 each corresponding root satisfies `|r zeta-1|^2>=r^2+r+1>3`.
Consequently

    M(P_d)>=3^((d/3-1)/2) --> infinity.

At the same time, its companion order modulo2 is nilpotent around1.
If a=2^ceil(log_2 d), then `(t+1)^a=0` in F_2[t]/P_d and t^a=1, with d<=a<2d.
Thus the scalar-congruence norm mechanism does give a uniform bound for this family after linear powering.
Using only the 2-adic contribution d-1 in(2), the discriminant certificate is `(d-1)log(2)/(2d)-log(d)/2`, which gives no positive uniform bound.
This limitation is specific to that single-prime input: the complete value `|disc P_d|=d^d 2^(d-1)`, combined with Mahler's original bound `log|disc P_d|<=d log d+(2d-2)m(P_d)`, does give `m(P_d)>=log(2)/2`.
The control only excludes the inference that a d-fold mod2 collision forces quadratic 2-adic discriminant energy; it does not exclude a gap obtained from the complete discriminant.

This identifies a concrete next arithmetic obligation: any ramified-coverage proposal must retain a usable valuation depth or an explicit nilpotent-power cost along with residue counts.
Neither a large multiplicity nor h(alpha)=m(P)/d small supplies those data automatically.
No infinite near-one family, universal coverage theorem or Lehmer counterexample is asserted.
