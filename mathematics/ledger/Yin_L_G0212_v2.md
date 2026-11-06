---
author: Yin
---

# Original spectral thresholds, zero-state rewards and the missing occupation bound

<a id="small-zero-reward-original-law-test"></a>
Date: 2026-11-05, Asia/Shanghai.
Contributor plan_entropy developed and checked this bounded construction test for Yin.
It continues the prescribed stationary-mass and return-tilt topic of [L212 v1](Yin_L_G0212_v1.md), whose complete theorem now belongs to [C511](../claims/Yin_C_G0511_v1.md#statement).
The fixed original mathematics and its actual review relationships are unchanged.
This version retains the new exploration only; its checking is author self-checking, without independent review or a new Claim assessment.

The question is whether a finite core selected for good spectral rate can acquire a useful original Perron zero-state occupation from a small reward at zero, followed by removal of that reward.
The actual [one-core upper-mean target](../drafts/Yin_D_G0009.md#one-finite-core-mean-target), its finite linear certificate, and its earlier holding and complete-bridge comparisons remain continuing author work in D9.
They are motivation, not adopted additional premises of the calculation below.
No new core, uniform upper mean, positive Mahler gap, external source inspection or computation is claimed.

## Original input and reused finite-prefix estimate

Let alpha be an actual nontorsion algebraic unit of degree d, let O=Z[alpha], and put m=log M(alpha).
Use natural logarithms and total Mahler measure, with

    0<m<=2^(-16).

The original chronological process is x -> alpha*x+eta, where the independent digits -1,0,1 have probabilities 1/4,1/2,1/4.
Let D be its actual zero-to-zero return core, let h be its collision entropy rate, and let f_n be its complete first-positive-return masses.
Let A be a finite subset of D containing zero for which the unchanged induced original matrix K_A is irreducible.
Every original edge between states of A is retained, and no boundary row is renormalized.
Write r_A=r(K_A), h_A=-log r_A, and assume

    h<=h_A<=2m.                                      (S1)

Let f_n^A be its complete original first-return masses and F_A(z)=sum_(n>=1)f_n^A z^n.
Then f_n^A<=f_n, f_1^A=1/2, and f_n^A=0 for 2<=n<=d.
The finite Perron and occupation proof in [C431](../claims/Yin_C_G0431_v1.md#statement), used only at its general finite-kernel scope, gives

    R_A=1/r_A=exp(h_A), F_A(R_A)=1,
    mu_A=R_A F_A'(R_A)=1/pi_A(0)<infinity,             (S2)

where pi_A is the original induced matrix's Perron stationary law.
The finite-kernel proof uses irreducibility and the original weights, not that material's separate finite-prime or Salem assumptions.
The rate domination h<=h_A is also part of [C479's finite original spectral comparison](../claims/Yin_C_G0479_v1.md#argument).

Set

    L_A=log(1/h_A), K_A^time=floor(L_A/(8h_A)),
    N_A=d(K_A^time+1)-1.

The [C557 small-total-measure argument](../claims/Yin_C_G0557_v1.md#statement), at its already accepted house-statement and source-inspection scope, gives d>64log(1/h).
Thus d>=64log(1/h_A), and h_A<=2^(-15)<1/64.
The [complete C557 prefix proof](../claims/Yin_C_G0557_v1.md#critical-delay-finite-mass) uses only these numerical conditions, the empty segment 2<=n<=d, and

    f_n^A<=f_n<=p_n<=(3 floor(n/d)+1)^(-d/2)
                                      for n>=d.

Replacing its positive tilt parameter by h_A therefore gives

    sum_(n=2)^(N_A) f_n^A R_A^n<=exp(-d/4).          (S3)

This is a direct use of that proof's parameter-dependent finite bound, not an assertion that h_A is the full critical exponent or that the infinite original critical law is recurrent.
No original late term within the displayed prefix is omitted.

## Exact reward pressure and the derivative direction

For theta>=0 multiply the entire zero row of K_A by exp(theta), leaving every other row and every induced edge unchanged.
Call the resulting comparison matrix K_A(theta); it is not another original digit law.
Each first-return word uses the zero row exactly once, so its Perron reciprocal R_A(theta) satisfies

    exp(theta) F_A(R_A(theta))=1.                     (S4)

This is the actual return-tilt mechanism already retained in [C511](../claims/Yin_C_G0511_v1.md#prescribed-zero-mass-frontier).
If B is the zero-deleted matrix, the finite hitting argument gives R_A rho(B)<1, including rho(B)=0.
Monotonicity of F_A gives 0<R_A(theta)<=R_A, so (S4) has a unique solution in the convergence interval and all its excursion moments are finite.
Put P_A(theta)=-log R_A(theta), and let mu_A(theta) and Var_A(theta) denote the mean and variance of the probability law

    q_(A,theta)(n)=exp(theta) f_n^A R_A(theta)^n.

Writing psi_A(t)=log F_A(exp(t)), its first two derivatives are the mean and variance of the corresponding normalized excursion-length law.
Differentiate psi_A(log R_A(theta))=-theta to obtain

    P_A'(theta)=1/mu_A(theta),
    P_A''(theta)=Var_A(theta)/mu_A(theta)^3>=0.        (S5)

These are complete original excursion-length moments with one reward factor; no different stationary mixture is substituted.
Entrywise comparison K_A<=K_A(theta)<=exp(theta)K_A gives

    P_A(0)<=P_A(theta)<=P_A(0)+theta.                 (S6)

Hence a rewarded spectral rate P_A(theta)>=-m with 0<=theta<=m would retain h_A<=2m after the reward was removed.
However, convexity bounds P_A'(0) from above by a chord slope, not from below.
A large derivative at positive theta does not provide the required original value P_A'(0)=pi_A(0).
Controlling that derivative change would require new information about the actual excursion variance in (S5).

## A small reward retains the full logarithmic delay

For every 0<=theta<=m, (S3)--(S4) imply

    sum_(n=2)^(N_A) q_(A,theta)(n)
       <=exp(theta) sum_(n=2)^(N_A) f_n^A R_A^n
       <=exp(m-d/4),
    q_(A,theta)(1)<=exp(3m)/2.                       (S7)

The conditions d>=64log(1/h_A) and h_A<=2^(-15) imply exp(m-d/4)<1/12.
The given m range also gives exp(3m)/2<7/12.
Thus the complete probability above N_A is greater than 1/3.
Because N_A+1=d(floor(L_A/(8h_A))+1)>dL_A/(8h_A),

    mu_A(theta)>d log(1/h_A)/(24h_A)
               >=d log(1/(2m))/(48m),
                    0<=theta<=m.                   (S8)

The last comparison uses that log(1/x)/x decreases on the positive range in question and h_A<=2m.
This applies the existing lower-delay argument to the proposed small reward; it supplies neither an upper mean nor an impossibility theorem for the one-core target.
The reward has not removed the logarithmic delay that a successful arithmetic construction would have to contradict by a uniform upper bound of order d/m.
Larger rewards lose the original spectral-rate control supplied by (S6), and asserting their removal without a new estimate repeats the missing occupation transfer.

## Construction outcome and remaining arithmetic information

Selecting the first core in an exhaustion whose rate crosses a threshold adds no occupation estimate to this calculation.
[C511's critical nonattainment alternatives](../claims/Yin_C_G0511_v1.md#statement) already show that, whenever either alternative occurs for an actual input, every information-minimizing sequence loses its zero-state mass.
C479's finite Perron cores have information h_A approaching h, so their spectral approximation alone cannot prevent that loss.
This is a conditional diagnostic, not a classification of near-one reciprocal endpoints.
[C856's actual radical family](../claims/Yin_C_G0856_v1.md#statement) separately calibrates fixed rate with arbitrarily small critical zero mass outside the reciprocal all-power endpoint domain; it is not a counterexample inside that domain.

The inspected reciprocal edge reversal in [C444 v2](../claims/Yin_C_G0444_v2.md#statement) and stationary residue/neutral-energy constraints in [L211](Yin_L_G0211_v1.md#stationary-geometry-fixed-scope) give no missing uniform original occupation bound at their present scopes.
No arithmetic state-selection or pruning rule with that bound emerged from this test.
Further manipulation of pressure convexity alone is not selected as a construction mechanism.
A substantive continuation needs a new rule using the endpoint's integral order and all its embeddings, or new control of the actual excursion distribution, rather than another finite-matrix certificate.

The author checked the reward count per first return, both implicit derivatives, their directions, the convergence condition including nilpotent B, the original prefix domination, numerical tail mass and the separation between original and rewarded kernels.
This records that actual author check only, with no independent proof review or unrestricted Task conclusion.
