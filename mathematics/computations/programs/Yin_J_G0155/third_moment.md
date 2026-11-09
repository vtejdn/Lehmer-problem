---
author: Yin
---

# The third-moment-six test in the complete conductor-81 coefficient chamber

<a id="scope"></a>
## Question and bounded contract

Keep the full \(p=81,k=3,x=0\) coefficient chamber of [L462v9](../../../ledger/Yin_L_G0462_v9.md#fixed-chamber) and the original [two-moment experiment](readme.md#fixed-incumbent).
This separate test adds precisely \(N=\sum_j b_j^2r_j=6\).
The exact moment coordinates give \(N=a_0+a_2\), so with \(a_0=2,a_1=0\) the added condition is \(a_2=4\).
All other coefficient bounds, forty node signs, strict endpoint and the absolute-coefficient objective are unchanged.
The complete covering box remains a consequence of the original two moments and signs, not an extra height truncation.

The test makes one MILP call with the original 60-second solver limit, 100000-node limit and at most one returned incumbent.
The numerical sign margin can omit true strict solutions, so neither a missing incumbent nor a numerical infeasibility status excludes the original integer chamber.
No other conductor, cut, profile, coefficient bound or objective is included.
This conditional test does not presume that its integer domain is nonempty or that matching the third moment makes the full measure small.

<a id="program"></a>
## Program and validation

[third_moment.py](third_moment.py) imports the unchanged [affine_milp.py](affine_milp.py) helpers.
Its model changes only the lower and upper bounds of coefficient \(a_2\) to four and checks that all other variable bounds remain identical.
It saves its model and numerical proposal to distinct replaceable files in the same J output home.
The original two-moment native program, retained incumbent and outputs are not overwritten.

For an integer proposal, the first three Laurent coefficients of \(C/B\) are recomputed exactly:
\[
 K=C_{39},\qquad
 L=C_{38}-B_{39}K,\qquad
 N=C_{37}-B_{39}L-B_{38}K.
\]
They must equal both the coefficient identities \((a_0,a_1,a_0+a_2)\) and the target \((2,0,6)\).
The preliminary check also verifies the complete coefficient box, \(\gcd(B,h)=1\), every strict grid sign using outward Arb evaluation, and \(P(-1)=-Q(-2)=2+U>0\).
Only a proposal passing these checks proceeds to the unchanged complete-resultant, exact factorization and all-root Mahler verifier.
All original root multiplicities and all factors remain in that product.

<a id="reproduction"></a>
## Reproduction and result boundary

From the repository root, using the dependencies specified in the [J entrance](readme.md#reproduction):

~~~text
python -B mathematics/computations/programs/Yin_J_G0155/third_moment.py propose
~~~

The generated model and proposal are replaceable local outputs in mathematics/computations/outputs/Yin_J_G0155, named model_81_k3_N6.json and proposal_81_k3_N6.json.

<a id="result"></a>
## Actual bounded result

The single proposal call reached its 60-second solver-time limit without an incumbent.
SciPy returned status 1 with the message that the time limit was reached and the primal status was None.
Its returned solution, objective, node-count, gap and dual-bound fields were all null.
Consequently no vector reached the exact N=6 screening or the complete-Mahler calculation.

The observed HiGHS stdout separately reported 54507 processed nodes, 798427 LP iterations, no primal bound and a final numerical dual bound of 26.
Those stdout observations are not returned SciPy fields, an exact L1 lower bound or a complete search.
The backend identified itself as HiGHS 1.12.0 and reported ignoring 18 matrix entries of magnitude at most \(10^{-9}\).
SciPy warned that the six nonstandard options were forwarded to HiGHS verbatim, as in the original experiment.
The actual call used Python 3.14.7, SciPy 1.18.1, NumPy 2.5.4 and python-flint 0.9.0.
No second solver call, parameter change or larger search was performed.

A separate solver-free negative control supplied the [original retained incumbent](inputs/incumbent.json) to the new validation function.
It recomputed \((K,L,N,U,P(-1))=(2,0,3,2,4)\), passed the coefficient box, endpoint, nonzero component and all strict node signs, and failed precisely the added moment target.
The returned complete-candidate field was null, so the rejected N=3 input did not invoke the Mahler verifier.
The successful N=6 validation branch remains unexercised because no such candidate was supplied.

The following Python snippet reproduces that negative control from the repository root:

~~~python
import json
import sys
sys.path.insert(0, "mathematics/computations/programs/Yin_J_G0155")
import third_moment as test
with open("mathematics/computations/programs/Yin_J_G0155/inputs/incumbent.json") as f:
    fixed = json.load(f)
result = test.validate(fixed["coefficients_E_basis"])
assert not result["precheck"]["valid"]
assert result["complete_candidate"] is None
assert not result["precheck"]["checks"]["moment_target"]
assert all(value for key, value in result["precheck"]["checks"].items()
           if key != "moment_target")
~~~

The test supplies neither a strict N=6 integer point nor an exclusion of that full chamber.
No conclusion about arbitrarily small positive Mahler measure or its probability follows from this time-limited failure.
The [independent finite review](../../../audits/reviews/Yin_R_G1107_v22.md#third-moment-review) checks the exact model restriction, saved-field comparison and executed negative control, retaining the stated historical-stdout and unexecuted-branch limits.
