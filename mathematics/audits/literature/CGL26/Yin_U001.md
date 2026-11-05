---
author: Yin
---

<a id="cgl26-u001"></a>
# CGL26-U001: construction scope and existing sparse-gap coverage

The [v1 original](readme.md) was inspected at its abstract and Sections 4.1--4.2, with PDF pages 16--17 rendered and checked against the versioned HTML.
Equation (15) gives

    F(X,Y)=X(X+1)Y^2+(X^2+X+1)Y+(X+1).

Equation (19) defines a seven-term integer family; its k=0 case is a signed monomial substitution into F.
The construction removes cyclotomic factors and tests the quotient.
The reported finite searches and the further asymptotic, irreducibility and cyclotomic-classification arguments were not independently verified here; no data or code were rerun.

For the project comparison, every nonzero numerator Q has at most seven collected terms.
The already accepted [DS17 fixed-support gap](../DS17/Yin_U001.md#ds17-u001) applies to Q.
If P=Q/Phi with Phi cyclotomic, then m(P)=m(Q); [L19's existing completion argument](../../../ledger/Yin_L_G0019_v1.md#cyclotomic-support-escape) therefore already excludes a positive-measure sequence tending to zero in this entire supplied family.
An arbitrary selected factor requires a separate argument; [C92](../../../claims/Yin_C_G0092_v1.md#statement) supplies one when Q's span divided by the original factor degree is bounded.
Neither comparison supplies bounded-support completion for arbitrary near-one inputs.
