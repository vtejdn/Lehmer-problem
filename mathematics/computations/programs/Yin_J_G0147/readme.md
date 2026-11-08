---
author: Yin
---

# Height-free reciprocal shell census at three prime conductors

<a id="whole-shell"></a>
## The complete finite result

Let \(D=p+1\), \(p\in\{13,17,19\}\), and put \(n=(p-1)/2\).
Take every monic reciprocal integer polynomial \(P=z^{D/2}Q(z+z^{-1})\) of exact degree \(D\) and constant coefficient one.
Write \(B\) for the monic trace polynomial with \(z^n B(z+z^{-1})=1+z+\cdots+z^{p-1}\).
The chamber requires \(Q(-2)/B(-2)<0\) and the residues \(Q(b)/B'(b)\) at the increasing roots of \(B\) to consist of a nonempty strictly negative block followed by a nonempty strictly positive block.
Repeated roots of \(P\), cyclotomic factors and both types of exceptional trace roots are allowed.
All measure comparisons concern the original \(P\).
No bound on coefficient height, resultant or unit exponents is imposed.

| \(p\) | \(D\) | After the 32 moment tests | \(M=1\) | Survivors with \(M>6/5\) | All \(1<M<6/5\) | Strict shell and chamber | Also \(\lvert\operatorname{Res}(B,Q)\rvert=1\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 14 | 2955 | 2257 | 660 | 38 | 0 | 0 |
| 17 | 18 | 21726 | 10133 | 11261 | 332 | 0 | 0 |
| 19 | 20 | 64799 | 20399 | 43550 | 850 | 1 | 0 |

These are counts of distinct polynomials, including all cyclotomic padding at each exact degree.
Every surviving input was assigned a strict side or the value one.
The unit column therefore covers arbitrary units of the trace order and every integer shift in \(Q=(t-a)B+C\), including the [circular-unit tests](../Yin_J_G0146/readme.md#unit-law).

<a id="unique-input"></a>
## A positive atom with nonunit resultant

The unique chamber input has leading-to-central coefficient vector
\[
                  (1,-3,4,-4,3,-1,-1,3,-4,4,-4).
\]
There is one negative residue and there are eight positive residues in increasing pole order.
The resultant has absolute value \(4313=19\cdot227\).
One has \(P(-1)=4\) and \(P=(z-1)^2 S(z)\) with \(S\) irreducible of degree 18.
Its degree-nine trace polynomial is
\[
        t^9-t^8-8t^7+7t^6+20t^5-14t^4-17t^3+8t^2+4t-1 .
\]
It has eight roots in \((-2,2)\) and one above \(2\), by integer Sturm counts.
The latter trace contributes the sole exterior root.
Rational sign evaluations of \(S\) give
\[
                1.18836814<M(P)<1.18836815 .
\]
The first ten coefficients of \(S\) agree term for term with entry 2 in [Boyd's Salem-number table](https://www.cecm.sfu.ca/organics/papers/boyd/paper/html/Salem.html), attributed there to his 1977 paper *Small Salem numbers*.
This identifies the measure as an existing Salem number, while the calculation above determines its occurrence and uniqueness in this chamber.
For a seed-free discrete probability law, choose the ten free reciprocal coefficients independently and uniformly in \(\{-4,\ldots,4\}\).
The probability of belonging both to this chamber and to \(1<M(P)<6/5\) is exactly \(9^{-10}\).
Under a second law that samples uniformly from the full strict degree-20 shell, the chamber has probability \(1/850\).
The input uses a real exterior root and supplies one fixed radius.
Arbitrarily small positive shells or a nonreal exceptional pair require separate evidence.

<a id="newton-cover"></a>
## Exhaustion by trace moments

Set \(R=6/5\).
Write \(s_k=\sum\alpha^k\) over all the roots of \(P\), with multiplicities, and \(T_k=\sum\cos(k\arg\alpha)\).
Integrality gives \(s_k\in\mathbb Z\).
Pairing an exterior root with \(1/\bar\alpha\) and taking real parts bounds the difference of the two sums by
\[
 |s_k-T_k|\le E_k=R^k+R^{-k}-2\qquad\text{if }M(P)\le R .
\]
In fact each corresponding radial pair contributes at most \(e^{ku}+e^{-ku}-2\), where \(u=\log|\alpha|>0\).
This function of \(u\) is superadditive on \(u\ge0\), since its derivative is increasing and its value at zero is zero.
The sum of the \(u\)'s is at most \(\log R\).
Unit roots contribute no error after taking real parts.
Thus \(|s_k|\le D+\lfloor E_k\rfloor\).

For the first \(D/2\) moments the enumeration also uses the nonnegative trigonometric polynomial \(|1+w+\cdots+w^m|^2\).
Summing its values on \(w=\omega e^{ih\arg\alpha}\) removes sine terms by conjugation.
For any positive integer \(h\) and \(m\) with \(hm\le D/2\), put \(w_j=(m+1-j)2\Re(\omega^j)\).
For \(\omega\) of order \(1,2,3,4,6\) with argument \(2\pi/\operatorname{ord}(\omega)\), the \(w_j\) are integers.
A necessary condition is
\[
        (m+1)D+\sum_{j=1}^m w_j s_{hj}
                +\left\lfloor\sum_{j=1}^m |w_j|E_{hj}\right\rfloor\ge0 .
\]
The floor is valid because the other terms are integral.
The code omits a test with zero final weight, which only relaxes pruning.
If \(P=z^D+a_1z^{D-1}+\cdots+1\), Newton's identity fixes
\(s_k=-k a_k-\sum_{j=1}^{k-1}a_j s_{k-j}\) for \(k\le D\).
Iterating over every integer \(a_k\) whose new \(s_k\) satisfies the necessary bounds reaches every admissible prefix.
At \(k=D/2\) reciprocity determines the remaining coefficients, and the absolute moment tests continue through \(k=32\).
Each distinct \(P\) occurs at most once.

All floors involving \(E_k=(6^k-5^k)^2/30^k\) use integer arithmetic with common denominator \(30^{32}\).
For prefix moments \(k\le10\), \(|s_k|\le26\) on every visited branch.
The formal identity \(\sum a_i z^i=\exp(-\sum s_j z^j/j)\) bounds \(|a_i|\) by the coefficient of \((1-z)^{-26}\) up to the visited order, hence by \(\binom{35}{10}=183579396\).
Every earlier moment in a tail test is at most \(20+\lfloor E_{32}\rfloor<362\).
The sum of the absolute values of the products in any Newton test and its initial term is below \(2^{42}\), safely within exact binary integer arithmetic.
In prefix divisions the denominator is at most 10 and distinct nonintegral quotients are at distance at least \(1/10\) from an integer.
The smaller linear trigonometric filters also have integer coefficients of absolute value at most 20 and exact integer numerators.
These bounds justify the use of ordinary JavaScript numbers for the enumeration outside the rational allowances.

<a id="measure-and-chamber"></a>
## Exact measure and chamber decisions

A reciprocal monic polynomial of even degree is a trace lift, so the multiplicities of \(1\) and \(-1\) as roots are even.
Kronecker's theorem identifies neutral inputs as products of \((z-1)^2,(z+1)^2\) and the cyclotomic polynomials of orders \(h\ge3\) with \(\varphi(h)\le D\).
The inequality \(\varphi(h)^2\ge h/2\) follows by multiplying \(\varphi(q^e)^2/q^e=q^{e-2}(q-1)^2\) over the prime powers dividing \(h\).
Thus the neutral product enumeration stops at \(h=2D^2\).
The census verifies that every neutral product at degree \(D\) survives the prefix enumeration.

For each remaining survivor \(M>1\).
A negative value of \(P(6/5)\) or \(P(-6/5)\) certifies a real root of modulus above \(6/5\).
Otherwise square the roots repeatedly with the [integer Graeffe routine](../Yin_J_G0144/pilot.py).
At step \(s\), the resulting monic polynomial with coefficients \(b_j\) has measure \(M(P)^{2^s}\) between \(\max_j |b_j|/\binom Dj\) and \(\sqrt{\sum b_j^2}\).
The lower bound is the elementary symmetric coefficient estimate, and the upper bound follows from Jensen's inequality and Parseval's identity on the circle.
All comparisons with \((6/5)^{2^s}\) are strict integer comparisons.
An unresolved input aborts the run.

For a strict survivor the program reconstructs \(Q\) using \(V_0=2,\ V_1=t,\ V_{j+1}=tV_j-V_{j-1}\).
It computes the exact integer resultant and tests the endpoint by exact evaluation.
At coprime inputs, rational isolating intervals for the poles and interval Horner evaluation certify the signs of \(Q(b)\).
The signs of the derivative alternate from the largest pole, where the derivative of the monic denominator is positive.
An undecided sign aborts the run.
For the unique input the separate factorization, real-root counts and two rational sign tests verify its whole-measure interval.

<a id="replay"></a>
## Reproduction

From this directory, run the following command with Python, SymPy and Node.js on the executable search path.
The Python program calls the JavaScript enumerator once per degree and then verifies the classifications and the unique chamber vector.

~~~text
python -B census.py 14 18 20
~~~

The two local entry points are [the Newton enumeration](newton.cjs) and [the exact census](census.py).
