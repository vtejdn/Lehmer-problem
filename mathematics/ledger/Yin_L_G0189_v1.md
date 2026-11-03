---
author: Yin
---

# Linear controlled return length for the original Lehmer input

Date: 2026-10-10.
Fixed retention of the complete coordinating-author D56 argument and resultant_research's full noncontributor review.
The original proof and finding below are preserved in full, with only heading depth and navigation relocated.

<a id="linear-return-length-fixed-scope"></a>
## Adopted scope

For every fixed Salem beta in(1,phi), the strong L180 control theorem implies an original-digit continuation from every narrow actual-order state into a finite compact residue of length at most A_beta rho+B_beta.
The finite control family can be chosen with endpoints bounded away from zero, making all later real normalization prefixes uniformly bounded and giving constant radial decrease.
All constants depend on the algebraic input.

If every actual compact-residue state has a zero continuation, the same linear bound holds for exact co-return.
The already fixed L170 theorem supplies that premise for the original degree-ten Lehmer unit.
Its narrow-domain return length therefore has matching linear order, since every zero-ending word has length at least rho/sqrt(s), and its narrow returning domain contains states with unbounded rho.
This improves the earlier coarser fixed-input chosen-word estimate without modifying historical proofs or computations.

Only a selected path probability of at least exp(-C_beta rho-D_beta) follows.
Universal compact termination, original-law average/tail control, input-uniform constants and the unrestricted Lehmer gap remain open.
Historical pending-review wording below preserves chronology; this adoption and the appended full finding determine the current mathematical scope.

<a id="retained-linear-return-length-proof"></a>
## Linear chosen-word length from unbounded small-Salem control

Date: 2026-10-10.
New responsible argument by the coordinating AI for Yin.
The fixed L180 arbitrary-negative directional control is stronger than mere PC.
This round asks whether that extra strength removes the repeated long zero-prefix overhead in the earlier chosen-path estimate.
The result below is a fixed-input deterministic length bound, with an explicitly conditional termination consequence; it is not an original-law average contraction or a uniform Mahler gap.

### Inputs and conventions

Fix a Salem beta with 1<beta<phi, degree d=2s+2, s>=1, O=Z[beta], B=1/(beta-1) and S=beta/(beta-1).
Select one unit-circle conjugate zeta_j from each reciprocal pair.
Use the unweighted joint neutral norm rho(x)=(sum_j |x_j|^2)^(1/2), and

    N={x in O: |x_+|<=1, |x_-|<=S}.

The original word map is T_w(x)=beta^n x+P_w(beta), with digits in{-1,0,1}.
Its neutral displacement is c_w=(sum_(i=1)^n eta_i zeta_j^(-i))_j.
If A is diagonal multiplication by the selected neutral conjugates, then z_(T_w x)=A^n(z_x+c_w).
Appending zero digits rotates the neutral endpoint further and leaves c_w unchanged.

