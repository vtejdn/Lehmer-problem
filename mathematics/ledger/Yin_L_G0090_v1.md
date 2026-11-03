---
author: Yin
---

# Entropy under random thinning and a Mahler-proportional Poisson bound

Date: 2026-10-07.
Direct derivation by the coordinating AI for Yin, within G0001.
The input is the finite fair-sum comparison H_infinity >= H_Shannon/2 from the separately inspected Li26 largest-fiber proof and its direct abelian-group adaptation.
The [source proof](../audits/literature/Li26/Yin_U001.md#li26-largest-fiber-proof) and [group adaptation](Yin_L_G0089_v1.md#abelian-binary-entropy-comparison) have received independent review at their explicitly recorded scopes.
No numerical experiment or novelty claim is involved.

All logarithms are natural.
Write ell=log 2.
For a finite discrete law mu, H(mu) is Shannon entropy, q(mu)=max_x mu(x), and Col(mu)=sum_x mu(x)^2.
Then Col(mu)<=q(mu).
Every entropy appearing below is the entropy of an actual finite law until the explicitly introduced Poisson step.
No probability entropy is identified with DGB16 algebraic entropy.

<a id="entropy-set-function-thinning"></a>
## Entropy of independent partial sums is a submodular set function

Let G be any abelian group, let v_1,...,v_n belong to G, and let xi_1,...,xi_n be independent fair {0,1} variables.
For I subset [n] put

    X_I=sum_(j in I) xi_j v_j,
    F(I)=H(X_I),       F(empty)=0,
    H_n=F([n]).                                           (1)

The function F is monotone, each one-coordinate increment belongs to [0,ell], and it is submodular: if I subset J and j notin J,

    F(I union {j})-F(I)>=F(J union {j})-F(J).              (2)

For the increment bounds, conditioning on the new independent summand gives H(U+X)>=H(U+X|X)=H(U), while the entropy of a function of (U,X) is at most H(U)+H(X)<=H(U)+ell.
Translation invariance is valid in every group used here, even when a weight vanishes or has torsion.

For (2), set U=X_I, V=X_(J\I), X=xi_j v_j.
The three variables are independent.
Since conditioning on X translates U,

    H(U+X)-H(U)=I(X;U+X),
    H(U+X+V)-H(U+V)=I(X;U+X+V).

The variables form the Markov chain X -> U+X -> U+X+V, so the second mutual information is at most the first.
The data-processing step follows directly from the chain rule and nonnegativity of conditional mutual information.
This proves (2).

Fix the order 1,...,n and define

    a_i=F({1,...,i})-F({1,...,i-1}).

Then 0<=a_i<=ell and sum_i a_i=H_n.
More decisively,

    F(I)>=sum_(i in I) a_i      for every I subset [n].   (3)

To prove this, telescope F(I) in the fixed order.
If i belongs to I, its increment after I intersect {1,...,i-1} is at least its increment after the full prefix {1,...,i-1}, by (2).
Sum these inequalities over the selected indices.
This is a deterministic additive lower bound; it does not say that every subset of a prescribed size retains the same entropy fraction.

<a id="sharp-thinning-laplace-bound"></a>
## An exponential bound with no concentration loss

Let I_p include each index independently with probability p in [0,1].
Applying the finite fair-sum comparison and (3),

    Col(X_I)<=q(X_I)<=exp[-F(I)/2]
                       <=exp[-sum_(i in I) a_i/2].

Independence of the inclusion bits gives

    E Col(X_(I_p))<=product_i (1-p+p exp(-a_i/2)).        (4)

For f_p(a)=log(1-p+p exp(-a/2)), one has f_p(0)=0 and

    f_p''(a)=p(1-p)exp(-a/2)
                /[4(1-p+p exp(-a/2))^2]>=0.

Thus convexity on [0,ell] places its graph below the chord joining its endpoint values: f_p(a)<=a f_p(ell)/ell.
In (4), sum a_i=H_n and exp(-ell/2)=1/sqrt(2), so

    E Col(X_(I_p)) <= (1-p+p/sqrt(2))^(H_n/ell)
                  = exp[-c(p) H_n],
    c(p)=-log(1-p+p/sqrt(2))/ell.                         (5)

Here c(0)=0, c(1)=1/2, and c(p)>0 for p>0.
The endpoints also follow directly.
Formula (5) has no prefactor, initial-time restriction or quadratic loss in H_n/n.
It bounds the random mask average; a pointwise bound for every mask is not asserted.

<a id="poisson-from-thinned-fair-bits"></a>
## Pointwise comparison with Poisson digits

Now take v_j=alpha^(j-1) in O=Z[alpha], where alpha is a nontorsion algebraic unit.
The additive group O is a free lattice of finite rank d, with dual torus T^d.
Fix lambda>0, take independent N_j~Pois(lambda), and denote by C_orig(n,lambda) the collision probability of sum_(j=1)^n N_j v_j.
Its Fourier expression is

    C_orig(n,lambda)=integral_(T^d) exp(-4lambda S_n(y))dy,
    S_n(y)=sum_(j=1)^n sin^2(pi<y,v_j>).                   (6)

This follows by taking the squared modulus of the product of Poisson characteristic functions.
Parseval applies to this probability mass function, whose l2 norm is finite.

Set p=1-exp(-4lambda), so p in (0,1).
For 0<=u<=1, concavity of log gives

    log(1-pu)>=(1-u)log1+u log(1-p)=-4lambda u.

For a fixed index set I, the Fourier square of X_I is product_(j in I) cos^2(pi<y,v_j>).
Averaging independently over I_p and using (6) yields

    C_orig(n,lambda)
      <=integral product_(j=1)^n [1-p sin^2(pi<y,v_j>)]dy
       =E Col(X_(I_p))
      <=exp[-c(p) H_n].                                 (7)

All inequalities have the direction needed for an upper bound on the Poisson collision probability.
The random thinning is only a comparison device; a Poisson variable is not represented as a sum of fair bits with deterministic weights.

<a id="mahler-dependent-poisson-rate"></a>
## Consequences for Mahler measure and linear-order moments

Put m=log M(alpha)>0 and u=min(m,ell).
Let c_0>0 be exactly the accepted symbolic BV20 constant, expressed in natural entropy units.
Its Bernoulli entropy theorem gives

    h_Shannon(alpha)>=c_0 u.                              (8)

The {0,1} and {-1,1} sum laws are related by multiplication by two and a deterministic translation; multiplication by two is injective on O, so their probability entropies agree.
Shannon entropy of independent time blocks is subadditive, since the shift A^n is injective and summation is a deterministic map.
Thus h_Shannon=inf_n H_n/n, and (8) gives H_n>=n c_0 u for every n, not just asymptotically.

Define the explicit positive constant

    b(lambda)=c(1-exp(-4lambda))
       =-log(exp(-4lambda)+(1-exp(-4lambda))/sqrt(2))/ell,
    gamma_lambda(m)=b(lambda)c_0 min(m,ell).              (9)

Equations (7)--(9) prove

    C_orig(n,lambda)<=exp[-gamma_lambda(m)n]  (n>=1).     (10)

The balanced law recording sum_j N_j has smaller collision probability.
By the exact polynomial comparison in [L G0086](Yin_L_G0086_v1.md#removing-poisson-total-coordinate), both collision entropy rates exist and agree.
Consequently

    gamma_lambda(m)<=h_2,Poisson(alpha,lambda)<=m.          (11)

The upper bound is the independent small-body proof in L G0086; it is not an infinite-alphabet algebraic-entropy formula.

For the original ordered orbit relation count A_(n,r), put a_(n,r)=A_(n,r)/n^(2r).
The central coefficient estimate of [L G0086](Yin_L_G0086_v1.md#balanced-poisson-moment-bridge) then gives, whenever floor(lambda n)>=1,

    a_(n,floor(lambda n))
       <=4(ceil(2lambda n)+1)^2 exp[-gamma_lambda(m)n].    (12)

This is a uniform finite formula with an exponent proportional to m near zero at each fixed lambda.
It reaches a linear moment order; unlike L G0085's window, it is not obtained from a nondegenerate-shape count and fixed-order asymptotics.
It still does not give a positive rate independent of m, nor L G0084's specific Gaussian-type target at slope 1/(16C).

For clarity, (12) and L G0086's lower bound do give an exact conditional equivalence on the nontorsion algebraic-unit domain:

* If m has a common positive lower bound delta, then for every fixed lambda>0, (10) and (12) have a common positive exponential rate gamma_lambda(delta), with universal displayed prefactors.
* Conversely, if for one fixed lambda>0 there is a common gamma>0 and, for every input, along an unbounded sequence of n, a_(n,floor(lambda n))<=exp[-gamma n+o(n)], then L G0086's liminf lower bound implies m>=gamma for every such input.

The o(n) term in the converse may depend on the input.
This equivalence concerns normalized moments at one linear slope, not fixed-order asymptotics and not a prescribed ratio C lambda.
Any new moment argument must now improve beyond the available Mahler-proportional exponential rate.
Establishing such a rate again would not remove the dependence obstructing the uniform gap.
There is no proof or refutation of the Lehmer gap here.

## Current proof and retained checking scope

The complete current statement and every original mathematical argument are retained in [C282](../claims/Yin_C_G0282_v1.md#argument), with its actual selected assessment.
The [current whole finding](../audits/reviews/Yin_R_G0535_v1.md#current-thinning-poisson-finding) is self-reviewed.
The [complete original checking account and precise findings](../audits/reviews/Yin_R_G0535_v1.md#historical-thinning-author-finding) retain their original2026-10-07 inputs, actual contributions, coverage and limitations.
Original independent or collaborator wording does not establish unrecorded initial context or bind a later C to an old finding.
