---
author: Yin
---
# Local ideals of the three mixed defects and actual polynomial realizations

Human author Yin.
New G0001 author round by g_bridge_audit, following the adopted C149.
Root supplied the investigation question only in this round; C149 retains root's earlier proof contribution.
This author owns only this new D and any separately declared J.
No native mathematical program is allocated or run.

## Exact question and bounded reuse

Let alpha be an actual nontorsion integer unit, P its monic irreducible integer minimal polynomial, R=Z[alpha], and K=Q(alpha).
Put a=P(alpha^2)/2,b=P(alpha^3)/3,c=P(alpha^5)/5, and E=b^2-a^3,F=2c^2-3a^5,G=c^3-2b^5.
Determine what the actual ideal I=(E,F,G) can say beyond the individual base quotients, with exact valuation/order/denominator costs.
In particular the generic characteristic5 obstruction of C149 is not automatically an actual polynomial realization.

Direct inputs screened: [C149's integral identity](Yin_C_G0149_v1.md#integral-three-defect-identity) and full norm/cost scope; [L63's base quotient](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation), including repeated reduced roots; [L66's reciprocal two-copy interface](../ledger/Yin_L_G0066_v1.md#reciprocal-frobenius-two-copy-module), which does not make a trace/order quotient a maximal-order ideal; and [L59's mixed resultants](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities), with all original copies.
The bounded no-ignore G claims/ledger search also found C78's actual-order value ideal and scalar-content mechanisms; it does not classify the present nonlinear ideal.
This round must distinguish norm divisibility, common ideal valuation and a scalar power-basis gcd.
No general ideal is assumed principal or invertible in R.

