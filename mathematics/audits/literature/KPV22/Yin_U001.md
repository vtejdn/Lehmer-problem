---
author: Yin
---

# KPV22-U001: diffusion criteria and the original quartic first-return boundary

<a id="kpv22-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Kleptsyn, Pollicott and Vytnova, Uniform lower bounds on the dimension of Bernoulli convolutions, arXiv:2102.07714v3,17 January2022; the retained50-page PDF [KPV22--arxiv-v3.pdf](../../../literature/pdf/KPV22--arxiv-v3.pdf).

Passages: Example1.11 p5; Definition1.15/equations4--5 p7; Theorems1.17/1.19 pp8--9; Definition1.21, Remark1.22 and Theorems1.23/1.25 pp10--11; Lemma5.2 p29 and its inequality p30; Definitions5.7--5.8/equations28--32 pp31--32; Lemmas5.9--5.10 and proof of Theorem1.17 pp32--34; Proposition5.11 statement p34; Section6 setup/Example6.1 p37 and proof setup pp38--39. Printed and one-based PDF page numbers coincide.

Inspection: On2026-10-26, original_signed_asymptotic for Yin checked the selected statements, hypotheses, original-law coordinate conversion and applicability boundary. The proof of Theorem1.17 and its survival/energy argument were read at pp32--34; selected source pages7,8,10,29,32,33,34 were rendered and visually checked. The existence proof of Theorem1.19/Proposition5.11, full Section6 proof, numerical algorithms and tables, other editions and any formal code were not audited. This is author source inspection, not an independent project review.


