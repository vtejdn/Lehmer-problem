---
author: Yin
---

# A conductor bound from angular matching for centrally perturbed cyclotomic products

<a id="statement"></a>
## Conductor and perturbation degree

Let \(A\) be a squarefree product of cyclotomic polynomials of orders at least three, of degree \(2d\), with \(d\ge2\) and \(A(z)=1+3z^2+O(z^4)\).
In the [squarefree-parent construction](../ledger/Yin_L_G0457_v6.md#degree-obstruction) put \(s=d-1\), take an odd \(r>2d+1\), and set \(p=r+2s=2n+1\), \(m=(r-1)/2\).
Write \(A(z)=z^d C_A(z+z^{-1})\), \(B_a(2\cos\theta)=\sin((2a+1)\theta/2)/\sin(\theta/2)\) and \(b_j=2\cos(2\pi j/p)\).
For \(H\in\mathbb R[t]\) of degree at most \(h\), with \(h\) a nonnegative integer and the zero polynomial allowed, form
\[
 Q=C_A B_m+H,\qquad \rho_j=Q(b_j)/B_n'(b_j)\quad(1\le j\le n).
\]
If for some \(1\le c<n\) the first \(c\) residues are strictly positive and all the rest strictly negative, then
\[
 p\le\max\{2(d-1)(h+2),\ 48\pi(h+2d)\}.                         \tag{1}
\]
In particular \(H=-1\) requires \(p\le96\pi d\), independently of the orders, number or coefficients of the cyclotomic factors.
This is necessary even without the endpoint condition.
It leaves open the comparable-degree regime, including varying parents with \(p/d\) bounded.
It gives no lower bound on the Mahler measure outside the sign test.

<a id="pairing"></a>
## Alternation on intervals between root angles

Assume \(p\) exceeds both quantities on the right of (1).
Let \(P\) be the multiset of the \(d\) upper-half-circle root angles of \(A\), in radians, and let \(S=\{k\pi/s:1\le k<s\}\).
The case \(d=2\) cannot occur because \(1+3z^2+z^4\) has roots off the unit circle, so \(s\ge2\).
The [grid identity](../ledger/Yin_L_G0457_v6.md#alternation) expresses the sign of \(\rho_j\) as the sign of
\[
 W(\theta_j)+(-1)^{j+1}H(b_j),\quad
 \theta_j=2\pi j/p,\qquad W(\theta)=C_A(2\cos\theta)\frac{\sin(s\theta)}{\sin(\theta/2)}.
\]
Choose \(\tau\in(\theta_c,\theta_{c+1})\) distinct from all the root and sine angles.
The desired sign is positive before \(\tau\) and negative after it.
The phase \(W\) starts and ends positive on \((0,\pi)\): the parent cosine factor starts positive and reverses at its \(d\) simple zeros, and the sine factor reverses at the \(d-2\) interior sine zeros.

Put \(X=S\cup\{\tau,\pi\}\).
First match every common angle of \(P\) and \(S\) at distance zero and remove it from both lists.
The remaining interior angles in \(P\) and \(X\) are distinct.
At each such angle the product of the desired sign and the phase changes sign.
This product starts positive and ends negative.
Adjoin the listed endpoint \(\pi\) and pair the remaining events in consecutive order, first with second, third with fourth, and so on.
The interiors of the paired intervals are precisely the intervals where the phase has the wrong sign, up to the removed double zeros.

Write \(\Delta=2\pi/p\) and let \(m_i\) be the number of grid nodes strictly inside the \(i\)-th such interval.
At these nodes the strict required sign forces \(H(b_j)\) to have alternating nonzero signs, even if \(W(\theta_j)=0\) at a removed double zero.
The desired sign is constant there because \(\tau\) cannot lie in the interior.
If \(H\ne0\), the intervals therefore require at least \(\sum_i\max(m_i-1,0)\) distinct zeros of \(H\), since \(b_j\) decreases strictly and the intervals are disjoint.
If \(H=0\), all \(m_i=0\).
In either case \(m_i\le h+1\) and \(\sum_i\max(m_i-1,0)\le h\).
Each interval has length at most \((m_i+1)\Delta\), also for the last interval ending at \(\pi\), by the spacing of the grid.
There are at most \(d\) intervals, so each length is at most \((h+2)\Delta<\pi/s\) and their total length is at most
\[
 \delta=(h+2d)\Delta<1/24.                                      \tag{2}
\]
The points in \(S\cup\{\pi\}\) are at least \(\pi/s\) apart.
Consequently any pair of two \(X\)-points must contain \(\tau\), so there is at most one such pair.
Both lists have size \(d\), hence there are equally many pairs of two \(P\)-points and pairs of two \(X\)-points.

<a id="moments"></a>
## The two excess roots

For \(j=1,2\) define
\[
 D_j=\sum_{a\in P}\cos(ja)-\sum_{b\in S}\cos(jb).
\]
The monic reciprocal parent has linear coefficient zero and quadratic coefficient three at either end.
Its first two power sums are therefore \(0,-6\).
The angles in \(S\) and their conjugates are all the \(2s\)-th roots except \(1,-1\), whose removal gives power sums \(0,-2\) for \(s\ge2\).
It follows that \(D_1=0,\ D_2=-2\).
The total error in a sum of \(j\)-th cosines over any subset of the matched pairs is at most \(j\delta\), by the Lipschitz estimate on each pair.

If all pairs are between the two lists, then \(|D_2-(\cos(2\tau)+1)|\le2\delta\).
This contradicts \(D_2=-2\).
Thus a unique pair \(\alpha,\beta\) of parent angles is paired within \(P\).
We now match \(P\) instead to the multiset \(S\cup\{\pi/2,\pi/2\}\) and bound the sum of the chord distances on the upper unit semicircle.
An angular displacement bounds its chord length.

If \(\tau\) is paired with \(\pi\), each sine point is already matched to a parent.
Using one member of the extra pair twice in \(D_1\) costs at most \(|\alpha-\beta|\), included in (2).
Hence \(|2\cos\alpha|,|2\cos\beta|\le\delta\).
An upper unit root at angle \(x\) has distance at most \(\sqrt2|\cos x|\) from \(i\), by squaring and using \(1-\sin x=\cos^2x/(1+\sin x)\).
The new matching has total upper chord length at most \((1+\sqrt2)\delta\).

In the remaining case \(\tau\) is paired with \(b\in S\), while \(\pi\) is paired with a parent angle.
Set \(u=\cos b\) and \(t=\cos\alpha\).
Retain the other sine matches, replace that last parent angle by \(\pi\), and use \(\alpha\) in place of \(\beta\).
The sum of all angular errors used in these replacements is at most \(\delta\).
Thus
\[
 |2t-1-u|\le\delta,\qquad
 4t^2+2(1-u^2)\le2\delta .
\]
The second bound follows by comparing \(D_2=-2\) with \(2\cos(2\alpha)+1-\cos(2b)=4t^2-2u^2\).
In particular \(u\le-1+\sqrt{2\delta}+\delta<0\), and then \(1+u\le1-u^2\le\delta\).
The first inequality gives \(|t|\le\delta\).
Reroute the parent at \(\pi\)'s end of a pair to \(b\) via \(-1\), paying extra chord length \(\sqrt{2(1+u)}\).
Match \(\alpha,\beta\) to \(i,i\), routing \(\beta\) via \(\alpha\).
The resulting upper chord sum is at most \(\delta+\sqrt{2\delta}+2\sqrt2\,\delta\).

<a id="integer-rigidity"></a>
## Integer coefficients force equality

In both cases the upper matching and its complex conjugate have total chord length less than one, since \(2((1+2\sqrt2)/24+\sqrt{2/24})<1\).
They compare the full root multisets of \(A\) and the monic integer polynomial
\[
 F(z)=\frac{z^{2s}-1}{z^2-1}(1+z^2)^2.
\]
For any two monic integer polynomials of the same degree with unit-circle roots matched at total chord cost \(L<1\), the polynomials are equal.
Indeed for every positive \(k\) the difference of their \(k\)-th power sums has magnitude at most \(kL<k\), by telescoping each matched pair of powers.
If the first unequal coefficient from the leading end has index \(k\), Newton's identities express the difference of these power sums as \(-k\) times that nonzero integer coefficient difference.
This is impossible.
Thus \(A=F\), contrary to squarefreeness because \(F\) has the repeated factor \((1+z^2)^2\).
This proves (1).

## Assessment history

### Decision conductor-bound-draft

| Field | Value |
| --- | --- |
| date | 2026-11-16T07:41 |
| status | open |
| reason | Retain the proposed uniform conductor bound for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Conductor bound](#statement) | All squarefree parents in the prescribed initial coefficient class, every terminal cut and all real polynomial perturbations within the specified degree. |
| argument | [Phase pairing](#pairing) | Grid signs, shared zero count, total displacements and possible same-list pairs. |
| argument | [First two moments](#moments) | Transport of the surplus roots to the double conjugate pair. |
| argument | [Integer rigidity](#integer-rigidity) | Exact coefficient conclusion and contradiction. |
| dependency | [Central perturbation sign identity](../ledger/Yin_L_G0457_v6.md#alternation) | The positive grid prefactor and the two phase summands at each grid node. |


### Decision angular-conductor-bound-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T07:44 |
| status | proved |
| reason | Adopt the conductor bound for every strict cut after independent review of the grid argument, angular matching and integer coefficient rigidity. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Conductor bound](#statement) | All squarefree parents in the prescribed initial coefficient class, every terminal cut and all real polynomial perturbations within the specified degree. |
| argument | [Phase pairing](#pairing) | Grid signs, shared zero count, total displacements and possible same-list pairs. |
| argument | [First two moments](#moments) | Transport of the surplus roots to the double conjugate pair. |
| argument | [Integer rigidity](#integer-rigidity) | Exact coefficient conclusion and contradiction. |
| dependency | [Central perturbation sign identity](../ledger/Yin_L_G0457_v6.md#alternation) | The positive grid prefactor and the two phase summands at each grid node. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v42.md#angular-matching-review) | Whole statement and proof, including the grid identity, every pairing case, the constants and the scope of the obstruction. |

## Current assessment
[Selected decision](#decision-angular-conductor-bound-reviewed)
