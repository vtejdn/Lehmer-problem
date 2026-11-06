---
author: Yin
---
# Exact weighted q=3 invariant-module evaluation

This computation supplies the finite quartic test in [L455 v2](../../../ledger/Yin_L_G0455_v2.md#finite-normalized-evaluation).
It retains the original inputs and the minimal seven-generator integer extension of the six orbit sums in [L455 v1](../../../ledger/Yin_L_G0455_v1.md#joint-evaluation-test).
The bottleneck_diagnosis contributor derived the module and performed the exact computation as ordinary author work for Yin.
No independent review, general stabilization theorem or near-one coverage is claimed.

## Native program and reproduction

Run `python mathematics/computations/programs/Yin_J_G0137/verify.py` from the repository root.
The standard-library-only [verify.py](verify.py) reconstructs the integer germ F=sqrt(UV), all seven normalized generators and their finite Taylor evaluation matrices from the embedded quartic coefficients.
It uses exact integers and binary row reduction, with no floating arithmetic, external input, random seed or earlier generated output.
The executable assertions check the explicit powers of two, the selected row certificates and full binary column rank.
Output is printed as compact JSON to stdout; no generated output file or large log is required.
The original calculation used Python 3.14.3.

## Inputs and exact scope

The fixed quartic is P(t)=t^4-t^3-t^2-t+1.
Its powered inputs are U=1-3x+x^2-3x^3+x^4 and V=1-7x-15x^2-7x^3+x^4.
Only q=3 and the two weighted windows N=9,13 are tested.
The native program computes coefficients of orders 0 through 48, then uses rows 0 through 24 for N=9 and rows 0 through 48 for N=13.
The original disposable calculation generated 96 coefficients; its decisive row certificates lie entirely in these retained shorter prefixes.
Removing unused higher coefficients does not change any tested entry.

The ordered generators are (1,delta_0,delta_1+delta_2,T-C,delta_0(delta_1+delta_2),delta_0(T-C),delta_12), where C=U_1 U_2 and T=F_1 F_2.
Their weights are (0,4,4,8,8,12,8), and their explicitly extracted binary exponents are (0,1,1,1,2,2,2).
Columns are ordered first by generator index and then by shift j from zero to N-weight-1.
The complete original integer lattice and the unimodular weighted change of basis are specified in L455 v2; dividing columns here is only the calculation of their residual matrix.
It is not an uncharged enlargement of the original module.

## Results and limits

For N=9 the evaluation has 22 columns and its normalized matrix has rank 22 over F_2.
Its certified independent rows are 0 through 18, followed by 21,22,24.
For N=13 there are 47 columns and normalized rank 47, with independent rows 0 through 45, followed by 48.
An odd normalized full-column minor therefore exists in each stated finite evaluation.
The corresponding original dyadic Smith exponents are nine zeros, eleven ones and two twos for N=9, and thirteen zeros, twenty-three ones and eleven twos for N=13.
Their total dyadic valuations are respectively 15 and 45.
All these factors are accounted for by the displayed explicit factors; neither finite map has an additional residual mod-2 loss or an exponent at least three.
These findings concern the complete stated rectangular evaluation maps, rather than a favorable isolated square minor.
The result does not bound deeper invariant factors for other inputs or windows and does not provide an arithmetic-to-complex-place comparison.
The quartic has the already covered Phi_5 reduction, so the computation supplies no near-zero sequence or unrestricted Mahler-gap conclusion.
