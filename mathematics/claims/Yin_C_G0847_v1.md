---
author: Yin
---

# Uniform Mahler gaps for repeated low-energy residue patterns

Human author Yin.
Root proposed the unbounded-period application, orbitwise minimum-energy test and binary family.
Primitive_second_eight checked and assembled the exact periodic identity, monomial reversal, original span and costs, uniform inequality, every orbit minimum and adopted nonvacuity interface.
Both are substantive contributors, not independent reviewers of this proof.
The [current adopted decision](#decision-whole-reviewed-2026-10-28) selects the complete statement and proof with [whole independent R1067](../audits/reviews/Yin_R_G1067_v1.md#whole-unbounded-period-energy-finding).
The OPEN wording retained inside the fixed argument describes its initial author status; the current selection and historical decisions remain distinct.
No native program, seed scan, source acquisition, numerical cutoff or numerical Mahler gap has been computed.

## Statement

### A. Fixed modulus and a q-only phase cutoff

Fix an integer q>=2 and use the exact constants of adopted C845, with the cutoff renamed J(q) so it cannot be confused with the residue period p:

    B_s(q)=q^2+1,
    delta(q)=1/(2q^2 B_s(q)),
    eta(q)=1/(8q^4 B_s(q)^2),
    Delta(q)=delta(q)*eta(q),
    B_ph(q)=4q^2+1,
    J(q)=ceil(B_ph(q)/(eta(q)*Delta(q)^2)).              (ST1)

Retain its exact angular modulus

    c0=log2/4, h0=c0 exp(-20),
    b(v)=max(v,sqrt(v/c0)log sqrt(c0/v)),
    epsilon(v)=min(1,15sqrt(b(v))+4v), 0<v<=h0.

Let u_q be any positive dyadic output of C845's ordered algorithm, so

    J(q)u_q<h0,
    (1+2q/Delta(q))u_q+2^(J(q))epsilon(J(q)u_q)<eta(q),
    (2q^2-1)epsilon(u_q)+4q^2 u_q<1.                   (ST2)

The domain inequality is certified before either epsilon value is used.
These constants are computable from q alone, with J(q)>=1; no numerical execution or useful-size estimate is asserted.

### B. The unbounded-period class and uniform gap

<a id="energy-and-repetition-coefficient-class"></a>
**Definition.** Let p>=1 be any integer and D>=2 be even.
For residues r_0,...,r_(p-1) modulo q, put s=D modulo p and tau(i)=s-i modulo p.
The energy-and-repetition class consists of monic reciprocal irreducible noncyclotomic polynomials

    P=x^D+sum_(j=1..D-1)a_j x^j+1 in Z[x],
    a_j=r_(j mod p) modulo q,
    D>J(q)p,                                          (ST3)

for which there is an integral vector(c_0,...,c_(p-1)) with

    c_i=r_i modulo q,
    c_i=c_(tau(i)) EXACTLY,
    E(c)=1+sum_(j=1..p-1)c_j^2+(c_0-1)^2<=q^2.         (ST4)

The variable p is unbounded and need not be fixed before P varies.
Every residue index occurs among the inner coefficients because D>p, so reciprocity forces r_i=r_(tau(i)) modulo q.
The number c_0 is the lift of an INNER residue class; both original endpoint coefficients remain exactly1.
The bound E(c) concerns the auxiliary lift and is not a bound on the original coefficient energy of P.

Every member of this class satisfies the actual original-degree inequality and its uniform consequence

    ((D+p)/D)m(P)>u_q,
    m(P)>g_q:=u_q/(1+1/J(q))>0,                        (ST5)

where m(P)=log M(P) is TOTAL logarithmic Mahler measure with natural logarithms.
For fixed q, the positive rational g_q is independent of p, D, the compatible residues, the admissible lifts and all original coefficients.
Every degree in the stated class satisfies the repetition premise; no low-degree patch or bounded-degree enumeration is used.

### C. Exact original auxiliary and all costs

For each admitted lift define

    Q_D=x^D+sum_(j=1..D-1)c_(j mod p)x^j+1,
    G=x^p+c_1x^(p-1)+...+c_(p-1)x+(c_0-1),
    G*=x^pG(1/x).

For p=1 the inner c_1,...,c_(p-1) list is empty.
The exact reciprocal identity is

    F=(x^p-1)Q_D=x^D G-G*.                             (ST6)

Write P=Q_D+qR with integral R of degree less than D.
At every original root alpha of P,

    F(alpha)/q=-(alpha^p-1)R(alpha) in Z[alpha],         (ST7)

allowing zero.
Let a=ord_xG, H=x^(-a)G, k=p-a and n=D+a.
Then H is monic integral with H(0)!=0, its energy remains E(c)<=q^2, and

    H*=x^kH(1/x)=G*,
    F=x^n H-H*,
    n>J(q)k,
    T=n+k=D+p.                                        (ST8)

If k=0, H=1; thus the excluded C845 constants +/-q never occur.
The polynomial F has leading coefficient1, constant coefficient-1 and true degree and span D+p.
The full original costs are

    #supp F<=2q^2, ||F||_1<=2q^2,
    frequency range J(q)(D+p), coefficient price2^(J(q)),
    finite matrix size2J(q)(D+p)+1,
    delta_raw=q Delta(q), B_raw=q^2 B_ph(q),
    radial multiplier1+2q/Delta(q).                    (ST9)

The original field degree remains D throughout.
C845's zero-value exclusion occurs before its signed norm logarithm; no auxiliary nonvanishing or new canonical system is assumed.
Removing the initial monomial from G does not reduce the original span or any cost in ST9.

### D. Exact lift-energy minimization and its binary form

<a id="reciprocal-orbit-minimum-energy"></a>
**Definition.** For a compatible residue vector r and the reflection tau above, let E_min be the minimum of E(c) over all integral congruent lifts satisfying the exact tau equalities.
If compatibility fails, no such lift exists.
The minimum is computed independently on the one- or two-element reflection orbits:

- On an orbit O not containing0, choose its common residue representative nearest0, contributing |O|c^2.
- If s=0, the orbit{0} contributes(c_0-1)^2 and its representative is chosen nearest1.
- If s!=0, the orbit{0,s} contributes c^2+(c-1)^2=2(c-1/2)^2+1/2 and its common representative is chosen nearest1/2.

Add the leading contribution1.
Each minimum requires only the two neighboring integers in the specified residue lattice, with either representative allowed at a tie.
This is an exact finite arithmetic algorithm, and E_min<=q^2 is necessary and sufficient for the lift-energy hypothesis ST4.
It does not replace the original polynomial or repetition hypotheses.

For q=2, take r_i in{0,1} and w=sum_i r_i.
Then the exact minimum and a minimizing lift are

    E_min=2+w-2r_0,
    c_i=r_i for every i.                              (ST10)

Thus the energy condition is equivalent to r_0=0,w<=2 or r_0=1,w<=4, for every compatible binary reflection pattern and every p>=1.

### E. Genuine unbounded periods, actual nonvacuity and limitations

For ANY p>2, take r_1=1 and all other residues0, and any even D congruent to2 modulo p with D>J(2)p.
For example D=2+2pL for every integer L>=J(2) satisfies these conditions.
The residue vector is reflection-compatible, has least positive cyclic period p and has E_min=3<4.
Its actual seed is G=x^p+x^(p-1)-1, and the SAME g_2 applies throughout this unbounded-period class.

At every admissible p,D,residue assignment satisfying ST3--ST4, adopted C842 NG supplies infinitely many actual monic irreducible reciprocal noncyclotomic integer-unit polynomials in that same degree and residue class.
Its complete CRT/Eisenstein construction and actual height/length costs are retained at that input; this statement assumes neither a near-one realization nor bounded original coefficient energy.
Every such polynomial shares the residue-lift certificate even when its own coefficients grow.

The fixed q, exact integer lift energy and actual repetition D/p>J(q) remain hypotheses.
No assertion is made for arbitrary residue patterns, inadequate repetition, a uniform varying-q gap, a numerical constant, efficient computation, near-one inputs, gap attainment or the unrestricted Lehmer objective.
The retained C135 binomial-product account is comparison only at its actual proof-draft status, and C775 concerns a different copied-sign family; no novelty or strict separation from older sufficient criteria is claimed.

## Complete argument

The entire UR1--UR7 proof follows, including every endpoint, monomial-reversal identity, original degree cost, orbit minimum, binary case, actual nonvacuity application and status/source boundary.
No mutable Draft or native output supplies a proof premise.

<a id="unbounded-period-energy-and-repetition-gap"></a>
## Unbounded residue periods with paid lift energy and repetition

Human author Yin; author development, 2026-10-28 UTC.
Root proposed this application of the varying-seed phase theorem, the orbitwise minimum-energy test and the explicit binary class.
Primitive_second_eight checked the actual period endpoints, monomial removal, original span, uniform inequality, every orbit minimum and the nonvacuity interface.
This is a separate author deduction fixed OPEN below, not an independent review of its input theorem or an adopted result.
No native computation, source acquisition or numerical cutoff is part of this fixed argument.

### UR1. Preparation and the exact adopted-input boundary

The decisive input is the complete fixed [C845 Statement B--C](Yin_C_G0845_v1.md#statement), including its actual [zero-before-norm proof](Yin_C_G0845_v1.md#ordered-cutoff-and-original-norm) and [all-degree window conclusion](Yin_C_G0845_v1.md#all-degree-class-gap-and-scale-boundary).
Its current selected decision is [adopted](Yin_C_G0845_v1.md#decision-whole-reviewed-2026-10-28); the statement and entire UP1--UP6 proof were read for this author application, without borrowing a review verdict for the new deduction.
The deductions below retain this exact adopted input; the present periodic application remains OPEN for its own whole independent review and responsible adoption.
C845 permits a varying integral seed H, requires H(0)!=0 and coefficient energy at most q^2, excludes the constants +/-q, and includes H=1, both signs and a possibly zero integral auxiliary value.
The new obligation here is to construct those exact data from a genuinely unbounded residue period and to pay the ORIGINAL span/window, rather than to repeat C845's analytic proof.

The targeted reuse screen read [C842's adopted finite-reversal criterion](Yin_C_G0842_v1.md#decision-whole-reviewed-2026-10-28) and [its general nonvacuity construction](Yin_C_G0842_v1.md#ng-every-compatible-reciprocal-residue-class-has-infinitely-many-actual-inputs).
C842 gives fixed finite seed families and bounded-period applications; those hypotheses alone do not supply constants uniform over the varying p below.
Its nonvacuity construction applies directly at each actual compatible degree/residue assignment and is reused without a new CRT/Eisenstein proof.

The retained [C135 binary binomial-product account](Yin_C_G0135_v1.md#statement) was read at its actual [proof-draft selection](Yin_C_G0135_v1.md#decision-initial), not promoted to an adopted input.
It studies complete divisibility modulo2 by a bounded number of binomials with controlled original exponent costs, including a central parity-block class.
The present hypotheses specify an integer energy lift and phase separation; a bounded-binomial factorization is neither assumed nor established here, and no strict separation from that earlier sufficient class has been proved.
[Adopted C775](Yin_C_G0775_v1.md#decision-whole-reviewed-2026-10-26) permits varying periodic comb periods in its fixed C801/C809 copied-sign domain, with actual support-availability and template-weight costs.
That is a different original family and measure comparison, not an existing arithmetic theorem for the irreducible residue class below.
The present deduction assumes no copied height-one source or C809 target.
No novelty or unrestricted-class claim follows from this bounded reuse comparison.

### UR2. Fixed modulus, unbounded period and exact hypotheses

Fix an integer modulus q>=2.
To avoid confusion with the residue period, write J(q) for the cutoff denoted J_p in C845, using precisely its q-only quantities

    B_s(q)=q^2+1,
    delta(q)=1/(2q^2 B_s(q)),
    eta(q)=1/(8q^4 B_s(q)^2),
    Delta(q)=delta(q)*eta(q),
    B_ph(q)=4q^2+1,
    J(q)=ceil(B_ph(q)/(eta(q)*Delta(q)^2)).              (UR1)

Let u_q be any positive dyadic output of C845's ordered cutoff algorithm, so with its inherited h0 and epsilon,

    J(q)u_q<h0,
    (1+2q/Delta(q))u_q+2^(J(q)) epsilon(J(q)u_q)<eta(q),
    (2q^2-1)epsilon(u_q)+4q^2 u_q<1.                   (UR2)

All these parameters depend only on q; no numerical value or execution is claimed.
In particular J(q)>=1.

Let p>=1 be ANY positive integer, allowed to vary without bound, and let P be a monic reciprocal irreducible noncyclotomic polynomial in Z[x] of original even degree D, with constant term1.
Suppose its actual inner coefficients satisfy

    P=x^D+sum_(j=1..D-1)a_j x^j+1,
    a_j=r_(j mod p) modulo q,
    D>J(q)p.                                          (UR3)

Set s=D modulo p and let tau(i)=s-i modulo p on the residue indices0,...,p-1.
Require an integral lift vector(c_0,...,c_(p-1)) such that

    c_i=r_i modulo q,
    c_i=c_(tau(i)) EXACTLY,
    E(c):=1+sum_(j=1..p-1)c_j^2+(c_0-1)^2<=q^2.       (UR4)

Every residue index occurs among the actual inner coefficients because D>p.
Thus reciprocity of P already forces r_i=r_(tau(i)) modulo q; the exact lift equality in UR4 is stronger than this congruence and is retained explicitly.
The number c_0 describes the INNER coefficient residue at indices divisible by p; it does not replace either endpoint coefficient1 of P.
The bound E(c) is the energy of an auxiliary lift, not a bound on the original coefficient energy of P.

The claimed author consequence of C845 is

    ((D+p)/D)m(P)>u_q,
    m(P)>g_q:=u_q/(1+1/J(q))>0.                       (UR5)

Here m(P)=log M(P) is total logarithmic Mahler measure.
The gap g_q is computable and uniform in p, the compatible residues, the selected lifts, D and all coefficients of P, at the exact hypotheses UR3--UR4.
This is an unbounded-period conditional class, not a conclusion for arbitrary periodic patterns or insufficiently repeated patterns.

### UR3. Full endpoint identity and legitimate monomial removal

Define the exact reciprocal comparison and its monic degree-p auxiliary seed by

    Q_D=x^D+sum_(j=1..D-1)c_(j mod p)x^j+1,
    G=x^p+c_1x^(p-1)+...+c_(p-1)x+(c_0-1),
    G*=x^pG(1/x)=1+c_1x+...+c_(p-1)x^(p-1)+(c_0-1)x^p.

The exact tau equalities make Q_D reciprocal, and its residues agree with P.
Since D>p, the following two endpoint blocks are disjoint:

    (x^p-1)Q_D=x^D G-G*.                              (UR6)

Indeed its coefficients at degrees0,...,p are -1,-c_1,...,-c_(p-1),1-c_0.
The middle coefficients at p+1,...,D-1 cancel by periodicity, with an empty interval allowed.
Its coefficients at D,...,D+p are c_0-1,c_(p-1),...,c_1,1 by reciprocity of Q_D, including c_s=c_0.
These are exactly the right-hand blocks.
The argument includes p=1; there is then no c_1,...,c_(p-1) list.

Write P=Q_D+qR with integral R of degree less than D.
For every original root alpha of P, UR6 gives the genuine original-order identity

    F(alpha)/q=-(alpha^p-1)R(alpha) in Z[alpha],
    F=x^D G-G*.                                       (UR7)

This is allowed to be zero; no nonzero-resultant assumption or replacement of the original minimal polynomial is made.

Let a=ord_x G, so0<=a<=p, and set H=x^(-a)G and k=p-a.
This is an actual integral monic polynomial with H(0)!=0 and the SAME collected coefficient energy E(c)<=q^2.
Its degree-k reversal satisfies exactly

    H*(x)=x^kH(1/x)=x^pG(1/x)=G*(x),
    F=x^(D+a)H-H*,
    n=D+a,
    n+k=D+p.                                         (UR8)

If k=0 then H=1, so it is an allowed constant seed; otherwise its positive degree already distinguishes it from the excluded constant polynomials +/-q.
The monomial removal therefore meets every seed hypothesis of C845 without changing F, discarding a scalar or reducing its original span.
Since G is monic, F has leading coefficient1 at degree D+p and constant coefficient-1; its true degree and support span are exactly D+p.

### UR4. Separation, original costs and the uniform all-degree implication

From D>J(q)p and a>=0,

    n=D+a>J(q)p+a>=J(q)(p-a)=J(q)k.                   (UR9)

This verifies C845's actual phase separation, including k=0.
Use its sign sigma=-1 and the actual algebraic integrality UR7 for the SAME original P, whose degree remains D.
C845 Statement B then gives

    (n+k)m(P)/D=(D+p)m(P)/D>u_q.

Because p/D<1/J(q), division yields both assertions in UR5.
Every degree in this class satisfies the required separation by definition, so no omitted low-degree branch or C394 bounded-degree completion is needed.
Removing UR3 would remove the proof's frequency-separation hypothesis; the present argument makes no claim for that enlarged class.

The actual costs inherited from C845 remain

    T=D+p,
    #supp F<=2q^2, ||F||_1<=2q^2,
    frequency range J(q)T,
    coefficient price2^(J(q)),
    finite matrix size2J(q)(D+p)+1,
    delta_raw=q Delta(q), B_raw=q^2 B_ph(q),
    radial multiplier1+2q/Delta(q).                   (UR10)

In particular unbounded p does not mean a bounded matrix or bounded original auxiliary degree.
The exact zero-value exclusion in C845 precedes its norm logarithm and applies to UR7 without a proof that P differs from Q_D.
The fixed modulus q, the integer lift energy and the actual repetition D/p>J(q) are the paid restrictions that make the seed degree uniformity usable.
No uniform positive lower bound as q varies is asserted.

<a id="minimum-reciprocal-periodic-lift-energy"></a>
### UR5. Exact finite arithmetic test for the lift-energy hypothesis

First test r_i=r_(tau(i)) modulo q for every actual residue orbit.
If it fails, no exact reciprocal lift exists.
Suppose it holds and partition{0,...,p-1} into the one- or two-element orbits of tau.
On each orbit O not containing0, every exact lift has one common integer c in its prescribed residue class, and its contribution to E(c) is |O|c^2.
Its minimum is attained by a representative nearest to0, with either minimizing representative permitted at a tie.

If s=0 modulo p, the orbit of0 is{0}; its contribution is(c_0-1)^2, minimized by a representative of r_0 nearest to1.
If s!=0, that orbit is{0,s}; its common-lift contribution is

    c^2+(c-1)^2=2(c-1/2)^2+1/2,

minimized by a representative of the common residue r_0=r_s nearest to1/2.
Adding these independent orbit minima and the leading contribution1 gives the EXACT minimum E_min of UR4 over every admissible integral lift.
There is no coupling between different orbits.
Thus E_min<=q^2 is necessary and sufficient for the existence of the lift required by UR4.
This is a finite arithmetic test for each supplied p and residue vector, not a numerical seed scan.
For any specified center, the two integers in its residue lattice adjacent to that center suffice to find the minimum by exact rational comparison; every orbit weight and the constant term remain included.

### UR6. The complete binary energy criterion and an unbounded-period class

For q=2 choose the actual residue representatives r_i in{0,1} and write w=sum_(i=0..p-1)r_i.
For an orbit not containing0, its minimum contribution is the sum of its binary residues, attained by c_i=r_i.
If0 is fixed, its minimum contribution is1-r_0.
If0 is paired with s, reciprocity gives r_s=r_0, and its minimum contribution is1 whether the common residue is0 or1.
After adding the leading1, both cases give exactly

    E_min=2+w-2r_0.                                   (UR11)

The full lift c_i=r_i attains this minimum in every case, including p=1.
Consequently, among reflection-compatible binary residue vectors, UR4 is equivalent to

    r_0=0 and w<=2, OR r_0=1 and w<=4.                 (UR12)

This is an equivalence for the energy hypothesis only; the original polynomial domain and repetition condition UR3 are still required for the gap inequality(UR5).

For a concrete genuinely unbounded-period subfamily, choose ANY p>2, r_1=1 and all other residues0.
Take any even D congruent to2 modulo p with D>J(2)p; for example D=2+2pL for any integer L>=J(2).
The reflection i->2-i fixes the unique nonzero class1 and preserves every zero class, so compatibility holds.
Here r_0=0, w=1 and E_min=3<4, and the actual seed is

    G=x^p+x^(p-1)-1.                                  (UR13)

The cyclic residue vector has least positive period p, because a nontrivial shift would move its unique nonzero entry.
Thus p is not merely an artificially enlarged label for one fixed short pattern.
The gap deduced from adopted C845 is the SAME g_2 for all these p and D.
No assertion that these classes escape the older binomial-product criteria, yield a near-one family, or attain the gap is made.

### UR7. Actual nonvacuity and remaining scope

For any supplied p,D,residue vector satisfying the exact compatibility, energy and repetition conditions UR3--UR4, apply [adopted C842 NG](Yin_C_G0842_v1.md#ng-every-compatible-reciprocal-residue-class-has-infinitely-many-actual-inputs) with its modulus m=q and the actual inner residue assignment j->r_(j mod p).
It constructs infinitely many actual monic irreducible reciprocal noncyclotomic integer-unit polynomials in this SAME degree and residue class, with the exact CRT/Eisenstein and coefficient costs retained there.
Since UR4 concerns only the residue lift, all these original polynomials share its energy certificate even though their own coefficient energies can grow.
This proves nonvacuity at every admissible degree, including the unbounded-period subfamily UR13, without a new construction or numerical example.

The new mathematical content is the exact unbounded-period application, the orbitwise necessary-and-sufficient energy test and its binary form.
C845 supplies the adopted uniform varying-seed theorem, and C842 supplies adopted nonvacuity; neither earlier review or adoption is silently transferred to this new author deduction.
There is no native computation, C845 edit, proof of arbitrary residue-pattern coverage, uniform varying-modulus gap, near-one realization, novelty claim or unrestricted Lehmer resolution.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision unbounded-period-energy-gap-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T22:46 |
| status | open |
| reason | Fix the complete original-polynomial unbounded-period application of adopted C845 under exact fixed-q lift energy and repetition, with all scalar/degree/span costs, exact orbitwise minimum algorithm and binary equivalence, genuine unbounded minimal periods and adopted C842 NG nonvacuity. Root and primitive_second_eight are substantive contributors. The complete proof is retained for fresh whole independent review and separate adoption; no native computation, numerical cutoff, novelty, older-class separation or unrestricted result is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire energy/repetition theorem](#statement) | ST1--ST10 and accompanying A--E: fixed-q parameters, every period and original degree in the exact class, actual residue/lift distinctions, uniform total gap, true auxiliary span and costs, complete minimum-energy/binary algorithm, unbounded minimal-period example, nonvacuity and limits. |
| argument | [Complete UR1--UR7 proof](#complete-argument) | Full targeted reuse and status boundaries, exact endpoints and c_s=c_0, monomial reversal and constant-H case, C845 separation/application with original span D+p, every orbit minimum and binary case, and exact C842 NG hypothesis matching. |
| dependency | [Adopted varying-seed phase theorem](Yin_C_G0845_v1.md#decision-whole-reviewed-2026-10-28) | Complete Statement B--C with its q-only constants and ordered cutoff, allowed H(0) nonzero/energy/sign/constant domain, n>kJ_p, integral value including zero, full original-degree inequality and all raw radial/Fourier/matrix costs. Its analytical proof is reused, not re-proved or re-reviewed here. |
| dependency | [Adopted compatible-class nonvacuity](Yin_C_G0842_v1.md#decision-whole-reviewed-2026-10-28) | NG only: infinitely many actual monic irreducible reciprocal noncyclotomic units in each compatible actual inner-residue assignment at every even degree, with its exact CRT/Eisenstein and height/length costs. C842's fixed finite-G gap and bounded-degree completion are not premises for the new uniform-in-period inequality. |
| support | [Earlier finite-reversal comparison](Yin_C_G0842_v1.md#fixed-reversal-auxiliary-class) | Prior finite-family scope only, distinguishing it from the new varying-period application; no uniform-in-p consequence is borrowed from a fixed finite seed set. |
| support | [Retained binary binomial-product comparison](Yin_C_G0135_v1.md#statement) | Bounded-binomial-product divisibility and central parity-block class, read at its actual proof-draft decision-initial. This is not an adopted input, and no class-separation theorem is asserted. |
| support | [Adopted periodic-comb comparison](Yin_C_G0775_v1.md#decision-whole-reviewed-2026-10-26) | Exact fixed-source C801/C809 copied-sign/period-availability/template-budget scope only; it is not used as an arithmetic theorem for the original irreducible residue class here. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T22:55 |
| status | proved |
| reason | Adopt the entire Statement A--E/ST1--ST10 and UR1--UR7 proof after root read the complete author proof, fixed statement and whole independent R1067. Exact endpoints, monomial removal and reversal, true original span D+p, C845 separation and every inherited cost, the uniform fixed-q gap, complete orbitwise minimum and binary equivalence, genuine unbounded minimal periods and C842 NG nonvacuity are covered. The exact lift-energy and repetition hypotheses remain required; no arbitrary-pattern coverage, varying-q gap, numerical cutoff, older-class separation or unrestricted Lehmer conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire energy/repetition theorem](#statement) | ST1--ST10 and accompanying A--E: fixed-q parameters, every period and original degree in the exact class, actual residue/lift distinctions, uniform total gap, true auxiliary span and costs, complete minimum-energy/binary algorithm, unbounded minimal-period example, nonvacuity and limits. |
| argument | [Complete UR1--UR7 proof](#complete-argument) | Full targeted reuse and status boundaries, exact endpoints and c_s=c_0, monomial reversal and constant-H case, C845 separation/application with original span D+p, every orbit minimum and binary case, and exact C842 NG hypothesis matching. |
| dependency | [Adopted varying-seed phase theorem](Yin_C_G0845_v1.md#decision-whole-reviewed-2026-10-28) | Complete Statement B--C with its q-only constants and ordered cutoff, allowed H(0) nonzero/energy/sign/constant domain, n>kJ_p, integral value including zero, full original-degree inequality and all raw radial/Fourier/matrix costs. Its analytical proof is reused, not re-proved or re-reviewed here. |
| dependency | [Adopted compatible-class nonvacuity](Yin_C_G0842_v1.md#decision-whole-reviewed-2026-10-28) | NG only: infinitely many actual monic irreducible reciprocal noncyclotomic units in each compatible actual inner-residue assignment at every even degree, with its exact CRT/Eisenstein and height/length costs. C842's fixed finite-G gap and bounded-degree completion are not premises for the new uniform-in-period inequality. |
| support | [Earlier finite-reversal comparison](Yin_C_G0842_v1.md#fixed-reversal-auxiliary-class) | Prior finite-family scope only, distinguishing it from the new varying-period application; no uniform-in-p consequence is borrowed from a fixed finite seed set. |
| support | [Retained binary binomial-product comparison](Yin_C_G0135_v1.md#statement) | Bounded-binomial-product divisibility and central parity-block class, read at its actual proof-draft decision-initial. This is not an adopted input, and no class-separation theorem is asserted. |
| support | [Adopted periodic-comb comparison](Yin_C_G0775_v1.md#decision-whole-reviewed-2026-10-26) | Exact fixed-source C801/C809 copied-sign/period-availability/template-budget scope only; it is not used as an arithmetic theorem for the original irreducible residue class here. |
| review | [Whole independent unbounded-period finding](../audits/reviews/Yin_R_G1067_v1.md#whole-unbounded-period-energy-finding) | Entire Statement A--E and UR1--UR7, all ten statement and thirteen proof formulas, exact adopted input interfaces, original endpoints/span/costs, all orbit and binary branches, true minimal periods and every admissible-class nonvacuity; independent arrangement without mutable Draft or substantive repair. |

