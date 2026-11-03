---
author: Yin
---

# Ste77-U001: degree-only primitive ideals and the rational-prime boundary

Date: 2026-10-07.
Source inspection and direct interface checks by assigned AI ms25_source for Yin during [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).
Bibliography.

<a id="ste77-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: C. L. Stewart, *Primitive Divisors of Lucas and Lehmer Numbers*, Chapter4 in A. Baker and D. W. Masser (eds.), *Transcendence Theory: Advances and Applications*, Academic Press, London and New York, 1977, pp.79--92. Author-hosted scan [Ste77.pdf](../../../literature/pdf/Ste77.pdf), 709375 bytes, 14 PDF pages.

Passages: Theorem1 and definition p.79/PDF1; height normalization and Lemma3 p.85/PDF7; Lemma4 and equations(11)--(12) p.86/PDF8; equation(13) and proof p.87/PDF9; conclusion of Theorem1 p.88/PDF10.

Inspection: Identity, page count, hash and author bibliography checked. Printed79--88 were rendered and visually read; the PDF has no usable text layer. Theorem1, Lemmas3--4 and the displayed analytic estimates are accepted external inputs at the boundaries stated below. Their direct unit specialization, ideal/rational-prime distinction, and two intermediate-display normalization issues were checked. No recursive audit of Baker, Schinzel, Blanksby--Montgomery or prime-distribution references is claimed.


**Read and accepted at statement scope; direct finite interfaces audited.**
This is not a full proof audit of the chapter or its external analytic inputs.
The later Lucas/Lehmer classification theorems are not adopted.

<a id="ste77-theorem-one"></a>
## The exact general theorem

Let K be a number field, A and B nonzero elements of its full ring of integers, and assume the principal ideals (A) and (B) are coprime.
Suppose A/B is not a root of unity and put

    d=[Q(A/B):Q].

Theorem1 on p.79 says that A^n-B^n has a primitive prime ideal divisor for every integer

    n > max{2(2^d-1), exp(452) d^67}.                           (1)

The second term is the product exp(452)*d^67, not exp(452*d^67).
The scan makes the exponent placement unambiguous.
A prime ideal q of O_K is primitive here precisely when it divides A^n-B^n but does not divide A^j-B^j for any integer 0<j<n.
This is a statement about prime ideals in the ambient field K.
The degree in (1) is the degree of the ratio, not necessarily [K:Q].
The introduction denotes the latter ambient degree by l.

There is no assumption that all complex conjugates avoid the unit circle.
The source handles their logarithmic small factors through its linear-form estimate.
Taking K=Q(alpha), A=alpha and B=1 therefore applies to every nontorsion algebraic unit, including units with unit-circle conjugates.
No power-degree-preservation, reciprocity, Perron or small-Mahler hypothesis is necessary.

For a larger ambient field, the same residue order is preserved under extending a prime ideal of Q(alpha), since the residue-field map is injective.
In the unit specialization it is simplest to apply (1) directly in K=Q(alpha), whose degree is then d.

<a id="ste77-imprimitive-bound"></a>
## The imprimitive-ideal bound and its exact norm consequence

Lemma4, p.86, states under the same standing assumptions: if

    n>2(2^d-1)

and a prime ideal q divides Phi_n(A,B) but is not primitive for A^n-B^n, then

    ord_q Phi_n(A,B) <= ord_q(n).                              (2)

Here Phi_n(X,Y) is the homogeneous cyclotomic polynomial, and ord_q is the integer-valued exponent in ideal factorization.
The printed proof consists of a reference to Schinzel's Lemma4; that original proof was not acquired or audited in this unit.
The current research's direct local reconstruction must therefore be recorded as an independent derivation, with attribution to this known interface, rather than a newly discovered general statement.

Let alpha be a nontorsion algebraic unit of degree d, and write

    D_n=|Norm_(Q(alpha)/Q) Phi_n(alpha)|.

If alpha^n-1 has no primitive prime ideal, (2), applied to every prime ideal in its cyclotomic layer, gives

    (Phi_n(alpha)) divides (n),
    D_n divides n^d,                                         (3)

for n>2(2^d-1).
The ideal-divisibility convention is the usual exponent comparison; equivalently n/Phi_n(alpha) is integral.
The last assertion uses the norm in Q(alpha), not a splitting-field norm.
Thus D_n>n^d is a sufficient test for a primitive ideal in this range.
A primitive ideal of alpha^n-1 necessarily divides Phi_n(alpha), by factorization of alpha^n-1 and minimality of n.

<a id="ste77-height-predicate"></a>
## The source's degree/Mahler-dependent sufficient inequality

For the unit specialization set m=log M(alpha)>0,

    C=2^436 (3d)^49,
    q(n)=2^omega(n).

The source's theta(A/B), defined on p.85 using a sum of complex logarithms minus the common ideal norm, equals m for A=alpha, B=1.
It is the logarithmic Mahler measure, not the normalized Weil height m/d.
Equation(12), specialized to this domain, is

    log D_n > phi(n)m-C d(d+m)q(n)log n,                       (4)

in the range n>2(2^d-1).
The source's equation(13) consequently gives the sufficient predicate

    phi(n)/(q(n)log n) > C d(2d/m+1).                          (5)

