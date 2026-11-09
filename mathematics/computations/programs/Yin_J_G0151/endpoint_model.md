---
author: Yin
---

# The missing endpoint value in the residual occupancy models

<a id="endpoint-value"></a>
## Exact original condition and relaxed test

The original [negative-one N=7 input](../../../claims/Yin_C_G0882_v6.md#statement) satisfies \(Q(-2)/B(-2)=-U=-1\).
This is an exact value condition, stronger than the endpoint sign alone.
For a real root configuration with two exceptional roots equal to \(s\in(-2,2)\), the [root-product identity](../../../ledger/Yin_L_G0464_v15.md#endpoint-value) gives
\[
 \log U=2\log(2+s)-\log(2+c)
             -\int_{-2}^2\frac{w(t)}{2+t}\,dt,
\]
where \(c\) is the unpaired pole and \(w\) is the indicator of the disjoint terminal pairing intervals.
Thus \(U=1\) requires this logarithmic expression to vanish.
The seven polynomial moment equations do not impose this additional logarithmic equation.

In fact all five particular step models retained in [C882v8](../../../claims/Yin_C_G0882_v8.md#diagonal-certificate) fail this endpoint-value extension.
In the first, second and fourth native rows the first cell is a free coordinate strictly greater than \(1/10\); in the third and fifth rows it is fixed at one.
Thus each has positive constant occupation immediately to the right of \(-2\), so its integral against \(1/(t+2)\) diverges.
The finite right side \(2\log(2+s)-\log(2+c)\) cannot equal that integral.
This rejects these particular step witnesses for the enlarged model, without rejecting other measurable occupations or any original integer branch.

The fixed test uses only \((O,V,W)=(10,18,27)\), \(s=-15/16\), the inherited midpoint \(c=-3219325/2000000\), and 256 equal coarse cells on \([-2,2]\).
On each cell the occupation is constant in \([0,1]\).
The first cell is fixed at zero so that its logarithmic integral is finite.
For cell \(i\ge1\), with endpoints \(-2+i/64\) and \(-2+(i+1)/64\), its logarithmic coefficient is exactly \(\log((i+1)/i)\).
The model retains all seven polynomial identities from [C882v8](../../../claims/Yin_C_G0882_v8.md#diagonal-statement) and adds
\[
 \sum_{i=1}^{255}\omega_i\log\frac{i+1}{i}
      =2\log(17/16)-\log(2+c).
\]
Fixing the first coarse cell at zero and making the others constant are extra restrictions on this proposal model.
They are not consequences of an actual root-to-pole configuration.

<a id="finite-result"></a>
## One bounded proposal and its actual limit

[endpoint_model.py](endpoint_model.py) made one SciPy HiGHS LP call, with a 15-second limit, for this one fixed model.
It returned numerical status 2, reporting infeasibility, and supplied no occupation vector.
The proposal remains at the replaceable local output mathematics/computations/outputs/Yin_J_G0151/endpoint_model_proposal.json.
There was no second location, different cell count, changed first-cell condition or second LP call.
The program's potential fixed-pattern Arb verification path was not reached and has no retained positive input.
No exact infeasibility certificate was obtained.

This failure neither excludes arbitrary measurable occupations nor proves impossibility for actual roots or original integer polynomials.
The numerical failure adds no exact exclusion to the preceding direct rejection of the old step witnesses.
The [separate true-interval experiment](terminal_intervals.py) addresses a different parameterization; neither experiment supplies the other's missing condition.

For comparison, a direct weighted Cauchy-Schwarz lower bound also fails to certify a contradiction at this location.
Writing \(m_j=\int t^jw(t)\,dt=(2s^{j+1}-c^{j+1}-\mathcal D(t^{j+1}))/(j+1)\), let \(A_{ij}=m_{i+j+1}+2m_{i+j}\) and \(v=(m_0,m_1,m_2)^t\).
The inequality \(\int w/(t+2)\ge v^tA^{-1}v\) follows by completing the nonnegative integral of \(w(t)(1-(t+2)q(t))^2/(t+2)\) for a quadratic \(q\).
At this fixed rational \(s,c\), exact rational solution of the \(3\times3\) system gives a lower bound approximately 0.8840963411, below the required logarithmic value approximately 1.0619927731.
These decimals report a failed sufficient test, not a certified endpoint-feasible model or a lower bound above the target.

<a id="reproduction"></a>
## Reproduction

From the repository root:

~~~text
python -B mathematics/computations/programs/Yin_J_G0151/endpoint_model.py explore
~~~

The exploratory mode requires SciPy and NumPy, and the module imports python-flint for its optional unexercised verification path.
The actual environment was Python 3.14.7, SciPy 1.18.1, NumPy 2.5.4 and python-flint 0.9.0.
The exact endpoint identity is independent of the floating-point proposal.
