---
author: Yin
---

# Cyclotomic central perturbations: squarefree parent closures and an exact phase test

Date: 2026-11-10.

This is a bounded construction comparison for the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The main researcher proposed changing the fixed neutral profile and observed that its total numerator-plus-denominator degree enters the Newton argument only logarithmically.
The strategic-discovery contributor developed the squarefree parent closure, its exact residue formula, the conductor-1009 sign calculation and the root-angle selection criterion.
The conditional measure extension was developed by both contributors and is retained with its full proof in [C881 v9](../claims/Yin_C_G0881_v9.md#statement).
These are author-side construction and computation contributions; their development does not constitute independent review or an admissible small-measure example.
The final construction and phase criteria have a separate [independent finding](../audits/reviews/Yin_R_G1107_v40.md#squarefree-parent-construction-review), and the specified exact measure calculation has its own [independent computation finding](../audits/reviews/Yin_R_G1107_v40.md#growing-profile-resultant-review).

The central-shift method already belongs to [C414](../claims/Yin_C_G0414_v1.md#real-trace-shift-criterion) and its retained source scope.
[L457 v2](../ledger/Yin_L_G0457_v2.md#cyclotomic-central-minus-one-scope) is the nearest fixed account of cyclotomic central subtraction, but its actual inputs do not contain this product closure.
This version retains the new construction calculations and unresolved selection question without changing the earlier fixed results or claiming a new perturbation method.

<a id="integer-family"></a>
## Actual integer family and automatic prefix

Let \(A\in\mathbb Z[z]\) be a squarefree product of distinct cyclotomic polynomials of orders at least three, with degree \(2d\), where \(d\ge2\).
Thus \(A\) is monic and reciprocal, has constant coefficient one, has no roots at \(1\) or \(-1\), and has a monic integer trace polynomial \(C_A\) with \(d\) distinct roots in \((-2,2)\):
\[
 A(z)=z^d C_A(z+z^{-1}).
 \tag{1}
\]
The integer trace representation follows from the reciprocal integer basis used in [C881 v3](../claims/Yin_C_G0881_v3.md#original-domain).

Choose an odd integer \(r>2d+1\), and put
\[
 m=\frac{r-1}{2},\qquad N=m+d,\qquad n=N-1,\qquad
 p=2n+1=r+2d-2.
\]
Define the complete parent and perturbed polynomial by
\[
 P^{(0)}(z)=A(z)\frac{1-z^r}{1-z},\qquad
 P(z)=P^{(0)}(z)-z^N.
 \tag{2}
\]
Both are monic reciprocal integer polynomials of degree \(2N=p+1\) and constant coefficient one.
The parent has measure one because it is an actual cyclotomic product.
When every order appearing in \(A\) is even, it is coprime to the odd-order factors of \((1-z^r)/(1-z)\), so the complete parent is squarefree.

There is no surviving factor of the parent in \(P\).
At every root \(\zeta\) of \(P^{(0)}\), one has \(P(\zeta)=-\zeta^N\ne0\).
Thus the operation changes the nonneutral core whenever its output is nonneutral, rather than padding an unchanged core.
New cyclotomic factors are not excluded by this coprimality argument, so nonneutrality remains a separate condition.

The exact reference series is \(R_A=A/(1-z)\).
Since \(r>N\),
\[
 P-R_A=-\frac{z^r A(z)}{1-z}-z^N=O(z^N).
 \tag{3}
\]
Every coefficient through index \(N-1=n\) agrees with this rational cyclotomic reference.
Its total numerator-plus-denominator degree is \(H=2d+1\).
For moving choices with \(r/d\to\infty\), this gives \(H=o(L)\) at \(L=N-1\), entirely by integer algebra.
No sign chamber or Mahler bound follows from this prefix alone.

The trace polynomial and endpoint are
\[
 Q(t)=C_A(t)B_m(t)-1,\qquad
 P(z)=z^NQ(z+z^{-1}),\qquad
 P(-1)=A(-1)-(-1)^N,
 \tag{4}
\]
where
\[
 B_m(2\cos\theta)=\frac{\sin(r\theta/2)}{\sin(\theta/2)}
\]
has the original \(B_m=E_m+E_{m-1}\) normalization.

If
\[
 A(z)=1+3z^2+O(z^4),
 \tag{5}
\]
then \(P=1+z+4z^2+4z^3+O(z^4)\).
Monic trace division gives \(Q=tB_n+C\), with \(\deg C<n\), and its original canonical coordinates satisfy \(a_0=2\), \(a_1=0\).
For the quotient, the coefficient of degree \(n\) in both \(Q\) and \(tB_n\) is one, so there is no constant shift.
For the next coefficient,
\[
 [t^{n-1}]Q=4-(n+1),\qquad
 [t^{n-1}]tB_n=-(n-1),
\]
whose difference is two.
The inverse congruence \(E_{n-1}B_{n-1}\equiv1\pmod {B_n}\) from [C881 v3](../claims/Yin_C_G0881_v3.md#prefix-coordinates) gives an actual integer \(h\) in the original residue-coordinate domain.

If an input satisfying (5) also had the original single-terminal-negative-node signs and strict endpoint, [C881 v8](../claims/Yin_C_G0881_v8.md#statement) would imply strict nonneutrality and exactly one conjugate pair of nonreal exterior roots.
This conditional use does not assert those signs.

<a id="residue-formula"></a>
## Complete residue formula on the correct grid

Put \(\theta_j=2\pi j/p\), \(b_j=2\cos\theta_j\), for \(1\le j\le n\).
The original residues are \(\rho_j=Q(b_j)/B_n'(b_j)\).
Differentiating the sine formula for \(B_n\) gives
\[
 B_n'(b_j)=
 \frac{(-1)^{j+1}p}{4\sin\theta_j\sin(\theta_j/2)}.
 \tag{6}
\]
All sine factors in this denominator are positive.

The corrected degree relation gives
\[
 \sin(r\theta_j/2)
 =\sin\bigl(\pi j-(d-1)\theta_j\bigr)
 =(-1)^{j+1}\sin\bigl((d-1)\theta_j\bigr).
\]
Define
\[
 W_A(\theta)=
 C_A(2\cos\theta)\frac{\sin((d-1)\theta)}{\sin(\theta/2)}.
 \tag{7}
\]
Equations (4)--(6) yield the complete formula
\[
 \boxed{\quad
 \rho_j=
 \frac{4\sin\theta_j\sin(\theta_j/2)}p
 \left(W_A(\theta_j)-(-1)^{j+1}\right).
 \quad}
 \tag{8}
\]
Thus an odd index intended to have positive residue requires \(W_A(\theta_j)>1\), whereas an even such index requires \(W_A(\theta_j)>-1\).
For a terminal negative residue the corresponding inequality is reversed.
Replacing (8) by the nonnegative square formula of [L462 v11](../ledger/Yin_L_G0462_v11.md#neutral-integer-supply) would be incorrect.

<a id="exact-1009-input"></a>
## One squarefree profile with the stated arithmetic inputs

Take
\[
 A(z)=\Phi_{60}(z)\Phi_{84}(z)\Phi_{140}(z),\qquad
 d=44,\qquad r=923.
 \tag{9}
\]
The three degrees are \(16,24,48\), with sum \(88=2d\).
The factors are distinct, and their even orders are disjoint from every order in the odd geometric factor of length \(923\).
The complete neutral parent is therefore squarefree.

For distinct odd primes \(u,v\),
\[
 \Phi_{uv}(x)=
 \frac{(1-x^{uv})(1-x)}{(1-x^u)(1-x^v)}
 =1-x+O(x^3).
\]
The orders \(60,84,140\) are \(4\cdot15,4\cdot21,4\cdot35\), and
\[
 \Phi_{4uv}(z)=\Phi_{uv}(-z^2)=1+z^2+O(z^6).
\]
This substitution identity follows by matching primitive root orders.
Multiplication gives
\[
 A(z)=1+3z^2+3z^4+O(z^6).
 \tag{10}
\]
At \(z=1\) and \(z=-1\), the argument \(-z^2\) is \(-1\), where the displayed quotient for \(\Phi_{uv}\) has value one.
Hence \(A(1)=A(-1)=1\).

The parameters become
\[
 m=461,\qquad N=505,\qquad n=504,\qquad p=1009,
\]
and the complete input is
\[
 \boxed{\quad
 P(z)=\Phi_{60}(z)\Phi_{84}(z)\Phi_{140}(z)
       \frac{1-z^{923}}{1-z}-z^{505}.
 \quad}
 \tag{11}
\]
It is monic reciprocal integral of degree \(1010\), has \(a_0=2,a_1=0\), and satisfies
\[
 P(-1)=1-(-1)^{505}=2>0.
\]
Its prefix agrees with \(A/(1-z)\) through index \(504\).
This is a changed profile: its coefficient at index four is seven, whereas the old zero profile has coefficient eight.
These statements require neither a full coefficient expansion nor numerical roots.

<a id="two-early-defects"></a>
## Two exact early negative residues

Write \(\theta=2\pi u\).
The first trace-root angle of \(A\) is \(u=1/140\).
There is no further trace root before \(u=1/86\).
The first roots of the other two factors are at \(1/84\) and \(1/60\), both larger than \(1/86\).
For order \(140\), the next possible primitive numerator is \(3\), with \(3/140>1/86\); numerator \(2\) is not coprime to \(140\).

Since \(C_A(2)=A(1)=1>0\) and every trace root is simple,
\[
 C_A(2\cos(2\pi u))<0
       \qquad\left(\frac1{140}<u<\frac1{86}\right).
\]
On this interval \(0<43\cdot2\pi u<\pi\), so the sine quotient in (7) is positive.
Therefore \(W_A(2\pi u)<0\) there.

The exact rational inclusions
\[
 \frac1{140}<\frac9{1009}<\frac1{86},\qquad
 \frac1{140}<\frac{11}{1009}<\frac1{86}
 \tag{12}
\]
follow from
\[
 1009<1260,\quad774<1009,\quad
 1009<1540,\quad946<1009.
\]
Both indices are odd, so (8) proves
\[
                         \rho_9<0,\qquad \rho_{11}<0.
 \tag{13}
\]
This rejects the \(\kappa=1\) chamber, and any terminal cut whose required-positive initial segment contains index nine or eleven.
These two early residues alone do not exclude every terminal cut.
It is not a calculation of the complete Mahler measure.

<a id="root-angle-gate"></a>
## An exact root-angle gate for choosing growing parents

Let \(\mathcal M\) be the set of orders in \(A\).
For \(0<u<1/2\), define
\[
 K_A(u)=
 \#\{(q,a):q\in\mathcal M,\ 1\le a<qu,\ \gcd(a,q)=1\}.
 \tag{14}
\]
This counts the trace-root angles already crossed.
Away from the zeros of both factors in (7),
\[
 \operatorname{sign}W_A(2\pi u)
 =(-1)^{K_A(u)+\lfloor2(d-1)u\rfloor}.
 \tag{15}
\]
The initial sign of \(C_A\) is positive, each simple root reverses it, and the second parity is the sign of \(\sin(\pi\cdot2(d-1)u)\).

On the grid the count is the exact integer expression
\[
 K_A(j/p)=
 \sum_{q\in\mathcal M}\ \sum_{e\mid q}
 \mu(e)\left\lfloor\frac{qj-1}{pe}\right\rfloor.
 \tag{16}
\]
The inner term counts positive multiples \(a=eb\) with \(pa<qj\), and inclusion-exclusion enforces coprimality.
The subtraction of one handles the strict inequality even at grid coincidences.
A root of \(A\) occurs at the grid point exactly when \(p/\gcd(p,j)\in\mathcal M\).
A zero of the sine factor is detected by \(p\mid2(d-1)j\).

At every odd index in the required-positive range, either coincidence gives \(W_A=0\) and an immediate rejection.
Otherwise the parity in (15) must be even.
This is a necessary gate using only root orders and integer arithmetic.
Passing it does not settle the amplitudes \(W_A>1\) at odd indices, \(W_A>-1\) at even indices, the terminal inequality, or the endpoint.

One can check all early phase defects by rational intervals instead of traversing all grid points.
Order the distinct rational locations \(a/q\) and \(k/(2(d-1))\) in \((0,1/2)\), keeping coincident events together.
Between consecutive locations the parity is constant.
For a negative interval \((a,b)\), the least odd integer strictly greater than \(pa\) is
\[
 j_0=2\left\lfloor\frac{pa+1}{2}\right\rfloor+1.
\]
If \(j_0<pb\) and this index belongs to the required-positive range, it proves rejection.
Every endpoint and comparison is rational.
A negative interval of width greater than \(2/p\) necessarily contains an odd grid point, subject to that range restriction.

The constructive selection question is whether growing squarefree parents with the prescribed first coefficients can make every negative phase interval avoid the required odd grid points and can then satisfy the complete amplitude inequalities.
This criterion exposes all early phase defects of each specified parent, rather than only its endpoint behavior.
No parent enumeration has been run, no asymptotic feasibility of the gate has been proved, and no growing family meeting the complete chamber is supplied here.

<a id="terminal-phase-gate"></a>
## A last-pole obstruction and the endpoint parity

The main researcher's further check of the exact residue formula gives a necessary endpoint condition before any interior phase test.
Keep the family (1)--(4), so \(\theta_n=\pi-\pi/p\).
If \(C_A(b_n)=0\) and \(n\) is even, (8) gives \(\rho_n>0\), which immediately contradicts a terminal negative block.
For \(C_A(b_n)\ne0\), let \(e\) be the number of trace roots of \(A\) in \((-2,b_n)\).
Every such root is simple.
Since the roots of \(A\) form nonreal conjugate pairs,
\[
 A(-1)>0,\qquad C_A(-2)=(-1)^dA(-1).
\]
Moving from \(-2\) to \(b_n\) crosses exactly those \(e\) roots, so \(C_A(b_n)\) has sign \((-1)^{d+e}\).
Also
\[
 \sin((d-1)\theta_n)=(-1)^d\sin((d-1)\pi/p),
 \qquad 0<(d-1)\pi/p<\pi.
\]
The denominator in (7) is positive; hence \(W_A(\theta_n)\) has sign \((-1)^e\).

When \(n\) is even, a negative last residue requires \(W_A(\theta_n)<-1\), so \(e\) must be odd and positive.
For a root in this endpoint interval, write its primitive angle as \(2\pi a/q\), with \(0<a<q/2\) and order \(q\) appearing in \(A\).
The strict interval condition implies
\[
 0<q-2a<q/p.
\]
The left side is a positive integer, so necessarily \(q>p\).
If every order in \(A\) is even, it is a positive even integer, and necessarily some order satisfies \(q>2p\).
This condition is only necessary: it supplies neither odd endpoint-root parity nor the required magnitude greater than one.

When \(n\) is odd, \(N=n+1\) is even and the strict endpoint instead requires \(P(-1)=A(-1)-1>0\).
Thus \(A(-1)>1\) is necessary in that parity.

These two cases reject every odd \(r>89\) for the specific fixed parent \(A=\Phi_{60}\Phi_{84}\Phi_{140}\).
For odd \(n\), its endpoint is zero because \(A(-1)=1\).
For even \(n\), one has \(p=r+86\ge177\), while every order is at most \(140<2p\), so the necessary last-pole condition fails.
In particular the conductor-1009 input has \(\rho_{504}>0\) and cannot have any strict terminal negative block.
This exact all-\(r\) sign-and-endpoint rejection does not claim a measure bound for every \(r\); the complete measure certificate below concerns only \(r=923\).

<a id="neutral-reference-bound"></a>
## Variable-reference bound and complete rejection of the fixed input

The exact hypotheses and complete proof of the variable-reference extension belong to [C881 v9](../claims/Yin_C_G0881_v9.md#statement).
Under its strict terminal-cut and endpoint hypotheses, a prefix through index \(L\) matching a unit-circle-root rational reference of total numerator-plus-denominator degree \(H\) gives
\[
 M(P)\le(8\lfloor L/2\rfloor+H+3)^{2/\lfloor L/2\rfloor}.
 \tag{18}
\]
It retains both real and nonreal residual pairs and the whole polynomial measure.
The condition \(\log(L+H)=o(L)\) suffices for the upper bound to tend to one.
For the integer subcase with (5), \(\kappa=1\), and the actual signs and endpoint, its use of [C881 v8](../claims/Yin_C_G0881_v8.md#statement) also supplies strict positivity.
No signs or integer sequence are supplied by that conditional conclusion.

For (11), the already established \(L=504\), \(H=89\) and endpoint would give
\[
 M(P)\le2108^{1/126}<6/5
 \tag{19}
\]
under any strict terminal-cut hypothesis.
The last inequality is exact: \((6/5)^5>2\) gives \((6/5)^{60}>4096>2108\), hence also \((6/5)^{126}>2108\).
The main researcher's completed [J138 whole-polynomial resultant calculation](../computations/programs/Yin_J_G0138/readme.md#growing-profile-resultant) uses the exact input (11).
With \(s=2053\), it obtains
\[
 R=|\operatorname{Res}(P,z^s-1)|>0,\qquad
 R\,4^{2053}>2^{1010}11^{2053}.
\]
The program also checks the exact identity \(R=922\operatorname{Res}(B_{1026},Q)^2\), with a binomial reconstruction of the complete reciprocal trace lift.
Both resultants use the same FLINT backend and are ordinary author controls.
For every root \(\alpha_i\) of \(P\), counting multiplicity,
\[
 |\alpha_i^s-1|\le2\max\{1,|\alpha_i|\}^s.
\]
Since \(P\) is monic of degree \(1010\), multiplication yields \(R\le2^{1010}M(P)^s\), and hence
\[
                         M(P)>11/4>6/5.
 \tag{20}
\]
This is a lower bound for the complete polynomial; it supplies no individual proper-factor bound.

Combining (19) and (20) gives, using the stated conditional theorem and trusted exact computation, that this fixed input satisfies no strict terminal-cut sign pattern for any \(1\le\kappa<504\).
Its endpoint and prefix were already verified, so the failed premise must be the signs.
This stronger all-cut conclusion uses the conditional full-measure lemma and the actual resultant evidence, not the two negative residues alone.
The separate [last-pole argument](#terminal-phase-gate) gives another exact exclusion of the same signs, and additionally covers every permitted \(r\) for this fixed \(A\).
It excludes neither the full moving-parent family nor extracted small factors.

<a id="comparison-and-return"></a>
## Comparison and unresolved construction step

[L462 v11](../ledger/Yin_L_G0462_v11.md#neutral-integer-supply) uses a fixed squared trace factor and a different neutral closure.
Here the complete parent can be squarefree, the perturbation breaks every parent factor, and the corrected degree relation produces (8).
The old nonnegative residue formula and retained-double-factor obstruction cannot simply be copied to this object.

[C884](../claims/Yin_C_G0884_v1.md#inputs) and its later signed-amplitude versions classify the fixed neutral profile with its specified \(tB_k\) deformation.
The numerator \(A\), reference \(A/(1-z)\), and constant trace shift here are different inputs.
[L464 v19](../ledger/Yin_L_G0464_v19.md#fixed-number-of-terms) still requires checking a proposed moving parent for a bounded-support cyclotomic completion.
Increasing degree or writing more factors alone does not escape that obstruction.

[L457 v2](../ledger/Yin_L_G0457_v2.md#cyclotomic-central-minus-one-scope) already studies central subtraction from one cyclotomic polynomial and leaves its unbounded-prime-count range open.
This product closure adds an automatic long reference prefix and the explicit phase gate, without establishing a new central-shift method or a general classification.
Compared with [S10's paused sampling allocation](../strategies/Yin_S_G0010.md#allocation-after-fixed-cell), it supplies exact integer parents and a deterministic necessary rejection test, not a sampling-performance claim.

The example satisfies the integer, prefix, first-coordinate and endpoint requirements.
The endpoint-parity and last-pole conditions reject this fixed parent at every permitted \(r\); independently, the complete measure at \(r=923\) is greater than \(11/4\).
The first unsupported construction step is a growing choice of \(A,r\) meeting the full phase and amplitude system, not another improvement of the conditional upper bound.
The bounded test recommended before any larger campaign checks the endpoint parity and last-pole condition first, then the exact rational root-angle gate for a specified new parent, followed only on a pass by certified amplitude and whole-measure checks.
No such growing choice, new finite value below \(6/5\), sublinear-degree factor or resolution of the unrestricted Task has been established here.
