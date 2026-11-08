---
author: Yin
---

# Necessary variation within the order-27 fibers

<a id="fiber-screen"></a>
## A test on arbitrary positive units in the original orbit

Fix the canonical representative \(h_0\) from the [full ternary sign construction](../../../ledger/Yin_L_G0464_v8.md#integral-sign-representative) at \(p=6561,\ k=746\).
Multiply by an integral totally positive unit \(u\) on the full grid, preserving the absolute norm \(2^{1502}\).
Write \(y=-68/45,\ U_a(b)=2+T_a(b)\), with \(T_a(2\cos\theta)=2\cos(a\theta)\).
For \(3\nmid a\) the \(U_a\) are totally positive units with product one on every primitive layer, since \(2+T_a=|1+\zeta^a|^2\) and the odd prime-power cyclotomic polynomial evaluates to one at \(-1\).
The [gap check](../Yin_J_G0151/readme.md#next-conductor) gives \((b-y)h_0(b)>0\).
Any double-moment hit must meet the exact budget
\[
  \sum_b (4-b^2)|b-y|\,|h_0(b)|u(b)=p(L-yK)=p(128/15)=279936/5 .
\]
Denote this budget by \(S\).
No endpoint assumption enters this calculation.

On the three nodes of order 9, write \(\log u=d\log U_1+e\log U_2\).
This has a unique solution in real \(d,e\) because the three logarithmic vectors have sum zero over the nodes and the two-by-two minors of the last two vectors are nonzero, as the program checks with interval arithmetic.
For each order \(q=9,27\) and representative \(1\le j<q/2,\ 3\nmid j\), put \(b=2\cos(2\pi j/q)\) and
\[
 A_j(d,e)=(4-b^2)|b-y|\,|h_0(b)|\,U_1(b)^d U_2(b)^e .
\]
The three necessary inequalities \(A_j<S\) on order 9 bound a triangle in \((d,e)\), since the three normals sum to zero and have rank two.
Its vertices are the pairwise intersections of the boundary lines.
Outward rounding encloses it in \([-7,8]\times[530,545]\).

At order 27 let \(\tilde u_j=u(b)/(U_1(b)^dU_2(b)^e)\), group the nine nodes into fibers \(F\) by their image under \(T_3\), and write \(g_F=(\prod_{j\in F}\tilde u_j)^{1/3}\).
Each fiber has three members and \(\prod_F g_F=1\), by the three unit norms.
Put \(D_*=\max_{F,j\in F}g_F/\tilde u_j\) and
\[
  V(d,e)=3\left(\prod_F\sum_{j\in F} A_j(d,e)\right)^{1/3}.
\]
The actual order-27 mass is at least \(V(d,e)/D_*\) by the arithmetic-geometric mean over the three fibers.
For all feasible real \((d,e)\), certified subdivision gives \(V(d,e)/S\ge238\).
Since the mass contributed by order 27 alone is strictly below \(S\) at a hit, every hit in the original orbit requires **\(D_*>238\)**.
In particular the joint event is empty for all full-grid positive units whose residual factors \(\tilde u_j\) are constant on each order-27 fiber.
This covers arbitrary integer powers of \(U_1,U_2\) times any totally positive full-grid unit of the form \(v(T_3)\), and arbitrary additional positive unit factors that equal one on the order-9 and order-27 layers.
For these pullback units the common order-9 value is one by its layer norm.
On the integral exponent rectangle exactly 75 pairs have total order-9 mass below budget.
The least of the order-9 mass plus \(V\) on those pairs is between \(16822209.23\) and \(16822209.24\), attained at \((0,533)\).

<a id="lower-layer-control"></a>
## An integral adjustment that meets the first three layer budgets

A concrete word can reduce the combined mass of orders \(3,9,27\) below \(S\).
Start from \(h_0 U_1 U_2^{537}\) and multiply by
\[
 (U_8/U_1)^3(U_{10}/U_1)^{-3}(U_7/U_2)^{-1}(U_{11}/U_2)^6
 (U_5/U_4)^{-1}(U_{13}/U_4)^{-2}
 J_5(T_3)^{-124}J_7(T_3)^{-122},
\]
where \(J_k(X)=T_k(X)/X\) for odd \(k\).
Each ratio is a positive unit and the last two even powers preserve the signs and all layer norms.
The first six corrections equal one at orders 3 and 9, and the last two also equal one there.
The order-9 mass was minimized over the small integer rectangle, then the remaining exponents were chosen by rounding a real least-squares fit to the order-27 logarithmic masses and comparing neighboring integer choices.
For the fixed word, 45 times the three layer masses is exactly \(2208,4272,12960\), respectively.
Their sum divided by 45 is \(432\), below \(279936/5\).
Nevertheless the order-81 layer alone costs more than \(2^{704}S\).
The adjustment therefore fails the two target moments.

## Reproduction

Run the [certificate](fibers.py) with the same Python environment as the [main search](readme.md).

~~~text
python -B mathematics/computations/programs/Yin_J_G0152/fibers.py
~~~

The program solves the full sign system, groups the 1611 selected logarithmic factors by residue at each small conductor and subtracts exactly the even powers removed by the canonical construction.
It uses 160-bit real balls for cosines, logarithms and exponentials.
For the continuous bound it subdivides the rectangle into squares of side \(1/8\).
The signs of the affine log coefficients give a lower bound for each exponential at the minimizing corner.
After removing squares where the lower bound on the order-9 mass already exceeds \(S\), 4969 closed squares remain and the least certified lower integer for \(V/S\) is 238.
For the control word the signed products are layer traces after clearing 45, so identifying the unique integer in each interval recovers the exact masses.
