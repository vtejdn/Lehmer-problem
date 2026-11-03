# Exact finite comparison certificates

This attachment accompanies the progress report's finite comparison of monomial auxiliary polynomials with an enlarged family of unit directions.
It contains [the complete exact input and witnesses](certificates.json) and [a standalone verifier](verify.py).
Both files can be copied to any directory and used without the research repository.
The verifier uses Python 3.9 or later and only its standard library.

| Report reference (TeX label) | Verification supplied here |
| --- | --- |
| Proposition 5.9, `ar:finite-certificate` | Complete original coefficient identities, energies and signed correlations; primal and dual feasibility; matched objectives; original integer realization. The real-weight weak-duality argument is stated below and in the script. |
| Proposition 5.11 and Table 2, `ar:unit-optima` and `ar:unit-comparison` | All five rational optimum intervals, both strict improvements, the full finite selector and the sixth feasible primal with its rejected dual. |
| Equation (5.18), `ar:unit-exact-domain` | Original full unit norms, energies and masses used by the exact true-surplus normalization. |

## Run

With the two files in the same directory, run:

```text
python verify.py
```

The data path is resolved relative to the script, so the current working directory does not matter.
No package installation, network access, optimizer, saved numerical solver state or external source file is required.
The program reads the data and prints its conclusions; it writes no files.
A failed check raises an exception and returns a nonzero exit code.
Checks remain enabled under `python -O`.

The attachment was run successfully on 11 October 2026 with Python 3.12.14.
That run checked all three inputs, all 304 supplied source columns and all six exact witnesses.
The coordinator also copied only the script and JSON to a fresh isolated directory and successfully ran `python -I verify.py` there; the disposable copy was then removed.
Five witnesses certify finite-family optima.
The sixth passes primal feasibility and is rejected as a dual certificate, as required.
The earlier numerical solver's reported tableau inconsistency is a historical observation discussed in the report; the floating tableau is neither supplied nor rechecked here.

For the strategy-structured report, the same unchanged verifier and data were rerun successfully with the same 304-column, five-optimum, two-improvement and rejected-sixth-dual conclusions.
The current proposition, equation and table numbers above were checked against the rebuilt report.
The earlier isolated-relocation test was not repeated.

## Inputs and the exact finite domain

All polynomial coefficient arrays use ascending powers of $t$, with their full indicated window retained.
The inputs are

\[
 P_{10}(t)=t^{10}+t^9-t^7-t^6-t^5-t^4-t^3+t+1
\]

and, for $n=18,30$, the degree-$(n+2)$ polynomials

\[
 P_{n+2}(t)=\frac{t^n(t^3-t-1)+1-t^2-t^3}{1+t}.
\]

The verifier checks these polynomial identities from their integer coefficients.
It does not reprove their irreducibility or classify their roots.
Every norm calculation uses the full original degree, and does not select expanding roots or pass to a trace polynomial.

| Input | Degree $d$ | Window $N=2d$ | Original denominator $q$ | Source columns | Monomials | Admitted additional columns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| $P_{10}$ | 10 | 20 | 26487 | 48 | 20 | 19 |
| $P_{20}$ | 20 | 40 | 36887312 | 98 | 40 | 23 |
| $P_{32}$ | 32 | 64 | 257188436220 | 158 | 64 | 41 |

For every one of these 304 source columns, the data contain complete integer coefficient vectors $B,F,U$, the signed norm of $B$, and the content of the original $F$.
The script verifies

\[
 F=qB-PU,\qquad
 \langle F,t^kP\rangle=0\quad(0\le k<d),
\]

where the inner product is the usual coefficient inner product in the $N$-term window.
Thus $F/q$ is the orthogonal residual of $B$ modulo the span of $P,tP,\ldots,t^{d-1}P$.
Each signed norm is independently recomputed as the determinant of multiplication by $B$ on $\mathbb Q[t]/(P)$.
Integer polynomial reduction and fraction-free elimination perform this check; the data do not supply a matrix whose correctness the reader must assume.

The first $N$ columns are checked to be exactly $B=t^j$, $0\le j<N$.
Their energies sum to $d$; consequently the common monomial masses $v_j=1/d$ have energy 1 and total mass 2.
Every energy and every positive-lag signed correlation is reconstructed by multiplying $F(t)$ by $t^{N-1}F(t^{-1})$.
The enlarged family retains exactly the source columns with

\[
 |\operatorname{Res}(P,B)|=1,
 \qquad e=\|F\|_2^2/q^2\le1.
\]

All rejected source columns remain in the attachment, so the full filter is checked including the equality boundary.
The list is finite and selected.
It is not a complete enumeration of the units in $\mathbb Z[t]/(P)$ or of the integer points in an energy ellipsoid.
Column indices in the attachment are zero-based positions in this explicitly supplied list.

## What proves optimality

For a chosen finite family, put

