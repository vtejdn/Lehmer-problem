---
author: Yin
---

# Independent review of the odd-prime residue block restriction

Review time: 2026-11-07T15:54 UTC.
A separately initialized agent for Yin received the fixed C871, its relevant dependency and the review assignment.
The reviewer had no substantive proof-development context and examined the complete statement and argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Integral block allocation](#integral-block-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Integral block allocation](#integral-block-finding) | [C871 statement](../../claims/Yin_C_G0871_v1.md#statement) | Every odd prime, squarefreeness, block allocation, count and reciprocal degree restrictions. |
| [Integral block allocation](#integral-block-finding) | [C871 argument](../../claims/Yin_C_G0871_v1.md#argument) | Complete determinant, rank defect, endpoint and Frobenius arguments, including the L458 inputs as used. |

<a id="integral-block-finding"></a>
## Finding on the entire proof

The reviewer found no gap in the stated proof.
The odd-prime identities P1鈥揚4 and the pure-endpoint exclusion were checked at their use, including the integral-halves formula in v3.
A factor supported only at the binary root one has degree at most two and its root field contains \(i\), where a Gaussian unit root is excluded by the evaluations at \(\pm1,\pm i\).
In \(D/2D\) the two denominators and \(\zeta-1\) are units.
The determinant for \(H_p(\zeta)/2\) is odd, giving exactly \(p-1\) for the valuation of the resultant.
The total dimension of the distinct primitive residue supports already exhausts this valuation, which prevents two appearances from sharing such a support.
The endpoint value \(H_p(1)=2\) separately prevents sharing the two copies of the endpoint.
Every monic nonconstant factor has a nonconstant reduction, giving squarefreeness.
Counting the Frobenius orbits yields the stated factor bound, and pairing inverse orbits for odd order yields the reciprocal degree formula.
The height and sublinear-degree comparison at the end of C871 is contextual.
This finding concerns the exact block restriction and supplies no existence result for a small global factor.
