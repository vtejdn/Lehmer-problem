---
author: Yin
---

<a id="ms26-u001"></a>
# MS26-U001: complete length-five Salem classification

Host locations in historical commands and records below are normalized; relative historical paths, arguments and execution facts are unchanged.
This records no new run.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: MS26, [retained PDF](../../../literature/pdf/MS26.pdf), arXiv:2605.19013v1, 18 May 2026; 21 pages.

Passages: Definitions p.1, Theorem 1 p.2, Table 1 p.3, relevant conclusions/proofs of Lemmas 2.1 and 2.2 pp.3--4, and Section 3 pp.8--10; printed and PDF pages coincide.

Inspection: 2026-10-07, assigned AI assess_shortness_route for Yin read the complete unit and visually inspected pp.3,4,8,9,10. Coordinating AI checked the argument and script, visually inspected pp.8--10, and executed a separate exact verification; the original review arrangement is retained at its exact scope in R_G524. Three local source slips are explicitly repaired below. Remaining paper outside scope.


## Source and adopted unit

James McKee and Chris Smyth, *Short Salem polynomials*, [arXiv:2605.19013v1](https://arxiv.org/abs/2605.19013v1), 18 May 2026.
The inspected [PDF](../../../literature/pdf/MS26.pdf) has 21 pages; PDF and printed page numbers coincide.
Its definition on p.1 permits repeated cyclotomic factors in a Salem polynomial.
Theorem 1 on p.2 states the complete classification of 17 length-five Salem polynomials, representing 13 Salem numbers, listed on p.3.
The smallest is Lehmer's number.

The adopted unit comprises only those definitions, Theorem 1/Table 1 as a classification of polynomials and their Salem numbers, Lemma 2.1's between-consecutive-zeros conclusion (pp.3–4), Lemma 2.2 (p.4), and Section 3 (pp.8–10), with the explicit corrections below.
The factorisation column of Table 1 is not adopted wholesale by this check: the finite verification instead identifies equal Salem roots by exact polynomial gcds and verifies the Lehmer factorisation separately.

Read the full text of this unit.
Visually inspected PDF pp.3,4,8,9,10 using local scratch renders.
The exact source PDF is permanently retained; disposable page renders are not a separate source artifact.

## Local corrections needed for the adopted reasoning

These are present in the PDF, not only in the HTML transcription.

1. **P.4, Lemma 2.2 proof:** after replacing `i'` by `i'−rb`, replace `j'` by `j'−ra`, in both occurrences.
   The printed plus sign does not preserve `i'a−j'b=1`.
   This correction preserves the claimed lemma: multiply both modified indices by a common sign to arrange `0<i<b/2`; then `j=(ia−epsilon)/b>0`.
   Taking the odd member of `a,b` as `a` gives `j<(a+1)/2`, hence `j<a/2`.
   Interchanging `a,b` if necessary just reverses the sign in the conclusion.
2. **P.10, first paragraph:** the inherited bounds are `2 ell < 2n−k` and `2m<k`, not the two swapped denominators printed there.
   Both doubled endpoints are therefore inside `(0,2pi)`.
   Their distance `4pi/[k(2n−k)]` is smaller than each of the two grid spacings because `k,2n−k>=3`; hence no third grid zero intervenes.
   The required consecutive positive hump and its estimate survive this correction.
3. **P.10, last paragraph of Section 3:** the terminal enumeration must include `2<=n<=13`, not just the printed `4<=n<=13`, since the degree is `2n` and Table 1 includes degree-four and degree-six polynomials.
   The independent enumeration below uses the complete corrected range and recovers exactly the printed table.

None of these corrections supplies an additional unproved mathematical hypothesis.
They are recorded instead of silently changing the source text.

## Checks on the analytic reduction

Write a neutral completion of a Salem minimal polynomial as `q`.
An odd length precludes `q(1)=0` and `q(-1)=0`, since evaluations modulo 2 equal the length.
Consequently a length-five such `q` is reciprocal of even degree, with leading and constant coefficient 1.
Its value at 1 is negative: the real Salem reciprocal pair contributes a negative factor, the remaining conjugate pairs a positive factor, and all cyclotomic factors other than `t−1` are positive at 1.
Therefore its interior coefficient mass three is negative.
The central case `t^(2n)−3t^n+1` has `n` expanding roots; for `n=1` its expanding root is quadratic Pisot, so it is not a Salem polynomial.
The remaining form is

\[
q_{n,k}(t)=t^{2n}-t^{2n-k}-t^n-t^k+1,
\qquad 1\leq k<n,\quad n\geq2.
\]

If `g=gcd(n,k)>1`, writing `q=Q(t^g)` and using `Q(1)=-1` shows that an expanding positive root of `Q` lifts to `g` expanding roots.
Thus the Salem case requires `g=1`; no all-power degree-stability assumption is needed here.

On the circle, `q(e^(i theta))=0` is equivalent to

\[
s(\theta)=-4\sin((2n-k)\theta/2)\sin(k\theta/2)=1.
\]

For a product of two sine functions, the logarithmic derivative is the sum of two cotangents, with strictly negative derivative between consecutive distinct zeros.
Its limits are `+infinity` and `−infinity` at the two ends, so there is exactly one critical point on each open interval.
This is the precise part of Lemma 2.1 used; shared zeros can themselves also be zeros of the derivative, so no stronger strict-interlacing assertion is needed.

Rechecked Section 3's gap, amplitude, parity, and root-count arguments:

| Case | A positive hump with maximum strictly below 1 exists when | Remaining bound |
| --- | --- | --- |
| `k=2k'` | `k'(n−k')>pi^2`; this holds for `n>=11` | `n<=10` |
| `k=1` | `8pi/(2n−1)<1`, for `n>=14` | `n<=13` |
| odd `k>=3` | `4pi^2/[k(2n−k)]<1`, for `n>=9` | `n<=8` |

In the first case, reflection about `pi/2` changes the sign of `s`, so a short interval of either sign supplies a positive short interval.
In the last case, a Bezout pair gives adjacent zeros; if their hump is negative, doubling both indices makes their sum even and makes the hump positive.
The corrected grid-spacing argument in item 2 justifies that operation.
Losing an entire positive hump prevents the required `2n−2` unit-circle roots, with multiplicity.
Thus `n<=13` suffices for the final exhaustive check.
A possible tangent root on some other hump does not repair this loss: one hump can supply at most two roots counted with multiplicity.

## Independent exact terminal verification

The retained [computation](../../../computations/programs/Yin_J_G0001/readme.md) owns both executed programs and outputs.
Its [main script](../../../computations/programs/Yin_J_G0001/main.py) uses only Python's standard library.
The retained machine result (`mathematics/computations/outputs/Yin_J_G0001/result.json`) contains all 57 candidate records, including each integer trace polynomial, endpoint values, derivative-gcd degree, and all root counts.

Define `C_0=2`, `C_1=x`, and `C_(j+1)=x C_j−C_(j−1)`.
Then

\[
q_{n,k}(t)=t^n H_{n,k}(t+t^{-1}),\qquad
H_{n,k}(x)=C_n(x)-C_{n-k}(x)-1.
\]

The script examines every coprime `1<=k<n`, `2<=n<=13`.
It uses rational Sturm chains for the square-free part and repeated derivative-gcd layers to count multiplicities, including nonreal-root counts by degree subtraction.
It checks that no endpoint `−2,2,3` is a zero.
A candidate is accepted exactly when `H` has `n−1` roots in `(−2,2)`, one in `(2,3)`, and no other roots, all counted with multiplicity.
In fact all 57 `H` polynomials proved square-free; multiplicity was not assumed.

This criterion is sufficient as well as necessary in this range.
It gives exactly one expanding positive root of `q` and its reciprocal; the two roots belong to the same irreducible factor: all irreducible factors are monic units, so a factor containing the sole expanding root must also contain the sole contracting root.
Every other irreducible factor has all roots on the circle and is cyclotomic by the accepted Kronecker criterion.
The exceptional factor cannot be quadratic: its trace would be an integer in `(2,3)`.
Hence it has a unit-circle conjugate and is a Salem minimal polynomial.

The upper endpoint 3 does not omit genuine Salem candidates.
Every `q` here is monic of coefficient height one.
For `rho>=2`, the leading term dominates all lower terms since `sum_(j=0)^(2n−1) rho^j < rho^(2n)`.
Therefore every root has modulus less than 2.
Its positive expanding root satisfies `tau+tau^(-1)<5/2<3`, as this function increases for `tau>1`.

The exact result is 17 polynomials, with `(n,k)` equal to

```
(2,1), (3,1), (3,2), (4,1), (4,3),
(5,1), (5,2), (5,3), (5,4), (6,1), (6,5),
(7,1), (7,2), (7,3), (8,1), (9,1), (10,1).
```

This is a set-by-set comparison with all 17 polynomials transcribed from Table 1, not merely a matching count.
Exact gcds identify 13 distinct expanding roots.
Rational isolating intervals, refined by 80 bisections, are disjoint between the 13 groups and certify their ordering.
The minimum group consists precisely of `(6,5)` and `(7,3)`.
Exact coefficient multiplication verifies

\[
q_{6,5}(t)=(t^2-t+1)
(t^{10}+t^9-t^7-t^6-t^5-t^4-t^3+t+1).
\]

Thus the minimum is identified exactly as Lehmer's number.
Decimal output is display-only and is not used for acceptance, equality, or ordering.
The script does not certify the preceding analytic reduction; that is a separate hand check recorded above.

Command actually run, exit 0:

```
python -X utf8 -B tmp/g0001-ms26-check/check_length5.py
```

## G0001 interface and exclusions

Combined with the already derived implication `E(p)=2 => L(p)=5`, the verified source unit gives, for a Salem minimal polynomial `p`,

\[
E(p)=2\quad\Longrightarrow\quad M(p)\geq\lambda_0.
\]

This is a classification of one branch of the excess-two class.
A general reciprocal irreducible unit can have several expanding conjugates; its length-five neutral completion need not be a Salem polynomial.
Those polynomials, all higher-excess classes, and a uniform reduction of an arbitrary hypothetical Lehmer counterexample to this class remain outside U.

Theorem 2, its length-six enumeration, and all later algorithms/tables are not audited or adopted here.
The source distinguishes a finite search above 1.01 from the conjectural completeness of the 126-entry sporadic list below that cutoff.
No full length-six classification by a finite explicit list, general length-five Mahler minimum, or general Lehmer conclusion is asserted.

The root-count method's exhibited missing hump is enough to exclude the single-expanding-root branch at large degree.
It does not, as stated, give a uniform linear lower bound on the number of expanding conjugates.
Such a density statement, even if proved, would also need a lower bound on their total logarithmic expansion; many expanding roots alone do not bound the sum of their logarithmic moduli away from zero.

## Project proof review

The complete original2026-10-07 author/source/native review account is retained in [R_G524](../../reviews/Yin_R_G0524_v1.md#original-ms26-author-finding), with the coordinator scope and unknown initial isolation declared separately.
The fresh2026-10-21 [independent finding](../../reviews/Yin_R_G0523_v1.md#current-excess-two-salem-finding) checks the exact corrected source unit and C247 application, actual original PDF passages and both original finite programs at their declared scope.
Its initial mathematical/source findings preceded comparison with the old accounts, and it certifies no old reviewer isolation or date.
The source artifact, source edition, accepted foundational inputs and all length6/whole-paper/human/formal-verification exclusions above are unchanged.
