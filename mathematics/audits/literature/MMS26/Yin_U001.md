---
author: Yin
---

# MMS26: quantitative Salem Fourier decay and transition-product limits

Source: [MMS26.pdf](../../../literature/pdf/MMS26.pdf).
The related dated entropy question is in [Var25-U001](../Var25/Yin_U001.md#var25-u001).
This source-interface audit retains the reading, corrections, search findings and proof limits below; it does not resume G0001.

Date: 2026-10-07.
Scoped source inspection for G0001 by the assigned AI ms25_source and the coordinator for Yin.
The former located, acquired and read the source; the coordinator independently checked the retained bytes, source passages and the limited repairs below.

<a id="mms26-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Juan Marshall-Maldonado and Boris Solomyak, *Quantitative weak mixing for typical Salem substitution suspension flows*, arXiv:2601.15035v1, 21 January 2026. Public research preprint; no journal publication is asserted. Retained edition: 23 PDF pages.

Passages: Printed/PDF pp.18--20, Appendix A, Proposition A.3 and (A.3)--(A.7); pp.20--22, Appendix B, Fourier product (B.1), Corollary B.1, Propositions B.2 and B.3. Page numbering agrees.

Inspection: Relevant full passages were read from the retained PDF extraction; the coordinator visually inspected p.21 and independently verified the hash and arXiv version. The authoring source reader rendered pp.18--22 and reported inspecting the relevant pages. Statements and the local corrections below are checked; the entire recurrence sketch, its external norm estimate and the omitted lower-bound proofs are not independently proof-audited.


The [version record](https://arxiv.org/abs/2601.15035v1) gives 21 January 2026 14:37:51 UTC and both authors.
This unit is a source-interface audit with explicit proof limits; it does not label the whole preprint audited.

## Checked statements and conventions

For a Salem number alpha>1, lambda=alpha^(-1), and p in (0,1), the source uses the distribution nu_lambda^p of the infinite series sum_(n>=0) xi_n lambda^n, with independent signs of probabilities p,1-p.
Its Fourier convention has the factors

    p exp(-2pi i lambda^n xi)+(1-p)exp(2pi i lambda^n xi).

The fair case p=1/2 has product cos(2pi lambda^n xi).
Corollary B.1 states that constants A,C>0 depending on alpha,p give

    |hat nu_lambda^p(xi)|<=A exp[-C log*(|xi|)], |xi|>=1.

Here log* is the iterated-logarithm count defined in Appendix A.
Changing its fixed base changes the constants; it is not log log.
This is an upper bound on an infinite scalar Bernoulli convolution.
It is not a lower bound on a finite product or a theorem identifying the entropy rate with log alpha.
We retain it as a checked source statement and mechanism comparison, without making it a premise of the local transition-collapse proof.

Proposition A.3 sketches the underlying recurrence estimate: at tower lengths N=k_l, k_0=1 and k_(i+1)=L^(k_i), a sum of squared distances ||w alpha^n||_(R/Z)^2 has a positive lower bound proportional to l, uniformly over w in [1,alpha).
The mechanism is nearest-integer rounding, an integer companion recurrence whenever errors remain small, and persistence of a nonzero central eigencomponent.
The lower bound for that component, (A.5), invokes an external Garsia estimate and source reference [5].
Those inputs and the complete recurrence proof were not reconstructed in this inspection.

The discussion before Proposition B.2 explicitly omits details of its small-conjugate multiplier lower-bound argument.
B.2 treats biased p<1/2 and restricts a possible logarithmic decay exponent.
B.3 treats the fair case: a uniform eventual bound of the form

    |hat nu_lambda(xi)| <= C [log_alpha(xi)]^(-gamma (log_alpha log_alpha(xi))^beta)

with beta,gamma>0 would force beta<=1.
These are source statements, not fully audited lower-bound proofs.
Neither supplies a transition product bounded away from zero along central-small multipliers.

<a id="mms26-local-proof-corrections"></a>
## Literal proof issues and bounded repairs

1. On pp.19--20, the alternative in which a nearest-integer error has magnitude at least delta_1 gives squared contribution at least delta_1^2, whereas the displayed block conclusion uses delta_1.
   Replace the final positive lower constant by the smaller delta_1^2 and retain a sufficiently large tower base.
   This fixes this particular constant passage; it does not independently establish the external estimate (A.5).
2. Equation (A.7) starts its blocks at k_0=1 and omits the term n=0.
   The displayed equality is therefore an inequality with the full sum greater than or equal to the blocked sum.
   This direction suffices for the stated lower-bound mechanism.
3. The p-dependent factor printed in the proof of Corollary B.1 is not valid uniformly for p in (0,1).
   At p=1/1000 and tau=1/2, |p+(1-p)e^(2pi i tau)|=499/500, while its claimed upper bound 1-((1-p)/2)||tau||^2 equals 7001/8000.
   A direct valid replacement is

       |p+(1-p)e^(2pi i tau)|
          =sqrt(1-4p(1-p)sin^2(pi tau))
          <=1-8p(1-p)||tau||_(R/Z)^2
          <=exp[-8p(1-p)||tau||_(R/Z)^2].

   This follows from sqrt(1-x)<=1-x/2 and |sin(pi tau)|>=2||tau||_(R/Z).
   It preserves a positive decay coefficient for every fixed p in (0,1).
   The fair case used in G0001 is included.
   The source's incorrect general coefficient is not adopted.

These are local algebraic checks of the cited steps.
The source statement's existential constants can absorb the first two changes.
This inspection does not certify the whole Appendix A proof or its other dependencies, and it supplies no new quantitative rate to the local finite-dimensional argument.

## G0001 use and search boundary

The search asked whether the finite transition-product mechanism already appears in Salem Fourier theory, and whether a strict Salem entropy deficit is established.
Primary arXiv records and the exact retained appendix were inspected on 2026-10-07.
The source directly identifies the rounded recurrence and small-central multiplier mechanisms, so these mechanisms are not claimed novel.
The local [transition-collapse working argument](../../../claims/Yin_C_G0330_v1.md#central-small-transition-collapse) has its own complete proof from C G0317; the source does not replace its all-conjugate scope or finite-window/smoothing arguments.

The scalar infinite-law theorem cannot automatically be applied to N-dependent mixed stable/central covectors.
In particular, central coordinates of size N^(-1/2) can have a bounded whitened norm without giving a negligible perturbation of every factor in a length-N product.
Any quantitative transfer needs its own proof.
The source's omitted lower-bound details are not treated as such a proof.
The related dated entropy question is recorded in Var25-U001.
No exhaustive October-2026 literature-status claim is made.
