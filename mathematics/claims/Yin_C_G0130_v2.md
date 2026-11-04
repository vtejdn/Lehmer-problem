---
author: Yin
---
# Original polynomial coverage beyond admissible residue inventories

Date: 2026-10-15.
Human author Yin.
Root assigns f_unitary_scope an author inquiry on actual arithmetic coverage.
This is separate from g_bridge_audit's arbitrary-thinning combinatorial inquiry; no proof advice is sent to that author.
No native program or J is allocated.

## Responsible question

Can the arithmetic of an ACTUAL monic irreducible nontorsion integer-unit polynomial force a good-prime original-root inventory with positive triple density, positive retained Euler-layer mass, or another affordable common-exponent income?
Alternatively, can it contradict the jointly required escapes in C116 and C124 by an original polynomial invariant?
Keep the original degree, full signed resultants, actual prime size and time, Frobenius orbit divisibility, and all height/discriminant costs.
Abstract phi capacities or finite-field realizations are not near-one integer inputs.

## Initial exact inputs and reuse scope

Read C116's full original-prime budget and its subpolynomial-prime/intermediate-collision consequences, C124's pointwise and global terminal-support capture with fixed-threshold escape, C127's complete Euler-layer and retained-thinning theorem, L159's actual Frobenius/inversion capacities and explicit finite-field-versus-integer boundary, and L209's growing-prime/residue-degree escape.
These are starting interfaces, not claimed automatic coverage.

A first bounded local search identifies L75's Chebotarev/discriminant cost and L160's inversion-matched Frobenius mechanism as mandatory comparisons before any least-prime or reciprocal matching attempt.
The source search and exact subsequent discriminator will be retained below.
No new proposition or inference from necessary conditions is asserted at allocation.
Substantive derivations and useful failed attempts will be developed in this responsible material.

## 1. Exact initial failures and changed arithmetic discriminator

L75 already compares generic effective Chebotarev bounds with the necessary original-degree period budget and retains the full splitting-field degree/discriminant.
L160 already turns Frobenius conjugate to complex conjugation into an inversion-matched common return, distinguishes matching from unlabelled cycle type, and leaves the affordable least-prime condition open.
Neither route is reproved here.
C116/C124/C127 remain sufficient capture interfaces conditional on original coverage; L209 gives necessary residue-degree escape and cannot be inverted into density.

The first exact-term search for Selmer, trace-one, Artin--Schreier and subgroup intersections found L32's existing bounded-Mahler all-power-preserving trinomial-factor family, but no corresponding modular return count in the inspected G Claims/ledgers.
An initial Windows wildcard-path invocation failed before searching; the corrected search used explicit directory roots and G-file globs.
Local literature contents/registry and source units did not supply the proposed modular estimate.
A bounded external primary search found Selmer's original publisher record and Conrad's authored exposition of the irreducibility theorem; the direct original-PDF endpoint returned404.
Irreducibility of the whole trinomial is NOT needed and is not adopted.
The accepted L32 minimal-factor construction suffices.
A further trace/norm/affine-line subgroup screen found related finite-field material but no exact adopted theorem for this application.
No novelty or exhaustive-search claim is made.
The elementary field identities used below are proved directly, within the same finite-field algebra already used in L159; no character-sum theorem is used.

The useful changed question is whether even an actual irreducible unit, bounded TOTAL Mahler measure, all-power degree preservation, good reduction and logarithmic residue degrees can guarantee short-order coverage at a specified small good prime.
The following exact construction answers that stronger proposed shortcut negatively.
It does not construct near-one inputs or obstruct choosing a different prime.

<a id="statement"></a>
## Exact bounded result

For every rational prime ell and integer r>=1 with q=ell^r>=3, let P_q be the actual minimal polynomial of the positive real root of t^q-t-1, and d_q its original degree.
Reuse theta0 and kappa from L32 as in(B).
Then P_q is an irreducible nonreciprocal nontorsion integer-unit polynomial with theta0<=M(P_q)<=sqrt3, kappa(q-1)<d_q<=q, and every positive power preserving degree.
The specified ell is good for P_q.