\[
 e_j=\|F_j\|_2^2/q^2,
 \qquad H_{\ell j}=q^{-2}\sum_i F_{j,i}F_{j,i+\ell}
 \quad(1\le\ell<N).
\]

The problem is to minimize $\kappa=2\|Hv\|_1$ over real masses satisfying

\[
 v_j\ge0,\qquad e\cdot v=1,\qquad S:=\sum_jv_j\ge2.
\]

Since each admitted seed has absolute norm 1, $F=qB\pmod P$ gives $|\operatorname{Res}(P,F)|=q^d$.
The normalized weights $w=v/S$ therefore have energy $E=q^2/S$, arithmetic income $I=\log q$, and true surplus $\eta=I-\frac12\log E=\frac12\log S$.
Conversely any normalized real weights with surplus at least $\frac12\log2$ give such a feasible $v$.
The finite linear constraints therefore impose the actual stated surplus target, without a logarithmic approximation or additional norm income.

The dual data consist of $y,\lambda,\mu$, and the script checks every constraint

\[
 |y_\ell|\le1,\quad \mu\ge0,
 \quad 2H^Ty-\lambda e-\mu\mathbf1\ge0.
\]

For every real primal feasible vector,

\[
 2\|Hv\|_1\ge2y\cdot Hv
 \ge\lambda(e\cdot v)+\mu S
 \ge\lambda+2\mu.
\]

An exactly equal feasible primal value proves global optimality over all real weights on this finite family.
The attachment uses the complete original columns and masses, so no compression is a premise of the check.
It also checks all energy/correlation equalities between mirrored monomial columns.

For the five complete witnesses, the verifier checks the original normalized weights, their least common denominator $M$, the integer multiplicities $m_j=Mw_j$, and every coefficient of

\[
 A(t)=\sum_jm_jF_j(t)t^{N-1}F_j(t^{-1}).
\]

It checks the central coefficient $Mq^2/S$, all lag coefficients $Mq^2(Hv)_\ell/S$, and the full signed arithmetic product, whose absolute value is $q^{dM}$.
The latter is retained exactly as a base and exponent, without expanding an enormous integer.
The original contents remain in $F_j$; no primitive rescaling is performed.
The full window gives the radial multiplier $(N-1)/d$, namely $19/10,39/20,63/32$ on the total logarithmic Mahler measure.

## Results and the retained rejection

All displayed interval endpoints are checked by rational arithmetic.
All five optimum witnesses have $S=2$, hence surplus exactly $\frac12\log2$.

| Input and family | Original columns | Exact conclusion |
| --- | ---: | --- |
| $P_{10}$, monomials | 20 | Optimum in $[3.0845,3.0846)$ |
| $P_{10}$, enlarged | 39 | Optimum in $[3.0617,3.0618)$; strict improvement |
| $P_{20}$, monomials | 40 | Optimum in $[4.0386,4.0387)$ |
| $P_{20}$, enlarged | 63 | Optimum in $[4.0185,4.0186)$; strict improvement |
| $P_{32}$, monomials | 64 | Optimum in $[4.6211,4.6212)$ |
| $P_{32}$, enlarged | 105 | Feasible primal; dual rejected at lag 9 |

The last witness has nonnegative primal masses, energy 1 and $S=2$.
Its dual multiplier and all column slacks are nonnegative, and its algebraic primal/dual objective gap is zero.
Nevertheless $y_9>1$, so it supplies no optimum certificate.
The verifier confirms that lag 9 is its only box violation.
Unreached normalized weights, multiplicities and aggregate fields for this last witness remain absent from the data.
Its feasible primal value is only an upper bound; no equality to the monomial optimum and no absence of improvement is inferred.

The last two output lines are:

```text
PASS: 304 source columns; 5 exact finite-family optima; 2 strict improvements; sixth feasible primal with rejected dual.
Not checked here: irreducibility/root classification, historical floating tableaus, candidate discovery, all-unit or varying-input claims.
```

## Data format and implementation scope

`certificates.json` uses integer JSON numbers and rational pairs `[numerator, denominator]`.
Denominators are positive and fractions are reduced; Python reads integers without a floating conversion.
The `inputs` array contains the complete original polynomial data and column lists.
`enlarged_indices` is checked against the selector computed from those columns.
The `certificates` array contains, in order, the baseline and enlarged witnesses for each input.
Each certificate gives the full original column indices, primal masses, dual variables and claimed objective.
Complete certificates additionally carry the exact integer realization; the last certificate explicitly records `invalid-dual` and its rejected lag.

The verifier is an independent implementation of the displayed identities and weak-duality argument, written for this attachment.
It imports no research checker, candidate generator or optimizer.
It checks the finite mathematical witnesses rather than reproducing how their candidates were discovered.
A passing run does not certify numerical solver stability, an optimum over all units, varying-input bounds, or a positive universal Mahler gap.
The report's analytic arguments and literature dependencies have their separate mathematical scope.
