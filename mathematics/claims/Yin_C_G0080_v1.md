---
author: Yin
---
# Infinitely many frozen six-digit return words and a paid midpoint invariant on the odd subsequence

Date: 2026-10-12T16:09.
Human author Yin.
Internal fixed extraction under the continuing G0001 authorization.
Root is the sole author of the new period18 family, tables, seam/padding proof and midpoint/invariant consequences in the complete original D36.
g0001_matrix_recovery independently WHOLE-reviewed that actual23:52 body in R303 and NOW authors this exact statement and extraction wrapper.
It is therefore a contributor to this new artifact and cannot independently review the extraction.
Its D35 local-test/old-library authorship and C76 wrapper role remain disclosed.
R303 is original-proof support only.
Initial status is proof draft / under review pending another noncontributor's actual extraction review.

## Statement

Use the ACTUAL irreducible Salem quartic

    P(t)=1-t-t^2-t^3+t^4,
    beta>1 its real root, zeta either unit-circle conjugate,
    u=zeta+zeta^-1=(1-sqrt13)/2, u^2=u+3.

For EVERY n>=7 put N=2n and let Omega_n contain ALL eta in{-1,0,1}^N satisfying the complete original return F_eta(beta)=0, with F_eta(t)=sum_(i=0)^(N-1) eta_i t^i.
Retain the original independent digit probabilities1/4,1/2,1/4 and define

    z(eta)=the number of original zero digits,
    W_n=sum_(eta in Omega_n)2^z(eta),
    Pr_original(return at N)=W_n/4^N,
    pi_n(eta)=2^z(eta)/W_n,
    Z_n(eta)=-zeta^-n sum_(i=0)^(n-1)eta_i zeta^i,
    E_pi_n Z_n=0.

The complex squared modulus is exactly the sum of squares of TWO unweighted real neutral coordinates.
All original conjugate constraints and prior visits remain.
For each j=0,...,N-6, H_j resamples the six original digits in I_j={j,...,j+5}, conditional on EVERY outside digit, over the COMPLETE same-endpoint fiber

    {theta in{-1,0,1}^6: sum_(r=0)^5 theta_r beta^r=x_j},
    x_j=sum_(r=0)^5 eta_(j+r) beta^r,

with probabilities proportional to2^z(theta).
This includes all endpoints.
Use EXACTLY the adopted C76 operator and clock

    S_n=(1/(N-5))sum_(j=0)^(N-6) H_j,
    D_6,n(g)=<g,(Id-S_n)g>_pi_n
       =(1/2)sum_(eta,xi)pi_n(eta)S_n(eta,xi)
                                    |g(xi)-g(eta)|^2.

It is a positive self-adjoint contraction for the original pi_n.
No irreducibility assumption is made.

**A. Complete local test, proved directly in the retained argument.**
Every same-endpoint six-digit difference is P(a+bt) with integers a,b and coefficient vector

    (a,b-a,-a-b,-a-b,a-b,b), abs(a)+abs(b)<=2.

There are exactly13 integer possibilities including zero:4 unit single-coordinate directions,4 doubles,4 paired directions and zero.
A legal double has a legal unit intermediate.
With p=(1,-1,-1,-1,1), an original returned word is frozen if and only if every five-window x has BOTH signs among p_i x_i and every six-window theta fails BOTH following tests for EACH sigma in{+1,-1}:

    (a,b)=(sigma,sigma): theta_2=theta_3=sigma,
                  sigma*theta_0<=0, sigma*theta_5<=0;
    (a,b)=(sigma,-sigma): theta_1=sigma, theta_4=-sigma,
                  sigma*theta_0<=0, sigma*theta_5>=0.

This is equivalent to every complete six-digit endpoint fiber being a singleton.
It is a test on ACTUAL returned words.
Its complete proof is included here and does not import the parallel pending local-criterion material as a premise.

**B. An explicit original frozen family at every n=9k or9k+1.**
In ascending coefficient order set

    W=(-1,1,0,1,1,1,1,1,0,-1,-1,-1,-1,-1,0,-1,1),
    Q(t)=-1-t^2-t^3-t^5+t^7+t^9+t^10+t^12,
    W(t)=P(t)Q(t), B=W0,
    C_k=B^(k-1)W, k>=1.

