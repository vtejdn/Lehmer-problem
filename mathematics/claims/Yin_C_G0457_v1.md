---
author: Yin
---

# Complete trace-field unit-sign obstruction and unbounded-degree bounded-measure Salem family

This retains the complete necessary mathematical argument from [the complete original G386 argument and source account](../ledger/Yin_L_G0386_v1.md).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

For an actual genuine Salem field K=Q(alpha) of original degree d=2s>=4, trace field F=Q(alpha+alpha^-1), inverse automorphism sigma and full integer rings O_K,O_F, assume every O_F unit has signed full norm+1.
Then every O_K unit has signed full K/Q norm+1; its relative norm u sigma(u) is an O_F unit, strictly positive at every original trace embedding, with product1.
The accepted positive-full-norm comparison consequently gives E>=1 for every finite normalized nonnegative constant unit profile explicitly identical at all original trace embeddings, also for maximal-order units.
For positive rational coefficients, a field identity sum lambda_i u_i sigma(u_i)=b inQ implies b>=sum lambda_i.
For arbitrary real coefficients the same all-embedding equation is an explicit hypothesis; a lone equality is not conjugated through real weights.
In particular u sigma(u)+2v sigma(v)=1 is impossible for any actual unit pair, at any signed/independent monomial twist or window/scalar denominator.
A negative-norm trace-field unit is not conversely sufficient for a relative norm or affine lift.

The full quadratic integer ring O_(Qsqrt3)=Z[sqrt3] and the norm equation x²-3y²=-1 has no integral solution by reduction modulo3, hence all its units have norm+1.
The exact input Q=x²-2x-2, P=t4-2t³-2t+1=t²Q(t+t^-1) is irreducible genuine Salem, with all four distinct roots and beta=(1+sqrt3+sqrt(2sqrt3))/2>2.
Its trace order B=Z[tau]=Z[sqrt3]=O_F, actual order O=B direct_sum alphaB and O intersectionF=B, without asserting O=O_K or computing that index.
The theorem excludes the constant unit profile even in O_K.
The tempting distinct seeds have full N_F(tau)=-2, N_K(tau)=4, N_K(1-alpha)=-2, N_K((1-alpha)^-1)=-1/2; the latter is not integral, their relative weighted sum is tau+2 rather than1, and their old unit/norm labels cannot be imported.
Rational norm-one vectors regular at all original roots with both residues actual units are excluded by evaluation; all rational columns or nonunit residues are not excluded.

