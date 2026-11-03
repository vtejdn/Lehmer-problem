---
author: Yin
---

# Complete original quartic return radius strictly between 68883 over 40000 and beta

Human author Yin.
The salem_collision_literature contributor supplied the exact original-law specialization and complete-return application of the newly inspected public source.
The independent quartic_source_check contributor inspected the source's entire qualitative Sections 2--5 proof in an isolated context and fixed its own CFMZ26-U002 finding.
The P1 finite certificate was inspected and replayed separately in J133 and CFMZ26-U003.
This is a source-based deduction, not a claim of a new proof of the external strict-drop theorem.
Whole independent project review and an explicit adoption remain outstanding.

## Statement

Fix P(t)=t^4-t^3-t^2-t+1 and its exterior real root beta.
For the COMPLETE chronological process X_0=0, X_(n+1)=beta X_n+eta_(n+1), the iid original digits have probabilities 1/4,1/2,1/4 at -1,0,1.
Let p_n=Pr(X_n=0), with p_0=1, and set

    h2=lim_(n->infinity) -log(p_n)/n,
    R=exp(h2), U(z)=sum_(n>=0)p_n z^n,
    t0=68883/40000=1.722075.

Every original word representation, intermediate zero visit and both neutral real coordinates remain part of this process.
Then

    U(t0) <= 302231454903657293676544000/2894667437079809876755951 < 105,
    68883/40000 < R < beta,
    log(68883/40000) < h2 < log(beta).

There exists a finite positive integer n with beta^n p_n>1.
No explicit such original return time is asserted by this statement.
The upper inequality is qualitative, with no adopted numerical upper deficit.
The statement neither classifies the critical first-return mean nor supplies a linear conditioned-midpoint estimate, a varying-input estimate, a higher-degree Salem theorem or the unrestricted G0001 conclusion.

## Complete argument

<a id="original-quartic-source-radius-argument"></a>
### RC1. Exact source law and true exponential radius

