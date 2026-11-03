---
author: Yin
---

# Finite-prime return cores, exact return languages, and the global coverage boundary

Date: 2026-10-09.
Bounded G0001/S_G0007 work by the assigned execution_and_deliverables AI for Yin, with the coordinating AI and the separately assigned entropy_status AI contributions specified below.
This argument is self-checked and has the complete independent AI written review and fixed-ledger adoption recorded below.
No numerical enumeration or new source acquisition was performed.
There is no novelty claim.

The direct external input is the already accepted [ESS02-U001 two-variable counting bound](../audits/literature/ESS02/Yin_U001.md#ess-exact-counting-bound), used at its retained statement-and-applicability scope, with the [L156 elementary rank bounds](Yin_L_G0156_v1.md#elementary-unit-rank-upper-bound) and [finite-prime extension](Yin_L_G0156_v1.md#finite-prime-and-norm-band-sojourns).
The original ESS proof is not re-audited.
Local reuse also includes [C212 hyperbolic carry-state bound](../claims/Yin_C_G0212_v1.md#carry-state-bound) and [L41's exact return presentation](Yin_L_G0041_v1.md#branch-return-budget): finite displayed transition data must preserve its actual delays.
The new scope here is the finite core of the *actual restricted return language*, together with exact criteria for when one fixed finite-prime restriction covers all returns.
It does not establish that coverage on the unresolved reciprocal class.

<a id="finite-prime-return-core"></a>
## 1. Actual restricted return states and finitely many nonzero edges

Let alpha be a nontorsion algebraic unit, let K=Q(alpha) have degree d, let O=Z[alpha], and let O_K be the maximal order.
In particular d>=2 and alpha^(-1) belongs to O.
For a finite word w=(eta_0,...,eta_(n-1)) over {-1,0,1}, use the original walk and weights

    X_0=0,  X_(j+1)=alpha X_j+eta_j,
    w_0=1/2,  w_1=w_(-1)=1/4.                       (1)

Let D consist of all states on finite words that end back at zero, including the empty word.
Every state in D lies in O.
Given a fixed finite set S of prime ideals of O_K, put s=|S| and

    E_S={x in K*:v_p(x)=0 for every p notin S},
    V_S=D intersect ({0} union E_S).

Define D_S to consist of all states on finite words from zero back to zero for which *every* state is in {0} union E_S.
Equivalently, every state of such a word is in V_S.
Membership in V_S alone does not assert the existence of such a restricted completion: D_S is the strongly connected component of zero in the restricted directed graph.
No equality D_S=V_S is assumed.

The retained rank argument gives rank(E_S)<=d-1+s.
Consider all edges

    x -> y=alpha x+a,
    a in {-1,1},  x,y in O intersect E_S.            (2)

For fixed a, the ordered pair (x,y) in E_S x E_S satisfies

    (-alpha/a)x+(1/a)y=1.

Both coefficients and both terms are nonzero, so this two-variable solution is nondegenerate.
The direct-product group has rank at most 2(d-1+s).
The accepted ESS bound therefore gives at most

    C=C_(d,s)=ceil(exp(12^6(2d+2s-1)))              (3)

edges for each choice of a, and at most 2C edges in total.
This count is first valid in the larger group E_S x E_S and remains valid after restricting to the integral order O.
The integrality restriction is retained in every endpoint set below.

Let A contain all nonzero endpoints of the edges (2), together with {1,-1,alpha^(-1),-alpha^(-1)}.
Then

    a_S=|A|<=4C+4.                                  (4)

The added endpoints include every possible nonzero endpoint of an edge incident with zero: 0 goes to +/-1, and +/-alpha^(-1) goes to zero using the opposite digit.
The zero digit gives only 0->0 at zero.
Every member of A is an integral S-unit in O; the set may include states that are not actually reachable or returnable.

## 2. Zero chains preserve finite lengths and give an exact finite core

Fix an ordered pair (a,b) in A x A.
There is at most one integer k>=0 such that alpha^k a=b.
Indeed two such integers would imply that a positive power of alpha is one.
When it exists, denote it by k_ab.
Let T be the finite set of ordered pairs for which it exists, and set J=max_(T) k_ab; this maximum is defined because every pair (a,a) has k_aa=0.

In a restricted zero-to-zero word, ignore zero steps taken at state zero.
Every maximal run of zero digits at nonzero states has an initial and a terminal endpoint in A: its adjacent nonzero digits are covered by (2), or by the boundary edges incident with zero.
Such a run has the exact form

    a, alpha a, ..., alpha^(k_ab) a=b.               (5)

Consequently every state of D_S belongs to the finite set

    G_S={0} union A
        union {alpha^i a:(a,b) in T, 1<=i<k_ab}.

All its nonzero states are still integral S-units.
If N=|D_S|, then

    N<=|G_S|<=1+a_S+sum_((a,b) in T)(k_ab-1)_+
       <=1+a_S+a_S^2 max(J-1,0).                    (6)

Take the finite directed graph on G_S with precisely those original digit edges whose endpoints lie in G_S.
Its strongly connected component containing zero is exactly D_S.
In one direction every restricted returning word lies in G_S by (5); in the other direction every closed walk through zero in this finite graph is itself an actual restricted returning word.
This proves finiteness without replacing a path by representative states from different paths.

There is a precise, but input-dependent, height cost for the lengths.
Choose an embedding sigma with rho=|sigma(alpha)|>1.
Such an embedding exists: otherwise the norm-one condition forces every conjugate to have modulus one, and the finite-kernel argument in L156 applied to all powers of alpha would contradict nontorsion.
Define

    H_A=max(1,max_(a in A, tau:K->C)|tau(a)|).

Because a is a nonzero algebraic integer, its absolute field norm is a positive integer.
Hence |sigma(a)|>=H_A^(-(d-1)).
From alpha^k a=b one obtains

    rho^k=|sigma(b)|/|sigma(a)|<=H_A^d,
    J<=d log(H_A)/log(rho).                          (7)

This argument would not apply to arbitrary fractional S-units; the integrality in (2) and in the definition of A is essential.
Equations (3)--(4) bound the number of edges, whereas (7) retains the height of their endpoints.
No bound on H_A or J in terms of d,s alone, no complete effective enumeration of the ESS solutions, and no practical algorithm for constructing G_S is obtained here.
Replacing each zero chain by a single edge and discarding k_ab would change the return law.

<a id="finite-prime-rational-return-law"></a>
## 3. Exact rational return series, with all original delays and weights

Index D_S with zero first and let P_S be its original substochastic transition matrix: an edge with digit a has weight w_a from (1), and transitions leaving D_S are killed.
Every returning path that stays in V_S already lies in D_S by its definition.
Thus, writing p_n^S for its complete return probability and f_n^S for its first-return probability,

    p_n^S=(P_S^n)_(00),
    U_S(z)=sum_(n>=0) p_n^S z^n,
    F_S(z)=sum_(n>=1) f_n^S z^n.                    (8)

As formal power series, the finite matrix inverse and first-return decomposition give

    U_S(z)=[(I-zP_S)^(-1)]_(00)
          =A_S(z)/D_S^det(z),
    F_S(z)=1-1/U_S(z)
          =[A_S(z)-D_S^det(z)]/A_S(z),              (9)

where A_S(z) is the (0,0) cofactor of I-zP_S and D_S^det(z)=det(I-zP_S).
Both constant terms are one.
Their degrees are at most N-1 and N, respectively, so the displayed numerator and denominator degrees for F_S are at most N and N-1.
Possible common factors can lower these degrees.
The first-return identity follows coefficientwise by splitting each nonempty returning word at its first positive return time; it uses all words and their product weights.
It does not infer return probabilities from a killed chain on a smaller arbitrary truncation.

The analytic positive window is already supplied by [L156](Yin_L_G0156_v1.md#complete-fixed-prime-return-certificate).
Specifically, for

    B=ceil(exp(12^6(d+s+1))), M=B+3,
    delta=2^(-B-5), gamma=-log(1-delta)/M,
    p_n^S<=(1-delta)^floor(n/M),
    U_S(z)<infinity and F_S(z)<1
        whenever 1<=z<exp(gamma).                  (10)

The present finite-core proof adds the exact rational presentation, not a better uniform rate or an execution of that presentation.
An algebraic continuation of (9) beyond convergence is not the nonnegative path sum.
The dependence on s in (10) cannot be removed by assigning a different finite S to each separate finite word.

<a id="global-prime-support-finite-core-equivalence"></a>
## 4. What global finite-prime coverage would actually assert

For a fixed alpha as above, the following are equivalent:

1. There is one finite S such that D\{0} is contained in E_S.
2. The full actual returning-state set D is finite.
3. The positive integers |Norm_(K/Q)(x)|, x in D\{0}, have a common finite upper bound.
4. The full zero-word language over {-1,0,1} is regular.
5. For the monic minimal polynomial P of alpha, the integer quotients q in all multiples Q=Pq with coefficient height at most one have a common coefficient-height bound.

For 1=>2, every returning word lies in the same finite-prime domain, so D=D_S and Section 2 applies.
If 2 holds, take the finite union of the prime-ideal supports of the nonzero algebraic integers in D; this gives 1, and finiteness also gives 3.
For 3=>1, let the norm bound be H>=1 and take all prime ideals of norm at most H.
There are finitely many: the retained L156 ideal-norm argument gives at most d pi(floor H).
Every prime ideal dividing the principal integral ideal (x) has norm at most |Norm(x)|<=H, so all x in question belong to E_S.

Here is a direct proof of the language assertion, without importing a language-minimization theorem.
Define

    L_0={w:X_w(0)=0},                               (11)

including the empty word, and use the definition of regularity as acceptance by a deterministic finite automaton.
If D is finite, the actual digit graph on D, together with one rejecting dead state for every transition leaving D, is such an automaton, with initial and sole accepting state zero.
Once a reachable prefix has left D, it cannot have a completing suffix to zero; otherwise its endpoint would by definition lie in D.
Thus the dead state loses no word.

Conversely, suppose a finite deterministic automaton accepts L_0.
For each x in D choose a prefix u_x that reaches x and a suffix v_x that brings x to zero.
If a suffix v has length n, then

    X_v(x)-X_v(y)=alpha^n(x-y).                     (12)

Distinct states therefore have disjoint nonempty sets of completing suffixes.
The automaton states after u_x and u_y cannot be equal: if they were, the accepted completion v_x after u_x would also be accepted after u_y, contradicting (12).
Hence D injects into the finite automaton state set, which proves 4=>2.
The construction in the other direction uses at most |D|+1 states.
The same argument shows that the fixed-S restricted zero-word language has a finite automaton based on D_S plus a dead state.

In particular, if D is infinite then its nonzero states have unbounded absolute norms and infinitely many different prime ideals occur in their supports.
This is a conditional conclusion; infinitude of D on the actual unresolved Salem class is not proved here.
Global finite-prime coverage is exactly a finite actual carry-core or regular-language condition, not an automatic weaker consequence of each word having finite prime support.
No converse from a rational one-variable return generating function to finite D is asserted.

<a id="return-core-quotient-height-equivalence"></a>
## 5. An exact quotient-height criterion and a fixed-seed limitation

Write the monic minimal polynomial as P(t)=sum_(i=0)^d p_i t^i, with p_d=1.
For an integer polynomial q, let H(q) be the maximum absolute value of its coefficients, with H(0)=0.
The coordinate argument in this section only requires alpha to be a nonzero algebraic integer; the preceding unit and nontorsion assumptions remain in force for the combined equivalence.
A word eta_0,...,eta_(L-1) returns exactly when

    Q(t)=sum_(j=0)^(L-1) eta_j t^(L-1-j)

vanishes at alpha.
For nonzero Q, minimal-polynomial divisibility and monic integer long division give Q=Pq with q in Z[t].
Conversely, every nonzero integer multiple Q=Pq with coefficient height at most one gives an actual returning word by reading its coefficients in descending order.
Every intermediate state is then both reachable and co-returning, rather than merely an ambient order element.

If Q=0 as a polynomial, every digit is zero and only zero is visited; use H(0)=0 for coefficient height.
Initial zero digits merely add initial zero states.
Final zero digits are also harmless: if Q=t^r Q_0 and Q_0(0)!=0, then alpha!=0 implies Q_0(alpha)=0, so these digits follow an already completed return.
Empty and all-zero words, and leading or trailing zero padding, are therefore included.

For a nonzero Q=Pq, write Q=sum_(j=0)^n a_j t^j.
Set q_r=0 outside 0<=r<=deg q.
For 0<=k<=n+1, the cut state after reading a_n,...,a_k is

    x_k=sum_(j=k)^n a_j alpha^(j-k),
    x_(n+1)=0,             x_0=Q(alpha)=0.            (13)

Define B_h(t)=sum_(i=h)^d p_i t^(i-h), for 1<=h<=d.
Then

    x_k=sum_(h=1)^d q_(k-h) B_h(alpha).              (14)

Indeed substitute a_j=sum_(i=0)^d p_i q_(j-i) into (13) and group by r=j-i.
For r>=k the entire contribution is q_r alpha^(r-k)P(alpha)=0.
For r<k, only k-d<=r<=k-1 can contribute.
Writing h=k-r gives the remaining contribution q_(k-h)sum_(i=h)^d p_i alpha^(i-h)=q_(k-h)B_h(alpha).
This also verifies the two endpoint cases using the zero extensions.

The degree of B_h is d-h and its leading coefficient is one, so B_1(alpha)...,B_d(alpha) form a triangular integral basis of O relative to alpha^(d-1)...,alpha,1.
In particular, all the coordinates in (14) are unique integers.
Consequently,

    D finite
      iff there is an integer A>=0 such that
          H(q)<=A for every Q=Pq with H(Q)<=1.        (15)

If this coefficient bound holds, (14) puts every returning state in the box of basis coordinates [-A,A]^d intersect Z^d and gives

    |D|<=(2A+1)^d.                                  (16)

Conversely, for finite D let A be the largest absolute value of its coordinates in this basis.
Given any admissible nonzero Q=Pq and any 0<=l<=deg q, use k=l+d.
Since deg Q=deg q+d, this is a valid cut with d<=k<=deg Q.
Its h=d coordinate in (14) is q_(k-d)=q_l.
Thus every quotient coefficient is bounded by A; the zero quotient satisfies the same bound.
This proves the equivalence of condition 5 with the other four conditions of Section 4.

There is an actual construction limit behind this criterion.
Fix a nonzero seed Q_0=Pq_0 with H(Q_0)<=1, and form signed-shift sums Q=Q_0 C with C in Z[t], H(C)<=1.
Consider only outputs with H(Q)<=1, so their digit words remain admissible.
Since q=q_0 C,

    H(q)<=sum_r |(q_0)_r|=||q_0||_1.                (17)

This follows coefficientwise from convolution.
All cut states of all these outputs therefore lie in one finite set of size at most (2||q_0||_1+1)^d, independently of the degree and number of shifts in C.
Cancellation between shifted seed words does not alter (17).
This construction with a fixed seed and the stated coefficient bound on C cannot prove D infinite.

No actual fixed Salem input with infinite D is constructed here.
By (15), that would require height-one multiples of the same P with unbounded integer quotient height.
Unit-circle conjugates alone do not establish this property, and the [L8 ambient quartic elements](Yin_L_G0008_v1.md#quartic-projection-obstruction) do not establish their own reachability and co-return.
The structural equivalence and the failed fixed-seed construction give no new entropy exponent or unrestricted finite-prime coverage.

<a id="finite-prime-core-golden-ratio-control"></a>
## 6. A fixed actual full-coverage example and its exact series

The already fixed [C212 golden-ratio certificate](../claims/Yin_C_G0212_v1.md#golden-ratio-certificate) exhausts the returning states for the inverse-carry convention at phi=(1+sqrt(5))/2, u=phi-1=phi^(-1).
To transfer conventions, take a forward returning word eta_0,...,eta_(n-1), reverse its digits by delta_i=eta_(n-1-i), and form

    c_0=0, c_(j+1)=phi^(-1)(c_j+delta_j).

For every 0<=j<=n the original zero-sum condition gives

    c_(n-j)=sum_(k=j)^(n-1) eta_k phi^(j-1-k)
           =-X_j.                                  (18)

This includes both zero endpoints.
Reversal is bijective and preserves every word weight.
Since L5's exhausted inverse-carry set {0,+/-u,+/-1} is closed under negation, the forward returning-state set is exactly the same set.
Every listed nonzero state is a unit, so S=empty covers the entire D in this fixed example.

In the forward convention the transitions inside D are 0->0 with weight 1/2, 0->+/-1 with weight 1/4 each, +/-1->+/-u with weight 1/4, and +/-u->0,+/-1 with weights 1/4,1/2.
On the classes (0,{+/-1},{+/-u}), the row matrix is

    P_phi=[[1/2,1/2,0],
           [0,0,1/4],
           [1/4,1/2,0]].                            (19)

This grouping is exact because the two signs have identical total transition weights into each class.
A nontrivial first return uses the length-three path through the two nonzero classes, with weight 1/32, and may make any number of the intervening length-two cycles of weight 1/8.
Thus the complete, untruncated series are

    F_phi(z)=z/2+(z^3/32)/(1-z^2/8),
    U_phi(z)=(32-4z^2)/(32-16z-4z^2+z^3).           (20)

These are formal identities and actual nonnegative sums on their convergence domains.
The finite-state exhaustion is reused from L5; only the convention transfer and the displayed rational expression are derived here.
This fixed nonreciprocal example has Mahler measure phi, and gives no new sufficiently-near-one coverage or unrestricted gap theorem.

<a id="finite-prime-core-scope-and-contributions"></a>
## 7. Scope, reuse, and contributions

The coordinating AI proposed the finite-edge/zero-chain proof of the finite restricted core, the global-support equivalence, and the regular-language criterion.
The execution_and_deliverables AI checked the tuple-rank and boundary-edge counts, integral endpoint and zero-chain length guards, assembled the full proof and rational degree bounds, and derived the forward golden-ratio transfer and expression (20).
The coordinating AI separately checked that example's transition matrix and expression.
The entropy_status AI supplied the quotient cut-state formula, its integral basis, and the fixed-seed signed-shift obstruction.
The coordinating AI supplied the reverse coordinate extraction proving finite D implies uniformly bounded quotient height; entropy_status checked and wrote its finite-index details.
The full component (13)--(17) was incorporated from its self-checked written source.
These are contributor checks, not independent review.

The assembling authoring AI has self-checked every displayed formula (1)--(20), the full actual-domain quantifiers, integral endpoint guard, zero-chain decomposition, rational and analytic distinctions, both directions of all five equivalent conditions, the quotient cut endpoints, and the golden-ratio forward transfer.
Existing fixed inputs retain their recorded review and contribution boundaries; this is not a new independent review of those old proofs.
The coordinating AI also read the complete frozen Sections 1--7 and (1)--(20), including the full quotient component and contribution boundaries, and reported no substantive defect.
That is a contributor check; whole-source independent review is recorded below.

The fixed L5 result already proves D finite whenever alpha has no unit-circle conjugates: its bounds at every embedding give a finite lattice region.
The forward/inverse relation (18), with phi replaced by alpha, transfers its convention.
Thus this existing hyperbolic scope already has some global finite-prime support.
It does not bound the size of that support uniformly in a varying input.
Neither the new ESS count nor language regularity resolves the unit-circle case.

The bounded round stops at an exact structural reduction and an actual fixed control.
To turn the L156 fixed-S positive window into a new unrestricted estimate, one must either prove global coverage together with useful d,s costs on the intended actual inputs, or control the full omitted departure-and-reentry contribution.
The current proof does neither.
Rationality and finiteness for each fixed S do not permit a uniform conclusion after S grows with the path length.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0056_v1.md#finite-prime-core-independent-review), with its original inspected scope and relationship.
