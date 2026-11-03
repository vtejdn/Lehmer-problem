---
author: Yin
---

# Var25: the Salem entropy-equality question and its scope

## Fixed retention and present registration

Date: 2026-10-10T14:59.
At Yin's request, this completed source-interface record is fixed from D G0003.
The complete 2026-10-07 reading, local corrections, inspection limits and dated search findings below are preserved; only source addresses and relative links change.
The historical statement that registration was pending describes that earlier date.
No source proof, current literature survey or mathematical program was rerun for this organization.
G0001 remains paused.


Date: 2026-10-07.
Scoped source reading for G0001 by assigned AI ms25_source and the coordinator for Yin.
This unit records a dated primary survey statement, not a theorem resolving it.

<a id="var25-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Péter P. Varjú, *Entropy rates in the dimension theory of self-similar measures*, arXiv:2509.22042v2, 22 March 2026; first submitted 26 September 2025. The arXiv record calls v2 the final accepted version to appear in Proceedings of Fractal Geometry and Stochastics 7. The key retains first-release year 2025; a separate published edition is not asserted. Retained Var25.pdf: 14 pages, 353260 bytes.

Passages: Section 3.1, printed/PDF pp.6--8, especially Question 8 on p.6 and the explicit Salem equality discussion on p.7. Page numbering agrees.

Inspection: Both readers inspected the relevant extracted text. The coordinator visually checked p.7, independently matched retained bytes and checked the exact arXiv version metadata. Statement/context reading only; no proof audit of the survey's cited dimension theorem or all cited entropy results.


The [fixed version record](https://arxiv.org/abs/2509.22042v2) gives 22 March 2026 21:17:48 UTC.
This draft records the available acquisition and inspection details above; bibliographic registration of the public retained artifact remains pending.

## Exact question and normalization

For the fair Bernoulli convolution parameter lambda in (0,1), h(lambda) is the entropy rate of its finite independent sign sums.
At an algebraic unit, the survey gives h(lambda)<=log M(lambda).
For a reciprocal Salem number, M(lambda)=lambda^(-1), so the specific question is

    h(lambda) = log(lambda^(-1)).

On p.7 the author explicitly presents deciding this for any or all Salem numbers as a delicate question.
This is neither an equality theorem nor a strict-inequality theorem.
Question 8 on p.6 asks whether a Bernoulli convolution in lambda in [1/2,1) can have dimension less than one when lambda^(-1) is not Pisot.
The survey explains the entropy/dimension connection in the surrounding text; this unit does not independently audit its cited general theorem.

The cited strict h<log M result assumes absence of unit-circle conjugates, so it cannot be extended to Salem inputs by omitting that hypothesis.
The retained BV20 source interface already records this restriction.
Conversely, singularity of a measure alone does not assert dimension below one or strict entropy loss; no such implication is adopted here.

The original sign-sum rate at alpha and at alpha^(-1) is identical: multiply a length-N sum by alpha^(N-1) and reverse the independent identically distributed signs.
This elementary normalization is already used in the local G0001 materials.
It does not change the digit distribution or turn the open equality into a premise.

## Typographical and adoption boundaries

The adjacent p.7 Garsia-number sentence prints h(lambda)=M(lambda)=log2, although M is the multiplicative Mahler measure defined on that same page.
The p.8 sentences also omit a logarithm when comparing h(lambda) with lambda^(-1).
Those literal equalities are not adopted.
The checked Salem question on p.7 includes the logarithm explicitly, and the unit's normalization above uses that statement.
No independent certification of the nearby numerical constant 0.44 is inferred from this survey.

The source's version date is 22 March 2026.
The fact that it poses this question is verified; an exhaustive assertion about the state of the question on 7 October 2026 is not.
A bounded follow-up search looked for recent Salem entropy, dimension and singularity claims.
The [OpenAI mathematical collection](https://github.com/openai/math) was located as a possible recent lead, but its large catalogue page did not expose manuscript text in the web reader and the direct overview-source endpoint failed.
No individual theorem or proof from that collection was checked or adopted in this unit.
This unresolved lead does not supply an entropy-equality or dimension-drop input.

## Consequence for the current route

A strict positive Salem entropy deficit would itself require substantive evidence.
The local [transition-collapse working argument](../../../claims/Yin_C_G0330_v1.md#subexponential-height-mixed-budget-collapse) only bounds one Fourier certificate family by o(N); it does not prove h=log M.
The finite averaging tools and the one-window consistency test remain separate, fully stated local arguments.
This source is used to preserve that problem boundary, without making a novelty or comprehensive current-status claim.
