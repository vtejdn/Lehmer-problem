---
author: Yin
---
# Isolated-support bounds for complete norm surplus in a fixed extra window

Date: 2026-10-12T11:48.
Human author Yin.
Internal fixed extraction under the continuing G0001 authorization.
Root authored the original D18 mathematics.
g0001_routes independently reviewed that complete original account in R278 and now authors this new registered statement and wrapper.
The extractor is therefore a contributor to this actual Claim and cannot independently review its extraction.
R278 remains a whole-original finding only; a different noncontributor must inspect the actual new statement and interfaces.
The entire original proof and history are retained below.
This action neither adopts the Claim nor retires the source draft.

## Statement

Let P(t)=sum_(i=0)^d p_i t^i be the ACTUAL monic irreducible nontorsion integer-unit minimal polynomial of alpha, with original d>=2, p_0 in{+1,-1}, p_d=1 and every p_i in{0,+1,-1}.
Use the actual field K=Q(alpha), monogenic order O0=Z[alpha] and total logarithmic Mahler measure m=m(P).
Put S={i:p_i!=0} and n=|S|.
No reciprocity hypothesis is imposed.

Fix an integer k>=0.
An index i in S is k-isolated when |i-i'|>k for EVERY different i' in S.
Let h count these actual original support indices, and set

    r=k+1, T=d+k, N=T+1, h>=1024r,
    kappa=sqrt(r/h)<=1/32,
    C=1+sqrt(r n/h), tau=T/d=1+k/d,
    a=(1+kappa)^(-2), b=2/(1+sqrt2 kappa)^2.

The allowed representatives are ALL rational polynomials f supported in[0,T] with f(alpha) a nonzero ACTUAL O0 integer.
There is no fixed residue inventory, coefficient-height cutoff, common fractional class or prescribed scalar denominator.
A value is called monomial in this allowed window precisely when it equals+/-alpha^ell for some0<=ell<=T; this concerns the actual value, not the coefficient shape of its representative.
All such values have absolute full norm1.
Other units may lie outside this class.

**A. All-representative fractional quotient and two shells.**
Let B have the r coefficient columns of t^jP,0<=j<=k, in the full N-dimensional allowed window.
Every allowed f admits

    f=z+B theta, z in Z^N, theta in Q^r,
    |theta_j|<=1/2, z(alpha)=f(alpha)!=0.

For e=||f||_2^2, these representatives satisfy

    e>=h||theta||_2^2,
    |(B theta)_ell|<=kappa sqrt(e) for every ell,
    e>=a.

If the ACTUAL value f(alpha) is not monomial in the stated window, then e>=b.
In particular

    a>=1-2kappa,
    b>=2-6kappa,
    b-a>=1-6kappa>=13/16>0.

These conclusions cover arbitrary integer shifts of all r kernel directions and both nearest-half endpoints.
They do not assert equality or sharpness of the bounds.

**B. Every final weight and every original norm.**
Take ANY finite packet of the allowed representatives with strictly positive normalized rational FINAL weights omega_i.
Write

    e_i=||f_i||_2^2, E=sum_i omega_i e_i<1,
    D_i=Norm_(K/Q)(f_i(alpha)) in Z minus{0},
    Lambda=(1/d)sum_i omega_i log|D_i|.

Let pi be the total final weight of values outside the above monomial-value class, and E_bad their total weighted energy.
Then

    E>=a+(b-a)pi>=a,
    0<=pi<(1-a)/(b-a)
              <=2kappa/(1-6kappa)<3kappa<=3/32.

For EACH label there is an integer representative z_i of the same actual value with

    1<=||z_i||_1<=C^2 e_i,
    0<=log|D_i|/d<=log(C^2 e_i)+tau m.

Monomial-value labels have zero norm logarithm.
If pi=0, Lambda=0; otherwise the FULL nonmonomial class satisfies

    Lambda<=pi[log(C^2 E_bad/pi)+tau m]
           <=pi[log(C^2/pi)+tau m].

