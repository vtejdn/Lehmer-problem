# Kou11: Square-root Newton and Halley iterations

## Yin's source notes

The selected original is Omran Kouba's [arXiv:1104.4175v2](https://arxiv.org/abs/1104.4175v2), dated 1 May 2011, retained as [Kou11--arxiv-v2.pdf](../../../literature/pdf/Kou11--arxiv-v2.pdf).
The first page identifies the author, title and exact version, and this original has ten PDF pages.
No journal-version equivalence is asserted.

The definitions (4)--(6) on printed/PDF page 2, Lemma 2.1 and its proof on pages 3--4, and Corollary 2.3 and its displayed proof on pages 4--5 were read for the square-root Cayley identity and its Newton/Halley and approximation-order consequences.
The source's \(V_{2t}(-Z)\), with \(Z=R-1\), is the explicit odd-power rational approximant used in [C860 v5](../../../claims/Yin_C_G0860_v5.md#pade-integrality).
These passages provide attribution for the established mechanism; they do not state the project's dyadic integral normalization, minimum-rank theorem or original-input return.
Those deductions and their exact hypotheses are proved at [their responsible Claim](../../../claims/Yin_C_G0860_v5.md#argument).
The actual inspection is confined to the identified definitions, statements and arguments, with no whole-paper review or priority claim.

The independent project reviewer found two incorrect displayed recurrences in the proof of Lemma 2.1(b), printed/PDF page 4; the coordinator confirmed them in the original text and checked the algebra.
Writing e_n for the current Cayley error and w for its initial value, the Newton and Halley recurrences are e_(n+1)=e_n^2 and e_(n+1)=e_n^3, respectively.
The source instead prints w^2 e_n and w^3 e_n at those two lines.
Its stated power formulas and the project's independently derived Cayley identities retain their separate scope; the erroneous displays are not proof premises of C860 v5.
