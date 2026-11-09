---
author: Yin
---

# Complete energy-six controls for three fixed conductor-81 square families

<a id="scope"></a>
## The three bases and the finite question

[energy_six.py](energy_six.py) uses \(p=81\), terminal cut \(k=9\), and exactly three previously fixed inputs.
The [original balanced base](balanced.md) is
\[
 h_*=h_{0,81}U_2^6U_1^{-1}(T_3/T_{15})^2,\qquad U_a=2+T_a.
\]
The [single-filter input](nonsquare_control.md#scope) is \(h_*q_1V_1\), and the [paired-filter input](paired_control.md#scope) is \(h_*q_{12}V_1V_2\).
Here \(V_a=T_{5a}+T_{4a}-T_{2a}-T_a-1\), and the rectifiers are those returned by the frozen calls `signed_filters.construct([1])` and `signed_filters.construct([1, 2])`.
No new unit descent, seed choice, filter label or conductor is introduced.

For each base \(h_{\rm base}\), test all integer square multiples
\[
 h=h_{\rm base}v^2\bmod B_{40},\qquad
 v\in\mathbb Z[t]/B_{40},\qquad 0<E\le6.
\]
The energy is \(E=3K+2L\).
Nonunits and multipliers vanishing at some nodes are included.
The new joint moment target is \(E=6,K=2,L=0\), corresponding to \(x=0\).
The full solid-ball traversal also counts energies one through five.
Other energies and other sign-compatible square classes remain outside the claim.

<a id="matrix-certificates"></a>
## Source reconstruction and exact integral matrices

The source reconstructs the original base through `signed_filters.balanced_base()` and the two rectified inputs through their frozen constructors.
No generated JSON is read.
For each input it verifies the integral inverse of the rectifier, its absolute resultant one, the positive multiplier's exact norm, the input's exact absolute resultant, and all 40 original signs.
Positivity and the cut signs are certified with 512-bit Arb balls, rejecting any interval containing zero.
The same exact Sturm check places \(-3/2\) between nodes 31 and 32.

Use the retained [integer matrix representation](low_energy_shell.md#scope) with Jacobi matrix \(J\) and monic second-kind Chebyshev coordinates.
For each base,
\[
 H=h_{\rm base}(J),\qquad G=(2J+3I)H,\qquad
 K=v^THv,\quad L=v^TJHv,\quad E=v^TGv.
\]
The source checks symmetry, the constant-coordinate moments, every positive fraction-free leading pivot of \(G\), and the determinant product.
In all three runs \(\det(2J+3I)=-638639601137\).

| Base name | Absolute input resultant | \(\det H\) | \(\det G\) |
| --- | ---: | ---: | ---: |
| `original` | 32 | \(-32\) | 20436467236384 |
| `single` | 5216 | \(-5216\) | 3331144159530592 |
| `paired` | 850208 | \(-850208\) | 542976498003486496 |

Exact Gram LLL returns an integer matrix \(A\) and reduced Gram matrix \(G'\).
Every run checks \(\lvert\det A\rvert=1\), \(G'=AGA^T\), positive pivots of \(G'\), and equality of determinants.
The actual determinant of \(A\) is one in each run.
The shared rational checker verifies size bounds \(\lvert\mu_{ji}\rvert\le51/100\) and Lovász inequalities with \(\delta=3/4\).
These identities establish a bijection of the original and reduced integer coordinates.

<a id="enumeration"></a>
## Parameterized exact traversal and stopping boundaries

The new `half_ball` function takes the energy bound, node bound and time bound as explicit parameters.
It uses the [fraction-free completed-square recurrence](low_energy_shell.md#exact-traversal), exact integer square roots and divisions checked for zero remainder.
It does not mutate constants or functions in any frozen module.
The highest nonzero reduced coordinate is positive, so each count represents one nonzero pair \(v,-v\).
Every returned vector receives direct integer evaluations of \(E,K,L\), including an independent check \(3K+2L=E\).

Each base has fixed bounds of 20,000,000 recursive tree nodes or 120 seconds, whichever is encountered first.
The timer starts after source reconstruction and LLL and includes traversal and leaf processing.
The bounds are checked before entering each recursive call.
A stopped run records `complete: false`, the stopping reason, completed-prefix counts and the first unentered call's index, scaled budget and higher coordinates.
This boundary record does not assert that the unvisited branches are empty.
Each of the present three runs exhausted every branch before either bound.

<a id="complete-result"></a>
## Completed counts and the endpoint obstruction

The exact observed counts are:

| Base | Completion | Nodes | Traversal and leaf time | Nonzero classes at \(E=1,2,3,4,5\) | Classes at \(E=6\) | Joint \(K=2,L=0\) hits |
| --- | --- | ---: | ---: | --- | ---: | ---: |
| `original` | Complete | 9156526 | 20.05 s | All zero | 6 | 0 |
| `single` | Complete | 2061933 | 4.47 s | All zero | 1 | 1 |
| `paired` | Complete | 1470714 | 3.19 s | All zero | 0 | 0 |

All three outputs have `complete: true`, `stop_reason: complete` and no unentered boundary.
The exact joint moment distribution of the original base's six classes is:

| \(E\) | \(K\) | \(L\) | Classes modulo simultaneous sign |
| ---: | ---: | ---: | ---: |
| 6 | 0 | 3 | 2 |
| 6 | 8 | \(-9\) | 1 |
| 6 | 12 | \(-15\) | 1 |
| 6 | 16 | \(-21\) | 2 |

The single-filter class has exactly one nonzero class in the entire ball, with \(E=6,K=2,L=0\).
Its recovered multiplier satisfies
\[
 \operatorname{Res}(B_{40},v)=1,\qquad
 \lvert\operatorname{Res}(B_{40},Q)\rvert=5216.
\]
It is an integer unit and preserves all original strict signs.
The resulting reciprocal monic polynomial has degree 82 but fails the strict endpoint:
\[
                            P(-1)=-104<0.
\]
Thus there are no strict-endpoint survivors in any of the three tested families at the new \(x=0\) target.
The original and single Gram lattices have minimum nonzero energy six, while the paired Gram lattice has no nonzero energy at most six.
These are statements about the specified integer-square families and the completed finite energy range.
They do not exclude other square classes, other filter labels, or the negative-\(x\) profiles at energies 17 and 34.
They supply no arbitrary-\(\varepsilon\) positive-probability conclusion.

<a id="single-candidate"></a>
## The unique failed-endpoint polynomial

For the single-filter moment hit, let \(P(z)=\sum_{i=0}^{82}a_i z^i\).
Its coefficients satisfy \(a_{82-i}=a_i\), and the first half including the central coefficient is
\[
\begin{aligned}
 (a_0,\ldots,a_{41})={}&
 (1,1,4,4,4,7,5,9,8,10,10,11,11,13,11,15,\\
 &12,16,15,17,17,20,18,24,19,25,22,25,24,26,24,28,\\
 &24,30,26,30,29,32,30,35,30,36).
\end{aligned}
\]
The full native record also regenerates the exact original and reduced multiplier coordinates, the ordinary polynomial \(v\), the cyclic word of \(h\), and the trace polynomial \(Q\).
The endpoint is checked both through the lift coefficients and through \((-1)^{41}Q(-2)\).
The moment and resultant checks occur before the endpoint test.

The shared candidate function receives the actual base norm explicitly, using 32, 5216 or 850208 as appropriate.
For a moment hit it rejects a zero multiplier resultant, constructs \(h,C,Q,P\), checks the target moments and exact norm, and then tests \(P(-1)>0\).
Only a strict-endpoint survivor would invoke the full Mahler enclosure over all complex roots with their multiplicities.
The unique candidate fails the endpoint, so no complete-root or Mahler calculation was invoked in any run.
Its Mahler measure is not reported by this traversal; the [separate fixed-polynomial diagnostic](candidate_diagnostic.md#full-measure) owns that later calculation.

<a id="reproduction"></a>
## Reproduction and retained data

Run the three invocations separately from the repository root with Python, python-flint, SymPy and NumPy:

~~~text
python -B mathematics/computations/programs/Yin_J_G0154/energy_six.py --base original
python -B mathematics/computations/programs/Yin_J_G0154/energy_six.py --base single
python -B mathematics/computations/programs/Yin_J_G0154/energy_six.py --base paired
~~~

The actual sequential runs used the existing Python 3.14.7 and python-flint 0.9.0 environment.
The output names are `energy_six_original_81.json`, `energy_six_single_81.json` and `energy_six_paired_81.json` under `mathematics/computations/outputs/Yin_J_G0154/`.
Each output retains its construction, exact base polynomial, norm, matrix determinants, original positive pivots, integral change matrix, reduced Gram matrix and pivots, rational LLL certificate, actual scope and limits, completion flag, every returned vector and moment, and every target inspection.
The single output also retains the unique candidate's full polynomial data and failed endpoint.
No source or output fingerprints are used.
Different valid reduced bases may change traversal order, node counts and timings; exact integral equivalence and exhausted branching determine the coverage.
The earlier smaller-bound and interrupted calculations keep their historical scopes.
The [independent energy-six finding](../../../audits/reviews/Yin_R_G1107_v17.md#energy-six-review) checks all three complete traversals and the actual failed endpoint at this scope.
