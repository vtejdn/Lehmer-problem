---
author: Yin
---

# Complete single-neutral-factor control with linearly many low modes and bounded actual joint symbols

This retains the complete necessary mathematical argument from [original L407 fixed record](../ledger/Yin_L_G0407_v1.md#neutral-factor-low-mode-question).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let n=9 mod120 with n>=129, theta the real root greater than1 of t^3-t-1, P_n(t)=t^n(t^3-t-1)+(1-t^2-t^3), d=n+3>=132 and N=2d.
The complete five-factor congruence table in C248 leaves no cyclotomic factor on this progression, so P_n itself is the original irreducible Salem polynomial; log theta<m(P_n)<log(4/3) and m(P_n) tends to the fixed positive log theta.
Let A be the N-by-d coefficient matrix of ALL d consecutive shifts of P_n, let G=A^tA, and let R_P=I-A G^(-1)A^t.
Set rho=1-1/36864 and C0=(1/36)[1/(1-rho)+12rho/(1-rho)^2].
The exact C160 fixed input supplies I_d/1024<=G<=36I_d and kappa_d(R_P)<=36C0, where kappa_d(R)=(2/d)sum_(h=1)^(N-1)|sum_i R_(i,i+h)| retains both signed Fourier directions and the ORIGINAL d.

Multiply by exactly ONE neutral factor F_n=(1-t)P_n of degree d+1 and unchanged logarithmic measure.
Let D be the d-by-(d-1) matrix with columns e_j-e_(j+1), 0<=j<d-1.
The complete F_n shift matrix in the SAME N coordinates is exactly A_F=A D, all d-1 shifts fit, G_F=D^tG D, and H_F=G_F/144<=I because ||F_n||_1<=12.
The full finite Dirichlet spectrum of D^tD is 4sin^2(k pi/(2d)), 1<=k<=d-1, with sine eigenbasis and zero endpoint coordinates.
Both ordered min-max bounds hold:

    (1/1024)4sin^2(k pi/(2d))<=lambda_k(G_F)<=144sin^2(k pi/(2d)),
    lambda_k(H_F)<=sin^2(k pi/(2d))<=pi^2 k^2/(4d^2).

For EVERY fixed 0<delta<=1, put q_d(delta)=floor(d sqrt(2delta)/pi), so 0<=q_d<d-1 on this domain.
For the exact smooth cutoff chi_delta of C506, zero on the CLOSED interval [0,delta/2], define X_F=A_F/12, Pi_F=A_F G_F^(-1)A_F^t and E_delta=Pi_F-X_F f_delta(H_F)X_F^t.
Then #{lambda(H_F)<delta}>=q_d and trace E_delta>=q_d, including eigenvalues exactly delta/2; the q_d=0 finite case is vacuous and liminf trace E_delta/d>=sqrt(2delta)/pi>0 as d grows through the stated irreducible progression.
Delta is fixed before the input limit, and no uniform constant as delta tends to zero is supplied.

Nevertheless R_F-R_P is a positive rank-one orthogonal projection in the same window, so

    |kappa_d(R_F)-kappa_d(R_P)|<=2-1/d<2,
    kappa_d(R_F)<=36C0+2.

Every exponent of F_n is e0+n e1 with 0<=e0<=4 and e1 in {0,1}; all offsets of A_F G_F^h A_F^t for 0<=h<=k lie in |e0|<=4(k+1), |e1|<=k+1.
Thus each row of X_F T_k(2H_F-I) X_F^t has at most (8k+9)(2k+3)<=27(k+1)^2 possible nonzeros for EVERY k>=0, including finite boundaries and coinciding offsets.
C506 therefore applies with B=144, C=27 and nu=2.
For its explicit fixed-threshold K_(delta,2,27), the good-symbol full Wiener norm divided by d is at most2K, while the ACTUAL nonconstant Fourier mass of E_delta divided by d is at most36C0+2+2K and its constant coefficient divided by d is at most(d-1)/d<1.
Its full normalized Wiener norm is consequently at most36C0+3+2K, uniformly in d despite linearly diverging unnormalized low-mode trace.

This actual fixed-positive-measure integer family proves representation sensitivity and failure of NECESSITY for bounded low-mode rank or trace in the one-sided sufficient cutoff criterion; it does not refute the criterion or replace a hypothetical cancellation by an assumption.
No arbitrary-polynomial theorem, near-one arithmetic coverage, numerical spectrum or new computation follows.
The different C494 moving family is used only for comparison: its count alone gives no coherence bound; the later C171 theorem separately proves its actual coherence divergence and is not a premise here.
The complete finite spectrum, strict/end-point cutoff, full raw shifts, positive rank-one transfer and actual entire remainder-symbol estimate are proved below, with the original dated checkpoint and all eight input roles preserved.
DMS84-U001 is inherited classical attribution only, with no bounded-inverse theorem, published-edition equivalence, new source constant or new original-source proof audit.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-22T02:50 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Complete proof](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact original Salem family](Yin_C_G0248_v1.md#excess-three-family) | The actual original polynomial, degree and fixed positive interval/limit, with n=9 mod120 and n>=129. |
| dependency | [Complete all-factor table](Yin_C_G0248_v1.md#family-cyclotomic-factors) | All five congruences and squarefreeness, checked on the actual progression to obtain an empty cyclotomic product. |
| dependency | [Exact full finite Gram bound](Yin_C_G0160_v1.md#fixed-seed-gram-coercivity) | I/1024 and 36I for ALL d shifts in the original window; no circulant or infinite-window substitution. |
| dependency | [Exact original projection input](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | The actual c=0 bound 36C0 with original d and the reproduced positive-semidefinite diagonal estimate. |
| dependency | [Complete finite cutoff and constant](Yin_C_G0506_v1.md#joint-cutoff-target) | Exact chi_delta, f_delta, E_delta, K_(delta,nu,C) and good-symbol theorem; the actual B=144,C=27,nu=2 hypotheses are proved here. |
| dependency | [Same-window coefficient normalization](Yin_C_G0506_v1.md#original-factor-cutoff-price) | Full polynomial relation spaces and both signed diagonal sums; raw degree d+1 does not replace the original d. |
| support | [Inherited classical attribution](../audits/literature/DMS84/Yin_U001.md#dms84-u001) | Existing inspected author-manuscript polynomial-support mechanism only, without external inverse theorem, approximation constant or new source audit. |
| support | [Different moving-family comparison](Yin_C_G0494_v1.md#moving-exponent-gram-feasibility) | Different actual raw Gram and low-mode geometry only; no bounded coherence transfer is claimed. |
| support | [Restricted arithmetic comparison](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | The fixed six-term original family is already covered by the restricted short-annihilator gap domain. |
| support | [Later divergence scope](Yin_C_G0171_v1.md#two-block-torus-statement) | Current historical-scope clarification only: a separate later argument settles the different actual moving-family coherence. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T02:58 |
| status | proved |
| reason | Adopt the actual complete current SELF check of the exact single-neutral-factor control, including the complete finite spectrum, strict threshold, full original-window rank-one and actual remainder symbol; no near-one coverage or independent-review upgrade follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Exact argument](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact dependency](Yin_C_G0248_v1.md#excess-three-family) | The actual original polynomial, degree and fixed positive interval/limit, with n=9 mod120 and n>=129. |
| dependency | [Exact dependency](Yin_C_G0248_v1.md#family-cyclotomic-factors) | All five congruences and squarefreeness, checked on the actual progression to obtain an empty cyclotomic product. |
| dependency | [Exact dependency](Yin_C_G0160_v1.md#fixed-seed-gram-coercivity) | I/1024 and 36I for ALL d shifts in the original window; no circulant or infinite-window substitution. |
| dependency | [Exact dependency](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | The actual c=0 bound 36C0 with original d and the reproduced positive-semidefinite diagonal estimate. |
| dependency | [Exact dependency](Yin_C_G0506_v1.md#joint-cutoff-target) | Exact chi_delta, f_delta, E_delta, K_(delta,nu,C) and good-symbol theorem; the actual B=144,C=27,nu=2 hypotheses are proved here. |
| dependency | [Exact dependency](Yin_C_G0506_v1.md#original-factor-cutoff-price) | Full polynomial relation spaces and both signed diagonal sums; raw degree d+1 does not replace the original d. |
| support | [Exact support](../audits/literature/DMS84/Yin_U001.md#dms84-u001) | Existing inspected author-manuscript polynomial-support mechanism only, without external inverse theorem, approximation constant or new source audit. |
| support | [Exact support](Yin_C_G0494_v1.md#moving-exponent-gram-feasibility) | Different actual raw Gram and low-mode geometry only; no bounded coherence transfer is claimed. |
| support | [Exact support](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | The fixed six-term original family is already covered by the restricted short-annihilator gap domain. |
| support | [Exact support](Yin_C_G0171_v1.md#two-block-torus-statement) | Current historical-scope clarification only: a separate later argument settles the different actual moving-family coherence. |
| review | [Exact review](../audits/reviews/Yin_R_G0715_v1.md#complete-neutral-factor-whole-self-finding) | Entire current Statement and #argument, all eight original formulas and fixed input roles, finite endpoints, actual full-symbol cost and inherited source limits. |

## Complete retained argument

<a id="argument"></a>

The original proofs and input descriptions below retain their dated mathematical scope; they supply no Task/E resumption.

Date: 2026-10-18T15:10.
Human author Yin.
Root develops this exact S3/S5 control after L406's fixed-threshold rank and trace obstruction.
This is author mathematics without numerical execution, independent review or adoption.

<a id="neutral-factor-low-mode-question"></a>
## Actual question and original inputs

[L406](Yin_C_G0506_v1.md#joint-cutoff-target) pays a low spectral remainder by rank or trace, while its [L402 application](Yin_C_G0506_v1.md#moving-exponent-low-mode-packing) has a diverging count at every fixed threshold and an unresolved actual coherence.
The question here is whether the low-mode count can grow EVEN WHEN the true original and raw-numerator coherences are already uniformly bounded on an actual nontorsion integer family.
A positive answer would make the representation dependence of that sufficient spectral certificate concrete.
The new control uses [C160's accepted fixed-seed theorem](Yin_C_G0160_v1.md#statement) and its explicit irreducible progression, not a freely specified matrix or hypothetical near-one sequence.

Take n=9 mod120, n>=129, and

    P_n(t)=t^n(t^3-t-1)+(1-t^2-t^3), d=n+3, N=2d.

On this progression P_n is itself the original irreducible Salem polynomial: the complete cyclotomic part is empty by C160/L38's retained table.
Its total logarithmic measure lies strictly between log theta and log(4/3), with fixed positive limit log theta.
Let A be the N-by-d full coefficient matrix of the d shifts of P_n.
C160 gives

    (1/1024) I_d <= G=A^tA <=36 I_d,
    kappa_d(R_P)<=36 C0,                                  (1)

with its fixed explicit C0 and original N=2d normalization.
No new irreducibility or varying-input small-measure assertion is needed.

Now multiply by exactly ONE neutral factor,

    F_n(t)=(1-t)P_n(t), deg F_n=d+1.

Its full logarithmic measure remains m(P_n); its anti-reciprocity is immaterial to the coefficient projection.
Let D be the d-by-(d-1) difference matrix with column j equal to e_j-e_(j+1), for0<=j<d-1.
The actual full F_n shift matrix in the SAME N coordinates is precisely A_F=A D, and

    G_F=A_F^t A_F=D^t G D.                                (2)

All d-1 shifts and their last coefficients remain inside the original2d window.
A_F has full column rank because A and D do.
The elementary convolution upper bound ||F_n||_1<=12 permits the fixed upper scale B=144, with H_F=G_F/144<=I.

<a id="neutral-factor-linear-low-count"></a>
## Complete eigenvalue comparison and linear count

D^tD is the (d-1)-by-(d-1) tridiagonal matrix with diagonal2 and adjacent entries-1.
For k=1,...,d-1, the vector whose coordinate j is sin((j+1)k pi/d) is nonzero and has eigenvalue

    lambda_k(D^tD)=4sin^2(k pi/(2d)).                      (3)

The two missing boundary coordinates are sin0=sin(k pi)=0, so the formula also holds on the first and last row.
These d-1 eigenvalues are distinct and increasing, and their eigenvectors therefore form a basis by symmetry.
This proves the entire finite spectrum with no periodic boundary substitution.

Equation(1) gives the quadratic-form bounds

    (1/1024)D^tD <= G_F <=36 D^tD.

The finite min-max principle, or its direct subspace comparison on the first k eigenvectors, yields for ordered eigenvalues

    (1/1024)4sin^2(k pi/(2d))
       <=lambda_k(G_F)<=144sin^2(k pi/(2d)),
    lambda_k(H_F)<=sin^2(k pi/(2d))
                      <=pi^2 k^2/(4d^2).                 (4)

Fix ANY0<delta<=1 before d varies and set

    q_d(delta)=floor(d sqrt(2delta)/pi).

For the present d>=132, 0<=q_d<d-1; if it is zero the following finite lower bound is vacuous.
Every1<=k<=q_d satisfies lambda_k(H_F)<=delta/2.
Therefore

    #{lambda(H_F)<delta}>=q_d(delta),
    trace E_delta>=q_d(delta),
    liminf_(d->infinity) trace E_delta/d
                              >=sqrt(2delta)/pi>0.         (5)

Here E_delta is exactly L406's smooth-cutoff remainder built from A_F and B=144.
Its cutoff vanishes on the complete interval[0,delta/2], so each of these eigenvalues contributes exactly1 to that trace, including the endpoint.
The limit runs through the actual irreducible progression above.
No random spectrum, computed eigenvalue or changed matrix normalization has entered the count.

<a id="neutral-factor-bounded-symbol"></a>
## Uniform true symbols despite the divergent paid count

The F_n relation subspace lies inside the P_n relation subspace and has codimension exactly1 there, because it is A times im D inside A R^d.
Consequently

    R_F-R_P is a positive rank-one orthogonal projection.

For any positive N-by-N matrix Q,

    sum_(i!=j)|Q_ij|<=(N-1)trace Q.

This is the C160/L406 diagonal Cauchy--Schwarz inequality, also obtained from |Q_ij|<=sqrt(Q_ii Q_jj).
Grouping its signed diagonal coefficients and dividing by the ORIGINAL d therefore proves

    |kappa_d(R_F)-kappa_d(R_P)|<2,
    kappa_d(R_F)<=36C0+2.                                (6)

The bound uses the same original P_n and same2d window, not degree d+1 as a new normalization.
Together(5)--(6) are an actual bounded-measure, growing-original-degree control where a positive proportion of normalized raw Gram eigenvalues lie below EVERY fixed positive threshold while the actual raw and original joint Fourier coherences remain bounded.
This disproves necessity of a bounded exceptional rank or trace in L406's sufficient criterion.
It does not contradict that criterion, which was explicitly one-sided.

For completeness the good-symbol support condition is also uniform on this control.
Every exponent of F_n is of the form e0+e1*n with0<=e0<=4 and e1 in{0,1}.
Each exponent difference has |e0|<=4, |e1|<=1.
An entry of A_F G_F^h A_F^t has an offset obtained by at most h+1 such differences; all powers0<=h<=k lie in the single box

    |e0|<=4(k+1), |e1|<=k+1.

Thus the number of possible offsets in any row is at most

    (8k+9)(2k+3)<=27(k+1)^2.                              (7)

This remains true for a Chebyshev polynomial of degree k in2H_F-I, including the k=0 term; boundaries and coinciding offsets only reduce the count.
L406 therefore applies with fixed C=27,nu=2,B=144 at each fixed delta.
Its good joint symbol has full Wiener norm divided by d at most2K_(delta,2,27).
By (6) and the triangle inequality, the ACTUAL remainder symbol has nonconstant Fourier mass divided by d at most

    36C0+2+2K_(delta,2,27),                              (8)

uniformly in d despite trace E_delta growing linearly.
Its constant coefficient divided by d is at most(d-1)/d<1 because0<=E_delta<=Pi_F.
Hence even its full normalized Wiener norm is uniformly bounded by adding1 to(8).
This is a bound on the complete low-mode symbol, not only a claim that cancellation might exist.
It follows from the established original projection and exact rank-one relation, not from a new localization theorem for arbitrary low modes.

<a id="neutral-factor-consequence"></a>
## Consequence and remaining arithmetic scope

Neutral multiplication can make a uniformly coercive relation Gram acquire linearly many arbitrarily low normalized eigenvalues while changing the actual joint projection by only rank1.
The spectral count and trace are therefore representation-sensitive quantities, even at exactly the same original input and coefficient window.
L402's specific raw low-mode count still stands, but cannot on its own diagnose its actual original or raw coherence.
Deflating known neutral factors is an exact change of representative with the stated rank cost; controlling the resulting coefficients or other Gram properties is a separate task.

This construction supplies no new automatic near-one coverage: the original six-term family is already covered by C92 and has a fixed positive measure limit.
It also does not prove a bounded joint symbol for the moving-exponent L402 family or for an arbitrary integer polynomial.
The useful next question is whether an actual factor-aware preconditioner or localized representation can control the low-mode SYMBOL with original arithmetic costs, rather than require its unbounded count or trace to stay bounded.
No new J or numerical scan is justified merely to reconfirm this exact construction.

Author checking covers the original irreducible progression, full same-window shift ranges, rectangular D and finite Dirichlet endpoints, both min-max inequalities, strict cutoff count, positive rank-one projection, signed Fourier normalization, uniform support box and every fixed-threshold versus input limit.

<a id="neutral-factor-fixed-inputs"></a>
## Exact fixed inputs and source boundaries

| Role | Target | Scope |
| --- | --- | --- |
| Original family and empty cyclotomic progression | [L38 family](Yin_C_G0248_v1.md#excess-three-family), [complete table](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Actual original irreducible Salem polynomial on n=9 mod120, n>=129; original d=n+3 and fixed positive measure interval/limit. No new irreducibility or near-one family is claimed. |
| Uniform finite Gram | [C160 exact coefficient bound](Yin_C_G0160_v1.md#fixed-seed-gram-coercivity) | Full consecutive-shift Gram between I/1024 and 36I, with no circulant or infinite-window replacement. |
| Original projection and rank comparison | [C160 original-factor projection](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection), [R385 accepted independent review](../audits/reviews/Yin_R_G0385_v1.md#fixed-seed-projection-whole-independent-finding) | Actual c=0 progression gives 36C0 at the original2d window; the same PSD diagonal inequality is reproduced here. C160 author relationship is disclosed in the separate review of this consumer. |
| Cutoff definition and good-symbol constant | [L406 complete finite cutoff](Yin_C_G0506_v1.md#joint-cutoff-target), [R409 whole review](../audits/reviews/Yin_R_G0409_v1.md#joint-cutoff-whole-independent-finding) | Exact chi_delta, E_delta, support hypothesis and K_(delta,nu,C); B=144, C=27, nu=2 and original d are verified in this consumer. |
| Same-window normalization | [L406 original-factor scope](Yin_C_G0506_v1.md#original-factor-cutoff-price) | Full polynomial relation spaces, signed diagonal symbol and original degree; no numerator-degree relabeling. |
| Earlier growing-mode obstruction | [L406 moving-exponent comparison](Yin_C_G0506_v1.md#moving-exponent-low-mode-packing), [L402 Gram scope](Yin_C_G0494_v1.md#moving-exponent-gram-feasibility) | Motivation and comparison only: its low-mode divergence does not determine actual coherence, and no bound for that different family is supplied here. |
| Existing arithmetic coverage | [C92 short annihilator](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | The fixed six-term family is already in the restricted short-annihilator gap domain; this projection control adds no automatic small-total-measure coverage. |
| Classical support mechanism | [DMS84-U001](../audits/literature/DMS84/Yin_U001.md#dms84-matrix-power-support) | Attribution inherited through C160/L406 for polynomial approximation and matrix-power support; no bounded-inverse theorem, source constant, published-edition equivalence or new original-source proof audit is imported. |

The complete root-authored argument above is retained without a mathematical change.
This table makes its existing input roles explicit; it supplies no independent review or adoption.