There is also the following complete family, indexed by every integer n>=1.
Put a=1+sqrt3,a'=1-sqrt3, U0=1,U1=x,U_n=xU_(n-1)-U_(n-2), q_n=U_n-aU_(n-1), q'_n=U_n-a'U_(n-1) (the prime denotes coefficient conjugation), and Q_n=q_n q'_n=(U_n-U_(n-1))²-3U_(n-1)².
They are the actual characteristic polynomials of the finite symmetric path matrices J_n(a),J_n(a') with first diagonal b, remaining diagonals0 and neighboring entries1.
All eigenvalues are simple with nonzero endpoint eigenvectors; all q'_n roots and all but one q_n root lie strictly in(-2,2).
The unique exterior trace x_n satisfies x1=a and, for n>1, a<x_n<a+a^-1.
It strictly increases to a+a^-1, by explicit finite quadratic forms and trial vectors; q_n and q'_n have no common root.

The full squarefree parent Pcal_n=t^(2n)Q_n(t+t^-1) is monic integral reciprocal of degree4n and constant1, with exactly one exterior/interior pair alpha_n,alpha_n^-1.
Let p_n be the actual minimal polynomial of alpha_n, d_n its actual degree, K_n=Q(alpha_n) and F_n=Q(x_n).
Its unit constant term forces inclusion of the sole interior root, hence p_n is reciprocal and has constant1.
The exact nonzero-denominator expression sqrt3=(U_n(x_n)-U_(n-1)(x_n))/U_(n-1)(x_n) gives Qsqrt3 contained inF_n, and[K_n:F_n]=2.
Thus p_n is genuinely Salem, d_n>=4 and4 divides d_n, but d_n is not assigned the parent degree4n.
The complete cofactor C_n=Pcal_n/p_n is squarefree cyclotomic, possibly1, of actual degree4n-d_n and measure1; all parent values and costs retain it.
In particular 1-3n²=Pcal_n(1)=p_n(1)C_n(1), and the parent integer is not automatically a field norm.

The actual exterior roots strictly increase with2<alpha1<=alpha_n<a and alpha_n->a.
All total measures are uniformly bounded and stay above2; bounded actual degrees on any infinite subsequence would violate finite integer coefficient bounds, so d_n tends to infinity.
Relative norm towers through Qsqrt3 give signed full norm+1 to every maximal-order unit of each F_n and K_n.
The same exact constant unit profile is excluded at every actual original p_n, with every conjugate, sign and monomial cost retained.
Its original field norm p_n(1) is negative and cannot be-1, hence p_n(1)<=-2; this is not a fabricated formula after dropping C_n(1).
The conclusion demonstrates failure of universal constant-unit-profile coverage at unbounded actual degree, while its total measures do not approach1.
It excludes no nonconstant/approximate profile, general unit inequality, nonunit auxiliary, arbitrary different-weight mechanism or unrestricted gap.
All finite path, arithmetic, factor and limit arguments are explicit; no numerical eigensolver, factorization list, field-index/unit/class-number algorithm, native run or new research execution is used.
## Current assessment
[Selected decision](#decision-complete-trace-sign-family-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:12 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted all-positive full-unit constant-profile comparison](Yin_C_G0407_v1.md#mixed-signed-unit-constant-obstruction) | Only genuine-Salem positive full norms, normalized common all-embedding profile and trace product-one inequality E>=1; the maximal-order interface/sign criterion and new family are proved here. |
| dependency | [Complete original reciprocal field and trace convention](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Only [K:F]=2, actual inverse pairs and all original/trace degree distinction, applied to each actual irreducible Salem factor, not its reducible parent. |
| dependency | [Actual monogenic-order module convention](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | Only B direct_sum alphaB, actual order/intersection convention and no asserted maximal-order equality; the specific B=O_F and full-unit argument are proved here. |
| dependency | [Exact quadratic integer and signed-unit-norm source](../audits/literature/Con26b/Yin_U001.md#con26b-u001) | Undated24-page Conrad note selected definitions/theorems/proofs pp2–4 at their recorded original reading depth; complete sqrt3 specialization local, no class-number/unit algorithm. |
| dependency | [Exact finite symmetric spectral and Rayleigh facts](../audits/literature/Bin22/Yin_U001.md#bin22-u001) | Actual2022-10-27 eight-page lecture, p1/pp3–4 elementary statements/displayed arguments; all path-specific strictness/rootcount/limit steps local, no infinite Jacobi/interlacing theorem. |
| dependency | [Exact accepted Kronecker/normalization interface](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only monic integer measure-one/circle-factor characterization at its original accepted statement/source-depth; no new original proof or survey audit. |


### Decision complete-trace-sign-family-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:14 |
| status | proved |
| reason | Adopt the complete exact trace-field sign criterion, fixed original quartic and actual unbounded-degree bounded-measure Salem family after full SELF reconstruction, retaining all source, root/cofactor/actual-degree/constant-profile and alternative-method limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0407_v1.md#mixed-signed-unit-constant-obstruction) | Only genuine-Salem positive full norms, normalized common all-embedding profile and trace product-one inequality E>=1; the maximal-order interface/sign criterion and new family are proved here. |
| dependency | [Exact accepted input](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Only [K:F]=2, actual inverse pairs and all original/trace degree distinction, applied to each actual irreducible Salem factor, not its reducible parent. |
| dependency | [Exact accepted input](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | Only B direct_sum alphaB, actual order/intersection convention and no asserted maximal-order equality; the specific B=O_F and full-unit argument are proved here. |
| dependency | [Exact accepted input](../audits/literature/Con26b/Yin_U001.md#con26b-u001) | Undated24-page Conrad note selected definitions/theorems/proofs pp2–4 at their recorded original reading depth; complete sqrt3 specialization local, no class-number/unit algorithm. |
| dependency | [Exact accepted input](../audits/literature/Bin22/Yin_U001.md#bin22-u001) | Actual2022-10-27 eight-page lecture, p1/pp3–4 elementary statements/displayed arguments; all path-specific strictness/rootcount/limit steps local, no infinite Jacobi/interlacing theorem. |
| dependency | [Exact accepted input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only monic integer measure-one/circle-factor characterization at its original accepted statement/source-depth; no new original proof or survey audit. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0663_v1.md#current-trace-sign-family-whole-finding) | Entire exact Statement/Argument and original Sections1–9/equations1–17, every original/maximal-order unit, full factor/measure/sign/source/cost and no-native/near-one limitation. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="complete-trace-sign-salem-family-obstruction"></a>
<a id="trace-sign-source-and-reuse"></a>
## 1. Reuse, source inspection and the actual order boundary

The accepted [L372 positive-full-norm constant-profile obstruction](Yin_C_G0407_v1.md#mixed-signed-unit-constant-obstruction) is the required analytic/algebraic inequality and is reused, not reproved as a new trace bound.
Its exact premise is a genuine Salem input, all chosen unit full norms +1, normalized nonnegative weights and the SAME constant profile at every original trace embedding.
Its conclusion is E>=1.
The successful mixed-sign quartic in L372 is a different polynomial; no unit or coefficient identity is transferred to the present candidate by similarity of notation.

The [L66 trace field/order interface](Yin_C_G0243_v1.md#reciprocal-trace-domain) and [order decomposition](Yin_C_G0243_v1.md#reciprocal-trace-order-index) preserve the reciprocal involution, original degree and distinction between Z[alpha] and the full ring of integers.
A bounded local search by quadratic integers, integral bases, sqrt(3), rings of integers and unit norms did not supply the precise quadratic-ring source needed here.
The existing Conrad unit-theorem source is a different document and is not substituted for it.

For the recognized standard quadratic-integer statement, the author directly read Keith Conrad, [Factoring in Quadratic Fields](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/quadraticgrad.pdf), the current 24-page author-hosted note, Definition 3.1 and Theorem 3.4 with its full proof on printed/PDF pp.2--3, Theorem 3.5 on p.3, and Theorem 3.9 with its proof on p.4.
The statements give the quadratic integer ring and the unit criterion by norm; the squarefree radicand 3 lies in the d not congruent to 1 modulo 4 case.
This is a selected source/proof inspection and standard attribution, not a whole-note or ideal-factorization audit.
No document date is inferred from a crawl timestamp.
The complete d=3 arithmetic is also supplied directly below, so no uninspected unit-group classification, class number, Pell solution theorem or maximal-order computation in K is a premise.
Canonical source navigation is [Con26b-U001](../audits/literature/Con26b/Yin_U001.md#con26b-u001).

For the later finite-matrix extension, the author read David Bindel, Cornell CS6210, *Matrix Computations*, [2022-10-27 lecture notes](https://www.cs.cornell.edu/courses/cs6210/2022fa/lec/2022-10-27.pdf), the 8-page version: Section 1, PDF p.1, gives real spectrum, orthogonal eigendecomposition and the displayed finite-dimensional arguments; Section 2, PDF pp.3--4, gives the Rayleigh extremum and variational arguments.
Section 3 Theorem 1 and its proof on p.5 were also read, but the local proof below uses only the preceding elementary spectral/Rayleigh facts and direct quadratic forms.
No general Jacobi, orthogonal-polynomial or interlacing theorem is imported without its hypotheses.
This is selected inspection, not a whole-notes audit or a new spectral theorem.
Canonical source navigation is [Bin22-U001](../audits/literature/Bin22/Yin_U001.md#bin22-u001); this adds no mathematical premise or inspection scope.
The accepted [Smy08 normalization/Kronecker account](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) supplies the measure-one cyclotomic-factor characterization at its recorded source depth and the bounded-degree coefficient-finiteness interface.

The contrasting successful fixed quartic lift is now [L384](Yin_C_G0453_v1.md).
Its actual unit/norm identities remain specific to that input.
The present failure of constant-unit-profile coverage does not modify that construction.

The general fact that the norm of an algebraic integer is integral follows by multiplying its conjugates; a unit and its inverse give mutually inverse integer norms.
Relative conjugation preserves integrality.
These elementary interfaces are used with their actual fields and all embeddings below.
There is no replacement of a signed full norm by its absolute value before the sign argument.

<a id="trace-field-sign-transfer-criterion"></a>
## 2. A general criterion that reuses the accepted constant-profile obstruction

Let P be an actual monic irreducible genuine Salem polynomial of degree d=2s>=4, alpha one root, K=Q(alpha), F=Q(alpha+alpha^-1), and sigma(alpha)=alpha^-1.
Let O_K,O_F be the full rings of integers.
Assume

    Norm_(F/Q)(O_F^times) is contained in {+1}.       (1)

For EVERY u in O_K^times, its relative norm c=u sigma(u) is in O_F^times: both c and its reciprocal are integral and belong to F.
The complete norm tower, equivalently the product over all original inverse pairs, gives

    Norm_(K/Q)(u)=Norm_(F/Q)(u sigma(u))=+1.          (2)

In particular (2) holds for every unit of the actual order O=Z[alpha] or of any other order contained in O_K.
No equality of those orders is assumed.

At the s-1 circle trace embeddings, c is |u(z)|^2>0.
Its remaining trace value is positive as well, since the full product is +1.
Thus c meets exactly L372's totally-positive/full-norm-one trace interface.
That accepted comparison applies to any finite normalized constant profile of these units and monomials and gives E>=1.
Its trace step uses only the just-checked positivity, full norm and all-embedding constant identity, so the same interface also covers maximal-order units; no residual representative or power-basis integrality is needed in that trace step.
This is reuse of the existing inequality, not a new arithmetic/geometric-mean proof.

For example, for positive rational weights lambda_i and actual maximal-order units u_i, an identity in F of the form

    sum_i lambda_i u_i sigma(u_i)=b in Q

forces b>=sum_i lambda_i after normalization.
All embeddings see the same rational coefficients.
With arbitrary real weights the conclusion is used only when the constant profile is explicitly assumed at every embedding, as in L372; conjugating a single equality with arbitrary real coefficients is not asserted.

In particular

    u sigma(u)+2v sigma(v)=1                        (3)

would give normalized weights 1/3,2/3 and E=1/3, contradicting E>=1.
The criterion is sufficient only.
Existence of a negative-norm unit in F would not by itself guarantee that it is a relative norm from K, participates in a suitable affine identity, or has a rational Laurent lift.

<a id="sqrt-three-maximal-integer-ring-and-norm-sign"></a>
## 3. Full quadratic integer ring and the absence of negative-norm units

Take F=Q(sqrt(3)).
Here is the complete elementary specialization of the checked standard source statement.
If w=x+y sqrt(3), x,y rational, is integral, its trace A=2x and norm N=x^2-3y^2 are integers.
Hence 3(2y)^2=A^2-4N is an integer.
For 2y=a/b in lowest terms, b^2 divides the squarefree integer 3, so b=1.
Put B=2y in Z.
Integrality of the norm requires

    A^2-3B^2 is divisible by 4.

If B were odd this would force A^2 congruent to 3 modulo 4, impossible.
Hence B is even, and the same congruence forces A even.
Thus x,y are integers.
Conversely every x+y sqrt(3) with integer x,y is a root of its monic integer trace/norm quadratic.
This proves

    O_F=Z[sqrt(3)].                                 (4)

For a unit x+y sqrt(3), the signed norm is x^2-3y^2=+1 or -1.
The negative case would imply x^2 congruent to -1 modulo 3, impossible.
Therefore

    Norm_(F/Q)(O_F^times)={+1}.                     (5)

The set is nonempty, for example 1 and 2+sqrt(3) are units of norm +1.
No classification of all solutions of the positive Pell equation is needed.
Crucially (4) is the FULL integer ring, so (5) does not miss units represented with half-integral coordinates or in an unexamined overorder.

<a id="actual-salem-control-over-sqrt-three"></a>
## 4. The actual quartic is irreducible, reciprocal and genuinely Salem

Use the exact root-supplied polynomial and trace polynomial

    Q(x)=x^2-2x-2,
    P(t)=t^4-2t^3-2t+1=t^2 Q(t+t^-1),
    tau_+=1+sqrt(3), tau_-=1-sqrt(3).                (6)

The trace field is F=Q(sqrt(3)), and Q is irreducible over Q.
Over F, alpha obeys alpha^2-tau_+ alpha+1=0.
Its discriminant is tau_+^2-4=2sqrt(3), whose other real conjugate is -2sqrt(3)<0.
A square in a totally real field cannot have a negative real conjugate.
Thus this quadratic is irreducible over F.
Since tau_+=alpha+alpha^-1 belongs to Q(alpha), the tower has [K:Q]=4, and the displayed degree-four P is the actual irreducible minimal polynomial.

The trace tau_+ exceeds 2, giving two distinct positive reciprocal real roots beta,beta^-1, beta>1.
The other trace lies in (-1,0), giving two distinct nonreal unit-circle roots.
All four roots are distinct.
Since P is irreducible and has beta>1, the circle pair cannot consist of roots of unity.
P is monic with constant coefficient 1, so alpha is an algebraic integer unit with full norm +1; inversion is its nontrivial reciprocal automorphism over F.
This verifies every genuine Salem hypothesis used in Section 2.

The actual total Mahler measure is M(P)=beta, where

    beta=(1+sqrt(3)+sqrt(2sqrt(3)))/2.

In fact beta>2 because tau_+>5/2 and y+y^-1 increases for y>1.
Therefore m(P)>log 2.
This is one fixed positive-measure control, not a near-one family.

The polynomial relation gives alpha^-1=2+2alpha^2-alpha^3, so tau=alpha+alpha^-1 lies in O=Z[alpha].
Its trace order is

    B=Z[tau]=Z[sqrt(3)]=O_F.                         (7)

Also alpha^2=tau alpha-1 and alpha^-1=tau-alpha give the exact integral decomposition O=B direct_sum alpha B; independence follows from [K:F]=2.
Thus O intersection F=B.
The proof does NOT assert O=O_K or compute that index.
It instead establishes the unit-sign obstruction on the larger group O_K^times, which automatically includes O^times.
This handles both the actual-order and maximal-order interpretations without silently replacing either one.

<a id="all-actual-unit-constant-profile-exclusion"></a>
## 5. Exact exclusion at this control and retained norm costs

Combining (5) with the full norm tower proves

    Norm_(K/Q)(u)=+1 for every u in O_K^times.       (8)

Hence every actual original-order unit also has norm +1, and every relative norm is totally positive.
The accepted L372 constant-profile obstruction now excludes (3) for every pair of maximal-order units, at every choice of unit, sign or independent monomial twist.
Twisting by alpha^k changes neither u sigma(u) nor its full norm because alpha sigma(alpha)=1 and Norm(alpha)=1.

More generally, no finite normalized nonnegative mixture of actual units and monomials on this input can have an EXACT all-embedding constant profile E<1.
Increasing the number of units, the common scalar denominator or the Laurent window does not alter this particular sign obstruction.
This does not exclude nonconstant or approximate profiles, other unit-based inequalities, or arbitrary nonunit auxiliaries.

There is no rational-function shortcut with both original residues still units: if rational f,g are regular at every original root, have f(alpha),g(alpha) in O_K^times and satisfy ff*+2gg*=1, evaluation through the original reciprocal quotient would give (3), already impossible.
The statement requires the original unit residues and well-defined evaluation.
It does not say that all rational norm-one columns are absent.

The most tempting seeds from the successful sqrt(2) quartic are explicitly different here.
Their actual full norms are

    Norm_(F/Q)(tau)=-2,
    Norm_(K/Q)(tau)=4,
    Norm_(K/Q)(1-alpha)=P(1)=-2,
    Norm_(K/Q)((1-alpha)^-1)=-1/2.                   (9)

Thus tau is not a unit, and (1-alpha)^-1 is not even an algebraic integer.
One cannot copy the old unit labels or old resultants.
Their relative norms are tau^2=2tau+2 and (2-tau)^-1=-tau/2, so their weighted sum with coefficients 1,2 is tau+2, not 1.
Paying a denominator does not turn their nonunit norms into unit norms for free.
Other nonunit constructions remain outside the exclusion.

Every norm here is the complete degree-four K-norm or the explicitly labeled degree-two F-norm.
No square trace norm, absolute value, selected conjugate or normalized degree replaces a full signed original norm.
The result supplies an exact failure of universal coverage for this constant mixed-unit mechanism, not a statement that its successful quartic construction was invalid.

<a id="jacobi-path-original-trace-family"></a>
## 6. A bounded-spectrum trace family with one exterior root

The following extension was supplied substantively by root before this draft's freeze; the author verifies every step and the factor/field interfaces.
Put a=1+sqrt(3)>2, a'=1-sqrt(3) in (-1,0), and define

    U_0(x)=1, U_1(x)=x,
    U_n(x)=x U_(n-1)(x)-U_(n-2)(x),
    q_n(x)=U_n(x)-a U_(n-1)(x),
    q'_n(x)=U_n(x)-a' U_(n-1)(x),
    Q_n(x)=q_n(x)q'_n(x)
          =(U_n-U_(n-1))^2-3U_(n-1)^2.            (10)

Here n>=1.
The symbol q'_n denotes the conjugate-coefficient polynomial, not a derivative.
Each U_n is monic integral of degree n, so Q_n is monic integral of degree 2n.
Let J_n(b) be the real symmetric n-by-n path matrix whose first diagonal entry is b, other diagonal entries are zero, and adjacent off-diagonal entries are 1.
Expansion at the last row of xI-J_n(b), starting from determinants 1 and x-b, shows det(xI-J_n(b))=U_n-b U_(n-1).
Thus q_n and q'_n are the actual characteristic polynomials at b=a,a'.

Every eigenvalue of J_n(b) is simple.
Indeed the first coordinate of a nonzero eigenvector cannot vanish, and the first row followed by the three-term row recurrence determines every other coordinate from it.
Hence each eigenspace has dimension at most one; real symmetric diagonalizability makes the algebraic multiplicity one.
The same recurrence from the last row shows the last coordinate is nonzero too.
This includes n=1.

For v in R^n, direct coefficient expansion gives

    2||v||^2-v^T J_n(b)v
      =(1-b)v_1^2+sum_(i=1)^(n-1)(v_i-v_(i+1))^2+v_n^2,
    2||v||^2+v^T J_n(b)v
      =(1+b)v_1^2+sum_(i=1)^(n-1)(v_i+v_(i+1))^2+v_n^2.
                                                               (11)

For -1<b<1 both forms are positive on nonzero vectors, so every root of q'_n lies in (-2,2).
For b=a the second form stays positive, giving the strict lower spectral bound -2.
On the codimension-one subspace v_1=0 the first form is also strictly positive.
There can therefore be at most one eigenvalue at least 2: if two existed, their two-dimensional orthogonal eigenspace span would contain a nonzero v with v_1=0 and Rayleigh quotient at least 2, contradicting (11).
The Rayleigh quotient at e_1 is a>2, so exactly one root x_n exceeds 2; every other root of q_n lies in (-2,2).
For n>1, e_1 is not an eigenvector, so its Rayleigh quotient is strictly less than the maximum and x_n>a; at n=1, x_1=a.

The complete upper form, also valid at n=1, is

    (a+a^-1)||v||^2-v^T J_n(a)v
      =a sum_(i=1)^(n-1)(v_(i+1)-v_i/a)^2+a^-1 v_n^2>0
      for v!=0.
    x_1=a, and a<x_n<a+a^-1 for n>1.               (12)

Positivity is strict because zero on the right forces v_n=0 and then every coordinate zero.
The largest x_n increases strictly with n: extending a unit top eigenvector of J_n(a) by a final zero has Rayleigh quotient x_n in J_(n+1)(a).
Equality with the new maximum would make that extended vector an eigenvector, while its last row would force the old nonzero last coordinate to vanish.
This is a direct strictness argument, not an assumption of strict interlacing at a potentially zero boundary coordinate.

Finally q_n and q'_n have no common root.
Their difference is -2sqrt(3) U_(n-1); a common root would annihilate both U_(n-1) and U_n.
Their defining recurrence would then annihilate U_0=1, impossible.
Consequently Q_n is squarefree, with exactly one root x_n>2 and its other 2n-1 roots all in (-2,2).

<a id="actual-salem-factor-and-retained-cofactor"></a>
## 7. Actual Salem factors, the trace subfield and full factor costs

Define the full parent polynomial and the exterior root by

    Pcal_n(t)=t^(2n) Q_n(t+t^-1) in Z[t],
    alpha_n=(x_n+sqrt(x_n^2-4))/2>1.                (13)

Pcal_n is monic reciprocal of degree 4n and constant coefficient 1.
Each trace root in (-2,2) gives its two distinct circle roots; x_n gives alpha_n,alpha_n^-1.
The trace roots are distinct and avoid +/-2, so Pcal_n is squarefree, with exactly one exterior root and one interior root.
There is no assertion that the entire parent is irreducible.

Let p_n be the actual monic irreducible integer minimal polynomial of alpha_n, and put d_n=deg p_n and K_n=Q(alpha_n).
Since p_n divides the monic constant-one parent, its constant coefficient is +/-1.
The absolute product of its conjugates is therefore 1.
It contains the exterior root alpha_n; the only possible compensating root of modulus below 1 in the entire parent is alpha_n^-1, so that root must also belong to p_n.
Every remaining root of p_n lies on the circle.
Its nonreal roots occur in conjugate pairs and hence in inverse pairs, so p_n is reciprocal with constant coefficient +1.

At x_n, U_(n-1) does not vanish by the same consecutive-polynomial argument.
The exact root equation therefore gives

    sqrt(3)=[U_n(x_n)-U_(n-1)(x_n)]/U_(n-1)(x_n),
    F=Q(sqrt(3)) is contained in F_n=Q(x_n) contained in K_n.
                                                               (14)

In particular x_n is irrational, so p_n cannot be quadratic.
It is a genuine Salem polynomial of degree d_n>=4.
The original reciprocal involution fixes F_n, with [K_n:F_n]=2 as in L66.
Thus d_n is a multiple of 4, but it is NOT identified with the parent degree 4n.

Retain the complete factorization Pcal_n=p_n C_n.
The monic integer cofactor C_n has only circle roots, no zero root and no overlap with p_n.
By the accepted Kronecker statement it is a product of distinct cyclotomic polynomials (possibly the empty product).
Its measure is one, so M(Pcal_n)=M(p_n)=alpha_n, while its actual degree is 4n-d_n.
It is not omitted from parent-polynomial identities, resultants or counts.
For example U_n(2)=n+1 by induction, so

    Pcal_n(1)=1-3n^2=p_n(1) C_n(1).                (15)

This parent value is not automatically the original field norm p_n(1)=Norm_(K_n/Q)(1-alpha_n).
The cofactor C_n(1) is retained.
No native factorization, list of d_n, maximal-order index or explicit field norm is asserted by this existence construction.
Each actual original input for the sign argument is p_n with all of its own conjugates.

<a id="unbounded-degree-bounded-measure-sign-obstruction"></a>
## 8. Unbounded actual degrees and the same unit-sign exclusion

The function x maps to (x+sqrt(x^2-4))/2 is strictly increasing for x>2.
Equation (12) therefore gives a strictly increasing sequence alpha_n with

    2<alpha_1<=alpha_n<a=1+sqrt(3).                 (16)

In fact the limit is a.
To verify this without an infinite-matrix theorem, use the finite trial vector v_i=a^(-(i-1)) in (12).
All difference squares vanish, so its Rayleigh quotient is

    a+a^-1 - a^(-(2n-1))/sum_(i=0)^(n-1) a^(-2i).

This tends to a+a^-1 and is bounded above by x_n, which has that same strict upper bound.
Hence x_n tends to a+a^-1 and alpha_n tends to a.
The total measures stay uniformly bounded and strictly away from one; they do not form a near-one family.

The ACTUAL degrees d_n tend to infinity.
If infinitely many were at most a fixed D, all roots of those monic integer p_n would have modulus at most a.
Their coefficients would then be bounded by the elementary symmetric-function bounds for degree at most D.
Only finitely many such integer polynomials, and hence finitely many roots, exist.
This contradicts the strict increase and distinctness of alpha_n.
This is the same finite coefficient-count principle recorded in Smy08/L168, not an assumption of parent irreducibility or a new enumeration.

For any unit of O_(F_n), its relative norm down to F is a unit of O_F.
Equation (5) and the full norm tower therefore force its norm to Q to be +1.
The same applies directly to every unit of O_(K_n).
Thus the general criterion (1) holds for the ACTUAL trace field F_n, and

    Norm_(K_n/Q)(u)=+1 for every u in O_(K_n)^times,
    u sigma_n(u)+2v sigma_n(v)!=1 for all such units u,v.
                                                               (17)

The exact constant positive-surplus unit profile is therefore excluded throughout this unbounded-degree family, including every original Z[alpha_n] unit and every maximal-order unit.
The argument uses the actual degree d_n and all original embeddings; it does not replace them by trace degree, the fixed quadratic subfield degree or parent degree 4n.
Since p_n is genuinely Salem, p_n(1) is negative by its real reciprocal pair and positive circle-pair products.
It cannot be -1, which would make 1-alpha_n a negative-full-norm unit; hence p_n(1)<=-2.
This is a sign/magnitude consequence, not a fabricated formula for that norm.

The extension demonstrates that the obstruction is not confined to one bounded-degree input.
Its precise limit remains unchanged: it excludes constant positive-surplus profiles of units, not all unit constructions, approximate or nonconstant covariance, nonunit auxiliaries, other coefficient weights without the same normalization, or the unrestricted Mahler-gap Task.
