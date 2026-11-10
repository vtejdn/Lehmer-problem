# A discriminant-action obstruction on the fixed degree-18 trace lattice

<a id="fixed-question"></a>
## Exact representation question

The [trace-lattice test](readme.md#question) supplies an exact integral splitting of the fixed degree-18 natural lattice as \(L=H_+\oplus U\), with \(H_+\) positive definite of rank sixteen.
Let \(C\) be the original companion matrix and \(A=T^{-1}CT\) its matrix in the displayed split basis.
The next question is whether this same integral isometry can be expressed using integral positive isometries of \(H_+\) extended by the identity on \(U\), and the permitted even-norm integral transvections at the two fixed cusps.
There is no word-length bound in the obstruction below.
Neither a matrix power, another invariant lattice nor an added dimension is substituted for this input.

The [GHS09 source unit](../../../audits/literature/GHS09/Yin_U001.md#integral-transvection-groups) supplies the dual-lattice and discriminant-group conventions.
Its separate two-hyperbolic-plane generation theorem is not used.
The [ERT19 construction](../../../audits/literature/ERT19/Yin_U001.md#companion-trace-gram) supplies the trace-Gram interpretation; the actual matrices and splitting are checked directly in this J.

<a id="necessary-condition"></a>
## Necessary condition for every permitted word

For an integral lattice \(L\), write
\[
 L^\vee=\{x\in L\otimes\mathbb Q:(x,L)\subseteq\mathbb Z\},
 \qquad D(L)=L^\vee/L.
\]
An integral lattice isometry acts on this finite abelian group.
For a permitted transvection and any \(x\in L^\vee\),
\[
 T_{e,v}x-x=-(v,x)e+(e,x)v-\tfrac12(v,v)(e,x)e\in L.
\]
Every coefficient here is integral, including the half-norm.
Thus each transvection acts trivially on \(D(L)\).

The remaining positive isometries all belong to \(O(H_+,\mathbb Z)\) and fix the same \(U\).
Their product \(R\) is again in that group.
Positive definiteness makes this group finite, by the bounded-integer-column argument already retained in [C885 v2](../../../claims/Yin_C_G0885_v2.md#argument).
It follows that the action of any permitted word on \(D(L)\) equals that of one finite-order integer matrix \(R\) on the positive rank-sixteen summand.
This conclusion does not require the individual positive isometries to commute.

If an eigenvalue of \(R\) has order \(n\), its cyclotomic minimal polynomial over \(\mathbb Q\) divides the degree-sixteen characteristic polynomial, so \(\varphi(n)\le16\).
For every prime power \(p^a\mid n\), one has \(\varphi(p^a)\le\varphi(n)\le16\).
The largest allowed prime powers therefore divide
\[
 E=2^5\,3^2\,5\,7\,11\,13\,17=24504480.
\]
Since a finite-order matrix is diagonalizable in characteristic zero, \(R^E=I\).
Consequently every permitted word \(W\), of any finite length, necessarily satisfies
\[
                     W^E=I\quad\hbox{on }D(L).                 \tag{1}
\]
This is a necessary condition only; satisfying it would supply no decomposition.

<a id="integer-certificate"></a>
## Actual integer certificate

In the original power basis, \(L=\mathbb Z^{18}\) and \(L^\vee=G^{-1}\mathbb Z^{18}\).
Put \(d=\det G\) and \(Q=\operatorname{adj}(G)\), so \(GQ=QG=dI\).
The criterion for \(C^E\) to act trivially on \(D(L)\) is exactly
\[
                 (C^E-I)Q\equiv0\pmod{|d|}.                   \tag{2}
\]
Indeed the columns of \(Q/d\) generate the dual lattice, and (2) says that their changes under \(C^E\) lie in the original integer lattice.
The verified basis matrix \(T\) is unimodular, so this condition is invariant under the change to \(H_+\oplus U\).

The separate [exact program](discriminant_action.py) reads the unchanged trace-lattice result, obtains \(Q\) by rational elimination, and directly verifies both identities \(GQ=QG=dI\).
It computes \(C^E\) modulo \(|d|\) by repeated squaring and then forms the entire defect matrix in (2).
All arithmetic is integral or exact rational; no spectral or root approximation is used.
The actual result is retained at
`mathematics/computations/outputs/Yin_J_G0158/discriminant_action.json`.

The complete output gives
\[
 d=-2915479459020775961521,
\]
and its zero-indexed \((0,0)\) defect entry is
\[
                 2850856976087321421046\pmod{2915479459020775961521}.
\]
This residue is strictly between zero and the modulus.
Therefore (2) fails, giving an explicit dual-lattice class on which \(C^E\) is nontrivial.
The witness class is the first column of \(Q/d\) modulo \(\mathbb Z^{18}\); the displayed nonintegral first coordinate of its change certifies nontriviality.

<a id="conclusion-and-limits"></a>
## Consequence and limits

The fixed natural trace-lattice isometry has no representation by the stated generators, at any word length.
The [separate independent finding](../../../audits/reviews/Yin_R_G1114_v5.md#discriminant-action-review) checks the complete argument, author program and actual output, independently reconstructing the modular power in the quotient polynomial ring.
The conclusion applies to every integral splitting of this same rank-eighteen lattice as a positive rank-sixteen lattice plus \(U\), because the discriminant action and the uniform exponent bound do not depend on that choice of basis.
It does not exclude another \(C\)-stable integral lattice in the same rational vector space, a different family of generators, or a different representation of the same Salem polynomial.
Taking powers or adding dimensions would change the selected test and its measure or representation obligations.
No new small measure, general one-plane generation theorem, or unrestricted Lehmer gap follows.

From the repository root, reproduce in order:

~~~text
python -B mathematics/computations/programs/Yin_J_G0158/trace_lattice.py
python -B mathematics/computations/programs/Yin_J_G0158/discriminant_action.py
~~~

Both programs require only the Python standard library.
Their generated JSON results are reproducible local outputs; the original polynomial remains the fixed J144 input.
