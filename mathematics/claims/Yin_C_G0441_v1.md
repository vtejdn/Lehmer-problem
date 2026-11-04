---
author: Yin
---

# Complete rational weighted delay factorization, orbit criterion and fixed-pole barriers

This retains the complete necessary mathematical argument from [the complete original G380 account](../ledger/Yin_L_G0380_v1.md).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Use rational coefficients throughout, H=diag(1,2), R=Q[t,t^-1], L=Q(t), a*=a(t^-1) and U^sharp=U(t^-1)^T.
For every r=(a,b)^T in Q^2 minus0, put

    Pi_r=[[a^2,2ab],[ab,2b^2]]/(a^2+2b^2),
    E_r=I-Pi_r+t Pi_r.

The denominator is positive, Pi_r is H-selfadjoint/idempotent, E_r^sharp H E_r=H, E_r^-1=I-Pi_r+t^-1 Pi_r and det E_r=t.
Every v in R^2 with v^sharp H v=1 has an exact rational factorization

    v=t^m E_(r_1)...E_(r_N)c,
    m in Z, c in Q^2, c^T H c=1.

If the actual union support is normalized to[0,T], one may take N<=T.
Conversely every such finite product has norm1 and union width at most N; length/width/McMillan degree are not identified.
Every constant column is c=((a^2-2b^2)/(a^2+2b^2),2ab/(a^2+2b^2)), including(-1,0), and C_c=[[x,-2y],[y,x]] gives a rational square completion.

Let S be the odd primes p for which-2 is a square in F_p and A=Z[S^-1].
All projection, factor, inverse-factor, constant-column and C_c coefficients lie in A, by primitive integer scaling, cancellation of the only factor2 and odd-prime anisotropy.
An actual resulting least denominator q divides q_c product delta_i for any chosen clearing factors; equality, realization of every admissible q and uniform word/q bounds are not asserted.

For the ORIGINAL irreducible reciprocal quartic P=t^4-2t^3+t^2-2t+1, let K=Q[t]/(P), alpha=t modP, tau=alpha+alpha^-1, sigma(alpha)=alpha^-1 and u=(tau,(1-alpha)^-1)^T.
It satisfies sigma(u)^T H u=1 with full signed unit norms+1,-1.
For Gamma generated as a finite-word subgroup by O_H(Q)={C:C^T H C=H} and all E_r(alpha), an exact Laurent norm-one v with v(alpha)=u exists iff u belongs to Gamma e_1.
Equivalently there are the finite parameters above with u=alpha^m E_(r_1)(alpha)...E_(r_N)(alpha)c.
All equalities are in the actual degree4 field and retain every original conjugate.
A supplied word lifts term by term, including inverses; alpha I is the product of coordinate delays.
The exact identities E_r^-1=t^-1 E_(-2b,a), C E_r C^-1=E_(Cr) normalize inverses/constants and give width at most the displayed elementary-factor count, without bounding an unknown word.
Arbitrary signed independent component twists are equivalent to untwisted existence at unrestricted width and unchanged scalar denominator; their union widths can change.
No equality Gamma=U_H(K,sigma), rational density argument, arbitrary-target surjectivity or finite-width case collapse is used.

For the fixed rational-function comparison v_rat=(A/D,B/D)^T, retain exactly

    D=t^4-8t^3+15t^2-8t+1,
    A=-t^4+4t^3-7t^2+4t-1,
    B=-2t^3+8t^2-8t+2.

It has norm1 and residue u, gcd(A,D)=1, four distinct nonzero reciprocal positive poles from traces4+/-sqrt3, no circle poles and full original resultants64,+64,-64.
No square Laurent U with U^sharp H U=H makes U v_rat Laurent, because its inverse H^-1 U^sharp H is Laurent.
No common scalar s in Q(t) with ss*=1 makes s v_rat Laurent, even composed with such a U: each reciprocal pole pair would require two positive orders contradicting the all-pass order sum0.
These all-degree impossibilities concern this fixed vector and leave different congruent Laurent interpolants possible.

For every rational norm-one column v=(f,g), the exact completion M_v=[[f,-2g*],[g,f*]] has determinant1, M_v^sharp H M_v=H and M_v e_1=v.
A rational weighted paraunitary W regular at all original roots with W(alpha)=I and W v_rat Laurent exists iff there is a Laurent norm-one interpolant of u.
Given one w, W=M_w M_(v_rat)^-1 proves the reverse implication with all starred residues and regularity retained.
The rational inverse alone changes u to e_1 and does not solve interpolation.

