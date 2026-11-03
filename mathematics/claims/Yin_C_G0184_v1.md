---
author: Yin
---
# Residual singleton: unramified three exclusion and exact full-norm prime shape

Date: 2026-10-20T10:46.
Human author Yin.
The entropy_attainment_bridge agent authored the new local exclusion, explicit-control application and exact norm specialization below.
Root requested continued analysis of the actual residual singleton and suggested checking how the new3-prime exclusion combines with the old2-prime data; root supplied no proof step in this candidate.
The author previously contributed C178 and C182 and does not independently review those inputs here.
Their accepted independent reviews are reused at their actual scopes.
The distinct local power-order discussion and general primitive-field reductions are not premises of this candidate.

## Statement

Let F be a totally real number field of degree r and let a,b,c be nonzero algebraic integers in F.
Assume s in{1,-1} and

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.                                  (1)

At a prime p over3, normalize the valuation to have integer value group and write e=v_p(3), A=v_p(a), B=v_p(b), C=v_p(c).
If e is odd and prime to3, then necessarily

    B=0, 0<A<e/3, A congruent to e mod2,
    v_p(b+s)=A.                                    (2)

In particular ANY unramified3-prime of F excludes the triple.
The explicit totally real quintic field Q(u), where

    u^5-18u^4+20u^2-4=0,

has integral nonzero a=6/u^2,c=108/u^5 satisfying f=0, but admits no b completing(1) for either sign.
This control excludes a specific candidate field; it does not exclude all totally real quintic fields.

For every prime p over a rational prime ell>3 put G=v_p(g) and e_p=v_p(ell).
Then G is a nonnegative multiple of15 when ell!=5, and G=15k or15k+e_p for some integer k>=0 when ell=5.
Consequently the complete original norm has the exact necessary form

    abs(Norm_F(g))=2^(3U)3^(5V)M^15 5^J,
    U,V>=0, M>=1 integers, gcd(M,6)=1,
    0<=J<=r.                                       (3)

If r=5, a norm below2^(5/2) can only be1 or5.
Neither of those remaining possibilities is excluded.
No assertion that every integer in(3) is attained is made.
The unrestricted target abs(Norm_F(g))>=2^(r/2) remains open outside the already proved classes.

<a id="argument"></a>
## Complete argument

The proof retains the actual integer-valued valuations and all original residue-degree weights.
It needs no assertion that any coordinate is primitive, no integer affine relation and no monogenic maximal-order hypothesis.

<a id="singleton-unramified-three-exclusion"></a>
### An unramified3-prime also excludes the complete residual system

The entropy_attainment_bridge author supplies this new deduction from the accepted C182 local identities.
It is not an independent review of that upstream contributor's argument.
Keep the original field F, its integer-normalized3-prime valuation, and e,A,B,C from R16.
If B>0, the identity2B=3A makes A even, and2C=e+5A then makes e even.
If B=0 and A=0, the latter identity again makes e even.
The only remaining possibility at an odd e is therefore B=0,A>0.
In this case the residual equation gives

    v_p(1-2s b^3)=3A>0.

Reduction in the characteristic3 residue field implies bbar^3=-s.
The cube map is injective in a field of characteristic3, so bbar=-s.
Put w=b+s and W=v_p(w)>0, allowing W=infinity if w=0.
The exact expansion is

    1-2s b^3=3-6s w+6w^2-2s w^3.                 (R23)

The four valuations are e,e+W,e+2W,3W.
If3 does not divide e, the quantities e and3W cannot be equal for finite integer W.
The value W=infinity would give3A=e and is likewise impossible.
If3W>e, the unique minimum is e, again contradicting3A=e.
Consequently the only possible branch when e is odd and prime to3 is

    B=0, W=A, 0<A<e/3, A congruent to e mod2.      (R24)

The parity follows from2C=e+5A.
In particular e=1 has no allowable A, and ANY unramified3-prime excludes the original triple.
This is an exclusion in the actual field, not a condition only on its normal closure.
It does not exclude e=5, for which A=W=1,C=5 is still locally compatible.
No local compatibility is promoted to a global existence statement.

<a id="explicit-quintic-no-completion"></a>
### Explicit totally real f-only control and its obstruction at3

Let

    P(U)=U^5-18U^4+20U^2-4,
    H(T)=4T^5-20T^3+18T-1=-T^5 P(1/T).           (R9)