Powers of words mean CONCATENATION.
The final0 in B is an actual digit, length(B)=18, and

    length(C_k)=18k-1,
    C_k(t)=P(t)Q(t)sum_(j=0)^(k-1)t^(18j),
    z(C_k)=4k-1.

For EVERY k>=1 and INDEPENDENT integers0<=l,r<=2, both signed words +/-0^l C_k 0^r return at every original conjugate and have every six-digit endpoint fiber singleton.
The complete18-row five-window sign table, exhaustive paired-residue exclusions and exceptional outer windows are retained in full.
No arbitrary larger padding or unchecked frozen-word concatenation is asserted safe.

At even original lengths the following are FOUR DISTINCT nonzero frozen states in Omega_n:

| Original half-length | Four states | Total outer zeros p |
| --- | --- | --- |
| n=9k | +C_k0, -C_k0, +0C_k, -0C_k | 1 |
| n=9k+1 | +0C_k00, -0C_k00, +00C_k0, -00C_k0 | 3 |

The statements hold for EVERY integer k>=1, with n>=9 in the operator's domain.
The list does not purport to exhaust all frozen states, components or lengths.
The word's full return and all-k frozen property are hand-proved; no finite native output or extrapolation is required.

**C. Zero global gap at infinitely many lengths and the exact refuted premise.**
Define the actual real Rayleigh gap

    lambda_(6,n)=inf_(Var_pi_n(g)>0)D_6,n(g)/Var_pi_n(g).

Then

    lambda_(6,n)=0 for EVERY n=9k and9k+1, k>=1.

Each displayed positive-mass singleton and the distinct zero state give a centered positive-variance indicator of zero Dirichlet energy.
Consequently there do NOT exist c>0 and n0 with lambda_(6,n)>=c/(N-5) for EVERY n>=n0.
This refutes that eventual-ALL-n positive global-gap premise for this exact operator.
C76's logical conditional implication from the premise remains valid; failure of the premise gives no conclusion about the original chronological critical mean.
No assertion is made about the gap or full graph at all other n.

**D. The original midpoint is nonzero exactly on the odd-k part of this displayed family.**
Put

    A_8(t)=-1+t+t^3+t^4+t^5+t^6+t^7, A_9=A_8.

The exact polynomial identity

    A_8+t^8-t^7-t^9=-P(1+t^2+t^3+t^5)

gives -zeta^-8 A_8(zeta)=1-u and -zeta^-9 A_9(zeta)=zeta^-1(1-u).
For ODD k, the two templates in each row of B with no overall sign reversal have midpoint values zeta^-1(1-u) and1-u, respectively.
The two reversed states have their negatives.
Thus ALL FOUR have squared modulus

    |Z_n(eta)|^2=(1-u)^2=4-u>0.

For EVEN k, all four original midpoints are EXACTLY0.
The midpoint then cuts at a complete period or omits only its actual terminal zero.
In particular zero global gap at every length in C does not assert a nonzero-midpoint invariant at every such length.

**E. Full original mass and an invariant obstruction on the odd-k subsequence.**
Let p be1 or3 as in B, so N=18k-1+p.
Each displayed state has exactly4k-1+p original zeros, unconditional original probability2^(4k-1+p)/4^N and stationary mass

    w_(k,p)=2^(4k-1+p)/W_n.

The total mass of the four-state family is2^(4k+1+p)/W_n.
For ODD k let F_(k,p) be exactly that family and define H_n=Z_n*1_(F_(k,p)).
Then

    E_pi_n H_n=0, S_n H_n=H_n,
    ||H_n||_2^2=<Z_n,H_n>_pi_n
       =rho_(k,p)=(4-u)2^(4k+1+p)/W_n>0.

Let P0 denote orthogonal projection onto ker(Id-S_n).
Then ||P0 Z_n||_2^2>=rho_(k,p).
The Poisson equation

    (Id-S_n)g=Z_n

has NO complex-valued solution at every displayed odd-k length.
This uses the ORIGINAL midpoint without removing its invariant component.
Moreover, in the real invariant space

    V_n=span_R{S_n^j Re Z_n,S_n^j Im Z_n: j>=0},

one has

    inf_(g in V_n,Var_pi_n(g)>0)D_6,n(g)/Var_pi_n(g)=0.

