"""Enumerate the irrational-trace degree-twelve cubic halves in the proved box."""

from collections import Counter
from dataclasses import dataclass
from math import isqrt


@dataclass(frozen=True)
class Quadratic:
    """A + B sqrt(discriminant) in the embedding with positive square root."""

    rational: int
    radical: int
    discriminant: int

    def __add__(self, other):
        if isinstance(other, int):
            return Quadratic(self.rational + other, self.radical, self.discriminant)
        return Quadratic(self.rational + other.rational, self.radical + other.radical,
                         self.discriminant)

    __radd__ = __add__

    def __neg__(self):
        return Quadratic(-self.rational, -self.radical, self.discriminant)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return other + (-self)

    def __mul__(self, other):
        if isinstance(other, int):
            return Quadratic(self.rational * other, self.radical * other, self.discriminant)
        real = self.rational * other.rational + self.discriminant * self.radical * other.radical
        radical = self.rational * other.radical + self.radical * other.rational
        return Quadratic(real, radical, self.discriminant)

    __rmul__ = __mul__

    def conjugate(self):
        return Quadratic(self.rational, -self.radical, self.discriminant)

    def sign(self):
        a, b = self.rational, self.radical
        if not a or not b or (a > 0) == (b > 0):
            return (a + b > 0) - (a + b < 0)
        squared_difference = a * a - self.discriminant * b * b
        return (1 if a > 0 else -1) * ((squared_difference > 0) - (squared_difference < 0))


def fundamental_discriminants():
    for disc in range(5, 91):
        if disc % 4 == 1:
            radicand = disc
        elif disc % 4 == 0 and (disc // 4) % 4 in (2, 3):
            radicand = disc // 4
        else:
            continue
        if all(radicand % (i * i) for i in range(2, isqrt(radicand) + 1)):
            yield disc


def twice_integers(disc, traces):
    for trace in traces:
        for coefficient in range(-4, 5):
            if (trace - coefficient * disc) % 2 == 0:
                yield Quadratic(trace, coefficient, disc)


def marked_cut_survives(t2, d4):
    """Use the weaker threshold 13/8 on the already positive squared difference d4."""
    if (t2 + 4).sign() > 0:
        numerator, denominator = 5 * (337 - 26 * t2), 546
    else:
        numerator, denominator = 21 * (26 * t2 + 129), 130
    return (numerator.sign() > 0
            and (numerator * numerator - denominator * denominator * d4).sign() > 0)


def main():
    counts = Counter()
    survivors = []
    for disc in fundamental_discriminants():
        for t2 in twice_integers(disc, range(-5, 13)):
            t2_other = t2.conjugate()
            if not t2.radical or 4 * t2.radical**2 * disc >= 361:
                continue
            if (t2 + 5).sign() <= 0 or (t2 - 13).sign() >= 0:
                continue
            if (t2_other + 6).sign() <= 0 or (t2_other - 12).sign() >= 0:
                continue
            for p2 in twice_integers(disc, range(20)):
                if p2.radical**2 * disc >= 121:
                    continue
                d4 = t2 * t2 - 8 * p2
                if d4.sign() <= 0 or (d4 - 16).sign() >= 0 or d4.conjugate().sign() >= 0:
                    continue
                p2_other = p2.conjugate()
                if (p2_other - 18).sign() >= 0:
                    continue
                delta4 = (p2_other * p2_other + 36 * p2_other + 12 * t2_other * p2_other
                          - 2 * t2_other * t2_other * t2_other - 108)
                if delta4.sign() >= 0:
                    continue
                counts[disc] += 1
                if marked_cut_survives(t2, d4):
                    survivors.append((disc, t2.rational, t2.radical, p2.rational, p2.radical))
    print("Before the marked root test:", sorted(counts.items()))
    print("Total before the marked root test:", sum(counts.values()))
    print("Surviving tuples:", survivors)
    if sum(counts.values()) != 40 or survivors:
        raise ArithmeticError("The enumerated box does not reproduce the stated counts.")


if __name__ == "__main__":
    main()