The signs of H at the rational endpoints -2,-3/2,-1,0,1/2,1,3/2,2 are respectively the signs of

    -5, 73/8, -3, -1, 45/8, 1, -89/8, 3.

Thus H has a root in each of the five disjoint intervals
(-2,-3/2),(-3/2,-1),(0,1/2),(1,3/2),(3/2,2).
Its degree is5, so these are all its roots, distinct, real and nonzero.
The same is true of P after reciprocation.

For any root u of P in Q_2bar, write v=v_2(u), with v_2(2)=1.
If v<2/5, the leading term u^5 has valuation strictly below each of 18u^4,20u^2,4.
If v>2/5, the constant term has valuation strictly below every other term.
Neither unique-minimum case can sum to zero, so every root has v_2(u)=2/5.
Any finite extension of Q_2 containing u consequently has ramification index divisible by5 and degree at least5.
The degree5 polynomial P is therefore irreducible over Q_2, and hence over Q.
For F=Q(u), the unique prime over2 has ramification index5 and residue degree1.
This proves the local assertion without a computed discriminant or numerical Newton polygon.

The field F is totally real of degree5.
The element u is integral with Norm_F(u)=4, and thus is a unit at every finite prime not over2.
Put t=1/u, a=6t^2 and c=108t^5.
At the unique2-prime, in the integer normalization, v(u)=2, v(a)=5-4=1 and v(c)=10-10=0.
At every other prime t is integral, so a,c belong to O_F and are nonzero.
They satisfy 2c^2=3a^5.
Hence the low-C=0 branch of f=0 is compatible with a genuinely totally real field and actual integral a,c.
There is still no b satisfying the second residual equation in this construction.

Its reduction modulo3 is Pbar(U)=U^5+2U^2+2, with

    Pbar'(U)=2U^4+U=2U(U-1)^3.

The two possible derivative zeros0 and1 have Pbar value2, so the reduction is squarefree.
Here is the exact standard local application without using a discriminant computation.
Choose a finite residue field F_(3^h) in which Pbar splits, lift a monic irreducible degree h polynomial over F_3 to Z_3, and let eta be a root.
The lifted polynomial is irreducible by reduction, so the complete local field Q_3(eta) has degree h; its residue degree is at least h and therefore exactly h, and its ramification index is1 by the degree formula.
In that unramified extension every distinct root of Pbar has an integral representative at which P has positive valuation and P' is a unit.
The accepted simple-root Hensel theorem gives five distinct roots of P there, so every local root field, and hence every completion of Q(u) at3, is unramified.
Subextensions have ramification index dividing1 by multiplicativity, and residue fields here are finite and separable.
The proved unramified3 exclusion therefore forbids any b completing(1) in this field, for both signs.
No factorization, root approximation, discriminant evaluation or numerical certificate is used.

<a id="singleton-complete-norm-prime-shape"></a>
### Exact prime shape of the full residual norm

