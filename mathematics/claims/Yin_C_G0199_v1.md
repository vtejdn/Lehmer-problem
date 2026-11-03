---
author: Yin
---
# An odd-order obstruction to zero Haar for actual canonical residuals

Date: 2026-10-20T15:10.
Human author Yin.
Root proposed the all-degree cyclotomic-order exclusion and the exact finite-field trace-orbit characterization.
The draft_inventory_later agent completed the author verification and assembled the full source-backed proof below.
Both are mathematical contributors, and this candidate has no independent review of its new application yet.
This is a distinct zero-Haar cyclotomic-order question, not a revision of C196's canonical-degree or all-representative questions.
The original author account at 2026-10-20T15:06 is preserved in the complete argument.
No new computation, parameter enumeration, source acquisition or original-input realization is used.

<a id="statement"></a>
## Exact theorem statement

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient 1 and degree d=2r.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), and assume F=Q(delta) is totally real.
Let T in Z[X] be the actual monic degree-r minimal polynomial of delta, so P(z)=z^r T(z+z^(-1)) and [K:F]=2.
Define C_p(z+z^(-1))=z^p+z^(-p) and use the ACTUAL integer quotient polynomials

    theta_p=rem_T(T(C_p(X)))/p in Z[X], p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.

The actual quotient values a,b,c are nonzero algebraic integers in this same F.
For either s in {1,-1}, assume the complete original residual equations

    f=0, e+s g=0, g!=0.

Put

    G=rem_T(theta_5^3-2theta_3^5), w=deg G<r,
    I_can=integral_T log G(z+z^(-1))^2 dmu,
    U=T mod 2, R=G mod 2,
    chi=C5 mod 2=X^5+X^3+X.

Here mu is normalized Haar probability and the finitely many circle zeros have the usual integrable-logarithm interpretation.

**A. Necessary order obstruction at zero Haar.**
If I_can=0, then w>=1 and G has leading coefficient epsilon in {1,-1}.
Its monic reciprocal pullback has the finite product factorization

    H(z)=epsilon z^w G(z+z^(-1))
        =product_m Phi_m(z)^(a_m), a_m>=0,
    sum_m a_m phi(m)=2w<d.

Here Phi_m is the m-th cyclotomic polynomial and phi is Euler's totient.
The original multiplicities are retained; in particular a_1 and a_2 are even.
There must be at least one m with a_m>0 whose odd part n=m/2^(v_2(m)) satisfies

    5 not congruent to +2^j or -2^j modulo n
                                  for every j>=0.

The conclusion holds at every original Mahler measure and without upper bounds on r,w,m,n or their multiplicities.
Equivalently, zero Haar is impossible if every occurring order has odd part n with 5 congruent to +/-2^j modulo n for some j>=0, allowed to depend on n.
For n=1 the congruence is automatic; if 5 divides n it is impossible.

**B. Exact finite-field mechanism.**
For any x in an algebraic closure of F_2 and any nonzero z satisfying z+z^(-1)=x, let n be the exact order of z.
This order is odd, and

    chi(x) lies in the Frobenius orbit of x
      iff 5 congruent to +/-2^j modulo n for some j>=0.

The criterion includes x=0,n=1 and is unchanged by replacing z by its inverse or x by a Frobenius conjugate.
For m=2^a n with n odd, reduction of Phi_m has precisely the roots of exact order n, with the full polynomial identity

    Phi_m mod 2=(Phi_n mod 2),             a=0,
    Phi_m mod 2=(Phi_n mod 2)^(2^(a-1)),  a>=1.

Under the hypotheses of part A, every irreducible factor psi of U divides R.
If every such psi is a self-target under chi, then U divides U(chi) with all original factor exponents, and the actual identity R=rem_U(U(chi)^3) forces R=0.
For zero Haar, monicity up to sign gives R!=0 and deg R=w, so this is impossible.
A permutation of several distinct factors is not a self-target condition.

**C. Unchanged original expense.**
In the zero-Haar situation all resultants are nonzero and

    sum_m a_m log|Res(P,Phi_m)|
       =2log|Norm_F(g)| >=(6d/11)log 2,
    sum_m a_m phi(m)=2w<d.

