---
author: Yin
---

# The complete radius-two unit window at the conductor-81 stationary base

<a id="scope"></a>
## Exact fixed window

Use \(p=81,k=9\), the [fixed conductor-81 base](balanced.md#descent-81)
\[
 h_*=h_{0,81}U_2^6U_1^{-1}(J_5(T_3)^2)^{-1},
 \qquad (K,L,E,U)=(-3,10,11,-30),
\]
and exactly the 37 totally positive units listed in phase two of that control.
Write them in their fixed order as \(u_1,\ldots,u_{37}\), including the 27 coprime-index \(U_a\), the eight displayed \(J_u(T_3)^2\), and \(J_5(T_9)^2,J_7(T_9)^2\).
The present finite set is labelled by
\[
 h_{\mathbf e}=h_*\prod_{i=1}^{37}u_i^{e_i},
 \qquad \mathbf e\in\mathbb Z^{37},\qquad \sum_i|e_i|\le2.
\]
The labels consist of zero, \(\pm e_i\), \(\pm2e_i\), and \(\pm e_i\pm e_j\) for \(i<j\).
Their total number is
\[
                  1+2\cdot37+2\cdot37+4\binom{37}{2}=2813.
\]
The traversal retains every label, even if two labels were to give the same integral polynomial.
It performs no energy pruning, new descent, random restart or Galois filtering, and includes no exponent vector of length three.

<a id="exact-method"></a>
## Reconstruction, moments and de-duplication

[unit_ball.py](unit_ball.py) reconstructs \(h_{0,81}\), the exact net word for \(h_*\), and all 37 units from their retained source functions.
It reads no generated JSON input.
The imported constructions verify integral inverse identities; their unit and positivity properties are those checked in the [balanced control](balanced.md#scope).
The reconstructed base's resultant is again checked directly to be 32.
Every input therefore has the same strict signs and absolute resultant 32.

For a symmetric normalized cyclic word \(w\), compute
\[
        K=w_0-w_2,\quad L=w_1-w_3,\quad E=3K+2L,\quad U=w_0-w_1.
\]
The sign separator \(c=-3/2\) gives \(E>0\).
The program checks this for every label but never uses an upper energy bound to discard an input.
For every one of the 2813 words, it independently reconstructs the ordinary trace polynomial and forms \(C=Dh\bmod B\).
It checks
\[
 [t^{n-1}]C=K,\qquad
 [t^{n-2}]C-K[t^{n-1}]B=L,\qquad C(-2)=-UB(-2).
\]
Thus both moments and the endpoint functional are checked through ordinary polynomial arithmetic, separately from their cyclic coefficient formulas.

De-duplication uses the entire normalized word, which determines the unique trace polynomial of degree below \(n=40\).
It is performed for reporting only, after the input label has been retained.
There are exactly 2813 distinct resulting \(h\), so no two labels in this window coincide.
The output retains each label, its word index, the full distinct words, and the complete joint distribution of \(K,L,E,U\), including label multiplicities.

<a id="results"></a>
## Complete finite outcome

The minimum energy is 11, attained only by the zero label \(h_*\).
The maximum energy is 792164.
Thus allowing all two-coordinate interactions and all single-coordinate squares does not lower the energy in this particular window.
This does not establish a global minimum in the unit orbit.

The five target profiles give the following complete counts:

| \(x\) | Required \((K,L)\) | Required \(E\) | Labels at that energy | Joint-moment labels | Distinct joint-moment \(h\) |
| ---: | --- | ---: | ---: | ---: | ---: |
| \(-2\) | \((6,8)\) | 34 | 17 | 0 | 0 |
| \(-1\) | \((3,4)\) | 17 | 3 | 0 | 0 |
| 0 | \((2,0)\) | 6 | 0 | 0 | 0 |
| 1 | \((3,-4)\) | 1 | 0 | 0 | 0 |
| 2 | \((6,-8)\) | 2 | 0 | 0 | 0 |

The three energy-17 labels, expressed as multipliers of \(h_*\), are:

| Multiplier | \((K,L,U)\) |
| --- | --- |
| \(U_{13}\) | \((1,7,-25)\) |
| \(U_{32}\) | \((-3,13,-34)\) |
| \(U_{23}U_{31}^{-1}\) | \((-3,13,-51)\) |

None has the required \(K=3\).
At energy 34 the set of first moments is
\[
 \{-56,-32,-24,-20,-16,0,2,4,8,14,38,140,214\},
\]
which omits the required \(K=6\).
All 17 labels and their individual \(L,U\) values are retained in the full output rather than collapsed by their first moment.

There is no moment-matching lift \(P\) in this window, so both the number of distinct matching \(P\) and the number passing the strict endpoint are zero.
No whole-measure root computation was called.
The exact endpoint functional was nevertheless checked for every input through \(C(-2)\); a matching lift would have \(P(-1)=2+2x+U\).
The native program reuses the existing exact polynomial reconstruction and complete-root certificate routines if a target hit occurs, counting a repeated matching polynomial only once for root certification.
No inference about an unexecuted root certificate is used in the present conclusion.

The window tests only the listed radius-two exponent labels at this fixed base.
It does not cover arbitrary positive units, longer words, different bases, or arbitrary integral square-root vectors.
For every probability law supported on this finite window, hitting any of these five exact moment targets has probability zero; this is not an unrestricted small-Mahler-shell exclusion.

<a id="reproduction"></a>
## Reproduction and checking scope

Run with the same Python, python-flint, SymPy and NumPy dependencies as the [baseline program](readme.md#reproduction):

~~~text
python -B mathematics/computations/programs/Yin_J_G0154/unit_ball.py
~~~

The command completed the full 2813-label traversal and all 2813 ordinary-polynomial cross-checks.
It writes the reproducible local file
`mathematics/computations/outputs/Yin_J_G0154/unit_ball_81.json`.
That file contains the summary, exact fixed base, ordered unit labels, every exponent label and \(K,L,E,U\), all distinct words, complete joint and energy histograms, target label numbers, and any matching-polynomial certificates.
No generated file is required to reproduce it.
These are author-level exact computation checks, without a claim of independent project review.
