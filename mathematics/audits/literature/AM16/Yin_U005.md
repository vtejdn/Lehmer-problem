---
author: Yin
---
# AM16-U005: the exact fixed-rank multivariate height input

Date: 2026-10-18T11:58.
Human record author Yin.
Root directly reread the complete primary statement for use in a bounded-support Salem monomial question.
This accepts an established source theorem at its exact fixed-rank scope; it is not a new project theorem or audit of the original deep proof.

<a id="am16-u005"></a>
## Read; accepted fixed-rank statement and joint-degree convention

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Francesco Amoroso and David Masser, Lower bounds for the height in Galois extensions, institutional author postprint dated3 August2016, printed1--5/PDF2--6; same retained AM16--author-postprint.pdf as U001--U004.

Passages: Height normalization on printed1/PDF2, complete Theorem2.1 across printed1--2/PDF2--3 and its immediately following joint-degree definition and attribution. The separate Theorem3.1 printed2 was also read for the explicit rank-dependence warning.

Inspection: Direct pdftotext reading of the actual retained PDF pages2--3, checking the complete statement, its continuation and adjacent attribution. Fixed K=Q and each fixed positive rank are accepted; no original Amoroso--David or Delsinne proof audit, explicit constant extraction or varying-rank uniformity.


The [actual postprint](../../../literature/pdf/AM16--author-postprint.pdf) identifies the inspected edition.
The author-order erratum and original proof-inspection boundaries remain those of [U001](Yin_U001.md#am16-u001).
The earlier units deliberately accepted narrower rank-one or rank-two applications and remain unchanged.

### Exact accepted statement

Fix an integer k>=1 and a real epsilon>0.
There exists C_k(epsilon)>0, independent of the nonzero algebraic numbers beta_1,...,beta_k and their joint field degree, such that whenever they are multiplicatively independent,

    max_i h_abs(beta_i)
      >=C_k(epsilon) J^(-1/k-epsilon),
    J=[Q(beta_1,...,beta_k):Q].

Multiplicative independence means that product beta_i^(n_i)=1 with integers n_i forces every n_i=0.
The absolute logarithmic height is normalized by the degree of each primitive minimal polynomial, as in the source introduction.
No integrality or Galois condition on the joint field is needed for this specialization.
The source permits an abelian base K/Q and uses the actual relative joint degree [K(beta_1,...,beta_k):K]; only K=Q is accepted for the present application.
The constant is written C(epsilon) in its statement, with k fixed by the quantified tuple; the explicit subscript here prevents a silent uniform-in-k interpretation.

The primary source attributes the K=Q specialization to Amoroso--David1999 and the general abelian-base result to Delsinne.
That attribution is read in AM16; the original statements and proofs are not independently accepted here merely from this report.
No explicit value, asymptotic lower bound or monotonicity of C_k(epsilon) is asserted.
Neither k nor epsilon may vary along an input sequence while treating this constant as a fixed positive number.
The source's separate Theorem3.1 explicitly writes its constant c(k,epsilon); its ambient Galois degree and exponent-1/(k+1)-epsilon must not be substituted for the joint degree or exponent above.

### Consuming boundary

For k fixed multiplicatively independent conjugates of one algebraic number alpha, their heights coincide, so the displayed maximum is exactly h_abs(alpha).
A consuming argument must still prove its ACTUAL joint-degree bound and retain any difference from the own degree of a monomial in those conjugates.
This source input alone gives no bounded-support stabilizer formula, exact monomial height, uniform lower bound in growing rank, or unrestricted Lehmer conclusion.
The proposed Salem application requires its separately retained complete orbit argument and review.
