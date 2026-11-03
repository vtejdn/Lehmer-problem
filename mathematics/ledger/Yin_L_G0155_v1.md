---
author: Yin
---

# Actual returning unit states obstruct norm-only and ideal-only one-step weights

Date: 2026-10-09.
Bounded direct G0001/S_G0007 test by the assigned entropy_status AI for Yin, with the coordinator's contribution disclosed below.
The candidate tests a specific arithmetic full-state weight, not a continuous-state relaxation or a truncated first-return table.
No numerical calculation, new source, or novelty claim is involved.
The proof is self-checked and has received the complete independent AI written proof review recorded below.
Canonical adoption is a separate coordinator decision.

The fixed [L33 Lehmer control](Yin_L_G0033_v1.md#lehmer-two-cycle-realization) supplies the named irreducible degree-ten polynomial and its retained algebraic identity.
Its irreducibility is reused at that existing scope, not newly audited here.
The exact original difference walk and its word weights are those of [L154](Yin_L_G0154_v1.md#actual-first-return-paths).
The full-state domination obligation is the one in [L8](Yin_L_G0008_v1.md#valid-finite-domination), with the forward walk convention explicitly fixed below.
L11's continuous full-place dual limitation was read for the reuse check but is not a mathematical premise of this discrete argument.

<a id="norm-cell-actual-returning-domain"></a>
## 1. The actual returning domain and safe killing

Let alpha>1 be the Lehmer root with minimal polynomial

    P(t)=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1.             (1)

Write O=Z[alpha], K0=Q(alpha), and use the original difference digits

    X_0=0, X_(j+1)=alpha X_j+eta_j,
    Pr(eta=0)=1/2, Pr(eta=1)=Pr(eta=-1)=1/4.

Every finite digit word has positive probability.
Define D to be the set of all states occurring on some finite path from 0 back to 0; in particular 0 belongs to D.
This is the full actual returning domain, not every order element in a bounded archimedean region.
Define the killed operator on nonnegative functions on D by

    (Tv)(x)=sum_(a in {-1,0,1}) w_a
               1_D(alpha x+a) v(alpha x+a),  x in D.  (2)

Killing outside D removes no returning path.
Indeed any intermediate state of a returning path belongs to D by definition.
More explicitly, if x belongs to D and y=alpha x+a is outside D, then y is reachable from zero; if it had a continuation to zero, concatenation would put y in D, a contradiction.
This is exactly the complete-domain killing permitted by the full-state comparison interface.
It is not killing at a chosen central cutoff, and no enumeration of D is asserted.

<a id="three-unit-successors-are-actual"></a>
## 2. All three successors of 1 remain on genuine first-return paths

Direct multiplication gives the exact signed-coefficient identities

    Q_0=P,
    Q_1=(t-1)P=t^11-t^9-t^8+t^3+t^2-1,
    Q_2=(t-1)^2P=t^12-t^11-t^10+t^8+t^4-t^2-t+1.     (3)

All coefficients are in {-1,0,1}, every leading coefficient is one, and each constant coefficient is nonzero.
Reading the coefficients from highest degree to constant term therefore gives returning digit words of lengths 11, 12 and 13, respectively.
Their first two digits are

    Q_0: (1,1),       Q_1: (1,0),       Q_2: (1,-1).  (4)

They are genuine first-return words.
To check every earlier time, suppose a word of length n from (3) returned at a time 1<=l<n.
The first l digits give a nonzero polynomial of degree l-1, since the first digit is one.
Its vanishing at alpha requires l>=11.
The remaining n-l digits also return from zero and give a nonzero polynomial, since the final digit of the entire word is nonzero.
They similarly require n-l>=11.
Thus n>=22, whereas each of the three lengths is at most 13.
This is a contradiction.

For clarity their positive probabilities under the unchanged digit law are 2^(-20), 2^(-18) and 2^(-21), since their numbers of nonzero digits are 9, 6 and 8.
These are symbolic word weights, not an executed path enumeration.
It follows from (4) that

    1, alpha+1, alpha, alpha-1 all belong to D,         (5)

and the three successors of 1 are nonzero.
Thus none of the three terms of (2) at x=1 is killed, even if one uses the smaller domain of nonzero states lying on first-return excursions and kills on hitting 0.

The field norm makes these four states indistinguishable:

    |Norm(1)|=|Norm(alpha)|=1,
    Norm(alpha-1)=P(1)=-1,
    Norm(alpha+1)=P(-1)=1.                            (6)

The degree is even, so the displayed evaluation signs agree with the products over all conjugates.
The first norm uses the constant coefficient one in the monic minimal polynomial.
Every norm in (6) is taken from K0 to Q.
In particular all four absolute norms equal one.
They are algebraic units: a nonzero algebraic integer of absolute field norm one has minimal-polynomial constant coefficient plus or minus one, so that polynomial expresses its inverse as an algebraic integer.

<a id="absolute-norm-weight-one-step-obstruction"></a>
## 3. No positive absolute-norm-only weight has strict one-step drift

Let phi be any function from the positive integers to (0,infinity), and let v(0) be any finite positive number.
On nonzero states of D put

    v(x)=phi(|Norm(x)|).

Every value is well defined because x is a nonzero algebraic integer and has a nonzero integer norm.
No monotonicity, boundedness or integrability assumption on phi is needed.
Equations (2), (5) and (6) give the exact equality

    (Tv)(1)=(1/4+1/2+1/4)phi(1)=v(1)>0.             (7)

Consequently no such weight can satisfy Tv<=rho v at every state of D with rho<1.
The same conclusion holds for the nonzero excursion domain just described, since all three successors in (5) remain there.
This includes weights proportional to |Norm(x)|^(-s), with any separately assigned finite positive value at zero.

More generally, the same equality holds for any positive weight that is constant on the actual algebraic units in the domain.
In particular it holds for a weight determined only by the principal ideal x O_(K0), by the complete prime-ideal valuation vector, or by all nonarchimedean absolute values: on every unit these data are, respectively, O_(K0), the zero vector, and the all-one vector.
Here O_(K0) denotes the maximal order.
No residue-sensitive information is included in these labels.

The obstruction already occurs in a finite sum at one actual state.
No limiting integral, tail truncation or exchange of infinite sums is being used to infer (7).
It therefore cannot be repaired by proving integrability of the same absolute-norm-only weight.

<a id="aggregate-first-blocking-obstruction"></a>
## 4. Taking powers after the one-step norm aggregation also fails

Let pi:D->A be any finite or countable aggregation that assigns all actual algebraic unit states to one cell a_1.
In particular this holds for every aggregation determined only by absolute field norm, including any coarsening or truncation of its values, or by any of the pure ideal or finite-place data just described.
The value of pi at zero is arbitrary.
Suppose a nonnegative matrix K=(K_ab) bounds all one-step cell transition weights entrywise:

    sum_(y in D: pi(y)=b) T(x,y)<=K_(pi(x),b)
                         for every x in D and b in A. (8)

The actual x=1 has its whole unit transition mass in cell a_1 by (5)--(6).
Hence

    K_(a_1,a_1)>=1,
    (K^N)_(a_1,a_1)>=1 for every integer N>=1.         (9)

The second inequality retains only the N-step cell path that stays at a_1.
For countably many cells, powers mean nonnegative path sums, possibly infinite.
Thus for any cell vector u with finite strictly positive coordinates,

    (K^N u)_(a_1)>=u_(a_1),

so no inequality K^N u<=rho u with rho<1 is possible.
If K is a finite matrix, (9) also implies its usual spectral radius is at least one, for example by the matrix-power spectral-radius formula.
No spectral-radius assertion for an infinite matrix on an unspecified Banach space is made or required.

The same aggregation also fails directly at the return entry.
To see this, the negatives of the Q_0 path show that -1 belongs to D; both 1 and -1 are units.
Moreover the state just before the final digit +1 of Q_0 is -alpha^(-1), since its next state is zero.
This is a nonzero unit on the already proved genuine first-return path.
Put a_0=pi(0).
If a_0 differs from a_1, (8) therefore gives

    K_(a_0,a_0)>=1/2,  K_(a_0,a_1)>=1/2,
    K_(a_1,a_0)>=1/4,  K_(a_1,a_1)>=1.               (10)

The first two bounds use the actual transitions from zero, the third uses the transition -alpha^(-1) -> 0 with digit +1, and the fourth uses the state 1 as before.
Thus the principal two-cell block dominates

    M=[ 1/2  1/2 ]
      [ 1/4   1  ],

and nonnegative path sums give

    (K^n)_(a_0,a_0)>=1/8 for every integer n>=2.      (11)

Indeed retain the cell path a_0 -> a_1, followed by n-2 unit-cell self steps and then a_1 -> a_0.
If a_0=a_1 instead, (9) gives the stronger lower bound (K^n)_(a_0,a_0)>=1 for n>=1.
These statements hold for both finite and countable aggregations.
They exclude an exponentially decaying upper bound obtained from this coarse return entry itself, even without choosing a positive vector u.
For a finite K, (10) additionally implies its spectral radius is at least the Perron eigenvalue (3+sqrt(3))/4>1 of M.
No such finite-matrix spectral claim is needed in the countable case.

The retained cell path in (11) need not lift to one actual state path: its row bounds use different unit states.
It is a lower bound for the dominating aggregate kernel, not a lower bound for the true return probability.
This precisely records the within-unit-state information lost by the one-step aggregation.

This proves failure of the specific procedure that first builds a one-step cell domination constant on units and then takes matrix powers.
It does NOT identify K^N with the best direct cell bound on T^N.
Computing an exact block operator first and only then aggregating can retain within-cell information discarded by (8); that different method is not excluded.
Nor does (7) by itself exclude a directly proved T^N v<=rho v for an absolute-norm-only v when N>1.

## Scope and contribution

This is a failed-method control on the actual retained Lehmer input, with every claimed state proved to lie on a true first-return path.
It closes one-step absolute-norm-only or pure ideal-data strict weights and their aggregate-first blocking extension.
It supplies no new lower bound for h_2, and no uniform Mahler gap.
It does not exclude weights that distinguish unit states through residue-sensitive, archimedean or other unit coordinates, exact-block-first aggregation, or a theorem with additional verified hypotheses restricted to a sufficiently smaller near-one class.
The control itself is fixed and does not form a sequence of measures tending to one.

The assigned entropy_status AI selected the absolute-norm weight test after reading S_G0007 and the fixed L8/L11/L154 boundaries.
The coordinating AI supplied the specific Lehmer polynomial, the state-1 unit-norm idea, the initial P first-return observation, the explicit pure ideal-data/finite-place interpretation, and the two-cell return-entry obstruction (10)--(11).
The assigned agent supplied and checked Q_1,Q_2, the full no-earlier-return and safe-killing guards, and the arbitrary positive weight and finite or countable aggregation argument.
These are contributions, not independent reviews of each other.
The coordinator also read the complete final Sections 1--4 and (1)--(11), including all finite and countable scope guards, and reported no contributor-check finding.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0054_v1.md#norm-cell-independent-review), with its original inspected scope and relationship.
