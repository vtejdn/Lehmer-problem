---
author: Yin
---

# JKZ08: simple-root generators and the positive E8 Cartan convention

<a id="jkz08-u001"></a>
## Source and scope

Use the [author-hosted 17-page original](readme.md#author-original).
Remark 2.5 on author/PDF pages 6--7, including diagram (2.5) and the continuing simple-root basis, was read in text and checked visually.
The title page and the cited-reference identities on pages 16--17 were also inspected.
The paper's degree-240 construction and its Galois-group proof are outside this reading.

<a id="simple-generators-and-gram"></a>
## Simple generators and the actual J158 basis

Remark 2.5 gives \(W(E_8)\) a Coxeter presentation on eight simple-root generators \(w_1,\ldots,w_8\).
It defines the simple-root convention by requiring every root to have either all nonnegative or all nonpositive integral coefficients in that basis.
The relations are \(w_i^2=1\) and \((w_iw_j)^{m(i,j)}=1\), with exponent three precisely on
\[
\{(1,3),(3,4),(2,4),(4,5),(5,6),(6,7),(7,8)\},
\]
and exponent two on other distinct pairs.
The source attributes the presentation to Bourbaki, *Groupes et algèbres de Lie*, Chapters 4--6 (1968), Chapter IV.
The same remark identifies this Weyl group with the full automorphism group of the positive Euclidean \(E_8\) lattice and identifies its roots as the squared-length-two vectors.
It points to Adams, *Lectures on Exceptional Lie Groups* (1996), Section 10, for the lattice-group identification.
Those foundational proofs were not inspected.

The continuation on page 7 states that the roots generate the lattice and supplies an integral simple-root basis.
Using standard orthonormal coordinates \(x_i\), its displayed vectors can be labelled compatibly with diagram (2.5) as
\[
\alpha_1=\tfrac12(x_1+x_2-x_3-x_4-x_5-x_6-x_7-x_8),\quad
\alpha_2=x_2+x_3,\quad \alpha_3=-x_2+x_3,\quad
\alpha_j=-x_{j-1}+x_j\quad(4\le j\le8).
\]
This labelling matches the diagram; the printed vector list itself places \(\alpha_3\) before \(\alpha_2\).

The source labels correspond to the ordered J158 basis by
\[
(h_1,h_2,h_3,h_4,h_5,h_6,h_7,\ell)
\longleftrightarrow
(\alpha_1,\alpha_3,\alpha_4,\alpha_5,
 \alpha_6,\alpha_7,\alpha_8,\alpha_2).
\]
Reading the actual e8_gram field in [J158's output](../../../computations/outputs/Yin_J_G0158/coxeter_model.json) gives diagonal entries two, off-diagonal minus one along the chain \(1-2-3-4-5-6-7\) and edge \(3-8\), and zero elsewhere.
Under the displayed permutation this is exactly the positive simply-laced Cartan Gram convention of the source diagram.
There is no division by two, reversal of the form, added lattice index or change of root length.
The corresponding column reflections are \(S_i=I-e_i(e_i^{\mathsf T}H)\), with \(H=\texttt{e8\_gram}\).
Consequently the source's finite simple-root generating set is the one used for this block.

The separate [WvL21 root-orbit statement](../WvL21/Yin_U001.md#full-isometry-and-transitivity) supplies transitivity on norm-two vectors.
This source unit checks notation and applicability; it performs no group enumeration and proves no new star-graph, component-permutation or indefinite-lattice assertion.
