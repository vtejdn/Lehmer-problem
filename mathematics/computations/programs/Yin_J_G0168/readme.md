---
author: Yin
---

# Powered-order exponents in the degree-ten Lehmer prime window

<a id="window"></a>
## Question and scope

Let \(\alpha\) be a root of the [degree-ten Lehmer polynomial](../../../claims/Yin_C_G0376_v2.md#irreducible-lehmer-radical-control)
\[
 P(x)=x^{10}+x^9-x^7-x^6-x^5-x^4-x^3+x+1 .
\]
For [Yin's Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract), take every prime \(p\) in \((y,2y]\), where \(y=\lceil(\log(3d))^4\rceil=134\) and \(d=10\).
Put \(O=\mathbb Z[\alpha]\), \(O'=\mathbb Z[\alpha^p]\), \(I_p=[O:O']\), and \(s_p=\exp(O/O')\) for its additive quotient.
The exponent enters the [constant-row upper bound](../../../claims/Yin_C_G0345_v376.md#statement), while \(I_p^{2/d}\) is the [average local lower bound](../../../ledger/Yin_L_G0462_v162.md#weights) for \(s_p\).
We also determine how much of \(\log I_p\) the [isolated-pair weight](../../../claims/Yin_C_G0345_v368.md#statement) \(E_p\) recovers at these same primes.

<a id="exact"></a>
## Exact indices and exponents

The table gives the integers \(a=I_p/s_p\) and the reduced rationals \(b=s_p^2/I_p\), so the two exact answers are \(s_p=ab\) and \(I_p=a^2b\).
The generated CSV gives both as ordinary integers.

| \(p\) | \(a\) | \(b\) |
| ---: | ---: | ---: |
| 137 | 1954496295630970177134505691129860039 | 28055812151 |
| 139 | 1653600731305632646031390675092388167 | 136454909 |
| 149 | 333649541363848786356761358990240482674259 | 686161391 |
| 151 | 28375876999957913855873490239525064537529 | 129496204459 |
| 157 | 23334228053447803023088245898232473723928189 | 215100754501 |
| 163 | 35961754210266685969364975675679421217441701 | 471860394823 |
| 167 | 3570678049215242715628212241307944272357270391 | 217868429123 |
| 173 | 23798599292339515401269425014605263274257946113 | 2539996587599 |
| 179 | 65280379647022387564657795816589789678988827371 | 48678198582203 |
| 181 | 133194548607675655571209849336481553344467228794491 | 3059801310857 |
| 191 | 722325698083316093759407947213457551173548156803613 | 360429381874489 |
| 193 | 34154965142318778725697329496015299307334388503030442977 | 237757859 |
| 197 | 250133073719088714704407335909528895047609713184462101 | 114399402512303 |
| 199 | 216032304983449443388966345214981942624671056547105537 | 935150377557569 |
| 211 | 23060494466672982087610981558565718319629709028968010336039 | 2551225938433087 |
| 223 | 134870618100131817980132173589081315832515841992230714598397749 | 365767376899471 |
| 227 | 1404481706815551309658742531146614663607201934749460737311233 | 6213019124006477 |
| 229 | 74962899112521900544794080112765327922980251401276969162295575927 | 40063771846499/457 |
| 233 | 35224286397142815645132038351438950689504700256791234313627892559 | 88140690538257571 |
| 239 | 2657647887003570582861670955077549258521507050902587266523157116881 | 120787766193734303 |
| 241 | 14315033192309489573034566621612617530401098047488967940484316993649 | 32561084069144531 |
| 251 | 11104287249215277369287443029610203702868724772247852319762653820515247 | 440273206613701313 |
| 257 | 570377567968528927331603733977872155678186042377554895668473658967856180649 | 308534647439 |
| 263 | 4030995652635288833306917069359978118657707083503452280878796790328325871 | 26157448295241378013 |

The minimum of \(\log(s_p)/p\) is attained uniquely at \(p=139\) and is approximately \(0.734730383456412\).
The maximum is attained uniquely at \(p=263\) and is approximately \(0.805668462945689\).
The concentration ratio \((\log(s_p)/p)/(2\log(I_p)/(dp))=5\log s_p/\log I_p\) has its unique minimum at \(p=193\), approximately \(2.675316508621504\), and its unique maximum at \(p=179\), approximately \(2.818853193633711\).
Thus throughout this window the exponent rate exceeds the average local lower bound by a factor greater than \(2.67\).
For this input none of the 24 primes has \(I_p=1\).
The constant-row upper construction alone does not determine the minimum resultant over all rows.

<a id="arithmetic"></a>
## Power-basis calculation and determinantal check

For \(\beta=\alpha^p\) form the integral matrix \(M\) whose column \(j\) consists of the coefficients of \(x^{pj}\bmod P\) in increasing powers, \(0\le j<10\).
The program obtains successive columns from a table constructed by multiplication by \(x\) and monic reduction.
It row reduces the augmented matrix \([M\mid 1_{10}\mid \beta^{10}]\) over the rationals, with the last column also expressed in the \(\alpha\)-basis.
All 24 determinants were nonzero, so \(\mathbb Q(\beta)=\mathbb Q(\alpha)\) and the columns are the power basis of \(O'\) in \(O\).
The absolute determinant gives \(I_p\).
The condition \(sO\subseteq O'\) is equivalent to \(sM^{-1}\) being integral, giving \(s_p\) as the least common multiple of all entry denominators.
The last augmented column gives the ten lower coefficients, with signs reversed, of the monic minimal polynomial \(Q\) of \(\beta\).

A second implementation constructs each column separately by long division of the individual monomial, then uses integer expansion by minors.
For each prime it recalculates the determinant and the gcd of all 100 minors of order nine.
The adjugate identity gives \(s_p=|\det M|/\gcd(\text{all minors of order nine})\), agreeing at every prime with rational elimination.
Both checks are executed by the program.
For the window, the ordering of rates, and the cofactor bounds below, rational interval arithmetic uses the two neighboring numbers around each correctly rounded 50-digit decimal logarithm.
The extremal primes are separated by disjoint intervals and the displayed decimals approximate the exact logarithmic quantities.

<a id="isolated"></a>
## Isolated pairs and double-root witnesses

In a polynomial expansion \(Q(X+T)\) let \(Q^{[2]}(X)\) be the coefficient of \(T^2\).
At a triple root modulo any prime, \(Q,Q'\) and \(Q^{[2]}\) all vanish.
Thus a prime at which \(Q\) has such a root divides both \(\operatorname{Res}(Q,Q^{[2]})\) and \(\operatorname{Res}(Q,Q^{[2]}+Q')\).
The program computes each needed resultant as a determinant of multiplication in the power basis modulo \(Q\).
It finds \(|\operatorname{disc}P|=1332031009\) by the same determinant formula applied to \(P'\).
For all 24 primes, \(\gcd(I_p,p\,\operatorname{disc}P)=1\) and
\[
 \gcd\!\left(I_p,\operatorname{Res}(Q,Q^{[2]}),
                      \operatorname{Res}(Q,Q^{[2]}+Q')\right)=1 .
\]
When the first two arguments already give one the second resultant can be skipped.
In particular every \(\ell\mid I_p\) has distinct original residues, differs from \(p\), and has at most two powered roots in any one residue.
At such a prime every positive pair depth is isolated throughout its length, so its full Vandermonde valuation enters \(E_p\).
The other good primes contribute zero by the [finite index decomposition](../../../claims/Yin_C_G0345_v368.md#depth).
Consequently \(E_p=\log I_p\) for every listed prime, and the actual stripped row resultant \(H\) of any two nonzero coprime integral Laurent rows in distinct classes modulo \(p\) giving a multiple of \(P^2\) satisfies \(\log H\ge4\log I_p\).

For a primitive ordinary witness of degree at most \(p(16d+1)=161p\), the sum of the stripped row degrees is at most \(321\), since at most one row has residue zero.
Let \(R\) be the product with multiplicity of the primitive noncyclotomic irreducible factors of \(F/P^2\), omitting \(x\), and let \(m=\log M\).
All 24 support primes are prime to \(\operatorname{disc}P\), so their [separate contribution](../../../ledger/Yin_L_G0462_v152.md#resultant) adds \(10\log p\) to \(4\log I_p\).
In the [resultant-to-measure bound](../../../claims/Yin_C_G0345_v366.md#arithmetic), the constant \(C\) is at most \(2\) by \(\sin(\pi t)\ge2\min(t,1-t)\) on \([0,1]\).
The Salem input has \(m(P)<\log(6/5)\) since \(P(1)=-1\), \(P(6/5)=6762031/9765625>0\) and it has only one real root greater than one.
We therefore obtain the finite inequality
\[
 m(R)\ \ge\ (1-4/p)\frac{4\log I_p+10\log p}{321}
            -2\log(6/5)-\frac2p\log(322p).
\]
The right side exceeds \(1.87\) throughout the window and \(4.37\) at \(p=263\).
These bounds apply to every witness under the stated assumptions and concern this one input and finite window.

## Files and reproduction

The [program](window.py) uses Python 3.9 or later and its standard library.
The independent long-division and minor-expansion routines are reused from [J167](../Yin_J_G0167/checks/maximal_minors.py).
From the repository root run

~~~~powershell
python -B mathematics/computations/programs/Yin_J_G0168/window.py
~~~~

The program enumerates primes by trial division, computes both lattice invariants by both methods, checks the collision and measure bounds, and regenerates the [24-row CSV](inputs/window.csv) from these inputs.
Compare a new run's 24 rows in `mathematics/computations/outputs/Yin_J_G0168/window.csv` with this fixed table.
The CSV contains the full integers, the normalized logarithms, their ratio, the portion of the index left after removing exceptional primes, and the common divisor detecting possible triple roots.
