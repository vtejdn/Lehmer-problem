using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;

// Enumerate reciprocal polynomials by their first half of Newton sums.
class Reciprocal {
    readonly int degree, half, last, first, second;
    readonly int[] limits, coeff, sums;
    readonly long[][] weights, caps;
    readonly BigInteger[][][] exact;
    readonly long[] passed;
    readonly TextWriter survivors;
    long prefixPasses, orbits, endpointPasses;

    static int[] Ints(string row) {
        return row.Split(' ').Select(int.Parse).ToArray();
    }

    Reciprocal(string[] args, TextWriter output) {
        string[] config = File.ReadAllLines(args[0]);
        degree = int.Parse(config[0]);
        half = degree / 2;
        limits = Ints(config[1]);
        last = limits.Length - 1;
        first = int.Parse(args[1]);
        second = int.Parse(args[2]);
        coeff = new int[degree + 1];
        coeff[0] = 1;
        sums = new int[last + 1];
        passed = new long[last + 1];
        weights = new long[5][];
        caps = new long[5][];
        exact = new BigInteger[5][][];
        int line = 2;
        for (int m = 0; m < 5; ++m) {
            weights[m] = config[line++].Split(' ').Select(long.Parse).ToArray();
            caps[m] = config[line++].Split(' ').Select(long.Parse).ToArray();
            exact[m] = new BigInteger[16][];
            for (int k = 1; k <= 15; ++k)
                exact[m][k] = config[line++].Split(' ').Select(BigInteger.Parse).ToArray();
        }
        survivors = output;
    }

    bool PassesPrefix() {
        for (int m = 0; m < 5; ++m) {
            long score = 0, error = 0;
            for (int k = 1; k <= 15; ++k) {
                score += weights[m][k] * sums[k];
                error += Math.Abs(sums[k]);
                long cap = caps[m][k];
                if (score > cap + error) return false;
                if (score > cap - error) {
                    BigInteger[] test = exact[m][k];
                    BigInteger fullScore = 0;
                    for (int j = 1; j <= k; ++j) fullScore += test[j] * sums[j];
                    if (fullScore > test[0]) return false;
                }
            }
        }
        return true;
    }

    bool IsRepresentative() {
        for (int q = 2; q <= degree; ++q) {
            if (degree % q != 0) continue;
            bool substitution = true;
            for (int j = 1; j <= half; ++j)
                if (j % q != 0 && coeff[j] != 0) { substitution = false; break; }
            if (substitution) return false;
        }
        for (int j = 1; j <= half; j += 2)
            if (sums[j] != 0) return sums[j] > 0;
        return false;
    }

    void Extend(int k) {
        int sum = 0;
        for (int j = 1; j < k; ++j) sum += coeff[k-j] * sums[j];
        int lo = -limits[k], hi = limits[k];
        if (k == 1) lo = hi = first;
        if (k == 2 && second != 99) lo = hi = second;
        int residue = ((-sum-lo) % k + k) % k;
        for (int s = lo + residue; s <= hi; s += k) {
            sums[k] = s;
            coeff[k] = -(sum + s)/k;
            if (k == 15) {
                if (!PassesPrefix()) continue;
                ++prefixPasses;
            }
            if (k < half) Extend(k+1);
            else if (first != 0 || IsRepresentative()) Check();
        }
    }

    void Check() {
        ++orbits;
        // Coefficients after the center are reflected only if the first new sum passes.
        int k = half + 1;
        long total = (long)k * coeff[half-1];
        for (int i = 1; i <= half; ++i) total += (long)coeff[i] * sums[k-i];
        if (Math.Abs(total) > limits[k]) return;
        sums[k] = (int)-total;
        ++passed[k];
        for (int i = half+1; i <= degree; ++i) coeff[i] = coeff[degree-i];
        for (++k; k <= last; ++k) {
            total = k <= degree ? (long)k * coeff[k] : 0;
            for (int i = 1; i <= Math.Min(degree,k-1); ++i) total += (long)coeff[i] * sums[k-i];
            if (Math.Abs(total) > limits[k]) return;
            sums[k] = (int)-total;
            ++passed[k];
        }
        long positive = 0, negative = 0;
        for (int i = 0; i <= degree; ++i) {
            positive += coeff[i];
            negative += (i % 2 == 0 ? coeff[i] : -coeff[i]);
        }
        if (positive == 0 || negative == 0) return;
        ++endpointPasses;
        survivors.WriteLine(string.Join(" ", coeff.Take(half+1)));
    }

    static int Main(string[] args) {
        using (var output = new StreamWriter(args[3])) {
            var test = new Reciprocal(args, output);
            if (test.first < 0 || test.first > test.limits[1] ||
                (test.second != 99 && Math.Abs(test.second) > test.limits[2])) return 2;
            test.Extend(1);
            Console.WriteLine(test.prefixPasses + " " + test.orbits + " " + test.endpointPasses);
            Console.WriteLine(string.Join(" ", test.passed.Skip(test.half+1)));
        }
        return 0;
    }
}
