---
author: Yin
---

# Global derivative preparation and Salem circle bounds limit finite-exactness certificates

Human author Yin.
Provenance: project deduction under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the derivative-degree question and the direct C711 circle-price comparison.
The characteristic_zero_bridge agent derived the complete DC1--DC12 argument; root read the entire candidate and checked its stated arithmetic, domains and source applications.
Both are contributors, so their checking supplies no independent review of this result.
No native mathematical computation, new literature acquisition or uninspected external theorem is used.

## Statement

Use the SAME canonical trace system of adopted [C720](Yin_C_G0720_v1.md#decision-whole-reviewed-2026-10-25).
For a monic integer trace polynomial T of degree D, set C2=X^2-2, C3=X^3-3X and C5=X^5-5X^3+5X, and

    a=rem_T(T(C2))/2,
    b=rem_T(T(C3))/3, c=rem_T(T(C5))/5,
    F=rem_T(2c^2-3a^5),
    X_s=rem_T(b^2-a^3+s(c^3-2b^5)), s in{1,-1}.

The actual divisions and canonical remainders are integral and all use this same T.
Whenever P(z)=z^D T(z+z^(-1)) is irreducible and nontorsion, write N=2D, m=log M(P)>0, S=max_(|z|=1)|P(z)| and

    A_F(S)=2S^2/25+3S^5/32,
    A_X(S)=S^2/9+S^3/8+S^3/125+2S^5/243,
    Theta(P)=max{log A_F(S)+10m,
                     log A_X(S)+15m},
    kappa=61319/243000,
    U(N,m)=m+(9/2)sqrt(N)+(log N)/(2sqrt(N))
           +sqrt(N(2log N+7)(2m+log N+4)), N>=8,
    B_U(N,m)=5U(N,m)+15m+log kappa.

All logarithms are natural except explicitly written log_2.
Theta and B_U are sufficient-certificate thresholds from C720; neither is asserted to be the actual residual norm or a necessary condition for the exact identities.
The full reciprocal degree and total Mahler measure retain their original normalization.

A. For EVERY integer n>=1 and monic T of positive degree D with T' coefficientwise divisible by2^(n+1), one has2^(n+1)|D and D>=2^(n+1).
If P is additionally irreducible and nontorsion, then

    N>=2^(n+2)>=8,
    B_U(N,m)>45*2^(n/2)-2log2>n log2.

Thus C720's strict U-based sufficient certificate at that precision n has empty coverage in this derivative-prepared domain, independently of any special finite-construction source.
This conclusion does not exclude C720 PC3 evaluated with TRUE S(P), another estimate, an exact residual solution, or an input lacking that derivative assumption at the same target precision.
The credited C706 derivative lemma supplies global squareness of a divided residual R/2^n modulo2 when both this derivative condition and its actual coefficient divisibility hold; the converse from global squareness is not asserted.

B. Take EVERY actual C711 construction with its residual-preservation exponent h>=1, trace degree D>=2, c0 in{3,75}, M=2^(h+1), L=c0 M and Z=LD.
Here c0=3 is the basic construction and c0=75 the norm-controlled tower choice, and neither denotes the canonical quotient c.
For its actual Salem polynomial P and Salem root beta, put m=log beta, with all original roots counted.
Then

    Z/2<=S<=2LD+3L/2-1<11Z/4,
    Z/3<beta<7Z/6,
    C_star=5log(11/4)+15log(7/6)+log kappa,
    20log Z-4log2-20log3
          <Theta(P)<20log Z+C_star,
    Theta(P)/log2
          >20h+16+20log_2 D+20log_2(c0/3)
          >=20h+36>h.

Thus the TRUE PC3 threshold has an explicit logarithmic, rather than square-root-degree, price on this family, but cannot be met by its h guaranteed residual bits.
For that application the supplied T_0 must already satisfy BOTH residual congruences modulo2^h; the bounds on S, beta and Theta hold for every prescribed coefficient class independently of that premise.
Possible additional divisibility beyond the guaranteed h is not excluded.
This is no nonexistence result for arbitrary lifts of the same class, and no new nonzero-residual assertion for h=1,2,3 is made.
For h>=4 retain the separate C711 explicit nonzero-first-residual theorem at its actual scope.

C. In the norm-controlled C711 tower, EVERY dyadic k>=1 gives the actual irreducible P_k(z)=P(z^k), with full degree2Dk and

    S(P_k)=S(P), m(P_k)=m(P), Theta(P_k)=Theta(P).

Each nonzero canonical residual has the same exact coefficient2-adic order throughout that tower, by C720's integer covariance and polynomial-composition injectivity.
Consequently the true threshold stays fixed, whereas the U threshold increases with k when the base full degree is at least8.
The lower bound in B uses the BASE D and h, not Dk; the tower polynomial need not be a newly centered C711 representative and only its base is Salem.
The whole theorem concerns the stated certificate mechanisms and exact domains, with no unrestricted G0001 conclusion or necessity claim for its auxiliary system.

## Complete argument

<a id="derivative-degree-and-certificate-obstruction"></a>
### Global derivative preparation excludes the coarse U certificate at its own precision

The characteristic_zero_bridge agent authored this bounded deduction from root's proposed derivative/degree test.
Root supplied the question and its certificate-scope distinction; this is contributor work awaiting any separate whole review.
The exact prior derivative mechanism was directly read in [C706 DP2](Yin_C_G0706_v1.md#argument), with its [adopted assessment](Yin_C_G0706_v1.md#decision-whole-reviewed-2026-10-25).
The all-degree U and norm certificate are the adopted [C720 PC1--PC5](Yin_C_G0720_v1.md#decision-whole-reviewed-2026-10-25).
No native computation or new external theorem is involved.

Let n>=1 be an integer and T in Z[X] be monic of positive degree D, and assume coefficientwise

    T' in 2^(n+1) Z[X].                            (DC1)

Then

    2^(n+1) divides D, D>=2^(n+1).                 (DC2)

If P(z)=z^D T(z+z^(-1)) is also irreducible and nontorsion, it is an actual monic reciprocal integer-unit input of full degree N=2D>=2^(n+2)>=8.
For EVERY such input, with its actual total measure m>0 and the exact C720 U and kappa, one has

    5U(N,m)+15m+log kappa
        >45*2^(n/2)-2log2
        >n log2.                                  (DC3)

Consequently the strict PC5 sufficient inequality at precision n is impossible throughout this entire derivative-prepared domain.
No C724 source, residue support, large-q choice, Salem condition or additional degree lower bound is used.
This is a comparison with the numerical U-based sufficient criterion, not a claim that actual nonzero residual precision is bounded by that criterion's lower bound.
It does not rule out PC3 evaluated with the TRUE S(P), another norm estimate, exact residual identities, or a solution produced without DC1.
It also does not apply at a later target precision for which DC1 has not been retained with that target's exponent.

For the complete proof, the leading coefficient of T' is D, so DC1 immediately gives DC2 without using any other coefficient.
The positive summands in C720 PC4 give U(N,m)>=(9/2)sqrt(N), while kappa=61319/243000>1/4 and m>=0.
Together with N>=2^(n+2), this proves the first strict inequality in DC3.
For the second, the elementary exponential bound gives

    45*2^(n/2)-(n+2)log2
      >=45+((43/2)n-2)log2>0, n>=1.               (DC4)

Indeed 2^(n/2)=exp((n/2)log2)>=1+(n/2)log2.
This proves DC3 at every allowed integer n, including n=1.

The precise relation to the original square-error preparation is one-way.
C706 proves that DC1 passes through the ACTUAL divided canonical quotients and both canonical residual derivatives, without losing a dyadic factor at a because Delta(T)'=X T'(C2)-TT'.
If either actual residual R is also coefficientwise divisible by2^n, its integer coefficient quotient H=R/2^n has H' even, so Hbar belongs to F_2[X^2] and is a global square.
Global squareness by itself is not asserted to imply DC1 or DC2.
The obstruction concerns this particular sufficient way to obtain the square property.

<a id="salem-direct-circle-price"></a>
### Direct circle price of the actual C711 representatives

This is a separate exact-family comparison, not an extra premise of DC1--DC4.
Reuse the complete adopted [C711 SL1--SL3 construction](Yin_C_G0711_v1.md#decision-whole-reviewed-2026-10-25).
Write h>=1 for its residual-preservation exponent, D>=2 for its trace degree, c0 in{3,75}, and

    M=2^(h+1), L=c0 M, Z=LD.

Here c0=3 is the basic construction and c0=75 is its norm-controlled tower choice.
The original C711 notation calls this precision exponent n; h separates it from the arbitrary derivative-preparation exponent in DC1.
Do not confuse c0 with the canonical quotient c.
The statement about guaranteed h residual bits assumes that the supplied T_0 already has BOTH actual residuals divisible by2^h; C711 then preserves that precision for the selected sign.
The circle and threshold bounds themselves hold for every supplied coefficient class, without assuming those residual congruences.
Let P be the ACTUAL resulting polynomial, beta its Salem root, S=max_(|z|=1)|P(z)| and m=log beta, the full logarithmic Mahler measure.
Then

    Z/2<=S<=2LD+3L/2-1<11Z/4,
    Z/3<beta<7Z/6.                               (DC5)

Thus S is bounded above and below by explicit absolute multiples of2^h D, uniformly over every prescribed coefficient class and both fixed choices c0.
Its direct logarithmic price is of order h+log D, with no square-root degree fee.

Define the TRUE C720 PC3 threshold by

    Theta(P)=max{log A_F(S)+10m,
                     log A_X(S)+15m},
    C_star=5log(11/4)+15log(7/6)+log kappa.

Then

    20log Z-4log2-20log3
        <Theta(P)<20log Z+C_star.                (DC6)

In particular

    Theta(P)/log2
      >20h+16+20log_2 D+20log_2(c0/3)
      >=20h+36>h.                                (DC7)

Therefore PC3 cannot certify the exact equations from the h residual bits GUARANTEED by C711, even when its TRUE circle supremum replaces the coarse U bound.
This conclusion holds for h=1,2,3 as well as higher h; it does not assert a nonzero first residual in those lower-precision cases.
For h>=4, C711 already supplies its own stronger explicit nonzero-first-residual theorem for these representatives; that theorem is neither reproved nor enlarged here.
Possible extra residual divisibility beyond the guaranteed h is not excluded by DC7, and no conclusion is drawn about arbitrary lifts of the same coefficient class.

For the proof retain every coefficient from C711's actual polynomial

    P(z)=z^(2D)+1-B(z^(2D-1)+z)
           +sum_(j=2)^(D-1) a_j(z^(2D-j)+z^j)
           +b z^D.

Its centered coefficients and actual central adjustment satisfy

    LD/2<=B<=LD/2+L-1,
    |a_j|<=L/2, |b|<=3L/2-1.                      (DC8)

The sum is empty at D=2.
The upper bound on B uses its integrality and C711's strict B<LD/2+L; L and LD/2 are integers.
The coefficient identity

    [z]P=(1/(2pi)) integral_0^(2pi)
                    P(exp(it))exp(-it) dt=-B

gives B<=S by the triangle inequality.
Counting the two endpoints, the two B terms, all D-2 paired a_j terms and the single central b gives

    S<=2+2B+2sum_(j=2)^(D-1)|a_j|+|b|
      <=2B+LD-L/2+1
      <=2LD+3L/2-1<11LD/4.                       (DC9)

The last inequality uses D>=2.
This includes the empty middle sum at D=2 and the possible central Eisenstein adjustment.

C711's actual root bounds are

    (L/2-2)D+1<beta<(L/2+2)D+L-2.

Since L>=12, L/2-2>=L/3 and L/2+2<=2L/3.
Since D>=2, L<=LD/2.
These give the two strict beta bounds in DC5, with every original unit-circle root retained in m=log beta.

For the lower DC6 use the actual second threshold, A_X(S)>=(2/243)S^5, S>=Z/2 and beta>Z/3:

    Theta(P)>=log A_X(S)+15log beta
      >log(2/243)+5log(Z/2)+15log(Z/3)
       =20log Z-4log2-20log3.                    (DC10)

For the upper DC6 use C720 PC12, namely A_F(S)<=(139/800)S^5, A_X(S)<=kappa S^5 and139/800<kappa.
Because m>0,

    Theta(P)<=5log S+15m+log kappa
             <20log Z+C_star.                    (DC11)

Substituting Z=c0 2^(h+1)D in DC10 proves DC7 exactly.
This prices the actual PC3 threshold itself from above and below; it is not merely an upper estimate whose failure is silently promoted to a necessity assertion.
The threshold is a sufficient-certificate parameter, not the exact residual norm or a necessary condition for the identities.

<a id="direct-circle-price-along-tower"></a>
### Full tower comparison and the distinct unresolved alternatives

For the norm-controlled C711 choice, EVERY k=2^r gives an actual irreducible P_k(z)=P(z^k), with full degree2Dk.
The unit-circle map z->z^k is surjective, so

    S(P_k)=S(P), m(P_k)=m(P), Theta(P_k)=Theta(P).  (DC12)

The measure identity counts all k roots over each original root, as in the fixed C711/C720 argument.
The exact canonical covariance and coefficient-composition injectivity established in C720 retain each nonzero residual's exact2-adic coefficient order throughout this tower.
Thus the TRUE PC3 threshold is constant along the tower, although the U-based PC5 threshold strictly increases with k when the base full degree is at least8, as required for that displayed U formula.
The original lower bound DC7 remains in terms of the BASE D and guaranteed exponent h; substituting Dk into DC5--DC7 as if the tower polynomial were a newly centered C711 representative would be invalid.
Neither the tower's shrinking house nor the improved direct S estimate supplies new residual bits or small total measure.

The two deductions have deliberately different domains.
DC3 excludes the coarse U certificate for every actually irreducible derivative-prepared input at the indicated precision, leaving the true-S criterion open there.
DC7 excludes the true-S certificate at the GUARANTEED precision on C711's specific representatives, leaving other representatives and other arguments open.
Both results distinguish certificate failure from residual nonexistence and from the unrestricted G0001 objective.
A useful next input must change a proved quantitative feature of the actual construction, rather than only raising the derivative exponent, composing a pure tower, or normalizing away its degree.

The local reuse pass found the exact derivative lemma in C706 and the complete coefficients, root geometry and tower in C711; C720 supplies the exact norm certificates already adopted through R941.
Those adequate fixed inputs suffice, so no new external-source search or native computation was needed.
All DC1--DC12 calculations above are author deductions awaiting fresh isolated whole review; current C720 acceptance is not a review of this new comparison.


## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision two-certificate-boundaries-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T16:10 |
| status | open |
| reason | Register the complete two-domain finite-exactness comparison DC1--DC12 after contributor checking. The derivative's leading coefficient forces an exponential degree floor that prevents the coarse U certificate at the same target precision. The actual C711 coefficients, central adjustment and full root bounds give two-sided logarithmic prices for the TRUE PC3 threshold, which still exceeds the guaranteed precision; its exact tower threshold stays constant. All derivative-versus-square, true-S-versus-U, guaranteed-versus-extra precision, original degree/measure, lower-h and nonexistence limitations are explicit. Fresh isolated whole review remains required; no residual realization or unrestricted Task completion is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete bounded certificate theorem](#statement) | Parts A--C, all n>=1 derivative inputs and h>=1/D>=2 actual C711 representatives, exact canonical system, full degree and total measure, true and coarse thresholds, both construction choices, every tower level and all excluded inferences. |
| argument | [Complete DC1--DC12 proof](#complete-argument) | Leading derivative coefficient and strict exponential comparison, one-way C706 square interface, full actual coefficient count including D=2 and central adjustment, both beta bounds, true-threshold lower/upper constants, guaranteed-bit limitation, exact tower circle/measure/precision invariance and all domain boundaries. |
| dependency | [Adopted finite-exactness certificates](Yin_C_G0720_v1.md#decision-whole-reviewed-2026-10-25) | PC1--PC5 exact Theta and U thresholds, PC12 scalar bounds, U monotonicity and exact dyadic coefficient-precision/covariance interface; its whole R941 does not review this new deduction. |
| dependency | [Adopted actual Salem construction and tower](Yin_C_G0711_v1.md#decision-whole-reviewed-2026-10-25) | SL1--SL3 and SL5--SL6 actual centered coefficients, integer B interval, possible central L adjustment, empty D=2 middle sum, complete beta/root/measure bounds, all prescribed classes and full irreducible norm-controlled tower. Its h>=4 nonzero-first-residual statement is retained only as separate comparison, not used to prove the new threshold bounds. |
| dependency | [Adopted canonical derivative lemma](Yin_C_G0706_v1.md#decision-whole-reviewed-2026-10-25) | DP2 actual monic-division derivative inheritance, dyadic Delta(T) formula without a factor2 loss, and residual quotient global-square consequence. This supplies only the one-way square-preparation interface; the leading degree and PC5 obstruction are proved here without it. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T16:21 |
| status | proved |
| reason | Adopt the entire fixed Parts A--C and DC1--DC12 after reading the whole theorem and fresh isolated whole R943. The derivative degree floor, exact same-precision U-certificate limitation, direct actual Salem coefficient/root/circle bounds including every endpoint, true-threshold lower and upper constants, guaranteed-versus-extra precision and complete tower comparison are supported. The repaired same-object C706 argument link changes no mathematics. These are specified sufficient-certificate limitations, not residual nonexistence, a controlled-measure realization or G0001 completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete bounded certificate theorem](#statement) | Parts A--C, all n>=1 derivative inputs and h>=1/D>=2 actual C711 representatives, exact canonical system, full degree and total measure, true and coarse thresholds, both construction choices, every tower level and all excluded inferences. |
| argument | [Complete DC1--DC12 proof](#complete-argument) | Leading derivative coefficient and strict exponential comparison, one-way C706 square interface, full actual coefficient count including D=2 and central adjustment, both beta bounds, true-threshold lower/upper constants, guaranteed-bit limitation, exact tower circle/measure/precision invariance and all domain boundaries. |
| dependency | [Adopted finite-exactness certificates](Yin_C_G0720_v1.md#decision-whole-reviewed-2026-10-25) | PC1--PC5 exact Theta and U thresholds, PC12 scalar bounds, U monotonicity and exact dyadic coefficient-precision/covariance interface; its whole R941 does not review this new deduction. |
| dependency | [Adopted actual Salem construction and tower](Yin_C_G0711_v1.md#decision-whole-reviewed-2026-10-25) | SL1--SL3 and SL5--SL6 actual centered coefficients, integer B interval, possible central L adjustment, empty D=2 middle sum, complete beta/root/measure bounds, all prescribed classes and full irreducible norm-controlled tower. Its h>=4 nonzero-first-residual statement is retained only as separate comparison, not used to prove the new threshold bounds. |
| dependency | [Adopted canonical derivative lemma](Yin_C_G0706_v1.md#decision-whole-reviewed-2026-10-25) | DP2 actual monic-division derivative inheritance, dyadic Delta(T) formula without a factor2 loss, and residual quotient global-square consequence. This supplies only the one-way square-preparation interface; the leading degree and PC5 obstruction are proved here without it. |
| review | [Fresh isolated whole cost review](../audits/reviews/Yin_R_G0943_v1.md#whole-certificate-cost-finding) | Independently reviewed entire fixed statement, complete proof, initial selected decision and the three consumed fixed inputs, all n/h/D endpoints, both c0 choices and every tower level, with source limits retained. |