The fixed [L180 theorem](Yin_L_G0180_v1.md#small-salem-global-pointwise-control) says that for every real x in[1/2,1], every unit real neutral direction u, and every real C, there is an original finite word with |T_w(x)|<1 and u.c_w<C.
Its complete independent reviews are retained there.
The [L176 finite-cover interface](Yin_L_G0176_v1.md#joint-neutral-pointwise-control) and [L183 finite-certificate criterion](Yin_L_G0183_v1.md#compact-termination-certificate-interface) are reused at their stated scopes.
No source theorem or program is newly adopted.

<a id="nonzero-endpoint-control-cover"></a>
### 1. A finite directional cover whose endpoints stay away from zero

For each pair (x,u) in [1/2,1] times the unit neutral sphere, a word exists with

    0<|T_w(x)|<1,    u.c_w<0.                       (1)

Indeed if x is not in O, no original word can end at zero: that would express x as -beta^(-n)P_w(beta), an element of O since beta is a unit.
The L180 negative word then already satisfies (1).
If x is in O, all words ending at zero have exactly the same neutral displacement c_w=-z_x, by applying the embeddings to their exact zero equation.
Choose the threshold C smaller than both zero and -u.z_x.
L180 supplies a word whose displacement cannot equal that of any zero-ending word and whose endpoint is still strictly narrow.
This proves (1) for every real x, without requiring the map x to z_x to extend continuously outside O.

For each successful pair, strict negativity and the two strict endpoint inequalities persist on an open product neighborhood of (x,u).
Shrink the neighborhood so that it has positive margins from all three boundaries.
Compactness of the interval times the unit sphere gives finitely many such neighborhoods with assigned words.
Consequently there are constants

    a>0,    0<epsilon<1/2,    C_*>0,    L>=1

and a finite word list such that for every (x,u) one of its assigned words satisfies

    u.c_w<=-a,
    epsilon<=|T_w(x)|<=1-epsilon,
    ||c_w||<=C_*,    length(w)<=L.                  (2)

The inequalities are required on the assigned neighborhoods, not on the full annulus for each individual word.
The displacement is nonzero for every chosen word by its negative directional cost.
A finite closed subdivision can be used if an interval-table presentation is wanted; the proof needs only the finite cover with its margins.

Append zero digits when the endpoint magnitude is less than one half, stopping at the first magnitude at least one half.
The number of appended digits is bounded by a fixed Z depending on epsilon and beta; for example

    Z=1+max{0,ceil(log(1/(2epsilon))/log(beta))}

is a safe bound.
The first crossing has magnitude less than beta/2<1.
Therefore the endpoint is again in the signed annulus, all original digits are unchanged, and both the displacement bound and directional inequality in (2) persist.
The resulting block length is at most L+Z.
There are finitely many possible zero suffix lengths.
Negative starting real values are handled by negating the state and the word; the radial directional inequality transfers with the same constants.

This strengthening uses arbitrary negative directional cost specifically to avoid exact zero endpoints.
An arbitrary PC certificate alone need not provide the uniformly nonzero endpoint margin by the same argument.

<a id="linear-neutral-radius-reduction-length"></a>
### 2. Constant radial decrease and a linear compact-reduction length

Choose

    R>=max{1,a,C_*^2/a}.

At an annular state with rho>=R, use (2) in the unit radial direction u=z_x/rho, with the sign convention just described.
After the controlled block and its bounded zero suffix, orthogonality gives

    rho_new^2<=rho^2-2a rho+C_*^2
              <=rho^2-a rho
              <=(rho-a/2)^2.

Since rho>=a, the last comparison has a nonnegative square root.
Hence

    rho_new<=rho-a/2.                              (3)

Each such block keeps the real endpoint in the annulus.
Every intermediate stable coordinate stays within S: beta^(-1)S+1=S.
Every intermediate real coordinate stays strictly inside(-B,B), by backward estimation from the final narrow endpoint.
Thus these are actual legal words in the original strip, not unconstrained neutral moves.

After at most 1+2rho_0/a blocks the process reaches rho<R, with real magnitude between one half and one and stable magnitude at most S.
The block count is a safe overestimate when the state is already compact.
In particular every initially annular state has a continuation into K_R=N intersect{rho<R} of length at most

    (L+Z)(1+2rho_0/a).                             (4)

The key improvement is the linear decrease of rho in (3), together with a bounded zero suffix.
It is not obtained merely by replacing a squared-radius count with a radius count while retaining uncontrolled normalization steps.

For completeness, handle an arbitrary nonzero x in N whose real magnitude is below one half.
Integer norm and the arithmetic-geometric mean inequality give

    1<=|Norm(x)|
       =|x_+ x_-| product_j |x_j|^2
       <=|x_+| S (rho(x)^2/s)^s.

Therefore

    |x_+|>=s^s/[S rho(x)^(2s)].                     (5)

A zero prefix takes this real coordinate into the annulus in at most

    1+max{0,log(S/(2s^s))/log(beta)
                 +2s log(rho(x))/log(beta)}

digits, with the obvious integer rounding upward if needed.
Equivalently it is bounded by A_0+A_1 log(1+rho(x)) for constants depending only on beta.
Neutral radius is unchanged and the stable bound remains valid.
Real zero means x=0 by injectivity of the embedding, and needs no prefix.
Combining (4)--(5), and absorbing log(1+rho)<=rho, proves fixed finite constants A_beta,B_beta such that

    every x in N has an original legal continuation into K_R
    of length at most A_beta rho(x)+B_beta.         (6)

If the initial state already belongs to K_R it may instead use the empty continuation.
The complete embedding lattice makes K_R finite.
No zero continuation for its members has been inferred from compactness.

<a id="conditional-linear-return-length-and-cost"></a>
### 3. Conditional exact return length and the probability boundary

If every actual member of K_R has some finite original continuation to zero, fix one for each member and take the finite maximum of their lengths.
Concatenating with (6) gives constants A'_beta,B'_beta such that every x in N has an exact zero continuation satisfying

    length(w_x)<=A'_beta rho(x)+B'_beta.            (7)

Conversely this universal assertion plainly implies compact termination.
The fixed [L170 original Lehmer input](Yin_L_G0170_v1.md#lehmer-infinite-core-theorem) satisfies beta<phi and already has complete narrow-domain co-return, so (7) applies unconditionally to that specific degree-ten input.
It improves its earlier coarser O(rho^2 log(1+rho)) chosen-word estimate without changing the fixed proof or its retained computations.
The quartic L169 input lies above phi and is not included by the present use of L180; no extension to it is claimed.

The linear order is optimal as a deterministic dependence on neutral radius whenever returning states have unbounded radius.
Along a word of length n, each digit changes the neutral norm by at most sqrt(s) after rotation.
More directly a zero endpoint gives

    rho(x)=||c_w||<=n sqrt(s),
    n>=rho(x)/sqrt(s).                             (8)

This is an individual-word lower bound, not a uniform lower bound in the varying algebraic input.
The actual Lehmer return core has unbounded neutral radius by L170, so its chosen return length has matching linear order up to input-dependent constants.

Under the unchanged independent original digit law with probabilities(1/4,1/2,1/4), the selected word in (7) has probability at least

    4^(-length(w_x))>=exp[-log(4)(A'_beta rho(x)+B'_beta)].

This is the probability of one explicitly selected existence path.
It supplies a lower bound on eventual co-return from that state when the termination premise holds.
It does not give an original-law expectation, a tail estimate for all paths, averaged negative drift, input-uniform constants or a Mahler gap.
Before compact termination is known, (6) gives only the corresponding lower bound for reaching the compact residue.
The norm drift under the unrestricted original law retains the positive quadratic drift recorded in L176.

### 4. Check and continuation scope

The coordinating author checked the exact-zero endpoint classification using the unit hypothesis, the pointwise-to-uniform finite-cover step, bounded zero suffixes and the unchanged cocycle, the sign transfer, radial decrease, integer-norm prefix bound, and the actual Lehmer application.
The preceding formulas are elementary deductions from fixed reviewed interfaces and require no numerical experiment or new J.
The constants are finite and input-dependent, not supplied as numerical values or bounded uniformly over degree.
A separate noncontributor full review is required before fixed adoption.
This draft does not resolve actual compact termination for all small Salem inputs or the unrestricted G0001 contract.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0088_v1.md#complete-separate-noncontributor-review), with its original inspected scope and relationship.




<a id="linear-return-length-retention-bindings"></a>
## Retention and review bindings

The coordinating AI for Yin supplied every new derivation in this round.
The [complete noncontributor review](../audits/reviews/Yin_R_G0088_v1.md#linear-chosen-word-independent-review) by resultant_research covers the entire [retained proof](#retained-linear-return-length-proof), including all exact-zero, compactness, radial, length, domain and probability arguments.
Its prior inspection of reused interfaces is disclosed rather than presented as authorship or a new audit of all foundations.
No numerical experiment, source adoption or J belongs to this proof-only result.

The retaining coordinator relocated the complete proof and review here and retired only D56 after updating its actual links.
Future changes to these conclusions require the corresponding explicit new scope and review.
