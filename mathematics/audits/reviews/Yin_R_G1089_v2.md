---
author: Yin
---
# Whole review of full small-prime valuation mass in permutation determinants

Date: 2026-11-05T11:18.
Human record author Yin.
This is a separately organized first whole-proof review of the fixed [C867v2 statement](../../claims/Yin_C_G0867_v2.md#statement) and [argument](../../claims/Yin_C_G0867_v2.md#argument), including HD1--HD12 and their quantifiers and scope.
The reviewer did not contribute to the candidate's development and received no proof-development discussion, mathematical summary, proposed repair or prior conclusion about this full-valuation candidate.
The reviewer read the fixed candidate and its necessary fixed mathematical inputs, enumerated the obligations and formed the mathematical findings before consulting the existing reviews of those accepted inputs.
D21--D23, other exploration drafts, author-development notes and the earlier R1089v1 conclusions were not consulted.
The candidate, its assessment and R1089v1 were not edited.
This new physical review version retains distinct evidence for the materially different full-valuation candidate.

## Reviewed inputs and inherited boundaries

The directly used inputs are [C147v5's complete original-degree envelope](../../claims/Yin_C_G0147_v5.md#statement) and its [argument](../../claims/Yin_C_G0147_v5.md#argument), [C265v1's exact idealwise cyclotomic layers](../../claims/Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers) and [critical-depth calculation](../../claims/Yin_C_G0265_v1.md#old-layer-exception-threshold), and [C256v1's norm and multiplicity identities](../../claims/Yin_C_G0256_v1.md#content-versus-ideal-norm) and [aggregate norm bound](../../claims/Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion).
The local ideal, binomial, critical-divisibility and archimedean norm calculations actually used here were rechecked directly.
The existing [R381 finding](Yin_R_G0381_v1.md#cyclic-loglog-whole-independent-finding), [R531 primitive-layer finding](Yin_R_G0531_v1.md#current-primitive-escape-finding) and [R527 cyclic-table finding](Yin_R_G0527_v1.md#current-cyclic-table-finding) were then checked for their precise input coverage and retained limitations.
Their declared relationships remain respectively unknown, self-reviewed and self-reviewed; this review does not reclassify them.
C147v5 is reused as an accepted numerical norm estimate, with its recorded finite-energy and external theorem boundaries.
The retained [Smy08 source unit](../literature/Smy08/Yin_U001.md#smy08-u001) and R381 disclose the numerical Dobrowolski source scope and the unused defective resultant explanation.
No original external theorem proof or source PDF was newly audited here.
The C867v1, L159, L446, C267 and C450 comparisons supply no additional premise to HD1--HD12; the needed permutation-cycle identity is proved directly in C867v2 and checked below.
The [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) was checked only to distinguish this obstruction theorem from the unrestricted gap objective.
The current erratum contained no recorded objection.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole full-valuation finding](#whole-full-valuation-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole full-valuation finding](#whole-full-valuation-finding) | [C867v2 statement](../../claims/Yin_C_G0867_v2.md#statement) | Entire exact statement: original nontorsion irreducible-unit domain, determinant and cyclotomic identities, HD1--HD5, bounded total measure, sublinear clocks, terminal mass, prescribed sublogarithmic prime budgets, uniformity, floors, empty sets and probability conclusion. |
| [Whole full-valuation finding](#whole-full-valuation-finding) | [C867v2 argument](../../claims/Yin_C_G0867_v2.md#argument) | Entire derivation of HD1--HD12: original multiplicities, complete low-clock envelope, terminal-mass implication, every local valuation depth and critical exception, degree costs, seed bounds, geometric tails and both limiting steps. |
| [Whole full-valuation finding](#whole-full-valuation-finding) | [C147v5 statement](../../claims/Yin_C_G0147_v5.md#statement) | Accepted complete cyclic norm bound with h=t m/d, original degree and all powered-field multiplicities; its small-h domain and monotonicity are matched to every invocation. |
| [Whole full-valuation finding](#whole-full-valuation-finding) | [C265v1 idealwise layers](../../claims/Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers) | Exact idealwise Mobius identity and norm weights used in HD6, with prime-to-p cofactors and no good-reduction or power-degree hypothesis. |
| [Whole full-valuation finding](#whole-full-valuation-finding) | [C265v1 critical-depth calculation](../../claims/Yin_C_G0265_v1.md#old-layer-exception-threshold) | All three binomial branches, uniqueness of the critical event, ramification divisibility and the local e_q f_q clock estimate used in HD7--HD10. |
| [Whole full-valuation finding](#whole-full-valuation-finding) | [C256v1 complete norm identities](../../claims/Yin_C_G0256_v1.md#content-versus-ideal-norm) | Sum e_q f_q=d, normalized versus integer valuations, and log R_t<=t m+d log 2 for each original-field norm, used in HD6 and HD11--HD12. |

<a id="whole-full-valuation-finding"></a>
## Complete full-valuation proof finding

No mathematical gap, unresolved used interface or corrective change was found in the complete C867v2 statement and argument at the stated scope.
HD1--HD12 support the all-prime short-clock bound, the conditional quadratic terminal-mass requirement and uniform disappearance of the full S-part when Theta_S=o(log d) and total logarithmic Mahler measure is bounded.
The following checks supply the mathematical grounds for that finding.

### Nonvanishing, original normalization and HD1

Irreducibility and nontorsion imply that P has no root of unity among its conjugates, so each R_k, D_t and det P(Pi_d) is nonzero.
The norms and the absolute determinant are positive integers, giving nonnegative logarithms and valuations.
The k-cycle resultant is exactly R_k in absolute value, with the original d conjugates.
Counting one distinguished k-cycle gives E C_k=1/k for every 1<=k<=d, without requiring independence of the cycle counts.
The finite factorization R_k=product_(t|k)D_t and its p-adic analogue therefore give the two exact harmonic sums in HD1 after k=t j.
There is no replacement of d by a powered-field degree, omission of H_floor(d/t), or exchange of infinite sums.
The prime set may depend on P and d because it is fixed when averaging over Pi_d.

### Complete short-clock estimate HD2

For t<=L, h=t m/d lies in the C147v5 domain because 0<m<=M and LM/d<=exp(-40).
Every D_t is a positive-integer factor of R_t, hence b_t/d<=Phi(t m/d)<=Phi(tM/d).
Writing ell=log(1/h), the logarithmic derivative is

    1/2-5/(2ell)+3/(2ell log ell)>=7/16=a>0

for ell>=40, including the endpoint.
Integrating this inequality from tM/d to LM/d gives the direction Phi(tM/d)<=Phi(LM/d)(t/L)^a used in the proof.
The decreasing positive function x^(a-1)(1+log(d/x)) on (0,d] is integrable at zero, and its value at integer t is at most its integral over (t-1,t).
Its integral through L is exactly

    L^a[(1+log(d/L))/a+1/a^2].

Together with H_floor(d/t)<=1+log(d/t), this proves HD2 with every prime and actual depth already included in b_t.
For fixed M>0, the expression B_M(x) tends to zero as x decreases to zero because its square-root decay dominates the logarithmic factors.
Thus any sublinear L_d eventually satisfies the small-h domain, and the bound is uniform in the arithmetic input for that L_d/d.
The stated rounded d/log log d example has that property for sufficiently large d; it requires no fixed finite clock cutoff.

### Positive mean and HD3

For the chosen fixed epsilon, L=floor(epsilon d) satisfies L/d tending to epsilon, L>=1 and LM/d<=exp(-40) eventually.
Continuity and the strict choice B_M(epsilon)<eta/2 give the same strict inequality for B_M(L/d) at sufficiently large d.
Subtracting the low-clock bound from mu>=eta d leaves at least eta d/2 in the weighted long-clock sum.
For t>L its weight is at most H_floor(d/L)/L, proving the first inequality in HD3.
The estimates L>=epsilon d/2 and floor(d/L)<=floor(2/epsilon) give exactly the second inequality, including its factor 4.
No integral-endpoint assumption is used.
The statement is a necessary mass condition under a supplied positive mean, not an existence assertion for that mean.

### All local depths and HD6--HD7

At q above p, integer ideal valuation contributes f_q ord_q to the rational norm valuation.
With v_q=ord_q/e_q, this is w_q v_q for w_q=e_q f_q, and sum_(q|p)w_q=d.
The residue order o_q is prime to p and at most p^(f_q)-1 because alpha is a unit.
Prime-to-p cofactors preserve a positive depth: in (1+z)^u-1 the linear term has the unique least valuation when p does not divide u and v_q(z)>0.
Applying Mobius inversion before taking the norm isolates exactly the clocks o_q p^j and gives the initial value and consecutive differences in HD6.

In the p-th-power binomial expansion, the last term uniquely minimizes valuation below 1/(p-1), the linear term uniquely minimizes it above that threshold, and only those two terms tie at equality.
This proves all three branches of HD7, including p=2 and fractional ramified depths.
The depth strictly increases, and the output of a critical step is already above the threshold, so there is at most one such step per ideal.
Below the threshold its increment is less than one; above it the increment is one.
Consequently the full initial contribution, the nonnegative excess over one at the unique critical step when present, and one unit of normalized depth at each old clock dominate the entire actual sequence.
No bound on either seed's depth is needed, and the initial seed is not counted again as an old lift.

### Degree cost and HD8--HD11

For a long initial clock o_q>L, p^(f_q)>=o_q+1>L+1 yields w_q>=f_q>log(L+1)/log p.
Summing the positive weights w_q to d proves HD8 even when its real upper bound exceeds the number of ideals trivially available.

At a critical step r, every preceding step is strictly below threshold, so u_0=1/[p^(r-1)(p-1)].
The positive integer e_q u_0 implies p^(r-1)(p-1) divides e_q.
Thus p<=e_q+1 and p^r<=p e_q/(p-1).
Combining o_q<=p^(f_q)-1 with p<=2^(e_q) and e_q p<=2(2^(e_q)-1) gives

    o_q p^r<=e_q p sum_(j=0)^(f_q-1)p^j
             <=2(2^(e_q f_q)-1).

For the elementary e_q bound, e_q(e_q+1)<=2(2^(e_q)-1) holds at e_q=1,2 and propagates using e_q+1<=2^(e_q).
The geometric sum then cancels its denominator 2^(e_q)-1 exactly.
Hence a critical clock exceeding L consumes w_q>log(L/2+1)/log 2, proving HD9--HD10.
This is the actual local e_q f_q, not a splitting-field ramification index, and the single-critical-event property justifies counting each ideal once.

Each seed contributing at t<=d is a nonnegative part of b_t, so it is bounded by log R_t<=t m+d log 2<=d(M+log 2).
The norm upper bound follows directly from multiplying |alpha_i^t-1|<=2 max(1,|alpha_i|)^t over the original conjugates; the final comparison uses t<=d and m<=M.
Multiplying the seed counts by the long-clock weight bound H/L and dividing by d yields exactly HD11.
Coincident clocks can only make this estimate less sharp; they cause no missing contribution.

### Geometric tails, HD5 and HD12

For each q, if t_0 is its first old clock larger than L, the infinite reciprocal tail is

    sum_(j>=0)1/(t_0 p^j)=p/[(p-1)t_0]<=2/L.

The actual finite tail through d is smaller, and each harmonic factor is at most H=H_floor(d/L).
Summing w_q over q above p therefore gives HD12 with the factor 2H log p/L.
Adding the long initial seeds, long critical excesses and the long slope-one envelope, and using HD2 for the entire actual low-clock contribution, proves HD5.
All logarithmic denominators are positive for L>=1.
L=d simply leaves no actual long clocks, and the still nonnegative displayed upper bound remains valid.
For S empty, both prime-budget terms vanish and Y_S=0, as claimed.

### Uniform limit HD4 and failure scope

Fix M and a prescribed nonnegative q(d)=o(log d).
For any fixed admissible epsilon>0, choose L=floor(epsilon d).
Eventually d/L and H are bounded by constants depending only on epsilon, while log(L+1) and log(L/2+1) are asymptotic to log d.
Since s log 2<=Theta_S<=q(d), both seed terms in HD5 tend uniformly to zero over every allowed P and S.
The remaining slope term is at most 2H q(d)/L and also tends uniformly to zero.
Thus the supremum of the expectations has limit superior at most B_M(epsilon).
Sending epsilon to zero proves uniform convergence of the full normalized expectation, with the limits taken in the required order.
Nonnegativity gives delta Pr(Y_S/d>=delta)<=E(Y_S/d), proving the probability conclusion for every fixed delta>0.
This reasoning allows arbitrarily large actual initial and critical valuations, bad primes, all local multiplicities and all Smith layers contributing to the determinant valuation.

The conclusion is restricted to irreducible nontorsion units, bounded total logarithmic Mahler measure, the original degree-size uniform permutation ensemble, and deterministic prime budgets in the stated range.
It does not inherit the wider polynomial domain of C867v1, bound unrestricted prime budgets, establish a positive determinant mean, or create the terminal mass required by HD3.
In particular, it rules out the proposed small-prime depth mechanism at its quantified scope without resolving or refuting the unrestricted G0001 contract.
No novelty, native computational evidence, proof-assistant verification or new original external-source audit is claimed.
Claim adoption remains a separate decision by the responsible coordinator.
