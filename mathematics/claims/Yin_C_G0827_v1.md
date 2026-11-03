---
author: Yin
---

# Radial-envelope obstruction for actual zero-deleted supersolutions and canonical first-hit ratios

Human author Yin.
Contributor original_signed_asymptotic developed the full returned-word comparison and the arbitrary radial-envelope exclusion; root identified the result for fixed reuse and checked the strict-core, compact-factor and equal-radius interfaces.
The argument is extracted from [D9, RE1--RE10](../drafts/Yin_D_G0009.md#radial-angular-deleted-kernel-test); that mutable extraction provenance is not a proof dependency.
The initial open assessment is retained in the history; the [current proved decision](#decision-whole-reviewed-2026-10-27) selects [whole independent R1047](../audits/reviews/Yin_R_G1047_v1.md#whole-radial-envelope-finding).

## Statement

Fix P(t)=t^4-t^3-t^2-t+1, its exterior Salem root beta, upper neutral conjugate zeta and actual order O=Z[beta].
For x in O write x_+=x(beta), x_-=x(beta^(-1)) and rho(x)=|x(zeta)|.
Put B=1/(beta-1), S=beta B and use the ENTIRE original accessible/coaccessible core

    D={x in O: |x_+|<B, |x_-|<S}.

This equality is the adopted fixed-quartic conclusion, including its retained co-return certificate scope; it is not an unproved replacement of the core by a strip.
The original digits are e in{-1,0,1}, with weights pi_(-1)=pi_1=1/4 and pi_0=1/2, and the chronological recursion is x_(j+1)=beta x_j+e_(j+1).
Define P_D(x,y)=pi_e if y=beta x+e belongs to D, and zero otherwise.
Let B_0 be P_D restricted to D minus{0}, killing transitions into zero without renormalizing a row.
For any finite F subset D containing zero, let B_F be P_D restricted to D minus F in the same way.

Let p_n=P_D^n(0,0), with p_0=1, be the COMPLETE original return probability, including every original returned word with its full product weight.
For a word w, write p(w) for the product of its digit weights pi_e.
The chronological endpoint is sum_(j=1)^n e_j beta^(n-j); reversing the finite iid word preserves its probability and gives the ascending-power convention used in C555.
Let f_n be the complete original first-positive-return probabilities and set

    U(z)=sum_(n>=0) p_n z^n,
    F_ret(z)=sum_(n>=1) f_n z^n,
    R=radius(U),                  R_f=radius(F_ret).

The notation F_ret distinguishes the first-return series from a finite exceptional set F.
Use the adopted entire root limit p_n^(1/n)->1/R, with 1<=R<=2.
For 0<t<R_f, the canonical actual first-hit function H_t has H_t(0)=1 and, for x!=0, is the sum of p(w)t^|w| over all original paths from x first hitting zero.
It is finite and strictly positive on D, with H_t=t P_D H_t off zero.
Separately use the adopted actual critical H=H_R, which is finite and strictly positive on D, satisfies H=R P_D H on D, and gives the stochastic kernel Q(x,y)=R P_D(x,y)H(y)/H(x).
Write Q_0 for its restriction to D minus{0}, killed on entry into zero.
The critical first-return mean is mu=sum_(n>=1) n f_n R^n, allowing infinity.

Fix t>0, any finite F subset D containing zero, and any pointwise finite W:D minus{0}->(0,infinity) satisfying

    t B_0 W(x)<=W(x),             x in D outside F.       (RE1)

No global boundedness, summability or regularity of W is assumed.
Put v=beta+beta^(-1)-2, tau=(3+sqrt13)/2 and h_k=v^(2k) for integers k>=1.
Then the following conclusions hold.

1. For every fixed integer n>=1, all sufficiently large k give actual endpoints h_k,beta^n h_k in D outside F and the complete original comparison

       B_F^n(h_k,beta^n h_k)>=p_n,
       t^n p_n W(beta^n h_k)<=W(h_k).

   The sufficient k conditions, strict legality of every translated intermediate state and its avoidance of F are proved below.
   The order of quantifiers is n fixed first, then all sufficiently large k; the translated paths are open.

2. Suppose there are epsilon>0, r_*>0, constants 0<c<=C<infinity and ANY function a:[r_*,infinity)->(0,infinity) such that

       c a(rho(x))<=W(x)<=C a(rho(x))

   for every x in D minus{0} with |x_+|,|x_-|<=epsilon and rho(x)>=r_*.
   Then t<=R.
   No monotonicity, growth or regularity hypothesis on a is imposed.
   In particular, t>R is impossible if, on all sufficiently large-radius actual states with real coordinates in an open neighborhood U of(0,0),

       W(x)=a(rho(x))G(x_+,x_-,x(zeta)/rho(x)),

   where G:U times S^1 ->(0,infinity) is continuous and a is any positive radial function on that radius range.
   W elsewhere may be arbitrary positive finite values.

3. For the actual critical candidate V=W/H, no inequality Q_0 V<=q V outside a finite F containing zero is possible with 0<q<1 when W has the radial-envelope comparison in item2.
   This is a candidate-class exclusion retaining the actual H, not a statement about all positive drift functions.

4. Conditionally on R_f>R, for every R<t<R_f and every fixed integer n>=1,

       H_t(h_k)/H_t(beta^n h_k)>=t^n p_n

   for all sufficiently large k.
   More explicitly, for every L>0, epsilon>0 and M>=0 there exist integers n,k>=1 such that both endpoints lie in D minus{0}, both have real-coordinate absolute values at most epsilon, their common neutral radius exceeds M, and H_t(h_k)/H_t(beta^n h_k)>L.
   Consequently this actual H_t cannot satisfy item2's radial comparison for any positive a, nor its positive continuous radius-angle representation.

These conclusions do not decide R_f>R, R_f=R, finite or infinite mu, a fixed-start tail lower bound, or positive linear bridge-level growth.
They do not exclude additive or nonuniform drift, the different square-root-affinity candidate, or arithmetic dependence that violates the stated envelope comparison.

## Exact inputs, reuse and boundaries

| Fixed input and selected assessment | Exact use |
| --- | --- |
| [C400 adopted exact core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Only the fixed quartic equality between D and the strict two-real-embedding strip, with original digits and actual-order membership; its C399 co-return input retains its complete certificate and review scope. |
| [C790 adopted unit geometry](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26) | Actual-order balanced unit v, v^2+3v-1=0, v^(-1)=v+3, v_+=v_-=tau^(-1), v(zeta)=-tau and tau>1; no count or probability lower bound is used. |
| [C555 adopted complete returns](Yin_C_G0555_v1.md#decision-isolated-whole-review-adoption-20261022) | Complete original independent-digit return probabilities and their entire entropy/root limit, with R=radius(U); chronological reversal preserves the iid word weight. No overlap or mean certificate is invoked. |
| [C511 adopted canonical family](Yin_C_G0511_v1.md#decision-complete-current-self-adoption) | The actual H_t first-hit definition, finite positivity and off-zero equation for every 0<t<R_f, including t>R when that interval exists; no endpoint at R_f is used. |
| [C805 adopted critical kernel](Yin_C_G0805_v1.md#decision-whole-reviewed-2026-10-26) | Actual finite positive critical H, its harmonic equation and stochastic original-weight Q in either mean branch; no reflection-block or Hilbert-space conclusion is needed. |

[C593 v2](Yin_C_G0593_v2.md#actual-real-projection-contraction-obstruction) already excludes its continuous two-real-coordinate contraction candidate and retains the distinct square-root-affinity route.
The present statement allows an arbitrary explicit neutral-radius factor and a continuous angular factor, and addresses the original chronological zero-deleted kernel.
[C405](Yin_C_G0405_v1.md#salem-strip-all-power-essential-norm) and [C673](Yin_C_G0673_v1.md#statement) supply the existing translation mechanism and its paid chronological/Doob limits; the exact finite-word comparison required here is written out below.
The bounded reuse search retained in the extraction source examined radial envelopes, angular supersolutions, polynomially weighted candidates and supercritical H ratios without finding this candidate-class statement in the existing materials.
This is a substantive project deduction, not a priority claim.
No new source theorem or native computation is a premise.

## Complete argument

### Whole returned words give a paid tail endpoint comparison

Put v=beta+beta^(-1)-2 and tau=(3+sqrt13)/2.
C790 proves v is an actual unit in O, with

    v_+=v_-=tau^(-1),  v(zeta)=-tau.

For integers k>=1 take h_k=v^(2k).
Then

    (h_k)_+=(h_k)_-=tau^(-2k),
    h_k(zeta)=tau^(2k),  rho(h_k)=tau^(2k).              RE2

Fix an integer n>=1 BEFORE letting k grow.
Let A_n be the finite set of all states on ALL original zero-to-zero words of length n, including both endpoints.
The all-zero word shows that A_n is nonempty.
Every member is in the actual strict core D.
This uses a finite word set of at most3^n words, without computing or truncating any of it.
Define the positive exact margin and finite exclusion radius

    delta_n=min_(y in A_n){B-|y_+|, S-|y_-|}>0,
    M_F=max_(y in F)rho(y).

For any such original word with chronological states x_j,0<=j<=n, its translate from h_k has states

    y_j=x_j+beta^j h_k.                                 RE3

They obey the SAME digit recursion and have the SAME complete word probability.
If

    beta^n tau^(-2k)<delta_n,
    tau^(2k)>M_F+n,                                    RE4

then all y_j satisfy both strict real bounds and belong to D.
Indeed their expanding-coordinate changes are at most beta^n tau^(-2k), and their contracting-coordinate changes are at most tau^(-2k).
Also rho(x_j)<=j<=n, while |(beta^j h_k)(zeta)|=tau^(2k), so rho(y_j)>=tau^(2k)-n>M_F.
Thus EVERY translated intermediate state avoids F, including zero.
These are genuine actual-core paths, not points in an unproved enlarged strip.
For each fixed n, conditions RE4 hold for all sufficiently large k.

Let B_F be P_D restricted to D minus F.
Dropping further nonnegative terms in RE1 gives t B_F W<=W there, so finite-row iteration yields t^n B_F^n W<=W.
Every translated returned word ends at beta^n h_k.
Different original digit words remain different paths, and their probabilities sum to the COMPLETE p_n.
Consequently

    B_F^n(h_k,beta^n h_k)>=p_n,
    t^n p_n W(beta^n h_k)<=W(h_k),
                        all sufficiently large k for each fixed n. RE5

All iterated sums have at most3^n paths and finite W values; no infinite integrability assumption is used.
The translated paths are OPEN: their two endpoints differ for n>=1.
No rooted closed-loop weight, entrance probability, count of freely available copies or stationary mass is inferred from this comparison.
The growth of the required k and radius with n is not discarded; RE5 first fixes n and then takes sufficiently large k, consistently with C673's chronological geometric expense.

### Arbitrary radial envelopes with bounded central angular distortion fail

Suppose there are an epsilon>0, r_*>0, constants 0<c<=C<infinity and ANY function a:[r_*,infinity)->(0,infinity) such that

    c a(rho(x))<=W(x)<=C a(rho(x))                      RE6

for every x in D minus{0} with |x_+|,|x_-|<=epsilon and rho(x)>=r_*.
There is no monotonicity, polynomial-growth, continuity or differentiability hypothesis on a.
No restriction on W at other states is added to RE1.

For each fixed n, both h_k and beta^n h_k enter the real neighborhood in RE6 for all sufficiently large k.
Crucially their neutral radii are EXACTLY equal for every n,k:

    rho(beta^n h_k)=|zeta^n|rho(h_k)=tau^(2k).            RE7

Thus the arbitrary radial factor cancels, giving W(h_k)/W(beta^n h_k)<=C/c.
Applying RE5 for each n gives t^n p_n<=C/c for EVERY n>=1.
Taking nth roots and using p_n^(1/n)->1/R proves

    RE1 and RE6 imply t<=R.                            RE8

Hence no function in this class can give a zero-deleted supersolution at t>R, even after an arbitrary finite repair.
This is the actual outcome of the candidate test, not another unverified sufficient condition for the mean.

In particular consider the explicit radius-angle ansatz

    W(x)=a(rho(x))G(x_+,x_-,x(zeta)/rho(x))             RE9

on sufficiently large-radius states whose real coordinates are in a neighborhood U of(0,0).
Assume G:U times S^1 ->(0,infinity) is continuous; elsewhere W may be arbitrary positive finite values.
Choose a closed square[-epsilon,epsilon]^2 contained in U.
Its product with S^1 is compact, so continuity and strict positivity give a finite maximum C and a strictly positive minimum c for G there.
These constants do NOT depend on n or k, and RE6 follows.
Thus RE8 excludes every such candidate for t>R, allowing ANY positive radial a, including exponentially varying or decreasing choices.

More explicitly, the endpoint angles are1 and zeta^n, and the two-real coordinates are respectively(tau^(-2k),tau^(-2k)) and(beta^n tau^(-2k),beta^(-n)tau^(-2k)).
For fixed n their G ratio tends to G(0,0,1)/G(0,0,zeta^n), uniformly bounded in n by the same compact-circle extrema.
The cancellation of a in RE7 is exact BEFORE this limit.
No angular equidistribution theorem, root-of-unity approximation rate or uniform choice of k across n is required.

### Actual critical and supercritical harmonic consequences

For the genuine critical H=H_R and Q_0, put V=W/H on D minus{0}.
The actual path-weight definition gives, without replacing H,

    Q_0 V(x)=R B_0 W(x)/H(x).

A proposed uniform multiplicative drift Q_0 V<=q V outside finite F with 0<q<1 would imply RE1 at t=R/q>R.
It is therefore impossible when W has RE6, in particular RE9.
This rules out a concrete H-sensitive radial-angular candidate of that form.
It does not cover the C593 square-root-affinity candidate, an additive/nonuniform drift, or irregular arithmetic dependence violating RE6.

There is also an exact necessary constraint if the strict-radius branch R_f>R is true.
Fix R<t<R_f.
C511 constructs the ACTUAL first-hit function

    H_t(x)=sum_(original first-hit words x to0) p(w)t^|w|,
    H_t(0)=1,

finite and strictly positive on D, with H_t=t P_D H_t off zero.
Hence t B_0 H_t<=H_t, so RE5 gives

    H_t(h_k)/H_t(beta^n h_k)>=t^n p_n,
                       all sufficiently large k for each fixed n. RE10

Since(t^n p_n)^(1/n)->t/R>1, these same-radius ratios are unbounded as n grows, with k taken large after n.
For every prescribed ratio bound, central real neighborhood and neutral-radius lower threshold, RE10 supplies actual endpoint pairs violating that ratio bound, lying in the neighborhood and beyond the threshold, with identical neutral radius.
Thus any such actual supercritical H_t must fail RE6 for EVERY positive radial envelope; it cannot have the positive continuous leading factor in RE9.
This is a conditional constraint on the canonical original H_t, not a constructed alternative law or a claim that H_t exists beyond R.

RE8--RE10 exclude the tested class of certificates and identify the oscillation a successful strict-radius branch would need to accommodate.
They do not prove R_f=R, infinite mu, finite mu, an exponential-tail lower bound from a fixed starting state, or linear bridge-level growth.
C852's uniform Hilbert-space obstruction remains separate and was not used to infer any entrywise decay rate.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-27)

## Assessment history

### Decision radial-envelope-open

| Field | Value |
| --- | --- |
| date | 2026-10-27T00:42 |
| status | open |
| reason | Fix the complete author argument RE1--RE10 for the exact original-law candidate-class exclusion and the conditional canonical first-hit ratio constraint. Whole independent review and responsible adoption remain outstanding; no critical-mean or strict-radius branch is classified. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire fixed quartic/original-law domain, all finite exceptions and pointwise finite positive W, exact fixed-n then large-k comparison, arbitrary positive radial envelope and continuous angular specialization, actual H-sensitive drift exclusion, conditional canonical H_t ratio quantifiers and all exclusions. |
| argument | [Complete RE1--RE10 argument](#complete-argument) | Actual unit embeddings, uniform strict-core margins for all returned words, every intermediate translated state outside F, full weights and finite-row iteration, exact same-radius cancellation, compact positive continuous factor, true critical Doob identity and actual supercritical first-hit consequence. |
| dependency | [Actual strict core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Fixed quartic actual accessible/coaccessible core equals the displayed strict strip, with the retained C399 certificate scope; no arbitrary Salem extension. |
| dependency | [Actual balanced unit](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26) | Actual O-unit v and its exact two real and neutral conjugates; no use of counting lower bounds as probability lower bounds. |
| dependency | [Complete original return root limit](Yin_C_G0555_v1.md#decision-isolated-whole-review-adoption-20261022) | Full p_n, true R and p_n^(1/n)->1/R under the unchanged iid law, equivalent to the chronological returned-word sum; no truncated finite graph. |
| dependency | [Canonical first-hit family](Yin_C_G0511_v1.md#decision-complete-current-self-adoption) | Finite positive actual H_t and off-zero t-harmonicity for every 0<t<R_f; supercritical use is explicitly conditional on R<t<R_f. |
| dependency | [Actual critical H and Q](Yin_C_G0805_v1.md#decision-whole-reviewed-2026-10-26) | Finite positive H_R and actual original-weight stochastic Doob kernel Q; no mean normalization or operator-power inference. |

### Decision whole-reviewed-2026-10-27

| Field | Value |
| --- | --- |
| date | 2026-10-27T00:51 |
| status | proved |
| reason | Adopt the unchanged complete fixed-quartic statement and RE1--RE10 after main-agent whole claim/finding reading and the separate whole independent R1047. Exact actual-core translation retains every returned-word weight and avoids each finite exception at every intermediate time; equal neutral radii cancel an arbitrary positive radial factor, yielding t<=R and the stated compact-angular specialization. The actual critical drift exclusion and conditional canonical H_t same-radius ratio quantifiers are established at their declared adopted-input scope. No strict-radius or finite/infinite-mean branch, fixed-start tail or unrestricted Task conclusion is decided. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire fixed quartic/original-law domain, all finite exceptions and pointwise finite positive W, exact fixed-n then large-k comparison, arbitrary positive radial envelope and continuous angular specialization, actual H-sensitive drift exclusion, conditional canonical H_t ratio quantifiers and all exclusions. |
| argument | [Complete RE1--RE10 argument](#complete-argument) | Actual unit embeddings, uniform strict-core margins for all returned words, every intermediate translated state outside F, full weights and finite-row iteration, exact same-radius cancellation, compact positive continuous factor, true critical Doob identity and actual supercritical first-hit consequence. |
| dependency | [Actual strict core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Fixed quartic actual accessible/coaccessible core equals the displayed strict strip, with the retained C399 certificate scope; no arbitrary Salem extension. |
| dependency | [Actual balanced unit](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26) | Actual O-unit v and its exact two real and neutral conjugates; no use of counting lower bounds as probability lower bounds. |
| dependency | [Complete original return root limit](Yin_C_G0555_v1.md#decision-isolated-whole-review-adoption-20261022) | Full p_n, true R and p_n^(1/n)->1/R under the unchanged iid law, equivalent to the chronological returned-word sum; no truncated finite graph. |
| dependency | [Canonical first-hit family](Yin_C_G0511_v1.md#decision-complete-current-self-adoption) | Finite positive actual H_t and off-zero t-harmonicity for every 0<t<R_f; supercritical use is explicitly conditional on R<t<R_f. |
| dependency | [Actual critical H and Q](Yin_C_G0805_v1.md#decision-whole-reviewed-2026-10-26) | Finite positive H_R and actual original-weight stochastic Doob kernel Q; no mean normalization or operator-power inference. |
| review | [Whole independent radial-envelope review](../audits/reviews/Yin_R_G1047_v1.md#whole-radial-envelope-finding) | Entire statement and RE1--RE10, all five adopted interfaces and bounded upstream scope traces; exact quantifiers, original path weights, positive finite-row iteration, equal-radius cancellation and conditional actual first-hit consequences checked. |

