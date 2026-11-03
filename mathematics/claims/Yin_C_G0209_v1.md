---
author: Yin
---

# Finite orbit Gram certificates, determinant ratios and their exact boundary costs

The complete original local arguments and finite failure boundaries are retained from [L4](../ledger/Yin_L_G0004_v1.md), dated 2026-10-06.
The original programs and exact outputs have their native home in [J114](../computations/programs/Yin_J_G0114/readme.md).
This is material organization; it supplies no new research run or uniform Mahler-gap conclusion.

## Statement

Let p be a monic squarefree polynomial in Z[t] of degree d>=1 with p(0) nonzero, let v_j be the coefficient column of t^j modulo p in the actual power basis, and put V_N=[v_0,...,v_(N-1)], W_N=V_NV_N^T, G_N=det W_N and Delta=|disc p| for every integer N>=d.
Use the full unnormalized logarithmic measure m(p)=log M(p), with all roots counted.

A. G_N is a positive integer and equals D_(N-d), where D_k is the Gram determinant of the complete integral kernel basis p,tp,...,t^(k-1)p and D_0=1.
The root-evaluation matrix E_N=(alpha_i^j) has

    Delta G_N=det(E_NE_N*)<=N^d M(p)^(2(N-1)).

For N>1 this gives B_N=[log(Delta G_N)-d log N]/[2(N-1)]<=m(p).
For integers a>1 and b>0, (Delta G_N)^b>=N^(bd) a^(N-1) is sufficient for m(p)>=log(a)/(2b).
The stronger fixed log(2)/8 test is the case a=2,b=4; a bare positive integer surplus is not a uniform positive measure bound.

B. For every k>=1, r_k=D_k/D_(k-1)>1, the r_k decrease to M(p)^2, and B_N tends to m(p) for each fixed p.
Thus m(p)<=log(r_k)/2: a finite residual is an upper bound, while B_N is the distinct lower certificate with its full dimension penalty.
For p=t-1, D_k=k+1 and r_k=(k+1)/k, so these strict finite increments coexist with zero entropy.
No degree-uniform certification window is supplied.

C. If q in Z[t] is monic squarefree of degree e>=1 with |q(0)|=1, r>=1 and L>=e are integers, p(t)=q(t^r) and d=re, then

    G_(rL)(p)=G_L(q)^r,
    |disc p|=r^d |disc q|^r,
    log(Delta_p G_(rL))-d log(rL)=r[log(Delta_q G_L)-e log L].

No irreducibility of q(t^r) is asserted.
For a prime ell, p=Phi_ell and every positive multiple N of ell, Delta G_N=N^d exactly.

D. For the actual original degree-ten Lehmer polynomial t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1, the retained exact certificate gives Delta=1332031009, G20=79461 and G40=18006972477.
The positivity test holds at N=20, while the stronger fixed log(2)/8 sufficient test fails there and holds at N=40.
Hence the proposed universal stronger test at N=2d is false; this does not refute the finite inequality or assert a value for the full capacity, a uniform positivity theorem or an entropy upper bound from the failed test.
The finite-field and trace-polynomial criteria used to certify the bounded examples are the exact sufficient criteria proved in the Argument; failed sufficient tests leave cases unclassified.

