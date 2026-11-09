---
author: Yin
---

# Balanced-base controls before the Galois-filter test

<a id="scope"></a>
## Two fixed finite controls

Keep the [baseline definition and filter law](readme.md#scope), including the deterministic \(h_{0,p}\), \(V_a\), all coprime indices modulo sign, and unordered double-filter pairs with repetitions.
This separate calculation tests a specified low-energy base at \(p=27,k=3\) and a bounded deterministic unit descent at \(p=81,k=9\).
It changes no baseline parameter or result in the preceding four-conductor computation.
[balanced_control.py](balanced_control.py) owns this additional calculation and imports the exact cyclic operations from the fixed baseline program.

Write \(U_a=2+T_a\).
Only indices coprime to \(p\) are used for these units.
For \(b\equiv a/2\pmod p\), one has \(U_a=T_b^2\) in the cyclic quotient.
The baseline twice-inverse identity produces an integral inverse of \(T_b\), and squaring gives an integral inverse of \(U_a\).
For odd \(u\) coprime to \(p/d\), put \(J_u(T_d)=T_{du}/T_d\).
The same identity gives both this integral quotient and its inverse; squaring gives a totally positive unit.
Every constructed unit and inverse is checked for an exact product equal to one.
At \(p=81\), all 37 forward units and all 37 inverses also have their absolute integer resultant with \(B\) checked directly to be one.

<a id="control-27"></a>
## The specified conductor-27 base

Use
\[
                     h_*=h_{0,27}U_2^2U_5U_8U_{11}.
\]
Exact reconstruction gives \((K,L)=(2,0)\), absolute resultant \(32\), and \(P(-1)=1\) for the \(x=0\) lift.
Its normalized symmetric cyclic word is determined by coefficients \(w_0,\ldots,w_{13}\):
\[
             (1,2,-1,2,0,1,0,1,1,1,0,1,1,0),
\]
with \(w_{27-j}=w_j\).
The complete degree-28 root product is enclosed by
\[
             3.34992786033438595897<M(P)<3.34992786033438595898.
\]
This newly recomputed enclosure is contained in the previously specified interval \([3.349927,3.349928)\).

The nine single filters and 45 unordered double filters yield no joint hit at any of the five targets \((x^2+2,-4x)\).
The single labels \(a=2\) and \(a=7\) give the only target first moments, respectively \((K,L)=(2,9)\) and \((2,10)\).
Neither satisfies the required \(L=0\).
No double filter has \(K\in\{2,3,6\}\).

<a id="descent-81"></a>
## A bounded deterministic unit descent at conductor 81

The exact odd-grid recurrence gives 31 poles above \(c=-3/2\), placing this rational strictly in the gap for \(k=9\).
Consequently every strictly sign-compatible input has positive integral energy
\[
 E=2L+3K=\sum_j(2b_j+3)\nu_jh(b_j)>0.
\]
The five prescribed moment profiles have respective energies \(34,17,6,1,2\) in the order \(x=-2,-1,0,1,2\).

Start with exactly \(h_{0,81}\).
Phase one uses all 27 units \(U_a\), \(1\le a\le40\), \(3\nmid a\), in ascending \(a\).
At each step test every forward and inverse multiplication, choose the least resulting energy strictly below the current one, and break ties by the listed unit order with the forward direction first.
Allow at most 100 strictly descending steps.
Phase two retains that list, appends
\[
 J_u(T_3)^2,\quad u=5,7,11,13,17,19,23,25,
 \qquad J_5(T_9)^2,\quad J_7(T_9)^2,
\]
in the displayed order, and applies the same rule for at most 100 further steps.
No random restart or additional seed is used.

The actual descent is:

| Phase | Step | Multiplier | Resulting \(E\) | Resulting \((K,L)\) |
| ---: | ---: | --- | ---: | --- |
| 1 | 0 | Initial base | 974939084158622447 | \((316789078141730201,12285924866715922)\) |
| 1 | 1 | \(U_2\) | 1466401551171931 | \((476481031405291,18479228478029)\) |
| 1 | 2 | \(U_2\) | 2205627931512 | \((716678870964,27795659310)\) |
| 1 | 3 | \(U_2\) | 3318251651 | \((1078184005,41849818)\) |
| 1 | 4 | \(U_2\) | 5020500 | \((1630492,64512)\) |
| 1 | 5 | \(U_2\) | 8739 | \((2791,183)\) |
| 1 | 6 | \(U_2\) | 189 | \((1,93)\) |
| 1 | 7 | \(U_1^{-1}\) | 121 | \((-119,239)\) |
| 1 | 8 | \(U_{31}^{-1}\) | 94 | \((-88,179)\) |
| 2 | 1 | \((J_5(T_3)^2)^{-1}\) | 12 | \((-2,9)\) |
| 2 | 2 | \(U_{31}\) | 11 | \((-3,10)\) |

Phase one stops after eight moves because the least energy among all 54 one-step neighbors is 120, exceeding the current 94.
Phase two stops after two moves because the least energy among all 74 neighbors is 12, exceeding the current 11.
Neither phase reaches its step cap.
The complete final-neighbor energy lists, every chosen move, and the exact original and final words are retained in the reproducible output.
These are one-step stationary points for the specified lists, not global minima over the unit group or proofs about longer products.

The final word is exactly
\[
             h_{\rm final}=h_{0,81}U_2^6U_1^{-1}(J_5(T_3)^2)^{-1}.
\]
Its absolute resultant remains \(32\), checked directly after reconstruction.
Its moments are \((-3,10)\), so it does not itself match one of the five profiles.
Also \(U=\sum_j r_j/(2+b_j)=w_0-w_1=-30\).
For each lift coefficient \(a=2x\), direct evaluation of the reconstructed \(Q\) verifies
\[
 P(-1)=2+2x+U=-28+2x,
\]
giving \(-32,-30,-28,-26,-24\) for the five \(x\).
Thus the final unfiltered base fails every corresponding strict endpoint as well.
No complete-measure value is asserted for these nonmatching conductor-81 lifts.

<a id="filtered-results"></a>
## Full finite support after balancing

The final conductor-81 base is tested against every one- and two-filter label.
No joint moment hit occurs.
The only target first moment is the double label \((a,b)=(28,31)\), which gives \((K,L)=(2,157)\), again failing \(L=0\).
The minimum energy after a single filter is 42, attained at \((K,L)=(-28,63)\); after two filters it is 67, attained at \((-9,47)\).
Both exceed the largest target energy 34, so the complete filtered energy lists already exclude all five targets at this final base.
This is a finite statement about the specified base and filters, not a lower bound for other unit balances.

| Base | Single labels | Unordered double labels | Ordered double labels | Single joint hits | Double joint hits |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(p=27,\ h_*\) | 9 | 45 | 81 | 0 | 0 |
| \(p=81,\ h_{\rm final}\) | 27 | 378 | 729 | 0 | 0 |

Within each single- or double-filter traversal the joint pairs are all distinct.
For an ordered double draw, each off-diagonal unordered pair has multiplicity two and each diagonal pair has multiplicity one.
Both joint histograms and the complete first-moment hit labels retain these multiplicities.
The absence of joint hits is therefore independent of the choice of probability weights on these finite label sets.
It does not assert that other unit balances, longer unit combinations, different filters or larger conductors cannot work.

<a id="complete-measure-check"></a>
## Complete-measure verification and reproduction

The conductor-27 original is reconstructed by \(C=Dh_*\bmod B\), \(Q=tB+C\), and \(P=z^{n+1}Q(z+z^{-1})\).
Its first two remainder coefficients, resultant, reciprocity, monicity and endpoint are checked exactly.
FLINT complex root balls at 256-bit precision enclose every root, and the product of \(\max(1,|\lambda|)\) counts every returned multiplicity.
The total root count is checked to be 28 and the product radius is less than \(10^{-25}\).
This is the complete Mahler measure, not the largest root radius.
For a ball straddling modulus one, the interval union with one encloses the clipped contribution.
All subsequent filtered inputs failed the exact two-moment test, so no filtered endpoint or root-product calculation was called.

Run with the same Python, python-flint, SymPy and NumPy environment as the [baseline](readme.md#reproduction):

~~~text
python -B mathematics/computations/programs/Yin_J_G0154/balanced_control.py
~~~

The command reconstructs both bases without reading old generated data and writes
`mathematics/computations/outputs/Yin_J_G0154/balanced_control_27.json` and
`mathematics/computations/outputs/Yin_J_G0154/balanced_control_81.json`.
These local outputs contain the exact words and coefficients, all descent data and final neighbor costs, complete finite joint supports, endpoint evaluations and the certified original root product.
The integer traversal and unit descent use no numerical rounding or probabilistic search.
The current checks are author-level computation checks; this material does not claim an independent project review.
