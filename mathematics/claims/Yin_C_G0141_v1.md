---
author: Yin
---
# Sparse auxiliary zero removal and simultaneous finite-prime obstructions

Date: 2026-10-15.
Human author Yin.
This is a new responsible inquiry under the continuing G0001 authorization.
It first retains two exact reuse consequences, then investigates whether finitely many fixed good primes automatically supply bounded-term, linear-degree modular auxiliaries for actual reciprocal units.
No near-one sequence is assumed.
No native program or J is used.

## Question, reuse and contribution boundary

The [C92 short-annihilator theorem](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) already excludes every short rational annihilator at its explicit fixed-support threshold.
It can remove the nonzero-value hypothesis of the adopted [C139 bounded-term auxiliary theorem](Yin_C_G0139_v1.md#statement) by a two-case argument.
This is a direct reuse consequence, not a new zero theorem.

The [L38 Salem factor theorem](Yin_C_G0248_v1.md#excess-three-family) already deals with the zero branch for any irreducible nontorsion factor of the C137 Salem--Boyd auxiliary.
Thus changing equal-degree congruence to full modular divisibility needs an explicit assembly, not a new root-family theorem.
The exact derivation and finite cutoff are retained below.
Root's separate normalized-coefficient inquiry is now fully fixed as [C140v1](Yin_C_G0140_v1.md#statement), still pending independent review at this writing.
It is not used as an adopted premise here.
The C92 reuse identified in this inquiry is accurately credited in that separate artifact; it does not make the present author an independent reviewer of C140's zero-removal assembly.

The new existence question is simultaneous avoidance at every prime in a fixed finite pool.
Before root's latest message, f had developed the odd-prime-half-degree norm-one count, sparse-factor counting, symmetric CRT lift and middle-coefficient sign adjustment.
Those steps had not yet been persisted; the actual delay is disclosed.
Root independently supplied the overlapping primitive norm-one construction, an all-half-degree lower bound, an optional Eisenstein lift, and the further maximal-order/content-normalization question.
Those actual contributions are recorded rather than asserting root independence for this round.
Root's optional extra Eisenstein prime is unnecessary when one pool reduction is already irreducible.
The full proofs, choice of retained route and limits are developed below.

## Source and prior-result screen

Actual C92, C137, C139, L20, L38, L81, L91, L237 and the Hir06 classical reciprocal-sequence attribution were inspected at their needed scope.
C130 and C136 are different fixed-prime controls and do not prove simultaneous sparse-auxiliary avoidance at a finite pool.
The new finite-field count is classical, not a project novelty.
A bounded primary-source search located Helmut Meyn and Werner Goetz, Self-reciprocal Polynomials Over Finite Fields, the SLC B21d electronic 8-page article.
Theorem3 gives the exact count.
The initial source-pending state was resolved before this freeze: root retained the actual electronic bytes as MG89 and registered [MG89-U001](../audits/literature/MG89/Yin_U001.md#mg89-u001), which this author read and checked against the inspected source.
Only the exact accepted count and its odd-prime substitution are used.
The source record identifies the inspected edition; no original Carlitz proof or whole-paper audit is claimed.

<a id="reuse-zero-removal"></a>
## 1. Exact zero removal already supplied by C92

Keep C139's actual domain: fixed integers K>=2 and S>=1, fixed C>0 and 0<eta<=1, an original monic irreducible nontorsion integer unit P of degree d and total logarithmic measure m, and a nonzero F in Z[t] of degree 1<=T<=Cd with at most K terms and ||F||_1<=S.
Suppose q>=2 is an integer, F(alpha)/q is an algebraic integer, and m(F)<=log q-eta.
Here the value is provisionally allowed to be zero.

Write the exact C92 constants as

    c0=log(2)/4,
    K0=c0/[2*36^8*5^64], eta_K=K0 K^(-64).             (1)

Then the direct consequence of C92 and C139 is

    m>min{g(K,S,C,eta), eta_K/C}>0.                     (2)

Indeed, suppose m is at most the right side.
If F(alpha)=0, remove its initial monomial factor.
Its actual exponent span A is positive, at most T, and its actual support r lies between 2 and K.
Thus A*m/d<=C*m<=eta_K<=eta_r.
C92's automatic independence theorem excludes the asserted rational relation, with its exact strict margin below 1/40 and within the original h0 domain.
A one-term polynomial cannot vanish at the nonzero unit alpha, so there is no omitted monomial case.
Hence F(alpha)/q is NONZERO, and the already adopted C139 theorem gives m>g, a contradiction.
All original embeddings and the integer content remain those of the existing inputs.
This proof supplies no new short-annihilator estimate.
The same zero-removal implication can be applied to a separately proved normalized-coefficient class, but no such unreviewed candidate is used to establish (2).

<a id="reuse-full-modular-divisor"></a>
## 2. C137 and L38 already cover full modular divisors of the classical auxiliary

Set f=t^3-t-1, h=1-t^2-t^3 and A_N=t^N f+h, N>=4.
Fix C>0.
Let P be any original monic irreducible nontorsion integer unit of degree d such that

    P mod2 divides A_N mod2 in F_2[t],
    N+3<=C*d.                                           (3)

Divisibility is of the FULL polynomial, with all reduction multiplicities.
Since both polynomials are monic, (3) implies d<=N+3 and therefore C>=1 whenever the class is nonempty.
Integer monic division A_N=P Q+R gives deg R<d.
Reducing the division modulo2 shows R mod2=0, so A_N(alpha)/2=(R/2)(alpha) is integral in the actual order Z[alpha].
No squarefree or good-prime assumption is needed.

Use C137's exact J=2^20, B0=3J+3, mu=(c0/J)*2^(-16(J+1)^2), and L168's positive bounded-degree height floor epsilon_(B0).
Then

    m(P)>min{mu/C, epsilon_(B0)/2}>0.                   (4)

For N>3J and A_N(alpha) nonzero, this is precisely C137's already proved original-degree linear-cost consequence.
For N>3J and A_N(alpha)=0, monicity and irreducibility imply P divides A_N over Z.
The actual L38 theorem gives one Salem minimal factor and only cyclotomic remaining factors for EVERY N>3; the original nontorsion P must be that Salem factor.
For N>=16 its expanding root exceeds the plastic number theta>5/4.
Thus m(P)>log(5/4)>mu>=mu/C.
This invokes L38's full factor statement, not C137's equal-degree argument P=A_N and not L20's formerly unspecified eventual threshold.
For 4<=N<=3J, monic modular divisibility gives d<=B0, and L168 gives m(P)>=epsilon_(B0), strictly above the second term in (4).
The C<1 domain is empty, not an unsupported extension of the zero-branch comparison.

The classical sequence attribution remains [Hir06's inspected reciprocal-sequence interface](../audits/literature/Hir06/readme.md#reciprocal-sequence-method-attribution).
No convergence rate, new Salem construction, graph realization or exact cyclotomic factor table is needed.
This is an assembly of existing results, rather than a new mechanism deserving a duplicate theorem.

<a id="statement"></a>
## 3. Simultaneous finite-prime avoidance for actual reciprocal units

Fix a NONEMPTY finite set Pi of rational primes, an integer K>=1 and a real C>0.
Put M=product_(p in Pi) p.
For every sufficiently large odd rational prime h, with d=2h, there exists a monic irreducible reciprocal P in Z[t], of constant coefficient1 and original degree d, with all of the following properties.

1. P has a real root greater than1; in particular it is a nontorsion integer unit.
2. For EVERY p in Pi, P mod p is irreducible of degree d, hence squarefree and good.
3. For EVERY p in Pi, NO nonzero polynomial over F_p of degree at most floor(Cd) and at most K nonzero terms is divisible by P mod p.
4. Its actual coefficient height and coefficient l1 norm obey

       H(P)<=2+2(h-1)(M-1)+M,
       ||P||_1<=4+4(h-1)(M-1)+M.                       (5)

5. More strongly, let alpha be ANY original root, let O_K be the full ring of integers of Q(alpha), and let q>=2 be ANY integer all of whose prime factors lie in Pi.
There is NO nonzero F in Z[t] of degree at most floor(Cd) with at most K terms such that

       F(alpha)/q belongs to O_K,
       m(F)-log q<0.                                   (6)

The value in (6) is allowed to be zero.
Coefficient heights of F, powers of primes in q and coefficient l1 norm divided by q are unrestricted.
Thus (6) excludes in particular any fixed positive normalized Mahler margin, even without a normalized coefficient bound.
It excludes an auxiliary for the SAME constructed input at every prime of the fixed pool; it is not merely a counterexample for one preselected prime with a different input at the other primes.

These particular inputs are explicitly FAR FROM ONE and are not Salem: they have no unit-circle roots and

    log((3+sqrt(5))/2)<=m(P)<=log ||P||_1.              (13)

The upper bound is O_Pi(log d), not a bounded-total-measure statement.
The constants Pi,K,C are fixed before h grows.
This does not exclude adaptive unbounded prime pools, growing term counts or superlinear auxiliary degrees, and cannot refute a coverage theorem restricted to sufficiently small m(P).

<a id="argument"></a>
## 4. Known finite-field supply and exact sparse-factor budget

For an odd prime h, the classical exact count of self-reciprocal monic irreducible polynomials over F_p of degree 2h is

    S_p(h)=(p^h-p)/(2h).                                (7)

This is the odd-prime specialization of Meyn--Goetz Theorem3, not a new counting result.
The actual primary electronic article and its product/Mobius proof mechanism on printed/PDF pages1--3 were inspected: Theorem1 identifies the factors of t^(p^h+1)-1, Lemma2 performs Mobius inversion and Theorem3 gives the count.
Theorem3's general formula is not silently treated as a project contribution.
The precise accepted source input is [MG89-U001](../audits/literature/MG89/Yin_U001.md#mg89-u001), including p=2 and h equal to the characteristic if it occurs.
No characteristic restriction has been inserted.

For clarity the specialization can also be read directly from that source factorization: when h is an odd prime, all roots of t^(p^h+1)-1 consist of the roots already in t^(p+1)-1 and disjoint Frobenius orbits of size 2h.
The former polynomial divides the latter because h is odd; both are separable in characteristic p.
The difference in degrees is p^h-p, yielding (7).
This is the source's argument specialized, not an independent new finite-field lemma.

Set N=floor(Cd), k0=min(K,N+1), and

    A_p(N,K)=sum_(j=1)^k0 binom(N+1,j)(p-1)^j.          (8)

This counts exactly all nonzero degree-at-most-N polynomials with at most K terms over F_p, including constants.
Each such polynomial has at most floor(N/d) DISTINCT irreducible factors of degree d, even when it has repeated factors.
Therefore the number of the polynomials counted in (7) which divide at least one of them is at most floor(N/d)*A_p(N,K).
It is enough to choose h so that, simultaneously for all p in Pi,

    (p^h-p)/(2h)>floor(N/d)*A_p(N,K).                   (9)

For fixed p,K,C the right side is O(d^K) and the left side is exponential in h; since Pi is finite, all sufficiently large odd prime h satisfy every inequality.
If C<1, floor(N/d)=0 and no nonzero polynomial in this degree window can have a degree-d factor anyway.
Formula (9) is an explicit finite sufficient test; no native search is claimed.
Choose one avoiding self-reciprocal irreducible R_p for each p.

<a id="simultaneous-crt-lift"></a>
## 5. One actual integer reciprocal lift with paid coefficients

For each 1<=i<=h choose the CRT representative c_i in {0,...,M-1} of the coefficient of t^i in every R_p.
Self-reciprocity gives the matching coefficient of t^(d-i), and monic self-reciprocal polynomials have constant coefficient1.
Put

    A=2+2 sum_(i=1)^(h-1) c_i,
    P0=t^d+1+sum_(i=1)^(h-1) c_i(t^i+t^(d-i))+c_h t^h,
    L=floor((A+c_h)/M)+1,
    P=P0-M L t^h.                                      (10)

The integer s=M L-(A+c_h) lies in {1,...,M}; this remains true when A+c_h is divisible by M.
Consequently

    P(1)=-s<0,
    coefficient_(t^h)(P)=-A-s.                        (11)

All other interior coefficients are in {0,...,M-1}; hence the middle coefficient has greatest absolute value and (5) follows from A<=2+2(h-1)(M-1), H(P)=A+s and ||P||_1=2A+s.
These are costs of the actual integer P, not of an abstract reduction inventory.
The extra Eisenstein prime proposed by root is unnecessary: since Pi is nonempty, choose any p in it.
A nontrivial monic factorization over Z would reduce to a factorization into positive-degree monic factors of R_p, contradicting its irreducibility.
The usual monic Gauss reduction supplies irreducibility over Q.

The polynomial is monic, reciprocal and of constant coefficient1.
By (11) and P(t)->+infinity on the positive real axis it has a real root greater than1.
Irreducibility makes that root an original conjugate of every chosen alpha, excluding torsion and establishing the stated unit domain.
Every R_p is irreducible over a finite field, hence separable, so p does not divide disc(P).
This is a good-prime statement for EVERY prime in Pi on the SAME lift.

The actual lift also pays a definite positive Mahler cost.
For |z|=1 the exact identity is

    -z^(-h)P(z)
       =s+|z^h-1|^2+sum_(i=1)^(h-1)c_i|z^(h-i)-1|^2
       >=1+|z^h-1|^2=3-z^h-z^(-h)>0.                 (14)

Thus P has no unit-circle root.
Integrating the logarithm and using scalar Jensen/root normalization gives

    m(P)>=integral_T log(3-z^h-z^(-h))
         =log((3+sqrt(5))/2).

For the last equality, multiplication by z^h changes no circle modulus; the two roots of u^2-3u+1 are (3+sqrt(5))/2 and its inverse, and Haar measure is invariant under z->z^h.
The opposite inequality m(P)<=log ||P||_1 is pointwise on the circle.
This proves (13) at the actual original degree.
In particular h>=3 makes these degree-at-least6 polynomials non-Salem, with every root off the circle.
The stronger explicit limitation was found during author self-check and prevents this finite-pool construction from being mistaken for a small-measure obstruction.

## 6. Maximal-order integrality and normalized content

Root supplied the content-normalization extension to be checked here.
The exact local input is [C241's direct etale algebra](Yin_C_G0241_v1.md#direct-etale-frobenius-lift): if p does not divide disc(P), the actual power-basis algebra O0 tensor Z_p, O0=Z[alpha], is a product of discrete valuation rings with uniformizer p.
In the present irreducible-mod-p case there is only one component, of residue degree d.
Thus it is integrally closed in Q(alpha) tensor Q_p.
For completeness, integrally closedness follows from the DVR valuation: if v(x)<0 then in any monic equation x^r+a_(r-1)x^(r-1)+...+a_0=0 with integral coefficients, the leading term has uniquely smallest valuation, an impossibility.
Products obey this coordinatewise.
Every element of O_K is integral over Z_p in that algebra, hence belongs to O0 tensor Z_p.
This is enough; a global maximal-order equality or a computed order index is not asserted.

Suppose (6) holds.
Let c be the positive integer content of F, let g=gcd(c,q), and put

    F1=F/g, q1=q/g.

Then F1 is a nonzero integer polynomial, gcd(content(F1),q1)=1, its degree and support do not increase, and

    F1(alpha)/q1=F(alpha)/q in O_K,
    m(F1)-log q1=m(F)-log q<0.                         (12)

If q1=1, the nonzero integer polynomial F1 has Mahler measure at least1: the leading coefficient is a nonzero integer and the root formula takes the product of max(1,abs(root)).
Hence m(F1)>=0, contradicting (12).
Otherwise choose p dividing q1.
This p lies in Pi; F1 mod p is nonzero by the coprimality of its content with q1.
In the good local algebra, maximal-order integrality gives

    F1(alpha)=q1*[F1(alpha)/q1] in p*(O0 tensor Z_p).

Reduction in O0/pO0=F_p[t]/(R_p) therefore gives R_p divides F1 mod p.
This is the FULL polynomial divisibility, not a selected root or radical-only statement.
The residue polynomial has degree at most N and at most K terms, contradicting its defining avoidance.
This proves (6), including possible zero values and arbitrary repeated prime powers in q.
The negative logarithmic margin is used only in the q1=1 branch; no coefficient-size or uniform positive-margin assumption has been smuggled in.

## 7. Current limits and retained alternative

Root additionally proposed a primitive norm-one route valid at arbitrary half-degrees h: primitive elements of the cyclic group of order p^h+1 have degree2h, and an elementary phi lower bound would already beat the polynomial sparse-factor count.
That alternative is not needed here, is not adopted as an extra theorem, and has not been fully source-checked in this author round.
The known exact source count at odd prime h supplies a simpler infinite sequence sufficient for the stated result.
Root's optional extra Eisenstein prime is likewise omitted because the chosen pool irreducibility already proves irreducibility of P.
Their omission does not erase root's actual content/local-order contribution to Section6.

The exact zero-removal and full-modular-divisor consequences in Sections1--2 remove unnecessary restrictions from already available sufficient mechanisms.
Sections3--6 show that a fixed finite prime pool and a fixed sparse linear-degree auxiliary class are not automatically available for every reciprocal unit, even with unrestricted coefficients and denominators and maximal-order integrality.
Formula(14) proves that these particular controls have a definite positive measure and no circle roots; they cannot be Salem or approach1.
The actual near-one existence obligation therefore remains open.
No conditional gap, reciprocal-family control or source statement is reported as unrestricted G0001 completion.

<a id="direct-inputs"></a>
## 8. Direct inputs and actual self-check

The logical/source interfaces used in the complete material are:

- [C92 actual short-annihilator and independence argument](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support), including its accepted C74 threshold: Section1 only; no new source reading behind its original angular estimate.
- [C139 actual bounded-term theorem](Yin_C_G0139_v1.md#statement): Section1, with its exact BS13-dependent g, fixed raw coefficient bound and all original-field costs.
  Its actual selected whole-reviewed decision was read.
- [C137 actual finite logarithmic theorem](Yin_C_G0137_v1.md#statement): Section2's nonzero large-degree case, exact J,mu and actual T/d expense.
- [L38 exact Salem-factor statement and full proof](Yin_C_G0248_v1.md#excess-three-family): Section2's zero case for every noncyclotomic irreducible original factor.
  Its separate graph and excess classification are not used.
- [L168 bounded original-degree height floor](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape): Section2's finite degree d<=B0 case, not a numerical enumeration.
- [MG89-U001 exact count](../audits/literature/MG89/Yin_U001.md#mg89-u001): Section4's actual supply of finite-field irreducibles, at the accepted statement/applicability scope and inspected product/Mobius mechanism.
- [C241 direct good-prime local algebra](Yin_C_G0241_v1.md#direct-etale-frobenius-lift): Section6's actual power-basis DVR component; its later Frobenius-error results are not used.
- [F109 scalar normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization): the ordinary logarithmic Mahler integral/root formula, including integer content, in Sections5--6.
  No matrix normalization, Gram maximization or unproved outer factor is used.
- [Hir06 method attribution](../audits/literature/Hir06/readme.md#reciprocal-sequence-method-attribution): Section2's classical polynomial form only, not an imported root theorem.

The earlier C130v2 and C136 actual controls, L20's historical eventual threshold, L81/L91's different arithmetic/counting subjects and L237's growing-support auxiliary are comparisons, not premises of the new finite-pool theorem.
C140v1 is a separately fixed but still-under-review comparison at this author's freeze; the present proof does not depend on its adoption.

The author reread the complete saved body and checked the following mathematical points: C92 actual span rather than maximal degree, r<=K threshold direction and the monomial case; C139's strict gap and original integral content; C137 full modular remainder including nilpotents, nonempty C>=1 domain, L38's unique noncyclotomic factor and all finite cutoffs; MG89's odd-prime count and both characteristics; exact count of all sparse polynomials including constants, distinct factor multiplicities, floors and C<1; simultaneous finite-pool quantifiers; the one CRT coefficient vector, middle adjustment at an exact multiple of M, actual irreducibility, unit and separability; exact height/l1 costs and the all-circle positive identity with its fixed positive measure lower bound; L64's original local algebra, valuation proof of integrally closedness and maximal-order inclusion; positive content, gcd cancellation, q1=1, arbitrary prime powers, nonzero residue and the full polynomial divisibility contradiction.
No native computation, polynomial-factor search, numerical conclusion or independent review was performed in this author round.

<a id="finite-pool-entire-author-freeze"></a>
## Complete author freeze

At 2026-10-15T10:51 the entire Sections1--8, all14 displayed numbered formulas, source/reuse/contribution boundaries and exact far-from-one restriction are frozen for retention and a different noncontributor's whole review.
Root contributed the substantive Section6 content/maximal-order extension and is not eligible to be that independent reviewer.
The f author developed the odd-prime-count route, sparse-factor avoidance, symmetric CRT lift, exact coefficient and circle-cost analysis and the reuse assemblies, with the classical count credited to MG89.
This is author self-check only, not an adopted fixed theorem or unrestricted G0001 completion.

## Fixed organization

Retain the entire frozen author account, all14 numbered formulas, both exact reuse assemblies, simultaneous actual finite-prime construction, maximal-order/content proof, explicit far-from-one bound and complete source/contribution limits.
Root and f contributed and cannot independently review this new whole proof.

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T10:53 |
| status | open |
| reason | Retain the simultaneous finite-prime sparse-auxiliary obstruction for actual reciprocal units and exact earlier-result assemblies. The constructed inputs have a fixed positive Mahler floor; near-one coverage and G0001 remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire finite-pool statement](#statement) | Section3 all five properties and exact far-from-one range, with Sections1--2 separately stated reuse consequences. |
| argument | [Entire finite-pool proof](#argument) | Whole Sections1--8 and14 formulas, complete reuse, actual count/CRT/local-order costs and contribution boundaries. |
| dependency | [Exact input](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Section1 actual span/short-annihilator inequality and its inherited explicit threshold. |
| dependency | [Exact input](Yin_C_G0139_v1.md#statement) | Section1 bounded-term nonzero theorem and its actual positive constant. |
| dependency | [Exact input](Yin_C_G0137_v1.md#statement) | Section2 finite logarithmic nonzero linear-degree result and exact cutoff. |
| dependency | [Exact input](../ledger/Yin_L_G0038_v1.md#excess-three-family) | Section2 exact unique noncyclotomic Salem factor and finite expanding-root guard. |
| dependency | [Exact input](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Section2 bounded original-degree positive height floor. |
| dependency | [Exact input](../audits/literature/MG89/Yin_U001.md#mg89-u001) | Section4 accepted exact finite-field self-reciprocal irreducible count. |
| dependency | [Exact input](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Section6 actual good-prime power-basis DVR algebra; local integral closure proved explicitly. |
| dependency | [Exact input](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Original Mahler integral/root formula with integer content retained. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T11:03 |
| status | proved |
| reason | Adopt actual whole independent review of the same-input finite-prime sparse-auxiliary obstruction, full maximal-order/content extension and exact earlier-result assemblies. The constructed inputs have a fixed positive Mahler floor and no circle roots; near-one coverage remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire finite-pool statement](#statement) | Section3 all five properties and exact far-from-one range, with Sections1--2 separately stated reuse consequences. |
| argument | [Entire finite-pool proof](#argument) | Whole Sections1--8 and14 formulas, complete reuse, actual count/CRT/local-order costs and contribution boundaries. |
| dependency | [Exact input](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Section1 actual span/short-annihilator inequality and its inherited explicit threshold. |
| dependency | [Exact input](Yin_C_G0139_v1.md#statement) | Section1 bounded-term nonzero theorem and its actual positive constant. |
| dependency | [Exact input](Yin_C_G0137_v1.md#statement) | Section2 finite logarithmic nonzero linear-degree result and exact cutoff. |
| dependency | [Exact input](../ledger/Yin_L_G0038_v1.md#excess-three-family) | Section2 exact unique noncyclotomic Salem factor and finite expanding-root guard. |
| dependency | [Exact input](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Section2 bounded original-degree positive height floor. |
| dependency | [Exact input](../audits/literature/MG89/Yin_U001.md#mg89-u001) | Section4 accepted exact finite-field self-reciprocal irreducible count. |
| dependency | [Exact input](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Section6 actual good-prime power-basis DVR algebra; local integral closure proved explicitly. |
| dependency | [Exact input](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Original Mahler integral/root formula with integer content retained. |
| review | [Actual whole finding](../audits/reviews/Yin_R_G0801_v1.md#finite-prime-pool-whole-independent-finding) | Entire actual fixed argument and statement, every direct interface, original cost and boundary, with antecedent authorship and source-proof limits preserved. Referenced finding relationship: unknown. |

### Decision current-local-trace-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:51 |
| status | proved |
| reason | Select C241/C243 as the complete current responsible homes for the identical already used L64 unramified local or L66 reciprocal trace/order/module interfaces at the exact selected anchors below. The full original arguments, current extracted statements and used guards were read; this is same-content locator adoption. Status, selected statement/argument/finding, all relation scopes and every other current proof home remain unchanged. Prior dated decisions and R bindings keep their actual L64/L66 inputs; no new independent review, local assumption, cheaper entropy normalization or stronger arithmetic estimate is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Section3 all five properties and exact far-from-one range, with Sections1--2 separately stated reuse consequences. |
| argument | [Argument](#argument) | Whole Sections1--8 and14 formulas, complete reuse, actual count/CRT/local-order costs and contribution boundaries. |
| dependency | [Dependency](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Section1 actual span/short-annihilator inequality and its inherited explicit threshold. |
| dependency | [Dependency](Yin_C_G0139_v1.md#statement) | Section1 bounded-term nonzero theorem and its actual positive constant. |
| dependency | [Dependency](Yin_C_G0137_v1.md#statement) | Section2 finite logarithmic nonzero linear-degree result and exact cutoff. |
| dependency | [Dependency](../ledger/Yin_L_G0038_v1.md#excess-three-family) | Section2 exact unique noncyclotomic Salem factor and finite expanding-root guard. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Section2 bounded original-degree positive height floor. |
| dependency | [Dependency](../audits/literature/MG89/Yin_U001.md#mg89-u001) | Section4 accepted exact finite-field self-reciprocal irreducible count. |
| dependency | [Dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Section6 actual good-prime power-basis DVR algebra; local integral closure proved explicitly. |
| dependency | [Dependency](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Original Mahler integral/root formula with integer content retained. |
| review | [Review](../audits/reviews/Yin_R_G0801_v1.md#finite-prime-pool-whole-independent-finding) | Entire actual fixed argument and statement, every direct interface, original cost and boundary, with antecedent authorship and source-proof limits preserved. |

### Decision current-excess-three-family-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:25 |
| status | proved |
| reason | Select the complete retained C248 proof as the current responsible home for the identical previously used L38 Salem-family interface at exactly the selected anchors below. The original whole argument and the current complete retained proof were read, including the actual all-N factorization and the n>=16 expanding-root guard. This changes only the current proof locator; statement, argument, relation scopes, mathematical status, all other inputs and the actual original R finding remain unchanged. Historical decisions and reviews keep their actual fixed L38 targets, and no new independent review or stronger family theorem is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Section3 all five properties and exact far-from-one range, with Sections1--2 separately stated reuse consequences. |
| argument | [Argument](#argument) | Whole Sections1--8 and14 formulas, complete reuse, actual count/CRT/local-order costs and contribution boundaries. |
| dependency | [Dependency](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Section1 actual span/short-annihilator inequality and its inherited explicit threshold. |
| dependency | [Dependency](Yin_C_G0139_v1.md#statement) | Section1 bounded-term nonzero theorem and its actual positive constant. |
| dependency | [Dependency](Yin_C_G0137_v1.md#statement) | Section2 finite logarithmic nonzero linear-degree result and exact cutoff. |
| dependency | [Dependency](Yin_C_G0248_v1.md#excess-three-family) | Section2 exact unique noncyclotomic Salem factor and finite expanding-root guard. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Section2 bounded original-degree positive height floor. |
| dependency | [Dependency](../audits/literature/MG89/Yin_U001.md#mg89-u001) | Section4 accepted exact finite-field self-reciprocal irreducible count. |
| dependency | [Dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Section6 actual good-prime power-basis DVR algebra; local integral closure proved explicitly. |
| dependency | [Dependency](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Original Mahler integral/root formula with integer content retained. |
| review | [Review](../audits/reviews/Yin_R_G0801_v1.md#finite-prime-pool-whole-independent-finding) | Entire actual fixed argument and statement, every direct interface, original cost and boundary, with antecedent authorship and source-proof limits preserved. |

### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Section3 all five properties and exact far-from-one range, with Sections1--2 separately stated reuse consequences. |
| argument | [Exact retained argument](#argument) | Whole Sections1--8 and14 formulas, complete reuse, actual count/CRT/local-order costs and contribution boundaries. |
| dependency | [Exact retained dependency](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Section1 actual span/short-annihilator inequality and its inherited explicit threshold. |
| dependency | [Exact retained dependency](Yin_C_G0139_v1.md#statement) | Section1 bounded-term nonzero theorem and its actual positive constant. |
| dependency | [Exact retained dependency](Yin_C_G0137_v1.md#statement) | Section2 finite logarithmic nonzero linear-degree result and exact cutoff. |
| dependency | [Exact retained dependency](Yin_C_G0248_v1.md#excess-three-family) | Section2 exact unique noncyclotomic Salem factor and finite expanding-root guard. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Section2 bounded original-degree positive height floor. |
| dependency | [Exact retained dependency](../audits/literature/MG89/Yin_U001.md#mg89-u001) | Section4 accepted exact finite-field self-reciprocal irreducible count. |
| dependency | [Exact retained dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Section6 actual good-prime power-basis DVR algebra; local integral closure proved explicitly. |
| dependency | [Exact retained dependency](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Original Mahler integral/root formula with integer content retained. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0801_v1.md#finite-prime-pool-whole-independent-finding) | Entire actual fixed argument and statement, every direct interface, original cost and boundary, with antecedent authorship and source-proof limits preserved. |

### Decision isolated-whole-review-20261023-m04

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:52 |
| status | proved |
| reason | Select the newly performed whole finding on this exact fixed statement, complete argument and all selected input interfaces at their stated restricted scopes, with its actual self-reviewed relationship. Preserve the proved mathematical status, unchanged statement and argument, every nonreview relation and scope, and all historical decisions. The retained older unknown finding keeps its actual date, checks and limits; this new finding supplies new evidence at its actual date without certifying old isolation, backdating adoption, or completing or resuming G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Section3 all five properties and exact far-from-one range, with Sections1--2 separately stated reuse consequences. |
| argument | [Exact retained argument](#argument) | Whole Sections1--8 and14 formulas, complete reuse, actual count/CRT/local-order costs and contribution boundaries. |
| dependency | [Exact retained dependency](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Section1 actual span/short-annihilator inequality and its inherited explicit threshold. |
| dependency | [Exact retained dependency](Yin_C_G0139_v1.md#statement) | Section1 bounded-term nonzero theorem and its actual positive constant. |
| dependency | [Exact retained dependency](Yin_C_G0137_v1.md#statement) | Section2 finite logarithmic nonzero linear-degree result and exact cutoff. |
| dependency | [Exact retained dependency](Yin_C_G0248_v1.md#excess-three-family) | Section2 exact unique noncyclotomic Salem factor and finite expanding-root guard. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Section2 bounded original-degree positive height floor. |
| dependency | [Exact retained dependency](../audits/literature/MG89/Yin_U001.md#mg89-u001) | Section4 accepted exact finite-field self-reciprocal irreducible count. |
| dependency | [Exact retained dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Section6 actual good-prime power-basis DVR algebra; local integral closure proved explicitly. |
| dependency | [Exact retained dependency](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Original Mahler integral/root formula with integer content retained. |
| review | [New whole finding](../audits/reviews/Yin_R_G0801_v1.md#g0141-m04-isolated-whole-finding) | Complete exact fixed statement, whole argument, every selected input, all parameter/domain/original-degree costs, exceptional branches and source/noncompletion limits. Finding relationship: self-reviewed. |
