---
author: Yin
---
# Exact centralizer local degrees and old height coverage for powered Frobenius lifts

Human author Yin.
Root proposed the centralizer/fixed-field mechanism for the unramified powered-Frobenius question.
The draft_comparison_cleanup AI checked the actual fields and completions, supplied the exact ramified inertia-quotient formula, matched the finite ADZ constants and compared the original bounded-residue theorem.
The original author argument was retained in D42 at2026-10-20T09:51; this registration contains its complete proof and precise source interfaces.
Root and this drafting agent are mathematical contributors and neither is an independent reviewer of this result.
No numerical calculation, prime scan, new arithmetic-family construction or mathematical program was performed.
The separate abelian/split compositum specialization already has its adequate complete home in ADZ14-U001 and is not registered again here.

## Statement

Let L/Q be finite Galois with group G, let p be a rational prime and choose a prime mathfrak P of L above p.
Let D and I be its decomposition and inertia groups, put t_res=|D/I|, and choose an actual lift sigma in D of the p-power residue Frobenius.
For any integer f>=1 put

    tau=sigma^f, C=C_G(tau), kappa=[G:C],
    N=<tau>, K=L^C, E=L^N,
    nu=[I intersect C:I intersect N].

Then L/K is finite Galois with group C, N is central in C, [K:Q]=kappa, and for the primes wp,q obtained by restricting mathfrak P to K,E,

    [K_wp:Q_p]=[D:D intersect C],
    [E_q:K_wp]=[D intersect C:N]=gcd(t_res,f) nu.       (S1)

The inclusion N subset D intersect C makes nu a positive integer.
For every nonzero nontorsion alpha in L, the established finite ADZ theorem gives

    h_abs(alpha)>=c_ADZ(p,gcd(t_res,f)nu,kappa)>0.      (S2)

The three parameters are exactly the rational prime, chosen relative local degree and base degree of the accepted finite ADZ theorem.
For an original integer unit of degree d this implies m(alpha)>=d c_ADZ(p,gcd(t_res,f)nu,kappa), without assuming that alpha generates K or L.

For a fixed nonempty finite prime set S and positive integer bounds F,K0,V, all instances with p in S, f<=F, kappa<=K0 and nu<=V have the uniform positive absolute-height bound

    c_* = min {c_ADZ(p,e,k):p in S,1<=e<=FV,1<=k<=K0}>0. (S3)

No monotonicity of the source constant is assumed.
If p is unramified in L then D=<sigma>, I={1}, nu=1, K_wp=Q_p and [E_q:K_wp]=gcd(t_res,f)<=f.
Thus every unramified bounded-p,f,kappa instance is already in this stronger old absolute-height domain.
For ramified instances, bounded inertia cardinality is sufficient but not necessary for bounded nu, and no bound on nu follows here merely from bounded kappa or f.

Separately, if original nontorsion integer-unit alpha belongs to L and t_res<=F_res for a fixed integer F_res>=1, the established original-polynomial bounded-residue theorem gives

    m(alpha)>=log2/[N_(p,F_res) p^2],
    N_(p,F_res)=lcm_(1<=j<=F_res)(p^j-1).             (S4)

This has no unramifiedness, centralizer or order-index hypothesis.
The case t_res=1, including total ramification at p, gives log2/[(p-1)p^2].
No new automatic parameter supply on previously unresolved input families, near-zero-measure sequence or unrestricted Mahler gap is asserted.

<a id="direct-inputs"></a>
## Exact inputs and their roles

