# Uniform cyclotomic-closure parents without enumerating the archive

This is algorithm preparation in the existing J156 group.
[cyclotomic_parent_sampling.py](cyclotomic_parent_sampling.py) samples the same accepted-parent class as [cyclotomic_closure.py](cyclotomic_closure.py), using integer multiset counts and rejection at the final coefficient-height test.
The existing [independent closure review](../../../audits/reviews/Yin_R_G1111_v7.md#cyclotomic-closure-review) supplies the neutral-factor list and conditional complete-class identification.
The [independent conditional-law finding](../../../audits/reviews/Yin_R_G1111_v10.md#parent-law-review) covers the new argument and repaired implementation, and its [finite-control finding](../../../audits/reviews/Yin_R_G1111_v10.md#parent-controls-review) checks the actual bounded outputs and saved witnesses.
That review does not cover a future online composition or a high-degree Mahler search.
No existing sampling protocol or frozen program is changed by this preparation.

<a id="class-and-bijection"></a>
## Class, exact hypotheses and uniqueness

The supplied core \(F\in\mathbb Z[z]\) is monic reciprocal of positive even degree \(d\), has constant coefficient one, no cyclotomic factor, exponent gcd one, and the frozen descending-coefficient sign normalization.
The constructor checks the coefficient, degree, reciprocal, exponent-gcd and sign interfaces; the caller still supplies the cyclotomic-free certification.
Irreducibility of \(F\) is not needed for this conditional construction.
Fix even \(D\ge d\) and integer height bound \(H\ge1\).
Write \(r_k=D-kd\) for \(1\le k\le\lfloor D/d\rfloor\).

Let \(\mathcal C_r\) be all monic reciprocal cyclotomic products of degree \(r\).
The allowed factors are \((z-1)^2\), \((z+1)^2\), and \(\Phi_m\) for \(m\ge3\) with \(\varphi(m)\le r\).
The reused bound \(m\le2\varphi(m)^2\) makes this list finite.
The squared real factors are counted as single multiset types, of degree two.
Their multiplicities correspond to even multiplicities of the irreducible factors \(z-1\) and \(z+1\).
The degree-zero class contains only the constant product one.

The raw and accepted classes are
\[
 \mathcal Q=\{F(\varepsilon z^k)C(z):\varepsilon\in\{-1,1\},\ C\in\mathcal C_{r_k}\},
 \qquad
 \mathcal A=\{P\in\mathcal Q:\max_i|P_i|\le H\}.
\]
No intermediate coefficient-height test is allowed: later factors may cancel earlier coefficients.
This is the full reciprocal template class, without the additional endpoint/grid restrictions used by some trace-chamber computations.

The parametrization by \((k,\varepsilon,C)\) is one-to-one under the stated hypotheses.
Unique factorization distinguishes the neutral multisets, including the two squared linear types.
Substitution introduces no root of unity into \(F(\varepsilon z^k)\), since its image would be a root of unity of \(F\).
Removing all cyclotomic factors from a parent therefore recovers exactly \(F(\varepsilon z^k)\).
Its nonzero exponent gcd is \(k\), so equality of two parents first forces their substitution indices to agree.
Compression then recovers \(F(z)\) or \(F(-z)\).
Exponent gcd one implies a nonzero odd-index coefficient, so these two polynomials are distinct and the sign is determined.
Finally cancellation recovers \(C\).
Thus no duplicate correction or parent-set enumeration is needed.

<a id="integer-counting-law"></a>
## Integer count table and probability law

Build the factor list once at \(R=D-d\), in the order of the two squared linear factors followed by increasing cyclotomic order.
Let its degrees be \(w_0,\ldots,w_{s-1}\).
An Euler-totient sieve filters orders through \(2R^2\); only selected factor polynomials are constructed, lazily, during a parent attempt.
Define the suffix table by
\[
 T_s(0)=1,\qquad T_s(r)=0\ (r>0),\qquad
 T_j(r)=T_{j+1}(r)+\mathbf 1_{r\ge w_j}T_j(r-w_j).
\]
The first term omits factor \(j\); the second removes one copy from a multiset containing it.
Consequently \(N(r)=T_0(r)=|\mathcal C_r|\).
All table entries, categorical bounds and rank operations are Python integers; no probability is converted to floating point.
The table has \((s+1)(R+1)\) integer entries, rather than one entry per product.
The default explicit order-sieve budget is 20000; a parameter exceeding that bound is rejected before the sieve is allocated.
Increasing that construction budget is an explicit caller choice.

Unranking partitions the integer interval \([0,N(r))\) by the first factor's multiplicity, then by the suffix multiplicities, recursively.
For multiplicity \(a\) at position \(j\), the block size is \(T_{j+1}(r-aw_j)\).
Each valid multiset has one rank and each rank yields one multiset.
The inverse rank method and complete finite product-set checks are included in the controls.

Set \(W=\sum_kN(r_k)\) and \(Q=2W=|\mathcal Q|\).
One raw attempt draws \(k\) with integer weights \(N(r_k)\), an independent fair sign, and an independent uniform integer rank in \([0,N(r_k))\).
Thus each raw parent has probability
\[
 \frac{N(r_k)}{W}\cdot\frac12\cdot\frac1{N(r_k)}=\frac1Q.
\]
The three random choices use `randrange` with integer bounds.
The exact-law statement assumes independent uniform integer choices; seeded Python RNG controls test mechanics and reproduction, not that probabilistic assumption.

Write \(A=|\mathcal A|\).
If \(A>0\), conditioning a raw attempt on the final height test gives the uniform accepted-parent law \(1/A\), equal to uniform choice from the original complete accepted closure.
Repeated independent attempts until acceptance terminate almost surely in the uncapped mathematical model, with expected attempt count \(Q/A\).
The DP does not calculate \(A\), prove a useful acceptance-rate lower bound, or eliminate height-rejection costs.
An empty accepted class has no conditional law, and exhausting a finite attempt cap does not prove emptiness.

<a id="stopping-and-costs"></a>
## Attempt boundaries, deadline and charged failures

`sample_accepted` requires a positive finite integer `max_attempts` and optionally an absolute deadline for its monotone clock.
It checks both limits before beginning a new raw attempt and never checks a deadline inside selection, unranking, multiplication or the final height test.
Every started attempt completes, whether it accepts or rejects.
The optional callback receives a detached deep copy of every completed attempt; its time and the copy cost contribute to total elapsed time.
Changing that supplied copy, including its acceptance flag or nested coefficient/factor arrays, cannot change internal rejection counts, the acceptance decision or the returned parent.
The callback remains observational with respect to the sampler and RNG: it must not alter their state or interrupt the call.
The return object records attempts, height rejections, total construction time, last/max attempt time, elapsed time and any soft overrun.
DP setup has a separate reported build cost and must also be charged by a future caller using an overall budget.
Import/startup time is not included in that DP build field.

For the stopping argument, let \(B_i\) be the event that attempt \(i\) starts.
Before first acceptance, this event depends only on earlier rejected outcomes, their costs and the clock/budget information available before drawing attempt \(i\).
With fresh independent integer draws, \(B_i\) is independent of the current raw parent.
For each \(p\in\mathcal A\), and a fixed maximum of \(n\) attempts,
\[
 \Pr(\text{return }p)=\sum_{i=1}^{n}\Pr(B_i)\Pr(\text{raw attempt }i=p)
                   =\frac1Q\sum_{i=1}^{n}\Pr(B_i).
\]
This is the same for every accepted parent.
Therefore the returned parent remains uniform conditional on a return, provided that event has positive probability.
Nonemptiness alone does not ensure a return if the deadline already prevents every attempt.

There can be one in-flight attempt, plus its callback and return bookkeeping, beyond the cooperative deadline; this is a soft limit with explicit reported cost, not a hard runtime guarantee.
Errors, callback failures or external interruption are not silently classified as height rejection.
A hard supervisor may interrupt a costly current attempt.
The uncensored proposal kernel above still has its stated law, but conditioning on completion before such a hard cap can bias the returned parents by their current construction costs.
No conditional-uniform guarantee is made for that censored collection, and this helper does not change the existing hard-deadline experiment.

<a id="actual-controls"></a>
## Actual bounded controls

[cyclotomic_parent_sampling_checks.py](cyclotomic_parent_sampling_checks.py) performs the controls without evaluating any Mahler measure or changing a parent coefficient.
For each of the following four degrees, it enumerated all DP ranks only for this bounded comparison, checked inverse ranks and raw-parent uniqueness, and compared complete neutral-product and accepted coefficient sets with the unchanged closure generator.
The production helper itself contains no such enumeration.
The accepted counts and per-index results agree with the [v7 review](../../../audits/reviews/Yin_R_G1111_v7.md#cyclotomic-closure-review).

| Degree | Raw parents | Accepted parents, height at most 4 | Accepted by substitution index |
| ---: | ---: | ---: | --- |
| 18 | 330 | 174 | 174 |
| 20 | 840 | 344 | 342, 2 |
| 24 | 4552 | 1170 | 1140, 30 |
| 30 | 41638 | 5532 | 5228, 302, 2 |

Mechanical controls check the five neutral degree-two products, integer categorical interval sizes, both signs, a forced rejection followed by acceptance, explicit exhaustion, no draw after a pre-attempt deadline, and completion of an accepted attempt crossing a soft deadline.
Large DP rank endpoints and middle ranks are checked at degree 80, and the construction-budget guard is exercised without allocating a larger table.
These controls all passed.
The separate detached-callback regression passed on two prescribed attempts, one rejected and one accepted.
It deliberately changed the callback copy's acceptance flag, coefficients and nested factor multiplicities on both attempts; internal rejection counting and the returned polynomial remained unchanged.

The degree-56/80 controls comprise DP counts, four explicit accepted parents, two short helper calls, and the fixed raw-count feasibility check below.
There was no high-degree enumeration.

| Output degree | Neutral degree limit | Factor types | DP integer cells | Raw parent count | Observed DP build seconds |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 56 | 46 | 90 | 4277 | 65939150 | 0.000762 |
| 80 | 70 | 131 | 9372 | 12471358536 | 0.001983 |

The exact substitution weights are respectively
\[
 (30373189,2449573,141877,4877,59)
\]
and
\[
 (5446097265,704595749,77568683,6931259,465493,20399,419,1).
\]
For each high degree, \(F(\pm z)(1+z^{D-10})\) supplies two distinct height-one accepted witnesses.
The neutral factors are \(\Phi_4\Phi_{92}=1+z^{46}\) and \(\Phi_4\Phi_{20}\Phi_{28}\Phi_{140}=1+z^{70}\), respectively.
The corresponding neutral ranks are 554273 and 54992772 in the specified factor ordering.
Exact multiplication, rank round trips and the height test checked these witnesses.

Using seeds 5601 and 8001, each mechanical call had at most 32 attempts and a two-second cooperative deadline.
Both exhausted 32 attempts with 32 height rejections, and neither overran its deadline.
The observed total times were about 0.003079 and 0.005703 seconds, with maximum single-attempt times about 0.000243 and 0.000232 seconds.
These are short implementation observations, not controlled throughput measurements or acceptance-rate estimates.
The failure to accept in these calls does not contradict the explicit accepted witnesses.

An additional parent-only feasibility control fixed 10000 raw proposals at each degree before execution, with seeds 56002 and 80002 and one shared 20-second soft cap checked between complete attempts.
It continued after accepted parents, so this was a fixed raw-count control rather than a first-acceptance call.
Both requested counts completed, in 2.634888 seconds combined and with no soft overrun.

| Degree | Seed | Raw proposals completed | Height at most 4 | Distinct accepted parents | Height rejections | Elapsed seconds |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 56 | 56002 | 10000 | 137 | 137 | 9863 | 0.910687 |
| 80 | 80002 | 10000 | 21 | 21 | 9979 | 1.724110 |

The maximum observed individual construction times were 0.001018 and 0.001963 seconds.
The result retains all 158 distinct accepted coefficient vectors, with their degree groups, as reproducible parent witnesses.
All of them remain in the supplied Lehmer core's closure.
These counts describe only the specified seeded samples; their observed fractions are not asserted to be general acceptance probabilities, a controlled timing comparison, or a conditional-uniformity guarantee for a hard-censored collection.
They demonstrate some legal-parent construction within the stated finite cost while leaving the general height-rejection cost unresolved.

<a id="scope-and-reproduction"></a>
## Research boundary and reproduction

Every constructed parent still has \(M(P)=M(F)\), by the already reviewed substitution and cyclotomic-multiplication identities.
The degree-56 and degree-80 examples therefore remain representations of the supplied degree-ten core, not new primitive cores or new Mahler values.
Reuse the [through-44 source-table scope](../../../audits/literature/Mos26/readme.md#complete-small-cores), [J149 reconstruction](../Yin_J_G0149/readme.md#core-coverage), and [even-degree-through-54 minimum statement](../../../audits/literature/MV226/Yin_U001.md#mv226-secondary-results-and-updates) at their inspected limits.
Increasing the padded parent degree does not move beyond those primitive-core facts.
The unrestricted small-positive-gap direction still needs genuinely new primitive cores of growing degree; a below-Lehmer counterexample must pass beyond the reused through-54 minimum range.
This helper supplies neither that arithmetic bridge nor evidence that a later mutation kernel reaches such cores.

Use Python 3.14.7 with `python-flint==0.9.0`, as in the existing J156 code.
From the repository root, a fresh output name reproduces the bounded controls:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/cyclotomic_parent_sampling_checks.py --output mathematics/computations/outputs/Yin_J_G0156/cyclotomic_parent_sampling_recheck.json
~~~

The completed first result is `mathematics/computations/outputs/Yin_J_G0156/cyclotomic_parent_sampling_controls.json`.
It records exact counts, complete comparison outcomes, explicit witness coefficients, individual high-degree attempt costs and the actual limit status.
The command refuses to overwrite an occupied result path and publishes its result only after all stated controls pass.
No earlier generated output, target-census input, external table, or mutation experiment is required to execute these controls.

The separate feasibility mode runs only the fixed 10000-raw controls under their shared soft cap:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/cyclotomic_parent_sampling_checks.py --feasibility --output mathematics/computations/outputs/Yin_J_G0156/cyclotomic_parent_sampling_feasibility_recheck.json
~~~

Its completed first output is `mathematics/computations/outputs/Yin_J_G0156/cyclotomic_parent_sampling_feasibility.json`.
If the shared cap prevents complete coverage on another machine, the result records each group's actual raw count and limit status without claiming the 10000-raw result was reproduced.

The affected callback boundary has the following separate two-attempt regression command:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/cyclotomic_parent_sampling_checks.py --callback-control --output mathematics/computations/outputs/Yin_J_G0156/cyclotomic_parent_sampling_callback_control.json
~~~

That command completed successfully and retained its result at the stated output path.
Use a fresh output filename to repeat it.