The root-evaluation equality and Hadamard bound also apply to a monic squarefree real polynomial with nonzero constant term, with its real companion and Delta=|disc p|; only the integral-lattice and positive-integer assertions require integer coefficients.
No determinant is identified with a binary-trajectory cardinality.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:19 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All A–D with the explicit monic/squarefree/integer, finite-window and dilation hypotheses, the named original-input certificate and the stated real-coefficient equality/bound boundary. |
| argument | [Argument](#argument) | Complete original Sections2–5, sufficient finite-field/trace proof, fixed-input limiting consequence and named historical native evidence, with all degree and source limitations. |
| dependency | [Den09 Toeplitz interface](../audits/literature/Den09/Yin_U002.md#den09-u002) | Only the retained nonnegative-symbol classical determinant limit, positive finite sections and Schur-complement interface; original Szego proof uninspected. |
| support | [Rational entropy formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Existing total-entropy interpretation with full characteristic polynomial and no division by degree, at the accepted source depth. |
| support | [Lattice entropy interface](../audits/literature/DGB16/Yin_U001.md#dgb16-u001) | Recorded integer-flow/rationalization interpretation only; the finite Mahler inequality is proved locally. |
| support | [Original exact native evidence](../computations/programs/Yin_J_G0114/readme.md) | The named Lehmer values and bounded sufficient-certificate outcomes retain their original executions, programs, complete JSON and nonuniform limits; no fresh run is claimed. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:26 |
| status | proved |
| reason | Adopt the actual current statement and complete retained argument with its resolved exact inputs and sufficient constructor self-review. Original targeted findings retain their own historical scopes; no new research execution, independent certification or unrestricted gap follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete exact A–D, finite-dimensional and fixed-input limit proofs, all native/source boundaries and the explicit real-coefficient extension; adequate current self-review, without a new independent or native-execution claim. |
| argument | [Argument](#argument) | Complete physically retained proof and all required local deductions, with the exact domains, source depths and limitations in the Statement. |
| dependency | [Den09 Toeplitz interface](../audits/literature/Den09/Yin_U002.md#den09-u002) | Only the retained nonnegative-symbol classical determinant limit, positive finite sections and Schur-complement interface; original Szego proof uninspected. |
| support | [Rational entropy formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Existing total-entropy interpretation with full characteristic polynomial and no division by degree, at the accepted source depth. |
| support | [Lattice entropy interface](../audits/literature/DGB16/Yin_U001.md#dgb16-u001) | Recorded integer-flow/rationalization interpretation only; the finite Mahler inequality is proved locally. |
| support | [Original exact native evidence](../computations/programs/Yin_J_G0114/readme.md) | The named Lehmer values and bounded sufficient-certificate outcomes retain their original executions, programs, complete JSON and nonuniform limits; no fresh run is claimed. |
| review | [Actual complete current finding](../audits/reviews/Yin_R_G0502_v1.md#orbit-gram-current-finding) | Complete exact A–D, finite-dimensional and fixed-input limit proofs, all native/source boundaries and the explicit real-coefficient extension; adequate current self-review, without a new independent or native-execution claim. |

## Argument

### 2. Orbit matrix and its exact integer relation lattice

The next calculations hold more generally for every **monic squarefree** \(p\in\mathbb Z[t]\) of degree \(d\ge1\), with \(p(0)\ne0\).
Unit and reciprocity are needed for the target family, not for these identities.
Put
\[
v_j=t^j\bmod p\in\mathbb Z^d,\qquad
V_N=[v_0\;v_1\;\cdots\;v_{N-1}],\quad N\ge d,
\]
\[
W_N=V_NV_N^{\mathsf T},\qquad G_N=\det W_N\in\mathbb Z_{>0},
\qquad \Delta=|\operatorname{disc}p|\in\mathbb Z_{>0}.
\]
The first \(d\) columns of \(V_N\) are the identity.
In particular this is a primitive quotient map of integer lattices.
It is not the cardinality of a binary-digit trajectory.

Write \(k=N-d\).
The kernel of \(V_N:\mathbb Z^N\to\mathbb Z^d\) has the basis consisting of the coefficient vectors of
\[
p,tp,\ldots,t^{k-1}p.
\]
Indeed monic polynomial division gives an integral quotient for every polynomial divisible by \(p\); degree bounds give exactly those shifts.
Let \(K_k\) be the \(N\times k\) matrix of these columns.
The bottom \(k\times k\) block is triangular with diagonal 1, so this is a saturated integral kernel, not a finite-index substitute.

The **finite dual Gram identity** is
\[
G_N=\det(K_k^{\mathsf T}K_k)=:D_k,\qquad D_0=1. \tag{1}
\]
For a direct verification write \(V_N=[I_d\ B]\).
A standard kernel basis is \(K_0=[-B;I_k]\), so
\(\det(K_0^{\mathsf T}K_0)=\det(I_k+B^{\mathsf T}B)=\det(I_d+BB^{\mathsf T})\).
The actual polynomial-shift basis differs by an integral unimodular matrix, by the triangular block above; its Gram determinant is unchanged.
This proves (1) without a lattice covolume theorem.

Thus the trajectory's integer recurrence and an integer Toeplitz determinant encode exactly the same finite object.
If \(p(t)=\sum_{j=0}^d a_jt^j\), then
\[
(K_k^{\mathsf T}K_k)_{ij}=\sum_\ell a_\ell a_{\ell+i-j},
\]
where missing coefficients are zero.
This is the Toeplitz section for \(|p(e^{it})|^2\), including when \(p\) has unit-circle zeros.

<a id="gram-lower-certificate"></a>
### 3. A finite integer lower certificate, with its full dimension cost

Let \(\alpha_1,\ldots,\alpha_d\) be the distinct roots of \(p\), and let
\(E=(\alpha_i^j)_{i=1,\ldots,d;\ j=0,\ldots,d-1}\).
Then \(EV_N=(\alpha_i^j)_{i;\ j=0,\ldots,N-1}\), because reduction modulo \(p\) preserves evaluation at its roots.
Taking Hermitian Gram determinants gives
\[
\Delta G_N
=\det\bigl((EV_N)(EV_N)^*\bigr)
\le \prod_{i=1}^d\sum_{j=0}^{N-1}|\alpha_i|^{2j}
\le N^d M(p)^{2(N-1)}. \tag{2}
\]
Here the first equality uses \(|\det E|^2=\Delta\), the first inequality is Hadamard, and the second bounds each finite geometric sum by \(N\max(1,|\alpha_i|)^{2(N-1)}\).
Every conjugate, including contracting and unit-circle conjugates, is retained.
Repeated roots are excluded because the Vandermonde determinant would vanish.

Consequently, for \(N\ge d\) and \(N>1\),
\[
h_{\rm alg}(A)=m(p)
\ge B_N(p):=
\frac{\log(\Delta G_N)-d\log N}{2(N-1)}. \tag{3}
\]
At \(N=d\), this is exactly the known discriminant lower estimate.
At longer windows \(G_N\) adds genuine orbit information.
A negative value is merely vacuous; taking its positive part is valid since \(m(p)\ge0\).

In particular, the following checks use **only positive integers**, not approximated algebraic roots:

- \(\Delta G_N>N^d\) certifies strictly positive entropy.
- \((\Delta G_N)^4\ge N^{4d}2^{N-1}\) certifies \(m(p)\ge(\log2)/8\).
- More generally, \((\Delta G_N)^b\ge N^{bd}a^{N-1}\), with integers \(a>1,b>0\), certifies \(m(p)\ge(\log a)/(2b)\).

These are sufficient finite tests.
They do not assert that a fixed threshold is met for every noncyclotomic \(p\).
The subtraction \(d\log N\) is indispensable.

### 4. What finite increments can and cannot say

By Den09's retained Toeplitz limit,
\[
\lim_{k\to\infty}D_k^{1/k}=M(p)^2.
\]
The Schur-complement residual interpretation also gives
\[
r_k:=D_k/D_{k-1}\quad\text{nonincreasing in }k,
\qquad r_k\longrightarrow M(p)^2. \tag{4}
\]
To check monotonicity, the residual norm of \(t^{k-1}p\) after projection on \(p,tp,\ldots,t^{k-2}p\) equals \(r_k\).
Multiplication by \(t^{-1}\) is an isometry on the coefficient Hilbert space.
The corresponding residual at the next step has an additional predecessor available for projection, so cannot increase.
The limit follows by taking the geometric mean of the positive decreasing ratios and applying the retained Toeplitz limit.

For a nonconstant **monic** polynomial with nonzero constant coefficient, in fact \(r_k>1\): the residual is \(p(t)q(t)\), where \(q\) is monic of degree \(k-1\); this product is monic, so its squared coefficient norm is at least 1.
Equality would make it the monomial \(t^{k+d-1}\), impossible since \(p\) has a nonzero root.
Because \(D_k\) are integers, \(D_k\ge D_{k-1}+1\).
Yet these facts alone imply no positive limiting entropy.
They hold, for example, for \(p=t-1\), where \(D_k=k+1\), \(r_k=(k+1)/k>1\), and entropy is zero.

Thus a finite residual supplies an **upper** estimate
\(m(p)\le\tfrac12\log r_k\), not a lower estimate.
Formula (3) is the complementary lower estimate, bought by the explicit discriminant/dimension boundary term.
The interval is a finite certificate for an individual polynomial, not a degree-uniform theorem.

The even coarser subgroup-index candidate fails already on the exact hard core.
The subgroup generated by \(v_0,\ldots,v_{N-1}\) is all of \(\mathbb Z^d\) as soon as \(N\ge d\), so every subsequent index is 1, including for \(p=t^2-3t+1\) with positive entropy.
Passing from finite sets to their generated subgroups destroys the needed metric information.

Nor can \(G_N^{1/2}\) be substituted for a binary trajectory cardinality.
For \(p=t^2-at+1\), \(N=3\), one has \(G_3=a^2+2\), while \(T_3(A,\{0,v_0\})\) has at most 8 elements.
Taking \(a=8\) already gives \(\sqrt{G_3}>8\).
This is a reciprocal irreducible unit example.
A comparison to digit counts needs an additional quantization or boundary argument and a declared digit set.

<a id="degree-window-tests"></a>
### 5. Degree-scale candidate and controls

The tested strong short-window candidate is: **every irreducible reciprocal noncyclotomic unit polynomial passes the \((\log2)/8\) certificate at \(N=2d\)**.
The retained exact Lehmer polynomial fails this integer test at \(N=20\), although it passes the weaker positivity test there and passes the \((\log2)/8\) test at \(N=40\).
Thus that universal fixed-threshold, fixed-window sufficient mechanism is false; this is not a refutation of (2), or a proof that the polynomial's true entropy is below the threshold.

The weaker candidate \(\Delta G_{2d}>(2d)^d\) survives the first named samples and is investigated separately below.
Even if it held throughout the core, the minimum integer surplus would give only \(\log(1+(2d)^{-d})/[2(2d-1)]\), which tends to zero.
A uniform gap requires an exponential surplus, not merely a strict integer inequality.

The diagnostic is compatible with time dilation.
If \(q\) is monic squarefree with constant coefficient of modulus one, \(p(t)=q(t^r)\), \(d=r\deg q\), and \(N=rL\), then direct separation into exponent residue classes gives
\[
G_{rL}(q(t^r))=G_L(q)^r,\qquad
|\operatorname{disc}(q(t^r))|=r^d|\operatorname{disc}q|^r,
\]
and therefore
\[
\log(\Delta_pG_{rL})-d\log(rL)
=r\bigl[\log(\Delta_qG_L)-(\deg q)\log L\bigr]. \tag{5}
\]
The Gram identity follows by permuting the orbit coordinates into \(r\) identical blocks.
For the discriminant identity use \(p'(\alpha)=r\alpha^{r-1}q'(\alpha^r)\) and take the product over all roots; unit constant terms remove the absolute-value factor \(\prod|\alpha|^{r-1}\).
No irreducibility of \(q(t^r)\) is asserted.
The \(r^d\) term precisely cancels the added \(d\log r\) boundary penalty.
Thus this normalization does not spuriously divide entropy by the dilation factor.

Cyclotomic controls are sharper.
For \(p=\Phi_\ell\) with \(\ell\) prime and \(N\) a positive multiple of \(\ell\), the rows \((1,\alpha_i,\ldots,\alpha_i^{N-1})\) are pairwise orthogonal and each has squared norm \(N\).
Hence \(\Delta G_N=N^d\) exactly, so (3) returns zero, not a false positive.
For other cyclotomic windows it remains nonpositive by (2).

The nonunit family \(t^d-2\) still has entropy \(\log2\), despite its house approaching one; (2) applies because the polynomial is monic squarefree.
The nonintegral \(2t-1\) is outside this lattice model and requires GBV15's leading-coefficient term.
Weighted semisimple length countermodels have no integral companion-polynomial norm/discriminant data, so this argument is not being applied to their arbitrary weights.
Infinite direct sums of zero-entropy flows are also outside this single finite-rank orbit calculation; nothing here claims their whole group has finite rank.

### Fixed-input limiting consequence

The retained Toeplitz limit gives log G_N=(N-d)[2m(p)+o(1)] for each fixed p.
Since d is fixed and log(Delta)-d log N=o(N), the displayed B_N tends to m(p).
Every threshold strictly below that particular positive measure is therefore eventually certified, without a degree-uniform bound on the first successful window.

### 8. Exact bounded reciprocal probe

This extension tests all monic reciprocal degree \(d\in\{2,4,6,8,10,12\}\) polynomials with constant coefficient 1 and each independent remaining coefficient in \(\{-1,0,1\}\).
It first seeks a finite-field irreducibility certificate among the primes listed in the code.
A successful modular certificate proves rational irreducibility; failure to find one does **not** prove reducibility and those cases remain outside the certified sample.
Cyclotomic polynomials are removed by exact equality against the finite list of orders with \(\varphi(n)=d\).
For \(d\le12\), it suffices to list \(n\le288\), using \(\varphi(n)\ge\sqrt{n/2}\).
The latter follows prime-power by prime-power from \(\varphi(n)^2/n=\prod_{p^a\parallel n}p^{a-2}(p-1)^2\), whose only factor below 1 is the single possible factor \(1/2\) at \(p=2,a=1\).

The precise finite outcome is the number of certified noncyclotomic irreducible polynomials, any failed \(N=2d\) positivity tests, and failures of the fixed \((\log2)/8\) threshold.
The latter test is stronger and has already failed for Lehmer, so its failure count is a diagnostic, not a new counterexample to the main Task.
All arithmetic below is exact.

### 9. Trace-polynomial completion of the bounded probe

The first modular filter can systematically miss irreducible reciprocal polynomials: the Lehmer discriminant is \(36497^2\), and its degree-ten polynomial had no successful certificate in the listed primes.
An even-degree irreducible polynomial with square discriminant cannot have a full-cycle Frobenius at an unramified prime, so extending only that prime list does not solve the coverage problem.

For \(d=2m\), form the integral monic trace polynomial
\[
p(t)=t^m Q(t+t^{-1}),\qquad
Q(x)=a_m+\sum_{j=1}^m a_{m+j}S_j(x),\quad
S_0=2,\ S_1=x,\ S_j=xS_{j-1}-S_{j-2}.
\]
If \(Q\) is irreducible over \(\mathbb Q\) and has a real root in \((-2,2)\), then \(p\) is irreducible: under the associated real embedding, \(u^2-4<0\), so \(u^2-4\) cannot be a square in \(\mathbb Q(u)\); adjoining a root of \(t^2-ut+1\) doubles the degree.
Total reality of every root of \(Q\) is not required.
The finite probe below certifies \(Q\)'s irreducibility by the same finite-field test and its interior real root by exact signs on the rational grid \(a/4\), \(-8\le a\le8\).
Failure of that sufficient test still leaves an unresolved case, not a claim of reducibility.

The finite-field test used in both blocks is the standard exact criterion: a monic degree-\(d\) polynomial is irreducible over \(\mathbb F_q\) iff it divides \(t^{q^d}-t\) and is relatively prime to \(t^{q^{d/\ell}}-t\) for every prime divisor \(\ell\) of \(d\).
The first condition forces all irreducible factor degrees to divide \(d\), with no repetitions; any proper divisor then divides \(d/\ell\) for some such \(\ell\).
This is an elementary finite-field input, not an empirical irreducibility heuristic.

### Named exact evidence and coefficient-domain boundary

The complete three native programs and their original exact outputs are retained in J_G0114.
The first output supplies the stated Lehmer discriminant and both Gram values; its integer comparisons distinguish positivity from the stronger fixed threshold.
The third output supplies the actual trace-polynomial certificate with coefficients [3,4,-5,-5,1,1], its finite-field prime 2 and the exact real bracket [-2,-7/4].
The preceding trace argument certifies irreducibility, while p(1)=-1 and a positive root above 1 exclude cyclotomy; no numerical root approximation is required.
The finite enumeration and its 477 unclassified cases remain bounded native evidence, not an all-degree theorem.

For real coefficients, the first d power-remainder columns still form I_d and W_N is positive definite.
The same evaluation identity E V_N=E_N and |det E|^2=|disc p| prove the root Gram equality and Hadamard estimate without integrality.
No integer kernel saturation, integral discriminant or arithmetic surplus is inferred in that real domain.
The original selected external source proofs are reused at their recorded depths; no source PDF, original Szego proof or native program was newly executed or audited during this retention.
