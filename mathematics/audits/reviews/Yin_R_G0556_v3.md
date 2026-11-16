---
author: Yin
---

# Independent arithmetic review of the four-phase certificate

An agent outside the construction reviewed J161 and its application in C336v2 for Yin on 2026-11-16T11:46 UTC.
The assignment supplied the fixed targets and arithmetic obligations without proof-development discussion or a previous review conclusion.

<a id="four-phase-arithmetic-review"></a>
## Exact coefficient comparison at all 31 exponents

I obtained the same signed test coefficient and integer floor as the supplied program at every integer \(k=-3,\ldots,27\).
The exceptional row \(k=1\) has floor \(2\) at coefficient index \(1\).
Among the other 30 rows the floor at index \(3\) has unique minimum \(1264\) at \(k=-2\).
For example, the endpoint floors at \(k=-3,27\) are respectively \(5871361787267\) and \(1365849653\).

I expanded \(A=z^{4\max(k,0)}(z^3-z-1)^4-z^{4\max(-k,0)}(1-z^2-z^3)^4\) directly by integer polynomial arithmetic.
For \(k\ne0\) its degree is \(4|k|+12\), with leading coefficient \(1\) for positive \(k\) and \(-1\) for negative \(k\).
At \(k=0\), the top and constant terms cancel, the leading term is \(-4z^{11}\), and the linear term is \(4z\).
Thus zero is a simple root in this row.

For an independent calculation of the coefficient at index \(u\), write \(A(z)=z^t Q(z)\), \(c=Q(0)\ne0\), \(j=u-t\) and \(Q(z)=c\prod_i(1-r_i z)\).
Here the \(r_i\) are the reciprocals of the nonzero roots.
Use the integer coefficients \(a_i=[z^i]Q(cz)/c\), so \(\sum_i a_i z^i=\prod_i(1-c r_i z)\).
With missing \(a_i=0\), the logarithmic derivative gives the Newton sums \(s_m=\sum_i(c r_i)^m\) for \(1\le m\le256j\) by
\[
 s_m=-m a_m-\sum_{i=1}^{m-1} a_i s_{m-i}.
\]
Set \(b_0=1\) and \(b_h=-h^{-1}\sum_{i=1}^{h}s_{256i}b_{h-i}\) for \(1\le h\le j\).
These are the coefficients of \(\prod_i(1-(c r_i)^{256}X)\).
Multiplying \(A(\xi z)\) over \(\xi^{256}=1\) and putting \(X=z^{256}\) gives the signed test coefficient
\[
 [X^u]G^8(A)=(-1)^t c^{256}b_j/c^{256j}.
\]
The factor \((-1)^t X^t\) is the contribution of the zero roots.
I implemented these two Newton recurrences in exact integer arithmetic, checked divisibility before each quotient, and compared every result with eight iterations of the supplied even/odd squaring code.
I also ran the certificate program as published and obtained the displayed two table rows.

For either degree parity, \(G(A)(z^2)=A(z)A(-z)\) preserves degree, squares all roots with multiplicities and squares the absolute leading coefficient.
Thus \(M(G^8(A))=M(A)^{256}\), also for the nonmonic degree-eleven row.
The triangle inequality on the elementary symmetric expansion gives \(|[X^u]G^8(A)|\le\binom{\deg A}{u}M(A)^{256}\).
All computed floors are at least two, yielding the uniform margin \(M(A)\ge 2^{1/256}(41/20)\).

For the application, \(0\le h=\deg H\le30\) and \(d=N+3-h\) place \(k=N-d=h-3\) in the tested interval, while the fourth power removes \(\sigma\).
Equation (1) of C336v2 then gives \(\log C_{4d}\ge d\log(41/20)+d(\log 2)/256-O(\log d)\).
The last two terms have positive sum for all sufficiently large \(d\).
The product bound \(C_{4d}\le 2^d M(S)^{4d}\) now yields the strict \(\log M(S)>\tfrac14\log(41/40)\).
This finding covers the exact computation and its fourth-multiple application using the stated torsion-degree and transfer inputs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Four-phase arithmetic](#four-phase-arithmetic-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Four-phase arithmetic](#four-phase-arithmetic-review) | [J161 certificate](../../computations/programs/Yin_J_G0161/readme.md#four-phase-certificate) | Both table rows, every signed coefficient and integer floor on the full 31-input domain, degree, zero roots and absolute leading coefficient. |
| [Four-phase arithmetic](#four-phase-arithmetic-review) | [J161 program](../../computations/programs/Yin_J_G0161/four_phase.py) | Fourth powers, shifts, high-coefficient cancellation, degree, chosen indices, scaling, exact division and reported minima. |
| [Four-phase arithmetic](#four-phase-arithmetic-review) | [J144 squaring code](../../computations/programs/Yin_J_G0144/pilot.py) | The imported Graeffe transform at both degree parities and for nonmonic input. |
| [Four-phase arithmetic](#four-phase-arithmetic-review) | [C336v2 fourth multiple](../../claims/Yin_C_G0336_v2.md#fourth) | Complete arithmetic justification and its implications for the strict original-degree cyclic and Mahler bounds. |
| [Four-phase arithmetic](#four-phase-arithmetic-review) | [C336v2 transfer](../../claims/Yin_C_G0336_v2.md#transfer) | The degree offset and application of the stated uniform logarithmic error at \(j=4\). |
| [Four-phase arithmetic](#four-phase-arithmetic-review) | [L462v24 admissible degrees](../../ledger/Yin_L_G0462_v24.md#all-delays) | Use of \(h\le30\) for the torsion factor at both signs and sufficiently large delays. |
