---
author: Yin
---

# Height-controlled exact dyadic descent and primitive-input limits for canonical residual certificates

Human author Yin.
Provenance: project deduction within the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root authored the height-controlled reconstruction and primitive-input HD1--HD7 argument and proposed the height1 binary-support application.
The characteristic_zero_bridge agent checked that entire argument, supplied exact trace-derivative descent and the maximal-base parity proof, and developed the height1 finite certificate and genuine-Salem corollary.
Root read and checked the completed HD1--HD13 candidate; both agents are contributors and neither supplies an independent review of this result.
The complete full-norm descent interface is credited to adopted C586v2, not presented as a new project theorem.
No native mathematical computation, new source acquisition or new uninspected external theorem is used.

## Statement

Let C_0=2,C_1=X,C_(r+1)=X C_r-C_(r-1), so C_r(z+z^(-1))=z^r+z^(-r).
For every positive-degree monic integer T define the SAME actual canonical integer polynomials

    a_T=rem_T(T(C_2))/2,
    b_T=rem_T(T(C_3))/3, c_T=rem_T(T(C_5))/5,
    F_T=rem_T(2c_T^2-3a_T^5),
    X_(s,T)=rem_T(b_T^2-a_T^3+s(c_T^3-2b_T^5)),
    G_T=rem_T(c_T^3-2b_T^5), s in{1,-1}.

All divisions and remainders are the actual integral ones in this one T.
For any monic polynomial P put H(P)=max_i|[z^i]P|, S(P)=max_(|z|=1)|P(z)| and let m(P) be its complete logarithmic Mahler measure with multiplicities.
For a nonzero integer polynomial R, ord_2(R) denotes the minimum2-adic valuation of its nonzero coefficients; set ord_2(0)=infinity.
The C720 functions used below are

    A_F(S)=2S^2/25+3S^5/32,
    A_X(S)=S^2/9+S^3/8+S^3/125+2S^5/243,
    Theta(P)=max{log A_F(S(P))+10m(P),
                     log A_X(S(P))+15m(P)},
    kappa=61319/243000,
    U(N,m)=m+(9/2)sqrt(N)+(log N)/(2sqrt(N))
           +sqrt(N(2log N+7)(2m+log N+4)), N>=8.

All logarithms are natural unless written log_2.
Theta is used as an exact finite sufficient-certificate threshold only in C720's irreducible nontorsion reciprocal integer-unit domain.

A. Let ell,b>=1 be integers, T monic integral of degree D>=1, T' in2^ell Z[X], P(z)=z^D T(z+z^(-1)), N=2D, and H(P)<2^b.
Set j=max(0,ell-b+1), k=2^j.
Then a UNIQUE monic reciprocal Q in Z[z] of constant coefficient1 and full EVEN degree N/k exists with

    P=Q(z^k), T=T_0(C_k), deg T_0=D/k,
    H(Q)=H(P), S(Q)=S(P), m(Q)=m(P).

Its trace polynomial T_0 is the unique monic integer one.
For EACH R in{a,b,c,F,X_s,G}, one has the exact INTEGER polynomial identity

    R_T=R_(T_0)(C_k),
    ord_2(R_T)=ord_2(R_(T_0)).

Zero and nonzero polynomials, both separately fixed signs, all multiplicities and the endpoint k=1 are included.
The algebraic reconstruction requires no irreducibility or total reality.
For EVERY actual nonconstant trace composition T=T_0(C_(2^j)), independently of the height premise,

    ord_2(T')=j+ord_2(T_0').

In A this implies T_0' in2^(ell-j)Z[X].
The stronger observable condition S(P)<2^b can replace the height premise.

B. If P in A is ALSO irreducible and nontorsion, then Q is irreducible and nontorsion, and Theta(P)=Theta(Q).
For an integer n>=0, if both original residuals are divisible by2^n, N/k>=8, and

    n log2>5U(N/k,m(P))+15m(P)+log kappa,

then both BASE and both ORIGINAL residuals vanish identically in characteristic zero.
This uses an actual reconstructed integer Q and its entire trace field; it does not divide the degree in an original-field norm by convention.
For alpha a root of P, beta=alpha^k, F=Q(alpha+alpha^(-1)) and F_0=Q(beta+beta^(-1)), the complete prior norm identities are [F:F_0]=k, Norm_F(g)=Norm_(F_0)(g)^k and Norm_(Q(alpha))(g)=Norm_(F_0)(g)^(2k) for every descended canonical value g.
No total-reality, new precision, decreased measure or automatically passing input is supplied.