The complete weighted-valuation proof in [C150 Section2](Yin_C_G0150_v1.md#weighted-valuation-comparison) was reread before this deduction.
Its lowest-coefficient argument is algebraic in the three integral coordinates; its fixed statement concerns actual trace quotients, so that statement is not silently enlarged here.
The following direct specialization supplies the proof in the present arbitrary integral-triple domain and adds the exact5-prime alternative.
The entropy_attainment_bridge agent authors this specialization.

Fix a prime p above a rational prime ell>3, put e=v_p(ell), and write A,B,C,G for the valuations of a,b,c,g.
The equation f=0 gives A=2k,C=5k for an integer k>=0.
If k>0 and B<3k, the two sides of b^2-a^3=-s g have valuations2B and5B, so B=0 and G=0.
If k>0 and B>3k, those valuations are6k and15k, a contradiction.
If k=0 and B>0, then G=0 directly.
Thus whenever G>0, one necessarily has

    A=2k, B=3k, C=5k, G>=15k, k>=0.              (R27)

If G>15k, divide a,b,c by their respective powers pi^(2k),pi^(3k),pi^(5k), obtaining units a_0,b_0,c_0 in the SAME local field.
The residual equation then gives b_0^2=a_0^3 in the residue field, and f=0 gives2c_0^2=3a_0^5.
The further assumption G>15k gives c_0^3=2b_0^5 there.
Squaring the last equality and substituting the first two yields5a_0^15=0.
This is impossible if ell!=5.
Therefore G is a multiple of15 at every prime not over2,3,5, with the value0 included.
This is exactly the relevant lowest-coefficient mechanism from C150, with no trace-polynomial hypothesis used in the displayed proof.

For ell=5 and G>15k, the element c^3+2b^5 has valuation15k, because c^3-2b^5 has strictly larger valuation and2 is a unit.
Substituting b^2=a^3-s g into the difference of squares gives the exact integral identity

    8g(c^3+2b^5)
      =-5a^15+160s a^12 g-320a^9 g^2
              +320s a^6 g^3-160a^3 g^4+32s g^5.  (R28)

The left valuation is G+15k.
Every term on the right except -5a^15 has strictly greater valuation: the first four such terms have valuations e+24k+G,e+18k+2G,e+12k+3G,e+6k+4G, and the last has valuation5G.
The strict inequalities follow directly from G>15k, including k=0.
The constant term must therefore have that same valuation, giving G+15k=e+30k.
Together with the case G=15k this proves that at every5-prime

    G=15k OR G=15k+e

for some k>=0, where G=0 is included in the first alternative.
No estimate for the norm of a single embedding or a smaller field replaces these local identities.

Combining this with C178's exact G=3C at2 and C182's exact G=5B at3, and summing ALL valuations with their residue degrees, gives

    abs(Norm_F(g))=2^(3U) 3^(5V) M^15 5^J,
    U,V>=0, M>=1 integers, gcd(M,6)=1,
    0<=J<=r=[F:Q].                                (R29)

Here U=sum_(p|2)f_p C_p and V=sum_(p|3)f_p B_p.
The integer M collects ell^(sum_(p|ell)f_p k_p) for ell>3, including the15k contributions at5.
The exponent J is the sum of e_p f_p over the5-primes using the second alternative; hence J<=r by the complete degree sum.
This is an exact necessary shape, not a declaration that every such integer occurs.
For an actual ambient field F of degree5, a norm strictly below2^(5/2) can consequently only be1 or5.
If a degree5 field containing the triple is embedded in a larger ambient field, both its norm logarithm and the target exponent are multiplied by the same relative degree.
The alternatives1 and5 are not excluded here.
In particular the precise prime shape does not supply the still missing uniform positive lower bound on log(abs(Norm_F(g)))/r.

<a id="inputs-and-boundaries"></a>
## Exact inputs, applicability and contributor limits

| Input | Actual use and limit |
| --- | --- |
| [C178 exact local theorem](Yin_C_G0178_v1.md#argument) | Only G=3C at every2-prime and its original full-norm convention; no unrestricted norm floor is imported. |
| [C178 accepted assessment](Yin_C_G0178_v1.md#decision-whole-reviewed-2026-10-20) and [R447](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | Accepted independent upstream finding; the present author does not re-review his own proof independently. |
| [C182-prime companion](Yin_C_G0182_v1.md#singleton-three-adic-companion) | Exact2C=e+5A, C>A, G=5B, C>B and2B=3A when B>0. The new cancellation expansion and unramified exclusion are proved here. |
| [C182 accepted assessment](Yin_C_G0182_v1.md#decision-whole-reviewed-2026-10-20) and [R453](../audits/reviews/Yin_R_G0453_v1.md#c182-whole-integer-affine-finding) | Accepted independent review of the contributor's upstream calculation; the affine theorem is not needed. |
| [C150 weighted-valuation proof](Yin_C_G0150_v1.md#weighted-valuation-comparison) | Reuse of the universal lowest-coefficient mechanism, while distinguishing its actual-trace fixed statement from this directly proved arbitrary-triple application. The exact5-prime alternative is supplied by(R28). |
| [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Complete-valued-field simple-root theorem, with integral representatives, positive polynomial valuation, unit derivative and disjoint residue classes in the explicit control. No stronger Hensel variant or source-proof upgrade is claimed. |
| [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Exact degree sum and complete-DVR ramification normalization, used for the explicit local extension and full norm weights. No normal-closure degree is substituted for r. |

The remaining inputs are elementary separability, integer residues, valuation cancellation, finite residue fields, multiplicativity of local ramification indices and field norms, with the specific calculations written out.
The proof does not use J111, an unreviewed primitive-field lemma, a numerical root count, a general integral-point existence theorem or a bounded-denominator substitute for the original integrality.
The continuing D37 is the extraction context, not a logical premise.
The author checked every local branch, the quintic's real and2-adic degree arguments, its exact squarefree3-reduction, all five terms of(R28), and every original norm weight.
This describes the original author checking; the later noncontributor whole review and adoption are recorded in the selected assessment.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:46 |
| status | open |
| reason | Register the complete unramified3 exclusion, actual quintic obstruction and exact full-norm prime shape for independent review, retaining the unrestricted singleton as unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete residual theorem](#statement) | Both signs, arbitrary totally real integral triples, exact local branch, actual quintic obstruction, all-prime norm shape and degree5 remaining possibilities. |
| argument | [Complete argument](#argument) | Entire local proof, explicit real/local field construction and exclusion, prime valuation specialization, five-prime identity and full original norm weights. |
| dependency | [C178 local proof](Yin_C_G0178_v1.md#argument) | G=3C at2 and original norm valuation normalization. |
| dependency | [C182 companion proof](Yin_C_G0182_v1.md#singleton-three-adic-companion) | Exact3-prime relations only; no affine or primitive-field assumption. |
| dependency | [C150 lowest-coefficient argument](Yin_C_G0150_v1.md#weighted-valuation-comparison) | Exact algebraic mechanism reused and directly specialized in(R27), with the fixed actual-trace domain distinguished. |
| dependency | [Simple-root Hensel statement](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Five distinct residue roots in an actual finite unramified complete local field. |
| dependency | [Original degree and ramification normalization](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Full degree sums and complete-DVR valuation scope in the explicit control and global norm. |
| support | [Exact input and role boundaries](#inputs-and-boundaries) | Actual author contribution, accepted upstream independent findings, complete controls and no numerical or unrestricted conclusion. |
| support | [C178 independent finding](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | Accepted upstream2-prime theorem only. |
| support | [C182 independent finding](../audits/reviews/Yin_R_G0453_v1.md#c182-whole-integer-affine-finding) | Accepted upstream3-prime calculation only. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:51 |
| status | proved |
| authority | Internal adoption within Yin's selected residual-singleton inquiry. |
| reason | Adopt the whole unramified3 exclusion, exact quintic obstruction and complete original norm prime shape through noncontributor R456. Both signs and every local weight are retained; degree5 leaves norm1 or5 below the target, and the unrestricted exponential floor remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete residual theorem](#statement) | Both signs, arbitrary totally real integral triples, exact local branch, actual quintic obstruction, all-prime norm shape and degree5 remaining possibilities. |
| argument | [Complete argument](#argument) | Entire local proof, explicit real/local field construction and exclusion, prime valuation specialization, five-prime identity and full original norm weights. |
| dependency | [C178 local proof](Yin_C_G0178_v1.md#argument) | G=3C at2 and original norm valuation normalization. |
| dependency | [C182 companion proof](Yin_C_G0182_v1.md#singleton-three-adic-companion) | Exact3-prime relations only; no affine or primitive-field assumption. |
| dependency | [C150 lowest-coefficient argument](Yin_C_G0150_v1.md#weighted-valuation-comparison) | Exact algebraic mechanism reused and directly specialized in(R27), with the fixed actual-trace domain distinguished. |
| dependency | [Simple-root Hensel statement](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Five distinct residue roots in an actual finite unramified complete local field. |
| dependency | [Original degree and ramification normalization](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Full degree sums and complete-DVR valuation scope in the explicit control and global norm. |
| support | [Exact input and role boundaries](#inputs-and-boundaries) | Actual author contribution, accepted upstream independent findings, complete controls and no numerical or unrestricted conclusion. |
| support | [C178 finding](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | Accepted upstream2-prime theorem only. |
| support | [C182 finding](../audits/reviews/Yin_R_G0453_v1.md#c182-whole-integer-affine-finding) | Accepted upstream3-prime calculation only. |
| review | [Whole prime-shape finding](../audits/reviews/Yin_R_G0456_v1.md#residual-prime-shape-whole-independent-finding) | Actual complete statement, local cancellations, full explicit field control and lifting, all-prime norm assembly, inputs and precise degree5 remainder. |

