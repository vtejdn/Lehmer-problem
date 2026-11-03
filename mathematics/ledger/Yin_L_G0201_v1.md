---
author: Yin
---

# Exact stationary information variational formula and critical-tilt obstruction

Date: 2026-10-10.

<a id="stationary-information-fixed-scope"></a>
## Adopted scope

The coordinating AI for Yin retains its complete actual-kernel proof and resultant_research's separate complete noncontributor review.
That reviewer disclosed its earlier L192 contribution and L198 review.
Classical finite-subgraph pressure, variational and recurrence mechanisms are attributed to the precisely inspected Sar15 author version; the retained argument proves the stated original-digit specialization directly.

For every algebraic unit, including torsion, the collision exponent is the infimum of original-digit relative entropy rates over positive recurrent auxiliary laws supported on the actual return core and containing zero; finite supported laws give the same infimum.
The full excursion relative-entropy defect gives the exact attainment criterion F(R)=1 with finite R F'(R), and uniqueness in that rooted class.
The complete canonical exponential-tilt family is monotone but can retain a strictly positive defect at its critical endpoint.
Actual high-degree cyclotomic inputs realize this failure, while finite Perron approximants still approach the true infimum.

The result supplies an exact interface and a concrete obstruction to choosing just one canonical stationary family.
It does not prove a positive lower information bound for nontorsion near-one inputs or supply an effective approximation rate.
The cyclotomic control has zero Mahler measure and is not a counterexample to the unrestricted Task.
G0001 remains active and unresolved.

The full author proof and complete review follow.
Historical pending-review text preserves chronology; the appended review determines the adopted review scope.
Only heading depth and relative navigation are transformed.

<a id="retained-stationary-information-proof"></a>
## Stationary information and the actual collision exponent

Date: 2026-10-10.
Starting question: Determine the exact relation between stationary original-digit information cost and the actual collision exponent, using full return laws and finite state exhaustion.
Investigate exponential tilts and the possible escape of near-minimizing stationary laws.
Preserve actual probability, infinite-tail and unrestricted-degree boundaries.

The full unrestricted Task remains active and unresolved.

### Reuse, attribution and exact objective

