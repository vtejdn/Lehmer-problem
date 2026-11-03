---
author: Yin
---
# LL10: pointed loop and Green function attribution

Date:2026-10-10.
The assigned structural_research AI for Yin directly inspected the retained author-hosted manuscript of Gregory F. Lawler and Vlada Limic, Random Walk: A Modern Introduction (2010).
Page locators below are the retained author's PDF/internal pages201--204, not a claim about another published edition.

<a id="pointed-loop-attribution"></a>
## Statement, proof inspection and precise use

Section9.3 on p.201 defines rooted-cycle generating functions for a weighted vertex set.
On p.202 equation(9.2) gives g=1/(1-f), with f the first-return generating function.
The pointed loop quantity F_x(A;lambda) is defined by exponentiating the sum of q(w)lambda^length/length over rooted loops in A which visit x; the set A is explicitly not required to be finite.
Lemma9.3.2 on pp.203--204 identifies this exponential with the Green generating function g_A(lambda;x).

The complete selected proof was read.
It handles periodic multiplicities using the number of distinct cyclic rotations and the number of visits to x.
After marking a visit, the loop weight rooted at x is divided by its number of returns.
Decomposition into j first excursions yields the series sum f^j/j=-log(1-f)=log g.
This is the classical identity specialized in [D156, Section3](../../../ledger/Yin_L_G0289_v1.md#rooted-cycle-subtraction-identity).
D156 includes its own complete marked-word coefficient proof, keeps every original digit weight, and proves finiteness of each diagonal sum in its arithmetic graph.
Its actual changing-modulus formula, zero-avoiding subtraction, critical-mean costs and quartic controls are separately proved local deductions.

Proposition9.3.3 on p.204 states the subsequent determinant identity for a FINITE state set X.
It is not adopted as an infinite Fredholm determinant identity, trace-class assertion or theorem about the actual infinite core.
D156 uses a nonnegative coefficient difference before summing; it does not subtract two potentially divergent loop series.

## Access, coverage and limits

The initial web PDF read failed.
After the coordinator's successful normal acquisition, the local registered PDF was read with pdftotext -layout on the four selected pages.
The first terminal display encountered a Windows text-encoding error after the first page; explicitly using UTF-8 for the display then delivered all four pages.
This was an operational extraction correction, not a failed mathematical computation.
No visual-layout audit or inspection of the rest of the book is claimed.

The selected lemma's statement, conventions and complete proof were actually inspected.
Its role here is classical attribution with a self-contained local proof, not an unproved imported mathematical input; no separate source unit is needed.
This compact record does not assert earliest priority, a full-book audit, project novelty, independent human endorsement or a source theorem beyond the inspected scope.
The source has no remaining access objection for this precise use.


<a id="countable-convergence-attribution"></a>
## Countable positive-recurrent convergence: bounded additional inspection

2026-10-10T11:27.
Authorized source extension by structural_research for Yin, preserving the earlier pointed-loop inspection above.
The same canonical LL10 author PDF was text-extracted on printed/PDF pp.269--279.
The exact consumed attribution is the unnumbered paragraph on p.271 immediately before Proposition12.4.2: for an irreducible, aperiodic Markov chain on a countable state space, positive recurrence (there expressed as existence of an invariant probability) gives p_n(x,y) tending to pi(y).
Section12.4.2 on p.275 defines total variation for countable laws and states inequality(12.21); rearranged, it says total variation is at most the disagreement probability of any coupling.

[D196, Section2](../../../ledger/Yin_L_G0329_v1.md#positive-branch-coupling-proof) attributes this classical qualitative convergence and coupling method to the selected source and supplies a complete local product-chain meeting proof for a chain with a positive loop at zero.
The local actual-input deductions concern the original return law, true H/L ratio limits, full midpoint occupation convergence and all-late central capture/escape.
The source is attribution, not an unproved proof dependency or a newly claimed project theorem.

Proposition12.4.2 adds the uniform k-step pairwise total-variation contraction hypothesis(12.15) and concludes an exponential rate.
Neither that extra hypothesis nor its conclusion or proof is adopted for the actual infinite core.
The maximal-coupling theorem12.4.5 is also stronger than needed and is not used.
No infinite-mean renewal limit, quantitative onset, uniform geometric mixing or sharp conditioned-bridge theorem is attributed to the two selected passages.
The surrounding extraction is not a full audit of every statement or proof on pp.269--279.

The separately assigned orbit_research AI independently confirmed the same p.271/p.275 statements by text extraction and visual inspection of those two full pages, without supplying a D196 mathematical derivation.
Structural_research's own inspection was text-only.
No other book edition, earliest-priority claim or full-book proof audit is asserted.
The previously retained limited reading history remains historical; this paragraph adds only the stated new scope.
