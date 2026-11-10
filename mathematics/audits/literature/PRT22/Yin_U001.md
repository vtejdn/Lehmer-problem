---
author: Yin
---

<a id="prt22-u001"></a>
# PRT22-U001: squarefree Sturm counts and positive scaling

## Source, inspection and accepted boundary

Use the [identified arXiv v1 edition](readme.md), with Notation on printed/PDF page 1, Theorem 1.2(1) and its distinct-root footnote on page 2, and Lemma 1.4(1),(3) on pages 2--3 with their local sign arguments on page 4.
On 2026-11-10 the assigned AI read the four-page retained PDF as text and visually inspected pages 1, 2 and 4.
The actual title, authors, version marking, theorem, examples and displayed common-factor assertion were checked against those rendered pages.
This was ordinary source Preparation, not an independent review of a project proof or computation.

The accepted external input is only the classical theorem for a nonconstant squarefree real polynomial and endpoints at which that polynomial is nonzero.
The source's broader treatment of multiple roots and root endpoints is not adopted.
The printed local slips described below do not enter the self-contained argument for this restricted statement.
No VTK or FLINT implementation, numerical root result, project root count or original nineteenth-century proof was inspected.
The source is an exposition and statement locator, without a claim of historical priority.

<a id="sturm-sequence-and-variation"></a>
## Definition: negative remainder sequence and zero-deleted sign variation

