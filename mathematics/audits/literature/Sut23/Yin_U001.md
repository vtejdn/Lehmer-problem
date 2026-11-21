---
author: Yin
---

<a id="sut23-u001"></a>
# The elliptic group law and the degree of Frobenius minus identity

<a id="group-law"></a>
## Divisor classes and addition

For an elliptic curve with distinguished rational point $O$, the map $P\mapsto[(P)-(O)]$ identifies its group of geometric points with its group of degree-zero divisor classes over the algebraic closure.
In particular, a degree-zero divisor $\sum n_P(P)$ is principal exactly when $\sum n_PP=O$ in the elliptic group law.
The theorem proves additivity using $(P)+(Q)\sim(P+Q)+(O)$ and reduces a degree-zero divisor to a difference of points.
The resulting identification commutes with the field action because $O$ is rational. [Lecture 23, Theorem 23.17, pp. 7–8](../../../literature/pdf/Sut23--lecture23.pdf#page=7)

<a id="frobenius"></a>
## Frobenius and rational points

For an elliptic curve $E/\mathbb F_q$, write $F$ for the endomorphism raising the coordinates to their $q$th powers.
Its fixed geometric points are exactly $E(\mathbb F_q)$, so this group is the kernel of $F-[1]$.
By Lemma 7.1 the sum of an inseparable isogeny and a separable isogeny is separable.
Here the summands are $F$ and $[-1]$.
Thus $F-[1]$ is a separable isogeny whose degree is the number of geometric points in its kernel.
Each geometric fiber has this cardinality, since an isogeny is surjective and any choice of a point in the fiber identifies it with a translate of the kernel. [Lecture 7, Lemma 7.1 and Theorem 7.3, p. 1](../../../literature/pdf/Sut23--lecture7.pdf#page=1)

Writing $t$ for the trace of $F$, Theorem 7.3 gives $\#E(\mathbb F_q)=q+1-t$.
The degree form $\deg(rF-[s])=qr^2-trs+s^2$ is nonnegative for integers $r,s$.
Nonnegativity on rational slopes and continuity give $t^2\le4q$, hence Hasse’s bound. [Lecture 7, Theorem 7.3, pp. 1–2](../../../literature/pdf/Sut23--lecture7.pdf#page=2)

The inspection on 21 November 2026 covered the divisor-class identity, the Abel–Jacobi theorem statement, and the fixed-point, separability and degree calculations in the [fall 2023 notes](readme.md#edition).
It uses the earlier isogeny degree and duality results cited in Lecture 7 at statement level.
