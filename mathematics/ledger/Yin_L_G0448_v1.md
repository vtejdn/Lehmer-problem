---
author: Yin
---
# Expansive Salem representations: unchanged Mahler value and degenerating Stieltjes margins

<a id="scope-and-original-cost"></a>
## Scope and source interface

This 2026-11-05 exploration for [G0001](../tasks/Yin_T_G0001_v1.md#contract) tests whether an actual expansive-polynomial representation supplies a decreasing quantity or a uniform positive separation for the original Salem value.
It concerns the Salem subdomain only and asserts no reduction of all reciprocal unit inputs to that subdomain.
The calculations and their ordinary checks are author work for Yin; no independent proof review, new Claim assessment or total-Mahler gap is asserted.

The source is Christelle Guichard and Jean-Louis Verger-Gaugry, [On Salem numbers, expansive polynomials and Stieltjes continued fractions](https://arxiv.org/pdf/1402.6681v2), arXiv:1402.6681v2 [math.NT], 22 July 2015.
The inspected passages are Theorem 1.1 on printed page 3; Theorem 2.5 on page 14; Proposition 2.3 and its construction on pages 21--22; Theorem 2.9 and its semigroup discussion on pages 25--26; and the transformations and Hurwitz alternants in Sections 3.1--3.2 on pages 27--31.
The actual online v2 was read at statement/applicability scope with the selected algebra checked below.
The complete source proof and the original Bertin--Boyd, Hurwitz and Stieltjes proofs were not independently audited, and no local original-file acquisition is claimed.

Theorem 1.1 supplies a same-degree monic expansive representation of a Salem polynomial.
The construction of a positive-constant representative uses the original admissible cone; Proposition 2.3 retains its input-dependent matrix and rounding costs.
The source does not supply a uniform upper bound for the least usable constant term.
The positive rational continued fraction is an actual representation, rather than a replacement by arbitrary positive data.
The earlier [MS12b Pisot/interlacing comparison](../audits/literature/MS12b/Yin_U001.md#ms12b-u001) concerns a different representative and already retains its missing coefficient-cost bounds.
The present test examines whether the expansive representation's positivity and boundary margins provide new information without importing those missing bounds.

<a id="fixed-salem-and-expansive-input"></a>
## The actual input and the source criterion

Let T be the monic irreducible minimal polynomial of a genuine Salem number beta>1, of even degree d>=4.
Thus its roots are beta, beta^(-1) and d-2 roots on the unit circle, paired by complex conjugation.
The roots are simple, T is reciprocal, T(0)=1 and T(1)T(-1) is nonzero.

Let P in Z[z] be an actually supplied monic expansive polynomial of the same degree d, with positive constant term q=P(0)>1, satisfying

    (z-1)T(z)=zP(z)-P*(z),                            (EX1)
    P*(z)=z^d P(1/z).

Expansive means that every root of P has modulus strictly greater than one.
Since P is monic, M(P)=q and its total logarithmic measure is log q.
The original total logarithmic measure is m(T)=log beta; it is not log q.

Theorem 2.5 gives the following exact criterion for the supplied association equation:

    P(1)T(1)<0,                                      (EX2)
    (alpha-1) alpha^(1-d) P(alpha) T'(alpha)
        is real and strictly negative                (EX3)

for every unit-circle root alpha of T.
Only this criterion's stated real-polynomial domain and the actual supplied integral representative are needed below.

The real reciprocal pair contributes (1-beta)(1-beta^(-1))<0 at z=1, while each unit-circle conjugate pair contributes |1-alpha|^2>0.
Consequently T(1)<0 and EX2 gives P(1)>0.
At z=-1 both the real reciprocal pair and every circle pair contribute positively, so T(-1)>0.
Evaluation of EX1 at -1 gives P(-1)=T(-1)>0.

<a id="same-value-semigroup"></a>
## Arbitrarily large expansive cost at exactly the same original value

For every integer n>=1 put

    P_n=T+n(P-T)=nP-(n-1)T,
    q_n=P_n(0)=1+n(q-1).                             (SV1)

The polynomial P_n is monic, integral and of degree d.
Reciprocity of T gives zT-T*=(z-1)T, so linearity of the fixed-degree reciprocal operation proves

    zP_n-P_n*=(z-1)T.

At a unit-circle root alpha of T one has P_n(alpha)=nP(alpha), and therefore EX3 is multiplied by the positive integer n.
Also

    P_n(1)=nP(1)-(n-1)T(1)>0.                         (SV2)

Together with T(1)<0, this preserves EX2.
The source criterion therefore proves that every P_n is expansive.
This is also the repeated-addition case of the source's Theorem 2.9, whose operation is P plus Q minus T.

The original polynomial T, all its conjugates, its degree and beta are unchanged.
In contrast,

    M(P_n)=q_n -> infinity,
    m(P_n)=log q_n -> infinity,
    m(T)=log beta remains fixed.                     (SV3)

Thus positivity can coexist with arbitrarily large actual representation cost at one fixed original value.
This does not exclude an inexpensive representative of that value; it prevents treating the cost of an arbitrary positive representative as a decreasing original-Mahler quantity.

<a id="unnormalized-hurwitz-and-boundary-margins"></a>
## The exact integer Hurwitz normalization and two vanishing margins

Retain the unnormalized integer polynomial

    H(w)=(w+1)^d P((w-1)/(w+1))
        =sum_(j=0..d) h_j w^j
        =E(w^2)+w O(w^2),                            (HU1)

where E(x)=sum_j h_(2j) x^j and O(x)=sum_j h_(2j+1) x^j.
Write h(x)=O(x)/E(x) for its Hurwitz alternant.

For a root rho of P the corresponding root of H is w=(rho+1)/(1-rho), and

    Re w=(1-|rho|^2)/|1-rho|^2<0.

The leading coefficient of H is P(1)>0.
Factoring the real polynomial H into its real linear factors and conjugate quadratic factors shows that every coefficient h_j is strictly positive: each factor has positive coefficients, since its roots have negative real part.
In particular E(x)>0 for x>=0 and the formulas below have no omitted positive-real denominator zero.
The source's Theorem 3.2 identifies this alternant with the positive rational terminating Stieltjes fraction at its stated scope.
The identities below use HU1 directly and need no uniform bound for those rational coefficients or their cleared denominators.

Expanding HU1 as sum_j p_j(w-1)^j(w+1)^(d-j), where p_d=1 and p_0=q, gives

    H(1)=2^d q, H(-1)=2^d,
    E(1)=2^(d-1)(q+1), O(1)=2^(d-1)(q-1).

The factor 2^d is retained rather than silently normalizing the integer polynomial.
Consequently

    h(1)=(q-1)/(q+1),
    1-h(1)=2/(q+1)>0.                               (HU2)

The two highest coefficients in HU1 are

    h_d=P(1),
    h_(d-1)=d P(1)-2P'(1).                           (HU3)

Differentiating EX1 at z=1, using (P*)'(1)=dP(1)-P'(1), gives

    T(1)=(1-d)P(1)+2P'(1)
        =h_d-h_(d-1).

As d is even, E has degree d/2 and O has degree d/2-1.
It follows that

    lim_(x->+infinity) x h(x)-1
        =h_(d-1)/h_d-1
        =-T(1)/P(1)>0.                              (HU4)

Apply HU1--HU4 to every P_n, writing its alternant h_n.
Equations SV1--SV2 now give both exact degenerations:

    1-h_n(1)=2/[2+n(q-1)] ->0,
    lim_(x->+infinity) x h_n(x)-1
        =-T(1)/[nP(1)-(n-1)T(1)] ->0.               (HU5)

All limits in HU5 are stated in their actual order: the second expression first takes x to infinity for each n and then takes n to infinity.
There is no exchanged-limit assertion.
These two positive margins tend to zero while the original beta, T and m(T) remain fixed.

<a id="original-salem-root-in-the-alternant"></a>
## The original Salem root remains in the exact recovery equation

Put

    s=(beta+1)/(beta-1)>1, x=s^2.

Then beta=(s+1)/(s-1), and HU1 gives

    H(-s)=(s-1)^d P(beta),
    H(s)=(s+1)^d P(beta^(-1)),

because d is even.
Evaluating EX1 at beta gives beta P(beta)=beta^d P(beta^(-1)).
Hence

    beta H(-s)=H(s).

Substituting H(s)=E(s^2)+sO(s^2) and H(-s)=E(s^2)-sO(s^2) yields

    (beta-1)E(s^2)=s(beta+1)O(s^2).

Since E(s^2)>0 and (beta+1)/(beta-1)=s, this is precisely

    x h(x)=1,
    x=((beta+1)/(beta-1))^2.                         (RT1)

The same computation applies to every P_n, with exactly the same beta and x.
Thus the two margins in HU5 are not standalone measures of how close the original Salem value is to one.
Their smallness can be purchased by changing the representation alone.
The equation RT1 retains the actual return, but positivity and these endpoint identities provide no uniform bound for its original solution.

## Mathematical outcome and remaining scope

The representation really supplies positive rational continued fractions for actual Salem inputs, and its degree equals the original degree.
The tested proposed gain was a decrease or a uniform separation obtained from that positivity, integer normalization or proximity to the two displayed boundaries.
The same-value family SV1 and its exact costs HU5 show why these quantities cannot provide that gain by themselves.

Minimizing q over expansive representatives of a fixed T would select a cheaper representative of the same value; such minimization does not lower m(T).
No bound for that minimum, no quantitative restriction on the other alternant coefficients and no original-value descent is supplied here.
The fixed-source representation theorem does not make any of those additional assertions.
A different restriction coupling the entire positive fraction to the original root might still be useful, but it would need actual information beyond the present construction.

This is a useful failure of this specific positive-representation test, not a theorem against all interlacing or Stieltjes methods.
It provides neither arbitrarily small positive Mahler values nor a positive uniform gap, even on the Salem subdomain.
It supplies no classification of all expansive representatives and no reduction from the unrestricted reciprocal-unit domain.
No numerical experiment or new computation was used.
