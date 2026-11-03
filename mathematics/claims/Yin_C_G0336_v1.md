---
author: Yin
---

# Exact triple-return norm mass with linear irreducible exponent and a finite Salem-family selector

This retains the complete original 2026-10-08 [L131 mathematical argument](../ledger/Yin_L_G0131_v1.md).
The original growth_arithmetic_status agent derived the norm-mass and selector proof for Yin; execution_and_deliverables supplied the exact Cayley identity (12) and stronger-input pointer, with original checking retained at R39.
No current Task/E execution, source acquisition, algorithm enumeration or mathematical program run is selected by this maintenance.

## Statement

Let f=t^3-t-1, f*=1-t^2-t^3 and F_N=t^N f+f*.
For every N=9 modulo120, N>=9, the complete retained all-N cyclotomic classification makes P_N=F_N itself the irreducible Salem polynomial of actual degree d_N=N+3.
For every such N the exact doubled norm is 2^(N+2)abs(gamma^N+1)^2<=2^(N+4), so its generic aggregate certificate is at most log2/(2N).
The triple-return norm is exactly 2*3^N product_(j=1)^3 abs(beta_j^N-omega)^2, where the full Cayley identity (12) proves all three cubic phases lie on the unit circle.
The nonzero integer N=9 baseline gives rational eta=1/(64*3^9), and Q=13/eta.
For every integer L>=1, finite three-angle pigeonholing supplies 1<=q<=Q^3 and N=9+120Lq with exact norm lower bound R_(3N)(P_N)>=3^(N-54)/2^41.
Equivalently the integer-resultant selector (23) terminates within those Q^3 candidates, without approximating phases or factoring norms.
All-prime actual valuation mass then has exponent n_N=3d_N-9 and gives (21), in particular m(P_N)>=log(3/2)/6 for every selected N>=500 and the displayed common aggregate constants.
The selected inputs have distinct unbounded degrees and actual measures tending to the plastic number above one.
No selector was executed; no fixed-prime scalar return, unselected-parameter bound, sufficiently-near-one coverage or new Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:38 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(23): direct all-N irreducible/cyclotomic input, actual degree, double/triple leading coefficients and exact Cayley cubic, rational baseline, full Q^3 selection/window cost, powers2^41/3^54, exact ideal/linear exponent/N500/common coverage and terminating integer selector with all limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(23): direct all-N irreducible/cyclotomic input, actual degree, double/triple leading coefficients and exact Cayley cubic, rational baseline, full Q^3 selection/window cost, powers2^41/3^54, exact ideal/linear exponent/N500/common coverage and terminating integer selector with all limits. |
| dependency | [Exact retained input](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Complete direct all-N Salem factorization and exact five-factor square-free cyclotomic table, removing the older unspecified external threshold. |
| dependency | [Exact retained input](Yin_C_G0222_v1.md#sparse-salem-delay-family) | Exact local cubic/root/distinctness and all-power degree arguments, reused with the stronger direct factorization. |
| dependency | [Exact retained input](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) | Exact distinct-ideal total norm mass and generic d log2 cost; primes/depths may vary with the input. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:48 |
| status | proved |
| reason | Adopt the complete exact original theorem and retained argument after actual whole self-review of every stated scope and used interface; preserve every finite guard, unexecuted algorithm, original checking input and nonuniformity limitation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(23): direct all-N irreducible/cyclotomic input, actual degree, double/triple leading coefficients and exact Cayley cubic, rational baseline, full Q^3 selection/window cost, powers2^41/3^54, exact ideal/linear exponent/N500/common coverage and terminating integer selector with all limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(23): direct all-N irreducible/cyclotomic input, actual degree, double/triple leading coefficients and exact Cayley cubic, rational baseline, full Q^3 selection/window cost, powers2^41/3^54, exact ideal/linear exponent/N500/common coverage and terminating integer selector with all limits. |
| dependency | [Exact retained input](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Complete direct all-N Salem factorization and exact five-factor square-free cyclotomic table, removing the older unspecified external threshold. |
| dependency | [Exact retained input](Yin_C_G0222_v1.md#sparse-salem-delay-family) | Exact local cubic/root/distinctness and all-power degree arguments, reused with the stronger direct factorization. |
| dependency | [Exact retained input](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) | Exact distinct-ideal total norm mass and generic d log2 cost; primes/depths may vary with the input. |
| review | [Actual current whole self-check](../audits/reviews/Yin_R_G0556_v1.md#current-triple-return-selection-finding) | Complete current statement, retained proof and directly used inputs; self-reviewed. Original findings retain their actual original dates, inputs, corrections and checking relationships. |

## Complete retained argument

<a id="argument"></a>
## Question and result

The [three-time obstruction in L G0128](Yin_C_G0333_v1.md#three-time-resultant-obstruction) leaves different exponents open.
Here the input polynomial varies with \(N\); the new return exponent is \(3N\).
This is not a fixed-input cyclic-norm asymptotic theorem.
We construct infinitely many actual irreducible Salem inputs for which a full cyclic norm at this exponent pays the degree cost in the [aggregate certificate](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion).
An explicit finite selector finds a successful input parameter in each specified multiplicative window.
The primes carrying the norm are allowed to vary with that input; no scalar return at one prime is asserted.

The family has Mahler measures tending to the plastic number, strictly greater than one.
Its positive gap was already known from its construction.
The new conclusion is finite-time norm mass at an exponent linear in the actual irreducible degree, with a parameter-selection theorem.
It does not provide coverage of the sufficiently near-one core or a new Lehmer gap.
All logarithms are natural.

### A progression with no cyclotomic padding

Put
\[
 f(t)=t^3-t-1,\qquad f^*(t)=1-t^2-t^3,\qquad
 F_N(t)=t^N f(t)+f^*(t).
 \tag{1}
\]
Let \(\theta>1\) denote the real root of \(f\).
The direct argument in [L G0038](Yin_C_G0248_v1.md) proves that for every \(N>3\), \(F_N\) has one Salem minimal factor and a cyclotomic part.
Its [complete cyclotomic table](Yin_C_G0248_v1.md#family-cyclotomic-factors) lists exactly
\[
 \begin{array}{c|c}
 \text{factor}&\text{condition}\\ \hline
 \Phi_2&N\equiv0\pmod2\\
 \Phi_8&N\equiv7\pmod8\\
 \Phi_{12}&N\equiv10\pmod{12}\\
 \Phi_{18}&N\equiv14\pmod{18}\\
 \Phi_{30}&N\equiv21\pmod{30}.
 \end{array}
 \tag{2}
\]
Each listed factor is simple.
In particular, on the progression
\[
 N\equiv9\pmod{120},\qquad N\geq9,
 \tag{3}
\]
none occurs: \(N\) is odd, \(N\equiv1\pmod8\), and \(N\equiv9\pmod{30}\); the remaining two conditions in (2) require even \(N\).
Therefore \(F_N\) itself is the actual monic irreducible Salem minimal polynomial.
Write it as \(P_N=F_N\), with positive exterior root \(\tau_N\), and put
\[
 d_N=\deg P_N=N+3.
 \tag{4}
\]
There is no omitted cyclotomic norm factor in the calculations below.

For \(N\geq16\), the same existing direct proof gives
\[
 \theta<\tau_N<4/3,\qquad M(P_N)=\tau_N\to\theta.
 \tag{5}
\]
The roots \(\tau_N\) are distinct and all their positive powers retain degree \(d_N\), as proved in L G0020 and retained by L G0038.
The latter direct Rouche argument removes the unspecified threshold of the earlier external Salem-construction statement; (2)--(5) here use this stronger already fixed internal result.
No new source theorem is adopted.
The parameter \(N=9\) will be used only as a nonzero integer-resultant baseline; it need not satisfy the upper bound in (5).

For a monic integer polynomial \(H\), let
\[
 R_n(H)=\lvert\operatorname{Res}(H,t^n-1)\rvert.
 \tag{6}
\]
On (3), all \(R_n(P_N)\) are positive integers: an irreducible Salem polynomial has no root of unity.

<a id="doubled-return-cost-boundary"></a>
### The doubled return has only the critical generic mass

Throughout this section \(N\) satisfies (3).
Splitting \(t^{2N}-1=(t^N-1)(t^N+1)\), one evaluates \(F_N\) by substituting \(t^N=1\) and \(t^N=-1\), respectively.
The first factor contributes two because
\[
 f+f^*=-t(t+1),\qquad N\text{ is odd}.
\]
For the second,
\[
 f^*-f=(1-t)(2t^2+3t+2).
 \tag{7}
\]
The factor \(1-t\) contributes two at \(t^N=-1\).
The quadratic has roots \(\gamma,\overline\gamma=(-3\pm i\sqrt7)/4\), both of modulus one.
The root-product formula for resultants, including its leading coefficient \(2\), thus gives
\[
 R_{2N}(P_N)
   =2^{N+2}\lvert\gamma^N+1\rvert^2
   \leq2^{N+4}.
 \tag{8}
\]

Consequently every valid aggregate local lower mass \(A(2N)\), even the exact mass from all prime ideals, satisfies
\[
 \frac{A(2N)-d_N\log2}{2N}
 \leq\frac{\log R_{2N}(P_N)-(N+3)\log2}{2N}
 \leq\frac{\log2}{2N}.
 \tag{9}
\]
Thus these doubled exponents cannot give a common positive floor through the specified generic \(d_N\log2\) certificate.
Equation (9) bounds that certificate, not the true Mahler measure.
It does not rule out a sharper archimedean inequality with additional input.

### Exact triple-return factorization and its fixed cubic phases

Let \(\omega=(-1+i\sqrt3)/2\), so \(t^{3N}-1=(t^N-1)(t^N-\omega)(t^N-\overline\omega)\).
Define
\[
 Q_\omega(t)=f^*(t)+\omega f(t)
  =(\omega-1)t^3-t^2-\omega t+(1-\omega).
 \tag{10}
\]
The factor at \(t^N=1\) again contributes two.
If \(\beta_1,\beta_2,\beta_3\) are the roots of \(Q_\omega\), then the other cubic is \(Q_{\overline\omega}=\overline{Q_\omega}\), with conjugate roots.
Because \(\lvert\omega-1\rvert=\sqrt3\), the two leading-coefficient contributions and the root products give the exact identity
\[
 R_{3N}(P_N)=2\,3^N
   \prod_{j=1}^{3}\lvert\beta_j^N-\omega\rvert^2.
 \tag{11}
\]
One may obtain (11) directly by evaluating \(F_N\) at the roots of each \(t^N-a\): there its value is \(f^*+a f\).
Swapping the two arguments of a resultant changes at most its sign, which disappears in (11).
In particular no equality with an unnormalized monic cubic has discarded the \(3^N\) contribution.

All three \(\beta_j\) lie on the unit circle.
An exact Cayley identity is
\[
 (\sqrt3-iy)^3
 Q_\omega\!\left(\frac{\sqrt3+iy}{\sqrt3-iy}\right)
 =-i(\omega-1)(y^3-y^2-21y-3).
 \tag{12}
\]
It follows by expanding (10) and using \(\omega^2+\omega+1=0\).
The real cubic \(g(y)=y^3-y^2-21y-3\) has the exact values
\[
 g(-5)=-48,\quad g(-4)=1,\quad
 g(-1)=16,\quad g(0)=-3,\quad
 g(5)=-8,\quad g(6)=51.
\]
It therefore has three distinct real roots, one in each of \((-5,-4),(-1,0),(5,6)\).
Their Cayley images have modulus one and are distinct.
Equation (12), and the fact that \(Q_\omega\) has degree three with nonzero leading coefficient, account for all its roots.
This is a finite exact algebraic argument; no approximation of the phases or logarithmic-form estimate is used.

### A rational baseline for all three phase factors

At \(N=9\), the irreducibility consequence of (2) is valid, so \(R_{27}(P_9)\) is a nonzero integer.
Equation (11) implies
\[
 \prod_{j=1}^{3}\lvert\beta_j^9-\omega\rvert^2
 \geq\frac1{2\,3^9}.
\]
Think of the product as six factors, each at most two.
Bounding the other five by \(2^5\) shows that every one of the three factors obeys
\[
 \lvert\beta_j^9-\omega\rvert\geq\eta,
 \qquad
 \eta=\frac1{64\,3^9}.
 \tag{13}
\]
This lower bound is deliberately conservative.
It needs no evaluation of the integer resultant and no numerical root computation.

Set the explicit integer
\[
 Q=13\eta^{-1}=13\cdot64\cdot3^9.
 \tag{14}
\]
For every positive integer \(L\), simultaneous pigeonholing gives an integer \(q\) with
\[
 1\leq q\leq Q^3,\qquad
 \max_{1\leq j\leq3}
   \lvert\beta_j^{120Lq}-1\rvert
   \leq\frac{2\pi}{Q}<\frac\eta2.
 \tag{15}
\]
For completeness, write the three phases of \(\beta_j^{120L}\) modulo one.
Partition \([0,1)^3\) into \(Q^3\) cubes of side \(1/Q\) and consider its \(Q^3+1\) successive orbit points from index zero through \(Q^3\).
Two lie in the same cube.
Their positive index difference is the required \(q\); the coordinate differences are at most \(1/Q\), and \(\lvert e^{2\pi ix}-1\rvert\leq2\pi\lvert x\rvert\).
The strict last inequality in (15) uses \(4\pi<13\).

For this \(q\), put
\[
 N=9+120Lq.
 \tag{16}
\]
Then (3) holds, \(N\geq129\), and
\[
 9+120L\leq N\leq9+120LQ^3.
 \tag{17}
\]
Using \(\lvert\beta_j\rvert=1\), (13) and (15) give
\[
 \lvert\beta_j^N-\omega\rvert
 \geq\lvert\beta_j^9-\omega\rvert
      -\lvert\beta_j^{120Lq}-1\rvert
 >\eta/2.
\]
Substitution into (11) proves the explicit norm-mass bound
\[
 R_{3N}(P_N)
 \geq2\,3^N(\eta/2)^6
 =\frac{3^{N-54}}{2^{41}}.
 \tag{18}
\]
The variable \(L\) is arbitrary.
Since the lower endpoint in (17) tends to infinity, these selections give infinitely many distinct degrees and inputs.
No recurrence time is assumed without its cost: the explicit upper cost \(Q^3\) is retained.

<a id="linear-exponent-cyclic-coverage"></a>
### Exact arithmetic mass and linear exponent cost

For each selected \(N\), let \(K_N=\mathbb Q(\tau_N)\), and take all the distinct prime ideals \(\mathfrak p\) dividing \(\tau_N^{3N}-1\).
With \(p_{\mathfrak p}\) the underlying rational prime and \(f_{\mathfrak p}\) its residue degree, define the full actual local mass
\[
 A_N=\sum_{\mathfrak p}
 f_{\mathfrak p}\operatorname{ord}_{\mathfrak p}(\tau_N^{3N}-1)
       \log p_{\mathfrak p}
 =\log R_{3N}(P_N).
 \tag{19}
\]
This is the exact [prime-ideal norm formula](Yin_C_G0256_v1.md#content-versus-ideal-norm).
The support is finite for each input.
Ramification and all valuation depths are included, and each prime ideal is counted once.
Equation (18) gives a lower bound for this total without claiming a prescribed prime set, uniform splitting pattern, bounded residue degrees or a simultaneous scalar return.

The exponent satisfies the exact degree relation
\[
 n_N=3N=3d_N-9.
 \tag{20}
\]
Combining (18)--(20) with the existing aggregate inequality yields
\[
 \begin{aligned}
 m(P_N)
 &\geq\frac{A_N-d_N\log2}{3N}\\
 &\geq\frac{\log(3/2)}3
       -\frac{44\log2+54\log3}{3N}.
 \end{aligned}
 \tag{21}
\]
In particular, for every selected \(N\geq500\),
\[
 m(P_N)\geq\frac{\log(3/2)}6>0.
 \tag{22}
\]
The integer threshold is verified without numerical logarithms: at \(N=500\),
\[
 500\log(3/2)-2(44\log2+54\log3)
 =196\log(9/8)>0,
\]
and the left side increases with \(N\).
Thus taking any \(L\geq5\) in (15)--(17) produces a member satisfying (22).

These selected members also satisfy common constants in the literal uniform-coverage hypothesis of L G0074.
Indeed (21)--(22) give \(A_N-d_N\log2\geq(N/2)\log(3/2)\).
Since \(d_N=N+3\leq2N\), one may take
\[
 \varepsilon=\frac{\log(3/2)}{4\log2},\qquad
 C=\frac3{\log2},
\]
to obtain \(A_N\geq(1+\varepsilon)d_N\log2\) and \(n_N\leq C A_N\).
The direct estimate (21) is sharper than the constant obtained by this last conversion.
The coverage is restricted to the selected polynomial family; it is not asserted for all inputs in a Mahler interval.

### An effective finite selector, with its large cost retained

For a supplied integer \(L\geq1\), enumerate \(q=1,\ldots,Q^3\).
At each candidate \(N=9+120Lq\), compute the integer resultant \(R_{3N}(F_N)\) and test
\[
 2^{41}R_{3N}(F_N)\geq3^{N-54}.
 \tag{23}
\]
All candidate \(N\) are at least 129, so the right exponent is a nonnegative integer.
The proof of (15)--(18) guarantees that at least one test succeeds.
This supplies an exact terminating selector without approximating the phases or factoring the norm.
Every output satisfies (18)--(21), whether or not its individual phase factors satisfy the particular lower bounds used to prove existence.

This is a mathematical finite-selection bound, not a claim of practical running time.
The number \(Q^3\) is very large, the possible degree grows with both \(L\) and \(q\), and the resultant computation has its actual growing integer-arithmetic cost.
No such enumeration or resultant computation has been run in this derivation.
The guarantee does not use an unknown \(1/m(P_N)\) time or a pointwise norm limit.

### What changes and what remains open

The double-return calculation (8)--(9) reaches at most the critical generic cost, while the triple return has a \(3^N\) leading mass.
The fixed cubic phases identify its possible loss, and the explicit simultaneous selection controls that loss on infinitely many actual irreducible inputs.
This explains why changing the exponent can produce a useful certificate after the three adjacent times in L G0128 fail, without rescanning a fixed prime set.

The arithmetic conclusion is collective norm mass, not a theorem about which individual primes must supply it.
A transfer demanding specific local fields, small primes or low scalar periods would require an additional argument.
The bound also does not cover every \(N\) in (3): the parameter selection is substantive.
It does not imply a uniform lower bound for every unselected phase product.

Every selected family member already satisfies (5), so the true measures approach \(\theta>1\).
The bound (22) is not a numerical improvement on the known lower bound \(\log\theta\).
What is added is an exact restricted-family realization of aggregate norm mass with \(n_N=3d_N-9\) and a finite explicit parameter-selection cost.
No sufficiently near-one coverage, vanishing positive-measure family, uniform original-binary collision estimate or Lehmer resolution follows.
