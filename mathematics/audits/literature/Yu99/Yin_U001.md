---
author: Yin
---

# Yu99-U001: fixed-algebraic-input p-adic logarithmic precision bound

<a id="yu99-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: [Yu99](../../../literature/pdf/Yu99.pdf), published Acta Arithmetica 89(4),1999,337--378; the complete42-page original PDF.

Passages: Printed337--339, PDF1--3: introductory consequence, equations(1.1)--(1.10), Theorem1 and the subsequent scope remarks; printed340's proof-method orientation was also read.

Inspection: Root,2026-10-28: direct extracted-text and full-page visual inspection of the statement, constants, valuation/height conventions and hypotheses; source proof, Theorem2 applications and later sections were not reviewed.


The coverage state is Read, with the specified statement and hypotheses checked.
The established Theorem1 and its displayed introductory consequence are accepted as external inputs for the exact hypotheses below.
This acceptance does not assert an independent audit of the original proof or an independent project review.
The intended use is the fixed finite cyclotomic-alphabet precision question of [G0001](../../../tasks/Yin_T_G0001_v1.md), with all project-specific nonvanishing, unit and degree arguments still to be supplied at their responsible home.

<a id="prime-ideal-valuation-and-height-conventions"></a>
## Valuation and height conventions

Let K be a number field of degree d, and let mathfrak p be a prime ideal above the rational prime p.
For alpha!=0 in K, ord_mathfrak p(alpha) is the integer exponent of mathfrak p in the principal fractional ideal(alpha); ord_mathfrak p(0)=infinity.
Write e_mathfrak p and f_mathfrak p for the ramification index and residue degree.
The normalized extension of the rational p-adic valuation is v_p=ord_mathfrak p/e_mathfrak p, so v_p(p)=1.
These are distinct normalizations; a bound for ord_mathfrak p must be divided by e_mathfrak p before comparison with coefficientwise p^k divisibility.
A mathfrak p-unit means ord_mathfrak p(alpha)=0; it need not be a global algebraic unit.

The source's h_0 is the absolute logarithmic Weil height.
For the primitive integer minimal polynomial a_0 product_(j=1)^r(X-alpha_j), with a_0>0, it is

    h_0(alpha)=(log a_0+sum_j log max(1,|alpha_j|))/r.

This agrees with the [existing height normalization](../Smy08/Yin_U001.md#smy08-height-normalization).
All logarithms are natural.
The source also uses h'(alpha)=max(h_0(alpha),f_mathfrak p log(p)/d).
Neither height is the unnormalized total logarithmic Mahler measure of a varying original polynomial.

<a id="fixed-input-logarithmic-bound"></a>
## Checked statement used here

Let n>=1 and let alpha_1,...,alpha_n be nonzero elements of K.
Assume each is a mathfrak p-unit.
The source's field hypothesis is zeta_3 in K if p=2, and either p^(f_mathfrak p)=3 modulo4 or zeta_4 in K if p>2.
For arbitrary integers b_1,...,b_n and any real B>=max(3,|b_1|,...,|b_n|), put

    Xi=product_(j=1)^n alpha_j^(b_j)-1.

When Xi!=0, Theorem1 gives

    ord_mathfrak p(Xi)<C(n,d,mathfrak p) product_j h'(alpha_j) log B,

with the explicit positive constant C defined in source equation(1.10).
No multiplicative independence of the alpha_j is required for this bound.
The extra Kummer-degree condition(1.11) is used only for the separately stated improvement and is not assumed here.

For a simpler fully displayed bound, the consequence on printed337 gives, under these hypotheses in particular,

    ord_mathfrak p(Xi)<K_Y log B,
    K_Y=19 (20 sqrt(n+1) d)^(2(n+1)) e_mathfrak p^(n-1)
        *p^(f_mathfrak p)/(f_mathfrak p log p)^2
        *log(exp(5) n d)*product_j max(h_0(alpha_j),log p).

The radical is sqrt(n+1), followed by the factor d outside the radical.
The full number field degree d occurs, not the degree of Xi or of a selected residual.
For fixed K,mathfrak p and the fixed finite ordered list of algebraic numbers, K_Y is a fixed positive effective constant independent of the integer exponents.
Thus the normalized valuation is at most(K_Y/e_mathfrak p)log B.
This direct division is a notation conversion, not a new project theorem.
The introductory consequence is stated more generally by the source; the present unit deliberately uses only the displayed unit/field hypotheses, so no additional reduction to that greater generality is needed.

## Inspection limits, intended application and search evidence

The source's proof is not re-established here.
The orientation on printed340 describes an auxiliary-function construction with a pigeon-hole step; its correctness and the later optimization of constants were not audited.
The explicit bound is accepted as an established published theorem after checking this exact primary statement and its hypotheses.
No numerical constant has been evaluated, and no effective usable cutoff for the current large alphabet is claimed.

For a project input of the form eta product_j u_j^(m_j)-1, the intended application includes eta as one fixed alpha with exponent1.
Every eta,u_j must actually lie in the selected K, be nonzero mathfrak p-units, and the whole difference must be nonzero.
Passing from such a single-value bound to a coefficientwise residual bound requires a proved evaluation identity and the actual integral divisor and degree costs.
No such application, no uniformity over growing alphabets or changing fields, and no Mahler-gap conclusion is supplied by this source unit alone.
In particular the totally real960 trace field does not contain zeta_3; a project may instead use the full cyclotomic field if it proves the other hypotheses and pays its degree.

The search was triggered by the need to distinguish fixed-alphabet high-precision construction from efficient degree growth.
No matching work or inspected theorem was found in the selected bibliography search for Kunrui Yu, the DOI, or Yu99.
Queries for Yu p-adic logarithmic forms and valuation log B located this1999 published original and the publisher's bibliographic page.
Search stopped after the source statement and exact conventions needed for this question were obtained.
No literature-priority claim or comprehensive erratum survey was made; no concrete contrary evidence was encountered in this bounded search.
There was no native mathematical computation, formal proof check or source-proof review.