In all cases the entire original norm income obeys

    0<=Lambda<=3kappa[log(C^2/(3kappa))+tau m].

No positive-weight label, negative norm sign or rare high-energy contribution is discarded.
No lag cancellation, bit law, atomwise sign condition, diagonal coefficient covariance or bounded number of labels is assumed for A or B.

**C. Complete surplus and the fixed-extra-width obstruction.**
EVERY packet in B satisfies

    0<Lambda-(1/2)logE
       <=3kappa[log(C^2/(3kappa))+(1+k/d)m(P)]
                     +log(1+kappa).

For any fixed k and fixed real c>0, along ANY sequence of the stated actual flat inputs with n->infinity, h>=c n and bounded m(P), the isolation threshold holds eventually and this upper bound tends to0, with coarse order O(log n/sqrt n).
The assertion does not posit existence of that sequence or a near-one family.
It rules out a constant positive full surplus from below-one packets in this isolated-support regime with fixed additional width k.
It is not an obstruction for a degree-proportional additional width, unrestricted growing k, h small, E>=1 or nonflat inputs, and it is not a solution of the unrestricted Mahler problem.

**D. Exact complementarity and all original costs.**
If additionally ALL aggregate lags cancel with those SAME final weights, the packet is complementary.
Its ACTUAL common union width after at most one common monomial normalization satisfies

    d<=T_act<=d+k.

No equality to d+k is asserted.
In the chosen common normalization let q be the actual least coefficient denominator, F_i=q f_i in Z[t], M the actual FINAL indexed-weight denominator and m_i=M omega_i positive integer copies, so sum_i m_i=M.
With the full signed norms of those actual values,

    Res(P,F_i)=q^d D_i,
    product_i Res(P,F_i)^(m_i)
       =q^(dM) product_i D_i^(m_i),
    S_int=q^2 E, I_income=log q+Lambda,
    I_income-(1/2)log S_int=Lambda-(1/2)logE
         <=(T_act/d)m(P)<=(1+k/d)m(P).

The last price uses exact complementarity and the generic monic direct full-root inequality, not a reciprocal lifting assumption.
The coefficient denominator q and final weight denominator M are distinct quantities; positive label splitting requires the actual final M.
If a numerator has content b_i its full b_i^d factor remains in its resultant.
No primitive reduction or sign deletion is performed.
A common shift preserves absolute norms, Lambda and energy because alpha is an actual O0 unit, while its signed Norm(alpha) power must be included if the recorded norms precede that shift.
The upper theorem in C remains valid independently of how large q or M is.

For k=0 this gives a weaker first-window income bound; the previously adopted sharper flat first-window energy floor remains distinct.
Dense flat inputs have h=0 when k>=1, so the actual dense d+1 dyadic escape is outside these hypotheses.
The old2d-1 monomial projection supplies individual representatives, not a full packet contradicting this income theorem.
No new external source theorem or native computation is a premise, and neither D16 nor D17 is used as a proof input.