The nonzero kernel projection of at least one real coordinate belongs to that SAME finite cyclic space and remains globally centered, so it is not a nonzero constant.
This supplies an infinite-subsequence obstruction to an eventual-ALL-n positive lower comparison obtained merely by restricting to V_n.
It does not assess component-centered residuals or classify all component means.

**F. All update times, every time average and the exact probability cost.**
For each FIXED displayed odd-k length and EVERY integer auxiliary update time t>=0,

    <Z_n,S_n^t Z_n>_pi_n>=rho_(k,p).

The correlations are real and nonnegative because the actual spectrum lies in[0,1].
For the stationary S_n chain X_t started in pi_n and EVERY integer J>=1,

    E |J^-1 sum_(t=0)^(J-1) Z_n(X_t)|^2>=rho_(k,p).

The normalization retains all J diagonal and2(J-h) lag terms, whose total is J^2.
These are statements about auxiliary updates at FIXED original n, not chronological growth as n varies.
From the original bounds2^N<=W_n<=4^N the EXACT paid contribution obeys, for odd k,

    (4-u)2^(3-32k-p)<=rho_(k,p)<=(4-u)2^(2-14k).

The displayed positive invariant contribution therefore tends to0 exponentially and yields no positive uniform fraction, diffusive lower variance or full component classification.
At even k this family's actual midpoint contribution is0 despite the zero global gap.

