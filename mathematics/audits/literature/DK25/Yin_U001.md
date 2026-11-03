---
author: Yin
---

<a id="dk25-u001"></a>
# DK25-U001: finite local energy, a conditional criterion and overlapping-field proof repair

Date: 2026-10-07.
Fixed source-unit argument by assigned AI ms25_source for Yin during [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).
The coordinator separately inspected the versioned HTML and independently identified the partition repair.
No new computational experiment or broad literature survey is used.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Anup B. Dixit and Sushant Kala, *A p-adic criterion for Lehmer's conjecture*, arXiv2507.20141v1,27 July2025; retained [DK25.pdf](../../../literature/pdf/DK25.pdf), acquisition,364404 bytes,10 pages. No journal publication verified.

Passages: Printed/PDF p.3 Theorem1.2 and Proposition1.3; p.4 actual-subfield definitions and Theorem1.5/Corollary1.6; pp.5--7 Mahler inequality and complete single-field proof; pp.8--9 multi-field proof.

Inspection: Versioned HTML read, retained text compared and complete PDF pp.3--9 rendered and visually inspected. The displayed source errors occur in the PDF too. The differently titled author-hosted discovery PDF is not treated as this version.


**Audited within scope** for the complete finite single-field inequality below and Proposition1.3.
**Questioned proof, repaired statement** for Theorem1.5: its original numerical bound follows from the separate partition proof.
**Not adopted** for Corollary1.6 with the original full-membership counts; its cited proof overlaps root pairs.
This is not a claim that Corollary1.6 itself is false.
No full-paper audit or verification of the cited foundational equidistribution literature is asserted.

## Exact finite single-field statement

Let alpha be a nonzero algebraic number of degree d, with primitive integer minimal polynomial P(t)=b_d product_i(t-alpha_i).
Write `m=log M(P)=d h(alpha)` and `Delta=disc P`.
Fix a prime p and an actual finite subfield K of one fixed algebraic closure of Q_p.
Let its ramification index be e, residue degree f, residue size q=p^f, and n_K=ef.
All valuations below extend v(p)=1.
Define

    s=#{i:alpha_i lies in K}.                            (1)

These are distinct characteristic-zero conjugates actually in K, not reduced roots and not prime ideals counted without weights.
The finite estimate underlying source equation(6), p.7, is

    v_p(Delta)>=(s^2/(q+1)-s)/e,

    m >= (log q)/(2 n_K d) * (s^2/(q+1)-s)
                              - (log d)/2.              (2)

The coarser source error term follows by s<=d:

    m >= (log q)/(2 n_K) * s^2/((q+1)d)
                         - (log q)/(2 n_K) - (log d)/2.  (3)

Dividing by d proves Theorem1.2 with an explicit error tending to zero for **fixed K**.
No Northcott step is needed for this finite-to-asymptotic implication.
Constants are not uniform in varying q or n_K merely because the notation suppresses them.

For c>0, the source threshold

    s^2 >= [2(q+1)n_K d/log q] * [c+log(qd)/2]           (4)

implies m>=c.
In fact (3) gives `m>=c+(log q)/2-(log q)/(2 n_K)>=c`.
This verifies Proposition1.3 without an exceptional-degree or limiting argument.
For fixed K and fixed c the threshold is of order sqrt(d log d), not a fixed positive fraction of d.

## Complete finite proof and normalization

Sort the conjugates in a common local splitting field so that `v(alpha_1)>=...>=v(alpha_r)>=0>v(alpha_(r+1))>=...`.
The p-adic Gauss norm of primitive P is1; multiplicativity gives

    v(b_d)=-sum_(j>r) v(alpha_j).

The ultrametric inequality gives the source bound

    v_p(Delta)>=2 sum_(i<j<=r) v(alpha_i-alpha_j)
                    -2 sum_(j>r)(d-j)v(alpha_j).         (5)

Every summand on the right is nonnegative.
Retain only those selected roots lying in K.
Let r' of the selected s roots be integral, let b=s-r', and let N_x count the selected integral roots in residue class x of F_q.
A pair in one residue class has difference valuation at least1/e.
Every selected nonintegral root has valuation at most-1/e.
The b distinct numbers d-j are nonnegative integers, whose sum is at least b(b-1)/2.
(The source calls them positive on p.6; j=d gives zero, and nonnegativity is the sufficient, correct statement.)
Thus

    v_p(Delta)>= [b(b-1)+sum_x N_x(N_x-1)]/e
               =[b^2+sum_x N_x^2-s]/e
               >=[s^2/(q+1)-s]/e.

