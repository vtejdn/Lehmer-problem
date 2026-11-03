---
author: Yin
---

# Complete Littlewood support bounds and quantified fixed trace-constant exclusion

This retains the complete necessary mathematical argument from [Entire original fixed-constant account](../ledger/Yin_L_G0373_v1.md#fixed-constant-littlewood-source).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P be an actual monic irreducible reciprocal nontorsion integer unit polynomial of degree d=2s, alpha an actual root, tau=alpha+alpha^-1, K=Q(alpha), F=Q(tau), O=Z[alpha] and B_trace=Z[tau].
Let u be an actual O-unit with unique integral degree-below-s relative-norm representative C_u(x)=-B+sum_(l=1)^(s-1)b_l C_l(x), where integer B>=1, b_l are integers, and C_l(t+t^-1)=t^l+t^-l.
Use the same original residual window, common q, actual monomial and u residuals and nonnegative original weights as the complete C397 theorem, and assume that every original lag at least s cancels.
Then the full actual square-sum circle symbol is G(t)=1-theta+theta C_u(t+t^-1)>=0, its mean E=1-theta(1+B)>0 and its signed lags are H_l=theta b_l.
Assume the true surplus target E<=1/2; no converse from a formal nonnegative symbol to actual unit or residual realization is asserted.

The mass lies in 1/[2(1+B)]<=theta<1/(1+B), and strict Fourier rounding gives |b_l|<=B.
The full integer Laurent polynomial f=(1+B)+sum_l b_l(t^l+t^-l) is nonnegative, with normalized Haar mean and full L1 norm1+B.
For S={l:1<=l<s,b_l!=0}, K_supp=|S| and N_supp=2K_supp+1, its actual signed Fourier support consists of zero and both signs of each such l.
The accepted own JKS v2 Theorem1.1(i), at distinct ordered real frequencies lambda_r with arbitrary complex coefficients a_r, bounds their long-interval mean by (1/26)sum_(r=1)^N |a_r|/(r+1); for integer frequencies this is the normalized single-period L1 norm.
Applied to all actual integer coefficients of f, it gives 2K_supp+2<=exp[52(1+B)], including empty S and arbitrary gaps or coefficient signs.
This uses no integral spectral factorization or bound on the original residual window.

If k>0 original roots lie on the unit circle, include all of them once as z_1,...,z_k and set delta_circ=max_(1<=l<s)|k^-1 sum_i z_i^l|.
In this nontorsion reciprocal domain, k>0 ensures s>=2; a degree-two all-circle integer trace would be -1,0 or1 and give torsion.
Actual unit positivity at each such embedding implies 0<-B+2sum_(l in S)b_l Re(k^-1 sum_i z_i^l)<=-B+2B K_supp delta_circ.
Thus delta_circ=0 is impossible and K_supp>1/(2delta_circ), so B>(1/52)log(2+1/delta_circ)-1 and delta_circ>1/[exp[52(1+B)]-2].
For every fixed real B_0>=1, all integer 1<=B<=B_0 are therefore excluded whenever delta_circ<=delta_0(B_0)=1/[exp[52(1+B_0)]-2], including the zero-discrepancy case without division.
These are uniform necessary conditions over actual units and original weights in this exact family, not existence statements above the threshold.

Put m=m(P)=log M(P)>0, retain c_0=log2/4, h_0=c_0 exp(-20), b(h)=max{h,sqrt(h/c_0)log sqrt(c_0/h)} and epsilon(h)=min{1,15sqrt(b(h))+4h} on 0<h<=h_0 from the exact accepted original-angular interface.
If m/2<=h_0 and k>0, applying that interface for every1<=l<s and subtracting all d-k other angular labels gives delta_circ<=min{1,[d epsilon(m/2)+(d-k)]/k}.
Hence along every hypothetical target-realizing reciprocal sequence with m->0 and k/d->1, B must tend to infinity; small total measure alone does not establish circle density for general reciprocal inputs.
For genuine Salem inputs d>=4, k=d-2, the bound is min{1,[d epsilon(m/2)+2]/(d-2)}.
Finite-degree coefficient bounds |p_j|<=binom(d,j)M(P) show that any hypothetical Salem m->0 sequence has d->infinity, and consequently B->infinity for actual realizations in the named family.
Equivalently, for each fixed B_0>=1 there exists mu(B_0)>0 such that no genuine Salem input with 0<m(P)<mu(B_0) has this actual residual realization, E<=1/2 and 1<=B<=B_0.
The complete proof constructs the quantifiers by D_0>=4 with 2/(D_0-2)<=delta_0/2, m_*/2<=h_0 with epsilon(m_*/2)<=delta_0/4, and the positive finite-degree lower measure for d<D_0 and M<2 (or log2 if empty); no numerical value or enumeration is claimed.

If the reduced support is empty, the actual trace-order unit c=-B has (-B)^s=Norm_K(u)=+1 or-1 and therefore B=1.
The actual no-circle quadratic P=t^2-3t+1, u=alpha-1, u^-1=alpha-2, c=-1 is a fixed-positive-measure relative-norm control; the circle-positivity argument is unavailable when k=0.
There is no upper bound for the original unbounded B, unit coefficients, energy or degree, and no actual lift or covariance realization is constructed.
N_supp is distinct from the original residual window N_window, whose T=N_window-1, common q, all contents, all d resultant factors, complete signed norms and integer multiplicity parity remain fully paid.
Real weights have no invented integer copies; rational weight denominators and their copies remain charged, and the radial expense is Tm(P)/d.
The JKS source is the actual arXiv:2303.10919v2,24July2023, retained under the canonical 2024 publication key, accepted only at its own theorem statement/applicability scope.
No inaccessible original MPS proof, all-ones-only substitute, uninspected journal equivalence, current-best constant, original-source proof re-audit, actual all-input construction or unrestricted Mahler gap is adopted.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:18 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Complete actual one-unit domain](Yin_C_G0397_v1.md#one-unit-low-lag-symbol-screen) | Only actual order/unit, original residual, full signed norm and exact degree-below-s forced-symbol interface, not a converse realization. |
| dependency | [Strict original Fourier rounding](Yin_C_G0403_v1.md#strict-integral-coefficient-bound) | Only strict nonzero-mode coefficient bound, integer basis and actual constant/no-circle unit branch; the whole root-lattice classification is not needed. |
| dependency | [Complete original angular statement](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Actual powered labels and multiplicities, increasing epsilon and its exact positive small-height domain; original Pri11/Dim19 proof depth unchanged. |
| dependency | [Exact accepted primary Littlewood theorem](../audits/literature/JKS24/Yin_U001.md#jks24-u001) | Own v2 Theorem1.1(i), all distinct ordered real frequencies/arbitrary complex coefficients and the exact integer-period normalization on pp.3–4; original proof unaudited and no journal-version equivalence. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:19 |
| status | proved |
| reason | Adopt the actual complete SELF finding after checking every exact primary-statement hypothesis, full original proof, signed support/strict discrepancy chain, complete finite-degree quantifiers and original realization/cost boundaries. All original dates, source-reading occurrences and known SELF review history remain separate; no new computation, source-proof audit or unrestricted gap is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0397_v1.md#one-unit-low-lag-symbol-screen) | Only actual order/unit, original residual, full signed norm and exact degree-below-s forced-symbol interface, not a converse realization. |
| dependency | [Exact accepted input](Yin_C_G0403_v1.md#strict-integral-coefficient-bound) | Only strict nonzero-mode coefficient bound, integer basis and actual constant/no-circle unit branch; the whole root-lattice classification is not needed. |
| dependency | [Exact accepted input](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Actual powered labels and multiplicities, increasing epsilon and its exact positive small-height domain; original Pri11/Dim19 proof depth unchanged. |
| dependency | [Exact accepted input](../audits/literature/JKS24/Yin_U001.md#jks24-u001) | Own v2 Theorem1.1(i), all distinct ordered real frequencies/arbitrary complex coefficients and the exact integer-period normalization on pp.3–4; original proof unaudited and no journal-version equivalence. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0612_v1.md#current-fixed-constant-whole-finding) | Entire precise current Statement and complete necessary original mathematical argument with all source, actual-domain, denominator, angular-label, strictness, finite-degree and original-expense limits. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="fixed-constant-littlewood-source"></a>
## 1. Checked primary input and exact acceptance boundary

The bounded local reuse search for McGehee/Pigno, Littlewood exponential norms and the precise support mechanism found no matching G input; unrelated Littlewood and Littlewood--Offord records do not supply it.
Root supplied the intended classical Littlewood scout.
The source search identified McGehee--Pigno--Smith's original Annals paper, *Hardy's inequality and the L1 norm of exponential sums*, 113(3) (1981), 613--618, DOI10.2307/2007000; its [primary publisher record](https://annals.math.princeton.edu/1981/113-3/p09) was read.
Original full-paper access failed.
An institutional Pigno collection indexed the original authors' Bulletin corollary for arbitrary complex coefficients of modulus at least one; direct collection download ended in an EOF transport error.
The accessible Konyagin primary abstract states only the all-ones version, which alone is insufficient here.
Neither inaccessible original proof nor a search excerpt is adopted as the mathematical premise.

A directly readable primary replacement is Philippe Jaming, Karim Kellay and Chadi Saba, *The Littlewood problem and non-harmonic Fourier series*, arXiv:2303.10919v2,24July2023,25pages, related published DOI10.1007/s00208-023-02692-w.
The [primary arXiv PDF](https://arxiv.org/pdf/2303.10919) explicitly identifies v2 in its first-page header; the [primary record](https://arxiv.org/abs/2303.10919) confirms that version/date.
Its OWN Theorem1.1(i), printed/PDFp.3, gives for distinct increasing real lambda_1,...,lambda_N and arbitrary complex a_1,...,a_N

    lim_(L->infinity) (1/L) integral_(-L/2)^(L/2)
       |sum_(r=1)^N a_r exp(2pi i lambda_r t)| dt
          >= (1/26) sum_(r=1)^N |a_r|/(r+1).       (1)

Printed/PDFp.4 explicitly identifies the left side with the normalized single-period L1 norm when all lambda_r are integers.
For a continuous periodic function this also follows directly by splitting into complete periods and a uniformly bounded remaining interval.
The complete statement, the frequency/coefficient hypotheses and this periodic specialization were directly text-read.
Screenshot calls supplied no inspectable image here, so no visual audit is claimed.
The original proof of Theorem1.1 was not independently audited.
This ordinary established primary theorem is accepted for the exact statement/interface above under the accepted-external-input rule.
The allocation-era unresolved premise is thereby resolved at statement/applicability scope; canonical registration and a reusable source-unit locator are coordinated by root.

TheoremB on p.2 separately reports the classical MPS weighted inequality.
It supplies attribution context only; the current proof uses the authors' own Theorem1.1(i), with its conservative explicit constant.
No optimal-constant, first-priority or current-best-bound claim is made.
Theorem1.1(ii)'s sharper logarithmic constant is unnecessary and is not used.

<a id="fixed-constant-integer-symbol"></a>
## 2. General integer-mean symbol and the support upper bound

Use exactly L367's actual one-unit-plus-all-monomials family: P is monic irreducible reciprocal nontorsion in Z[t], degree d=2s; alpha is its class, tau=alpha+alpha^-1, K=Q(alpha), F=Q(tau), O=Z[alpha] and B_trace=Z[tau].
The actual order unit u has a unique reduced relative-norm representative C_u of degree below s.
To avoid confusing the trace order with the following integer, denote the NEGATIVE REDUCED CONSTANT by B=-b>=1.
Write

    C_u(x)=-B+sum_(l=1)^(s-1) b_l C_l(x),
    C_l(t+t^-1)=t^l+t^-l, b_l in Z,
    G(t)=1-theta+theta C_u(t+t^-1)>=0 on |t|=1,
    E=1-theta(1+B)>0, H_l=theta b_l.                (2)

These are consequences of actual cancellation of ALL lags at least s in the common original residual window.
They are not independent formal assignments.
The true surplus target is E<=1/2.
Hence

    1/[2(1+B)]<=theta<1/(1+B),
    0<E/theta=1/theta-(1+B)<=1+B.

The strict Fourier bound in L370 yields |b_l|<1+B, so integer b_l obey |b_l|<=B.
Moreover adding the nonnegative constant 2(1+B)-1/theta to G/theta gives

    f(t)=(1+B)+sum_(l=1)^(s-1) b_l(t^l+t^-l)>=0,
    integral f dmu=||f||_1=1+B,                    (3)

where dmu is normalized Haar measure on the circle.
This is the exact general-mean nonnegative symbol implied by the true target, not a stronger actual-realization converse.

Let S={l:1<=l<s,b_l!=0}, K_supp=|S|.
The ACTUAL Fourier support of f has N=2K_supp+1 distinct integer exponents, including zero.
Its nonzero coefficients are integers of modulus at least one; the constant is the integer 1+B.
Apply (1) to these actual exponents in increasing order, with their signed coefficients.
The periodic specialization and (3) give

    1+B >= (1/26) sum_(r=1)^N 1/(r+1)
        >= (1/52) sum_(r=1)^N 1/r
        >= (1/52) log(N+1).

The middle inequality follows from r+1<=2r; the last follows by integrating 1/x over [1,N+1].
Consequently

    2K_supp+2<=exp[52(1+B)],
    K_supp<=[exp[52(1+B)]-2]/2.                    (4)

Every finite symbol in (3) satisfies (4), including K_supp=0.
Negative Fourier coefficients, nonconsecutive frequencies, arbitrary trace degree and large integer coefficients introduce no omitted hypothesis.
No sum of moduli or separate positive-frequency polynomial replaces the nonnegative full f.
Positivity is precisely what identifies its entire L1 norm with the mean.
Integral Fejer--Riesz factorization, a bound for the ACTUAL residual degree or a general root-lattice classification is not used.

<a id="fixed-constant-circle-discrepancy"></a>
## 3. Original-circle positivity forces support and constant growth

Suppose P has k>0 ORIGINAL circle conjugates z_1,...,z_k, with every such conjugate included once.
For 1<=l<s put

    mu_l=(1/k) sum_(i=1)^k z_i^l,
    delta_circ=max_(1<=l<s) |mu_l|<=1.             (5)

At each original circle embedding, the ACTUAL order unit has nonzero u_i and u_i sigma(u_i)=|u_i|^2>0.
Evaluating its actual reduced representative there and averaging gives

    0<(1/k)sum_(i=1)^k |u_i|^2
      =-B+2sum_(l in S) b_l Re(mu_l)
      <=-B+2 delta_circ sum_(l in S)|b_l|
      <=-B+2B K_supp delta_circ.                  (6)

All powers have l<s, and the original roots, not a selected powered minimal polynomial, define this average.
In particular delta_circ=0 is impossible; for delta_circ>0,

    K_supp>1/(2delta_circ).

Combining with (4) yields the complete necessary inequality

    B>(1/52)log(2+1/delta_circ)-1,
    delta_circ>1/[exp[52(1+B)]-2].                (7)

The inequalities are strict because each actual circle unit value is positive.
Thus for any fixed real B_0>=1, this original family with integer 1<=B<=B_0 cannot realize the true target whenever

    delta_circ<=delta_0(B_0)
       :=1/[exp[52(1+B_0)]-2].                   (8)

This includes delta_circ=0 without division.
It is a discrepancy-conditional exclusion, independent of which actual unit and nonnegative original weights were proposed.
It does not establish that a unit or residual realization exists above the threshold.
The count K_supp refers to nonzero REDUCED Fourier coefficients of C_u; it is not the number of original monomial residuals or integer copies.

<a id="fixed-constant-salem-near-one"></a>
## 4. Near-one specialization with all original angular labels

Let m=m(P)=log M(P)>0.
When m/2<=h_0, L229 applies at each integer 1<=l<s with h_l=lm/d<m/2.
Its increasing epsilon gives the full original angular moments

    |a_l|=|d^-1 sum_(i=1)^d (alpha_i/|alpha_i|)^l|
        <=epsilon(m/2).

For a reciprocal input having k>0 original circle roots, subtract the d-k remaining unit-modulus angular labels and divide by k.
This gives

    delta_circ<=min{1,[d epsilon(m/2)+(d-k)]/k}.    (9)

No sign or actual-circle positivity is assigned to those off-circle relative-norm embeddings.
Thus (9) tends to zero along any hypothetical input sequence with m->0 and k/d->1.
In such a sequence (7) forces B->infinity.
Total measure tending to zero by itself does NOT prove k/d->1 for arbitrary reciprocal inputs.

In particular, a genuine Salem input has exactly two positive real roots and k=d-2 original circle roots.
Therefore

    delta_circ<=min{1,[d epsilon(m/2)+2]/(d-2)}.    (10)

A hypothetical sequence of genuine Salem inputs with m->0 has d->infinity: for bounded d and M(P)<2 the elementary coefficient estimate |p_j|<=binom(d,j)M(P) leaves only finitely many monic integer polynomials, and the finitely many nontorsion measures have a positive minimum.
This is finite-degree finiteness, not an executed scan or a uniform all-degree gap.
L229 gives epsilon(h)->0, so (10) indeed implies delta_circ->0.
The bound (7) then forces the negative reduced constant magnitude B to diverge.
Every fixed b=-B is excluded eventually, uniformly in the unit and original nonnegative residual weights within THIS low-lag-only family.

Equivalently, for each fixed B_0>=1 there exists a positive mu(B_0) such that no genuine Salem input with 0<m(P)<mu(B_0) has an actual realization (2) with E<=1/2 and 1<=B<=B_0.
To see the quantifiers explicitly, choose an integer D_0>=4 such that 2/(D_0-2)<=delta_0(B_0)/2.
For d>=D_0 use d/(d-2)<=2 and choose m_* >0 with m_*/2<=h_0 and epsilon(m_*/2)<=delta_0(B_0)/4.
Then (10) gives delta_circ<=delta_0(B_0) whenever m<=m_*, contradicting (8).
For d<D_0 use the existing elementary finite-degree argument with M(P)<2 to choose a positive lower measure, or log2 if the bounded set is empty.
The minimum of this lower measure and m_* supplies mu(B_0).
The constants are conservative and no numerical evaluation, enumeration or useful numerical size is claimed.

<a id="fixed-constant-original-boundaries"></a>
## 5. Actual realization, no-circle and large-constant boundaries

The new result is a necessary support/constant-growth obstruction.
It extends the mean-two b=-1 analysis to EVERY fixed integer B under a small actual circle discrepancy, with the explicit genuine-Salem near-one specialization above.
It does not cover arbitrary reciprocal near-one inputs without the additional circle-root density/discrepancy information.
When k=0 the positive average in (6) is unavailable, so it is not replaced by a formal average over all off-circle embeddings.

If K_supp=0, the actual relative norm c=-B is an integer unit of the trace order.
Norm_F(c)=(-B)^s=Norm_K(u)=+/-1 forces B=1.
L370's actual quadratic u=alpha-1 for P=t^2-3t+1 has c=-1 and no circle conjugates, demonstrating why the no-circle branch cannot be discarded.
It remains a relative-norm control of fixed positive measure, not a complementary residual realization or a near-one construction.

The integer B is unbounded in the original Task.
The lower growth law (7) is compatible with B growing; no upper bound for B, unit coefficients, actual unit energy, full residual covariance or degree is obtained for free.
Even at fixed B the nonnegative relaxed symbol is not a converse for original weights.
Every actual unit still needs its order lift a^2+tau ab+b^2==C_u modulo the actual Q, and every claimed symbol needs the SAME original nonnegative weights in the full covariance equations.
No actual lift or realization is produced here.

The original common q, complete auxiliary coefficients and contents, actual residual degree T=N_window-1, all d original resultants, full signed unit norms and integer multiplicity parity remain as in L367.
The frequency count N=2K_supp+1 used in (1)--(4) is NOT the residual window N_window.
It changes neither the full original income nor the radial expense Tm(P)/d.
Real weights are not assigned integer copies; rational denominators and all resulting copies remain charged.
This result does not give a uniformly bounded coherence construction, all-input auxiliary coverage or an unrestricted positive Mahler gap.