The exact collision radius, supermultiplicative original return probabilities and all-unit domain are fixed in [L173](Yin_L_G0173_v1.md#core-operator-collision-sandwich).
The complete first-return bounds and the unweighted excursion-conditioned law/information identity are fixed in [L198](Yin_L_G0198_v1.md#general-unit-return-moments-fixed-scope), using L154.
Finite Perron normalization is already used in L181/L186.
The new purpose is to identify exactly which stationary information costs recover the actual collision exponent and what can prevent the full canonical tilted family from reaching it.

A bounded local screen found no existing project statement of this exact variational/attainment interface.
The recognized general mechanisms are classical countable-state thermodynamic formalism, finite-subgraph pressure approximation and positive recurrence, not new discoveries.
Sarig's author-hosted survey, Thermodynamic formalism for countable Markov shifts (published2015), was acquired as Sar15.
Its Theorem4.7, Definition4.8 and Theorems4.9,5.3 give those general interfaces at PDF/printed pp.14-18.
The actual graph below is mixing because every state communicates through0 and0 has a self-loop; its edge potential log K has two finite values and depends on two consecutive states, hence has summable variations.
Weighted closed-path pressure is log r=-h_2.
These are attribution and checked correspondence, not an adopted uninspected proof of the formulas below.
The complete elementary actual-kernel argument is retained to expose the excursion law, finite-mean and degree boundaries.
No historical novelty claim is made.
[Scoped source reading](../audits/literature/Sar15/readme.md) records the retained author version, exact inspection and the excluded p.18 pressure/eigenvalue sentence.
The correct relation is eigenvalue=exp(pressure), as source Theorem4.9 also states.
Source proofs are not re-audited here.

<a id="actual-stationary-information-variational-interface"></a>
### 1. Actual core, critical return weight and admissible stationary laws

Let alpha be any algebraic unit, including torsion, O=Z[alpha], and D its actual original return core.
The chronological update is x -> alpha*x+eta with eta in{-1,0,1} and original probabilities p_0=1/2, p_1=p_(-1)=1/4.
Let K be the unchanged kernel killed outside D, p_n=K^n(0,0), p_0=1, and f_n the complete first-positive-return probability.
Write

    U(z)=sum_(n>=0)p_n z^n,    F(z)=sum_(n>=1)f_n z^n,
    r=lim_n p_n^(1/n)=sup_n p_n^(1/n),
    h=-log r=h_2(alpha),       R=1/r=exp(h).

Supermultiplicativity and the always available zero loop give1/2<=r<=1, hence1<=R<=2.
For0<z<R, complete renewal gives U(z)=1/(1-F(z)), so F(z)<1.
Monotone passage to R gives

    0<F_R:=F(R)<=1.                                      (1)

F'(R) denotes the one-sided nonnegative series and may be infinite.
No critical recurrence is inferred from(1).

An admissible auxiliary law Q is an irreducible positive recurrent Markov chain on a subset S of D containing0, using only the original allowed edges.
Its stationary probability is pi, its first-return excursion law from0 is q(w), and its finite mean return time is mu.
Here w ranges over all complete original first-return words; q is zero on words not used by Q.
Finite subsets S are allowed, including{0}.
The standard positive-recurrent return occupation identity gives mu=1/pi(0), and its proof is the same finite-mean occupation shift used in L198.
Equivalently one may require recurrent Q with finite mean and obtain pi by that construction; uniqueness follows from irreducibility.

If q_x(eta) is the Q digit row, define its original-law relative entropy rate by

    I(Q)=sum_x pi(x) sum_eta q_x(eta)log(q_x(eta)/p_eta).

A missing edge has q=0.
Distinct digits have distinct successors.
Each row has0<=D(q_x||p)<=log4.
Its expected absolute log likelihood is at most log3+log4.
Thus sums of log likelihood over a Q excursion are absolutely integrable: their expectation is at most mu(log3+log4).
Occupation and summation may therefore be interchanged, giving

    E_q log(q(w)/p(w))=mu I(Q).                           (2)

This argument does not assume finite entropy of pi or cancellation of an unbounded log pi coboundary.

Normalize the complete critical original excursion weights to a probability

    nu_R(w)=p(w)R^|w|/F_R.

By(2), finite mu and finite log R, its relative entropy is finite and satisfies

    D(q||nu_R)=mu I(Q)-mu log R+log F_R.

Consequently the exact critical defect formula is

    I(Q)=h+pi(0)[D(q||nu_R)-log F_R]>=h.                  (3)

All complete words, rather than only their lengths, are included.
This is an identity for a changed stationary law, not an assertion that the original walk is stationary or recurrent.

### 2. The infimum is the collision exponent; finite approximation needs no prime theorem

Let A_N be the finite set of all states on all original zero-to-zero words of length at most N, and K_N=K restricted to A_N.
The set contains0, is nested, and every member has a prefix from0 and suffix to0 inside A_N.
Thus K_N is a finite irreducible nonnegative matrix.
Its Perron radius r_N is positive.
Entrywise domination of all powers gives r_N<=r using the fixed L173 actual-core radius.
Conversely, for N>=n all length-n closed words occur in A_N, and concatenating k of them yields

    K_N^(kn)(0,0)>=p_n^k,    r_N>=p_n^(1/n).

Taking the supremum over n proves r_N increases to r.
This is the ordinary finite-word form of the classical finite-subgraph pressure approximation; it applies to torsion as well.
It does not assert finite-prime restricted cores are finite, and needs no ESS input, effective error bound or bounded N.

Choose positive finite right/left Perron vectors v_N,w_N with sum_x w_N(x)v_N(x)=1.
Then

    Q_N(x,y)=K_N(x,y)v_N(y)/(r_N v_N(x)),
    pi_N(x)=w_N(x)v_N(x)

define an admissible finite chain.
Stationarity cancels the finite log v_N coboundary, giving I(Q_N)=-log r_N.
Combining this with(3),

    inf_(admissible Q) I(Q)
       =inf_(finite admissible Q) I(Q)=h_2(alpha).        (4)

This is an explicit actual-kernel specialization of the classical variational principle.
The finite chains approximate from above in information cost.
A favorable upper bound for one selected I(Q) gives an upper bound for h_2, not a positive lower gap.
A uniform lower bound must hold for every admissible law, or follow from an independent arithmetic condition preventing all low-cost laws.

<a id="critical-excursion-attainment-condition"></a>
### 3. Exact attainment and the critical mean obstruction

The infimum in(4) is attained by an admissible Q if and only if

    F(R)=1,       R F'(R)<infinity.                       (5)

For necessity, equality in(3) forces F_R=1 and D(q||nu_R)=0, so every complete excursion has q(w)=p(w)R^|w|.
Its mean is therefore R F'(R), finite by admissibility.
Every state of D occurs in a first-return word: take a closed word containing that state and retain its segment between consecutive zero visits that contains the occurrence.
Thus equality also forces S=D.

For sufficiency, define H_R(0)=1 and, for x!=0,

    H_R(x)=E_original,x[R^tau_0; tau_0<infinity].

It is positive and finite.
Indeed choose a path from0 to x avoiding0 after its departure, of weight a>0 and length l.
Concatenating each x-to-zero first-hit path gives a distinct first-return word, hence a R^l H_R(x)<=F_R.
First-step decomposition gives H_R(x)=R(KH_R)(x) off0, while R(KH_R)(0)=F_R=1.
Therefore

    Q_R(x,y)=R K(x,y)H_R(y)/H_R(x)                       (6)

is stochastic on all D.
The first-return word probabilities telescope to p(w)R^|w|, whose total is1 and mean is R F'(R)<infinity.
The finite-mean occupation construction gives positive recurrence and a stationary probability, so Q_R is admissible.
Its information rate is h by(3).
Equality of all first-return word probabilities determines the transition row at each state: conditional on any supported prefix ending at x before the return, the continuation first digit has probability R K(x,y)H_R(y)/H_R(x).
Thus Q_R is the only admissible minimizer.
This is precisely the positive-recurrence boundary in the named class, with its actual finite-mean condition explicit.

If F_R<1, equation(3) also gives for every admissible law

    pi(0)<= (I(Q)-h)/(-log F_R).                         (7)

Hence any information-minimizing sequence loses stationary mass at0.
If F_R=1 but R F'(R)=infinity, the infimum is still not attained.
No critical invariant probability is silently substituted in either case.
No criterion is asserted here for arbitrary auxiliary recurrent classes avoiding0.

<a id="canonical-full-tilt-information-defect"></a>
### 4. The canonical full tilted family and its exact failure mode

For0<z<R, the same prefix comparison proves finite positive H_z(x)=E_x[z^tau_0;tau_0<infinity], H_z(0)=1.
Put

    Q_z(x,y)=z K(x,y)H_z(y)/H_z(x) for x!=0,
    Q_z(0,y)=z K(0,y)H_z(y)/F(z).

First-step equations normalize the rows.
Its complete first-return law is p(w)z^|w|/F(z), with finite mean

    mu_z=z F'(z)/F(z).

Finiteness of every derivative for z<R follows directly by comparing n^k z^n with a geometric weight at some z' in(z,R), where F(z')<infinity.
Thus this is an admissible infinite chain.
Excursion likelihood telescoping and the same absolute-integrability bound give

    I(z)=log z-(F(z)/(zF'(z)))log F(z).                  (8)

At z=1 within this domain this recovers L198; its endpoint cases retain L198's own degree assumptions.
Write theta=log z and psi(theta)=log F(exp theta).
Differentiating the absolutely convergent sums gives psi'=mu_z and psi''=Var_q_z(|w|)>=0.
Therefore

    dI/dtheta=psi psi''/(psi')^2<=0                      (9)

because F(z)<1.
As z decreases to0, f_1=1/2 gives I(z)->log2.
As z increases to R, monotone convergence of F and zF' gives

    lim I(z)=h-F_R log F_R/(R F'(R)),                    (10)

where a finite numerator divided by infinity is zero.
The denominator is positive since the one-step term is R/2.
If F_R=1 or F'(R)=infinity, this full tilted family reaches the variational infimum in the limit, whether or not it attains it.
If F_R<1 and F'(R)<infinity, it retains a strictly positive information defect even at the critical boundary.
Finite state Perron approximants from Section2 still converge to h.
Merely moving the full canonical tilt to its critical endpoint need not minimize information.

### 5. An actual all-unit discriminator and the remaining arithmetic question

The last failure mode occurs on actual algebraic units.
Let alpha be a root of unity of actual degree d>4.
There are only finitely many vectors alpha^j in the integral power basis, so every length-n binary sum has each coefficient bounded by C_alpha n.
Its support has at most(2C_alpha n+1)^d elements.
Cauchy--Schwarz gives p_n>=1/|support|, while p_n<=1; therefore h_2=0 and R=1.

The complete L198/L154 rank bound gives F(1)<1 for d>2 and F'(1)<infinity for d>4.
Thus every such cyclotomic input has F_R<1 and finite critical mean numerator.
The full canonical family has the strictly positive limiting information

    lim_(z up to1) I(z)=-(F(1)/F'(1))log F(1)>0,

while inf_Q I(Q)=0.
Along roots of unity of unbounded actual degree, L198 proves this positive defect tends to log2.
The finite approximating laws must have pi_N(0)->0 by(7), and no admissible minimizer exists.
This is an actual-domain control, not a hypothetical generic Markov counterexample.
Its measure is zero, so it is not a nontorsion near-one family or a refutation of Lehmer.

For the unrestricted goal the new usable boundary is exact: stationary normalization is insufficient; even a complete canonical critical tilt can stay separated from the true variational infimum.
A lower information bound for all admissible actual-core laws would give a lower h_2 bound, and h_2<=m then gives a Mahler lower bound.
The unproved obligation is new nontorsion near-one arithmetic excluding low-cost finite/infinite laws, or a useful classification/control of F_R and its critical derivative in that regime.
The general pressure/recurrence theorem and the zero-mass controls do not themselves provide it.
All original Task quantifiers remain unchanged.

### Contribution and checking

The coordinator supplied the actual excursion relative-entropy defect formula, exact interface assembly, canonical tilt calculation and actual cyclotomic failure-mode comparison, using the stated fixed project inputs.
Finite-subgraph approximation, variational pressure and critical positive recurrence are recognized classical mechanisms with the checked Sar15 attribution; no new general theorem or priority claim is made.
The direct proof specializes them to the original algebraic digit law and keeps all normalization and mean hypotheses visible.
No numerical program or new J is needed.

Self-check covered all original versus auxiliary probabilities, R in[1,2], complete word rather than length distributions, integrability without stationary entropy, all finite words, the singleton core, torsion, the strict direction of approximation, finite and infinite critical means, uniqueness on the declared rooted class, derivative signs and limit order.
Full separate noncontributor review is pending; G0001 remains active and unresolved.



The original `Yin_R_G0100_v1#stationary-variational-independent-review` checked this entire frozen proof at2026-10-10 day precision; [the later complete comparison](../audits/reviews/Yin_R_G0697_v1.md#l201-and-r100) preserves its actual inspected scope, inputs, verdict, UNKNOWN relationship and distinct original author/source accounts.
