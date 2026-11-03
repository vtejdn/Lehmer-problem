## Logarithmic determinant in the citation applications map

Yin reports a mathematical normalization error in Yin's [citation applications map](manuscripts/Yin_T_G0001/citation.md), line 116, in the Luc22 application row.
It writes the scalar-return identity as \(\det_{\mathcal N(\mathbb Z)}(A)=m(\det A)\), but the report defines the Fuglede--Kadison determinant multiplicatively and \(m\) logarithmically.
The actual [TeX proposition](manuscripts/Yin_T_G0001/progress/sections/determinants.tex), lines 23--31, correctly states \(\log\det_{\mathcal N(\mathbb Z)}(A)=m(\det A)\).
The error is confirmed in the citation-map description; no error in that TeX proposition or its proof is asserted.
Repair and check the affected description under the mathematical correction rules, preserving the source's trace convention and the existing manuscript review's true scope.

## Schur elimination setting in the citation applications map

Yin reports an application-description mismatch in Yin's [citation applications map](manuscripts/Yin_T_G0001/citation.md), line 38, for the BV04 Schur-complement attribution.
The map describes a maximizing last variable and a negative-Hessian optimization setting, whereas [the actual TeX passage](manuscripts/Yin_T_G0001/progress/sections/entropy.tex), lines 378--389, eliminates an endpoint block from a matrix pencil over the formal variable t and asserts a polynomial determinant identity after clearing denominators.
That passage introduces no maximizing variable or negative-definite Hessian hypothesis.
The finite block-algebra calculation is presented locally, so this discrepancy does not by itself refute the determinant identity or create reliance on an optimization theorem.
Check and correct the attribution/application description against the actual algebraic setting and retained BV04 inspection scope, preserving the distinction between the local proof and external method attribution.

## Coefficient energy of the tenth packet representative and its residue

Yin reports a quantity-description error in Yin's [C31](claims/Yin_C_G0031_v1.md#statement), lines 59 and 738, and matching descriptions in [R790](audits/reviews/Yin_R_G0790_v1.md) lines 421/1920/1991 and [R232](audits/reviews/Yin_R_G0232_v1.md) line 139.
The displayed canonical residue is R_star=(4,6,6,3,1,-2,-4,-7,-5,-2), whose squared coefficient norm is 196.
The actual tenth rational representative is f_10=(9R_star-16P)/9; its numerator has squared norm 13284, so its coefficient energy is 164.
The text assigns or compresses the latter energy into a description of the nonternary residue, although these are different polynomials.
Clarify the actual object in the affected statement and review prose, preserving the correct packet, signed norm, exact capacity sandwich and original finite-family exclusion.
No error in the packet's saved coefficients or capacity bound is established by this wording defect.

## Scalar matrix versus its block automorphism

Yin reports an object-description error in Yin's [C227](claims/Yin_C_G0227_v1.md#statement), line 30.
It assigns the primitive quadratic polynomial \(qt^2-(2q+1)t+q\) and entropy \(\log q+\log\lambda_q\) to the rational scalar matrix \(A=2+1/q\).
The scalar matrix itself has a linear characteristic polynomial; the retained argument at lines 240--248 correctly assigns the quadratic polynomial and stated entropy to its two-dimensional block automorphism \(B_A\).
Identify that block automorphism explicitly in the statement, checking affected uses while preserving the correct leading-coefficient entropy charge and the existing proof and review scopes.
This wording defect does not refute the block construction or its entropy calculation.

## Missing path factor in the unit-cycle leaf review formula

Yin reports a confirmed formula omission in Yin's [R776 current C567 finding](audits/reviews/Yin_R_G0776_v1.md#current-unit-cycle-leaf), line 221.
It writes \(P_a=(t+1)(t^a+1)^2-t\), omitting the leaf-deletion path factor \(C_{2a-1}(t)=1+t+\cdots+t^{2a-1}\) multiplying the final \(t\).
The complete formula in [C567](claims/Yin_C_G0567_v1.md#statement), lines 16 and 110, is \(P_a=(t+1)(t^a+1)^2-tC_{2a-1}(t)\), obtained by deleting the leaf and then its neighbor.
The retained original finding in R776 also includes that path term.
Correct the affected review summary and check its actual consumers under the mathematical correction rules, preserving the fixed matrix, full determinant, root-count proof and original review scopes.
This omission does not establish a defect in C567's retained complete formula or construction.
