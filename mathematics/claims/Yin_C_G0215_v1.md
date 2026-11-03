---
author: Yin
---

# Reciprocal negative-spectrum and integer-moment constraints

This retains the complete original main argument and integer-moment supplement of [L10](../ledger/Yin_L_G0010_v1.md), dated 2026-10-06.
The coordinating agent authored the first argument and uniqueness_lehmer authored the supplement; the original scoped findings remain distinct from the actual current retention inspection.
No mathematical program, new source acquisition or novelty claim is introduced.

## Statement

All logarithms are natural.
Let p be a real monic squarefree reciprocal polynomial of positive integer degree d>=1 with p(0)=1, and let N>=d be any positive integer.
Use its actual power-basis columns v_j, V_N=[v_0,...,v_(N-1)], W_N=V_N V_N^T, G_N=det W_N, H_(i,j)=sum_alpha alpha^(i-j), K_N=V_N^T H V_N and R_N=|disc p| G_N/N^d.
Put Delta=|disc p| and m=sum_(|alpha|>1) log|alpha|.

A. K_N is real symmetric, has rank d and zero multiplicity N-d, and its d nonzero eigenvalues sum to Nd and have absolute product |disc p| G_N.
For each expanding root lambda the Hermitian pair in the Argument accounts for lambda and 1/conjugate(lambda); all expanding roots are counted, including both members of each nonreal conjugate pair.
Writing nu for the sum of negative eigenvalue magnitudes and X=nu/N, one has

    X <= sum_(|lambda|>1) [f_N(log|lambda|)-1] <= f_N(m)-1,
    f_N(x)=sinh(Nx)/(N sinh x), with f_N(0)=1.

If K_N is positive semidefinite then R_N<=1.
Otherwise, for its number r of negative eigenvalues, 1<=r<d and

    R_N <= (X/r)^r [(d+X)/(d-r)]^(d-r) <= exp(X)(eX/r)^r.

B. For every p,N in this real domain, R_N>1 implies m>1/N.
In particular N=2d gives only the necessary m>1/(2d), even when several real or nonreal expanding pairs occur.
There is no integrality assumption, converse, positivity theorem or degree-independent conclusion in A–B.

C. Now let p in Z[t] be monic irreducible reciprocal noncyclotomic and a unit, with d>1, and keep every integer N>=d.
The power sums s_j=sum_alpha alpha^j=s_(-j) are integers, with s_0=d; the formal logarithmic-derivative identity and both exact Newton recurrences in the Argument hold at all their stated indices.
The exact rank-at-most-two Toeplitz and companion displacement identities (A)–(B) hold.
Every d-element column index set I satisfies det K_N[I,I]=det(H) det(V_N[:,I])^2, and summing those minors gives det(H)G_N.
These arithmetic constraints alone assert no determinant lower bound.

D. In C let r be the number of negative nonzero eigenvalues, nu their total magnitude, x=nu/(rN)>0 and Q_N=tr(K_N^2)/N^2.
Then 1<=r<=d-1, the exact power-sum formula (D) and product estimate (E) hold, and

    R_N>1 implies Q_N>d+25dr/[16(d-r)]>=d+25d/[16(d-1)].

At N=2d, for S(p)=sum_(j=1)^(2d-1) (2d-j)s_j^2, this implies

    8(d-1)S(p)>d^3(8d+17).

The strict antecedent R_N>1 is essential; neither moment excess nor these integer identities are a sufficient positivity test.