Let \(f\in\mathbb R[t]\) have positive degree and \(\gcd(f,f')=1\).
Define its classical Sturm sequence by
\[
s_0=f,\qquad s_1=f',\qquad
s_{i+1}=-\operatorname{rem}(s_{i-1},s_i)
\]
using ordinary Euclidean division over \(\mathbb R[t]\), stopping at the last nonzero term.
The degrees decrease strictly after the initial pair.
The last term \(s_m\) is a nonzero constant because the Euclidean algorithm computes a scalar multiple of \(\gcd(f,f')\).
Zero remainders are not used as divisors.

For a finite real sequence, delete all zero entries and count adjacent pairs with opposite signs in what remains.
A sequence with fewer than two remaining entries has variation zero.
Write
\[
V_f(c)=\operatorname{Var}\bigl(s_0(c),\ldots,s_m(c)\bigr).
\]
This is precisely the zero-skipping sign convention in PRT22's Notation.
The source pads its sequence with zero polynomials; stopping at the last nonzero term leaves the variation unchanged.
Although the source calls its chain a pseudo-remainder sequence, the adopted definition is its displayed ordinary quotient/remainder recurrence.
An arbitrary integer pseudo-remainder sequence does not inherit this convention without the appropriate sign factors.

<a id="classical-sturm-count"></a>
## Accepted count and a self-contained sign argument

For finite real \(a<b\) with \(f(a)f(b)\ne0\),
\[
\#\{x\in(a,b):f(x)=0\}=V_f(a)-V_f(b).
\tag{1}
\]
The count is of distinct roots; under the squarefree hypothesis it is also the count with multiplicity.
This is the direct restriction of PRT22 Theorem 1.2(1): its interval \((a,b]\) agrees with \((a,b)\) when \(f(b)\ne0\).
Intermediate sequence members may vanish at either endpoint; the zero-deletion rule remains required.

The following proof checks the needed classical mechanism directly, using the recurrence and the local sign behavior identified in Lemma 1.4(1),(3).

Two successive members cannot vanish at the same real point.
Indeed, the recurrence
\[
s_{i-1}=q_i s_i-s_{i+1}
\]
would propagate two adjacent zeros backward to \(f=f'=0\), contrary to squarefreeness.
The last constant has no zero.

If an interior member \(s_i(c)\) vanishes, its neighbors are nonzero and satisfy
\[
s_{i-1}(c)=-s_{i+1}(c).
\]
Their opposite signs persist in a neighborhood of \(c\).
Consequently the two adjacent sign comparisons across the triple \(s_{i-1},s_i,s_{i+1}\) contribute exactly one variation on both sides of \(c\), and also at \(c\) after its zero entry is deleted.
Several nonadjacent members may vanish at the same point; the affected comparison pairs are disjoint, even when two such triples share a nonzero endpoint, so this argument applies to them together.
All other comparisons are locally constant.

At a root \(c\) of \(f=s_0\), squarefreeness gives \(s_1(c)=f'(c)\ne0\).
For sufficiently small positive \(\varepsilon\), \(f(c-\varepsilon)\) has sign opposite to \(f'(c)\), while \(f(c+\varepsilon)\) has the same sign.
The first comparison therefore loses exactly one variation as \(c\) is crossed from left to right.
Any other vanishing sequence members leave the remaining comparisons unchanged by the preceding argument.

There are only finitely many zeros of the nonzero sequence polynomials.
Partitioning the interval around these points shows that \(V_f\) decreases by one precisely at roots of \(f\) and is unchanged at all other points.
At an endpoint where \(f\ne0\), deletion of intermediate zeros gives the same variation as the neighboring values.
Summing the drops proves (1).
No assertion about a multiple-root endpoint is needed.

<a id="positive-scaling"></a>
## Positive normalization and infinite endpoints

For arbitrary constants \(c_i>0\), replacing \(s_i\) by \(c_i s_i\) preserves every sign and every zero at each evaluation point.
It therefore preserves \(V_f\) and the count (1).
This elementary consequence also matches Theorem 3's following paragraph on the [inspected official FLINT page](readme.md).

The same reasoning permits positive normalizations during construction of the chain, rather than only after constructing it.
For nonzero constants \(\alpha,\beta\),
\[
\operatorname{rem}(\alpha A,\beta B)
 =\alpha\,\operatorname{rem}(A,B).
\]
To see this, multiply \(A=QB+R\), \(\deg R<\deg B\), by \(\alpha\), and use uniqueness of the quotient and remainder after division by \(\beta B\).
If the two current members are positive scalar multiples of the exact Sturm members, their negative Euclidean remainder is a positive scalar multiple of the next Sturm member.
Applying another positive normalization preserves this property inductively.

Thus, for \(f\in\mathbb Q[t]\), clearing denominators by a positive common denominator and dividing integer coefficients by their positive gcd is permitted at each step.
The gcd of coefficient magnitudes is positive; dividing by a signed leading coefficient is not this operation.
An implementation using pseudo-division must establish its corresponding positive-scalar relation or explicitly supply the necessary sign corrections.
The theorem alone is not a verification of such an implementation.

The whole-line version uses the limits of the same finite sequence:
\[
\operatorname{sgn}s_i(+\infty)=\operatorname{sgn}\operatorname{lc}(s_i),
\qquad
\operatorname{sgn}s_i(-\infty)
 =(-1)^{\deg s_i}\operatorname{sgn}\operatorname{lc}(s_i).
\]
Every nonzero polynomial has these constant signs beyond all of its real zeros.
Choose finite endpoints beyond the zeros of all sequence members and apply (1).
It follows that the total number of real roots is \(V_f(-\infty)-V_f(+\infty)\).
The same limiting convention applies with just one infinite endpoint.
This is a direct consequence of the adopted finite theorem, not an additional claim about root endpoints.

<a id="source-slips-and-exclusions"></a>
## Inspected slips and their exact exclusion

The following problems were checked in the actual rendered v1, rather than inferred solely from extracted text.

In Example 1.1, the polynomial is \((t^2-1)^2\).
The continuation at the top of page 2 says that \(-1\) is its only root in \((-2,1]\), but both \(-1\) and \(1\) belong to that interval.
The displayed comparison of variations at \(-2\) and \(0\) instead concerns an endpoint at \(0\).
Neither example assertion is used in (1).

In Example 1.3, the displayed polynomial factors exactly as
\[
t^3-5t^2+7t-3=(t-1)^2(t-3).
\]
Its multiple root is \(1\), and its simple root is \(3\).
The printed root set \(\{2,3\}\) and the subsequent description of which roots are multiple/simple are therefore incorrect.
The selected theorem and local proof do not rely on this example.

Lemma 1.4(2) on page 2 prints \(P_f=(1/g)P_{f/g}\).
That equation cannot hold as written for a general nonconstant \(g\): its zeroth components would be \(f\) and \(f/g^2\).
In addition, dividing the pair \((f,f')\) by \(g\) is not automatically the defining pair \((f/g,(f/g)')\).
This unit neither repairs nor adopts the common-factor assertion or the general reduction that invokes it.
The squarefree proof above uses no such reduction.

These are concrete local source issues, not a refutation of classical Sturm counting or a complete assessment of every broader endpoint statement.
The current accepted scope has a complete argument independent of these slips.
There is no remaining acquisition or attribution task for that restricted input.
