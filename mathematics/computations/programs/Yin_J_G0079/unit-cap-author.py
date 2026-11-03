"""Sole six-instance retained norm-one energy-cap comparison; no new seeds."""
from fractions import Fraction as F
from math import gcd, lcm, isfinite
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import importlib.util
import json
import subprocess
import sys
import time
import traceback

HERE = (_J_PROGRAM / 'unit-cap-author.py').parent
OUTPUT = (_J_OUTPUT / 'unit-cap-output.json')
CAP = 180
ORDER = [('P10', 'baseline'), ('P10', 'enlarged'),
         ('n18', 'baseline'), ('n18', 'enlarged'),
         ('n30', 'baseline'), ('n30', 'enlarged')]
SOURCES = ['fast-optimum-result.json', 'residual-lattice-output.json',
           'lehmer-bundle-output.json']


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


def save(out):
    pending = OUTPUT.with_suffix('.json.pending')
    pending.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    pending.replace(OUTPUT)


def helper(name, filename):
    spec = importlib.util.spec_from_file_location(name, ((_J_PROGRAM if filename in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def worker(start):
    out = json.loads(OUTPUT.read_text(encoding='utf-8'))
    lp = helper('unit_cap_existing_tableau', 'fast-optimum.py')
    poly = helper('unit_cap_existing_division', 'nonmonomial-author.py')
    rat, vec, dot = lp.rat, lp.vec, lp.dot

    def rr(x):
        return F(*x)

    def cap():
        if time.monotonic() - start >= CAP:
            raise TimeoutError('Declared aggregate180-second cap')

    def column(raw, index, kind, p, q, N, source_locator):
        """Copy retained witnesses; check identities, never recompute a norm determinant."""
        cap()
        d = len(p) - 1
        b, f, up = raw['B'], raw['F_coefficients'], raw['kernel_multiplier']
        norm, full, content = raw['signed_res_B'], raw['signed_res_F'], raw['content']
        assert len(b) == len(f) == N and any(f)
        assert all(type(a) is int for a in b + f + up)
        conv = [0] * N
        for i, a in enumerate(up):
            for j, c in enumerate(p):
                conv[i+j] += a*c
        assert all(f[i] + conv[i] == q*b[i] for i in range(N))
        assert norm != 0 and full == q**d * norm
        assert content == gcd(*f) > 0 and full % content**d == 0
        E = sum(a*a for a in f)
        auto = [sum(f[i]*f[i+h] for i in range(N-h)) for h in range(1, N)]
        e, h = F(E, q*q), [F(a, q*q) for a in auto]
        if 'integer_energy' in raw:
            assert E == raw['integer_energy']
            assert auto == raw['integer_autocorrelations']
        if 'e_B' in raw:
            assert e == rr(raw['e_B']) and h == list(map(rr, raw['h_B']))
        if 'e' in raw:
            assert e == rr(raw['e']) and h == list(map(rr, raw['h']))
        primitive = [a//content for a in f]
        if 'primitive_coefficients' in raw:
            assert primitive == raw['primitive_coefficients']
            assert full//content**d == raw['signed_res_primitive']
        norm_one, energy_cap = abs(norm) == 1, e <= 1
        monomial = kind == 'monomial'
        assert e > 0
        if monomial:
            assert norm_one and energy_cap
        rec = {'source_index': index, 'kind': kind, 'source_locator': source_locator,
               'B': b, 'F_coefficients': f, 'kernel_multiplier': up,
               'signed_res_B': norm, 'signed_res_F': full, 'content': content,
               'primitive_coefficients': primitive, 'signed_res_primitive': full//content**d,
               'integer_energy': E, 'integer_autocorrelations': auto,
               'e': rat(e), 'h': vec(h), 'actual_degree': max(i for i, a in enumerate(f) if a),
               'coefficient_height': max(map(abs, f)), 'coefficient_l1': sum(map(abs, f)),
               'norm_one': norm_one, 'energy_at_most_one': energy_cap,
               'baseline_included': monomial, 'enlarged_included': monomial or (norm_one and energy_cap),
               'exclusion_reasons': ([] if monomial or (norm_one and energy_cap) else
                                     (['nonunit_norm'] if not norm_one else []) +
                                     (['energy_above_one'] if not energy_cap else []))}
        for key in ['norm_matrix', 'z', 'basis_index', 'sign', 'basis_or_monomial_index']:
            if key in raw:
                rec[key] = raw[key]
        if not monomial:
            rec['retained_seed_kind'] = raw['kind']
        return rec

    try:
        cap()
        data = {name: json.loads((((_J_PROGRAM if name in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / name)).read_text(encoding='utf-8')) for name in SOURCES}
        assert all(value['status'] == 'complete' for value in data.values())
        old = {r['n']: r for r in data[SOURCES[0]]['records']}
        lattice = {r['n']: r for r in data[SOURCES[1]]['records']}
        lehmer = data[SOURCES[2]]
        raw_inputs = [('P10', lehmer['coefficients'], lehmer['d'], lehmer['N'],
                       lehmer['q'], lehmer['C_rows'], lehmer['family'])]
        assert len(lehmer['family']) == 48
        for n in [18, 30]:
            a, parent = old[n], lattice[n]
            d, N, q, p, C = (a[k] for k in ['d', 'N', 'q', 'coefficients', 'input_C_rows'])
            assert [parent[k] for k in ['d', 'N', 'q', 'coefficients']] == [d, N, q, p]
            assert len(parent['candidates']) == 3*d-2
            assert parent['L_rows'] == [row[:d] for row in C]
            raws = []
            for j in range(N):
                b = [int(i == j) for i in range(N)]
                f = [C[i][j] for i in range(N)]
                up = poly.quotient([q*b[i]-f[i] for i in range(N)], p)
                norm = ((-1)**d*p[0])**j
                raws.append({'kind': 'monomial', 'B': b, 'F_coefficients': f,
                             'kernel_multiplier': up, 'signed_res_B': norm,
                             'signed_res_F': q**d*norm, 'content': gcd(*f)})
            raws.extend(parent['candidates'])
            raw_inputs.append((f'n{n}', p, d, N, q, C, raws))
        for label, p, d, N, q, C, raws in raw_inputs:
            cap()
            assert N == 2*d and len(p) == d+1 and p[0] == p[-1] == 1
            assert len(C) == N and all(len(row) == N for row in C)
            cols = []
            for j, raw in enumerate(raws):
                kind = 'monomial' if j < N else 'retained_residue'
                source = (f'lehmer-bundle-output.json:family[{j}]' if label == 'P10' else
                          f'fast-optimum-result.json:{label}:column[{j}]' if j < N else
                          f'residual-lattice-output.json:{label}:candidates[{j-N}]')
                cols.append(column(raw, j, kind, p, q, N, source))
            e = [rr(c['e']) for c in cols]
            H = [[rr(c['h'][h]) for c in cols] for h in range(N-1)]
            assert sum(e[:N]) == d
            assert all(e[j] == F(C[j][j], q) and cols[j]['F_coefficients'] ==
                       [C[i][j] for i in range(N)] for j in range(N))
            assert all(e[j] == e[N-1-j] and all(row[j] == row[N-1-j] for row in H)
                       for j in range(d))
            bv = [F(1, d)]*N + [F(0)]*(len(cols)-N)
            bcorr = [dot(row, bv) for row in H]
            assert dot(e, bv) == 1 and sum(bv) == 2
            out['inputs'].append({'input': label, 'coefficients': p, 'd': d, 'N': N, 'q': q,
                'C_rows': C, 'columns': cols, 'source_column_count': len(cols),
                'baseline_indices': list(range(N)),
                'enlarged_indices': [j for j,c in enumerate(cols) if c['enlarged_included']],
                'admitted_residue_indices': [j for j,c in enumerate(cols) if j >= N and c['enlarged_included']],
                'excluded_residue_indices': [j for j,c in enumerate(cols) if j >= N and not c['enlarged_included']],
                'mirror_pairs': [[j, N-1-j] for j in range(d)],
                'uniform_v': vec(bv), 'uniform_correlations': vec(bcorr),
                'uniform_kappa': rat(2*sum(map(abs, bcorr))),
                'degree_bound': N-1, 'radial_multiplier': rat(F(N-1, d)),
                'each_admitted_abs_res_F': q**d, 'status': 'inputs-certified'})
            save(out)
        out['status'] = 'inputs-certified'
        save(out)
        for rec in out['instances']:
            cap()
            inp = next(a for a in out['inputs'] if a['input'] == rec['input'])
            d, N, q = (inp[k] for k in ['d', 'N', 'q'])
            ids = inp[rec['family']+'_indices']
            family = [inp['columns'][j] for j in ids]
            e = [rr(c['e']) for c in family]
            H = [[rr(c['h'][h]) for c in family] for h in range(N-1)]
            assert all(c['norm_one'] and c['energy_at_most_one'] for c in family)
            comp = list(range(d)) + list(range(N, len(family)))
            ep, hp = [e[j] for j in comp], [[row[j] for j in comp] for row in H]
            rec.update(status='matrices-ready', family_source_indices=ids, family_count=len(family),
                e=vec(e), H_rows=[vec(row) for row in H], compressed_local_indices=comp,
                compressed_source_indices=[ids[j] for j in comp], compressed_count=len(comp),
                e_compressed=vec(ep), H_compressed=[vec(row) for row in hp])
            save(out)
            cand = lp.tableau([[float(a) for a in row] for row in hp], list(map(float, ep)), cap)
            rec.update(status='candidate-returned', floating_candidate=cand)
            save(out)
            assert all(isfinite(a) for a in cand['pair_masses'] + cand['candidate_correlations'] + cand['y'])
            support = [j for j,a in enumerate(cand['pair_masses']) if a > lp.ACTIVE]
            zeros = [h for h,a in enumerate(cand['candidate_correlations']) if abs(a) < lp.ACTIVE]
            tight = abs(sum(cand['pair_masses'])-2) < lp.ACTIVE
            rows, rhs = [[ep[j] for j in support]], [F(1)]
            if tight:
                rows.append([F(1)]*len(support)); rhs.append(F(2))
            rows += [[hp[h][j] for j in support] for h in zeros]
            rhs += [F(0)]*len(zeros)
            approx = [cand['pair_masses'][j] for j in support]
            rec['primal_reconstruction_input'] = {'support': support, 'zero_lags': [h+1 for h in zeros],
                'S_tight': tight, 'rows': [vec(row) for row in rows], 'rhs': vec(rhs), 'approx': approx}
            save(out)
            sub, info = lp.solve_exact(rows, rhs, approx)
            vc = [F(0)]*len(comp)
            for j,a in zip(support, sub): vc[j] = a
            v = [F(0)]*len(family)
            for k,j in enumerate(comp):
                if j < d: v[j] = v[N-1-j] = vc[k]/2
                else: v[j] = vc[k]
            S = sum(v)
            corr = [dot(row, v) for row in H]
            kappa = 2*sum(map(abs, corr))
            rec.update(status='primal-reconstructed', primal_reconstruction=info,
                compressed_v=vec(vc), v=vec(v), S=rat(S), correlations=vec(corr), kappa=rat(kappa))
            save(out)
            assert all(a >= 0 for a in v) and dot(e,v) == 1 and S >= 2
            assert sum(vc) == S and all(dot(row, vc) == a for row,a in zip(hp,corr))
            y, free = [None]*(N-1), []
            for h,a in enumerate(corr):
                if a: y[h] = F(1 if a > 0 else -1)
                elif abs(abs(cand['y'][h])-1) < lp.ACTIVE: y[h] = F(1 if cand['y'][h] > 0 else -1)
                else: free.append(h)
            rows, rhs = [], []
            for j,a in enumerate(vc):
                if a:
                    rows.append([2*hp[h][j] for h in free] + [-ep[j], F(-1)])
                    rhs.append(-sum(2*hp[h][j]*y[h] for h in range(N-1) if y[h] is not None))
            if S > 2 or abs(cand['mu']) < lp.ACTIVE:
                rows.append([F(0)]*(len(free)+1)+[F(1)]); rhs.append(F(0))
            approx = [cand['y'][h] for h in free] + [cand['lambda'], cand['mu']]
            rec['dual_reconstruction_input'] = {'free_y_lags': [h+1 for h in free],
                'fixed_y': [None if a is None else rat(a) for a in y],
                'rows': [vec(row) for row in rows], 'rhs': vec(rhs), 'approx': approx}
            save(out)
            sol, dinfo = lp.solve_exact(rows, rhs, approx)
            for h,a in zip(free,sol): y[h] = a
            lam, mu = sol[-2:]
            slacks = [2*sum(y[h]*H[h][j] for h in range(N-1))-lam*e[j]-mu for j in range(len(family))]
            lower = lam+2*mu
            rec.update(status='dual-reconstructed', dual_reconstruction=dinfo, y=vec(y),
                lambda_value=rat(lam), mu=rat(mu), dual_slacks=vec(slacks),
                lower_bound=rat(lower), gap=rat(kappa-lower))
            save(out)
            assert all(-1 <= a <= 1 for a in y) and mu >= 0 and all(a >= 0 for a in slacks)
            assert kappa == lower and mu*(S-2) == 0 and all(v[j]*slacks[j] == 0 for j in range(len(v)))
            w = [a/S for a in v]
            den = lcm(*(a.denominator for a in w))
            mult = [int(a*den) for a in w]
            aggregate = [0]*(2*N-1)
            sign = 1
            for copies,c in zip(mult,family):
                if copies:
                    sign *= c['signed_res_B']**(copies % 2)
                    for i,a in enumerate(c['F_coefficients']):
                        for j,b in enumerate(c['F_coefficients']): aggregate[i+N-1-j] += copies*a*b
            energy, auto = F(q*q)/S, [F(q*q)*a/S for a in corr]
            assert sum(mult) == den and F(aggregate[N-1], den) == energy
            assert aggregate == aggregate[::-1]
            assert all(F(aggregate[N-1+h],den) == auto[h-1] for h in range(1,N))
            rec.update(status='complete', global_finite_family_optimum_certified=True,
                weights=vec(w), weight_denominator=den, multiplicities=mult,
                positive_local_indices=[j for j,a in enumerate(w) if a],
                positive_source_indices=[ids[j] for j,a in enumerate(w) if a],
                zero_lags=[h+1 for h,a in enumerate(corr) if not a],
                strict_dual_slack_local_indices=[j for j,a in enumerate(slacks) if a > 0],
                energy=rat(energy), aggregate_autocorrelations=vec(auto), aggregate_polynomial=aggregate,
                income={'log_q_argument': q},
                exact_arithmetic_product={'sign': sign, 'q_base': q, 'q_exponent': d*den},
                true_surplus={'half_log_argument': rat(S), 'at_least_half_log_two': S >= 2},
                degree_bound=N-1, radial_multiplier=rat(F(N-1,d)), kappa_le_4=kappa <= 4,
                kappa_ten_thousandth_bin=[kappa.numerator*10000//kappa.denominator,
                                          kappa.numerator*10000//kappa.denominator+1])
            if rec['family'] == 'enlarged':
                base = next(a for a in out['instances'] if a['input'] == rec['input'] and a['family'] == 'baseline')
                assert base['status'] == 'complete'
                K0 = rr(base['kappa'])
                assert kappa <= K0
                out['comparisons'].append({'input': rec['input'], 'baseline_kappa': rat(K0),
                    'enlarged_kappa': rat(kappa), 'improvement': rat(K0-kappa),
                    'strict_improvement': kappa < K0, 'equal_optima': kappa == K0})
            save(out); cap()
            print(json.dumps({'input': rec['input'], 'family': rec['family'], 'status': rec['status'],
                'bin': rec['kappa_ten_thousandth_bin'], 'pivots': cand['pivot_count']}), flush=True)
        out['status'], out['all_six_optima_certified'] = 'complete', True
    except BaseException as exc:
        out.update(status='incomplete', error_type=type(exc).__name__, error=_record_text(str(exc)), traceback=_record_text(traceback.format_exc()))
    pass
    pass
    save(out)
    return 0 if out['status'] == 'complete' else 1


def main():
    if len(sys.argv) == 3 and sys.argv[1] == '--worker':
        return worker(float(sys.argv[2]))
    if len(sys.argv) != 1:
        raise SystemExit('Usage: unit-cap-author.py')
    if OUTPUT.exists():
        raise SystemExit('Refusing to overwrite first native output')
    start = time.monotonic()
    out = {'schema': 'J79-unit-cap-comparison-v1', 'status': 'started', 'input_files': SOURCES, 'helper_files': ['fast-optimum.py', 'nonmonomial-author.py'], 'candidate_rule': {'EPS': 1e-09, 'ACTIVE': 1e-07, 'ratio_tie': 1e-10, 'pivot_cap_per_instance': 10000, 'free_denominator_cap': 10 ** 6, 'candidate_calls_per_instance': 1, 'reconstructions_per_instance': 1}, 'instances': [{'input': a, 'family': b, 'status': 'not-started'} for a, b in ORDER], 'inputs': [], 'comparisons': []}
    with OUTPUT.open('x', encoding='utf-8') as handle:
        json.dump(out, handle, indent=2)
    proc = subprocess.Popen([sys.executable, str((_J_PROGRAM / 'unit-cap-author.py')), '--worker', repr(start)],
                            creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    timeout = False
    try:
        code = proc.wait(timeout=max(0.01, CAP-(time.monotonic()-start)))
    except subprocess.TimeoutExpired:
        timeout = True; proc.kill(); code = proc.wait()
    result = json.loads(OUTPUT.read_text(encoding='utf-8'))
    result.update(actual_worker_exit_code=code, outer_timed_out=timeout)
    if timeout:
        result.update(status='incomplete', error_type='OuterDeadline', error='Declared aggregate180-second cap')
    save(result)
    print(json.dumps({'status': result['status'], 
        'error': result.get('error'), 'instances': [{k:r.get(k) for k in ['input','family','status',
        'kappa_ten_thousandth_bin']} for r in result['instances']]}), flush=True)
    return 0 if code == 0 and not timeout and result['status'] == 'complete' else 1


if __name__ == '__main__':
    raise SystemExit(main())
