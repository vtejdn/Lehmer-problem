---
author: Yin
---

# Sparse trinomial auxiliaries and the boundary of nonnegative phase balance

Date: 2026-10-10.
Fixed retention under the coordinating AI for Yin's explicit instruction after the complete noncontributor reviews of D G0041 and D G0042.
The retaining AI reviewed both arguments but authored neither.
All original proofs, contributor disclosures, full review accounts and J36 evidence remain at their actual scopes.
This adoption does not complete G0001 or assert a new Claim decision.

<a id="seed-phase-boundary-fixed-scope"></a>
## Adopted conclusions and unresolved lower-sign question

For coprime 0<b<a, the [trinomial account](#sparse-trinomial-auxiliary) proves an exact sparse and Chebyshev trace form for G_f=((f*)^2 f(t^2)+f^2 f*(t^2))/2, f=t^a-t^b-1.
The seed's complete circle factor is either1 or one Phi_6, with the exact congruences retained below.
The residual is monic reciprocal except at(a,b)=(2,1), whose leading and constant coefficients are2.
The Pisot seed t^3-t^2-1 produces an irreducible reciprocal degree-ten polynomial with three expanding roots and nonreal trace roots, excluding closure within Salem polynomials or the specified block-bipartite Seifert determinants.
This does not exclude arbitrary graph or Seifert realizations.

The exact bounded pilot covers all45 coprime pairs with2<=a<=12.
It gives two Salem rows, both the original Lehmer polynomial;42 multiple-expanding residuals; and the sole nonmonic exception.
Its positive approximate phase balances remain unvalidated discovery, not an accepted sign theorem.
All J36 author and reviewer programs, exact outputs, original failed-attempt corrections and library-dependence disclosures are preserved.

The [separate cubic counterfamily](#negative-doubling-phase-balance) f_A=t^3+A t^2+(1-A)t-1, integer A>=2, consists of primitive irreducible monic units and satisfies Delta_A=log2+m(G_A)-3m(f_A)<=log(170/A).
Thus Delta_A tends to minus infinity.
This disproves nonnegativity over all primitive irreducible monic unit seeds, but its height and measure grow with A.
It does not settle the precise height-one trinomial class or a controlled-small-measure version of that question.
Both accounts retain the complete phase integral and every auxiliary factor/leading coefficient.

The complete original bodies follow.
Their date-specific pending-review and exploration wording records their state when written and is superseded only by this fixed adoption and their full reviews.
Mathematical prose, formulas and review scope are unchanged; only heading depth and relative navigation are relocated.

<a id="sparse-trinomial-auxiliary"></a>
## Sparse doubling residuals of primitive trinomial seeds

Date: 2026-10-10.
Assigned arithmetic AI resultant_research for Yin.
This bounded exploratory round generalizes the [plastic doubling numerator](Yin_L_G0174_v1.md#plastic-lehmer-resultant-reduction) to f=t^a-t^b-1 with 0<b<a and gcd(a,b)=1.
It derives an exact two-variable sparse formula and structural factor/root certificates.
The pilot was restricted to a<=12 with a 120-second execution guard and completed all 45 pairs; the range was not enlarged.
This draft is exploratory responsible mathematics, not a fixed ledger or an independently reviewed result.

### Current question and scope

For f*=t^a f(1/t), define G_f=[(f*)^2 f(t^2)+f^2 f*(t^2)]/2.
The question is to separate actual trinomial structure from unrestricted factor occurrence.
The [general doubling-auxiliary universality theorem](Yin_L_G0174_v1.md#doubling-auxiliary-factor-universality) warns that an unrestricted seed presentation alone is not selective.
This draft gives an exact trace normal form, a seed cyclotomic reduction, a small explicit obstruction to Salem and block-bipartite graph closure, and the finite pilot.
Mahler decimals in the pilot remain unvalidated discovery estimates.

Reuse/provenance: the plastic identity G_(t^3-t-1)=t L was already retained in [L38's odd-order elimination row](Yin_L_G0038_v1.md#family-cyclotomic-factors).
The arithmetic agent rediscovered it in former D38; that draft's initial absence claim was corrected and the full history retained in [L174](Yin_L_G0174_v1.md#retained-plastic-resultant-argument).
The complete resultant and phase-energy deductions there are distinct from the older numerator identity.
This pilot does not claim the plastic identity as new.
The coordinator supplied the general circle upper bound and multiplicative cyclotomic-factor observation used below; the assigned arithmetic agent derived the sparse/trace formulas, exact seed root-of-unity criterion, finite pilot, and explicit graph obstruction.
No historical or external-literature novelty is claimed for these elementary deductions.

### Exact sparse and trace forms

Put u=t^b and v=t^(a-b), so f=uv-u-1 and f*=1-v-uv.
Direct expansion gives

    G(u,v)=u^4 v^3-u^4 v^2+u^3 v^4-2u^3 v^2
             +u^3 v-u^2 v^2+u v^3-2u v^2+u-v^2+v.   (1)

In particular G(1,1)=-1, so none of these auxiliaries is identically zero.
Interchanging b and a-b is not a symmetry; explicitly

    G(u,v)-G(v,u)
       =-(u-v)(uv-1)(u^2 v+u v^2+2uv+u+v).          (2)

There is a useful exact reciprocal trace form.
Define C_j(x) by C_0=2, C_1=x and C_(j+1)=x C_j-C_(j-1), so C_j(t+t^(-1))=t^j+t^(-j).
Then

    G_f(t)/t^(2a)=R_(a,b)(t+t^(-1)),
    R_(a,b)(x)=C_(a+b)(x)+C_(2a-b)(x)-C_(2b)(x)
                       -2C_b(x)+C_(|a-2b|)(x)-1.   (3)

For ell=min(b,a-b), the largest index is h=2a-ell.
Except at the permitted pair (a,b)=(2,1), its coefficient is one and unique; all negative-index terms have smaller degree.
Thus G_f=t^ell W_(a,b), where W is a monic reciprocal integer polynomial of degree 2h=4a-2ell, with constant coefficient one.
At (2,1) both largest positive terms coincide, and the leading/constant coefficient of W is two.
This exception must not be labelled a monic unit residual.
Equation (3) gives an exact finite trace-root discriminator without assuming a Coxeter realization.

### Exact seed cyclotomic reduction

Every unit-circle zero of a coprime trinomial f=t^a-t^b-1 is a primitive sixth root.
Indeed, if |z|=1 and z^a=1+z^b, taking absolute squares gives z^b+z^(-b)=-1.
Therefore z^b is a primitive third root, z^a is a primitive sixth root, and z^(2a-b)=1.
Since gcd(a,2a-b)=1, Bezout together with z^(6a)=1 gives z^6=1; the primitive-sixth order of z^a then forces z itself to have order six.
Conversely a primitive sixth root is a zero exactly when

    a=1 or 5 mod6, and b=2a mod6.                         (4)

Such a root is simple: f'(z)=z^(b-1)[a z^(a-b)-b] is nonzero because a>b>0 and |z|=1.
Thus the complete cyclotomic part of the seed is either 1 or Phi_6, with multiplicity one.
In particular f(1) and f(-1) are nonzero; there are no additional noncyclotomic unit-circle zeros.
This argument is for coprime a,b, not an assertion for arbitrary trinomial exponents.

If f=c g with a monic reciprocal cyclotomic c, reversal at actual degrees gives f*=c g*.
Substitution in the definition proves the exact identity

    G_(c g)(t)=c(t)^2 c(t^2) G_g(t).                      (5)

All three cyclotomic factors on the right have Mahler measure one, with their stated multiplicities.
This is why a duplicate Salem output can appear in a trinomial table without a new noncyclotomic seed.
In fact

    t^5-t^4-1=Phi_6(t)(t^3-t-1),
    G_(5,4)=Phi_6(t)^2 Phi_12(t) t L(t).                  (6)

The equality c(t^2)=Phi_12(t) here is exact.
Equation (5) does not say that every cyclotomic factor of G comes from a cyclotomic factor of f; the pilot has additional Phi_12 and Phi_15 factors.

### A Pisot input already leaves the Salem and block-bipartite classes

The next primitive cubic f=t^3-t^2-1 is irreducible by the rational-root test.
Its discriminant is -31, so it has exactly one real root rho, with 1<rho<2.
Its other two roots are complex conjugates with common modulus rho^(-1/2)<1, since the product of the three roots is one.
Hence it is a genuine Pisot seed, rather than a relaxed angular example.

For this input, (1)-(3) give

    G_(3,2)=t W,
    W=t^10-2t^7+t^6-t^5+t^4-2t^3+1,
    W/t^5=R(t+t^(-1)),
    R=x^5-5x^3-2x^2+6x+3.                              (7)

Here is an explicit exact irreducibility and root-count certificate, independent of the pilot's factorization routine.
Modulo two, q=R mod2=x^5+x^3+1 satisfies x^32=x mod q and gcd(q,x^2-x)=1.
Since five is prime, these two conditions prove q irreducible over F_2, so R is irreducible over Q.
Its rational Sturm chain is

    R,
    5x^4-15x^2-4x+6,
    2x^3+(6/5)x^2-(24/5)x-3,
    (6/5)x^2+(37/10)x-3/2,
    221/24-(937/72)x,
    -1509084/877969.                                    (8)

Successive entries are exactly the negatives of the polynomial remainders.
The sign variations at (-infinity,-2,2,+infinity) are (4,4,2,1); neither endpoint is a zero, since R(-2)=-9 and R(2)=-1.
Thus R has no real root below -2, two roots in (-2,2), one above 2, and two nonreal roots.

For any root x of R the degree-five field Q(x) has a real embedding with x in (-2,2).
At that embedding x^2-4 is negative, and therefore cannot be a square in Q(x).
The quadratic equation t^2-x t+1 is irreducible over Q(x), so W is irreducible of degree ten.
Each of the two inside trace roots gives a pair on the unit circle.
The real trace root above two gives one expanding real root.
Each nonreal trace root gives one expanding and one contracting root, since a unit-modulus root would have real trace and the two quadratic roots multiply to one.
Consequently W has four unit-circle roots and three expanding roots, two of the latter nonreal.
It is a reciprocal monic unit polynomial but is not Salem.

This also yields a precise graph-class obstruction.
Let B be any real p-by-q matrix, and consider a block-bipartite Seifert matrix

    E = [ I_p  -B ; 0  I_q ].

Orthogonal singular-value decomposition of B gives

    det(tE+E^T)
      =(t+1)^|p-q| product_(j=1)^min(p,q)
                       [(t+1)^2-sigma_j(B)^2 t].        (9)

Thus every zero other than -1 has real t+t^(-1)=sigma_j(B)^2-2.
Polynomial W in (7) cannot divide any determinant in (9), because its nonreal trace roots violate this necessary condition.
This includes positive or signed real edge weights with the bipartition block ordering.
No exclusion of arbitrary ordered Coxeter graphs, non-bipartite graphs, or arbitrary Seifert matrices is asserted.
The obstruction is stronger than merely observing a larger Mahler value: even a small Pisot trinomial can leave this explicit graph class under doubling.

### Bounded finite pilot and phase balance

[J36](../computations/programs/Yin_J_G0036/readme.md) retains the complete program, exact coefficient/factor data, rational trace counts, discovery decimals, and a separate structural-certificate program.
The main pilot covered every pair 2<=a<=12, 0<b<a, gcd(a,b)=1: 45 pairs, without a cap stop.
All inputs gave a nonzero G, and every normalized W had exactly one simple noncyclotomic irreducible factor; all those factors were reciprocal.
The exact finite findings are:

| Noncyclotomic residual type | Number of pairs | Interpretation |
| --- | ---: | --- |
| Salem | 2 | (3,1) and (5,4), both the same original Lehmer polynomial by (6) |
| Multiple expanding roots | 42 | Between two and nine expanding roots, certified by exact trace root counts |
| Nonmonic, one expanding root | 1 | (2,1); leading/constant coefficient two, not a monic unit polynomial |

The only cyclotomic factors encountered in G after monomial removal were Phi_6, Phi_12 and Phi_15, with the exact multiplicities retained per row.
This is a finite statement, not a complete cyclotomic classification for arbitrary a,b.
The claim that each row has one simple noncyclotomic factor is likewise finite evidence, not an unrestricted irreducibility theorem.
No new Salem graph family appeared in this pilot; its two Salem rows are the same plastic/Lehmer mechanism.
The other rows are genuine reciprocal unit outputs (except the stated nonmonic exception), not discarded because they lack the Salem shape.

For interpretation, include all factors and leading content in m(G), and set

    Delta(f)=log2+m(G_f)-3m(f).                          (10)

All circle integrals below use normalized Haar measure.
On the unit circle put r=f*/f where defined.
Almost everywhere |r|=1 and

    |2G_f(z)|=|f(z)|^2 |f(z^2)| |r(z)^2+r(z^2)|.

Polynomial logarithms are integrable even at their finitely many circle zeros; G is nonzero by G(1)=-1.
Subtracting their integrals therefore proves the full phase-integral identity

    Delta(f)=integral log|r(z)^2+r(z^2)|,
    m(G_f)<=3m(f),  Delta(f)<=log2.                     (11)

The inequality also follows directly from the triangle inequality |G_f(z)|<=|f(z)|^2|f(z^2)|.
Equations (5) and (10) show Delta(cg)=Delta(g) for cyclotomic c in that formula.
These facts explain why the two Salem rows have equal balance.
They provide no general lower bound on Delta.

Every discovery Delta in the finite pilot was positive, with approximate values between 0.011906 and 0.323027.
These bounds and signs have not been interval-certified and are not mathematical claims.
The plastic value is separately certified in [L174's full energy calculation](Yin_L_G0174_v1.md#complete-plastic-mixed-energy-limit).
No negative candidate appeared to justify a focused negative certificate, and the scan was not enlarged.
In general (10) is the full fixed-seed phase integral; its interpretation as a limit of actual Salem-family mixed energies requires the separate family and nonvanishing arguments present for the plastic seed.
It is not inherited for every trinomial automatically, and none of these fixed seeds has m tending to zero.

### What this round discriminates

The output is a sparse Chebyshev family with an exact seed reduction, not a newly discovered list of small Salem measures.
The explicit cubic example disproves closure of Pisot-trinomial doubling outputs within Salem polynomials or within the block-bipartite determinant class (9).
This identifies a concrete limitation of seeking only the familiar Salem graph structure in these residuals.
The one-factor pattern and positive phase balances remain possible conjectural directions, with exact finite evidence and no general assertion.

A useful next test would be a proof or a counterexample for the lower sign of the complete phase integral (11) under this precise trinomial constraint, or a theorem controlling the noncyclotomic trace factor in (3) after removing the seed factor (4).
Either would constrain an actual complete polynomial and its factor costs.
A larger minimum-value table alone would not resolve either issue, so this bounded round stops with the present exact obstruction and formulas.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0074_v1.md#trinomial-auxiliary-independent-review), with its original inspected scope and relationship.



<a id="retained-negative-phase-control"></a>
## A cubic integral-unit control with arbitrarily negative doubling phase balance

Date: 2026-10-10.
The coordinating AI for Yin developed this bounded control after the primitive-trinomial pilot in [D41](#sparse-trinomial-auxiliary) reported only positive numerical phase balances.
This changes the seed class to primitive irreducible monic cubic units with growing coefficients.
It tests a possible sign assumption, not a near-one family or the height-one trinomial subclass.
No computation or new external source is needed.

<a id="negative-doubling-phase-balance"></a>
### Statement and exact seed geometry

For an integer A>=2, put

    f_A(t)=t^3+A t^2+(1-A)t-1,
    f_A*(t)=t^3 f_A(1/t),
    G_A=[(f_A*)^2 f_A(t^2)+f_A^2 f_A*(t^2)]/2.

The polynomial G_A is a nonzero integer polynomial by the Frobenius parity identity and the direct value G_A(1)=1.
The seed is monic with constant coefficient -1 and is irreducible: its only possible rational roots are +/-1, whereas f_A(1)=1 and f_A(-1)=2A-3 are nonzero.
It is consequently a primitive irreducible algebraic-unit input of fixed degree three.

All its roots are real, with one in each of

    (-A-1,-A),       (-1,0),       (0,1).

Indeed f_A(-A-1)=-2A-3<0, f_A(-A)=A^2-A-1>0, f_A(-1)=2A-3>0, f_A(0)=-1 and f_A(1)=1.
The three disjoint sign changes already account for its entire degree.
Thus exactly one root lies outside the unit circle; if its modulus is tau_A then

    A<tau_A<A+1,          m(f_A)=log(tau_A)>log A.       (1)

This is a negative exterior root.
Neither it nor the resulting auxiliary is declared to be a positive near-one Salem input.

Let m denote the usual logarithmic Mahler measure, including the leading coefficient for a nonmonic polynomial, and define the exact total phase balance

    Delta_A=log2+m(G_A)-3m(f_A).

Then

    Delta_A<=log(170/A).                               (2)

In particular Delta_A<0 for every integer A>=171, and Delta_A tends to minus infinity in the sense that it is eventually below every fixed real number.
This disproves a nonnegative phase-balance assertion over all primitive irreducible monic unit seeds.
It says nothing against such a statement on a genuinely smaller specified seed class.

### Direct quadratic-size bound for the numerator

The key is the exact relation

    f_A+f_A*=u,             u(t)=t+t^2,

whose right side is independent of A.
Write f=f_A, f_2=f_A(t^2), u_2=u(t^2).
The numerator of G_A becomes

    (f*)^2 f_2+f^2 f*(t^2)
       =(-f+u)^2 f_2+f^2(-f_2+u_2)
       =-2f u f_2+u^2 f_2+f^2 u_2.                   (3)

The order-A^3 part has cancelled exactly.
On the unit circle,

    |u|<=2, |u_2|<=2,
    |f|,|f_2|<=3+2A<=5A.

With F=3+2A, equation(3) gives

    |G_A|<=3F^2+2F<=85A^2,             A>=1.

Jensen's integral definition of Mahler measure therefore yields

    m(G_A)<=log(85A^2).                               (4)

Combine (4) with (1) to obtain Delta_A<log2+log85+2log A-3log A=log(170/A).
The weaker non-strict version in(2) is retained for convenience.
The upper bound tending to minus infinity is sufficient for the stated divergence; no root approximation for G_A is needed.

### Why this is the actual full circle-phase balance

The general direct identity also clarifies the scope of this control.
For any nonzero integer f for which G_f is nonzero, and away from its finitely many circle zeros, let r(z)=f*(z)/f(z).
Then |r(z)|=1 on the circle and

    G_f(z)=[f(z)^2 f(z^2)/2] [r(z)^2+r(z^2)].

All logarithmic singularities are integrable because the rational expression is nonzero.
Integrating and using that z->z^2 preserves normalized Haar measure gives

    log2+m(G_f)-3m(f)
       = integral_(|z|=1) log|r(z)^2+r(z^2)| dmu(z).    (5)

In particular this is a full circle integral; selecting positive Fourier modes would not determine its sign.
The same identity and |r(z)^2+r(z^2)|<=2 give the general upper bound m(G_f)<=3m(f), consistently with (4).
The root-free unit circle for f_A has already been proved by its real-root intervals, although the integrable identity does not need that stronger condition.

For the plastic seed, the retained [complete arithmetic analysis](Yin_L_G0174_v1.md#complete-plastic-mixed-energy-limit) identifies its positive balance with the complete normalized mixed energy of a specific delayed Salem family.
No corresponding family-limit theorem is being assumed for f_A here.
Equation(5) is the directly defined total phase balance itself.
Its negative sign does not refute the existing positive plastic-family result, nor supply a near-one counterexample: m(f_A)>log A grows without bound.
The auxiliaries G_A need not be irreducible or have only one expanding pair, and all their factors and leading coefficients remain in (2)--(5).

### Contribution and review boundary

The coordinator supplied the cubic family, exact three-root geometry, A-independent sum with its reversal, quadratic numerator bound and complete integral interpretation.
The arithmetic agent's finite positive trinomial controls motivated the changed hypothesis; those controls are not premises of this proof.
The whole written argument is self-checked and ready for independent noncontributor review.
It uses elementary polynomial arithmetic and the standard Mahler integral convention already fixed in G0001.
No finite computation, unknown convergence rate or uninspected source theorem is used.
G0001 remains active and unresolved.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0074_v1.md#negative-phase-balance-independent-review), with its original inspected scope and relationship.



<a id="seed-phase-retention-map"></a>
## Retention and review map

| Completed draft | Fixed home and complete review |
| --- | --- |
| D G0041 | [Entire trinomial proof and finite evidence](#sparse-trinomial-auxiliary), [complete noncontributor finding](../audits/reviews/Yin_R_G0074_v1.md#trinomial-auxiliary-independent-review) |
| D G0042 | [Entire negative cubic control](#retained-negative-phase-control), [statement and geometry](#negative-doubling-phase-balance), [complete noncontributor finding](../audits/reviews/Yin_R_G0074_v1.md#negative-phase-balance-independent-review) |

The arithmetic agent authored D41's sparse/trace algebra, complete seed-circle classification, Pisot/graph obstruction and original finite pilot.
The coordinator supplied only the general Mahler inequality and cyclotomic multiplicativity identified in that account.
The coordinator alone authored D42's cubic counterfamily and complete proof.
The orbit_research reviewer supplied none of those mathematical arguments and recorded both full independent findings.
Its separately authored exact J36 retained-data checker shares SymPy's underlying exact arithmetic; no independent algebra-system implementation is claimed.
The finite pilot's unvalidated Delta decimals remain so after adoption.

Actual consumers were migrated and no remaining incoming retired-path references were found.
Its author/reviewer evidence and recorded failed runs remain preserved.
Only D41 and D42 were retired; later sign investigations receive separate responsible drafts.
No new mathematical run or external source-proof audit was performed by retention.