For any successful word, compute its actual least common q and common Laurent normalization before applying the original q>=3, full signed resultants+q^4,-q^4 and FF*+2GG*=q^2.
Weights1/3,2/3 give integer energy q^2/3 and preliminary surplus log3/2, while actual width/radial/degree, individual content and denominator costs remain paid.
No constant covariance transfers automatically to least-energy residuals.
The three J85 degree4 certificate absences are historical bounded evidence, not premises of the arbitrary-degree proofs or nonlinear impossibility.
AJL17/AJL16 supply only exact selected complex attribution; rational descent, original Potapov/completion proofs, interpolation and McMillan-width equality are not imported.
No program, native search, solver or new source reading occurs.
The original dated orbit question was open at its 2026-10-11T14:43 freeze; the later separate [L384 exact finite word](Yin_C_G0453_v1.md#exact-width-five-lift-discovery) supplies the specific target's solution.
That later result does not remove the fixed-vector pole obstruction or settle general orbit surjectivity, residual covariance or the unrestricted Task.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:08 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Full original quartic/unit and denominator domain](Yin_C_G0430_v1.md#paraunitary-lift-reuse-and-domain) | Only exact original all-root unit residues/signs, independent-twist/leastq restrictions and fixed rational comparison with its full gcd/poles/norms/costs; no J85 nonlinear inference. |
| support | [Complex FIR attribution](../audits/literature/AJL17/Yin_U001.md#ajl17-u001) | Only original v2/2014 selected Theorem3.5/eq3.10–3.13 statement/displayedargument/cancellation attribution; no rational descent or theorem premise. |
| support | [Complex rational-factor comparison](../audits/literature/AJL16/Yin_U001.md#ajl16-u001) | Only original v2/2015 Theorem3.1/eq3.2–3.5 selected attribution and genuine finite-pole distinction, not original Potapov/completion proof or interpolation. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:12 |
| status | proved |
| reason | Adopt the actual complete SELF check of every rational projection/factor/prime/orbit/pole/correction proof, all original whole/source and expense limits. Preserve dated original target status separately from its later exact solution, all original SELF and source occurrences, and no native/source-proof or Task/E expansion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0430_v1.md#paraunitary-lift-reuse-and-domain) | Only exact original all-root unit residues/signs, independent-twist/leastq restrictions and fixed rational comparison with its full gcd/poles/norms/costs; no J85 nonlinear inference. |
| support | [Exact support](../audits/literature/AJL17/Yin_U001.md#ajl17-u001) | Only original v2/2014 selected Theorem3.5/eq3.10–3.13 statement/displayedargument/cancellation attribution; no rational descent or theorem premise. |
| support | [Exact support](../audits/literature/AJL16/Yin_U001.md#ajl16-u001) | Only original v2/2015 Theorem3.1/eq3.2–3.5 selected attribution and genuine finite-pole distinction, not original Potapov/completion proof or interpolation. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0644_v1.md#current-rational-delay-whole-finding) | Entire exact Statement and Argument, all original five theorems/equivalences, full old whole/author/source scope, all original costs and useful boundaries. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="complete-rational-delay-factorization"></a>
The original dated proofs below retain their actual 2026-10-11T14:43 scope and then-open target language.
The separate later [L384 exact word](Yin_C_G0453_v1.md#exact-width-five-lift-discovery) records that target's subsequent solution; it supplies no premise to the general factorization, prime or fixed-vector pole proofs here.

<a id="rational-factorization-source-and-input"></a>
## 1. Fixed input, reuse and source boundary

The original frozen construction and its completed review are now retained in [L377](../ledger/Yin_L_G0377_v1.md#explicit-rational-function-norm-lift).
Its all-width scalar-denominator restrictions, width-at-most-four exclusion, exact original units and rational-function costs are reused at their stated scope.
[J85](../computations/programs/Yin_J_G0085/readme.md) establishes only absence of three degree-four product-span certificates; no nonlinear feasibility or arbitrary-degree assertion is imported.

The precise new need is a factorization over Q for the weighted form H=diag(1,2), together with an exact criterion for preserving an original algebraic quotient under that factorization.
A bounded local search of D/L and the literature bibliography/registry by paraunitary, delay projection, Potapov, FIR and factorization found L377's related real-FIR lead, but no retained input covering this coefficient-field/interpolation question.
No source-wide negative conclusion or novelty claim follows.

The standard complex FIR factorization is identified in Daniel Alpay, Palle Jorgensen and Izchak Lewkowicz, [Characterizations of Families of Rectangular, Finite Impulse Response, Para-Unitary Systems](https://arxiv.org/pdf/1410.0280), arXiv:1410.0280v2, dated 16 November 2014, Section 3.2, Theorem 3.5, equations (3.10)--(3.13), printed/PDF pp.12--13.
The actual statement, hypotheses, displayed specialization argument and cancellation warning were read.
It uses complex orthogonal rank-one projections and a constant isometry, and specializes poles to zero and infinity.
Its general rational predecessor, [Characterizations of Rectangular (Para)-Unitary Rational Functions](https://arxiv.org/pdf/1410.0283), arXiv:1410.0283v2, dated 4 January 2015, Section 3, Theorem 3.1, equations (3.2)--(3.5), pp.10--11, was read for the exact rational-versus-FIR distinction.
That proof invokes earlier Potapov and completion results, which were not recursively audited.

These sources supply checked attribution and a related complex formulation, not an adopted rational-field or prescribed-interpolation theorem.
No rationality descent from complex normalized vectors, McMillan-degree identity with our union width, rational spectral factorization or strong approximation is assumed.
The weighted rational version and the interpolation/pole conclusions below have complete direct proofs.
A source read is not a full-paper audit.
The earlier Caltech 1989 lossless tutorial and 1988 synthesis article were located, but PDF fetches failed; no uninspected theorem from them is used.
The search stopped when the exact classical factor form and its actual limitations had been identified.

Canonical source navigation, added without changing the above inspected versions or mathematical freeze: [AJL17-U001](../audits/literature/AJL17/Yin_U001.md#ajl17-u001) and [AJL16-U001](../audits/literature/AJL16/Yin_U001.md#ajl16-u001).
Their journal years2017 and2016 are distinct from the actual retained preprint dates above.

Fix throughout the ORIGINAL data

    P=t^4-2t^3+t^2-2t+1,
    K=Q[t]/(P), alpha=t mod P, tau=alpha+alpha^-1,
    sigma(alpha)=alpha^-1, H=diag(1,2),
    u=(tau,(1-alpha)^-1)^T,
    sigma(u)^T H u=tau^2+2(-tau)=1.                 (1)

L377 supplies irreducibility, the full real/circle root configuration and full unit norms +1,-1.
Let R=Q[t,t^-1] and L=Q(t).
For a scalar a put a*=a(t^-1); for a matrix U put U^sharp=U(t^-1)^T.
A norm-one column is v=(f,g)^T with v^sharp H v=1.
A square weighted paraunitary matrix means, by definition, U^sharp H U=H.
These definitions are exact rational identities; positivity of H over the real rationals will be used explicitly.

<a id="rational-weighted-delay-factorization"></a>
## 2. Complete rational factorization of an existing Laurent norm-one column

For r=(a,b)^T in Q^2 minus {0}, define the H-orthogonal projection and elementary factor

    Pi_r = r(r^T H)/(r^T H r)
         = [[a^2,2ab],[ab,2b^2]]/(a^2+2b^2),
    E_r(t)=I-Pi_r+t Pi_r.                          (2)

The denominator is positive, so the definition introduces no square root or field extension.
Direct multiplication gives

    Pi_r^2=Pi_r, Pi_r^T H=H Pi_r,
    E_r(t)^sharp H E_r(t)=H,
    E_r(t)^-1=I-Pi_r+t^-1 Pi_r, det E_r(t)=t.       (3)

**Theorem 1.** Every v in R^2 satisfying v^sharp H v=1 has an exact factorization

    v(t)=t^m E_{r_1}(t)...E_{r_N}(t)c,
    m in Z, r_i in Q^2 minus {0},
    c in Q^2, c^T H c=1.                           (4)

After normalizing the actual union support to [0,T], one may take N<=T.
Conversely every expression (4) is a rational Laurent norm-one column.
Its actual union width is at most N, but factor length need not equal width.

*Proof.* Choose m as the smallest exponent appearing in either component and write v=t^m w with w=sum_{j=0}^T w_j t^j.
The scalar monomial has norm one, so w^sharp H w=1.
If T=0 take c=w_0.
Otherwise w_T is a nonzero rational vector and the coefficient of t^T in w^sharp H w is w_0^T H w_T=0.
Put r=w_T and

    w'=E_r(t)^-1 w=(I-Pi_r)w+t^-1 Pi_r w.         (5)

The possible negative coefficient is Pi_r w_0=0 by that extreme-lag orthogonality.
The possible degree-T coefficient is (I-Pi_r)w_T=0.
Thus w' is an ordinary rational polynomial of degree at most T-1.
It remains norm one by (3), and in particular is not zero.
Iterate; degree decreases at every nonconstant step, and a constant rational norm-one column is reached after at most T steps.
Reversing the steps proves (4).
Conversely each factor preserves the weighted norm and a product of N degree-one polynomial matrices has degree at most N.
A common monomial does not enlarge the union width.
This proves both directions, including zero endpoint coefficients at intermediate steps.
No completion theorem is needed.

For explicit rational parameters every constant column is

    c(a,b)=((a^2-2b^2)/(a^2+2b^2),
                   2ab/(a^2+2b^2))^T,
    (a,b) in Q^2 minus {0}.                        (6)

Indeed for c=(x,y) with x^2+2y^2=1 and x not -1, the rational slope y/(1+x) gives this formula; x=-1 forces y=0 and is the case a=0.
The constant matrix

    C_c=[[x,-2y],[y,x]]                            (7)

satisfies C_c^T H C_c=H, det C_c=1 and C_c e_1=c.
Hence the column factorization also supplies a square Laurent paraunitary completion explicitly.
Formula (4) is a construction from its rational parameters; it does not say those parameters achieve any prescribed quotient residue.

<a id="factor-denominator-prime-preservation"></a>
## 3. The same scalar-denominator restrictions hold factor by factor

Let S be the set of odd primes p for which -2 is a square in F_p, and let A=Z[S^-1], the rational numbers whose reduced denominator uses only primes in S.

**Theorem 2.** Every entry of Pi_r and E_r(t) has its scalar denominator in A, as does every constant norm-one column c and matrix C_c in (6)--(7).
Consequently the factorization (4) may be carried out entirely in A[t,t^-1]; it automatically preserves the forbidden-prime restriction of L377.

*Proof.* Scaling r does not change Pi_r, so take a,b to be relatively prime integers.
If a is odd, s=a^2+2b^2 is odd.
If a is even, b is odd and s has exactly one factor 2; all four numerator entries in (2) are even, so this factor cancels.
If an odd nonsquare-(-2) prime divided s, anisotropy would force both a and b divisible by p, impossible.
Thus every reduced denominator of Pi_r is odd and supported on S.
The same conclusions hold for I-Pi_r.

For (6), again take relatively prime integers a,b.
The same odd-prime argument applies to s.
In the even-a case both a^2-2b^2 and 2ab are even, so the sole factor 2 in s cancels.
Formula (7) adds no denominators.
Products and inverses in (3) therefore introduce no forbidden primes.
This completes the claim without using a classification of represented primes or any algebraic-number-theoretic factorization theorem.

More precisely, if delta_i clears the entries of Pi_{r_i}, and q_c clears c, then the actual least common denominator q of the resulting pair in (4) divides q_c times product_i delta_i.
Cancellation can reduce q; one must calculate its actual value before an energy/norm inference.
This formula is neither a uniform upper bound independent of the word nor a proof that every admissible q occurs.
For an exact original-unit interpolant, L377 still forces q>=3 and the full original resultants +q^4,-q^4.
The factorization does not assign those unit resultants to arbitrary intermediate columns.

<a id="finite-word-exact-interpolation-criterion"></a>
## 4. The precise quotient interpolation criterion

Let O_H(Q)={C in GL_2(Q): C^T H C=H}.
In K put

    Gamma=< O_H(Q), E_r(alpha) : r in Q^2 minus {0} >,
    U_H(K,sigma)={M in GL_2(K): sigma(M)^T H M=H}.
                                                               (8)

The angle brackets mean the subgroup generated by finite words, with inverses allowed.
Since sigma(alpha)=alpha^-1, every generator lies in U_H(K,sigma).
Evaluation at alpha is a ring map R to K and is defined also for each factor's rational scalar denominator.

**Theorem 3.** There exists a rational Laurent pair with exact weighted norm one and the original untwisted residues v(alpha)=u if and only if

    u belongs to Gamma e_1.                        (9)

An explicit word giving (9) constructs the full Laurent pair by replacing alpha by t in exactly that word.
Equivalently, there exist m,N,r_1,...,r_N,c as in (4) with

    u=alpha^m E_{r_1}(alpha)...E_{r_N}(alpha)c.      (10)

This is equality in the actual degree-four field, not just at a selected real or circle embedding.

*Proof.* The forward implication follows from Theorem 1 and C_c e_1=c.
The scalar matrix alpha I belongs to Gamma because E_{e_1}(alpha)E_{e_2}(alpha)=alpha I.
Thus every factor in the evaluation of (4) belongs to Gamma.
Conversely a finite word in the displayed generators has a Laurent paraunitary lift: use the corresponding rational constant C, E_r(t) or the explicit inverse in (3).
Apply it to e_1.
Its norm is identically one and its residue is exactly the stated word.
This proves (9).
Applying Theorem 1 to that constructed column proves the equivalence with (10).

One can also normalize inverse factors without an existence theorem.
If r=(a,b), choose r_perp=(-2b,a); then Pi_{r_perp}=I-Pi_r and

    E_r(t)^-1=t^-1 E_{r_perp}(t).                  (11)

Constants can be moved past factors by C E_r(t) C^-1=E_{Cr}(t).
Hence a finite word with M elementary factors and arbitrary rational orthogonal constants gives a common monomial times a product of M positive elementary factors and one constant column; its actual width is at most M.
This is a finite verifiable construction certificate when a word is supplied, not a bound on the unknown word length.

For stepwise exact algebra the generator action in K is

    w maps to w+(alpha-1) r(r^T H w)/(r^T H r).     (12)

Every value can be reduced in the basis 1,alpha,alpha^2,alpha^3 using P.
Thus a proposed rational word has finitely checkable exact interpolation obligations, while norm preservation is built into the factors.
No word or parameter scan has been run here.

There is a useful distinction from bounded-width testing.
For arbitrary Laurent width, existence with ANY signed independent twist

    (epsilon alpha^k tau, eta alpha^l/(1-alpha))    (13)

is equivalent to untwisted existence: multiply the two components independently by epsilon t^-k and eta t^-l, or reverse that operation.
This preserves their individual Laurent norms and common scalar denominator.
It can change the common union width, so it does not collapse the distinct width-five cases of J85.
In (8), the same fact follows because diagonal signs belong to O_H(Q), and diag(alpha,1), diag(1,alpha) are the coordinate factors.
Thus arbitrary-degree existence has one orbit target u; no finite-width inference is smuggled into this simplification.

The missing condition is exact orbit membership (9).
Neither density of rational parameters, the existence of the rational-function lift, the generic complex factorization nor the degree-four certificate absences establishes it.
No claim is made that Gamma equals U_H(K,sigma), or that its orbit is all norm-one vectors.
Such a claim would require a new arithmetic argument, not a relabeling of the factorization theorem.

<a id="genuine-poles-survive-laurent-paraunitary-correction"></a>
## 5. Structural impossibility of clearing the known poles by finite Laurent factors

The fixed L377 comparison vector is v_rat=(A/D,B/D)^T, where

    D=t^4-8t^3+15t^2-8t+1,
    A=-t^4+4t^3-7t^2+4t-1,
    B=-2t^3+8t^2-8t+2.                            (14)

Its exact norm is one and v_rat(alpha)=u, but gcd(A,D)=1.
D has four nonzero positive roots in two reciprocal pairs, from trace values 4 plus/minus sqrt(3), and has no circle root.
The full original resultants remain Res(P,D)=64, Res(P,A)=+64, Res(P,B)=-64.

**Theorem 4.** No square U in M_2(R) satisfying U^sharp H U=H makes U v_rat belong to R^2.
In particular no finite composition of rational orthogonal constants, monomial delays and rational Laurent paraunitary factors converts this existing rational-function lift into a Laurent lift, whether or not it preserves the quotient residue.

*Proof.* The displayed identity gives the left inverse H^-1 U^sharp H over the fraction field.
A square left inverse is the inverse, and all its entries lie in R.
Thus U v_rat in R^2 would imply v_rat=U^-1(U v_rat) in R^2.
This contradicts the genuine finite nonzero poles of A/D.
Equivalently, at any nonzero finite point U and U^-1 are regular, so they cannot eliminate a nonzero principal part of a vector.
There is no degree bound in this obstruction.

**Theorem 5.** A common scalar rational all-pass correction cannot do so either: there is no s in Q(t) with ss*=1 and s v_rat in R^2.

*Proof.* Since gcd(A,D)=1, at every root rho of D the function A/D has a pole.
For s A/D to be Laurent, s must have positive vanishing order at rho.
The reciprocal rho^-1 is also a root of D, so it too requires positive vanishing order.
But ord_rho(ss*)=ord_rho(s)+ord_(rho^-1)(s)=0, a contradiction.
All roots are nonzero, so inversion is a local isomorphism and preserves these orders.
This remains true if one also composes with any Laurent paraunitary U, since its Laurent inverse first reduces to the same scalar case.
No circle or original conjugate pole has been silently discarded.

These results exclude two concrete repair mechanisms at every degree.
They do not exclude a different Laurent norm-one vector congruent to v_rat modulo P.
Theorem 1 factors an ALREADY Laurent vector.
Applying the complex rational Blaschke-Potapov theorem to v_rat instead permits genuine finite poles in its factors; it does not transform those factors into delays or preserve rational coefficients and quotient values automatically.

<a id="rational-matrix-correction-is-the-same-interpolation-obligation"></a>
## 6. What a genuinely rational matrix correction would have to prove

For any rational norm-one column v=(f,g)^T define

    M_v=[[f,-2g*],[g,f*]],
    M_v^sharp H M_v=H, det M_v=ff*+2gg*=1,
    M_v e_1=v.                                    (15)

These are direct two-by-two identities over Q(t).
In particular M_(v_rat)^-1 does send v_rat to e_1 using a rational paraunitary matrix.
It changes the original residue from u to e_1, so it does not solve interpolation.

There exists a rational paraunitary W, regular at every original root, with

    W(alpha)=I and W v_rat in R^2                  (16)

if and only if the original Laurent interpolation problem is solvable.
One implication follows immediately by evaluation and preservation of norm.
For the other, let w be such a Laurent interpolant and set W=M_w M_(v_rat)^-1.
Both matrices are regular at the original roots because D is coprime to P and P is reciprocal; their evaluations agree by w(alpha)=v_rat(alpha), including starred entries.
Therefore W(alpha)=I, and W v_rat=w.
This proves the equivalence without a matrix completion or approximation theorem.

Consequently allowing genuine rational matrix factors removes the simple pole invariant, but exact residue-preserving cancellation is precisely the original unresolved interpolation obligation.
An unrestricted rational factorization is not a construction of (16).
The finite-word criterion (9) supplies a separate exact way to settle that obligation if a word or an orbit obstruction is established.

<a id="structural-factorization-costs-and-next-gate"></a>
## 7. Complete original costs and the discriminating next gate

Any word actually meeting (10) produces rational Laurent f,g with the exact original full norms +1,-1.
After their actual common scalar denominator q and common Laurent normalization are computed, the integral pair F=qf,G=qg has full resultants +q^4,-q^4, exact FF*+2GG*=q^2, and weighted coefficient energy q^2/3.
All original conjugates and individual contents remain.
Its preliminary true surplus is log(3)/2, but the actual union width and the original radial/degree expense still have to be paid.
This factorization supplies no uniform bound on that width or on the word denominators.

The existing rational comparison retains D, its resultants and both exterior poles.
Theorems 4--5 show that finite Laurent factor multiplication and a common scalar all-pass cannot erase that expense.
The criterion does not transfer constant covariance to orthogonal least-energy residuals; the L377 residual-projection gap remains unchanged.

The useful next theoretical question is the exact membership of the original vector u in Gamma e_1, or an invariant separating that vector from the orbit.
A successful explicit word would be a constructive certificate requiring only exact quotient evaluation and final original-cost verification.
A failed finite word search, should one ever be separately authorized, would still not prove nonmembership.
No such search, native mathematical calculation, larger Macaulay system or new J occurred in this round.
The current result is the complete rational parameterization/criterion together with two all-degree obstructions to repairing the specific rational-function lift, not a decision of arbitrary-degree lifting or of G0001.
