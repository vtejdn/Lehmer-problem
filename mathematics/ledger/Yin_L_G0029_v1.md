---
author: Yin
---

# G0001: a strongly connected presentation gives an exponential shortness bound

Date: 2026-10-06.
The complete current mathematical home is [the responsible Claim](../claims/Yin_C_G0233_v1.md#argument), with [actual whole self-review](../audits/reviews/Yin_R_G0516_v1.md#current-compression-finding).
The original mathematical body remains its historical fixed input and substantive exploration.
Root for Yin with separate assigned AI review_matrix_completion.
This sharpens the quantitative conversion in [L G0027](Yin_L_G0027_v1.md#boundedness-equivalence).
It gives an explicit smaller presentation for an existing realization, not a uniform existence theorem or a Lehmer result.

<a id="scc-length-bound"></a>
## Statement

Let A in GL_N(Z) have characteristic polynomial p c, where p is monic irreducible, M(p)>1, and c is a monic cyclotomic product.
Put k=||A||_F^2-N.
There is a diagonal block A_* after a simultaneous permutation making A block triangular such that

    det(tI-A_*)=p c_*,       ||det(tI-A_*)||_1 <= 4^k,

where c_* is cyclotomic.
In particular the invariants of L G0027 satisfy

    L(p) <= 4^{E(p)}.

Unlike its earlier determinant construction, this bound uses the block's actual characteristic polynomial without adding a power of the signed-cycle determinant.
Both polynomial degree and matrix dimension are unrestricted.

## Selecting one component

Choose the signed permutation P and integer perturbation E=A-P using a nonzero determinant matching as in [L G0025](Yin_L_G0025_v1.md#bounded-excess-gap).
Contract every signed cycle of P to a vertex; each nonzero E_ij supplies a directed edge from the column's cycle to the row's cycle.
Strongly connected components can be topologically ordered, giving the asserted block triangular form.
Each P cycle lies wholly in one diagonal block.
The chosen matching entries cannot be canceled in A: P used their signs and E has the remaining magnitude there.

Every diagonal block is integral unimodular, since their integer determinants multiply to det A=+1 or -1.
Their monic characteristic polynomials multiply to p c.
Unique factorization and multiplicity one of p imply that exactly one block contains p, with all its remaining factors cyclotomic.
Select it as A_*=P_*+E_*.

Let r be its number of signed cycles, s the number of nonzero E_* entries, and q=sum|E_* entries|.
If r>1, strong connectivity requires at least one outgoing perturbation edge from each cycle, so r<=s.
If r=1, the presence of p forces s>=1.
The matching inequality and the nonnegative excess of all diagonal blocks give

    r <= s <= q <= k_* := ||A_*||_F^2-dim(A_*) <= k.

Off-diagonal blocks contribute additional nonnegative squares to k, so they cannot invalidate the last inequality.

## Minors of signed cycles

Set C=tI-P_*.
Expand det(C-E_*) by subsets T of perturbation entries.
Only subsets occupying distinct rows and columns contribute; their terms are

    +/- (product_{e in T} c_e) det C[I_T^c,J_T^c].

There is no factorial factor: a chosen set of entries fixes the matching on its rows and columns; the remaining sum is exactly the indicated cofactor.

The cofactor vanishes unless remaining row and column counts agree separately in each P cycle.
On a full signed cycle of length l and sign product sigma, the full minor is t^l-sigma, with coefficient norm 2.
Every proper square minor is zero or a signed monomial.
For l>=2, the bipartite graph of tI-P_cycle is one alternating cycle.
Deleting a row and a column breaks it into paths and isolated vertices.
A forest has at most one perfect matching, since two distinct perfect matchings would have a cycle as their symmetric difference.
Thus its determinant is zero or one signed monomial.
When l=1 the only proper square minor is the empty minor, equal to 1.

It follows that every cofactor has coefficient norm at most 2^r.
Submultiplicativity and the triangle inequality imply

    ||det(tI-A_*)||_1
      <= 2^r sum_{T partial matching} product_{e in T}|c_e|
      <= 2^r product_e(1+|c_e|)
      <= 2^{r+q} <= 4^k,

using 1+a<=2^a for positive integers a.
Cancellation only improves the bound.
Since det(tI-A_*)=p c_*, it is an admissible completion, proving the claim.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0005_v1.md#scope-and-review), with its original inspected scope and relationship.
