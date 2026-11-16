---
author: Yin
---

# A conductor bound for central perturbations with repeated cyclotomic factors

<a id="statement"></a>
## Conductor bound and exceptional parent

Let \(A\) be a product of cyclotomic polynomials of orders at least three, with arbitrary positive multiplicities, of degree \(2d\) with \(d\ge2\) and \(A(z)=1+3z^2+O(z^4)\).
Put \(s=d-1\), take an odd \(r>2d+1\), and put \(p=r+2s=2n+1\) and \(m=(r-1)/2\).
Write \(A(z)=z^d C_A(z+z^{-1})\) and \(B_a(2\cos\theta)=\sin((2a+1)\theta/2)/\sin(\theta/2)\).
For a real polynomial \(H\) of degree at most \(h\), with \(h\ge0\) and \(H=0\) allowed, set
\[
 Q=C_A B_m+H,\qquad b_j=2\cos(2\pi j/p),\qquad \rho_j=Q(b_j)/B_n'(b_j).
\]
A strict terminal cut consists of an index \(1\le c<n\) with \(\rho_j>0\) for \(1\le j\le c\) and \(\rho_j<0\) for \(c<j\le n\).
Every such cut satisfies at least one of
\[
 p\le\max\{2s(h+2),48\pi(h+2d)\},\qquad
 A(z)=F_s(z)=(1+z^2)^2\frac{1-z^{2s}}{1-z^2}.
 \tag{1}
\]
For \(A=F_s\), no real constant \(H\) admits a strict terminal cut at any permitted \(p\).
Consequently every real constant perturbation of any parent in the stated coefficient class requires \(p\le96\pi d\), including the original central subtraction \(H=-1\).
All these assertions use the residues alone.

