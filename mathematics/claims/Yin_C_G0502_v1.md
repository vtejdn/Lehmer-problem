---
author: Yin
---
# Exact complete one-expanding Gaussian pressure and analytic versus actual controls

The complete original argument and every source/contribution/cost/domain/negative boundary are retained.
The original L remains meaningful development and a fixed review input; no research Task/E resumes.

## Statement

For EVERY real beta>1 put rho=beta^-1, a0=log2, a=a0*beta^2, c=a0*(beta^2-1)>0 and

    H(z)=(1-rho*z)/(1-beta*z)=sum_(j>=0)h_j*z^j,
    h0=1, h_j=(beta-rho)*beta^(j-1) for j>=1.

For EVERY integer n>=1 let C_n be the REAL UPPER coefficient matrix h_(j-i) for j>=i and0 below, and v_n=(1,beta,...,beta^(n-1))^T.
The EXACT finite identities and singular values are

    C_n^T C_n=rho^2*I+(1-rho^2)*v_n*v_n^T,
    a*C_n^T C_n=a0*I+c*v_n*v_n^T,
    singular values: rho repeated n-1 times, beta^(n-1),
    det C_n=1.

For ORIGINAL independent difference digits Pr(xi=0)=1/2,Pr(xi=+/-1)=1/4 and S_n(beta)=sum_(j=0)^(n-1)beta^j*xi_j, the COMPLETE UNshifted partition has

    Z_n=sum_(e in{-1,0,1}^n)exp[-a*norm(C_n e)^2],
    Gamma_n=2^-n*Z_n=E_original exp[-c*S_n(beta)^2].

Every word and its full weight is present; this is no Gaussian replacement of the discrete digits.
With c_a=1+2exp(-a), g(log beta)=log(2/c_a) and G_n=log(c_a^n/Z_n), G_n>=0 and -log Gamma_n/n=g(log beta)+G_n/n.
The matrix orientation and n1 boundary are part of the exact statement.

For EVERY algebraic integer beta>1 of ACTUAL degree d whose actual monic irreducible polynomial has beta as its ONLY conjugate of modulus greater than1, let q count ALL unit-circle conjugates with both nonreal members, and define

    C_st=product_(abs(alpha_i)<1)(1-abs(alpha_i))^-1,
    B=2^(d-1)*C_st, delta_n=(B*n^q)^-1.

Empty products and degree1 are included, with no unit or reciprocity hypothesis.
Distinct ORIGINAL difference-word support points are separated by at least delta_n, using coefficient differences bounded by2 and EVERY other stable/neutral embedding.
The exact maximum displacement atom is at0 by the finite binary-endpoint Cauchy--Schwarz identity.
For EVERY n>=1,

    p_n:=Pr_original(S_n=0)<=Gamma_n
       <=[1+B*sqrt(pi/c)*n^q]*p_n.

The complete original collision exponent exists and, at each FIXED input,

    lim_n -log Gamma_n/n=h2(beta)=lim_n -log p_n/n,
    lim_n G_n/n=h2(beta)-g(log beta),
    TOTAL m(P)=log beta.

The explicit B/q/c cost may deteriorate arbitrarily with the input; no uniform changing-degree/root/measure convergence or onset is claimed.
This covers actual Pisot/Salem beta>1 in the stated one-expanding domain, not a theorem obtained by dropping further exterior conjugates.
It does not evaluate h2, prove h2=m, recurrence, finite critical mean or a Mahler gap.

For EACH integer k>=1, set beta_k=2^(1/k) and the ANALYTIC rank-one parameter m_k=(log2)/k.
The full original density/tail argument gives positive finite input-dependent A_k,B_k and all sufficiently large n with

    A_k*beta_k^-n<=Gamma_n(beta_k)<=B_k*beta_k^-n,
    lim_n -log Gamma_n(beta_k)/n=m_k,
    lim_n G_n/n=m_k-g(m_k),
    [m_k-g(m_k)]/m_k ->1-log2 as k->infinity.

