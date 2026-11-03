---
author: Yin
---
# BS09-U001: multiple-prime derivations and commuting Frobenius lifts

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

Date: 2026-10-15.
Root records strategy_critique's actual SOURCE-only inspection for the fixed-prime quotient inquiry.
The source checker supplied no project proof.
This is classical algebraic mechanism attribution, not an Archimedean estimate for the project auxiliaries.

<a id="bs09-u001"></a>
## Read; exact algebraic interface and attribution

## Source and inspection

Source edition: Alexandru Buium and Santiago R. Simanca, Arithmetic Laplacians, actual arXiv:0805.0256v1,2 May2008,27 pages. The published work is Advances in Mathematics220(1)(2009),246--277; those are not this artifact's page numbers.

Source passages: Title and Sections1.3--1.4 scope; Section2.1 printed/PDF6--7, Definitions2.1--2.2, equations(9)--(15), Remarks2.3--2.4.

Inspection: Definitions, exact displayed compatibility and adjacent conventions read. Accepted for this algebraic interface; not a whole27-page proof audit or a theorem about evaluation in an arbitrary algebraic order.

For a prime p the source uses C_p(X,Y)=(X^p+Y^p-(X+Y)^p)/p and delta_p(n)=(n-n^p)/p on integers.
In the same-ring setting the displayed source p-derivation rules are delta_p(x+y)=delta_p(x)+delta_p(y)+C_p(x,y), and delta_p(xy)=x^p delta_p(y)+y^p delta_p(x)+p delta_p(x)delta_p(y).
Its associated Frobenius lift is phi_p(a)=a^p+p delta_p(a).

For different primes p,q the source equation (12) is the INTEGER polynomial

    C_(p,q)(X0,X1,X2)
      =C_q(X0^p,pX1)/p-C_p(X0^q,qX2)/q
       -[delta_p(q)/q]X2^p+[delta_q(p)/p]X1^q.

Integrality concerns the complete combination, not each displayed fraction separately.
For a finite set of distinct primes, equation (14) has the order

    delta_p delta_q(a)-delta_q delta_p(a)
      =C_(p,q)(a,delta_p(a),delta_q(a)).

It implies the commuting-lift equation (15), phi_p phi_q=phi_q phi_p.
The reverse implication in this same-ring setting assumes every selected prime is a nonzero divisor in A.
Separately, recovering a p-derivation uniquely from a map A->B by division by p requires p to be a nonzero divisor in B.
These are different hypotheses and neither is silently omitted.
The same source discussion also gives phi_p delta_q(a)=delta_q phi_p(a) under its stated compatible structure.

The pair 2,3 is allowed by this Section 2.1 framework; restrictions in later arithmetic-group results are not transferred to this elementary interface.
It identifies the classical source for polynomial-ring calculations with commuting substitutions.
It does NOT say such substitutions preserve a chosen minimal-polynomial ideal or descend to Z[alpha]; that is a separate project obligation.
The selected reading and bounded full-text keyword screen found no bound on the actual P(alpha^p)/p Archimedean size.
This is not a whole-paper or whole-literature nonexistence assertion.

The [retained v1](../../../literature/pdf/BS09--arxiv-v1.pdf) identifies the inspected source edition.
There is no printed contents list; Section1.4 is an organization paragraph, not a table of contents.
A Borger all-prime lambda-model lead was not used, its attempted acquisition failed, and no theorem from it is accepted here.
The bounded search stopped after the precise multi-prime algebraic interface was located and its missing height role identified.

## Actual source correction

2026-10-15T12:39.
The source-only final comparison identified that the earlier account attributed delta_p(1)=0 to the displayed source Definition2.1/Eq9, which explicitly lists the addition and multiplication rules.
The corrected account removes that extra display attribution; it neither denies a separately adopted unital convention nor changes the checked mixed-prime polynomial or nonzero-divisor guards.
