using System;
using System.IO;
using System.Linq;

// Each process handles a disjoint pair (s1,s2). The two lists of suffixes
// contain at most 256 rows each and are reused for all seventeen-sum prefixes.
class Sieve66 {
    const int H = 33, D = 2*H, Start = H+1, Width = 9;
    const int PrefixEnd = 17, LowStart = PrefixEnd+1, HighStart = LowStart+8;
    readonly int[] bound, fixedSums, c = new int[D+1], s = new int[121];
    readonly int[] baseC = new int[D+1], baseS = new int[121], inverse = new int[Width];
    readonly int[] choices = new int[H+1];
    readonly int[][] shift = new int[H+1][];
    readonly long[][] caps;
    readonly int[] low = new int[256*Width], high = new int[256*Width];
    readonly int[] lowMask = new int[256], highMask = new int[256];
    readonly ulong[] a = new ulong[D+1], b = new ulong[D+1];
    readonly long[] counts = new long[8];
    readonly TextWriter remaining;
    readonly bool audit;

    Sieve66(string config, int[] fixedSums, TextWriter remaining, bool audit) {
        var rows = File.ReadAllLines(config);
        bound = rows[0].Split(' ').Select(int.Parse).ToArray();
        caps = rows.Skip(1).Select(line => line.Split(' ').Select(long.Parse).ToArray()).ToArray();
        this.fixedSums = fixedSums;
        this.remaining = remaining;
        this.audit = audit;
        c[0] = 1;
        for (int j = LowStart; j <= H; j++) shift[j] = new int[Width];
    }

    static int First(int sum, int k, int lo) {
        int offset = (-sum-lo)%k;
        return lo + (offset < 0 ? offset+k : offset);
    }

    void Prefix(int k, bool oriented) {
        int previous = 0;
        for (int i=1; i<k; i++) previous += c[i]*s[k-i];
        int lo = -bound[k], hi = bound[k];
        if (k <= fixedSums.Length) lo = hi = fixedSums[k-1];
        for (int val=First(previous,k,lo); val<=hi; val+=k) {
            if (!oriented && k%2==1 && val<0) continue;
            bool nextOriented = oriented || (k%2==1 && val>0);
            c[k] = -(previous+val)/k;
            s[k] = val;
            if (k<PrefixEnd) Prefix(k+1,nextOriented);
            else if (nextOriented && (s[1]!=0 || (!Substitution(3) && !Substitution(11)))) CompletePrefix();
        }
    }

    bool Substitution(int q) {
        for (int k=1; k<=PrefixEnd; k++)
            if (k%q!=0 && s[k]!=0) return false;
        return true;
    }

    static int Newton(int[] coeff, int[] sums, int k) {
        int total = k <= D ? k*coeff[k] : 0;
        for (int i=1; i<=Math.Min(D,k-1); i++) total += coeff[i]*sums[k-i];
        return -total;
    }

    void CompletePrefix() {
        Array.Copy(c,baseC,LowStart);
        Array.Copy(s,baseS,LowStart);
        for (int j=LowStart; j<=H; j++) {
            int previous = 0;
            for (int i=1; i<j; i++) previous += baseC[i]*baseS[j-i];
            int first = First(previous,j,-bound[j]);
            if (first > bound[j]) return;
            baseS[j] = first;
            baseC[j] = -(previous+first)/j;
            choices[j] = first+j <= bound[j] ? 2 : 1;
        }
        for (int i=H+1; i<=D; i++) baseC[i] = baseC[D-i];
        for (int k=Start; k<Start+Width; k++) baseS[k] = Newton(baseC,baseS,k);
        inverse[0] = 1;
        for (int i=1; i<Width; i++) {
            int sum = 0;
            for (int j=1; j<=i; j++) sum += c[j]*inverse[i-j];
            inverse[i] = -sum;
        }
        for (int j=LowStart; j<=H; j++) {
            if (choices[j]==1) continue;
            for (int k=Start; k<Start+Width; k++) {
                int v = 0;
                for (int t=Start; t<=k; t++) {
                    int reflected = D-t-j;
                    int difference = (reflected>=0 ? baseC[reflected] : 0) - baseC[t-j];
                    v += difference*inverse[k-t];
                }
                shift[j][k-Start] = k*v;
            }
        }
        int nl = Fill(LowStart,HighStart-1,low,lowMask), nh = Fill(HighStart,H,high,highMask);
        counts[0] += (long)nl*nh;
        for (int u=0; u<nl; u++) {
            int x = u*Width;
            int offset = baseS[Start]+low[x];
            for (int v=0; v<nh; v++) {
                int y = v*Width;
                int val = offset+high[y];
                if ((uint)(val+bound[Start]) > 2U*bound[Start]) continue;
                counts[1]++;
                int k = Start+1;
                for (; k<Start+Width; k++) {
                    int index = k-Start;
                    val = baseS[k]+low[x+index]+high[y+index];
                    if ((uint)(val+bound[k]) > 2U*bound[k]) break;
                }
                if (k==Start+Width) {
                    counts[2]++;
                    Check(lowMask[u]|highMask[v],x,y);
                }
            }
        }
    }

