from collections import Counter

witnesses = Counter()
second = []
for n in range(4, 40):
    a = [1] + [-1] * (n - 1) + [1]
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if p < n:
            continue
        sums = [0]
        for t in range(1, 2 * p + 1):
            total = sum(a[i] * sums[t-i] for i in range(1, min(t-1, n) + 1))
            if t <= n:
                total += t * a[t]
            sums.append(-total % (p*p))
        j = next(j for j in (1, 2) if (sums[p*j] - sums[j]) % (p*p))
        witnesses[j] += 1
        if j == 2:
            second.append((n, p))
print(witnesses, second)
