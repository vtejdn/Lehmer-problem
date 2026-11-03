---
author: Yin
---
# RY26-U001: the exterior-root expense of the changing-trace construction

Date: 2026-10-18T13:06.
Human record author Yin.
Root supplied the Roy--Yatsyna primary-source lead and the bounded-measure/coherence question.
The entropy_attainment_bridge AI inspected the actual source and supplies the direct exterior-root calculation and applicability screen below.
No numerical program or mathematical scan is used.

<a id="ry26-u001"></a>
## Read; exact construction formulas and direct measure screen checked

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Subham Roy and Pavlo Yatsyna, The Minimal Degree of Salem Numbers with Negative Trace, arXiv:2608.00778v1,1August2026; 27 pages, printed and PDF page numbers equal.

Passages: Definition(1.1), Theorems1.1 and1.3 on page2; Proposition2.1 and equations(3.1)--(3.5) on page5; Lemmas3.5--3.7 and equations(3.11)--(3.16) on pages8--10; Theorem5.1 on page14; Section7, equations(7.1)--(7.3) and the degree/trace account on pages23--24.

Inspection: Direct primary-PDF text reading at these locators and visual checks of pages5,9,23. The construction equations, positive real-root specialization and local two-sided root bound below were checked. No complete audit of the torsion-coset, prime-counting, cyclotomic-counting or global existence/degree-bound proofs.


The [actual v1 PDF](../../../literature/pdf/RY26--arxiv-v1.pdf) is retained under.
The official explicit-version download supplied the inspected article; no inference from a search-result abstract substitutes for it.

### Scope of the advertised degree statements

The paper defines D(T) as the MINIMUM degree over Salem numbers with trace AT MOST -T, not necessarily exactly -T.
Theorem1.1 states, for sufficiently large positive integer T,

    2T^2/[16log(2T)+11]<=D(T)<=2(1+o(1))T^2log T.

Theorem5.1 states that, for sufficiently large odd n, one of its constructed Salem numbers has trace -floor(n/2)+o(n) and degree at most n(n+2)(log n+log log n).
Theorem1.3 instead fixes any odd n>=10^4 and gives Salem numbers of EXACT trace -floor(n/2) in every sufficiently large even degree.
Those distinctions are consequential to the current application.
These are inspected source statements; this unit does not upgrade their complete proofs to project-audited results.
The exclusion below requires only the displayed construction equations, so it does not depend on accepting the new asymptotic degree theorems.

<a id="prime-paired-construction-formula"></a>
### The Section3 construction and its actual factor accounting

Let n be odd, let p_1,...,p_n be the first n rational primes, and write H for the paper's specialization exponent M, to keep it separate from multiplicative Mahler measure.
For the Salem-factor construction the source takes H>p_n and gcd(H,p_n)=1.
Its equations(3.1)--(3.2) define

    R_n(x,x^H)=x-x^-1
       -sum_(j=1)^((n-1)/2)
          (x^(p_(2j-1)+p_(2j))-1)
           /[(x^p_(2j-1)-1)(x^p_(2j)-1)]
       -(x^(p_n+H)-1)/[(x^p_n-1)(x^H-1)],
    P_n(x,x^H)=R_n(x,x^H) x(x^H-1)
                  product_(i=1)^n(x^p_i-1)/(x-1)^(n-1).

The resulting integer polynomial has

    D_raw=H+3+sum_i p_i-n,
    trace(P_n)=-floor(n/2)+1.                      (1)

Lemma3.5 removes the explicit cyclotomic product

    E_(n,H)(x)=(x-1)product_(p|H,p<=p_(n-1))Phi_p(x),
    P_n=E_(n,H) Q_n.

