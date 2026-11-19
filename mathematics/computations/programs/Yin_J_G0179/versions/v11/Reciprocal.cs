using System;
using System.IO;
using System.Linq;

// Direct half-polynomial enumeration. The three cyclotomic
// remainders and modular Graeffe recurrences follow the degree-56–62 worker.
class Reciprocal {
    const int Last = 120;
    readonly int D, H;
    readonly int[] bounds, prefix, coeff, oddPrimes, sums = new int[Last + 1];
    readonly long[][] caps;
    readonly ulong[] left, right;
    readonly long[] counts = new long[8];
    readonly TextWriter survivors;

    Reciprocal(int degree, string path, int[] prefix, TextWriter survivors) {
        D = degree;
        H = D / 2;
        coeff = new int[D + 1];
        left = new ulong[D + 1];
        right = new ulong[D + 1];
        oddPrimes = Enumerable.Range(3, D - 2).Where(q => q % 2 == 1 && D % q == 0
            && !Enumerable.Range(2, (int)Math.Sqrt(q) - 1).Any(p => q % p == 0)).ToArray();
        var rows = File.ReadAllLines(path);
        bounds = rows[0].Split(' ').Select(int.Parse).ToArray();
        caps = rows.Skip(1).Select(row => row.Split(' ').Select(long.Parse).ToArray()).ToArray();
        this.prefix = prefix;
        this.survivors = survivors;
        coeff[0] = 1;
    }

    void Extend(int k, bool oriented) {
        long sum = 0;
        for (int i = 1; i < k; ++i) sum += (long)coeff[i] * sums[k - i];
        int low = -bounds[k], high = bounds[k];
        if (k <= prefix.Length) low = high = prefix[k - 1];
        int offset = (int)((-sum - low) % k);
        int first = low + (offset < 0 ? offset + k : offset);
        for (int value = first; value <= high; value += k) {
            if (!oriented && k % 2 == 1 && value < 0) continue;
            bool nextOriented = oriented || (k % 2 == 1 && value > 0);
            sums[k] = value;
            coeff[k] = checked((int)(-(sum + value) / k));
            if (k < H) Extend(k + 1, nextOriented);
            else if (nextOriented && (sums[1] != 0 || !oddPrimes.Any(PowerSubstitution))) Check();
        }
    }

    bool PowerSubstitution(int q) {
        for (int i = 1; i <= H; ++i)
            if (i % q != 0 && coeff[i] != 0) return false;
        return true;
    }

    void Check() {
        ++counts[0];
        for (int i = H + 1; i <= D; ++i) coeff[i] = coeff[D - i];
        for (int k = H + 1; k <= Last; ++k) {
            if (k == H + 10) {
                long even = 0, odd = 0;
                for (int i = 0; i <= D; i += 2) even += coeff[i];
                for (int i = 1; i <= D; i += 2) odd += coeff[i];
                if (even == odd || even == -odd) { ++counts[3]; return; }
            }
            long total = k <= D ? (long)k * coeff[k] : 0;
            for (int i = 1; i < k && i <= D; ++i) total += (long)coeff[i] * sums[k - i];
            if (total < -bounds[k] || total > bounds[k]) {
                if (k >= H + 10) ++counts[4];
                return;
            }
            sums[k] = (int)-total;
            if (k == H + 1) ++counts[1];
            if (k == H + 9) ++counts[2];
        }
        foreach (int linear in new int[] {-1, 0, 1}) {
            long real = 0, imag = 0;
            for (int i = D; i >= 0; --i) {
                long next = coeff[i] - imag;
                imag = real + linear * imag;
                real = next;
            }
            if (real == 0 && imag == 0) { ++counts[5]; return; }
        }
        for (int i = 0; i <= D; ++i) left[i] = unchecked((ulong)coeff[i]);
        var from = left;
        var to = right;
        foreach (long[] cap in caps) {
            for (int i = 0; i <= H; ++i) {
                ulong z = 0;
                for (int j = 0; j < i; j += 2) z += from[j] * from[2 * i - j];
                for (int j = 1; j < i; j += 2) z -= from[j] * from[2 * i - j];
                ulong middle = from[i] * from[i];
                ulong val = 2 * z + (i % 2 == 0 ? middle : 0UL - middle);
                if (cap[i] >= 0 && Math.Min(val, unchecked(0UL - val)) > (ulong)cap[i]) {
                    ++counts[6];
                    return;
                }
                to[i] = to[D - i] = val;
            }
            var temp = from;
            from = to;
            to = temp;
        }
        ++counts[7];
        survivors.WriteLine(string.Join(" ", coeff.Take(H + 1)));
    }

    static void Main(string[] args) {
        using (var output = new StreamWriter(args[1])) {
            var run = new Reciprocal(int.Parse(args[2]), args[0], args.Skip(3).Select(int.Parse).ToArray(), output);
            if (run.prefix.Length > run.H || run.prefix.Where((v, i) => Math.Abs(v) > run.bounds[i + 1]).Any())
                throw new ArgumentException("Prefix outside the Newton box");
            run.Extend(1, false);
            Console.WriteLine(string.Join(" ", run.counts));
        }
    }
}