This uses the proved finite dyadic uniform distribution and convolution of k scaled triangular densities, with exact deterministic tail beta_k^-n/(beta_k-1); no normal approximation, almost-everywhere parameter theorem or unproved density assumption is used.
The n limit is taken first for each fixed k; all density constants may depend on k.
The COMPLETE analytic loss can be linear in small m_k beyond the particular O(m_k^2) first-lag certificate, while its total rate still tends to0.

For the SAME numerical beta_k the ACTUAL irreducible minimal polynomial is P_k=t^k-2, of degree k, with ALL k conjugates exterior and TOTAL m(P_k)=log2.
For k>1 it fails the one-expanding hypothesis; the analytic m_k must not be relabelled as arithmetic total measure.
Its full actual inverse and Gaussian precision are

    H_actual=(1-(1/2)*z^k)/(1-2*z^k), a_actual=4log2.

For EVERY n>=0, coordinate permutation by residues modulo k gives exactly Gamma_n^actual=product_(a=0)^(k-1)Gamma_(n_a)(2), sum_a n_a=n, Gamma_0(2)=1.
With Cstar=sum_(s in Z)exp[-3(log2)*s^2]<infinity,

    2^-n<=Gamma_n^actual<=Cstar^k*2^-n,
    p_n(beta_k)=2^-n,
    h2(beta_k)=lim_n -log Gamma_n^actual/n=log2.

Empty residue blocks, full digit normalization, actual Eisenstein degree and strict leading-digit dominance are retained.
This is a fixed-positive-total-measure nonunit family, not a near-one reciprocal counterexample.
All results concern the COMPLETE unshifted limiting inverse matrix; no arbitrary-translation bound, growing-window substitution into actual finite matrices, uniform input cost, unrestricted gap or Task completion follows.

<a id="argument"></a>
## Complete original argument

The following complete original author body is historical at its original date; its initial/pending/next-direction language supplies no current research authority.
Same-scope mathematical href maintenance does not backdate current home reading; every original L/R input and date remains fixed.

## Exact Gaussian partition rates at one expanding conjugate

<a id="one-expanding-gaussian-reuse"></a>
### 1. Changed question, reuse and scope

Date:2026-10-10.
The coordinating AI for Yin develops this argument.
The unrestricted G0001 contract remains active and unresolved.
This is an author argument awaiting complete separate review.

