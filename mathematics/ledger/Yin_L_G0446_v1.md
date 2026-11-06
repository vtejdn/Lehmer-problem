---
author: Yin
---
# Arithmetic random matrices: local ceilings and the original-measure return

## Scope and strategic assessment

This bounded exploration on 2026-11-05 tests arithmetic random-matrix mechanisms for [G0001](../tasks/Yin_T_G0001_v1.md#contract).
The actual current contract remains unresolved.
The fixed external [F0016 classification](https://github.com/vtejdn/yin-math-research/blob/d08144cfd271975b5808cd7e68d3b86c762b6f56/mathematics/claims/Yin_C_F0189_v1.md#statement) motivated the question; no source material is imported or adopted by this comparison.
All finite cycle identities needed here are derived directly.

The round found no new positive uniform arithmetic lower bound and no independently selectable new strategy with a supported gain mechanism.
The probability step for nonnegative cycle rewards can already be closed once the arithmetic mean is positive at linear scale.
The new all-prime first-Smith-layer ceiling is retained separately in [C867](../claims/Yin_C_G0867_v1.md#statement), whose own assessment and exact review own its acceptance.
The remaining comparisons below are complete author-checked explorations and source applicability checks, not independently reviewed Claims or a whole-Task review.
Their formal scope is the particular models and certificates inspected; no impossibility theorem for all arithmetic random matrices is asserted.

Retain the diagnostic within S3 and S8, with the entropy comparison available to S7, rather than create a new S merely for the unresolved mean lower bound.
A useful reopening must supply either original-input excess valuations or a sufficiently large genuinely contributing prime budget, or a changed integral ensemble with a proved original-measure return and new arithmetic information.
The actual contribution must exceed repeated cycle clocks, unimodular presentation changes, marginal CRT mixing and abstract orbit-count integrality.

## Original-scale upper interface

Let P be a monic irreducible noncyclotomic integer-unit polynomial of actual degree d, with full logarithmic measure m>0.
Put R_k=|Res(P,x^k-1)| and a_k=log R_k.
Every R_k is a nonzero positive integer, so a_k>=0.
For a uniform permutation pi_N, let C_k count its k-cycles.
Block diagonalization into cyclic shifts gives Y_N=log|det P(Pi_N)|=sum_(k<=N) C_k a_k.
Counting a distinguished k-cycle gives E C_k=1/k, hence E(Y_N/N)=N^(-1)sum_(k<=N)a_k/k.
No independence across different dimensions is needed for these finite statements.

Write Phi(t)=86 sqrt(t) log(1/t)^(5/2)/[log log(1/t)]^(3/2), on 0<t<=exp(-40).
[C147v5](../claims/Yin_C_G0147_v5.md#statement) gives a_k/d<=Phi(km/d) whenever km/d is in this domain.
Writing ell=log(1/t), direct differentiation gives d log Phi(t)/d log t=1/2-5/(2ell)+3/(2ell log ell)>=7/16.
Therefore Phi(t)<=Phi(T)(t/T)^(7/16) for 0<t<=T<=exp(-40).
Since sum_(k<=N) k^(-9/16)<=integral_0^N x^(-9/16)dx=(16/7)N^(7/16),

    E(Y_N/N)<=(16/7)(d/N)Phi(Nm/d).                 (RM1)

In particular E(Y_d/d)<=(16/7)Phi(m), uniformly in d when m<=exp(-40).
For any fixed C>=1 and d<=N<=Cd with Cm<=exp(-40), the bound is at most (16/7)Phi(Cm).
This is a direct summation of the accepted original-degree bound, not an automatic arithmetic lower bound or a newly independently reviewed result.
It does not convert a harmonic sum into a single large norm and therefore does not discard the harmonic normalization in [C450](../claims/Yin_C_G0450_v1.md#statement).

## Exact cycle law and the probability step

Block diagonalizing a permutation matrix and multiplying the eigenvalue factors on each cycle gives

    Y_N=log|det P(Pi_N)|=sum_(k<=N) a_k C_k,
    a_k=log R_k>=0,
    mu_N=E Y_N=sum_(k<=N) a_k/k.

The coefficient and exponent conventions are those of the original monic polynomial.
The factor corresponding to a k-cycle is exactly R_k, with all original conjugates retained.

For prescribed nonnegative integers r_k, count ordered disjoint marked cycles.
Choosing their symbols and cyclic orders, and then an arbitrary permutation on the unused symbols, gives

    E product_k (C_k)_(r_k)=product_k k^(-r_k)

when sum k r_k<=N; the expectation is zero otherwise.
Here (x)_r is the falling factorial.
Consequently Var(C_k)<=1/k and Cov(C_k,C_l)<=0 for k!=l.
For arbitrary deterministic nonnegative rewards a_k,

    Var(Y_N)<=sum_(k<=N) a_k^2/k<=a_max mu_N,
    E Y_N^2<=mu_N^2+a_max mu_N.                         (CY1)

For mu_N>0, split the expectation at Y_N=mu_N/2 and apply Cauchy--Schwarz on the upper event.
This gives

    Pr(Y_N>=mu_N/2)>=mu_N/[4(mu_N+a_max)].              (CY2)

This is the usual Paley--Zygmund argument, not a new probability inequality.
For its attribution, the original HTML of [Terence Tao's 2019 Notes 9, Exercise 5](https://terrytao.wordpress.com/2019/11/12/254a-notes-9-second-moment-and-entropy-methods/) was inspected on 2026-11-05: it states the nonnegative L2 variable inequality with factor (1-lambda)^2.
The finite setting here satisfies those hypotheses, and the complete Cauchy--Schwarz derivation is supplied locally.
The bounded source search used the terms Paley--Zygmund and second moment after the local probability-source search found no exact matching retained unit.
No full-source audit or priority claim is made.

The elementary all-root estimate is

    R_k<=2^d exp(km).

Thus at N=d and m<=M, a_max<=d(M+log 2).
If mu_d/d>=eta>0, then

    Pr(Y_d/d>=eta/2)>=eta/[4(eta+M+log 2)].             (CY3)

Conversely, Pr(Y_d/d>=a)>=p0 implies mu_d/d>=a p0 because Y_d>=0.
Therefore a uniform mean lower bound and a uniform positive-probability lower bound are quantitatively interchangeable on a bounded-m domain.
The probability step needs no advanced random-matrix concentration theorem; the missing input is the arithmetic mean lower bound itself.

## First Smith layer at every prime

[C867](../claims/Yin_C_G0867_v1.md#statement) retains the entire exact formula, multiplicity-stratum proof, uniform estimate and weighted-prime consequence.
For every monic P with constant coefficient plus or minus one, including repeated reductions,

    E nullity_(F_p) P(Pi_N)<=(2+p^(-1/2))sqrt(2d)H_N.

For N=d, a permutation-independent finite prime set S with sum_(p in S)log p=o(sqrt(d)/log(d+1)) therefore cannot produce a positive constant determinant-density certificate from its first Smith layers with fixed positive probability.
This controls that lower certificate alone; the full determinant and higher actual Smith layers remain unbounded by this statement.

## Every automatic good-prime lift still has vanishing density

Now let S consist of good primes for P.
Use [C256](../claims/Yin_C_G0256_v1.md#statement)'s original-root counts w_(p,o), with sum_o w_(p,o)=d and w_(p,o)<=phi(o), and its automatic lower floor

    A_S(k)=sum_(p in S,o|k)w_(p,o)(1+v_p(k))log p.

The random reward Y_S=sum_(k<=N)A_S(k)C_k is at most Y_N, but may be strictly smaller than the entire S-part of Y_N.
Since p does not divide o,

    1_(o|k)(1+v_p(k))=sum_(j>=0)1_(o p^j|k).

Therefore its exact expectation and the inspected [L159 capacity](Yin_L_G0159_v1.md#good-prime-short-order-capacity) give

    E Y_S=sum_(p in S,o,j>=0) [w_(p,o)log p/(o p^j)]
                                         H_floor(N/(o p^j))
          <=2H_N sqrt(2d)Theta_S.                       (AU1)

The full geometric factor is p/(p-1)<=2.
This includes all automatic lifts; repeated use of the same residue order creates no extra uncharged income.
At N=d its normalized expectation is at most 2H_d sqrt(2/d)Theta_S.
A probability bound Pr(Y_S/d>=a)>=p0 would require

    Theta_S>=a p0 sqrt(d)/(2sqrt(2)H_d).                (AU2)

That budget is necessary for this certificate, not sufficient for actual short-order root coverage.
Exceptional initial depths, true primitive excess and other primes remain possible sources of new arithmetic.

## Existing actual invisibility

[C536](../claims/Yin_C_G0536_v1.md#statement) supplies actual reciprocal irreducible units for every prescribed finite nonempty S and every even d=2r>=4, with all roots modulo p having order p^r+1 for each p in S.
The complete cyclic norms have v_p(R_k)=0 unless p^r+1 divides k.
Hence, for every fixed C, the entire S-part of every P(Pi_N) determinant is one for all N<=Cd once d is large enough.
This includes all actual depths and every realization of the permutation, not only the first-layer or automatic-floor estimates.
The constructed measures satisfy log(d+1)<=m(P)<=log((product_(p in S)p+4)d), so this is not a near-one counterexample.
Its relevance is to reject integrality, reciprocity and fixed-prime sampling alone as an automatic source of gain.

## Changed integral ensembles: reuse and source scope

The local bounded search used signed permutations, random signs, cycle signs, shears and modular randomization in Claims, ledger and S3/S6.
[C229](../claims/Yin_C_G0229_v1.md#statement) already identifies zero-excess integral unimodular matrices with signed permutations and retains the costs of leaving that class.
[C73](../claims/Yin_C_G0073_v1.md#statement) already proves that polynomial shears preserve the full scalar determinant while open-convolution sections carry an additional boundary charge.
These existing findings prevent treating random basis changes or uncharged boundary amplification as a new arithmetic source.

On 2026-11-05 a bounded primary-source search used randomized permutation characteristic polynomials, signed permutations and wreath products.
The published [Dehaye--Zeindler article](https://numdam.org/item/10.5802/aif.2802.pdf), Annales de l'Institut Fourier 63(4), 2013, pp. 1227--1262, was inspected at Section 4.2, Lemma 4.2, equation (4.4), and its displayed proof on printed pp. 1234--1235.
It gives the characteristic polynomial of a permutation with unit-circle weights as a product over cycles, with each cycle carrying the product of its weights.
The signed calculation below is a direct specialization and original-Mahler comparison, not a claim of novelty for the wreath-product model or cycle factorization.
No asymptotic theorem from that paper is used and no whole-source proof audit is claimed.
The search stopped because the exact needed structural formula was available and the remaining calculations below are finite identities.

<a id="signed-permutation-collapse"></a>
## Independent integral signs only replace the clock by twice the clock

Let P be a monic irreducible noncyclotomic integer unit polynomial of degree d, let alpha be a root, and retain K=Q(alpha).
For every k>=1 define

    R_k=|Norm_(K/Q)(alpha^k-1)|,
    T_k=|Norm_(K/Q)(alpha^k+1)|.

Both are nonzero positive integers, and R_(2k)=R_k T_k.
The noncyclotomic irreducibility excludes alpha^k=+1 and alpha^k=-1, and no extension field or powered-degree normalization is taken.

Let pi be uniform on S_N, and independently choose epsilon_1,...,epsilon_N uniformly in {+1,-1}.
Put S=D_epsilon Pi, a uniform integral orthogonal matrix.
On a permutation cycle c of length k, S has characteristic polynomial x^k-sigma_c, where sigma_c is the product of the signs on that cycle.
One proof writes S e_j=epsilon_(pi(j)) e_(pi(j)), takes k powers around the cycle, and notes that the first basis vector is cyclic.
The products sigma_c are independent fair signs conditional on pi, because distinct cycles use disjoint sign coordinates.

The block resultant formula therefore gives

    |det P(S)|=product_(c:sigma_c=+1) R_(|c|)
               product_(c:sigma_c=-1) T_(|c|).

P(S) is invertible over Q, its determinant is a nonzero integer, and no reduced-determinant convention is needed.
With X_N=N^(-1)log|det P(S)|, conditional expectation is exactly

    E[X_N | pi]=(1/(2N))sum_(cycles c) log R_(2|c|).

Indeed the two possible cycle contributions have mean (log R_k+log T_k)/2=(log R_(2k))/2.
For a uniform permutation the expected number of k-cycles is 1/k: choosing its k symbols, their (k-1)! cyclic orders and the arbitrary remaining permutation yields binomial(N,k)(k-1)!(N-k)!/N!=1/k.
Consequently

    E X_N=(1/(2N))sum_(k=1)^N (log R_(2k))/k.       (S1)

The N independent coordinate signs reduce to one fair sign per cycle, and after averaging even those signs disappear into the original doubled-time norms.
This formula does not furnish a lower bound for their full arithmetic mass.

There is also an exact bound for every choice of signs, including choices depending on P and on pi.
Since R_k and T_k are positive integers, both are at least one and

    max(log R_k,log T_k)<=log R_(2k).

As long as the underlying permutation remains uniform,

    0<=E X_N<=(1/N)sum_(k=1)^N (log R_(2k))/k.       (S2)

Thus adaptive choice of signs improves this upper comparison by at most a factor two over the fair-sign mean.
This includes all sign correlations; it is not a restriction to independent signs in (S2).
Biasing the permutation itself is a different operation with different cycle weights and is outside this identity's uniform-marginal assertion.

<a id="signed-small-mahler-return"></a>
### Full small-Mahler return and the remaining lower-bound obligation

Write m=m(P), and use [C147v5](../claims/Yin_C_G0147_v5.md#statement) with its original degree and full norm convention.
For 2m<=exp(-40), it gives log R_(2k)<=d Phi_5(2km/d) for 1<=k<=d.
For 0<t<=exp(-40), put ell=log(1/t).
Direct differentiation gives

    d log Phi_5(t)/d log t
       =1/2-5/(2ell)+3/(2ell log ell)>=7/16.

Hence Phi_5(2km/d)<=(k/d)^(7/16)Phi_5(2m).
The decreasing-function integral comparison gives

    sum_(k=1)^d k^(-9/16)<=integral_0^d x^(-9/16)dx
                              =(16/7)d^(7/16).

Substituting in (S1)--(S2), with actual matrix dimension N=d, yields

    fair signs: E X_d <=(8/7)Phi_5(2m),
    arbitrary chosen signs: E X_d <=(16/7)Phi_5(2m). (S3)

Both upper bounds tend uniformly to zero with the original m.
A lower estimate Pr(X_d>=a)>=p_0 with absolute positive a,p_0 on all sufficiently near-one inputs would contradict (S3) and prove a positive gap.
No such estimate has been obtained: the cycle identities reduce its possible arithmetic content to the existing full original norms R_(2k).
All results here are a direct working comparison using the accepted C147 input, not a new independently reviewed Claim.

### Scope of the integral norm-one restriction

Every real orthogonal integer matrix is a signed permutation: each integer column has squared Euclidean length one, so has exactly one nonzero entry, equal to +1 or -1; orthogonality forces those positions to be distinct.
The same conclusion holds for an invertible integer matrix of Euclidean operator norm at most one.
Its integer columns have lengths at least one and at most one, and invertibility prevents repeated occupied rows.
Thus replacing the ensemble by another distribution on integral orthogonal matrices does not escape the signed-cycle description.
Products of independent such matrices also remain in that group.
This does not classify nonorthogonal integral matrices, random matrices over larger coefficient rings, or several signed matrices occurring in a genuinely noncommuting polynomial.

<a id="unimodular-randomization-boundary"></a>
## Random unimodular bases preserve the arithmetic statistic exactly

Let C be the integral companion matrix of the same original P, and let U,V be arbitrary random matrices in GL_d(Z).
For each fixed k>=1,

    |det(U(I-C^k)V)|=|det(I-C^k)|=R_k.

Moreover U and V are invertible modulo every rational prime, so the mod-p rank and Smith invariant factors of this presentation are unchanged.
For the invariant factors, U and V are invertible over Z and therefore induce isomorphic cokernels; this is an exact module isomorphism, not a distributional approximation.
Random conjugation C'=UCU^(-1) also gives det(I-(C')^k)=det(I-C^k).
These randomizations can alter entries and singular vectors, but they create no averaging gain in the determinant or its prime divisibilities.
An argument using their randomness would still have to prove a new theorem about that unchanged invariant of the original P.
This complements, rather than supersedes, C73's exact same-P polynomial-shear and finite-boundary calculation.

<a id="nonconjugating-shear-control"></a>
## A nonconjugating shear creates an artificial positive determinant floor

To test what happens when the same-scalar protection is removed, take the actual cyclotomic source

    P_0(x)=x^2+1, C_0=[[0,-1],[1,0]], m(P_0)=0,
    U_t=[[1,t],[0,1]], t uniformly chosen from {+4,-4}.

Then

    U_t C_0=[[t,-1],[1,0]],
    det(xI-U_t C_0)=x^2-tx+1,
    det(I-U_t C_0)=2-t.

Therefore B_t=I-U_t C_0 is an invertible integer matrix in both outcomes, and

    (1/2)log|det B_t| >=(1/2)log2>0,
    E[(1/2)log|det B_t|]=(1/4)log12.

The source is the irreducible cyclotomic polynomial x^2+1, so there is no nilpotent or reducible-source explanation for this extra gain.
The one-sided shear has changed the full characteristic polynomial: its expanding root has modulus 2+sqrt3, so the new total Mahler measure is log(2+sqrt3) in both outcomes.
The source's original measure remains zero.
Consequently this ensemble cannot obey a return estimate E X<=Psi(m(P)) with Psi(0)=0 on a domain containing this source.
Nor can its positive determinant floor by itself be credited to noncyclotomic arithmetic.
This control does not disprove a specially constructed return theorem restricted to noncyclotomic near-one inputs; that would require an actual additional theorem using that restriction.
It rules out the unrestricted return for this concrete mixing mechanism and makes its added scalar cost explicit.

## Assessment and a discriminating continuation

The inspected integral orthogonal and unimodular-basis randomizations do not furnish a substantively new arithmetic lower-bound mechanism.
The fair-sign ensemble has a complete original-measure upper return, but its expectation is exactly an old doubled-time norm statistic.
The elementary nonconjugating shear supplies positive growth without original Mahler control, already on a cyclotomic input.
These two facts are obstacles for the specified mechanisms, not a refutation of all arithmetic random matrices or G0001.

A useful new model must retain an explicit original-P determinant/norm comparison while changing the arithmetic information beyond signed-cycle clocks or unimodular presentation.
For a proposed noncommuting integral pencil, the first discriminating test is to compute its full determinant at cyclotomic companion inputs and to identify precisely which term could be bounded by the original m(P) as degree grows.
If it has a nonvanishing positive baseline there, a stated subtraction or quotient must retain integrality or replace it by another proved arithmetic input; omitting that baseline is not a return theorem.
No such corrected model with both a uniform return and a new lower probability estimate has been obtained in this bounded comparison.

## Inverse concentration does not remove the degree/time cost

Let alpha be an algebraic unit of degree d, let epsilon_j be independent fair bits, and put Z_n=sum_{j=0}^{n-1} epsilon_j alpha^j.
Write H for Shannon entropy in natural logarithms and p_max for the largest atom.
The first d powers are linearly independent over Q, so H(Z_n)=n log 2 and p_max(Z_n)=2^{-n} for n<=d.
Conditioning on the remaining digits gives p_max(Z_n)<=2^{-d} for n>=d.
Consequently, these short-time bounds distinguish no noncyclotomic arithmetic gap; they hold for degree-d cyclotomic examples as well.

The full exponential-scale obstruction is already retained in [C G0286](../claims/Yin_C_G0286_v1.md#power-orbit-inverse-time-cost), rather than being a new result of this preparation.
For 0<epsilon<log 2, its elementary dissociation argument converts p_max>=exp(-epsilon n) only into a signed spanning set of size at most epsilon n/log 2.
For the power orbit, that probability hypothesis can hold only once n>=d log 2/epsilon, when the allowed rank is already at least d.
Its [generic rank obstruction](../claims/Yin_C_G0286_v1.md#generic-exponential-rank-obstruction) prevents replacing this with a bounded-rank conclusion for arbitrary weights.

The primary-source check of Tao--Vu, [A sharp inverse Littlewood--Offord theorem](https://arxiv.org/pdf/0902.2357), v2, Theorems 1.9--1.10, confirms that the parameters controlling the rank, exceptional set and implicit constants are fixed before n grows.
Substituting a polynomial-probability exponent A=epsilon n/log n supplies no uniform constants in the exponential regime.
The repository's [NV11 interface](../audits/literature/NV11/Yin_U001.md) already records the analogous boundary for the optimal inverse theorem.
No new inverse theorem for the special multiplicative power orbit was established here.

## Finite quotients retain arithmetic but do not create independence

Put R=Z[alpha].
For a finite-index ideal I, the quotient random variable W_n=Z_n mod I satisfies H(W_n)<=log|R/I|.
Therefore a fixed quotient, or any fixed finite collection of quotients, has zero asymptotic entropy rate even if its distribution becomes uniform.
The relevant original rate is h(alpha)=lim_{n to infinity} H(Z_n)/n; the limit exists by subadditivity because multiplication by the nonzero alpha is injective.
The existing [BV20 interface](../audits/literature/BV20/Yin_U003.md) gives h(alpha)<=m(alpha), with m the total logarithmic Mahler measure.
A positive uniform lower bound for h(alpha) would thus suffice, but this is the existing affine-entropy problem.

Let I_1,...,I_k be pairwise comaximal finite-index ideals and W_j=Z_n mod I_j, using the same bit sequence in every coordinate.
The Chinese remainder theorem identifies the joint residue space, whereas the entropy chain rule gives exactly

\[
H(Z_n\bmod\bigcap_{j=1}^k I_j)
=\sum_{j=1}^k H(W_j\mid W_1,\ldots,W_{j-1}).
\]

There is no corresponding lower bound by the sum of the marginal entropies without a separate independence or conditional-entropy estimate.
For example, a fair bit reduced modulo 2 and modulo 3 has joint entropy log 2, although its two marginal entropies sum to 2 log 2.
The quotient coordinates remain dependent even though the ideals are comaximal.
Thus independent mixing estimates for the factors cannot be added as fresh randomness.

The inspected finite-field lead is also already recorded in [S7's source boundary](../strategies/Yin_S_G0007.md#unadopted-finite-field-source-leads).
Its retained reading of Breuillard--Varju, [Cut-off phenomenon for the ax+b Markov chain over a finite field](https://arxiv.org/abs/1909.09053), v2, Theorem 5, requires a sufficiently large multiplicative order and gives a prime-field mixing time with additional logarithmic factors.
It supplies neither uniform joint mixing for the quotient product above nor an extension-field statement for every reduction of alpha.
The abstract was rechecked in this round; the theorem scope and costs here are reused from S7, not asserted from a fresh proof audit.

## Generic random cokernels are not the original arithmetic ensemble

Nguyen--Wood, [Random integral matrices: universality of surjectivity and the cokernel](https://arxiv.org/pdf/1806.00596), v1, Theorem 1.1, concerns independent identically distributed integer entries with a polynomial size bound and a quantitative balance condition modulo primes.
For fixed rectangular excess it gives limiting probabilities of fixed finite cokernel groups.
This does not itself give an exponential lower bound for determinant size: escaping every fixed finite group does not specify a linear logarithmic rate.
The paper's discussion also explicitly distinguishes dependence between reductions of an entry modulo different primes from its entrywise independence hypotheses.

For a fixed integer polynomial P and permutation matrix Pi, the entries of P(Pi) have algebraic and cycle dependence and do not satisfy that independent-entry model.
Left or right multiplication by random unimodular integer matrices preserves both the cokernel and absolute determinant; it therefore cannot establish a new size lower bound merely by changing presentation.
A universality transfer to this dependent ensemble would itself require a new theorem with quantitative constants and a mechanism retaining P's arithmetic constraints.
No such transfer was obtained or assumed.

## A fixed-prime negative control

Consider the standard comparison ensemble A_n with independent normalized Haar entries in Z_p, and let V_n=v_p(det A_n).
The Gaussian-elimination recursion in Evans, [Elementary divisors and determinants of random matrices over a local field](https://statistics.berkeley.edu/sites/default/files/tech-reports/614.pdf), Section 4, pages 9--10 of the July 8, 2002 text, yields the following elementary expectation calculation.
For the first-column minimum r, P(r>=k)=p^{-nk}, so E r=1/(p^n-1).
After division by p^r, a matrix in GL_n(Z_p) sends the primitive column to the first basis vector.
Conditionally on that column, Haar invariance leaves the other columns independent and Haar, so the remaining determinant has the law of det A_{n-1}.
Starting with V_0=0 gives

\[
\mathbb E V_n
=\sum_{j=1}^n\frac{1}{p^j-1}
\le \frac{p}{(p-1)^2}.
\]

For a fixed finite prime set S, the sum of log p times these expected valuations is consequently O_S(1), not a positive constant times n.
This is a known-model comparison, not a new theorem about P(Pi).
It excludes only the naive explanation by generic local behavior at finitely many fixed primes; it does not exclude a growing prime set or arithmetic dependence producing exceptional valuations.

## Exact remaining statement and assessment

A concrete sufficient replacement would be the following conditional-entropy statement for every noncyclotomic algebraic unit alpha, with absolute constants a,B>0.
For every sufficiently large n, choose pairwise comaximal finite-index ideals I_{n,1},...,I_{n,k(n)} such that

\[
an\le\sum_j\log|R/I_{n,j}|\le Bn,
\qquad
\sum_j\left(\log|R/I_{n,j}|
-H(W_j\mid W_1,\ldots,W_{j-1})\right)
\le\frac12\sum_j\log|R/I_{n,j}|.
\]

Here each W_j is the residue of the same Z_n, and the onset in n may depend on alpha.
The chain rule and data processing would imply h(alpha)>=a/2 and hence m(alpha)>=a/2.
The second inequality is the missing arithmetic conditional-mixing lemma, not an output of CRT, marginal mixing, inverse concentration or cokernel universality.
Any attempted proof must retain its dependence on degree, reduction order, mixing time and the number of previously exposed quotients.

Without the capacity and conditional-defect estimates, choosing larger finite quotients merely rewrites the original entropy question: since R is a free abelian group of finite rank, a sufficiently large integer modulus separates the finite support of each Z_n exactly.
The inspected sources give no independent accessibility argument for the displayed uniform estimates.
Retain this as a diagnostic inside the existing entropy/finite-quotient route and do not promote it to a new Strategy on the strength of this round.

## Source and inspection scope

The bounded searches and primary-source reads above were performed on 2026-11-05 to test exponential-scale inverse concentration, dependent quotient mixing and quantitative cokernel size.
Tao--Vu v2 was inspected through its introductory theorem statements; Nguyen--Wood v1 through Theorem 1.1 and its introductory dependence discussion.
Evans was inspected at the ensemble definition and Section 4 recursion, Theorem 4.1 and its elimination argument; the expectation deduction above is included to make this comparison checkable without importing its full distribution formula.
The BV finite-field abstract was read, while its exact theorem applicability is reused only within the existing S7 reading boundary.
These are scoped applicability checks, not independent reviews of the cited proofs or a comprehensive literature search.
No external theorem is being adopted as a new Claim, and no uninspected external source is needed for the bounded negative conclusion.

## Positive determinant moments and orbit-count integrality

Another possible source of arithmetic information is the whole expectation of the determinant rather than its logarithm.
Put D_N=exp(Y_N) and A_N=E D_N, with A_0=1.
The number of permutations with specified counts c_k satisfying sum k c_k=N is N!/product(k^(c_k)c_k!).
Summing that exact formula gives the formal identity

    sum_(N>=0) A_N z^N=exp(sum_(k>=1) R_k z^k/k).     (RM2)

Let B be the integer companion automorphism of P on the torus R^d/Z^d.
Since B^k-I is nonsingular, its kernel on the torus has cardinality |det(B^k-I)|=R_k, by the integer lattice index.
The points of exact finite period l split into finite orbits of size l; write their number of orbits as O_l, a nonnegative integer.
Then R_k=sum_(l|k) l O_l, so (RM2) is product_(l>=1)(1-z^l)^(-O_l).
In particular every A_N is an integer, with nonnegative coefficients in this formal product.
This supplies genuine integer combinatorics, but Jensen has the direction E log D_N<=log E D_N.
A positive lower bound for log A_N/N cannot be substituted for one for E Y_N/N.

The following exact control also rules out obtaining a uniform exponential rate solely from positive integral periodic-orbit data and primitivity.
Take a finite directed graph with two loops of lengths L and L+1, sharing their initial vertex and with all other vertices disjoint, where L>=2.
The graph is strongly connected and its cycle-length gcd is one.
For its integer adjacency matrix A, determinant expansion over vertex-disjoint cycles gives det(I-zA)=1-z^L-z^(L+1), since the two cycles cannot be selected simultaneously.
The formal identity exp(sum tr(A^k)z^k/k)=1/det(I-zA) follows by differentiating both sides at z=0 and matching constant term one.
This is again a nonnegative integer orbit-count series.
Its positive growth root lambda_L solves 1=lambda_L^(-L)+lambda_L^(-(L+1)); thus 1<lambda_L<=2^(1/L), and log lambda_L tends to zero.
Consequently positive integral orbit data, even from primitive finite graphs, do not alone force a uniform exponential rate.
These graphs are not asserted to realize the full reciprocal toral spectrum of a near-one G0001 input.
The control identifies the extra structure a successful use of (RM2) must exploit; it is not a Lehmer counterexample.

## Search and inspection scope

On 2026-11-05 the main agent searched for toral dynamical zeta formulas and multiplicative permutation class functions after recognizing (RM2).
The primary abstracts of [Zeindler, arXiv:0910.5069v2](https://arxiv.org/abs/0910.5069v2) and [Baake--Lau--Paskunas, arXiv:0810.1855v2](https://arxiv.org/abs/0810.1855v2) confirm the respective generating-function and toral-zeta settings.
Only those abstracts were inspected; no full-source theorem, novelty claim or source-proof verification is imported.
The identities actually used above are derived directly, so no further original passage is needed for this comparison.
