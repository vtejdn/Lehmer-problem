---
author: Yin
---
# All sixteen divided whole-order classes for the normalized unit gate

Human author Yin.
The same_trace contributor authored this exact extension while C608/J119 were fixed for separate review; those inputs and outputs are not edited.

## Question and scope

For every odd n divisible by5, B_n is the complete nonidentity n-th-root trace polynomial and phi=X^2+X+1 divides it exactly once.
Put D_n=B_n/phi, M=X^4 phi^8 and M_tilde=X^4 phi^9.
Does the explicit character `lambda(u)=[X^13](u'/u)+[X^15](u'/u)` vanish on all D_n?
The proved predivision period is160 in n, so the exact complete finite range is n=5,15,...,155, with no order or degree cutoff.
The target is one16-row certificate and its verification; no group enumeration, coefficient search or original-input construction is included.
The complete analytical implication and original-input boundary are fixed in [C609](../../../claims/Yin_C_G0609_v1.md#argument), currently an open candidate awaiting separate review.
The substantive [C609v2 analytic proof](../../../claims/Yin_C_G0609_v2.md#argument) preserves that first proof and removes the16-row premise from its all5-order step; this group's unchanged computation is corroboration for v2.

## Mathematical reduction

The recurrence matrix A=[[X,1],[1,0]] has A^5-I divisible byphi and A^8-I divisible byX^4.
Hence A^80=I moduloM_tilde, which yields B_(n+160)=B_n moduloM_tilde.
Divide the exact polynomial congruence byphi before reducing moduloM: D_(n+160)=D_n moduloM.
No differentiation or illegal inverse ofphi is taken in the predivision ring.
For odd n, the n-th roots are distinct and phi is the complete order5 factor, so each D_n is prime toX phi and is a unit moduloM.
The low-X effect of dividing byphi is retained in the same full ringM, rather than discarded in a phi-primary projection.

The finite rows cover every D_n by this period.
Together with the separately fixed coprime5 character certificate, the exact divisor identity D_n=product_(d|n,d>1,d!=5)W_d proves by induction that the character vanishes on every complete odd-order group W_d other than1 and5.
Both full normalized A_0=2 target classes have character1, so the proposed implication is a complete support contradiction on that branch, conditional on the complete proof and review.
No statement about another normalized A_0, multiple unsaturated factors or the unrestricted Lehmer question follows.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Bit-polynomial recurrence modulo the full predivision modulus, exact division, inverses and16 separating-character rows. |
| [verify.py](verify.py) | Separate coefficient-set arithmetic, exact division and multiplication linear systems for every row and the matrix period. |
| [independent_c630_v2.py](independent_c630_v2.py) | Isolated reviewer's dense-coefficient arithmetic, direct symmetric Laurent reconstruction, all32 C608 premise rows, both targets and all16 J120 corroborating rows. |
| certificate.json (`mathematics/computations/outputs/Yin_J_G0120/certificate.json`) | Generated16-row polynomial certificate and exact order25 row. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0120/verification.json`) | Generated verification result for the complete mathematical payload. |
| independent_c630_v2_verification.json (`mathematics/computations/outputs/Yin_J_G0120/independent_c630_v2_verification.json`) | Generated independent arithmetic checks at the precise C609v2 input and corroboration scopes. |

The elementary arithmetic kernels of main.py and verify.py are copied into this new group from the same author's J119 implementations; those programs do not import or alter J119.
Generated output uses the ignored output directory of this actual J identity.

## Reproduction

Only standard-library exact polynomial arithmetic overF_2 is used.
Generation requires no previous outputs or cross-J generated input.
The verifier consumes this group's certificate and reconstructs all16 rows with coefficient sets and multiplication linear systems.
Both implementations are author work, not independent agent review.

Run from the repository root:

```text
python mathematics/computations/programs/Yin_J_G0120/main.py
python mathematics/computations/programs/Yin_J_G0120/verify.py
```

The generator creates its output directory when absent; the verifier requires the preceding generated certificate.
Optional --output and --input arguments select explicit files; ordinary reproduction uses the defaults derived from the actual containing J identity.
The two generated files can be coherently replaced by this sequence.

The isolated reviewer's additional command is:

```text
python mathematics/computations/programs/Yin_J_G0120/independent_c630_v2.py
```

This command reads this group's generated certificate and the exact32-row table in [C608's fixed argument](../../../claims/Yin_C_G0608_v1.md#argument).
It imports neither author program and needs no J119 generated output.
It writes only its distinct independent verification output in this J's output home.

## Results and limits

Both native programs completed successfully.
All16 canonical predivision residues divide byphi with zero remainder; every resulting quotient is a unit moduloM and has character0.
The verifier reconstructed A^80=I moduloM_tilde, every quotient and inverse, all16 logarithmic derivatives and the exact order25 identity using its separate arithmetic.
The two source programs and complete output payload were inspected at this precise finite scope.
The all-order interpretation requires the proved160-period, exact simple phi factor and complete divisor induction; it is not an extrapolation from16 arbitrary orders.
The order25 example is included as one exact row, with D_25=phi(C_5 mod2)=Psi.
The supplied ring character and both target values are reused at their precisely fixed scope from C608/J119 without changing those materials.

The isolated C609v2 reviewer reran both author programs and completed the additional independent command successfully.
The independent program reconstructed all32 C608 logical-premise rows and both full-gate target classes, all16 J120 rows including each inverse and logarithmic derivative, the80/160 order periods, the endpoint inverse and the three character-zero chain-rule terms.
For each n=5,15,...,155, it also checked the exact polynomial composition B_n=phi B_(n/5)(chi) and its exact differentiated identity.
Whole-root polynomials were reconstructed directly by triangular inversion of their symmetric Laurent expressions using dense coefficient lists.
The infinite-order composition and truncation argument is mathematical reasoning in C609v2 and its review, not a conclusion inferred solely from these16 compositions.
J120's16 rows remain corroboration for v2; C608's32 rows remain a logical finite input, and accepted C199 interfaces are not recursively re-audited by this program.
The complete new review and its accepted-input limits are retained in [R812](../../../audits/reviews/Yin_R_G0812_v1.md#whole-trace-parity-finding).

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