This is only an initial removal, not the full cyclotomic factorization.
Its degree cost is e=1+sum_(p|H,p<=p_(n-1))(p-1).
Lemma3.6 gives trace(Q_n)=-floor(n/2)+omega_n^*(H), where omega_n^*(H) is the number of prime divisors of H among p_1,...,p_(n-1).
The source defines it separately as0 when H is prime; under H>p_n this agrees with that count.
Lemma3.7 states that Q_n consists of the actual Salem minimal polynomial S_tau and further cyclotomic factors, with each further cyclotomic multiplicity at most2.
Thus, writing the complete remaining product as product_s Phi_s^(v_s), the actual irreducible degree and trace are

    d_tau=D_raw-e-sum_s v_s phi(s),
    trace(tau)=-floor(n/2)+omega_n^*(H)
                         -sum_s v_s mu(s).         (2)

Here phi is Euler's totient and mu is the Mobius function.
No explicit complete list of the remaining v_s is claimed by this unit.
The paper's global selection/counting argument is what controls their aggregate trace effect in Theorem5.1.
Neither D_raw nor deg Q_n may be silently substituted for d_tau in a projection normalized at N=2d_tau.

<a id="exterior-root-measure-expense"></a>
### The decisive direct bound, independent of cyclotomic removal

For x>1 and positive integers a,b,

    (x^(a+b)-1)/[(x^a-1)(x^b-1)]
       =(1/2)[(x^a+1)/(x^a-1)+(x^b+1)/(x^b-1)].   (3)

This identity follows by bringing the right side to a common denominator.
Any exterior root tau>1 of P_n therefore satisfies

    tau-tau^-1
       =(1/2)sum_(k in {p_1,...,p_n,H})
                       (tau^k+1)/(tau^k-1).        (4)

All denominators are nonzero and positive.
Set c=(n+1)/2.
Every summand in (4) is strictly greater than1 and at most (tau+1)/(tau-1), since every exponent is at least1.
Consequently

    tau-tau^-1>c,
    tau-tau^-1<=c(tau+1)/(tau-1),
    tau+tau^-1<=c+2.

The last line follows by cancelling tau+1 in the second inequality and expanding (tau-1)^2/tau.
In particular,

    c<tau<c+2,
    asinh(c/2)<log tau<log(c+2).                   (5)

For any genuine Salem minimal factor containing tau, its complete total logarithmic Mahler measure is exactly log tau.
Removing ANY cyclotomic factors preserves tau and that total measure.
Hence along this construction with n tending to infinity,

    log M(S_tau)=log n+O(1) -> infinity.            (6)

This is a statement about this construction, not a lower bound for every Salem number with the same trace.
Its degree improvement cannot turn the changing-n family into a bounded-TOTAL-measure family; small absolute height log(tau)/d_tau is a different quantity.

### Section7 has the same expense, including its fixed-trace limit

Equation(7.1) uses

    h(x,x_0,...,x_n)=2(x^2-1)product_(i=0)^n(x_i-1)
              -x sum_(j=0)^n(x_j+1)product_(i!=j)(x_i-1).

At the source's positive exponent choices x_i=x^(ell_i), the asserted irreducible construction is

    h(x,x^ell_0,...,x^ell_n)=2(x-1)^n S_(tau,n)(x),
    d_tau=2+sum_(i=0)^n ell_i-n,
    trace(tau)=-(n-1)/2.                           (7)

The source fixes its explicit even killer exponent ell_0 and takes the remaining ell_i as distinct primes coprime to it; its subsequent prime-representation argument varies them to obtain all sufficiently large even d_tau for each fixed odd n>=10^4.
The complete prime-representation and old irreducibility arguments are not audited here.
Dividing the displayed h identity at tau>1 gives exactly (4), now with exponent list ell_0,...,ell_n.
Thus (5) holds independently of their size and independently of the asserted full irreducibility theorem.
Putting T=(n-1)/2 gives

    T+1<tau<T+3,
    asinh((T+1)/2)<log tau<log(T+3).               (8)

Unbounded negative trace therefore forces unbounded total measure in this Section7 construction as well.
For FIXED n, the source's Theorem1.3 instead asserts a genuine family of unbounded degrees and bounded measure in the interval(5), while its exponent data vary.
That is a fixed-trace family with large fixed exterior scale, not a changing-trace bounded-measure family or a near-one construction.
This distinction remains even if the global existence theorem is accepted as an external input.

