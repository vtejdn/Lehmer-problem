"""Only the two predeclared exact scopes; successful JSON is published atomically."""

import argparse
import json
import os
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sys
import tempfile
from time import perf_counter

import direct
import fast

GROUP = (_J_PROGRAM / 'worker.py').parent
EXPECTED = {
    "cyclotomic_linear": [-1, 1],
    "cyclotomic_quadratic": [1, 1, 1],
    "positive_reciprocal_quadratic": [1, -3, 1],
    "lehmer_degree_ten": [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1],
}


def publish(name, payload):
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=_J_OUTPUT,
                                     prefix=f".{name}-", suffix=".tmp", delete=False) as stream:
        json.dump(payload, stream, indent=2)
        stream.write("\n")
        temporary = stream.name
    os.replace(temporary, ((_J_PROGRAM if name in ('direct.py', 'fast.py', 'inputs.json', 'main.py', 'readme.md', 'worker.py') else _J_OUTPUT) / name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("compare", "lehmer1024"), required=True)
    mode = parser.parse_args().mode
    cases = json.loads(((_J_PROGRAM / 'inputs.json')).read_text(encoding="utf-8"))
    if cases != EXPECTED:
        raise ValueError("Inputs differ from the exact predeclared J84 coefficient lists")
    start = perf_counter()
    payload = {'complete': True, 'mode': mode, 'arithmetic': 'exact Python integers', 'integer_encoding': 'state/checkpoint values are decimal integer strings', 'cases': {}}
    if mode == "compare":
        payload["depth"] = 64
        total_equalities = 0
        for name, p in cases.items():
            first = perf_counter()
            actual = fast.compute(p, 64, retain_states=True)
            fast_seconds = perf_counter() - first
            first = perf_counter()
            reference, direct_checks = direct.compute(p, 64)
            direct_seconds = perf_counter() - first
            equalities = 0
            for n, (row, other) in enumerate(zip(actual["states"], reference, strict=True)):
                for k, (value, expected) in enumerate(zip(row, other, strict=True)):
                    if value != expected:
                        raise ArithmeticError(f"Independent mismatch: {name}, n={n}, k={k}")
                    equalities += 1
            total_equalities += equalities
            payload["cases"][name] = {'coefficients_ascending': p, 'H': actual['H'], 'degree': actual['degree'], 'R_ascending': actual['R_ascending'], 'state_vectors': [[str(v) for v in row] for row in actual['states']], 'fast_checks': actual['checks'], 'direct_checks': direct_checks, 'independent_state_equalities': equalities}
        payload["independent_state_equalities"] = total_equalities
        output = "comparison.json"
    else:
        prior = json.loads(((_J_OUTPUT / 'comparison.json')).read_text(encoding="utf-8"))
        if (prior.get("complete") is not True or prior.get("mode") != "compare"
                or prior.get("depth") != 64 or set(prior.get("cases", {})) != set(EXPECTED)
                or prior.get("independent_state_equalities") != 1235):
            raise ValueError("The completed exact declared Stage1 is required")
        for prior_name, coefficients in EXPECTED.items():
            old = prior["cases"][prior_name]
            degree = len(coefficients) - 1
            if (old.get("coefficients_ascending") != coefficients
                    or old.get("H") != sum(abs(a) for a in coefficients)
                    or old.get("degree") != degree
                    or old.get("independent_state_equalities") != 65 * (degree + 1)
                    or len(old.get("state_vectors", [])) != 65
                    or any(len(row) != degree + 1 for row in old["state_vectors"])):
                raise ValueError("Stage1 input/range/normalization payload mismatch")
        name = "lehmer_degree_ten"
        actual = fast.compute(cases[name], 1024, checkpoints=(0, 64, 128, 256, 512, 1024))
        # This one overlap is inherited comparison data, not a new n>64 oracle.
        if actual["checkpoints"]["64"] != prior["cases"][name]["state_vectors"][64][0]:
            raise ArithmeticError("Larger run disagrees at the independently checked overlap n64")
        payload["depth"] = 1024
        payload["independent_verification_beyond_64"] = False
        payload["cases"][name] = {
            "coefficients_ascending": cases[name], "H": actual["H"], "degree": actual["degree"],
            "R_ascending": actual["R_ascending"],
            "scalar_numerator_checkpoints": actual["checkpoints"],
            "final_state": [str(v) for v in actual["final_state"]],
            "checks": actual["checks"], "n64_overlap_matched": True}
        output = "lehmer1024.json"
    pass
    payload["mahler_lower_certificate_computed"] = False
    publish(output, payload)
    print(json.dumps({'complete': True, 'output': output, 'mode': mode, 'depth': payload['depth'], 'independent_state_equalities': payload.get('independent_state_equalities')}))


if __name__ == "__main__":
    main()