The [squarefree bound](Yin_C_G0890_v1.md#statement) supplies the underlying moment and integer arguments.
The main researcher extended its matching to repeated angles and developed the all-scalar comparison below, with the construction contributor checking the exceptional phase, parity and bounds on both nodes.
The neutral product \(F_s(z)(1-z^r)/(1-z)\) also occurs in the [different trace deformation](Yin_C_G0884_v1.md#inputs) with even length \(2s\) and odd length \(r\).

<a id="multiplicities"></a>
## Pairing repeated angles

Assume \(p\) exceeds the bound in (1).
The [grid identity](../ledger/Yin_L_G0457_v6.md#alternation) follows from the sine formulas for \(B_m,B_n'\) and therefore applies with all multiplicities.
With \(\theta_j=2\pi j/p\), the sign of \(\rho_j\) is the sign of \(W(\theta_j)+(-1)^{j+1}H(b_j)\), where
\[
 W(\theta)=C_A(2\cos\theta)\sin(s\theta)/\sin(\theta/2).
\]
Let \(P\) list the \(d\) upper root angles of \(A\) with multiplicity and \(S=\{k\pi/s:1\le k<s\}\).
The case \(d=2\) is impossible by the [degree-four calculation](Yin_C_G0890_v1.md#pairing), so \(s\ge2\).
Choose a cut angle \(\tau\) strictly between \(\theta_c,\theta_{c+1}\) and outside \(P\cup S\), and put \(X=S\cup\{\tau,\pi\}\).
Match one parent occurrence to each coincident sine point and remove these pairs from both lists.
Merge the residual lists in nondecreasing order with every remaining parent copy present, and pair the first two events, the next two, and so on.
Both original lists have size \(d\), so this pairs every event.

The product of \(W\) with the desired sign starts positive.
Between consecutive distinct interior event locations its sign is determined by the parity of the number of preceding residual events, since a root of multiplicity \(a\) contributes the factor \((-1)^a\) across its location.
The removed common pairs contribute even multiplicity.
The product ends negative before the listed endpoint \(\pi\), since the parent and sine factors together have \(d+(d-2)\) interior zeros counted with multiplicity and the cut supplies one sign reversal.
Every paired interval of positive length thus has the wrong phase throughout its interior, allowing zeros at removed common pairs.
Equal event locations give intervals of length zero when paired together.
All positive-length intervals have disjoint interiors and none contains \(\tau\) in its interior.

Write \(\Delta=2\pi/p\), and count \(m_i\) grid nodes strictly inside the \(i\)-th paired interval.
On those nodes the signed perturbation must strictly overcome a weakly wrong phase.
The prescribed sign is constant there, so consecutive interior nodes force alternating nonzero signs of \(H(b_j)\).
For \(H\ne0\) the disjoint intervals therefore require \(\sum_i\max(m_i-1,0)\le h\) by distinct real zeros of \(H\).
For \(H=0\) all \(m_i\) vanish.
Each length is at most \((m_i+1)\Delta\), also at \(\pi\) and for a zero-length pair.
There are at most \(d\) intervals, so every length is at most \((h+2)\Delta<\pi/s\) and their sum is at most \(\delta=(h+2d)\Delta<1/24\).
The spacing in \(S\cup\{\pi\}\) forces any pair internal to \(X\) to contain \(\tau\).
There is at most one such pair and, by the equal original sizes, equally many pairs internal to \(P\).

These are exactly the inputs to [the two-moment comparison](Yin_C_G0890_v1.md#moments).
Newton sums count roots with multiplicity, giving the same two differences \(D_1=0,D_2=-2\) there.
Each error estimate bounds a sum over individual matched occurrences, including the case of equal angles in the internal parent pair.
The comparison excludes the all-cross-pair case and matches the full parent root multiset to that of \(F_s\) at total chord length less than one.
The [integer rigidity argument](Yin_C_G0890_v1.md#integer-rigidity) then gives \(A=F_s\), proving (1).

<a id="scalar-exclusion"></a>
## Comparing the middle and last nodes for every scalar

For \(A=F_s\), normalization of the geometric sum on the unit circle gives
\[
 C_{F_s}(2\cos\theta)=4\cos^2\theta\,\frac{\sin(s\theta)}{\sin\theta},
 \qquad W(\theta)=\frac{4\cos^2\theta\,\sin^2(s\theta)}
                         {\sin\theta\,\sin(\theta/2)}\ge0
 \quad (0<\theta<\pi).
\]
Since \(p\ge4s+5\ge13\), the node \(j\) of parity \(n\bmod2\) nearest to \(p/4\) satisfies \(1\le j<n-1\) and \(|j-p/4|\le3/4\).
Indeed \(p/4\) has fractional part \(1/4\) or \(3/4\), and integers of either given parity have spacing two.
Thus \(|\theta_j-\pi/2|\le3\pi/(2p)\), so \(\pi/3\le\theta_j\le2\pi/3\).
Using \(|\cos\theta_j|\le3\pi/(2p)\), \(\sin\theta_j\ge\sqrt3/2\), and \(\sin(\theta_j/2)\ge1/2\) gives
\[
 W(\theta_j)\le \frac{12\sqrt3\,\pi^2}{p^2}.
\]
At the last node \(\theta_n=\pi-\pi/p\) one has \(4\cos^2(\pi/p)\ge3\) and \(\sin\theta_n\sin(\theta_n/2)\le\pi/p\).
By concavity on \([0,\pi/4]\), \(\sin(s\pi/p)\ge2\sqrt2\,s/p\).
It follows that
\[
 W(\theta_n)\ge\frac{24s^2}{\pi p}>\frac{12\sqrt3\,\pi^2}{p^2},
\]
where the strict comparison uses \(ps^2\ge52>\sqrt3\,\pi^3/2\).

If \(H\) is a constant, terminal negativity requires \((-1)^{n+1}H<-W(\theta_n)\).
The opposite parity therefore has strictly positive residues, including at \(n-1\).
The cut must be after \(n-1\), so positivity at the earlier index \(j\) of the same parity as \(n\) requires \(W(\theta_j)>|H|>W(\theta_n)\).
The two bounds exclude this for every permitted size.

## Assessment history

### Decision repeated-parent-draft

| Field | Value |
| --- | --- |
| date | 2026-11-16T07:58 |
| status | open |
| reason | Retain the multiset extension and its scalar exclusion for independent proof inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Conductor bound](#statement) | Repeated cyclotomic factors, bounded-degree real trace perturbations and every real scalar. |
| argument | [Repeated-angle pairing](#multiplicities) | Event parity, disjoint intervals and unchanged moment inputs. |
| argument | [Scalar exclusion](#scalar-exclusion) | Two nodes of the same parity on the exceptional parent and all permitted grid sizes. |
| dependency | [Squarefree proof's moment estimates](Yin_C_G0890_v1.md#moments) | Both matching cases for the excess roots. |
| dependency | [Integer rigidity](Yin_C_G0890_v1.md#integer-rigidity) | Equality from the total chord cost for two monic integer polynomials. |
| dependency | [Grid identity](../ledger/Yin_L_G0457_v6.md#alternation) | Positive prefactor and sign of the perturbation. |


### Decision repeated-parent-conductor-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T08:07 |
| status | proved |
| reason | Adopt the repeated-parent alternative and the all-scalar exclusion following independent proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Conductor bound](#statement) | Repeated cyclotomic factors, bounded-degree real trace perturbations and every real scalar. |
| argument | [Repeated-angle pairing](#multiplicities) | Event parity, disjoint intervals and unchanged moment inputs. |
| argument | [Scalar exclusion](#scalar-exclusion) | Two nodes of the same parity on the exceptional parent and all permitted grid sizes. |
| dependency | [Squarefree proof's moment estimates](Yin_C_G0890_v1.md#moments) | Both matching cases for the excess roots. |
| dependency | [Integer rigidity](Yin_C_G0890_v1.md#integer-rigidity) | Equality from the total chord cost for two monic integer polynomials. |
| dependency | [Grid identity](../ledger/Yin_L_G0457_v6.md#alternation) | Positive prefactor and sign of the perturbation. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v44.md#repeated-parent-review) | Full multiset extension, inherited moment and rigidity steps, middle-node comparison and all allowed scalar cases. |

## Current assessment
[Selected decision](#decision-repeated-parent-conductor-reviewed)
