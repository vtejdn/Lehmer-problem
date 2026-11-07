"""Exhaust the Phi_47-divisible slice of the fixed height-three degree-64 cell."""

from bisect import bisect_left, bisect_right
from itertools import product

from trace64_cell import disk_rows, signed_rows


def trace_vector(at_one, partial_sums):
    # Coefficients of the degree-18 cofactor from the leading end to its center.
    partial = (1, *partial_sums)
    outer = [1] + [right - left for left, right in zip(partial, partial[1:])]
    center = at_one - 2 * partial[-1]
    return (center, *reversed(outer))


def taylor_values(rows, coefficients):
    return [(sum(x * y for x, y in zip(real, coefficients)),
             sum(x * y for x, y in zip(imag, coefficients))) for real, imag in rows]


def full_lift(partials, at_one):
    trace = trace_vector(at_one, partials)
    cofactor = trace[:0:-1] + trace
    return [sum(cofactor[j] for j in range(len(cofactor)) if 0 <= i-j < 47)
            for i in range(65)]


def inspect(at_one, signs, rows):
    # B_j and B_(17-j) = S-B_j must both be in [-3,3].
    low, high = at_one - 3, 3
    values = range(low, high + 1)
    zero = (0,) * 8
    base = taylor_values(rows, trace_vector(at_one, zero))
    directions = []
    for j in range(8):
        unit = tuple(int(k == j) for k in range(8))
        point = taylor_values(rows, trace_vector(at_one, unit))
        directions.append([(r-r0, i-i0) for (r, i), (r0, i0) in zip(point, base)])

    # Bound the nonconstant Taylor tail over the entire integer box.
    # Taylor coefficients already include the powers of the disk radius.
    tail = 0
    for k in range(1, len(rows)):
        for component in (0, 1):
            lower = upper = base[k][component]
            for direction in directions:
                a = direction[k][component]
                lower += min(low * a, high * a)
                upper += max(low * a, high * a)
            tail += max(abs(lower), abs(upper))

    def half_sums(start):
        for coords in product(values, repeat=4):
            columns = directions[start:start+4]
            real = sum(v * col[0][0] for v, col in zip(coords, columns))
            imag = sum(v * col[0][1] for v, col in zip(coords, columns))
            yield real, imag, coords

    right = sorted(half_sums(4))
    keys = [row[0] for row in right]
    near = possible = bracketed = 0
    for left_re, left_im, left_coords in half_sums(0):
        center = -base[0][0] - left_re
        lo, hi = bisect_left(keys, center-tail), bisect_right(keys, center+tail)
        for right_re, right_im, right_coords in right[lo:hi]:
            imag = base[0][1] + left_im + right_im
            real = right_re - center
            if max(abs(real), abs(imag)) > tail:
                continue
            near += 1
            coords = left_coords + right_coords
            remainder = sum(abs(r)+abs(i) for r, i in
                            taylor_values(rows, trace_vector(at_one, coords))[1:])
            if real*real + imag*imag > remainder*remainder:
                continue
            possible += 1
            lift = full_lift(coords, at_one)
            assert len(lift) == 65 and lift == lift[::-1] and max(map(abs, lift)) <= 3
            if all(sum(a*b for a,b in zip(row, lift[32:])) > 0 for row in signs):
                bracketed += 1
                print("unresolved candidate", at_one, coords)
    size = len(values)**8
    print(f"S={at_one}  vectors={size}  uniform disk test={near}  "
          f"individual disk test={possible}  remaining with brackets={bracketed}")
    return size, bracketed


def main():
    signs = signed_rows()
    # Since the cofactor trace polynomial has degree nine, terms k>9 vanish.
    rows = [(r[:10], i[:10]) for r, i in disk_rows()[:10]]
    results = [inspect(s, signs, rows) for s in (1, 2, 3)]
    print("all vectors", sum(size for size, _ in results))
    print("unresolved", sum(left for _, left in results))


if __name__ == "__main__":
    main()
