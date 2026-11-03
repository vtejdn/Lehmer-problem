---
author: Yin
---

# A finite-prime discriminant gap and the remaining entropy obstruction

Date: 2026-10-06.
Coordinating AI agent for Yin, under [T G0001](../tasks/Yin_T_G0001_v1.md#contract).
This applies a known Mat96 determinant estimate, with a direct proof of its finite-prime case and consequences for algebraic entropy.
It does not resolve Lehmer.

## Source reuse and threshold check

The initial input was [Smy08-U003](../audits/literature/Smy08/Yin_U003.md#smy08-discriminant-separation), accepting Mat96 Theorem 1 at statement scope.
A proposed compact-positivity application of f(x)=(log(log(x))/log(x))^3 required a threshold a>e, not merely a>1: f is negative on (1,e), zero at e, and positive above e.
That shortcut was withheld pending inspection.

The unchanged retained Mat96 PDF was freshly rendered and read at printed pp.416--420 / PDF pp.2--6.
The decisive passages are equation (7), p.417, and the first two paragraphs of p.418.
Equation (7) permits an auxiliary delta at least the actual discriminant parameter; the first paragraph takes it sufficiently large, resolving the threshold issue at proof-interface scope.
The second paragraph gives a finite-prime specialization, used below instead of the asymptotic theorem.
Other read pages supply degree-reduction context, not a full-paper audit.
External confluent-determinant and prime-asymptotic proofs were not audited and are not premises below.
Acquisition metadata remains in the literature registry; no new download, external search or novelty claim is made.

Throughout m=log M uses natural logarithms, d is actual degree, and Delta is the absolute polynomial discriminant, not the number-field discriminant.

<a id="finite-prime-discriminant-gap"></a>
## Direct finite-prime proof

Let alpha be a nonzero nontorsion algebraic integer of degree d>=2, with monic minimal polynomial P and conjugates alpha_i.
Fix a prime p with deg(alpha^p)=d.
Set Q(t)=product_i(t-alpha_i^p), Delta=|disc P| and D=d/Delta^(1/d).
Then Q is monic integral and squarefree, and M(Q)=M(P)^p.

The Frobenius congruence Q=P mod p gives p^d dividing Res(P,Q): write Q=P+pR and take the norm of Q(alpha)=pR(alpha).
The resultant is nonzero.
Indeed, if alpha_i^p=alpha_j, a Galois automorphism sigma of the splitting field sends alpha_i to alpha_j.
Iterating its finite order r gives alpha_i^(p^r)=alpha_i, contrary to nonzero nontorsion.

The quotient J=product_(i<j) (alpha_i^p-alpha_j^p)/(alpha_i-alpha_j) is an integer: each quotient is a polynomial in the roots, and their product is symmetric with integer coefficients.
Degree preservation makes J nonzero.
Hence |disc Q|=Delta J^2>=Delta.
This is the essential degree-preservation step.

Form the Vandermonde matrix W of the 2d distinct roots of P Q with powers 0 through 2d-1.
Its product formula and Hadamard inequality give

\[
 \Delta^2p^{2d}\le |\det W|^2
 =\Delta|\operatorname{disc}Q|\,|\operatorname{Res}(P,Q)|^2
 \le(2d)^{2d}M(P)^{2(2d-1)(p+1)}.
\]

Taking logarithms and dividing by 2d proves

\[
 \log\frac{p}{2D}\le (2-1/d)(p+1)m(\alpha). \tag{1}
\]

For fixed B>0 choose one prime p>2B.
On D<=B and deg(alpha^p)=d this gives

\[
 m(\alpha)\ge c_{B,p}:=\frac{\log(p/(2B))}{2(p+1)}>0. \tag{2}
\]

Only infinitude of primes is needed to choose p, not a quantitative distribution estimate.
Formula (2) is the weaker degree-free form of (1).
It matches Mat96 (7) with k=S=1, f(S)=log p and g(S)=p, as directed in the proof of Theorem 2.
The theorem statement gives the D<=1 case.
General fixed B is a direct specialization of that known mechanism, not a new unrestricted Lehmer bound.

<a id="discriminant-escape"></a>
## Vanishing entropy and restricted finite capture

Suppose alpha_n satisfy all-prime degree preservation and 0<m(alpha_n)->0.
Degree-one nonzero nontorsion integers have m>=log2, so eventually d_n>=2.
For each B choose the fixed prime above; (2) excludes D(alpha_n)<=B for all sufficiently large n.
Therefore

\[
 D(\alpha_n)\longrightarrow\infty,\qquad
 \frac{|\operatorname{disc}(\alpha_n)|^{1/d_n}}{d_n}\longrightarrow0. \tag{3}
\]

[L G0014](Yin_L_G0014_v1.md#power-degree-reduction) replaces any hypothetical vanishing positive-measure sequence by one satisfying those degree conditions, with no larger positive weights.
Endpoints of a sufficiently small unit sequence are reciprocal by the accepted nonreciprocal gap.
Formula (3) applies to the reduced sequence; twists need not preserve its original discriminant parameter.
This restricts possible counterexamples without constructing or excluding them.

For a concrete restricted rational-flow result, fix B>0 and a prime p>2B.
Assume a finite-entropy Q-linear flow has, for each positive monic unit primary factor, a root alpha with D(alpha)<=B and deg(alpha^p)=deg(alpha).
Such positive unit factors have degree at least two.
Every positive monic nonunit or nonmonic primitive factor has weight at least log2.
All positive weights are therefore at least eta=min(log2,c_(B,p))>0.
By the [L G0002 primary formula](Yin_L_G0002_v1.md#capture-equivalence), the sum of positive primary lengths is at most h_alg/eta.
Only finitely many positive types occur, and a finite set attains entropy.
Zero-entropy components may remain infinite-dimensional.
Neither a uniform B nor that common-prime hypothesis has been established for the unrestricted Task.

<a id="gram-cancellation-boundary"></a>
## Short-window Gram consequence

For a monic minimal P in the integer core, use [L G0004](Yin_L_G0004_v1.md#gram-lower-certificate)'s G_N and R_N=Delta G_N/N^d.
At N=2d,

\[
 R_{2d}=G_{2d}/(2D)^d.
\]

If R_(2d)>1, that record's upper bound Delta G_N<=N^d exp(2(N-1)m) gives

\[
 0<d^{-1}\log G_{2d}-\log(2D)\le(4-2/d)m. \tag{4}
\]

Along a hypothetical reduced vanishing-measure sequence passing positivity, D diverges while G_(2d)^(1/d)/(2D) tends to one.
Positivity is compatible with this precise cancellation.
An arithmetic strengthening must prevent it or supply a uniform positive lower bound for the difference in (4).
Discriminant integrality and the estimate above do not do so.

## Actual review and next obligation

The original author check is retained at [R509](../audits/reviews/Yin_R_G0509_v1.md#original-single-prime-author-check).
The complete current finite-prime and cover theorem is [C219](../claims/Yin_C_G0219_v1.md#statement), adopted after the [whole current self-review](../audits/reviews/Yin_R_G0509_v1.md#current-finite-prime-finding).

The remaining question is whether integer recurrence excludes D->infinity together with (4), or supplies another degree-uniform entropy bound.
Formula (2) tends to zero when B grows with an admissible prime; it does not close this obligation.
The known Mat96 multiprime asymptotic remains dependent on the discriminant parameter.
