---
author: Yin
---

<a id="nat26-u001"></a>
# Nat26-U001: finite-grid Hahn norms and the binomial-basis normalization

## Source and inspection

[Source and edition notes](readme.md).

Source edition: NIST Digital Library of Mathematical Functions, online version1.2.8, release2026-09-15, at the existing Nat26 scope.

Passages: Section18.19, [Table18.19.1](https://dlmf.nist.gov/18.19#T1) and [Table18.19.2](https://dlmf.nist.gov/18.19#T2), specifically Hahn weight, squared norm and leading coefficient at alpha=beta=0 and grid endpointN-1.

Inspection: Original2026-10-07 reading by assigned AI ms25_source and the coordinator for Yin, retained from the complete L57 source-normalization account. Exact formula and normalization reading only; the underlying book references and their proofs were not audited. This organization performs no new source reading.


## Exact inspected specialization

For an integerN>=1, use the finite grid0,...,N-1 and integer degrees0<=j<N.
The inspected Hahn convention at alpha=beta=0 has weight one on that grid.
Writing Q_j for its degree-j polynomial, h_j for the squared norm sum_(x=0)^(N-1) Q_j(x)^2 and ell_j for its leading coefficient, the table specialization is

    h_j=(N+j)!(N-j-1)!/[(2j+1)((N-1)!)^2],
    ell_j=(-1)^j(2j)!(N-j-1)!/[(j!)^2(N-1)!].

The degree-j Gram--Schmidt residual of binom(x,j) is Q_j/(j! ell_j), because the binomial polynomial has leading coefficient1/j!.
Its squared norm is therefore

    h_j/(j! ell_j)^2
      =(N+j)!(j!)^2
         /[(2j+1)(N-j-1)!((2j)!)^2].

These are the exact source normalization and its elementary rescaling checked in the original account.
All factorials have nonnegative integer arguments at0<=j<N.
This unit supplies checked classical attribution for the [complete local finite-difference derivation](../../../ledger/Yin_L_G0057_v1.md#exact-confluent-block-cost).
That argument proves its own residual norm and product formula directly, without relying on a newly accepted book proof or treating source attribution as an additional arithmetic gain.
The local determinant/entropy deductions and their original proof-review scopes remain separate project mathematics.

## Depth and limits

The original bounded lookup stopped after verifying the table normalization.
The retained evidence establishes the exact displayed source formulas and applicability of this specialization; it does not establish a full proof audit of the DLMF table, the underlying Hahn literature or the rest of DLMF.
The two named agents' reading does not by itself certify a formal independent proof-review arrangement.
The fixed Nat26-U001 Euler/Jacobi product scope is a separate unit and supplies none of these Hahn formulas.
