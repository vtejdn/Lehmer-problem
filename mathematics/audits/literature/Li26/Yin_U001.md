---
author: Yin
---

# Li26: positive-order entropy comparisons for fair Bernoulli sums

Date: 2026-10-07.
Bounded source inspection by assigned AI ms25_source for Yin, during [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).

<a id="li26-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Jiange Li, *Multiplicative comparisons of Renyi entropies for weighted Bernoulli sums*, arXiv:2609.01529v2, 19 September 2026, 11 pages. First submitted 1 September 2026. This is a public preprint; no journal publication is asserted. Exact retained artifact [Li26.pdf](../../../literature/pdf/Li26.pdf), 303516 bytes.

Passages: Definitions and equation (1.1), printed/PDF p.1; fair-cube setup in Conjecture 1.1 and Theorem 1.4, p.2; complete Section 2, Lemma 2.1 and equations (2.1)--(2.7), pp.5--7; biased-law limitation, Remark 2.2, p.8.

Inspection: The arXiv identity/version and retained title/author/page count were checked. The original theorem on p.2 and its entire elementary proof on pp.5--7 were extracted, read and visually inspected. Definitions on p.1 and Remark 2.2 were read in original-source text. The checks below cover the complete proof of Theorem 1.4, including its small-order induction. Theorem 1.5 and Section 3 are not adopted or proof-audited here.


**Audited within the stated scope.**
The proof is elementary and is checked below; this does not claim a full-paper audit, peer-reviewed publication or independent certification of the paper's other results.

<a id="li26-positive-order-comparison"></a>
## Source theorem and conventions

Let X_1,...,X_n be independent fair Bernoulli variables on {0,1}, and let w_1,...,w_n be arbitrary fixed real numbers.
Repeated, zero and negative weights are permitted.
Put S=sum_i w_i X_i.
All laws have finite support.
We use natural logarithms and

    H_q(S)=(1/(1-q)) log sum_t P(S=t)^q,  q>0, q!=1,
    H_1(S)=-sum_t P(S=t) log P(S=t),
    H_infinity(S)=-log max_t P(S=t),
    H_0(S)=log |supp S|.

The same multiplicative comparisons hold with any common logarithm base.
Theorem 1.4 states

    H_q(S)<=C_q H_infinity(S),                            (1)

where

    C_q=[k+2(1-2^k q)]/(1-q),
         k=ceil(log_2(1/(2q))),                 0<q<1/2;
    C_q=2,                                     1/2<=q<2;
    C_q=q/(q-1),                               2<=q<infinity.

In particular,

    H_1(S)<=H_(1/2)(S)<=2H_infinity(S)<=2H_2(S).           (2)

The final inequality uses ordinary monotonicity of Renyi entropy.
These bounds are uniform in n and every weight.
There is no degree, height, house, rank or Mahler-measure condition.
Fairness and independence are part of the theorem; neither follows merely from finite support.

The distinct endpoint statement H_0(S)<=2H_infinity(S) is labeled **Conjecture 1.1** in this source.
It is not adopted here.
In particular, (2) does not identify support entropy with Shannon entropy or Mahler measure.

<a id="li26-largest-fiber-proof"></a>
## Checked largest-fiber proof

Write f(t)=P(S=t), rho=max f, choose tau with f(tau)=rho, and let B be its fiber in {0,1}^n.
Thus |B|=2^n rho.
Let X be uniform on the cube, let Y be independently uniform on B, and put Z=X XOR Y.
For every z and y in B,

    P(Z=z,Y=y)=2^(-n)/|B|.

Thus Z is uniform and independent of Y.
If f_z is the law of S conditional on Z=z, counting the points in a fiber of S gives

    f_z(t)<=f(t)/rho,       average_z f_z(t)=f(t).         (3)

Here and below average_z means the uniform average over the cube.
For any 0<q<1, put phi_z(t)=f_z(t)/f(t) when f(t)>0.
Since phi_z<=1/rho and its average is one,

    sum_t f(t)^q<=rho^(q-1) average_z sum_t f_z(t)^q.     (4)

The zero phi case is handled directly, so no negative power of zero is used.
To verify the inequality when phi>0, multiply phi^(q-1)>=rho^(1-q) by f(t)^q phi, then average.

For fixed z let I={i:z_i=0}, let U=sum_(i in I) w_i X_i and V=sum_(i notin I) w_i X_i, and let c=sum_(i notin I) w_i.
These U,V are independent under the original fair product law.
The conditional law f_z is the image of the law of U given U+V=tau under

    u -> c-tau+2u.

