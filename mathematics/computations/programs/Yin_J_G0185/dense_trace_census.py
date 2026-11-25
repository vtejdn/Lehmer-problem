"""Exhaust the first-nonunit pole grid for every height through trace degree 40."""
from collections import Counter
from math import factorial
from reflected_trace_search import prefix_search


def main():
    maximum = 40
    # Voutier gives q < log(6D)^3/2. The displayed rational sum proves exp(6)>240.
    denominator = factorial(8)
    assert sum(6**j * (denominator // factorial(j)) for j in range(9)) > 240 * denominator
    total = Counter()
    largest_moment = 0
    witnesses = []
    for q in range(2, 108):
        for degree in range(2, maximum + 1):
            for depth in sorted({min(degree, k) for k in (10, 18, 28, degree)}):
                status, stage, results = prefix_search(q, degree, depth)
                if status != "open":
                    break
            if status == "open":
                raise ValueError((q, degree, "unfinished"))
            total[status] += 1
            if status == "moment":
                largest_moment = max(largest_moment, stage)
            witnesses.extend((q, degree, h) for h in results)
    print("Pairs by final status:", sorted(total.items()))
    print("Largest moment used for exclusion:", largest_moment)
    print("Realizations:", witnesses)


if __name__ == "__main__":
    main()
