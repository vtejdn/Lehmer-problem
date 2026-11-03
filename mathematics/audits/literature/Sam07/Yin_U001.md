---
author: Yin
---

# Sam07: the integral factor-congruence interface

Date: 2026-10-07.
Narrow inspection by assigned AI ms25_source for Yin, during [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Charles L. Samuels, *The Weil height in terms of an auxiliary polynomial*, Acta Arithmetica128(3)(2007),209--221, DOI10.4064/aa128-3-2; published publisher PDF, 156150 bytes,13 pages; retained [Sam07.pdf](../../../literature/pdf/Sam07.pdf); acquisition.

Passages: Printed209 height normalization; printed213--214 definitions; Theorem3.1 and Corollaries3.2--3.3, printed214--215/PDF6--7, including proofs.

Inspection: Extracted text read and PDF6--7 rendered and viewed. This unit checks the monic integral interface by a complete direct norm argument. The source's general local approximation theorem and its algebraic-coefficient extension are not proof-audited here.


The source's omega_m is the **logarithm** of the Taylor-coefficient gcd;
DM05 uses omega_m for that gcd itself.
Its mu is the sum of root heights.
For the monic polynomial adopted here this is exactly logarithmic Mahler measure.
No claim about polynomial content is needed.

<a id="sam07-u001"></a>
## Sam07-U001: adopted integral factor interface

State: **Audited within scope** for the integral specialization and direct proof below.
The general source proof is not fully audited.

Let P be the monic minimal polynomial of a nonzero algebraic integer alpha, let d=deg P, and let a>=1 and m>=2 be integers.
Suppose

    (alpha^a-1)/m is an algebraic integer.                 (1)

For a nonconstant T in Z[t], define

    w_m(T)=gcd{m^j T^(j)(1)/j!:0<=j<=deg T},
    B_m(T)=(log w_m(T)-log ||T||_circle)/deg T.            (2)

If T(alpha^a) is nonzero, then

    log M(P) >= (d/a) B_m(T).                            (3)

Write T(1+mx)=sum_j c_j x^j.
Every c_j is divisible by w_m(T).
Thus T(alpha^a)/w_m(T) is an algebraic integer.
Its nonzero norm from Q(alpha) is an integer of absolute value at least1, so

    |Norm T(alpha^a)| >= w_m(T)^d.

The maximum principle, also applied to the reversed polynomial, gives |T(z)|<=||T||_circle max(1,|z|)^deg T for every complex z.
Multiplication over the d embeddings gives the upper bound `||T||_circle^d M(P)^(a deg T)`, proving(3).
Powered conjugates may coincide; neither distinctness nor powered degree is used.

In the directly computable monogenic-order case, (1) follows from

    P mod m divides t^a-1 in (Z/mZ)[t].                  (4)

Because P is monic, choose a monic integer lift Q of the quotient.
The polynomial f=PQ has degree a and f congruent to t^a-1 modulo m.
Samuels Corollary3.2 applied to the factor P gives precisely(3), provided gcd(P,T(t^a))=1.
This is equivalent to the nonvanishing condition for irreducible P.
It also handles the factor t-1 in P mod m; there is no need to form an odd-coefficient completion or double a.
If P is nontorsion and every root of T has modulus1, the condition is automatic: a zero T(alpha^a) would make every conjugate of the algebraic integer alpha^a have modulus1, contradicting Kronecker.

Corollary3.3 is separately a totally-p-adic **unit** result, with denominator `(p-1)deg T`; it does not by itself cover merely a positive fraction of roots with low residue degree.
That weaker coverage is addressed by the direct cyclic-norm argument, not silently attributed to this source.

## Use and remaining boundary

This interface applies to the original Mahler measure and hence to G0001's original companion-flow algebraic entropy.
If a<=Cd and B_m(T)>0, it gives the uniform gap B_m(T)/C.
Existence of such a linear congruence exponent for all small-Mahler inputs remains a separate, unproved arithmetic coverage obligation.
The theorem does not establish it.
No current-best or novelty claim is made.

Actual review: the drafting agent checked the exact normalization, source statement and complete direct proof above.
The coordinator independently read this complete direct argument, checked the Taylor-gcd norm, all embedding multiplicities and monic quotient lift, compared the extracted definitions and Corollary 3.2, and visually checked PDF7.
No defect was found within this scope.
The source's general approximation theorem remains outside this audit.
Kronecker and the elementary height normalization are retained classical inputs, not new proof audits.
