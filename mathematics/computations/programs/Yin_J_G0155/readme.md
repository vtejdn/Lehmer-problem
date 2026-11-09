---
author: Yin
---
# One affine integer candidate test on the conductor-81 three-node cut

<a id="question-scope"></a>
## Question and scope

This group executes the unique fixed candidate contract in [L462 v9](../../../ledger/Yin_L_G0462_v9.md#candidate-test).
Use \(p=81\), \(n=40\), terminal cut \(k=3\), profile \(x=0\), and the complete integer coordinate chart
\[
 h=\sum_{i=0}^{39}a_iE_i,\qquad
 E_0=1,\ E_1=t,\ E_{i+1}=tE_i-E_{i-1}.
\]
The moments are fixed by \(a_0=2,a_1=0\), every original node has the prescribed strict sign, and the strict endpoint condition is
\[
                  U=\sum_{i=0}^{39}(-1)^ia_i\ge-1.
\]
The [proved full coefficient box](../../../ledger/Yin_L_G0462_v9.md#complete-coefficient-box) is
\[
 |a_i|\le B_i=\left\lceil1550(i+1)/3\right\rceil-1
                    \quad(2\le i\le39).
\]
This chart covers every integer input in that chamber, with no fixed norm, square class, third moment or other residue constraint.
The one floating MILP proposal minimizes \(\sum_i|a_i|\); it supplies an incumbent for separate exact verification.
The positive numerical sign margin is a proposal device and need not contain every true strict solution.

<a id="files"></a>
## Files

| File | Role |
| --- | --- |
| [affine_milp.py](affine_milp.py) | Fixed model construction, one solver call in `propose`, and solver-free exact verification in `verify`. |
| [inputs/incumbent.json](inputs/incumbent.json) | The complete fixed vector of 40 integer coefficients returned by the one proposal. |
| `mathematics/computations/outputs/Yin_J_G0155/model_81_k3.json` | Replaceable local model, including all 121 rows, 80 columns, bounds, objective, dyadic node coefficients and certified approximation bounds. |
| `mathematics/computations/outputs/Yin_J_G0155/proposal_81_k3.json` | Replaceable local solver status, raw incumbent, limits, rounding and exact candidate checks. |
| `mathematics/computations/outputs/Yin_J_G0155/incumbent_verification_81_k3.json` | Replaceable solver-free reconstruction and complete-root verification of the tracked incumbent. |

Generated outputs are replaceable local data.
The tracked integer input suffices for candidate reproduction in a checkout that has none of those outputs.

<a id="model"></a>
## Numerical proposal model and actual solver return

There are 40 integer coefficient variables and 40 continuous absolute-value auxiliaries \(s_i\).
The model contains every coefficient bound, fixes \(a_0=2,a_1=0\), imposes \(s_i\ge a_i\) and \(s_i\ge-a_i\), includes all 40 sign rows, and includes \(U\ge-1\).
The auxiliaries have \(0\le s_i\le B_i\), with bounds two and zero for the two fixed coordinates; these upper bounds leave the coefficient domain unchanged.
The objective is \(\sum_i s_i\).
There are 121 original rows and 80 original columns.

The basis values at the 40 nodes are enclosed with 512-bit Arb balls and then converted to binary64 midpoint proposals \(m_{ji}\).
Each midpoint is also retained as its exact dyadic numerator and denominator.
The program verifies
\[
               |E_i(b_j)-m_{ji}|<2^{-46}
\]
for every entry.
Since \(E_0=1\) is exact and \(a_1=0\), the full-box error in each node row is bounded by
\[
                 \frac{422091}{70368744177664}.
\]
The proposal requires \(\sigma_j\sum_i m_{ji}a_i\ge10^{-6}\), with 37 positive and three negative rows.
This margin is not used as an exact feasibility or exclusion certificate.

The single SciPy `milp` call uses HiGHS with a 60-second time limit, a 100000-node limit, presolve enabled, one thread, random seed zero, and zero requested relative and absolute MIP gaps.
The requested MIP feasibility tolerance is \(10^{-8}\), and requested primal and dual LP feasibility tolerances are \(10^{-9}\).
SciPy forwards the backend-specific options to HiGHS and emits a warning identifying those forwarded keys; the actual warning is retained in the proposal data.
HiGHS also reported ignoring 18 extremely small matrix entries, between approximately \(1.68\cdot10^{-154}\) and \(7.03\cdot10^{-143}\), below its \(10^{-9}\) small-matrix threshold.
The returned integer vector is verified independently of those numerical simplifications.

The actual solver finished in about 3.65 seconds after six branch nodes and reported status 0, `Optimal`, with objective and dual bound approximately \(3.9999999999999902\) and reported gap zero.
Only one floating solver call was made.
The coefficient coordinates were already exact integer-valued floats, so their maximum rounding change was zero, below the declared \(10^{-6}\) recovery tolerance.
Neither floating optimality nor its dual bound is adopted as a mathematical optimality proof.

<a id="fixed-incumbent"></a>
## Exact incumbent and chamber verification

The returned vector has exactly three nonzero coordinates:
\[
                         a_0=2,\qquad a_2=1,\qquad a_7=1.
\]
Thus its exact coefficient objective is four and
\[
 h=2E_0+E_2+E_7
   =t^7-6t^5+10t^3+t^2-4t+1.
\]
Every coefficient satisfies the full proved box, and the two fixed coordinates are correct.
Writing
\[
 B=E_{40}+E_{39},\quad D=E_{39}+E_{38},\quad
 C=Dh\bmod B,\quad Q=tB+C,
\]
the verifier recovers \(K=C_{39}=2\) and \(L=C_{38}-B_{39}K=0\), independently of the coordinate readings \(a_0,a_1\).
The third moment is an output, not an imposed equation:
\[
                              N=a_0+a_2=3.
\]
All 40 strict signs are certified at the first 256-bit Arb attempt: 37 positive and the last three negative, with no unresolved or wrong sign.
The exact polynomial gcd \(\gcd(B,h)\) is one.

The endpoint and actual signed resultants are
\[
 U=2,\qquad P(-1)=-Q(-2)=2+U=4>0,
\]
\[
       \operatorname{Res}(B,h)=\operatorname{Res}(B,Q)
                               =-23915931223391.
\]
No norm ceiling or specified resultant was imposed before or after the proposal.
The lift \(P(z)=z^{41}Q(z+z^{-1})\) is verified to be a monic reciprocal integer polynomial of degree 82 with constant coefficient one.
The candidate therefore supplies an actual integer point in the full prescribed strict chamber.

<a id="factorization-measure"></a>
## Exact factorization and complete Mahler measure

Exact integer factorization returns
\[
                         P(z)=(z^2+1)R(z),
\]
with both exponents one and \(R\) an irreducible noncyclotomic polynomial of degree 80 in FLINT's exact factorization.
The exact factors are multiplied back to \(P\).
For a compact complete specification, write \(R(z)=\sum_{i=0}^{80}r_i z^i\).
Then \(r_{80-i}=r_i\),
\[
                 (r_0,\ldots,r_7)=(1,1,3,3,2,2,3,3),
\]
and, for \(8\le i\le40\),
\[
 r_i=
 \begin{cases}
 2,&i\equiv0\pmod4,\\
 4,&i\equiv2\pmod4,\\
 3,&i\text{ odd}.
 \end{cases}
\]
All factor coefficients are also regenerated in native output.
The cyclotomic factor \(z^2+1=\Phi_4(z)\) has exact measure one.

The root computation includes all 82 roots with multiplicity.
At 256 bits, two roots of \(R\) have modulus certified below one, two above one, and 76 modulus balls meet one.
The two roots of \(\Phi_4\) also have modulus balls meeting one and use their exact cyclotomic contribution.
For every noncyclotomic root whose modulus ball meets one, the union of that ball with the point one encloses \(\max(1,|\alpha|)\).
Those 76 roots are neither omitted nor asserted to be exact unit-circle roots.
The full product has reported radius at most \(1.40\cdot10^{-74}\), yielding
\[
\boxed{
 2.62059765161094301246636259541059
 <M(P)=M(R)<
 2.62059765161094301246636259541060.
}
\]
The value is strictly greater than one.
This is the complete Mahler measure, not a maximum-root proxy.
The candidate is a valid arithmetic supply but does not have measure close to one.

<a id="reproduction"></a>
## Reproduction

Candidate verification does not run a MILP and does not read ignored output.
From the repository root, use the tracked input:

~~~text
python -B mathematics/computations/programs/Yin_J_G0155/affine_milp.py verify --input mathematics/computations/programs/Yin_J_G0155/inputs/incumbent.json
~~~

This verification entry was run successfully on the saved input.
It regenerates the exact coefficient checks, all signs and endpoint, signed resultants, full lift and factorization, all root balls and complete measure.
The proposal and the fixed-input verification both used Python 3.14.7, SciPy 1.18.1, NumPy 2.5.4 and python-flint 0.9.0; the solver identified itself as HiGHS 1.12.0.
SciPy is imported by the shared program, but the `verify` branch makes no solver call.

The actual original one-proposal command was:

~~~text
python -B mathematics/computations/programs/Yin_J_G0155/affine_milp.py propose
~~~

That command is not required to review or reproduce the fixed candidate.
The model's limits and arithmetic are in the native source and generated model data.
Candidate sign checks may refine from 256 through 4096 bits if necessary, and whole-root checks refine until the declared \(10^{-25}\) radius criterion and exact-one or strict-above-one distinction are resolved.
This candidate required no refinement beyond 256 bits.

<a id="results-limits"></a>
## Results and limits

The single bounded proposal produced one fully checked strict-endpoint integer input, with third moment three and full measure approximately 2.620597651610943.
The observation establishes that arithmetic supply exists at this concrete value in the new coefficient chart and cut.
Both the cut and the domain differ from the earlier selected square-family controls, so the successful return does not isolate which earlier restriction caused their failures.
That original two-moment experiment tried no additional third-moment model, seed, objective, conductor or candidate.
No exact global coefficient minimum, chamber exclusion or arbitrary-\(\varepsilon\) positive-probability statement is claimed.
The [independent fixed-incumbent finding](../../../audits/reviews/Yin_R_G1107_v20.md#affine-incumbent-review) reproduces the solver-free candidate verification and checks the saved model at its actual evidence scope.
Its [separate theoretical finding](../../../audits/reviews/Yin_R_G1107_v20.md#affine-chamber-review) checks the complete coefficient chart and box.

The [separate N=6 conditional test](third_moment.md#result) fixes \(a_2=4\) in the same complete coefficient chamber.
Its one bounded solver call reached 60 seconds without an incumbent, so no N=6 candidate received a complete-Mahler calculation.
The original N=3 incumbent was used only as a solver-free negative control for the additional moment check.
This bounded failure supplies no exact chamber exclusion.