At that prime its complete original order groups satisfy the finite bounds(A)--(F): in particular H_X<=sqrt(ell X) and T_X<=ell^(3/2)X^(5/2) for all integer X>=1.
EVERY selection of complete groups with W>=gamma d_q satisfies(F) at X<=C d_q.
Thus for fixed ell,C,gamma>0, no such selection has uniformly positive triple density as r grows, and its capture fraction tends to zero even at every fixed enlargement of the original linear time.
This is failure at the specified prime ell, not at every prime simultaneously.

For ell2 and q>=4, all original binary depths are exactly(I), the full signed original norm has the exact binary valuation(J), and its uniform bound(K)--(L) tends to zero after division by d_q at every fixed linear time.
No odd-prime depth equality is claimed.
All other-prime norm contributions are left uncontrolled.

The construction is uniformly separated from measure1 by theta0 and is nonreciprocal.
It therefore refutes only the stated broader coverage shortcuts, not any sufficiently-small-total-measure or reciprocal-specific hypothesis, the unrestricted Mahler gap, or existence of a useful different prime.
There is no assertion that the whole trinomial is irreducible or that d_q=q.
No native computation supplies these results.

<a id="argument"></a>
<a id="translation-root-subgroup-bound"></a>
## 2. Translation-Frobenius roots have few short multiplicative returns

Let ell be a rational prime, r>=1 and q=ell^r.
In an algebraic closure of F_ell let

    R_q={z:z^q=z+1}.

The polynomial z^q-z-1 has derivative-1, so R_q has exactly q distinct nonzero elements.
Iterating the defining relation gives z^(q^j)=z+j for all integers j>=0, with j interpreted in F_ell.
In particular z^(q^ell)=z, so all roots lie in F_(q^ell).
None lies in F_q.

For ANY integer n>=1 put

    h_q(n)=#{z in R_q:z^n=1},
    M_n=gcd(n,q^ell-1),
    S=(q^ell-1)/(q-1),
    a=gcd(M_n,q-1), b=gcd(M_n,S).

Since S=1+q+...+q^(ell-1), gcd(S,q-1)=gcd(ell,q-1)=1.
Thus M_n=ab with a|q-1 and b|S.
The n-th roots in F_(q^ell)^* form its subgroup H of order M_n.
The following finite bound holds:

    h_q(n)<=min(ell*a,b-1)<=sqrt(ell*M_n)<=sqrt(ell*n).   (A)

Here is the full argument.
The group homomorphism z->z^S on H has image size M_n/gcd(M_n,S)=a.
On a translation root,

    z^S=product_(i=0)^(ell-1)z^(q^i)
        =product_(i=0)^(ell-1)(z+i)=z^ell-z.

The last polynomial identity follows because both sides are monic degree ell with the elements of F_ell as their distinct roots.
For each of the a possible image values, the polynomial equation z^ell-z=c has at most ell solutions.
This proves h_q(n)<=ell a.

The other homomorphism z->z^(q-1) on H has image size M_n/gcd(M_n,q-1)=b.
For a translation root its value is1+1/z, which is an injective function of z and never1.
At most b-1 possible image elements can therefore occur, proving the second bound.
Finally min(ell a,b-1)<=sqrt(ell a(b-1))<=sqrt(ell ab), including b1 when both sides of the first inequality are zero.
This proves(A).
It uses no distributional or random-root assertion.

The estimate is valid for an arbitrary subset of R_q as well.
In particular it remains an upper bound for roots of a selected integer factor after good reduction; it does not require that factor to contain every translation root.

<a id="actual-trinomial-fixed-prime-control"></a>
## 3. An actual bounded-total-Mahler family, without a new irreducibility input

