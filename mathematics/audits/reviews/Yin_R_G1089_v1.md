---
author: Yin
---
# Independent whole-proof review of the uniform first-Smith-layer ceiling

Review time: 2026-11-05T09:01.
Human record author: Yin.
This is an independently organized first whole-proof inspection of [C867](../../claims/Yin_C_G0867_v1.md#statement), including its complete [argument](../../claims/Yin_C_G0867_v1.md#argument) and scope paragraphs.
The reviewer did not contribute to the proof and received no proof-development discussion, exploration notes, author explanations or earlier C867 review conclusions.
The supplied inputs were the fixed candidate, the review assignment, applicable rules and operational authorization facts.
The reviewer formed the mathematical findings directly from the candidate, then matched the standard PID input against the existing source inspection identified below.
The final wording specifying nonzero Q in the cycle-module lemma was reread and checked before this finding was recorded.
No substantive repair was supplied by this reviewer.
The actual shared erratum was read and contained no entries.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Exact statement](../../claims/Yin_C_G0867_v1.md#statement) | All hypotheses, FS1-FS4, uniform convergence, empty prime set and conditional determinant interpretation. |
| [Whole-proof finding](#whole-proof-finding) | [Complete argument](../../claims/Yin_C_G0867_v1.md#argument) | Entire cycle-module, root-order capacity, multiplicity-stratum, harmonic, probability and Smith-form argument, including the nonzero-Q qualification. |

## Obligations and decisive checks

The monic hypothesis preserves degree d after reduction at every prime, and P(0)=1 or -1 excludes zero roots at every prime.
Thus the multiplicities in the algebraic closure sum to d.
Each root lies in a finite extension of F_p, so its multiplicative order is finite and prime to p.
These facts supply all root-count and divisibility inputs without irreducibility, reciprocity or squarefree reduction.

For nonzero Q, cancellation of g=gcd(P,Q) gives Q|Pf if and only if Q/g divides f.
The resulting kernel is isomorphic as a vector space to F_p[x]/(g), with dimension deg g.
The actual cycle polynomial Q=x^k-1 is always nonzero, including when p divides k.
For k=p^s t with p not dividing t, Frobenius gives x^k-1=(x^t-1)^(p^s), and t x^(t-1) is nonzero at every root of x^t-1.
Consequently the cycle nullity is exactly the stated sum of min(e_beta,p^s), with o_beta|t equivalent to o_beta|k.
The expected number of k-cycles is binomial(N,k)(k-1)!(N-k)!/N!=1/k.
Linearity of expectation therefore proves FS2; cycle-count independence is unnecessary.

For the distinct-root capacity, a finite multiplicative subgroup is abelian, and elements attaining each prime-power factor of its exponent combine to attain the whole exponent.
The root bound for x^E-1 and the attained element of order E then show the subgroup is cyclic.
Hence w_o<=phi(o), with no roots of order divisible by p.
Splitting the weighted sum at R gives a tail contribution at most its root count divided by R+1.
For the low orders, replacing w_o by phi(o)<=o is valid because 1/o-1/(R+1) is nonnegative.
The remaining numerical sum is exactly

    sum_(o=1)^R o(1/o-1/(R+1))=R/2.

Writing a=sqrt(2n) and x=ceil(a), the proposed bound equals a-1/2+(x-a)^2/(2x).
For n>=1, x>=2 and 0<=x-a<1, so this is at most a.
The n=0 case is separately zero, as required for empty multiplicity strata.

The increments Delta_j telescope to min(e,p^s), are nonnegative, and vanish for sufficiently large j.
Because o is prime to p, the conditions o|k and v_p(k)>=j are equivalent to op^j|k.
The corresponding reciprocal sum is H_floor(N/(op^j))/(op^j), including zero when op^j>N.
Thus the displayed harmonic identity is exact; all sums are finite before the harmless geometric upper bound.
For j>=1, a nonzero increment requires e>p^(j-1), its normalized size is at most 1-1/p, and the number of such roots satisfies n_j<=d/p^(j-1).
The same capacity estimate applies separately to every stratum, regardless of overlaps between strata.
Finally,

    (1-1/p) sum_(j>=1) p^(-(j-1)/2)=1+p^(-1/2).

Adding the j=0 contribution gives exactly FS1, including p=2 and arbitrary repeated roots.

For each fixed admissible finite S, weighted linearity of expectation and 2+p^(-1/2)<=2+1/sqrt(2) give FS3.
The nonnegative inequality a 1_(Z_d>=a)<=Z_d gives FS4 without any independence between different prime nullities.
The bound is uniform in P and in the selected sets at a common prime budget: for any deterministic b_d=o(sqrt(d)/log(d+1)), its right side tends to zero uniformly over all admissible P of degree d and all S with Theta_S<=b_d.
This follows since H_d<=1+log d and (1+log d)/log(d+1) is bounded for d>=1.
No joint coupling of permutations at different d is required for this convergence-in-probability statement.
The formulas use S as a fixed finite parameter for the permutation experiment; a randomly selected independent S would instead require conditioning on S or averaging its budget.
Permutation-dependent selection is outside the stated conclusion.
The empty S gives Z_N=Theta_S=0 exactly.

Every eigenvalue of a permutation matrix is a root of unity, so the absence of such roots of P implies det P(Pi_N) is nonzero.
For an integer Smith decomposition, the left and right unimodular factors stay invertible modulo p.
Consequently the nullity is the number of nonzero Smith entries divisible by p, while the determinant valuation is the sum of their nonnegative valuations.
The pointwise inequality follows, and summing only over S gives

    Z_N <= log|det P(Pi_N)|/N.

This is a lower certificate and supplies no upper bound for the determinant or its higher p-adic layers.

## Source and dependency boundary

The root-order estimate is proved inside the inspected argument; the motivating L159 reference is not an unchecked logical premise.
The elementary cycle count, harmonic estimate and nonnegative probability inequality were checked directly.
For the standard integer PID and invariant-factor input, the applicable existing source inspection is [Hun74-U005](../literature/Hun74/Yin_U005.md#hun74-u005), especially Hungerford, Algebra, IV.6.10-IV.6.13, printed pp. 224-226.
Its commutative PID and finite-generation hypotheses apply to the integer matrix cokernel here.
This reuses that source statement and inspection at their recorded scope; it does not claim a new inspection of the original textbook or an independent audit of the textbook foundations.
No specialized external theorem is needed for FS1-FS4.
No priority or literature-novelty conclusion was inspected or inferred.

## Whole-proof finding

The exact C867 statement and its complete final argument are mathematically valid at the stated scope.
All required interfaces, constants, quantifiers, repeated-root cases and relevant degenerate cases were checked, and no unresolved mathematical gap remains in this candidate.
The result applies to every monic integer P of degree at least one with constant term 1 or -1, every positive N and every prime, with the stated fixed prime-budget convention.
The nonsingularity and determinant interpretation require the separately stated absence of roots of unity; FS1-FS4 do not.
This finding supports acceptance of C867 as an intermediate result only.
It does not establish a positive Mahler gap, construct a near-one counterexample, control higher Smith layers, or complete the unrestricted [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract).