| Input | Role and boundary |
| --- | --- |
| [ADZ14-U001](../audits/literature/ADZ14/Yin_U001.md#adz14-u001) | Accepted finite central-extension Proposition4.2 of the acquired2011 HAL manuscript, with exact p/local-degree/base-degree dependence; source theorem, not a project proof. |
| [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Actual decomposition/inertia and residue-lift conventions, including ramified primes and finite-field separability. |
| [Additional local-degree interface](#local-degree-source-interface) | Exact already retained chapter passages, their current inspection and standard local-degree application to nonnormal intermediate fields. |
| [L205 all-input residue-mass theorem](../ledger/Yin_L_G0205_v1.md#local-rigidity-near-one-mass-fixed-scope) | Full ramification/index allowance and all multiplicities; gamma=1 is used only after verifying the complete original reduction. |
| [L435 powered ratio criterion](../ledger/Yin_L_G0435_v1.md#powered-lift-residue-transfer) | Existing total-measure inclusion as a scope comparison, not a premise of the ADZ argument or an automatic supply theorem. |
| [Existing abelian/split source specialization](../audits/literature/ADZ14/Yin_U001.md#abelian-split-compositum-application) | Adequately retained application, not repeated here and not needed in the proof of S1--S4. |

<a id="local-degree-source-interface"></a>
## Exact local-algebra source interface

The decomposition/inertia and residue-lift conventions are already accepted in The26b-U001.
For the additional local-degree step, this author directly read the existing [More on Algebra chapter](../literature/pdf/The26b--more-algebra-20261002.pdf), version ed88ff78 compiled14 July2026, using its [registered contents](../literature/contents/The26b--more-algebra-20261002.md).
The inspected relevant passages are printed/PDF pages333--336: Lemma113.3, Tag0BRL, on multiplicative ramification/residue degrees; Remark113.6, Tag09E8, on the degree sum and one-prime complete-DVR case; Lemmas114.1--114.2, Tags09EA--09EB, on Galois prime transitivity and [L:K]=nef; Definition114.3 and Lemma114.4, Tags09EC--09ED; and the opening paragraph of the proof of Lemma114.5, Tag09EE, deriving |D|=ef by orbit-stabilizer.
The complete named statements and their short displayed justifications were read, plus that exact opening paragraph of09EE.
No use or complete audit of the later wild-inertia filtration argument or ancestor proofs is asserted.
The chapter omits its leading chapter number in these internal labels; the stable tags identify the exact statements in the separately identified chapter version.
These standard statements are accepted for the finite number-field application below.

Completion preserves the normalized value group and finite residue field of a number-field place.
The complete-DVR case of09E8 therefore gives local degree ef, while the cited Galois orbit-stabilizer paragraph gives |D|=ef.
For any subgroup U of Gal(L/Q), put H=L^U and let v be the restriction of mathfrak P to H.
The extension L/H is Galois with group U; its chosen decomposition group is D intersect U directly from the stabilizer definition.
Consequently [L_mathfrak P:H_v]=|D intersect U|.
No normality of H/Q is required.
This is the accepted standard local-degree interface; the specific centralizer and exact inertia-quotient adaptation is proved below.

<a id="argument"></a>
## Complete centralizer and height argument

### Full subgroup and completion calculation

For the general ramified setting of the statement, sigma commutes with its power tau, hence sigma belongs to C.
Every element of C commutes with tau and all its powers, so N=<tau> is contained in Z(C).
It is also contained in D because sigma lies in D.
The Galois correspondence gives L/K Galois with group C, [K:Q]=[G:C]=kappa, K contained in E, and Gal(E/K)=C/N.
The class of tau in the GLOBAL group G has size kappa by orbit-stabilizer; no local conjugacy class replaces it.

Apply the preceding source interface to U=G,C,N.
The respective local degrees [L_mathfrak P:Q_p], [L_mathfrak P:K_wp] and [L_mathfrak P:E_q] are |D|, |D intersect C| and |N|.
The tower law of the actual embedded completions gives both quotients in S1.
In particular a possibly nonnormal K/Q is harmless: L/K and L/E, which are used for the denominator degrees, are both Galois.

The quotient D/I is cyclic of order t_res, generated by the image of the actual residue-Frobenius lift sigma.
Since sigma lies in D intersect C, the latter group's residue image is all of D/I and its kernel is I intersect C.
Thus |D intersect C|=t_res |I intersect C|.
The image of N=<sigma^f> has order t_res/gcd(t_res,f), and its kernel is I intersect N.
Dividing these two exact group orders yields

    [D intersect C:N]=gcd(t_res,f)
                          [I intersect C:I intersect N].

This proves the general S1, including all ramification and the trivial residue group t_res=1.
Different actual Frobenius lifts may give different C,N,nu; no lift-invariance of those parameters is asserted.

### Complete unramified specialization and old-height comparison

Let L/Q be an actual finite Galois extension, fix a prime of L above a rational prime p that is unramified in L, and let sigma be its actual residue Frobenius.
Write D for the decomposition group and t for the order of sigma, so D=<sigma> is cyclic of order t.
For any integer f>=1 put

    tau=sigma^f, C=C_G(tau), kappa=[G:C],
    K=L^C, N=<tau>, E=L^N.

The field K need not be Galois over Q, but L/K is Galois with group C and [K:Q]=kappa.
Every power of sigma commutes with tau, hence D is contained in C.
Also N is a subgroup of Z(C), so E/K is the central fixed-field extension required by ADZ.
For the chosen prime of K, the local-degree formula gives [K_wp:Q_p]=[D:D intersect C]=1.
The decomposition group of L/K at the chosen prime is D intersect C=D.
Its image in C/N is D/N because N is contained in D.
Consequently, for the resulting prime q of E,

    [E_q:K_wp]=[D:N]=gcd(t,f)<=f.                    (U1)

The [finite ADZ proposition](../audits/literature/ADZ14/Yin_U001.md#central-local-height-theorem) therefore applies to these actual fields and gives

    h_abs(alpha)>=c(p,gcd(t,f),kappa)>0              (U2)

for every nonzero nontorsion alpha in L.
The theorem does not require alpha to generate K or L, to be integral, or to be a unit.
For an original integer unit of degree d this implies m(alpha)>=d c(p,gcd(t,f),kappa).
Thus every unramified bounded-p,f,kappa instance already has an old absolute-height bound, stronger in its degree dependence than the completed total-measure bridge.
For p in one fixed finite set, f<=F and kappa<=K0, take the minimum of the finitely many positive constants c(p,e,k), with 1<=e<=F and 1<=k<=K0.
This establishes uniformity without assuming any unrecorded monotonicity of the source constant.
The conclusion is an inclusion for this exact unramified method class, not a global literature-novelty verdict.

### The precise ramified boundary and the bounded-residue exclusion

For a ramified prime, retain an actual residue-Frobenius lift sigma in D, inertia I, and the same tau,C,N,K,E.
Then sigma belongs to C and N is contained in D intersect C, but the full D need not be contained in C.
The actual finite local degree used by ADZ is now

    [E_q:K_wp]=[D intersect C:N].                    (U3)

Let t_res=|D/I| be the residue degree.
Because sigma maps to a generator of D/I and lies in C, the image of D intersect C in D/I is the whole quotient.
The image of N has order t_res/gcd(t_res,f), giving

    [D intersect C:N]
      =gcd(t_res,f) [I intersect C:I intersect N]
      <=f [I intersect C:I intersect N].            (U4)

Thus a uniform bound on this inertia quotient also puts the ramified powered instances under the same ADZ criterion.
Unbounded total inertia by itself does not obstruct that inclusion; the relevant cost is precisely the quotient in (U4).
No bound on that quotient follows here merely from the global class size of tau.

Separately, the [all-input bounded-residue theorem in L205](../ledger/Yin_L_G0205_v1.md#local-rigidity-near-one-mass-fixed-scope) already applies whenever a fixed positive fraction of the original polynomial degree lies in reduction factors of uniformly bounded degree.
It has no saturation, order-index or ramification assumption.
In particular, if the normal closure is totally ramified at p, all original conjugates reduce in F_p and every irreducible reduction factor is linear, including all multiplicities.
Its gamma=1,F=1 case yields m(alpha)>=log2/[(p-1)p^2] directly.
More generally a uniformly bounded residue degree of the normal closure puts all those reduction-factor degrees under the same fixed bound.

A genuinely distinct remaining application therefore needs an actual arithmetic family for which the bounded-p,f,kappa supply is proved, the ADZ local-degree quotient above is not automatically uniformly bounded, and the original bounded-residue-mass criterion is not already automatic.
These are applicability obligations, not assertions that such a family exists or that no other old theorem covers it.
The unrestricted automatic-supply question remains open.

### Uniform ramified constants and original reduction details

In the general ramified case, the same ADZ application uses K of degree kappa, the central subgroup N of Gal(L/K)=C, E=L^N and the exact chosen relative local degree gcd(t_res,f)nu.
Every hypothesis of the finite theorem is thus checked, proving S2.
The theorem's ramification allowance does not mean its relative local degree is free; that degree is precisely the quantity computed here.
For f<=F and nu<=V it lies between1 andFV, and kappa lies between1 andK0.
All applicable triples lie in the finite set in S3, whose positive minimum proves the uniform conclusion without any monotonicity assumption.
Bounding |I| certainly bounds nu, but the denominator |I intersect N| can absorb large inertia, so the stronger bound on total inertia is not necessary.
No converse or automatic bound from kappa is proved.

For S4, take the complete original factorization P_alpha(X)=product_beta(X-beta) in L[X].
Every original conjugate beta is an integral unit and reduces at mathfrak P into the same finite residue field F_(p^t_res), with nonzero residue.
Reduction of that full factorization, retaining all d multiplicities, shows that P_alpha modulo p splits over F_(p^t_res).
Each distinct irreducible factor over F_p therefore has degree dividing t_res, hence at most F_res when t_res<=F_res.
This argument assumes neither squarefree reduction nor maximality of the order Z[alpha].
L205 consequently has gamma=1 in its original degree-fraction theorem, whose denominator p^(ceil(1/gamma)+1) becomes p^2; this proves S4.
For t_res=1 use F_res=1, giving N_(p,1)=p-1 whether or not the prime is totally ramified.
The broader L205 criterion also permits only a fixed positive fraction of bounded-degree factors; the all-degree specialization here is not presented as its full coverage.

## Current assessment
[Selected decision](#decision-current-complete-residue-mass-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:00 |
| status | open |
| reason | Register the complete actual centralizer/local-degree adaptation, exact ramified quotient, finite ADZ uniformity and old original bounded-residue comparison. Root and the drafting agent contributed; independent whole review is required. No automatic new arithmetic-family coverage is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact powered local-degree and height statement](#statement) | Arbitrary finite Galois L, actual ramified lift, every f>=1, exact global class/base degree and relative local degree, finite-parameter absolute-height inclusion and separate old original-residue bound. |
| argument | [Complete actual-field argument](#argument) | Fixed fields, completion quotients, cyclic residue-image count, all ADZ hypotheses and finite minimum, original polynomial reduction with every multiplicity. |
| dependency | [Accepted finite ADZ statement](../audits/literature/ADZ14/Yin_U001.md#adz14-u001) | Finite central-extension Proposition4.2, exact c(p,relative-local-degree,base-degree), ramification allowance and actual HAL source inspection limits. |
| dependency | [Actual local Frobenius conventions](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Residue lift surjectivity at ramified primes, actual decomposition/inertia definitions and finite-field separability. |
| dependency | [Precise local-degree source interface](#local-degree-source-interface) | Identified existing chapter and exact passages, accepted local degree equals decomposition order, including nonnormal intermediate fields. |
| dependency | [All-input original residue theorem](../ledger/Yin_L_G0205_v1.md#local-rigidity-near-one-mass-fixed-scope) | Positive bounded-residue-degree fraction with all ramification and index allowance, used at gamma=1 after checking the full original reduction. |
| support | [Complete powered ratio comparison](../ledger/Yin_L_G0435_v1.md#powered-lift-residue-transfer) | Earlier total-measure bridge as a scope comparison, not an ADZ proof premise or supply theorem. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:05 |
| status | proved |
| authority | Internal adoption under Yin's retained-D42 continuation. |
| reason | Adopt the complete exact centralizer and local-degree argument through noncontributor whole R450, including the actual source passages, finite ADZ uniformity and all original reduction multiplicities. This settles old coverage of every unramified bounded-power/class instance and the precise ramified bounded-quotient class, without claiming new automatic input supply. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact powered local-degree and height statement](#statement) | Arbitrary finite Galois L, actual ramified lift, every f>=1, exact global class/base degree and relative local degree, finite-parameter absolute-height inclusion and separate old original-residue bound. |
| argument | [Complete actual-field argument](#argument) | Fixed fields, completion quotients, cyclic residue-image count, all ADZ hypotheses and finite minimum, original polynomial reduction with every multiplicity. |
| dependency | [Accepted finite ADZ statement](../audits/literature/ADZ14/Yin_U001.md#adz14-u001) | Finite central-extension Proposition4.2, exact c(p,relative-local-degree,base-degree), ramification allowance and actual HAL source inspection limits. |
| dependency | [Actual local Frobenius conventions](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Residue lift surjectivity at ramified primes, actual decomposition/inertia definitions and finite-field separability. |
| dependency | [Precise local-degree source interface](#local-degree-source-interface) | Identified existing chapter and exact passages, accepted local degree equals decomposition order, including nonnormal intermediate fields. |
| dependency | [All-input original residue theorem](../ledger/Yin_L_G0205_v1.md#local-rigidity-near-one-mass-fixed-scope) | Positive bounded-residue-degree fraction with all ramification and index allowance, used at gamma=1 after checking the full original reduction. |
| support | [Complete powered ratio comparison](../ledger/Yin_L_G0435_v1.md#powered-lift-residue-transfer) | Earlier total-measure bridge as a scope comparison, not an ADZ proof premise or supply theorem. |
| review | [Whole centralizer finding](../audits/reviews/Yin_R_G0450_v1.md#powered-centralizer-whole-independent-finding) | Complete final statement, S1--S4 and U1--U4, all six input roles, exact accepted primary-source interfaces and original-field costs. |


### Decision current-complete-residue-mass-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:42 |
| status | proved |
| authority | Internal adoption under Yin's retained-D42 continuation. |
| reason | Maintain exactly the current original L205 dependency as the complete same-object C491 proof home after reading the full needed consumer scope and complete C491 Sections1--5/equations1--15. Its actual original-degree/all-input/repeated-reduction/no-index-or-ramification-hypothesis mass bound, full same-exponent and cost scope is unchanged. Every other field except this actual date/reason, all nonmatching relations and scopes, review tuples, Statement/Argument, original source/authority and old decisions remain unchanged. Existing review findings keep their actual old inputs; this maintenance does not assert that an old reviewer read C491, add whole independent coverage or select a research Task/E. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact powered local-degree and height statement](#statement) | Arbitrary finite Galois L, actual ramified lift, every f>=1, exact global class/base degree and relative local degree, finite-parameter absolute-height inclusion and separate old original-residue bound. |
| argument | [Complete actual-field argument](#argument) | Fixed fields, completion quotients, cyclic residue-image count, all ADZ hypotheses and finite minimum, original polynomial reduction with every multiplicity. |
| dependency | [Accepted finite ADZ statement](../audits/literature/ADZ14/Yin_U001.md#adz14-u001) | Finite central-extension Proposition4.2, exact c(p,relative-local-degree,base-degree), ramification allowance and actual HAL source inspection limits. |
| dependency | [Actual local Frobenius conventions](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Residue lift surjectivity at ramified primes, actual decomposition/inertia definitions and finite-field separability. |
| dependency | [Precise local-degree source interface](#local-degree-source-interface) | Identified existing chapter and exact passages, accepted local degree equals decomposition order, including nonnormal intermediate fields. |
| dependency | [All-input original residue theorem](Yin_C_G0491_v1.md#local-rigidity-near-one-mass-fixed-scope) | Positive bounded-residue-degree fraction with all ramification and index allowance, used at gamma=1 after checking the full original reduction. |
| support | [Complete powered ratio comparison](Yin_C_G0580_v1.md#powered-lift-residue-transfer) | Earlier total-measure bridge as a scope comparison, not an ADZ proof premise or supply theorem. |
| review | [Whole centralizer finding](../audits/reviews/Yin_R_G0450_v1.md#powered-centralizer-whole-independent-finding) | Complete final statement, S1--S4 and U1--U4, all six input roles, exact accepted primary-source interfaces and original-field costs. |

