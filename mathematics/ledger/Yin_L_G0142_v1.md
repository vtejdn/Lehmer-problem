---
author: Yin
---

# Two-block phase elimination and central norm costs

Date: 2026-10-08.
Joint bounded G0001 derivation by the coordinating AI and assigned AI `growth_arithmetic_status` for Yin.
The assigned agent derived the separated-singleton elimination, its automatic trinomial nondivisibility criterion, and the finite-collar consequence.
The coordinator generalized the elimination to two arbitrary blocks and supplied its linear central-amplitude and collar bounds.
The assigned agent checked that extension and assembled the full proof.
Both are contributors; the complete independent review and its final scope clarification are recorded below.

No new source, numerical search or novelty claim is a premise.
The proof retains the exact input of [L G0138](Yin_L_G0138_v1.md#all-central-coercivity-radius): P is a monic irreducible integer polynomial of degree d, with constant coefficient +/-1, logarithmic Mahler measure m>0, and q>0 roots on the unit circle.
Put h=d-q and M=exp(m)>1.
Count every conjugate, including both members of complex pairs.
No root of P is a root of unity, since that would make its irreducible polynomial cyclotomic and give m=0.
All roots are distinct and nonzero.

The earlier norm bound charges the complete exponent span of a cluster polynomial.
Here the gap between two blocks disappears from that charge, provided an explicitly specified reciprocal-product polynomial is not divisible by P.
A three-defect cluster always satisfies the needed nondivisibility after a suitable split.
No global improvement to the K-step coercivity radius is claimed without a rule supplying these splits and controlling their exceptions.

<a id="two-block-phase-elimination"></a>
## 1. Two-block elimination and its exact arithmetic alternative

Let U,V be nonzero integer polynomials of degrees a,b, respectively, and let v>a be an integer.
Set

    Z(t)=U(t)+t^v V(t),
    D=max(a,b),       W_0=||U||_1+||V||_1=||Z||_1,
    U*(t)=t^a U(t^(-1)),       V*(t)=t^b V(t^(-1)),
    A(t)=t^(D-a) U(t)U*(t)-t^(D-b) V(t)V*(t),
    H_A=||A||_1.                                         (1)

The two displayed supports are disjoint.
Zero constant coefficients or a degree drop under reversal cause no difficulty: the displayed reversals retain their specified ambient degrees.
One always has

    A in Z[t],       deg A<=2D when A!=0,
    H_A<=||U||_1^2+||V||_1^2<=W_0^2.                     (2)

If the blocks are initially given as Laurent polynomials, first shift the whole polynomial and each block into this form, absorbing the block shifts into v.
Thus a,b can be their actual exponent spans, with nonzero constant coefficients.
Multiplication by a Laurent monomial does not change central absolute values.

For a unit-circle root beta, real coefficients give

    A(beta)=beta^D (|U(beta)|^2-|V(beta)|^2).

The phase beta^v has modulus one, so the reverse triangle inequality implies

    |A(beta)|
       <=|Z(beta)| (|U(beta)|+|V(beta)|)
       <=W_0 |Z(beta)|.                                  (3)

This is the elimination of the unknown separating phase.
Neither A nor the bounds (2)--(3) depend on v.

Suppose P does not divide A.
In particular A is nonzero and H_A>=1.
For any root alpha of P, A(alpha) is a nonzero algebraic integer.
Its absolute field norm is a positive integer, hence at least one.
At an off-circle conjugate gamma use

    |A(gamma)|<=H_A max(1,|gamma|)^(2D).

Together with (3) at every central root, this gives

    product_central |Z(beta)|
             >=W_0^(-q) H_A^(-h) M^(-2D).                (4)

Consequently, writing e=max_central |Z(beta)|,

    e>=W_0^(-1) H_A^(-h/q) M^(-2D/q).                    (5)

No factor M^v or M^(v+b) occurs.
The cost is determined by the within-block widths and coefficients, not by the intervening gap.
This does not assert that (5) beats the old bound for every split; its coefficient cost or twice the larger block width can be larger when the gap is small.
Both valid estimates may be retained.

The excluded case is a precise arithmetic condition, not an assumed genericity statement:

    P divides A
      iff |U(beta)|=|V(beta)| at one central root beta
      iff that equality holds at every central root.      (6)

For the converse, equality at one root makes A vanish there, and irreducibility forces divisibility by P.
The forward direction is immediate.
This includes A=0.
There is no implication that P must then divide Z, or that a cube-feasible response exists.
Polynomial division decides this exceptional branch exactly for supplied blocks.

<a id="singleton-refinement-and-trinomial-rigidity"></a>
## 2. A sharper singleton estimate and automatic trinomial rigidity

Suppose V=c is a nonzero integer and deg U<=delta.
Use the ambient reversal U#(t)=t^delta U(t^(-1)) and define

    A_c(t)=U(t)U#(t)-c^2 t^delta,
    H_c=||A_c||_1,
    Z(t)=U(t)+c t^v,                    v>delta.          (7)

This form explicitly permits padding and zero endpoint coefficients.
Its degree is at most 2delta, and H_c<=||U||_1^2+c^2.
At every central root put e_beta=|Z(beta)|.
Then ||U(beta)|-|c||<=e_beta, giving the sharper bound

    |A_c(beta)|<=e_beta(2|c|+e_beta).

If P does not divide A_c, the same norm calculation therefore gives

    product_central [e_beta(2|c|+e_beta)]
                         >=H_c^(-h) M^(-2delta).          (8)

In particular the common upper bound e=max_central e_beta obeys

    e(2|c|+e)>=C,
    C=H_c^(-h/q) M^(-2delta/q),
    e>=sqrt(c^2+C)-|c|>0.                                (9)

The estimate retains the exact coefficient of the singleton instead of replacing every factor by W_0.
It is again independent of v.
Here P not dividing A_c ensures H_c>=1, so 0<C<=1.

Two nondegenerate cases make the arithmetic guard automatic.

First, A_c=0 occurs exactly when U is a monomial whose coefficient has absolute value |c|.
To see this, let i_0 and i_1 be the lowest and highest occupied exponents of U.
If i_1>i_0, the highest term of U U# has exponent delta+i_1-i_0>delta and nonzero coefficient; it cannot be canceled by c^2 t^delta.
For a monomial a t^i, A_c=(a^2-c^2)t^delta, proving the assertion.
Hence if U has at least two terms and 2delta<d, then A_c is nonzero of degree below d, so P cannot divide it.
This covers any compact nonmonomial block of width less than d/2 paired with a remote singleton.

Second, for a binomial block

    U(t)=a+b t^delta,       a b c!=0, delta>=1,

one has

    A_c(t)=ab+(a^2+b^2-c^2)t^delta+ab t^(2delta).          (10)

P never divides this polynomial, with no restriction on delta.
Indeed A_c(beta)=0 at a central root would imply

    beta^delta+beta^(-delta)=-(a^2+b^2-c^2)/(ab) in Q.

Since beta is an algebraic unit, this rational number is also an algebraic integer, and hence an integer.
Its absolute value is at most two.
For each integer in {-2,-1,0,1,2}, the roots of w^2-s w+1 are roots of unity of order dividing 12.
Therefore beta^(12delta)=1, contrary to the nontorsion input.
This proves the automatic nondivisibility used in (8)--(9).

Every integer trinomial with three distinct occupied exponents can be put in this form by a monomial shift and, if necessary, reversal.
Choose its closest pair of occupied exponents.
Then

    delta=min(the two adjacent exponent gaps),           (11)

and the third term is the remote singleton.
Reversal of a real polynomial multiplies its conjugated central value by a unit complex number; thus it preserves all |Z(beta)| used here.
This choice makes the new charge independent of the larger adjacent gap.
All three nonzero coefficients, including their signs and magnitudes, remain in (10); they need not be +/-1.

For two occupied exponents the exact elementary alternative is different.
Unequal coefficient magnitudes give |Z(beta)|>=||a|-|c||>=1 at every central root, independently of the gap.
Equal magnitudes give A_c=0; this class includes the opposite-sign difference family with the recurrence suppression proved in L G0117.
No simultaneous suppression for every same-sign family is asserted.
Thus the trinomial assertion does not silently extend across the balanced-binomial exception.

<a id="two-block-finite-collar-charge"></a>
## 3. Consequence for the actual finite-energy collar test

Use exactly the finite problem of L G0130/L G0138.
For a rational B>0, suppose x in [-1/2,1/2] on I_R has energy at most B, with integer defects z_j=P(S)x_j for -R<=j<=R and z_0!=0.
Retain

    C_1=sum_i i|p_i|,       K=floor(||P||_1^2 B).

The established integer budget is sum_j|z_j|<=K.
Let a cluster interval [a_0,b_0] contain its nonzero origin defect, and suppose both length-dT collars are inside [-R,R] and have zero defects.
For its polynomial

    Z_c(t)=sum_(j=a_0)^(b_0) z_j t^(b_0-j),

the already proved disjoint-block boundary identity of [L G0135](Yin_L_G0135_v1.md#explicit-finite-energy-coercivity-radius) gives, at every central root,

    |Z_c(beta)|<=2 C_1 sqrt(B/T).                         (12)

This uses T disjoint states of d coordinates in each collar, one state on each side of norm at most sqrt(B/T), and the exact boundary telescoping identity.
All states and recurrence indices are in the finite allowed window.
We retain this established constant; no new boundary-flux estimate is a premise.

Suppose Z_c, after a monomial shift or reversal as above, has the two-block form (1), and P does not divide its A.
Then the two empty collars are impossible whenever

    T>4 C_1^2 B W_0^2 H_A^(2h/q) M^(4D/q).              (13)

Indeed (12) would make its central maximum strictly smaller than the lower bound (5).
A concrete integer choice is one plus the ceiling of the right side of (13); certified rational upper bounds can be used instead.
The common scalar factor from a monomial shift or reversal has modulus one on the circle and does not affect this comparison.

For the singleton split (7), a possibly stronger sufficient condition is

    T>4 C_1^2 B (2|c|+1)^2 H_c^(2h/q) M^(4delta/q),      (14)

provided P does not divide A_c.
For then (12) is strictly less than C/(2|c|+1), where C is defined in (9).
This is at most one, so e(2|c|+e)<e(2|c|+1)<C, contradicting (9).

Neither (13) nor (14) requires the homogeneous endpoint constant Gamma, monic division of Z_c by P, or construction of a finite integer response: the central boundary estimate itself is already inconsistent with the nondivisibility of the new polynomial A.
They are sufficient local obstructions, not an alternative proof that an arbitrary exceptional cluster is impossible.

In particular, every cluster with exactly three nonzero integer defects has a split satisfying (14) automatically, with delta given by (11), regardless of the other adjacent gap.
For such a cluster the separating gap no longer enters the norm exponent.
The total interval and its collars must still fit inside [-R,R].
A gap-independent collar length is not a gap-independent bound on the location of the cluster or on the complete search radius.

The inherited budget also gives usable coarse controls

    W_0<=K,       H_A<=K^2,
    ||U||_1+|c|<=K,       H_c<=K^2.                      (15)

Exact block coefficients normally give smaller costs and should not be replaced by these coarse bounds without retaining the loss.
No arithmetic exponent has been dropped from (13)--(14).

<a id="reciprocal-product-exception-and-scope"></a>
## 4. The exceptional branch is genuine

The condition P dividing A cannot be replaced by the assertion that the two blocks are nonzero or have disjoint supports in Z.
For example, taking V=-U gives A=0 and Z=U(1-t^v).
This is the same phase-cancellation mechanism as the balanced-binomial obstruction, with a fixed block attached.

The exceptional case can also occur with nonzero A and a nonmonomial block against a singleton.
Take U=P+t and c=-1, using delta=d.
At a central root beta, U(beta)=beta, so

    U(beta) U#(beta)-beta^d=0.

Hence P divides A_c.
This A_c is nonzero because U has nonzero constant and leading coefficients and is not a monomial, by the criterion following (9).
But for v>d,

    (U-t^v)(beta)=beta(1-beta^(v-1))!=0,

so P does not divide U-t^v.
The already retained simultaneous return construction in [L G0117](Yin_L_G0117_v1.md#moving-binomial-central-suppression) supplies unbounded v with these values simultaneously tending to zero at all central roots.
The coefficient norm remains at most ||P||_1+2.
This is an application of that existing recurrence result, not a new source or a claimed cube-feasible construction.

The exception is therefore an actual equal-modulus relation in the number field, and does not force the original cluster polynomial to be divisible by P.
Its treatment requires additional recurrence, energy, or arithmetic information.
In particular one cannot iterate (13) across every merge while ignoring the exact test in (6).

The new positive information is a support-sensitive norm estimate and a valid actual finite-collar obstruction: in the nonexceptional case, the width of each block replaces the complete span, and in the three-defect case nonexceptionality is automatic.
The old support-count/empty-collar combinatorial model does not record this reciprocal-product information.
No theorem is supplied that every feasible low-energy defect set must exhibit enough of these nonexceptional splits to shorten the global radius.
No optimized E_R value, uniform near-one energy lower bound, or solution of G0001 is claimed.


## Contributions and actual review

The coordinating AI and growth_arithmetic_status AI for Yin made the contributions stated above.
Both checked the complete assembled proof; these are contributor checks.
On 2026-10-08 the separately assigned entropy_status AI for Yin independently checked all four sections, (1)--(15) and scope statements, without contributing to this new arithmetic derivation or editing its file.
The research question and other branch context were visible, so this was not blind review.

It checked actual and padded degrees, zero endpoints and Laurent shifts, disjoint supports, coefficient norms, central phase elimination, the nonzero integer norm over all conjugates, and every exponent in (4)--(5).
It checked the exact equal-modulus/divisibility equivalence, the singleton quadratic refinement, its zero-polynomial classification, the low-degree test, the rational algebraic-integer trinomial argument, and preservation under reversal and closest-pair selection.
It directly verified the used fixed L G0130 finite problem, L G0138 integer budget, L G0135 finite cuts and existing boundary constant, and L G0117's simultaneous returns for difference binomials.
The strict collar thresholds, lack of a Gamma requirement, coefficient budgets and both true exceptional examples were covered.
Its prior contributions to L G0135/L G0138 are disclosed: those checks are reuse of fixed interfaces, not new independent review of those older proofs.

The reviewer found one source-scope sentence to clarify before adoption: the balanced-binomial class includes the difference family with the L G0117 suppression, but that result does not assert simultaneous suppression for every same-sign family.
The coordinator applied the reviewer's precise restriction; the reviewer reread the final paragraph and confirmed coverage of the corrected complete version.
No numbered formula changed, and no substantive mathematical defect or missing hypothesis remained.
It explicitly checked that a local collar obstruction does not imply an improved global radius, a feasible cube response or uniform near-one coverage.

This is complete independent AI written-proof review, not formal verification, a numerical experiment, external source-proof audit or novelty determination.
The coordinator accepted this result for fixed-ledger preservation on 2026-10-08.
The unrestricted G0001 Task remains unresolved.
