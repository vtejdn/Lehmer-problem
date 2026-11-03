---
author: Yin
---
# Quantitative dyadic image defect of the actual residual trace order

Date: 2026-10-20T14:41.
Human author Yin.
Root proposed the odd-index/content chain and then the quantitative cluster image bound.
The draft_inventory_later agent supplied the stronger ramified-local contradiction under odd index and completed the local kernel, saturation, exact cluster cases and full index proof in author discussion with root.
Both are contributors to this theorem and its complete retained intermediate arguments.
The two author developments on2026-10-20T14:34 and2026-10-20T14:37 are preserved below.
This is a distinct trace-order rank/index question, not a revision of the canonical-degree statement in C196.
The author contributed to the old original-return portion of C191v2; its actual local arithmetic is reused through the independent R468, and those older return formulas are not inputs here.
No numerical computation, parameter scan, actual near-one construction or independent review of this new theorem is claimed.

<a id="statement"></a>
## Exact theorem statement

Let P in Z[z] be monic irreducible reciprocal nontorsion, of degree d=2r and constant coefficient1.
For a root alpha set K=Q(alpha), delta=alpha+alpha^(-1), and assume F=Q(delta) is totally real.
Let T in Z[X] be its actual monic degree-r minimal polynomial, so P(z)=z^r T(z+z^(-1)) and[K:F]=2.
Use C_n(z+z^(-1))=z^n+z^(-n) and the ACTUAL integer quotient polynomials

    theta_p=rem_T T(C_p)/p in Z[X], p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5,
    A_tr=Z[delta], O=O_F, J=[O:A_tr],
    t_2=dim_(F_2) O/(A_tr+2O).

The values a,b,c are nonzero integral elements of this specified trace order.
The quotient defining t_2 is an additive F_2-vector space; no ideal property of A_tr in O is assumed.

**A. Exact image, without a residual hypothesis.**
For every p over2 normalize v_p to have value group Z, write e_p=v_p(2), f_p=[k_p:F_2], phi_p=minpol_(F_2)(delta_bar), h_p=deg phi_p, and m_p=f_p/h_p.
Let eta_p be the unique lift of delta_bar solving C_(2^(h_p))(eta_p)=eta_p in the actual completion F_p, and let j_p=v_p(delta-eta_p)>0.
Nontorsion makes this positive integer finite.
Group primes with the same phi and put

    kappa_p=ceil(e_p/j_p),
    kappa_phi=max_(p in the phi cluster) kappa_p,
    S_phi=sum_(p in the phi cluster)e_p f_p/deg phi.

Then the exact local kernel and complete image are

    ker(F_2[X] -> O_(F_p)/2O_(F_p))=(phi_p^(kappa_p)),
    image(A_tr -> O/2O)
         isomorphic to F_2[X]/product_phi phi^(kappa_phi),
    t_2=r-sum_phi deg(phi) kappa_phi.

The image is not assumed to be the full maximal-order quotient, and h_p need not equal f_p.

**B. Quantitative full residual obstruction.**
If for either s in{1,-1} one has

    f=0, e+s g=0, g!=0,

then every e_p>=2 and

    kappa_phi<=(10/11)S_phi for every cluster,
    dim_(F_2) image(A_tr -> O/2O)<=floor(10r/11),
    v_2(J)>=t_2>=ceil(r/11),
    2^(ceil(r/11)) divides J.

All dyadic primes, their full residue multiplicities and the original degree r are counted.
No bounded degree, small measure, Galois or maximal-order hypothesis is imposed.

**C. Odd-index and retained conditional content mechanism.**
If J is odd and f=0, every prime of F over2 is unramified.
Hence the full residual system in part B is impossible when J is odd, at every degree and for both signs.
Separately, whenever each residue cluster contains a single prime, f=0 gives a/2,c/4 in O, and the full residual hypotheses give g/64 in O.
Under odd J these divisions return to A_tr; the conditional canonical polynomial G_can=rem_T(theta_5^3-2theta_3^5) then has every coefficient divisible by64 and its squared Haar logarithm is at least12log2.
The latter full-residual odd-index hypothesis is excluded by the preceding stronger result, so this retained chain is not asserted to be a nonempty canonical family.
The f-only divisibility implications and the more general singleton-cluster argument retain their own conditional scopes.

These statements concern the index of the ACTUAL trace order Z[delta].
They do not imply an upper bound for that index from m(P), residual existence at even index, automatic odd-index coverage of near-one inputs, or an unrestricted Mahler gap.
The complete argument and all intermediate scopes follow.

<a id="argument"></a>
## Complete proof and retained mechanisms

<a id="odd-index-trace-order-residual-obstruction"></a>
### Odd trace-order index excludes the full actual residual system at every degree