<a id="trace-and-coherence-comparison"></a>
### Exact reuse and the first-moment limit

The earlier [MS05 source account](../MS05/readme.md) and [C_G8 measure screen](../../../claims/Yin_C_G0008_v1.md#arbitrary-trace-construction-measure-screen) already retain the same lower-bound mechanism for the original arbitrary-trace construction.
The local source key MS05 identifies the2005 all-traces paper with a2004 manuscript; MS04 is the different trace-minus-two paper cited by Roy--Yatsyna.
Thus the present screen matches the new explicit formulas to an existing obstruction; it does not claim a newly discovered trace barrier.
The upper estimate in (5) records the additional fixed-trace bounded-measure boundary directly.

For a genuine Salem tau of actual degree d, define its FULL phase measure by projecting all conjugates radially to the unit circle, including the two positive real roots with phase1.
Its first Fourier moment is exactly

    nuhat(1)=[trace(tau)-tau-tau^-1+2]/d.           (9)

For the fixed-n Section7 family, (5), (7) and (9) give nuhat(1)=O_n(1/d), which tends to0.
The unnormalized trace is not a Fourier coefficient of the actual C158 projection kernel.
No implication forcing divergence of the actual kappa follows here from (9).
In particular this unit does not claim a bounded or unbounded projection coherence for the varying exponent choices in (7).

The accepted [C_G160 fixed Perron-seed bound](../../../claims/Yin_C_G0160_v1.md#statement) concerns its specific seed t^3-t-1, complete cyclotomic table and actual window N=2d, with multiplicative measure less than4/3 and uniformly bounded kappa.
It does not cover the different Section7 exponent family by name alone.
Conversely, [C_G143](../../../claims/Yin_C_G0143_v1.md#statement) already gives growing actual coherence on a different construction with unbounded measure.
Coherence growth on the changing-n branch here would likewise not answer the bounded-measure question.
A proved divergence on the FIXED-n exponent family would address a different bounded-measure class, albeit at a large fixed measure; it would not automatically enter a near-one class, and no such divergence has been proved here.
The [C_G158 definition](../../../claims/Yin_C_G0158_v1.md#statement) keeps kappa as an aggregate of ALL nonzero projection diagonal sums in the actual2d window; one raw trace coefficient is not that aggregate.

The bounded inquiry finds no changing-trace bounded-total-measure family, no verified coherence growth, and no reason to run a polynomial or Gram scan on this lead.
The exact unresolved alternative is a different construction with controlled exterior root while the relevant arithmetic complexity changes, or a proved actual-projection estimate on a specified bounded-measure family.
No new Claim, Task/strategy decision, original Mahler gap, counterexample or novelty assertion is made.

<a id="original-moving-exponent-author-and-reviewer-readings"></a>
## Distinct original fixed-trace feasibility readings

Retained 2026-10-22T01:16.
After the earlier exterior-root screen above, the entropy_attainment_bridge author of L402 again text-read retained arXiv2608.00778v1 printed/PDF pages23--25, including the individual construction, Proposition7.1, its use in Theorem1.3 and the first counting-lemma passages, and visually checked page23.
The separate R547 angular_envelope_review agent text-read pages23--24 and visually checked page23.
These are distinct actual source-reading occurrences, not one merged primary inspection or a full counting/Vinogradov/global Theorem1.3 proof audit.
The four-exponent equation7.2 and exact2(x-1)^3 removal apply to the individual n3 construction; n>=10^4 belongs to the every-large-degree representation theorem, which the local schedule does not use.
Their individual original reading minutes are unknown;21:06 is the earlier source-unit document,21:55 the L402 document and22:10 the R547 whole completion, not reconstructed reading minutes.
The original v1 edition, holding account and uninspected proof boundaries remain unchanged.
Current maintenance reads these sufficient retained facts without another PDF/source passage, acquisition, numerical prime evaluation or new original-proof review.
