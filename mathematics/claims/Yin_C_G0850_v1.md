---
author: Yin
---

# Polynomial periodic-state counts and the exact distance-eight loop-rate criterion

Human author Yin.
Contributor jt26_source_check identified the retained logarithmic-form input, derived the complete-diagonal/fixed-state comparison and direct first-return injection, and assembled the proof.
Root supplied the detailed complete exterior-component argument, checked the proposed reduction and requested the whole strict-criterion equivalence.
Both are proof contributors; their checks are not an independent review of this new result.
This project deduction is [adopted](#decision-whole-reviewed-2026-10-28) after [whole independent R1070](../audits/reviews/Yin_R_G1070_v1.md#whole-periodic-trace-criterion-finding).
The [D9 PT section](../drafts/Yin_D_G0009.md#periodic-state-count-and-distance-eight-loop-rate) supplies extraction provenance only; the entire proof is fixed below.
The separate [Buzzi comparison](../drafts/Yin_D_G0009.md#entropy-at-infinity-source-boundary) is exploratory context, not a proof input.

## Statement

Fix q(X)=X^4-X^3-X^2-X+1, its real root beta>1, upper neutral conjugate zeta and O=Z[beta].
Use its actual original-digit accessible/coaccessible core D, with probabilities1/4,1/2,1/4 for digits-1,0,1 and transition x->beta*x+e.
All kernels retain original weights and chronological times; killing never renormalizes surviving rows.
Here d(x) is the shortest original legal word length from x to0, with d(0)=0, using C846's adopted convention.
Let P_D be that original kernel, p_n=P_D^n(0,0), f_n its first-positive-return probabilities, R the radius of sum_(n>=0)p_n z^n and R_f the radius of F(z)=sum_(n>=1)f_n z^n.
All logarithms are natural.
Let kappa>=1 be a constant admitted by the exact accepted Dim16 interface in PT1, put A=64 kappa log4, and use C790's C_D=A^+_(w,0)>0 with N(r)<=C_D(r+2)^2.
No numerical value of kappa or optimization is asserted.
Then all the following hold.

1. For every integer n>=2, L_n={x in D:P_D^n(x,x)>0} satisfies

       |x(zeta)|<=n^(A+1), x in L_n,
       card L_n<=C_D(n^(A+1)+2)^2<=9 C_D n^(2A+2).

   This bounds all original periodic states without a finite radius search.
2. For every subset K of D, define B_K as the original kernel killed outside G_K=D minus K and use the [exact rates](#deleted-loop-rates)

       r_K(x)=limsup_n B_K^n(x,x)^(1/n),
       r_*(K)=sup_(x in G_K)r_K(x),
       d_n(K)=sum_(x in G_K)B_K^n(x,x),
       alpha_K=limsup_n d_n(K)^(1/n).

   Empty suprema and identically zero rates are0.
   Every d_n(K) is finite, and

       B_K^n(x,x)<=(r_K(x))^n, n>=1,
       d_n(K)<=9 C_D n^(2A+2)(r_*(K))^n, n>=2,
       alpha_K=r_*(K).

   Constants do not depend on K; r_*(K)=0 forces every positive-length diagonal coefficient to vanish.
3. For the actual K8={x in D:d(x)<=8}, including0, its ENTIRE exterior consists of one infinite true communicating class C and eight acyclic singleton classes Z:

       D minus K8=C disjoint-union Z,
       Z={51,52,59,68,72,85,88,105}.

   IDs denote the exact tuples below and C846's accepted convention.
   C contains I={47,48,49,50,53,54,55,56,75,82}; it is the full exterior outside Z, not the finite417-state induced component.
   Every x in C has the same fixed-state rate r_I=r_K8(47), and alpha_K8=r_I.
4. For every K containing0, alpha_K<=1/R_f, with1/infinity=0.
   This follows by a direct original first-return injection, without adopting D49 CL6 as a premise.
5. The following strict criteria are equivalent for this actual K8:

       R_f>R
         iff alpha_K8<1/R
         iff r_I<1/R
         iff some t_*>R satisfies
             D_K8(t_*)=sum_(n>=1)t_*^n d_n(K8)<infinity.

   None of these equivalent strict properties is established by the equivalence.
   Finite critical mean alone is not asserted equivalent to them.
   No inequality R_f>=1/alpha_K follows; for positive alpha_K the proved bound instead gives R_f<=1/alpha_K.

### Exact state and input convention

Ascending tuples mean coefficients of1,beta,beta^2,beta^3.
C846's [complete adopted boundary](Yin_C_G0846_v1.md#actual-domain-and-complete-boundary) supplies the ID map and all required complete local rows and connectors, without a new native run.

| ID | Actual tuple | ID | Actual tuple |
| --- | --- | --- | --- |
| 51 | (0,-1,2,-1) | 52 | (0,1,-2,1) |
| 59 | (-2,1,-2,1) | 68 | (2,-1,2,-1) |
| 72 | (-2,2,1,-1) | 85 | (2,-2,-1,1) |
| 88 | (-2,0,2,-1) | 105 | (2,0,-2,1) |

Anchor47 is(-2,-1,3,-1).
The adopted inputs and their actual mathematical/native/source limits are specified completely in PT1.
No new graph, program, state enumeration, external theorem proof audit, numerical transcendence constant or unconditional radius/mean classification is claimed.

## Complete argument

<a id="exact-inputs-and-logarithmic-form-scope"></a>
### PT1. Exact inputs and fixed-polynomial scope

Keep the actual quartic q(X)=X^4-X^3-X^2-X+1, its real root beta>1, upper neutral conjugate zeta and original law with digit probabilities1/4,1/2,1/4.
[Adopted C396](Yin_C_G0396_v1.md#statement) and [C400's adopted exact strip](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) supply irreducibility, the Salem root configuration, beta<2 and the actual accessible/coaccessible core D.
[Adopted C546](Yin_C_G0546_v1.md#decision-complete-isolated-whole-adoption) supplies the unique fixed starting point of a nonempty word and the original p_n, first-return f_n, F(z)=sum_(n>=1)f_n z^n and complete-return radius R conventions.
Write R_f for the radius of F.
[Adopted C790](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26), UC1, supplies the upper count
N(r)<=C_D(r+2)^2 for all r>=0, where C_D=A^+_(w,0)>0 and N(r)=card{x in D:|x(zeta)|<=r}.
Only this upper count is used, not the sharp density or probability bounds.
[Adopted C846](Yin_C_G0846_v1.md#decision-whole-reviewed-2026-10-28) supplies the entire K8 boundary, special rows, positive connectors and conditional critical transfer.
These interfaces are reused at their accepted scopes without rerunning earlier native work.

The sole transcendence input is the already inspected and accepted [Dim16 reported logarithmic-form bound](../audits/literature/Dim16/Yin_U001.md#dim16-reported-bound), equation(1) there.
Its original Baker--Wustholz proof and numerical absolute constant remain outside the source inspection.
For a nontorsion algebraic number gamma of degree D_0>=2 and h(gamma)<=1, and n>=2, that interface gives
-log|gamma^n-1|<=kappa D_0^4 log(D_0) max{h(gamma),1/D_0} log n,
with a fixed admitted absolute kappa>=1, not a newly calibrated numerical constant.

Here zeta has degree4 and is nontorsion: a root-of-unity conjugate of irreducible q would force beta to be a root of unity.
Its absolute logarithmic Weil height is log(beta)/4<1/4, since the full root configuration has Mahler measure beta<2.
Thus the source applies to gamma=zeta, D_0=4 and n>=2, with

    A=64 kappa log4,
    |1-zeta^n|>=n^(-A), n>=2.                          (PT1)

No estimate at n=1 is inferred from the source's log n expression, and no uniform assertion over varying polynomials is made.

<a id="polynomial-periodic-state-count"></a>
### PT2. Polynomially many starting states of a periodic word

Let L_n={x in D:P_D^n(x,x)>0}, for n>=1.
A length-n original word w=(e_1,...,e_n) returning to x satisfies, in the neutral embedding,

    (1-zeta^n)x(zeta)=sum_(j=1)^n e_j zeta^(n-j).

The modulus of the right side is at most n, so PT1 gives |x(zeta)|<=n^(A+1) for n>=2.
C790's complete lattice count therefore gives

    card L_n<=C_D(n^(A+1)+2)^2
             <=9 C_D n^(2A+2), n>=2.                  (PT2)

This counts distinct actual starting states, not words, and includes all integral original periodic states without a finite height search.
The finite n=1 case is already covered by C546's unique-fixed-word bound and is irrelevant to the limiting exponent.
The constant and polynomial exponent may be very large and are not numerically evaluated.

<a id="complete-diagonal-and-fixed-state-rates"></a>
### PT3. Complete diagonal growth equals the supremum of fixed-state loop rates

<a id="deleted-loop-rates"></a>
**Definition (complete deleted-diagonal and fixed-state loop rates).**
For any subset K of D, let G_K=D minus K, let B_K be the original kernel killed outside G_K, and define

    b_n^K(x)=B_K^n(x,x), x in G_K, n>=1,
    r_K(x)=limsup_(n->infinity)(b_n^K(x))^(1/n),
    r_*(K)=sup_(x in G_K)r_K(x),
    d_n(K)=sum_(x in G_K)b_n^K(x),
    alpha_K=limsup_(n->infinity)d_n(K)^(1/n).           (PT3)

The supremum over an empty set is0, as are the rates of identically zero sequences.
These are original-weight closed-path rates, not operator norms.
All d_n(K) are finite by C546, and their nonzero starting states form a subset of L_n, uniformly in K.

For each fixed x and n, concatenating k allowed length-n loops at x gives

    b_(kn)^K(x)>=(b_n^K(x))^k, k>=1,
    b_n^K(x)<=(r_K(x))^n<=(r_*(K))^n.                 (PT4)

The second line follows by taking the subsequence kn in the defining limsup.
If r_*(K)>0, PT2 yields d_n(K)<=9 C_D n^(2A+2)(r_*(K))^n for n>=2, hence alpha_K<=r_*(K).
Conversely d_n(K)>=b_n^K(x) for each fixed x gives alpha_K>=r_K(x), and taking the supremum gives the reverse inequality.
If r_*(K)=0, PT4 forces every positive-length diagonal coefficient to vanish, so d_n(K)=0 and alpha_K=0.
Therefore

    alpha_K=sup_(x in G_K)r_K(x)                      (PT5)

for EVERY subset K, in particular for every finite deletion.
The upper-bound constants in PT2 do not depend on K.
This uses the specific algebraic periodic-state count; a generic countable graph does not acquire this conclusion from a local entropy or zeta theorem alone.

<a id="whole-distance-eight-exterior-component"></a>
### PT4. The complete exterior component structure at distance eight

Now put K=K8={d<=8}, G=D minus K8, and use C846's exact ID convention.
Let

    Z={51,52,59,68,72,85,88,105},
    I={47,48,49,50,53,54,55,56,75,82},

and let C be the true G communicating class containing I, whose mutual positive paths are fixed in C846.
Then

    G=C disjoint-union Z.                            (PT6)

To prove completeness, take any x in G minus Z.
Since x is an actual accessible/coaccessible core state, a finite original0-to0 word contains x.
Choose the last K8 visit before that occurrence and the first K8 visit after it.
The intervening segment is an actual G path u->x->v with u in U and v in V, and every point of this segment stays outside K8.

C846's complete rows imply that an excursion beginning at51 or52 immediately returns to K8; one beginning at59 or68 has at most the two exterior states(59,51) or(68,52).
Such a segment cannot contain x outside Z.
Every other entrance either starts at75 or82 in I, or starts at one of72,85,88,105 and takes its first step to one of61,66,74,83,113,122.
All six targets lie in C by C846's positive two-way connectors.
Because x is not the source itself, the segment therefore gives a path from C to x.

If its terminal v were51, its only G predecessor would be59, and59 has no G predecessor.
Thus any G path ending at51 is confined at its beginning to59 or51 and cannot contain x outside Z.
The same argument applies to52 and68.
Consequently v is in V intersect I, and the segment gives x->I.
Together the two directions put x in C.
Conversely every element of Z has either no G predecessor, no G successor, or only its one-step route to a terminal sink, so C846's complete rows rule out a positive return and exclude it from C.
This proves PT6 without enumerating any additional exterior vertex.
C is infinite because C396's accepted actual-core result gives infinite D and only the finite sets K8 and Z were removed.

For any x,y in C choose fixed positive G paths x->y and y->x.
Their concatenation with an arbitrary loop at y gives c B_K^n(y,y)<=B_K^(n+ell)(x,x), with fixed c>0 and ell.
Taking root limsups and reversing x,y proves equality of their fixed-state rates.
All eight states in Z have zero positive-length diagonal coefficients.
Using anchor47, put r_I=r_K(47); then PT5 and PT6 give

    alpha_K8=r_I
       =limsup_(n->infinity)B_K8^n(x,x)^(1/n),
                                      EVERY x in C.   (PT7)

This is a whole-graph consequence of complete boundary gates and accessibility/coaccessibility, not a claim that the417 supplied vertices enumerate C.

<a id="first-return-injection-and-strict-equivalence"></a>
### PT5. Direct first-return injection and the precise equivalence

Suppose0 belongs to K and x belongs to D minus K.
Choose a finite positive original0->x word with no intermediate0, by taking the suffix after the last zero of a0->x word.
Choose a finite positive original x->0 first-hit word by stopping a continuation at its first zero.
Let their combined length and probability be L_x and c_x>0.
Concatenating these fixed words with any length-n B_K loop at x gives a first-positive-return word to0, since the middle avoids K and therefore0.
The map is injective at each fixed n, retains all original weights and times, and gives

    c_x B_K^n(x,x)<=f_(n+L_x).                        (PT8)

By the power-series root test, limsup_m f_m^(1/m)=1/R_f, with the usual1/infinity=0 convention.
The fixed shift and multiplier in PT8 imply r_K(x)<=1/R_f.
PT5 therefore gives

    alpha_K<=1/R_f for EVERY K containing0.           (PT9)

No unadopted D49 CL6 statement or whole deleted-zero irreducibility argument is used.

For the actual K8, adopted C846 proves alpha_K8<1/R implies R_f>R.
Conversely R_f>R and PT9 give alpha_K8<=1/R_f<1/R.
The root test also identifies alpha_K8<1/R with existence of a t_*>R for which the complete D_K8(t_*) converges.
Together with PT7,

    R_f>R
      iff alpha_K8<1/R
      iff r_I<1/R
      iff some t_*>R satisfies D_K8(t_*)<infinity.     (PT10)

The supplied inequalities prove no one of these equivalent strict properties.
Finite critical mean alone is not asserted equivalent to them.
PT9 is an upper bound on alpha_K, and does not imply R_f>=1/alpha_K.
A finite-core coupling pole below1/alpha_K remains compatible with the proof.
The result sharpens the exact remaining original-weight closed-loop question; it supplies neither an actual diagonal estimate nor an unrestricted G0001 conclusion.
Root read this entire author argument and the directly used Dim16/C790/C396 interfaces before fixation.
The [selected adoption](#decision-whole-reviewed-2026-10-28) uses [whole independent R1070](../audits/reviews/Yin_R_G1070_v1.md#whole-periodic-trace-criterion-finding) for these new deductions; C846's prior review retains its original scope.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision periodic-trace-equivalence-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T23:38 |
| status | open |
| reason | Fix the whole polynomial periodic-state bound, every-deletion diagonal/fixed-state rate identity and zero case, complete actual K8 infinite-component classification, direct first-return upper bound and exact strict-criterion equivalence. Root/contributor whole author checks and exact accepted interfaces are retained; fresh whole independent review and adoption remain outstanding. No actual strict-rate estimate, mean classification, new native calculation or numerical Baker constant is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | All fixed-quartic periodic-state counts, every subset K with conventions, whole K8 component, alpha_K upper bound for0 in K, exact strict equivalence and all source/numerical/radius limits. |
| argument | [Complete argument](#complete-argument) | Entire PT1--PT5/PT1--PT10: exact logarithmic-form applicability, complete periodic-state count, loop concatenation and zero case, actual U-to-V global component proof, direct first-return injection and C846 conditional assembly. |
| dependency | [Dim16 accepted source unit](../audits/literature/Dim16/Yin_U001.md#dim16-u001) | Only its exact reported-bound interface, equation1: n>=2, bounded Weil height, degree4 and admitted nonnumerical kappa; no original Baker--Wustholz proof audit or exponent-one use. |
| dependency | [C790 adopted count](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26) | UC1 at k=0 and delta_c=2 gives N(r)<=C_D(r+2)^2; no sharp density or probability-bound premise. |
| dependency | [C546 adopted periodic/return interface](Yin_C_G0546_v1.md#decision-complete-isolated-whole-adoption) | Unique nonempty-word affine fixed point, complete finite diagonal, original f_n/F and complete return radius; no existing strict-tail premise. |
| dependency | [C846 adopted exact K8 input](Yin_C_G0846_v1.md#decision-whole-reviewed-2026-10-28) | Complete K/U/V/A, eight special rows/exclusions, six target connectors, boundary communication and paid diagonal-to-strict-critical implication, with accepted native scope unchanged. |
| dependency | [C396 actual-core input](Yin_C_G0396_v1.md#statement) | Fixed quartic irreducible Salem configuration, beta<2, accessible/coaccessible interpretation and infinite actual core, at its existing accepted native/review scope. |
| dependency | [C400 adopted strict strip](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Exact actual fixed-quartic strip equality and original order, with no all-Salem extension. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T23:51 |
| status | proved |
| reason | Adopt the complete Statement and PT1--PT5/PT1--PT10 after root read the entire author proof, fixed statement, directly used Dim16/C790/C396 interfaces and whole independent R1070. The complete polynomial periodic-state bound, every-deletion diagonal/fixed-state identity including zero and empty cases, whole K8 infinite-component classification, direct original first-return injection and exact strict-criterion equivalence are covered. C396 SELF/native and the reported Baker--Wustholz source limits remain unchanged. No actual strict-rate estimate, numerical transcendence constant, unconditional mean classification or unrestricted conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | All fixed-quartic periodic-state counts, every subset K with conventions, whole K8 component, alpha_K upper bound for0 in K, exact strict equivalence and all source/numerical/radius limits. |
| argument | [Complete argument](#complete-argument) | Entire PT1--PT5/PT1--PT10: exact logarithmic-form applicability, complete periodic-state count, loop concatenation and zero case, actual U-to-V global component proof, direct first-return injection and C846 conditional assembly. |
| dependency | [Dim16 accepted source unit](../audits/literature/Dim16/Yin_U001.md#dim16-u001) | Only its exact reported-bound interface, equation1: n>=2, bounded Weil height, degree4 and admitted nonnumerical kappa; no original Baker--Wustholz proof audit or exponent-one use. |
| dependency | [C790 adopted count](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26) | UC1 at k=0 and delta_c=2 gives N(r)<=C_D(r+2)^2; no sharp density or probability-bound premise. |
| dependency | [C546 adopted periodic/return interface](Yin_C_G0546_v1.md#decision-complete-isolated-whole-adoption) | Unique nonempty-word affine fixed point, complete finite diagonal, original f_n/F and complete return radius; no existing strict-tail premise. |
| dependency | [C846 adopted exact K8 input](Yin_C_G0846_v1.md#decision-whole-reviewed-2026-10-28) | Complete K/U/V/A, eight special rows/exclusions, six target connectors, boundary communication and paid diagonal-to-strict-critical implication, with accepted native scope unchanged. |
| dependency | [C396 actual-core input](Yin_C_G0396_v1.md#statement) | Fixed quartic irreducible Salem configuration, beta<2, accessible/coaccessible interpretation and infinite actual core, at its existing accepted native/review scope. |
| dependency | [C400 adopted strict strip](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Exact actual fixed-quartic strip equality and original order, with no all-Salem extension. |
| review | [Whole independent periodic-trace criterion finding](../audits/reviews/Yin_R_G1070_v1.md#whole-periodic-trace-criterion-finding) | Entire Statement/PT1--PT5, all ten formulas, state conventions and six exact dependency scopes, every-deletion/zero/infinite-component and original-weight/time argument, strict equivalence and correct radius directions, preserving source/native/SELF evidence limits. |

