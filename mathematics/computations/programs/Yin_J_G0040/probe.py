"""Bounded floating discovery for actual normalized ideal-preserving vectors."""
import argparse
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sys
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scipy-path')
    parser.add_argument('--length', type=int, default=10)
    parser.add_argument('--cells', default='50,75,99')
    parser.add_argument('--grid', type=int, default=100)
    parser.add_argument('--output', default='pilot.json')
    args = parser.parse_args()
    if args.scipy_path:
        sys.path.insert(0, args.scipy_path)
    import numpy as np
    from scipy.spatial import ConvexHull
    start = time.monotonic()
    roots = np.roots([1, -1, 0, -1, 0, -1, 1])
    beta = max(r.real for r in roots if abs(r.imag) < 1e-8)
    zs = np.array(sorted([r for r in roots if r.imag > 1e-8], key=lambda r: r.real))
    assert len(zs) == 2
    S = beta/(beta-1)
    J = 2**0.5 * (4/S)**0.25
    cells = [int(x) for x in args.cells.split(',')]
    lists = {j: [] for j in cells}
    ids = {j: [] for j in cells}
    q = np.zeros(1)
    c = np.zeros((1, 2), dtype=complex)
    residue = np.zeros(1, dtype=np.uint8)
    mb = np.array([0, 2, 3, 1], dtype=np.uint8)
    for k in range(1, args.length+1):
        old_size = len(q)
        q = np.repeat(q, 3)*beta + np.tile([-1, 0, 1], old_size)
        c = np.repeat(c, 3, axis=0) + np.tile(
            np.array([-1, 0, 1])[:, None]*zs[None, :]**(-k), (old_size, 1))
        residue = np.repeat(mb[residue], 3) ^ np.tile([1, 0, 1], old_size).astype(np.uint8)
        v = np.column_stack((c.real, c.imag))
        norm2 = np.sum(v*v, axis=1)
        eligible = (residue == 0) & (norm2 > 1e-12)
        for j in cells:
            low = beta**k*j/args.grid+q
            high = beta**k*(j+1)/args.grid+q
            ix = np.flatnonzero(eligible & (low > -1+1e-7) & (high < 1-1e-7))
            lists[j].append(v[ix]/norm2[ix, None])
            ids[j].extend((k, int(i)) for i in ix)

    def word(k, index):
        out = []
        for _ in range(k):
            out.append(index % 3 - 1)
            index //= 3
        return out[::-1]

    output = {'scope': 'floating discovery only', 'beta': beta, 'J': J,
              'target_radius': 1/(2*J), 'max_length': args.length,
              'grid': args.grid, 'coordinate_order': 'Re1,Re2,Im1,Im2', 'cells': []}
    for j in cells:
        V = np.concatenate(lists[j])
        hull = ConvexHull(V)
        distances = -hull.equations[:, -1]/np.linalg.norm(hull.equations[:, :-1], axis=1)
        worst = int(np.argmin(distances))
        vertex_indices = list(map(int, hull.vertices))
        index_map = {index: i for i, index in enumerate(vertex_indices)}
        row = {'j': j, 'candidate_count': len(V), 'vertices': len(hull.vertices),
               'facets': len(hull.simplices), 'numerical_radius': float(distances[worst]),
               'worst_normal': hull.equations[worst, :-1].tolist(),
               'words': [word(*ids[j][i]) for i in vertex_indices],
               'facet_vertex_indices': [[index_map[int(i)] for i in simplex]
                                        for simplex in hull.simplices]}
        output['cells'].append(row)
        print(json.dumps({key: value for key, value in row.items()
                          if key not in ('words', 'facet_vertex_indices')}), flush=True)
    pass
    (_J_OUTPUT/args.output).write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'target_radius': output['target_radius']}), flush=True)


if __name__ == '__main__':
    main()
