---
author: Yin
---

# Complete polynomial return moments and the information cost of excursion conditioning

Date: 2026-10-10.

<a id="general-unit-return-moments-fixed-scope"></a>
## Adopted scope

The coordinating AI for Yin adopts the complete new argument and its separate noncontributor review by resultant_research.
The coordinator supplied the new mathematics; the reviewer supplied none of it and disclosed its earlier L192 contribution.

For every actual degree-d algebraic unit, all fixed polynomial first-return moments obey the displayed complete bounds at their stated degree thresholds.
For d>4 the actual infinite excursion-conditioned chain has the proved stationary occupation formula, with the reciprocal specialization obtained without operator-norm Green summability.
All fixed neutral moments concentrate in high degree.
The exact per-step relative entropy is -(F/F')log F and tends to log2, while the stationary mass at zero tends to one.
These statements include torsion inputs at the specified degrees.

The actual fixed-positive-limit Salem family simultaneously retains a nonvanishing original exponential weighted tail.
The result separates full polynomial-moment and conditioned concentration information from the missing original exponential-scale gate; it supplies no near-one counterexample or uniform Mahler gap.

G0001 remains active and unresolved.
Historical pending-review language records the original chronology; the complete appended review determines the reviewed scope.
Only heading depth and relative navigation are transformed in the retained source below.

<a id="retained-complete-return-moment-proof"></a>
## Complete polynomial return moments and stationary concentration

Date: 2026-10-10.
New direct argument by the coordinating AI for Yin.
Starting question: combine the full actual integral-basis return bound in L154 with the explicit excursion-conditioned law in L192 to determine whether unweighted moment and stationary concentration information can approach the full original weighted-return gate.
Extend beyond Salem inputs where the actual proof permits, retaining every original probability, moment condition and changed-law distinction.
The coordinator alone supplies the derivations; no result or independent review is asserted at creation.
No new source or program is currently planned.

### Starting retained interfaces

The [L154 full rank bound](Yin_L_G0154_v1.md#uniform-small-unweighted-return-tail) gives p_n<=b_floor(n/d)^d for n>=d and b_q<=1/sqrt(3q+1), with f_n=0 for2<=n<=d.
These hold for every degree-d algebraic unit, including torsion.
The [L192 complete excursion-conditioned construction](Yin_L_G0192_v1.md#complete-return-conditioned-excursion-chain) proves pi(0)=F(1)/F'(1) on its Salem domain.
The present test is whether all fixed-order unweighted moments can concentrate near the one-step loop even while the original weighted obstruction survives.
A new proof is developed here; source interfaces retain their existing inspection boundaries.


<a id="full-unweighted-return-moment-bound"></a>
### 1. Every fixed polynomial moment has a complete degree-dependent bound

Let alpha be any algebraic unit of degree d, including a root of unity, and let the original digits eta in{-1,0,1} have probabilities(1/4,1/2,1/4).
Put X_(n+1)=alpha X_n+eta_n, X_0=0.
Let p_n=Pr_0(X_n=0), f_n=Pr_0(tau_+=n), tau_+=inf{n>=1:X_n=0}.
Thus f_1=1/2 and f_n=0 for2<=n<=d, by the exact degree argument in L154.
Infinite return times are excluded in every weighted finite-return sum below.

For every integer k>=0 and degree d>2k+2,

    sum_(n>=2) n^k f_n <= B_(d,k),
    B_(d,k)=2^k d^(k+1) 2^(-d)
                *[1+8/(3(d-2k-2))].                       (1)

The k=0 case is exactly L154's T_d, not a new mass theorem.
To prove the higher moments, group n by q=floor(n/d)>=1.
There are at most d terms in a block, and n^k<=d^k(q+1)^k.
Reuse f_n<=p_n<=b_q^d and b_q<=(3q+1)^(-1/2).
Since q+1<=(3q+1)/2 for q>=1,

    sum_(n>=2)n^k f_n
       <=d^(k+1) sum_(q>=1)(q+1)^k(3q+1)^(-d/2)
       <=2^(-k)d^(k+1)sum_(q>=1)(3q+1)^(-a),
    a=d/2-k>1.

The last summand is decreasing, so its full infinite sum is bounded by its value at1 plus its integral on[1,infinity).
Direct integration gives

    sum_(q>=1)(3q+1)^(-a)
       <=4^(-a)+4^(1-a)/(3(a-1)).

This is exactly(1).
It includes all late excursions and needs neither a Mahler bound nor an exponential collision estimate.
For every fixed k, the right side tends to zero as d tends to infinity.
It is not a bound uniform in k when k grows with d.

In particular, for d>4, writing F=sum f_n and F'=sum n f_n,

    0<=F-1/2<=T_d,
    0<=F'-1/2<=B_(d,1),
    B_(d,1)=2d^2 2^(-d)[1+8/(3(d-4))].                  (2)

Also U=sum_(n>=0)p_n is finite for d>2 by the same unweighted endpoint bound, with the finitely many n<d terms retained.
Complete renewal gives F<1 and U=1/(1-F).
No entropy positivity or non-torsion premise is needed for this transience statement at d>2.

<a id="general-unit-excursion-stationary-law"></a>
### 2. The infinite excursion-conditioned chain for general units

Assume d>4.
Let D be the actual return core, the states occurring on finite original zero-to-zero words, and let K be the original kernel killed outside D.
Its positive graph is irreducible through zero by definition.
Let H(x)=Pr_x(tau_0<infinity) for x!=0 in D, with H(0)=1.
It is positive on D.
All ambient co-return paths from x in D stay in D, since prefixing any zero-to-x path makes them part of a closed word.
Therefore these are the actual core-kernel hitting probabilities.

The matrix

    Q(x,y)=K(x,y)H(y)/H(x) for x!=0,
    Q(0,y)=K(0,y)H(y)/F                                  (3)

is stochastic by first-step decomposition: KH=H away from zero and KH(0)=F.
Its positive edges are precisely the core edges.
Every first-return excursion telescopes to its original probability divided by F, including the one-step zero loop.
Thus its first-return law is f_n/F, its mean is F'/F<infinity, and it is a positive recurrent chain on the entire possibly infinite core.
This extends the L192 construction beyond the Salem domain using(1), without assuming any infinite critical Perron normalization.

There is a direct stationary occupation formula valid without reciprocity.
For a set A of core states put

    pi(A)=(1/F') E_original,0[
                  sum_(j=0)^(tau_+-1) 1_A(X_j); tau_+<infinity].    (4)

This is a probability because its numerator for A=D is F'.
It is the Q excursion occupation divided by its mean return time.
For each state y, summing expected Q transitions during a whole excursion shifts occupation indices from j=0,...,tau_+-1 to j=1,...,tau_+.
Both endpoint states are zero, so the sums agree.
Nonnegative summation and finite expected length justify this operation, proving pi Q=pi.
In particular

    pi(0)=F/F',
    pi(D minus{0})=(F'-F)/F'<=2B_(d,1).                    (5)

A bound exceeding one is simply weakened to one.
All statements here allow torsion and nonreciprocal algebraic units.
Degree is actual irreducible degree, not padded presentation rank.

If P is reciprocal, its degree is even and the automorphism sigma(alpha)=alpha^(-1) defines T(x)=alpha^(-1)sigma(x).
This is an additive involution preserving O=Z[alpha] and D, and K(Ty,Tx)=K(x,y) because reversed digits have the same weight.
In this case the entire distribution has the explicit formula

    pi(0)=F/F',
    pi(x)=H(x)H(Tx)/F' for x!=0.                           (6)

Here is a proof requiring no l2 Green-operator convergence.
The autocorrelation maximum-atom argument in L173 bounds each ambient n-step endpoint atom by p_n, also when its starting state is fixed and nonzero.
Hence each Green entry G(x,y)=sum_n K^n(x,y) is finite, bounded above by U.
First-hit decomposition gives G(x,0)=H(x)U, and reciprocal reversal gives G(0,x)=UH(Tx).

For x!=0 let V(0,x) be the expected number of visits to x after leaving time0 and before the first positive return, allowing paths that never return.
Decomposing all zero-to-x paths at their last visit to zero gives G(0,x)=U V(0,x) by nonnegative path summation.
At a pre-return visit to x, the conditional probability of a future zero hit is H(x).
Thus the numerator in(4) at x is H(x)V(0,x)=H(x)H(Tx), giving(6).
Its complete normalization follows from(4), rather than an unproved exchange of critical Green sums.
This recovers L192's formula on its scope and extends it to every reciprocal unit of degree d>4, including cyclotomic inputs.
No exponential radius tail outside L192's hypotheses is inferred.

### 3. Stationary neutral moments also vanish in high degree

Suppose alpha has s>=1 selected unit-circle conjugate pairs, and define the joint neutral radius rho(x)^2=sum_(j=1)^s |x(zeta_j)|^2.
No assumption is made on the other conjugates, so several expanding pairs are allowed.
Along a zero-to-zero word of total length n, both forward and backward neutral propagation imply

    rho(X_j)<=sqrt(s) min(j,n-j)<=sqrt(s)n/2.

Each digit has neutral norm at most sqrt(s), and neutral multiplication is orthogonal; these two estimates use the same complete word.
For every integer k>=1 with d>2k+4, applying(4) to rho^k yields

    E_pi rho^k
       <=(sqrt(s)/2)^k (1/F')sum_(n>=2)n^(k+1) f_n
       <=2(sqrt(s)/2)^k B_(d,k+1).                         (7)

The one-step zero loop contributes no neutral radius.
Since s<=d/2, for each fixed k this bound tends to zero with d, uniformly in the actual unit input of that degree.
This is concentration under the deliberately conditioned law.
It asserts neither a uniform lower separation of nonzero lattice radii nor original-walk stationarity.

<a id="excursion-conditioning-information-cost"></a>
### 4. Exact information cost per step, and its high-degree limit

For each x let q_x(eta) be the three original-digit probabilities under(3), with zero for successors outside D.
Distinct digits give distinct successors.
Define the nonnegative relative entropy of this row with respect to the original digit law p by

    D_x=sum_eta q_x(eta) log(q_x(eta)/p_eta),

where a zero summand is zero, and put I=sum_x pi(x)D_x.
All logarithms are natural.
Row normalization and p_eta>=1/4 give0<=D_x<=log4.
Its nonnegativity follows from the elementary log-sum inequality, or Jensen applied to log(p_eta/q_x(eta)) on the positive q support.

For each complete Q first-return excursion, the product likelihood ratio to the original path is1/F.
Therefore the sum of the transition log likelihoods is exactly-log F, for every such finite excursion.
This can be averaged and reordered safely: at each state the expected absolute log likelihood is at most log3+log4, because -sum q log q<=log3 and -log p_eta<=log4.
The Q expected excursion length F'/F is finite, so the expected sum of absolute values is finite.
Using its stationary occupation formula gives the exact identity

    I=-(F/F')log F=-pi(0)log F.                            (8)

Thus the conditional chain pays a definite information cost even though all its excursions return.
From F=1/2+a with0<=a<=T_d and(5),

    0<=log2-I
       <=2B_(d,1)log2+log(1+2a)
       <=2B_(d,1)log2+2T_d.                               (9)

Consequently I tends uniformly to log2 as actual degree tends to infinity, and pi(0) tends uniformly to one.
These limits need no near-one or nontorsion assumption.
They show how this conditioning concentrates on the original zero loop.
It is not a low-cost critical transform merely because it is normalized and stationary.
Equation(8) does not identify I with the original collision entropy or Mahler measure.

<a id="polynomial-moments-versus-weighted-return"></a>
### 5. Actual weighted obstruction survives every fixed polynomial moment

Use L154's retained actual irreducible Salem family

    P_N=t^N(t^3-t-1)+(1-t^2-t^3),
    N=9 modulo120, N>=129, d=N+3,

whose measures tend to the plastic value theta>1 and remain below4/3.
Its full original first-return law satisfies

    sum_(n>d) f_n(4/3)^n>=1/3.                             (10)

At the same time(1), (5), (7), (9) imply, along this very same actual family:

    sum_(n>=2)n^k f_n ->0 for every fixed integer k>=0,
    pi(0)->1,   E_pi rho^k->0 for every fixed k>=1,
    I->log2.

For each fixed k the degree condition eventually holds; no statement about a simultaneous unbounded order k is made.
The weighted lower bound(10) is reused at its complete original-law scope, with every late excursion included.
These facts demonstrate that even convergence of all fixed polynomial moments, together with the displayed stationary concentration, supplies no modulus forcing the chosen exponential weighted tail to vanish across actual inputs.
They sharpen L154's earlier mass-only distinction, rather than repeating its theorem as new.

This family has fixed positive limiting measure and does not exclude a smaller common positive weight or a new arithmetic theorem restricted essentially to hypothetical total measure tending to one.
For any such hypothesis the current unweighted moment and conditioning statements still hold, so an attempted gap proof must add information about exponential tilting or genuinely new arithmetic control.
The degree-rank Holder estimates by themselves do not give that missing exponential-scale control.

### Contribution and checking boundary

The coordinator supplied the higher-moment summation, general-unit excursion/occupation extension, reciprocal formula without operator-norm summability, all neutral moments, exact information-rate identity with its absolute-integrability justification, and the combined actual-family comparison.
L154's rank bound, first-return gap and weighted example and L173's maximum-atom argument are explicit fixed reuse.
L192 supplies the earlier Salem construction and interpretation; no new external theorem, program or finite scan is needed.
Self-check covered degree restrictions, complete summation, last-zero decomposition, torsion cases, actual core paths, original versus conditioned probabilities, reciprocal orientation, moment factors, likelihood telescoping and limit order.
Full separate noncontributor review is pending; G0001 remains active and unresolved.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0097_v1.md#complete-return-moment-independent-review), with its original inspected scope and relationship.

## Retention and review bindings

The [complete separate review](../audits/reviews/Yin_R_G0097_v1.md#complete-return-moment-independent-review) applies to the entire [retained argument](#retained-complete-return-moment-proof) and its stated reused interfaces.
Its contribution disclosures and all limits remain part of this fixed record.

The complete D G0066 argument and its noncontributor finding are retained here at their original scopes.
Fixed proof retention does not complete the Task.