This follows from the coordinate XOR identity and from Y having the law of X conditioned on S=tau.
The displayed affine map is injective over the reals, so if a(u)=P(U=u), b(v)=P(V=v), then

    sum_t f_z(t)^q
       =rho^(-q) sum_u a(u)^q b(tau-u)^q
       <=rho^(-q) [sum_u a(u)^(2q)]^(1/2)
                     [sum_v b(v)^(2q)]^(1/2).            (5)

At q=1/2 both bracketed sums are one.
Equations (4)--(5) yield sum_t sqrt(f(t))<=rho^(-1), exactly H_(1/2)<=2H_infinity.
Monotonicity supplies (1) for 1/2<=q<2.
For q>=2 the elementary inequality sum f^q>=rho^q gives C_q=q/(q-1), including q=2.

For 0<q<1/2, suppose a universal constant D_(2q) has already been proved for order 2q.
Independence and convolution give H_infinity(U),H_infinity(V)<=H_infinity(S).
Substituting the order-2q bound into (5), and then into (4), gives

    D_q<=[1+(1-2q)D_(2q)]/(1-q).                         (6)

Writing E_q=(1-q)D_q reduces this to E_q<=1+E_(2q).
After k=ceil(log_2(1/(2q))) iterations, 2^k q lies in [1/2,1), whose proved constant is two.
Consequently E_q<=k+2(1-2^k q), as stated in (1).
The induction uses only finitely many larger orders for each prescribed positive q.
The point-mass case is direct.
No theorem about unit equations, arithmetic dissociation, Gaussian estimates or log-concavity is an input.

<a id="li26-complex-weight-interface"></a>
## Immediate complex-weight specialization and limits

For any finite list of complex weights, the additive subgroup they generate is a finitely generated torsion-free abelian group.
Choose its free integer basis and send that basis to real numbers linearly independent over Q.
This gives an injective additive map into R.
All subset-sum fibers and their probabilities are unchanged, so (1)--(2) apply verbatim to complex weights.
For algebraic powers in Q(alpha), one can instead choose a Q-basis of the number field and one fixed injective Q-linear map into R.
This map need not preserve multiplication or complex absolute value; the source proof needs only the additive fiber distribution.
This observation is a direct applicability check, not a new source statement about field embeddings.

Remark 2.2 explicitly leaves a biased-Bernoulli analogue open in the source.
An unrestricted comparison independent of the bias is false already for one Bernoulli(p): as p tends to zero, H_1 is asymptotic to p log(1/p), while H_infinity is asymptotic to p.
This does not obstruct the fair law adopted here.

The direct extension to arbitrary abelian groups, including groups with 2-torsion, and its consequences for entropy rates belong to [C_G280](../../../claims/Yin_C_G0280_v1.md#abelian-binary-entropy-comparison).
They are not silently included in the source's real-weight statement.
The source result changes the G0001 transfer question: a valid Shannon lower bound can supply a min-entropy and collision lower bound with a factor of two.
It does not remove the remaining obligation to prove an input-independent positive entropy gap.

## Search and actual review

The bounded search began with the exact question of weighted Bernoulli entropy comparisons and algebraic power-set moment constants after reading L G0086 and BV20-U001.
The primary arXiv record identified this September 2026 preprint and its fixed v2; no duplicate identifier, title, author or Li26 key was found.
It was selected as the sole new source and the broader Sidon/Lambda(p) search was stopped.
No new assertion about the best literature bound in those subjects is made.

The drafting agent checked the complete displayed proof and the complex-weight application against the retained original pages.
No numerical computation or formal verification was performed.

Assigned AI review_matrix_completion independently read the complete assembled unit and the original arXiv v2 HTML Theorem 1.4, all of Section 2 and Remark 2.2.
It checked the largest-fiber XOR independence, likelihood estimate, conditional affine pushforward, the half-order rho exponents, partial-sum min-entropy directions and dyadic constants for q<1/2, the generic q>=2 bound, and the complex additive embedding.
It found no substantive defect.
Its original-source inspection used HTML, not a fresh visual PDF-page review; it did not audit Section 3, other papers or artifact metadata, and performed no computation.

The coordinator read the complete source unit and original Section 2 HTML, and visually inspected the retained PDF pages 2, 5, 6 and 7.
It checked every theorem parameter, the full largest-fiber argument, all positive-order constants and the complex-weight applicability check, finding no substantive defect.
This supplements the separate independent review above; no full-paper audit is asserted.
