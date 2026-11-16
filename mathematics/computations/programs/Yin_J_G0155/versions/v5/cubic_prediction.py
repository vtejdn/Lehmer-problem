"""Enclose cubic roots and exhaust all integer Fourier continuations."""

from dataclasses import dataclass
from math import isqrt


SCALE = 1 << 192


@dataclass(frozen=True)
class Interval:
    """Endpoints in units of 1/SCALE, with outward integer rounding."""

    lo: int
    hi: int

    def __add__(self, other):
        other = point(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-point(other))

    def __rsub__(self, other):
        return point(other) + (-self)

    def __mul__(self, other):
        other = point(other)
        corners = [a * b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Interval(min(corners) // SCALE, -(-max(corners) // SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = point(other)
        assert other.lo > 0 or other.hi < 0
        reciprocal = Interval(SCALE**2 // other.hi, -(-SCALE**2 // other.lo))
        return self * reciprocal

    def sqrt(self):
        # In every call the underlying quantity is known to be nonnegative.
        assert self.hi >= 0
        upper = isqrt(self.hi * SCALE)
        return Interval(isqrt(max(0, self.lo) * SCALE),
                        upper + (upper**2 < self.hi * SCALE))


def point(value):
    if isinstance(value, Interval):
        return value
    return Interval(value * SCALE, value * SCALE)


def real_root(a, b, c, d):
    low, high = -2 * SCALE, -3 * SCALE // 2
    while high - low > 1:
        mid = (low + high) // 2
        value = ((a * mid + b * SCALE) * mid + c * SCALE**2) * mid + d * SCALE**3
        if value == 0:
            return Interval(mid, mid)
        if value < 0:
            low = mid
        else:
            high = mid
    return Interval(low, high)


def candidates():
    for a in range(1, 4):
        for b in range(-21, 22):
            for c in range(-49, 50):
                for d in range(1, 39):
                    if -8*a + 4*b - 2*c + d >= 0 or -27*a + 18*b - 12*c + 8*d <= 0:
                        continue
                    disc = 18*a*b*c*d - 4*b**3*d + b*b*c*c - 4*a*c**3 - 27*a*a*d*d
                    if disc >= 0:
                        continue
                    y = real_root(a, b, c, d)
                    real_part = (-point(b) / a - y) / 2
                    modulus_sq = -point(d) / (a * y)
                    axis = ((4 + modulus_sq + 4 * real_part).sqrt()
                            + (4 + modulus_sq - 4 * real_part).sqrt()) / 2
                    radius = (axis + (axis * axis - 4).sqrt()) / 2
                    measure = a * radius * radius
                    if measure.lo <= (-12 - 8 * y).hi:
                        yield (a, b, c, d), y, measure


def prediction_tree(y, measure):
    c0, c1 = -4 * y, point(6)
    first = c1 / c0
    error = c0 - first * c1
    if error.hi < measure.lo:
        return 1, 0
    states = [([2, 0, 4], [c0, c1], [first], error)]
    largest = 1
    for k in range(2, 31):
        following = []
        for a, c, predictor, error in states:
            assert error.lo > 0
            predicted = sum((v * c[k-j] for j, v in enumerate(predictor, 1)), point(0))
            # A true extension needs (c_k - predicted)^2 <= error*(error - M).
            allowance = error * (error - measure)
            if allowance.hi < 0:
                continue
            radius = allowance.sqrt().hi
            offset = -(a[k-3] if k >= 3 else 0) - y * (a[k] - a[k-2])
            center = predicted - offset
            low = -(-(center.lo - radius) // SCALE)
            high = (center.hi + radius) // SCALE
            for coordinate in range(low, high + 1):
                moment = offset + coordinate
                residual = moment - predicted
                reflection = residual / error
                next_error = error - reflection * residual
                if next_error.hi < measure.lo:
                    continue
                updated = [v - reflection * w for v, w in zip(predictor, reversed(predictor))]
                following.append((a + [coordinate], c + [moment],
                                  updated + [reflection], next_error))
        if not following:
            return k, largest
        states = following
        largest = max(largest, len(states))
    raise RuntimeError("a surviving branch requires further analysis")


if __name__ == "__main__":
    for coefficients, y, measure in candidates():
        depth, largest = prediction_tree(y, measure)
        print(*coefficients, depth, largest)
