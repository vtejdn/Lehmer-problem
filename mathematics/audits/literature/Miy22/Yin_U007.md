---
author: Yin
---

<a id="miy22-u007"></a>
# Miy22-U007 - The Affiliated Rationality Criterion and Bounded Intersection

This source analysis comprises [U006](Yin_U006.md#miy22-u006), [U007](#miy22-u007), [U008](Yin_U008.md#miy22-u008).
Its [shared source, inspection and setting](Yin_U006.md#miy22-affiliated-operators-and-domain-sensitive-rationality) and [joint review dated 2026-09-08](Yin_U008.md#independent-cross-review-of-u006-u008) retain their original scopes.


- Kind: criterion and closure argument.
- Source locators: Remark 4.4, Theorem 4.5, and Lemma 4.6, p. 20; Remark 4.7 and Lemmas 4.8-4.11, pp. 21-22; proof of Theorem 4.5, p. 22.
- Verification: every displayed closure identity and the two containments of the theorem reconstructed, conditional on Theorem 3.1 and the shared affiliation infrastructure.

### Exact Result and Imported Inputs

Under the shared setting and the definitions in [U006](Yin_U006.md#miy22-u006), Theorem 4.5 states
\[
R(s)=R'(s)=D(s),\qquad D(s)\cap M=C_{\mathrm{div}}(s).
\]
For every \(u\in D(s)\), bounded \(a,b,f,g\in C_{\mathrm{div}}(s)\) may be chosen with regular \(f,g\) such that \(u=f^{-1}a=bg^{-1}\).

Theorem 3.1, p. 8, is used with its exact bounded hypothesis:
\[
a\in M:\qquad
a\in C_{\mathrm{div}}(s)
\ \Longleftrightarrow\
[r_i^*,a]\text{ has finite rank for every }i.
\]
This Section 4 review does not independently verify the proof of that theorem.
Remark 3.10 supplies \([r_i,a]=-[r_i^*,a]\) for bounded \(a\in M\).
Neither input licenses replacing the semicircular setting by an arbitrary affiliated algebra.

The source also identifies \(D(s)\) with the free skew field using reference [13] and states that affiliated rational closure equals division closure.
That external identification was not independently verified here and is not needed for the following proof of the displayed equalities when \(D(s)\) is defined simply as division closure.

### Proof Mechanism and Lemma Checks

**Remark 4.4: switching right annihilation and creation.**
Because \(r_i+r_i^*\) commutes with \(a,b,f,g\) and \(fb=ag\),
\[
f(r_i+r_i^*)b-a(r_i+r_i^*)g=0.
\]
Thus \(f r_i b-a r_i g=-\Delta_i(f,a,b,g)\).
This is a bounded identity.

**Remark 4.7: bounded intersection before the final theorem.**
For a bounded \(u\), the representation \(u=1^{-1}u=u1^{-1}\) has defect \([r_i^*,u]\).
U006 and Theorem 3.1 yield
\[
R(s)\cap M=C_{\mathrm{div}}(s).
\]
This establishes the needed bounded input without presupposing \(R(s)=D(s)\).

**Lemma 4.8: addition.**
Use common regular denominators from U006:
\[
u_k=f^{-1}a_k=b_kg^{-1}.
\]
The defect of \(u_1+u_2\), with numerators \(a_1+a_2,b_1+b_2\), is the sum of the two defects and hence finite rank.

**Lemma 4.9: multiplication.**
Choose bounded fractions
\[
a_1f_2^{-1}=x^{-1}y,\qquad
g_1^{-1}b_2=pq^{-1},
\]
where \(x,q\) are regular.
Unlike the invertible ratios in U006, these ratios need not be invertible, so no regularity of \(y,p\) is assumed or required.
Then
\[
u_1u_2=(xf_1)^{-1}ya_2=b_1p(g_2q)^{-1}.
\]
The relations \(xa_1=yf_2\) and \(g_1p=b_2q\) give the checked cancellation
\[
\begin{aligned}
xf_1r_i^*b_1p-ya_2r_i^*g_2q
={}&x(f_1r_i^*b_1-a_1r_i^*g_1)p\\
&+y(f_2r_i^*b_2-a_2r_i^*g_2)q.
\end{aligned}
\]
Both terms are finite rank; the new denominators are regular products.

**Lemma 4.10: inversion.**
The hypothesis is invertibility of \(u\) in \(U(M)\), not merely \(u\ne0\).
It implies that \(a=fu\) and \(b=ug\) are invertible in \(U(M)\), hence regular bounded elements.
With
\[
u^{-1}=a^{-1}f=gb^{-1},
\]
the new defect is \(-\Delta_i(f,a,b,g)\).

**Lemma 4.11: adjoints.**
The fractions
\[
u^*=(g^*)^{-1}b^*=a^*(f^*)^{-1}
\]
have defect
\[
g^*r_i^*a^*-b^*r_i^*f^*
=-(f r_i b-a r_i g)^*.
\]
The corrected Remark 4.4 and finite rank of adjoints establish the claim.
Adjoint closure is needed for the following regularization argument.

**Theorem 4.5: assembly without a cycle.**
These operations, together with the polynomial elements already supplied by Remark 4.7, make \(R(s)\) an inverse-closed subalgebra of \(U(M)\); hence \(D(s)\subset R(s)\).
For the reverse inclusion, take \(u\in R(s)\) and set
\[
f=(1+uu^*)^{-1},\qquad a=fu.
\]
Closure under multiplication, adjoints, and inversion puts both in \(R(s)\), while functional calculus puts both in \(M\).
Remark 4.7 therefore puts them in \(C_{\mathrm{div}}(s)\).
Every bounded polynomial division expression belongs to \(D(s)\), since a bounded inverse is also the affiliated inverse; thus \(C_{\mathrm{div}}(s)\subset D(s)\).
Since \(f\) is regular, \(u=f^{-1}a\in D(s)\).

The source explicitly gives the left regularization in this final paragraph.
The right side of the theorem's “moreover” clause follows by the same already established operations with
\[
g=(1+u^*u)^{-1},\qquad b=ug.
\]
Both are bounded elements of \(R(s)\), hence of \(C_{\mathrm{div}}(s)\), and \(g\) is regular.
This spells out the symmetric step rather than adding an assumption.

### Source Corrections and Their Consequences

1. **Remark 4.4, p. 20:** the printed hypothesis is \(f r_i^* a-b r_i^*g\) finite rank.
   Its displayed calculation, the definition of the defect, and its use in Lemma 4.11 require \(f r_i^* b-a r_i^*g\).
   The two numerators are swapped in the printed hypothesis.
   The checked result here uses the corrected hypothesis.
2. **Lemma 4.10, p. 21:** the last line concludes \(u\in R(s)\).
   Its statement and the just-computed defect require \(u^{-1}\in R(s)\).
   This is a conclusion-variable typo.

Both readings were confirmed in the page images rather than inferred solely from text extraction.
They affect literal transcription and should be carried with any reuse; neither leaves an unresolved step in the reconstructed criterion under its stated inputs.

### Scope, Dependencies, and Verification Facts

This unit depends on U006, bounded Theorem 3.1, Remark 3.10, and standard affiliated functional calculus.
It supplies the rational bounded numerators and denominators used in U008.
It does not replace finite rank by compactness, does not claim regular denominators have bounded inverses, and does not promote an arbitrary nonzero affiliated operator to an invertible one.

The local algebraic identities and regularization chain were checked on 2026-09-08 against text and rendered pp. 20-22.
Theorem 3.1 was treated as a stated input.
No independent audit of the free-field identification in reference [13], external errata search, numerical check, formal proof, or external human review was performed.
This is the initial unit audit.


## Source and inspection

[Source and edition notes](readme.md).

Source edition: Miy22, the retained 24-page published Journal of Functional Analysis 283 (2022), article 109609, DOI 10.1016/j.jfa.2022.109609. Printed and PDF pages agree, treating the opening article page as p. 1. The related 20-page arXiv preprint was not compared line by line; its locators are not substituted here.

Passages: Remark 4.4, Theorem 4.5 and Lemma 4.6, p. 20; Remark 4.7 and Lemmas 4.8-4.11, pp. 21-22; proof of Theorem 4.5, p. 22.

Inspection: 2026-09-08: the affiliated rationality and bounded-intersection chain reconstructed with the recorded corrections, under the separately linked common setting and shared independent U006-U008 review. The bounded theorem is an input; the optional free-field identification is not a premise of the core chain. Affiliation foundations and outside papers keep the original inspection limits; no formal verification.
