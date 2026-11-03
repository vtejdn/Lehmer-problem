---
author: Yin
---

# DM05: the first explicit escape from the dyadic auxiliary constant

Date: 2026-10-07.
Narrow inspection by assigned AI ms25_source for Yin, during [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Arturas Dubickas and Michael J. Mossinghoff, *Auxiliary polynomials for some problems regarding Mahler's measure*, Acta Arithmetica119(1)(2005),65--79, DOI10.4064/aa119-1-5; publisher PDF,177285 bytes,15 pages; retained [DM05.pdf](../../../literature/pdf/DM05.pdf); acquisition.

Passages: Printed67--71/PDF3--7: Lemma2.1, definitions(4)--(5), Theorem2.2, unit-circle nonvanishing paragraph, F2 and F3 construction. Printed68--70/PDF4--6 were rendered and viewed.

Inspection: Exact factor theorem and F3 interface read; F3's Taylor valuation and circle reduction checked directly below. Later optimized constants and the complete iterative algorithm are not adopted.


Theorem2.2 bounds an integer factor g of an odd-coefficient (more generally all-coefficients-1-mod-m) polynomial f of degree n-1: `log M(g)>=B_m(T) deg(g)/n`, subject to gcd(g,T(t^n))=1.
Here w_m is an integer gcd, with B_m as defined in [Sam07-U001](../Sam07/Yin_U001.md#sam07-u001).
The following explicit auxiliary works for every integral nontorsion alpha satisfying alpha^a congruent to1 modulo2 in its integer ring.

<a id="dm05-u001"></a>
## DM05-U001: exact retained auxiliary

State: **Audited within scope** for this particular auxiliary and its direct integral-congruence application.
The later numerical optimization is not adopted.

Put

    G(t)=(t^2-1)^4(t^2+1),
    Q(t)=5t^4+6t^2+5,
    F(t)=G(t)^4 Q(t).

Then deg F=44 and w_2(F)=2^40.
Indeed in t=1+2x, `(t^2-1)/4=x+x^2`, `(t^2+1)/2=1+2x+2x^2`, and `Q(t)/16=1+4x+9x^2+10x^3+5x^4` are integral primitive polynomials.
Gauss's lemma makes their product primitive after removing exactly `4^16 2^4 16=2^40`.

Writing y=cos(2theta), the exact circle norm is

    ||F||_circle = 2^11 max_{-1<=y<=1}
                      (1-y)^8(1+y)^2 |5y+3|.           (1)

The endpoints and y=-3/5 give zero.
At any other maximum, logarithmic differentiation gives

    55y^2+60y+13=0,
    y_plus/minus=(-30 +/- sqrt(185))/55.               (2)

Thus (1)--(2) are a finite exact algebraic expression for

    B_2(F)=(40log2-log ||F||_circle)/44.                (3)

The source prints `0.4161410261...`.
That decimal is reported as a source value, not as a newly rerun numerical certificate.
Equations(1)--(3), rather than a floating estimate, specify the adopted score.
A direct rational comparison certifies a strict improvement without that decimal.
Let f(y)=(1-y)^8(1+y)^2|5y+3|.
Since 13<sqrt(185)<14,

    -4/5<y_minus<-3/4,       -1/3<y_plus<-1/4.

It follows that

    f(y_minus)<(9/5)^8(1/4)^2=43046721/6250000<7,
    f(y_plus)<(4/3)^8(3/4)^2(7/4)=7168/729<10.

The other candidate values are zero.
Thus ||F||<5*2^12, and

    B_2(F)>(28log2-log5)/44>log5/4,

where the final inequality is exactly 5^12=244140625<268435456=2^28.
These are hand-checked integer and rational inequalities, not a floating-point computation.

All zeros of G are roots of unity; the roots of Q have `t^2=(-3 +/- 4i)/5`, hence modulus1.
Therefore the integral nontorsion nonvanishing test from [Sam07-U001](../Sam07/Yin_U001.md#sam07-u001) applies, with no powered-degree assumption and no upper bound on d.

The earlier G alone yields log5/4: this is exactly BDM07 Corollary3.4, printed355.
Q vanishes at the circle points where G is maximal.
This is the source's explicit mechanism for escaping the restricted dyadic-cyclotomic auxiliary class.
A theorem about optimality **inside** that restricted class cannot imply optimality among all integral auxiliaries.

Actual review: source inspection and the exact reductions above were performed by the drafting agent.
The coordinator read the complete reductions, checked the Taylor expansion and circle critical equation, and visually compared PDF6.
Assigned AI assess_shortness_route independently derived and checked the strict rational bounds above and the integral nonvanishing guard; the coordinator checked those inequalities.
No computation program was run or used.
This independent targeted review does not assert an audit of the whole source.
The source's later F4/F5 constants and algorithmic global behavior remain outside this adoption.
