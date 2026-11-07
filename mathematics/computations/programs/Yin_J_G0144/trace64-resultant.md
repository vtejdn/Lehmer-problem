---
author: Yin
---

# An integer resultant forces movement of the real trace roots

Consider the [degree-64 pilot](../../../ledger/Yin_L_G0462_v1.md#complex-trace-cells) with monic integer trace polynomial \(Q\) of degree 32.
Write \(A=Q_9\) for its degree-nine control and \(t_1<\cdots<t_{30}\) for the real zeros of \(A\Psi_{47}\), with \(t_0=-2\) and \(t_{31}=2\).
Suppose \(Q\) has thirty ordered real roots \(x_1,\ldots,x_{30}\) and a conjugate pair \(w,\bar w\), where \(w\) belongs to the closed disk of center \((-177624+8300i)/100000\) and radius \(1/10000\).
The following two exclusions hold for arbitrary integer coefficient heights.

1. Some \(x_i\) lies outside the closed interval \([(3t_i+t_{i-1})/4,(3t_i+t_{i+1})/4]\).
2. Choose any interior separator \(s_i\) with \(|s_i-(t_i+t_{i+1})/2|\le 1/1000\) for \(1\le i<30\), and use \(s_0=-2,s_{30}=2\).
   If \(s_{i-1}\le x_i\le s_i\) throughout, then \(|x_i-t_i|>1/50\) for at least one of the seven indices with \(A(t_i)=0\).

In the second statement all 23 real roots indexed by the cyclotomic factor may occupy their entire separator intervals.
The widths of the seven other intervals permit only eleven directed moves.
The root \(x_7\) can move to the right, and \(x_{11},x_{14},x_{17},x_{21},x_{25}\) can each move in either direction.
The thirtieth root always stays within \(1/50\) of its seed.
At least one of these eleven directed moves is necessary.

Each alternative gives a rational linear sign test on the coefficients of \(Q\).
Write \([\ell_i,u_i]\) for the millionth bracket enclosing \(t_i\).
A left move places \(x_i\) strictly below \(u_i-1/50\), and a right move places it strictly above \(\ell_i+1/50\).
At the selected rational test point inside the separator interval, require the sign of \(Q\) at the right endpoint for a left move and at the left endpoint for a right move, using the pilot's fixed nonzero alternating endpoint signs.
The real root in that interval is simple and unique, and the test points are nonintegral rationals, so \(Q\) has no zero there.
Thus a coefficient search can impose each branch as a single linear inequality.

## Certificate

The nonreal pair of \(A\) has its upper member in the disk of center \((-177624+8576i)/100000\) and radius \(1/100000\), as verified by the [degree-18 control](trace_control.py).
This disk is disjoint from the target.
Reduction modulo two gives \(\bar A=X^9+X^8+X^4+X^2+1\).
The [rational verifier](trace64_resultant.py) checks by division that none of the thirty monic binary polynomials of degrees one through four divides \(\bar A\).
Every reducible polynomial of degree nine has a factor of degree at most four, so \(A\) is irreducible over the rationals.
Consequently \(Q\) and \(A\) have no common root, since \(A\mid Q\) would put an additional nonreal pair in \(Q\).
Their resultant is a nonzero integer with absolute value
\[
    |\operatorname{Res}(Q,A)|=|A(w)|^2\prod_{i=1}^{30}|A(x_i)|.
\]

At the target center \(c\) the verifier obtains \(|A(c)|<19/1000\) and bounds the Taylor tail on the closed disk by \(1/1000\), giving \(|A(w)|<1/50\).
It encloses each \(t_i\) between consecutive millionths by a sign change of \(A\) or \(\Psi_{47}=1+\sum_{k=1}^{23}D_k\), where \(D_0=2,D_1=X,D_{k+1}=XD_k-D_{k-1}\).
These are thirty disjoint brackets, accounting for the seven real roots of \(A\) and every root of \(\Psi_{47}\).
Interval arithmetic on the bracket endpoints encloses each permitted \(x_i\), including the full separator tolerance in the second test.
On each of sixteen equal subdivisions with center \(s\) and half-width \(h\), the verifier bounds \(|A(x)|\) by \(\sum_{j=0}^9 |A^{(j)}(s)|h^j/j!\).
It takes the largest bound for each real interval before multiplying over all thirty.
Rational arithmetic gives a product below 1000 if all thirty quarter-spacing constraints hold, and below 2400 if the seven displacements are all at most \(1/50\) in the midpoint search.
Either bound makes the resultant's absolute value strictly less than one, proving the two exclusions.

From this directory run `python -B trace_control.py` and `python -B trace64_resultant.py` with standard Python.
The developer ran both exact checks.
For the single original set of rational separators, the separate [convex hull certificate](../../../claims/Yin_C_G0876_v2.md#statement) excludes the entire target cell for all integer coefficient heights.
The displacement tests above also allow the stated perturbations of those separators.
