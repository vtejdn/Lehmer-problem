# Independent J106 verification protocol

Prepared by loglog_cyclic_review for Yin under root's explicit assignment.
This is a non-blind independent implementation, with no import of main.py or any author helper.
The complete analytic candidate was prechecked before author execution; its actual fixed [C170 theorem](../../../claims/Yin_C_G0170_v1.md#statement) has the separate [R803 whole analytic finding](../../../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding).
The verifier completed ONE declared mathematical run after the author output and root's explicit go.
The actual main.py and inputs.json public schema were read after preparation, and all count, edge, marginal, component and exact-field adapters are now bound to those native structures.
Execution followed root's explicit go and a fresh authenticated usage gate at 2026-10-18T15:20, with ordinary use allowed in the unchanged weekly window.

The exact domain is the six cases n=5,6,7,8,9,10, b=2 and P=1-t-t^2-t^3+t^4.
All calculations are exact integers or rational coordinates in Q(u), with u=(1-sqrt(13))/2 and u^2=u+3.
No numerical eigensolver or lower-gap claim is involved.

The independent program uses these methods:

- Full descending monic polynomial division for coefficient reduction.
- Original c_l tables for every l=0,...,10 reconstructed as the autocorrelation of fair BINARY endpoint multiplicities, not the author's ternary weighted recurrence.
- Carry edges generated from the RIGHT endpoint through a=-beta^k(theta+beta^4 c), with all 81 middle words and complete original weights.
- Midpoint marks reconstructed from the RIGHT half as theta_2+theta_3 beta+beta^2 c.
- Graph components reconstructed by traversal of the complete weighted edge support; every component's original mass, mean and second moment is checked, independently of numeric component labels.
- Complete half-word masses and midpoint moments obtained with the exact reciprocal map Jx=beta^-1 iota(x).
- For n=5, direct enumeration of ALL 3^10 original ternary words, direct return reduction and right-half evaluation, with conditional moments grouped by COMPLETE left and right tail WORDS.

Every complete author count table, endpoint coordinate, edge weight, middle word, algebraic mark, marginal, component, mass and reported moment/energy/Rayleigh value is a verification target.
The full n=5 direct-word edge table and both conditional-variance contributions are separately checked.
No author output is treated as its own correctness oracle.

Before execution the verifier declares an aggregate wall-time cap of 60 seconds, a worker-memory cap of 512 MiB and a native-verifier-output cap of 64 MiB.
There is no automatic retry, input reduction, approximate box or cap escalation.
A parent process starts a worker waiting for an explicit resource handshake, places it in a Windows Job Object with hard process/job commit limits and kill-on-close, separately enforces the process working-set maximum, and enforces the aggregate timeout.
The verifier explicitly enables and reads back the hard working-set maximum before the handshake, using the independently read primary [Microsoft API contract](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsizeex).
The worker also checks its peak working set and private usage, its deadline and cumulative output size during construction and before each publication.
The small parent resource monitor is excluded from the declared worker-memory cap, as it is in the author protocol; it performs no mathematical reconstruction.
If the resource wrapper is unavailable, execution fails without an unguarded fallback.
On failure the completed-case files remain, while the aggregate states incomplete and lists only cases reported by that actual worker.
Stale files from a previous invocation are not evidence that the new invocation completed them.
The default invocation refuses a nonempty verifier output directory, so no implicit retry or output overwrite occurs.

The default author inputs are this group's author/counts.json and case_n05.json through case_n10.json in mathematics/computations/outputs/Yin_J_G0106/.
Independent outputs use that same group's verifier/ directory.
Programs and inputs resolve relative to the native J directory, independently of the caller's working directory.
The executed command was `python mathematics/computations/programs/Yin_J_G0106/verify.py` from the repository root.

## Actual complete verification

The aggregate verification (`mathematics/computations/outputs/Yin_J_G0106/verifier/verification.json`) and execution record (`mathematics/computations/outputs/Yin_J_G0106/verifier/execution.json`) show all six completed cases and exact agreement on the entire declared mathematical payload.
The independent count tables and six case files are in the same verifier output directory.
The case edge counts are 29,75,95,141,247,331, and the component counts are 3,3,3,1,1,1 in increasing n order.
All 405972 candidate lookups, complete half-word checks and component marks agree with the author implementation.
Direct n=5 enumeration inspected all 59049 original words, found 29 returned words and total original integer weight 1532, and independently matched the edge table, midpoint moment and full-tail conditional energy.
No theorem about untested lengths was inferred.

The single verifier mathematical run used parent wall time 1.3468295 seconds and worker time 1.1420618 seconds.
Peak worker and job commit were 26976256 and 28250112 bytes; complete verifier output occupies 457282 bytes.
The unchanged 60-second, 512-MiB-worker and 64-MiB-output limits were all respected.
The author's earlier WinError1314 occurred before worker creation and did not execute mathematics.
Root corrected only the redundant Job Object working-set flag, retained both commit limits and the separately enforced/read-back hard working-set maximum, and checked an idle child before either successful mathematical run.
This verifier used that corrected guard and had no failed or repeated mathematical invocation.
The complete initial failure and equivalent-cap correction are retained in the J README.

Both implementations share standard Python integer/Fraction arithmetic and the same Windows host.
The author source/schema and completion notice were available before the non-blind verifier run; no author mathematical helper was imported.
The independent count, reduction, edge orientation, midpoint orientation, component traversal and direct-word paths supply the actual reconstruction evidence.

Exact finite agreement can certify only the declared six graphs and marks.
It cannot prove eventual connectivity, uniform carry contraction, asymptotic midpoint growth, finite or infinite critical mean, or a Mahler gap.
