---
author: Yin
---
# Complete cyclic norm expense retaining the Dobrowolski log-log factor

Human author Yin.
Root develops this physical successor of C147v4 under the continued G0001 authority.
The earlier versions remain preserved with their exact statements and assessments.
This version changes the bound for the SAME complete cyclic logarithmic norm by retaining the full log-log factor of its already recorded numerical Dobrowolski input.
It is not inferred from the separate angular-moment inquiry in D39, and no angular bound is silently substituted for a logarithmic-norm bound.
Root is the sole contributor to this local refinement and cannot independently review it.
No native mathematical program or numerical parameter test is used.

## Reuse and source scope

Read the accepted C147v4 actual-degree argument and C147v2 finite direct-energy estimate, including all original norm multiplicities and cutoff costs.
The exact numerical benchmark is already quoted in C147v4's source discussion and accepted there at its external statement/applicability scope.
Root additionally reread the retained Smy08 PDF pp5--6 (printed326--327), Section4.2 equation(11), through pdftotext in this continuation.
It states M(beta)>1+(1/1200)(log log N/log N)^3 for the original degree N>=2 and the stated nontorsion algebraic-integrality domain.
The survey's erroneous minimal-polynomial resultant explanation is not used; neither the original1979 proof nor a new stronger Voutier constant is adopted here.
The local improvement is the monotonicity of x/log x on x>=e, keeping the numerator which v4 deliberately discarded.

## Statement

Let alpha be any nontorsion algebraic integer unit of ORIGINAL degree d and total logarithmic Mahler measure m>0.
For every integer n>=1 put

    beta=alpha^n, N=[Q(beta):Q], h=nm/d,
    C_n=abs Norm_(Q(alpha)/Q)(alpha^n-1).

For 0<h<=exp(-40), write ell=log(1/h), and define

    Phi_5(h)=86 sqrt(h) ell^(5/2)/(log ell)^(3/2).

Then

    0<=log C_n/d<=Phi_5(h).                            (1)

Every original conjugate and powered-field multiplicity is retained; N need not equal d.
The bound is numerical, uniform in all stated inputs and strictly improves the v4 upper envelope on this domain.
The function Phi_5 is strictly increasing and tends to zero with h.
No original angular mean is identified with this cyclic logarithmic norm.

For every tau>0 define the capped threshold H_5(tau) as follows.
If tau/2>=Phi_5(exp(-40)), set H_5(tau)=exp(-40).
Otherwise H_5(tau) is the unique h in(0,exp(-40)) for which Phi_5(h)=tau/2.
If the actual norm density satisfies log C_n/d>=tau, then necessarily h>H_5(tau).
Moreover, with L=log(1/tau),

    H_5(tau) ~ [1/(128*86^2)] tau^2 L^(-5)(log L)^3
    as tau decreases to0.                            (2)

This is a threshold for an ACTUAL supplied positive norm income, not automatic income or input coverage.
The definition and asymptotic do not assert that any numerical inversion was executed.
No unrestricted positive Mahler gap follows without the separate arithmetic coverage obligation.

<a id="argument"></a>
## 1. Actual field and the full degree inversion

