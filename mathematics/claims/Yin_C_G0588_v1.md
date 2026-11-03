---
author: Yin
---

# Complete actual selected trace transforms, radical selection and paid boundary costs

This common actual selected-edge object retains BOTH complete [L304](../ledger/Yin_L_G0304_v1.md) and [L308](../ledger/Yin_L_G0308_v1.md) mathematical proof chains, with distinct general, finite-Salem and odd-radical domains.
Formal original findings remain in R203/R207; current checking follows separately.

<a id="statement"></a>
## Complete statement

Let P be the ACTUAL monic irreducible reciprocal nontorsion unit of degree d=2s, constant1, P=t^s Q(t+t^-1), with original alpha, tau=alpha+alpha^-1, O=Z[alpha], B=Z[tau] and TOTAL m=log M(P)>0.
Write Q(x)=sum_(j=0)^s q_j x^j with q_s=1; Q is monic irreducible degree s and need not be totally real.
For EVERY n>=s, let U_0=1,U_1=x,U_(j+1)=xU_j-U_(j-1), r_l=coeff rem_Q U_(l-1), R=[r_1...r_n], H=RR^T and Pi=R^T H^-1 R.
The integral symmetric divided-difference matrix
    (Q(x)-Q(y))/(x-y)=sum_(i,j=0)^(s-1) S_ij x^i y^j
has S_ij=q_(i+j+1) when i+j<=s-1 and0 otherwise, determinant(-1)^(s(s-1)/2).
For EVERY w, c=R^T w and a=polynomial with coefficients S w, the actual full edge satisfies
    C_c=sum_l c_l(t^(n+l)-t^(n-l)),
    P C_c=A_n(w)-t^(2n+1)A_n(w)*,
    deg A_n(w)<=d-1, A*=t^(d-1)A(1/t),
    A_n(w)=rem_P[t^(n+s)a(t+t^-1)].
Thus the integral unimodular trace transform E_n=S is INDEPENDENT of n; real/complex scalar extension is allowed but integrality is claimed at integral w.
The formal reversal degree stays d-1 at actual degree drops.

