---
author: Yin
---
# Pri11-U002: direct Dirichlet-energy discrepancy on compact Lipschitz tests

Date: 2026-10-15T13:42.
Human record author Yin.
Root directly inspected this new source interface for the G0001 complete cyclic-norm energy inquiry.
This unit is separate from U001's already accepted Theorem3.1 Lipschitz/support-radius estimate; it does not revise that unit or retroactively change L167/L168.

<a id="pri11-u002"></a>
## Read; accepted restricted external statement

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Igor E. Pritsker, Distribution of algebraic numbers, J. reine angew. Math.657 (2011),57--80; actual retained Pri11.pdf, arXiv1307.5734v1,22 July2013,22 pages.

Passages: Printed/PDF p.2 normalized circle and zero-counting measures; pp.14--15 modulus of continuity and planar Dirichlet definition; p.15 Theorem4.2/(4.16); pp.15--16 its displayed proof, including (4.17)--(4.18), energy bound and Theorem3.1 deduction.

Inspection: Root text-read the actual retained pp.2,14--16 and visually inspected a fresh rendering of complete p.15, checking the absolute values, leading-coefficient/discriminant factor, both square roots and every coefficient in(4.16). The displayed proof was read for its regularization/Green/energy mechanism. Foundational potential identities and the cited external energy theorem were not independently re-proved; no whole-source proof audit, new edition comparison or new acquisition is claimed.


Let P(z)=a product_(j=1)^N(z-beta_j), a!=0, have simple zeros, N>=1.
Put tau=N^(-1)sum_j delta_(beta_j), and let mu be probability arclength on the unit circle.
The multiplicative Mahler measure M(P) includes abs(a); Delta(P) is the ordinary polynomial discriminant.
For a real test phi put

    omega_phi(epsilon)=sup_(abs(z-w)<=epsilon) abs(phi(z)-phi(w)),
    D[phi]=integral_(R^2) [phi_x^2+phi_y^2] dx dy.

For the accepted domain here, phi is CONTINUOUS, COMPACTLY SUPPORTED and GLOBALLY LIPSCHITZ, with finite D[phi].
For EVERY epsilon>0 the source gives

    abs(integral phi d tau-integral phi d mu)
       <=omega_phi(epsilon)
          +sqrt(D[phi]/(2pi))
             *sqrt( (2/N)log M(P)
                     -(1/N^2)log abs(a^2 Delta(P))
                     -(1/N)log epsilon+4epsilon ).        (4.16)

The globally Lipschitz restriction is a deliberately retained additional hypothesis of THIS accepted use.
The printed theorem states continuity, compact support and finite Dirichlet integral, with a.e. partial derivatives described just before it.
This unit does not adopt or settle an interpretation of that more general regularity domain.
Every proposed project test is globally Lipschitz and piecewise differentiable; the source's Green/energy argument is used only on that regular class.
No extension to arbitrary continuous singular functions is inferred.

The source theorem itself imposes no integer-coefficient, monic, irreducibility, Salem, unit-disk-root or N>=55 condition.
Those extra arithmetic conditions enter only when needed in a consumer.
In particular N>=55 belongs to the simplified Theorem3.1 estimate, not to(4.16).

## Applicability accepted for the current project

For the monic irreducible integral minimal polynomial of beta=alpha^n, characteristic zero gives simple zeros, a=1, and abs Delta(P_beta)>=1.
Thus the negative discriminant term can be DROPPED in an upper estimate, leaving

    omega_phi(epsilon)+sqrt(D[phi]/(2pi))
                       *sqrt(2h(beta)-log(epsilon)/N+4epsilon).

This is a direct statement specialization, not a new discrepancy theorem or an arithmetic income bound.
The normalized height is h(beta)=log M(P_beta)/N.
N is the ACTUAL powered degree, and the original-field norm repetition must still be handled by the project proof.
No substitution of the original degree for N or lower degree bound is supplied by this source unit.

The project must prove compactness, global Lipschitz regularity, a valid Dirichlet integral bound, modulus of continuity, circle integral and control of all exterior conjugates for its particular test.
A raw logarithm with a pole or unbounded support is not an admissible test.
The direct energy estimate does not make the Lipschitz or support fees disappear unless the project actually computes the smaller energy.

Root accepts this established restricted statement at exact statement/applicability scope.
The proof reading identifies circular regularization, Green's identity, Cauchy--Schwarz and the discriminant energy bound, but does not certify the full external potential-theory proof.
The previous U001 source-proof limit remains unchanged.

## Discovery and source boundary

The source was already registered.
A bounded current project search by Theorem4.2, equation4.16 and Dirichlet integral located the original L167 attribution and Pri11 reading note; those notes explicitly withheld adoption of this direct theorem.
Root read the complete relevant L167 proof, which is a self-contained SALEM circle calculation, and L168's general compact test, which instead consumes U001.
No existing accepted direct general-unit energy application was identified in that bounded search; this is not a global novelty claim.

The fresh attempt to open the exact arXiv v1 abstract page with the web reader returned DisabledError.
The actual registered local PDF was fully available and supplied all inspection above; the online failure does not change its edition or provenance.
No replacement artifact, publisher equivalence or later version is asserted.
The original mathematical consumer is the new [complete fixed direct planar-energy inquiry](../../../claims/Yin_C_G0147_v2.md#argument), retained for its separate whole independent project review.
