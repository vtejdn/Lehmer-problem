---
author: Yin
---

# Local exponents of the different and the field discriminant

<a id="con26g-u001"></a>
## From ramification indices to the discriminant exponent

For any number field \(K\), Definition 4.1 in the [author's notes](readme.md#author-edition) defines the different \(\mathfrak D_K\) as the inverse fractional ideal of the trace dual \(\{x\in K:\operatorname{Tr}_{K/\mathbb Q}(x\mathcal O_K)\subseteq\mathbb Z\}\).
Theorem 4.8 on page 11 identifies the absolute ideal norm \(N(\mathfrak D_K)=[\mathcal O_K:\mathfrak D_K]\) with \(|\operatorname{disc}K|\).
Its proof computes the index of \(\mathcal O_K\) in its trace dual from the absolute determinant of the trace matrix of an integral basis.

Let \(p\) be a rational prime and \(\mathfrak p\) any prime of \(K\) above \(p\), with ramification index \(e_{\mathfrak p}\) and residue degree \(f_{\mathfrak p}=[\mathcal O_K/\mathfrak p:\mathbb F_p]\).
Write \(d_{\mathfrak p}=\operatorname{ord}_{\mathfrak p}(\mathfrak D_K)\), with the prime-ideal valuation normalized by \(\operatorname{ord}_{\mathfrak p}(\mathfrak p)=1\) and the rational valuation by \(v_p(p)=1\).
Equation (4.12) on page 18 gives

\[
e_{\mathfrak p}-1\ \leq\ d_{\mathfrak p}\ \leq\
e_{\mathfrak p}-1+e_{\mathfrak p}v_p(e_{\mathfrak p}).
\]

The upper bound uses \(\operatorname{ord}_{\mathfrak p}(e_{\mathfrak p})=e_{\mathfrak p}v_p(e_{\mathfrak p})\), since \(\operatorname{ord}_{\mathfrak p}(p)=e_{\mathfrak p}\).
When \(p\nmid e_{\mathfrak p}\) the bounds give \(d_{\mathfrak p}=e_{\mathfrak p}-1\), including zero for an unramified prime.
The upper bound also applies at every wildly ramified prime.
Conrad attributes the lower bound to Dedekind and the upper bound to Hensel.
This inspection covers the statement and normalization of (4.12) and the proof of Theorem 4.8 in the notes.
Conrad cites Hensel's proof of the upper bound on page 18.

Factoring the ideal norm in Theorem 4.8 and using \(N(\mathfrak p)=p^{f_{\mathfrak p}}\) gives

\[
v_p(|\operatorname{disc}K|)
=\sum_{\mathfrak p\mid p}f_{\mathfrak p}d_{\mathfrak p}
\ \leq\sum_{\mathfrak p\mid p}f_{\mathfrak p}
\bigl(e_{\mathfrak p}-1+e_{\mathfrak p}v_p(e_{\mathfrak p})\bigr).
\]

This estimates the discriminant of the full ring of integers of a root field, including a non-Galois root field or one without a power integral basis.
