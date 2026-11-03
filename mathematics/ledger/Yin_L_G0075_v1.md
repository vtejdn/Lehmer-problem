---
author: Yin
---

<a id="chebotarev-period-cost"></a>
# G0001: standard split-prime bounds do not supply the logarithmic period budget

Date: 2026-10-07.
Current complete proof and exact statement: [responsible claim](../claims/Yin_C_G0259_v1.md#chebotarev-period-cost).
The original mathematical input below remains fixed; its full historical review account is retained at the review entrance below.
Bounded source comparison and direct deductions by assigned AI ms25_source for Yin.
No parameter scan or numerical experiment is used.
Source statements and actual inspection limits are in [BS96-U001](../audits/literature/BS96/Yin_U001.md#bs96-u001) and [Fio19-U001](../audits/literature/Fio19/Yin_U001.md#fio19-u001).

The changed next-step conclusion is specific: do not use a generic effective Chebotarev theorem as the missing coverage input for [L G0070](Yin_L_G0070_v1.md#identity-period-log-prime-budget).
Its degree/discriminant cost is insufficient.
Conversely, the known general-field lower examples do not refute small-Mahler coverage: the selected hard family has no integral primitive generators with bounded Mahler measure.
A new input must exploit the small-Mahler generator, or measure its actual residue order without demanding complete splitting of its entire field.

## Target and exact field normalization

Let alpha be a nontorsion algebraic unit, K=Q(alpha), d=[K:Q]>=2, and P its monic minimal polynomial.
Set m=log M(P)=d h(alpha).
Let O_K be the maximal order and

    T_p=min{a>=1:alpha^a=1 in (O_K/pO_K)^*}.

The target under discussion is a constant C independent of the input and some prime p, allowed to depend on it, satisfying

    T_p<=C d log p.                                           (1)

By L G0070 this suffices for a uniform positive algebraic-entropy gap, including its separate p=2 estimate.
No power-degree preservation is needed for the norm inequality behind (1).

Let L be the normal closure of K, n=[L:Q], and D_L its absolute field discriminant.
For a prime unramified in L, complete splitting in K is equivalent to Frobenius acting trivially on every embedding of K in L.
The action of Gal(L/Q) on these embeddings is faithful: an automorphism in its kernel fixes every conjugate of K and hence their compositum L.
Thus this is the identity Frobenius class in Gal(L/Q), and it is equivalent to complete splitting in L.

If one starts from a completely split prime of K, it is also unramified in L: every local conjugate extension of K is trivial, so their compositum is trivial.
Therefore the equivalence is not lost at a prime dividing the power-basis index.
A mere degree-one prime ideal in K is insufficient; it supplies only one local embedding, rather than splitting all d components.

Complete splitting gives O_K/pO_K=F_p^d, hence T_p divides p-1.
It follows that a supplied split prime p<=B d log d gives (1) with the conversion already proved in L G0070.
This is precisely the missing existence assertion, not a consequence of splitting itself.
The checked Mig78 Corollary2 input likewise assumes an odd completely split prime p<=d log d; it does not locate one.
The weakened unramified-only survey quotation was already corrected in [Smy08-U002](../audits/literature/Smy08/Yin_U002.md).

For comparison, the available elementary height control is

    log|D_K|<=log|disc P|
              <=d log d+(2d-2)m.                              (2)

The first inequality uses disc P=D_K[O_K:Z[alpha]]^2; the second is the directly checked Hadamard bound in [DK25-U001](../audits/literature/DK25/Yin_U001.md#dk25-u001).
Neither discriminant in (2) may be substituted for D_L in a theorem stated for L.
In general d<=n<=d!, and the upper degree bound follows from the faithful permutation action.
No bounded ratio n/d is inferred from m bounded, or from h(alpha)=m/d small.

## What the standard conditional theorem actually supplies

Bach--Sorenson Theorem5.1, printed p.1729, gives under its ERH hypotheses a prime in any prescribed conjugacy class of a Galois extension, with

    p<=U=(4 log D_L+2.5n+5)^2                                (3)

when the base is Q.
Here n and D_L belong to the top field L.
The source assumes the relevant Dedekind zeta functions of L and Q have no nontrivial zero with real part greater than1/2.
The theorem and this source normalization are accepted only at statement scope; its analytic proof and numerical verification of the displayed constants have not been independently audited.

Take the identity class.
From this black box alone the safe certificate for (1) is bounded by

    T_p/(d log p)<=(p-1)/(d log p)<=(U-1)/(d log U),           (4)

since (x-1)/log x is increasing for x>1.
The last expression does not stay bounded as a function of the guaranteed input range: U>=(2.5d+5)^2, and monotonicity gives a lower bound of order d/log d for the rightmost expression in (4).
This is a failure of that upper-bound certificate.
It is not a lower bound on the actual least split prime or actual T_p.

Even in the favorable additional case L=K and m<=m_0, (2) gives log D_L=O_(m_0)(d log d), so the rightmost expression delivered by (3)--(4) is at most of order d log d, rather than O(1).
The asymptotic rational-base variant of the same source gives p<=(1+o(1))(log D_L)^2; this still has square-discriminant-log scale.
Reducing a numerical constant in (3) cannot repair the missing uniform degree quantifier.

Unconditionally, the standard polynomial-discriminant bound p<=D_L^A for an absolute A>0, reported with its original reference in Fiori's retained introduction, is still weaker for this purpose.
This comparison uses only that general shape.
It is not a claim that A is the best current exponent.
No third theorem or paper is adopted to optimize A.

## A genuine general-field obstruction, and its small-Mahler exclusion

Fiori's published Theorem1 constructs infinitely many Galois fields whose least completely split prime has scale at least (log D_L)^(2+o(1)).
The following elementary deductions from the source's family show both its force and its limit for G0001.

To avoid conflict with the target degree d, write D for the absolute discriminant of an imaginary quadratic field F.
Let H be its Hilbert class field, h_F its class number, and n_H=[H:Q]=2h_F.
The inspected source interfaces give

    D_H=D^(h_F),       p_split(H)>=D/4,                       (5)

and an infinite chosen family with D tending to infinity and

    h_F<=C_0 sqrt(D)/log log D                               (6)

for one absolute C_0 and all sufficiently large family members.
The analytic extreme-value input used for (6) remains an external source theorem.
The elementary norm lower bound in (5) is checked: a principal degree-one prime in F is the norm of x+y sqrt(-D), where y is a nonzero half-integer, hence p=x^2+D y^2>=D/4.
Hilbert-class-field reciprocity supplies principality; its original class-field-theoretic proof is not re-audited here.

As x/log x is increasing for x>e, (5)--(6) imply

    p_split(H)/(n_H log p_split(H))
       >= D/[4 n_H log(D/4)]
       >= sqrt(D) log log D/[8 C_0 log(D/4)] --> infinity.    (7)

Thus no bound p_split<=C n_H log p_split can hold for all number fields with a universal C.
This concerns the complete-splitting route.
It does not give a lower bound on T_p for arbitrary primes or for a particular generator of H.

More decisively for scope, let gamma be any integral primitive generator of H.
Its degree is n_H.
By (2) applied to gamma and the exact discriminant in (5),

    n_H log(D)/2 <= n_H log n_H+(2n_H-2)m(gamma),

so

    m(gamma)>=n_H/(2n_H-2) log(sqrt(D)/n_H)
             >=n_H/(2n_H-2)
                    *[log log log D-log(2C_0)] --> infinity. (8)

The last conclusion holds uniformly over all integral primitive generators, not just over a chosen defining polynomial.
For sufficiently large D the bracket is positive and the coefficient is at least1/2.
Consequently this particular hard split-prime family cannot be used as a bounded-Mahler counterexample to the proposed coverage.
No source claim about such a counterexample is being made.

## Search outcome and next obligation

The bounded search used exact split-prime, polynomial-order and small-height terms, and compared the existing Mig78, Smy08 and DK25 interfaces.
No located theorem supplies (1) on the irreducible small-Mahler unit core.
A search hit about the least prime that does not split completely concerns the opposite Frobenius condition and supplies no such input.
Statements about height gaps for a fixed totally p-adic field already assume the local containment; they do not choose p with the necessary uniform cost.
DK25 likewise supplies conditional local-root counts rather than their existence.

The useful next question is therefore generator-sensitive: can small m(P) control the minimum, over primes, of the actual maximal-order cost T_p/(d log p), without replacing T_p by the worst possible exponent p-1 of a completely split field?
A positive-density or almost-all-fields theorem would still need an explicit treatment of every exceptional possible small-core family.
No such treatment was obtained in this pass.
Searching for another field-only Chebotarev constant is not the next step.

Complete splitting is also stronger than the cyclic-norm method itself needs.
Contributions from different primes and different proper subsets of the roots can be added in one norm.
[J G0011](../computations/programs/Yin_J_G0011/readme.md) retains the coordinator's separate degree22 certificate

    m(P)>=log(5^4*7^2*11^6*23^2/2^22)/120>0.

Its computation and valuation proof belong to that separate retained work and were not independently reproduced in this source comparison.
This is an illustration of a different arithmetic target, not a claim of complete splitting or of uniform coverage on all small-core inputs.
The next mechanism should therefore permit partial returns aggregated across primes, rather than require one prime to split the entire field.

This is a bounded negative source comparison, not a proof that no applicable theorem exists.
The source search is stopped.

## Actual review

The complete original contribution, source-boundary and review account is retained in [R530](../audits/reviews/Yin_R_G0530_v1.md#historical-period-author-finding).
The original date and inspected scopes remain unchanged; current findings are separate from the original reported relationship labels.
