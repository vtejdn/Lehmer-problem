"""Independent rational checks of margins used in Ope26 Section 6/Appendix A.

These check displayed constants, not the entire analytic reduction.
All arithmetic is exact Fraction arithmetic; no floating-point inputs.
"""
from fractions import Fraction as F

def check(name, predicate):
    assert predicate, name
    print('PASS:', name)

x=F(199,1000)
cost=(1+2*x**4/(1-x*x))**18*(1+2*x**3/(1-x*x))-1
check('admissible pattern cost below .081', cost<F('0.081'))
check('mean damping below .101', F('.081')/(21*x*x*(1-F('.081')/3))<F('.101'))
check('cubic log-loss C*x below .136', (2*x/3)**2<F('.136')**2*(1-x*x))
check('stationary mean rate above .000222', F(21,22)*(2*F('.000210')-F('1.237')*F('.000145')-F('.000007'))>F('.000222'))
beta=F('1.8392')
check('recurrence perturbation below .005', beta**(-9)/(beta-1)<F('.005'))
check('slow-frequency perturbation below .025', 5*beta**(-9)/(beta-1)<F('.025'))
check('lower fast tail below 1.192', 1/(beta-1)<F('1.192'))
check('separated block tail below .649', 1/(beta*(beta-1))<F('.649'))
check('forbidden-state frequency retains .1 margin', beta*(beta-1)-F('.005')-F('1.192')-F('.025')>F('.1'))
check('nonterminal-state frequency retains .1 margin', beta-1-F('.005')-F('.649')-F('.025')>F('.1'))
r=F('.994')
check('negative omitted-product error below 5e-8', F('3.142')**2*200**2/2*r**5994/(1-r*r)<F(5,10**8))
check('real-root omitted-tail error below 1e-20', F('3.142')*8*F('.545')**100/(1-F('.545'))<F(1,10**20))
a=F('.9999')
check('weak geometric denominators exceed .00019', 1-a*a>F('.00019'))
penalty=sum(F('.11')**d/(f*(1-a**d)) for d,f in [(2,2),(4,12),(6,45)])
check('weak-tail truncated penalty below 31', penalty<31)
check('log-cosine tail remainder below 3e-6', F('.1')*F('.11')**8/(1-a**8)<F(3,10**6))
check('combined stated moment error below 3.055e-6', F(3,10**6)+F(5,10**8)+F(4,10**9)+F(3,10**11)+F(1,10**20)<F('0.000003055'))
check('upper-rounding factors bound denominators', F('1.002')**2*(1-F('.06')**2)>1 and F('1.004')*(1-F('.06')**2)>1)
check('anisotropy bound below .000007', F('.000116')*F('.011')+2*F('.012')*F('.011')*F('.015')+F('.012')**2*F('.0032')<F('.000007'))
check('cover exponent retains 6.6e-6 saving', F('.000216')-F('.0002094')==F('.0000066'))
print('PASS: all independent rational margin checks passed.')
