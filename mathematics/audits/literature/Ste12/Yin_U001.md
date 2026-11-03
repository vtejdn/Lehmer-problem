---
author: Yin
---
# Ste12-U001: initial unit runs and constant cyclic-resultant prefixes

Date: 2026-10-18T16:20.
Human record author Yin.
The loglog_cyclic_review agent directly read these primary statements while checking whether G0001's proposed linear unit-prefix rigidity question was new.
This unit records the established source interfaces and the historical conjecture separately; it does not claim an original-proof audit or current resolution of the conjecture.

<a id="ste12-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: C. L. Stewart, Exceptional units and cyclic resultants, Acta Arithmetica155.4 (2012),407--418, DOI10.4064/aa155-4-5; retained institutional author-hosted typeset article, twelve PDF pages.

Passages: Printed407/PDF1 definitions; printed408/PDF2 Corollary1; printed409--410/PDF3--4 cyclic/cyclotomic normalization and Corollary2; printed417/PDF11 historical e(d) statement and conjecture.

Inspection: Source identity, standing nonzero hypothesis, both complete corollary statements and exact historical conjecture text read directly in the primary PDF text, with local extraction compared against the primary web PDF. The transcendence, prime-counting and computational proofs were not re-audited; no new numerical constants or Groebner certificate reproduction.


The [retained PDF](../../../literature/pdf/Ste12.pdf) and [section navigation](../../../literature/contents/Ste12.md) supply the exact reading target.
This is a different work from the already retained Ste13 sequel.

<a id="exceptional-unit-prefix-definition"></a>
## Definition and established bounds

Let alpha be a NONZERO algebraic integer of degree d over Q and K=Q(alpha).
The source defines E0(alpha)=0 if alpha-1 is not a unit of O_K; otherwise it is the largest N for which alpha^j-1 is a unit for every1<=j<=N.
The standing nonzero restriction matters: alpha=0 would make every difference equal-1 and is outside this domain.
A root of unity is allowed in Corollary1; its zero difference at its order is not a unit.

Corollary1 gives an effectively computable absolute c1>0 such that

    E0(alpha)<=c1 d (log(d+1))^4/(log log(d+2))^3.

No numerical c1 is supplied or computed here.
This is a near-linear degree bound with a genuine unbounded logarithmic factor, not a universal fixed multiple of d.

For f in Z[t] monic of degree d>=1, the source defines the SIGNED complete cyclic resultant

    R_n(f)=Res(f,t^n-1)=product_(all roots alpha_i)(alpha_i^n-1),

with all multiplicities retained.
Corollary2 supplies an effectively computable absolute c2>0: if f is not t^d, f(1)!=0, and

    |R_1(f)|=...=|R_k(f)|,

then

    k<c2 d (log(d+1))^4/(log log(d+2))^3.

The common absolute value need not be1.
Neither irreducibility, reciprocity nor an integer-unit constant coefficient is required by that statement.
With C_n(f)=Res(f,Phi_n), the exact factorization R_n=product_(j|n)C_j shows that the constant-prefix condition is equivalent to |C_2|=...=|C_k|=1 when f(1)!=0.
The source retains C_1 separately; replacing every cyclotomic layer by1 would change this general condition.

These two established corollaries are accepted at their exact primary-statement and applicability scope for the reuse comparison.
The original proof, its invoked Baker--Wustholz/Dobrowolski inputs and its constants are not newly audited.

<a id="historical-linear-prefix-conjecture"></a>
## Historical linear question and application limit

Printed417 defines e(d) as the maximum of E0 over the paper's nonzero degree-d algebraic integers.
The paper reports e(d)=d for1<=d<=6, e(7)<7 and e(8)>=7, and states its suspicion that e(d)<d for every d>=7.
The finite-degree reports are read as published computational results, not reproduced or needed as project proof premises.
The final assertion is a historical CONJECTURE, not an established inequality or a claim that no later work has resolved it.
The sequel Ste13 Section6 repeats that history, but its prior local source screen did not cover that section.

For the G0001 original monic irreducible nontorsion unit P, all C_n=abs Norm(alpha^n-1) are nonzero integers.
The condition C_1=...=C_N=1 is therefore precisely E0(alpha)>=N.
This makes the proposed fixed-linear-prefix rigidity question a specialization of an existing question rather than a new consequence of the project's higher Smith-depth capacity construction.
The original-order unit equivalence and any additional finite-prime control belong to their project consumer, not to Stewart's theorem.
Even finding one n<=Cd with C_n>1 guarantees only log C_n/d>=log2/d.
No positive d-scale norm income, uniform Mahler gap or automatic near-one coverage follows from that fact alone.

No full-paper, source-proof, computational-certificate or independent audit is claimed by this unit.