    int Fill(int first, int last, int[] list, int[] masks) {
        int size = 1;
        for (int j=first; j<=last; j++) {
            if (choices[j]==1) continue;
            for (int i=0; i<size; i++) {
                int old = i*Width, added = (size+i)*Width;
                for (int k=0; k<Width; k++) list[added+k] = list[old+k]+shift[j][k];
                // U^3 begins at degree 54. Both members of a quadratic
                // pair contributing through degree 42 are in the lower block.
                if (j<HighStart) {
                    if (2*j<Start+Width) list[added+2*j-Start] += j;
                    for (int p=LowStart; p<j && p+j<Start+Width; p++)
                        if ((masks[i] & (1<<(p-LowStart)))!=0) list[added+p+j-Start] += p+j;
                }
                masks[size+i] = masks[i] | (1<<(j-LowStart));
            }
            size *= 2;
        }
        return size;
    }

    void Check(int mask, int x, int y) {
        Array.Copy(baseC,c,H+1);
        Array.Copy(baseS,s,H+1);
        for (int j=LowStart; j<=H; j++) {
            if ((mask & (1<<(j-LowStart)))==0) continue;
            s[j] += j;
            for (int i=j; i<=H; i++) c[i] -= baseC[i-j];
        }
        for (int i=H+1; i<=D; i++) c[i]=c[D-i];
        for (int k=Start; k<Start+Width; k++) {
            s[k]=baseS[k]+low[x+k-Start]+high[y+k-Start];
            if (audit && Newton(c,s,k)!=s[k]) throw new ArithmeticException("Reflected sum mismatch");
        }
        int even=0, odd=c[H];
        for (int i=0; i<H; i+=2) even+=2*c[i];
        for (int i=1; i<H; i+=2) odd+=2*c[i];
        if (even==odd || even==-odd) { counts[3]++; return; }
        for (int k=Start+Width; k<bound.Length; k++) {
            long total = k<=D ? (long)k*c[k] : 0;
            for (int i=1; i<=Math.Min(D,k-1); i++) total += (long)c[i]*s[k-i];
            if (total>bound[k] || total< -bound[k]) { counts[4]++; return; }
            s[k]=(int)-total;
        }
        // Divisibility by Phi_3, Phi_4, Phi_6 is exact over the integers.
        for (int order=3; order<=6; order++) {
            if (order==5) continue;
            int real=0, imag=0;
            int linear=order==3 ? -1 : order==4 ? 0 : 1;
            for (int i=D; i>=0; i--) {
                int next = c[i]-imag;
                imag=real+linear*imag;
                real=next;
            }
            if (real==0 && imag==0) { counts[5]++; return; }
        }
        for (int i=0; i<=D; i++) a[i]=unchecked((ulong)c[i]);
        var from=a; var to=b;
        for (int g=1; g<=caps.Length; g++) {
            for (int i=0; i<=H; i++) {
                ulong z=0;
                for (int j=0; j<i; j+=2) z += from[j]*from[2*i-j];
                for (int j=1; j<i; j+=2) z -= from[j]*from[2*i-j];
                ulong middle=from[i]*from[i];
                ulong val=2*z + (i%2==0 ? middle : 0UL-middle);
                ulong mag=Math.Min(val,unchecked(0UL-val));
                if (caps[g-1][i]>=0 && mag>(ulong)caps[g-1][i]) { counts[6]++; return; }
                to[i]=to[D-i]=val;
            }
            var temp=to; to=from; from=temp;
        }
        counts[7]++;
        remaining.WriteLine(string.Join(" ",c.Take(H+1)));
    }

    static void Main(string[] args) {
        using (var output=new StreamWriter(args[1])) {
            var prefix=args.Skip(3).Select(int.Parse).ToArray();
            var sieve=new Sieve66(args[0],prefix,output,args[2]=="audit");
            sieve.Prefix(1,false);
            Console.WriteLine(string.Join(" ",sieve.counts));
        }
    }
}
