---
author: Yin
---

# Primitive Salem numbers and intersections of trace fields in Mossinghoff's table

<a id="powers"></a>
## Every listed input is primitive

For each of the 72 Salem numbers \(\sigma\) in [Mossinghoff's fixed June 2026 table](../../../audits/literature/Mos26b/readme.md), the element \(\sigma\) is not a \(p\)-th power in \(\mathbb Q(\sigma)\) for any prime \(p\).
In particular none of them is a proper positive power of a Salem number.
The [432 certificates](inputs/powers.tsv) give six simple modular roots per input, one for each possible prime exponent.

Write \(P\) for the monic minimal polynomial and \(d=\deg P\le46\).
If \(\beta^p=\sigma\) in \(\mathbb Q(\sigma)\), then \(\mathbb Q(\beta)=\mathbb Q(\sigma)\).
The equations for \(\beta\) and its inverse over the algebraic integers show that \(\beta\) is a unit.
Only one conjugate has modulus greater than one, so its logarithmic Mahler measure is \((\log\sigma)/p\).
The individual-degree bound in [Voutier's Corollary 2](../../../audits/literature/Vou96/Yin_U001.md#height) and the [exact upper cutoff](../Yin_J_G0173/readme.md#window) give
\[
             p<\tfrac12\log(49/37)\bigl(\log138\bigr)^3<17.
\]
For rational controls, the exponential series through degree three at \(282/1000\) exceeds \(49/37\), and through degree sixteen at \(493/100\) exceeds 138.
The resulting upper bound \((282/1000)(493/100)^3/2\) is below 17.

For each \(p=2,3,5,7,11,13\) the program finds a rational prime \(\ell\equiv1\bmod p\) and \(a\ne0\bmod\ell\) satisfying
\[
                  P(a)=0,\qquad P'(a)\ne0,\qquad
                  a^{(\ell-1)/p}\ne1\pmod\ell .
\]
The [simple-root form of Hensel's lemma](../../../audits/literature/Con26e/Yin_U001.md#con26e-u001) gives an embedding \(\mathbb Q(\sigma)\hookrightarrow\mathbb Q_\ell\) under which \(\sigma\) reduces to \(a\).
Any putative \(p\)-th root there would be a local unit and would give a \(p\)-th root of \(a\) in \(\mathbb F_\ell^\times\), contradicting the last test.
For example, at rank 1 and \(p=2\) the witness is \(\ell=23,a=17\), with \(P'(17)\equiv3\) and \(17^{11}\equiv22\bmod23\).
The largest witness prime used is 727.

The exact minimum logarithmic Mahler measure among individually half-mass-admissible Salem numbers multiplicatively commensurable with any listed \(\sigma\) is \(e(\sigma)\log\sigma\), with all 72 exponents given in [J173](../Yin_J_G0173/readme.md#exponents).
Indeed suppose \(\eta\) is Salem and \(\eta^v=\sigma^u\) for positive integers \(u,v\), reduced to coprime exponents using positivity.
A [positive power of a Salem number preserves its field](../../../claims/Yin_C_G0345_v392.md#local), so \(\eta\in\mathbb Q(\sigma)\).
Choose integers \(a,b\) with \(au+bv=1\).
Then \((\eta^a\sigma^b)^v=\sigma\), which forces \(v=1\) by the exclusions above.
The commensurable Salem outputs are therefore exactly \(\sigma^u\), \(u\ge1\), and their logarithmic measures are \(u\log\sigma\).

<a id="fields"></a>
## All ordered inclusions between distinct catalogue trace fields are excluded

For rank \(i\) put \(t_i=\sigma_i+\sigma_i^{-1}\), \(K_i=\mathbb Q(t_i)\), and let \(Q_i\) be its monic minimal polynomial of degree \(s_i=d_i/2\).
For every two distinct ranks \(i,j\) there is no \(\mathbb Q\)-embedding of \(K_j\) into \(K_i\).
Among all \(72\cdot71=5112\) ordered pairs, 4627 are excluded by \(s_j\nmid s_i\).
The [field certificates](inputs/inclusions.tsv) give a prime and both factor-degree lists for each of the other 485 pairs, with source \(i\) and proposed subfield \(j\).
The numbers first excluded at \(\ell=2,3,5,7,11\) are respectively \(298,142,28,16,1\).

Here is the exclusion test when \(s_i=h s_j\).
Take \(\ell\) at which both reductions are squarefree.
All roots of both polynomials lift uniquely from a common finite residue field to a common unramified extension of \(\mathbb Q_\ell\).
Frobenius permutes them with cycle lengths equal to their irreducible factor degrees, by the [squarefree Frobenius argument](../../../claims/Yin_C_G0345_v255.md#symmetric).
If \(K_j\) embeds in \(K_i\), restriction of the embeddings of \(K_i\) into \(\overline{\mathbb Q}_\ell\) to the embedded \(K_j\) gives an equivariant surjection with all fibers of size \(h\).
Each source cycle must map onto one target cycle of length \(b\) dividing its length, and all source lengths assigned to that target must sum to \(hb\).
Thus the two degree lists must admit such an assignment, including when cycles have the same length.
The program tries every assignment subject to the remaining capacities, identifying identical capacities for the same target length.
When \(h=1\) it compares the two sorted degree lists directly.

<a id="subfields"></a>
## Every listed trace field has no proper intermediate field

All 72 trace fields \(K_i/\mathbb Q\) are primitive, in the sense of having no \(F\) with \(\mathbb Q\subsetneq F\subsetneq K_i\).
The 33 prime trace degrees imply this immediately.
For each of the other 39 ranks the [subfield certificates](inputs/subfields.tsv) give a squarefree reduction at \(\ell\le31\) whose factorization has a prime degree \(r>s_i/2\).
The rational Galois group acting on the \(s_i\) embeddings consequently contains a permutation of order divisible by \(r\).
A proper intermediate field would partition these embeddings into \(b\) blocks of equal size \(c\), with \(bc=s_i\) and \(b,c\ge2\).
All permutations preserving this partition form a group of order \((c!)^b b!\), prime to \(r\) because \(b,c\le s_i/2\).
This excludes the intermediate field.
The same [block argument](../../../claims/Yin_C_G0345_v255.md#symmetric) applies without computing a complete Galois group.
Consequently for distinct ranks any two embedded copies of the corresponding trace fields intersect in precisely \(\mathbb Q\), since a larger intersection would imply one of the excluded inclusions.

<a id="transforms"></a>
## Salem outputs of rational trace transformations below 1.3

Take any listed source of degree at most 44 and rational polynomials \(U,V\) with \(V(t_i)\ne0\).
If \(U(t_i)/V(t_i)=\tau+\tau^{-1}\) for a Salem number \(1<\tau<1.3\), then \(\tau=\sigma_i\).
In particular a listed source \(\sigma_i\ge1.3\) of those degrees has no such output.
For a source below \(1.3\) the output equals the source exactly when \(Q_i(X)\mid U(X)-XV(X)\).
Indeed the output trace generates a subfield of \(K_i\), so \(\deg\tau\le d_i\).
By the [source's stated completeness](../../../audits/literature/Mos26b/readme.md) every such output has a catalogue rank, and the exclusion of distinct ranks leaves only the source.
The divisibility condition follows by evaluating at its minimal-polynomial root.
For inputs as well as outputs below \(1.3\) this covers all Salem inputs of degree at most 44.
In the strip \(1.3\le\sigma<49/37\) the assertion covers the listed sources of those degrees.
In degree 46 the pairwise calculation still excludes every distinct listed output, and its trace field has no proper intermediate field.

<a id="reproduction"></a>
## Reproduction and certificate files

Run the [certificate program](certificates.py) from the repository root using Python and SymPy (tested with SymPy 1.14.0).
It reuses the [J173 parser and source-recovery command](../Yin_J_G0173/readme.md#reproduction) for Mossinghoff's June 1, 2026 native table at the July 2 revision.

~~~sh
python mathematics/computations/programs/Yin_J_G0174/certificates.py
~~~

The program reconstructs each \(Q_i\) by subtracting integral multiples of \(X^{s_i-j}(1+X^2)^j\) from the reciprocal polynomial in descending \(j\).
All full remainders are checked for zero.
It evaluates \(P_i\) and its derivative by modular Horner evaluation, and factors the trace polynomials over each indicated prime field after testing squarefreeness.
Compare the three generated TSV files under `mathematics/computations/outputs/Yin_J_G0174/` with the power, inclusion and subfield certificates linked above.
An author check also recovered the factor degrees from successive gcds with \(X^{\ell^k}-X\) and obtained the same exclusion totals and coverage.
The field results concern these specified inputs, and the half-mass minima additionally use the [proved exponent criterion](../../../claims/Yin_C_G0345_v392.md#statement).