Date: 2026-10-20T14:34.
Human author Yin.
Root proposed the odd-index trace-order condition, its singleton-cluster implication and the64-divisibility/Haar chain.
The draft_inventory_later agent checked all of those implications, derived the stronger ramified-local contradiction below and assembled the complete arbitrary-prime and order-saturation argument.
Root separately checked the stronger argument during author discussion and contributed to its final scope assessment.
Both are mathematical contributors; this account is author work awaiting independent review.
No mathematical computation, coefficient search or new numerical input is used.

#### Reuse, attribution and exact statement

The reuse check read [L66's actual trace quotient](../ledger/Yin_L_G0066_v1.md#reciprocal-frobenius-two-copy-module), [C14's unique power-basis coordinates and overorder boundary](Yin_C_G0014_v2.md#short-width-power-order-obstruction), [C78's order-content distinction](Yin_C_G0078_v1.md#statement), [C191v2's complete local proof](Yin_C_G0191_v2.md#argument), [C196v3's original multiplicity interface](Yin_C_G0196_v3.md#canonical-c5-residue-graph), and [L205's local maximal-order proof](../ledger/Yin_L_G0205_v1.md#minimal-frobenius-maximal-order).
C14/C78 distinguish actual order membership and coordinate content from mere norm integrality; no change of order is free.
L205 obtains a related local factorization under minimal Frobenius-resultant income, a hypothesis not imposed here.
The new issue is the interaction of the explicit odd trace-order index with the ACTUAL quotient equations.
No general theorem about norm floors or a finite canonical degree cutoff is substituted for that interaction.

<a id="trace-order-dedekind-kummer-attribution"></a>
The factorization part is the classical Dedekind--Kummer interface, not a novelty claim.
During the original 2026-10-20 author work, the author directly text-read the official online Theorem 6.14 and its displayed proof on printed p. 9 of Andrew V. Sutherland's MIT 18.785 Fall 2021 Lecture 6, dated 27 September 2021.
The official PDF was obtained and registered separately on 2026-10-20T14:45 as Sut21c; the matching selected passages were then read back in the [retained 16-page artifact](../literature/pdf/Sut21c.pdf).
[Sut21c-U001](../audits/literature/Sut21c/Yin_U001.md#sut21c-u001) owns the precise Section 6.5/Theorem 6.14 inspection and applicability scope.
Its monogenic hypothesis gives primes generated by the base prime and lifted irreducible factors, with the corresponding residue degrees and exponents.
Here odd index makes the localized order monogenic at 2, and the complete finite-ring proof below supplies the needed specialization directly.
The earlier online reading and later successful retention are distinct historical facts; neither supplies a whole-course audit, a new project proof review or reliance on the later conductor argument.
The existing [The26b-U001 local interface](../audits/literature/The26b/Yin_U001.md#the26b-u001) retains its actual DVR, all-prime degree-sum and standard finiteness boundaries.

Use the complete original [C153v2 trace domain](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain).
Thus P is monic irreducible reciprocal nontorsion, has constant1 and degree d=2r; K=Q(alpha), delta=alpha+alpha^(-1), F=Q(delta) is totally real, and T is its actual monic minimal polynomial with P(z)=z^r T(z+z^(-1)).
Put

    A_tr=Z[delta], O=O_F, J=[O:A_tr],
    theta_p=rem_T T(C_p)/p in Z[X], p=2,3,5,
    a=theta_2(delta), b=theta_3(delta),
    c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.         (OI1)

All three quotient values are the actual nonzero integral values in A_tr.
The finite index J refers to this trace order, not Z[alpha], an unspecified isomorphic field or another choice of integral generator.
The claim proved in this section is

    J odd and f=0 imply every prime of F over2
                                      is unramified;
    J odd excludes f=e+s g=0,g!=0
                                  for either s in{1,-1}.     (OI2)

Equivalently, any actual full residual input must have even J.
There is no degree, coefficient, ramification-degree or m(P) cutoff in this implication.
It gives a necessary order-index defect for a residual input, not automatic near-one coverage by odd J.
The initially proposed64-divisibility chain is retained fully below, with its conditional and eventually empty full-residual scope explicit.

<a id="odd-index-dyadic-order-and-clusters"></a>
#### Odd index gives exact dyadic order saturation and singleton clusters

The integral power basis1,delta,...,delta^(r-1) makes A_tr a full order of rank r, so O/A_tr is a finite group of order J.
If J is odd, multiplication by2^k is a bijection of this group for every k>=1.
Therefore

    A_tr intersect 2^k O =2^k A_tr,
    A_tr+2^k O=O,
    A_tr/2^k A_tr isomorphic to O/2^k O.          (OI3)

For the first equality, 2^k y in A_tr with y in O forces the class of y to vanish.
For the second, choose for any y in O a class z with2^k[z]=[y], so y-2^k z belongs to A_tr.
The induced map gives the third assertion with its exact kernel.
These are statements about actual coordinates, not just full norms.

At k=1, monic reduction and the ordinary all-prime decomposition give

    F_2[X]/(Tbar) isomorphic to O/2O
         isomorphic to product_(p|2) O_(F_p)/2O_(F_p).
                                                            (OI4)

The final factors are local finite rings with maximal-ideal filtrations of length e_p and residue field k_p of degree f_p over F_2, in the same convention as C191.
Every ring isomorphism here is induced by the actual delta evaluation.
The maximal ideals of F_2[X]/(Tbar) are indexed by its distinct monic irreducible factors phi.
The maximal ideals on the right are indexed by the actual primes p over2.
The isomorphism therefore identifies each phi with EXACTLY ONE prime p, and its residue map identifies

    F_2[X]/(phi) with k_p,
    h_p=deg(phi)=f_p.

In particular no two different primes have the same delta-residue minimal polynomial.
This is a singleton in EVERY residue cluster, not a claim that F has only one prime over2.
The actual repeated exponent formula of C191 now gives

    Tbar=product_(p|2) phi_p^(e_p),
    O_(F_p)/2O_(F_p) isomorphic to
                                  F_2[X]/(phi_p^(e_p)).       (OI5)

The local isomorphism follows by localizing(OI4) at the corresponding maximal ideal; all other irreducible factors are units there.
This retains repeated factors, all residue degrees and all primes.
It does not assume that2 is unramified or that any f_p equals1.

<a id="singleton-cluster-exact-quotient-and-content"></a>
#### Exact self-cluster values and the complete64-divisibility chain

Use the C191 periodic lift eta_p for C_(2^h)(X)-X in the actual F_p, where h=deg phi_p.
Normalize v_p to have value group Z and set

    e_p=v_p(2), A_p=v_p(a), C_p=v_p(c),
    beta_p=A_p/e_p, j_p=v_p(delta-eta_p)>0.

Its existence, simple-root uniqueness and delta!=eta_p are precisely the accepted C191/Con26e interface, with nontorsion retaining finite positive j_p.
The original matching-factor calculation of C191 is an EXACT equality when the cluster contains only p.
Indeed all nonmatching factors are units, and every matching self factor has exact2-adic value j_p/e_p because the C2 lift displacement has strictly larger value.
There are e_p f_p/h of those factors.
Consequently the correctly divided ACTUAL quotient satisfies

    1+beta_p=(f_p/h)j_p,
    beta_p=j_p-1 in Z under(OI5).                (OI6)

The second equality uses f_p=h; the first already shows that any singleton cluster has an integral beta_p, even without that equality.
Thus the globally-one-prime conclusion printed in C191 is being reused at its actual self-factor proof scope, with the per-cluster application checked explicitly.
No positive contribution from another residue cluster is missing.

Assume f=0.
Then5A_p=e_p+2C_p and beta_p>=1/5.
Its integrality in(OI6) yields beta_p>=1, hence

    A_p>=e_p, C_p>=2e_p at EVERY p|2.
    If also e+s g=0,g!=0, then
    G_p=v_p(g)=3C_p>=6e_p at EVERY p|2.          (OI7)

The last equality is the [C178 full residual identity](Yin_C_G0178_v1.md#statement), not an f-only assertion.
More generally, if every cluster is a singleton without assuming odd J, the first equality of(OI6) still makes every beta_p a positive integer under f=0, so the local inequalities(OI7) remain valid.
Odd index is needed for the later return from the maximal order to A_tr, not for this conditional singleton-cluster valuation deduction.
The division statements have a full global meaning: a/2,c/4 and, in the full residual case,g/64 are integral at every dyadic prime by(OI7), and at every odd prime because their denominators are2-powers and the original elements are integral.
They therefore belong to O.
Using(OI3) gives

    a/2 in A_tr, c/4 in A_tr,
    g/64 in A_tr under the full residual hypothesis.          (OI8)

The assertion that an element is integral at every finite prime iff it lies in O is the standard maximal-order/DVR intersection already used by the exact order and local-field interfaces; no selected-prime norm is substituted for it.
One may equivalently check the fractional principal ideals' valuations at every prime.
This is why odd places and actual order saturation are both required before making a coefficient conclusion.

Let G_can=rem_T(theta_5^3-2theta_3^5), and assume g!=0.
The unique rational representative of g/64 of degree below r is G_can/64.
Its membership in A_tr makes those coordinates integers, so

    G_can in64 Z[X],
    H_64(z)=z^w(G_can/64)(z+z^(-1)) in Z[z] minus{0},
    w=deg G_can<r,
    I_can=12log2+2m(H_64)>=12log2.               (OI9)

The scalar Jensen convention is the existing [Smy08-U001 normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
For w=0, H_64 is a nonzero integer constant; for w>0 it has degree2w and nonzero endpoints.
All circle zeros remain logarithmically integrable.
This conditional chain works at every width and retains all dyadic divisibilities, rather than inferring coefficient content from a large norm.
The next argument shows that its full residual assumptions are actually empty under odd J, so(OI9) is not advertised as a nonempty residual family.
The f-only order-divisibility implications in(OI8) retain their own conditional scope.

<a id="odd-index-ramified-periodic-lift-obstruction"></a>
#### The stronger ramified-prime contradiction

Continue with odd J, and suppose p over2 is ramified, so e_p>=2.
Write phi=phi_p, h=f_p, and choose any monic integer coefficient lift Phi of phi.
Under(OI5), the maximal ideal of the finite local ring O_(F_p)/2O_(F_p) corresponds to the ideal generated by phi in F_2[X]/(phi^e_p).
Taking its full preimage in the DVR O_(F_p) therefore gives

    (2,Phi(delta)) O_(F_p)=maxideal_p,
    min{e_p,v_p(Phi(delta))}=1.

As e_p>=2, this forces

    v_p(Phi(delta))=1.                           (OI10)

This step uses the actual generation of the finite local ring by delta, not merely generation of its residue field.
It is exactly where the odd-index saturation matters beyond the weaker singleton-cluster estimate.

Put F_h(X)=C_(2^h)(X)-X.
Its reduction is X^(2^h)-X, which has derivative-1 and contains phi exactly once because deg phi=h.
Thus for integer polynomials S,M one has

    F_h=Phi S+2M, phi not dividing Sbar.

At delta, S(delta) is a unit, so the first term has value1 by(OI10), whereas the second has value at least e_p>=2.
There is no cancellation, and

    v_p(F_h(delta))=1.                           (OI11)

The already constructed periodic root eta_p has the same residue as delta and F_h(eta_p)=0.
The polynomial difference factors as
F_h(delta)-F_h(eta_p)=(delta-eta_p)D(delta,eta_p),
where D is integral and reduces to F_h'(delta_bar)=-1.
Hence this difference quotient is a unit, and(OI11) gives j_p=1.
The exact singleton equality(OI6) then gives beta_p=0, or A_p=0.
But f=0 gives beta_p>=1/5 at every prime by C191.
Therefore

    J odd and f=0 rule out ANY ramified prime over2.          (OI12)

No assumption of total ramification, global uniqueness of a dyadic prime, residue degree1, Galoisness or bounded r is used.
The linear factors phi=X and phi=X+1 are included: the periodic polynomial still has simple reduction there and the same maximal-ideal argument applies.
The argument does not claim f=0 alone is impossible when all dyadic primes are unramified.

<a id="odd-index-full-residual-exclusion"></a>
#### Full exclusion and the exact all-degree boundary

Finally impose both f=0 and e+s g=0 with g!=0.
If J were odd, (OI12) would make every prime over2 unramified.
There is at least one such prime in the number field F, and C178 excludes the full residual system in the presence of even one unramified2-prime.
This contradiction proves(OI2) for both signs.
Equivalently,

    f=e+s g=0,g!=0 imply2 divides[O_F:Z[delta]].  (OI13)

This is an all-degree obstruction on the actual trace-order class and is stronger there than the conditional64-coefficient conclusion.
It is not the converse: an even index does not supply an actual residual input, a favorable canonical Haar value or any near-one realization.
An odd index is not automatically forced by small total m(P), by total reality, by integrality of a,b,c or by the existence of an abstract field model.
The previously established positive original norm gate and the separate full signed transfer obligation remain distinct.
Neither a new unrestricted Mahler gap nor an all-input canonical Haar theorem follows.

| Input | Exact role |
| --- | --- |
| C153v2 and L66, linked above | Actual original trace field and nonzero integral divided quotient polynomials in the specified monogenic trace order. |
| C191v2 actual local proof and its whole R468 evidence | All matching roots, full local residue multiplicities, periodic lift, strict self distance, actual division by2 and the positive f-only valuation. |
| C178 full residual theorem | Exact G_p=3C_p and the exclusion at a single unramified dyadic prime, only under both residual equations. |
| C14/C78 and L205 comparisons | Existing coordinate/order distinction and local-order algebra; their different hypotheses are not imported as automatic coverage. |
| The26b-U001 and Con26e through C191 | Accepted finite local/DVR conventions and simple periodic-root lifting, without extending their original source-proof scope. |
| Smy08-U001 | Only the retained scalar Jensen consequence for the conditional nonzero integer H_64. |
| Dedekind--Kummer, MIT Lecture6 Theorem6.14 | Primary naming/statement attribution for the classical factorization step; finite-ring saturation and the new actual-quotient contradiction are proved explicitly here. |



<a id="quantitative-dyadic-trace-order-defect"></a>
### Full residual inputs lose at least one eleventh of the trace order modulo2

Date: 2026-10-20T14:37.
Human author Yin.
Root supplied the quantitative local-image formula and the two cluster cases extending the preceding odd-index question.
The draft_inventory_later agent checked and completed the exact local polynomial kernel, the truncated valuation argument, the all-prime intersection, the unequal-distance equality and the finite-index conclusion.
Both are contributors, and this is author mathematics awaiting independent whole review.
The assertion is about actual trace-order rank and index at arbitrary degree, not a new canonical-degree cutoff.
No mathematical computation or new original input is supplied.

#### Exact unrestricted-index statement

Use all the original definitions and hypotheses of(OI1), but DO NOT assume J odd.
Impose both actual residual equations f=e+s g=0 and g!=0, with either s in{1,-1}.
Set

    t_2=dim_(F_2) O/(A_tr+2O),
    J=[O:A_tr].

Then

    t_2>=ceil(r/11),
    v_2(J)>=t_2>=ceil(r/11),
    2^(ceil(r/11)) divides J.                    (QD1)

Every original completion and its full residue multiplicity is retained.
No residue-degree bound, Galois assumption, single global dyadic prime, maximal power order, bounded canonical degree or small m(P) is assumed.
The positive rank defect is stronger information than the parity conclusion(OI13).
It does not bound m(P) below: no uniform upper bound on this order index from small total Mahler measure is supplied.

<a id="trace-order-local-image-exact-kernel"></a>
#### The exact local polynomial kernel without order saturation

For each actual p over2, use C191's notation

    e_p=v_p(2), f_p=[k_p:F_2],
    phi_p=minpol_(F_2)(delta_bar), h_p=deg phi_p,
    m_p=f_p/h_p, n_p=e_p m_p,
    j_p=v_p(delta-eta_p) in Z_(>0).

Here eta_p is the existing simple periodic lift for C_(2^(h_p))(X)-X.
There is no assertion that delta_bar generates k_p; m_p may exceed1.
Let Phi_p be any monic integer lift of phi_p.
The polynomial F_h=C_(2^h)-X reduces to X^(2^h)-X, which contains phi_p once, so

    F_h=Phi_p S+2M, S(delta) a local unit.

The same integral difference quotient used in(OI11) is a unit, and hence v_p(F_h(delta))=j_p.
It follows that

    j_p<e_p implies v_p(Phi_p(delta))=j_p;
    j_p>=e_p implies v_p(Phi_p(delta))>=e_p.       (QD2)

For the first line, a term of value below e_p cannot come from2M; equality of the first term's value with j_p follows by the unequal-valuation rule.
For the second, a value of Phi_p(delta) below e_p would force F_h(delta) to have that same value and contradict j_p>=e_p.
The value of Phi_p(delta) may be infinite in the second case; no equality to j_p is claimed there.

Consider the actual algebra map

    F_2[X] -> O_(F_p)/2O_(F_p), X -> delta.

For a nonzero polynomial Rbar=phi_p^k Ubar with phi_p not dividing Ubar, choose integer lifts.
Evaluation of Ubar is a local unit, and changing the lift adds a multiple of2.
Thus Rbar maps to zero exactly when k v_p(Phi_p(delta))>=e_p.
Combining this with(QD2), including its infinite-value case, proves

    kernel=(phi_p^(kappa_p)),
    kappa_p=ceil(e_p/j_p).                       (QD3)

The image may be a proper subalgebra of the local quotient.
In particular the proof uses neither equality with the local maximal order nor primitive residue generation.
The nilpotence exponent is computed from actual evaluation modulo2; it is not assumed to be e_p.

Group the primes by common phi, let h=deg phi, and put

    kappa_phi=max_(p in cluster) kappa_p,
    S_phi=sum_(p in cluster)n_p.

The kernel of the map into the product of ALL local factors is the intersection of the local kernels.
Within a cluster this is the largest power phi^(kappa_phi), and distinct irreducibles are coprime.
Consequently

    image(A_tr -> O/2O)
      isomorphic to F_2[X]/product_phi phi^(kappa_phi),
    dim_(F_2) image=sum_phi h kappa_phi,
    r=sum_phi h S_phi,
    t_2=r-sum_phi h kappa_phi.                   (QD4)

This is the image of A_tr modulo the maximal-order2O, or equivalently A_tr/(A_tr intersect2O).
It is NOT an assertion that A_tr/2A_tr injects into O/2O when the index is even.
The original r in(QD4) follows from C191's full e_p f_p count and the accepted all-prime degree sum.
The exact image formula(QD2)--(QD4) uses the original trace domain and nontorsion but no residual equation; the full residual assumptions enter the quantitative bound in the next subsection.

<a id="trace-order-cluster-image-eleven-bound"></a>
#### Every residue cluster has image dimension at most ten elevenths

The full residual hypotheses and C178 exclude every e_p=1, so e_p>=2 at all dyadic primes.
The same f=0 identity gives beta_p=A_p/e_p>=1/5.
Fix a cluster and any p in it.

First suppose m_p j_p>=2.
If j_p>=2, then

    kappa_p<=ceil(e_p/2)<=2e_p/3<=2n_p/3.

For even e_p the middle inequality is immediate; for odd e_p=2u+1>=3 it is equivalent to u>=1.
If instead j_p=1, then m_p>=2 and kappa_p=e_p<=n_p/2.
Therefore in either case

    kappa_p<=(2/3)S_phi<=(10/11)S_phi.           (QD5)

The e_p>=2 hypothesis is needed here; the estimate is not claimed under f=0 alone if an unramified prime is present.

Now suppose m_p=j_p=1.
Then n_p=e_p and kappa_p=e_p.
Write e=e_p and R=sum_(q!=p in cluster)n_q, so S_phi=e+R.
If R<e/10, each other prime q satisfies e_q<=n_q<=R and

    t_q=j_q/e_q>=1/e_q>10/e,
    ell_p=v_2(C2(delta)-C2(eta_p))=2/e.          (QD6)

The last equality uses j_p=1 and e>=2: the quadratic displacement has value2/e, strictly below the linear term's value at least1+1/e.
Thus every other matching-root distance is strictly greater than ell_p.
C191's actual factor calculation is then an equality for EACH such factor, not just its stated lower bound.
The self factors contribute exactly1 in total and the other factors exactly2R/e, while every nonmatching factor is a unit.
This gives

    beta_p=2R/e<1/5,

contradicting f=0.
The case R=0 uses the same equality with an empty other-factor sum.
Therefore R>=e/10, which is exactly

    kappa_p=e<=(10/11)(e+R)
                          =(10/11)S_phi.        (QD7)

These cases apply to every p, whether or not it attains the maximum kappa_phi and whether or not the cluster contains many primes.
Taking the maximum yields

    kappa_phi<=(10/11)S_phi for EVERY phi.       (QD8)

No sum of only selected residue degrees or good-prime subset is used.

<a id="trace-order-rank-and-index-conclusion"></a>
#### Complete rank loss, index and retained limitations

Multiply(QD8) by the corresponding h and sum all clusters in(QD4).
Then the image dimension is at most10r/11, so

    t_2>=r/11, hence t_2>=ceil(r/11).             (QD9)

For the finite group Q=O/A_tr, the quotient Q/2Q is exactly O/(A_tr+2O).
Its order is2^(t_2), and as a quotient of Q its order divides J.
Therefore v_2(J)>=t_2, proving every assertion in(QD1) without assuming a particular integral basis or Smith form.

This strengthens odd-index impossibility by quantifying the necessary defect in the actual trace power order.
The f-only implication(OI12), the full odd-index contradiction and the exact64-divisibility/coordinate argument remain retained above at their separate scopes.
The full-residual odd-index conditions for the64 conclusion are empty; the more general singleton-cluster calculation and the f-only implications keep their precise conditional meanings.
A large2-primary index need not itself force large total m(P), and no such implication is claimed.
The result does not produce a residual input at even index, a small-measure family, a canonical Haar saving or a paid rational transfer.
It isolates the order defect that any future actual residual construction or uniform transfer argument must accommodate.

The complete logical inputs are C153/L66 for the original trace order, C191v2 with its independently reviewed R468 for actual local factors and periodic comparisons, C178 for all e_p>=2 and the exact residual valuation, and the accepted The26b/Con26e local conventions already used there.
The new finite-image and rank argument is proved explicitly in(QD2)--(QD9).
The author did contribute to C191's older original-return formulas; those formulas are not premises here, and its accepted local arithmetic is reused through R468 rather than described as a new independent review.
The proof remains author work pending whole independent review; no further numerical constant improvement or new branch is supplied.

<a id="exact-inputs"></a>
## Exact inputs and source boundaries

| Input | Exact role |
| --- | --- |
| [C153v2 actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original P/K/F/T and the nonzero integral quotient values; no abstract residual triple is substituted. |
| [L66 exact integral quotient](../ledger/Yin_L_G0066_v1.md#reciprocal-frobenius-two-copy-module) | Integer remainder divisibility and membership in the actual trace power order. |
| [C191v2 local proof](Yin_C_G0191_v2.md#argument) | All local factors and multiplicities, simple periodic lifts, exact unequal-distance contributions, actual division by2 and f-only beta>=1/5. |
| [C178 full residual theorem](Yin_C_G0178_v1.md#statement) | All e_p>=2 through the unramified exclusion and G_p=3C_p only under both residual equations. |
| [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Original-field DVR normalization, standard maximal-order/local-factor interface and complete degree sum, with the recorded source-proof limits. |
| [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Complete-field simple-root periodic lift already used by C191, with its actual integral unit-derivative hypotheses. |
| [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Scalar Jensen and circle-zero convention only for the retained conditional64-content Haar conclusion. |
| [R468](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Existing C191 evidence at the needed local scope, with initial review context currently unknown; not a review of the new trace-order theorem. |
| [Classical attribution account](#trace-order-dedekind-kummer-attribution) | Retained Sut21c and Sut21c-U001, with earlier online reading, later acquisition and exact naming/applicability scope preserved; no enlarged original-source audit. |

The C14/C78 order-content and L205 maximal-order accounts in the reuse paragraph are comparisons and elementary-coordinate guidance, not hypotheses replacing odd index or the new local image proof.
The rank formula and all ten-elevenths estimates are proved here.
No current mutable draft, manuscript or new computation is a logical premise.

## Current assessment
[Selected decision](#decision-current-local-trace-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T14:41 |
| status | open |
| reason | Register the complete arbitrary-degree trace-order image/index obstruction, its exact local kernel, all-cluster quantitative bound, stronger f-only odd-index ramification consequence and full retained64-content mechanism. Both authors contributed; whole noncontributor review is required before adoption. No near-one coverage or uniform transfer is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete trace-order theorem](#statement) | Exact image formula, t_2>=ceil(r/11), v_2(J)>=t_2, all original full-residual hypotheses and primes, f-only odd-index conclusion, singleton-cluster content and its empty full-residual odd-index boundary. |
| argument | [Complete original proof](#argument) | All OI1--OI13 and QD1--QD9, including CRT/saturation, every local kernel and finite-index step, original periodic/self-factor equality, both quantitative cases and no unsupported Mahler inference. |
| dependency | [Original trace domain](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Same actual P,T,K,F and nonzero quotient values. |
| dependency | [Integral trace quotient](../ledger/Yin_L_G0066_v1.md#reciprocal-frobenius-two-copy-module) | Monic integer remainders and actual order membership. |
| dependency | [All local factors and lifts](Yin_C_G0191_v2.md#argument) | Local Sections1--3 only, exact root multiplicities and unequal distances, beta>=1/5; old original-return formulas are not used. |
| dependency | [Full residual prime exclusion](Yin_C_G0178_v1.md#statement) | e_p>=2 at EVERY prime and G_p=3C_p under the complete residual system. |
| dependency | [Local-field and maximal-order conventions](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Exact accepted unit and original completion/valuation/degree conventions with unchanged ancestor-proof limits. |
| dependency | [Simple periodic lift](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Actual complete finite F_p, integral polynomial and unit derivative; no new extension theorem. |
| dependency | [Scalar integer Haar bound](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Conditional H_64 with full scalar12log2, constants and integrable circle zeros. |
| support | [Actual independent C191 review](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Existing local arithmetic coverage with author-overlap boundary; does not review this candidate. |
| support | [Classical source attribution](#trace-order-dedekind-kummer-attribution) | Actual retained MIT Lecture 6 Theorem 6.14 and Sut21c-U001 inspection, naming/applicability and fully proved local specialization; prior online history and later acquisition stay distinct. |
| support | [Complete inputs and boundaries](#exact-inputs) | Nine input rows, comparison-versus-dependency roles, author contributions, no computation, actual order and all-degree limits. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T15:01 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft arithmetic and transfer inquiries. |
| reason | Adopt the exact local image and complete trace-order index theorem through actual whole consumer R480. Full original residual inputs satisfy t_2>=ceil(r/11) and v_2([O_F:Z[delta]])>=t_2 at arbitrary degree. The f-only odd-index ramification exclusion, all singleton/content steps and the empty full-residual odd-index boundary remain explicit. The actual Sut21c artifact and source unit close the identified source-retention issue without changing mathematics. No upper index bound from m(P), even-index realization or uniform Mahler transfer is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete trace-order theorem](#statement) | Exact image formula, t_2>=ceil(r/11), v_2(J)>=t_2, all original full-residual hypotheses and primes, f-only odd-index conclusion, singleton-cluster content and its empty full-residual odd-index boundary. |
| argument | [Complete original proof](#argument) | All OI1--OI13 and QD1--QD9, including CRT/saturation, every local kernel and finite-index step, original periodic/self-factor equality, both quantitative cases and no unsupported Mahler inference. |
| dependency | [Original trace domain](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Same actual P,T,K,F and nonzero quotient values. |
| dependency | [Integral trace quotient](../ledger/Yin_L_G0066_v1.md#reciprocal-frobenius-two-copy-module) | Monic integer remainders and actual order membership. |
| dependency | [All local factors and lifts](Yin_C_G0191_v2.md#argument) | Local Sections1--3 only, exact root multiplicities and unequal distances, beta>=1/5; old original-return formulas are not used. |
| dependency | [Full residual prime exclusion](Yin_C_G0178_v1.md#statement) | e_p>=2 at EVERY prime and G_p=3C_p under the complete residual system. |
| dependency | [Local-field and maximal-order conventions](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Exact accepted unit and original completion/valuation/degree conventions with unchanged ancestor-proof limits. |
| dependency | [Simple periodic lift](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Actual complete finite F_p, integral polynomial and unit derivative; no new extension theorem. |
| dependency | [Scalar integer Haar bound](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Conditional H_64 with full scalar12log2, constants and integrable circle zeros. |
| support | [Actual C191 review](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Existing local arithmetic coverage with author-overlap boundary; does not review this candidate. |
| support | [Classical source attribution](#trace-order-dedekind-kummer-attribution) | Actual retained MIT Lecture 6 Theorem 6.14 and Sut21c-U001 inspection, naming/applicability and fully proved local specialization; prior online history and later acquisition stay distinct. |
| support | [Complete inputs and boundaries](#exact-inputs) | Nine input rows, comparison-versus-dependency roles, author contributions, no computation, actual order and all-degree limits. |
| review | [Whole trace-order consumer finding](../audits/reviews/Yin_R_G0480_v1.md#dyadic-trace-order-image-whole-finding) | Entire actual OI1--OI13 and QD1--QD9, all original and f-only domains, exact image kernels and all-prime dimensions, ten-elevenths cases, ceilings, index divisibility and conditional64 scalar; all input/source scopes checked with upstream author roles disclosed and actual independent evidence reused. |


### Decision current-local-trace-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:51 |
| status | proved |
| reason | Select C241/C243 as the complete current responsible homes for the identical already used L64 unramified local or L66 reciprocal trace/order/module interfaces at the exact selected anchors below. The full original arguments, current extracted statements and used guards were read; this is same-content locator adoption. Status, selected statement/argument/finding, all relation scopes and every other current proof home remain unchanged. Prior dated decisions and R bindings keep their actual L64/L66 inputs; no new independent review, local assumption, cheaper entropy normalization or stronger arithmetic estimate is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact image formula, t_2>=ceil(r/11), v_2(J)>=t_2, all original full-residual hypotheses and primes, f-only odd-index conclusion, singleton-cluster content and its empty full-residual odd-index boundary. |
| argument | [Argument](#argument) | All OI1--OI13 and QD1--QD9, including CRT/saturation, every local kernel and finite-index step, original periodic/self-factor equality, both quantitative cases and no unsupported Mahler inference. |
| dependency | [Dependency](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Same actual P,T,K,F and nonzero quotient values. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-frobenius-two-copy-module) | Monic integer remainders and actual order membership. |
| dependency | [Dependency](Yin_C_G0191_v2.md#argument) | Local Sections1--3 only, exact root multiplicities and unequal distances, beta>=1/5; old original-return formulas are not used. |
| dependency | [Dependency](Yin_C_G0178_v1.md#statement) | e_p>=2 at EVERY prime and G_p=3C_p under the complete residual system. |
| dependency | [Dependency](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Exact accepted unit and original completion/valuation/degree conventions with unchanged ancestor-proof limits. |
| dependency | [Dependency](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Actual complete finite F_p, integral polynomial and unit derivative; no new extension theorem. |
| dependency | [Dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Conditional H_64 with full scalar12log2, constants and integrable circle zeros. |
| support | [Support](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Existing local arithmetic coverage with author-overlap boundary; does not review this candidate. |
| support | [Support](#trace-order-dedekind-kummer-attribution) | Actual retained MIT Lecture 6 Theorem 6.14 and Sut21c-U001 inspection, naming/applicability and fully proved local specialization; prior online history and later acquisition stay distinct. |
| support | [Support](#exact-inputs) | Nine input rows, comparison-versus-dependency roles, author contributions, no computation, actual order and all-degree limits. |
| review | [Review](../audits/reviews/Yin_R_G0480_v1.md#dyadic-trace-order-image-whole-finding) | Entire actual OI1--OI13 and QD1--QD9, all original and f-only domains, exact image kernels and all-prime dimensions, ten-elevenths cases, ceilings, index divisibility and conditional64 scalar; all input/source scopes checked with upstream author roles disclosed and actual independent evidence reused. |

