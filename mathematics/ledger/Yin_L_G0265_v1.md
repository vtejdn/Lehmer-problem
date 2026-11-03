---
author: Yin
---

# Exact trace-unit orbit reduction and complete quartic auxiliary costs

The complete current mathematical home is [C464](../claims/Yin_C_G0464_v1.md#statement), adopted after the [R671 whole SELF finding](../audits/reviews/Yin_R_G0671_v1.md#trace-unit-orbit-whole-self-finding).
The [original R124](../audits/reviews/Yin_R_G0124_v1.md#trace-unit-orbit-complete-independent-review) remains UNKNOWN on its entire original proof, source, control and clarification scope because the actual initial target context is not established.
The complete historical exploration, author contribution, source occurrences, fixed inputs and dated review below remain retained; this maintenance selects no Task or execution.

Date: 2026-10-10.
The coordinating AI for Yin adopts this restricted result after complete separately organized noncontributor review under the continuing G0001 authorization.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="trace-unit-orbit-fixed-scope"></a>
## Current adopted scope

For the actual irreducible quartics P_a=t^4-at^3+t^2-at+1, a>=2, the entire unit group of the actual quadratic trace order is proved directly.
Every exhibited unit power preserves primitive content, the full original resultant and each labeled nonarchimedean depth.
The exact orbit-minimum coefficient energy has a discrete hyperbolic-cosine formula; the order automorphism gives no additional minimum.
An infinite actual even-parameter family has an unbounded ratio between its discrete and continuous orbit minima, and its entire-orbit auxiliary Mahler minimum is also computed with all exterior roots charged.
Its original degree is four and measure grows, so it is a cost control, not a near-one family.
Complete author proof, scope clarification and full noncontributor review are retained.

The complete D132 author proof and review follow without abridgment.
Historical pending-review or pending-adoption sentences are superseded only by this current adoption paragraph.
Heading depths and relative navigation are relocated; all statements, proofs, source boundaries, unsuccessful-test scope and review history are preserved.
G0001 remains active and unresolved.

<a id="complete-retained-proof-and-review"></a>
## Complete retained author proof and independent review

## Exact trace-unit orbit reduction and its discrete cost on actual quartics

<a id="trace-unit-orbit-reuse"></a>
### 1. Changed question, existing inputs and source scope

Date:2026-10-10.
Authored by resultant_research AI for Yin.
Root supplied the broad question and coordination, not any proof step below.
The unfinished D133--D135 arguments are not premises.
This is an authored proof draft, not an independently reviewed or fixed result.

[L261](Yin_L_G0261_v1.md#trace-symmetry-fixed-scope) supplies the exact actual-trace-order norm/content/depth invariance and the formal-degree-four norm/energy formulas.
[L257](Yin_L_G0257_v1.md#adjacent-edge-trace-factor-cost) supplies their full original-root and primitive normalization meaning.
These are reused.
A bounded G-ledger and registry search by trace-order unit, unit orbit, quadratic norm, Pell and fundamental unit located [L31's older qualitative obstruction](Yin_L_G0031_v1.md#relative-unit-orbit): a full principal ideal and all finite valuations can stay fixed along an unbounded actual unit direction.
That qualitative fact is NOT a new result here.
The changed test is to compute the exact minimum of the complete auxiliary coefficient energy over an entire actual trace-order unit orbit, rather than selecting one improving unit or presenting another unbounded orbit without its optimization.

The real-quadratic-order unit-group language is classical.
A bounded primary-source check located Keith Conrad, [*Dirichlet's Unit Theorem* (Con26)](../literature/pdf/Con26.pdf), the official undated27-page author PDF, Section4, printed pp.7--8.
The exact order statement and least-positive-unit discussion were read online and then directly in the acquired local PDF on p.8.
Con26's inspection-year address does not supply an unknown publication date.
This source is attribution for the classical framework only.
The specific order's entire unit group is proved directly below by an integer-coordinate inequality and a logarithmic floor.
No general Dirichlet theorem, maximal-order substitution, continued-fraction algorithm or regulator estimate is imported.
Canonical source intake was completed; no whole-source proof inspection is claimed.
No new program or numerical enumeration is used.

The infinitely many actual input polynomials below have degree four and growing total measure.
They are not a hypothetical near-one sequence or an unbounded-degree coverage theorem.
All conclusions use anti-reciprocity at FORMAL degree four, with actual degree drops explicitly allowed.

<a id="actual-quartic-trace-unit-family"></a>
### 2. An actual irreducible family and its complete trace-order unit group

Fix an integer a>=2 and put

    Q_a(x)=x^2-a x-1,
    P_a(t)=t^4-a t^3+t^2-a t+1=t^2 Q_a(t+t^(-1)),
    D=a^2+4, lambda=(a+sqrt(D))/2>2,
    lambda'=a-lambda=-lambda^(-1).                  (1)

The discriminant D lies strictly between a^2 and(a+1)^2 for a>=2, so Q_a is irreducible.
The field K=Q(lambda) is real quadratic.
The element lambda^2-4 is positive at its displayed embedding but negative at the conjugate embedding, since |lambda'|<1.
It cannot be a square in K.
Therefore a root beta>1 of t^2-lambda t+1 has degree two over K and degree four over Q.
Its displayed polynomial P_a is its actual minimal polynomial.
Its roots are beta,beta^(-1) and the two conjugate unit-circle roots with trace lambda'.
This proves actual irreducibility, reciprocal unit structure and nontorsion, without assuming that the trace order is maximal.
Its full original logarithmic Mahler measure is

    m(P_a)=log beta,
    beta=(lambda+sqrt(lambda^2-4))/2,
    beta/a ->1 and m(P_a)=log a+o(1) as a->infinity. (2)

The last limit follows from lambda/a->1 and beta/lambda->1.
Degree remains four; small normalized height is not being substituted for small total measure.

Let tau denote lambda as an element of the ACTUAL order O_a=Z[tau].
Since tau^2=a tau+1, tau is a unit with inverse tau-a.
In fact

    O_a^times={+/-tau^k:k in Z}.                     (3)

Here is a complete proof for this order.
Any unit epsilon has field norm+/-1, since its norm and the norm of its integral inverse are rational integers with product1.
If its displayed real value y lies in(1,lambda), its conjugate is either y^(-1) or-y^(-1).
Writing epsilon=u tau+v in the integral order basis gives

    0<u=(y-epsilon')/sqrt(D)
       <=(y+y^(-1))/sqrt(D)<1.

The last strict inequality uses that y+y^(-1) is strictly increasing for y>1 and lambda+lambda^(-1)=sqrt(D).
This contradicts u being an integer.
Thus no positive unit lies strictly between1 and lambda.
For any positive unit epsilon choose k=floor(log(epsilon)/log(lambda)); then epsilon tau^(-k) is a unit in[1,lambda), hence equals1.
A negative unit is reduced to the positive case by its sign.
This proves(3), including inverse powers, by direct algebra rather than an unproved fundamental-unit assertion.

<a id="exact-entire-trace-unit-orbit-energy"></a>
### 3. Exact minimization of every actual trace-unit orbit

Let z=u tau+v be nonzero with u,v in Z and gcd(u,v)=1.
Its nonzero trace norm is

    n=Norm_(K/Q)(z)=-u^2+a u v+v^2.                 (4)

Irreducibility of Q_a excludes n=0.
For every k in Z write tau^k z=u_k tau+v_k.
Multiplication and its inverse have the explicit matrices

    T=[[a,1],[1,0]],     T^(-1)=[[0,1],[1,-a]],
    (u_k,v_k)^T=T^k(u,v)^T.                         (5)

All pairs are integral and primitive.
With V_k(x)=u_k x+v_k, retain the actual auxiliary

    C_k(t)=t(t^2-1)V_k(t+t^(-1))
          =(t^2-1)(u_k t^2+v_k t+u_k),
    E_k=S_2(C_k)^2=2(u_k^2+v_k^2),
    Res(P_a,C_k)=(9-4a^2)n^2.                      (6)

The trace norm itself is(-1)^k n; its square in the complete original resultant is unchanged.
Every C_k is nonzero and avoids all four original roots.
The content remains one; the degree is four when u_k!=0 and three with a monomial factor when u_k=0.
In either case it is anti-reciprocal at formal degree four.
Every original rootwise p-adic depth is identical to that of C_0, by L261's actual-order-unit argument.
Equation(6) keeps the full time-two factor9-4a^2 and the entire trace norm, not only a selected prime.

Because T is real symmetric, the unit vectors

    e_+=(lambda,1)/sqrt(lambda^2+1),
    e_-=(1,-lambda)/sqrt(lambda^2+1)

are orthonormal eigenvectors, with eigenvalues lambda and-lambda^(-1).
Define the positive numbers

    A=(lambda u+v)^2/(lambda^2+1),
    B=(u-lambda v)^2/(lambda^2+1),
    x=log(B/A)/(4log lambda),
    delta=dist(x,Z),       0<=delta<=1/2.            (7)

A and B are positive because a nonzero integral vector cannot lie in either irrational eigenline.
Multiplying the two conjugate values in(4) gives

    AB=n^2/D,
    E_k=2(A lambda^(2k)+B lambda^(-2k))
       =4|n|/sqrt(D) cosh(2log(lambda)(k-x)).        (8)

It follows that the exact minimum over the ENTIRE actual-order unit orbit is attained at the nearest integer or integers to x and is

    E_min=4|n|/sqrt(D) cosh(2log(lambda)delta),
    4|n|/sqrt(D)<=E_min<=2|n|.                      (9)

For the upper bound, cosh is increasing on[0,infinity) and cosh(log lambda)=sqrt(D)/2.
Only the floor and ceiling of x need comparison; this is an exact formula for an infinite orbit, not an enumeration cutoff.
The continuous extension of the displayed energy formula, not a literal fractional power of tau in its real field, attains4|n|/sqrt(D), and the extra cosh factor is the full discretization cost.
It cannot be omitted merely because all real conjugate products have been balanced.
When x is a half-integer both neighboring integers minimize; otherwise there is a unique exponent minimizing energy, apart from the harmless overall sign of the unit.

The nontrivial field automorphism sigma(tau)=a-tau preserves the actual order and sends(u,v) to(-u,a u+v).
Its corresponding quantities in(7) are A_sigma=B/lambda^2 and B_sigma=lambda^2 A.
Thus x_sigma=1-x and

    E_k(sigma z)=E_(1-k)(z).                        (10)

Consequently adjoining BOTH trace-field automorphisms to all actual-order units does not lower the energy minimum at all.
Any finite composition belongs to the unit orbit of z or of sigma z, since sigma sends units to units;(10) proves their complete energy spectra coincide.
This is special to this actual family and this exact coefficient energy, not a theorem for general trace orders.

For clarity, the exact optimal normalized resultant-minus-coefficient margin over this orbit is

    Delta_orbit=(1/4)log(4a^2-9)
         +(1/2)log(sqrt(D)/4)
         -(1/2)log cosh(2log(lambda)delta).          (11)

It is at least(1/4)log(4a^2-9)-(1/2)log2.
The first two terms in(11) are precisely L261's full formal-degree-four supremum on P_a.
Thus the last term is an exact measurable loss from restricting to the stated fixed-norm unit/automorphism orbit.
Different unit orbits with the same norm need not be included here; no classification of all solutions of a fixed norm equation is asserted.


<a id="sharp-discrete-trace-orbit-loss-family"></a>
### 4. An infinite actual family attaining the worst orbit cost

Set a=2b for an integer b>=3, and choose the primitive trace element

    z_b=b tau+1=tau(tau-b),
    n_b=Norm(z_b)=b^2+1.                             (12)

Here lambda=b+sqrt(b^2+1).
The two consecutive unit representatives are

    (u_0,v_0)=(b,1),
    (u_(-1),v_(-1))=(1,-b),
    E_0=E_(-1)=2(b^2+1).                            (13)

In(7) their A/B ratio is lambda^2: indeed z_b(lambda)=lambda sqrt(b^2+1), whereas the conjugate value is sqrt(b^2+1)/lambda.
Thus x=-1/2, and(9) proves that EXACTLY k=0,-1 minimize energy among all integer powers.
The minimum saturates the general upper bound2|n_b|.
The continuous real-exponent minimum and the exact ratio are

    E_cont=2sqrt(b^2+1),
    E_min/E_cont=sqrt(b^2+1) ->infinity.             (14)

This is a primitive family with growing trace norm, not the constant norm-one observation already in L261.
Every auxiliary in each orbit has the SAME nonzero complete original resultant

    Res(P_(2b),C_k)=(9-16b^2)(b^2+1)^2,             (15)

and every original p-adic root depth is individually unchanged.
The full content remains one.
These are actual integral trace auxiliaries; they are not asserted to be outputs of a particular centered-window construction.
Varying k does not create any extra norm income, while optimizing over the entire orbit still leaves the unbounded relaxation loss(14).

Even adjoining the trace automorphism does not enlarge this particular orbit: since sigma(tau)=-tau^(-1) and sigma(tau-b)=-(tau-b), one has sigma(z_b)=tau^(-2)z_b.
Thus arbitrary compositions of actual trace units and order-preserving field automorphisms have been covered, not merely one chosen generator step.
There may still be other elements of the same norm generating different principal ideals or lying in different unit orbits.
Nothing here claims their exclusion or a global fixed-norm minimum over all integral pairs.

The exact orbit margin and its loss against L261's all-formal-degree-four supremum are

    Delta_orbit=(1/4)log(16b^2-9)-(1/2)log2>0,
    Delta_all-sup - Delta_orbit=(1/4)log(b^2+1).     (16)

The strict positivity uses16b^2-9>4.
The second equality follows either from(11) or from(14).
The expression Delta_all-sup is a supremum over all primitive integral directions, with their norms allowed to vary; it is not asserted to be attained.
In fact the relevant eigenvalue discriminant4(b^2+1) is not a square.
Formula(16) measures an actual unbounded orbit restriction, not a claim that a fixed norm is globally incapable of doing better by another nonunit construction.
No coefficient-height or search-time bound is inferred from approximating the unrestricted real direction.

<a id="full-trace-orbit-archimedean-and-leading-cost"></a>
### 5. Complete original conjugate values and an exact Mahler minimum

The unchanged local depths do not mean the archimedean values are unchanged.
At each original root alpha_i, the exact ratio is

    C_k(alpha_i)/C_0(alpha_i)
        =(alpha_i+alpha_i^(-1))^k.                  (17)

On the two real reciprocal original roots it has modulus lambda^k, and on the neutral conjugate pair it has modulus lambda^(-k).
Thus the individual logarithmic changes are(+k log lambda,+k log lambda,-k log lambda,-k log lambda), whose sum is zero.
Every original factor alpha_i(alpha_i^2-1) remains present in C_k; the trace action only changes its remaining value.
This explicitly records the full joint-conjugate redistribution rather than treating the preserved product as a bound for each place.
Nonarchimedean equality follows separately from the unit and inverse being integral, including primes dividing the discriminant or the order index.

For any real integral pair(u,v), the COMPLETE Mahler measure of the corresponding formal-degree-four auxiliary has the exact formula

    M((t^2-1)(u t^2+v t+u))
      =|v|,                              if u=0;
      =|u|,                              if u!=0, |v|<=2|u|;
      =(|v|+sqrt(v^2-4u^2))/2,           if |v|>2|u|.
                                                            (18)

For u=0 the retained factor is v t(t^2-1).
Otherwise the two quadratic roots have product1.
When their real trace -v/u has modulus at most2 both lie on the circle, leaving the leading coefficient |u|; when it exceeds2 the larger root magnitude times |u| gives the last formula.
The equality case gives repeated circle roots and is included.
The forced t^2-1 is retained and has measure1.
In particular

    M(C)>=max{|u|,|v|/2}                            (19)

with the first expression understood as0 when u=0.

For the family(12), the two equal-energy minimizing polynomials are

    C_0=(t^2-1)(b t^2+t+b),       M(C_0)=b,
    C_(-1)=(t^2-1)(t^2-b t+1),
    M(C_(-1))=eta_b=(b+sqrt(b^2-4))/2<b.            (20)

The first has all roots on the circle and leading coefficient b.
The second is monic and has an exterior reciprocal pair, with all four auxiliary factors and its positive measure retained.
Their coefficient energies and full resultants are equal, but their full Mahler costs are different.
In this family removing the exterior auxiliary pair is therefore not the same as minimizing the complete Mahler cost: the all-circle representative is slightly more expensive because of its leading coefficient.

In fact eta_b is the exact minimum over the ENTIRE actual unit/automorphism orbit.
For k>=1, recurrence(5) gives positive u_k,v_k with u_k>=u_1=2b^2+1.
Hence(19) gives M(C_k)>b.
For k<=-2, beginning with(u_(-2),v_(-2))=(-b,2b^2+1), the inverse recurrence gives opposite signs; at each further negative step the absolute coordinates update as(X,Y) to(Y,X+2bY).
Thus |v_k|>=2b^2+1, so(19) gives M(C_k)>b again.
The only remaining k are0,-1, whose costs are in(20); the harmless overall sign has no effect.
The automorphism adds no representative by the identity following(15).
Consequently

    min_orbit log M(C_k)=log eta_b,
    log eta_b=log b+o(1),
    log eta_b-m(P_(2b)) ->-log2.                    (21)

There is no unpaid leading coefficient or discarded root left in(21).
The exact best orbit energy, best complete auxiliary measure and complete original resultant are all known here, with each original local depth invariant throughout.
The measure cost nevertheless grows, alongside the original measure.
This does not contradict any hypothetical near-one arithmetic behavior.

<a id="trace-orbit-reduction-scope-and-next-gate"></a>
### 6. What changes, and what is still required near one

The structural gain is an exact entire-orbit optimization for every primitive trace element on an infinite actual family, including the full order unit group and both field automorphisms.
It replaces an unbounded search over powers by an exact nearest-integer formula with the explicit discretization penalty.
The subfamily(12) makes that penalty grow without bound even though the same original full norm and every finite root depth are kept.
Its trace norm grows, so this is not merely the older observation that norm-one units cannot manufacture income.
The two minimizing representatives also separate coefficient energy, all-circle auxiliary roots and full Mahler expense in a completely calculated way.

The geometric optimum in(9) is a continuous REAL relaxation.
It is not another actual trace unit and cannot be inserted as a permissible integral auxiliary.
The penalty depends on log lambda, the actual spacing of this order's positive units.
On this family that spacing grows with the original measure.
No estimate of such spacing, a useful integral orbit minimum, or full joint-conjugate control is proved for arbitrary high-degree trace orders near measure one.
Neither a maximal order nor the unit group of the full original degree-four field replaces the stated trace order.
Additional full-field multiplications might leave the trace-auxiliary class, which would require a new complete construction and cost proof.

All original input degrees in this family are four; the original total measure tends to infinity.
The proof is therefore a structural and cost discriminator, not near-one coverage, a high-degree obstruction or a counterexample to Lehmer.
In particular it does not prove that all useful integer auxiliaries lie in a known orbit or that the least coefficient-energy representative minimizes a joint archimedean bound.
The full values(17) show why such a bound must track the actual representative, even when the product and local arithmetic are identical.

[L237's uniform scalar-margin existence](Yin_L_G0237_v1.md#uniform-auxiliary-margin-fixed-scope) remains established.
[L261's norm-one near-one boundary](Yin_L_G0261_v1.md#trace-norm-symmetry-unresolved-near-one-scope) remains valid independently of this family.
A changed near-one test would need a genuinely sufficient trace norm and an integral reduction with its actual order spacing and joint-conjugate cost controlled, or a different nonunit/separated-window construction with full degrees, nonvanishing and normalization.
This proof supplies no permission to sum unrelated representatives' income or to infer a common cyclic time.
All active directions remain open, and the unrestricted G0001 Task is unresolved.


<a id="trace-orbit-author-selfcheck"></a>
### 7. Author self-check and complete freeze

The author self-check covers Sections1--7 and equations(1)--(21).
The author rechecked the actual degree-four irreducibility through the conjugate sign of the quadratic discriminant; the complete unit-group proof in the actual, possibly nonmaximal trace order; both integral inverse matrices and primitive content; the exact original signed resultant and individually invariant finite-place depths; both orthonormal eigenvectors and the product AB; the nearest-integer formula and its tie cases; the conjugate orbit spectrum and all finite compositions; the sharp family with nonconstant growing trace norm; the distinct domains of the continuous relaxation, all-direction supremum and fixed-norm unit orbit; the complete leading/exterior-root formula and every outside exponent in the whole-orbit Mahler minimum; the four actual conjugate-value ratios and measure asymptotics; and the stated source attribution and near-one limits.
The author replaced a preliminary reference to “principal-ideal classes” by “different principal ideals”: all principal ideals have trivial ideal class, whereas equal absolute norm does not identify their generators' unit orbits.
This clarification changes no calculation.

All new values are proved symbolically in the responsible draft.
No mathematical computation, continuing program, enumeration, J allocation or numerical experiment was performed.
The source was checked only at its identified classical attribution scope; the actual group classification and every optimizing deduction have their complete local proofs.
Root supplied no derivation.
A full separately organized noncontributor review remains required before adoption.
This self-check neither supplies that review nor resolves G0001.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0124_v1.md#trace-unit-orbit-complete-independent-review), with its original inspected scope and relationship.
