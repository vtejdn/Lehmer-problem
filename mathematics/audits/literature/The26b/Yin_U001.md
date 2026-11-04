---
author: Yin
---
# The26b-U001: residue Frobenius lifts and original-field ramification degree

Date: 2026-10-15.
Root records direct selected online reading by g_bridge_audit and separate SOURCE-only checking/acquisition by strategy_critique.
The latter supplied no new project proof.

<a id="the26b-u001"></a>
## Read; accepted local-algebra statements and applicability

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Official Stacks Project stable-tag HTML snapshots09EC,09ED,09E8 obtained15 October2026. No whole-project commit was identified in these pages; they do not inherit the earlier chapter-PDF revision.

Passages: Definition15.114.3, Tag09EC; Lemma15.114.4, Tag09ED and its complete displayed short proof; Remark15.113.6, Tag09E8 and its displayed degree sum. Native tag anchors are retained in each original HTML.

Inspection: Entire indicated definition/statement/remark read, plus the short09ED proof. Referenced ancestor proofs and page comments were not audited or used as independent evidence. Standard statements accepted at the exact number-field application below.


In09EC, A is a discrete valuation ring with fraction field K, L/K is finite Galois with group G, and B is the integral closure of A in L.
For a maximal ideal m of B, its decomposition group D is the subgroup preserving m.
Its inertia group is the kernel of D acting on the residue extension kappa(m)/kappa_A.

Lemma09ED states that this residue extension is normal and that the map D->Aut(kappa(m)/kappa_A) is surjective.
With the additional separability of the residue extension it is Galois, giving surjectivity onto its Galois group.
Finite number-field residue extensions are finite fields and satisfy that separability hypothesis.
No unramified-prime hypothesis is imposed.
Thus residue Frobenius has a lift in the decomposition group even at ramified primes; different lifts need not have the same conjugacy size.
The source does not assert a bound on that size.

The displayed short proof uses Tags0BRJ and09EA; those ancestors were not recursively read in this inspection.
Its standard surjectivity statement is accepted without upgrading that boundary to a complete foundational proof audit.

Remark09E8 uses a finite SEPARABLE L/K, not necessarily Galois.
With the integral closure and all maximal ideals m_i above the DVR maximal ideal, it gives

    [L:K]=sum_i e_i f_i.

For a number field F/Q, take A=Z_(p) and L=F.
The sum includes ALL primes of F above p and all ramification indices, so each e_i<= [F:Q].
Under the normalized additive valuation v(p)=1, an integral element with positive valuation at that prime has valuation at least1/e_i.
The source's DVR setting supplies this value-group normalization; it does not use the degree or ramification of a larger normal closure in place of F.
Finiteness/Dedekind/degree-sum ancestor proofs are retained standard inputs and were not recursively audited.

These inputs support the project's supplied-Frobenius and local-valuation interfaces.
They do not establish the new intermediate subgroup, its index, conjugate counting, power-growth bound, original relative norm or a bounded-class hypothesis.
Those remain project arguments and conditions.
No bounded conjugacy class, automatic near-one coverage or new global Galois assumption is supplied by these tags.

Actual original files: [09EC](../../../literature/pdf/The26b/tag-09EC-20261015.html#09EC), [09ED](../../../literature/pdf/The26b/tag-09ED-20261015.html#09ED), [09E8](../../../literature/pdf/The26b/tag-09E8-20261015.html#09E8).
Their group links the three separate acquisition accounts.
The HTML retains native mathematics, anchors, references, scripts and comments unchanged.
External CSS/JavaScript were not downloaded, so no complete offline visual mirror is claimed.
No PDF page numbers or invented printed contents list are assigned to these HTML snapshots.
