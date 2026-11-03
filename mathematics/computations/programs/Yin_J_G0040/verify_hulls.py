"""Exact inner-polytope proof; no numerical hull facets or radii are trusted."""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import random
import time
from exact import roots, word_geometry, image, floor

GRID = 10**10
Q_RADIUS = F(201, 1000)
ACTUAL_RADIUS = F(2009, 10000)
COORDINATE_ERROR = F(1, 100000)


def det3(rows):
    a, b, c = rows
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))


def plane(face, vertices, interior_sum):
    base = vertices[face[0]]
    rows = [[vertices[i][j]-base[j] for j in range(4)] for i in face[1:]]
    normal = [(-1)**j*det3([[r[k] for k in range(4) if k != j] for r in rows])
              for j in range(4)]
    offset = -sum(a*b for a, b in zip(normal, base))
    side = sum(a*b for a, b in zip(normal, interior_sum))+5*offset
    if side == 0: raise ValueError('degenerate face or interior point')
    if side > 0: normal, offset = [-n for n in normal], -offset
    return tuple(normal), offset


def evaluate(plane_, vertex):
    normal, offset = plane_
    return sum(a*b for a, b in zip(normal, vertex))+offset


def exact_hull(vertices):
    # The first five points form an exact simplex; its centroid stays strictly
    # inside every subsequent hull. General position is explicitly checked at
    # every inserted point against all current facet planes.
    assert len(vertices) >= 5
    interior = [sum(v[j] for v in vertices[:5]) for j in range(4)]
    facets = {tuple(face): plane(tuple(face), vertices, interior)
              for face in combinations(range(5), 4)}
    assert all(evaluate(p, vertices[i]) < 0
               for face, p in facets.items() for i in range(5) if i not in face)
    for index in range(5, len(vertices)):
        sides = {face: evaluate(p, vertices[index]) for face, p in facets.items()}
        if any(side == 0 for side in sides.values()):
            raise ValueError('coplanar insertion; retry harmless rational perturbation')
        visible = [face for face, side in sides.items() if side > 0]
        if not visible: continue
        ridge_counts = {}
        for face in visible:
            for ridge in combinations(face, 3):
                ridge_counts[ridge] = ridge_counts.get(ridge, 0)+1
        assert all(count in (1, 2) for count in ridge_counts.values())
        horizon = [ridge for ridge, count in ridge_counts.items() if count == 1]
        for face in visible: del facets[face]
        for ridge in horizon:
            face = tuple(sorted((*ridge, index)))
            assert face not in facets
            facets[face] = plane(face, vertices, interior)
        # The exact visible-facet/horizon operation builds the next hull.
        assert all(evaluate(p, vertices[i]) <= 0
                   for p in facets.values() for i in range(index+1))
    ridge_counts = {}
    for face in facets:
        for ridge in combinations(face, 3): ridge_counts[ridge] = ridge_counts.get(ridge, 0)+1
    assert all(count == 2 for count in ridge_counts.values())
    return facets


def main():
    started = time.monotonic()
    base = (_J_PROGRAM / 'verify_hulls.py').parent
    data = json.loads(((_J_OUTPUT / 'cover12.json')).read_text())
    assert data['grid'] == 100 and data['max_length'] == 12
    assert [row['j'] for row in data['cells']] == list(range(50, 100))
    beta, zs = roots()
    cached = {}
    result = []
    minimum_norm2 = None
    minimum_real_margin = None
    for row in data['cells']:
        j = row['j']
        words = row['words']
        intervals = []
        for word in words:
            assert 1 <= len(word) <= 12
            key = tuple(word)
            if key not in cached: cached[key] = word_geometry(word, beta, zs)
            _, norm2, vector = cached[key]
            minimum_norm2 = min(minimum_norm2, norm2[0]) if minimum_norm2 is not None else norm2[0]
            endpoints = image(word, (F(j, 100), F(j+1, 100)), beta)
            margin = min(endpoints[0]+1, 1-endpoints[1])
            assert margin > 0
            minimum_real_margin = min(minimum_real_margin, margin) if minimum_real_margin is not None else margin
            intervals.append(vector)
        for trial in range(5):
            rng = random.Random(1729+j*100+trial)
            vertices = [[floor((a+b)*GRID/2)+rng.randrange(-30, 31) for a, b in vector]
                        for vector in intervals]
            for vertex, vector in zip(vertices, intervals):
                assert all(max(abs(F(v, GRID)-a), abs(F(v, GRID)-b)) <= COORDINATE_ERROR
                           for v, (a, b) in zip(vertex, vector))
            try:
                facets = exact_hull(vertices)
                break
            except ValueError:
                if trial == 4: raise
        for normal, offset in facets.values():
            assert offset < 0
            # Exact Euclidean distance of the origin to every supporting plane.
            assert offset*offset > Q_RADIUS**2*GRID**2*sum(n*n for n in normal)
        assert Q_RADIUS-2*COORDINATE_ERROR > ACTUAL_RADIUS
        result.append({'j': j, 'selected_words': len(words), 'rational_facets': len(facets),
                       'perturbation_trial': trial, 'rational_vertices': vertices})
        print(json.dumps({k: v for k, v in result[-1].items() if k != 'rational_vertices'}), flush=True)
    m = F(floor(minimum_norm2*1000), 1000)
    assert m > 0
    delta = m*(5*ACTUAL_RADIUS-1)
    output = {'exact_cells': len(result), 'word_uses': sum((row['selected_words'] for row in result)), 'distinct_words': len(cached), 'max_length': 12, 'rational_inner_radius': str(Q_RADIUS), 'actual_inner_radius': str(ACTUAL_RADIUS), 'coordinate_error_bound': str(COORDINATE_ERROR), 'minimum_squared_displacement_lower': str(m), 'squared_radius_drop_lower': str(delta), 'minimum_real_margin_lower': str(F(floor(minimum_real_margin * 10 ** 8), 10 ** 8)), 'rational_grid': GRID, 'cells': result}
    ((_J_OUTPUT / 'hull_verification.json')).write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: v for k, v in output.items() if k != 'cells'}))


if __name__ == '__main__': main()