C. Call P dyadically primitive when it is not Q(z^2) for any integer polynomial Q; this concerns ACTUAL integer support.
For every irreducible nontorsion reciprocal trace input with T' in2^(n+1)Z[X], n>=1, and dyadically primitive P,

    S(P)>=H(P)>=2^(n+1),
    Theta(P)>log(2/243)+5(n+1)log2+15m(P)>n log2.

Every genuine Salem minimal polynomial is dyadically primitive, so this TRUE-PC3 certificate obstruction covers every genuine Salem input with that same derivative/precision premise.
It does not assert nonzero residuals or exclude other precision, other methods or exact identities.
More generally, for an irreducible nontorsion reciprocal P let j be its MAXIMAL integer dyadic exponent and Q its primitive base.
Then Q always has even degree, including when j>=ell, so actual trace reconstruction and all canonical identities above hold at that maximal base.
If T' in2^ell Z[X] and j<ell, then

    S(P)=S(Q)>=H(Q)>=2^(ell-j),
    Theta(P)>[5(ell-j)+1]log2-5log3+15m(P).

Any integer n>=0 for which nlog2>Theta(P) must therefore satisfy

    5(ell-j)<n-1+5log_2 3-15m(P)/log2

in that j<ell case.
For j>=ell only the trivial height floor1 is asserted from this specified derivative lower bound; no negative exponent is used.
The even-base conclusion uses actual irreducibility and nontorsion and is not asserted for arbitrary reducible reciprocal inputs.

D. Independently of a derivative premise, suppose P is monic irreducible reciprocal nontorsion integral with constant1 and H(P)=1, and its actual binary reduction is Pbar=Rbar^q, q=2^u, u>=0, where Rbar is monic, nonconstant, has constant1 and is NOT a square in F_2[z].
Then its maximal INTEGER dyadic exponent is EXACTLY u, and the actual base satisfies

    P=Q(z^q), Qbar=Rbar, H(Q)=1,
    deg Q=deg Rbar=:r,
    S(Q)=S(P), m(Q)=m(P).

The actual Q is irreducible, nontorsion and reciprocal, r is even, and its trace polynomial of degree r/2 gives all six canonical identities with exact coefficient precision as in A.
For a fixed Rbar the bases belong to a finite family of coefficient sign choices of fixed degree, not a family of freely chosen residual coordinates; no irreducibility of all choices or ascents is asserted.
If s is the number of nonzero coefficients of Rbar including its endpoints, then

    S(Q)<=s, m(Q)<=log s,
    Theta(P)=Theta(Q)<=20log s+log kappa.

Thus for ANY integer n>=0, both original residual congruences modulo2^n and

    n log2>20log s+log kappa

force BOTH base and original residuals to be exactly zero.
This finite certificate is independent of q for the specified binary source and requires no small-measure assumption.
It supplies no actual height1 lift or passing input, no equality of synthetic and actual canonical Haar data and no unrestricted G0001 conclusion.
Outside height1, maximal integer composition and maximal binary Frobenius power are distinct quantities and are never identified here.

## Complete argument

<a id="height-controlled-exact-desubstitution"></a>
### Small actual height forces an exact dyadic trace desubstitution

Root authored the following candidate while investigating the true-S alternative left open by C722.
The local Claim-title pass found the accepted C697 exact composition interface and C720's full original-domain circle/norm account adequate; the earlier sparse-factor constructions have different hypotheses and are not premises here.
The characteristic_zero_bridge agent checked the full HD1--HD7 as coauthor, supplied the exact trace-derivative descent and maximal-base parity proofs, and developed the height1/support and genuine-Salem applications below.
This is new contributor mathematics, with no independent review or claimed characteristic-zero realization.
No native mathematical computation or new external theorem is used.

Let ell>=1 and b>=1 be integers, T in Z[X] monic of degree D>=1, and suppose T' is coefficientwise divisible by2^ell.
Put P(z)=z^D T(z+z^(-1)), N=2D, and let H(P) be the maximum absolute coefficient of the ACTUAL P.
Assume

    H(P)<2^b, j=max(0,ell-b+1), k=2^j.             (HD1)

