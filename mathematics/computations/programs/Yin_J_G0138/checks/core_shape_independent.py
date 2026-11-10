"""Independent finite verification of the fixed J138 quotient and controls.

Integer lists implement Mobius-product generation, monic division, triangular reciprocal trace conversion and positive-pivot pseudo-remainder counting.
No author program or counting function is imported or executed.
The existing FLINT backend is used only for the separate exact factorization and fresh 256-bit all-root measure check.
Irreducibility and root isolation retain the trusted FLINT/Arb implementation boundary.
Run from the repository root with Python 3.14 and -B.
"""

import ast
from fractions import Fraction as F
import json
import math
from pathlib import Path
import platform
import re
import sys

HERE = Path(__file__).resolve().parents[1]
OUT = HERE.parent.parent / "outputs" / HERE.name
PACKAGES = HERE.parent.parent / "outputs" / "Yin_J_G0156" / "packages"
BLOCK = [(1,2),(2,2),(3,1),(4,1),(5,1),(6,1),(8,1),(10,1),(12,1),(24,1)]


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def multiply(a,b):
    result = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            result[i+j] += x*y
    return trim(result)


def monic_division(a,b):
    assert b[-1] == 1
    remainder = list(a)
    quotient = [0]*max(0,len(a)-len(b)+1)
    while len(remainder) >= len(b):
        shift,value = len(remainder)-len(b),remainder[-1]
        quotient[shift] = value
        for j,coefficient in enumerate(b):
            remainder[shift+j] -= value*coefficient
        remainder = trim(remainder)
    assert not remainder
    quotient = trim(quotient)
    assert multiply(quotient,b) == a
    return quotient


def mobius(n):
    sign = 1
    prime = 2
    while prime*prime <= n:
        if n % prime == 0:
            n //= prime
            sign = -sign
            if n % prime == 0:
                return 0
        prime += 1
    return -sign if n > 1 else sign


