"""Independent exact verification of the predeclared J88 finite certificate.

Never imports or executes the author programs. No LP or floating arithmetic.
"""
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import argparse
import json
import subprocess
import sys
import time
import traceback

HERE = (_J_PROGRAM / 'review-check.py').parent
P = (1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1)
D, N, Q, CAP = 10, 11, 9, 180
BETA = (1, 0, 1, 0, 0, 0, -1, -1, 1, 1, -1)
INPUTS = ('worker.py', 'main.py', 'result.json',
          'exact-validation.py', 'exact-validation.json', 'readme.md')


# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def require(condition, message):
    if not condition:
        raise ValueError(message)


def determinant(matrix):
    """Integer fraction-free elimination, with checked exact divisions."""
    a = [list(row) for row in matrix]
    size, sign, previous = len(a), 1, 1
    if not size:
        return 1
    for k in range(size - 1):
        row = next((i for i in range(k, size) if a[i][k]), None)
        if row is None:
            return 0
        if row != k:
            a[k], a[row] = a[row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                require(numerator % previous == 0, 'Nonexact Bareiss division')
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def fraction_pair(value):
    value = Fraction(value)
    return [value.numerator, value.denominator]


def laurent_square(vector):
    """Full product F(t)F(t^-1), rather than the author lag-array loops."""
    coefficients = [0] * (2 * N - 1)
    for i, left in enumerate(vector):
        for j, right in enumerate(vector):
            coefficients[N - 1 + i - j] += left * right
    require(coefficients == coefficients[::-1], 'Laurent star symmetry failed')
    return coefficients[N - 1], coefficients[N:]


def quotient_reduce(coefficients):
    values = list(coefficients)
    values += [0] * max(0, D - len(values))
    for degree in range(len(values) - 1, D - 1, -1):
        leading = values[degree]
        if leading:
            for j, coefficient in enumerate(P):
                values[degree - D + j] -= leading * coefficient
    return values[:D]


def worker(input_directory):
    started = time.monotonic()
    report = {'status': 'started', 'method': 'Independent position/radix generator, full Laurent multiplication, integer certificate, Cramer/Bareiss systems.', 'coefficients': list(P), 'd': D, 'allowed_T': D, 'author_programs_imported_or_executed': False, 'LP_rerun': False, 'historical_Phase_A_bytes_authenticated': False, 'scope_extended': False}

    def deadline():
        require(time.monotonic() - started < CAP, 'Reviewer180-second worker cap')

    def publish(name):
        pass
        temporary = _J_OUTPUT / (name + '.pending')
        temporary.write_text(json.dumps(report, indent=2) + '\n', encoding='utf8')
        temporary.replace(((_J_PROGRAM if name in ('exact-validation.py', 'main.py', 'readme.md', 'review-check.py', 'worker.py') else _J_OUTPUT) / name))

    def input_path(name):
        return (_J_PROGRAM if name.endswith('.py') or name == 'readme.md' else input_directory) / name

    try:
        raw_inputs = {name: input_path(name).read_bytes() for name in INPUTS}
        result = json.loads(raw_inputs['result.json'])
        exact = json.loads(raw_inputs['exact-validation.json'])
        require(tuple(result['coefficients']) == P == tuple(exact['coefficients']), 'Wrong polynomial')
        require(result['d'] == exact['d'] == D and result['N'] == N, 'Wrong dimensions')
        require(result['allowed_T'] == exact['allowed_T'] == D, 'Wrong allowed window')
        expected_parameters = {'ternary_coordinates': D, 'first_nonzero': 1, 'k': [-2, -1, 0, 1, 2], 'coefficient_denominator_divides': Q, 'atom_energy_cap': 4, 'pivot_cap': 2000, 'reduced_cost_tolerance': 1e-09, 'pivot_tolerance': 1e-10, 'ratio_tie_tolerance': 1e-10}
        require(result['parameters'] == expected_parameters, 'Saved scope differs from declaration')
        require(sum(p*p for p in P) == Q and P[0] == P[-1] == 1, 'Wrong projection norm/unit guards')
        require(result['A_rows'] == [[int(i == j) for j in range(D)] + [-P[i]] for i in range(D)], 'Wrong remainder matrix')
        require(result['status'] == exact['status'] == 'complete', 'Incomplete author payload')

        atoms, labels, indices = [], [], {}
        generated = residues_count = accepted_labels = sign_flips = 0

        def insert(coefficients, label):
            nonlocal sign_flips
            value = tuple(coefficients)
            require(any(value), 'Generated zero coefficient vector')
            if next(v for v in value if v) < 0:
                value = tuple(-v for v in value)
                sign_flips += 1
            if value not in indices:
                indices[value] = len(atoms)
                atoms.append(value)
                labels.append(label)
            return indices[value]

        # Original lexicographic order, constructed by the location of the first
        # nonzero entry and a base-three suffix, without the author product loop.
        for first in range(D - 1, -1, -1):
            tail_length = D - first - 1
            for suffix_code in range(3 ** tail_length):
                if residues_count % 512 == 0:
                    deadline()
                suffix = [0] * tail_length
                radix = suffix_code
                for place in range(tail_length - 1, -1, -1):
                    radix, digit = divmod(radix, 3)
                    suffix[place] = digit - 1
                residue = [0] * first + [1] + suffix
                residues_count += 1
                dot = sum(residue[i] * P[i] for i in range(D))
                residue_energy = sum(r*r for r in residue)
                for offset in range(-2, 3):
                    generated += 1
                    kernel_numerator = offset - dot
                    numerator = [Q*residue[i] + kernel_numerator*P[i] for i in range(D)] + [kernel_numerator]
                    energy_by_projection = Q*Q*residue_energy + 2*Q*kernel_numerator*dot + Q*kernel_numerator*kernel_numerator
                    require(energy_by_projection == sum(v*v for v in numerator), 'Projection energy identity failed')
                    if energy_by_projection <= 4*Q*Q:
                        accepted_labels += 1
                        insert(numerator, {'r': residue, 'k': offset})
        require(residues_count == (3**D - 1)//2 == 29524 and generated == 147620,
                'Incomplete residue/offset enumeration')
        initial = []
        initial_numerators = []
        for h in range(N):
            vector = [0] * N
            vector[0] = Q
            if h:
                vector[h] = Q
            initial.append(insert(vector, {'initial_basis_h': h}))
            initial_numerators.append(vector)
        require(len(atoms) == len(set(atoms)) == 13197, 'Wrong canonical distinct atom count')
        require(generated + N == result['generated_labels'] == exact['regenerated_labels'] == 147631,
                'Wrong full generated-label count')
        require(len(atoms) == result['distinct_atoms'] == exact['regenerated_atom_count'], 'Saved atom count differs')
        require(initial == exact['true_initial_basis'] and initial_numerators == exact['true_initial_numerators'],
                'True initial vectors/indices differ')
        require(len(set(initial)) == N, 'Initial basis is not distinct')

        energies, lags, residues, slacks = [], [], [], []
        for index, vector in enumerate(atoms):
            if index % 256 == 0:
                deadline()
            require(next(v for v in vector if v) > 0, 'Noncanonical sign')
            raw_residue = [vector[i] - vector[-1]*P[i] for i in range(D)]
            require(all(r % Q == 0 for r in raw_residue), 'Nonintegral residue')
            residue = [r//Q for r in raw_residue]
            require(any(residue), 'Forbidden zero residue')
            energy, correlations = laurent_square(vector)
            require(0 < energy <= 4*Q*Q, 'Energy cutoff failed')
            slack = energy - Q*Q*BETA[0] - sum(BETA[h]*correlations[h-1] for h in range(1,N))
            require(slack >= 0, 'Negative exact slack at atom' + str(index))
            energies.append(energy); lags.append(correlations); residues.append(residue); slacks.append(slack)
        require(slacks == exact['all_slack_numerators'], 'Saved full slack payload differs')
        require(min(slacks) == exact['minimum_slack_numerator'] == 0, 'Wrong minimum slack')
        require(exact['dual_beta'] == [[b,1] for b in BETA] and exact['dual_integer_numerators'] == list(BETA),
                'Wrong saved exact dual')
        require(exact['dual_common_denominator'] == 1 and exact['slack_denominator'] == Q*Q,
                'Wrong exact dual/slack scale')
        require(exact['checked_atom_count'] == len(atoms) and exact['exact_minimum'] == [1,1]
                and exact['outcome'] == 'exact-finite-family-minimum-one', 'Wrong finite certificate conclusion')

        final = result['floating_lead']['basis']
        require(len(final) == len(set(final)) == N and all(type(j) is int and 0 <= j < len(atoms) for j in final),
                'Invalid saved final basis')
        require(final == result['initial_basis'] == exact['saved_alias_affected_initial_basis'] == exact['saved_final_basis'],
                'Alias/final-basis evidence differs')
        require(final != initial, 'Erroneously treating alias list as original initial indices')
        system = [[Q*Q] + lags[j] for j in final]
        rhs = [energies[j] for j in final]
        require(system == exact['transpose_system_rows'] and rhs == exact['transpose_rhs'], 'Saved transpose system differs')
        require(all(sum(a*b for a,b in zip(row,BETA)) == value for row,value in zip(system,rhs)), 'Dual system equality failed')
        system_det = determinant(system)
        require(system_det != 0, 'Singular exact system')
        constraint = [list(row) for row in zip(*system)]
        target = [Q*Q] + [0]*D
        constraint_det = determinant(constraint)
        weights = []
        for column in range(N):
            changed = [row[:] for row in constraint]
            for row in range(N):
                changed[row][column] = target[row]
            weights.append(Fraction(determinant(changed), constraint_det))
        require(all(w >= 0 for w in weights) and sum(weights) == 1, 'Bad exact primal reconstruction')
        support = [(j,w) for j,w in zip(final,weights) if w]
        require(support == [(initial[0],Fraction(1))], 'Returned support is not the exact constant attainer')
        require(result['outcome'] == 'no-below-one-witness-returned' and len(result['packet']) == 1,
                'Wrong Phase A mathematical outcome')
        record = result['packet'][0]
        vector = atoms[initial[0]]
        coefficients = [Fraction(v,Q) for v in vector]
        q = lcm(*(c.denominator for c in coefficients))
        mw = lcm(*(w.denominator for j,w in support))
        numerator = [int(q*c) for c in coefficients]
        residue = residues[initial[0]]
        columns = [quotient_reduce([0]*j + residue) for j in range(D)]
        norm_matrix = [list(row) for row in zip(*columns)]
        full_norm = determinant(norm_matrix)
        require(numerator[1:] == [0]*D, 'Expected constant numerator only')
        full_resultant = numerator[0] ** D
        require(full_resultant == q**D * full_norm == 1 and full_norm != 0, 'Full original-degree norm/resultant failed')
        content = gcd(*numerator)
        require(record['atom_index'] == initial[0] and record['generator_label'] == labels[initial[0]], 'Packet index/label differs')
        require(record['coefficients'] == [fraction_pair(c) for c in coefficients]
                and record['weight'] == [1,1] and record['integer_residue'] == residue
                and record['numerator_coefficients'] == numerator and record['content'] == content
                and record['signed_residue_norm'] == full_norm and record['signed_numerator_resultant'] == full_resultant
                and record['multiplicity'] == 1 and record['energy'] == [1,1]
                and record['autocorrelations'] == [[0,1]]*D, 'Packet exact fields differ')
        require(result['energy'] == result['integer_numerator_energy_S'] == [1,1]
                and result['all_lags'] == [[0,1]]*D and result['actual_union_width'] == 0
                and result['actual_coefficient_denominator'] == q == 1
                and result['actual_weight_denominator'] == mw == 1, 'Aggregate packet costs differ')
        require(result['copied_full_signed_product'] == {'sign':1,'scalar_factor':[1,D],
                                                      'absolute_residue_factors':[[1,1]]}, 'Copied full product differs')
        require(all(input_path(name).read_bytes() == data for name,data in raw_inputs.items()), 'Current input bytes changed during verification')
        deadline()
        report.update({'status': 'complete', 'outcome': 'independent-exact-restricted-minimum-one', 'residue_vector_count': residues_count, 'generated_labels': generated + N, 'energy_kept_generator_labels': accepted_labels, 'canonical_sign_flip_count': sign_flips, 'distinct_atom_count': len(atoms), 'true_initial_basis': initial, 'true_initial_numerators': initial_numerators, 'saved_final_basis': final, 'integer_dual': list(BETA), 'slack_denominator': Q * Q, 'all_atom_numerators': [list(v) for v in atoms], 'all_integer_residues': residues, 'all_slack_numerators': slacks, 'minimum_slack_numerator': min(slacks), 'all_residue_energy_sign_guards_passed': True, 'complete_saved_slack_payload_equal': True, 'exact_system_rows': system, 'exact_system_rhs': rhs, 'exact_system_determinant': system_det, 'exact_basis_weights': [fraction_pair(w) for w in weights], 'constant_attainer': {'atom_index': initial[0], 'q': q, 'M': mw, 'content': content, 'energy': [1, 1], 'actual_width': 0, 'full_degree': D, 'signed_norm': full_norm, 'signed_resultant': full_resultant, 'multiplication_matrix': norm_matrix, 'copied_product': 1}, 'current_input_lengths': {name: len(value) for name, value in raw_inputs.items()}, 'limits': 'Independent exact verification of only the declared13197atoms. No original Phase A byte authentication, LP replay, all-denominator9 exclusion or full-capacity lower bound. Irreducible original Lehmer input reused at fixed scope; unused-atom norm magnitudes not computed.'})
        publish('review-verification.json')
        print(json.dumps({'outcome': report['outcome'], 'atoms': len(atoms), 'minimum_slack': min(slacks), 'true_initial_basis': initial}))
    except BaseException as error:
        report.update({'status':'failed','error_type':type(error).__name__,'error':_record_text(str(error)),
                       'traceback':_record_text(traceback.format_exc())})
        publish('review-failure.json')
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, default=_J_PROGRAM / 'inputs')
    parser.add_argument('--worker', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        worker(args.input_dir)
    else:
        try:
            result = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(_J_PROGRAM / 'review-check.py'), '--worker', '--input-dir', str(args.input_dir)], timeout=CAP)
            code = result.returncode
        except subprocess.TimeoutExpired:
            (_J_OUTPUT / 'review-failure.json').write_text(json.dumps({'status':'supervisor-timeout','complete':False})+'\n',encoding='utf-8')
            code = 124
        raise SystemExit(code)
