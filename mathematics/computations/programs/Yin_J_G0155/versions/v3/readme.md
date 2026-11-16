---
author: Yin
---

# The first conductor for integral zero-profile matches through indices six and seven

<a id="first-conductor"></a>
## The unique integer completion

In the [full odd-grid zero profile](../../../../../claims/Yin_C_G0881_v3.md#prefix-coordinates) with one strict terminal sign cut and the strict endpoint, \(p=55\) is the first conductor at which any integer input matches through coefficient index six.
Its unique such input also matches index seven and first differs at index eight.
Thus \(55\) is also the first conductor reaching index seven, and seven is the maximum matching index there.
The calculation for Yin's [Lehmer Task](../../../../../tasks/Yin_T_G0001_v1.md#contract) on 2026-11-16 takes the candidate identified by the main researcher and tests all completions of this prefix.

Write \(p=2n+1\), \(b_j=2\cos(2\pi j/p)\), \(E_0=1,\ E_1=t,\ E_{i+1}=tE_i-E_{i-1}\), \(B_0=1\) and \(B_i=E_i+E_{i-1}\) for \(i\ge1\).
The integer coordinates \(a_i\) specify \(h=\sum_{i=0}^{n-1}a_iE_i\), \(Q=tB_n+\sum_{i=0}^{n-1}a_iB_{n-i-1}\), and \(P(z)=z^{n+1}Q(z+z^{-1})\).
For \(p=55\) the witness has \(n=27\), \(26\) positive residues and a single negative last residue, with
\[
 (a_0,\ldots,a_{26})=
 (2,0,4,0,4,0,3,0,2,0,1,0,0,0,-1,0,-2,0,-2,0,-1,0,0,0,0,0,0).
\]
All \(27\) signs are certified by rational evaluation of \(h\) at the isolated ordered roots of \(B_{27}\), since \(\rho_j=(4-b_j^2)h(b_j)/p\).
The coefficient vector also has the factorization supplied by the construction collaborator and checked by exact expansion,
\[
 h(t)=u(u+1)(u+2)\bigl(1+T_2(u)-T_2(u)T_5(u)\bigr),\qquad
 u=t^2-2,\quad T_k(2\cos\theta)=2\cos(k\theta).
\]
The endpoint ratio is \(Q(-2)/B_{27}(-2)=-12\), so \(P(-1)=12\).
The signed resultant \(\operatorname{Res}(B_{27},Q)\) is \(7303\).
The reciprocal lift is monic of degree \(56\) with constant term one, and direct expansion gives
\[
   (1-z)(1-z^2)P-(1+z^2)^2=-z^8+O(z^9).
\]
This is equivalent to \(P-P_{*,0}=-z^8+O(z^9)\), with \(P_{*,0}=(1+z^2)^2/((1-z)(1-z^2))\).

<a id="enumeration"></a>
## The complete extensions of the five fixed coordinates

The [earlier enumeration](../v2/readme.md#first-conductor) excludes index six at every odd \(5\le p\le37\).
For each odd \(39\le p\le55\), the new search fixes \((a_0,a_1,a_2,a_3,a_4)=(2,0,4,0,4)\), which is equivalent to matching through index six.
At \(L=6\) the [real quadrature bound](../../../../../ledger/Yin_L_G0464_v24.md#quadrature-bound) gives \(6(2\kappa+1)\le p\) for the terminal block size \(\kappa\).
Thus the largest block to test is two at \(p=39,41\), three at \(p=43,45,47,49,51,53\), and four at \(p=55\).
All \(26\) remaining conductor and cut pairs were enumerated.

The [coefficient box and rational outer inequalities](../v2/readme.md#covering-box) depend only on the already fixed first two moments and apply without changing their bounds.
For each permitted cut, the new program substitutes all five prescribed coordinates into the full rational system, including its integer endpoint inequality.
It branches on every remaining coefficient using the [certified integer bounds](../v2/readme.md#integer-bounds), directly importing the existing node isolation, rational row enclosures, dual-multiplier checker and exact strict-sign test.
The linear solver only proposes multipliers for these integer-arithmetic implications.
Every complete outer leaf undergoes the original strict grid test.
The following are all the cuts with nonzero outer-leaf counts.

| Conductor \(p\) | Negative residues \(\kappa\) | Complete outer leaves | Exact grid zeros | Strict inputs |
| ---: | ---: | ---: | ---: | ---: |
| 45 | 1 | 4 | 4 | 0 |
| 45 | 2 | 1 | 1 | 0 |
| 51 | 1 | 3 | 3 | 0 |
| 55 | 1 | 1 | 0 | 1 |

The other \(22\) pairs have no complete outer leaf.
The strict input is the coefficient vector above.
This exhausts the integral chart at these conductors under the stated prefix, signs and endpoint, without any bound on the resultant or Mahler measure as a search condition.

<a id="complete-measure"></a>
## Factorization and complete measure

Exact integer factorization and multiplication back into \(P\) give
\[
                  P=\Phi_3\Phi_4\Phi_6\Phi_8\,R_{46}.
\]
The irreducible monic residual factor is
\[
 R_{46}(z)=\sum_{i=0}^{46}z^i+\sum_{i\in I}\bigl(z^i+z^{46-i}\bigr),
 \qquad I=\{2,3,8,9,10,11\}.
\]
The trace remainder \(Q-tB_{27}\) has degree \(26\) and leading coefficient two.
Together with the certified signs and endpoint, the [complete root count](../../../../../claims/Yin_C_G0881_v10.md#nonreal-pair) puts precisely one nonreal conjugate pair outside the unit circle.
Exact rational complex root counting finds one root of \(R_{46}\) in
\[
      [0.0003079691,0.0003079692]+i[1.2253983046,1.2253983047].
\]
Its squared modulus equals the complete Mahler measure, including the neutral factors, and the endpoints of the rectangle give
\[
                     1.5016010997 < M(P) < 1.5016011001 .
\]

<a id="reproduction"></a>
## Reproducing the conductor-55 calculation

The [native checker](long_prefix.py) contains the fixed integer vector and regenerates all arithmetic from the checkout.
The full command can distribute different cuts among processes, or run them in one worker by omitting the jobs option.
The witness-only command uses SymPy without the linear solver.

~~~text
python -B mathematics/computations/programs/Yin_J_G0155/versions/v3/long_prefix.py --jobs 4
python -B mathematics/computations/programs/Yin_J_G0155/versions/v3/long_prefix.py --witness-only
~~~

The author run used Python 3.14.3, SymPy 1.14.0, SciPy 1.17.1 and NumPy 2.4.4.
The full command atomically writes the [per-cut counts, strict inputs and witness](../../../../outputs/Yin_J_G0155/long_prefix_enumeration.json).
The witness-only command writes its [factorization and exact measure certificate](../../../../outputs/Yin_J_G0155/long_prefix_witness.json).
