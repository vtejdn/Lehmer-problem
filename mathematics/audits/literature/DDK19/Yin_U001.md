---
author: Yin
---

<a id="ddk19-u001"></a>
# Real circular units and their signatures at odd prime-power conductor

<a id="sine-signatures"></a>
## The circular unit signature matrix

Let \(m\) be an odd prime power, \(\zeta_m=\exp(2\pi i/m)\), \(K=\mathbb Q(\zeta_m+\zeta_m^{-1})\), and \(I=\{b\in\mathbb Z:1\le b<m/2,\ \gcd(b,m)=1\}\).
The real embeddings of \(K\) are \(\sigma_b\) indexed by \(b\in I\), using the restriction of \(\zeta_m\mapsto\zeta_m^b\).
The signature of a nonzero \(u\in K\) records the signs of all the \(\sigma_b(u)\), using \(0\in\mathbb F_2\) for a positive sign and \(1\) for a negative sign.
The signature of a product is the sum of the vectors.

For this conductor the authors give the following generators for the group of real circular (cyclotomic) units, namely \(-1\) and, for \(a\in I\setminus\{1\}\),
\[
 u_a=\frac{\zeta_m^a-\zeta_m^{-a}}{\zeta_m-\zeta_m^{-1}}.
\]
The signature of \(-1\) is the all-ones vector.
The other entries follow from
\[
 \sigma_b(u_a)=\frac{\sin(2\pi ab/m)}{\sin(2\pi b/m)}.
\]
The denominator is positive, and the numerator is negative exactly when the least positive residue of \(ab\bmod m\) lies in \((m/2,m)\).
Equivalently, the bit for \(u_a\) at the embedding \(\sigma_b\) is \(\lfloor2ab/m\rfloor\bmod2\).
The row span is the image of the circular unit group under the signature map.
Its dimension is the circular unit signature rank.

These definitions and formulas were checked in Sections 2–3, printed pp. 286–288, especially equations (2)–(3) on p. 288 of the [published paper](../../../literature/pdf/DDK19.pdf).
The prime-power generator statement on p. 287 invokes Washington, Lemma 8.1.
The cited generator theorem was used as stated, and the sine formula and sign conversion were directly checked.
Remark 4 on p. 291 reports rank 11 at conductor 29 and attributes it to Davis.
The present inspection does not cover the cited proofs of the group structure or the paper's asymptotic signature-rank results.
The [conductor-13 computation](../../../computations/programs/Yin_J_G0146/readme.md#unit-law) uses only the displayed units and their signatures, and computes its conductor-29 ranks and individual residue cuts directly.
