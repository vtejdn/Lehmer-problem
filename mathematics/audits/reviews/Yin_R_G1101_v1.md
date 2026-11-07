---
author: Yin
---

# Independent review of the two degree-64 convex hull certificates

The reviewer for Yin received the fixed inputs in a fresh context outside the development of either proof.
The two findings relate to different fixed statements, domains and integer search trees.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Height-three review](#height-three-finding) | independently reviewed |
| [Arbitrary-height review](#natural-box-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Height-three review](#height-three-finding) | [V1 statement](../../claims/Yin_C_G0876_v1.md#statement) | Entire enclosure and the degree-64 height-three cell. |
| [Height-three review](#height-three-finding) | [V1 argument](../../claims/Yin_C_G0876_v1.md#argument) | Interpolation, closed disk enclosure, lattice bounds, fixed certificate tree and final leaf. |
| [Arbitrary-height review](#natural-box-finding) | [V2 statement](../../claims/Yin_C_G0876_v2.md#statement) | General enclosure and exact degree-64 cell for unrestricted integer coefficients. |
| [Arbitrary-height review](#natural-box-finding) | [V2 argument](../../claims/Yin_C_G0876_v2.md#argument) | Full height-free proof, natural integer bounds, independently checked complete certificate tree and both terminal exclusions. |

<a id="height-three-finding"></a>
## Height-limited finding

Review time: 2026-11-07T17:01 UTC.
The reviewer checked the interpolation signs and the monic normalization, including degree zero for the real factor, the affine coordinates, and the four quadratic corners.
The reviewer replayed the [supplied verifier](../../computations/programs/Yin_J_G0144/exact_cell_hull.py) and its [fixed input](../../computations/programs/Yin_J_G0144/exact_cell_hull_proof.json.gz).
An independent reconstruction used convolution in ordinary reciprocal coefficients to obtain all 124 vertices.
Independent child-by-child integer comparisons reproduced all 959 internal prefixes and the unique leaf.
The leaf is the degree-18 control multiplied by \(\Phi_{47}\).
An independent Taylor recurrence gives a lower bound for the constant term exceeding 16 times the tail bound.
The finding accepts the full result in the height-three box.

<a id="natural-box-finding"></a>
## Arbitrary-height finding

Review time: 2026-11-07T17:04 UTC.
The same reviewer subsequently received the complete fixed v2 and its separate [natural-box verifier](../../computations/programs/Yin_J_G0144/exact_cell_unbounded.py) and [certificate](../../computations/programs/Yin_J_G0144/exact_cell_unbounded_proof.json.gz).
Using the actual cell data and independently reconstructed vertices, the reviewer derived every coordinate bound directly from the hull.
This verifies coverage without assuming an input height limit.
Separate integer cross-multiplication over the possible child ranges reproduced the full 2639-prefix tree and its two leaves.
The [fixed geometry and Chebyshev data](../../computations/programs/Yin_J_G0144/trace64_cell.py) and the [seed input](../../computations/programs/Yin_J_G0144/trace_control.py) were checked at their use.
The seed has \(Q(-2)=7\) and its closed-disk constant term dominates the tail by a factor greater than 16.
The other leaf has height four and \(Q(-2)=0\), and its constant term also dominates by a factor greater than 18.
The finding accepts the whole unrestricted-height exclusion for the specified gaps and disk.
No solver generator, other root cell, unrestricted Lehmer conclusion or prime-family theorem is included in either finding.
