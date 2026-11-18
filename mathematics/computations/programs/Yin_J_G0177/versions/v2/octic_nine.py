"""Exact signed minima and mixed width-nine minima for one octic at primes through 251."""

import json
import runpy
from math import gcd, isqrt
from pathlib import Path


GROUP = Path(__file__).resolve().parents[2]
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "versions" / "v2" / "results.json"
BASE = runpy.run_path(str(GROUP / "minimum.py"))
row_system = BASE["row_system"]
reduce_plane, short_vectors = BASE["reduce_plane"], BASE["short_vectors"]
dot, norm_one, search = BASE["dot"], BASE["norm_one"], BASE["search"]
mixed_rows, certify_graph = BASE["mixed_rows"], BASE["certify_graph"]
coprime, unequal_moduli = BASE["coprime"], BASE["unequal_moduli"]

SEED = (1, 0, 0, -1, -1, -1, 0, 0, 1)
WIDTH = 9
PRIME_LIMIT = 251


def signed_record(columns, prime, sign, plane):
    first, second = plane
    a, b, c = dot(first, first), dot(first, second), dot(second, second)
    assert 0 < a <= c and 2*abs(b) <= a
    minors = [first[i]*second[j]-first[j]*second[i]
              for j in range(WIDTH+1) for i in range(j)]
    assert gcd(*minors) == 1
    for vector in plane:
        assert len(vector) == WIDTH+1
        assert all(sum(vector[i]*(columns[prime*i][k]+sign*columns[prime*(WIDTH-i)+1][k])
                       for i in range(WIDTH+1)) == 0 for k in range(2*(len(SEED)-1)))
    radius = 2**(prime+1)
    candidates = list(short_vectors(plane, radius)) if a <= radius**2 else []
    rank = 0
    if candidates:
        start = candidates[0]
        independent = any(dot(start, start)*dot(v, v) != dot(start, v)**2
                          for v in candidates[1:])
        rank = 2 if independent else 1
    return {"lambda_squared": [a, c], "basis": [first, second], "off_diagonal": b,
            "cutoff_vector_count": len(candidates), "cutoff_span_rank": rank}, candidates


def cutoff_pairs(columns, prime, positive, negative):
    compatible = 0
    inside = 0
    genuine = []
    for a in positive:
        for b in negative:
            if any((x-y) % 2 for x, y in zip(a, b)):
                continue
            compatible += 1
            u, v = mixed_rows(a, b)
            height = max(norm_one(u), norm_one(v))
            if not any(u) or not any(v) or height > 2**prime:
                continue
            inside += 1
            while u[0] == v[0] == 0:
                u, v = u[1:]+[0], v[1:]+[0]
            if unequal_moduli(u, v) and coprime(u, v):
                certify_graph(columns, prime, u, v)
                genuine.append({"cost": height, "rows": [u, v]})
    return {"same_parity": compatible, "inside": inside,
            "genuine": sorted(genuine, key=lambda pair: pair["cost"])}


def prime_record(prime):
    columns, kernels = row_system(SEED, prime, WIDTH)
    planes = [reduce_plane(*kernel) for kernel in kernels]
    positive, plus_rows = signed_record(columns, prime, 1, planes[0])
    negative, minus_rows = signed_record(columns, prime, -1, planes[1])
    cutoff = cutoff_pairs(columns, prime, plus_rows, minus_rows)
    ceiling = sum(norm_one(first) for first, second in planes)
    minimum, counts = search(planes, columns, prime, ceiling)
    if minimum is None:
        raise ValueError(f"No uncapped witness inside the tested ceiling at {prime}")
    assert minimum["cost"] == max(norm_one(v) for v in minimum["rows"])
    certify_graph(columns, prime, *minimum["rows"])
    assert bool(cutoff["genuine"]) == (minimum["cost"] <= 2**prime)
    if cutoff["genuine"]:
        assert cutoff["genuine"][0]["cost"] == minimum["cost"]
    return {"prime": prime, "plus": positive, "minus": negative, "cutoff_pairs": cutoff,
            "uncapped_search_ceiling": ceiling, "uncapped_search_counts": counts,
            "uncapped_minimum": minimum}


def width_eight_control():
    columns, ((plus,), (minus,)) = row_system(SEED, 17, 8)
    assert plus[0]*minus[-1] + plus[-1]*minus[0] != 0
    scale = 2 if any((a-b) % 2 for a, b in zip(plus, minus)) else 1
    u, v = mixed_rows([scale*x for x in plus], [scale*x for x in minus])
    certify_graph(columns, 17, u, v)
    return {"prime": 17, "least_cost": max(norm_one(u), norm_one(v)), "rows": [u, v]}


def main():
    primes = [p for p in range(3, PRIME_LIMIT+1, 2)
              if all(p % i for i in range(3, isqrt(p)+1, 2))]
    records = [prime_record(p) for p in primes]
    assert all(r["uncapped_minimum"]["cost"]**4 > 2**(5*r["prime"])
               for r in records if r["prime"] >= 19)
    data = {"seed_ascending": SEED, "width": WIDTH, "prime_limit": PRIME_LIMIT,
            "records": records, "width_eight_control": width_eight_control()}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Computed {len(records)} uncapped minima.")
    print([(r["prime"], r["uncapped_minimum"]["cost"])
           for r in records if r["cutoff_pairs"]["genuine"]])


if __name__ == "__main__":
    main()