The source statements below are accepted for this selected definition and applicability comparison at the specified reading depth.
No new numerical estimate or theorem about the actual critical first-return mean is adopted.
The complete original-law consumer is [D_G9](../../../drafts/Yin_D_G0009.md#closed-loop-source-applicability); its exact B_0/R_f interface and remaining cancellation assumptions retain their own author status.

<a id="symmetric-diffusion-criterion"></a>
## Symmetric operator, admissible interval and source conclusion

**Definition.**
For0<lambda<1, let S consist of similarities f_j(x)=lambda x-c_j with probabilities p_j>0 summing to one.
Choose a compact invariant interval J_lambda containing the support of the stationary probability mu.
An interval J is lambda-admissible when its interior contains J_lambda-J_lambda.
Let F_J consist of functions psi on R, zero outside J, positive on J and bounded there between two finite strictly positive constants.
For0<alpha<1, the source's symmetric diffusion operator is

    D^(2)_(alpha,S) psi(z)
      =lambda^(-alpha) sum_(i,j) p_i p_j
                         psi((z-c_i+c_j)/lambda).          K1

The sign of the displayed digit difference can be reversed by interchanging i,j; the sum is unchanged.
The correlation dimension used here is the energy threshold

    D2(mu)=sup({0} union {alpha>0: integral integral |x-y|^(-alpha)
                                           dmu(x)dmu(y)<infinity}).

**Source statements.**
Theorem1.17 states that if an admissible J and psi in F_J satisfy D^(2)_(alpha,S)psi(z)<psi(z) for every z in J, then D2(mu)>=alpha, hence dim_H(mu)>=alpha.
Theorem1.19 states that for every alpha<D2(mu) such a piecewise constant test function and admissible interval exist.
Its more quantitative existence/partition formulation is Proposition5.11; its construction proof is not accepted as newly proof-audited here.
No condition excluding intermediate visits to zero is part of either statement.

For the complementary digit law, combine equal differences d=c_i-c_j with probability q_d=sum_(c_i-c_j=d)p_i p_j.
The complementary contracting maps are g_d(z)=lambda z-d, with stationary probability mu*(-mu).
Their backward random process uses z maps to(z+d)/lambda, and equation32 writes K1 as lambda^(-alpha) times its expectation operator.
An admissible interval cannot be reentered after exit.
The proof of Theorem1.17 uses the nonnegative supermartingale lambda^(-alpha n)psi(z_n) to bound survival in J by C lambda^(alpha n), then bounds the small-ball probability of two independent mu samples and their energies.
This is real-interval survival of the unconditioned backward process, not the return-time tail of a critical Doob chain.

At the Bernoulli specialization, the printed strict inequality max|d|/(1-lambda)<m in the p32 proof is unnecessary and is not reused: here m=1/(1-lambda), and strict admissibility puts the interval endpoints beyond +/-m.
That exact endpoint fact gives the claimed no-reentry comparison directly.
For the potential psi(r)=integral integral |x-y-r|^(-alpha)dmu(x)dmu(y), the p29 Lemma5.2 display also prints psi(r)<psi(0) including r=0, while its proof uses the non-strict inequality.
Neither that impossible strict-at-zero form nor its Fourier proof is used in this inspection.
These bounded observations do not constitute an audit of the source's unselected arguments.

<a id="asymmetric-diffusion-criterion"></a>
## Section6 has a different measure-regularity target

**Definition.**
Let T be finitely many orientation-preserving, uniformly contracting C^(1+epsilon) diffeomorphisms f_j of R preserving a compact interval J, with probabilities p_j>0 summing to one.
For0<alpha<1 the asymmetric diffusion operator is

    D^(1)_(alpha,T)psi(z)
      =sum_j p_j |(f_j^(-1))'(z)|^alpha psi(f_j^(-1)(z)). K2

A probability mu is alpha-regular when some finite C bounds mu(B_r(x)) by C r^alpha for every x and r>0.
Its Frostman dimension D1 is the supremum of those exponents; this source D1 notation is not Shannon entropy dimension.
Theorem1.23 requires a test function supported on a closed positive-radius neighborhood of J, positive and uniformly bounded above and below there, and strictly decreasing under K2 at every point of that neighborhood.
Its conclusion is alpha-regularity of the stationary probability of T.
Theorem1.25 supplies such tests for alpha<D1(mu).
The full proof of those two statements is not newly audited.

Remark1.22 identifies K1 for fair Bernoulli bits with K2 for the three contracting maps lambda z-1,lambda z,lambda z+1 and weights1/4,1/2,1/4.
Example6.1 separately identifies an L1 fixed density for the asymmetric alpha=1 operator of the original two-map IFS with absolute continuity of its real stationary measure.
These are statements about contracting-IFS stationary measures on R.
They neither identify the actual critical H nor supply a stationary probability for the critical countable return core.

<a id="actual-quartic-diffusion-specialization"></a>
## Exact original-law conversion and its quantitative limit

Choose the source Example1.11 fair maps z maps to lambda z and lambda z+1, and lambda=beta^(-1) for P(t)=t^4-t^3-t^2-t+1.
The difference digit d then has EXACTLY the original probabilities q_0=1/2 and q_1=q_(-1)=1/4.
Under z=beta x, its backward map becomes

    z' = beta(z+d),
    x' = z'/beta = beta x+d.                              K3

Thus the source backward process is an exact rescaling of the original unconditioned expanding-coordinate process, with no new digit law or renormalization.
For a test psi satisfying Theorem1.17, put f(x)=psi(beta x); then K1 becomes

    (D^(2)_(alpha,S)psi)(beta x)
        =beta^alpha sum_(d=-1)^1 q_d f(beta x+d).           K4

The source interval condition contains the full expanding core strip: use J_lambda=[0,1/(1-lambda)], so the interior of J contains[-S,S], S=beta/(beta-1), whereas |x_+|<B=1/(beta-1) gives beta x_+ in(-S,S).
After restriction to the actual algebraic core D, dropping nonnegative terms from successors outside D gives

    beta^alpha P_D f<=f on D.                            K5

Here f means f(x_+) and remains strictly positive and bounded on D.
It includes f(0)>0 and the original zero row.
For any n, positive iteration gives beta^(alpha n)p_n f(0)<=f(0), so

    p_n<=beta^(-alpha n),   R>=beta^alpha.                K6

The same restriction to B_0=P_D on D minus{0} yields

    B_0^n(x,y)<=beta^(-alpha n) f(x)/f(y),
    limsup_n B_0^n(x,y)^(1/n)<=beta^(-alpha),              K7

for each fixed nonzero x,y.
Every coefficient and domain restriction in K5--K7 retains the original law.
This comparison does not transfer a norm between the real function space and l2(sigma).

The [accepted CFMZ26 exact dimension identity](../CFMZ26/Yin_U001.md#original-collision-and-energy-dimension) gives d_*=D2(mu)=log R/log beta<1; affine rescaling from fair bits to fair signs preserves the energy threshold.
The source existence theorem provides tests for alpha<d_*.
Letting alpha increase to d_* in K7 supplies only r_0<=1/R, equivalently R_f>=R through D49's CL6.
It does not give r_0<=1/beta, R_f>R or a finite critical mean.
A full-process test of the source form with alpha>d_* would contradict K6, or Theorem1.17 itself.
In particular the spectral parameter t=beta^alpha needed beyond R lies outside the supplied existence range.

Deleting the distinguished zero, changing a test function there to vanish, or checking inequalities only on D minus{0} changes the source hypotheses.
Theorem1.19 supplies no existence result for that modified problem.
Likewise the identical three-map operator in Remark1.22 does not add a zero-avoidance condition or the actual H-dependent critical tilt.
A genuinely new avoidance/continuation estimate is still needed for the original first-return question.
No such estimate, whole-source audit, numerical reproduction or new project theorem is claimed here.