## Current assessment
[Selected decision](#decision-review-literal-corrected)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:48 |
| status | open |
| reason | Register the exact all-residue isolated-support theorem and complete original D18 proof, with every full norm, final weight, actual window and limiting hypothesis. R278 supplies only the original whole review. This new statement and wrapper were written by that earlier reviewer and require a different actual extraction reviewer. No uniform unrestricted surplus, adoption or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D on the actual flat original input, h>=1024(k+1), all nonzero actual O0 residues and positive final rational weights, with the fixed-extra-width and complementary-only cost boundaries. |
| argument | [Entire retained original proof](#argument) | Complete19:39 D18 Sections1--7/equations1--13, original allocation/reuse/contributions, every proof, cost, comparison and freeze. |
| dependency | [Generic-monic original-root price](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | ONLY after exact lag cancellation with the same final weights, full nonzero original norms and actual common union width; no reciprocal-lift hypothesis imported. |
| dependency | [Monogenic short-window interface](Yin_C_G0017_v1.md#statement) | ONLY E_T=1 for T<d in actual O0, hence a below-one packet has actual union width at least d; no full duality or optimizer claim needed. |
| dependency | [Actual short-width proof](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | Power-basis uniqueness after an actual unit shift, integer coefficients below degree d and the actual lower union-width boundary. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0278_v1.md#isolated-extra-window-whole-independent-finding) | Complete original D18 proof and its inspected direct interfaces; it does not cover this new registered statement/wrapper or prospectively adopt it. |


### Decision organized-reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:57 |
| status | proved |
| reason | Adopt the separately performed whole R278 and actual extraction R280 findings. Preserve every original isolation/window/energy hypothesis, full arithmetic and proof history; fixed additive width and degree-proportional width remain distinct. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D on the actual flat original input, h>=1024(k+1), all nonzero actual O0 residues and positive final rational weights, with the fixed-extra-width and complementary-only cost boundaries. |
| argument | [Entire retained original proof](#argument) | Complete19:39 D18 Sections1--7/equations1--13, original allocation/reuse/contributions, every proof, cost, comparison and freeze. |
| dependency | [Generic-monic original-root price](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | ONLY after exact lag cancellation with the same final weights, full nonzero original norms and actual common union width; no reciprocal-lift hypothesis imported. |
| dependency | [Monogenic short-window interface](Yin_C_G0017_v1.md#statement) | ONLY E_T=1 for T<d in actual O0, hence a below-one packet has actual union width at least d; no full duality or optimizer claim needed. |
| dependency | [Actual short-width proof](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | Power-basis uniqueness after an actual unit shift, integer coefficients below degree d and the actual lower union-width boundary. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0278_v1.md#isolated-extra-window-whole-independent-finding) | Complete original D18 proof and its inspected direct interfaces; it does not cover this new registered statement/wrapper or prospectively adopt it. |
| review | [Actual independent extraction](../audits/reviews/Yin_R_G0280_v1.md#c63-isolated-extra-window-actual-extraction-finding) | Entire actual statement, completely retained argument/history and all current direct interfaces, independently inspected after allocation by a noncontributor. |


### Decision review-literal-corrected

| Field | Value |
| --- | --- |
| date | 2026-10-12T12:43 |
| status | proved |
| reason | Select the actual reviewer-authored R280v2 at the SAME mathematical scope after its explicit repair of malformed square characters. Original v1 and earlier Claim decision remain historical; the reviewer re-read the actual affected formulas and preserved the complete finding and role/source limits. This changes the selected literal review evidence, not this Claim proof or scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D on the actual flat original input, h>=1024(k+1), all nonzero actual O0 residues and positive final rational weights, with the fixed-extra-width and complementary-only cost boundaries. |
| argument | [Entire retained original proof](#argument) | Complete19:39 D18 Sections1--7/equations1--13, original allocation/reuse/contributions, every proof, cost, comparison and freeze. |
| dependency | [Generic-monic original-root price](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | ONLY after exact lag cancellation with the same final weights, full nonzero original norms and actual common union width; no reciprocal-lift hypothesis imported. |
| dependency | [Monogenic short-window interface](Yin_C_G0017_v1.md#statement) | ONLY E_T=1 for T<d in actual O0, hence a below-one packet has actual union width at least d; no full duality or optimizer claim needed. |
| dependency | [Actual short-width proof](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | Power-basis uniqueness after an actual unit shift, integer coefficients below degree d and the actual lower union-width boundary. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0278_v1.md#isolated-extra-window-whole-independent-finding) | Complete original D18 proof and its inspected direct interfaces; it does not cover this new registered statement/wrapper or prospectively adopt it. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0280_v2.md#c63-isolated-extra-window-actual-extraction-finding) | Entire actual statement, completely retained argument/history and all current direct interfaces, separately inspected after allocation by a noncontributor. Finding relationship: self-reviewed. |

## Registration and complete preservation

The ENTIRE original19:39 D18 author body is retained below.
Only its duplicate front matter is represented once, its first title is demoted from one hash to two, and line endings/separating terminal blank space are normalized.
All original equations, anchors, mathematical statements, historical statuses, author roles, limits and freeze remain.
Relative ../claims/ and ../ledger/ paths remain valid from the Claim directory, so no locator replacement is necessary.

The original [D18 freeze](#isolated-extra-window-controls-and-freeze) is extraction ancestry and a preservation target, not an additional unprovided proof.
[C25](Yin_C_G0025_v1.md#statement), [C29](Yin_C_G0029_v1.md#statement) and [L237's projection passage](../ledger/Yin_L_G0237_v1.md#monomial-projection-uniform-margin) retain the comparison and attribution scopes stated in the whole proof.
The historical references to then-pending D16/D17 are kept as history; neither becomes a dependency of this Claim.
No new source intake or source-wide proof claim is made.

Root is the original mathematical author.
The current extractor previously completed R278's original whole noncontributor review and now contributes this wrapper; that does not change the earlier review's historical scope but prevents self-review of this actual extraction.
Complete-body comparison and a scoped material check are operational validation only.
Another actual fixed review and a separate responsible decision remain required for adoption.
This operation does not edit the source proof, retire D18 or perform any new native mathematics.

## Argument

## Isolated flat coefficients obstruct uniform full surplus in a fixed extra window

Date: 2026-10-12T11:39.
Human author Yin.
Root AUTHOR inquiry under the unchanged G0001 continuation.
Root supplies the isolated-row, two-shell and full-income proof here and cannot independently review it.
No native mathematical computation, external theorem or new source is planned.
This normal D allocation carries its own present scope only.

## Bounded reuse and changed question

[C25](Yin_C_G0025_v1.md#statement) already gives the complete first-window flat energy floor and denominator price; [C29](Yin_C_G0029_v1.md#statement) separates diagonal/full covariance and records a dense one-extra-power escape.
The actual [L237 monomial projection argument](../ledger/Yin_L_G0237_v1.md#monomial-projection-uniform-margin) was read: shifted-P columns, rational projection and trace give an individual monomial-valued low-energy representative in the2d-1 window, without a full complementary packet.
Those established interfaces are credited.
A bounded G-Claim search by isolated support/extra window/shell terms found no corresponding all-residue income bound in a fixed extra width.
No novelty or priority assertion follows.

Root's separate D17 first-window second-shell proof motivated asking what persists when the kernel has several shifted-P directions; D17 is still under whole review and is NOT a premise here.
All new estimates below are independently proved from integer coordinates, actual isolated coefficient rows and complete original norms.
The domain deliberately excludes dense inputs with no isolated coefficients, where the old one-extra-power escape is already real.

<a id="isolated-extra-window-domain"></a>
## 1. Actual input, isolated support and full representative domain

Fix the ACTUAL monic irreducible nontorsion integer-unit minimal polynomial P=sum_(i=0)^d p_i t^i, d>=2,p_0=+/-1,p_d=1,p_i in{0,+/-1}.
Put S={i:p_i!=0},n=|S|, actual O0=Z[alpha], original field Q(alpha) and total logarithmic Mahler measure m=m(P).
No reciprocity is required.
Choose a nonnegative integer k, put

    r=k+1, T=d+k, N=T+1.

An index i in S is k-isolated if |i-i'|>k for EVERY different i' in S.
Let h be the number of such indices.
We impose the explicit quantitative condition

    h>=1024 r,
    kappa=sqrt(r/h)<=1/32,
    C=1+sqrt(r n/h), tau=T/d.                     (1)

All counts refer to the original polynomial and degree, not a shortened support-degree surrogate.
For k0 every support index is isolated, so h=n; the resulting bound is weaker than the separate first-window inquiry and is retained only as a consistency case.

Let B be the N-by-r integer matrix whose j-th column is the coefficient vector of t^jP,0<=j<=k.
These columns are independent by their distinct monic highest terms.
Every rational polynomial f of degree at most T whose ACTUAL value is a nonzero O0 integer has a representation

    f=z+B theta, z in Z^N,
    theta in Q^r with |theta_j|<=1/2.              (2)

To prove this, subtract the actual degree<d integer power-basis representative of f(alpha).
Polynomial division gives P times a rational polynomial of degree at most k.
Subtract an integer nearest to each of those quotient coefficients and absorb its integer P multiple into z.
This reduces theta to the stated cube without changing the actual residue.
In particular z(alpha)=f(alpha)!=0, hence z is nonzero.
No random law, common per-atom fractional class, scalar denominator, coefficient-size cutoff or covariance assumption is imposed in (2).

<a id="isolated-extra-window-row-floor"></a>
## 2. Isolated rows control every fractional kernel coordinate

For each isolated i in S and0<=j<=k, row i+j of B has exactly ONE nonzero entry: it is p_i in column j.
Indeed if another column ell contributes, the original coefficient index is i+j-ell, distinct from i by at most k, contradicting isolation.
These h r rows are all DISTINCT: equality i+j=i'+j' with i!=i' would contradict |i-i'|>k, while i=i' forces j=j'.
Each row lies between0 and T.

In (2), the coefficient at that row is an integer plus p_i theta_j.
Its absolute value is at least |theta_j| because theta_j is in[-1/2,1/2].
If e=||f||^2, summing these distinct rows gives

    e>=h||theta||^2.

Every row of B has at most r entries of absolute value1.
By Cauchy--Schwarz,

    |(B theta)_ell|<=sqrt(r)||theta||
                         <=kappa sqrt(e) for every ell.       (3)

Both inequalities are global in f: there is no small-energy or small-coefficient assumption needed to prove them, and nearest-half endpoints are permitted.
Counting overlapping rows without the isolation proof would not be valid; the exact disjointness above pays that issue.

<a id="isolated-extra-window-two-shells"></a>
## 3. Whole-domain energy floor and a separated nonmonomial shell

Define a residue to be monomial in this allowed window if it equals+/-alpha^ell for some0<=ell<=T.
Every such value has absolute norm1.
This classification concerns the actual value, not the number of coefficients of its chosen rational representative.
Since z in(2) is a nonzero integer vector, at least one coordinate has |z_ell|>=1.
Equation(3) gives

    1<=|f_ell|+|(B theta)_ell|<=(1+kappa)sqrt(e).

Consequently every admissible representative satisfies

    e>=a=(1+kappa)^(-2).                            (4)

If the actual residue is NOT monomial in this window, z cannot be a signed unit coordinate vector.
If z has two nonzero coordinates, their absolute values sum at least2 and(3) gives

    2<=|f_i|+|f_j|+2kappa sqrt(e)
         <=(sqrt2+2kappa)sqrt(e).

If z has only one nonzero coordinate its magnitude is at least2, giving the stronger e>=4/(1+kappa)^2.
Thus in both cases

    e>=b=2/(1+sqrt2 kappa)^2.                       (5)

This shell statement does not call all nonmonomial values nonunits; additional units may lie there and contribute zero logarithmic income.
Nor does it require a specific integer representative: ANY cube reduction (2) satisfies the implications.
The bound b is strictly larger than a, since sqrt2/(1+sqrt2 kappa)>1/(1+kappa).

For later explicit constants, the elementary inequality (1+x)^(-2)>=1-2x for x>=0 gives

    a>=1-2kappa, b>=2-4sqrt2 kappa>=2-6kappa,
    b-a>=b-1>=1-6kappa>=13/16.                     (6)

The first inequality follows by multiplying by(1+x)^2, or by differentiation; sqrt2<=3/2 proves the second weakening.
In particular the selected condition(1) gives a genuine second shell above1.

<a id="isolated-extra-window-mass-and-norm"></a>
## 4. All nonunit norm income is charged by the actual energy

Take ANY finite rational packet with positive normalized rational FINAL weights omega_i, every f_i in[0,T] having nonzero actual O0 value, and

    E=sum_i omega_i e_i<1, e_i=||f_i||^2.

No lag cancellation is needed for the upper estimates.
Let pi be the total weight of residues that are not monomial in this window.
Equations(4)--(6) imply

    E>=a+(b-a)pi, E>=a,
    0<=pi<(1-a)/(b-a)
           <=2kappa/(1-6kappa)<3kappa<=3/32.        (7)

There is no cardinality restriction on this potentially nonunit part.
Every such label and every full norm will now be included.

For an individual f use the integer z from(2).
Each of the r columns of B has squared norm n, so its Frobenius norm is sqrt(rn), which bounds its operator norm by direct Cauchy--Schwarz.
Thus(3) gives

    ||z||<=||f||+||B theta||
           <=sqrt(e)+sqrt(rn)sqrt(e/h)=C sqrt(e).

Since z has integer coefficients, sum |z_ell|<=sum z_ell^2.
Its nonzero actual residue therefore has the integer coefficient bound

    1<=||z||_1<=C^2 e.                             (8)

At every ORIGINAL conjugate beta, |z(beta)|<=||z||_1 max(1,|beta|)^T.
Multiplying all d roots and dividing the logarithm by d yields, for D_i=Norm_(Q(alpha)/Q)(f_i(alpha)),

    0<=log|D_i|/d<=log(C^2 e_i)+tau m.             (9)

These D_i are nonzero signed integers, with no norm-one assumption in this estimate.
The lower bound in(8) ensures its logarithm is well-defined and nonnegative before the extra m term.
The original degree d and allowed exponent T are both retained.

Let Lambda=(1/d)sum omega_i log|D_i|.
Monomial residues have absolute norm1.
If pi0 then Lambda0.
Otherwise Jensen's inequality for the finite conditional weights on its complementary part, with E_bad<=E<1, gives

    Lambda<=pi[log(C^2 E_bad/pi)+tau m]
              <=pi[log(C^2/pi)+tau m].             (10)

For0<x<=3kappa the derivative of x[log(C^2/x)+tau m] is log(C^2/x)-1+tau m, positive because C^2>=1,3kappa<=3/32 and log(32/3)>1.
For example log4>1 by integrating1/t over[1,2] and[2,4], and32/3>4.
Hence(7) also covers the pi0 endpoint and proves

    0<=Lambda<=3kappa[log(C^2/(3kappa))+tau m].      (11)

This is a bound on the ENTIRE original norm income.
It is not a bound on only a chosen unit inventory or one embedding, and no rare high-energy label is lost: its energy enters E_bad in(10).

<a id="isolated-extra-window-full-surplus-theorem"></a>
## 5. Full-surplus theorem and the fixed-extra-width consequence

Since E>=a, -(1/2)logE<=log(1+kappa).
Combining this with(11) proves:

**Theorem.**
For EVERY actual finite rational packet in the full nonzero O0 residue domain of allowed window[0,d+k], with E<1 and the original coefficient-isolation condition h>=1024(k+1),

    0<Lambda-(1/2)logE
       <=3kappa[log(C^2/(3kappa))+(1+k/d)m(P)]
                     +log(1+kappa).               (12)

The strict positivity uses actual nonzero integer norms and E<1.
The theorem has no common marginal, bit law, prescribed residue inventory, atomwise sign, diagonal-covariance, coefficient-height or scalar-denominator restriction.
Every definition in(1) belongs to the actual input.
No supremum optimizer or actual packet attaining the upper bound is asserted.

In particular fix k and a real constant c>0.
Along ANY sequence of actual flat inputs with n->infinity, h>=c n and bounded m(P), condition(1) holds eventually and the right side tends to0.
Indeed r=k+1 is fixed, kappa<=sqrt(r/(cn)) tends to0, C^2<=(1+sqrt(r/c))^2 is bounded, and1+k/d is bounded (and tends to1 since d>=n-1).
The x log(1/x) factor tends to0.
The same proof gives the coarse order O(log n/sqrt n) in this fixed-k, fixed-c regime.
Existence of such a sequence or a near-one family is NOT asserted; this is an implication for any sequence satisfying the named hypotheses.

This rules out constant full surplus from below-one packets in these fixed extra windows on that specific isolated-support regime.
It does not cover h small, k growing with degree without the stated quantitative condition, energy E>=1, nonflat coefficients or the unrestricted Mahler problem.
In particular it does not rule out an absolute multiple C*d window; fixed additional k and degree-proportional additional width are different quantifiers.

<a id="isolated-extra-window-all-original-costs"></a>
## 6. True denominators, FINAL weights and physical-width accounting

If all aggregate lags additionally vanish, the packet is complementary.
Let T_act be its ACTUAL common union width after at most one common monomial normalization.
Its existing [0,d+k] representation gives T_act<=d+k.
Since alpha is a unit, a common normalization preserves nonzero O0 integrality and absolute norms.
The accepted monogenic short-width floor C17 and E<1 imply T_act>=d.
No exact equality T_act=d+k is claimed.

Let q be the ACTUAL least common coefficient denominator, F_i=q f_i in Z[t], M the ACTUAL FINAL indexed-weight denominator and m_i=M omega_i positive copies, sum m_i=M.
Keep every nonzero signed original D_i, including the known unit signs in the monomial class.
Then

    Res(P,F_i)=q^d D_i,
    product_i Res(P,F_i)^(m_i)=q^(dM)product_i D_i^(m_i),
    S_int=q^2E,
    I_income=logq+Lambda,
    I_income-(1/2)logS_int=Lambda-(1/2)logE
                       <=(T_act/d)m(P)<=(1+k/d)m(P).         (13)

The last inequality uses the accepted C10 generic direct argument ONLY after exact complementarity with these SAME final weights and original roots.
Positive label splitting changes actual M and copies; no pre-splitting denominator bound is reused.
If any numerator has content b_i, its full b_i^d resultant factor remains.
No polynomial is silently made primitive, no negative norm discarded from the copied product, and q is not identified with M.
A common unit shift contributes its actual signed norm power while preserving Lambda and energy.
This maintains the full original arithmetic even though the upper bound(12) is independent of how large q or M becomes.

<a id="isolated-extra-window-controls-and-freeze"></a>
## 7. Controls, source boundary and complete author self-check

For k0 one has h=n and r1; the above proof is an all-residue first-window upper bound of order log n/sqrt n.
C25's sharper energy floor and the separately authored D17 sharper second-shell income argument remain distinct.
Neither pending D17 nor pending all-subset D16 is a mathematical premise here.

For dense flat P and k>=1, adjacent original nonzero coefficients prevent every index from being k-isolated, so h0.
The hypothesis(1) fails exactly where the old dense dyadic d+1 escape may operate.
No conflict with C25/C29 is inferred.
L237's2d-1 monomial projection controls individual representatives at a different kernel dimension and says nothing about the complete income/covariance bound here.
These old mechanisms are credited at their actual scopes; the isolated-row argument does not claim them anew.

Root checked all monic/order and arbitrary rational-quotient details, coefficientwise nearest-integer reduction, exact h*r isolated-row disjointness, half-integer endpoints and sparse support; every global coordinate bound and both complete shell cases; true residue-versus-polynomial monomial distinction, pi0, positive shell gap and explicit1024 constant; integer l1 bound from squared coefficients and Frobenius norm, original T/d price and all full norms; conditional Jensen with rare large-energy atoms, derivative sign and growing-support/fixed-k quantifiers; actual width inequalities, one common shift, q/FINAL M/content/signed copies and C10 scope; and all dense/first-window/wider-window limitations.
No external lattice/mixing theorem or native program is a premise.
This is author checking, not independent review.

Freeze the ENTIRE current account, allocation/reuse/roles, Sections1--7/equations1--13 and every hypothesis/cost/limitation at 2026-10-12T11:39.
Root is the sole new mathematical author and cannot independently review it.
A separate whole noncontributor finding and any later actual Claim extraction review remain required before adoption.
No new weekly allowance, mathematical program, source acquisition or unrestricted Task conclusion is created.
