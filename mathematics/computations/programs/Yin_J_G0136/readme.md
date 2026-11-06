---
author: Yin
---

# Bounded integer Hermitian-square autocorrelation enumeration

Context: [G0001](../../../tasks/Yin_T_G0001_v1.md#contract) and the [L133 v8 integral-square control](../../../ledger/Yin_L_G0133_v8.md#positive-polynomial-integer-sos-control).
This group retains two actual exploratory Python stdin calculations by the witt_moment_compatibility delegate and their native reproduction.
The coordinating agent requested retention after the bounded report.
These are ordinary author computations, not independent review or evidence for a general SOS theorem.

## Question and arithmetic

The first calculation tests two integer polynomial squares of degree at most two whose total autocorrelation is (6,2,2), namely the doubled p4 control.
Every coefficient is enumerated in -2,...,2 and each nonzero row has squared coefficient energy at most six.
These bounds exhaust the stated two-square problem because its total energy is six.
All coefficient products, autocorrelations, differences and lookups are exact Python integers.

The second calculation takes d in (3,4,5), constant Laurent coefficient three, highest positive coefficient one and each intervening positive coefficient in -2,...,2.
It generates all integer autocorrelations of rows of length d+1 with energy one through six, then all sums with total energy six by exact integer dynamic programming.
Separately, NumPy Chebyshev derivative roots provide a floating-point positivity screen: accept nearly real critical points with imaginary part smaller than 1e-8 and real part strictly between -1 and 1; evaluate those points and both endpoints; keep a candidate only if the computed minimum exceeds 1e-8.
This numerical screen has no interval or exact-root certificate.
It neither classifies strictly positive inputs nor proves a universal representation statement.

## Native files and reproduction

The native files [original_p4_pairs.py](original_p4_pairs.py) and [original_small_scan.py](original_small_scan.py) preserve the actual executed Python bodies, without the PowerShell stdin wrapper.
The [replay.py](replay.py) wrapper reruns both bodies and stores their mathematical output and the Python/NumPy versions in the group's ignored output home.
From the repository root run `python mathematics/computations/programs/Yin_J_G0136/replay.py`.
The generated result is [results.json](../../outputs/Yin_J_G0136/results.json), at `mathematics/computations/outputs/Yin_J_G0136/results.json`.
No external input file, randomness, seed or preceding generated output is required.
The first calculation needs only the Python standard library; the second uses NumPy.
The observed environment was Python 3.14.3 and NumPy 2.4.4.

## Results and limits

The original first run returned no two-row pair, count zero.
The second returned 119, 329 and 799 exact energy-six autocorrelation states for d=3,4,5 respectively.
The floating screen selected 3,5,4 inputs respectively, with no failure among the selected inputs.
The final no-failure observation is only an exploratory screen outcome, not a rigorous positivity classification or coverage theorem.
The subsequent p4 minimum-rank proof and the finite coefficient-energy criterion are mathematical deductions; neither depends on this floating screen.
The complete author arguments are in the [C868 v6 candidate](../../../claims/Yin_C_G0868_v6.md#doubled-quartic-minimum-rank), whose assessment remains with that Claim.
The original runs wrote no files; the retained native bodies and the replay produce reproducible current output rather than claiming to recover historical output bytes.

The isolated computation review recorded in [R1091 v6](../../../audits/reviews/Yin_R_G1091_v6.md#integral-reflection-whole-proof-finding) read these native bodies and ran both stdout-only originals, reproducing the recorded results.
That check preserves the floating screen's exploratory scope and does not make the outputs proof inputs or establish a general SOS theorem.
