---
author: Yin
---

<a id="fs08-u001"></a>
# Minimal digit weight and supports of zero expansions

<a id="weight"></a>
## Weight within an expansion class

For a real base \(\beta>1\), a finite integer digit word \(x=x_1\cdots x_n\) has value \(v(x)=\sum_{j=1}^n x_j\beta^{-j}\) and weight \(\|x\|=\sum_{j=1}^n|x_j|\).
The authors write \(x\sim_\beta y\) if \(v(x)=\beta^k v(y)\) for some integer \(k\), allowing the radix point to shift.
A word is heavy if an equivalent integer digit word has smaller weight and is of minimal weight otherwise.
Strict heaviness additionally requires that removing the first digit or removing the last digit gives a word of minimal weight. [§1, pp. 1–2](../../../literature/pdf/FS08--arxiv-v3.pdf#page=2)

Theorem 3.11 constructs a finite automaton recognizing minimal-weight words at a Pisot base.
Theorems 4.1, 5.4 and 6.4 specialize to words over \(\{-1,0,1\}\) for the golden ratio, Tribonacci number and smallest Pisot number, respectively.
The automata are Figures 1, 7 and 11; Theorem 6.4 omits the dashed arrows from Figure 11. [General theorem and golden ratio](../../../literature/pdf/FS08--arxiv-v3.pdf#page=8) · [Tribonacci](../../../literature/pdf/FS08--arxiv-v3.pdf#page=17) · [Smallest Pisot case](../../../literature/pdf/FS08--arxiv-v3.pdf#page=22)

<a id="zero"></a>
## Recognizing zero

Lemma 3.6 treats a different language, finite words of value zero over the difference alphabet of \(A=\{1-B,\ldots,B-1\}\).
Its carry edges send \(s\) to \(\beta s+e\) for a difference digit \(e\), and a word represents zero exactly when its path starts and ends at zero.
Lemma 3.7 labels each such edge by pairs \((a,b)\in A^2\) with \(a-b=e\), recognizing pairs of equal-length words of equal value. [§3, Lemmas 3.6–3.7, pp. 6–7](../../../literature/pdf/FS08--arxiv-v3.pdf#page=6)

For a signed nonzero word of value zero, the all-zero word is equivalent and has strictly smaller weight.
Thus the paper's minimal-weight test rejects every nontrivial zero relation, including a relation whose exponent support is inclusion-minimal.
Strict heaviness tests deletion at the ends of the word, while inclusion-minimality must exclude a relation on every proper subset of the exponent support, with arbitrary allowed signs.
The carry automaton of Lemma 3.6 supplies a zero test to which further support tests can be applied. [Project support convention](../../../claims/Yin_C_G0345_v576.md#series)
The inspection checked the source definitions, the zero automaton construction and the cited theorem statements, without verifying all minimal-weight digit automata. [Edition](readme.md#edition)