def cyclotomic(n):
    numerator = denominator = [1]
    for divisor in range(1,n+1):
        if n % divisor:
            continue
        sign = mobius(n//divisor)
        if not sign:
            continue
        polynomial = numerator if sign == 1 else denominator
        product = [0]*(len(polynomial)+divisor)
        for j,value in enumerate(polynomial):
            product[j] -= value
            product[j+divisor] += value
        if sign == 1:
            numerator = product
        else:
            denominator = product
    return monic_division(numerator,denominator)


def generate(n,block):
    numerator = cyclotomic(n)
    assert (len(numerator)-1) % 2 == 0
    numerator[(len(numerator)-1)//2] -= 1
    divisor = [1]
    for order,power in block:
        for _ in range(power):
            divisor = multiply(divisor,cyclotomic(order))
    quotient = monic_division(numerator,divisor)
    assert quotient == quotient[::-1] and quotient[0] == quotient[-1] == 1
    return numerator,divisor,quotient


def lift(trace):
    d = len(trace)-1
    result = [0]*(2*d+1)
    for j,c in enumerate(trace):
        for k in range(j+1):
            result[d+j-2*k] += c*math.comb(j,k)
    return result


def extract_trace(polynomial):
    assert polynomial == polynomial[::-1] and (len(polynomial)-1)%2 == 0
    d = (len(polynomial)-1)//2
    remainder = list(polynomial)
    result = [0]*(d+1)
    for j in range(d,-1,-1):
        result[j] = remainder[d+j]
        for k in range(j+1):
            remainder[d+j-2*k] -= result[j]*math.comb(j,k)
    assert not any(remainder) and lift(result) == polynomial
    return result


def primitive(a):
    a = trim(a)
    if not a:
        return []
    content = math.gcd(*a)
    assert content > 0
    return [value//content for value in a]


def positive_remainder(a,b):
    """Return a positive scalar multiple of the ordinary remainder.

    Every cancellation replaces R by abs(lc(B))*R-sign(lc(B))*lc(R)*t^j*B.
    Positive content division preserves R = positive_scalar*A mod B.
    The terminating degree condition therefore proves the required positive-scalar relation without rational polynomial division.
    """
    remainder = primitive(a)
    pivot = abs(b[-1])
    sign = 1 if b[-1] > 0 else -1
    while len(remainder) >= len(b):
        old_length = len(remainder)
        shift,top = len(remainder)-len(b),remainder[-1]
        remainder = [pivot*value for value in remainder]
        for j,value in enumerate(b):
            remainder[shift+j] -= sign*top*value
        remainder = primitive(remainder)
        assert len(remainder) < old_length
    return remainder


def evaluate(a,x):
    value = 0
    for coefficient in reversed(a):
        value = value*x+coefficient
    return value


def sgn(x):
    return (x > 0)-(x < 0)


def sturm(poly):
    derivative = [j*value for j,value in enumerate(poly)][1:]
    chain = [primitive(poly),primitive(derivative)]
    while True:
        remainder = positive_remainder(chain[-2],chain[-1])
        if not remainder:
            break
        chain.append([-value for value in remainder])
    assert len(chain[-1]) == 1
    signs = {
        "-infinity":[sgn(p[-1])*(-1)**(len(p)-1) for p in chain],
        "-2":[sgn(evaluate(p,-2)) for p in chain],
        "2":[sgn(evaluate(p,2)) for p in chain],
        "+infinity":[sgn(p[-1]) for p in chain]}
    variations = {}
    for key,values in signs.items():
        values = [v for v in values if v]
        variations[key] = sum(a != b for a,b in zip(values,values[1:]))
    return {"degrees":[len(p)-1 for p in chain],"signs":signs,"variations":variations,
            "last_nonzero_gcd_degree":0}


def shape(poly,record):
    chain = sturm(poly)
    assert evaluate(poly,-2) and evaluate(poly,2)
    assert record["trace_coefficients_ascending"] == poly
    assert record["trace_degree"] == len(poly)-1
    assert record["endpoint_values"] == [evaluate(poly,-2),evaluate(poly,2)]
    assert len(record["squarefree_components"]) == 1
    component = record["squarefree_components"][0]
    assert component["coefficients_ascending"] == poly and component["multiplicity"] == 1
    assert component["sturm_degrees"] == chain["degrees"]
    assert component["sturm_signs"] == chain["signs"]
    assert component["variations"] == chain["variations"]
    v = chain["variations"]
    real,inside = v["-infinity"]-v["+infinity"],v["-2"]-v["2"]
    nonreal = len(poly)-1-real
    counts = {"real_trace_roots":real,"trace_roots_in_minus2_2":inside,
              "real_trace_roots_outside":real-inside,"nonreal_trace_roots":nonreal,
              "complete_exterior_roots":nonreal+real-inside,
              "complete_interior_roots":nonreal+real-inside,"complete_unit_circle_roots":2*inside}
    assert 0 <= inside <= real <= len(poly)-1 and nonreal%2 == 0
    assert all(record[key] == value for key,value in counts.items())
    return {"trace_coefficients_ascending":poly,"endpoint_values":record["endpoint_values"],
            **chain,**counts,"every_author_chain_entry_matched":True}


def bareiss(matrix):
    a = [row[:] for row in matrix]
    last,sign = 1,1
    for k in range(len(a)-1):
        pivot_row = next(i for i in range(k,len(a)) if a[i][k])
        if pivot_row != k:
            a[k],a[pivot_row] = a[pivot_row],a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator % last == 0
                a[i][j] = numerator//last
            a[i][k] = 0
        last = pivot
    return sign*a[-1][-1]


def discriminant_monic(poly):
    derivative = [j*value for j,value in enumerate(poly)][1:]
    m,n = len(poly)-1,len(derivative)-1
    rows = []
    for coefficients,repeats in ((poly,n),(derivative,m)):
        for shift in range(repeats):
            rows.append([0]*shift+coefficients[::-1]+[0]*(m+n-shift-len(coefficients)))
    return (-1)**(m*(m-1)//2)*bareiss(rows)


def rational_ball(text):
    match = re.fullmatch(r"\[([+\-0-9.eE]+) \+/- ([+\-0-9.eE]+)\]",text)
    if match:
        midpoint,radius = map(F,match.groups())
        assert radius >= 0
        return midpoint-radius,midpoint+radius
    value = F(text)
    return value,value


def dyadic(endpoint):
    mantissa,exponent = endpoint
    return F(mantissa*2**max(0,exponent),2**max(0,-exponent))


def factor_and_measure(quotient,exact_shape):
    sys.path.insert(0,str(PACKAGES))
    import flint
    from flint import fmpz_poly,arb,ctx
    ctx.prec,ctx.threads = 256,1
    p = fmpz_poly(quotient)
    content,factors = p.factor()
    assert int(content) == 1 and len(factors) == 1
    factor,power = factors[0]
    assert int(power) == 1 and list(map(int,factor)) == quotient
    factor_record = json.loads((OUT/"core_factors.json").read_text())
    measure_record = json.loads((OUT/"core_measure.json").read_text())
    for record in (factor_record,measure_record):
        assert record["status"] == "completed" and record["N"] == 1155
        assert record["content"] == 1 and record["timeout_seconds"] == 60
        assert record["factors"] == [{"degree":446,"multiplicity":1,"coefficients_ascending":quotient}]
    certificate = measure_record["measure_certificate"]
    assert certificate["coefficients_ascending"] == quotient
    assert certificate["factorization_product_verified"] and certificate["root_count_with_multiplicity"] == 446
    assert certificate["precision_bits"] == 128 and len(certificate["factors"]) == 1
    stored_factor = certificate["factors"][0]
    assert stored_factor["coefficients_ascending"] == quotient and stored_factor["exponent"] == 1
    assert stored_factor["degree"] == stored_factor["root_count"] == 446
    assert not stored_factor["cyclotomic"] and not certificate["neutral"]
    support_gcd = math.gcd(*(j for j,c in enumerate(quotient) if j and c))
    assert support_gcd == 1
    opposite = [value*(-1)**j for j,value in enumerate(quotient)]
    core = min(quotient[::-1],opposite[::-1])[::-1]
    assert certificate["core_coefficients_ascending"] == core
    fresh = p.complex_roots()
    assert len(fresh) == 446 and all(int(power) == 1 for _,power in fresh)
    used = set()
    product = arb(1)
    regions = {"outside":0,"inside":0,"meets_one":0}
    fresh_records = []
    def contained(value,bounds):
        lower,upper = bounds
        if lower == upper:
            return value == arb(lower.numerator)/lower.denominator
        return (value > arb(lower.numerator)/lower.denominator and
                value < arb(upper.numerator)/upper.denominator)
    for row in stored_factor["roots"]:
        assert row["multiplicity"] == 1
        real_text,imag_text = row["root_ball"].split(" + ")
        assert imag_text.endswith("j")
        real_bounds,imag_bounds = rational_ball(real_text),rational_ball(imag_text[:-1])
        matches = [j for j,(root,_) in enumerate(fresh) if j not in used and
                   contained(root.real,real_bounds) and contained(root.imag,imag_bounds)]
        assert len(matches) == 1
        j = matches[0]
        used.add(j)
        root = fresh[j][0]
        modulus = abs(root)
        assert contained(modulus,rational_ball(row["modulus_ball"]))
        region = "outside" if modulus > 1 else "inside" if modulus < 1 else "meets_one"
        assert row["region"] == region
        regions[region] += 1
        if region == "outside":
            product *= modulus
            assert contained(modulus,rational_ball(row["contribution_ball"]))
        else:
            lower,upper = rational_ball(row["contribution_ball"])
            assert lower <= 1 <= upper
        fresh_records.append({"root_ball":str(root),"multiplicity":1,"region":region})
    assert len(used) == 446
    assert regions == {"outside":104,"inside":104,"meets_one":238}
    assert regions["outside"] == exact_shape["complete_exterior_roots"]
    assert regions["inside"] == exact_shape["complete_interior_roots"]
    assert regions["meets_one"] == exact_shape["complete_unit_circle_roots"]
    # The exact count and the 208 strictly classified balls force all other roots onto the unit circle.
    # Thus the product of only the 104 certified exterior moduli is the COMPLETE measure.
    interval = [[int(x) for x in product.lower().man_exp()],
                [int(x) for x in product.upper().man_exp()]]
    old_interval = certificate["measure_interval"]
    assert old_interval == stored_factor["measure_interval"]
    assert dyadic(old_interval[0]) < dyadic(interval[0]) <= dyadic(interval[1]) < dyadic(old_interval[1])
    assert F("2.10642510401468") < dyadic(old_interval[0])
    assert dyadic(old_interval[1]) < F("2.10642510401469")
    assert dyadic(old_interval[0]) > F(6,5)
    assert contained(product,rational_ball(certificate["measure_ball"]))
    assert certificate["measure_ball"] == stored_factor["measure_ball"]
    for threshold in ("6/5","5/4","13/10","7/5"):
        assert dyadic(old_interval[0]) > F(threshold)
        assert certificate["thresholds"][threshold] == stored_factor["thresholds"][threshold] == "above"
    return {"python_flint_version":flint.__version__,"precision_bits":256,
            "factorization":"one degree-446 irreducible factor, multiplicity and content one, using trusted FLINT factorization",
            "every_exact_factor_coefficient_matched":True,"every_author_root_ball_matched_once":True,
            "region_counts":regions,"measure_method":"exact Sturm count plus only the certified exterior moduli",
            "complete_measure_ball":str(product),"complete_measure_interval":interval,
            "strictly_inside_author_dyadic_interval":True,"author_dyadic_interval":old_interval,
            "strict_decimal_bounds":["2.10642510401468","2.10642510401469"],
            "roots":fresh_records,"trusted_backend_boundary":"FLINT irreducible factorization and Arb root isolation; no independent backend implementation"}


def main():
    author = json.loads((OUT/"core_shape.json").read_text())
    numerator,block,quotient = generate(1155,BLOCK)
    assert [len(x)-1 for x in (numerator,block,quotient)] == [480,34,446]
    assert author["N"] == 1155 and author["central_exponent"] == 240
    assert author["specified_cyclotomic_block"] == [list(x) for x in BLOCK]
    for key,polynomial in (("original_coefficients_ascending",numerator),
                           ("block_coefficients_ascending",block),
                           ("quotient_coefficients_ascending",quotient)):
        assert author[key] == polynomial
    trace = extract_trace(quotient)
    result = shape(trace,author["result"])
    assert not author["passes_necessary_exterior_count"]
    _,_,p10 = generate(35,[(1,2),(2,2),(3,1),(4,1),(6,1),(8,1)])
    assert p10 == [1,-1,0,0,0,1,0,0,0,-1,1]
    t10 = extract_trace(p10)
    control10 = shape(t10,author["controls"]["degree10"])
    source = HERE.parent/"Yin_J_G0144"/"trace_control.py"
    constants = {}
    for node in ast.parse(source.read_text()).body:
        if isinstance(node,ast.Assign) and isinstance(node.targets[0],ast.Name) and node.targets[0].id in ("TRACE","SOURCE_HALF"):
            constants[node.targets[0].id] = ast.literal_eval(node.value)
    t18 = list(constants["TRACE"])
    p18 = lift(t18)
    assert p18[::-1] == list(constants["SOURCE_HALF"]+constants["SOURCE_HALF"][-2::-1])
    control18 = shape(t18,author["controls"]["degree18"])
    assert discriminant_monic(t10) == author["controls"]["degree10"]["trace_discriminant"] == -18583
    bounds = [sum(j*abs(value)*2**(j-1) for j,value in enumerate(poly) if j)
              for poly in (t10,t18)]
    assert bounds == [193,10902]
    assert author["controls"]["degree10"]["endpoint_derivative_bound"] == bounds[0]
    assert author["controls"]["degree18"]["endpoint_derivative_bound"] == bounds[1]
    assert 484*193 < 49*45**2 and 484*10902 < 49*329**2
    print("Independent integer generation, trace, squarefreeness and all Sturm entries passed.",flush=True)
    measure = factor_and_measure(quotient,result)
    output = {"scope":"fixed N=1155 quotient and two exact controls; no other N or independent factorization-library proof",
              "python_version":platform.python_version(),"generation_method":"integer Mobius products and exact monic long division",
              "trace_method":"triangular subtraction of binomial reciprocal lifts",
              "root_count_method":"positive-pivot integer pseudo-remainders, independently of author rational division",
              "original_coefficients_ascending":numerator,"block_coefficients_ascending":block,
              "quotient_coefficients_ascending":quotient,"result":result,
              "controls":{"degree10":control10,"degree18":control18},
              "trace10_discriminant_by_Sylvester_Bareiss":-18583,
              "derivative_bounds":bounds,"strict_integer_control_inequalities_verified":True,
              "factor_and_measure":measure,
              "limits":"No author program imported or executed, no exhaustive cyclotomic extraction, no Rouche recertification, no family search."}
    path = OUT/"core_shape_independent.json"
    path.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(path),"variations":result["variations"],
                      "exterior":result["complete_exterior_roots"],"interior":result["complete_interior_roots"],
                      "unit_circle":result["complete_unit_circle_roots"],"measure":measure["complete_measure_ball"]},indent=2))


if __name__ == "__main__":
    main()