The accepted [C147v2 finite bound](Yin_C_G0147_v2.md#statement) supplies for every T>=1,R>=2,rho>0

    log C_n/d<=h+exp(-T)/2+1/R+(3exp(T)+T/R)rho
                  +sqrt((4T+7)(2h-log(rho)/N+4rho)).   (3)

Its proof uses beta's actual field and multiplicity d/N, so h=h_abs(beta) and log C_n/d is the average over its N distinct conjugates with exactly that multiplicity removed from both numerator and denominator.
Beta is still a nontorsion algebraic integer unit, and C_n is a nonzero integer, possibly1.
The [C147v4 actual-degree argument](Yin_C_G0147_v4.md#quantitative-actual-degree-inversion) already proves N>=exp(e) on h<=exp(-40), using the accepted L80 house input to exclude smaller degrees.
Only that degree threshold is needed from v4 here; its weaker final inversion is not substituted for the next calculation.

The full [Smy08 numerical statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001), as explicitly selected and quoted in C147v4, gives

    M(beta)>1+x,
    x=(1/1200)(log log N/log N)^3.

For N>=exp(e), one has 0<x<=1, so log(1+x)>=x/2 yields

    h>= (log log N)^3/[2400N(log N)^3].               (4)

There is no missing degree factor: h=m(beta)/N.
Put ell=log(1/h)>=40.
If N>=1/h, then 1/N<=h<=2400h(ell/log ell)^3.
If N<1/h, put y=log N; then e<=y<ell.
The derivative of y/log y is (log y-1)/(log y)^2>=0 for y>=e.
Rearranging (4) and applying that monotonicity gives

    1/N<=2400h(y/log y)^3<=2400h(ell/log ell)^3.

Thus BOTH actual-degree branches give

    1/N<=2400h ell^3/(log ell)^3.                     (5)

The assertion log N<=ell is confined to its valid branch.
Neither small total measure N h nor degree preservation is assumed.
This retains the full already recorded log-log contribution without changing the source constant or source proof boundary.

## 2. Complete analytic substitution

Choose exactly the finite direct-energy parameters

    T=ell/2, R=exp(T)=h^(-1/2), rho=h.

They satisfy T>=20, R>=exp(20)>2 and rho>0.
From (5),

    4T+7=2ell+7<=3ell,
    2h-log(rho)/N+4rho=6h+ell/N
       <=h[6+2400ell^4/(log ell)^3]
       <=2401h ell^4/(log ell)^3.                    (6)

For the last inequality, log ell<=ell implies ell^4/(log ell)^3>=ell>=40>6.
The square-root term in (3) is therefore less than

    85 sqrt(h)ell^(5/2)/(log ell)^(3/2),

since sqrt(7203)<85.
The remaining terms are exactly those already evaluated in v4:

    h+(9/2)sqrt(h)+(ell/2)h^(3/2)
       <=ell sqrt(h)
       <=sqrt(h)ell^(5/2)/(log ell)^(3/2).            (7)

The first comparison uses h<1 and ell>=40>=11.
The second is equivalent to log ell<=ell.
Combining (6)--(7) with (3) proves the upper bound (1).
Nonzero integral C_n gives its lower bound zero.
All truncation, exterior radius, continuity and original-height costs in (3) have been retained.
Because log ell>1 on ell>=40, Phi_5 is strictly smaller than the v4 envelope86sqrt(h)ell^(5/2).

## 3. Monotone threshold and its exact asymptotic

As a function of ell, the logarithm of Phi_5(exp(-ell)) has derivative

    -1/2+5/(2ell)-3/(2ell log ell)<0

for ell>=40.
Thus Phi_5 is strictly increasing in h and tends to zero as h decreases to zero.
This proves existence and uniqueness in the capped definition of H_5.
For 0<h<=H_5(tau), (1) gives log C_n/d<=tau/2<tau.
If h exceeds the initial domain, it already exceeds H_5(tau), so the stated inverse implication has no omitted branch.

For the asymptotic let tau decrease to0, L=log(1/tau), and fix any constant c>0.
Put v_c=c tau^2 L^(-5)(log L)^3.
Eventually v_c lies in(0,exp(-40)), and its logarithm is

    ell_c=log(1/v_c)=2L+5log L-3log log L-log c.

Consequently ell_c/L tends to2 and log ell_c/log L tends to1.
Direct substitution, without an uninspected inversion theorem, gives

    Phi_5(v_c)/tau
       =86sqrt(c)(ell_c/L)^(5/2)
                    [(log L)/(log ell_c)]^(3/2)
       ->86sqrt(c)2^(5/2).

The last limit is1/2 exactly when c=c_*=1/(128*86^2).
For any fixed c<c_*, it is eventually below1/2; for any c>c_*, it is eventually above1/2.
Monotonicity then places H_5(tau) between the corresponding v_c values.
Letting the two fixed constants approach c_* proves (2).
This asymptotic concerns the explicitly defined threshold and no purported near-one input sequence.

## Author check and remaining scope

Root checked both actual-degree branches, the full numerical source statement, every source-to-height factor, analytic parameter, square-root and nonsquare-root constant, the log-log denominator, monotonicity and the capped inverse's small/large branches and asymptotic constant.
This is an author check; whole independent review remains pending.
The separate new angular estimate in D39 has a different left side and is not used anywhere in this proof.
Application to the Frobenius-class criterion remains a separate consumer obligation after this cyclic refinement is accepted.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-18)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T10:29 |
| status | open |
| reason | Preserve v4 and register the stronger same-norm logarithmic estimate retaining the accepted numerical Dobrowolski log-log factor, with complete finite costs and inverse threshold, for separate whole review. No angular-to-logarithmic inference, numerical inversion or new source constant is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete strengthened cyclic statement](#statement) | Every original nontorsion integer unit and positive exponent, actual powered degrees, numerical envelope, monotonic inverse and exact inverse asymptotic. |
| argument | [Complete local proof](#argument) | Full actual-degree inversion, all direct-energy substitutions, monotonicity and capped threshold/asymptotic with all branches. |
| dependency | [Accepted finite direct-energy estimate](Yin_C_G0147_v2.md#statement) | The full parameterized cyclic bound with actual powered field, complete original norm multiplicity, finite cutoff, exterior and continuity costs. |
| dependency | [Accepted small-degree exclusion and numerical source selection](Yin_C_G0147_v4.md#quantitative-actual-degree-inversion) | Only N>=exp(e) on h<=exp(-40) and the exact already quoted numerical Dobrowolski source interface, not its discarded log-log factor. |
| dependency | [Numerical Dobrowolski benchmark](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Retained PDF printed326 equation11, M>1+(1/1200)(log log N/log N)^3 at statement/applicability scope; the defective survey resultant explanation and original proof are not used. |

### Decision whole-reviewed-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T10:34 |
| status | proved |
| reason | Adopt the stronger same-complete-norm envelope retaining the numerical Dobrowolski log-log factor, with all actual-degree, finite analytic, monotonicity and inverse costs, after the actual whole R381 review. No angular-to-logarithmic substitution or automatic arithmetic income is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete strengthened cyclic statement](#statement) | Every original nontorsion integer unit and positive exponent, actual powered degrees, numerical envelope, monotonic inverse and exact inverse asymptotic. |
| argument | [Complete local proof](#argument) | Full actual-degree inversion, all direct-energy substitutions, monotonicity and capped threshold/asymptotic with all branches. |
| dependency | [Accepted finite direct-energy estimate](Yin_C_G0147_v2.md#statement) | The full parameterized cyclic bound with actual powered field, complete original norm multiplicity, finite cutoff, exterior and continuity costs. |
| dependency | [Accepted small-degree exclusion and numerical source selection](Yin_C_G0147_v4.md#quantitative-actual-degree-inversion) | Only N>=exp(e) on h<=exp(-40) and the exact already quoted numerical Dobrowolski source interface, not its discarded log-log factor. |
| dependency | [Numerical Dobrowolski benchmark](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Retained PDF printed326 equation11, M>1+(1/1200)(log log N/log N)^3 at statement/applicability scope; the defective survey resultant explanation and original proof are not used. |
| review | [Whole finding with unknown relationship](../audits/reviews/Yin_R_G0381_v1.md#cyclic-loglog-whole-independent-finding) | Complete cyclic statement/proof, all three direct inputs, retained full numerical source factor, every original multiplicity, analytic cost and inverse threshold/asymptotic. |
