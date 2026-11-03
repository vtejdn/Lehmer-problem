---
author: Yin
---

# Exact two-prime remainder and quartic parameter elimination

## Question and scope

For original monic irreducible reciprocal nontorsion integer units, test P dividing 9P(t^2)^3-8P(t^3)^2.
The actual finite scope consists of nine fixed polynomials and the full symbolic trace quadratic T=x^2-Ax+B.
[C148](../../../claims/Yin_C_G0148_v1.md#quartic-exact-classification) owns the projection, specialization, exceptional-branch and original-domain argument.
No numerical roots, additional degree or coefficient-box search is used.

## Files and reproduction

[main.py](main.py) uses exact SymPy polynomial arithmetic to retain both remainder coefficients, their gcd, both elimination resultants and full factorizations, every specialized branch and every resulting original quartic.
[verify.py](verify.py) independently reconstructs the quotient with pairs in Z[A,B][x]/(x^2-Ax+B), rather than author composition/division.
The existing repository Python environment supplies the required SymPy dependency.
Each command has a live 180-second subprocess limit and atomically publishes its completed mathematical payload.

```powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0096/main.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0096/verify.py
```

The author has no generated input dependency.
The verifier requires the author's results.json (`mathematics/computations/outputs/Yin_J_G0096/results.json`) and writes verification.json (`mathematics/computations/outputs/Yin_J_G0096/verification.json`).
Default paths resolve from the actual program location, independently of the caller's working directory.

## Results and limits

The author calculation completed on 2026-10-15.
All nine controls completed; only Phi5, Phi7 and (t-1)^2 had zero remainder.
Both symbolic elimination resultants are nonzero and have degree 66.
The complete integral trace-quadratic solutions are (-1,-1), (0,-4), (1,-2) and (4,4), with no surviving whole parameter line.
Their original quartics are Phi5, (t^2-1)^2, (t-1)^2 Phi3 and (t-1)^4.
All are torsion or reducible, so none is an admissible nontorsion counterexample.
The A=0 vertical specialization remains a nonzero polynomial and is included in the complete branch check.

## Independent native verification

Root was a noncontributor to the new trace/cusp, degree-two and elimination arguments supplied by g_bridge_audit.
Its separately implemented verifier uses quotient-pair multiplication, rational factorization and irreducibility checks, all specialized gcds, and independent monic long reduction/modular multiplication on the nine controls and four candidates.
The author's saved coefficients are comparison values, not generators for the new reconstruction.
Those distinct implementation and execution facts do not establish the initial substantive-context isolation.
The current R365 whole analytic/native finding has an unknown relationship; the original date, algorithms, exact output comparisons and shared-SymPy limitation remain unchanged.

<a id="independent-native-result"></a>
## Actual independent verification result

The separate verification completed on 2026-10-15 and matched both full coefficient polynomials, gcd, both resultants and all factor products, all four integer pairs, every exceptional-branch check and all thirteen original polynomial remainders/factorizations.
Both implementations share SymPy's exact polynomial kernels; this is an independent implementation and run, not an independent CAS or formal proof.
[Whole R365](../../../audits/reviews/Yin_R_G0365_v1.md#trace-cusp-quartic-whole-independent-finding) and [C148's selected decision](../../../claims/Yin_C_G0148_v1.md#decision-whole-reviewed-2026-10-15) retain the actual mathematical scope.
The historical independent headings identify the original native account; they do not certify the current unknown review relationship, and this clarification performs no new run.
A zero remainder for a torsion/reducible control is not a counterexample, and finitely many nonzero remainders do not prove the general problem.
Higher-degree nonvanishing and a controlled original coefficient/Archimedean-cost transfer remain open.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
