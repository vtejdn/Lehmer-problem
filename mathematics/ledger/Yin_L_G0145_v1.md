---
author: Yin
---

# Three consecutive cuts resolve the equal-modulus branch

Current checking scope is owned by [R46](../audits/reviews/Yin_R_G0046_v1.md), with its exact findings and declared relationships.
Retained review narration and relationship labels below preserve historical declarations; they do not establish an independent current relationship beyond those responsible findings.


Date: 2026-10-08.
Bounded G0001 derivation by assigned AI `growth_arithmetic_status` for Yin.
The assigned agent derived the three-cut rigidity, exceptional-cut count and complete local collar alternative.
The coordinator requested an explicit cost control and proposed the family (1+t)(1-t^L), whose full properties are checked below.
The coordinator is therefore a contributor to that control, not an independent reviewer of the complete account.
The full checking account below retains the responsible findings' actual relationships.
No new source or numerical execution is part of this derivation.

Use the exact domain of [L G0142](Yin_L_G0142_v1.md#two-block-phase-elimination): P is a monic irreducible integer polynomial of degree d, with constant coefficient +/-1, positive logarithmic Mahler measure, and q>0 roots on the unit circle.
Write h=d-q and M=M(P)>1.
All roots are distinct and nonzero, and none is a root of unity.
The result below uses one central root for rigidity and all central roots for the retained norm and collar costs.
It does not invoke a norm-one classification or Hilbert 90.

<a id="three-consecutive-cut-rigidity"></a>
## 1. The exact finite splitting test

Let Z be a nonzero integer Laurent polynomial.
After a monomial shift, enumerate its occupied exponents as

    0=n_0<n_1<...<n_(s-1),
    Z(t)=sum_(i=0)^(s-1) a_i t^(n_i),       a_i in Z minus {0}.

Assume first s>=4.
For each cut j=0,...,s-2, define the normalized left and right blocks

    U_j(t)=sum_(i=0)^j a_i t^(n_i),
    V_j(t)=sum_(i=j+1)^(s-1) a_i t^(n_i-n_(j+1)),
    Z=U_j+t^(n_(j+1))V_j,
    a_j'=deg U_j=n_j,
    b_j'=deg V_j=n_(s-1)-n_(j+1),
    D_j=max(a_j',b_j'),
    A_j=t^(D_j-a_j') U_j U_j*
                   -t^(D_j-b_j') V_j V_j*.              (1)

Reversal in (1) is with each block's own displayed degree.
The blocks have nonzero constant coefficients and disjoint supports after the indicated shift.
Call cut j exceptional if P divides A_j, including the case A_j=0.
These are precisely the two-block tests in L G0142.
Put H=||Z||_1 and H_j=||A_j||_1.

For any three consecutive cuts j,j+1,j+2, where 0<=j<=s-4,

    P divides all three A_j,A_(j+1),A_(j+2)
                  if and only if P divides Z.             (2)

Thus at most three exact polynomial-division tests either find a nonexceptional two-block split or establish the original residue-zero branch P|Z.
There is no unproved assertion that a generic split is nonexceptional.

Here is the proof with the normalization factors retained.
Fix one central root beta of P, set z=Z(beta), and write u_j=U_j(beta).
The omitted monomial in the right block has modulus one, so

    beta^(-D_j) A_j(beta)
       =|u_j|^2-|z-u_j|^2
       =2 Re(u_j overline(z))-|z|^2.                    (3)

The factors beta^(-D_j) differ from cut to cut; the proof does not subtract unnormalized polynomial values A_j(beta).

If P|Z, then z=0 and all expressions (3) vanish, so irreducibility implies P|A_j for every j.
Conversely suppose the three expressions in (2) vanish.
Subtracting consecutive equalities in (3) gives

    Re(a_(j+1) beta^(n_(j+1)) overline(z))=0,
    Re(a_(j+2) beta^(n_(j+2)) overline(z))=0.             (4)

If z!=0, the two nonzero products inside Re in (4) lie on the imaginary axis; hence their quotient is real.
Since their coefficient ratio is real and nonzero and |beta|=1, it follows that

    beta^(n_(j+2)-n_(j+1)) is 1 or -1.

This would make beta a root of unity, a contradiction.
Hence z=0, and irreducibility proves P|Z after clearing the harmless monomial shift.
This proves (2).

The same argument supplies a useful count.
If P does not divide Z, there can be at most one adjacent pair of exceptional cuts among all s-1 cuts.
Each adjacent exceptional pair forces its particular intervening monomial to be perpendicular to z in (4); two different pairs would supply two different monomials and the same torsion contradiction.
If b cuts are exceptional and g are nonexceptional, the exceptional runs number at most g+1.
At most one adjacency means b is at most the number of these runs plus one.
Therefore

    b<=g+2,
    g>=floor((s-2)/2).                                  (5)

This is a guaranteed number of available splits, not a lower bound on the sizes of the gaps they remove.

<a id="complete-local-collar-alternative"></a>
## 2. What the test gives for an actual finite cube defect

Keep the finite data of L G0130/L G0142.
Thus x is a real vector on I_R={-R,...,R+d}, |x_i|<=1/2, its energy is at most a supplied rational B>0, and its integer defects z_i=P(S)x_i are constrained on [-R,R], with z_0!=0.
Let a nonzero cluster containing the origin have polynomial Z_c as in L G0142 and two zero-defect collars of length dT inside [-R,R].
Put

    C_1=sum_i i|p_i|,
    Gamma=sum_(i,j)|(V^(-1))_(i,j)|,
    V=(beta_i^j)_(0<=j<d,1<=i<=d).

The fixed L G0135 disjoint-state boundary estimate is

    max_central |Z_c(beta)|<=2 C_1 sqrt(B/T).             (6)

Monomial normalization and reversal preserve the absolute central values, so the splitting test applies to this actual cluster.

Suppose Z_c has s>=4 nonzero coefficients and choose any three consecutive cuts.
If a test gives P not dividing A_j, the exact L G0142 norm estimate gives

    max_central |Z_c(beta)|
        >=H^(-1) H_j^(-h/q) M^(-2D_j/q).                (7)

Thus the two empty collars are impossible whenever

    T>4 C_1^2 B H^2 H_j^(2h/q) M^(4D_j/q).             (8)

The best cost among the successful tested cuts may be used.
If all three tests are exceptional, (2) gives P|Z_c instead.
Monic division then supplies the nonzero finite integer response w of L G0135, supported inside the original cluster and vanishing on the two selected boundary states.
The homogeneous difference x-w is bounded from the left for stable and central modes and from the right for expanding modes.
Consequently the same fixed argument gives

    |x_i-w_i|<=2 Gamma sqrt(B/T)<1/2
                       whenever T>16 Gamma^2 B.          (9)

At a nonzero integer coordinate of w, this contradicts |x_i|<=1/2.
All support and recurrence indices are exactly those of L G0135; no infinite response or energy outside the finite collars is used.

For a completely uniform certificate over the selected triple of cuts, let J be its nonexceptional indices and put

    F_j=4 C_1^2 B H^2 H_j^(2h/q) M^(4D_j/q),       j in J.

If J is nonempty, T=1+ceil(min_(j in J) F_j) suffices.
If J is empty, T=1+ceil(16 Gamma^2 B) suffices.
These are explicit local choices; certified rational upper bounds may replace the displayed real-algebraic quantities.
They retain the widths and coefficients of whichever split actually succeeds.

The remaining support sizes have already determined branches.
For exactly three occupied exponents, L G0142's closest-pair trinomial argument gives a nonexceptional split automatically, and its stated norm/collar bounds apply.
For one occupied exponent, the absolute central value is its nonzero integer coefficient's absolute value, at least one.
For two occupied exponents, unequal coefficient magnitudes give the same lower bound by the reverse triangle inequality.
Equal magnitudes give the balanced-binomial exception; the opposite-sign family can have arbitrarily small central values by L G0117.
No claim is made that every same-sign family simultaneously suppresses all central values.

Thus every cluster with at least three nonzero defects either has nonzero residue and a successful two-block split, or has residue zero and the separately controlled integer-response endpoint branch.
Among clusters admitting a nontrivial cut, the only case in which every available split can remain exceptional while P does not divide the cluster is the balanced two-term case.
This is a complete local branching statement, not a uniform bound on its cost and not an assertion that every abstract cluster has a cube-feasible response.

<a id="successful-cut-width-cost-control"></a>
## 3. The successful cut need not remove the largest gap

The following concrete integer polynomial family was proposed by the coordinator to test the cost of the splitting result.
For integers L>=3, put

    Z_L(t)=(1+t)(1-t^L)
          =1+t-t^L-t^(L+1).                             (10)

Its coefficient l1 norm is exactly four, and its occupied exponents are 0,1,L,L+1.
The middle adjacent exponent gap has length L-1 and is uniquely the largest adjacent gap.
The middle split has

    U=1+t,       V=-(1+t),       v=L,

and its eliminant A is identically zero.
Thus the cut that removes the large gap is exceptional for every P in the stated domain.

P does not divide Z_L.
Every root of the two factors in (10) is a root of unity, whereas no root of P is one.
By (2), at least one of the two outer cuts is nonexceptional.
But their normalized block degrees are respectively

    (0,L)  and  (L,0).

Every successful cut therefore has D_j=L, while the full exponent span of Z_L is only L+1.
The new norm estimate at such a cut has the M^(-2L/q) amplitude factor, and its collar has the M^(4L/q) factor.
It does not remove the large scale L, and it can be worse than the old full-span norm cost.
This control does not assert that the other coefficient factors are identical between the two estimates; the retained exponent alone prevents the proposed large-gap improvement here.

This is also compatible with arbitrarily small central values on each fixed P.
The already accepted simultaneous-return construction of [L G0117](Yin_L_G0117_v1.md#moving-binomial-central-suppression) gives unbounded L with max_central |1-beta^L| tending to zero.
Since |1+beta|<=2,

    max_central |Z_L(beta)|
          <=2 max_central |1-beta^L| ->0.                (11)

Its four coefficients and nonzero residue therefore do not yield a span-independent central floor.
The earlier return result is used at its existing scope; no new recurrence theorem is claimed.

The polynomials (10) are actual integer sparse polynomials, not a claim of actual finite cube realizability.
No x with P(S)x=Z_L, the required box, and bounded energy is asserted.
The long middle zero-defect interval in any proposed realization is precisely where the actual coupled gap-energy estimates of [L G0140](Yin_L_G0140_v1.md#summed-gap-weighted-variance) can add information beyond the eliminant test.
The present control does not disprove such energy charges.

<a id="equal-modulus-cut-scope"></a>
## 4. Resulting scope

The new fact is a finite, complete split alternative for actual clusters with at least three occupied exponents.
Equal-modulus conditions at three consecutive cuts force the original algebraic residue to vanish, which connects directly to the existing finite integer-response endpoint obstruction.
When the residue is nonzero, the split norm/collar estimate has at least one certified admissible cut; (5) gives further available cuts as support grows.

What is not supplied is a guarantee that a successful cut is well placed geometrically.
The four-term control shows that one cannot promote this finite algebraic completeness to removal of the largest gap, a short uniform coercivity radius, or a span-independent central lower bound.
Actual intervening-gap energy and the residue-zero endpoint branch remain substantive additional information.
No numerical search, optimized energy value, near-one uniform lower bound or resolution of G0001 is claimed.




The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0046_v1.md#contributions-and-actual-review), with its original inspected scope and relationship.
