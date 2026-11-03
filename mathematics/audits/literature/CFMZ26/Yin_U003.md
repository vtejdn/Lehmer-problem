---
author: Yin
---

# CFMZ26-U003: verified complete P1 finite lower supersolution

<a id="cfmz26-u003"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: [CFMZ26 original arXiv:2610.09902v1 HTML](../../../literature/pdf/CFMZ26/arxiv-v1.html), 7 October 2026, and [Zenodo verification release 1.0](../../../literature/pdf/CFMZ26/Quartic-Salem-Verification-v1.0.zip), record 23179204.

Passages: Entire Appendix B; Appendix C, Theorem C.1 and Proposition C.2 for P1 only; Appendix D root/strip/row/logarithm procedures; native archive members verification/lower_math.py, verification/verify_lower.py and verification/lower_p1/states.bin and W.bin under its Quartic-Salem-Verification-v1.0 directory.

Inspection: On 2026-10-26, salem_collision_literature checked the whole Appendix B analytic reduction, read both selected native source modules completely before execution, checked their actual finite scope against P1, and executed the bounded [J_G133 runner](../../../computations/programs/Yin_J_G0133/verify_p1.py). This is source-code inspection and replay of the unchanged source algorithm, not an independent implementation or isolated independent review of the project deduction. The complete output (`mathematics/computations/outputs/Yin_J_G0133/cfmz26_p1_lower.json`) records the actual mathematical result. P2, the upper-bound code and all quantitative upper deficits are excluded.


## Accepted external finite conclusion

Use only P1(X)=X^4-X^3-X^2-X+1, its exterior root beta and the original independent difference digits with probabilities 1/4,1/2,1/4 at -1,0,1.
Let p_n be the full zero-return probability and U(t)=sum_(n>=0)t^n p_n, including p_0=1 and every intermediate zero visit.
The source's Theorem C.1 is accepted here for P1 at the complete proof-and-native scope described below:

    t=68883/40000=1.722075,
    U(t) <= 302231454903657293676544000/2894667437079809876755951 < 105.

