---
author: Yin
---

# CK14: The Free-Projection Spectral Interface

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Source identity: [CK14 in the sole bibliography](../../../literature/readme.md), open [arXiv:1211.6037v3](https://arxiv.org/pdf/1211.6037), 53 pages, revised 2013-09-07.

Passages: Inspection: the group-theoretic research agent read equations (1.5)-(1.7), pp.3-4, and the representation in Section 4.2, p.45, while writing the two-projection argument. the polynomial-core research agent independently checked these exact inputs in the project proof review.

Inspection: The coordinating agent integrates that evidence here; the full liberation-process proofs and the original S-transform derivation are retained external results, not independently audited by this record.


<a id="ck14-u001"></a>
## CK14-U001: Generic Support and Endpoint Characters

Date: 2026-09-11.
Source identity: [CK14 in the sole bibliography](../../../literature/readme.md), open [arXiv:1211.6037v3](https://arxiv.org/pdf/1211.6037), 53 pages, revised 2013-09-07.
Formal publication year 2014 and journal pagination were checked against the author's publication list.
The locators below refer to the author version, not the journal pagination.

Inspection: the group-theoretic research agent read equations (1.5)-(1.7), pp.3-4, and the representation in Section 4.2, p.45, while writing the two-projection argument.
The polynomial-core research agent independently checked these exact inputs in the project proof review.
The coordinating agent integrates that evidence here; the full liberation-process proofs and the original S-transform derivation are retained external results, not independently audited by this record.

For freely independent projections p,q in a faithful tracial W*-probability space with traces alpha,beta strictly between zero and one, the generic parameter t in the standard matrices

\[
p(t)=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
q(t)=\begin{pmatrix}t&\sqrt{t(1-t)}\\\sqrt{t(1-t)}&1-t\end{pmatrix}
\]

has diffuse measure with support [r_-,r_+], positive density on its interior, where

\[
r_\pm=\alpha+\beta-2\alpha\beta
\pm2\sqrt{\alpha\beta(1-\alpha)(1-\beta)}.
\]

The source identifies the atom at one of the product law with the intersection projection, of trace (alpha+beta-1)_+.
Applying this statement to complements gives the four character weights

\[
\tau(e_{10})=(\alpha-\beta)_+,\quad
\tau(e_{01})=(\beta-\alpha)_+,\quad
\tau(e_{11})=(\alpha+\beta-1)_+,\quad
\tau(e_{00})=(1-\alpha-\beta)_+.
\]

Complementing a projection preserves freeness.
The generic support is nondegenerate under the stated strict trace bounds.
The endpoint relations r_-=0 iff alpha=beta and r_+=1 iff alpha+beta=1 follow directly from the displayed formula.
The consuming argument (original material now separated into Yin_C_F0055_v1, Yin_C_F0056_v1, Yin_L_F0047_v1) proves the resulting spectral-gap and bounded-inverse consequences separately; they are not additional assertions of CK14.
Traces zero or one are handled there using faithfulness.

These precise statements and their applicability are accepted external inputs for Yin_T_F0007.
Section 4.2 also supplies the four scalar central summands and generic matrix von Neumann algebra representation, compared with [BSS17-U001](../BSS17/Yin_U001.md#bss17-u001).
No bounded scalar division-closure theorem is attributed to either source.
No whole-paper audit, formal verification or novelty claim is made.
