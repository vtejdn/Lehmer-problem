---
author: Yin
---

# The Baker–Wüstholz lower bound with variable heights

<a id="wus02-u001"></a>
<a id="logarithmic-form"></a>
## The ordinary complex logarithmic form

G. Wüstholz gives the quantitative Baker–Wüstholz theorem at the end of printed p. 5 and the start of p. 6 in §5 of the [2002 chapter](readme.md#cambridge-2002).
The inspection used these pages in the publisher's online PDF.
Let \(\alpha_1,\ldots,\alpha_s\) be algebraic numbers different from zero and one, choose a complex logarithm for each, and let \(D=[\mathbb Q(\alpha_1,\ldots,\alpha_s):\mathbb Q]\).
The author uses the logarithmic Weil height relative to that field, denoted here by \(h_K=D h_{\rm abs}\), where \(h_{\rm abs}\) is the [absolute logarithmic height](../Smy08/Yin_U001.md#smy08-height-normalization).
The two modified heights in the displayed bound are
\[
 h'(\alpha_i)=D^{-1}\max\{h_K(\alpha_i),|\log\alpha_i|,1\},\qquad
 h'(L)=D^{-1}\max\{h_K(L),1\}.
\]
For \(L(z)=\sum_{i=1}^s b_i z_i\), the \(b_i\) are integers, at least one is nonzero, and \(h_K(L)=D\log(\max_i|b_i|/g)\), where \(g=\gcd(|b_1|,\ldots,|b_s|)\).
In particular the coefficient height uses the primitive coefficient vector and applies to either sign and to positive integers.
If \(\Lambda=\sum_i b_i\log\alpha_i\ne0\), the theorem gives
\[
 \log|\Lambda|>-C(s,D)\,h'(L)\prod_{i=1}^s h'(\alpha_i),
 \qquad
 C(s,D)=18(s+1)!\,s^{s+1}(32D)^{s+2}\log(2sD).
\]
The stated hypotheses allow roots of unity other than one as arguments and arbitrary finite heights.
The bound is accepted from this coauthor's statement after checking both definitions, the field degree, the integer coefficients, the nonvanishing assumption and the constant.
The chapter attributes the proof to Baker and Wüstholz, *Logarithmic forms and group varieties* (1993), cited on printed p. 9.
The original proof was not reviewed.

<a id="unit-circle"></a>
## Distance of a power to one

The following specialization converts the source's lower bound on a logarithm into one on a distance.
Let \(\xi\ne0,1\) be algebraic of degree \(D\), let \(p\ge1\) be an integer, and suppose \(\xi^p\ne1\).
Use the principal argument \(-\pi<\arg\xi\le\pi\), take \(\log(-1)=i\pi\), and choose an integer \(k\) nearest to \(p\arg\xi/(2\pi)\).
Then \(\Lambda=p\log\xi-2k\log(-1)\ne0\), since exponentiation gives \(\xi^p\).
The coefficient magnitudes are bounded by \(p+1\le2p\), so \(h'(L)\le\max\{\log(2p),1/D\}\).
The local bound \(|\log|\xi||\le D h_{\rm abs}(\xi)\) follows by applying the height formula at the selected archimedean place to both \(\xi\) and \(\xi^{-1}\).
Thus \(h'(\xi)\le h_{\rm abs}(\xi)+\pi/D\) and \(h'(-1)=\pi/D\).
When \(|1-\xi^p|<1/2\), \(\Lambda\) equals the principal logarithm of \(\xi^p\), since its imaginary part lies in \([-\pi,\pi]\) and the disk excludes the negative real axis.
Integrating \(1/z\) along the segment from \(1\) to \(\xi^p\) gives \(|\Lambda|\le2|1-\xi^p|\).
In the complementary case \(-\log|1-\xi^p|\le\log2\), so in all cases
\[
 -\log|1-\xi^p|\le\log2+
 C(2,D)\bigl(h_{\rm abs}(\xi)+\pi/D\bigr)(\pi/D)
                  \max\{\log(2p),1/D\}.
\]
For \(|\xi|=1\) the original modified height also gives the sharper bound \(h'(\xi)\le\max\{D h_{\rm abs}(\xi),\pi\}/D\).
