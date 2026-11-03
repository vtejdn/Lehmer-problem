---
author: Yin
---
# Sim08-U001: projection commutators and the OPUC boundary

Date: 2026-10-15.
Root records actual selected reading by strategy_critique and SOURCE-only verification by f_unitary_scope, including the proof continuation on page8.
This is related classical attribution, not an imported theorem about the project's finite coefficient-ideal projection.

<a id="sim08-u001"></a>
## Read; scoped statements and related attribution

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Barry Simon, The Christoffel--Darboux Kernel, arXiv:0806.1528v1,9 June2008,41 pages. Printed pagination equals PDF pagination. This is the actual v1, not a later published edition.

Passages: Definitions pages2--4; Section3 pages5--8 top, Theorem3.1 page6 equations(3.5)--(3.7), Theorem3.3 page7 equation(3.18) and its proof through page8 top. Strategy also inspected the Section5 page9 CD/Gohberg--Semencul attribution sentence.

Inspection: Statements, domain conventions and selected proof passages read; f visually checked title/contents page1 and relevant pages6--8. Read with the exact printed observations below; not all of Section3 or the41-page source audited.


The general setup is a nontrivial positive measure mu on C with all moments finite, not supported on finitely many points.
X_n is the monic orthogonal polynomial, x_n its normalized version, pi_n is the orthogonal projection to polynomials of degree at most n, and M_z is multiplication by z.
The convention is [M_z,pi_n]=M_z pi_n-pi_n M_z.
Compact support gives bounded L2 operators; otherwise the source specifies the polynomial domain.

Theorem3.1 gives the two zero diagonal blocks of this commutator and the forward boundary identity

    (I-pi_n)[M_z,pi_n]pi_n
       =(||X_(n+1)||/||X_n||) <x_n, .> x_(n+1).

Only this forward block is asserted rank one in the general complex-measure setting.
It does not imply that the complete commutator is rank two for every such measure.

For OPUC, M_z is unitary and Theorem3.3 gives

    pi_n-M_z pi_n M_z^*
       =<varphi_(n+1)^*, .> varphi_(n+1)^*
        -<varphi_(n+1), .> varphi_(n+1).

The polynomial star denotes reversed conjugation.
This is a signed trace-zero boundary of rank at most two.
It is not a positive-semidefinite inequality or an arithmetic gain.
These precisely scoped statements and their applicability as related attribution are accepted; no transfer to an arbitrary finite coefficient Gram matrix or nilpotent shift is assumed.
The project's actual finite identity must be proved in its own space.

### Actual v1 observations and limits

The inspected page6 equation(3.12) lacks a minus sign under the stated commutator convention: the reverse block expands to -pi_n M_z(I-pi_n).
Page7 equation(3.16) uses the correct sign.
Page7 equation(3.20) writes a total-mass factor mu(boundary D) where the general L2 norm requires its square root; the adjacent norm ratio is unchanged.
The page6 nearby wording about a generic reverse-block rank n is not accepted as an exact rank theorem.
There are also adjacent formula-reference slips, so this record does not label all displayed formulas of Section3 audited.
None of these observations supplies or refutes the local project proof, which does not use those formulas as premises.

The [actual v1 PDF](../../../literature/pdf/Sim08--arxiv-v1.pdf) and [printed contents transcription](../../../literature/contents/Sim08--arxiv-v1.md) retain the exact edition.
The official [arXiv record](https://arxiv.org/abs/0806.1528) gives v1 submission2008-06-09 20:16:14UTC; the PDF's2024 generation metadata is not a publication date or new revision.
Local duplicate screening found BSS17 to be a different Simon work, and Nat26's CD formula to be a different source.
No inverse-Toeplitz estimate, uninspected Gohberg theorem or whole-source proof correctness is asserted.

<a id="original-toeplitz-boundary-reading-20261018"></a>
## Original finite-boundary attribution reading

Retained 2026-10-22T01:53 from the complete original L404 author account and its actual R550 input description.
The original L404 account, dated2026-10-18T14:40, records a text reading of the retained arXiv0806.1528v1 at printed/PDF pp8--11, especially p9 identifying the Toeplitz Gohberg--Semencul formula with the CD formula.
The individual source reader and reading minute are not established by that account; the document's22:40 and R550's22:41 completion are not source-reading minutes.
This is a distinct occurrence from the original strategy_critique and f_unitary_scope readings above, not a replacement of their actual page/proof/visual scopes.
The source does not print the finite inverse-matrix formula used in L404 at the cited passage; the complete finite real matrix identity is proved locally by Schur complements and nilpotent shifts, without substituting nearby OPUC conventions.
R550 inspected this existing source record at that attribution/restricted-use scope and did not perform a new original Simon proof audit.
The present maintaining constructor read the complete retained original account and this U, without opening a new primary PDF, inspecting another source proof or upgrading any earlier proof coverage.