The theorem concerns the SAME fixed quartic and original law.
It proves neither an all-n graph classification nor the original chronological mean/variance branch, a degree-uniform arithmetic surplus or a Mahler gap.
The earlier C76 annihilation paths and older-block results concern different words and remain compatible.
D33/J93 supplied a discovery lead only, and the parallel D35/C79 local-test or library material is not a logical dependency.
Every mathematical step of this periodic result is retained below, with only the adopted C76 original operator/law interface reused.
No new external mixing theorem is imported.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T16:09 |
| status | open |
| reason | Register the complete period18 frozen family, exact original midpoint parity/masses, infinitely recurring zero global gap, and the paid odd-subsequence invariant/Poisson/correlation/time-average obstruction. Retain the entire original23:52 D36. R303 whole-reviewed the original body, but its reviewer now authors this new statement/wrapper, which requires another noncontributor's actual extraction review before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, SAME original law and six-digit clock, all k and allowed paddings, exact odd/even restrictions, original rho bounds, and only the stated infinite-subsequence and eventual-premise conclusions. |
| argument | [Entire retained original body](#argument) | COMPLETE original allocation/lead/reuse/candidate, Sections1--6/equations1--14, six anchors, every period/seam/boundary table, source/contribution limits and actual23:52 freeze. |
| dependency | [C76 adopted original operator](Yin_C_G0076_v1.md#six-digit-original-law-operator) | Exact fixed quartic/full-return state space, positive original probabilities2^z/W_n, complete arbitrary-endpoint heat bath with N-5 clock, true complex midpoint, global sign symmetry, positive self-adjoint contraction and Dirichlet normalization. |
| dependency | [C76 actual gap interface](Yin_C_G0076_v1.md#six-digit-quantitative-gap-boundary) | Actual global Rayleigh definition and precisely conditional eventual positive-gap premise whose failure is proved here. No global irreducibility or positive gap is an assumed input. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0303_v1.md#period18-whole-independent-finding) | Complete actual original23:52 D36 and its direct C76 interfaces were independently reconstructed before this new wrapper was authored. It is not prospective review or adoption of this extraction. Finding relationship: self-reviewed. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T16:18 |
| status | proved |
| reason | Adopt original whole R303 and distinct actual extraction R306. Fix the full period18 frozen family on two infinite length subsequences, odd-k paid true-midpoint invariant and exact limits. This refutes the eventual-ALL-n positive global-gap premise of the specified six-digit operator, not the conditional implication or a chronological mean classification. Root authored the proof and relies on the disclosed separately organized noncontributor findings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, SAME original law and six-digit clock, all k and allowed paddings, exact odd/even restrictions, original rho bounds, and only the stated infinite-subsequence and eventual-premise conclusions. |
| argument | [Entire retained original body](#argument) | COMPLETE original allocation/lead/reuse/candidate, Sections1--6/equations1--14, six anchors, every period/seam/boundary table, source/contribution limits and actual23:52 freeze. |
| dependency | [C76 adopted original operator](Yin_C_G0076_v1.md#six-digit-original-law-operator) | Exact fixed quartic/full-return state space, positive original probabilities2^z/W_n, complete arbitrary-endpoint heat bath with N-5 clock, true complex midpoint, global sign symmetry, positive self-adjoint contraction and Dirichlet normalization. |
| dependency | [C76 actual gap interface](Yin_C_G0076_v1.md#six-digit-quantitative-gap-boundary) | Actual global Rayleigh definition and precisely conditional eventual positive-gap premise whose failure is proved here. No global irreducibility or positive gap is an assumed input. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0303_v1.md#period18-whole-independent-finding) | Complete actual original23:52 D36 and its direct C76 interfaces were independently reconstructed before this new wrapper was authored. It is not prospective review or adoption of this extraction. Finding relationship: self-reviewed. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0306_v1.md#c80-period18-actual-extraction-finding) | ENTIRE actual A--F, full retained original and exact C76 interfaces; all parity/mass/clock/projection limits checked by a noncontributor at the actual SELF relationship. |

## Registration and complete preservation

The [original entire D36 freeze](#period18-scope-and-author-freeze) is extraction ancestry, not an additional mathematical dependency.
The complete original saved file has18431 characters,215 lines and6 explicit anchors.
Its ENTIRE body follows after removing only duplicate author/framework front matter, demoting its first title by one hash, and rebasing the two draft-local D33/D35 links to ../drafts/ from this Claim directory.
Ordinary line-ending and separating/terminal blank-line normalization is allowed.
All original paragraphs, formulas,14 numbered equations, tables, six explicit anchors, discovery/reuse/candidate history, role/source limits and freeze remain.
No proof passage is replaced by a summary.

Root remains the sole author of the new periodic theorem.
g0001_matrix_recovery's R303 is the original independent whole review; the same agent NOW contributes this extraction wrapper and therefore needs another noncontributor's actual review.
Its own D35 antecedent and C76 wrapper history were disclosed in R303 and remain separate from root's period18 proof.
The local criterion is reproved completely in the retained original; neither D35/C79 nor J93 supplies an unreviewed premise.
Historical pending-review and discovery-lead prose remains at its actual original date and is not overwritten by this extraction.

The sole adopted proof interface is C76's actual original-law operator, including its established positive finite-dimensional spectral properties.
Existing source-attribution/access boundaries remain; no new source theorem or native result is adopted.
Exact preservation and structural validation are not mathematical acceptance.
This allocation performs no adoption, D retirement or native mathematical execution.

## Argument

## Infinitely recurring frozen words for the original six-digit heat bath

Date: 2026-10-12T15:52.
Human author Yin.
Root AUTHOR inquiry under the continuing G0001 instruction and retained weekly allowance.
Root selects the period18 concatenation, proves all local and seam conditions, and derives its actual midpoint/invariant consequences here.
A different noncontributor must review the complete proof.
No new native mathematical execution, external source or allowance is proposed.

## Actual lead, bounded reuse and responsible candidate

The just-completed AUTHOR [D33 finite observation](Yin_C_G0081_v1.md#six-digit-finite-complete-author-observation) and [J93 actual payload](../computations/programs/Yin_J_G0093/readme.md) exhibit a17-digit word W and its padded signs among frozen states at n9,10.
That new native payload is still awaiting independent reconstruction; it is a DISCOVERY LEAD, not a proof premise for the all-length claims below.
Its word and quotient will be verified directly by integer polynomial multiplication, and every local fiber obstruction will be checked by complete hand tables.
No n beyond10 is computed or inferred from that table.

The adopted [C76](Yin_C_G0076_v1.md#statement) fixes the precise SIX-digit arbitrary-endpoint operator and original conditional law, but only eliminates the older long-core pair.
[C64](Yin_C_G0064_v1.md#statement), [C68](Yin_C_G0068_v1.md#statement) and [C70](Yin_C_G0070_v1.md#statement) treat different update operators or older families.
The currently frozen AUTHOR [D35](Yin_C_G0079_v1.md#six-digit-library-entire-author-freeze) investigates the complete local six-digit criterion and removal of the entire old F/G/H library; it is not yet adopted and is NOT a missing premise here.
Its exact local algebra is directly proved below so the all-length argument does not depend on its pending review.
This records the parallel antecedent and does not claim novelty for the basic quotient test.

A bounded G Claim/ledger/draft search for period18,17-digit and six-digit periodic families found the new D33 observation and unrelated number occurrences, but no adopted version of this particular all-length frozen mechanism.
This is not an exhaustive literature or priority claim.
The old finite Markov projection facts are locally rederived at the NEW operator's exact scope.

The candidate is B=W followed by ONE zero digit, length18, with C_k=B^(k-1)W.
Every C_k remains a full P multiple.
The essential new obligation is every six-digit SEAM of repeated B and every allowed outer padding: neither arbitrary zero padding nor concatenation of frozen states is generally safe.
The intended conclusion is global-gap failure at infinitely many original lengths, and a paid nonzero TRUE-midpoint invariant at an odd-k subsequence, without claiming diffusive growth, a uniform probability fraction or an unrestricted Mahler gap.

<a id="period18-exact-local-frozen-test"></a>
## 1. Complete local immobility test

Fix the ACTUAL quartic P(t)=1-t-t^2-t^3+t^4, its real root beta>1 and neutral root zeta.
Let u=zeta+zeta^-1=(1-sqrt13)/2, so u^2=u+3.
For n>=7 let N=2n and use EXACTLY C76's full original returned words Omega_n, original independent digit probabilities1/4,1/2,1/4, weight2^z, normalizer W_n and pi_n=2^z/W_n.
The operator S_n chooses uniformly one of N-5 six-digit intervals and resamples its complete SAME-ENDPOINT fiber with those original weights.
All endpoints and all original field returns are retained.

Two length-six words theta,theta' in{-1,0,1}^6 have equal endpoint if and only if their difference is P(a+bt) for integers a,b, by monic division and minimal degree4.
Its coefficients are

    Delta=(a,b-a,-a-b,-a-b,a-b,b).                       (1)

Since each digit difference is at most2 in absolute value, abs(a+b)<=2 and abs(a-b)<=2, hence abs(a)+abs(b)<=2.
Apart from(0,0), the COMPLETE integer possibilities are the four unit single-coordinate changes, their four doubles, and the four paired changes(a,b)=(sigma,sigma) or(sigma,-sigma), sigma in{+1,-1}.
A doubled single-coordinate change, if legal, has a legal unit intermediate change by convexity of[-1,1] and integrality.
Thus it suffices to exclude the unit single changes and the paired changes; no integer quotient outside this list can be legal.

A five-digit word x admits addition of sigma*P exactly when sigma*p_i*x_i<=0 for all five indices, where p=(1,-1,-1,-1,1).
Consequently BOTH signs are excluded when the signed list(p_i*x_i) has at least one positive and one negative entry.
These single-coordinate changes occupy the first or last five positions of a six-digit interval.
For words of length at least6, every five-position interval is contained in a six-position interval, including both ends.

For a six-digit word theta the paired changes have exact necessary and sufficient conditions

    (a,b)=(sigma,sigma):
      theta_2=theta_3=sigma,
      sigma*theta_0<=0, sigma*theta_5<=0;

    (a,b)=(sigma,-sigma):
      theta_1=sigma, theta_4=-sigma,
      sigma*theta_0<=0, sigma*theta_5>=0.                 (2)

Indeed the first increment is(sigma,0,-2sigma,-2sigma,0,sigma), and the second is(sigma,-2sigma,0,0,2sigma,-sigma).
Checking those entries proves both directions.
An original returned word is S_n-frozen if and only if ALL its five-windows exclude both single signs and ALL six-windows fail both paired tests(2).
Equivalently each six-digit endpoint fiber is a singleton.
This is a complete criterion for actual returned words, not for words that fail the full return equation.

<a id="period18-original-word-and-return"></a>
## 2. Exact period and original return at every repetition

In ascending coefficient order define

    W=(-1,1,0,1,1,1,1,1,0,-1,-1,-1,-1,-1,0,-1,1),
    Q=(-1,0,-1,-1,0,-1,0,1,0,1,1,0,1),
    B=W0, length(B)=18.                                (3)

The terminal0 in B is an ACTUAL original digit.
Direct coefficient multiplication gives W(t)=P(t)Q(t):

    Q(t)=-1-t^2-t^3-t^5+t^7+t^9+t^10+t^12.

In particular the convolution coefficients at13,14,15,16 are-1,0,-1,1, and the low coefficients are exactly the first13 entries displayed in W.
This checks the entire finite polynomial identity, not a numerical evaluation or a native-result assumption.
W has length17 and exactly three zero digits.

For EVERY integer k>=1 form the concatenation

    C_k=B^(k-1) W, length(C_k)=18k-1,
    C_k(t)=W(t)sum_(j=0)^(k-1)t^(18j),
    C_k(t)=P(t)Q(t)sum_(j=0)^(k-1)t^(18j).              (4)

Every digit is still in{-1,0,1}.
Every block is an original full-field return, so(4) proves return directly at beta and all its conjugates.
The word has exactly4k-1 zeros: three per W and k-1 actual separating zeros.
This concatenation is not asserted frozen until every seam is checked in Section3.

<a id="period18-complete-seam-and-padding-table"></a>
## 3. Every internal window, every seam and both boundaries

Consider the two-sided period obtained by repeating B.
Its digits at positions0,...,17 are

    -1,1,0,1,1,1,1,1,0,-1,-1,-1,-1,-1,0,-1,1,0.

All internal windows of C_k occur in this period, so a finite period table checks every k and EVERY seam.
For each starting residue j, the following two relative positions in its five-window have respectively POSITIVE and NEGATIVE signed p_i*x_i.
Positions are numbered0,...,4.

| Start j mod18 | Positive position | Negative position |
| --- | --- | --- |
| 0 | 4 | 0 |
| 1 | 0 | 2 |
| 2 | 4 | 1 |
| 3 | 0 | 1 |
| 4 | 0 | 1 |
| 5 | 0 | 1 |
| 6 | 0 | 1 |
| 7 | 0 | 4 |
| 8 | 1 | 4 |
| 9 | 1 | 0 |
| 10 | 1 | 0 |
| 11 | 1 | 0 |
| 12 | 1 | 0 |
| 13 | 2 | 0 |
| 14 | 1 | 2 |
| 15 | 3 | 0 |
| 16 | 0 | 3 |
| 17 | 1 | 2 |

Each sign follows by substituting the explicitly displayed period and p=(1,-1,-1,-1,1); none is zero.
This excludes every one-site move and its double, including seams.

For the same-sign paired case in(2), the prerequisite theta_2=theta_3=sigma occurs ONLY at the following residues.
The displayed endpoint product is positive and violates its required<=0 inequality.

| Start residues | sigma | Violating endpoint product |
| --- | --- | --- |
| 1,3,4 | +1 | sigma*theta_0=+1 |
| 2 | +1 | sigma*theta_5=+1 |
| 7,8 | -1 | sigma*theta_5=+1 |
| 9,10 | -1 | sigma*theta_0=+1 |

At every other residue there is no such nonzero common middle sign.
For the opposite-sign paired case, the prerequisite theta_1=sigma,theta_4=-sigma occurs ONLY in the next table; again the indicated endpoint violates(2).

| Start residues | sigma | Violating endpoint product |
| --- | --- | --- |
| 5,6 | +1 | sigma*theta_0=+1, whereas it must be<=0 |
| 12 | -1 | sigma*theta_0=+1, whereas it must be<=0 |
| 17 | -1 | sigma*theta_5=-1, whereas it must be>=0 |

These three finite hand tables exhaust all possible legal quotient changes by Section1.
Hence EVERY internal six-fiber of C_k is singleton.

Now attach l leading zeros and r trailing zeros, where INDEPENDENTLY0<=l,r<=2.
With one leading zero the additional windows agree with the period immediately before W; with one trailing zero they agree with its period immediately after W.
Two leading zeros add just ONE exceptional first five-window and ONE exceptional first six-window,

    (0,0,-1,1,0), (0,0,-1,1,0,1).

Two trailing zeros similarly add just ONE exceptional last five-window and ONE exceptional last six-window,

    (0,-1,1,0,0), (-1,0,-1,1,0,0).                      (5)

The five-windows in(5) have signed lists(0,0,1,-1,0) and(0,1,-1,0,0), respectively, so have both signs.
Both exceptional six-windows have theta_2=-1 and theta_3=+1, excluding the same-sign pair, and theta_1=0, excluding the opposite-sign pair.
All other windows were already checked.
No arbitrary further zero padding is asserted safe.
Global sign reversal preserves singleton fibers because it bijects all legal original digits and endpoints.

It follows that EVERY padded signed word +/-0^l C_k 0^r with l,r<=2 is locally frozen; it is also an actual return by(4).
For the EVEN original length N=2n the useful choices are l+r=1 or3:

    n=9k:   +/-C_k0, +/-0C_k;
    n=9k+1: +/-0C_k00, +/-00C_k0.                        (6)

These are FOUR distinct actual frozen states at each displayed n, for EVERY k>=1.
They have length2n with all original zero digits included, and n>=9 lies in the adopted C76 domain.
Their four-state list need not exhaust the frozen states or other components.
In particular this is not an extrapolation of the exact finite counts at k1.

<a id="period18-gap-and-exact-midpoint"></a>
## 4. Infinitely many zero global gaps and the true midpoint

The original stationary probability of every word is positive.
Each word in(6) is a singleton component, while the all-zero returned word is a distinct positive-mass state.
Its centered indicator therefore has positive variance and zero Dirichlet energy.
Thus the ACTUAL C76 global Rayleigh gap satisfies

    lambda_(6,n)=0 for EVERY n=9k and9k+1, k>=1.        (7)

This is an infinite unbounded set.
It DISPROVES the formerly unproved possible eventual premise lambda_(6,n)>=c/(N-5) for ALL sufficiently large n with c>0.
C76's logical conditional implication from that premise remains valid, but that particular global-gap route can no longer use it.
No conclusion about the original chronological critical mean follows from failure of the auxiliary premise.

For the TRUE midpoint Z_n=-zeta^-n times the first-half digit polynomial, put

    A_8(t)=-1+t+t^3+t^4+t^5+t^6+t^7,
    A_9=A_8.

The equality A_9=A_8 uses the actual zero digit W_8.
Direct polynomial multiplication gives

    A_8(t)+t^8-t^7-t^9=-P(t)(1+t^2+t^3+t^5).

At the actual neutral root this yields

    -zeta^-8 A_8(zeta)=1-u,
    -zeta^-9 A_9(zeta)=zeta^-1(1-u),
    abs(1-u)^2=(1-u)^2=4-u>0.                           (8)

This is a hand-verified original-field identity, not acceptance of the native midpoint values.

If k=2j+1 is ODD, the midpoint of each word in(6), after its actual leading padding l, lies after j COMPLETE18-digit blocks and then8 or9 digits of the next W.
Those complete blocks return exactly, and their common monomial factor cancels with the midpoint normalization.
Thus the two positive-orientation values at either displayed n are zeta^-1(1-u) and1-u, respectively; the two negatives give their opposites.
All four squared moduli are4-u.

If k=2j is EVEN, the cut after removing l leading zeros is at18j or18j-1.
The latter omits only the actual terminal zero of a complete B block.
In both cases the prefix consists of complete returned blocks, with no remaining nonzero contribution.
Thus all four midpoints are0.
In full,

    abs(Z_n(eta))^2=4-u for all four displayed states if k odd,
    Z_n(eta)=0 for all four if k even.                  (9)

The even-k case is essential: the global zero gap alone is not a nonzero-midpoint invariant claim at every listed length.

<a id="period18-original-mass-and-invariant"></a>
## 5. Every original probability and the infinite observable obstruction

Let p=l+r be1 at n9k and3 at n9k+1.
Every displayed frozen word has exactly4k-1+p zero digits.
Its UNCONDITIONAL original probability and CONDITIONAL stationary mass are respectively

    2^(4k-1+p)/4^N, w_(k,p)=2^(4k-1+p)/W_n.            (10)

The four states are distinct and no labels are merged.
For ODD k let F_(k,p) be these four states and put H_n=Z_n*1_(F_(k,p)).
Sign pairing gives E_pi H_n=0.
Every state in its support is a singleton, so S_n H_n=H_n, and

    ||H_n||_2^2=<Z_n,H_n>
      =rho_(k,p)=(4-u)2^(4k+1+p)/W_n>0.                (11)

The constant in(11) retains the ENTIRE original conditioned law.
It agrees with the native k1 expressions if that finite calculation is independently accepted, but the present equality uses only the direct all-k proof and the definition of W_n.

Since E_pi Z_n=0 by original global sign symmetry, the finite self-adjoint projection P0 onto ker(Id-S_n) satisfies

    ||P0 Z_n||_2^2>=rho_(k,p)>0.                        (12)

Indeed H_n is invariant and <Z_n,H_n>=||H_n||^2; orthogonal projection and Cauchy--Schwarz yield the bound.
Thus the uncentered Poisson equation(Id-S_n)g=Z_n has NO solution at EVERY displayed odd-k length.
Taking inner product with H_n proves this directly.
For the real invariant space generated by S_n^j ReZ_n and S_n^j ImZ_n, the Poincare infimum is0 as well: the nonzero kernel projection of at least one real coordinate belongs to that finite cyclic space, obtained by the real polynomial which is1 at eigenvalue1 and0 at the finitely many other eigenvalues.
Its global mean is0, so it is not a nonzero constant.

C76's operator is a positive self-adjoint contraction, hence every eigenvalue lies in[0,1].
Therefore for ALL integer UPDATE times t>=0, with n held fixed at one of these odd-k lengths,

    <Z_n,S_n^t Z_n>_pi>=rho_(k,p).

For its stationary update chain and every integer J>=1 this gives

    E|J^-1 sum_(t=0)^(J-1) Z_n(X_t)|^2>=rho_(k,p).      (13)

To verify the last line, expand the square as J diagonal correlations and2(J-h) correlations at lag h, then use the preceding nonnegative spectral bound at every lag.
The total count is J^2.
This concerns auxiliary UPDATE time at fixed original word length, not chronological variance growth as n changes.

The original all-zero word gives W_n>=2^N, and the total independent original mass gives W_n<=4^N.
With N=18k-1+p the EXACT payment in(11) obeys

    (4-u)2^(3-32k-p)<=rho_(k,p)<=(4-u)2^(2-14k).        (14)

Thus this displayed rare-family lower component tends to0 exponentially.
It supplies no positive uniform fraction, diffusive lower growth, complete component-mean classification or positive lower spectral estimate.
At EVEN k its actual-midpoint contribution is0 by(9), even though(7) still holds.

<a id="period18-scope-and-author-freeze"></a>
## 6. Scope, changed discriminator and entire author freeze

The exact new result is a SAME-original-law frozen construction at EVERY n=9k or9k+1, with nonzero TRUE-midpoint invariant obstruction when k is odd.
It closes the proposed eventual positive GLOBAL-gap lower bound for the six-digit operator, and also closes a simple repair that merely restricts to the uncentered true-midpoint-generated invariant space at all large n.
A future useful dynamics must change this operator, control actual component means/centered residuals with their masses, or use a different original-law argument.
The prior all-n paths for the OLD C70 cores and D35's older block library are compatible: those are different words.
No source or Claim is silently corrected or retired.

This proof does not classify all frozen words, every component or every n; does not give chronological mean/variance growth; and does not establish a degree-uniform arithmetic surplus or a Mahler gap.
The input remains the same fixed quartic with positive m.
No phase, neutral root or original norm is discarded.
J93 only suggested W; every all-k proof obligation was proved above without native enumeration, and no mathematical program was executed in this inquiry.
The classical finite spectral/projection facts used in Section5 are proved locally at their explicit finite-dimensional scope; no new external source theorem is invoked.

Author checking covered all thirteen bounded(a,b) possibilities including zero, both doubled-single intermediate moves, both paired signs, all18 five-window sign witnesses, every qualifying paired residue and its strict endpoint violation, both exceptional outer windows, each finite-core length/zero count and entire polynomial quotient, all four padded signed words at both even lengths, the ODD versus EVEN midpoint split, original probability and normalization powers, zero-gap versus observable conclusions, the eigenvalue1 projection in the real cyclic space, every update-lag and probability factor, and the nonimplication to original chronological mean.
Root supplied all new periodic-family mathematics and cannot independently review it.

Freeze the ENTIRE allocation/lead/reuse/candidate history and Sections1--6/equations1--14 at 2026-10-12T15:52.
The assigned noncontributor review must check the actual full body and the accepted C76 operator/input scope, not infer the periodic theorem from the pending J93 finite findings or from an earlier operator's obstruction.
This is a complete AUTHOR proof draft, not an adopted Claim, independent finding or unrestricted result.