Then there is a unique monic reciprocal Q in Z[z], of constant coefficient1 and full even degree N/k, such that

    P(z)=Q(z^k).

Its unique monic integer trace polynomial T_0 has degree D/k and

    T=T_0(C_k),
    H(Q)=H(P), S(Q)=S(P), m(Q)=m(P).                (HD2)

Here S is the actual circle supremum and m the complete logarithmic Mahler measure, with every root counted.
The case k=1 is allowed and yields no degree reduction.
If P is irreducible and nontorsion, Q has those properties as well.
The full canonical polynomials a,b,c,F,X_s of C697 satisfy their exact composition identities in HD2; in particular both residuals of T_0 have exactly the same coefficient2-adic orders as the corresponding residuals of T, with infinity for the zero polynomial.
The same holds for the canonical G=rem_T(c^3-2b^5), by that same monic-division argument.
Consequently actual vanishing and nonvanishing are preserved.
For irreducible nontorsion P, C720's TRUE threshold Theta is exactly preserved; its U threshold can instead be evaluated at the genuinely smaller full degree N/k when N/k>=8.
This is an actual integral polynomial reconstruction, not a change of degree convention in a norm of the original field.
All later norms for Q use its own entire trace field and degree.
Under these irreducible nontorsion hypotheses, for an original root alpha and beta=alpha^k, set F=Q(alpha+alpha^(-1)) and F_0=Q(beta+beta^(-1)).
The accepted [C586v2 exact norm descent](Yin_C_G0586_v2.md#exact-self-composition-descent-and-every-original-norm-factor), at its [actual adopted scope](Yin_C_G0586_v2.md#decision-complete-current-self-adoption), gives

    [F:F_0]=k,
    Norm_(F/Q)(g)=Norm_(F_0/Q)(g)^k,
    Norm_(Q(alpha)/Q)(g)=Norm_(F_0/Q)(g)^(2k)

for every actual descended canonical polynomial value g, including the residuals.
These are retained prior identities: F and F_0 have degrees D and D/k by actual irreducibility, and each base embedding has exactly k extensions to F.
No total reality is required, no smaller own field of g replaces F_0, and no new norm income is obtained by changing to the actual base.

For the proof the leading coefficient of T' gives2^ell|D, so k|D and N/k is even.
Differentiating the Laurent trace identity gives

    P'(z)=z^(D-1)[D T(z+z^(-1))
                    +(z-z^(-1))T'(z+z^(-1))].     (HD3)

Both terms on the right have integer Laurent coefficients divisible by2^ell.
Their sum is the actual polynomial derivative, so P' is coefficientwise divisible by2^ell.
For every nonzero coefficient c_i of P with i>=1, the integer identity2^ell|i c_i and |c_i|<2^b imply v_2(c_i)<=b-1 and hence v_2(i)>=ell-b+1.
If this lower bound is negative it imposes no condition, exactly as in HD1.
Thus k divides every index carrying a nonzero coefficient, proving the unique integral Q by coefficient extraction.
Monicity, reciprocity and constant coefficient1 pass to Q, and its degree is N/k.
An integer reciprocal Laurent polynomial z^(-D/k)Q(z) is a unique integral polynomial in z+z^(-1): pair its opposite powers and use the monic recurrence C_r(z+z^(-1))=z^r+z^(-r).
This constructs T_0 with integral coefficients and leading coefficient1.
Substituting z^k into its trace identity and comparing with P gives HD2's trace composition; injectivity of X->z+z^(-1) follows from the top Laurent term of a nonzero polynomial.

If Q factors over Q, substituting z^k gives a nontrivial factorization of P over Q, so irreducibility descends.
If Q had only roots of unity, all k-th roots of those roots would also be roots of unity, so nontorsion descends by contrapositive.
No assertion that irreducibility ascends for an arbitrary Q is used.
The coefficient lists give H(Q)=H(P).
The circle map z->z^k is surjective, giving S(Q)=S(P).
Every root gamma of Q, counted with its multiplicity, has k roots of modulus |gamma|^(1/k) in P, contributing together log^+|gamma| to the full measure; this proves m equality without normalization.

The accepted [C697 exact covariance](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) applies to every monic integer T_0 and C_k.
For a nonzero integer residual R_0=2^v H_0 with H_0bar nonzero, its composition reduces after division by2^v to H_0bar(X^k), since k is dyadic.
Distinct monomial degrees remain distinct, so the result is nonzero and the exact order stays v.
Nonconstant integer composition is injective, which also handles zero versus nonzero residuals.
For G explicitly write c_0^3-2b_0^5=T_0 Q_G+G_0 by actual monic integer division.
Composing with C_k gives the corresponding numerator for T=T_0(C_k), and deg G_0(C_k)<deg T, so its actual canonical remainder is exactly G_0(C_k).
This proves the G covariance before applying the same exact coefficient-order argument.
C720's Theta depends only on S and m, proving its equality; the smaller-degree U application is legitimate only after using this actual Q in all hypotheses.

The height premise can be replaced by the stronger observable condition S(P)<2^b, because the Fourier coefficient integral gives |c_i|<=S(P).
For a prescribed integer precision n>=0, irreducible nontorsion P satisfying HD1 and both residual congruences modulo2^n therefore gives an exact finite C720 test on Q at its full reconstructed degree.
If N/k>=8 and

    n log2>5U(N/k,m(P))+15m(P)+log kappa,           (HD4)

both base residuals vanish identically, and so do both original residuals by exact composition.
This sufficient implication supplies no currently passing example.
It does not contradict C722: after removing k, the base derivative need only be divisible by2^(ell-j), and its same-precision hypothesis need no longer hold.
Indeed P' coefficients i k c_(ik) give Q' divisible by2^(ell-j).
The exact trace-derivative descent is proved below: its coefficient2-adic order drops by exactly j under the actual trace desubstitution, so T_0' is divisible by2^(ell-j) here, with no larger guaranteed divisor inferred.

A high derivative exponent at small coefficient height therefore forces an actual tower structure whose base preserves the relevant analytic and residual data.
This neither creates extra bits nor decreases the full measure; it exposes a smaller actual candidate on which the finite certificate can be evaluated honestly.
No bounded height or circle supremum for the actual finite-construction inputs is proved here, and no equality of synthetic and canonical Haar data follows.


<a id="primitive-input-true-circle-obstruction"></a>
### The true-circle test also fails on dyadically primitive derivative-prepared inputs

Root continued the preceding author deduction with the following sharper domain distinction.
Call an actual P dyadically primitive here when there is no Q in Z[z] with P(z)=Q(z^2); this is a definition about integer exponents, not a claim about maximal binary Frobenius multiplicity.
Suppose T' is divisible by2^(n+1), n>=1, and P=z^D T(z+z^(-1)) is irreducible, nontorsion and dyadically primitive.
Then

    S(P)>=H(P)>=2^(n+1),
    Theta(P)>log(2/243)+5(n+1)log2+15m(P)
               >n log2.                          (HD5)

Thus even the TRUE C720 PC3 sufficient test at that same precision cannot be met in this smaller primitive domain.
This supplies no nonexistence statement for exact residual identities and no claim that the actual constructed P is primitive.

For proof, (HD3) gives coefficientwise2^(n+1)|P'.
Primitivity means some coefficient c_i is nonzero at an odd positive index i; otherwise extracting the even indices would give P=Q(z^2).
The integer divisibility2^(n+1)|i c_i forces2^(n+1)|c_i, proving the height and Fourier-supremum floor.
Since A_X(S)>(2/243)S^5, the first strict threshold inequality follows at the true S and full m.
For the second, after exponentiation and division by2^n the factor is at least2^(4n+6)/243, which is greater than1 already at n=1 because2^10=1024>243; exp(15m)>1 only increases it.
No rounded upper bound on S was used to infer this obstruction.

More generally let P be an actual monic irreducible reciprocal nontorsion integer-unit polynomial of constant coefficient1, and let j be the maximum integer for which P equals Q(z^(2^j)).
Let Q be that dyadically primitive integer polynomial.
It exists because P is nonconstant; j is the minimum2-adic valuation among all positive indices with nonzero coefficients.
The maximal base Q is irreducible and nontorsion by the same factor/root argument already given.
It is reciprocal with constant coefficient1.
If its degree were odd, reciprocity would give Q(-1)=0; irreducibility and monicity would force Q=z+1, contradicting nontorsion.
Thus Q has even degree for EVERY j, so2^j|D and the full trace reconstruction and residual equalities in HD2 apply to this actual base even when j>=ell.
This parity conclusion uses the actual irreducibility and nontorsion hypotheses; it is not asserted for an arbitrary reducible reciprocal polynomial.
If T' is divisible by2^ell and j<ell, the remaining derivative exponent is positive.
Coefficient differentiation gives Q' divisible by2^(ell-j), hence

    S(P)=S(Q)>=H(Q)>=2^(ell-j),
    Theta(P)>[5(ell-j)+1]log2-5log3+15m(P).        (HD6)

If j>=ell, this height bound is replaced by the trivial floor1; no negative derivative exponent is used.
The even-degree trace base nevertheless exists in the present irreducible nontorsion domain by the parity proof just given.
Any input satisfying n log2>Theta(P) must therefore, in the j<ell case, obey

    5(ell-j)<n-1+5log_2 3-15m(P)/log2.            (HD7)

In particular a same-precision derivative condition ell>=n+1 forces a substantial exact dyadic composition before that true-circle test can possibly pass.
The resulting base retains actual residual precision and total measure; it need not retain the same high derivative exponent.
These conclusions identify a necessary structure for this sufficient-certificate route, not a construction of a passing base or a universal necessary structure for a solution of G0001.


<a id="exact-trace-derivative-descent"></a>
### Exact derivative loss and the parity of the maximal base

For a nonzero integer polynomial A, write ord_2(A) for the minimum2-adic order of its nonzero coefficients.
Let k=2^j with j>=0 and let T=T_0(C_k) be an ACTUAL nonconstant integer trace composition, with T_0 monic.
Then

    ord_2(T')=j+ord_2(T_0').                       (HD8)

No irreducibility or height assumption is needed for this exact identity.
For j=0, C_1=X and the formula is immediate.
For every j>=0, repeated differentiation of C_(2u)=C_u^2-2 gives

    C_(2^j)'=2^j product_(r=0)^(j-1) C_(2^r).

The empty product at j=0 is1, and every displayed factor is monic integral.
Hence

    T'=2^j T_0'(C_k) product_(r=0)^(j-1) C_(2^r).

Composition by a monic positive-degree integer polynomial preserves ord_2: after dividing an input by its exact coefficient2-adic power, its nonzero binary reduction remains nonzero under the corresponding positive-degree monic composition.
Multiplication by a monic integer polynomial also preserves ord_2, since the corresponding binary factors are nonzero and F_2[X] has no zero divisors.
These observations prove HD8, retaining the nonzero derivatives in characteristic zero.
In HD1, j<=ell, so HD8 supplies T_0' in2^(ell-j)Z[X].
For a maximal dyadic base j>=ell, HD8 is still valid and implies ord_2(T')>=j; it creates no negative exponent premise.
Together with the preceding irreducible reciprocal parity proof, this closes both provisional base-trace and derivative qualifications at their actual hypotheses.

<a id="salem-primitive-derivative-corollary"></a>
### Every genuine Salem input belongs to the primitive domain

A genuine Salem minimal polynomial P has exactly one root outside the unit circle, its positive real root beta>1.
If P were Q(z^2), then -beta would also be a distinct root outside the unit circle, a contradiction.
Thus every genuine Salem polynomial is dyadically primitive in the exact integer sense used above.
Consequently, for EVERY genuine Salem trace input satisfying T' in2^(n+1)Z[X] at an integer n>=1, HD5 applies and

    Theta(P)>n log2.                              (HD9)

This excludes the TRUE C720 PC3 certificate at that same guaranteed precision throughout this derivative-prepared Salem domain, not merely on C711's constructed representatives.
It supplies no nonzero-residual assertion and does not exclude exact identities or a stronger precision at which the corresponding derivative premise is absent.
The statement uses the full Salem root count; it is not applied to the non-Salem higher members of C711's tower.

<a id="height-one-binary-source-descent"></a>
### Height1 fixes the integer dyadic base of a prescribed binary source

Let P be monic, irreducible, reciprocal and nontorsion in Z[z], with constant coefficient1 and H(P)=1.
Suppose its ACTUAL coefficient reduction is

    Pbar=Rbar^q, q=2^u, u>=0,
    Rbar in F_2[z] monic and nonconstant,
    Rbar(0)=1, Rbar not a square.                  (HD10)

No derivative-divisibility hypothesis is needed in this separate application.
Since every coefficient of P is0,1 or-1, its nonzero integer support is exactly its binary support.
Over F_2 one has Rbar^q=Rbar(z^q), and a nonsquare binary polynomial has a nonzero coefficient at some odd positive index.
Therefore the minimum2-adic order of a positive supported exponent of P is EXACTLY u.
The maximal integer dyadic decomposition is consequently

    P(z)=Q(z^q), Qbar=Rbar,
    H(Q)=1, deg Q=deg Rbar=:r,
    S(Q)=S(P), m(Q)=m(P).                         (HD11)

The actual Q is monic, integral, reciprocal, irreducible and nontorsion.
The preceding parity argument forces r even; in particular no such actual input can have an odd-degree Rbar.
Its monic trace polynomial T_0 has degree r/2, the original trace polynomial is T=T_0(C_q), and all six canonical polynomials a,b,c,F,X_s,G obey exact composition with EXACT coefficient2-adic precision and vanishing preserved.
The base degree r and its finite coefficient support depend on the fixed Rbar, not q.
Each nonzero coefficient of Q is a choice of sign at a fixed supported index, with the monic, constant and reciprocal constraints retained; the actual possible bases form a finite subset of this finite sign family.
No claim is made that every sign choice is irreducible or that irreducibility ascends under every q.

Let s be the number of nonzero coefficients of Rbar, including its endpoints.
The ACTUAL coefficient l1 sum of Q is exactly s, hence

    S(Q)<=s, m(Q)<=log S(Q)<=log s,
    Theta(P)=Theta(Q)<=20log s+log kappa.          (HD12)

The measure bound is the accepted C720 circle/Mahler inequality, with the original complete measure of Q.
Its PC12 coefficient bounds give the last inequality, retaining the actual15m radial term and5log S term.
Thus if, for an integer n>=0, both original canonical residuals are coefficientwise divisible by2^n and

    n log2>20log s+log kappa,                     (HD13)

then both BASE residuals vanish identically by C720 PC3, and so do both ORIGINAL residuals by exact composition.
This is a finite explicit certificate independent of the dyadic q for the fixed binary source, with no assumption of small total measure.
It supplies no height1 lift or passing example.
Increasing q alone in a pure actual tower preserves exact residual precision, and even allowing varying height1 lifts of this fixed binary source only selects among the finite fixed-degree bases; it does not supply unconstrained new residual coordinates.

Outside height1, an even nonzero integer coefficient can disappear modulo2, so the maximal integer dyadic exponent need not equal the maximal binary Frobenius exponent.
No such equality is used in HD1--HD9.
The height1 hypothesis is exactly what permits the support equality in HD10--HD11; no height1 bound is currently established for the constructed finite-precision family.
Root and the characteristic_zero_bridge agent are contributors to this entire HD1--HD13 candidate; a fresh independent whole review remains separate.


## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision height-controlled-descent-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T16:30 |
| status | open |
| reason | Register the entire HD1--HD13 theorem and proof after contributor checking. Actual derivative and strict height information force an integral dyadic reconstruction with even trace base, exact analytic and all-six canonical data, derivative-order loss and fully retained norm multiplicities. Primitive and genuine Salem inputs have a true-circle certificate obstruction at the stated precision; maximal bases and the height1 binary-source application have their precise parity and support hypotheses. The fixed-support finite certificate does not supply a height1 or bounded-height input, and no synthetic Haar identification or unrestricted completion follows. Fresh isolated whole review remains required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete height and primitive-base theorem](#statement) | Parts A--D, all ell/b/k endpoints, arbitrary-monic algebra versus irreducible-nontorsion certificate domains, all six canonical polynomials and exact orders, actual analytic/degree/norm costs, maximal-base parity, primitive/Salem obstruction, and height1 fixed-binary-source certificate with every scope limitation. |
| argument | [Complete HD1--HD13 proof](#complete-argument) | Integer derivative/support extraction, reciprocal integral trace basis, every root/multiplicity and exact covariance, explicit G monic division, actual full-field norm interface, exact monic derivative-content argument, maximal odd-base contradiction, primitive threshold and Salem root count, exact height1 support equality and finite s-based norm certificate. |
| dependency | [Adopted actual canonical covariance](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | DP7 integer monic-division covariance for a,b,c,F,X_s at an actual trace composition; G covariance is explicitly derived here from the same canonical divisions. No irreducibility ascent or field normalization is inferred. |
| dependency | [Adopted finite exactness and circle bounds](Yin_C_G0720_v1.md#decision-whole-reviewed-2026-10-25) | PC1--PC5 true Theta and actual-degree U certificates, PC12 scalar bounds and S>=M, exact coefficient-precision mechanism, complete reciprocal/trace domain and all source limits. Its review does not cover this new reconstruction and primitive/height1 application. |
| dependency | [Adopted full original norm descent](Yin_C_G0586_v2.md#decision-complete-current-self-adoption) | Exact self-composition descent section and formulas46--47 only: actual degree-k original and trace extensions, common-value descent and Norm_F=Norm_F0^k, Norm_K=Norm_F0^(2k). Retain the source's actual self-reviewed scope; no unrelated total-real coordinate gate is used. |
| support | [Adopted derivative and finite-Salem certificate boundaries](Yin_C_G0722_v1.md#decision-whole-reviewed-2026-10-25) | Motivation/comparison only: the coarse-U obstruction and original remaining true-S question. The current exact base and primitive-domain results are proved here and are not inferred from a failure of the coarse bound. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T16:41 |
| status | proved |
| reason | Adopt the whole fixed Parts A--D and HD1--HD13 after reading the entire theorem and fresh isolated whole R945. Actual integer dyadic reconstruction, every endpoint and parity domain, all six canonical identities and exact coefficient orders, exact derivative descent, full root/field norm multiplicities, primitive and genuine-Salem true-circle limitations, and the height1 fixed-source finite certificate are supported. This gives no actual bounded-height lift, passing certificate, extra precision, decreased total measure, synthetic/canonical identification or unrestricted Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete height and primitive-base theorem](#statement) | Parts A--D, all ell/b/k endpoints, arbitrary-monic algebra versus irreducible-nontorsion certificate domains, all six canonical polynomials and exact orders, actual analytic/degree/norm costs, maximal-base parity, primitive/Salem obstruction, and height1 fixed-binary-source certificate with every scope limitation. |
| argument | [Complete HD1--HD13 proof](#complete-argument) | Integer derivative/support extraction, reciprocal integral trace basis, every root/multiplicity and exact covariance, explicit G monic division, actual full-field norm interface, exact monic derivative-content argument, maximal odd-base contradiction, primitive threshold and Salem root count, exact height1 support equality and finite s-based norm certificate. |
| dependency | [Adopted actual canonical covariance](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | DP7 integer monic-division covariance for a,b,c,F,X_s at an actual trace composition; G covariance is explicitly derived here from the same canonical divisions. No irreducibility ascent or field normalization is inferred. |
| dependency | [Adopted finite exactness and circle bounds](Yin_C_G0720_v1.md#decision-whole-reviewed-2026-10-25) | PC1--PC5 true Theta and actual-degree U certificates, PC12 scalar bounds and S>=M, exact coefficient-precision mechanism, complete reciprocal/trace domain and all source limits. Its review does not cover this new reconstruction and primitive/height1 application. |
| dependency | [Adopted full original norm descent](Yin_C_G0586_v2.md#decision-complete-current-self-adoption) | Exact self-composition descent section and formulas46--47 only: actual degree-k original and trace extensions, common-value descent and Norm_F=Norm_F0^k, Norm_K=Norm_F0^(2k). Retain the source's actual self-reviewed scope; no unrelated total-real coordinate gate is used. |
| support | [Adopted derivative and finite-Salem certificate boundaries](Yin_C_G0722_v1.md#decision-whole-reviewed-2026-10-25) | Motivation/comparison only: the coarse-U obstruction and original remaining true-S question. The current exact base and primitive-domain results are proved here and are not inferred from a failure of the coarse bound. |
| review | [Fresh isolated whole descent review](../audits/reviews/Yin_R_G0945_v1.md#whole-height-descent-finding) | Independently reviewed the entire fixed statement and complete proof, initial selected decision and consumed fixed interfaces, all algebraic versus irreducible domains, full norm multiplicities, derivative/support endpoints, primitive/Salem and height1 criteria, with accepted source limits retained. |