Reuse exactly the [retained original L32 construction](Yin_C_G0239_v1.md#power-stable-many-expanding-control).
For q=ell^r>=3 let alpha_q>1 be the positive real root of

    F_q(t)=t^q-t-1,

and let P_q be its ACTUAL monic minimal polynomial over Q, of degree d_q.
Put theta0>1 equal to the plastic constant from the accepted nonreciprocal theorem and kappa=log(theta0)/log2>0.
L32 proves, without assuming F_q irreducible,

    P_q in Z[t], P_q(0)=+/-1, P_q irreducible nonreciprocal,
    theta0<=M(P_q)<=sqrt3,
    kappa(q-1)<d_q<=q,                                  (B)

and every positive power of alpha_q preserves its degree.
The lower degree bound follows from L32's count of expanding conjugates; no claimed equality d_q=q is needed.
Its use retains L32's accepted Smyth statement/applicability boundary.
Nontorsion follows already from alpha_q>1.

Because P_q is a monic integer divisor of F_q, its reduction modulo ell is a monic divisor of t^q-t-1.
The latter has derivative-1.
Its distinct nonzero roots force P_q modulo ell to have d_q distinct nonzero roots.
Therefore ell does not divide disc(P_q): it is genuinely a GOOD prime for the actual minimal polynomial, not merely a prime unramified in another field.
Every original reduced root lies in R_q.

For the complete actual order inventory w_o at ell, define

    W=d_q,
    h(n)=sum_(o|n)w_o,
    H_X=max_(1<=n<=X)h(n),
    T_X=sum_(lcm(o1,o2,o3)<=X) w_o1*w_o2*w_o3.

All sums use complete original root groups and ordered repeated triples.
They have the exact L159 Frobenius divisibility and phi capacities.
No abstract array is inserted.
By(A),

    h(n)<=sqrt(ell*n),
    H_X<=sqrt(ell*X)                                    (C)

for every integer X>=1.
In particular for every fixed C>0 and B>=1 with floor(BC d_q)>=1,

    H_(floor(BC d_q))/d_q<=sqrt(ell*BC/d_q).             (D)

When ell is fixed and r->infinity, this tends to zero at EVERY fixed enlarged linear window.
This controls the actual first-layer peak at the chosen good prime.
It does not upper-bound exceptional local valuation depths or the entire integer norm.

<a id="actual-translation-triple-vanishing"></a>
## 4. A direct original triple-density bound, with no analytic kernel input

For ANY complete order inventory and integer X>=1, each compatible ordered triple has lcm L<=X and is counted at least once in sum_(n=1)^X h(n)^3, namely at n=L.
Expanding the cube gives exactly its weight times floor(X/L).
Thus

    T_X<=sum_(n=1)^X h(n)^3.

Apply(C), then the elementary sum bound n^(3/2)<=X^(3/2):

    T_X<=ell^(3/2) X^(5/2),
    T_X/d_q^3<=ell^(3/2) C^(5/2)/sqrt(d_q)
                    whenever1<=X<=C d_q.                (E)

This tends to zero for each fixed ell,C as r grows.
There is no unproved universal short-pair estimate, C101/GW21 constant, divisor-function asymptotic or mixing assumption in this calculation.

For any selection of COMPLETE actual order groups of mass W>=gamma d_q with fixed gamma>0, its triple mass is at most that of the full inventory.
Hence, at the SAME original X<=C d_q,

    T_selected(X)/W^3
       <=ell^(3/2) C^(5/2)/(gamma^3 sqrt(d_q)).           (F)

Its peak is likewise at most the full H_X.
Explicitly, at every fixed enlargement with floor(BCd_q)>=1,

    H_selected(floor(BCd_q))/W
       <=gamma^(-1)sqrt(ell*BC/d_q).                    (F2)

Thus no fixed-positive-mass selection can restore positive density or proportional capture at this prescribed good prime.
The bound also records its possible varying-prime domain: it tends to zero whenever ell^3/d_q->0 with C,gamma fixed.
For example q=ell^r with any fixed integer r>=4 has this property as ell->infinity by(B).
This is a stated sufficient range, not a sharp cutoff.

<a id="translation-control-coverage-scope"></a>
## 5. What the actual control changes and what remains open

All residue roots lie in F_(q^ell)=F_(ell^(r ell)), so every actual irreducible residue factor has degree dividing r ell.
Since d_q>kappa(q-1), this is O_ell(log d_q) for fixed ell.
Nevertheless(C)--(F) show vanishing short-return peak and triple density at every fixed linear time scale.
Merely bounding residue degrees by a constant multiple of log d is therefore insufficient for the desired common-exponent coverage, even with genuine good reduction, original integer-unit roots, bounded TOTAL Mahler measure and all-power degree preservation.
This assertion is about a chosen fixed good prime, not the existence of some favorable prime.

This is materially different from the abstract finite-field capacity realizations and the known CRT controls with total measure of order d.
It reuses the already accepted L32 family but proves its previously unrecorded modular return obstruction.
It does not claim a new family of small measures: log M(P_q)>=log theta0 uniformly, and P_q is nonreciprocal.
Consequently it neither contradicts L209's hypothetical near-one residue escape nor refutes any C116/C124/C127 conditional capture theorem.
Here their requisite positive density at the selected prime fails explicitly.
No terminal-support escape is inferred from C124 without that premise.

The positive arithmetic mechanism sought in the responsible question is still missing.
A successful coverage argument must exploit more than bounded Mahler, original Frobenius orbit legality and logarithmic residue degree, and must either choose a different prime or use small-TOTAL-measure/reciprocal structure unavailable in this control.
The exact root relation z^q=z+1 gives additive Frobenius structure but forces poor multiplicative return counts; additive structure alone cannot be read as short multiplicative periods.
No other-prime coverage obstruction, near-one realization, uniform gap or zero-gap sequence has been proved in this round.

<a id="binary-translation-exact-depths"></a>
## 6. At the fixed prime2 even all exceptional depths are excluded

Now specialize to ell=2, q=2^r>=4 and the SAME actual minimal polynomial P_q.
All roots of F_q lift to an unramified finite extension E/Q_2 because F_q modulo2 is squarefree.
This is the existing [retained original L64 simple-root/unramified Frobenius interface](Yin_C_G0241_v1.md#direct-etale-frobenius-lift), together with [L74's original norm accounting](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm), not a hypothesis that the global splitting field is unramified at every prime.
Let O_E be its ring of integers, v(2)=1, and sigma the arithmetic Frobenius automorphism, so sigma(u) reduces to u^2 modulo2.
It fixes rational integers.
For any original root alpha of P_q let o be its residue multiplicative order; o is odd.

We claim that BOTH first signed depths are exactly one:

    v(alpha^o-1)=v(alpha^o+1)=1.                         (G)

The following elementary congruence observation supplies the necessary modulo4 uniqueness.
If units u,v have the same nonzero residue and u^o=v^o modulo4 with o odd, then

    u^o-v^o=(u-v)sum_(j=0)^(o-1)u^(o-1-j)v^j

has a second factor reducing to the nonzero value o*bar(u)^(o-1).
Thus u=v modulo4.
In particular, if beta^o=1 modulo4, both sigma(beta) and beta^2 have o-th power1 modulo4 and the same residue, so

    sigma(beta)=beta^2 modulo4.                          (H)

Suppose first alpha^o=1 modulo4.
Equation(H) gives sigma(alpha)=alpha^2 modulo4.
Apply sigma to the exact equation alpha^q-alpha-1=0 and reduce modulo4.
It would imply

    0=alpha^(2q)-alpha^2-1
      =(alpha+1)^2-alpha^2-1=2alpha modulo4,

which is impossible because alpha is a unit and E is unramified.

Suppose instead alpha^o=-1 modulo4.
Then beta=-alpha obeys beta^o=1 modulo4, since o is odd.
Equation(H) gives sigma(alpha)=-alpha^2 modulo4.
Since q is even, applying sigma to the same exact relation would imply

    0=alpha^(2q)+alpha^2-1
      =(alpha+1)^2+alpha^2-1=2alpha(alpha+1) modulo4.

This too is impossible: alpha is a unit and alpha+1=alpha^q is a unit.
Both alpha^o-1 and alpha^o+1 are divisible by2, so the exclusions prove(G).
This is a direct modulo4 argument; no independence, generic non-Wieferich assertion or unproved equality of initial depths is used.

For n not divisible by o, v(alpha^n-1)=0.
If n=o*t*2^k with t odd, the odd geometric sums preserve both signed depths in(G).
The first square therefore has depth2.
At depth a>=2, x+1 has depth1 whenever x-1 has depth a, so each further square increases the depth by exactly1.
Consequently for EVERY n>=1,

    v(alpha^n-1)=(1+v_2(n))*1_(o divides n).              (I)

Sum this identity over ALL d_q original roots in the full signed norm

    D_n=Res(P_q,t^n-1)
       =Norm_(Q(alpha_q)/Q)(alpha_q^n-1), C_n=|D_n|.

The chosen unramified valuation restricts to the ordinary rational2-adic valuation, so, without another residue-degree factor,

    v_2(C_n)=(1+v_2(n))*h(n).                           (J)

This is the exact full binary depth formula; the initial first-layer-only warning after(C) is superseded ONLY in this binary specialization.
No analogous equality for odd ell is asserted.

Every residue order is odd, hence for k=v_2(n) and t=n/2^k one has h(n)=h(t).
Combining(J) and(A) at ell2 gives

    v_2(C_n)<=(k+1)sqrt(2n/2^k)
             <=(3/2)sqrt(2n).                           (K)

Indeed the maximum of (k+1)2^(-k/2) over integers k>=0 is3/2 at k2: direct checks cover k0,1,2, and the ratio of successive terms is at most(4/3)/sqrt2<1 for k>=2.
Thus, for EVERY fixed C>0 and each q with floor(C*d_q)>=1 (automatically for all sufficiently large r),

    max_(1<=n<=floor(Cd_q))[(log2)v_2(C_n)/d_q]
          <=(3log2/2)sqrt(2C/d_q) ->0.                  (L)

All original roots and every binary valuation layer have now been paid, including exceptional first-squaring possibilities (which(G) excludes).
This is stronger than a first-layer inventory failure at2.
It still gives no upper bound on contributions of OTHER rational primes, on the total log C_n, or on possible certificates using a different auxiliary or prime.
The signed norm is retained before its absolute value; no subnorm or changed degree is used.

The modulo4 observation was recognized as related to Teichmuller lifting.
A bounded primary check read Bill Casselman's author note, *Witt vectors*, revision12April2018, Section2/Proposition2.1 on printedp3 and its preceding unramified-extension statement (https://personal.math.ubc.ca/~cass/research/pdf/Witt.pdf).
It identifies the standard unramified Frobenius and multiplicative representative mechanism; it is attribution/background, not a new imported theorem for(H), whose complete congruence proof is above.
No full Witt-vector proof audit or source theorem beyond the already accepted unramified interface is claimed.
The direct binary-depth argument and exact maximum in(K) are current author contributions; root has supplied only scope/quantifier requests.

## Direct dependencies and self-check boundary

The original-family facts and uniform degree comparison are exactly L32#power-stable-many-expanding-control, retaining its accepted nonreciprocal Smyth input and its recorded review relationship.
L159#good-prime-short-order-capacity identifies the actual complete root counts and finite-field cyclic groups; its separate abstract realization is not used.
L64#direct-etale-frobenius-lift supplies the existing unramified lift/Frobenius facts; L74#content-versus-ideal-norm supplies the full original norm valuation convention.
The trace/norm subgroup counting, triple bound, both modulo4 exclusions and exact binary-depth estimate are proved in the present original.
C116/C124/C127/L209/L75/L160 are comparisons and research motivation, not theorem premises for(A)--(L).
Casselman is checked standard-mechanism attribution only.
Selmer's full-trinomial irreducibility is not an input.

The author checked all finite fields and subgroup kernels/images, gcd(S,q-1), b1, ell2 and q>=3 restrictions, the distinction between F_q and its actual factor P_q, degree comparability rather than degree equality, preservation of good reduction under taking that factor, original complete-group normalization and every W>=gamma d_q selection, all integer times and fixed enlargement constants, the ordered-triple overcount, the varying-prime sufficient range, residue-degree divisibility, both signed modulo4 exclusions, unramified valuation normalization, odd-power and first-squaring steps, the exact maximizer k2, and full original signed norms.
This is contributing self-review, not independent evidence or Claim adoption.
The author has not bounded other-prime contributions or proved actual near-one coverage.

<a id="translation-control-entire-author-freeze"></a>
## Entire author freeze

2026-10-15T08:57.
The f_unitary_scope author freezes this ENTIRE original, including its responsible question and unsuccessful automatic-coverage direction, exact statement, Sections1--6, equations(A)--(L) and(F2), complete group/finite-field/binary-depth proofs, full original-polynomial degree/norm costs, source/reuse limits and contributing self-check.
Root requested the exact chosen-prime versus all-primes and full-group selection distinctions but supplied no proof step.
No independent review, Claim adoption or new positive coverage theorem is asserted.
No native mathematical program was run.


## Revision scope

2026-10-15T09:10.
Preserve v1 and its reviewed finite-domain finding.
Version2 adds only floor(C*d_q)>=1 to formula(L); for each fixed C this holds eventually because d_q tends to infinity.
All other proofs and formulas and the final asymptotic conclusion are unchanged.
strategy_critique identified the boundary and f confirmed it.
Actual separate reinspection remains pending.

## Fixed organization

The entire frozen author account is retained without mathematical abridgment.
The complete actual bounded-total-Mahler trinomial-factor family, finite-field return bound, all linear-mass complete selections, specified-good-prime coverage failure and full binary local-depth calculation.
Nonreciprocal and uniformly positive measure; other primes and the near-one class are not controlled.
Root supplied the inquiry and quantifier requirements, without a finite-field or depth proof step.
Actual fixed whole independent review is pending.

## Current assessment
[Selected decision](#decision-isolated-current-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T09:10 |
| status | open |
| reason | Repair only the finite nonempty-window domain of formula L, preserving the prior version and all original proofs and scope. Actual whole review of this version remains pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual fixed-prime control](#statement) | All A--L and F2 with the explicit nonempty finite window in L. |
| argument | [Complete finite-field and depth proof](#argument) | Entire original argument, precise source scope and unchanged final asymptotic consequence. |
| dependency | [Actual minimal-factor family](../ledger/Yin_L_G0032_v1.md#power-stable-many-expanding-control) | Original degree, total Mahler measure and all-positive-power degree preservation. |
| dependency | [Actual root inventory](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete good-prime order-group conventions and capacities, not abstract realization. |
| dependency | [Unramified Frobenius](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Existing good-prime unramified lift and Frobenius interface for the local modulo4 proof. |
| dependency | [Full original norm](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Original field, full-root norm and normalized local-depth convention. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T09:16 |
| status | proved |
| reason | Adopt [R798 original translation-v2](../audits/reviews/Yin_R_G0798_v1.md#translation-v2-whole-independent-finding) actual whole v2 finding. The original minimal-factor family has vanishing chosen-good-prime linear-time density and capture, including every complete linear-mass selection; the binary specialization pays every local valuation depth. Formula L now has its necessary finite nonempty-window guard. Preserve v1 and its precise finding. Other primes, near-one reciprocal coverage and the unrestricted goal remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual fixed-prime control](#statement) | All A--L and F2 with the explicit nonempty finite window in L. |
| argument | [Complete finite-field and depth proof](#argument) | Entire original argument, precise source scope and unchanged final asymptotic consequence. |
| dependency | [Actual minimal-factor family](../ledger/Yin_L_G0032_v1.md#power-stable-many-expanding-control) | Original degree, total Mahler measure and all-positive-power degree preservation. |
| dependency | [Actual root inventory](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete good-prime order-group conventions and capacities, not abstract realization. |
| dependency | [Unramified Frobenius](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Existing good-prime unramified lift and Frobenius interface for the local modulo4 proof. |
| dependency | [Full original norm](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Original field, full-root norm and normalized local-depth convention. |
| review | [Actual v2 whole independent finding](../audits/reviews/Yin_R_G0798_v1.md#translation-v2-whole-independent-finding) | Entire corrected fixed proof, all A--L/F2, source scope and original complete norm; v1 finite-domain finding remains separately preserved in the same review. |


### Decision current-control-and-local-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:54 |
| status | proved |
| reason | Select the complete retained original minimal-factor and unramified-lifting proofs at their current C239/C241 homes; statement, full argument, source limits, assessment and actual original [R798 original translation-v2](../audits/reviews/Yin_R_G0798_v1.md#translation-v2-whole-independent-finding) finding are unchanged. This maintenance adds no independent review or unrestricted-goal conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual fixed-prime control](#statement) | All A--L and F2 with the explicit nonempty finite window in L. |
| argument | [Complete finite-field and depth proof](#argument) | Entire original argument, precise source scope and unchanged final asymptotic consequence. |
| dependency | [Actual minimal-factor family](Yin_C_G0239_v1.md#power-stable-many-expanding-control) | Original degree, total Mahler measure and all-positive-power degree preservation. |
| dependency | [Actual root inventory](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete good-prime order-group conventions and capacities, not abstract realization. |
| dependency | [Unramified Frobenius](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Existing good-prime unramified lift and Frobenius interface for the local modulo4 proof. |
| dependency | [Full original norm](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Original field, full-root norm and normalized local-depth convention. |
| review | [Original actual v2 whole finding](../audits/reviews/Yin_R_G0798_v1.md#translation-v2-whole-independent-finding) | Entire corrected fixed proof, all A--L/F2, source scope and original complete norm; v1 finite-domain finding remains separately preserved in the same review. |

### Decision current-original-norm-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:48 |
| status | proved |
| reason | Select C256 as the complete current responsible home for the identical original L74 norm interface at the same exact anchor and unchanged relation scope below. The complete retained L74 proof and current extraction were checked for full original-field/root multiplicities and exact local-depth conventions. This is same-content locator adoption: selected statement, argument, actual review finding, all other dependencies and mathematical status remain unchanged. Historical decisions and R bindings keep their actual fixed L74 inputs. No original R input, native result or execution is reassigned. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual fixed-prime control](#statement) | All A--L and F2 with the explicit nonempty finite window in L. |
| argument | [Complete finite-field and depth proof](#argument) | Entire original argument, precise source scope and unchanged final asymptotic consequence. |
| dependency | [Actual minimal-factor family](Yin_C_G0239_v1.md#power-stable-many-expanding-control) | Original degree, total Mahler measure and all-positive-power degree preservation. |
| dependency | [Actual root inventory](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete good-prime order-group conventions and capacities, not abstract realization. |
| dependency | [Unramified Frobenius](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Existing good-prime unramified lift and Frobenius interface for the local modulo4 proof. |
| dependency | [Full original norm](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Original field, full-root norm and normalized local-depth convention. |
| review | [Original actual v2 whole finding](../audits/reviews/Yin_R_G0798_v1.md#translation-v2-whole-independent-finding) | Entire corrected fixed proof, all A--L/F2, source scope and original complete norm; v1 finite-domain finding remains separately preserved in the same review. |

### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:28 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | All A--L and F2 with the explicit nonempty finite window in L. |
| argument | [Exact retained argument](#argument) | Entire original argument, precise source scope and unchanged final asymptotic consequence. |
| dependency | [Exact retained dependency](Yin_C_G0239_v1.md#power-stable-many-expanding-control) | Original degree, total Mahler measure and all-positive-power degree preservation. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete good-prime order-group conventions and capacities, not abstract realization. |
| dependency | [Exact retained dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Existing good-prime unramified lift and Frobenius interface for the local modulo4 proof. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Original field, full-root norm and normalized local-depth convention. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0798_v1.md#translation-v2-whole-independent-finding) | Entire corrected fixed proof, all A--L/F2, source scope and original complete norm; v1 finite-domain finding remains separately preserved in the same review. |


### Decision isolated-current-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:50 |
| status | proved |
| reason | Adopt the new isolated R798 whole finding for this exact highest physical statement and complete argument, after necessary fixed-mathematics/source inspection and subsequent comparison with all original review accounts. Preserve the complete current mathematical status, input relations and scopes, all original costs and open coverage limits. R798 separately retains the original unknown findings, dates, exact historical bindings, missing-table observations and negative predecessor findings; this new independent review does not retrospectively upgrade them or claim source-proof audits or Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | All A--L and F2 with the explicit nonempty finite window in L. |
| argument | [Exact retained argument](#argument) | Entire original argument, precise source scope and unchanged final asymptotic consequence. |
| dependency | [Exact retained dependency](Yin_C_G0239_v1.md#power-stable-many-expanding-control) | Original degree, total Mahler measure and all-positive-power degree preservation. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete good-prime order-group conventions and capacities, not abstract realization. |
| dependency | [Exact retained dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Existing good-prime unramified lift and Frobenius interface for the local modulo4 proof. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Original field, full-root norm and normalized local-depth convention. |
| review | [Isolated current whole finding](../audits/reviews/Yin_R_G0798_v1.md#g130-current-whole-independent) | Entire exact current statement and complete argument, every necessary original/current mathematical interface, original norms/weights/times/costs, source depth, finite controls and explicit limits; old physical-version and relationship findings remain separate in R798. |