For the LEAST minimizer k of ell_k=r_k^T H^-1 r_k, let delta=content(r_k),u=r_k/delta,Delta=det H,gamma=content(adj(H)u),L=Delta/gamma and q_k=L/delta.
Then L is a positive integer, q_k may be rational, w_k=adj(H)u/gamma=q_k H^-1r_k is primitive, and a_k=S w_k is primitive.
The exact full selected data are
    c_l=Tr[a_k(tau)U_(l-1)(tau)/Q'(tau)],
    Res(P,A_k)=Norm(a_k)^2,
    Res(P,F_k)=L^d P(1)P(-1)Norm(u(tau))^2,
    S_2(F_k)^2=2q_k^2 ell_k,
    rho(F_k)=2(sum|c_l|)^2/sum c_l^2,
    deg F_k<=2n, coefficient height<=Delta,
    v_p(F_k(alpha_i))=v_p(L)+v_p(alpha_i-alpha_i^-1)+v_p(u(tau_i)).
ALL original embeddings/prime depths, complete leading/Mahler costs and ACTUAL monomial-removed degree T in Tm/d remain.
Edge depths are instead v_p(a_k(tau_i)); edge norm is not the auxiliary norm or its floor.

For multiplication T_Q by x mod Q,
    T_Q H-H T_Q^T=r_(n+1)r_n^T-r_n r_(n+1)^T,
    T_Q S=S T_Q^T.
Put z_j=S H^-1r_j,z_0=0,h_ij=r_i^T H^-1r_j, extending r to n+1.
For EVERY in-window k,
    T_Q z_k=z_(k+1)+z_(k-1)-h_(n,k)z_(n+1)+h_(n+1,k)z_n.
At the selected primitive column this is
    coeff rem_Q(xa_k)=q_k(z_(k+1)+z_(k-1))-c_n z_(n+1)+c_(n+1)z_n.
The c_(n+1) is an EXTENDED integer, not an in-window coefficient, and individual z_j/summands need not be integral or primitive.
Cauchy--Schwarz gives the two exact bounds with sqrt(ell_n ell_k) and sqrt(h_(n+1,n+1)ell_k) times q_k.
Only ell_n<=1 is an in-window projection diagonal; h_(n+1,n+1)<=1 is NOT established.

For ANY real w extend c_l=lambda_w(U_(l-1)) to all l>=1.
The exact FORMAL series, with P(0)=1, is
    sum_(l>=1)c_l z^(l-1)=z^(s-1)a(z+z^-1)/P(z).
The numerator is polynomial, formally reciprocal at degree2s-2, integral for integral w.
For nonzero INTEGRAL w, no original denominator root cancels.
No convergence/Hardy assertion is made, and c_(n+1) is exactly its z^n coefficient.

For ANY monic irreducible reciprocal nontorsion base p of degree2s0, ANY odd q>=3 with ACTUALLY irreducible P_q=p(t^q), and EVERY N>=s0 at n=qN, the whole anti projection is orthogonally conjugate by signed coordinate permutation to
    Pi_N^anti(p) direct_sum [(q-1)/2 copies Pi_(2N)^full(p)].
Residue0 has N anti coordinates and every paired nonzero residue has the full LENGTH2N base coefficient projection.
All qN coordinates and qs0 ranks are included.
If min diag anti < min diag full, precisely the dilated anti minimizers survive; unique base k0 yields unique k=qk0.
Reverse strict inequality selects a nonzero paired block; equality permits both.
Under the strict anti case the primitive F/A substitute t->t^q, signed resultants raise to q, all contents/coefficient norms/rho/leading factors/COMPLETE Mahler measures persist, actual degrees multiply by q and the full radial charge is unchanged.
The extra q-1 formal-reversal padding is retained.

For EVERY odd prime q, the actual irreducible P_q=t^(2q)-3t^q+1 has d=2q,s=q,n=3q and fixed TOTAL m=log beta, beta=(3+sqrt5)/2.
Its q expanding/q contracting roots have no unit-circle member.
The base anti diagonal minimum1/74 at k0=1 is STRICTLY below the full length6 minimum7/345, from the complete orthogonal rows(5,2,1,1,2,5) and(-11,-4,-1,1,4,11).
Thus the UNIQUE actual global selected index is k=q>0 at n=3s>2s, with
    F_q=8t^(6q)+3t^(5q)+t^(4q)-t^(2q)-3t^q-8,
    A_q=-8+21t^q, a_k=1, Res(P_q,A_q)=1,
    q_k=L=74,delta=1,Res(P_q,F_q)=(-27380)^q,
    S_1=24,S_2^2=148,rho=144/37,T=6q,
    height/leading F=8,degree/leading A=q/21.
At EVERY original p-adic conjugate normalized by v_p(p)=1, F depths are1 at2/37,1/2 at5 and0 elsewhere, including ramification and q=5; every A depth is0.
The COMPLETE measures are M(F)=8,M(A)=21, and
    B(F)=log185/2, Tm/d=3log beta,
    B-Tm/d=log[185/(161+72sqrt5)]/2<0.
The full original positive A-evaluation sum is4q log beta, normalized2log beta.
For the actual trace Q_q=V_q-3 and a=1,
    sum c_l z^(l-1)=z^(q-1)/(1-3z^q+z^(2q)),
    c_l=0 unless q|l,c_(jq)=U_(j-1)(3),
    c_n=8,c_(n+1)=0,c_(n+q)=21.
No original denominator/root/degree is suppressed.
The other boundary term remains and no several-endpoint or near-one obstruction follows.

The COMPLETE original15-window J77 domain retains P4/P6/PL, windows{s,2s-1,2s,2s+1,3s}, all50 row-basis edges/100 diagonals, complete ties and native fields.
Author2026-10-10T07:17 sole run1.467747499991674seconds within120seconds and separate whole computational2761 scalar-leaf finding remain historical evidence, without a rerun.
The unique quartic n3 selected unit edge and tied n4 unit edge have fixed positive measure and n<=2s; n4/n5 edge leading costs>=4/>=27 remain.
The later two-boundary proof is OUTSIDE that native scope.
L300's older quadratic all-window unit control, radical base costs and irreducibility remain prior results; the new radical contribution is the ALL-competitor selection.
The original2026-10-10T08:23 reversed1/8 transcription correction is fully retained before its original freeze; no program/formula scope is silently changed.
Syn26 and Nat26 supply only actual scoped classical definition/telescoping attribution, not a consumed external theorem or positive measure for Q's roots.
No uniform near-one coherence, compulsory nonzero next endpoint, general selected norm growth, unpaid leading/positive-evaluation cost or unrestricted gap is proved.

## Complete argument

<a id="argument"></a>

## Entire trace-transform, selected-cost and two-boundary argument

<a id="selected-edge-fixed-dual-reuse"></a>
### 1. Reuse, changed question and actual domain

The resultant_research AI for Yin develops the proof here; root supplied the broad question and no derivation.
The actual Task, applicable rules and [L300 complete proof/review](Yin_C_G0571_v1.md#statement) were read.
The immediate question is now the edge of the ACTUAL selected column, not an arbitrary direction in its row space.
L300 supplies the actual orders, content-preserving edge bijection, integer scale decomposition and all original finite-place costs.
[L296](Yin_C_G0571_v1.md#statement) supplies the selected anti projection and complete two-edge identity.
Those results already settle scalar positive-margin existence, the whole-row-space unit-edge example, and a QUADRATIC all-window selected unit-edge control with growing leading cost.
Thus the mere occurrence of a selected unit edge is already known.
The present fixed controls extend that phenomenon to actual higher-degree Salem inputs with unit-circle conjugates; the general changed step is the exact identification of E_n and its coupling to H_n, not a first counterexample to unrestricted selected norm growth.

A local screen for trace-dual coefficients, edge/Gram coupling and the polynomial divided-difference kernel found [L107's Lagrange trace-dual normalization](Yin_C_G0304_v1.md#canonical-trace-defect), and [L257's adjacent centered-edge calculation](Yin_C_G0438_v1.md#adjacent-edge-reuse-and-domain).
L257 concerns different centered windows, not the anti row basis used here.
L107's dynamical setting excludes unit-circle roots, but its displayed Lagrange coefficient identity is purely algebraic for a separable monic polynomial; that identity is the only part reused.
Its stable/expanding trace tails, multiplier bounds and positivity assertions are NOT transferred to this setting.
The divided-difference coefficient matrix below is the classical polynomial Bezout kernel, with its elementary anti-triangular and Lagrange identities verified directly; no general Bezoutian spectral theorem, codifferent theorem, Christoffel--Darboux theorem or new external theorem is imported.
The exact identification with the actual selected edge is the changed step, not the classical kernel itself.
This bounded reuse screen makes no priority or exhaustive absence claim.

Use the complete L300 domain: P is monic irreducible reciprocal nontorsion of degree d=2s and constant term1; P=t^s Q(t+t^-1), Q monic irreducible of degree s.
Let alpha be an original root, tau=alpha+alpha^-1, O=Z[alpha], B=Z[tau], m=log M(P)>0.
The original fields and orders, with all d original embeddings, are retained.
For n>=s put

    C_c(t)=sum_(l=1)^n c_l(t^(n+l)-t^(n-l)),
    r_l=coeff rem_Q U_(l-1), R_n=[r_1 ... r_n],
    H_n=R_n R_n^T, Pi_n=R_n^T H_n^-1 R_n,
    W_n=image_R(R_n^T).                                (1)

The recurrence is U_0=1,U_1=x,U_(j+1)=x U_j-U_(j-1).
For c=R_n^T w, w is the coefficient functional lambda_w(f)=w^T coeff(rem_Q f).
The L300 lattice identity gives integral c if and only if integral w, with equal contents.
For every nonzero integral w, the actual edge A_n(w) is determined by

    P C_(R_n^T w)=A_n(w)-t^(2n+1)A_n(w)*,
    deg A_n(w)<=d-1,
    A_n(w)*=t^(d-1)A_n(w)(1/t),
    A_n(w)(alpha)=alpha^(n+s)a_n(w)(tau), a_n(w) in B. (2)

The formal reversal degree remains d-1 even if the actual degree drops.
L300 proved that w to the trace coefficient vector of a_n(w) is an integral unimodular matrix E_n.
It did not identify that matrix or bound its dependence on n.
We now identify it exactly.

<a id="window-independent-trace-edge-matrix"></a>
### 2. The edge coordinate map is independent of the window

Write Q(x)=sum_(j=0)^s q_j x^j, q_s=1.
Define the integral symmetric s-by-s matrix S_Q by

    K_Q(x,y)=(Q(x)-Q(y))/(x-y)
       =sum_(i,j=0)^(s-1) (S_Q)_(ij) x^i y^j,
    (S_Q)_(ij)=q_(i+j+1) if i+j<=s-1, and0 otherwise.
    a_w(x)=lambda_w,y K_Q(x,y), coeff(a_w)=S_Q w.      (3)

The anti-diagonal entries are1 and every entry beyond that anti-diagonal is0.
Therefore det S_Q=(-1)^(s(s-1)/2), so S_Q is integral unimodular.
This is a coefficient expansion, not a positivity assertion about S_Q.

The exact all-window statement is

    a_n(w)=a_w for EVERY n>=s,
    E_n=S_Q,
    A_n(w)=rem_P[t^(n+s)a_w(t+t^-1)].                 (4)

The Laurent expression in the last line is evaluated in the actual unit order, so its unique degree-below-d representative is integral when w is integral.
Statement(4) also holds by scalar extension for real or complex w; the integral claim is only made at integral w.

Here is a complete proof, retaining every trace root.
Let tau_1,...,tau_s be the distinct roots of Q, and Q_j(x)=Q(x)/(x-tau_j).
Lagrange interpolation, exactly the algebraic mechanism retained in L107, gives

    lambda_w(f)=sum_j b_j f(tau_j),
    b_j=lambda_w(Q_j)/Q'(tau_j),
    a_w(tau_j)=lambda_w(Q_j)=b_j Q'(tau_j).            (5)

These formulas apply to remainders of arbitrary f; no root location is assumed.
For a fixed j put c_l^(j)=U_(l-1)(tau_j).
The quadratic recurrence proves directly

    (t^2-tau_j t+1) C_(c^(j))
       =D_(n,j)-t^(2n+1)D_(n,j)*,
    D_(n,j)=-U_(n-1)(tau_j)+t U_n(tau_j),
    D_(n,j)*=t D_(n,j)(1/t).                         (6)

One can check(6) by multiplying each anti monomial and cancelling successive U terms; only the two endpoint blocks remain.
It is the same formal recurrence used for L300's quadratic control, now valid at every complex tau_j, without importing that control's real-root inequalities.
The quotient

    M_j(t)=P(t)/(t^2-tau_j t+1)
          =t^(s-1)Q_j(t+t^-1)

is reciprocal of degree d-2.
Multiplying(6) by M_j gives a full edge of degree at most d-1, and its low block is M_j D_(n,j).
Since c_l=lambda_w(U_(l-1))=sum_j b_j c_l^(j), linearity identifies the complete actual low edge as sum_j b_j M_j D_(n,j).

For an original root alpha_i whose trace is tau_i, all terms with j!=i vanish on evaluation.
In the remaining term,

    M_i(alpha_i)=alpha_i^(s-1)Q'(tau_i),
    D_(n,i)(alpha_i)=alpha_i^(n+1),
    A_n(w)(alpha_i)=alpha_i^(n+s)b_i Q'(tau_i)
                   =alpha_i^(n+s)a_w(tau_i).           (7)

The middle identity follows either by the U recurrence or by U_(l-1)(alpha+alpha^-1)=(alpha^l-alpha^-l)/(alpha-alpha^-1).
All original roots avoid plus/minus1 by nontorsion.
The argument gives the same a_w on the inverse root of each pair as well.
Equations(2) and(7) prove(4).
Thus the previously implicit E_n has no window dependence, although H_n and the selected primitive w do.

<a id="selected-edge-dual-system"></a>
### 3. The exact selected-column dual system

At a specified window n choose the LEAST index k minimizing ell_(n,k)=r_k^T H_n^-1 r_k.
This is exactly L296's selection rule; all ell are positive and their sum is s.
Use L300's quantities

    delta_k=content(r_k), u_k=r_k/delta_k,
    Delta_n=det H_n, gamma_k=content(adj(H_n)u_k),
    L_k=Delta_n/gamma_k, q_k=L_k/delta_k,
    w_k=adj(H_n)u_k/gamma_k=q_k H_n^-1 r_k.           (8)

All primitive and positivity assertions here are those already proved in L300.
In particular L_k is an integer but q_k can be rational.
For this ACTUAL selected column, (4) gives

    coeff(a_k)=S_Q w_k=q_k S_Q H_n^-1 r_k,
    A_k=rem_P[t^(n+s)a_k(t+t^-1)],
    c_l=Tr_(Q(tau)/Q)[a_k(tau)U_(l-1)(tau)/Q'(tau)],
    F_k=C_c, S_2(F_k)^2=2 sum_(l=1)^n c_l^2
                          =2 w_k^T H_n w_k=2q_k^2 ell_(n,k),
    Res(P,A_k)=Norm_(Q(tau)/Q)(a_k(tau))^2.           (9)

The trace identity follows by summing(5); it is the actual algebraic trace, including each complex trace embedding, without conjugating the summand.
Since a_k is an actual element of the trace order, this agrees with the already integral c_l.
Primitivity of a_k follows from unimodularity of S_Q and primitivity of w_k.
The edge norm can be1 or a larger square; it is neither the original auxiliary norm nor its guaranteed all-root floor.

For clarity the simultaneous other costs remain

    coeff(v_k)=H_n w_k=L_k u_k,
    Res(P,F_k)=P(1)P(-1) Norm(v_k(tau))^2
              =L_k^d P(1)P(-1) Norm(u_k(tau))^2,
    rho(F_k)=2(sum_l |c_l|)^2/(sum_l c_l^2),
    deg F_k<=2n, h(F_k)<=Delta_n,
    v_p(F_k(alpha_i))=v_p(L_k)+v_p(alpha_i-alpha_i^-1)
                              +v_p(u_k(tau_i)).         (10)

Here h(F_k) means its maximum coefficient magnitude, not absolute Weil height.
All original prime/root labels are retained and every extra valuation in(10) is nonnegative.
The edge valuations instead equal v_p(a_k(tau_i)); no equality between these two collections is inferred.
Removing an initial monomial of F changes neither norm nor coefficient expense but its ACTUAL remaining degree must be used in Tm/d.
Full leading/exterior auxiliary costs remain part of M(F) and M(A), with the general bounds M<=S_2; they are not replaced by a norm of evaluations.
Equations(9)--(10) therefore give a joint description of a selected column, without yet supplying a uniform small-coherence inequality.

<a id="selected-edge-exact-pilot-declaration"></a>
### 4. Predetermined actual controls and complete cost declaration

Before any mathematical program execution, declare [J77](../computations/programs/Yin_J_G0077/readme.md) to contain EXACTLY these three inputs and five windows per input:

    P4=t^4-t^3-t^2-t+1,                 s=2;
    P6=t^6-t^5-t^3-t+1,                 s=3;
    PL=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1, s=5;
    n in {s,2s-1,2s,2s+1,3s}.                         (11)

There are15 distinct input/window pairs.
The aggregate author mathematical-runtime cap is120seconds.
There will be no expanded parameter set, coefficient-box search, random sample or numerical optimization.
Hand calculations preceding this declaration checked the quartic at n=2,3,4,5 and suggested both unit and nonunit SELECTED edges; these are disclosed discovery calculations, not independent evidence or a hidden computer search.
The declared complete domain includes them and the fixed corresponding windows on the other two inputs.

The exact irreducibility/Salem premises are the retained [L280 input verification](Yin_C_G0515_v1.md#small-measure-norm-moment-controls), with PL's trace irreducibility and all-real root locations coming from [L170](Yin_C_G0399_v1.md#lehmer-infinite-core-proof).
In particular the sextic is the displayed polynomial, not the different S6=t^6-t^4-t^3-t^2+1 from the current structural route.
Their actual trace polynomials are x^2-x-3, x^3-x^2-3x+1, and x^5+x^4-5x^3-5x^2+4x+3.
Each has exactly one trace root greater than2 and every other trace root in(-2,2), with the accepted real-embedding nonsquare argument supplying the quadratic extension.
These are fixed positive TOTAL measures, not a sequence approaching one.
The program will reconstruct the trace polynomials from P and additionally check their exact polynomial irreducibility; this supplements rather than changes the accepted source premises.

Every run will retain all projection diagonals, the complete minimizing-index set and the least-index choice, R,H,Delta,S_Q, the primitive w and a, q/delta/L, and every full F/A coefficient.
It will check(4) on EACH row-basis vector at every window, and then separately check the selected column.
Original resultants will also be evaluated directly from the full polynomials.
Complete energies, l1 norms, rho, primitive contents, removed monomial degree, actual degrees, leading coefficients, order-remainder content and all prime factors of L will be retained.
The explicit cost ratios are |Res(P,F)|/S_2(F)^d and |Res(P,A)|/S_2(F)^d; neither ratio includes radial expense.
The remaining radial charge is the exact Tm/d for the original P and actual monomial-removed F degree T.
Both full measures M(F),M(A) are charged at least by retaining their exact polynomials and leading coefficients, and using the proved upper bounds M(F)<=S_2(F), M(A)<=S_2(A) when a bound is used.
No decimal Mahler approximation or unverified exterior-root omission will enter a claimed inequality.

<a id="selected-edge-two-boundary-recurrence"></a>
### 5. An exact two-boundary relation for the selected edge

There is a useful algebraic relation between the window Gram matrix and multiplication in the ACTUAL trace order.
Let T_Q denote the coefficient matrix of multiplication by x modulo Q, with columns in the same ascending monomial basis as(1).
Put r_0=0 and extend the U recurrence to r_(n+1).
Then

    T_Q r_l=r_(l+1)+r_(l-1),
    T_Q H_n-H_n T_Q^T
       =r_(n+1)r_n^T-r_n r_(n+1)^T,
    T_Q S_Q=S_Q T_Q^T.                              (12)

The middle identity follows by substituting H_n=sum_(l=1)^n r_l r_l^T into the first recurrence.
The terms with indices l and l+1 cancel in pairs; the l=0 boundary is zero, leaving exactly the displayed n,n+1 term and its transpose, with the stated sign.
To prove the last identity, reduce (x-y)K_Q(x,y)=Q(x)-Q(y) modulo Q(x),Q(y).
Multiplication by x acts on its coefficient matrix on the left by T_Q, and multiplication by y acts on the right by T_Q^T.
This proves the equality without a real-root, positivity or diagonalizability hypothesis for T_Q.

Fix n, and define raw (usually rational) edge coefficient vectors and scalar pairings for j=0,...,n+1 by

    z_j=S_Q H_n^-1 r_j, z_0=0,
    h_(i,j)=r_i^T H_n^-1 r_j.

For 1<=k<=n, (12) gives the exact identity

    T_Q z_k=z_(k+1)+z_(k-1)
             -h_(n,k)z_(n+1)+h_(n+1,k)z_n.          (13)

Indeed, multiply the middle line of(12) by H_n^-1 r_k, solve for T_Q^T H_n^-1 r_k, and multiply by S_Q using its last line.
In particular, for the selected primitive column define c_(n+1)=r_(n+1)^T w_k, an integral extended coefficient that is NOT a coefficient already present in F_k.
The same equation becomes

    coeff[rem_Q(x a_k)]
       =q_k(z_(k+1)+z_(k-1))
           -c_n z_(n+1)+c_(n+1)z_n.                 (14)

No z_j in(13)--(14) is claimed primitive, and q_k need not be integral.
The equation is an equality of coefficient vectors of actual trace elements; individual summands may be rational even though its left side is integral.

The recurrence telescoping is classical Christoffel--Darboux algebra, rather than a new general identity.
The precise primary comparison read online on2026-10-10 is [Nat26, DLMF18.2(v), equation18.2.12](https://dlmf.nist.gov/18.2.E12), with x!=y and its displayed h_l,k_l normalizations, including the definitions18.2.5/18.2.7.
That source writes the usual product-sum kernel as two endpoint products.
The [responsible exact scope](../audits/literature/Nat26/readme.md#christoffel-darboux-attribution-20261010) records attribution and the acquisition failed with HTTP403, with no local artifact for this new scope.
It is cited only for this recognized algebraic mechanism; no positive orthogonality measure for Q's roots, kernel positivity at those roots, or external theorem hypothesis is presumed here.
All of(12)--(14) is proved directly above, including its orientation after quotient reduction.
This proof-only extension is separate from J77's predeclared finite payload, which does not claim to test(12)--(14).

The boundary issue is precise.
For k selected, Cauchy--Schwarz in the positive matrix H_n^-1 gives

    |c_n|<=q_k sqrt(ell_(n,n) ell_(n,k)),
    |c_(n+1)|<=q_k sqrt(h_(n+1,n+1) ell_(n,k)).        (15)

Here ell_(n,n)<=1 because it is a diagonal of Pi_n.
There is no corresponding projection-diagonal justification for h_(n+1,n+1)<=1: r_(n+1) is not a column of R_n.
Thus(14) identifies an actual extra endpoint expense, rather than discarding it.
The unknown control of that endpoint and its interaction with a_k's conjugates is a possible next joint-arithmetic test; (15) alone does not pay L229 coherence.

<a id="selected-edge-complete-finite-controls"></a>
### 6. Complete finite outcomes and actual selected unit edges

The first and sole author mathematical execution of [J77 verify.py](../computations/programs/Yin_J_G0077/verify.py) completed at2026-10-10T07:17 in1.467747499991674seconds, using Python3.12.14 and SymPy1.14.0, inside the declared aggregate120second cap.
It passed all15 windows, all50 row-basis edges and all100 projection diagonals.
There was no failed mathematical run, timeout, expanded parameter set or second optimization.
The complete exact native result (`mathematics/computations/outputs/Yin_J_G0077/result.json`) records every field declared in Section4, including the full coefficient arrays; the table below reports all15 cases rather than only the favorable unit edges.
Delta, gamma, every diagonal, all norm/cost ratios, all prime factors of L, and both complete auxiliary polynomials are retained in that native result.

In the table N(a) is the SIGNED trace norm; the original edge resultant is N(a)^2.
The minimizing set is complete and its least element is selected.
E is the COMPLETE original coefficient energy S_2(F)^2, and T is the degree after removing only an initial monomial.
All15 cases have delta_k=1, so q_k=L_k here; this finite observation is not asserted for all inputs.

| Input | n | All minimizing indices | L | N(a) | E | T |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| P4 | 2 | 1,2 | 1 | -3 | 2 | 2 |
| P4 | 3 | 1 | 3 | -1 | 6 | 6 |
| P4 | 4 | 1,3 | 10 | 1 | 60 | 8 |
| P4 | 5 | 1,3 | 42 | -87 | 924 | 10 |
| P4 | 6 | 4 | 59 | -17 | 590 | 12 |
| P6 | 3 | 1,2,3 | 1 | -2 | 2 | 2 |
| P6 | 5 | 2,4 | 12 | 4 | 120 | 10 |
| P6 | 6 | 2,4 | 44 | 2228 | 1496 | 12 |
| P6 | 7 | 4 | 161 | -1765 | 7728 | 14 |
| P6 | 9 | 4 | 1150 | -803735 | 227700 | 18 |
| PL | 5 | 1,2,3,4,5 | 1 | 1 | 2 | 2 |
| PL | 9 | 3 | 68 | 2025253 | 3536 | 18 |
| PL | 10 | 5 | 293 | 2594303251 | 57428 | 20 |
| PL | 11 | 8 | 661 | -143050942863 | 257790 | 22 |
| PL | 15 | 8 | 11089 | -32121334824918709 | 42914430 | 30 |

Here are short exact proofs of the two nontrivial selected unit-edge controls, so their force does not rest only on a program's success flag.
For P4, Q=x^2-x-3, so

    S_Q=[[-1,1],[1,0]],
    r_1=(1,0), r_2=(0,1), r_3=(2,1), r_4=(3,2).

At n=3 one has

    H_3=[[5,2],[2,2]], Delta_3=6,
    (ell_1,ell_2,ell_3)=(1/3,5/6,5/6),
    k=1 uniquely, w=(1,-1), L=q=3, a=x-2,
    F=-1+t-t^2+t^4-t^5+t^6,
    A=-1+2t-t^2+t^3,
    N(a)=Q(2)=-1, Res(P4,A)=1,
    Res(P4,F)=-243, E=6, rho(F)=6, T=6.             (16)

The equality N(tau-2)=Q(2) uses the even trace degree2.
All of these follow by multiplying the displayed2-by-2 matrices, then(4) and(10); multiplying P4 F also checks the full edge identity.
In particular the selected index is unique, so this cannot be dismissed as a choice of a nonselected unit direction.

At n=4 the corresponding complete data include

    H_4=[[14,8],[8,6]], Delta_4=20,
    (ell_1,ell_2,ell_3,ell_4)=(3/10,7/10,3/10,7/10),
    k=1 by the specified least-index rule,
    w=(3,-4), L=q=10, a=3x-7, N(a)=1,
    F=-1-2t+4t^2-3t^3+3t^5-4t^6+2t^7+t^8,
    A=-1-t+7t^2-4t^3,
    Res(P4,F)=-30000, E=60, rho(F)=20/3, T=8.         (17)

For a=u tau+v in this quadratic order, N(a)=v^2+uv-3u^2; applying this to(3,-7) gives1.
The full polynomial A has leading coefficient-4, hence M(A)>=4 despite Res(P4,A)=1.
At n=5, a=11x-23 instead has norm-87; the retained full A=4-13t-5t^2+27t^3 has M(A)>=27.
Neither its leading factor nor any of its other roots can be omitted.
Thus selected edges are neither always units nor forced to have nontrivial norm solely by the least-diagonal rule.

The full norm-to-energy ratios in(16)--(17) are respectively27/4 and25/3, but these are exp(d B) with B=(log|Res(P,F)|)/d-log S_2(F), BEFORE radial and conjugate-coherence charges.
Their actual original radial expenses are(3/2)m and2m respectively.
There is no deduction of a positive fully paid margin from these two ratios.
The exact leading factors and all coefficients of F and A are retained, with M(F)<=sqrt(E) and M(A)<=S_2(A) as upper bounds only; neither a norm-one value nor these inequalities sets the complete measures to1.

An unqualified claim that every selected column on every genuine nontorsion input with n>s must have edge norm larger than1 was ALREADY excluded by L300's quadratic all-window control.
The present controls extend that counterboundary to the actual quartic Salem input, including a unique minimizer and genuine unit-circle conjugates.
In the class with trace degree at least2, these particular controls do not refute a claim whose hypotheses require n>2s, a particular larger proportional window, or total m approaching0: the two quartic controls have n=3,4 with s=2 and fixed positive total measure.
PL at n=s is also a genuine selected unit edge, but W_n is then the whole coefficient space, so its unit example is a weaker boundary.
No numerical sequence, growing-degree family, uniform upper estimate or near-one obstruction is inferred from this table.

<a id="selected-edge-source-and-status"></a>
### 7. Source boundaries, contribution and remaining test

The primary definition actually inspected for the classical matrix in(3) is [Syn26, retained INRIA SYNAPS HTML, section The Bezout matrix](../literature/pdf/Syn26/bezout-20261010.html#UResultantThe_Bezout_matrix), whose [official page](https://www-sop.inria.fr/galaad/software/synaps/UResultant.html) was read online before derivation and whose defining TeX alt text was subsequently checked in the retained local artifact.
It defines coefficients of (f_0(x)f_1(y)-f_1(x)f_0(y))/(x-y), under deg f_1>=deg f_0; with f_0=1,f_1=Q our S_Q is the NEGATIVE of that convention's matrix.
The [source note](../audits/literature/Syn26/readme.md#bezout-kernel-attribution) retains the exact role.
This is definition/attribution scope only.
No personal author or publication date was verified: Syn26 uses the project-name fallback and inspection-year address, with publication year n.d.
No rank/resultant theorem from the following paragraph is consumed, and no publication-priority claim is made.
A bounded screen also opened the author-hosted Andrews--Wigderson2024 paper's title and contents, but did not locate and inspect a matching exact definition; that paper is NOT a premise.
Nat26's online equation18.2.12 is used only for the attribution stated in Section5.
The local L107 algebraic trace identity, L300 order/content results and L280/L170 actual control premises remain the substantive retained inputs, with their original scopes unchanged.

The changed result consists of the exact identification E_n=S_Q at every admissible window, the simultaneous selected formula(9) with the complete original norm/energy/depth costs(10), the explicit two-boundary coupling(12)--(15), and true selected unit/nonunit controls with every leading and radial expense retained.
The classical Bezout and recurrence identities are not claimed as newly discovered general results.
Root allocated the broad question and J77; no root derivation entered this author proof.
The exact program is author evidence, not independent review.

The remaining arithmetic question is now more specific than arbitrary row-space norm growth: for the actual minimizer k, can the vector S_Q H_n^-1 r_k, its rational primitive scale, and the endpoint term c_(n+1) jointly yield an upper bound on all conjugate coherence that is useful uniformly when m tends to0?
An alternate admissible target is a precise additional hypothesis (necessarily excluding the retained quadratic control) under which selected norm-one edges cannot occur at larger degree-linear windows, while still paying the full leading and coefficient costs.
This draft proves neither target.
It does not replace full signed edge correlations by a product of absolute values, identify edge norm with full auxiliary norm, reuse fixed-m examples as near-one counterexamples, or improve a basis-invariant determinant bound by changing coordinates.
The retained all-input scalar margin remains in force, and the unrestricted G0001 objective remains unresolved with current execution paused.


## Entire formal-sequence, radical-selection and paid-control argument

<a id="selected-radical-reuse-and-domain"></a>
### 1. Changed question and exact reuse

This is proof-only work by the resultant_research AI for Yin.
The coordinator supplied the broad question and no derivation.
The actual Task and current knowledge-reuse rules were checked.
The required conclusion is about the ACTUAL least-diagonal selected anti column at a window strictly larger than2s, not just an integral row-space direction or an arbitrarily lifted column.

The direct algebraic input is [L304's complete selected trace-edge and two-boundary identity](#statement), with the integral orders, primitive scales and full original norm formula reused from [L300](Yin_C_G0571_v1.md#statement).
Its Bezout matrix S_Q and trace pairing retain the exact Syn26/L107 attribution and proof scopes.
No classical Bezout or Christoffel--Darboux mechanism is recredited here.

The local reuse screen also found the exact relevant older controls, which substantially narrow the new contribution.
[L296 Section6](Yin_C_G0571_v1.md#actual-anti-column-quadratic-all-window-control) already proves the all-window quadratic anti-column formulas, their complete circle-root/leading costs and negative radial excess.
It already lifts those actual columns to P(t^q), but explicitly does NOT claim that the lifted column minimizes all diagonals in the larger anti space.
[L241's full residue-block projection](Yin_C_G0570_v1.md#projection-radical-block-control) already gives the corresponding full coefficient projection by exponent residues; its old determinant optimization is not reused as new mathematics.
[L193](Yin_C_G0463_v1.md#exact-resultant-content-collapse) proves actual irreducibility of t^(2q)-3t^q+1 for EVERY odd prime q and its fixed total measure.
These interfaces were read directly, including the prime proof and the precise original-degree costs.
They supply a workable method, so no new external theorem or source acquisition is needed.

The changed step below is to pair all nonzero residue classes under anti reversal, expose every competing diagonal, and prove that one specific lifted column is the UNIQUE global minimum.
A general formal generating identity also makes the complete selected trace-edge's extended boundary coefficient explicit.
The original family, composition measure rule, fixed positive total measure, quadratic full costs and ordinary residue separation are retained inputs or elementary specializations, not newly discovered results.

Use the L304 domain P monic irreducible reciprocal nontorsion, degree d=2s, constant1, with P(t)=t^s Q(t+t^-1), actual trace order B=Z[tau], tau=alpha+alpha^-1.
The field degree is the actual degree of P, not a formal power.
Define U_0=1,U_1=x,U_(l+1)=xU_l-U_(l-1), r_l=coeff rem_Q U_(l-1), H_n=sum_(l=1)^n r_l r_l^T for n>=s, and Pi_n=R_n^T H_n^-1R_n.
The selected k is the least minimizer of ell_k=(Pi_n)_(kk).
For its positive primitive scale q_k and integral vector w_k=q_k H_n^-1r_k, L304 gives

    a_k=polynomial with coeff S_Q w_k,
    c_l=w_k^T r_l,
    F_k=sum_(l=1)^n c_l(t^(n+l)-t^(n-l)),
    P F_k=A_k-t^(2n+1) A_k*,
    A_k(alpha)=alpha^(n+s)a_k(tau),
    Res(P,A_k)=Norm_B(a_k)^2.                         (1)

Here Norm_B denotes the field norm of the displayed order element.
The formal reversal degree of A is d-1, even if its actual degree drops.
The letter q below is an ODD INTEGER dilation factor, whereas q_k in(1) is the rational primitive scale; their meanings are kept distinct.

<a id="trace-edge-formal-generating-identity"></a>
### 2. The actual trace edge determines the entire extended sequence

Let w be any real coefficient functional lambda_w(f)=w^T coeff(rem_Q f), and set a(x)=lambda_w,y((Q(x)-Q(y))/(x-y)).
For a selected column these are exactly w_k,a_k.
Extend c_l=lambda_w(U_(l-1)) to ALL l>=1, not only the first n entries.
The exact formal identity is

    sum_(l>=1)c_l z^(l-1)=B_a(z)/P(z),
    B_a(z)=z^(s-1) a(z+z^-1).                        (2)

B_a is a real polynomial of degree at most2s-2, formally reciprocal at that degree.
It is integral when w is integral.
This is a formal power series around zero; P(0)=1.
No convergence on the unit circle or Hardy-space integrability is assumed.

To prove(2), work in the quotient algebra R[x]/(Q) with a separate indeterminate Y.
Since Q(x)=0 there,

    (Y-x)^-1=(Q(Y)-Q(x))/((Y-x)Q(Y)),
    lambda_w((Y-x)^-1)=a(Y)/Q(Y).                    (3)

The finite recurrence gives sum_(l>=1)U_(l-1)(x)z^(l-1)=1/(1-xz+z^2).
Put Y=z+z^-1 in(3), multiply by z^-1, and use Q(z+z^-1)=z^-s P(z).
This yields precisely(2).
All operations are identities of rational functions and then of formal power series with nonzero denominator constant.
This is the same classical polynomial resolvent/divided-difference algebra already consumed in L304 and L107, directly specialized to the actual recurrence; it introduces no uninspected analytic theorem.

For integral nonzero w, L304 makes a a nonzero degree-below-s polynomial.
Thus B_a and P have no common original root: at alpha, B_a(alpha)=alpha^(s-1)a(tau)!=0 by actual trace irreducibility.
The full original denominator in(2) has not been simplified by silently cancelling conjugates.
In particular

    c_(n+1)=[z^n]B_a/P,
    S_2(F_k)^2=2 sum_(l=1)^n c_l^2,
    rho(F_k)=2(sum_(l=1)^n |c_l|)^2/sum_(l=1)^n c_l^2. (4)

These formulas expose the exact boundary and coefficient expense, not a bound on them.
The recurrence can produce zero coefficients at specific future indices despite a nonzero numerator and a noncancellable original denominator.
Section5 gives that phenomenon for the ACTUAL selected columns of unbounded irreducible degree.

<a id="odd-radical-anti-selection-decomposition"></a>
### 3. A complete selection criterion under odd radical dilation

Let p be a monic irreducible reciprocal nontorsion unit polynomial of degree2s_0.
Let q>=3 be odd, assume P_q(t)=p(t^q) is ACTUALLY irreducible, and fix N>=s_0.
Its trace degree is s=q s_0, and take n=qN.
Let Pi_N^anti(p) be the base N-coordinate anti projection from(1).
Let Pi_(2N)^full(p) be the Euclidean projection onto the real remainder row space of the ordinary coefficient window of LENGTH2N, with indices0,...,2N-1.
Then the enlarged anti projection is conjugate by a signed coordinate permutation to

    Pi_(qN)^anti(P_q)
       = Pi_N^anti(p) direct_sum
          [(q-1)/2 copies of Pi_(2N)^full(p)].        (5)

The displayed equality means orthogonal identification of those blocks, not literal equality in the original index order.
It covers ALL n anti coordinates; dimensions are N+(q-1)N=qN.
The first block consists exactly of indices l=q,2q,...,Nq.
The other blocks collect l congruent to plus/minus r modulo q, for1<=r<q/2; their diagonal multisets are exactly those of the indicated full base projection.
The sum of their ranks is s_0+(q-1)s_0=q s_0, the actual trace degree.

For proof, begin in the full coefficient space of polynomials of degree at most2qN, with its orthonormal monomial basis.
Orthogonal complement to multiples of P_q is the actual remainder row space.
As in L241, exponent residues modulo q give an orthogonal direct sum: residue0 has LENGTH2N+1, while each nonzero residue has LENGTH2N.
Monic division by p(t^q) separates each component, so the residual projection is the corresponding full base projection on each component.
This extension of the retained equal-length formula only keeps the actual extra residue-zero coordinate; it follows from the identical divisibility argument.

Full reversal J:t^j to t^(2qN-j) preserves the relation space because P_q is reciprocal.
Hence its orthogonal complement and its orthogonal projection are J-invariant, and the projection restricts to the anti eigenspace.
Residue0 is J-invariant and restricts to the base anti space about index N.
For nonzero residue r, J exchanges it with q-r and reverses the internal2N coordinates.
Write J_0 for this internal reversal.
An anti vector in this pair is precisely(v,-J_0 v)/sqrt(2), which is an isometric copy of the full base2N-coordinate space.
The base full projection commutes with J_0 by the same reciprocity, so its restriction on this pair is exactly Pi_(2N)^full(p).

Finally the orthonormal anti basis of the large space is (t^(qN+l)-t^(qN-l))/sqrt(2),1<=l<=qN.
In each paired block this is the isometric image of an ordinary basis vector, possibly with a sign or reversed order.
In residue0 it is the standard base anti basis.
The anti row space coincides with the U-remainder row space in(1): an anti polynomial has original value alpha^n(alpha-alpha^-1) times its trace polynomial, so its relation space is precisely ker R_n.
This proves(5), including the projection and every diagonal, rather than only a determinant or chosen-vector equality.

Consequently put

    mu_anti=min diag Pi_N^anti(p),
    mu_full=min diag Pi_(2N)^full(p).

If mu_anti<mu_full, ALL minimizing enlarged anti indices come from the residue-zero block, and are q times the minimizing base anti indices.
If the base minimizer k_0 is unique, the enlarged minimizer is UNIQUE at k=q k_0.
The projected column lifts exactly by t->t^q, as does its positive primitive integral representative.
If the inequality is reversed, the enlarged minimum comes from a nonzero paired block; equality permits both blocks.
Thus an arbitrary lifted anti column is not silently called the selected column.

When the strict inequality holds, let F_0,A_0,a_0 be the selected base polynomials in(1).
Their exact enlarged data obey

    F=F_0(t^q), A=A_0(t^q),
    a(tau)=a_0(alpha^q+alpha^-q),
    Res(P_q,F)=Res(p,F_0)^q,
    Res(P_q,A)=Res(p,A_0)^q,
    S_1(F)=S_1(F_0), S_2(F)=S_2(F_0), rho(F)=rho(F_0),
    M(F)=M(F_0), M(A)=M(A_0).                         (6)

The full edge identity after substitution has high shift q(2N+1) with base reversal degree q(2s_0-1).
Relative to the required enlarged shift2qN+1, the enlarged formal reversal of A has degree2q s_0-1 and contributes the extra t^(q-1).
Their sum is the same exponent; therefore A=A_0(t^q) satisfies exactly(1), not a changed edge convention.
Primitive contents and leading coefficients are unchanged under substitution.
Every base original root has ALL q preimages; multiplying their values proves both signed resultant equalities.
Factoring each nonzero auxiliary root into its q preimages proves the Mahler equalities with full multiplicities and leading factor.
Actual auxiliary degrees and any initial monomial degree multiply by q.
Thus Tm(P_q)/(2q s_0)=T_0 m(p)/(2s_0); no degree charge or total measure is divided away.

<a id="unique-selected-unit-unbounded-degree"></a>
### 4. A unique selected unit edge at n=3s and unbounded actual degree

Apply(5) to p(t)=t^2-3t+1 and N=3.
For every odd prime q, L193 supplies actual irreducibility of

    P_q(t)=t^(2q)-3t^q+1,
    d=2q, s=q, n=3q,
    beta=(3+sqrt(5))/2,
    m(P_q)=log beta>0.                              (7)

All q expanding roots have modulus beta^(1/q), and all q contracting roots have reciprocal modulus.
There are no unit-circle conjugates.
This is a genuine unbounded-degree family but has FIXED positive total measure, even as the individual moduli approach one.

The base anti row is (1,3,8), by the quadratic U recurrence.
Its squared length is74, so its three projection diagonals are

    (1/74,9/74,64/74).                              (8)

The full base window in(5) has LENGTH6.
Its two-dimensional remainder row space is spanned by the sequences beta^j,beta^-j,0<=j<=5.
The two explicitly integral orthogonal rows

    u=(5,2,1,1,2,5), ||u||^2=60,
    v=(-11,-4,-1,1,4,11), ||v||^2=276               (9)

span that same space.
Each satisfies y_(j+2)=3y_(j+1)-y_j; u is reversal-symmetric and v is reversal-antisymmetric, and they are linearly independent.
Thus its full projection diagonal at j is u_j^2/60+v_j^2/276.
Both summands strictly increase when one moves from a central index to an adjacent outer pair, since both displayed magnitudes do.
Hence its minimum occurs precisely at j=2,3 and is

    mu_full=1/60+1/276=7/345>1/74=mu_anti.            (10)

The strict inequality is exact:7*74=518>345.
There are no unexamined coefficient classes.
Equations(5),(8)--(10) prove the UNIQUE global selected anti index k=q, for EVERY odd prime q, at n=3q=3s>2s.

The selected primitive polynomials and edge are therefore

    F_q=8t^(6q)+3t^(5q)+t^(4q)-t^(2q)-3t^q-8,
    A_q=-8+21t^q,
    P_q F_q=A_q-t^(6q+1)A_q*,
    A_q*=t^(2q-1)A_q(1/t),
    a_q(tau)=1, Res(P_q,A_q)=1.                      (11)

For the last line, beta^2=3beta-1 gives beta^4=21beta-8.
At every original root alpha, alpha^q is beta or beta^-1, and A_q(alpha)=alpha^(4q).
The normalization n+s=4q in(1) proves a_q=1 in the actual degree-q trace order, including all embeddings.
This is the true selected direction, not only a norm-one row-space direction.
Its coefficients contain1, so no content or rational scale was omitted.

<a id="selected-radical-full-boundary-and-cost"></a>
### 5. Complete original norm, boundary and Mahler costs

The selected raw anti column has its only nonzero coordinates at l=q,2q,3q, equal to(1,3,8)/74.
Hence its positive primitive scale is q_k=74, its integral coordinate content is1, and its full data are

    F_q(alpha)=74 alpha^(2q)(alpha^(2q)-1),
    Res(P_q,F_q)=(-5*74^2)^q=(-27380)^q,
    S_1(F_q)=24, S_2(F_q)^2=148, rho(F_q)=144/37,
    deg F_q=6q, initial monomial degree0,
    height(F_q)=8, leading(F_q)=8,
    deg A_q=q, leading(A_q)=21,
    Res(P_q,A_q)=1.                                 (12)

The projection evaluation is the L296 paired-monomial identity at k=q and n=3q.
For the full signed norm, each of the q original preimages of beta or beta^-1 is included; the base endpoint product is p(1)p(-1)=(-1)*5=-5.
Thus the original degree exponent on the scalar74 is2q, not q or6q.
The original cyclic resultant is Res(P_q,t^(2q)-1)=(-5)^q, a different quantity from the scalar income.
Since U_(q-1) has degree q-1 and is monic, its trace-remainder content is delta_k=1.
L300's integral Gram order is therefore L_k=74; it is not inferred from an average norm divisibility.

At EVERY original p-adic conjugate, normalized by v_p(p)=1, alpha is a unit.
The value alpha^(2q)-1 equals beta^2-1 or beta^-2-1 after the corresponding quadratic embedding.
Each is a unit times sqrt(5), because beta-beta^-1=sqrt(5), and its full quadratic norm has magnitude5.
Consequently the complete individual depths are

    v_2(F_q(alpha))=1,
    v_37(F_q(alpha))=1,
    v_5(F_q(alpha))=1/2,
    v_p(F_q(alpha))=0 for other primes p,
    v_p(A_q(alpha))=0 for EVERY p.                   (13)

These statements include the ramified/index-prime case and q=5: the valuation is normalized on Q_p and extended, so the half-depth is meaningful.
The same formulas follow algebraically from alpha^(2q)-1 being a unit times sqrt(5), independent of splitting-field choices.
Summing over all2q original roots reproduces precisely the integer valuation of(-27380)^q, including q copies of5.
No repeated reduction or root label has been dropped.

The complete auxiliary measures are ALSO exact, not upper bounds from the edge norm.
Writing u=t^q, the base factorization is

    F_0(u)=u^2(u^2-1)[8(u+u^-1)^2+3(u+u^-1)-7],
    M(F_q)=8, M(A_q)=21.                            (14)

The displayed Laurent expression expands to the polynomial in(11).
The quadratic8x^2+3x-7 has one root in(-2,0) and one in(0,2): its values at-2,0,2 are19,-7,31, respectively, and its degree is2.
Each root supplies its full reciprocal pair on the unit circle; the factor u^2-1 supplies both endpoints.
Thus all six roots of F_0 are on the circle, its actual degree is6 and its leading coefficient is8.
After substitution every root has all q preimages on the circle, giving M(F_q)=8 at actual degree6q.
Each root of A_q satisfies |t|=(8/21)^(1/q)<1, so all q edge roots are inside and its complete measure is its leading coefficient21.
No scalar, endpoint or exceptional root is omitted.

The normalized signed-conjugate information and fully charged radial balance are

    B(F_q)=log|Res(P_q,F_q)|/(2q)-log S_2(F_q)
          =(1/2)log185,
    T m(P_q)/d=3log beta,
    B(F_q)-T m(P_q)/d
          =(1/2)log[185/(161+72sqrt(5))]<0.           (15)

Here beta^6=161+72sqrt(5)>185.
This is the same negative base balance already proved in L296, now attached to the UNIQUE global selected column by Section4.
It is not credited as a new cost inequality.
Although the degree grows without bound, neither total m nor the negative constant in(15) tends to zero.
The complete original positive evaluation cost of the edge is also explicit:

    sum_(all original alpha) log^+|A_q(alpha)|
         =4q log beta,
    (1/d)sum log^+|A_q(alpha)|=2log beta.             (16)

It follows from A_q(alpha)=alpha^(4q) and the q expanding and q contracting original roots.
Thus full edge norm1, degree-independent edge Mahler measure21 and degree-independent coefficient support do not make all original positive evaluations vanish.

Finally the next boundary term in L304 is exactly zero for this actual selected column.
To see the ENTIRE sequence, let V_q(x) be the monic polynomial specified by V_q(z+z^-1)=z^q+z^-q; it has integer coefficients by V_0=2,V_1=x,V_(j+1)=xV_j-V_(j-1).
The actual trace polynomial is Q_q=V_q-3, degree q.
Its S_Q matrix has final column e_0, so the unit trace element a_q=1 corresponds exactly to w=e_(q-1).
The formal identity(2) yields

    sum_(l>=1)c_l z^(l-1)
       =z^(q-1)/(1-3z^q+z^(2q)),
    c_l=0 if q does not divide l,
    c_(jq)=U_(j-1)(3) for j>=1,
    c_n=8, c_(n+1)=0, c_(n+q)=21 at n=3q.           (17)

All2q original roots, equivalently all q inverse-pair traces, remain in the denominator; it has not been reduced to a smaller original-degree problem.
One can describe the sparse coefficient sequence via z^q without changing the actual input degree or any charged quantity above.
In particular, the upper-end coefficient can vanish even when k is uniquely selected, n>2s, the full original input is nontorsion and the trace edge is a unit.
This excludes an unqualified lower bound demanding that EVERY next endpoint be nonzero under just those hypotheses.
It does not bound the other boundary term in L304: c_n=8 is nonzero, and the recurrence still includes its associated vector z_(n+1).

<a id="selected-radical-scope-and-next-test"></a>
### 6. What this settles and what remains open

The general result is the complete odd-radical anti decomposition(5), its strict selection criterion and full cost transfer(6), together with the exact trace-edge generating identity(2).
The actual consequence is an unbounded-degree family in which the globally selected column at n=3s has trace edge1 and a zero next extended coefficient, with every conjugate, leading factor, primitive scale, degree, depth and Mahler cost explicit.
The ordinary residue decomposition, the family and irreducibility, the base unit edge, its complete root/leading costs and its negative radial balance are prior inputs.
The new argument supplies the previously missing comparison with ALL competing nonzero residue blocks.
It does not improve the generic determinant invariant or claim that a chosen favorable lifted column is automatically selected.

This is a precise obstruction to degree growth and the condition n>2s ALONE forcing selected edge-norm growth or a nonzero next endpoint.
It also shows why the complete boundary pair and original coefficient/radial expense must accompany any estimate.
It is NOT an actual near-one sequence, has no unit-circle conjugates and has q expanding roots.
Therefore it does not exclude a theorem using small TOTAL m, a genuine additional Salem restriction, or several coordinated window endpoints.
The fixed positive margin of L237 remains established, and this fixed-measure counter-control neither contradicts nor pays L229's near-one coherence bound.

A sharper next question is to control the full selected numerator B_a and its rational function B_a/P at several actual degree-linear indices simultaneously, with the scale q_k and the original m retained.
Formula(17) rules out treating one endpoint as a compulsory payment even in unbounded degree; a multiple-endpoint or genuinely near-one assertion would require a new argument.
This draft neither conjectures that the near-one class has the residue pattern above nor supplies an input-uniform upper bound for its boundary energy.
The unrestricted G0001 objective remains unresolved with current execution paused.

<a id="selected-radical-working-correction"></a>
### Working correction retained before author freeze

At2026-10-10T08:23, the author self-check caught a handwritten coefficient-transcription error in the first candidate message and the initial Section4 display of F_q: the entries1 and8 had been placed in reverse order.
The actual selected coordinate row is(1,3,8), so the correct polynomial is8t^(6q)+3t^(5q)+t^(4q)-t^(2q)-3t^q-8 as now displayed.
The candidate's A=-8+21t^q, energy148, norm(-27380)^q, M(F)=8 and all block/minimum calculations were already based on the correct coordinate row and did not change.
The literal product is now8t^(8q)-21t^(7q)+21t^q-8, agreeing with the complete formal edge identity.
The coordinator was notified immediately.
No program was executed, no failed mathematical run or search output was discarded, and this correction occurred before freeze or independent review.


## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:59 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Full actual anti/order/edge proof](Yin_C_G0571_v1.md#statement) | Actual integral row lattice, selected primitive scale, both full norm identities, original all-place costs and prior quadratic/lifted controls only. |
| dependency | [Actual odd-prime irreducibility](Yin_C_G0463_v1.md#exact-resultant-content-collapse) | EVERY odd prime actual degree2q and fixed TOTAL measure; no assumed irreducibility of an arbitrary composition. |
| support | [Full residue projection](Yin_C_G0570_v1.md#projection-radical-block-control) | Actual ordinary residue-kernel mechanism; the odd anti-pairing, unequal lengths and every competitor are proved fully here. |
| support | [Algebraic Lagrange normalization](Yin_C_G0304_v1.md#canonical-trace-defect) | Only its separable monic coefficient interpolation identity, not its no-neutral dynamics or decay. |
| dependency | [Actual finite Salem inputs](Yin_C_G0515_v1.md#small-measure-norm-moment-controls) | Only the exact quartic/sextic/Lehmer trace and field-degree controls for the original finite15-window evidence. |
| support | [Original J77 evidence](../computations/programs/Yin_J_G0077/readme.md) | Full declared15-window native scope and separate whole computational finding, not the later proof-only boundary recurrence. |
| support | [Original L304](../ledger/Yin_L_G0304_v1.md#complete-retained-proof-and-review) | Complete first proof, original author/native/source and R203 frozen inputs; no source reinspection. |
| support | [Original L308](../ledger/Yin_L_G0308_v1.md#complete-retained-proof-and-review) | Complete second proof, actual pre-freeze correction/author and R207 original frozen input. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:02 |
| status | proved |
| reason | Adopt the complete actual selected-edge object after actual whole SELF of its entire Statement and BOTH full mathematical proof chains, retaining all original formal checking relationships and fixed inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Full actual anti/order/edge proof](Yin_C_G0571_v1.md#statement) | Actual integral row lattice, selected primitive scale, both full norm identities, original all-place costs and prior quadratic/lifted controls only. |
| dependency | [Actual odd-prime irreducibility](Yin_C_G0463_v1.md#exact-resultant-content-collapse) | EVERY odd prime actual degree2q and fixed TOTAL measure; no assumed irreducibility of an arbitrary composition. |
| support | [Full residue projection](Yin_C_G0570_v1.md#projection-radical-block-control) | Actual ordinary residue-kernel mechanism; the odd anti-pairing, unequal lengths and every competitor are proved fully here. |
| support | [Algebraic Lagrange normalization](Yin_C_G0304_v1.md#canonical-trace-defect) | Only its separable monic coefficient interpolation identity, not its no-neutral dynamics or decay. |
| dependency | [Actual finite Salem inputs](Yin_C_G0515_v1.md#small-measure-norm-moment-controls) | Only the exact quartic/sextic/Lehmer trace and field-degree controls for the original finite15-window evidence. |
| support | [Original J77 evidence](../computations/programs/Yin_J_G0077/readme.md) | Full declared15-window native scope and separate whole computational finding, not the later proof-only boundary recurrence. |
| support | [Original L304](../ledger/Yin_L_G0304_v1.md#complete-retained-proof-and-review) | Complete first proof, original author/native/source and R203 frozen inputs; no source reinspection. |
| support | [Original L308](../ledger/Yin_L_G0308_v1.md#complete-retained-proof-and-review) | Complete second proof, actual pre-freeze correction/author and R207 original frozen input. |
| review | [Actual whole current SELF](../audits/reviews/Yin_R_G0760_v1.md#selected-trace-radical-whole-self) | Entire current Statement, both complete arguments and every cost/source/native/correction/negative domain; actual SELF, with no isolated replacement of historical UNKNOWN or known SELF. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:26 |
| status | proved |
| reason | Adopt the ENTIRE unchanged current Statement and all complete mathematical Arguments after the actual isolated whole review, necessary fixed interfaces and bounded original finite-evidence check where applicable; all original mathematical/source/native/correction/negative scopes and historical checking relationships remain distinct. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Full actual anti/order/edge proof](Yin_C_G0571_v1.md#statement) | Actual integral row lattice, selected primitive scale, both full norm identities, original all-place costs and prior quadratic/lifted controls only. |
| dependency | [Actual odd-prime irreducibility](Yin_C_G0463_v1.md#exact-resultant-content-collapse) | EVERY odd prime actual degree2q and fixed TOTAL measure; no assumed irreducibility of an arbitrary composition. |
| support | [Full residue projection](Yin_C_G0570_v1.md#projection-radical-block-control) | Actual ordinary residue-kernel mechanism; the odd anti-pairing, unequal lengths and every competitor are proved fully here. |
| support | [Algebraic Lagrange normalization](Yin_C_G0304_v1.md#canonical-trace-defect) | Only its separable monic coefficient interpolation identity, not its no-neutral dynamics or decay. |
| dependency | [Actual finite Salem inputs](Yin_C_G0515_v1.md#small-measure-norm-moment-controls) | Only the exact quartic/sextic/Lehmer trace and field-degree controls for the original finite15-window evidence. |
| support | [Original J77 evidence](../computations/programs/Yin_J_G0077/readme.md) | Full declared15-window native scope and separate whole computational finding, not the later proof-only boundary recurrence. |
| support | [Original L304](../ledger/Yin_L_G0304_v1.md#complete-retained-proof-and-review) | Complete first proof, original author/native/source and R203 frozen inputs; no source reinspection. |
| support | [Original L308](../ledger/Yin_L_G0308_v1.md#complete-retained-proof-and-review) | Complete second proof, actual pre-freeze correction/author and R207 original frozen input. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0785_v1.md#selected-edge-current-independent) | Entire exact current Statement and complete Argument, every original quantified input, complete proof chain/cost, actual finite versus universal evidence, source-depth/contribution/correction/negative limit; real independently reviewed arrangement and exact current bindings in R785. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0077](../computations/programs/Yin_J_G0077/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
