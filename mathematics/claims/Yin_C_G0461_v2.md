---
author: Yin
---
# Direct Blaschke budgets and the exact Galois obstruction to norming their small energy

This version extends the same original exterior-factor question by retaining the complete analytic theorem in [C461 v1](Yin_C_G0461_v1.md#statement) and proving the Galois behavior of that actual function for irreducible reciprocal units.
The earlier direct/inverse budgets, finite-lag statements, controls and limitations remain at their exact v1 scope; they are not silently restricted to the new reciprocal domain or assigned a stronger review relationship.
The new theorem identifies why its small original coefficient energy cannot be passed unchanged to every embedding in an integer norm.
The [unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

## Inputs and retained scope

The [v1 statement and complete argument](Yin_C_G0461_v1.md#statement) retain all original Sections 1--7 and equations 1--24: the actual exterior-root direct function, exact total and weighted squared coefficient masses, coefficientwise bound, both finite-lag detection estimates, formal moment identity, fixed-input residual convergence, actual dyadic golden controls, separately nonarithmetic controls, bounded quadratic-certificate limits, and genuine inverse-pole and delay costs.
The [v1 selected decision](Yin_C_G0461_v1.md#decision-complete-whole-self-adoption) adopts them through the actual [R667 whole self-review](../audits/reviews/Yin_R_G0667_v1.md#blaschke-budget-whole-self-finding).
That relationship is SELF, not independent, and neither it nor the older R123 supplies independent review of the new theorem below.
The new proof uses only v1's exact direct-function identification, total squared mass exp(2m)-1, and coefficient bound 2sinh(m); its algebraic integrality, orbit identities, pole classification, finite Galois-energy bound and coefficient-norm costs are proved here.
The original [GMR18 passage account](../audits/literature/GMR18/Yin_U001.md#gmr18-u001) remains the existing arXiv v2 introductory normalization and printed-page-14 Section 7 derivative-formula scope, not a new source proof or PDF inspection.
No other v1 result is needed as a premise of the new Galois conclusions.

## Statement

Let P be the actual monic irreducible reciprocal minimal polynomial of a nontorsion algebraic integer unit, of original degree d=2h and total logarithmic Mahler measure m>0.
Let L be its splitting field with chosen embedding into C, let G=Gal(L/Q), let S be its set of exterior roots, and put r=|S|, so 1<=r<=h.
For A in the distinct Galois orbit O of S, define

    R_A(z)=product_(a in A)(1-a*z)/(1-a^(-1)*z),
    R_S(z)=1+sum_(j>=1)c_j*z^j,
    b=|O|, F=Q(c_1,c_2,...).                           (S1)

All roots and inverse pairs are those of the same original P; roots on the unit circle are permitted.
The conclusions are as follows.

1. Every c_j is an algebraic integer in L.
   The field F is the fixed field of the set stabilizer of S, so [F:Q]=b, and every original root occurs in exactly t=br/d orbit subsets, where t is a positive integer.
   The exact rational-function norm is

       N_(F(z)/Q(z))(R_S)=product_(A in O)R_A(z)=1.
                                                               (S2)

   The sum over G of every coefficient of the formal series log R_S is therefore zero.
2. R_S is the unique distinct orbit member with square-summable Taylor coefficients.
   It is analytic on a neighborhood of the closed disk and satisfies the reused original budget

       sum_(j>=1)|c_j|^2=exp(2m)-1,
       |c_j|<=2sinh(m).                                (S3)

   Every A!=S has a genuine pole on or inside the unit circle, and some orbit member has a pole strictly inside.
   Uniqueness concerns orbit members, equivalently embeddings of F, not Galois automorphisms of L: several automorphisms may stabilize S.
3. For every integer N>=1,

       (1/|G|)sum_(sigma in G)sum_(j=1)^N|sigma(c_j)|^2
         >=floor(N/r).                                (S4)

   This is a splitting-field average and is not an original-field degree-d norm or a complementary coefficient-covariance statement.
4. The first nonzero c_q has 1<=q<=r and Tr_(L/Q)(c_q)=0.
   With delta=[Q(c_q):Q] one has

       c_q=(-1)^q(e_q(S)-e_q(S^(-1))),
       2<=delta<=b<=2^r*binom(h,r),
       1<=2sinh(m)*[2*binom(r,q)*exp(m)]^(delta-1).       (S5)

   Here e_q is the elementary symmetric polynomial of degree q.
   In particular, for 0<m<=1,

       m >= [2*sinh(1)*(2*exp(1)*binom(r,q))^(delta-1)]^(-1).
                                                               (S6)

The complete old v1 theorem remains available at its original wider domain and actual self-review scope.
The new statements show that the original small Hardy budget does not survive the other coefficient-field embeddings, while norming the whole rational function cancels identically.
The coefficient estimate retains an uncontrolled actual field degree and binomial cost; it supplies no degree-independent positive Mahler gap, short binary auxiliary, original-law rate gain or near-zero example.
It excludes neither a different paid integral combination nor any other method for the unrestricted Task.

<a id="argument"></a>
## Complete argument

### 1. Actual integrality and genuine pole sets

Irreducibility in characteristic zero makes the original roots distinct.
Reciprocity and the nontorsion hypothesis exclude roots 1 and -1, so the original roots form h disjoint inverse pairs.
There are r exterior roots and r interior roots, with 1<=r<=h.
Thus S and S^(-1) are disjoint.
Complex conjugation preserves S, so

    R_S(z)=N_S(z)/D_S(z)
          =product_(a in S)(1-a*z)/(1-a^(-1)*z)
          =1+sum_(j>=1)c_j*z^j                         (1)

has real coefficients and is exactly v1's direct function, whose denominator there uses the conjugated inverses of S.
Conjugation permutes S, so those denominator products agree.
The original budget S3 is therefore the direct application of [v1's exact statement](Yin_C_G0461_v1.md#statement), with the original total m and all exterior conjugates retained.

Every root and its inverse is an algebraic integer because the original number is a unit.
The coefficients of N_S and D_S are consequently integral in L, and D_S(0)=1.
Formal division, or its coefficient recurrence, proves c_j in O_L for every j.
This uses neither rationality of c_j nor containment in Q(alpha).

For each sigma in G, taking inverses commutes with sigma and gives

    sigma(R_S)=R_(sigma(S)).                            (2)

Each image A and A^(-1) remain disjoint.
The denominator zeros of R_A are the roots a in A; its numerator zeros are the roots a^(-1) with a in A.
They never cancel, and all these poles are simple.

### 2. Full orbit incidence and exact norm cancellation

Every original root occurs in the same number t of sets in O.
Indeed a Galois automorphism sending one root to another bijects the sets containing them, and such an automorphism exists by irreducibility.
Every original root occurs in at least one set, since S is nonempty and the action on roots is transitive.
Counting incidences gives

    dt=br,
    t=br/d in Z_(>0),
    b>=d/r>=2.                                        (3)

It follows that

    product_(A in O)R_A(z)
      =[product_(P(a)=0)(1-a*z)
        /product_(P(a)=0)(1-a^(-1)*z)]^t
      =1.                                              (4)

The last equality uses inversion as a permutation of all d original roots.
No conjugate, leading-coefficient term or normalization by the original degree has been removed.

The stabilizer of R_S equals the set stabilizer of S, since its reduced denominator has constant coefficient 1 and precisely S as its simple pole set.
An automorphism fixes every c_j if and only if it fixes the formal series R_S, equivalently its rational function.
Thus Gal(L/F) is this same stabilizer, and the Galois correspondence gives [F:Q]=b.
The distinct embeddings of F give exactly the orbit functions in (4), so (4) is S2.
Multiplying over all sigma in G gives the same identity with a common positive multiplicity.
Taking formal logarithms in 1+zL[[z]] now shows that the sum over G of each coefficient of log R_S is zero.
The use of a formal logarithm does not claim an analytic logarithm across the actual numerator zeros.

### 3. The unique orbit member with a finite Hardy budget

All poles of R_S lie strictly outside the closed disk, so it is analytic on a neighborhood of that disk.
If A!=S, then A cannot consist entirely of exterior roots: A and S both contain r roots, and S contains all r exterior roots of P.
Hence A contains a root a with |a|<=1, and Section 1 proves that this root is a genuine pole of R_A.

If R_A has a pole strictly inside the disk, its Taylor radius is below 1, whereas a square-summable coefficient sequence has Taylor radius at least 1.
Thus its coefficients are not square summable.
If its poles all have modulus at least 1 and some pole a lies on the circle, square summability would give the uniform radial bound

    integral_T |R_A(rho*z)|^2
      <=sum_(j>=0)|[z^j]R_A|^2<infinity,
    0<rho<1.                                          (5)

Here the integral is Haar probability on the unit circle, and (5) follows by integrating the squared Taylor series at radius rho.
Near the simple genuine pole a, write

    R_A(z)=v/(z-a)+H(z),  v!=0,

where H is bounded on a fixed neighborhood of a.
For |theta-arg(a)|<=1-rho and rho sufficiently close to 1, the distance |rho*exp(i*theta)-a| is at most 2(1-rho).
The pole term therefore dominates H and gives a lower bound by a positive constant times (1-rho)^(-2) for |R_A(rho*exp(i*theta))|^2 on that arc.
The arc has length 2(1-rho), so its integral tends to infinity at least as a positive constant times (1-rho)^(-1), contradicting (5).
This proves non-square-summability also in the circle-pole case.

Consequently exactly one distinct orbit member, R_S, retains finite coefficient energy.
This statement does not identify a unique sigma in G: all automorphisms in the stabilizer of S give R_S.
Finally, transitivity sends a fixed exterior root to an interior root, so at least one orbit member has a pole strictly inside the disk.
All conclusions apply to the same original irreducible unit, including any hypothetical such input with arbitrarily small positive total m.

### 4. The finite all-embedding energy lower bound

If c_j!=0, its norm from L to Q is a nonzero integer.
The arithmetic-geometric mean inequality for the positive numbers |sigma(c_j)|^2 gives

    (1/|G|)sum_(sigma in G)|sigma(c_j)|^2
      >=|N_(L/Q)(c_j)|^(2/|G|)>=1.                    (6)

No r consecutive positive-index c_j can all be zero.
In fact D_S has degree r and constant coefficient 1, while N_S has degree r.
Its coefficient recurrence is homogeneous at every index greater than r.
If a block c_k,...,c_(k+r-1) vanished with k>=1, the recurrence at k+r and all subsequent indices would force every later coefficient to vanish.
Then R_S would be a polynomial, contradicting its nonempty genuine pole set.
Among every r consecutive positive indices there is therefore at least one nonzero coefficient.
Partitioning the first N indices into disjoint blocks of length r and summing (6) proves S4.
At N=r this average is at least 1, while the original embedding has total nonconstant energy exp(2m)-1.
The two quantities have different embedding domains; no contradiction or uniform gap follows by identifying them.

### 5. The first coefficient and every field-degree cost

There is a first nonzero coefficient c_q with 1<=q<=r, either by the preceding block argument or by comparing all coefficients of N_S and D_S.
At degree q in D_S R_S=N_S, all previous positive coefficients vanish, so

    c_q=(-1)^q(e_q(S)-e_q(S^(-1))).                    (7)

The degree-q coefficient of the formal logarithm equals c_q.
Section 2 therefore gives Tr_(L/Q)(c_q)=0.
Since c_q is nonzero, it cannot be rational, and delta=[Q(c_q):Q]>=2.

At each embedding, (7) holds with S replaced by an orbit subset A.
The product of any q distinct original roots has modulus at most exp(m): the sum of their positive radial logarithms is bounded by the original total m.
The inverse product has the same bound, since for a unit the total negative radial logarithm also equals m.
Each elementary symmetric polynomial in (7) has binom(r,q) such terms, giving

    |sigma(c_q)|<=B,
    B=2*binom(r,q)*exp(m).                             (8)

Every embedding of Q(c_q) extends to L, so (8) bounds all delta conjugates of c_q.
Its norm from Q(c_q) to Q is a nonzero integer.
Use S3 at the distinguished conjugate and (8) at the other delta-1 conjugates to obtain

    1<=|N_(Q(c_q)/Q)(c_q)|
      <=2sinh(m)*[2*binom(r,q)*exp(m)]^(delta-1).        (9)

The coefficient field is a subfield of F, so delta<=b.
Each orbit subset contains at most one root from each original inverse pair and exactly r roots in total.
Choosing the r pairs and then one root in each gives

    delta<=b<=2^r*binom(h,r).                          (10)

These are bounds on the actual degrees, not assertions that they are attained or equal to the original d.
For 0<m<=1, convexity gives sinh(m)<=m*sinh(1) and exp(m)<=exp(1).
Substituting these upper bounds into (9) proves S6.
The exponent delta-1 and the binomial factor remain uncontrolled as d varies; no positive degree-independent lower bound has been deduced.
In particular c_q need not belong to Q(alpha), so a norm of degree d is not available without another containment proof.

## Reuse, source and scope boundaries

The targeted reuse screen read v1's actual exterior-factor definition, exact small-energy and finite-lag budgets, coefficient recurrence and distinct analytic-control boundary.
The neighboring [C296 endpoint statement](Yin_C_G0296_v1.md#statement), [C445 direct-limit statement](Yin_C_G0445_v1.md#statement), [L268 inverse-amplification scope](../ledger/Yin_L_G0268_v1.md#inverse-compression-fixed-scope), and [GMR18's exact inspected passage](../audits/literature/GMR18/Yin_U001.md#gmr18-u001) were checked at their actual analytic and source scopes.
A focused text search in those materials and L263/L264 for Galois action, conjugate coefficients, splitting fields and factor norms found no prior statement of the orbit-norm identity or unique finite-energy orbit member; this is a bounded reuse finding, not a novelty assertion.
The screen also inspected [C214's original inverse-trace theorem](Yin_C_G0214_v1.md#statement), [C16's integer-residue moment domain](Yin_C_G0016_v1.md#statement), and [C145's original dense-kernel obstruction](Yin_C_G0145_v1.md#all-root-radial-kernel-contact); none is a premise of the new proof.
A bounded primary-oriented search on 2026-11-04 used Mahler measure, Galois conjugates, exterior roots, algebraic-integral coefficients and Blaschke factors.
The returned general Mahler/Galois source descriptions supplied no theorem used here; no original proof or new external input is asserted inspected from those descriptions.
The sole retained analytic premise is the exact v1 interface specified in Inputs, with its actual self-review and source limits.
All new algebraic counting, integrality, recurrence, norm and circle-pole arguments are contained in this fixed file; no rolling draft is a proof premise.

The responsible contributor supplied the new theorem and its complete argument, and the coordinating agent checked the draft as a contributor.
Those contributor checks establish no independent review; the separate [selected assessment](#decision-whole-independent-review-2026-11-04) now adopts the exact finding of R667 v2.
No numerical computation or native program is used.
The obstruction concerns transferring the same exterior-factor Hardy budget to all embeddings, or seeking positive income from its full rational-function norm.
It does not exclude a different integral combination of orbit functions, a genuinely paid coefficient estimate or a direct original-field auxiliary.
Any such application still owes its actual field degree, conjugate poles and numerator values, denominator clearing, original span and probability-law costs where applicable.

## Current assessment
[Selected decision](#decision-whole-independent-review-2026-11-04)

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T19:50 |
| status | proved |
| reason | Adopt the complete new Galois theorem after independent R667 v2: the actual exterior-factor function has norm one over its coefficient field, exactly one square-summable orbit member, a finite all-embedding energy floor and the stated nonuniform first-coefficient norm cost. The wider v1 analytic theorem retains its original SELF assessment and all source limits. No unrestricted Mahler gap or auxiliary supply is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact new statement](#statement) | All S1--S6 on actual irreducible reciprocal nontorsion units, including neutral roots, true coefficient/orbit fields, uniqueness, finite energy and actual degree costs. |
| argument | [Complete argument](#argument) | All five sections: integral coefficients, genuine poles, orbit incidence and norm, Hardy failure, recurrence blocks and nonuniform coefficient-norm bounds. |
| dependency | [Adopted v1 budget](Yin_C_G0461_v1.md#decision-complete-whole-self-adoption) | Exact direct-factor identification, total energy exp(2m)-1 and coefficient bound 2sinh(m); the wider retained v1 theorem and its SELF/source limits remain unchanged. |
| review | [Independent Galois finding](../audits/reviews/Yin_R_G0667_v2.md#galois-orbit-energy-independent-finding) | Complete new theorem and argument plus exact accepted-input interface, without reclassifying the old SELF review or claiming a new source-proof audit. |
