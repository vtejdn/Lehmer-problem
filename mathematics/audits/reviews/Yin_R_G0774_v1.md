---
author: Yin
---

# C572 v1: independent negative finding on the stated reduction multiplicity

Review act: 2026-10-22T20:44 UTC.
Human record author: Yin.
A separately assigned reviewer outside substantive development read the exact current C572 mathematical statement and argument directly.
No target old R, index, handbook conclusion or author-development explanation was supplied before this finding.
The finding is limited to the contradictory reduction multiplicity below.
It does not claim a completed whole-proof review, a complete native-data inspection or a new review of the original source papers.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Reduction-multiplicity defect](#reduction-multiplicity-defect) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Reduction-multiplicity defect](#reduction-multiplicity-defect) | [Exact current statement](../../claims/Yin_C_G0572_v1.md#statement) | Only the P6 sentence asserting reduction multiplicity4; this concrete assertion is false. No whole-statement or whole-proof PASS is supplied. |
| [Reduction-multiplicity defect](#reduction-multiplicity-defect) | [Exact control table and depth argument](../../claims/Yin_C_G0572_v1.md#three-actual-reciprocal-low-energy-controls) | The complete P6 reduction is Phi3 cubed in the control table, and the root-depth argument explicitly uses multiplicity three. |
| [Reduction-multiplicity defect](#reduction-multiplicity-defect) | [Multiplicity and period mechanism](../../claims/Yin_C_G0572_v1.md#reciprocal-binary-trinomial-classification) | Exact order h uses the least power of two covering the actual factor exponent; that covering power differs from the exponent itself. |

## Reduction multiplicity defect

The current Statement says that P6 retains “reduction multiplicity4”.
Here P6=t^6-t^5-t^3-t+1, whose complete reduction in F2[t] is
\[
 \overline{P6}=t^6+t^5+t^3+t+1=(t^2+t+1)^3.
\]
Indeed \((t^2+t+1)^2=t^4+t^2+1\) in characteristic two, and multiplication by \(t^2+t+1\) gives exactly the displayed reduction.
The quadratic is irreducible over F2, since neither zero nor one is a root.
Its exponent in the complete factorization is therefore exactly three, not four.

The same fixed argument's Section 4 control table states Phi3 cubed.
Its subsequent every-root depth derivation explicitly uses reduction multiplicity three and the bound e<=3.
Section 2 sets the binary primary exponent to \(2^{\lceil\log_2 E\rceil}\); for E=3 this covering exponent is four, giving h=12.
This does not make the reduction factor exponent four.
The contradiction concerns the new Statement's multiplicity assertion.

This finding by itself does not reject h=12, the depth4/3 claim, the norm256 claim, the general classification or the actual native calculation.
Their complete review requires its own exact input coverage.
No J51 program was executed, and no original execution or earlier reviewer replay is counted as this review's reproduction.
No C mathematics or decision was edited or adopted by this reviewer.
Any corrected version requires its actual new acceptance evidence; this finding remains tied to the false v1 Statement.
