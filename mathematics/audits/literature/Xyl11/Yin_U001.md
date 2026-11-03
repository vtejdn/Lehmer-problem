---
author: Yin
---

<a id="xyl11-u001"></a>
# Xyl11-U001: a uniform least-prime bound for the incidence construction

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Xyl11, [retained publisher PDF](../../../literature/pdf/Xyl11.pdf), Acta Arithmetica 150.1 (2011), 65--91, DOI 10.4064/aa150-1-4.

Passages: Introduction, printed p.65 / PDF p.1; Theorem 1.1, printed p.66 / PDF p.2. The downloaded PDF has 28 pages, including a blank final page.

Inspection: 2026-10-08, human record author Yin. The coordinating AI reviewer directly read the primary publisher text and inspected the rendered theorem page. A separately assigned reviewer of the consuming manuscript independently located the same statement. Statement and substitution checked; original proof not re-audited.


## Accepted input and exact application

For coprime positive integers \(a,Q\), let \(P(a,Q)\) be the least prime in the residue class \(a\pmod Q\).
Theorem 1.1 supplies an absolute, effectively computable constant \(C\) such that

\[
P(a,Q)\le C Q^{5.18}.
\]

This established external theorem is accepted for use at this precise statement and applicability scope.
Its source-reading state is **Read**; acceptance does not claim a fresh audit of the proof, the numerical tables, or their implementation.

The [characteristic-two manuscript](../Ope26/Yin_U001.md#ope26-u001) uses it at the start of Section 5.
There \(q=2^h\), \(Q=q^{100}\), and \(a=Q-1\), so \(\gcd(a,Q)=1\).
The least prime \(\ell\equiv-1\pmod {q^{100}}\) exists, is odd, and satisfies \(\ell\le Cq^{518}\).
With \(D=\ell+1\) and \(s=\lfloor\log_qD\rfloor\), one obtains

\[
q^{100}\mid D,\qquad 100\le s\le 518+\log_2(C+1).
\]

Thus the upper bound for \(s\), and consequently the dimension \(n=10(s+20)\), is independent of \(h\).
This is exactly what the uniform asymptotic estimates for the finite incidence construction require.
Neither a sharp Linnik exponent nor an executed least-prime search is needed.
Dirichlet's theorem alone would give existence but would not supply this uniform polynomial bound.

## Verification limits

The publisher's title, author, DOI, printed pages and Theorem 1.1 were checked directly.
No claim is made about the best currently known exponent.
The original proof, auxiliary zero estimates, Map26 calculations and earlier Linnik/Heath-Brown proofs remain accepted external mathematics, not locally rerun evidence.
This bounded acceptance resolves the named external input of the consuming audit; it does not audit the rest of the published article.
