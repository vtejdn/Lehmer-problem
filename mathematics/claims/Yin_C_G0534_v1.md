---
author: Yin
---

# Exact partial-mask Shannon and collision information with complete causal costs

The complete original L223 Sections 1--6/(1)--(21) are retained, including the full-mask reconstruction, every conditional-information convention and actual positive/torsion controls.
The original [R793 whole](../audits/reviews/Yin_R_G0793_v1.md#conditional-mask-complete-independent-review) retains its actual 2026-10-09T21:40 written-chain inspection, precise ODo07 statement/normalization reading and attribution-only correction.
The correction identified a classical contraction and filled source attribution without changing the complete local proof; it is not an independently found mathematical gap.
No original C binding or isolated-context fact is invented from the old noncontribution/independent label.

## Statement

<a id="partial-mask-fixed-scope"></a>
Let alpha be any algebraic unit with actual monic minimal P=sum_(i=0)^d p_i t^i,p_d=1,p_0 in {-1,1}, and let xi_j be two-sided iid fair bits.
For every n>=1, the finite endpoint sums indexed j<n below mean j=0,...,n-1.
Use the exact original parity/carry construction
\[
b_j=\sum_{i=1}^d(p_i\bmod2)\xi_{j-i}\bmod2,\quad
M_j=(1-p_0)/2+p_0b_j,\quad
\sigma_j=\xi_j\ {\rm XOR}\ b_j,\quad
C_j=\lfloor(\sum_i p_i\xi_{j-i})/2\rfloor,
\quad S_n=\sum_{j<n}\sigma_j\alpha^j,\ T_n=\sum_{j<n}C_j\alpha^j .
\]
Set ell=min{i>=1:p_i odd},w=d-ell, and
Z_k=b_(k+ell)=xi_k+sum_(r=1)^w q_r xi_(k-r) mod2, q_r=p_(ell+r) mod2.
For w=0 this is the identity filter; otherwise q_w=1.
Every complete bi-infinite output sequence has exactly 2^w input lifts, determined by any w consecutive input bits.
For the original uniform input, those w bits are independent of the full output sigma-field and the conditional lifts are equiprobable.
For every finite input endpoint Y, H(Y|full mask)<=w log2.
For every n>=1 the iid vector V_n=(Z_k:-d<=k<=n-1), of length n+d, gives
H(T_n|V_n)<=w log2 and E Col(T_n|V_n)>=2^(-w).
Its original mask times are -d+ell,...,n-1+ell; the ell-step look-ahead and every boundary bit are charged.

For any finite vector V of independent coordinates, any finite Y jointly distributed with V, and an independent selector A including each coordinate with probability theta in [0,1],
\[
H(Y|A,V_A)\ge(1-\theta)H(Y)+\theta H(Y|V),\quad
I(Y;A,V_A)\le\theta I(Y;V)\le\theta H(Y).
\]
There is no Y/V independence requirement.
If V consists of iid fair bits, kappa=(1-theta)/(1+theta) and
K_Y(theta)=E_(A,V_A)Col(law(Y|A,V_A)), then
\[
Col(Y)\le K_Y(\theta)\le Col(Y)^\kappa .
\]
The average includes both the selector and its actually observed values; it is not a bound for every observation or an adaptive selector.
The classical Boolean hypercontractive specialization p=1+theta,q=2,rho=sqrt(theta) is attributed precisely to ODo07, with the complete local two-point/strong-convexity/tensor proof retained.

For the actual endpoints, p_n=Col(S_n), K_n=K_(T_n), every finite n has
\[
H(T_n|A,(V_n)_A)\ge(1-\theta)[H(S_n)-2d\log2],\quad
2^{-2d}p_n\le K_n(\theta)\le2^{2d\kappa}p_n^\kappa.
\]
At each fixed alpha and theta<1,
liminf H(T_n|A,(V_n)_A)/n>=(1-theta)h_1(alpha), and
\[
\kappa h_2(\alpha)\le\liminf-\log K_n/n
\le\limsup-\log K_n/n\le h_2(\alpha).
\]
For 0<delta<kappa the exceptional observation bound is
\[
\Pr\{Col(law(T_n|A,V_A))>
e^{-(\kappa-\delta)H_2(T_n)}\}\le e^{-\delta H_2(T_n)}.
\]
The H_2(T_n)=0 case is only trivial; no uniform positive original rate is supplied.

For causal observation O_n=(xi_(-d),...,xi_(-1),M_0,...,M_(n-1)), let L=min(n,ell),t_0=n-L and G(o)=sum_(u=t_0)^(n-1)M_u.
Conditional on every possible O_n=o, the terminal L input bits remain independent fair bits, S_n is uniform on 2^L values, and
\[
T_n=\operatorname{constant}(o)+\sum_{u=t_0}^{n-1}\xi_u v_u(o),\quad
v_u(o)=\alpha^u[p_0M_u+\sum_{i=1}^{n-1-u}(p_i/2)\alpha^i].
\]
The positive indices in that sum are less than ell and have even p_i.
For every Renyi order a in [0,infinity], at each such observation,
\[
H_a(S_n|O_n=o)=L\log2,\quad
G(o)\log2\le H_a(T_n|O_n=o)\le L\log2,\quad
2^{-L}\le Col(T_n|O_n=o)\le2^{-G(o)}.
\]
On sampling the observation, G is Binomial(L,1/2), so
E H_a(T_n|O_n)>=(L/2)log2 and
2^(-L)<=E Col(T_n|O_n)<=(3/4)^L.
The Renyi expression is explicitly the average of individual conditional entropies.
If p_i=0 for 1<=i<ell, the upper average collision bound is attained, including every ell=1 case.
Without the initial past bits,
H(T_n|M_0,...,M_(n-1))<=(d+L)log2 and conditional support is at most 2^(d+L).
Thus full causal disclosure still has zero endpoint conditional rate at fixed input; the valid independent remainder has horizon L<=d.

For the actual torsion family P=t^d+1,d a power of two, ell=d,w=0, full disclosure determines all input, the causal average collision is exactly (3/4)^min(n,d), and every partial-observation collision is at least (n+1)^(-2d).
For alpha=phi,P=t^2-t-1,ell=w=1, full disclosure leaves one global-complement bit, causal average collision is 3/4, while independent theta<1 disclosure satisfies
K_n(theta)<=2^(4kappa)2^(-kappa ceil(n/2)) and has lower collision rate at least kappa log2/2.
The radical controls have their actual ell=r,w=r,degree 2r and fixed M=phi.
No result permits dependent/adaptive mask selection, repeated independent gains from overlapping terminal windows, a uniform near-one endpoint floor, or an unrestricted gap.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:10 |
| status | open |
| reason | Register the exact complete statement and every necessary original argument, with genuine author, source, finite-evidence and failure boundaries. Current whole mathematical inspection and adoption are separate actual acts; no old review is backfilled with this C input and no research execution is resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Any actual algebraic unit/original parity carry, all span-zero/nonzero full reconstruction and exactly charged finite observations, arbitrary jointly dependent finite Y with independent-coordinate Shannon disclosure, fair-cube average collision and exceptional outcomes, every causal terminal/p0/Renyi case and exact positive/torsion/radical controls, with all uniformity/selection limits. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/equations(1)--(21), complete two-sided finite reconstruction and infinite-cylinder argument, entropy concavity, exact Walsh projection/noise identity/local tensor proof, Holder exponents, all2d charges/limit directions, causal independent basis/triangular coefficients and actual controls, plus original resolved ODo07 attribution correction and inspection limits. |
| dependency | [Exact parity carry and all-Renyi boundary](Yin_C_G0530_v1.md#statement) | Complete original iid mask/parity output, dependent carry, actual endpoint identity and at-most2d log2 comparison for all Renyi orders; not independent summand selection. |
| dependency | [Finite convexity and tensorization](Yin_C_G0508_v2.md#cyclic-noise-tensor-contraction) | Only fully proved finite-probability strong-convexity inequality and correct-direction Minkowski tensorization; no stationary theorem or substitute process. |
| support | [Independent thinning distinction](Yin_C_G0282_v1.md#statement) | Existing theorem needs external independent selection of summands; it is not applied to the dependent original mask. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:21 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire retained argument after the actual whole SELF inspection recorded in R735. Every used mathematical dependency is resolved at its explicit scope, the complete original proof and necessary source/native/failure facts are retained, and no unresolved mathematical issue affects this restricted theorem. The old whole review retains its missing declaration and unestablished initial context; this current SELF neither creates independent evidence nor closes M04 or any research Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Any actual algebraic unit/original parity carry, all span-zero/nonzero full reconstruction and exactly charged finite observations, arbitrary jointly dependent finite Y with independent-coordinate Shannon disclosure, fair-cube average collision and exceptional outcomes, every causal terminal/p0/Renyi case and exact positive/torsion/radical controls, with all uniformity/selection limits. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/equations(1)--(21), complete two-sided finite reconstruction and infinite-cylinder argument, entropy concavity, exact Walsh projection/noise identity/local tensor proof, Holder exponents, all2d charges/limit directions, causal independent basis/triangular coefficients and actual controls, plus original resolved ODo07 attribution correction and inspection limits. |
| dependency | [Exact parity carry and all-Renyi boundary](Yin_C_G0530_v1.md#statement) | Complete original iid mask/parity output, dependent carry, actual endpoint identity and at-most2d log2 comparison for all Renyi orders; not independent summand selection. |
| dependency | [Finite convexity and tensorization](Yin_C_G0508_v2.md#cyclic-noise-tensor-contraction) | Only fully proved finite-probability strong-convexity inequality and correct-direction Minkowski tensorization; no stationary theorem or substitute process. |
| support | [Independent thinning distinction](Yin_C_G0282_v1.md#statement) | Existing theorem needs external independent selection of summands; it is not applied to the dependent original mask. |
| review | [Actual current whole SELF](../audits/reviews/Yin_R_G0735_v1.md#current-g223-whole-self-finding) | Entire exact current statement and complete argument with every explicit domain, input interface, full mathematical proof, source/native/control scope and limitation inspected at this current C; actual SELF, not a retrospective old review or isolated replacement. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:48 |
| status | proved |
| reason | Adopt the entire exact current Statement and complete retained Argument after the actual independently reviewed whole finding in R793. All eight batch initial conclusions preceded every old target finding and Assessment. Necessary inputs are resolved at their exact fixed scopes, original mathematical and evidence/source/failure/negative history is retained, and no unresolved issue affects this restricted result. This is a new actual current adoption, with no old relationship or binding backfill and no Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Any actual algebraic unit/original parity carry, all span-zero/nonzero full reconstruction and exactly charged finite observations, arbitrary jointly dependent finite Y with independent-coordinate Shannon disclosure, fair-cube average collision and exceptional outcomes, every causal terminal/p0/Renyi case and exact positive/torsion/radical controls, with all uniformity/selection limits. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/equations(1)--(21), complete two-sided finite reconstruction and infinite-cylinder argument, entropy concavity, exact Walsh projection/noise identity/local tensor proof, Holder exponents, all2d charges/limit directions, causal independent basis/triangular coefficients and actual controls, plus original resolved ODo07 attribution correction and inspection limits. |
| dependency | [Exact parity carry and all-Renyi boundary](Yin_C_G0530_v1.md#statement) | Complete original iid mask/parity output, dependent carry, actual endpoint identity and at-most2d log2 comparison for all Renyi orders; not independent summand selection. |
| dependency | [Finite convexity and tensorization](Yin_C_G0508_v2.md#cyclic-noise-tensor-contraction) | Only fully proved finite-probability strong-convexity inequality and correct-direction Minkowski tensorization; no stationary theorem or substitute process. |
| support | [Independent thinning distinction](Yin_C_G0282_v1.md#statement) | Existing theorem needs external independent selection of summands; it is not applied to the dependent original mask. |
| review | [Actual current whole independent finding](../audits/reviews/Yin_R_G0793_v1.md#conditional-mask-current-independent) | Entire exact current Statement and complete Argument, with every actual domain, fixed mathematical interface, complete proof, finite/source/failure/control boundary and cost; true isolated initial mathematical conclusion 2026-10-22T21:39, followed by old-scope comparison, without rewriting historical relations or resuming research. |

## Complete argument

<a id="argument"></a>

### Reuse, contribution and changed mechanism

[L219](Yin_C_G0530_v1.md#parity-carry-fixed-scope) supplies the exact original-iid parity output, the dependent integer carry and the endpoint identity with at most2d boundary bits.
Its actual torsion example shows a future mask can reveal the selected input.
The present round first resolves the coordinator's conjectural generalization: every nonzero binary finite filter has a finite reconstruction boundary, and the relevant number is its span, not merely a qualitative finite-memory condition.
That conjecture was proposed by the coordinating AI; the derivations, partial-observation results and controls below were developed by the assigned structural_research AI for Yin.

The next mechanism observes only an independently chosen part of the iid mask vector.
It is an observation experiment on the unchanged original process, not substitution of an independent mask for its dependent selection mask.
A relative Shannon information bound and a collision bound retain a positive fraction of the actual endpoint information with constants independent of degree.
They do not create an unknown growth floor.
A separate exact causal-prefix calculation shows why genuine independent remaining bits at a terminal window still give only a finite-degree information quantity.

The exact [L90 thinning theorem](Yin_C_G0282_v1.md#sharp-thinning-laplace-bound) was reread; its independent selection of summands is not assumed here.
A local screen of the retained ledgers for erasure observations and random-subset disclosure found no matching statement.
The elementary entropy set-function and two-point norm arguments below are not claimed historically new.
The norm proof reuses the fully proved strong-convexity inequality and mixed-norm tensorization in [L211](Yin_C_G0508_v2.md#cyclic-noise-tensor-contraction), at their stated finite-probability scope; no new external theorem or source acquisition is a premise.
This is a bounded local reuse screen, not a literature-wide novelty search.
No computation is needed.

Use L219's original setup throughout: alpha is an algebraic unit with actual minimal polynomial P(t)=sum_(i=0)^d p_i t^i, p_d=1, p_0 in{-1,1}; xi_j, j in Z, are iid fair bits.
Put

    b_j=sum_(i=1)^d (p_i mod2) xi_(j-i) mod2,
    M_j=(1-p_0)/2+p_0 b_j,
    sigma_j=xi_j XOR b_j,
    C_j=floor[(sum_i p_i xi_(j-i))/2],
    S_n=sum_(j=0)^(n-1) sigma_j alpha^j,
    T_n=sum_(j=0)^(n-1) C_j alpha^j.

The complement in M is an invertible fixed relabeling of b, so observing either gives exactly the same information.
The mask process M is iid fair, but is dependent on xi and the endpoints.
Logarithms are natural.
Entropies and collision sums below are for finite actual laws.
Conditional entropy means ordinary Shannon entropy unless an individual conditional law or an averaged collision probability is explicitly specified.

<a id="full-mask-finite-reconstruction"></a>
### 1. Exact reconstruction and the full-mask obstruction

Let ell=min{i>=1:p_i is odd} and w=d-ell.
Both endpoints of the delayed binary filter are nonzero.
Set

    Z_k=b_(k+ell)=xi_k+sum_(r=1)^w q_r xi_(k-r) mod2,
    q_r=p_(ell+r) mod2.                                (1)

If w=0 this is simply Z_k=xi_k.
Otherwise q_w=1.
This section in fact applies to any nonzero finite binary filter after its first nonzero lag is shifted to zero.

For an integer a and N>=1, knowledge of the w boundary bits xi_(a-w)...,xi_(a-1) and outputs Z_a,...,Z_(a+N-1) reconstructs inputs xi_a,...,xi_(a+N-1) successively using the leading coefficient1 in(1).
The map from those w+N input bits to (boundary, output) is a bijection over F_2.
Thus the N outputs are iid fair and independent of the uniform boundary.
A one-sided infinite output sequence plus that boundary reconstructs the full one-sided input sequence.
Since q_w=1, the recurrence also runs backward: knowing a full output sequence and any w consecutive input bits determines all inputs in both directions.
Each complete output sequence therefore has exactly2^w bi-infinite input preimages; for w=0 it has one.

The boundary is independent even of the FULL bi-infinite output sequence.
To verify this without an infinite entropy calculation, consider a finite linear combination of output coordinates.
Its coefficient Laurent polynomial is the product of a nonzero polynomial for the selected shifts and Q(z)=1+sum_(r=1)^w q_r z^(-r).
Every nonzero such product has support span at least w, since extreme coefficients cannot cancel.
A nonzero combination of w consecutive boundary coordinates has span at most w-1.
They cannot agree.
Thus any finite collection of output rows together with those boundary coordinates has full rank.
Their joint law is uniform; finite cylinder events prove independence from the full output sigma-field.
Conditioned on that sigma-field, the2^w reconstructions have equal probabilities.
In particular, for every finite endpoint function of the input,

    H(endpoint | full mask)<=w log2.                   (2)

This asserts finite global ambiguity, not finite unconditional entropy of an infinite sequence.

A finite observation vector already suffices for the endpoint T_n.
Choose

    V_n=(Z_k: -d<=k<=n-1),  length n+d.                 (3)

Given V_n and the w input bits immediately preceding -d, recurrence(1) determines every input xi_(-d)...,xi_(n-1) used by T_n.
Therefore

    H(T_n|V_n)<=w log2,
    E Col(law(T_n|V_n))>=2^(-w).                       (4)

Here Col(mu)=sum_x mu(x)^2.
For the collision bound, each conditional law is supported on at most2^w possibilities.
The masks in(3) have original chronological indices -d+ell,...,n-1+ell; the latest observation includes an ell-step look-ahead, and the number of observed bits is n+d.
These costs are explicit.
Full observation kills the conditional endpoint entropy rate at every fixed input, including positive-growth inputs, not only the previous torsion control.

<a id="partial-mask-shannon-information-retention"></a>
### 2. Independently sampled partial observations preserve relative Shannon information

Let V=(V_1,...,V_N) be any finite vector of independent coordinates, and let Y be any finite-valued variable jointly distributed with V.
There is no independence assumption between Y and V.
Independently of this entire law, choose A subset{1,...,N} by including each index with probability theta in[0,1].
The observation is (A,V_A).
Write

    F(theta)=H(Y|A,V_A)=E_A H(Y|V_A).

Then

    F(theta)>=(1-theta)H(Y)+theta H(Y|V),
    I(Y;A,V_A)<=theta I(Y;V)<=theta H(Y).               (5)

This bound charges the information actually revealed about Y, not the total number of exposed coordinates times log2.

Here is a complete entropy proof.
For i notin B, adding that observation decreases conditional entropy by I(Y;V_i|V_B).
If i,j are distinct and outside B, the chain rule and independence of V give

    I(Y;V_i|V_B,V_j)-I(Y;V_i|V_B)
       =I(V_i;V_j|Y,V_B)-I(V_i;V_j|V_B)
       =I(V_i;V_j|Y,V_B)>=0.                           (6)

For theta in(0,1), differentiating the finite subset average yields F'(theta)=-sum_i E_B I(Y;V_i|V_B), where B is a theta-subset of the other N-1 coordinates.
Couple these subsets by independent uniform thresholds.
Equation(6) makes each summand nondecreasing as theta increases, so F' is nonincreasing and F is concave.
Its endpoint values are F(0)=H(Y), F(1)=H(Y|V); the chord inequality gives(5).
The selector A is independent, so I(Y;A)=0, and the second formula is the equivalent chain rule.
Continuity includes theta=0,1.
No finite-dimensional or coefficient constant occurs.

Applying this to the actual iid mask vector V_n in(3) and Y=T_n gives

    H(T_n|A,(V_n)_A)>=(1-theta)H(T_n)
       >=(1-theta)[H(S_n)-2d log2].                    (7)

The final step is L219's exact finite-boundary comparison.
For every fixed actual input,

    liminf_(n->infinity) H(T_n|A,(V_n)_A)/n
       >=(1-theta)h_1(alpha).                          (8)

The expression is the average conditional Shannon entropy with fresh independent selectors for each n; no limit existence beyond this lower limit is asserted.
For changing inputs the full loss2d log2/n remains.
In contrast, replacing(5) by the generic bound I(Y;observation)<=theta(n+d)log2 would consume near-one information at a fixed positive observation density.
Equation(5) avoids that loss, but is still proportional to the actual unknown endpoint entropy.

<a id="partial-mask-collision-information-retention"></a>
### 3. A dimension-free bound for the average conditional collision law

Now suppose V consists of N iid fair bits, still allowing arbitrary joint dependence of Y on V.
With the same independent selector, set

    K_Y(theta)=E_(A,V_A) Col(law(Y|A,V_A)),
    kappa(theta)=(1-theta)/(1+theta).

For every theta in[0,1],

    Col(Y)<=K_Y(theta)<=Col(Y)^kappa(theta).             (9)

Thus an independent random partial disclosure retains a positive fraction of the collision information whenever theta<1.
This is an average over the selector AND its observed actual values, not a bound for every realized observation.

Classical attribution added after the first author freeze: the Boolean norm inequality used below is the hypercontractivity theorem, in the specialization p=1+theta, q=2 and rho=sqrt(theta).
The exact general statement was checked in Ryan O'Donnell's [ODo07, Theorem1.1, printed/PDF p.1](../literature/pdf/ODo07.pdf), *Lecture16: The Hypercontractivity Theorem*, CMU18-859S,8March2007; its Fourier multiplier convention is displayed on p.4.
The [compact ODo07 source record](../audits/literature/ODo07/readme.md#boolean-hypercontractivity-attribution) retains the exact statement, normalization, inspected passages and attribution-only role.
O'Donnell is the lecturer and scribe of this primary teaching exposition of the classical theorem.
The original author source screen did not establish that explicit attribution; this paragraph closes that source-identification boundary after the reviewer recognized it.
The local two-point proof through L211 and its tensorization are retained as a self-contained verification of precisely this specialization, not a new hypercontractivity theorem.
ODo07 supplies classical attribution and corroboration, rather than an additional unproved premise; the observation-function collision identity, actual endpoint application and finite boundary costs are local deductions.
The complete source proof and historical priority are not claimed audited here.

To prove it, for each y define f_y(v)=Pr(Y=y|V=v), so0<=f_y<=1 and E f_y=Pr(Y=y).
On the uniform binary cube, write its orthogonal expansion in products chi_B(v)=product_(i in B)(-1)^(v_i).
Orthogonality follows by averaging each independent fair bit.
The conditional expectation onto V_A retains exactly the coefficients with B subset A.
Hence

    K_Y(theta)=sum_y sum_B theta^|B| (fhat_y(B))^2
              =sum_y ||T_(sqrt theta) f_y||_2^2,         (10)

where the positive product operator T_gamma multiplies coefficient chi_B by gamma^|B|.
Equivalently each coordinate is retained with weight gamma and independently resampled from a fair bit with weight1-gamma.
This auxiliary averaging operator acts on observation functions; it does not change the original digit process.

For0<theta<1, put p=1+theta.
On a two-point fair space, write a nonnegative f=m+h with mean m; the centered h takes opposite equal-magnitude values, so ||h||_p=||h||_2.
The fully proved finite-space convexity inequality L211(6) gives

    ||f||_p^2>=m^2+(p-1)||h||_2^2
              =||T_(sqrt theta) f||_2^2.

The mixed-norm Minkowski argument written in L211 tensorizes this contraction without dependence on N: applying the two-point inequality in one coordinate, using ||g||_(L^2 L^p)<=||g||_(L^p L^2) for p<=2, and iterating proves ||T_(sqrt theta)f||_2<=||f||_p.
All operators preserve nonnegativity, as required.
Therefore, with a=2/(1+theta) in(1,2), (10) gives

    K_Y(theta)<=sum_y (E f_y^p)^(2/p)
                <=sum_y Pr(Y=y)^a
                <=[sum_y Pr(Y=y)^2]^(a-1).             (11)

The middle inequality uses f_y^p<=f_y.
The last is Holder applied to p_y^a=p_y^(2-a)(p_y^2)^(a-1), with sum p_y=1.
Since a-1=kappa, this proves the upper bound.
Jensen on each conditional probability gives the lower bound in(9).
At theta=0 there is no observation and equality holds; at theta=1 the upper bound1 is immediate.
This proof uses the accepted L211 elementary convexity/tensorization argument, not a new uninspected hypercontractivity theorem.

For the actual carry endpoint and mask vector V_n, let p_n=Col(S_n) be the unchanged original fair-binary collision probability and K_n(theta)=K_(T_n)(theta).
L219 yields

    2^(-2d) p_n <= K_n(theta)
       <=2^(2d kappa) p_n^kappa.                       (12)

Consequently, for fixed alpha and fixed theta<1,

    kappa h_2(alpha)
       <=liminf -log K_n(theta)/n
       <=limsup -log K_n(theta)/n<=h_2(alpha).           (13)

Every finite-time degree charge is explicit in(12); no convergence time uniform in the actual input is inferred.
This is genuine surviving conditional endpoint collision information, proportional to the original rate.
In particular it is different from the unconditional local carry-symbol entropy in L219.

There is also a fully charged high-probability consequence.
For0<delta<kappa, Markov's inequality and(9) give

    Pr_(A,V_A){Col(law(T_n|A,V_A))
          >exp[-(kappa-delta) H_2(T_n)]}
       <=exp[-delta H_2(T_n)].                         (14)

When H_2(T_n)=0 the bound is merely trivial.
Otherwise most observation outcomes retain a fixed fraction of the collision information, with the exact exceptional probability displayed.
One may insert H_2(T_n)>=H_2(S_n)-2d log2 only when retaining the resulting finite-time cost.
The formula assumes an independent selector; a selector chosen from the observed mask or endpoint need not satisfy any bound proved here.


<a id="causal-mask-terminal-window"></a>
### 4. Exact causal-prefix conditioning: safe thinning with a finite horizon

The random disclosure theorem is not an assertion that the entire original mask is safe to condition on.
A direct causal calculation shows precisely what remains at the terminal time.
Let n>=1, L=min(n,ell), t_0=n-L, and observe

    O_n=(xi_(-d)...,xi_(-1), M_0,...,M_(n-1)).          (15)

There is no mask look-ahead beyond the last carry time.
Recurrence(1) reconstructs xi_0,...,xi_(t_0-1) from these observations.
Conversely every coordinate of O_n depends only on the given past and those reconstructed prefix bits: the largest input index of M_(n-1) is n-1-ell<t_0.
Consequently, conditional on every possible O_n value, the terminal L bits xi_(t_0)...,xi_(n-1) are still independent fair bits.
This is an actual valid independent remainder, proved from the complete observation sigma-field rather than the one-time predictability of each mask.

The parity bits before t_0 are known, and each terminal parity is xi_u XOR b_u with b_u observed.
Since L<=ell<=d, the consecutive powers alpha^(t_0)...,alpha^(n-1) are linearly independent over Q.
Thus each conditional law of S_n is uniform on exactly2^L distinct values.
For every Renyi order a in[0,infinity], including its endpoint conventions,

    H_a(law(S_n|O_n=o))=L log2.                        (16)

The carry endpoint has the exact conditional form

    T_n=constant(o)+sum_(u=t_0)^(n-1) xi_u v_u(o),
    v_u(o)=alpha^u [p_0 M_u+
               sum_(i=1)^(n-1-u) (p_i/2) alpha^i].     (17)

Indeed sigma_j=b_j+(1-2b_j)xi_j, and inserting this in2C_j=Y_j-sigma_j gives the coefficient of each free input bit.
Every positive index i in(17) is less than ell, so p_i is even and the coefficients are actual integers.
The own-position coefficient is (p_0-1)/2+b_u=p_0 M_u, for both signs of p_0.

Let G(o)=sum_(u=t_0)^(n-1) M_u.
Relative to the independent basis of L consecutive powers, the vectors v_u at positions with M_u=1 have a triangular square submatrix with diagonal p_0.
They are linearly independent.
After conditioning further on the other terminal bits, those G bits therefore give2^G distinct equiprobable endpoints.
Mixtures over the other bits cannot increase the maximal atom above2^(-G).
The entire conditional law has at most2^L points, so

    G(o)log2<=H_a(law(T_n|O_n=o))<=L log2,
    2^(-L)<=Col(law(T_n|O_n=o))<=2^(-G(o)).             (18)

The original mask coordinates are iid fair, hence G has the Binomial(L,1/2) law when the observation is sampled.
It follows that

    E H_a(law(T_n|O_n)) >=(L/2)log2,
    2^(-L)<=E Col(law(T_n|O_n))<=(3/4)^L.               (19)

The first expression is the average of the individual conditional Renyi entropies, not an unstated convention for conditional Renyi entropy.
For Shannon entropy it is the usual conditional entropy.
The collision expression is averaged separately, as written.
If p_i=0 for1<=i<ell, only the selected coefficients p_0 M_u alpha^u remain in(17), and equality holds in the upper collision bound.
In particular this equality always holds when ell=1.

This is a rigorous place where conditioning does leave independent usable bits, and some of their information survives the actual algebraic endpoint.
But L<=d: it is a terminal-window result, not time-linear growth.
Even without exposing the initial d bits, the complete causal mask prefix leaves at most d+L input bits undetermined, giving

    H(T_n|M_0,...,M_(n-1))<=(d+L)log2.                  (20)

The corresponding conditional support is at most2^(d+L), so the averaged conditional collision probability is at least2^(-(d+L)).
Thus causal full-prefix observation also has zero conditional endpoint entropy rate at every fixed alpha.
Repeating(19) on overlapping windows would reveal or charge input information again; it cannot be multiplied as independent chronological gains.
The actual total chronological length, observed coordinate count and finite degree remain visible in(15)--(20).

<a id="actual-full-and-partial-mask-controls"></a>
### 5. Actual positive and zero-growth controls

For the actual primitive2d-th root of unity with d a power of two, P=t^d+1, ell=d and w=0.
Formula(1) says Z_k=xi_k: the full mask determines every input exactly.
The carry is C_j=xi_j xi_(j-d), as in L219.
For the causal experiment(15), L=min(n,d) and the upper averaged collision bound in(19) is exactly(3/4)^L.
Thus the safe terminal independent bits are real, but their total horizon is at most d.
Because C_j is binary and alpha has only2d distinct powers, every unconditional carry endpoint has at most(n+1)^(2d) possible values.
Every conditional law is supported on that same set, so for any partial observation experiment

    K_n(theta)>=(n+1)^(-2d).

Its collision exponent is zero, including under independent random partial disclosure.
The degree-d free initial window remains, and no limit uniform in d is inferred.

For alpha=phi, P=t^2-t-1, ell=1 and w=1.
The full mask filter is Z_k=xi_k XOR xi_(k-1).
A complete mask therefore fixes the whole input up to one uniform global-complement bit.
In particular H(T_n|full mask)<=log2 for every n, even though the original binary endpoint has positive collision rate.
This makes the full-disclosure obstruction an actual positive-growth phenomenon rather than a torsion artifact.
Causally, (19) is exact with L=1: E Col(law(T_n|O_n))=3/4 for every n>=1.

Independently revealing a fixed fraction theta<1 has a different asymptotic outcome.
To see positivity directly from the original binary law, condition on the odd-position bits in S_n.
Its even-position bits have weights in powers of phi^2>2, so distinct binary choices give distinct sums: in a nonzero difference the largest weight exceeds the sum of all smaller weights.
The maximum endpoint atom is at most2^(-ceil(n/2)), and hence p_n<=2^(-ceil(n/2)).
Formula(12), with d=2, gives

    K_n(theta)<=2^(4 kappa) 2^(-kappa ceil(n/2)),
    liminf -log K_n(theta)/n>=kappa log2/2>0.           (21)

No Mahler lower bound was assumed to obtain this actual positive control.
Full disclosure loses its conditional endpoint rate, whereas independent partial disclosure retains a positive rate.
The high-degree actual radical controls P=t^(2r)-t^r-1 from L219/L215 have ell=r and w=r; (4), (12) and (19) retain these degree costs.
Their fixed M=phi is not a near-one reciprocal family.
These examples discriminate conditioning mechanisms; none refutes a suitably restricted near-one growth conjecture.

<a id="partial-mask-next-endpoint-survival-gate"></a>
### 6. What survives, and the remaining arithmetic question

The full-mask reconstruction conjecture is verified with exact span w=d-ell.
It explains why observing every mask coordinate, including only a long causal prefix with a bounded initial uncertainty, destroys conditional endpoint rates for all fixed actual inputs.
A predictable iid process cannot be treated as an independent external selection mechanism.

There is nevertheless a useful partial-observation mechanism.
Independently sampling which actual mask coordinates to disclose preserves a dimension-free fraction of the actual Shannon and collision endpoint information, with no theta*n*log2 penalty.
The information is measured after conditioning on the entire selected observation, not by adding local carry-symbol entropies.
Formula(14) also controls the exceptional observation outcomes.
The original binary word weights have not changed.
The finite representation charge remains2d log2, and the observation window contains n+d mask coordinates with the explicit ell look-ahead.
Formula(19) separately identifies a valid causal independent remainder and shows exactly why its safe rank contribution is only O(d).

A next arithmetic test can therefore work on fibers of an independently partially observed actual mask, where information survival has a rigorous rate transfer.
The missing estimate is a degree-uniform, time-linear lower bound on the actual conditional endpoint collision information for nontorsion near-one inputs, derived from their algebraic structure.
It must account for correlations between unobserved coordinates and the carry endpoint; neither the random selector nor the iid mask law supplies independent summands.
A candidate could seek a controlled integral-recurrence obstruction to large conditional endpoint fibers, or compare disclosures on separated time blocks while charging all overlap information.
These are research questions, not proved criteria.

This target remains quantitatively as hard as a uniform original collision floor unless additional arithmetic enters: (12)--(13) compare the two actual rates, and do not furnish a new positive lower constant.
In particular no unknown Mahler floor, all-degree uniform convergence time, endpoint injectivity beyond the proved terminal window, or inequality for adaptive or every deterministic mask is silently imported.

### Author self-check and contribution boundary

The coordinating AI supplied the broad continuation question and the conjectural finite-boundary reconstruction idea.
The assigned structural_research AI developed and checked the full reconstruction proof, its exact span and finite observation choices, the partial-disclosure Shannon inequality, the collision-information deduction from the retained L211 inequality, the high-probability consequence, the causal terminal-window formula and its actual controls.
L219 supplies the exact original-law representation, all-Renyi boundary cost and preexisting control input identities; L211 supplies its already proved convexity and tensorization interface.
This author verification does not constitute a noncontributor review of those new deductions.

The [complete original author checking/evidence account](../audits/reviews/Yin_R_G0735_v1.md#original-g223-author-self-finding) retains its actual original input, recorded precision and scope, separately from the current whole SELF finding.


Author freeze: 2026-10-09T21:29.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0793_v1.md#conditional-mask-complete-independent-review), with its original inspected scope and relationship.
