---
author: Yin
---
# Normalized coefficient budgets for sparse logarithmic auxiliary income

Date: 2026-10-15.
Human author Yin.
Root continues the bounded-term logarithmic line after fixing C139v1.
That original has an independent whole review in progress.
The present question is a genuine further extension: can the raw coefficient bound be replaced by a coefficient bound AFTER dividing by the actual arithmetic modulus, allowing that modulus and all raw coefficients to grow?
Root is the author of the new argument and cannot independently review it.
No native program or J is used.

## Exact reuse and changed obligation

Read actual [C139v1](Yin_C_G0139_v1.md#argument), the complete accepted [L237 auxiliary construction](../ledger/Yin_L_G0237_v1.md#uniform-auxiliary-margin-fixed-scope), and the C137 finite logarithmic mechanism.
L237 gives all-input primitive linear-degree auxiliaries with positive coefficient-energy margin, but only growing effective support; it does NOT supply the normalized l1 or term-count bounds below.
C139 uses integer Parseval to bound the circle supremum below1, which is lost after division by an unbounded modulus.
The proposed repair is a two-case estimate at a fixed circle-supremum threshold.
A source-dependent constant remains inherited from the exact accepted BS13-U001, not a new external theorem.

<a id="candidate-statement"></a>
<a id="statement"></a>
## Stronger arithmetic class and final scope

Fix integers K>=2 and S>=1, C>0 and0<eta<=1.
Let P be an original monic irreducible nontorsion integer unit, degree d and total m>0.
Assume an actual F in Z[t] of degree1<=T<=Cd has at most K nonzero terms, and an integer q>=2 satisfies

    F(alpha)/q is a NONZERO algebraic integer,
    ||F||_1/q<=S,
    m(F)-log q<=-eta.                                  (1)

The conclusion proved below is a positive lower bound m>g_normal(K,S,C,eta) independent of q and every raw coefficient.
This is stronger than the bounded-raw-coefficient sufficient class in C139, but is still conditional on existence, nonvanishing and all listed quantitative bounds.
It does not cover L237 automatically.
The complete argument follows.
Section5 further removes the nonzero-value condition by the already adopted C92; the new final class then permits zero integral values as well.
Actual independent whole review remains separate from this author proof.

<a id="argument"></a>
## 1. Normalize first and pay the missing scale by two cases

Put f=F/q, beta=1/(K-1), D=1/beta+1/(2-beta), and retain A>=1 from BS13.
Then ||f||_1<=S and integral log|f|<=-eta.
Set a=exp(-eta/2).
Choose a positive rational delta such that

    delta<=1,
    delta^2<=eta/16,
    A exp(beta/2) D delta^beta<=eta/16.              (2)

For instance take delta=1/L with L the ceiling of the maximum of1,4/sqrt(eta), and[16A exp(beta/2)D/eta]^(1/beta).
All these constants are independent of q and of the particular polynomial.

If sup_T|f|>=a and the actual term count N>=2, the exact Turan--Nazarov substitution yields mu{|f|<=t}<=A(t/a)^(1/(N-1)) for0<t<=a.
For t<=a this is at most A(t/a)^beta.
For t>a the trivial bound1<=A(t/a)^beta applies.
For a monomial with supremum at least a, the same bound holds because its modulus is constant.
Thus

    mu{|f|<=t}<=A a^(-beta)t^beta
                           <=A exp(beta/2)t^beta.     (3)

The same nonnegative layer-cake integral proved in C139 therefore gives regularization error at most eta/16.
In this case

    integral (1/2)log(|f|^2+delta^2)<=-15eta/16.       (4)

The other case is sup_T|f|<a.
No lower-scale estimate or approximation to m(f) is needed: pointwise |f|^2+delta^2<=exp(-eta)+delta^2.
For0<eta<=1,

    exp(-eta/2)-exp(-eta)
       =exp(-eta)(exp(eta/2)-1)>=eta/(2e)>eta/16.

The elementary inequality e<3, for example from its factorial series, is more than sufficient for the last strict comparison.
By(2), exp(-eta)+delta^2<exp(-eta/2), and hence

    integral (1/2)log(|f|^2+delta^2)<-eta/4.          (5)

Both cases give the common upper bound -eta/4.
This is the key change: uniform absolute approximation to the logarithm is unnecessary for polynomials whose entire circle supremum is already small.
Treating f as an integer polynomial or asserting its Parseval norm is at least1 would have been false.

## 2. One finite logarithmic majorant for both cases

Take B=S^2+1 and J=ceil(8B/(eta delta^2)).
Define H=|f|^2+delta^2, Y=1-H/B and Phi_J=(log B)/2-(1/2)sum_(j=1)^J Y^j/j.
As in the fully written C139/C137 mechanism,0<=Y<=1-delta^2/B<1.
The finite series majorizes log H/2, and its omitted tail is at most B/[2(J+1)delta^2]<=eta/16.
Consequently its actual constant coefficient satisfies

    c_J(f)<=-3eta/16.                               (6)

Every coefficient except the single log B/2 is rational because f=F/q,delta are rational and B is integer.
Actual denominator size is unbounded, but this is a finite analytic upper certificate; no assertion that its coefficient denominator yields arithmetic income is made.
Its nonconstant Fourier coefficient sum is less than2^J and its frequencies have absolute value at most JT.
The centered matrix realization, if used, has the full size2JT+1.
The previous derivation uses rational coefficients and their l1 norm; it does not require integer coefficients at this stage.

## 3. Original integral values after normalization

Let h=Tm/d.
The original radial comparison with coefficient budget S applies directly to f.
Writing r_i=|alpha_i|,z_i=alpha_i/r_i and V_i=f(alpha_i)/max(1,r_i)^T gives |V_i-f(z_i)|<=S min(1,T|log r_i|).
The original unit identities sum log^+r_i=m and sum|log r_i|=2m, followed by the1/(2delta) Lipschitz bound, pay(1+S/delta)h.
Thus, on0<Jh<=h0,

    (1/d)sum_i log|f(alpha_i)|
       <=c_J(f)+(1+S/delta)h+2^J epsilon(Jh).        (7)

The L229 epsilon and original powered-field costs are exactly those of C139.
The left side is nonnegative: the original value f(alpha)=F(alpha)/q is a nonzero algebraic integer, so its FULL ORIGINAL field norm is a nonzero integer.
This is also log|Res(P,F)|/d-log q.
There is no need to assign an integer resultant to the rational polynomial f, or discard any local or original-root multiplicity.

Choose the least integer ell>=32 for which, with h_star=(log2/(4J))2^(-ell), both(1+S/delta)h_star<=eta/32 and2^J epsilon(Jh_star)<=eta/32.
Such an ell exists, stays in the actual angular domain and is independent of F,P,q.
If0<h<=h_star then(6)--(7) give

    0<=-3eta/16+eta/32+eta/32=-eta/8<0,

a contradiction.
Hence h>h_star and T<=Cd gives

    m>h_star/C.                                    (8)

No case requires a bound on q or raw coefficient size.
Monomials are included in the two-case analysis; alternatively their actual unit norm immediately contradicts(1)'s negative normalized logarithmic cost.
Zero auxiliary values remain an explicit exclusion.

## 4. Why this does not yet close the universal auxiliary construction

L237 supplies T<2d and a fixed coefficient-energy margin after dividing by its actual modulus, but its general estimate only gives normalized l1 norm at most a constant times sqrt(d), and the term count can be2d.
Its forced effective-support growth on a hypothetical near-one sequence must not be erased.
The current two-case argument removes raw scale and modulus as extra costs, not support complexity.
It therefore isolates the remaining bounded-term/normalized-size issue more faithfully than a raw-height restriction.
No universal sparse representative, bounded normalized l1 theorem, actual near-one family, or contradiction to the unrestricted goal is claimed.

The old fixed-denominator low-energy criterion, the C135 binomial class and C137 six-term congruence family remain at their exact scopes.
This candidate changes the sufficient analytic hypotheses and permits unbounded moduli.
It does not prove that an input outside all those old sufficient classes satisfies(1), or that this criterion is strictly stronger on a demonstrated near-one family.
The exact additional reuse and author checking are recorded below; actual independent whole checking is still required before adoption.


<a id="normalized-cost-zero-value-closure"></a>
## 5. Existing sparse-annihilator theorem closes the zero branch

The f_unitary_scope author identified the exact already adopted [C92 short rational annihilator theorem](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) during the concurrent actual-auxiliary screen.
Root then read that complete original statement and proof, its original-root phase/radial normalization, and the following fixed-rank consequence.
This is reuse of the old zero-value theorem, not a new annihilator result or a source-proof extension.
The contribution to recognizing and assembling this additional branch is shared with that author.

C92 says that a nonzero rational Laurent polynomial vanishing at alpha, of positive support span T0 and effective coefficient support rho, necessarily satisfies

    (rho-1)epsilon(T0*m/d)+2rho*T0*m/d>=1

on its actual small-parameter domain.
A polynomial with at most K nonzero terms has rho<=K by Cauchy--Schwarz.
Its span T0 is at most the actual degree T used above; a monomial cannot vanish at the nonzero alpha.
Choose the least integer ell0>=32 such that

    u0=(log2/4)2^(-ell0),
    (K-1)epsilon(u0)+2K*u0<=1/2.                    (9)

It exists because epsilon tends to0, and u0<h0.
If T*m/d<=u0, a vanishing F would have positive T0*m/d<=u0 and would contradict C92 by monotonicity.
This argument has no coefficient-height, denominator, good-prime, irreducibility-of-F or cofactor-cost assumption.
It uses the actual original d and every original conjugate, exactly as in that theorem.

Consequently the FINAL theorem can replace the first condition of(1) by merely

    F(alpha)/q is an algebraic integer,              (10)

while still requiring F itself to be a nonzero polynomial.
The full uniform conclusion is

    m(P)>min(h_star,u0)/C>0.                         (11)

Indeed, if m were at most this bound, the degree bound would give T*m/d<=min(h_star,u0).
C92 would first force F(alpha) nonzero, after which Sections1--3 contradict the nonzero original integral norm.
This treats the zero branch without pretending a zero norm supplies income and without requiring that P and F have equal degree.
No actual near-one sequence is assumed.

The nonzero version(8), the general version(11), and all source/contribution boundaries are part of the final statement.
The genuine remaining hypotheses are at most K terms, degree at most C*d, normalized coefficient l1 at most S, negative normalized logarithmic Mahler cost at least eta, and actual integral value.
Their automatic existence is not proved.
L237 still supplies no uniform K or normalized l1 bound, so the all-input gap remains open.


<a id="normalized-cost-entire-author-freeze"></a>
## Entire author check and freeze

2026-10-15T10:47.
Freeze this entire account: original changed question and reuse, full normalized-coefficient theorem, the optional nonzero version and automatic zero-branch closure, Sections1--5 and all11 equations, explicit finite parameter selections and all original norm/domain costs.
Root checked the supremum-threshold cases, exponent direction below/above a, monomial endpoints, integrability and the two tails, delta and log-series error budgets, rational finite coefficients and full matrix/frequency expenses, the original integral norm of F(alpha)/q rather than an integer resultant for a rational polynomial, strict cutoff and C92's actual support span/degree substitution.
The supremum-small case does not claim a uniform approximation to an arbitrarily scaled logarithm.
The source A remains existential; no numerical universal constant or computation is claimed.

Root authored the normalized two-case estimate and its finite transfer.
The finite-majorant/radial mechanism is the already accepted C137/C139 input at its actual scope.
The f reader identified the already accepted C92 zero-value interface; that supplied the additional assembly in Section5, now separately read and checked by root.
Neither contributor is eligible to independently review this whole new account.
No native program or new source theorem is required.
Whole independent review and actual adoption remain pending; auxiliary existence and G0001 are unresolved.

## Fixed organization

Retain the whole frozen normalized-cost account and automatic zero-branch assembly.
This is a distinct parameter-uniform extension allowing unbounded arithmetic moduli and raw coefficients, with unchanged original auxiliary coverage obligations.

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T10:47 |
| status | open |
| reason | Complete normalized sparse auxiliary transfer and known zero-branch assembly retained for actual whole review; all-input existence remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire final theorem](#statement) | Normalized coefficient budget with unbounded q/raw heights, both nonzero and automatically closed zero-value scopes including Section5. |
| argument | [Entire argument](#argument) | Complete Sections1--5, all11 equations, original norms, finite constants, all cases and contribution limits. |
| dependency | [Uniform regularization mechanism](Yin_C_G0139_v1.md#argument) | Accepted layer-cake tails and finite logarithmic/radial transfer, with the changed normalized scale proved locally. |
| dependency | [Measurable-set inequality](../audits/literature/BS13/Yin_U001.md#bs13-u001) | Accepted absolute-constant pure-imaginary statement; no original-proof upgrade. |
| dependency | [Original angular estimate](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Exact epsilon, domain and original powered-degree costs. |
| dependency | [Existing short-annihilator exclusion](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Exact zero-value effective-support inequality, applied at true span and original d. |
| dependency | [Scalar logarithmic normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Scaling by q and normalized circle integral with content retained. |
| support | [Finite logarithmic mechanism](Yin_C_G0137_v1.md#argument) | Majorant, matrix path, coefficient and radial mechanism attribution at its accepted scope. |
| support | [All-input auxiliary existence boundary](../ledger/Yin_L_G0237_v1.md#uniform-auxiliary-margin-fixed-scope) | Exact comparison: positive margin and linear degree are known, while term count/normalized l1 are not uniformly bounded. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T11:03 |
| status | proved |
| reason | Adopt actual whole independent review of the normalized two-case logarithmic transfer and existing C92 zero-branch assembly. Raw coefficients and q may grow, while uniform support/normalized-size/degree/margin hypotheses remain; automatic auxiliary coverage is open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire final theorem](#statement) | Normalized coefficient budget with unbounded q/raw heights, both nonzero and automatically closed zero-value scopes including Section5. |
| argument | [Entire argument](#argument) | Complete Sections1--5, all11 equations, original norms, finite constants, all cases and contribution limits. |
| dependency | [Uniform regularization mechanism](Yin_C_G0139_v1.md#argument) | Accepted layer-cake tails and finite logarithmic/radial transfer, with the changed normalized scale proved locally. |
| dependency | [Measurable-set inequality](../audits/literature/BS13/Yin_U001.md#bs13-u001) | Accepted absolute-constant pure-imaginary statement; no original-proof upgrade. |
| dependency | [Original angular estimate](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact epsilon, domain and original powered-degree costs. |
| dependency | [Existing short-annihilator exclusion](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Exact zero-value effective-support inequality, applied at true span and original d. |
| dependency | [Scalar logarithmic normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Scaling by q and normalized circle integral with content retained. |
| support | [Finite logarithmic mechanism](Yin_C_G0137_v1.md#argument) | Majorant, matrix path, coefficient and radial mechanism attribution at its accepted scope. |
| support | [All-input auxiliary existence boundary](Yin_C_G0570_v1.md#uniform-auxiliary-margin-fixed-scope) | Exact comparison: positive margin and linear degree are known, while term count/normalized l1 are not uniformly bounded. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0801_v1.md#normalized-sparse-cost-whole-independent-finding) | Entire actual fixed argument and statement, every direct interface, original cost and boundary, with antecedent authorship and source-proof limits preserved. |


### Decision isolated-whole-review-20261023-m04

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:52 |
| status | proved |
| reason | Select the newly performed isolated whole review of this exact fixed statement, complete argument and all selected input interfaces at their stated restricted scopes. Preserve the proved mathematical status, unchanged statement and argument, every nonreview relation and scope, and all historical decisions. The retained older unknown finding keeps its actual date, checks and limits; this new finding supplies new evidence at its actual date without certifying old isolation, backdating adoption, or completing or resuming G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire final theorem](#statement) | Normalized coefficient budget with unbounded q/raw heights, both nonzero and automatically closed zero-value scopes including Section5. |
| argument | [Entire argument](#argument) | Complete Sections1--5, all11 equations, original norms, finite constants, all cases and contribution limits. |
| dependency | [Uniform regularization mechanism](Yin_C_G0139_v1.md#argument) | Accepted layer-cake tails and finite logarithmic/radial transfer, with the changed normalized scale proved locally. |
| dependency | [Measurable-set inequality](../audits/literature/BS13/Yin_U001.md#bs13-u001) | Accepted absolute-constant pure-imaginary statement; no original-proof upgrade. |
| dependency | [Original angular estimate](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact epsilon, domain and original powered-degree costs. |
| dependency | [Existing short-annihilator exclusion](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Exact zero-value effective-support inequality, applied at true span and original d. |
| dependency | [Scalar logarithmic normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Scaling by q and normalized circle integral with content retained. |
| support | [Finite logarithmic mechanism](Yin_C_G0137_v1.md#argument) | Majorant, matrix path, coefficient and radial mechanism attribution at its accepted scope. |
| support | [All-input auxiliary existence boundary](Yin_C_G0570_v1.md#uniform-auxiliary-margin-fixed-scope) | Exact comparison: positive margin and linear degree are known, while term count/normalized l1 are not uniformly bounded. |
| review | [New isolated whole finding](../audits/reviews/Yin_R_G0801_v1.md#g0140-m04-isolated-whole-finding) | Complete exact fixed statement, whole argument, every selected input, all parameter/domain/original-degree costs, exceptional branches and source/noncompletion limits. |
