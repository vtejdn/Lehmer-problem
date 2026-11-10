"""Uniform closure parents by integer multiset counts and final rejection.

This helper constructs representations of a supplied certified core only.
It never evaluates a Mahler measure or mutates a parent.  The caller must
certify that the structurally checked, normalized core is cyclotomic-free.
See parent_sampling.md for the law, uniqueness and stopping conditions.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from functools import reduce
from math import gcd, isfinite
import time

from flint import fmpz_poly

from cyclotomic_closure import multiply


def _positive_integer(value, name):
    if type(value) is not int or value < 1:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class Factor:
    """Orders 1 and 2 denote squared real linear factors; others denote Phi_m."""

    order: int
    degree: int


class NeutralMultisets:
    """Count and unrank multisets, without enumerating products or parents."""

    def __init__(self, max_degree, *, max_order_bound=20000):
        if type(max_degree) is not int or max_degree < 0 or max_degree % 2:
            raise ValueError("max_degree must be a nonnegative even integer")
        _positive_integer(max_order_bound, "max_order_bound")
        started = time.perf_counter()
        bound = 2 * max_degree**2
        if bound > max_order_bound:
            raise ValueError("the proven order bound exceeds the explicit construction budget")
        self.max_degree = max_degree
        factors = []
        if max_degree:
            factors.extend((Factor(1, 2), Factor(2, 2)))
            phi = list(range(bound + 1))
            for prime in range(2, bound + 1):
                if phi[prime] == prime:
                    for multiple in range(prime, bound + 1, prime):
                        phi[multiple] -= phi[multiple] // prime
            factors.extend(Factor(m, phi[m]) for m in range(3, bound + 1)
                           if phi[m] <= max_degree)
        self.factors = tuple(factors)
        # ways[j][r]: multiplicities of factors j,...,s-1 totaling degree r.
        ways = [[0] * (max_degree + 1) for _ in range(len(factors) + 1)]
        ways[-1][0] = 1
        for j in range(len(factors) - 1, -1, -1):
            width = factors[j].degree
            for r in range(max_degree + 1):
                ways[j][r] = ways[j + 1][r]
                if r >= width:
                    ways[j][r] += ways[j][r - width]
        self.ways = ways
        self._polynomials = {}
        self.build = {
            "max_neutral_degree": max_degree,
            "order_bound": bound,
            "factor_count": len(factors),
            "dp_integer_cells": (len(factors) + 1) * (max_degree + 1),
            "build_seconds": time.perf_counter() - started,
        }

    def count(self, degree):
        if type(degree) is not int or not 0 <= degree <= self.max_degree:
            raise ValueError("degree lies outside this DP")
        return self.ways[0][degree]

    def unrank(self, degree, ticket):
        """Multiplicity-lexicographic unranking using exact integer blocks."""
        count = self.count(degree)
        if type(ticket) is not int or not 0 <= ticket < count:
            raise ValueError("multiset ticket lies outside [0, count)")
        powers = [0] * len(self.factors)
        remaining = degree
        for j, factor in enumerate(self.factors):
            while ticket >= self.ways[j + 1][remaining]:
                ticket -= self.ways[j + 1][remaining]
                remaining -= factor.degree
                assert remaining >= 0
                powers[j] += 1
        assert remaining == ticket == 0
        return tuple(powers)

    def rank(self, degree, powers):
        """Inverse rank, also useful for explicit nonempty-class witnesses."""
        self.count(degree)
        powers = tuple(powers)
        if (len(powers) != len(self.factors)
                or any(type(x) is not int or x < 0 for x in powers)
                or sum(x * f.degree for x, f in zip(powers, self.factors)) != degree):
            raise ValueError("invalid multiset multiplicities")
        ticket, remaining = 0, degree
        for j, (power, factor) in enumerate(zip(powers, self.factors)):
            for _ in range(power):
                ticket += self.ways[j + 1][remaining]
                remaining -= factor.degree
        assert remaining == 0 and 0 <= ticket < self.count(degree)
        return ticket

    def polynomial(self, powers):
        """Exact multiplication; deliberately no intermediate height pruning."""
        powers = tuple(powers)
        if (len(powers) != len(self.factors)
                or any(type(x) is not int or x < 0 for x in powers)):
            raise ValueError("invalid multiset multiplicities")
        degree = sum(x * f.degree for x, f in zip(powers, self.factors))
        if degree > self.max_degree:
            raise ValueError("multiset degree exceeds this DP")
        product = (1,)
        for factor, power in zip(self.factors, powers):
            if not power:
                continue
            if factor.order not in self._polynomials:
                if factor.order == 1:
                    polynomial = (1, -2, 1)
                elif factor.order == 2:
                    polynomial = (1, 2, 1)
                else:
                    polynomial = tuple(map(int, fmpz_poly.cyclotomic(factor.order)))
                assert len(polynomial) - 1 == factor.degree
                assert polynomial == polynomial[::-1] and polynomial[0] == polynomial[-1] == 1
                self._polynomials[factor.order] = polynomial
            for _ in range(power):
                product = multiply(product, self._polynomials[factor.order])
        assert len(product) == degree + 1
        return product


class ParentSampler:
    """Same accepted-parent law as uniform choice from the complete closure.

    The default construction budget permits an order sieve through 20000.
    Changing it is explicit; no parent enumeration is hidden in construction.
    """

    def __init__(self, core, degree, height=4, *, max_order_bound=20000):
        started = time.perf_counter()
        core = tuple(core)
        d = len(core) - 1
        if (d < 2 or d % 2 or core != core[::-1]
                or core[0] != 1 or core[-1] != 1
                or any(type(a) is not int for a in core)
                or reduce(gcd, (i for i, a in enumerate(core) if i and a), 0) != 1):
            raise ValueError("an even monic reciprocal integer core with exponent gcd one is required")
        opposite = tuple(a * (-1)**i for i, a in enumerate(core))
        if core[::-1] > opposite[::-1]:
            raise ValueError("the core must have the frozen descending-coefficient sign normalization")
        if type(degree) is not int or degree < d or degree % 2:
            raise ValueError("an even output degree at least the core degree is required")
        _positive_integer(height, "height")
        self.core, self.degree, self.height = core, degree, height
        self.neutral = NeutralMultisets(degree - d, max_order_bound=max_order_bound)
        self.weights = tuple(self.neutral.count(degree - k * d)
                             for k in range(1, degree // d + 1))
        self.weight_sum = sum(self.weights)
        assert self.weight_sum > 0
        self.build = dict(self.neutral.build, build_seconds=time.perf_counter() - started,
                          degree=degree, core_degree=d, height=height,
                          substitution_weights=list(self.weights),
                          raw_parent_count=2 * self.weight_sum)

    def select_k(self, ticket):
        if type(ticket) is not int or not 0 <= ticket < self.weight_sum:
            raise ValueError("substitution ticket lies outside [0, weight_sum)")
        for k, count in enumerate(self.weights, 1):
            if ticket < count:
                return k
            ticket -= count
        raise AssertionError("unreachable substitution interval")

    def construct(self, k, sign, neutral_ticket):
        if type(k) is not int or not 1 <= k <= len(self.weights):
            raise ValueError("invalid substitution index")
        if type(sign) is not int or sign not in (-1, 1):
            raise ValueError("sign must be -1 or 1")
        remainder = self.degree - k * (len(self.core) - 1)
        powers = self.neutral.unrank(remainder, neutral_ticket)
        neutral = self.neutral.polynomial(powers)
        lifted = [0] * (k * (len(self.core) - 1) + 1)
        for i, a in enumerate(self.core):
            lifted[k * i] = a * sign**i
        polynomial = multiply(lifted, neutral)
        assert len(polynomial) == self.degree + 1 and polynomial == polynomial[::-1]
        assert polynomial[0] == polynomial[-1] == 1
        observed_height = max(map(abs, polynomial))
        return {
            "substitution_index": k, "sign": sign, "neutral_ticket": neutral_ticket,
            "neutral_factor_powers": [[f.order, m] for f, m in zip(self.neutral.factors, powers) if m],
            "coefficients_ascending": list(polynomial), "observed_height": observed_height,
            "accepted": observed_height <= self.height,
        }

    def draw_raw(self, rng):
        """Exactly three randrange calls, with integer bounds only."""
        k = self.select_k(rng.randrange(self.weight_sum))
        sign = (-1, 1)[rng.randrange(2)]
        return self.construct(k, sign, rng.randrange(self.weights[k - 1]))

    def sample_accepted(self, rng, *, max_attempts, deadline=None,
                        clock=time.perf_counter, on_attempt=None):
        """Stop only BEFORE an attempt; an in-flight attempt always completes.

        All rejected attempts are counted and charged.  max_attempts is an
        integer bound even when a deadline is supplied.  on_attempt receives
        a detached copy of each outcome; its cost is included in total time.
        It must not alter the sampler/RNG or interrupt the call. Exceptions
        propagate as failures, never as height rejections.
        A hard external interruption is outside this conditional-uniform law.
        """
        _positive_integer(max_attempts, "max_attempts")
        if deadline is not None and (type(deadline) not in (int, float) or not isfinite(deadline)):
            raise ValueError("deadline must be an absolute value for the supplied clock")
        started = clock()
        attempts = rejected = 0
        construction_seconds = last_seconds = max_seconds = 0.0
        parent = None
        status = "attempt_limit"
        while attempts < max_attempts:
            before = clock()
            if deadline is not None and before >= deadline:
                status = "deadline"
                break
            candidate = self.draw_raw(rng)
            after = clock()
            last_seconds = after - before
            construction_seconds += last_seconds
            max_seconds = max(max_seconds, last_seconds)
            attempts += 1
            rejected += not candidate["accepted"]
            if on_attempt is not None:
                on_attempt(attempts, deepcopy(candidate), last_seconds)
            if candidate["accepted"]:
                parent, status = candidate, "accepted"
                break
        finished = clock()
        return {
            "status": status, "parent": parent, "attempts_started": attempts,
            "height_rejections": rejected, "max_attempts": max_attempts,
            "elapsed_seconds": finished - started,
            "construction_seconds": construction_seconds,
            "last_attempt_seconds": last_seconds, "max_attempt_seconds": max_seconds,
            "soft_overrun_seconds": max(0.0, finished - deadline) if deadline is not None else 0.0,
        }
