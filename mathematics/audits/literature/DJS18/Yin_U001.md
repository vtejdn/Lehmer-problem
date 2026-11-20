---
author: Yin
---

<a id="djs18-u001"></a>
# The finite graph for bounded-digit multiples

Section 4 of the [authors’ preprint](readme.md) treats a nonconstant monic integer polynomial \(F\) with nonzero constant term and all roots off the complex unit circle.
Fix a finite digit set \(D\subset\mathbb Z\) containing a nonzero digit and put \(B=\max_{b\in D}|b|\).
For a root \(\alpha\) of multiplicity \(e\), Definition 15 bounds the degree-less-than-\(\deg F\) integer remainder \(R\) by
\[
 |R^{(j)}(\alpha)|\le \frac{j!B}{\bigl||\alpha|-1\bigr|^{j+1}}
 \qquad(0\le j<e).
\]
Lemma 14 bounds these derivatives for every high-order prefix of a digit polynomial divisible by \(F\).
Reduction modulo \(F\) preserves those derivatives at each root.
In Lemma 16 the derivative evaluations form an invertible confluent Vandermonde system on the coefficients of \(R\), so the bounds leave finitely many integral remainders.

Definition 17 adds the single-digit states to these remainders and allows a step from \(R\) to the remainder of \(XR+b\) modulo \(F\) for \(b\in D\).
Theorem 18 on pp. 23–24 identifies the degree-\(n\) multiples with paths of length \(n\) from their nonzero leading digit to zero, reading the remaining digits from highest power to lowest.
The necessity follows from the prefix bounds, and the reverse implication follows by composing the labelled congruences.
Applying this criterion to \(F=P^k\) retains the full derivative range for each repeated root.
The inspected result concerns existence and recognition of digit multiples; maximizing the density of allowed exponent positions requires a separate argument.