No approximation to a finite killed return series replaces U.
The analytic dependency is the complete first-stop supersolution theorem retained in [CFMZ26-U001](Yin_U001.md#complete-return-supersolution).
The exact original-law identity is [CFMZ26-U001](Yin_U001.md#original-collision-and-energy-dimension).
The result uses no qualitative strict-drop theorem or quantitative upper-bound appendix.

## Exact inspected native argument

The two source modules use only Python's standard library, exact integers and Fraction arithmetic for all acceptance decisions.
The root is isolated inside (17/10,7/4), with opposite polynomial signs and a strictly positive interval lower bound for the derivative.
Two hundred rational bisections preserve both strict signs and the exact width.
Thus the computed interval contains precisely the actual exterior beta.

For x=(x0,x1,x2,x3), the strip d(x)=(beta-1)L_beta(x) is evaluated through the four reduced degree-at-most-three polynomials

    d0(X)=-X^3+X^2+X,
    d1(X)=X^3-2X^2+1,
    d2(X)=X^2-2X+1,
    d3(X)=X-1.

Interval Horner evaluation and outward rounding on denominator Lambda=2^80 give enclosing coefficient pairs [g_j,g_j+1]/Lambda, where

    (g0,g1,g2,g3)=
    (-506912470679028648998986,
      212552539420349734382772,
      630339994189785769387358,
      872945756683522319935030).

For signed integer coordinates the source chooses the interval endpoint according to the coordinate sign.
It accepts membership only if the entire resulting interval lies strictly in (-1,1), and accepts nonmembership only if the interval is entirely on or outside one boundary.
Its fallback reduces a remaining polynomial symbolically, accepts a constant by exact comparison, and rejects any undecided nonconstant case.
In this replay no fallback or undecided case occurred.
This is a strict real-strip decision, not a decimal approximation or coefficient-height substitute.

The retained states are four little-endian signed 16-bit integers per row; each nonnegative supersolution numerator is one little-endian unsigned 128-bit integer.
Exactly 455137 canonical sign representatives and the same number of numerators are read, with Lambda as the weight denominator.
Every representative is nonzero, has its first nonzero coordinate positive, lies in the strict strip, has height at most 180, and is distinct from all previous rows.
The initial representative is e=(0,0,0,1).
These checks establish the declared sign-symmetric finite set, not a presumed reachable-state enumeration.

For every listed representative and each digit -1,0,1, the program recomputes the successor

    y=(x1,x2,x3,-x0+x1+x2+x3+digit).

The terminal value is Lambda at zero or at a height exit remaining in the strip, and zero outside the strip.
An internal successor is required to have its exact canonical sign representative in the supplied list.
Thus closure is verified, with every cube exit that might return charged value 1 and no row renormalization.
Sign symmetry proves the corresponding statement and inequality for all 910274 nonzero signed states.

Every row checks the exact integer inequality

    residual_j=4*40000*W_j-68883*(Wtilde_-+2Wtilde_0+Wtilde_+)>=0.

All 455137 row inequalities and all 1365411 digit-labelled successors passed.
Their exact class counts are

    internal=791800, zero=1, paid_exit=1104, noncompletion=572506.

The minimum residual is 2791379258189148576 at row 329275.
The initial numerator is W_0=181660711014187729550784, and direct rational arithmetic gives

    1-(t/2)*(1+W_0/Lambda)
      =2894667437079809876755951/302231454903657293676544000
      >1/105.

This proves every hypothesis of Appendix B's theorem and the displayed complete Green-series bound.
The source also verifies t<beta and its stated lower-dimension exponent by rational log-series tails; these checks passed, but the strict original-radius deduction below needs neither that decimal exponent nor a general dimension theorem.

## Reproduction, dependencies and scope limits

The [J_G133 README](../../../computations/programs/Yin_J_G0133/readme.md) supplies the exact command and input/output locators.
Run from the repository root:

    .venv/Scripts/python.exe -B -S mathematics/computations/programs/Yin_J_G0133/verify_p1.py

The runner extracts only the two inspected source modules and the P1 state/weight arrays into disposable operational storage within its own output home, executes source verify_case(1) with metadata comparison disabled, and removes the extraction afterward.
Disabling metadata comparison omits only claims about the certificate metadata and digests; it preserves every mathematical root, strip, state, successor, row, endpoint and logarithm check.
The runner separately checks the exact initial numerator and minimum residual against Proposition C.2.
All complete results are published atomically after success.
No pre-existing report or stored transition graph is used as an oracle.
The original source and necessary witnesses remain in the registered archive; generated reports retain no authored-material digest baseline.

The fixed caps are 455137 sign representatives, 1365411 digit edges, state input 3641096 bytes, weight input 7282192 bytes and source archive at most 25000000 bytes.
There is no new graph exploration, search for a supersolution or increase of the source height.
This bounded replay has no separate live process-memory monitor or asserted hard memory ceiling.
The actual first replay completed successfully at exactly the stated scope.

The native algorithm and its elementary arithmetic were inspected, but this does not certify the Python runtime or provide formal verification.
The external source's Appendix B is the analytic dependency; standard nonnegative Fourier inversion, finite conditioning, induction and monotone sums are its retained mathematical ingredients.
No uninspected quantitative source theorem is substituted for the checked finite inequalities.

The project [C_G526](../../../claims/Yin_C_G0526_v1.md#statement) independently gives U(R)=infinity at its true radius.
Hence the present finite U(t) bound implies t<R: positivity first gives t<=R, and equality would contradict critical recurrence.
This is a direct source application, not a source assertion that its boundary series converges at R.
It gives no estimate of F'(R), no critical-mean classification, no positive linear conditioned-midpoint estimate and no degree-uniform Mahler conclusion.
Project acceptance of a C using this source still requires the applicable complete project review and explicit decision.
