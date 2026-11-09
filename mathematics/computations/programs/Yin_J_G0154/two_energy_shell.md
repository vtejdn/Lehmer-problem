---
author: Yin
---

# Complete integer-square exclusion at energies one and two

<a id="scope"></a>
## The fixed conductor-81 square class

Use \(p=81\), \(k=9\), and exactly the [balanced base and integer matrices](low_energy_shell.md#scope)
\[
 h_*=h_{0,81}U_2^6U_1^{-1}\bigl(J_5(T_3)^2\bigr)^{-1},
 \qquad H=h_*(J),\qquad G=(2J+3I)H.
\]
The variables are all \(v\in\mathbb Z^{40}\) in the monic basis \(U_i(t/2)\).
They give \(h=h_*v^2\bmod B\), with \(K=v^THv\), \(L=v^TJHv\), and \(E=v^TGv=3K+2L\).
The [new program](two_energy_shell.py) completely traverses \(0<E\le2\) modulo \(v\mapsto-v\).
Every integer square multiplier is eligible, including nonunits and inputs having a zero component at some grid pole.

The exact result is
\[
       v^TGv\notin\{1,2\}\qquad\text{for every }v\in\mathbb Z^{40}.
\]
Consequently the moment targets \((E,K)=(1,3)\) and \((2,6)\), corresponding to profiles \(x=1\) and \(x=2\), are empty throughout this integer-square domain.
This conclusion concerns the specified square-multiple family.
Coverage of additional sign-compatible inputs requires a corresponding representation argument.

<a id="exact-enumeration"></a>
## Exact construction and completed traversal

The program reuses the frozen base-construction and downstream hit-checking routines from [low_energy_shell.py](low_energy_shell.py).
It regenerates the base from its specified unit word and checks \((K,L,U)=(-3,10,-30)\) and absolute norm 32.
The original Gram matrix is symmetric with positive fraction-free pivots and determinant
\[
                      \det G=20436467236384.
\]
FLINT's exact Gram LLL returns \(G'\) and \(A\), and the program checks
\[
                  |\det A|=1,\qquad G'=AGA^T.
\]
It also checks positive fraction-free pivots of \(G'\) and the same final determinant.
These identities certify a bijection between the original and reduced integer coordinates.
The actual run has \(\det A=1\).

The new traversal uses the [fraction-free completed-square formula](low_energy_shell.md#exact-traversal) with initial budget \(2D_{40}\).
At coordinate \(i\), it includes every integer obeying the exact bound obtained from the integer square root of the remaining numerator times \(D_{i-1}\).
Every division after subtracting a square is checked for zero remainder.
The highest nonzero coordinate is required to be positive, giving one representative of each nonzero pair under simultaneous negation.
The final remaining budget identifies each leaf's integer energy.
If a leaf is reached, its quadratic energy and both moments are independently evaluated in the reduced integer matrices.

The traversal has a fixed boundary of five million recursive tree nodes or 120 seconds, whichever comes first.
The actual traversal completed after 2084 tree nodes, before either limit.

| Energy | Nonzero classes modulo simultaneous sign | Joint target hits |
| ---: | ---: | ---: |
| 1 | 0 | 0 |
| 2 | 0 | 0 |

The generator exhausted every branch and returned `complete: true` with `stop_reason: complete`.
The earlier energy-six traversal retains its [partial scope](low_energy_shell.md#partial-result).

For any joint hit, the retained checking routine would recover \(v,h,C,Q,P\), evaluate \(\operatorname{Res}(B,v)\), use its nonvanishing to certify all original strict signs, check the strict endpoint, and enclose the full Mahler product with all root multiplicities.
The complete energy-one and energy-two enumeration produced no nonzero leaf, so it required no candidate-specific resultant, endpoint or root calculation.

<a id="reproduction"></a>
## Reproduction and output

Run from the repository root with Python, python-flint, SymPy and NumPy.
The retained J150 dependency imports NumPy at module load time.

~~~text
python -B mathematics/computations/programs/Yin_J_G0154/two_energy_shell.py
~~~

The retained dependencies are the native routines named by `low_energy_shell.py`, including its same-group base constructor and explicitly imported J151 matrix and polynomial operations.
The computation needs no preexisting generated JSON.
It writes the replaceable local output `mathematics/computations/outputs/Yin_J_G0154/two_energy_shell_81.json`, containing the base, integral change matrix, reduced Gram matrix, positive pivots, scope, counts and completion flag.
Different valid reduced bases can change the number and order of visited nodes.
The exact congruence checks and exhaustive termination determine the claimed coverage.
The reported checks are author-level computational checks.
