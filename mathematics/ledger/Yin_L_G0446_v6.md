---
author: Yin
---
# Arithmetic random matrices: cycle-law selection and the entropy cost of recovering an isolated certificate

<a id="scope-and-strategic-assessment"></a>
## Scope and strategic assessment

This 2026-11-05 comparison tests whether the uniform permutation law loses arithmetic information already available at a single original exponent.
It continues the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract), without replacing its unrestricted domain by the example family below.
The main agent supplied the full-valuation and relative-entropy comparison; the joint-cycle contributor checked it, and the terminal-prime contributor checked the arbitrary-law normalization and exact original-measure return.
These are ordinary author contributions and checks, not independent project review or a new Claim assessment.

The [uniform-law C867v2 theorem](../claims/Yin_C_G0867_v2.md#statement) retains its exact hypothesis that the permutation is uniformly distributed.
The [older single-time obligation](../strategies/Yin_S_G0008.md#original-norm-coverage-reassessment-2026-10-19) already permits an actual degree-scale exponent without a positive average over other exponents.
The present comparison makes that distinction explicit for arbitrary cycle laws and supplies an actual full-depth example showing that relative entropy divided by degree is not enough to transfer the uniform-law ceiling.
It gives no new uniform supply of such exponents on the unresolved near-one domain.

<a id="arbitrary-cycle-law-and-original-return"></a>
## Arbitrary cycle laws are convex averages of actual norm densities

Let P be a monic irreducible noncyclotomic integer-unit polynomial of original degree d, and write m=m(P)>0 and a_k=log|Res(P,x^k-1)|>=0.
For any probability distribution on permutations of N symbols, including a distribution depending on P, let C_k be the number of k-cycles and put Y=log|det P(Pi_N)|.
Cycle decomposition gives, pointwise,

    Y=sum_(k<=N) C_k*a_k,
    sum_(k<=N) k*C_k=N.

Consequently

    E(Y/N)=sum_(k<=N) w_k*(a_k/k),
    w_k=k*E(C_k)/N>=0,
    sum_(k<=N) w_k=1,
    E(Y/N)<=max_(k<=N) a_k/k.

No independence is used.
At fixed N, the last maximum is only an upper bound: a maximizing k need not divide N, so a permutation consisting only of k-cycles may not exist.
This normalization is consistent with [C450's general time-weight accounting](../claims/Yin_C_G0450_v1.md#statement); a weighted numerator alone is not the normalized income.

Suppose all cycle lengths occurring under the law satisfy epsilon*d<=k<=C*d, for fixed epsilon,C>0.
If C*m<=exp(-40), the original-degree envelope [C147v5](../claims/Yin_C_G0147_v5.md#statement) gives the pointwise bound

    Y/N=sum_k (k*C_k/N)*(a_k/k)
       <=epsilon^(-1)*Phi_5(C*m).

Here Phi_5 is exactly the increasing function in C147v5, with its original powered-field multiplicities retained.
The lower restriction on cycle length is necessary for this displayed estimate; arbitrary mass on very short cycles cannot use the same epsilon-independent return.
With the capped inverse H_5 from that Claim, E(Y/N)>=eta>0 therefore forces m>H_5(epsilon*eta)/C.
Indeed m<=H_5(epsilon*eta)/C would put every displayed density at most eta/2 by the defining cap and inverse.

If an actual exponent k<=C*d already satisfies a_k>=tau*d, C147v5 directly gives m>H_5(tau)/C.
Taking N=k and a single k-cycle realizes Y/N=a_k/k>=tau/C.
If also m<=M, any successful k automatically satisfies k/d>H_5(tau)/M, so it already lies at proportional scale.
This is the existing single-time norm criterion, not a new covering theorem.
For example, the [v5 mod-four output](Yin_L_G0446_v5.md#fixed-eisenstein-output-already-has-a-gap) has an actual 2d<=k<4d with a_k>=d log4, supplied by C864v2; its direct binomial return is stronger than reapplying the small-measure envelope.

Thus C867v2's quadratic terminal-layer requirement belongs to its uniform averaging law.
It is not an additional prerequisite for an original norm certificate or every other permutation ensemble.
Changing the law can recover a supplied certificate, but cannot by itself prove that such a certificate exists for every original input.

<a id="full-prime-mass-under-uniform-and-conditioned-laws"></a>
## A fixed-measure original family with different full prime mass under two laws

Reuse the actual family of [C376v2](../claims/Yin_C_G0376_v2.md#actual-isolated-linear-return-certificate), at its [selected independent adoption](../claims/Yin_C_G0376_v2.md#decision-canonical-source-binding-adoption).
Let P_0 be the fixed Lehmer polynomial and, for a rational prime q>40, set

    F_q(x)=P_0(x^q),
    d=10q,
    N=164q=(82/5)d.

C376v2 proves irreducibility, constant original measure m(F_q)=m(P_0)>0, good reduction at 3 and the isolated actual norm floor

    v_3(R_N(F_q))*log3>=d log3.

This reuses its exact retained root-order data and proof; no factorization or native numerical run is repeated.
The family is not Salem, has a q-th-power degree drop, and is not a near-one or all-power-degree-preserving counterfamily.

For any positive integers k,q, let g=gcd(k,q).
Evaluation on all k-th roots of unity gives the exact pullback identity

    R_k(P_0(x^q))=R_(k/g)(P_0)^g.

Indeed the map zeta -> zeta^q sends the k-th roots onto the (k/g)-th roots, with each image repeated g times.
Taking the absolute product of P_0 on these roots proves the identity.
It retains the full original resultant, not only the first Smith layer.

Put b_n=v_3(R_n(P_0))*log3.
The fixed-input full local estimate in [C256](../claims/Yin_C_G0256_v1.md#statement) gives a finite constant B, independent of n and q, with

    0<=b_n<=B+10 log n.

Equivalently, the good-prime ideal formula here has only finitely many fixed residue orders and initial depths, with subsequent depth linear in v_3(n).
The fixed original degree in this estimate is ten, not the growing degree d of F_q.

Let U_q be the uniform distribution on permutations of N symbols, and define the complete prime contribution

    Y_3=v_3(det F_q(Pi_N))*log3.

Uniform cycle counting and the pullback identity give, since q is prime,

    E_(U_q)Y_3
      =sum_(k<=N, q not dividing k) b_k/k
        +sum_(t<=164) b_t/t
      <=B*H_N+10*(log N)*H_N+sum_(t<=164)b_t/t
      =O((log d)^2).

The final finite sum is independent of q.
The equality and bound include q=41 and all actual valuation depths.
Therefore E_(U_q)(Y_3/d) tends to zero along these actual irreducible bounded-measure inputs.
This is a direct full-depth calculation at N=(82/5)d; it does not silently replace the dimension d in C867v2's statement by N.

Now let E_q be the event that the permutation is a single N-cycle, and let Q_q=U_q conditioned on E_q.
There are (N-1)! such permutations, so U_q(E_q)=1/N.
On E_q the full determinant equals R_N(F_q) in absolute value, hence

    Y_3/d>=log3                       Q_q-almost surely.

The relative entropy is exactly

    D_KL(Q_q||U_q)
      =sum_pi Q_q(pi)*log(Q_q(pi)/U_q(pi))
      =log N,
    D_KL(Q_q||U_q)/d -> 0.

Thus a change of law with vanishing relative entropy per original degree can turn vanishing normalized expected full prime mass into a fixed positive mass.
The same contrast holds with matrix dimension N in the denominator, where the conditional lower bound is 5log3/82.
Sublinear relative entropy alone therefore cannot transfer the uniform-law fixed-prime ceiling to a proposed new law.
The example does not assert that the unnormalized relative entropy tends to zero or that the two laws are close in total variation.

<a id="cycle-law-return-and-allocation"></a>
## Remaining supply and allocation

The full-depth calculation strengthens the law comparison for an already retained fixed-measure family; it does not provide a new near-one family or a new original-input norm floor.
The exact convex formula also leaves the existing original-time supply obligation unchanged.
A useful changed-law construction must identify its actual supplied exponents or other disjoint arithmetic income and prove the complete return to the original measure.
Neither a uniform-law obstruction nor a small relative entropy divided by d decides that obligation for another law.

Retain the single-exponent route inside the existing S8 allocation and C147v5 interface.
Do not require it to prove C867v2's quadratic averaged mass first, and do not promote selection of a favorable cycle into a new Strategy without a uniform arithmetic mechanism that supplies the favorable exponent.
The unrestricted G0001 contract remains unresolved.
