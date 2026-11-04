---
author: Yin
---

<a id="height-one-edge-resultant-uniform-mahler"></a>
# Exact height-one edge resultants and finite-ratio Mahler lower bounds

Human author Yin.
At author registration, this complete fixed candidate was OPEN pending fresh independent whole review and separate adoption.
The initial investigation compared Smyth and Salem--Boyd inputs; the exact retained edge values instead give a direct finite cyclic resultant with a positive surplus after the FULL degree expense.
Salem_completion derived the sharp e=2 endpoint resultant and bound, and root proposed the extension to every admissible local-mask multiplier in the C740/C747 range.
Both contributors checked the actual integer half-sum, complete support, root-of-unity products, sign domains and unchanged multiplicities below.
The direct cyclic-resultant upper estimate is the elementary one already retained in [adopted C245, equation(5)](Yin_C_G0245_v1.md#cyclic-norm-residue-density); it is proved again here for the present possibly reducible polynomial, without importing that Claim's irreducible arithmetic hypotheses.
The [adopted C755 PX5--PX8](Yin_C_G0755_v1.md#decision-whole-reviewed-2026-10-25) supplies the actual endpoint family; the broader local mask interface is [adopted C740/C747](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25).
The separate source comparison following this proof is not an external theorem dependency of the result.

Root read the entire saved EM1--EM5/equations EM1--EM16 and the entire integrated source comparison.
Root and Salem_completion are substantive contributors, not independent reviewers.
No native mathematical computation or numerical root/support enumeration is used.

## Statement

The complete theorem consists of the general actual local-mask domain and bound in EM1, the a=d-2 empty-coprime boundary in EM3, the sharper exact e2 endpoint result in EM4, and every raised-source and fixed-ratio/nearzero consequence in EM5.
All quantities concern the full monic polynomial with its actual multiplicities; no individual-factor Mahler bound or degree-normalized measure is asserted.

### EM1. General actual local-mask domain and result

Let U_0 be any actual complete source in the structural local domain verified in C740/C747, including the paid complete extensions whose same properties are explicitly established in C753/C755.
Let d=deg U_0, r=2d-2 and

    Dbar=z^d U_0(z+z^(-1))/(z^2+1).

Retain Dbar monic reciprocal of full degree r, constant1 and zero central coefficient, with every supported coefficient interpreted as an actual height1 sign below.
Let

    ceil(d/2)<=a<=d-2, n=2a+1, gcd(n,15)=1,
    mu=r-n=2(d-a)-3,
    D=deg P=r+2n=2d+4a.                         (EM1)

Here mu is the ambient edge-block degree, not a Mahler measure or the original source parameter m_src.
The inequalities give1<=mu<n and n>=d+1.
Let P be an ACTUAL monic reciprocal height1 integer lift, with constant1, of the full binary polynomial Dbar(1+z^(2n)).
Its exact C740 parametrization is

    P=L+z^(2n)L*, L*=z^r L(z^(-1)),
    deg L=r, L(0)=1, Lbar=Dbar,
    L_j in{1,-1} on support(Dbar), and0 elsewhere. (EM2)

In this general mask domain the leading coefficient L_r can be either sign; it is NOT assumed that L itself is monic.
P is monic because its leading coefficient is L(0)=1, and2n>r makes the two blocks disjoint.
Use P's OWN trace T and the actual canonical residuals defined in C747, with all prime divisions performed over the integers before reduction.
Assume the ADDED-MODULUS local condition for either residual, equivalently for both:

    B_n^2 divides F_Tbar and X_(epsilon,T)bar.

No full old-primary or irreducibility assumption is included in this local condition.
By the exact C740/C747 carry this is precisely the actual mask condition

    S=(L+L*)/2 in Z[z],
    Sbar=(1+z)(1+z^n)J,
    deg J<=mu-1, z^(mu-1)J(z^(-1))=J(z).       (EM3)

The mask support is contained in the actual support of Dbar.

If in addition gcd_(Q[z])(P,z^(2n)-1)=1, then

    m(P)>=((2n-r)/(2n)) log2
         =((2a-d+2)/(2a+1)) log2>0.             (EM4)

The convention is the FULL absolute logarithmic Mahler measure m(P)=sum_(P(alpha)=0)log max(1,|alpha|), with every root repeated according to its actual multiplicity.
No division by degree is made.
Every irreducible P in this domain automatically meets the coprimality hypothesis, since deg P=r+2n>2n.
The theorem also applies to reducible P whenever that explicit coprimality condition holds.

## Complete argument

### EM2. The genuine integer blocks and their extra factor2

At each supported position the actual integer S coefficient is0,1 or-1, and at unsupported positions it is0.
Thus Sbar detects EXACTLY the nonzero coefficient positions of S; a binary zero cannot conceal a coefficient2 in S.
Set K=(1+z)J, so deg K<=mu.
Because mu<n, the binary formula Sbar=K+z^nK consists of disjoint low and high blocks.
It follows coefficientwise that the actual S is supported only in[0,mu] and[n,n+mu].
Write its actual low block as A in Z[z], with degree at most mu and coefficients in{0,1,-1}.
Since S is reciprocal with AMBIENT degree r=n+mu, its upper block is forced to be the ambient reversal of A:

    S=A+z^n A*, A*=z^mu A(z^(-1)).             (EM5)

No actual degree mu or nonzero endpoint coefficient of A is assumed.
The polynomial K=(1+z)J is itself reciprocal with ambient degree mu, by EM3.
Consequently Abar=K=A*bar, and both actual integer halves

    B_+=(A+A*)/2, B_-=(A-A*)/2                 (EM6)

belong to Z[z].
These divisions by2 take place before any reduction or evaluation.
Either polynomial may be zero when the forthcoming coprimality fails; such a case must not be assigned a nonzero resultant.

At a root zeta of z^(2n)-1, one has zeta^(2n)=1 and hence P(zeta)=L(zeta)+L*(zeta)=2S(zeta).
Splitting the two disjoint root sets

    Omega_+={zeta:zeta^n=1},
    Omega_-={zeta:zeta^n=-1}

gives the exact values

    P(zeta)=4B_+(zeta) on Omega_+,
    P(zeta)=4B_-(zeta) on Omega_-.              (EM7)

This factor4 is an actual integral consequence of the supported sign mask, not a division by2 in a binary quotient.

### EM3. Full resultant and full-degree Mahler expense

By the monic root-product definition of resultant, EM7 gives

    |Res(P,z^(2n)-1)|
       =4^(2n)|Res(z^n-1,B_+) Res(z^n+1,B_-)|. (EM8)

The order of the two polynomials in a resultant can change its sign but not its absolute value.
Since B_+,B_- are actual integer polynomials, the two resultants on the right are integers.
The assumption gcd(P,z^(2n)-1)=1 is equivalent, through EM7, to BOTH of those resultants being nonzero.
Their absolute product is therefore at least1, and

    log|Res(P,z^(2n)-1)|>=4n log2.              (EM9)

On the other hand, write the COMPLETE monic polynomial P=product_(i=1)^D(z-alpha_i), listing repeated roots separately.
For every root,

    |alpha_i^(2n)-1|<=2 max(1,|alpha_i|)^(2n).

Multiplying over ALL D=r+2n roots gives

    |Res(P,z^(2n)-1)|<=2^D exp(2n m(P)).        (EM10)

This estimate uses neither irreducibility nor squarefreeness.
It is the direct archimedean root estimate of C245's cyclic-resultant proof, here applied after an exact nonvanishing calculation instead of a modular valuation argument.
Combining EM9--EM10 yields

    2n m(P)>=(4n-D)log2=(2n-r)log2,

which proves EM4.
The positive difference is paid on the full original polynomial degree.
Bounding the two resultants in EM8 separately with two degree-D factors would lose this surplus; EM10 applies ONCE to the single binomial z^(2n)-1.
No degree reduction, primitive-factor extraction or uncharged removal of a cyclotomic multiplier is used.

If P is irreducible over Q, any common factor with z^(2n)-1 would force the whole P to divide that smaller-degree polynomial, contradicting D>2n.
Thus irreducible local-passing inputs are all covered without an additional root-of-unity test.
If P is reducible and shares such a factor, EM8 can vanish and this argument supplies no bound for P or for a remaining factor.
The zero-mask family L(1-z^(2n)) is one such excluded case.
There is a useful exact boundary check at a=d-2, where mu=1.
If the mask is zero then S=0, while any nonzero mask has K=1+z and hence A=a_0+a_1z with a_0,a_1 in{1,-1}.
When a_0=a_1 one has B_-=0, and when a_0=-a_1 one has B_+=0.
In either case P has the full factor z^n+1 or z^n-1 respectively; the zero mask has both.
Thus the coprime local-passing domain is empty at this upper endpoint, without an old-X parity assumption.
No higher-a domain is added to this theorem.

### EM4. Sharper exact e=2 endpoint with its four actual edge patterns

At the C755 endpoint a=d-3, one has

    r=2d-2, n=2d-5=r-3,
    D=r+2n=3n+3=3r-6.

For its unique nonzero even mask the actual low block is

    A=1+eta_1z+eta_2z^2+eta_3z^3,
    eta_j in{1,-1}, eta_1 eta_2 eta_3=-1.       (EM11)

These are exactly (++-),(+-+),(-++),(---); all nonedge supported pairs remain opposite-sign pairs, as retained in C755.
Here A*=z^3A(z^(-1)), and the actual two possibilities for EM6 are

| Edge case | B_+ | B_- |
| --- | --- | --- |
| eta_3=-1, eta_1=eta_2=eta | eta z(1+z) | 1-z^3 |
| eta_3=1, eta_1=-eta_2=eta | 1+z^3 | eta z(1-z) |

The endpoint n is odd and coprime to3.
The map zeta -> zeta^3 permutes each of Omega_+ and Omega_-: it maps the set to itself, and equality of two cubes would give a ratio with both third and n-th power1, hence ratio1.
The exact monic product identities are

    product_(Omega_+)(1+zeta)=2,
    product_(Omega_-)(1-zeta)=2,
    |product_(Omega_+)zeta|=|product_(Omega_-)zeta|=1.

The first follows by evaluating z^n-1 at-1 with n odd, and the second by evaluating z^n+1 at1.
The cube permutation therefore gives, in either row of the table,

    |Res(z^n-1,B_+)|=2,
    |Res(z^n+1,B_-)|=2.                        (EM12)

In particular nonvanishing and gcd(P,z^(2n)-1)=1 are proved again, independently of every nonedge sign.
The FULL exact cyclic resultant is consequently

    |Res(P,z^(2n)-1)|=2^(4n+2),                (EM13)

with no missing irreducible factor or multiplicity.
Using the same full-degree upper bound EM10 gives the stronger finite estimate

    m(P)>=((n-1)/(2n))log2
         =((d-3)/(2d-5))log2.

Since n>=7 in the actual endpoint domain,

    m(P)>=(3/7)log2>0,
    M(P)>=2^(3/7).                              (EM14)

The sharper lower coefficient tends to1/2 as the ACTUAL endpoint degree grows.
This is a bound on absolute Mahler measure of the complete P; it is not a degree-normalized height bound or a claim that every individual noncyclotomic factor has this measure.
The theorem does not require L or P to be irreducible, and does not require an exterior-root count or a Pisot/Perron seed.
Height1 and actual support enter through the true half-sum in EM5--EM6, not through a numerical norm bound on L.

### EM5. Raised sources, finite-ratio exclusion and exact boundaries

For any positive integer q, put P_q(z)=P(z^q).
Every root alpha_i of P has q roots beta with beta^q=alpha_i, each of modulus |alpha_i|^(1/q), and all multiplicities are retained.
Thus the full root-product definition gives

    m(P_q)=m(P),
    |Res(P_q,z^(2nq)-1)|=|Res(P,z^(2n)-1)|^q. (EM15)

The latter equality follows because beta^(2nq)=alpha_i^(2n) for each of the q roots; it is not a distinct-root or field-degree assumption.
At the actual dyadic q in C724/C747/C755, height1 support descent supplies precisely these P_q, of full degree qD.
Therefore EM4 and EM14 hold with the SAME absolute lower bounds throughout the exact raised families.
They cannot be weakened by dropping their genuine power multiplicities or dividing the logarithm by qD.

More generally fix delta>0 and suppose the EM1 domain additionally has a/d>=1/2+delta.
Then

    (2a-d+2)/(2a+1)
       >=(2delta*d+2)/((1+2delta)*d+1)
       >2delta/(1+2delta).

Every coprime local-passing P in this finite-ratio range consequently has the degree-uniform bound

    m(P)>[2delta/(1+2delta)]log2.                (EM16)

For any sequence of coprime local-passing inputs with m(P) tending to0, EM4 forces a/d to tend to1/2 and d to tend to infinity.
In particular the e=2 a=d-3 family stays uniformly away from a near-one Mahler sequence.
If coprimality is not imposed, an infinite family can instead fall into the common-cyclotomic-factor branch; no residual-factor estimate is inferred by removing that factor without a new argument.
All irreducible inputs satisfy coprimality automatically, but irreducibility is not established by any of these estimates.

The adopted C755 family supplies actual nonempty height1 outputs in each of the four EM11 patterns, passing its old-X and added-modulus first-bit conditions.
EM14 applies to every one of those outputs, including every nonedge choice and every original dyadic q.
It also applies if further old-primary equations happen to select a subfamily of them.
It gives no old-primary solution, new residual precision, factor-precision inheritance or uniform gap for all integer polynomials outside this explicit class.
No unrestricted G0001 conclusion is supplied.

<a id="finite-ratio-salem-boyd-source-comparison"></a>
## Comparison and source inspection

This section retains the source comparison requested before the direct EM argument was found.
It is not a premise of EM1--EM16, and does not replace the exact finite resultant with an asymptotic statement.
The bounded local search read the accepted [Smy08-U002 nonreciprocal statement](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number), the exact prior [Hir06-U001 reading boundary](../audits/literature/Hir06/Yin_U001.md#hir06-u001), the later [L434 printed507--511 comparison](../ledger/Yin_L_G0434_v1.md#residual-cubic-retained-reading), and [C488's fixed-seed local proof](Yin_C_G0488_v1.md#bounded-measure-chain-root-control).
Those supplied no existing quantitative theorem for varying seeds at the specific finite ratio2r-6.

At the four actual endpoint patterns L is monic with constant1 and has at least one nonedge opposite-sign supported pair, because the original complete source has k_support>=5 and C755 has its full nonedge run.
Thus L* is neither L nor-L.
Factoring L over Z shows that at least one nonzero monic irreducible factor is nonreciprocal; otherwise the product would be reciprocal up to sign.
The accepted Smyth statement then gives M(L)>=theta_0, theta_0^3-theta_0-1=0, without requiring L itself irreducible.
All other monic integer factor measures are at least1 by the root-product definition.
This is a valid lower bound for the SEED, while the actual P is reciprocal and Smyth's nonreciprocal theorem does not directly apply to P.

With f=L*, the actual P is the plus Salem--Boyd polynomial

    P(z)=z^N f(z)+f*(z), N=2n=2r-6.

The retained published [Hir06 PDF](../literature/pdf/Hir06.pdf), with its institutional cover and printed497=PDF2, was text-read in this new bounded comparison at printed504--511/PDF9--16.
Printed505--506 and509--510/PDF10--11 and14--15 were also visually inspected from rendered pages, including the exact limit and threshold formulas.
No whole-paper or original Boyd/Salem proof audit is claimed; the sole registry's acquired artifact and original source provenance are unchanged.
Theorem12 states exterior-root-count control and convergence of the house and full Mahler measure to those of a FIXED monic integer seed f as N tends to infinity.
It does not give an input-uniform error at N=2deg f-6 when f itself varies.
Factoring a reciprocal seed factor in that proof must keep its actual Mahler contribution and multiplicity; it is not an automatic zero-measure removal.

The dependence is visible directly in Lemma10's proof.
For an exterior root alpha of f, take a small disk D_alpha strictly outside the unit circle and containing no other distinct seed root.
Write

    A_alpha=min_(boundary D_alpha)|f|>0,
    B_alpha=max_(boundary D_alpha)|f*|,
    R_alpha=min_(boundary D_alpha)|z|>1.

The displayed Rouche guard is R_alpha^N>B_alpha/A_alpha.
The needed N therefore depends on the actual seed, its exterior-root separation, the selected disk and its boundary lower bound.
None of the cited fixed-seed statements proves this guard at the actual N=2r-6 uniformly over the endpoint signs or growing source degree.
The accepted Smyth lower bound on the product M(f) does not itself supply those individual root and boundary constants.

Hir06 Proposition14 requires a Perron seed and a seed-dependent index n_0 beyond which its houses are monotone; its bound contains the actual initial house lambda(Q_(n_0)).
Proposition15 is restricted further to a P-V seed and gives the special thresholds n_0^+=1 and n_0^-=deg f-2f'(1)/f(1)+1, together with a monotonicity criterion.
The present complete height1 support/sign conditions do not prove either seed hypothesis, and those formulas do not evaluate a degree-uniform initial measure for the actual sign family.
No fixed-L limit, eventually monotone tail or small-degree seed example is substituted for the varying-degree endpoint.

A bounded primary-source web screen also inspected the introduction and Theorem1.2 on pp1--3 of Sawin--Shusterman--Stoll, [Irreducibility of polynomials with a large gap](https://mathe2.uni-bayreuth.de/stoll/papers/SaShSt.pdf), the author-hosted25-page rendering dated28March2018.
Its family is f_N(z)=z^N c(z^(-1))+d(z), and Theorem1.2 explicitly assumes c!=+/-d, as well as its other hypotheses; it concerns the nonreciprocal part.
For the present P that parametrization has N=D and c=d=L, so that hypothesis fails identically.
This was an applicability screen only, not an acquisition, accepted source theorem or audit of its proof or algorithm, and it supplies no Mahler bound here.
The separate arXiv1803.10811 record was used only for discovery, without asserting byte/version equivalence to the author PDF.

These source limitations explain why the originally proposed general comparison did not itself pay the finite-ratio bound.
The affirmative bound for the ACTUAL endpoint instead follows from EM7--EM14's exact unit-root values and complete cyclic resultant, with every degree and multiplicity charged.
It does not assert that no stronger external theorem exists or that all reciprocal constructions share this gap.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision height-one-edge-resultant-gap-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T22:18 |
| status | open |
| reason | Register the complete EM1--EM5/equations EM1--EM16 and integrated source comparison after root read both entire sections. Actual supported integer half-sums yield integral B_+,B_- and a full cyclic resultant divisible by4^(2n); nonvanishing pays the complete degree r+2n and gives the general finite-ratio lower bound. Every irreducible input is coprime, the a=d-2 coprime domain is empty, and all four e2 endpoint patterns have exact resultant2^(4n+2), hence m(P)>=3log2/7. Complete multiplicities, exact dyadic substitutions and nearzero necessary ratio a/d->1/2 are retained. The comparison records the accepted Smyth seed-only use, actual Hir06 text/visual scope and seed-dependent constants, and SSS reciprocal-domain mismatch without acquisition or theorem adoption. Root and Salem_completion are contributors; fresh independent whole review and separate adoption were outstanding at author registration. No individual-factor bound, full old-primary solution, new precision, irreducibility construction or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete general, endpoint, raised and ratio theorem](#statement) | EM1 exact structural domain and general absolute Mahler bound; EM3 upper-endpoint empty-coprime boundary; EM4 four-pattern exact cyclic resultant and sharper bound; EM5 all multiplicities, raised inputs, fixed-ratio exclusion and nearzero necessary boundary. |
| argument | [Entire actual integer-resultant proof](#complete-argument) | Complete EM2--EM5 and EM1--EM16 interfaces: true supported half-sum, ambient reversal, legitimate integer halves, two nonzero component resultants, single full-degree binomial cost, exact edge products, irreducible coprimality, raised roots and ratio consequences. |
| dependency | [Adopted full local height1 mask](Yin_C_G0740_v1.md#decision-whole-reviewed-2026-10-25) | WM1--WM15 actual reciprocal support, disjoint blocks, own canonical carry and equivalence of either added B_n^2 condition with the reciprocal mask, allowing old-factor overlap. No arbitrary multiplier source-jet preservation. |
| dependency | [Adopted reflection and zero-trace theorem](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | Actual multiplier/mask domains, e2 structure, canonical conventions, local/global boundaries and raised covariance. All original and enlarged degrees remain charged. |
| dependency | [Adopted actual paid endpoint family](Yin_C_G0755_v1.md#decision-whole-reviewed-2026-10-25) | PX5--PX8 genuine eight-edge half-sum and four patterns, full actual signs and trace polynomials, nonempty local-passing family, paid degrees and original raised sign family. No full old-primary or irreducibility output presumed. |
| dependency | [Adopted exact height1 descent](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Actual dyadic P_q=P(z^q) and full qD degree. EM15 directly proves the complete measure/resultant identities with every root multiplicity. |
| support | [Existing elementary cyclic-resultant expense](Yin_C_G0245_v1.md#cyclic-norm-residue-density) | Equation(5) full root bound2^D M(P)^k, proved again in EM10 for reducible/repeated-root P. No modular collision, unramified prime, irreducible field or powered-degree premise imported. |
| support | [Absolute Mahler convention](../tasks/Yin_T_G0001_v1.md#contract) | Full root-product definition including all multiplicities, without normalization by degree or unrestricted gap conclusion. |
| support | [Complete integrated source comparison](#comparison-and-source-inspection) | Entire separate comparison including source versions and text/visual scope; external theorem statements there are not EM proof premises. No independent project review or extra source acquisition is claimed. |
| support | [Accepted precise Smyth statement](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only the nonreciprocal-number section in the comparison: an irreducible nonreciprocal seed factor gives M(L)>=theta_0 without L irreducibility. Original proof scope unchanged; no direct inference for reciprocal P. |
| support | [Retained Hir06 source unit](../audits/literature/Hir06/Yin_U001.md#hir06-u001) | Published2006 version, cover/pagination and prior fixed-seed scope. The integrated section retains current printed504--511 text and505--506/509--510 visual reading, without whole-paper or original Boyd/Salem proof audit. |
| support | [Earlier bounded Perron/P-V comparison](../ledger/Yin_L_G0434_v1.md#residual-cubic-retained-reading) | Prior printed507--511 discovery scope only; no uniform threshold or source-wide theorem acceptance imported. |
| support | [Existing fixed-seed local proof](Yin_C_G0488_v1.md#bounded-measure-chain-root-control) | Comparison only: fixed circle-zero-free seed Rouche argument and full multiplicities. Special seed estimates are not assigned to varying endpoint seeds. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T22:27 |
| status | proved |
| reason | Register the complete EM1--EM5/equations EM1--EM16 and integrated source comparison after root read both entire sections. Actual supported integer half-sums yield integral B_+,B_- and a full cyclic resultant divisible by4^(2n); nonvanishing pays the complete degree r+2n and gives the general finite-ratio lower bound. Every irreducible input is coprime, the a=d-2 coprime domain is empty, and all four e2 endpoint patterns have exact resultant2^(4n+2), hence m(P)>=3log2/7. Complete multiplicities, exact dyadic substitutions and nearzero necessary ratio a/d->1/2 are retained. The comparison records the accepted Smyth seed-only use, actual Hir06 text/visual scope and seed-dependent constants, and SSS reciprocal-domain mismatch without acquisition or theorem adoption. Adopt fresh isolated whole R977 mathematical PASS and its separate bounded comparison/source PASS after root read the entire EM theorem, integrated source comparison, fixed statement/input scopes and both complete independent findings. Root and Salem_completion remain contributors; the reviewer supplied no repair. All finite, endpoint, raised and ratio conclusions retain their exact coprime/four-pattern domains, and external comparison statements remain separate from the EM proof premises. No individual-factor bound, full old-primary solution, new precision, irreducibility construction or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete general, endpoint, raised and ratio theorem](#statement) | EM1 exact structural domain and general absolute Mahler bound; EM3 upper-endpoint empty-coprime boundary; EM4 four-pattern exact cyclic resultant and sharper bound; EM5 all multiplicities, raised inputs, fixed-ratio exclusion and nearzero necessary boundary. |
| argument | [Entire actual integer-resultant proof](#complete-argument) | Complete EM2--EM5 and EM1--EM16 interfaces: true supported half-sum, ambient reversal, legitimate integer halves, two nonzero component resultants, single full-degree binomial cost, exact edge products, irreducible coprimality, raised roots and ratio consequences. |
| dependency | [Adopted full local height1 mask](Yin_C_G0740_v1.md#decision-whole-reviewed-2026-10-25) | WM1--WM15 actual reciprocal support, disjoint blocks, own canonical carry and equivalence of either added B_n^2 condition with the reciprocal mask, allowing old-factor overlap. No arbitrary multiplier source-jet preservation. |
| dependency | [Adopted reflection and zero-trace theorem](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | Actual multiplier/mask domains, e2 structure, canonical conventions, local/global boundaries and raised covariance. All original and enlarged degrees remain charged. |
| dependency | [Adopted actual paid endpoint family](Yin_C_G0755_v1.md#decision-whole-reviewed-2026-10-25) | PX5--PX8 genuine eight-edge half-sum and four patterns, full actual signs and trace polynomials, nonempty local-passing family, paid degrees and original raised sign family. No full old-primary or irreducibility output presumed. |
| dependency | [Adopted exact height1 descent](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Actual dyadic P_q=P(z^q) and full qD degree. EM15 directly proves the complete measure/resultant identities with every root multiplicity. |
| support | [Existing elementary cyclic-resultant expense](Yin_C_G0245_v1.md#cyclic-norm-residue-density) | Equation(5) full root bound2^D M(P)^k, proved again in EM10 for reducible/repeated-root P. No modular collision, unramified prime, irreducible field or powered-degree premise imported. |
| support | [Absolute Mahler convention](../tasks/Yin_T_G0001_v1.md#contract) | Full root-product definition including all multiplicities, without normalization by degree or unrestricted gap conclusion. |
| support | [Complete integrated source comparison](#comparison-and-source-inspection) | Entire separate comparison including source versions and text/visual scope; external theorem statements there are not EM proof premises. No independent project review or extra source acquisition is claimed. |
| support | [Accepted precise Smyth statement](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only the nonreciprocal-number section in the comparison: an irreducible nonreciprocal seed factor gives M(L)>=theta_0 without L irreducibility. Original proof scope unchanged; no direct inference for reciprocal P. |
| support | [Retained Hir06 source unit](../audits/literature/Hir06/Yin_U001.md#hir06-u001) | Published2006 version, cover/pagination and prior fixed-seed scope. The integrated section retains current printed504--511 text and505--506/509--510 visual reading, without whole-paper or original Boyd/Salem proof audit. |
| support | [Earlier bounded Perron/P-V comparison](../ledger/Yin_L_G0434_v1.md#residual-cubic-retained-reading) | Prior printed507--511 discovery scope only; no uniform threshold or source-wide theorem acceptance imported. |
| support | [Existing fixed-seed local proof](Yin_C_G0488_v1.md#bounded-measure-chain-root-control) | Comparison only: fixed circle-zero-free seed Rouche argument and full multiplicities. Special seed estimates are not assigned to varying endpoint seeds. |
| review | [Fresh independent whole edge-resultant finding](../audits/reviews/Yin_R_G0977_v1.md#whole-edge-resultant-finding) | Entire fixed EM1--EM5/EM1--EM16, actual integer masks and resultants, complete degree/multiplicity expense, empty upper endpoint, exact four-pattern result, raised inputs and necessary nearzero ratio, with exact statement and argument bindings. |
| review | [Independent bounded comparison and source finding](../audits/reviews/Yin_R_G0977_v1.md#source-comparison-finding) | Entire integrated comparison at its stated source scope: accepted Smyth seed application, actual Hir06 text/visual passages and fixed-seed/threshold limits, SSS primary-text hypothesis mismatch, and all source-proof/acquisition boundaries; not an external premise for EM. |