This proves the first part of(2), including nonintegral alpha.
For integral alpha the empty nonintegral box may be omitted, replacing q+1 by q; for an algebraic unit the zero residue box is also empty, allowing q-1.
These are elementary refinements, not silently substituted into the source theorem.

The Mahler discriminant estimate follows directly here from Hadamard's inequality.
Let V have rows `(1,alpha_i,...,alpha_i^(d-1))`.
Dividing row i by `max(1,|alpha_i|)^(d-1)` gives Euclidean norm at most sqrt(d).
Consequently

    |Delta|=|b_d|^(2d-2)|det V|^2
           <=d^d M(P)^(2d-2),

including d=1.
Taking logarithms gives `log|Delta|<=d log d+(2d-2)m<=d log d+2dm`.
Since `log|Delta|>=v_p(Delta)log p` and `log p/e=log q/n_K`, the second part of(2) follows.
The last weaker denominator2d is valid also when the resulting lower bound is negative; it is not an unjustified replacement of 2d-2 in a signed quotient.

No equality Z[alpha]=O_Q(alpha), field unramifiedness, absence of an order index, or degree preservation of powers is assumed.
The discriminant is the **polynomial** discriminant.
In the integral case its p-valuation can include order-index effects.

## Two literal multi-field proof errors

The v1 definition uses actual generated subfields

    Q_(p,alpha)={Q_p(alpha_i):1<=i<=d},
    S_K(alpha)={alpha_i:alpha_i in K}.

The standing embedding is fixed into one algebraic closure; these are not disjoint embedding labels or isomorphism classes.
The p.8 identity `d=sum_K |S_K(alpha)|` need not hold.

For P(t)=t^3-t-1, irreducibility follows from the rational-root test.
It is a nontorsion algebraic-unit polynomial, and modulo5

    P=(t-2)(t^2+2t+3).

The quadratic discriminant is2 modulo5, a nonsquare.
The factors are coprime.
Hensel lifting gives one root in Q_5 and two roots generating the unramified quadratic field K; K also contains the rational local root.
Hence the generated-field set is `{Q_5,K}`, its full-membership counts are1 and3, and their sum is4, whereas d=3.
This is an exact counterexample to that proof identity, not to the theorem's final lower bound.

Also p.8 explicitly writes a sum of normalized valuations over generated fields (and over primes) equal to v_p(Delta).
For the fixed rational integer Delta, every local valuation extending v_p has the same value v_p(Delta); adding fields duplicates that value.
The identity is not a valid valuation decomposition.
Both faulty displays were visually confirmed on PDF p.8; neither is an HTML-conversion artifact.

The separate [assigned-partition proof](../../../claims/Yin_C_G0255_v1.md#dk25-assigned-local-energy) repairs Theorem1.5 **without changing its stated numerical RHS**.
For Corollary1.6 it supplies only a modified statement using assigned disjoint root counts, not all roots belonging to each field.
That distinction must be retained in every reuse.

## Coverage limits and actual review

The source supplies conditional lower bounds; it supplies no theorem asserting the needed local-root count for every small-Mahler input.
The comparison and ramification boundary are spelled out in the [fixed partition/coverage argument](../../../claims/Yin_C_G0255_v1.md#dk25-assigned-local-energy).
No Chebotarev existence claim is promoted to a uniform prime or linear exponent bound.
The retained Mig78 splitting-prime input already has its own more specific hypotheses and is not newly adopted from this preprint's reference to it.

The drafting agent read all passages listed above, checked the complete single-field proof for integral and nonintegral inputs, and independently identified the disjoint-assignment repair.
The coordinator read the complete versioned HTML proof, visually checked PDF pp.7--8, and checked the assembled audit and finite proof in full, including the direct Hadamard derivation.
The coordinator independently derived the same partition repair and is therefore a contributor to that repair, not its independent reviewer.
Assigned AI review_matrix_completion separately read the complete finite source-audit proof interface and the retained source text definitions and faulty p.8 displays.
That independent review passed the nonintegral Gauss-norm proof, finite threshold, overcount example and partition interface.
A final reread also checked the added direct Hadamard proof, including primitive nonmonic P and d=1.
This review did not include a new PDF visual inspection or audit of external foundational sources.
Other sections and external cited proofs are outside the adoption.