This uses the actual P, actual canonical G and every original conjugate and factor multiplicity.
It identifies neither 2w with d nor phi(m) with m.
The order obstruction asserts no existence for the remaining orders, no exclusion of the positive-Haar reciprocal noncyclotomic branch, and no unrestricted paid transfer or Mahler gap.

<a id="argument"></a>
## Complete author proof

<a id="zero-haar-cyclotomic-order-obstruction"></a>
## The all-degree cyclotomic-order obstruction to zero canonical Haar

Date: 2026-10-20T15:06.
Human author Yin.
Root proposed the all-order exclusion and the exact finite-field trace-orbit criterion below.
The draft_inventory_later agent checked the complete reduction, both directions of the criterion, the original canonical support and multiplicity implications, and wrote this author account.
Both are contributors; this new application has not received an independent review.
No computation, parameter enumeration, new source acquisition or new original-input construction is used.

The responsible question is whether the actual canonical residual can have zero Haar logarithm, with its complete cyclotomic factorization and original weighted resultant expense retained.
The already fixed [C196v3 graph proof](Yin_C_G0196_v3.md#canonical-c5-residue-graph) supplies the exact remainder identity, every original residue-cluster support and the saturation of a self-target orbit.
It does not already state the cyclotomic-order characterization proved here.
For the classical cyclotomic step, [L79's exact CRT-defect argument](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) already gives the complete reduction of Phi_(p^a n) and the exact orders of its roots when p does not divide n.
[Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) owns the inspected definition, integrality and divisor-factorization source interface, with its original inspection limits.
The elementary reduction is reused from L79, not newly attributed to Bel17's characteristic-zero separability statements.
The measure-zero characterization is the product-with-multiplicities convention in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001).
No assertion of new classical cyclotomic or finite-field theory is made.

### Exact actual input and conclusion

Use the complete actual trace domain and full residual equations of [C196v3's statement](Yin_C_G0196_v3.md#statement).
Explicitly, P in Z[z] is monic irreducible reciprocal nontorsion with constant coefficient 1 and degree d=2r; alpha is a root, delta=alpha+alpha^(-1), K=Q(alpha), and F=Q(delta) is totally real.
Its actual monic degree-r trace polynomial is T, with P(z)=z^r T(z+z^(-1)) and [K:F]=2.
For p=2,3,5 put

    theta_p=rem_T(T(C_p(X)))/p in Z[X],
    a=theta_2(delta), b=theta_3(delta),
    c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5,
    f=e+s g=0, g!=0, s in {1,-1}.               (KC1)

Here C_p(z+z^(-1))=z^p+z^(-p), and a,b,c are the actual nonzero integral quotient values for this same T.
Define

    G=rem_T(theta_5^3-2theta_3^5), w=deg G<r,
    I_can=integral_T log G(z+z^(-1))^2 dmu,
    U=T mod 2, R=G mod 2,
    chi=C5 mod 2=X^5+X^3+X.                      (KC2)

The measure mu is normalized Haar probability and the finite circle zeros use the integrable logarithm convention.
The conclusion is that I_can=0 requires at least one cyclotomic factor Phi_m in the monic reciprocal pullback of G whose odd part n=m/2^(v_2(m)) satisfies

    5 is not congruent to +2^j or -2^j modulo n
                         for every integer j>=0. (KC3)

There is no upper bound on w, r, m, n or their multiplicities in this implication.
It is a necessary obstruction, not an assertion that such an actual residual G exists or that an order satisfying (KC3) supplies one.

### The exact odd-order trace criterion

Let x belong to an algebraic closure of F_2 and choose z with z+z^(-1)=x.
Such z exists by the monic equation z^2+xz+1=0, and its constant coefficient makes z nonzero.
It belongs to the multiplicative group of some finite extension of F_2, so its exact order n is odd.
The other choice of z is z^(-1); when x=0 they coincide at z=1 and n=1.
For every j>=0 the characteristic-two Chebyshev and Frobenius identities give

    chi(x)=z^5+z^(-5),
    x^(2^j)=z^(2^j)+z^(-2^j).                    (KC4)

For nonzero u,v in any field, equality u+u^(-1)=v+v^(-1) holds exactly when u=v or u=v^(-1).
Indeed u is then a root of Y^2-(v+v^(-1))Y+1=(Y-v)(Y-v^(-1)); this argument also covers a repeated root in characteristic two.
Apply this with u=z^5 and v=z^(2^j).
It proves

    chi(x) belongs to the Frobenius orbit of x
      iff 5 congruent +/-2^j modulo n
                            for some j>=0.       (KC5)

The Frobenius orbit is exactly the root set of the irreducible polynomial of x over F_2.
The criterion is independent of the chosen root x of that irreducible polynomial: replacing x by x^(2^k) replaces z by z^(2^k) or its inverse and preserves its odd exact order.
For n=1 the congruence is automatic and chi(0)=0.
If 5 divides n, the congruence is impossible since 2^j is a unit modulo n whereas 5 is not.
No identification of the generator's irreducible degree with a full local residue-field degree is used.

### Cyclotomic reduction identifies the relevant orders

For m=2^a n with n odd, the exact reduction already proved in L79 specializes to

    Phi_m(Z) mod 2 =
       Phi_n(Z) mod 2,                  if a=0,
       (Phi_n(Z) mod 2)^(2^(a-1)),      if a>=1.  (KC6)

For clarity, the second equality is the reduction of
Phi_(2^a n)(Z) Phi_n(Z^(2^(a-1)))=Phi_n(Z^(2^a)).
Frobenius gives the two powers of Phi_n modulo 2, and cancellation is in the polynomial domain F_2[Z].
This includes n=1 and a=1, so no exception for Phi_1, Phi_2 or higher powers of 2 is omitted.
Because n is odd, Z^n-1 has no repeated roots in characteristic two.
Its divisor factorization, or equivalently L79's exact-order proof, shows that the roots of Phi_n mod 2 are precisely the distinct elements of exact order n.
Consequently every geometric root of Phi_m mod 2 has exact order n; the exponent in (KC6) retains all repetitions.

Now suppose I_can=0.
Scalar Jensen and Kronecker, with the full scalar factor, imply that the leading coefficient of G is a sign epsilon in {1,-1} and that

    H(Z)=epsilon Z^w G(Z+Z^(-1))
        =product_m Phi_m(Z)^(a_m),
    a_m>=0, sum_m a_m phi(m)=2w<d.               (KC7)

Only finitely many a_m are nonzero.
The constant coefficient of H is 1, so there is no monomial factor.
If w=0, then G=+1 or -1 and R=1, contradicting the C196v3 assertion that every irreducible factor of the positive-degree U divides R.
Thus the possible zero-Haar case has w>=1 and a nonempty factor product.
The multiplicities of Phi_1 and Phi_2 in H are even because the trace pullback has double contact at Z=1 and Z=-1, respectively; (KC6) itself does not need this additional restriction.
Monicity up to sign implies R!=0 and deg R=w, so there is no degree drop here.

### Original support and full multiplicities force the contradiction

Assume, for contradiction, that every m with a_m>0 fails (KC3), so its odd part satisfies the congruence in (KC5).
Let psi be any irreducible factor of U and let x be one of its roots.
The actual per-cluster consequence (CG4) of C196v3 gives psi|R, hence R(x)=0.
Choose z with z+z^(-1)=x as above.
Reducing the pullback identity in (KC7) gives

    H mod 2=Z^w R(Z+Z^(-1)),

so z is a root of H mod 2 and therefore a root of Phi_m mod 2 for some occurring m.
By (KC6) its exact odd order is the odd part n of that m.
The assumed congruence and (KC5) show that chi(x) is a root of the same psi.
This works for every psi|U, not merely for one cluster carrying some positive part of the original norm.

Write U=product_psi psi^(N_psi), retaining all original exponents.
Since psi(chi(x))=0, the irreducibility of psi gives psi|psi(chi).
The factor psi(chi)^(N_psi) in U(chi) then gives

    ord_psi U(chi)>=N_psi for every psi|U,
    U divides U(chi), hence U divides U(chi)^3.  (KC8)

Possible ramification of chi or collisions with other factors only increase this divisibility.
It does not require U to be squarefree.
But the exact original remainder identity (CG3) in C196v3 is R=rem_U(U(chi)^3).
Equation (KC8) therefore forces R=0, contradicting the nonzero monic reduction from (KC7).
This proves (KC3).
Equivalently, C196v3 guarantees an unsaturated orbit for every nonzero R of degree less than deg U, and (KC5) says that its associated odd order cannot satisfy the stated congruence.
The contradiction concerns self-target orbits, not arbitrary permutations or longer cycles of the full chi-stable root set.

### What this closes and what it leaves

This is an all-degree exclusion for the specified class of occurring cyclotomic orders.
In particular, arbitrary powers of 2 in the orders do not evade it when every odd part satisfies the same congruence criterion.
It does not eliminate an order failing that criterion, bound the number or sizes of such orders, or settle the positive-Haar reciprocal noncyclotomic branch.
No finite table of orders or additional numerical cutoff is substituted for the universal quantifier in (KC3).

All original K11 expenses and multiplicities remain:

    sum_m a_m phi(m)=2w<d,
    sum_m a_m log|Res(P,Phi_m)|
       =2log|Norm_F(g)| >=(6d/11)log 2.          (KC9)

Indeed H(alpha)=epsilon alpha^w g, Norm_K(alpha)=1 and [K:F]=2, so the absolute full resultant is |Norm_F(g)|^2.
Every resultant factor is nonzero because P is irreducible nontorsion.
The last inequality is the original full-residual income supplied by [C191v2's all-cluster theorem](Yin_C_G0191_v2.md#statement) at its adopted scope; it is not strengthened by the order test.
The degree of H is 2w, not the field degree d, and phi(m) has not been replaced by m.
Thus the next unresolved zero-Haar object is the same original weighted cyclotomic resultant expression with at least one order satisfying (KC3), subject to the full divided self-composition equations.
No uniform Mahler gap, useful paid transfer or actual realization follows from this necessary order obstruction alone.

The new argument uses C196v3's already adopted graph/remainder theorem with its [whole independent R474 finding](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding), and reuses L79, Bel17-U001 and Smy08-U001 at the precise scopes stated above.
The draft_inventory_later agent's earlier review of C196v3 does not independently review this new root-proposed application, and its C191 original-return authorship is not presented as an independent recheck of the reused arithmetic income.
This completes the bounded order test at author-check scope; whole independent review of the new application remains required.

<a id="exact-inputs"></a>
## Exact inputs and contribution boundaries

| Input | Exact role |
| --- | --- |
| [C196v3](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | Same original trace domain and full residual equations; CG3 exact canonical remainder, CG4 every-cluster support and CG5 full multiplicities/self-target saturation. The finite cutoff and mod4 equality-shape exclusion are not new premises for this application. |
| [C191v2](Yin_C_G0191_v2.md#statement) | Full original residual norm income abs(Norm_F(g))>=2^(6r/11), with every original local weight; used only to retain the exact weighted-resultant inequality in KC9. |
| [L79](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) | Complete existing cyclotomic reduction and exact prime-to-characteristic root orders, specialized to p=2 with n=1 and all multiplicities retained. Its later module/entropy deductions are not used. |
| [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Inspected classical cyclotomic definition, integrality and divisor factorization; no new proof audit or inference of separability in bad characteristic. |
| [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Scalar Jensen, integrable circle zeros and the precise product-with-multiplicities Kronecker characterization. |
| [R474](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Already completed independent coverage of C196v3; it is not a review of this new application. |
| [R468](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Existing whole independent coverage of the reused C191 original norm interface and its actual authorship boundary. |

The draft_inventory_later agent independently reviewed the new C196v3 graph/lift proof in R474 but is a contributor to the present order application.
It also contributed to older C191 original-return formulas; its reused arithmetic norm income is supported by the actual independent R468, not presented as an independent self-review here.
Root contributed to the upstream graph route and the present theorem.
The current theorem's source reduction, trace criterion, support identification and complete contradiction are preserved in KC1--KC9 above.
No mutable draft, unfinished later C196 version or native computation is a logical premise.
The classical source units retain their actual historical inspection limits.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T15:10 |
| status | open |
| reason | Register the complete all-degree zero-Haar cyclotomic-order obstruction and exact finite-field iff with original residual hypotheses, multiplicities, unchanged weighted resultants and source/review boundaries. Both authors contributed; the new application requires whole noncontributor review before adoption. No realization, positive-Haar exclusion or unrestricted transfer is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact order theorem](#statement) | Zero-Haar necessary bad odd order, both-sign original domain, exact finite-field iff and all-characteristic-two reductions, constant/power-of-two cases, no degree drop and complete weighted-resultant expense. |
| argument | [Complete KC proof](#argument) | All KC1--KC9, full support-to-order identification, factorwise multiplicities, self-target contradiction and all remaining boundaries. |
| dependency | [Actual canonical graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | CG3--CG5 at the complete original trace/residual domain; every cluster support and full exponent saturation, no later candidate version. |
| dependency | [Original residual income](Yin_C_G0191_v2.md#statement) | The full Norm_F(g) floor with every original local degree, used in the unchanged KC9 comparison. |
| dependency | [Exact cyclotomic reduction](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) | Phi_(2^a n) mod2, exact odd-order roots, n=1 and all original multiplicities; not later module/entropy statements. |
| dependency | [Classical cyclotomic source](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Definition, integrality and divisor factorization at the retained inspected scope; no enlarged bad-characteristic or book-proof audit. |
| dependency | [Scalar Jensen and Kronecker](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact normalized Haar, leading sign and product with multiplicities, no monomial factor for constant1 and integrable circle zeros. |
| support | [Independent graph review](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Actual accepted upstream graph coverage; the reviewer of that input is an author here and does not review this new deduction. |
| support | [Independent C191 review](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Existing original norm coverage with the disclosed prior original-return contribution, not a new C191 audit. |
| support | [Complete input and role account](#exact-inputs) | Seven explicit input/support rows, both authors, fixed source scopes, no mutable proof dependency and no new computation. |

### Decision whole-reviewed-2026-10-20

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T15:21 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft zero-Haar and original-transfer inquiry. |
| reason | Adopt the complete KC1--KC9 odd-order obstruction through actual whole independent consumer R481. Zero canonical Haar requires an occurring odd part n with 5 not congruent to either sign of any power of2 modulo n. Every original degree, cyclotomic multiplicity, finite-field equivalence, norm phase and weighted resultant expense is retained. This excludes only the stated all-good-order class; it proves neither remaining realization nor positive-Haar exclusion or unrestricted transfer. The later joint C3/C5 author extension is not adopted here. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact order theorem](#statement) | Zero-Haar necessary bad odd order, both-sign original domain, exact finite-field iff and all-characteristic-two reductions, constant/power-of-two cases, no degree drop and complete weighted-resultant expense. |
| argument | [Complete KC proof](#argument) | All KC1--KC9, full support-to-order identification, factorwise multiplicities, self-target contradiction and all remaining boundaries. |
| dependency | [Actual canonical graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | CG3--CG5 at the complete original trace/residual domain; every cluster support and full exponent saturation, no later candidate version. |
| dependency | [Original residual income](Yin_C_G0191_v2.md#statement) | The full Norm_F(g) floor with every original local degree, used in the unchanged KC9 comparison. |
| dependency | [Exact cyclotomic reduction](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) | Phi_(2^a n) mod2, exact odd-order roots, n=1 and all original multiplicities; not later module/entropy statements. |
| dependency | [Classical cyclotomic source](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Definition, integrality and divisor factorization at the retained inspected scope; no enlarged bad-characteristic or book-proof audit. |
| dependency | [Scalar Jensen and Kronecker](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact normalized Haar, leading sign and product with multiplicities, no monomial factor for constant1 and integrable circle zeros. |
| support | [Independent graph review](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Actual accepted upstream graph coverage; the reviewer of that input is an author here and does not review this new deduction. |
| support | [Independent C191 review](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Existing original norm coverage with the disclosed prior original-return contribution, not a new C191 audit. |
| support | [Complete input and role account](#exact-inputs) | Seven explicit input/support rows, both authors, fixed source scopes, no mutable proof dependency and no new computation. |
| review | [Whole independent odd-order consumer finding](../audits/reviews/Yin_R_G0481_v1.md#zero-haar-odd-order-consumer-whole-finding) | Entire actual KC1--KC9, complete statement, both directions of the trace-orbit criterion, every reduction/multiplicity and original expense, all five dependencies and three supports, with upstream author roles disclosed and actual independent graph evidence reused. |

