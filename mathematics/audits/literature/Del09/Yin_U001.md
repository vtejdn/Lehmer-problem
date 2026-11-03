---
author: Yin
---
# Del09-U001: explicit rank penalties and failure of full-packet gap extraction

Date: 2026-10-18T12:03.
Human record author Yin.
The angular_envelope_review AI directly read the primary published source for the bounded G0001 growing-rank feasibility test.
This retains selected definitions, exact statements and their direct application; it does not audit the original proof or its appendix constant derivation.

<a id="del09-u001"></a>
## Read; accepted statement with explicit constants

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Emmanuel Delsinne, Le probleme de Lehmer relatif en dimension superieure, Annales scientifiques de l'Ecole normale superieure, fourth series42(6) (2009), 981--1028; published Numdam rendering with one cover and 48 article pages.

Passages: Printed981--984/PDF2--5: height convention, Definition1.2, explicit kappa1/kappa2, Theorem1.6 and the displayed admissible c2(n) on printed984.

Inspection: Complete selected pages text-read; printed983--984 also rendered and visually checked for every exponent and the outer inverse. The multiplicative-independence specialization and complete Salem packet substitution below were checked. No proof or appendix audit, source-wide verification, optimal-constant assertion or uniform-rank theorem is claimed.


The [retained primary article](../../../literature/pdf/Del09--published.pdf) identify the exact edition.
The established Theorem1.6 and its printed explicit admissible constant are accepted at this statement/applicability scope.
The complete packet, height normalization and joint-degree calculation are retained in [AD99-U001](../AD99/Yin_U001.md#complete-salem-packet-specialization).
This unit does not extend [AM16-U005](../AM16/Yin_U005.md) by asserting that its fixed-rank constants are uniform.

<a id="relative-obstruction-and-torsion-conventions"></a>
### Definitions and degree conventions

For x=(x_1,...,x_n) in (Qbar^*)^n, h(x) is the absolute logarithmic projective height of (1:x_1:...:x_n).
Individual coordinate heights h_abs(x_i) have the standard Weil normalization; the theorem below uses their PRODUCT.
The source's Definition1.2 defines omega_K(x) as the least degree of a hypersurface defined over K containing x, with degree taken after the specified natural embedding into projective n-space.
Here K can be Qab, the maximal abelian extension of Q, and

    D_ab=[Qab(x_1,...,x_n):Qab]

is a finite relative degree even though the base field itself is infinite.
It is not the original degree of one coordinate and not automatically the full degree D over Q.
A proper torsion subvariety is a finite union of translates of proper subtori by torsion points, in the source's convention.
Multiplicatively independent coordinates lie in none: a proper torsion translate imposes a nonzero integral monomial relation with a root of unity on the right, whose suitable power contradicts independence.
The product theorem does not require replacing D_ab by an obstruction index.

### Exact positive denominator and logarithmic exponent

Put

    A_n=2(n+1)^2 (n+1)!,
    kappa1(n)=3 A_n^n,
    kappa2(n)=n kappa1(n),
    c2(n)=(2n^2)^n exp(64 n^2 n! A_n^(2n)).          (1)

For every n>=1, Theorem1.6 says that if the product of coordinate heights is at most

    [c2(n) D_ab (log(3D_ab))^(kappa2(n))]^(-1),

then x belongs to a proper torsion subvariety, with a further explicit degree bound not needed here.
The displayed c2(n) is one admissible choice printed on page984, not an optimized constant.
In particular multiplicative independence gives the STRICT contrapositive

    product_i h_abs(x_i)
       > [c2(n) D_ab (log(3D_ab))^(kappa2(n))]^(-1). (2)

The enormous positive c2(n) is in the DENOMINATOR; interpreting it as a favorable numerator reverses the actual statement.
Taking an n-th root divides the exponent kappa2 by n, leaving kappa1(n), which is still rapidly rank-dependent.
The constants eta1, eta2 and mu concern the exceptional subvariety degree and are not needed to apply(2) to independent coordinates.

### Full Salem packet: all degree and rank costs

For the complete inverse-pair packet of a genuine degree-2t Salem unit, every coordinate height is m/(2t), the coordinates are multiplicatively independent, and their joint field is the entire normal closure L.
These facts need no full signed-symmetric group hypothesis.
Write D=[L:Q], so D_ab=[LQab:Qab]<=D.
Applying(2) at n=t yields

    m > 2t c2(t)^(-1/t) D_ab^(-1/t)
                  [log(3D_ab)]^(-kappa1(t)).         (3)

Replacing D_ab by the larger D weakens this positive bound and is legitimate because its degree and logarithmic factors are decreasing in that positive degree.
For the actual full signed-symmetric root action, D=2^t t!, so this gives the entirely explicit conservative floor

    B_t = [t/(t!)^(1/t)] [1/(2t^2)]
          * exp(-64 t t! A_t^(2t))
          * [log(3*2^t*t!)]^(-3 A_t^t).             (4)

Thus m>B_t, but B_t tends to zero extremely rapidly.
There is no large-coordinate-height or projective-height factor available to cancel these penalties: the complete packet has maximum coordinate height m/(2t) and projective height m/2, exactly as recorded in AD99-U001.

Even the hypothetical most favorable replacement D_ab=1 does not rescue this selected explicit theorem.
The right side of(3) is then

    (1/t) exp(-64 t t! A_t^(2t))
                  [log3]^(-3 A_t^t),

which tends to zero; for every D_ab>=1 the actual source floor is no larger.
This is a bound on the explicit certificate supplied by(2), not an upper bound on the true Salem measure or a proof that better high-rank theorems are impossible.
No numerical evaluation or rank scan is necessary to establish the decay.

### Scope, source search and stopped inference

The bounded search traced AM16's actual higher-dimensional antecedents to the AD99 institutional primary artifact and this published Numdam article.
The selected primary statements and constants suffice to decide this feasibility question, so no source proof, appendix reconstruction, broader search or second construction was pursued.
The original AD99 publisher rendering required visual reading; a search-summary expression was not substituted for its actual printed kappa(n).
The two sources have different rank exponents and normalizations and are not treated as interchangeable editions.

The missing useful input would have to replace the present rank penalty by at most exponential total loss in t for the complete Salem packet, such as the explicitly unproved packet estimate in AD99-U001.
On the full signed-symmetric class that estimate is already equivalent up to an absolute factor to the desired measure gap, so this source reuse does not reduce it to a routine application.
The conditional C162 estimates, low-subdegree AM16 application and normal-trace results remain valid at their own scopes; no new qualitative gap coverage follows here.
This completed negative source-application test requires no new C or continuing D and changes no Task or execution authority.
