"""Exact S-part cyclic resultants for all n from finite modular probes.

Uses main.py's tested integer polynomial and logarithm routines. This is
additional retained arithmetic evidence, not an independent verification.
All current inputs have squarefree reduction at each selected prime.
"""
from fractions import Fraction
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import flint
import main


def v_p(n, p):
    assert n != 0
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def probe(coeff, n, p):
    precision = 64
    while True:
        modulus = p**precision
        residue = main.sub(main.ppow([0, 1], n, coeff, modulus), [1], modulus)
        value = int(flint.fmpz_poly(coeff).resultant(flint.fmpz_poly(residue))) % modulus
        if value:
            valuation = v_p(value, p)
            assert valuation < precision
            return {"n": n, "prime": p, "precision": precision,
                    "remainder": residue, "resultant_residue": value, "valuation": valuation}
        precision *= 2
        assert precision <= 1024


def local_table(coeff, record):
    p = record["prime"]
    assert record["squarefree"]
    orders = sorted({r["root_order"] for r in record["factors"]})
    groups = []
    for o in orders:
        w = sum(r["degree"] for r in record["factors"] if r["root_order"] == o)
        probes = [probe(coeff, o*p**r, p) for r in range(2 if p == 2 else 1)]
        values = []
        for r, item in enumerate(probes):
            b = item["valuation"]-sum(g["B"][r] for g in groups if o % g["order"] == 0)
            assert b >= w*(r+1)
            values.append(b)
        groups.append({"order": o, "weight": w, "B": values, "probes": probes})
    constant = sum((g["B"][1]-g["weight"] if p == 2 else g["B"][0]) for g in groups)
    return {"prime": p, "groups": groups, "upper_constant": constant}


def weights(n, tables, degree):
    out = {p: 0 for p in main.PRIMES}
    out[2] -= degree
    for table in tables:
        p, r = table["prime"], v_p(n, table["prime"])
        for g in table["groups"]:
            if n % g["order"]:
                continue
            if p == 2 and r:
                out[p] += g["B"][1]+g["weight"]*(r-1)
            else:
                out[p] += g["B"][0]+g["weight"]*r
    return out


def optimize(tables, degree):
    logs = {p: main.log_interval(p) for p in main.PRIMES}
    constant_upper = sum(t["upper_constant"]*logs[t["prime"]][1] for t in tables)-degree*logs[2][0]
    # (C+d log n)/n decreases for n>=1 when C>=d; verify rigorously.
    constant_lower = sum(t["upper_constant"]*logs[t["prime"]][0] for t in tables)-degree*logs[2][1]
    assert constant_lower > degree*main.SCALE
    limit = 4096
    while True:
        low = [-degree*logs[2][1]]*(limit+1)
        high = [-degree*logs[2][0]]*(limit+1)
        for t in tables:
            p = t["prime"]
            for g in t["groups"]:
                step = g["order"]
                events = [(step, g["B"][0])]
                step *= p
                if p == 2:
                    events.append((step, g["B"][1]-g["B"][0]))
                    step *= p
                while step <= limit:
                    events.append((step, g["weight"]))
                    step *= p
                for step, weight in events:
                    a, b = weight*logs[p][0], weight*logs[p][1]
                    for n in range(step, limit+1, step):
                        low[n] += a
                        high[n] += b
        best = 1
        for n in range(2, limit+1):
            if low[n]*best > low[best]*n:
                best = n
        assert low[best] > 0
        tail_upper = constant_upper+degree*main.log_interval(limit+1)[1]
        if tail_upper*best < low[best]*(limit+1):
            break
        limit *= 2
        assert limit <= 1048576
    bestw = weights(best, tables, degree)
    ties, strict = [], 0
    for n in range(1, limit+1):
        if high[n]*best < low[best]*n:
            strict += 1
        else:
            wn = weights(n, tables, degree)
            assert all(wn[p]*best == bestw[p]*n for p in main.PRIMES), (n, best)
            ties.append(n)
    first = min(ties)
    wf = weights(first, tables, degree)
    lo, hi = main.score_interval(wf, logs)
    decimal_floor = (lo*10**10)//(main.SCALE*first)
    return {"enumerated_n_max": limit, "maximizer_exponents": ties, "representative_n": first,
            "numerator_log_weights": wf, "numerator_lower": lo, "numerator_upper": hi,
            "scale_bits": main.BITS, "strict_nonmaximizer_comparisons": strict,
            "tail_at": limit+1, "tail_upper_numerator": tail_upper,
            "certified_lower_decimal_truncated": f"{decimal_floor//10**10}.{decimal_floor%10**10:010d}"}


def build():
    original = json.loads((_J_OUTPUT / "result.json").read_text(encoding="utf-8"))
    output = []
    for inp in original["inputs"]:
        tables = [local_table(inp["coefficients"], r) for r in inp["prime_records"]]
        optimum = optimize(tables, inp["degree"])
        winner = optimum["representative_n"]
        # Fresh probes at the winner directly check the sum-of-groups formula.
        direct = [probe(inp["coefficients"], winner, p) for p in main.PRIMES]
        ww = weights(winner, tables, inp["degree"])
        for r in direct:
            actual = ww[r["prime"]]+(inp["degree"] if r["prime"] == 2 else 0)
            assert r["valuation"] == actual
        output.append({"name": inp["name"], "degree": inp["degree"], "coefficients": inp["coefficients"],
                       "local_tables": tables, "actual_optimum": optimum, "winner_direct_probes": direct})
        print(inp["name"], "actual S-part optimum", optimum["maximizer_exponents"],
              optimum["certified_lower_decimal_truncated"], "weights", ww, flush=True)
    return {"primes": main.PRIMES,
            "arithmetic": "exact modular resultants and rational logarithm intervals; finite local tables determine all n",
            "inputs": output}


if __name__ == "__main__":
    (_J_OUTPUT / "actual-result.json").write_text(json.dumps(build(), indent=2)+"\n", encoding="utf-8")
