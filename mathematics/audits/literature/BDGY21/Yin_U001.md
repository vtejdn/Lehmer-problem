---
author: Yin
---

# Cluster subspaces of a Vandermonde matrix on the unit circle

<a id="bdgy21-u001"></a>
## Source and inspection

On 2026-11-21 an agent for Sheng Yin checked the retained arXiv v2 title page, the matrix convention in (1.1), Definitions 2.1–2.5, Theorems 2.1–2.2 and the deduction of (2.2) from (3.18) in §3.4.
The findings below accept those theorem statements for the indicated comparison.
The inspection covered the direction of the principal-angle estimate and its hypotheses; the proofs of the estimates feeding (3.18) and the full singular-value theorem were outside its scope. [Edition and file](readme.md#edition)

<a id="cluster-conventions"></a>
## Angular clusters and the minimal principal angle

In the author manuscript \(V_N\) has one column \(v(x)=(e^{ijx})_{j=0}^{N}\) per distinct node and \(N\ge s-1\) for \(s\) nodes.
The angular distance is the length in radians of the shorter arc, \(\Delta(x,y)=|\operatorname{Arg}e^{i(x-y)}|\).
An \((h,s)\)-cluster consists of \(s\) distinct nodes at pairwise distance at most \(h\).
The optional parameter \(\tau\) requires also \(\Delta(x,y)\ge\tau h\) for distinct nodes.
In a partition into clusters, \(\theta\) bounds below every distance between nodes in different clusters. [(1.1), p. 1](../../../literature/pdf/BDGY21--arxiv-v2.pdf#page=1) · [Definitions 2.1–2.3, pp. 4–5](../../../literature/pdf/BDGY21--arxiv-v2.pdf#page=4)

For a cluster \(X\), let \(L(X,N)=\operatorname{span}_{\mathbb C}\{v(x):x\in X\}\).
The smallest principal angle between two such nonzero subspaces is \(\arccos\sup|\langle v,w\rangle|\), with the supremum over unit vectors in the respective spaces. [Definitions 2.4–2.5, p. 5](../../../literature/pdf/BDGY21--arxiv-v2.pdf#page=5)

<a id="cluster-angles"></a>
## Pairwise angle and the time-coordinate projection

For two clusters of sizes \(s_1,s_2\), maximum diameter bound \(h>0\) and separation \(\theta>0\), Theorem 2.1 gives constants \(C_1,\ldots,C_4>0\) depending only on those two sizes.
For \(C_1\le N\le C_2/h\) the minimal angle satisfies
\[
  \angle_{\min}\big(L(X,N),L(Y,N)\big)
        \ge \frac{\pi}{2}-\frac{C_4}{N\theta}-C_3Nh .
\]
Arbitrarily small positive gaps within a cluster are allowed.
The v2 abstract describes the formula as an upper bound on the minimal angle.
The displayed theorem gives the lower bound written here, consistent with the proof's upper bound on the absolute inner product of two unit vectors. [Abstract, p. 1](../../../literature/pdf/BDGY21--arxiv-v2.pdf#page=1) · [Theorem 2.1 and Remark 2.2, p. 5](../../../literature/pdf/BDGY21--arxiv-v2.pdf#page=5) · [(3.18) and the angle deduction, p. 13](../../../literature/pdf/BDGY21--arxiv-v2.pdf#page=13)

Theorem 2.2 instead compares the ordered singular values of the full matrix to the ordered union of the singular values of its cluster matrices.
Its admissible range is \(C_5/\theta\le N\le C_6/h\); the stated constants depend on the list of cluster sizes. [Theorem 2.2, p. 6](../../../literature/pdf/BDGY21--arxiv-v2.pdf#page=6)

After transposition the source's \(N+1\) samples correspond to the project block length \(N_{\rm block}\).
C345 v725 allows each cluster to have at most \(b\) nodes within \(D/N_{\rm block}\) of a chosen center for any fixed \(D\), and chooses a sufficient separation between centers depending on \(b,D\).
Its proof bounds every diagonal entry of the projection onto the joint time-coordinate space by \(C(b,D)u/N_{\rm block}\) for \(u\) selected phases, uniformly in the number of clusters.
The pairwise angle and singular-value estimates above give context for that independently proved projection bound. [C345 v725, separated clusters](../../../claims/Yin_C_G0345_v725.md#packets)
