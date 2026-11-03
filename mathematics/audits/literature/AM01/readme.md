# AM01: coefficient-growth applicability screen

Source: [registered publisher PDF](../../../literature/pdf/AM01.pdf), Amoroso--Mignotte (2001), DOI 10.4064/aa99-1-1.
Coordinator for Yin, 2026-10-09T16:00; self-checked scope comparison, no accepted U input.

<a id="coefficient-growth-screen"></a>
The G0001 question is whether known coefficient bounds remove D G0015's condition log H=o(sqrt(D)).
The bounded search inspected existing G-line coefficient/length results and DS17, then primary-source searches for irreducible coefficient bounds.
The publisher's complete statements on printed/PDF pp.2 and 7 were read and visually checked; underlying Siegel-lemma inputs and the full proof were not audited.
The earlier institutional PDF endpoint returned HTTP 403; the publisher artifact was retained.

For one variable, Theorem 1 bounds log||P||_circle by, for every x>0,

    F_D(x,m)=x log(e(D+1))
             +(1+D/x)[2 log(D+x+1)+(1+x/D)m],

where P is irreducible integral, deg P<=D and m=log M(P).
For D>=2 and m>=0, its displayed right side satisfies

    F_D(x,m)>=log D (x+2D/x)>=2 sqrt(2D) log D.

Thus even optimizing this particular displayed bound cannot certify o(sqrt(D)).
This is a limitation of that estimate, not a lower bound on actual coefficients.
Corollary 1 at n=1 likewise gives only O(sqrt(D) log D) for bounded m.
No near-one coefficient-growth theorem is adopted.