E. The actual cyclotomic p=t^2+t+1,N=4 has tr(K_4^2)=34>32, Delta=3,G_4=5 and R_4=15/16<1, refuting only the unrestricted basic-moment-excess inference.
The retained degree-ten Lehmer polynomial at N=d=10 has G_10=1, Delta=1332031009 and R_10<1 while satisfying the full core identities; this does not decide its different N=2d window.
No polynomial violating the necessary condition in D within the core is supplied.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:23 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All A–E with every real/positive-degree/window and integer-core quantifier, exact inverse-conjugate pairing, normalized negative sums, strict antecedents, named controls and nonimplications. |
| argument | [Argument](#argument) | Entire original main proof and full (A)–(G) supplement, including variational subadditivity, superadditivity, both-group AM–GM, Newton/displacement/minor identities, strict threshold and all actual controls. |
| dependency | [Inverse-trace and root-Gram structure](Yin_C_G0214_v1.md#statement) | Exact root-evaluation trace form, real symmetric/inertia and product identities, integral-core involution and noncyclotomic boundary at their retained scope; no finite positivity conclusion imported. |
| dependency | [Finite Gram theorem and exact controls](Yin_C_G0209_v1.md#statement) | Complete dual-Gram/root-evaluation identities, actual power-basis convention and named Lehmer discriminant/Gram controls, without a uniform or minimum-entropy conclusion. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:25 |
| status | proved |
| reason | Adopt the exact complete main-and-supplement theorem after actual whole current self-review with resolved C209/C214 interfaces; strict necessary conditions and actual controls do not become a sufficient positivity or uniform-gap conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A–E with every positive-degree/window/real and integer-core hypothesis, scaled quantities, strict antecedent and actual control limitation. |
| argument | [Argument](#argument) | Complete real negative-spectrum and full integer (A)–(G) proofs, both group-normalizations, exact displacement/minors and all actual-orbit controls. |
| dependency | [Inverse-trace and root-Gram structure](Yin_C_G0214_v1.md#statement) | Exact root-evaluation trace form, real symmetric/inertia and product identities, integral-core involution and noncyclotomic boundary at their retained scope; no finite positivity conclusion imported. |
| dependency | [Finite Gram theorem and exact controls](Yin_C_G0209_v1.md#statement) | Complete dual-Gram/root-evaluation identities, actual power-basis convention and named Lehmer discriminant/Gram controls, without a uniform or minimum-entropy conclusion. |
| review | [Actual complete spectrum/moment finding](../audits/reviews/Yin_R_G0507_v1.md#current-spectrum-moment-finding) | Actual whole current Statement and Argument at their exact scopes, with adequate self-review and no new experiment/source-audit or isolated-review claim. |

## Argument

<a id="general-reciprocal-necessary-bound"></a>
### Exact statement and inputs

Let p be a real monic squarefree reciprocal polynomial of positive degree d, with p(0)=1.
Write its roots as alpha_i.
For a positive integer N>=d, retain the power-basis orbit matrices V_N,W_N and G_N from L G0009 and set

\[
R_N=|\operatorname{disc}p|G_N/N^d,
\qquad m=\sum_{|\alpha_i|>1}\log|\alpha_i|.
\]

Then

\[
R_N>1\quad\Longrightarrow\quad m>1/N. \tag{1}
\]

The argument uses root pairing and elementary Hermitian linear algebra.
Integrality and irreducibility are not needed.
In particular the conclusion applies to the whole reciprocal-unit core of the Task, including several expanding pairs and nonreal expanding roots.
It is still degree dependent at N=2d and does not prove the hypothesis R_N>1.

For completeness, put H_ij=sum_alpha alpha^(i-j), 0<=i,j<d, and K_N=V_N^T H V_N.
Reality and reciprocal pairing make H and K_N real symmetric.
Vandermonde evaluation as in L G0009 proves that K_N has exactly d nonzero eigenvalues, their sum is Nd, and the absolute value of their product is |disc p|G_N.
These identities hold in this real-coefficient setting too; field-trace language is unnecessary.
The zero spectrum has multiplicity N-d.

### Pairing all expanding roots

For each root lambda with |lambda|>1, let ell_lambda=log|lambda| and define complex N-vectors

\[
u_j=\lambda^j,\qquad v_j=\bar\lambda^{-j},\qquad 0\le j<N.
\]

The Hermitian rank-two matrix B_lambda=u v^*+v u^* has entries

\[
(B_\lambda)_{ij}=\lambda^{i-j}+\bar\lambda^{j-i}.
\]

It accounts for exactly the roots lambda and 1/bar(lambda), not lambda and 1/lambda unless lambda is real.
The root set is closed under this pairing because p is real and reciprocal.
Summing over every expanding root, counting a nonreal conjugate pair as two roots, gives

\[
K_N=\sum_{|\lambda|>1} B_\lambda
 +\sum_{|\zeta|=1}w_\zeta w_\zeta^*,\qquad
(w_\zeta)_j=\zeta^j. \tag{2}
\]

Every root occurs exactly once in the resulting entries; the sum is real.
Since u^*v=N, the two nonzero eigenvalues of B_lambda are

\[
N\pm T_N(\ell_\lambda),\qquad
T_N(x)=\frac{\sinh(Nx)}{\sinh x}.
\]

These follow by restricting to span{u,v}, or directly from its trace and rank-two characteristic polynomial.
The vectors are independent for N>=2 and x>0.
Unit-circle terms in (2) are positive semidefinite.

For a Hermitian matrix B write nu(B) for the sum of the absolute values of its negative eigenvalues.
The elementary variational formula

\[
\nu(B)=\max_{0\le P\le I}-\operatorname{tr}(PB)
\]

shows that nu is subadditive and that adding a positive semidefinite matrix cannot increase it.
Hence

\[
\nu(K_N)\le\sum_{|\lambda|>1}\bigl(T_N(\ell_\lambda)-N\bigr).
\tag{3}
\]

To combine the expanding roots, use

\[
f_N(x)=T_N(x)/N
=\frac1N\sum_{j=0}^{N-1}e^{(N-1-2j)x}.
\]

Its Taylor series has constant coefficient 1, zero odd coefficients and nonnegative even coefficients.
Since (a+b)^(2k)>=a^(2k)+b^(2k) for a,b>=0, f_N-1 is superadditive on the nonnegative half-line.
Thus, with X=nu(K_N)/N,

\[
X\le\sum_{|\lambda|>1}\bigl(f_N(\ell_\lambda)-1\bigr)
\le f_N(m)-1. \tag{4}
\]

No separation between the phases of different expanding roots is assumed here.

### Product bound and necessary entropy

If K_N has no negative eigenvalues, its d positive eigenvalues have sum Nd.
Arithmetic--geometric mean immediately gives R_N<=1.
Otherwise let r>=1 be its number of negative eigenvalues.
Since its trace is positive, r<d.
The negative magnitudes sum to NX and the positive eigenvalues sum to N(d+X).
Apply arithmetic--geometric mean separately to these two groups:

\[
R_N\le (X/r)^r\left(\frac{d+X}{d-r}\right)^{d-r}
\le e^X(eX/r)^r. \tag{5}
\]

If 0<X<=1/4 then eX<1, so (eX/r)^r<=eX.
Consequently

\[
R_N\le Xe^{1+X}\le e^{5/4}/4<1. \tag{6}
\]

If Nm<=1, (4) instead gives

\[
X\le \frac{\sinh(Nm)}{N\sinh m}-1
\le\frac{\sinh(Nm)}{Nm}-1
\le\sinh1-1<1/4,
\]

with the value at m=0 interpreted by continuity.
Equations (5)--(6), or the positive semidefinite case, therefore imply R_N<1 or R_N<=1.
This proves (1).

### Consequence and review boundary

The necessary m>1/(2d) consequence of the candidate N=2d positivity statement is not confined to Salem numbers.
However, this calculation uses no arithmetic and therefore cannot prove that positivity statement for integral p.
The real nonintegral counterexamples in L G0009 remain valid.
The surviving research obligation is an integral orbit constraint yielding enough positive surplus; a uniform gap still needs more than this degree-dependent necessary bound.

<a id="integer-orbit-constraints"></a>
### Complement: exact integer power sums and displacement

The following supplement was authored by the separately assigned uniqueness_lehmer agent on 2026-10-06.
Its complete calculation is retained below together with the coordinating proof.


Let \(p(t)=t^d+c_1t^{d-1}+\cdots+c_d\) be monic, irreducible, reciprocal, noncyclotomic and integral, with \(d>1\); then \(c_d=1\).
Use L G0009's companion map \(A\), columns \(v_j=A^je_0\), inverse-trace matrix \(H\), \(V_N\), \(W_N\), \(C_N=HW_N\), and \(N\ge d\).
Put
\[
s_j=\operatorname{Tr}(\alpha^j)=s_{-j}\in\mathbb Z,\qquad
\mathcal K_N=V_N^{\mathsf T}HV_N=(s_{i-j})_{0\le i,j<N}.
\]
Its rank is \(d\), its nonzero spectrum agrees with that of \(C_N\), and its positive and negative inertia are those of \(H\).
The fixed L G0009 and [C209](Yin_C_G0209_v1.md#gram-lower-certificate) supply these identities, the kernel basis and determinant interpretation at their recorded review scopes.

The bounded local reuse check also searched the ledger and Den09 source units for Newton sums and Toeplitz displacement.
The following coefficient extraction is the classical Newton power-sum formula; an exact primary attribution was not established in that lookup.
It is derived directly here, used as elementary bookkeeping and not claimed novel.
A future attribution claim would require its own precise source check; no uninspected external theorem is a mathematical premise below.

### Integer moments, recurrence and displacement

The reciprocal coefficient polynomial \(q(z)=z^dp(1/z)=\prod_i(1-\alpha_i z)\) gives the formal identity
\[
-zq'(z)/q(z)=\sum_{n\ge1}s_nz^n.
\]
Coefficient comparison determines \(s_1,\ldots,s_{2d-1}\) exactly from \(p\):
\[
s_n+c_1s_{n-1}+\cdots+c_{n-1}s_1+n c_n=0\quad(1\le n\le d),
\]
\[
s_n+c_1s_{n-1}+\cdots+c_ds_{n-d}=0\quad(n>d).
\]
There is no numerical root computation in these formulas.

Let \(Z_Ne_i=e_{i+1}\) for \(i<N-1\), and \(Z_Ne_{N-1}=0\).
With \(u=(d,s_1,\ldots,s_{N-1})^{\mathsf T}\), Toeplitz cancellation gives the exact integral rank-at-most-two displacement
\[
\mathcal K_N-Z_N\mathcal K_NZ_N^{\mathsf T}
=e_0u^{\mathsf T}+ue_0^{\mathsf T}-d e_0e_0^{\mathsf T}. \tag{A}
\]
Likewise telescoping the actual companion orbit, rather than replacing it by an arbitrary matrix, gives
\[
AW_NA^{\mathsf T}-W_N=v_Nv_N^{\mathsf T}-e_0e_0^{\mathsf T},
\]
\[
(A^{\mathsf T})^{-1}C_NA^{\mathsf T}-C_N
=H(v_Nv_N^{\mathsf T}-e_0e_0^{\mathsf T}). \tag{B}
\]
Here \(A^{-1}\) is integral because the polynomial is a unit.
The second identity uses \(A^{\mathsf T}HA=H\).
These are direct consequences of the existing orbit representation; rank two alone is not a surplus theorem.

For every \(d\)-element column index set \(I\subseteq\{0,\ldots,N-1\}\), principal minors have the stronger arithmetic shape
\[
\det\mathcal K_N[I,I]=\det(H)\,\det(V_N[:,I])^2. \tag{C}
\]
Thus all nonzero maximal principal minors have the same sign and are the same signed discriminant factor times integer squares.
Summing them gives
\[
\sum_{|I|=d}\det\mathcal K_N[I,I]=\det(H)G_N,
\]
by the already used Cauchy--Binet identity.
These constraints are not satisfied by arbitrary matrices having only the same trace and inertia.
They nevertheless give no lower estimate on how large the sum of integer squares must be relative to \(N^d/\Delta\).

<a id="power-sum-rejection-gate"></a>
### An exact necessary power-sum threshold

The Toeplitz entries make the second spectral moment explicit:
\[
Q_N:=\frac{\operatorname{tr}(\mathcal K_N^2)}{N^2}
=\frac{Nd^2+2\sum_{j=1}^{N-1}(N-j)s_j^2}{N^2}. \tag{D}
\]
Suppose the nonzero spectrum has \(r\) negative and \(d-r\) positive eigenvalues.
In the core, \(1\le r\le d-1\).
Let \(\nu\) be the sum of the negative eigenvalue magnitudes and set \(x=\nu/(rN)>0\).
The positive eigenvalues sum to \(Nd+\nu\).
Arithmetic--geometric mean on the two groups gives
\[
R_N=\frac{\Delta G_N}{N^d}
\le x^r\left(\frac{d+rx}{d-r}\right)^{d-r}
\le [xe^{1+x}]^r. \tag{E}
\]
If \(x\le1/4\), then \(xe^{1+x}\le e^{5/4}/4<1\), so \(R_N>1\) requires \(x>1/4\).
Under this antecedent \(R_N>1\), applying Cauchy--Schwarz to each spectral group gives
\[
Q_N\ge r x^2+\frac{(d+rx)^2}{d-r}
>d+\frac{25dr}{16(d-r)}
\ge d+\frac{25d}{16(d-1)}. \tag{F}
\]
The strict step uses the increasing right side as a function of \(x>0\), evaluated at \(x=1/4\).
Thus a small weighted sum of integer power sums is a rigorous **rejection test** for short-window positivity.
In particular, at \(N=2d\), writing
\[
S(p)=\sum_{j=1}^{2d-1}(2d-j)s_j^2,
\]
one obtains the all-integer necessary condition
\[
R_{2d}(p)>1\quad\Longrightarrow\quad
8(d-1)S(p)>d^3(8d+17). \tag{G}
\]
Equivalently, a core polynomial with the reverse weak inequality would refute this finite sufficient-positivity mechanism, not Lehmer.
No such polynomial is supplied here.
The sharper \(r\)-dependent version in (F) is available when the inertia is independently known.

For completeness, \(\operatorname{tr}(\mathcal K_N^2)\ge N^2d\) already follows from its \(d\) nonzero real eigenvalues and trace \(Nd\); it is strict for an indefinite \(H\).
Condition (F) strengthens that basic second-moment constraint.
Its converse has not been proved.
In particular, moment excess can arise from dispersion of positive eigenvalues and does not by itself detect a large determinant.

### Actual-orbit controls and the stopping point

The limits of the constraints must be tested on actual polynomial orbits.
For the cyclotomic \(p=t^2+t+1\), \(N=4\), the power sums are \(s_0=2,s_1=s_2=-1,s_3=2\), so \(\operatorname{tr}\mathcal K_4^2=34>32=N^2d\), while the retained exact values \(\Delta=3,G_4=5\) give \(R_4=15/16<1\).
This is only a counterexample to treating basic second-moment excess as sufficient; its form is positive definite, so it is not a core counterexample or a test of (F)'s converse in the core.

Inside the integral irreducible noncyclotomic core, the retained Lehmer polynomial at \(N=d=10\) satisfies \(G_{10}=1\) and \(\Delta=1332031009<10^{10}\).
All exact Newton, displacement and principal-minor identities above apply, and the form is indefinite, yet \(R_d<1\).
Consequently these full orbit constraints do not force positivity at every \(N\ge d\).
This does not settle the distinguished \(N=2d\) question, where L G0004 gives positivity for the same polynomial.

The new useful output of this bounded test is (G), together with the exact constraints (A)--(D).
They retain arithmetic and the actual orbit but yield only a necessary screen.
No inequality controlling the maximal-minor square sum from below by an exponential surplus was obtained.
Neither this screen nor universal short-window positivity has been shown equivalent to the original Lehmer objective.
The preceding total-negative-spectrum argument supplies the complementary m>1/N consequence and has its own actual review scope above.
