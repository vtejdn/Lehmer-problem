---
author: Yin
---

# G0001: an adopted interior criterion and an exact small-core control beyond its threshold

Date: 2026-10-07.
Synthesis by assigned AI ms25_source for Yin from [HS16-U001](../audits/literature/HS16/Yin_U001.md#hs16-u001), [L G0039's degree-22 unit](Yin_L_G0039_v1.md#degree22-small-core-counterexample), and the exact root-isolation certificate prepared by the coordinator and independently verified below.
The conclusion is failure of a particular sufficient interior condition, not absence of interior or positive volume.

<a id="entropy-dimension-interior-threshold"></a>
## The adopted theorem in algebraic-entropy coordinates

Let p be a monic irreducible integral unit polynomial with M(p)>1.
Let U be its full expanding real Minkowski space, and let r=dim_R U: a real expanding conjugate contributes one dimension and a nonreal conjugate pair contributes two.
Let A be multiplication by the algebraic unit on U, and let v be the image of 1.
Define

    S(A,v)={sum_(j>=1) epsilon_j A^(-j)v : epsilon_j in {0,1}}.

All eigenvalues of A have modulus greater than one.
Distinct conjugates give cyclicity of v by the Vandermonde determinant; the same is true for A^(-1).
Moreover

    |det A|=product_(|alpha|>1)|alpha|=M(p).

The adopted HS16 statement, with the scope and repaired endpoint-path step in HS16-U001, asserts interior for the contracting binary attractor when the contraction determinant is at least 2^(-1/r).
Its r=1 version is the elementary scalar interval case.
With B=A^(-1), its attractor is

    T(B,v)={sum_(j>=0) epsilon_j B^j v},
    S(A,v)=A^(-1) T(B,v).

The invertible linear map preserves interior.
Hence the sufficient condition becomes

    M(p)^r<=2,
    equivalently r*m(p)<=log 2,       m(p)=log M(p).   (1)

This conversion retains the entire expanding real dimension, not just the positive real place.
The source dependency is HS16-U001's adopted Theorem 1.1, including its stated connectedness input and replacement for the source's overly broad path-sum proposition; this application does not enlarge that adoption.

Interior implies positive r-dimensional volume.
Under [L G0035's support interface](Yin_L_G0035_v1.md#positive-volume-support-interface), this captures the full algebraic entropy m(p) in binary support growth.
It does not supply the same lower bound for Shannon entropy or maximum-atom entropy.
Condition (1) is a sufficient geometric condition, not a positive lower bound on m(p).

<a id="degree22-interior-threshold-control"></a>
## The retained degree-22 reciprocal unit

Put

    q(t)=t^24-t^17-t^12-t^7+1,
    Phi_6(t)=t^2-t+1,
    p(t)=q(t)/Phi_6(t).

L G0039 proves by exact identities, finite-field irreducibility, field arguments and a rational Sturm count that p is an irreducible reciprocal unit of degree 22, with all-power degree preservation and M(p)<theta_0.
Its unique largest-modulus conjugate is a positive root lambda>1.
It has exactly three expanding conjugates, consisting of lambda and one nonreal conjugate pair.
Thus its expanding real dimension is r=3.

We prove exactly that

    M(p)^3>2.                                       (2)

Consequently the sufficient condition (1) does not decide interior for this actual small reciprocal, multiple-expanding control.
The proof below uses no floating-point root location or unproved rounding bound.
A numerical probe can guide the choice of rational disk; it is not proof evidence for (2).

## One nonreal root in a certified rational disk

Take

    c=(-94095-52062 i)/100000,
    eta=1/100000,
    q(c+w)=sum_(j=0)^24 a_j w^j,
    a_j=q^(j)(c)/j! in Q(i).

For a Gaussian rational z=x+iy, put |z|_1=|x|+|y|.
Define exact rational quantities

    U=|a_0|_1+sum_(j=2)^24 |a_j|_1 eta^j,
    L=max(|Re a_1|,|Im a_1|) eta.

The retained certificate lists every a_j and the exact summands of U and L.
The coordinator's standard-library calculation and the independent SymPy reconstruction agree on these values; the latter additionally verifies the particularly simple exact brackets

    U<19/100000<31/100000<L.                          (3)

For |w|=eta, the triangle inequality and |z|<=|z|_1 give

    |q(c+w)-a_1 w|<=U<L<=|a_1| eta=|a_1 w|.

In particular a_1 is nonzero.
Rouche's theorem compares q(c+w) with a_1 w and gives exactly one root beta, counted with multiplicity, in the open disk |z-c|<eta.
The coefficients of q are real, so the conjugate disk contains the conjugate root.
The disks are disjoint and avoid the real line because |Im c|>eta.

Every point beta in the first disk satisfies the strict coordinate bounds

    |Re beta|>94094/100000,
    |Im beta|>52061/100000.

Both lower coordinates are positive.
Thus

    |beta|^2>
      (94094/100000)^2+(52061/100000)^2
      =11564028557/10000000000>1.                    (4)

The two certified roots therefore lie strictly outside the unit circle.
They cannot be roots of Phi_6, so they are roots of p.
This inference depends on a strict open-disk certificate, not on displayed decimal approximations.

## The positive root and the strict Mahler lower bound

Take lambda_0=2727/2500>1.
Exact evaluation gives

    q(lambda_0)=
      -18898970932408885735109939653013949631370342753796650746438919341455788197728959
       /3552713678800500929355621337890625000000000000000000000000000000000000000000000000
      <0.                                            (5)

By L G0039, q has a unique positive root above one, namely lambda; since q tends to positive infinity, (5) implies lambda>lambda_0.
Again lambda is a root of p because Phi_6 has no root outside the unit circle.

The three distinct expanding roots give

    M(p)>=lambda |beta|^2
       >(2727/2500)(11564028557/10000000000)
       =31535105874939/25000000000000=:L_M.           (6)

For this lower bound it is enough that these three expanding roots exist; the complete expanding-root count from L G0039 is not being inferred from a numerical scan.
The exact rational check

    L_M^3-2=
      110492920411956326344758731902507398019
       /15625000000000000000000000000000000000000
      >0                                             (7)

proves (2).
In particular 3*m(p)>log 2, so the adopted theorem's hypothesis fails at the actual dimension r=3.

## Consequence and proof boundaries

The control meets the structural scope important for G0001: an irreducible small reciprocal unit, several expanding conjugates, and no degree collapse under powers.
Nevertheless this dimension-dependent sufficient theorem does not settle its interior.
Equations (2)--(7) exclude application of condition (1) to this input; they do not assert that S(A,v) has empty interior, zero volume, or any particular weighted entropy.

Nor does the failure contradict HS16: its implication runs from the determinant condition to interior, and no converse is adopted.
Further progress for this control requires a different sufficient criterion or a direct geometric argument.
The source threshold and this isolated input do not give a uniform Mahler gap.

## Native evidence, review and current proof home

The complete original code, retained mathematical outputs, exploratory-versus-exact roles and reproduction instructions remain at [J4](../computations/programs/Yin_J_G0004/readme.md).
The original synthesis/certificate contributor inspections and actual2026-10-07 executions are retained at [R528](../audits/reviews/Yin_R_G0528_v1.md#original-threshold-contributor-finding); separate algorithms do not establish whole-proof agent isolation.
The complete current exact statement and proof are [C258](../claims/Yin_C_G0258_v1.md#argument), adopted after the actual [whole current self-check and read-only verifier recheck](../audits/reviews/Yin_R_G0528_v1.md#current-complete-threshold-control-finding).
The theorem’s failed sufficient condition remains distinct from any necessity, empty-interior or weighted-entropy claim.
