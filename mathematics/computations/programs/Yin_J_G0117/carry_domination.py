from collections import Counter
from fractions import Fraction
from math import comb
import json
import platform

def next_digit_law(law, lower_coefficients, modulus=None):
    d = len(lower_coefficients)
    result = Counter()
    for vector, mass in law.items():
        top = vector[-1]
        shifted = tuple((vector[i-1] if i else 0)
                        - top*lower_coefficients[i] for i in range(d))
        for digit in (0,1):
            value = (shifted[0]+digit,) + shifted[1:]
            if modulus is not None:
                value = tuple(x % modulus for x in value)
            result[value] += mass
    return result

p = (1,-1,-1,-1)
law = Counter({(0,0,0,0): 1})
mod_law = law.copy()
rows = []
for n in range(17):
    assert sum(law.values()) == sum(mod_law.values()) == 2**n
    exact = Fraction(sum(x*x for x in law.values()), 4**n)
    modular = Fraction(sum(x*x for x in mod_law.values()), 4**n)
    upper = Fraction(3,4)**(n//2)
    assert exact <= modular and modular >= Fraction(1,16)
    assert exact <= upper
    if n in (0,2,4,8,12,16):
        rows.append({"n":n, "support":len(law), "q":str(exact),
                     "q_mod_2":str(modular), "block_bound":str(upper)})
    if n < 16:
        law = next_digit_law(law,p)
        mod_law = next_digit_law(mod_law,p,2)

for n in range(65):
    exact = Fraction(comb(2*n,n),4**n)
    killed = Fraction(1,2)**n
    assert exact >= Fraction(1,2*n+1)
    assert exact / killed >= Fraction(2**n,2*n+1)

print(json.dumps({
    "python":platform.python_version(),
    "quartic_exact_checks":"n=0..16 passed",
    "cyclotomic_truncation_checks":"n=0..64 passed",
    "quartic_rows":rows,
},indent=2))
