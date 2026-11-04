---
author: Yin
---

<a id="mcq08-u001"></a>
# MCQ08-U001: projected integer-lattice definition of A_n star

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [MCQ08 retained arXiv v2](../../../literature/pdf/MCQ08--arxiv-v2.pdf), Robby G. McKilliam, I. Vaughan L. Clarkson and Barry G. Quinn, *An Algorithm to Compute the Nearest Point in the Lattice A_n star*, arXiv:0801.1364v2,30September2008,3PDF pages.

Passages: SectionII, printed/PDF p.1, vector/transpose conventions and equations(1)--(2).

Inspection: 2026-10-11T19:29. The D16 author had already directly read this selected definition. A separate source-intake agent acquired the exact v2, checked title/ordered authors/version and3-page count, text-read and visually checked the entire p.1, including the complete displayed equations. Read coverage; no nearest-point algorithm or source proof was audited.


For a positive integer n let1 be the all-ones column of length n+1 and let I be the identity matrix of that size.
The selected source defines

    Q=I-11^T/(n+1),
    A_n^*={Qx:x in Z^(n+1)}.

Here Q is the Euclidean orthogonal projection onto1-perpendicular, and the norm convention is the ordinary Euclidean norm.
The star denotes the dual-root-lattice name in the source; no additional determinant normalization is inserted.

The [G0001 Task](../../../tasks/Yin_T_G0001_v1.md#contract) uses n=d and embeds an integer coordinate vector x in Z^d as y=(0,x).
Then the direct coordinate conversion is

    ||Qy||^2=x^T[I_d-11^T/(d+1)]x.

Every projected integer vector has a representative with first coordinate zero, by subtracting its first coordinate times1 before projection.
These elementary coordinate identities identify the classical lattice form.
The complete project proof separately derives its full nonzero integer minimum d/(d+1) by squared integer differences and uses its own weighted-quotient certificate.
No source shortest-vector theorem, finite enumeration or nearest-point algorithm is a mathematical premise of that proof.

The canonical bibliography records the related IEEE Transactions on Information Theory54(9)(2008),4378--4381 and DOI10.1109/TIT.2008.928280 as reported by the official arXiv entry.
That four-page journal pagination is not the inspected three-page preprint.
No journal-version equivalence, publisher proof, whole-paper result or runtime claim is audited here.
No native mathematical program or Lean check was used; download, text extraction and rendering were operational source inspection only.

Current exact consumer: [C_G21's retained projected-lattice attribution](../../../claims/Yin_C_G0021_v1.md#first-window-deficit-reuse-and-attribution).
Its full integer minimum and capacity use are proved and assessed separately from this source definition inspection.
