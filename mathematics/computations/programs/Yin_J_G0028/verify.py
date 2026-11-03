"""Independent enclosing-certificate validation and complete integer traversal.

No author prepare/checker/traversal code is imported. This reviewer's earlier
J23 exact-root helper is reused. The new certificate check uses Arb and exact
SymPy matrix identities; traversal uses Python integers and math.isqrt, with
range-checked NumPy int64 batches for the outward coordinate filters.
"""

from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from math import isqrt, prod
import importlib.util
import json
import time

import flint
from flint import arb, arb_mat, fmpq, ctx
import numpy as np
import sympy as sp

HERE = (_J_PROGRAM / 'verify.py').parent
AUTHOR = (_J_ROOT / 'mathematics/computations/programs/Yin_J_G0026')
PRECISION = 320


def load_roots():
    spec = importlib.util.spec_from_file_location("reviewer_j23", (_J_ROOT / 'mathematics/computations/programs/Yin_J_G0023/verify.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.independent_roots()


def ball(q):
    q = sp.Rational(q)
    return arb(fmpq(int(q.p),int(q.q)))


def euclidean(vector):
    return sum(v*v for v in vector).sqrt()


def check_certificate(c):
    ctx.prec = PRECISION
    beta, roots, root_brackets = load_roots()
    s = beta/(beta-1)
    assert s < arb(fmpq(67,10))
    matrix = [[beta**i for i in range(10)], [beta**(-i) for i in range(10)]]
    matrix += [[(z**i).real for i in range(10)] for z in roots]
    matrix += [[(z**i).imag for i in range(10)] for z in roots]
    inverse = arb_mat(matrix).inv()
    ab = list(map(int,c["original_coefficient_bounds"]))
    assert len(ab) == 10 and all(0 <= a <= 7 for a in ab)
    coefficient_bounds = []
    for i in range(10):
        bound = abs(inverse[i,0])+s*abs(inverse[i,1])+8*euclidean([inverse[i,j] for j in range(2,10)])
        # |a_i| <= bound < A_i+1 implies the saved integer bound A_i.
        assert bound < ab[i]+1
        coefficient_bounds.append(bound.str(50))
    u = sp.Matrix(c["unimodular_U"])
    assert u.shape == (10,10) and abs(u.det()) == 1
    ui = u.inv()
    assert all(v.q == 1 for v in ui) and ui*u == sp.eye(10)
    bb = [sum(ab[i]*abs(int(ui[i,j])) for i in range(10)) for j in range(10)]
    assert bb == c["reduced_coefficient_bounds"]
    B = sp.Matrix(c["integer_rounded_weighted_embedding_basis"])
    Q,H,E = c["B_scale"],c["T_scale"],c["embedding_scale"]
    assert Q > 0 and H > 0 and E > 0
    reduced = u*B
    gram = reduced*reduced.T/(Q*Q)
    l,d = gram.LDLdecomposition(hermitian=False)
    assert l*d*l.T == gram and all(d[i,i] > 0 for i in range(10))
    assert all(d[i,j] == 0 for i in range(10) for j in range(10) if i != j)
    assert all(l[i,i] == 1 for i in range(10))
    assert all(l[i,j] == 0 for i in range(10) for j in range(i+1,10))
    T = c["integer_triangular_T"]
    assert all(T[j][j] > 0 for j in range(10))
    assert all(T[i][j] == 0 for i in range(10) for j in range(i+1,10))
    weights = [arb(8).sqrt(),arb(8).sqrt()/ball(sp.Rational(67,10))]+[arb(1)]*8
    error_B, error_T = [], []
    for j in range(10):
        error_B.append(sum(ab[i]*abs(matrix[j][i]*weights[j]-ball(B[i,j]/Q)) for i in range(10)))
        error_T.append(sum(bb[i]*abs(ball(l[i,j])*ball(d[j,j]).sqrt()-ball(sp.Rational(T[i][j],H)))
                           for i in range(j,10)))
    eps_B,eps_T = euclidean(error_B),euclidean(error_T)
    radius_bound = (arb(80).sqrt()+eps_B+eps_T)**2
    radius = int(c["squared_enumeration_radius"])
    assert radius > 0 and ball(sp.Rational(radius,H*H)) >= radius_bound
    lo,hi = c["embedding_lower"],c["embedding_upper"]
    for j in range(10):
        for i in range(10):
            assert ball(sp.Rational(lo[j][i],E)) <= matrix[j][i].lower()
            assert ball(sp.Rational(hi[j][i],E)) >= matrix[j][i].upper()
    assert ball(sp.Rational(c["stable_outer_bound_scaled"],E)) >= s.upper()
    # Check every family of fixed-width intermediate operations, including
    # coordinate conversion before the original-box filter.
    limit = 2**63-1
    transform_bounds = [sum(bb[i]*abs(int(u[i,j])) for i in range(10)) for j in range(10)]
    triangular_bounds = [sum(bb[i]*abs(T[i][j]) for i in range(j,10)) for j in range(10)]
    coordinate_bounds = [sum(ab[i]*max(abs(lo[j][i]),abs(hi[j][i])) for i in range(10)) for j in range(10)]
    assert max(transform_bounds) < limit
    assert all(v*v < limit for v in triangular_bounds)
    assert all(v+isqrt(radius)+2 < limit for v in triangular_bounds)
    assert (isqrt(radius)+2)**2 < limit
    assert max(coordinate_bounds) < limit
    assert sum(v*v for v in coordinate_bounds[2:]) < limit
    assert 64*E*E < limit
    x = sp.symbols("x")
    p = x**10+x**9-x**7-x**6-x**5-x**4-x**3+x+1
    discriminant = int(sp.discriminant(p,x))
    assert discriminant == 1332031009 == 36497**2
    assert abs(arb_mat(matrix).det()).contains(ball(sp.Rational(36497,16)))
    return {
        "original_coefficient_upper_enclosures":coefficient_bounds,
        "root_brackets":root_brackets,"stable_bound":s.str(50),
        "unimodular_determinant":int(u.det()),"exact_LDL_identity":True,
        "error_B_upper_enclosure":eps_B.str(50),"error_T_upper_enclosure":eps_T.str(50),
        "required_squared_radius_over_H_squared":radius_bound.str(50),
        "saved_squared_radius":radius,"discriminant":discriminant,
        "covolume":"36497/16","dense_box_count":prod(2*a+1 for a in ab),
        "max_prebox_transform_coordinate_bound":max(transform_bounds),
        "max_triangular_coordinate_bound":max(triangular_bounds),
        "max_embedding_scaled_coordinate_bound":max(coordinate_bounds),
        "sum_neutral_scaled_coordinate_square_bounds":sum(v*v for v in coordinate_bounds[2:]),
        "all_int64_filter_and_source_branch_operations_bounded":True,
    }


def enumerate_independently(c):
    t,bb = c["integer_triangular_T"],c["reduced_coefficient_bounds"]
    u = np.array(c["unimodular_U"],dtype=np.int64)
    ab = np.array(c["original_coefficient_bounds"],dtype=np.int64)
    elo,ehi = [np.array(c[name],dtype=np.int64) for name in ("embedding_lower","embedding_upper")]
    E,stable = c["embedding_scale"],c["stable_outer_bound_scaled"]
    node_cap,candidate_cap = c["node_cap"],c["candidate_cap"]
    nodes = leaves = retained = 0
    b = [0]*10
    batch = []
    partial = (_J_OUTPUT / 'independent-states.partial.bin')
    destination = (_J_OUTPUT / 'independent-states.bin')
    start = time.monotonic()
    with partial.open("wb") as output:
        def flush():
            nonlocal batch,retained
            if not batch:
                return
            a = np.asarray(batch,dtype=np.int64) @ u
            batch = []
            a = a[np.all(np.abs(a) <= ab,axis=1)]
            if not len(a):
                return
            positive,negative = np.maximum(a,0),np.minimum(a,0)
            low = positive @ elo.T + negative @ ehi.T
            high = positive @ ehi.T + negative @ elo.T
            mask = (low[:,0] <= E) & (high[:,0] >= -E)
            mask &= (low[:,1] <= stable) & (high[:,1] >= -stable)
            minimum_abs = np.where((low<=0)&(high>=0),0,np.minimum(np.abs(low),np.abs(high)))
            neutral = np.sum(minimum_abs[:,2:]**2,axis=1,dtype=np.int64)
            mask &= neutral < 64*E*E
            a = a[mask]
            assert np.all(a >= -8) and np.all(a <= 7)
            packed = np.zeros(len(a),dtype=np.uint64)
            for j in range(10):
                packed |= (a[:,j]+8).astype(np.uint64) << np.uint64(4*j)
            retained += len(a)
            if retained > candidate_cap:
                raise RuntimeError("Independent candidate cap reached; no complete result published")
            output.write(packed.astype("<u8",copy=False).tobytes())

        def visit(j,remaining):
            nonlocal nodes,leaves,batch
            nodes += 1
            if nodes > node_cap:
                raise RuntimeError("Independent node cap reached; no complete result published")
            assert remaining >= 0
            if j < 0:
                leaves += 1
                batch.append(b.copy())
                if len(batch) >= 50000:
                    flush()
                return
            center = sum(b[i]*t[i][j] for i in range(j+1,10))
            span = isqrt(remaining)
            low = max(-bb[j],-((span+center)//t[j][j]))
            high = min(bb[j],(span-center)//t[j][j])
            for value in range(low,high+1):
                b[j] = value
                term = value*t[j][j]+center
                visit(j-1,remaining-term*term)
        visit(9,int(c["squared_enumeration_radius"]))
        flush()
    original = np.fromfile((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0026/compact-states.bin'),dtype="<u8")
    independent = np.fromfile(partial,dtype="<u8")
    assert len(independent) == retained and np.all(independent < np.uint64(1<<40))
    sorted_values = np.sort(independent)
    assert np.all(sorted_values[1:] != sorted_values[:-1])
    assert np.array_equal(np.sort(original),sorted_values)
    same_order = bool(np.array_equal(original,independent))
    for j in range(10):
        decoded = ((independent >> np.uint64(4*j)) & np.uint64(15)).astype(np.int64)-8
        assert np.all(np.abs(decoded) <= ab[j])
    report = json.loads(((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0026/enumeration.json')).read_text(encoding="utf-8-sig"))
    assert report["completed"] and report["nodes"] == nodes
    assert report["ellipsoid_leaves"] == leaves and report["retained_candidates"] == retained
    assert nodes < node_cap and retained < candidate_cap
    partial.replace(destination)
    return {'completed': True, 'nodes': nodes, 'ellipsoid_leaves': leaves, 'retained_candidates': retained, 'distinct_states': len(sorted_values), 'same_mathematical_state_set': True, 'same_sequence_order': same_order, 'node_cap': node_cap, 'candidate_cap': candidate_cap, 'both_caps_unhit': True, 'encoding': 'explicit little-endian uint64; nibble j minus 8'}


def main():
    certificate = json.loads(((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0026/enumeration-certificate.json')).read_text())
    bounds = check_certificate(certificate)
    print("Independent embedding, LDL, rounding, filter and overflow certificate checks passed.",flush=True)
    traversal = enumerate_independently(certificate)
    result = {'arb_precision_bits': PRECISION, 'reused_helpers': 'reviewer J23 independent_roots only; no author code imported', 'certificate': bounds, 'enumeration': traversal, 'scope': 'Complete independently reproduced finite superset of K8. No paths to zero or compact termination are checked.'}
    ((_J_OUTPUT / 'verification.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(traversal,indent=2),flush=True)


if __name__ == "__main__":
    main()
