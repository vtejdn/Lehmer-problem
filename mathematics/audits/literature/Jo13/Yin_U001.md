---
author: Yin
---

# Primitive permutation groups with a full cycle

<a id="jo13-u001"></a>
<a id="full-cycle-classification"></a>
## The classified permutation actions

Let \(G\le S_n\) be primitive, let \(G\not\supseteq A_n\), and suppose that \(G\) contains an \(n\)-cycle.
The [published edition](readme.md#published-edition), Theorem 1.2(1), pp. 159–160, gives the following alternatives:

| Group in its indicated permutation action | Degree and parameters |
| --- | --- |
| \(C_p\le G\le\operatorname{AGL}_1(p)\) on \(\mathbb F_p\) | \(n=p\), with \(p\) prime |
| \(\operatorname{PGL}_d(q)\le G\le\operatorname{P\Gamma L}_d(q)\) in the projective point action | \(n=(q^d-1)/(q-1)\), with \(d\ge2\) and \(q\) a prime power |
| \(L_2(11)=\operatorname{PSL}_2(11)\) | Its exceptional degree \(11\) action |
| \(M_{11}\) or \(M_{23}\) | The degree \(11\) or degree \(23\) action, respectively |

Here the projective point set is the set of one-dimensional subspaces of \(\mathbb F_q^d\); the displayed containments are containments of permutation groups on that set.
Theorem 1.2 uses a single cycle with \(k\) fixed points, and the case adopted here is exactly \(k=0\).
A fixed-point-free permutation with several cycles does not by itself supply this hypothesis.
The lower projective bound is \(\operatorname{PGL}_d(q)\), not merely \(\operatorname{PSL}_d(q)\).

<a id="prime-degree"></a>
## Application to a transitive group of prime degree

For a transitive subgroup \(G\le S_p\) of prime degree, primitivity follows because every block size divides \(p\).
Orbit–stabilizer gives \(p\mid|G|\), so Cauchy's theorem supplies an element of order \(p\); in degree \(p\) this is a full \(p\)-cycle.
Consequently either \(A_p\le G\le S_p\), or one of the displayed alternatives holds with its displayed degree equal to \(p\).
This elementary specialization also agrees with published Remark 1.7, p. 160.

<a id="small-degree-even"></a>
## Evenness of the three exceptional groups

In the listed degree \(11,11,23\) actions,
\[
       L_2(11)\le A_{11},\qquad
       M_{11}\le A_{11},\qquad M_{23}\le A_{23}.
\]
For this additional interface, use the [inspected official ATLAS pages](../WWT+99/readme.md#exceptional-generators); Jones's classification statement alone is not being cited as a proof of evenness.

The ATLAS \(L_2(11)\) page, “Standard generators,” supplies generators \(a,b\) with \(b\) of order \(3\) and \(ab\) of order \(11\).
For the sign homomorphism of any permutation action, both odd-order elements have sign \(+1\), and hence \(a=(ab)b^{-1}\) also has sign \(+1\).
Thus the whole group is even, in particular in either degree \(11\) action; no identification with the degree \(12\) action is needed.

The ATLAS \(M_{11}\) page, “Standard generators,” gives natural degree \(11\) generators
\[
 a=(2\ 10)(4\ 11)(5\ 7)(8\ 9),\qquad
 b=(1\ 4\ 3\ 8)(2\ 5\ 6\ 9).
\]
Their signs are respectively \((-1)^4=1\) and \((-1)^{3+3}=1\).
The ATLAS \(M_{23}\) page supplies standard generators of orders \(2,4\), and its degree \(23\) representation page, “On conjugacy classes,” gives their cycle types as \(2^8\) and \(2^2 4^4\).
Their signs are \((-1)^8=1\) and \((-1)^{2+4\cdot3}=1\).
Since these pairs generate the indicated groups, the three containments follow.
In particular, an involution in any of these actions has an even number of transpositions.

I read the ATLAS generator descriptions, the degree \(23\) representation's order-\(2\) and order-\(4\) rows, and its linked GAP generator files; the latter directly confirm the stated cycle types.
I checked the sign computations above, while accepting the ATLAS identification and generation statements at their published-data scope.
I did not rerun the ATLAS presentation or group-order certifications, and no simplicity theorem is needed for this deduction.

<a id="action-scope"></a>
## Action and inspection boundaries

The classification concerns the actual permutation image, not just an abstract group isomorphism.
In particular, the degree \(11\) action of \(L_2(11)\) in this list is not its degree \(12\) projective-line action.
Likewise the \(M_{11}\) entry here has degree \(11\); the degree \(12\) action elsewhere in Theorem 1.2 belongs to a different case.
Applying a further fixed-point calculation requires its own justification in the listed action, including possible semilinear elements in the projective case.
This U does not classify involutions, signed lifts or permutation representations of these abstract groups in other degrees.

I inspected the original published PDF pp. 159–161, including rendered formulas, and compared the adopted statement with the [author manuscript](readme.md#arxiv-v1), pp. 1–3.
Published §2, p. 161, attributes the \(k=0\) case to Jones's earlier paper [12], completing Feit's work [11]; Remark 1.11 on that page states the reliance on the classification of finite simple groups.
The established classification is used here at the theorem-statement level.
Neither the earlier classification proofs nor the classification of finite simple groups were independently audited for this U.
