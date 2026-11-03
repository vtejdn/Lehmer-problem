---
author: Yin
---
# Fixed-support source scope and the flat first-window surplus limit

Date: 2026-10-20T08:55.
Human author Yin.
This integrated source/applicability account preserves the completed author reading recorded on2026-10-12T12:11 for the fixed-support question.
It reuses the already fixed C27, C62, L19 and DS17-U001 rather than registering their results again.
The present reorganization adds no original-source reading, proof audit, independent review, source acceptance, acquisition or mathematical computation.
The source observations and direct applicability reasoning below retain their original author-checking scope.

<a id="fixed-support-existing-source-reading"></a>
## Completed source reading and its exact limits

The original bounded local screen inspected relevant C/L/U materials, bibliography and registry for sparse/lacunary/few-term, coefficient-count, Schinzel, Lawton and Dobrowolski inputs.
It found [DS17-U001](../audits/literature/DS17/Yin_U001.md#ds17-u001), [L19](Yin_L_G0019_v1.md#cyclotomic-support-escape) and [Smy08-U002](../audits/literature/Smy08/Yin_U002.md#smy08-u002).
The last is a survey report whose original sparse proofs remain uninspected.

The completed2026-10-12 reading directly inspected the existing [DS17 PDF](../literature/pdf/DS17.pdf): title, normalization and Theorem1 on printed/PDFp1; equation(3), H_K and Theorem2 onp2; the historical numerical-bound paragraph onp3; complete Section4 onp5; and reference[13] onp7.
Pages2,3,5 were rendered and visually inspected, including the exponent in the historical numerical bound.
The inspected artifact was Edward Dobrowolski and Chris Smyth, *Mahler measures of polynomials that are sums of a bounded number of monomials*, arXiv:1606.04376v2, version strip23January2017, with a distinct title-page body date17August2016.
The registered publication is International Journal of Number Theory13(2017),no6,1603--1610.
No journal/preprint equivalence audit was performed.
The existing source account and registry were inspected first, without a new acquisition, artifact write or source-version change.

The full multivariable definition and Theorem2 are already adequately retained in DS17-U001.
For each fixed integer K>=1, H_K consists of nonzero integer Laurent polynomials in any finite positive number of variables with at most K nonzero monomials; coefficient heights, exponents, degree and variable count are unrestricted.
The theorem concerns TOTAL logarithmic torus measure m, with M=exp(m), and states that m(H_K) is closed in the nonnegative reals and has isolated zero.
The already accepted univariate consequence is that each fixed K has eta_K>0 and every nonzero integer polynomial with at most K nonzero coefficients has m=0 or m>=eta_K.
No monicity, irreducibility, unit or nonreciprocity condition is needed for that source consequence.
The present consumer uses only this already accepted univariate scope, not an enlarged source acceptance.

The selected Section4 mechanism is also already retained in that unit: on bounded-measure ranges, Corollary2 bounds coefficient height, leaving finitely many coefficient tuples; source reference[13], Smyth's *Closed sets of Mahler measures*, Theorems1--2 supply closedness and isolated zero for each tuple.
Closed tuple sets not containing zero have a neighborhood avoiding zero.
The original reference[13] proofs were not acquired or re-audited in the completed reading.
DS17-U001's actual-single-monomial correction remains applicable: use M(a t^r)=abs(a), not the printed Corollary2 height formula at actual K=1.
The zero polynomial is excluded.
The one-variable zero-measure exception includes signed monomials times cyclotomic products, not merely a single cyclotomic polynomial.
For the actual irreducible nontorsion unit inputs, the usual Kronecker reduction supplies positive m and excludes that branch.

<a id="fixed-support-constants-and-alphabet-boundary"></a>
## Reported numerical history and the coefficient-alphabet distinction

DS17-U001 supplies a positive eta_K for every fixed K, not an adopted numerical value, effective law, monotonicity or positive constant uniform over all K.
No numerical eta_K is required for the application below.

The visually inspected DS17p3 paragraph reports the earlier one-variable estimate attributed to Dobrowolski2006, reference[5], in multiplicative notation:

    M(f)>=1+exp[-a 3^floor((k-2)/4) k^2 log k],
    a<0.785.

This remains a report by DS17, not an adopted numerical premise.
The original2006 paper, its precise noncyclotomic convention and numerical proof were not inspected.
The reported paper is *Mahler's measure of a polynomial in terms of the number of its monomials*, Acta Arith.123(2006),no3,201--231; DS17 references[3],[4] also credit1983 and1991 bounds.
DS17 says the same gap extends to several variables by the Corollary2 argument, but this report is not substituted for the accepted qualitative input.
Further acquisition was unnecessary for the bounded question and did not occur.

A fixed number of nonzero terms, or a fixed finite coefficient tuple with a fixed number of occurrences, meets the fixed-K hypothesis.
A fixed finite alphabet with an unbounded number of occurrences does not.
In particular the alphabet{-1,0,1} with arbitrarily many occurrences lies outside a fixed-K hypothesis; this input supplies no eta_K independent of support size.
The inspected records establish no unrestricted positive gap from that alphabet restriction alone; this is a bounded applicability statement, not a nonexistence or novelty result.

The completed reading also inspected the existing [BDM07 PDF](../literature/pdf/BDM07.pdf), Peter Borwein, Edward Dobrowolski and Michael J.Mossinghoff, *Lehmer's problem for polynomials with odd coefficients*, Annals of Mathematics166(2007),347--366.
Printed347--349/PDF1--3 were text-read for conventions, and printed355/PDF9 was text-read and visually inspected for Corollary3.4 and its displayed proof.
The [earlier BDM07 account](../audits/literature/BDM07/readme.md#classical-certificate) and [L67 attribution](Yin_L_G0067_v1.md#dyadic-log-five-norm-certificate) already preserve the auxiliary-certificate reading.
The additional applicability distinction is that Corollary3.4 assumes degree N-1, EVERY coefficient odd and NO cyclotomic factors, and gives

    m(f)>=(log5)/4 * (1-1/N).

This statement was used at the completed reading's comparison scope, without a re-audit of Theorem3.3 or the whole source proof, and it is not a premise of the C62 coupling.
For an actual irreducible nontorsion polynomial with every coefficient equal to+/-1, N=d+1 and d>=2 give m(P)>=(log5)/6, regardless of reciprocity.
A sparse flat polynomial with an internal zero fails the every-position odd premise.
The bound cannot be applied merely because every NONZERO coefficient is+/-1.
No general finite-alphabet theorem follows.

<a id="fixed-support-existing-c27-escape"></a>
## Reused all-late support escape

[C27 PartB](../claims/Yin_C_G0027_v1.md#statement) already states that every hypothetical sequence of actual flat monic irreducible nontorsion integer-unit minimal polynomials with0<m(P_j)->0 has original support n(P_j)->infinity.
[L19](Yin_L_G0019_v1.md#cyclotomic-support-escape) gives the stronger escape even after optimal cyclotomic completion; completion1 supplies the original support statement.
For each fixed K, eventually m(P_j)<eta_K, so every sufficiently late input has n(P_j)>K.
This is all-late convergence, not just an unbounded subsequence, and needs no monotone or explicit eta_K.
Since n(P_j)<=d_j+1, degree also escapes, without a proportional support/degree bound.
These are reused deductions, not new sparse results.

C27's separate actual coefficient-denominator conclusion retains exact cancellation of the SAME log q in norm income and coefficient cost.
It neither supplies an additional scalar loss nor bounds the distinct final-weight denominator.
Those arithmetic facts are not new premises needed for the support-to-C62 application.

<a id="fixed-support-c62-hypothetical-interface"></a>
## Uniform application to the complete C62 packet class

Use [C62 PartC](../claims/Yin_C_G0062_v1.md#statement) at an actual flat input of original degree d with n>=4.
Its domain contains every finite rational first-window packet in[0,d], with nonzero actual values in O0=Z[alpha], positive normalized rational final weights and aggregate energy E<1.
There is no common bit law, common fractional coefficient, selected norm inventory, covariance or complementarity assumption in this branch.
Writing Lambda for the complete normalized weighted log income from the nonzero signed original norms, C62 gives

    0<S:=Lambda-(1/2)log E
       <=B(n,m):=[log(3n-6)+m]/(n-3)
                         +(1/2)log[n/(n-1)].

For every hypothetical sequence of actual flat inputs with0<m(P_j)->0, the already adopted C27 consequence supplies n_j->infinity and eventually m(P_j)<=1.
Hence eventually n_j>=4 and

    B(n_j,m(P_j))
       <=[log(3n_j-6)+1]/(n_j-3)
                         +(1/2)log[n_j/(n_j-1)] ->0.

For every epsilon>0 there is j0 such that EVERY j>=j0 and EVERY packet in that input's stated C62 domain has S<epsilon.
The bound is uniform over representatives, actual coefficient denominators, all final indexed weights and residue classes.
No optimizer, attainment, packet selection or final-weight denominator bound is assumed.

This directly links two already adopted inputs; it neither constructs nor rules out the hypothetical sequence.
For complementary packets the older C10 inequality already gives S<=m(P_j)->0, as C62 PartD retains with actual width d, all q/final M/copy costs and full signed norms.
C62 PartC additionally treats the noncomplementary E<1 domain and bounded-measure growing-support regimes.
No contradiction follows without a separately justified incompatible positive gain.
Nothing extends to nonflat inputs, overorders, E>=1 or windows wider than d.

<a id="fixed-support-reading-closeout"></a>
## Completed scope and unresolved broader assertions

The fixed-support statement, the actual source-inspection limits, tuple-versus-alphabet distinction, dense-odd comparison and uniform C27--C62 interface settle this bounded applicability question.
The original reading stopped after those existing inputs sufficed; it performed no internet search, new acquisition or mathematical native program.
PDF extraction and the four inspected page renders were reading operations only.
The earlier numerical originals and broader finite-alphabet questions remain outside the inspected or adopted scope.
This author reading/application account supplies no new independent review, no change to the accepted C27/C62/DS17 scopes and no unrestricted G0001 conclusion.
