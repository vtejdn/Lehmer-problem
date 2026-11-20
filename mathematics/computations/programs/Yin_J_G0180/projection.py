"""Exact two-term projection for a fixed signed tuple at Lehmer's unit."""
from functools import reduce
from itertools import combinations
from math import gcd


POLYNOMIAL = (1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1)
WINDOW = 32
SIGNS = (1, 1, -1, -1, 1, 1)
ZERO = (0,) * 10
ONE = (1,) + ZERO[1:]


def add(left, right, scale=1):
    return tuple(a + scale * b for a, b in zip(left, right))


def powers(limit):
    result = {0: ONE}
    for index in range(limit):
        pos = result[index]
        result[index + 1] = add((0,) + pos[:-1], POLYNOMIAL[:-1], -pos[-1])
        neg = result[-index]
        result[-index - 1] = add(neg[1:] + (0,), POLYNOMIAL[1:], -neg[0])
    return result


def primitive(vector):
    content = reduce(gcd, vector, 0)
    if not content:
        return vector
    if next(entry for entry in vector if entry) < 0:
        content = -content
    return tuple(entry // content for entry in vector)


def terminal(terms, power, directions):
    for size in range(1, len(terms) // 2 + 1):
        for subset in combinations(terms, size):
            value = ZERO
            for exponent, coefficient in subset:
                value = add(value, power[exponent], coefficient)
            if value == ZERO or (size >= 2 and primitive(value) in directions):
                return False
    return True


def run():
    # (7/6)^16 > 10, so every rational-power split has |k| <= WINDOW+16.
    assert 7**16 > 10 * 6**16
    assert sum(c * 7**i * 6**(10-i) for i, c in enumerate(POLYNOMIAL)) < 0
    power = powers(WINDOW + 16)
    directions = {primitive(vector) for vector in power.values()}
    traces = {u: add(power[u], power[-u]) for u in range(1, WINDOW + 1)}
    target = {add(tuple(8 * x for x in ONE), v, 4): u for u, v in traces.items()}
    assert len(target) == WINDOW
    pairs = [(i, j, SIGNS[i] * SIGNS[j]) for i, j in combinations(range(6), 2)]
    # In base 1024 each of the 15 residues is represented by a digit 0,...,3.
    # No carries occur, and the low two bits in every digit test mod 4 exactly.
    low_bits = sum(3 << (10 * i) for i in range(10))
    packed = {(u, sign): sum(((sign * c) % 4) << (10 * i) for i, c in enumerate(v))
              for u, v in traces.items() for sign in (-1, 1)}
    stages = ('all', 'divisible', 'even', 'trace', 'phase', 'span', 'full', 'terminal')
    counts = dict.fromkeys(stages, 0)
    shapes = {stage: set() for stage in stages}
    witnesses = []
    even_trace = 0
    negative_phase = 0
    for rest in combinations(range(1, WINDOW + 1), 5):
        positions = (0, *rest)
        divisor = reduce(gcd, positions)
        shape = tuple(t // divisor for t in positions)
        def record(stage):
            counts[stage] += 1
            shapes[stage].add(shape)
        record('all')
        differences = [(positions[j] - positions[i], sign) for i, j, sign in pairs]
        if (6 + sum(packed[difference] for difference in differences)) & low_bits:
            continue
        record('divisible')
        small_sum = ZERO
        for exponent, sign in zip(positions, SIGNS):
            small_sum = add(small_sum, power[exponent], sign)
        if all(c % 2 == 0 for c in small_sum):
            record('even')
        norm = (6,) + ZERO[1:]
        for u, sign in differences:
            norm = add(norm, traces[u], sign)
        assert all(x % 4 == 0 for x in norm)
        gap = target.get(norm)
        if gap is None:
            continue
        record('trace')
        even_trace += all(c % 2 == 0 for c in small_sum)
        for s in range(-16, WINDOW + 17 - gap):
            t = s + gap
            if add(add(small_sum, power[s], 2), power[t], 2) == ZERO:
                negative_phase += 1
                break
            if add(add(small_sum, power[s], -2), power[t], -2) != ZERO:
                continue
            record('phase')
            if max(t, positions[-1]) - min(s, 0) > WINDOW:
                break
            record('span')
            if not positions[2] < s < t < positions[3]:
                break
            record('full')
            terms = sorted([*zip(positions, SIGNS), (s, -2), (t, -2)])
            if terminal(terms, power, directions):
                record('terminal')
                witnesses.append(tuple(e for e, _ in terms))
            break
    # Recompute the residual test in the binary quotient, on every support.
    modulus = sum((c % 2) << i for i, c in enumerate(POLYNOMIAL))
    binary = [1]
    for _ in range(WINDOW):
        nxt = binary[-1] << 1
        binary.append(nxt ^ modulus if nxt & (1 << 10) else nxt)
    assert binary.index(1, 1) == 31
    even_count = sum(1 for a, b, c, d, e in combinations(range(1, WINDOW + 1), 5)
                     if binary[a] ^ binary[b] ^ binary[c] ^ binary[d] ^ binary[e] == 1)
    assert even_count == counts['even']
    for stage in stages:
        print(stage, counts[stage], len(shapes[stage]))
    print('trace with even residual', even_trace)
    print('negative phase', negative_phase)
    print('terminal witnesses', witnesses)


if __name__ == '__main__':
    run()
