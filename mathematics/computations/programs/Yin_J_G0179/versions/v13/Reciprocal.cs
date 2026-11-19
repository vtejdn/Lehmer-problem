using System;
using System.IO;
using System.Linq;

// Enumerate trace tuples by prime-power congruences and impose reciprocal
// symmetry at the middle coefficient. All polynomial arithmetic is signed.
class Reciprocal {
    const int Last = 120;
    readonly int degree, half;
    readonly int[] prefix, bounds, sums = new int[Last + 1];
    readonly int[][] parents, weights;
    readonly long[] coefficients, counts = new long[7];
    readonly TextWriter survivors;

    Reciprocal(int degree, string config, int[] prefix, TextWriter survivors) {
        this.degree = degree;
        half = degree / 2;
        this.prefix = prefix;
        this.survivors = survivors;
        bounds = File.ReadAllText(config).Trim().Split(' ').Select(int.Parse).ToArray();
        coefficients = new long[degree + 1];
        coefficients[0] = 1;
        parents = new int[half + 1][];
        weights = new int[half + 1][];
        for (int k = 1; k <= half; ++k) {
            var sources = new System.Collections.Generic.List<int>();
            var multipliers = new System.Collections.Generic.List<int>();
            int remaining = k;
            for (int p = 2; p <= remaining; ++p) {
                if (remaining % p != 0) continue;
                int power = 1;
                while (remaining % p == 0) { remaining /= p; power *= p; }
                int w = k / power;
                while (w % power != 1) w += k / power;
                sources.Add(k / p);
                multipliers.Add(w);
            }
            parents[k] = sources.ToArray();
            weights[k] = multipliers.ToArray();
        }
    }

    void Extend(int k, bool oriented) {
        int residue = 0;
        for (int j = 0; j < parents[k].Length; ++j)
            residue += weights[k][j] * sums[parents[k][j]];
        int lower = -bounds[k], upper = bounds[k];
        if (k <= prefix.Length) lower = upper = prefix[k - 1];
        if (!oriented && k % 2 == 1) lower = Math.Max(lower, 0);
        int first = lower + ((residue - lower) % k + k) % k;
        if (first > upper) return;
        long sum = 0;
        for (int j = 1; j < k; ++j) sum += coefficients[j] * sums[k - j];
        for (int value = first; value <= upper; value += k) {
            sums[k] = value;
            coefficients[k] = -(sum + value) / k;
            bool next = oriented || (k % 2 != 0 && value > 0);
            if (k < half) Extend(k + 1, next);
            else if (next && (sums[1] != 0 || IsPrimitive())) Check();
        }
    }

    bool IsPrimitive() {
        int factor = degree;
        for (int i = 1; i <= half && factor > 1; ++i) {
            if (coefficients[i] == 0) continue;
            int x = i;
            while (x > 0) { int next = factor % x; factor = x; x = next; }
        }
        return factor == 1;
    }

    void Check() {
        ++counts[0];
        for (int i = half + 1; i <= degree; ++i) coefficients[i] = coefficients[degree - i];
        for (int k = half + 1; k <= Last; ++k) {
            if (k == half + 10) {
                long even = 0, odd = 0;
                for (int i = 0; i <= degree; i += 2) even += coefficients[i];
                for (int i = 1; i <= degree; i += 2) odd += coefficients[i];
                if (even == odd || even == -odd) { ++counts[3]; return; }
            }
            long total = k <= degree ? k * coefficients[k] : 0;
            for (int i = 1; i < k && i <= degree; ++i)
                total += coefficients[i] * sums[k-i];
            if (total < -bounds[k] || total > bounds[k]) {
                if (k >= half + 10) ++counts[4];
                return;
            }
            sums[k] = (int)-total;
            if (k == half + 1) ++counts[1];
            if (k == half + 9) ++counts[2];
        }
        foreach (int linear in new int[] {-1, 0, 1}) {
            long real = 0, imag = 0;
            for (int i = degree; i >= 0; --i) {
                long next = coefficients[i] - imag;
                imag = real + linear * imag;
                real = next;
            }
            if (real == 0 && imag == 0) { ++counts[5]; return; }
        }
        ++counts[6];
        survivors.WriteLine(string.Join(" ", coefficients.Take(half + 1)));
    }

    static void Main(string[] args) {
        using (var output = new StreamWriter(args[1])) {
            var run = new Reciprocal(int.Parse(args[2]), args[0], args.Skip(3).Select(int.Parse).ToArray(), output);
            if (run.prefix.Length > run.half || run.prefix.Where((v, i) => Math.Abs(v) > run.bounds[i+1]).Any())
                throw new ArgumentException("Prefix outside the trace intervals");
            run.Extend(1, false);
            Console.WriteLine(string.Join(" ", run.counts));
        }
    }
}
