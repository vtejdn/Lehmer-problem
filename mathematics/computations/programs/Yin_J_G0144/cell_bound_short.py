"""Certify the degree-64 cell on every height-three mutation of support <= 5."""

from collections import Counter
from itertools import combinations
from math import comb

from trace64_cell import D, N, R, SEPARATORS, U, V, seed_vector


HEIGHT = 3


def real_rows(base):
    rows = []
    for index, pt in enumerate(SEPARATORS):
        denominator = 1000
        # C_j(z+1/z) = z^j + z^(-j), including C_0 = 2 in the recurrence.
        numerators = [2, pt]
        for j in range(2, N+1):
            numerators.append(pt*numerators[-1] - denominator**2*numerators[-2])
        numerators[0] = 1  # The free central reciprocal coefficient occurs only once.
        row = [a * denominator**(N-j) * (-1)**index for j,a in enumerate(numerators)]
        seed_value = row[-1] + sum(a*b for a,b in zip(base, row))
        assert seed_value > 0
        rows.append((seed_value, row[:-1]))
    return rows


def disk_basis():
    # Gaussian-integer coefficients of D^N C_j(c + r*u); the target is |u|<1.
    x, y, h = U, V, R
    polys = [[(2, 0)], [(x, y), (h, 0)]]
    for j in range(2, N+1):
        coeffs = [[0, 0] for _ in range(j+1)]
        for k, (a, b) in enumerate(polys[-1]):
            coeffs[k][0] += x*a - y*b
            coeffs[k][1] += y*a + x*b
            coeffs[k+1][0] += h*a
            coeffs[k+1][1] += h*b
        for k, (a, b) in enumerate(polys[-2]):
            coeffs[k][0] -= D**2 * a
            coeffs[k][1] -= D**2 * b
        polys.append(coeffs)
    polys[0] = [(1, 0)]
    basis = []
    for j, poly in enumerate(polys):
        scale = D**(N-j)
        values = [coordinate*scale for term in poly for coordinate in term]
        basis.append(values + [0]*(2*(N+1) - len(values)))
    return basis


def disk_test(changes, seed_jet, basis):
    jet = list(seed_jet)
    for j, delta in changes:
        for k, value in enumerate(basis[j]):
            jet[k] += delta * value
    if max(abs(jet[0]), abs(jet[1])) > sum(map(abs, jet[2:])):
        return "disk_empty"
    if max(abs(jet[2]), abs(jet[3])) > sum(map(abs, jet[:2] + jet[4:])):
        return "one_root"
    return "undecided"


def visit_sign_survivors(left, right, split, rows, consume):
    """Join the two supports using all strict sign inequalities via integer bitsets."""
    # A canonical join requires every coordinate on the left to precede the right.
    masks_by_end = {}
    for end in {mut[-1][0] if mut else -1 for mut in left}:
        mask = 0
        for i, mut in enumerate(right):
            if not mut or end < mut[0][0]:
                mask |= 1 << i
        masks_by_end[end] = mask
    allowed = [masks_by_end[mut[-1][0] if mut else -1] for mut in left]
    for seed_value, weights in rows:
        rv = [sum(weights[j]*delta for j, delta in mut) for mut in right]
        lv = [sum(weights[j]*delta for j, delta in mut) for mut in left]
        # Descending right effects meet the strict lower threshold in this order.
        ordered_right = sorted(range(len(right)), key=rv.__getitem__, reverse=True)
        ordered_left = sorted(range(len(left)), key=lv.__getitem__)
        qualifying = 0
        pos = 0
        for i in ordered_left:
            if not allowed[i]:
                continue
            threshold = -seed_value-lv[i]
            while pos < len(right) and rv[ordered_right[pos]] > threshold:
                qualifying |= 1 << ordered_right[pos]
                pos += 1
            allowed[i] &= qualifying
    for i, mask in enumerate(allowed):
        while mask:
            low = mask & -mask
            mut = left[i] + right[low.bit_length()-1]
            assert len(mut) == split
            consume(mut)
            mask ^= low


def visit_weight_five(changes, pairs, rows, consume):
    # The middle changed coordinate is unique. Enumerate the two earlier and
    # two later coordinates with the same exact inequality join as at weight 4.
    for middle in range(2, N-2):
        left = [mut for mut in pairs if mut[-1][0] < middle]
        right = [mut for mut in pairs if mut[0][0] > middle]
        for change in changes[middle]:
            delta = change[1]
            translated = [(a + row[middle]*delta, row) for a, row in rows]
            def include_middle(outer):
                consume(outer[:2] + (change,) + outer[2:])
            visit_sign_survivors(left, right, 4, translated, include_middle)


def main(on_sign_survivor=None):
    base = seed_vector()
    rows = real_rows(base)
    basis = disk_basis()
    seed_jet = [basis[N][k] + sum(base[j]*basis[j][k] for j in range(N))
                for k in range(2*(N+1))]
    changes = [[(j, value-base[j]) for value in range(-HEIGHT, HEIGHT+1)
                if value != base[j]] for j in range(N)]
    single = [(entry,) for options in changes for entry in options]
    pairs = [(a,b) for j,k in combinations(range(N), 2) for a in changes[j] for b in changes[k]]
    blocks = [[()], single, pairs]
    totals = Counter()
    for weight in range(6):
        counts = Counter()
        def consume(mut):
            if on_sign_survivor is not None:
                coefficients = list(base)
                for j, delta in mut:
                    coefficients[j] += delta
                on_sign_survivor(mut, coefficients)
            result = disk_test(mut, seed_jet, basis)
            counts[result] += 1
            if result != "disk_empty":
                print("Inspect", result, mut)
        if weight < 5:
            lower = weight // 2
            visit_sign_survivors(blocks[lower], blocks[weight-lower], weight, rows, consume)
        else:
            visit_weight_five(changes, pairs, rows, consume)
        size = comb(N, weight)*(2*HEIGHT)**weight
        totals.update(counts)
        print(f"support={weight} domain={size} sign_survivors={sum(counts.values())}"
              f" empty_disk={counts['disk_empty']} one_root={counts['one_root']}"
              f" undecided={counts['undecided']}", flush=True)
    print("total domain", sum(comb(N,k)*6**k for k in range(6)),
          "total sign survivors", sum(totals.values()), "classifications", dict(totals))


if __name__ == "__main__":
    main()