The primary source is [CFMZ26, arXiv:2610.09902v1](../literature/pdf/CFMZ26/arxiv-v1.html).
Its source P1 is exactly the polynomial in the statement, with the same exterior root in (1,2).
Write r=beta^(-1).
For independent fair signs epsilon_j, let Y_n=sum_(j<n)epsilon_j r^j, and let Y_n' be an independent copy.
The source defines Q_n=Pr(Y_n=Y_n') after all equal atoms are merged.
The half-differences (epsilon_j-epsilon_j')/2 are iid with probabilities 1/4,1/2,1/4.
Multiplying their sum at r by beta^(n-1) and reversing the iid digit vector gives

    Q_n=Pr(sum_(j<n)eta_j beta^j=0)=p_n.                 (RC1)

Chronological X_n has the same endpoint law by the same reversal.
Both bijections preserve all original word weights and multiplicities and impose no first-return condition.
This full law identity was checked in [CFMZ26-U001](../audits/literature/CFMZ26/Yin_U001.md#original-collision-and-energy-dimension) and independently in [CFMZ26-U002](../audits/literature/CFMZ26/Yin_U002.md#cfmz26-u002).

Independent zero events on consecutive blocks give p_(n+m)>=p_n p_m, and the all-zero word gives p_n>=2^(-n)>0.
Fekete's lemma therefore gives

    rho=lim_n p_n^(1/n)=sup_(n>=1)p_n^(1/n),
    R=1/rho.

The nonnegative series U has radius R by the root test.
These are the same true-radius conventions as adopted [C526](Yin_C_G0526_v1.md#decision-complete-isolated-whole-adoption); no finite-core spectral radius is substituted.

### RC2. Accepted qualitative external strict collision inequality

The complete qualitative proof of CFMZ26 Theorem 1.1 was independently inspected in CFMZ26-U002 and accepted there within its fixed v1 source scope.
Its chain consists of Proposition 2.1 and Lemma 2.2 for the actual algebraic hypotheses, Lemma 3.1 for the exact weighted four-torus integral, Definition 3.2 and Lemma 3.3/Proposition 3.4 for the finite packet-amplification implication, Lemmas 4.1/4.3/4.4 for the reciprocal construction and seed, and Lemma 5.1/Theorem 5.2 for its controlled-return hierarchy.
Those exact statements, definitions, proof checks and standard retained inputs are in the independent source unit.
No quantitative appendix or computation is a premise of that chain.

In particular, the proof constructs a packet with positive amplification exponent, and Proposition 3.4 then gives Q_n beta^n>1 for some finite n.
This is a checked consequence of the actual source proof, not an inference from singularity or full Hausdorff dimension.
Using RC1 and rho>=p_n^(1/n) gives

    rho>beta^(-1), hence R<beta.                         (RC2)

The source's separate collision-energy dimension identity is compatible with this conclusion but is not needed for this deduction.
The full Section 2--5 inspection is a resolved external input at the displayed source scope; it does not by itself constitute an independent review of the present combined project argument.

### RC3. Complete finite supersolution and paid exits

Use the source's integral coordinates

    M(x0,x1,x2,x3)=(x1,x2,x3,-x0+x1+x2+x3),
    e=(0,0,0,1), Z_(n+1)=M Z_n+eta_(n+1)e,
    L_z(x)=(z^3-z^2-z-1)x0+(z^2-z-1)x1+(z-1)x2+x3.

Reduction modulo P gives L_beta(Mx+ue)=beta L_beta(x)+u.
Injectivity of L_beta on Z^4 follows from the actual degree-four minimal polynomial, so Pr_0(Z_n=0)=p_n.
Define Omega={x: |(beta-1)L_beta(x)|<1} and Omega_180={x in Omega:0<max_j|x_j|<=180}.
The complement of Omega is forward invariant, because |d|>=1 implies |beta d+(beta-1)u|>=1.

For every m and initial state y, Pr_y(Z_m=0)<=p_m.
Indeed the difference-law characteristic function from zero is a product of nonnegative cos^2 factors, so Fourier inversion bounds every endpoint mass by its value at zero; the law from y is a translate.
This is the full original chain, before restricting to any finite set.

The source certificate supplies a sign-symmetric finite set F subset Omega_180 containing +/-e and closed under every successor remaining in Omega_180, together with an even nonnegative w:F->[0,infinity).
Its terminal extension wtilde is 1 at zero and at cube exits that remain in Omega, and 0 outside Omega.
All original potentially returning exits are charged; the chain is never row-normalized.
The complete inspected native replay proves, for every x in F,

    w(x)>=(t0/4)(wtilde(Mx-e)+2wtilde(Mx)+wtilde(Mx+e)). (RC3)

There are exactly 455137 canonical sign representatives, hence 910274 signed nonzero states.
Their weights have denominator Lambda=2^80, with initial numerator

    W_e=181660711014187729550784.

The native result checks all 1365411 representative digit edges: 791800 internal, 1 zero, 1104 paid exits and 572506 noncompletion exits.
The minimum exact cleared row residual is 2791379258189148576, and every strip decision succeeds with no unresolved case.
Sign symmetry establishes the same closure and inequality at the negatives of all representatives.
The complete source-code/finite-proof inspection and actual result are retained in [CFMZ26-U003](../audits/literature/CFMZ26/Yin_U003.md#cfmz26-u003), with [J133 native runner](../computations/programs/Yin_J_G0133/verify_p1.py) and complete output (`mathematics/computations/outputs/Yin_J_G0133/cfmz26_p1_lower.json`).

Here is the entire analytic step from the finite certificate to the complete series.
Let pi_k be the original probability that the first positive stop, at either zero or exit from the finite region, occurs at k and is either zero or a cube exit that remains in Omega.
Every zero-returning path has one such kept first stop, and its remaining return probability is at most p_(n-k).
Thus

    p_n<=sum_(k=1)^n pi_k p_(n-k).

Induction on the remaining allowed number of steps in the first-stop problem, starting with zero internal terminal function, bounds the full t0-weighted first-stop transform from each x in F by w(x), using RC3 and the paid terminal extension.
At zero the initial step therefore gives

    sum_(k>=1)pi_k t0^k <= c=(t0/2)(1+W_e/Lambda).

All sums here are nonnegative; no infinite unknown tail is discarded.
For U_N(t0)=sum_(n=0)^N t0^n p_n, the first-stop inequality yields U_N<=1+c U_(N-1).
Since U_0=1 and c<1, induction gives U_N<=1/(1-c); monotone convergence gives the same complete-series bound.

The exact initial value gives

    1-c=2894667437079809876755951/302231454903657293676544000>1/105.

Consequently U(t0)<=1/(1-c)<105, as asserted.
This is CFMZ26 Appendix B's fully paid theorem applied to the completely checked P1 witness, not a killed-box lower bound or an extrapolation of finite returns.

### RC4. Strict lower radius and remaining scope

The adopted C526 true-radius theorem applies to this actual algebraic unit, whose neutral real dimension is two, and gives U(R)=infinity.
Since U(t0)<infinity, the root test gives t0<=R.
Equality t0=R would contradict the adopted critical recurrence; hence

    68883/40000<R.                                      (RC4)

Together with RC2 and monotonicity of log, this proves the statement.
No derivative estimate at the true radius was used or obtained.
Strict R<beta does not select a finite or infinite critical-mean branch.

The supporting J133 replay has exactly the declared 455137 rows and 1365411 edges, input lengths 3641096 and 7282192 bytes, height 180 and source archive cap 25000000 bytes.
It constructs no new graph or candidate supersolution and does not enlarge a prior source bound.
It has no separate live memory monitor or hard memory ceiling; the fixed input and finite iteration bounds are the actual resource scope.
The runner executes the inspected unchanged source verifier, with mathematical checks active and only source metadata/digest comparison disabled.
It is not an independent implementation or formal verification.
Original source programs and witnesses remain in the registered local source archive, with exact member locators in J133 and CFMZ26-U003.
The source's P2 certificate, quantitative upper deficits, entire sequel and unrestricted Mahler problem are outside this argument.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision source-radius-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T13:03 |
| status | open |
| reason | Fix the complete source-based original-law deduction, combining independently inspected qualitative strict loss with the fully inspected and replayed P1 lower supersolution and already adopted true-radius recurrence. Whole independent project/native review and explicit adoption remain outstanding; no quantitative upper deficit or critical-mean result is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact original quartic interval and Green bound](#statement) | Same fixed P1, original ternary law, complete U(t0)<105, strict t0<R<beta, entropy inequalities and finite strict-collision existence, with all exclusions. |
| argument | [Complete RC1--RC4](#original-quartic-source-radius-argument) | Full-law bijection, true exponential normalization, accepted qualitative source implication, complete finite supersolution/paid-exit reduction and strict lower-radius use of critical recurrence. |
| dependency | [Independent qualitative source proof](../audits/literature/CFMZ26/Yin_U002.md#cfmz26-u002) | Exact v1 Sections 2--5 proof and its finite Q_n beta^n>1 consequence for the actual P1; no quantitative appendix or native premise. |
| dependency | [Checked source law and complete-return theorem](../audits/literature/CFMZ26/Yin_U001.md#cfmz26-u001) | Exact weighted-law correspondence, source coordinate convention, maximum-at-zero lemma and complete Appendix B first-stop supersolution theorem. |
| dependency | [Verified P1 finite source witness](../audits/literature/CFMZ26/Yin_U003.md#cfmz26-u003) | Entire stated height180 P1 certificate, exact roots/strip/state/closure/row/initial arithmetic, unchanged-source code inspection and actual bounded replay. |
| dependency | [Adopted true-radius recurrence](Yin_C_G0526_v1.md#decision-complete-isolated-whole-adoption) | Only the same actual original-law radius convention and U(R)=infinity for this unit's neutral real dimension two; no critical-mean classification. |
| support | [Native reproduction group](../computations/programs/Yin_J_G0133/readme.md) | Exact original archive/member dependencies, finite input and row/edge caps, executable command and actual verification limits. |
| support | [Bounded source runner](../computations/programs/Yin_J_G0133/verify_p1.py) | Entire authored runner selecting only the inspected unchanged P1 lower verifier and witnesses, with mathematical payload checks and atomic result publication. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0133/readme.md#recorded-runs) | All finite P1 root/strip/state/edge/row/initial checks, exact Green fraction and declared result scope; no stored transition graph or prior output oracle. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0133/cfmz26_p1_lower.json`; this target locates its run account. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T13:25 |
| status | proved |
| reason | Root read the entire fixed RC1--RC4, exact U001/U002/U003 source scopes, J133 author runner and the complete independent R1017. Adopt the full Green bound U(68883/40000)<105 and strict68883/40000<R<beta, with exact original-law correspondence, independently inspected qualitative source proof, independently checked complete finite witness and adopted critical recurrence. Every455137 row and1365411 digit edge is checked by the separate native implementation. No numerical upper deficit, explicit crossing time, critical-mean branch, higher-degree or unrestricted Task conclusion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact original quartic interval and Green bound](#statement) | Same fixed P1, original ternary law, complete U(t0)<105, strict t0<R<beta, entropy inequalities and finite strict-collision existence, with all exclusions. |
| argument | [Complete RC1--RC4](#original-quartic-source-radius-argument) | Full-law bijection, true exponential normalization, accepted qualitative source implication, complete finite supersolution/paid-exit reduction and strict lower-radius use of critical recurrence. |
| dependency | [Independent qualitative source proof](../audits/literature/CFMZ26/Yin_U002.md#cfmz26-u002) | Exact v1 Sections 2--5 proof and its finite Q_n beta^n>1 consequence for the actual P1; no quantitative appendix or native premise. |
| dependency | [Checked source law and complete-return theorem](../audits/literature/CFMZ26/Yin_U001.md#cfmz26-u001) | Exact weighted-law correspondence, source coordinate convention, maximum-at-zero lemma and complete Appendix B first-stop supersolution theorem. |
| dependency | [Verified P1 finite source witness](../audits/literature/CFMZ26/Yin_U003.md#cfmz26-u003) | Entire stated height180 P1 certificate, exact roots/strip/state/closure/row/initial arithmetic, unchanged-source code inspection and actual bounded replay. |
| dependency | [Adopted true-radius recurrence](Yin_C_G0526_v1.md#decision-complete-isolated-whole-adoption) | Only the same actual original-law radius convention and U(R)=infinity for this unit's neutral real dimension two; no critical-mean classification. |
| support | [Native reproduction group](../computations/programs/Yin_J_G0133/readme.md) | Exact original archive/member dependencies, finite input and row/edge caps, executable command and actual verification limits. |
| support | [Bounded source runner](../computations/programs/Yin_J_G0133/verify_p1.py) | Entire authored runner selecting only the inspected unchanged P1 lower verifier and witnesses, with mathematical payload checks and atomic result publication. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0133/readme.md#recorded-runs) | All finite P1 root/strip/state/edge/row/initial checks, exact Green fraction and declared result scope; no stored transition graph or prior output oracle. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0133/cfmz26_p1_lower.json`; this target locates its run account. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1017_v1.md#whole-source-radius-finding) | Entire fixed statement and complete argument, every exact mathematical/source/native input interface and all original scope limits; adoption remains this separate root decision. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0133](../computations/programs/Yin_J_G0133/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
