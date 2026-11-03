"""Bounded exact factorization and Mahler exclusion for L G0048 r_g.

Run from repository root with .venv/Scripts/python.exe -B followed by this
path. Only g in (3,4,5,8,16,32) are allowed. JSON is updated after each
parameter and prior retained parameter results are preserved. NumPy root
probes are exploratory. Graeffe coefficient inequalities are exact.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import argparse
import json
import math

import numpy as np
import sympy as sp

t = sp.symbols('t')
ALLOWED = (3, 4, 5, 8, 16, 32)
OUT = (_J_OUTPUT / 'result.json')
TOL = 1e-7


def coefficients(poly):
    return [int(poly.nth(j)) for j in range(poly.degree()+1)]


def cyclotomic_order(poly):
    if not poly.is_cyclotomic:
        return None
    d = poly.degree()
    # phi(m)^2 >= m/2 gives this exhaustive finite bound.
    for m in range(1, 2*d*d+1):
        if sp.totient(m) == d and sp.Poly(sp.cyclotomic_poly(m,t),t) == poly:
            return m
    raise AssertionError('Cyclotomic order not found within proven bound')


def numeric_probe(poly):
    coeff = np.array(poly.all_coeffs(), dtype=np.float64)
    roots = np.roots(coeff)
    moduli = np.abs(roots)
    residuals = []
    for z in roots:
        denominator = float(np.polyval(np.abs(coeff), abs(z)))
        residuals.append(float(abs(np.polyval(coeff,z))/denominator))
    return {
        'status': 'exploratory_only_no_root_enclosures',
        'algorithm': 'numpy.roots companion-matrix eigenvalues',
        'dtype': 'complex128; float64 coefficients; 53-bit significand',
        'unit_modulus_tolerance': TOL,
        'mahler_estimate': float(math.exp(sum(math.log(max(1.0,float(x))) for x in moduli))),
        'expanding_count_above_1_plus_tolerance': int(sum(moduli > 1+TOL)),
        'contracting_count_below_1_minus_tolerance': int(sum(moduli < 1-TOL)),
        'near_unit_count': int(sum(abs(moduli-1) <= TOL)),
        'maximum_modulus': float(max(moduli)),
        'maximum_normalized_residual': max(residuals),
        'roots_real_imag': [[float(z.real),float(z.imag)] for z in roots],
    }


def square_coefficients(a):
    out = [0]*(2*len(a)-1)
    for i,x in enumerate(a):
        if x:
            out[2*i] += x*x
            for j in range(i+1,len(a)):
                if a[j]:
                    out[i+j] += 2*x*a[j]
    return out


def graeffe(a):
    # P(t)=E(t^2)+t O(t^2); G(P)=(-1)^degree [E(t)^2-t O(t)^2].
    e, o = square_coefficients(a[::2]), square_coefficients(a[1::2])
    out = [0]*len(a)
    for j,x in enumerate(e): out[j] += x
    for j,x in enumerate(o): out[j+1] -= x
    if out[-1] == -1:
        out = [-x for x in out]
    assert out[-1] == 1 and len(out) == len(a)
    return out


def lower_certificate(poly, target):
    num, den = target
    a = coefficients(poly)
    d = len(a)-1
    checks = []
    for s in range(13):
        exponent = 2**s
        best = max(range(d+1), key=lambda j: sp.Rational(abs(a[j]),math.comb(d,j)))
        coefficient = abs(a[best])
        divisor = math.comb(d,best)
        left = coefficient*den**exponent
        right = divisor*num**exponent
        passed = left > right
        checks.append({'iteration':s,'coefficient_index':best,
                       'absolute_coefficient':str(coefficient),
                       'binomial_divisor':str(divisor),'strict_comparison':passed})
        if passed:
            return {'status':'strict_lower_certified','target_numerator':num,
                    'target_denominator':den,'degree':d,'iteration':s,
                    'comparison_exponent':exponent,'coefficient_index':best,
                    'absolute_coefficient':str(coefficient),'binomial_divisor':str(divisor),
                    'left_integer':str(left),'right_integer':str(right),
                    'graeffe_coefficients_ascending':[str(x) for x in a],
                    'iteration_checks':checks,
                    'inference':'|a_k(G^s P)|/binomial(d,k) <= M(P)^(2^s); left > right gives M(P) > num/den'}
        if s<12:
            a = graeffe(a)
    return {'status':'not_certified_within_12_iterations','target_numerator':num,
            'target_denominator':den,'iteration_checks':checks}


def certificate_target(probe):
    measure = probe['mahler_estimate']
    for num,den in ((4,3),(133,100),(53,40)):
        if measure > num/den+1e-4:
            return num,den
    return None


def one_parameter(g):
    r = sp.Poly(sum((-1)**j*t**(g*j) for j in range(7))-t**(2*g+1)-t**(4*g-1),t,domain=sp.ZZ)
    q = sp.Poly(t**(7*g)+1-t**(2*g+1)-t**(5*g-1)-t**(3*g+1)-t**(4*g-1),t,domain=sp.ZZ)
    assert r*sp.Poly(t**g+1,t) == q
    content,factors = sp.factor_list(r)
    assert content == 1
    reconstructed = sp.Poly(1,t)
    factor_records = []
    for p,multiplicity in factors:
        reconstructed *= p**multiplicity
        order = cyclotomic_order(p)
        probe = numeric_probe(p)
        record = {'degree':p.degree(),'multiplicity':multiplicity,
                  'coefficients_ascending':coefficients(p),
                  'factorization_scope':'irreducible factor from exact SymPy factor_list over ZZ',
                  'cyclotomic_order':order,'numerical_probe_only':probe}
        if order is None:
            target = certificate_target(probe)
            if target:
                record['mahler_lower_certificate'] = lower_certificate(p,target)
        factor_records.append(record)
    assert reconstructed == r
    whole_probe = numeric_probe(r)
    result = {'g':g,'degree':r.degree(),'r_coefficients_ascending':coefficients(r),
              'q_coefficients_ascending':coefficients(q),
              'exact_product_identity_checked':True,'factorization_product_checked':True,
              'factorization_content':int(content),'factors':factor_records,
              'whole_numerical_probe_only':whole_probe}
    if len(factors)==1 and factors[0][1]==1:
        result['whole_mahler_lower_certificate_same_as_factor_index'] = 0
    else:
        target = certificate_target(whole_probe)
        if target:
            result['whole_mahler_lower_certificate'] = lower_certificate(r,target)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--g',type=int,nargs='+',default=list(ALLOWED),choices=ALLOWED)
    args = parser.parse_args()
    payload = json.loads(OUT.read_text(encoding='utf-8')) if OUT.exists() else {}
    payload.update({'question':'Finite r_g factorization and strict Mahler lower certificates; not a claim for untested g',
                    'allowed_parameters':list(ALLOWED),
                    'coefficient_order':'ascending exponents; large certificate integers serialized as decimal strings',
                    'numeric_warning':'Numerical roots, measures and expanding counts are exploratory only',
                    'lower_threshold_above_plastic_check':{
                        'threshold':[4,3],'f_at_threshold':'1/27',
                        'reason':'x^3-x-1 is increasing for x>=1 and has one positive root theta_0'}})
    payload.setdefault('parameters',{})
    for g in args.g:
        print(f'BEGIN g={g}',flush=True)
        result = one_parameter(g)
        payload['parameters'][str(g)] = result
        OUT.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
        summary = {'g':g,'factor_degrees':[f['degree'] for f in result['factors']],
                   'cyclotomic_orders':[f['cyclotomic_order'] for f in result['factors']],
                   'measure':result['whole_numerical_probe_only']['mahler_estimate'],
                   'expanding_count':result['whole_numerical_probe_only']['expanding_count_above_1_plus_tolerance'],
                   'certificate_status':[f.get('mahler_lower_certificate',{}).get('status') for f in result['factors']]}
        print(json.dumps(summary),flush=True)


if __name__ == '__main__':
    main()