The changed question concerns the ENTIRE unshifted limiting Gaussian partition, rather than a sum of selected entry losses.
[L268](Yin_C_G0475_v1.md#statement) already proves the finite Blaschke inverse defect rank and gives the analytic family (1-exp(-m)z^r)/(1-exp(m)z^r).
Its spectrum alone was not a digit-probability estimate.
[L271](Yin_C_G0487_v1.md#statement) removes a first-lag density loss but retains a small certified amplitude; [L272](Yin_C_G0490_v1.md#statement) computes the limitation of its different fully paid threshold recipe.
Neither is an upper bound on actual entropy.

The needed arithmetic inputs already exist.
[L83's norm separation](Yin_C_G0274_v1.md#norm-separation-with-central-loss) keeps every stable and unit-circle embedding and the polynomial neutral loss.
[C560's maximum displacement atom](Yin_C_G0560_v1.md#all-state-return-dominance), reusing L173/L186, is the Cauchy--Schwarz inequality for a difference of two independent binary endpoint laws.
We use that elementary inequality for all nonzero algebraic integers; its two-line proof below does not require a unit inverse or a return core.
The change from binary endpoint differences to differences of difference-endpoints doubles the coefficient bound and is charged explicitly.
A bounded G-ledger screen for Gaussian pressure, one-factor inverses, norm separation and original return comparisons located these adequate interfaces, but not the following complete unshifted comparison.
No literature-wide novelty is claimed.

The new result identifies the complete unshifted Gaussian exponent with the actual collision exponent when there is just one expanding conjugate.
It also evaluates an arbitrarily-small-parameter analytic control, and restores its actual minimal polynomial to show precisely which arithmetic data the relaxed control discarded.
All proofs are written here; no numerical test, new J or external source theorem is needed.
The dyadic uniform-series fact used below is proved directly from its finite dyadic intervals.
The concurrent D140--D142 arguments are not inputs and have not been read.

<a id="rank-one-complete-gaussian-partition"></a>
### 2. Exact finite rank-one partition identity

Let beta>1 be any real number, not yet assumed algebraic, and put

    m=log beta, rho=beta^(-1), a0=log2,
    a=a0 beta^2, c=a0(beta^2-1)>0,
    H(z)=(1-rho z)/(1-beta z)
        =1+sum_(j>=1) h_j z^j,
    h_j=(beta-rho) beta^(j-1), j>=1.                 (1)

This is precisely L268's one-factor normalized inverse, with h0=1.
For n>=1 let C_n be the REAL UPPER triangular matrix with entry h_(j-i) at j>=i and zero below the diagonal.
Thus this is the transpose of L268's lower coefficient-matrix convention.
Set v_n=(1,beta,...,beta^(n-1))^T.
Direct finite geometric summation gives

    C_n^T C_n=rho^2 I+(1-rho^2)v_n v_n^T,
    a C_n^T C_n=a0 I+c v_n v_n^T.                  (2)

For clarity, its diagonal at i is 1+sum_(l=1)^i h_l^2=rho^2+(1-rho^2)beta^(2i).
At i<j, the entry is h_(j-i)+sum_(l=1)^i h_l h_(l+j-i)=(1-rho^2)beta^(i+j).
These include i=0 and n=1.
The finite matrix has n-1 singular values rho and one beta^(n-1); the latter follows by applying the rank-one matrix to v_n and summing its squared coordinates.
Its determinant remains1.
No asymptotic or coefficient truncation is used.

Let xi_j be independent digits with the ORIGINAL difference law

    Pr(xi=0)=1/2, Pr(xi=1)=Pr(xi=-1)=1/4,
    S_n(beta)=sum_(j=0)^(n-1) beta^j xi_j.

Define the complete unshifted partition and its normalized value by

    Z_n(beta)=sum_(e in{-1,0,1}^n) exp[-a ||C_n e||^2],
    Gamma_n(beta)=2^(-n) Z_n(beta).

Since exp(-a0 e^2)/2 is exactly the displayed digit law, (2) gives the FINITE identity

    Gamma_n(beta)=E exp[-c S_n(beta)^2].             (3)

Every one of the3^n words, its full weight, every coefficient and the entire rank-one direction are retained.
This is not a Gaussian approximation to those digits.
It is an exact Gaussian function averaged under their discrete law.

For comparison with L267/L271 write c_a=1+2exp(-a), g(m)=log(2/c_a) and G_n=log(c_a^n/Z_n).
Then

    -log Gamma_n/n=g(m)+G_n/n.                      (4)

The L267 nonnegative complete-block loss applies to this real unit upper triangular matrix at zero translation, so G_n>=0.
We do not assert a translated maximum or identify Z_n with the actual finite quotient matrix before its input-dependent limiting onset.
Formula (3) instead supplies a direct comparison with the original law in the next section.

<a id="one-expanding-soft-return-comparison"></a>
### 3. Actual algebraic inputs: only a polynomial separates the two quantities

Now suppose beta>1 is a nonzero algebraic integer of actual degree d, with actual monic irreducible minimal polynomial P.
Assume beta is its ONLY conjugate of modulus greater than1.
Count the unit-circle conjugates, including both members of a complex pair, as q.
Put

    C_st=product_(|alpha_i|<1) (1-|alpha_i|)^(-1),
    B=2^(d-1) C_st >=1,
    delta_n=(B n^q)^(-1), n>=1.                    (5)

The empty product is1.
Pisot inputs have q=0; Salem inputs have q=d-2.
No reciprocal, unit or degree bound is needed for the stated one-expanding-conjugate result.

Let p_n(beta)=Pr(S_n(beta)=0), the COMPLETE original collision probability.
For two distinct support points s,t of S_n, their difference is a nonzero algebraic integer R(beta), where deg R<n and every integer coefficient has absolute value at most2.
At a contracting conjugate its value is bounded by2/(1-|alpha_i|), and at a unit-circle conjugate by2n.
The nonzero integer absolute norm is at least1.
Since there is only ONE expanding conjugate, this proves

    |s-t| >= delta_n.                               (6)

This is L83's norm-separation argument at the actual doubled coefficient bound.
In particular it does not replace projected real points by integers or discard neutral conjugates.
All degree and root-shape dependence stays in B and q.

For the atom bound let nu_n be the actual binary endpoint law, formed with independent fair0/1 digits.
Its difference law is the law of S_n.
For every actual endpoint s,

    Pr(S_n=s)=sum_x nu_n(x)nu_n(x-s)
       <=(sum_x nu_n(x)^2)^(1/2)
         (sum_x nu_n(x-s)^2)^(1/2)
       =p_n.                                       (7)

Extend nu_n by zero on the finite union of its translated supports when necessary.
This is exactly the reused maximum-atom calculation and uses no group-inverse transition rule.

The support contains0.
By(6), the kth positive support point is at least k delta_n, and the absolute value of the kth negative one is at least k delta_n.
Therefore

    sum_(s in supp S_n) exp(-c s^2)
      <=1+2sum_(k>=1) exp[-c(k delta_n)^2]
      <=1+sqrt(pi/c)/delta_n.

The last inequality compares a decreasing Gaussian sum with its integral on[0,infinity).
Combining it with(3),(7) and the exact zero term yields the complete finite comparison

    p_n <= Gamma_n
        <=[1+B sqrt(pi/c) n^q] p_n.                 (8)

No omitted return states, relative tail assumption or finite core is used.
The prefactor may depend very badly on P and beta; it has not been bounded uniformly over changing inputs.

The original collision exponent exists: independent zero-sum blocks give p_(n+k)>=p_n p_k, and p_r>=2^(-r).
For any fixed k and n=lk+r,0<=r<k, this bounds the limsup of -log p_n/n by -log p_k/k.
Taking the infimum over k gives equality with the liminf.
Consequently (8) proves

    lim_(n->infinity) -log Gamma_n(beta)/n
        =h2(beta):=lim_(n->infinity)-log p_n(beta)/n,
    lim_(n->infinity) G_n/n=h2(beta)-g(log beta).     (9)

On this ACTUAL domain, total logarithmic Mahler measure is log beta.
The limits in(9) are for each fixed input.
Neither uniform convergence in varying degree/m nor a degree-free prefactor follows.

Equation(9) says that the complete unshifted limiting inverse partition retains the entire exponential collision information in the one-expanding-conjugate case.
This is stronger than selecting a few entries, but is not an evaluation of the difficult exponent.
It does not prove h2=log beta, positive recurrence, finite critical mean or a uniform positive gap.
It also makes no assertion about arbitrary outside translations in an actual finite-block upper bound.
General inputs with several expanding conjugates require their full joint geometry; keeping just one coordinate would invalidate(6).

<a id="small-parameter-analytic-partition-control"></a>
### 4. A fully evaluated analytic control with parameter tending to zero

For each integer k>=1 take beta_k=2^(1/k), so m_k=(log2)/k.
Use the rank-one matrices(1)--(3) with this beta and with their ANALYTIC parameter m=m_k.
This is the existing L268 analytic class at r=1, not a degree-one algebraic minimal polynomial.

We prove its complete normalized partition has EXACT exponent m_k.
Let

    T_infinity=sum_(j>=1) beta^(-j) xi_j,
    T_n=sum_(j=1)^n beta^(-j) xi_j,
    b_beta=1/(beta-1), epsilon_n=beta^(-n).

The deterministic tail bound is

    |T_infinity-T_n|<=b_beta epsilon_n.             (10)

Reversing the iid digits shows S_n has the same distribution as beta^n T_n.
Splitting the infinite series by residues1,...,k modulo k gives a sum of INDEPENDENT random variables

    T_infinity=sum_(a=1)^k beta^(-a) X_a,
    X_a=sum_(l>=0) 2^(-l) xi_(a+kl).                (11)

Here each X_a has density (2-|x|)/4 on[-2,2].
To verify this without a source theorem, write xi as the difference of two independent fair bits.
The random number sum_(l>=0) 2^(-l-1) bit_l is uniform on[0,1]: each half-open dyadic interval of length2^(-r) prescribes its first r bits, has probability2^(-r), and the exceptional eventually constant expansions have probability zero.
These intervals determine the uniform law.
Thus X_a is twice the difference of two independent uniforms; its density is the stated triangular function, directly obtained by the overlap length of two intervals.

Every scaled summand in(11) has a bounded continuous density positive near0.
Their finite convolution f is bounded and continuous, and f(0)>0: integrate over a small box where the first k-1 arguments and their negative sum all lie in intervals of strict positivity.
Hence there exist K<infinity, b>0 and eta>0, depending on k, such that

    f(x)<=K for every x,   f(x)>=b for |x|<=eta.

These are finite-input constants, not uniform constants as k grows.
When epsilon_n<=eta, (10) gives

    Pr(|T_n|<=(b_beta+1)epsilon_n)
       >=Pr(|T_infinity|<=epsilon_n)>=2b epsilon_n.

Consequently (3) has the lower bound

    Gamma_n>=2b exp[-c(b_beta+1)^2] epsilon_n.

For every u>=0, the other direction of(10) gives Pr(|T_n|<=u epsilon_n)<=2K(u+b_beta)epsilon_n.
Use exp(-c y^2)=integral_(|y|)^infinity 2cu exp(-cu^2) du and nonnegative integration to obtain

    Gamma_n
       <=2K epsilon_n [b_beta+sqrt(pi)/(2sqrt c)].

Thus there are positive finite constants A_k,B_k, independent of n, with

    A_k beta_k^(-n)<=Gamma_n(beta_k)
         <=B_k beta_k^(-n) for all sufficiently large n,
    lim -log Gamma_n(beta_k)/n=m_k ->0.             (12)

No almost-everywhere parameter theorem, numerical density assumption or limiting normal approximation enters.
In particular the complete block, including all large inverse coefficients and every spectral direction, can have arbitrarily small exponential rate within this analytic relaxation.

By(4),(12) its entire loss rate is EXACTLY

    lim G_n/n=m_k-g(m_k),
    [m_k-g(m_k)]/m_k ->1-log2>0 as k->infinity.      (13)

For the last equality differentiate the explicit g at0: g(0)=0 and g'(0)=log2.
Thus the complete-block improvement can be linear in the small analytic parameter even though the first-lag certified increment in L271 is only O(m^2).
The evaluated total rate nevertheless remains m_k.
This distinguishes a limitation of the selected certificate from the actual whole-partition loss.
It is not a counterexample to any arithmetic Mahler gap.

<a id="restored-minimal-degree-dyadic-control"></a>
### 5. Restoring every conjugate in the same numerical root

For the very same number beta_k, the actual minimal polynomial is

    P_k(t)=t^k-2,    actual degree k,
    actual total m(P_k)=log2.                       (14)

For completeness, P_k is irreducible by the elementary Eisenstein argument at2: in a nontrivial factorization into monic integer factors, reduction modulo2 forces both constant coefficients even, contradicting constant coefficient -2 not divisible by4.
Such a monic factorization would exist if a monic primitive integer polynomial were reducible over Q, by the usual rational-denominator clearing/Gauss lemma.
All k roots have modulus beta_k>1.
Hence their complete product of exterior moduli is beta_k^k=2.
The one-expanding-conjugate hypothesis of Section3 fails when k>1, even though the chosen real root tends to1.

The full inverse formed from ALL exterior roots is

    H_actual(z)=(1-(1/2)z^k)/(1-2z^k).               (15)

This follows directly by multiplying the factors over all kth roots of unity.
Its constant normalization is exp(-m(P_k))=1/2, its exterior count is r=k, and its actual Gaussian coefficient a is4log2.
After reordering finite coordinates by residues modulo k, its upper matrix is a direct sum of the rank-one blocks from Section2 with beta=2.
This reordering permutes the complete digit cube and original product weights; it is an exact factorization, not an uncharged change of integer lattice.

Let n_a count the coordinates of residue a in0,...,n-1, so sum_a n_a=n and some n_a may vanish.
Define Gamma_0(2)=1.
The FULL actual normalized partition is

    Gamma_n^actual=product_(a=0)^(k-1) Gamma_(n_a)(2). (16)

For a length l block at beta=2, a fair binary endpoint is uniform on the integers0,...,2^l-1.
Thus its difference atom at s is (2^l-|s|)/4^l for |s|<2^l, zero otherwise, and p_l(2)=2^(-l).
With c=3log2, (3) gives the explicit all-length bounds

    2^(-l)<=Gamma_l(2)<=C_*2^(-l),
    C_*=sum_(s in Z) exp[-3(log2)s^2]<infinity,

including l=0 by C_*>=1.
Therefore

    2^(-n)<=Gamma_n^actual<=C_*^k 2^(-n),
    lim -log Gamma_n^actual/n=log2.                 (17)

The same exponent is the EXACT original collision exponent.
Since1,beta,...,beta^(k-1) are Q-linearly independent, a zero original digit sum splits into k independent residue sums at powers of2.
A nonzero finite signed base2 sum with digits{-1,0,1} cannot vanish: its leading magnitude2^L exceeds the sum2^L-1 of all smaller magnitudes.
Hence every digit must be0, and

    p_n(beta_k)=2^(-n) for every n>=0,
    h2(beta_k)=log2.                                (18)

This is a nonunit family with fixed positive total measure, not the hard reciprocal near-one class.
Equations(12) and(17)--(18) exhibit exactly the difference between a one-root analytic relaxation and the same root's complete actual algebraic data.
The discarded k-1 expanding conjugates cannot be restored by calling log beta_k the total measure.

### 6. What this changes and author self-check

The positive new interface is (8)--(9): on the entire one-expanding-conjugate domain, including actual Salem inputs, the full unshifted inverse Gaussian partition has precisely the original collision exponent, with an explicit finite polynomial comparison and all neutral/degree expenses.
It can therefore serve as a complete pressure object for further exact analysis.
A uniform original-law estimate still needs the arithmetic behavior of that full partition; entrywise loss, inverse amplitude and spectrum are partial data.

The independently evaluated analytic family shows why a proposed universally positive bound based only on this one-factor analytic class would be false.
It simultaneously shows that the full loss can be of linear order beyond the small first-lag certificate.
Restoring the actual irreducible polynomial gives the full fixed measure log2, exact factorized partition and exact collision law.
None of these comparisons asserts that every reciprocal near-one input has one expanding conjugate, or that a low analytic parameter is arithmetically realizable at rank1.

The author has checked both matrix orientations and all finite diagonal/off-diagonal identities; the exact digit normalization and factor2^n; doubled coefficient norm separation and all stable/neutral conjugates; the zero atom and Gaussian packing constant; collision-exponent existence; every tail/density bound and its input dependence; the unshifted versus arbitrarily translated distinction; actual irreducibility, full exterior count and both measures; empty residue blocks and all-length dyadic bounds.
The local dependency statements are sufficient, and no current subagent proof, unseen external statement or numerical observation supplies a premise.
Complete separate noncontributor review and fixed adoption are pending.

Author freeze:2026-10-10T02:51.
Complete Sections1--6 and equations(1)--(18) passed the author self-check and scoped material check1.
No computation or source acquisition was run.
The entire body is now frozen for separate full review.

## Current assessment
[Selected decision](#decision-complete-whole-self-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T01:55 |
| status | open |
| reason | Register the complete original theorem and every actual domain, finite/infinite quantifier, full probability, source, contribution, cost and negative boundary. Sufficient existing inputs are reused; inspection of the actually written whole target, a real whole finding and adoption remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete one-expanding and analytic-actual theorem](#statement) | Every real beta>1 exact finite matrix/original-law identity, actual one-expanding algebraic-integer comparison, EACH fixed-k analytic full rate and restored actual all-k-root/minimal-degree partition/collision controls with all costs and limits. |
| argument | [Complete original proof](#argument) | Entire original starting/reuse/Sections1--6/equations1--18/all matrix orientations/norm-atom-packing/dyadic-density-tail/limit/minimal-degree/residue-factorization/actual all-length law/contribution/self-check/source and negative scope. |
| dependency | [Complete actual inverse/compression](Yin_C_G0475_v1.md#argument) | Exact normalized one-factor analytic and full-exterior inverse conventions/finite compression, no probability consequence borrowed from spectrum alone. |
| dependency | [Whole Gaussian nonnegative loss](Yin_C_G0469_v1.md#finite-block-entropy-loss-identity) | Complete arbitrary real unit-upper/zero-shift full Gaussian law G>=0 at a>=log2; no translated maximum claimed here. |
| support | [Complete norm-separation comparison](Yin_C_G0274_v1.md#norm-separation-with-central-loss) | Original unit/binary support norm mechanism and stable/neutral/complex expenses; present proof explicitly re-proves its doubled-coefficient/nonunit word application. |
| support | [Original exact maximum-atom interface](../ledger/Yin_L_G0232_v1.md#all-state-return-dominance) | Actual fixed unit/core original interface as comparison; present complete finite convolution proof applies to nonunits without a state-kernel extension. |
| support | [Earlier first-lag certificate](Yin_C_G0487_v1.md#first-nonzero-lag-full-density) | Complete actual certified O(m^2) increment limit only, not an upper bound on whole Gaussian pressure or entropy. |
| support | [Different paid threshold recipe](Yin_C_G0490_v1.md#statement) | Complete existing all-threshold/o(m) certificate limitation, without suppressing onset/degree/density or inferring an entropy upper bound. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T02:08 |
| status | proved |
| reason | The actually written open Statement and complete Argument have been fully read and checked under the explicit entire SELF finding. Adopt that complete mathematical scope with every original input-dependent cost and analytic-versus-actual restriction. Original author SELF and R175 original whole independent/date/fixed inputs remain historical at their actual scopes; no research Task/E resumes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete one-expanding and analytic-actual theorem](#statement) | Every real beta>1 exact finite matrix/original-law identity, actual one-expanding algebraic-integer comparison, EACH fixed-k analytic full rate and restored actual all-k-root/minimal-degree partition/collision controls with all costs and limits. |
| argument | [Complete original proof](#argument) | Entire original starting/reuse/Sections1--6/equations1--18/all matrix orientations/norm-atom-packing/dyadic-density-tail/limit/minimal-degree/residue-factorization/actual all-length law/contribution/self-check/source and negative scope. |
| dependency | [Complete actual inverse/compression](Yin_C_G0475_v1.md#argument) | Exact normalized one-factor analytic and full-exterior inverse conventions/finite compression, no probability consequence borrowed from spectrum alone. |
| dependency | [Whole Gaussian nonnegative loss](Yin_C_G0469_v1.md#finite-block-entropy-loss-identity) | Complete arbitrary real unit-upper/zero-shift full Gaussian law G>=0 at a>=log2; no translated maximum claimed here. |
| support | [Complete norm-separation comparison](Yin_C_G0274_v1.md#norm-separation-with-central-loss) | Original unit/binary support norm mechanism and stable/neutral/complex expenses; present proof explicitly re-proves its doubled-coefficient/nonunit word application. |
| support | [Original exact maximum-atom interface](Yin_C_G0560_v1.md#all-state-return-dominance) | Actual fixed unit/core original interface as comparison; present complete finite convolution proof applies to nonunits without a state-kernel extension. |
| support | [Earlier first-lag certificate](Yin_C_G0487_v1.md#first-nonzero-lag-full-density) | Complete actual certified O(m^2) increment limit only, not an upper bound on whole Gaussian pressure or entropy. |
| support | [Different paid threshold recipe](Yin_C_G0490_v1.md#statement) | Complete existing all-threshold/o(m) certificate limitation, without suppressing onset/degree/density or inferring an entropy upper bound. |
| review | [Entire current SELF finding](../audits/reviews/Yin_R_G0712_v2.md#one-expanding-whole-self-finding) | ENTIRE actual Statement and complete original Argument, all six sections/equations1--18, exact finite original law, all polynomial norm costs, EACH fixed-k analytic density/rate and restored actual all-conjugate/minimal-degree/full partition/collision control, source/contribution and every negative boundary. |