The exact [C78 ideal/normalization scope](Yin_C_G0078_v1.md#integer-ideal-energy-closure) was read: its scalar-content packet class requires an ACTUAL ideal equality and cannot infer one from an integer norm or ideal norm.
The shifted-Eisenstein construction mechanism is already present in [C135v2](Yin_C_G0135_v2.md#reciprocal-parity-class-realization) and its L217 antecedent; the present degree4 nonreciprocal instance is checked in full below.
No new literature theorem beyond the explicitly read source interfaces is imported.

<a id="statement"></a>
For the original actual-unit domain above, the residue criterion(1) is exact at every maximal ideal of R and every nonzero prime of O_K.
The weighted maximal-order ideals A=(a^15,b^10,c^6) and D=(E^5,F^3,G^2) agree away from5 and obey125 A subset D subset A, hence1<=[A:D]<=5^(3d), with a power-of5 index and all original residue degrees.
Original-order inclusions are(9)--(10) with the ACTUAL n=[O_K:R] cost.
The actual quartic(12) realizes the extra5 branch and gives D strictly smaller than A; the actual golden and reciprocal quadratic controls give I_R=J_R=A_R=D_R=R.
Section6 supplies the exact finite residue-polynomial test, including repeated reduction/bad-index primes, but makes no higher-depth inference from residue factors.
Section7 preserves the common30d width, denominator and Archimedean limitations.
These statements are a comparison and realizability theorem, not uniform positive joint income or a Mahler gap.

<a id="argument"></a>
The complete proof is Sections1--7, including all three original-polynomial controls, all full-order/order interfaces and all costs.
Root supplied this round's question only; the new proof is this author's work, with C149's older contribution history retained as an input.

<a id="residue-ideal-criterion"></a>
## 1. Exact residue-field criterion

Let k be ANY field of positive characteristic ell.
For values a,b,c in k define E,F,G as above.
If ell!=5, their simultaneous vanishing is equivalent to a=b=c=0.
Indeed the accepted identity gives5a^15=0, hence a=0; E then gives b=0 and G gives c=0.
The converse is immediate.
This proof includes characteristics2 and3 and never divides by either of them.

In characteristic5, their common zero locus is exactly

    (a,b,c)=(v^2,v^3,3v^5), v in k.                    (1)

If a=0, then b=c=0.
If a!=0, let v=b/a; E=0 gives v^2=a,v^3=b, and v!=0.
Let z=c/v^5.
Then F=G=0 gives z^2=4,z^3=2, whence z=2/4=3.
Conversely every displayed triple directly makes E,F,G zero in characteristic5.
This includes the zero point and requires no algebraic closure.

Consequently for any maximal ideal m of R, or nonzero prime ideal q of the full O_K, reduce the ACTUAL a,b,c in its residue field.
Away from5, I is contained in that ideal if and only if a,b,c all belong to it.
Above5 there is exactly the additional nonzero residue curve(1).
In particular the radical supports of I and (a,b,c) agree away from5.
This is a residue criterion, not yet an equality of ideal multiplicities or a norm bound.
For the monogenic order it uses only maximal ideals and residue fields, not a false Dedekind factorization.

<a id="weighted-valuation-comparison"></a>
## 2. Exact weighted valuations away from5, with bounded5 discrepancy

Work at a nonzero prime q of O_K with integer-normalized DVR valuation v, uniformizer pi, residue characteristic ell and v(0)=infinity.
The actual a,b,c are nonzero and integral.
Write

    r=min{v(a)/2,v(b)/3,v(c)/5},
    s=min{v(E)/6,v(F)/10,v(G)/15}.                     (2)

Then s>=r; if ell!=5, equality holds.
At ell=5 one has

    0<=s-r<=v(5)/10.                                  (3)

The lower bound follows term by term: E has valuation at least6r, F at least10r and G at least15r; the integer coefficients cannot lower valuations.
To prove the exact upper statements without adjoining an auxiliary field, let a0 be the residue of a/pi^(v(a)) if v(a)=2r, and0 otherwise.
Define b0,c0 with equality to3r,5r in the same way.
At least one of a0,b0,c0 is nonzero.
If s>r, the lowest-weight coefficient of each defect vanishes and gives

    b0^2-a0^3=0,
    2c0^2-3a0^5=0,
    c0^3-2b0^5=0                                      (4)

in the residue field.
This assertion remains valid when a target weight is not an integer: a term achieving that weight exists only when its base coordinate achieves its defining equality, and the displayed coefficient is otherwise0.
Equivalently, assign a formal variable of weight1/30 to the associated graded DVR and read its lowest coefficients; no extension norm or fractional uniformizer is being introduced.

For ell!=5, Section1 contradicts the nonzero initial triple.
For ell=5, it says that a0,b0,c0 are all nonzero.
Thus v(a)=2r,v(b)=3r,v(c)=5r; since both2r and3r are integers, r is an integer.
We may therefore NORMALIZE INSIDE THE SAME LOCAL FIELD by a'=a/pi^(2r),b'=b/pi^(3r),c'=c/pi^(5r), all units.
Their defects E',F',G' have respective valuations v(E)-6r,v(F)-10r,v(G)-15r, and their weighted minimum is s-r.

Put e=v(5).
Suppose s-r>e/10.
Then v(E')>3e/5,v(F')>e,v(G')>3e/2.
In C149's identity, the coefficient S' has the exact expansion, obtained from b'^2=a'^3+E',

    S'=5a'^12+10a'^9 E'+10a'^6 E'^2
                         +5a'^3 E'^3+E'^4.           (5)

Its first term has valuation e and every other term has strictly larger valuation, so v(S')=e.
The coefficients T',U' of that identity are integral.
Consequently all three terms F'T',8G'U',32E'S' have valuation strictly greater than e, whereas5a'^15 has valuation exactly e.
This contradicts their sum identity and proves(3).
Cases E'=0,F'=0 or G'=0 are covered by infinity; the full triple cannot vanish by C149.

Define genuine nonzero O_K ideals

    A=(a^15,b^10,c^6),
    D=(E^5,F^3,G^2).                                  (6)

Their q-valuations are30r and30s.
Thus the local statement is equivalent to

    D_q=A_q for q not above5,
    (5)^3 A subset D subset A in O_K.                 (7)

In particular A/D is killed by125.
With all original residue degrees retained, its order is a power of5 between1 and5^(3d):

    1<=Norm(D)/Norm(A)=[A:D]<=5^(3d).                 (8)

Here d=[K:Q], not a smaller field degree for one quotient.
The bound uses sum_(q|5) e_q f_q=d, the same full-number-field/DVR scope as [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001).
The ideal valuation interpretation is in the full Dedekind order O_K; it is NOT automatically an equality or inclusion of the original monogenic ideals.

<a id="original-order-denominator-cost"></a>
## 3. Exact original-order statements and the index cost

For ideals in R write I_R=(E,F,G), J_R=(a,b,c), A_R=(a^15,b^10,c^6), D_R=(E^5,F^3,G^2).
C149's identity gives5a^15 in I_R.
Since E*S=b^10-a^15 and G*U=c^6-4b^10, it also gives5b^10 and5c^6 in I_R.
Pigeonhole counting of monomials in three generators now gives the unconditional original-order inclusions

    5 J_R^29 subset I_R subset J_R^2.                 (9)

Indeed a monomial of total exponent29 has a-exponent at least15, b-exponent at least10, or c-exponent at least6; otherwise its total is at most14+9+5=28.
The reverse inclusion follows directly from E,F,G.
No invertibility of these R ideals is used.
In particular, if J_R=R, then5 belongs to I_R.
This assertion does not make I_R the unit ideal.

Let n=[O_K:R] be the ACTUAL additive order index, so n O_K subset R.
Extending A_R,D_R to O_K gives exactly A,D in(6).
Equation(7), followed by clearing each O_K coefficient with n, yields

    n D_R subset A_R,
    125 n A_R subset D_R.                             (10)

For example125a for a in A_R is an O_K-linear combination of E^5,F^3,G^2; multiplication by n places each coefficient in R.
The other inclusion is proved in the same way from D subset A.
This pays a single actual order index, not a declaration that R is integrally closed.
Nothing here bounds n, the heights of those ideal-combination coefficients, or the l1 norm/degree of polynomial representatives in R.
Replacing them by a free integral normalization would be unjustified.

The unweighted maximal-order ideals I=(E,F,G),J=(a,b,c) also obey

    5 J^15 subset I subset J^2.                       (11)

The upper valuation bound follows from5a^15,5b^10,5c^6 in I: v(I)<=v(5)+min{15v(a),10v(b),6v(c)}<=v(5)+15v(J).
Thus if J=O_K, any remaining common ideal divisor is supported above5 and is bounded by(5); no common prime divisor away from5 can create a new joint income.
The smaller exponent15 uses maximal-order valuations; it is not substituted for29 in(9).

<a id="actual-extra-five-control"></a>
## 4. Actual nonreciprocal quartic realizes the extra5 branch

Consider the original integer polynomial

    P(t)=t^4+8t^2+28t+1.                              (12)

Its shift is P(t+1)=t^4+4t^3+14t^2+48t+38.
All nonleading coefficients are even and38 is not divisible by4, so the polynomial is Eisenstein at2 and irreducible over Q.
In the reused elementary criterion, a factorization of this monic integer polynomial would have monic integer factors; their reductions multiply to t^4, so both nonconstant factors have even constant terms, contradicting the constant38.
Thus an original root alpha has degree4 and is an integer unit.
It is nontorsion: if all conjugates were on the unit circle, the t^2 coefficient, the sum of six pair products, would have absolute value at most6, whereas it is8.
This uses an ACTUAL original polynomial, not a prescribed abstract valuation array.

Modulo5, Pbar=t^4+3t^2+3t+1 and Pbar(2)=0.
Hence m=(5,alpha-2) is a maximal ideal of R with residue F5.
The base quotients have the following exact residues:

    a mod m=Pbar(4)/2=2/2=1,
    b mod m=Pbar(3)/3=3/3=1,
    c mod m=3.                                       (13)

For the divided5 quotient, use the INTEGER polynomial delta_5 P(t)=(P(t^5)-P(t)^5)/5, whose value at alpha is c.
At t=2, P(2)=105 so P(2)^5/5 is0 modulo5.
Also32=7 modulo25 and P(7)=2990, so P(32)/5 is598=3 modulo5.
This proves the last residue without dividing a zero residue by5 or assuming any p-derivation descends to R.
The first two computations use the invertible scalars2,3 in F5.

Thus a,b,c are all units in R_m, but E,F,G all lie in m: this is the NONZERO branch v=1 of(1).
In particular J_R localized at m is the unit ideal, whereas I_R localized there is proper.
The generic5 exception in C149 therefore really occurs for an irreducible nontorsion integer-unit polynomial; it cannot be removed from the residue criterion by invoking only those original-domain hypotheses.

For the full-order transfer, the integral injection R subset O_K has a prime q lying over m by the actual accepted [The26b-U002](../audits/literature/The26b/Yin_U002.md#the26b-u002), Stacks Tag00GQ/Lemma10.36.17.
This source registration was pending when the argument was first written; the official statement and complete displayed short proof have now been read, and the canonical unit resolves that pending stage without extending its ancestor-audit scope.
The same residues persist in its residue field, so J_q is the unit ideal and I_q is proper.
In the normalized valuation,0<v_q(I)<=v_q(5) by C149's5a^15 identity.
Moreover v_q(A)=0 but v_q(D)>=2, because every E,F,G has positive integer valuation and their powers are5,3,2.
Thus D!=A, and the actual ratio[A:D] is at least25.
No unramified or depth-one conclusion is claimed, and no Hensel theorem is needed.
The polynomial is not reciprocal and is a fixed positive-measure control, not a near-one sequence or a counterexample to a small-measure-specific assertion.

<a id="actual-unit-defect-ideal-control"></a>
## 5. Actual golden unit has NO joint defect ideal surplus

Reuse the original nontorsion unit from the existing golden-ratio controls: P=t^2-t-1, alpha^2=alpha+1, and R=Z[alpha].
Direct exact reductions give

    a=alpha, b=alpha^3, c=2alpha^5,
    E=2alpha^4,
    F=425alpha+263,
    G=6alpha^15.                                     (14)

For example alpha^3=2alpha+1,alpha^5=5alpha+3,alpha^6=8alpha+5 and alpha^10=55alpha+34.
Thus P(alpha^2)=2alpha,P(alpha^3)=3alpha^3 and P(alpha^5)=10alpha^5, proving the base values; substituting into E,F,G proves the rest.
All powers retain the same original quadratic field.

There is the explicit identity INSIDE THE ORIGINAL ORDER

    1=(2-alpha)F-(12alpha+7)E.                        (15)

Indeed (2-alpha)F=162alpha+101 and (12alpha+7)E=162alpha+100.
Consequently I_R=R.
Also J_R=R since a=alpha is a unit.
The powers in D_R have the same common maximal ideals as E,F,G, so D_R=R; explicitly expand the seventh power of(15), since every resulting monomial is divisible by E^5 or F^3.
Likewise A_R=R since a^15 is a unit.
Thus even before passing to O_K, the new joint ideal need not have any surplus above the base joint ideal, and the ratio in(8) can be1 for an actual nontorsion integer unit.

For further original-norm clarity, Norm(x alpha+y)=y^2+xy-x^2 gives Norm(E)=4, Norm(F)=319=11*29 and Norm(G)=-36.
Thus all three individual defects are NONUNITS despite generating the unit ideal.
Their norm gcd1 also rules out a common maximal ideal, but(15) additionally gives explicit original-order coefficients; the general common-ideal norm is not an integer gcd of separate norms, as explained in Section7.

The irreducible polynomial is the standard actual golden unit already used in [C87](Yin_C_G0087_v1.md#statement); these newly displayed E,F,G computations and Bezout coefficients are checked directly here, not attributed to C87.
Its measure is fixed and positive, so this is not a near-one counterfamily.
It rejects the unrestricted inference that the nonmultiplicative family itself forces a nontrivial common ideal divisor or strict joint ideal income on every nontorsion input.

The same negative conclusion also holds inside the RECIPROCAL original domain.
Take P=t^2-3t+1, alpha=(3+sqrt5)/2, which is irreducible, a unit and nontorsion.
The inherited trace identities with z=3 give C2(z)=7,C3(z)=18,C5(z)=123.
Therefore

    a=2alpha^2, b=5alpha^3, c=24alpha^5,
    E=17alpha^6, F=1056alpha^10, G=7574alpha^15,
    1=497alpha^(-6)E-8alpha^(-10)F.                  (15a)

The last equality is497*17-8*1056=8449-8448=1; negative powers are ACTUAL units of the original R.
Also J_R=R since2 and5 are coprime after multiplying its generators by order units.
Thus I_R=A_R=D_R=R as before.
This control retains its fixed positive measure log((3+sqrt5)/2); it removes reciprocity as a possible rescue of a universal strict joint-ideal inference, but gives no counterexample restricted to a sufficiently small-measure family.

<a id="actual-remainder-local-test"></a>
## 6. A finite original-polynomial residue test, without a good-prime restriction

Use the actual L63 remainder polynomials

    rho_p(t)=rem_P P(t^p)/p in Z[t], deg rho_p<d,
                                  p in{2,3,5}.        (16)

Integrality is established BEFORE reduction modulo a rational prime ell.
Let h be a monic irreducible factor of Pbar over F_ell, allowing Pbar to have repeated factors, and let k_h=F_ell[t]/(h).
The corresponding maximal ideal of R is m_h=(ell,h(alpha)); the base residues in k_h are rho2bar,rho3bar,rho5bar.
Therefore I_R subset m_h exactly when h divides all three reduced defect polynomials

    rho3bar^2-rho2bar^3,
    2rho5bar^2-3rho2bar^5,
    rho5bar^3-2rho3bar^5.                             (17)

For ell!=5 this is equivalent to h dividing EACH of rho2bar,rho3bar,rho5bar.
For ell=5, either all three base residues vanish, or rho2bar is nonzero and, with v=rho3bar/rho2bar IN THE FIELD k_h, their residues are(v^2,v^3,3v^5).
Thus away from5 the radicals of the two gcd polynomials

    gcd(Pbar,rho2bar,rho3bar,rho5bar),
    gcd(Pbar,the three polynomials in(17))             (18)

are equal.
This is a statement about their irreducible factors, NOT equality of multiplicities in a repeated Pbar.
It neither divides by p after reduction nor infers a p-adic depth from one residue equation.

Every full-order prime q over m_h has an injective residue-field map k_h->kappa(q).
Therefore this exact zero/nonzero criterion remains valid for full-order support even when ell divides[O_K:R] or ramifies.
Several q can lie over a given m_h; their individual higher valuations remain the local data of Section2 and cannot be recovered from h alone.
No squarefree or good-prime assumption is smuggled into(16)--(18).

<a id="weighted-ideal-original-costs"></a>
## 7. Original norms, common width and what the comparison does not supply

The weighted ideals compare actual values represented by the following two triples of polynomials, ALL of degree30d:

    A: P(t^2)^15/2^15, P(t^3)^10/3^10, P(t^5)^6/5^6;
    D: H23(t)^5/(-72)^5,
       H25(t)^3/(-800)^3, H35(t)^2/(-30375)^2.         (19)

Their values at alpha are precisely a^15,b^10,c^6 and E^5,F^3,G^2.
These are rational-coefficient original-variable polynomials with the displayed denominators; their evaluation integrality is the existing base/defect fact.
The scalar denominators are retained and are not discarded because ideal norms are integral.
A zero defect label contributes the zero ideal generator; a nonzero label retains its entire original signed norm and all repetitions, as in C149.

For each nonzero generator, divisibility by its actual ideal gives, for example,

    Norm(D) divides |Norm_K(E)|^5 if E!=0,
    Norm(D) divides |Norm_K(F)|^3 if F!=0,
    Norm(D) divides |Norm_K(G)|^2 if G!=0.             (20)

The common ideal Norm(A) is not, in general, the integer gcd of |Norm(a)|^15,|Norm(b)|^10,|Norm(c)|^6: different primes of K over one rational prime can contribute to different norms.
Equations(7)--(8) compare the ACTUAL valuation minima at each prime of K.
In logarithmic form their precise possible extra weighted common-ideal income is

    0<=log Norm(D)-log Norm(A)<=3d log5.              (21)

There is no universal positive lower bound for this difference: the golden control gives zero exactly.
The quartic control shows it can be positive.
Neither fixed control constrains a hypothetical m(P)->0 family.

Retain L=||P||_1 and m=m(P).
For the base triple, ordinary coefficient/whole-root bounds give

    log|Norm(a^15)|<=d[15log(L/2)+30m],
    log|Norm(b^10)|<=d[10log(L/3)+30m],
    log|Norm(c^6)|<=d[6log(L/5)+30m].                 (22)

Each left side is the log absolute full original norm of a nonzero algebraic integer.
The three defect bounds are exactly C149(12) multiplied by5,3,2, with the SAME30dm radial term and coefficient terms5log(L23/72),3log(L25/800),2log(L35/30375).
Those latter coefficient terms are already positive for L>=3, as proved in C149; reusing a weighted ideal does not remove them.
The generic bound L<=2^d exp(m) again leaves an O(d^2) original norm expense.

Finally, (7) does not say A or D is principal, supply a common algebraic divisor, or construct a low-height combination.
Returning actual ideal combinations to the original order costs the index n in(10), and converting those coefficients to original-variable polynomials has no height bound here.
C78's scalar-content normalization only applies when its ACTUAL stronger ideal/content hypotheses hold; the norm comparison is not such a hypothesis.
Thus the new result gives a complete local support/depth comparison and positive/negative actual realizations, while sharply locating the only new common-ideal support at5 and the unresolved original polynomial coefficient/near-one expenses.

<a id="author-freeze"></a>
Author freeze2026-10-15T15:37.
This complete seven-section statement/argument, formulas(1)--(22) and(15a), has been self-checked.
The check retained characteristics2,3,5 separately; fractional r and zero defect/infinite valuation cases; same-field normalization only after r is proved integral; the exact5-adic S expansion and125 bound; all original-order index factors; all three explicit original-polynomial controls and signed norm values; repeated/bad-index residue factors; and common30d polynomial width with all denominators and Archimedean expenses.
The26b-U002 now resolves the earlier source-pending lying-over step at its actual inspected scope.
No Hensel statement, native mathematical run, independent review or unrestricted near-one conclusion is claimed.
Root supplied the question and source-only assistance, not this round's new project proof; C149's earlier root/authorship relationship remains disclosed separately.

## Current assessment
[Selected decision](#decision-current-sylvester-proof-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T15:46 |
| status | open |
| reason | Fix the entire local-ideal comparison and actual polynomial controls for independent review. This is a precise support/depth theorem with paid original-order and Archimedean costs, not uniform positive income or G0001 completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire local-ideal statement](#statement) | Actual nontorsion integer units, exact residue curve, weighted full-order comparison, original-order index costs, all actual realizations and original costs. |
| argument | [Complete seven-section proof](#argument) | Formulas1--22 and15a, all characteristic/fractional-valuation/zero-defect cases and original norm/degree/denominator interfaces. |
| dependency | [Integral defect identity](Yin_C_G0149_v1.md#integral-three-defect-identity) | Exact original-order identity and its coefficients, without dividing by5 or by a nonunit. |
| dependency | [Original defect polynomials and norms](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Three actual numerators, denominators, original degrees, full signed norms and allowed zero individual defects. |
| dependency | [Integral base remainders](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation) | Integral original-order prime quotients and remainder test before reduction, including repeated reduction. |
| dependency | [Nonzero base values](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | Nontorsion excludes equality with another powered conjugate, without reciprocal/Galois restrictions. |
| support | [Full number-field DVR input](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Accepted standard full-order valuation and complete ramification/residue-degree sum scope; ancestor proofs not recursively audited. |
| support | [Actual lying-over statement](../audits/literature/The26b/Yin_U002.md#the26b-u002) | Integral inclusion Z[alpha] into O_K gives a prime above the explicit original-order kernel, without unramified or degree-one inference. |
| support | [Normalization comparison](Yin_C_G0078_v1.md#integer-ideal-energy-closure) | Earlier stronger actual ideal/content hypotheses are not supplied by the new norm comparison. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T15:50 |
| status | proved |
| reason | Adopt the whole local-ideal comparison and actual realizations after R368. The extra weighted ideal support is confined to5 with bounded depth; actual inputs realize both positive and zero extra income, including a reciprocal zero-surplus control. All original-order index and coefficient/norm costs remain. This is not automatic small-measure coverage or unrestricted G0001 completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire local-ideal statement](#statement) | Actual nontorsion integer units, exact residue curve, weighted full-order comparison, original-order index costs, all actual realizations and original costs. |
| argument | [Complete seven-section proof](#argument) | Formulas1--22 and15a, all characteristic/fractional-valuation/zero-defect cases and original norm/degree/denominator interfaces. |
| dependency | [Integral defect identity](Yin_C_G0149_v1.md#integral-three-defect-identity) | Exact original-order identity and its coefficients, without dividing by5 or by a nonunit. |
| dependency | [Original defect polynomials and norms](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Three actual numerators, denominators, original degrees, full signed norms and allowed zero individual defects. |
| dependency | [Integral base remainders](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation) | Integral original-order prime quotients and remainder test before reduction, including repeated reduction. |
| dependency | [Nonzero base values](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | Nontorsion excludes equality with another powered conjugate, without reciprocal/Galois restrictions. |
| support | [Full number-field DVR input](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Accepted standard full-order valuation and complete ramification/residue-degree sum scope; ancestor proofs not recursively audited. |
| support | [Actual lying-over statement](../audits/literature/The26b/Yin_U002.md#the26b-u002) | Integral inclusion Z[alpha] into O_K gives a prime above the explicit original-order kernel, without unramified or degree-one inference. |
| support | [Normalization comparison](Yin_C_G0078_v1.md#integer-ideal-energy-closure) | Earlier stronger actual ideal/content hypotheses are not supplied by the new norm comparison. |
| review | [Actual whole independent review](../audits/reviews/Yin_R_G0368_v1.md#weighted-ideal-whole-independent-finding) | Complete new statement and all seven sections, every local/order/control/cost interface, with root's earlier-input and source-only roles disclosed. |


### Decision current-confluent-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:11 |
| status | proved |
| reason | Select C231#mixed-power-resultant-identities as the complete current home of the identical original L59 full-root cross-exponent nonvanishing, multiplicity and exact resultant conventions at the unchanged used scope. The complete retained proof and actual current statement were read, including non-torsion and degree-drop boundaries; this is routine same-content interface adoption. Mathematical status, selected statement/argument/finding and every relation scope remain. Original dated decisions and R bindings retain their actual L59 inputs, and no new independent review or additional arithmetic surplus is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual nontorsion integer units, exact residue curve, weighted full-order comparison, original-order index costs, all actual realizations and original costs. |
| argument | [Argument](#argument) | Formulas1--22 and15a, all characteristic/fractional-valuation/zero-defect cases and original norm/degree/denominator interfaces. |
| dependency | [Dependency](Yin_C_G0149_v1.md#integral-three-defect-identity) | Exact original-order identity and its coefficients, without dividing by5 or by a nonunit. |
| dependency | [Dependency](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Three actual numerators, denominators, original degrees, full signed norms and allowed zero individual defects. |
| dependency | [Dependency](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation) | Integral original-order prime quotients and remainder test before reduction, including repeated reduction. |
| dependency | [Dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Nontorsion excludes equality with another powered conjugate, without reciprocal/Galois restrictions. |
| support | [Support](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Accepted standard full-order valuation and complete ramification/residue-degree sum scope; ancestor proofs not recursively audited. |
| support | [Support](../audits/literature/The26b/Yin_U002.md#the26b-u002) | Integral inclusion Z[alpha] into O_K gives a prime above the explicit original-order kernel, without unramified or degree-one inference. |
| support | [Support](Yin_C_G0078_v1.md#integer-ideal-energy-closure) | Earlier stronger actual ideal/content hypotheses are not supplied by the new norm comparison. |
| review | [Review](../audits/reviews/Yin_R_G0368_v1.md#weighted-ideal-whole-independent-finding) | Complete new statement and all seven sections, every local/order/control/cost interface, with root's earlier-input and source-only roles disclosed. |


### Decision current-sylvester-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:29 |
| status | proved |
| reason | Select C237 as the complete current responsible home of the identical retained L63 original-order prime quotient, nonreduced Frobenius and exact integral coefficient-pairing/Sylvester interfaces at the actual anchors below. The full proof, current statement and each used scalar/local/index boundary were read; this is same-content locator adoption. Mathematical status, selected statement/argument/finding and all relation scopes remain unchanged. All prior current C226/C231/Haar homes remain selected where present, while old dated decisions and R bindings keep their actual L63 inputs. No new independent review, low-cost norm or uniform arithmetic gain is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual nontorsion integer units, exact residue curve, weighted full-order comparison, original-order index costs, all actual realizations and original costs. |
| argument | [Argument](#argument) | Formulas1--22 and15a, all characteristic/fractional-valuation/zero-defect cases and original norm/degree/denominator interfaces. |
| dependency | [Dependency](Yin_C_G0149_v1.md#integral-three-defect-identity) | Exact original-order identity and its coefficients, without dividing by5 or by a nonunit. |
| dependency | [Dependency](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Three actual numerators, denominators, original degrees, full signed norms and allowed zero individual defects. |
| dependency | [Dependency](Yin_C_G0237_v1.md#base-prime-power-extra-valuation) | Integral original-order prime quotients and remainder test before reduction, including repeated reduction. |
| dependency | [Dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Nontorsion excludes equality with another powered conjugate, without reciprocal/Galois restrictions. |
| support | [Support](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Accepted standard full-order valuation and complete ramification/residue-degree sum scope; ancestor proofs not recursively audited. |
| support | [Support](../audits/literature/The26b/Yin_U002.md#the26b-u002) | Integral inclusion Z[alpha] into O_K gives a prime above the explicit original-order kernel, without unramified or degree-one inference. |
| support | [Support](Yin_C_G0078_v1.md#integer-ideal-energy-closure) | Earlier stronger actual ideal/content hypotheses are not supplied by the new norm comparison. |
| review | [Review](../audits/reviews/Yin_R_G0368_v1.md#weighted-ideal-whole-independent-finding) | Complete new statement and all seven sections, every local/order/control/cost interface, with root's earlier-input and source-only roles disclosed. |