Indeed multiplying (5) by q(n)log n*m and subtracting the loss in (4) leaves more than C d^2 q(n)log n, which is at least d log n.
Therefore D_n>n^d and (3) implies a primitive ideal.

For clarity, the direct deduction of (4) from the accepted Lemma3 uses the following conservative termwise bound.
Normalize the d conjugates to z_i of modulus at most1, as in Dim16-U001.
The source Lemma3 gives an error between -C(d+m)log(s+1) and log2 for each root at exponent s.
Mobius inversion in (3)'s cyclotomic product therefore yields, for n>1,

    log D_n >= phi(n)m
      -d log2 * #{s|n: mu(n/s)=-1}
      -C d(d+m) sum_{s|n, mu(n/s)=1} log(s+1).                (6)

Both sign classes have q(n)/2 elements.
For n>=3, use log(s+1)<=log(n+1), C(d+m)>=1 and 2(n+1)<n^2 to obtain (4).
Thus the d in the first error term is retained.
The printed intermediate equation(11) appears without this d; we use (6), not that literal termwise display.
The coarser equation(12) needed by the theorem follows with the correct factor.

The source then replaces m by a Blanksby--Montgomery lower bound and uses explicit elementary-prime estimates to obtain (1).
Those original external estimates have not been recursively audited here.
The visible last comparison on p.88 also has its direction reversed: with the stated C, elementary algebra gives

    (200 C d^4)^(5/4)
      = exp((5/4)(log200+436log2+49log3)) d^(265/4)
      < exp(452) d^67                                        (7)

for d>=1.
The scan prints '>' between these two expressions.
For example log2<0.6935, log3<1.1 and log200<5.3 bound the constant exponent by451.9575<452.
These inequalities follow from the positive exponential series.
The corrected '<' is exactly the direction that makes the threshold in Theorem1 sufficient; this display issue does not reverse the theorem's claimed conclusion.

<a id="ste77-rational-prime-boundary"></a>
## What the primitive-ideal conclusion supplies for G0001

A primitive ideal q at index n means that the residue of alpha has exact order n in (O_K/q)^*.
Writing Norm(q)=p^f, one gets

    n | p^f-1,   p does not divide n,   Norm(q)>=n+1.           (8)

It follows that D_n>=n+1 whenever such a primitive ideal exists.
But the underlying rational prime p may already divide an earlier cyclic norm through another prime ideal above p having another residue order.
No statement in (1) supplies a new rational prime at every index.
If one chooses a primitive ideal for each of T distinct indices in K=Q(alpha), those ideals are distinct, and there are at least ceil(T/d) underlying rational primes because there are at most d prime ideals above any rational prime.
This elementary aggregate observation does not make each selected rational prime primitive for the norm sequence.

Neither (1) nor (8) yields the required linear entropy-capture cost.
The first threshold grows with d, and a single ideal gives only the logarithmic mass log(n+1).
Also the elementary upper bound for the cyclotomic layer is

    log D_n <= phi(n)(m+d log2),

from the product over primitive n-th roots of unity.
Substituting only D_n>=n+1 produces no degree-independent positive lower bound for m.
Predicate(5) retains m in its premise; it must not be inverted into a uniform lower bound without new information.
No effective upper bound for the rational prime p in (8), no positive-fraction residue-degree coverage, and no density of primitive ideals at small indices is asserted by this source.

The bounded search also inspected Flatters' arXiv0708.2190v1, Theorem1.4 and the beginning of Section2 online: its sharp rational prime statements concern positive real quadratic units, and norm -1 has permanent failures at n=2 mod4.
That is a useful scope warning, not an adopted theorem for the unrestricted reciprocal core.
It was not selected for acquisition.
Schinzel74/93 were locators for the general ideal theorem; only the quantitative Stewart source was selected.
No latest-status or optimality claim about primitive-divisor bounds is made.

## Actual review

The source agent completed the stated visual inspection, checked the degree, height and ideal conventions, and directly verified (3)--(8) conditional on the accepted source interfaces.
The original linear-form, Blanksby--Montgomery, Schinzel and prime estimate inputs remain external.
The coordinator independently read the complete unit and rendered original pp.79,85--88, checking the actual theorem/lemma statements, both degree conventions, height normalization, the Mobius error and final comparison.
It checked the direct deductions (3)--(8) and found no substantive defect.
Assigned AI review_matrix_completion independently checked those deductions conditional on the stated external interfaces: ideal/norm divisibility, both Mobius sign classes and the d log2 factor, strict coarsening and residual inequality, the exponent 265/4 and constant bound 451.9575<452, distinct ideal/rational-prime counts, and the archimedean cost.
That review found no substantive defect.
It did not inspect the scan, audit the accepted original proofs or run a computation.
The independently developed [C_G265](../../../claims/Yin_C_G0265_v1.md#old-layer-exception-threshold) proves the unit-domain stable-layer refinement without importing Lemma4; its finite-S primitive certificate also uses no premise from this source.
[C_G266](../../../claims/Yin_C_G0266_v1.md#cyclotomic-exact-period-away-from-index) supplies the corresponding exact module/period distinction.
