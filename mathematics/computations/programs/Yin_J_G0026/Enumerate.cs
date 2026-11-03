using System;
using System.IO;

public static class LehmerCompactG26
{
    static long[,] T, U, Elo, Ehi;
    static long[] abounds, bbounds, b, a;
    static long scale, stable, radius, nodeCap, candidateCap;
    static long nodes, leaves, candidates;
    static BinaryWriter output;
    static bool capped;

    static long FloorDiv(long n,long d) { long q=n/d; if(n%d<0) q--; return q; }
    static long CeilDiv(long n,long d) { return -FloorDiv(-n,d); }
    static long SqrtFloor(long n) {
        long r=(long)Math.Sqrt((double)n);
        while(checked((r+1)*(r+1))<=n)r++;
        while(checked(r*r)>n)r--;
        return r;
    }
    static void Evaluate(int row,out long low,out long high) {
        checked {
            low=0;high=0;
            for(int i=0;i<10;i++) {
                low+=a[i]*(a[i]>=0?Elo[row,i]:Ehi[row,i]);
                high+=a[i]*(a[i]>=0?Ehi[row,i]:Elo[row,i]);
            }
        }
    }
    static long MinSquare(long low,long high) {
        if(low<=0 && high>=0)return 0;
        return Math.Min(checked(low*low),checked(high*high));
    }
    static void Leaf() {
        checked {
            leaves++;
            for(int j=0;j<10;j++) {
                a[j]=0;
                for(int i=0;i<10;i++)a[j]+=b[i]*U[i,j];
                if(Math.Abs(a[j])>abounds[j])return;
            }
            long lo,hi;
            Evaluate(0,out lo,out hi);
            if(lo>scale || hi< -scale)return;
            Evaluate(1,out lo,out hi);
            if(lo>stable || hi< -stable)return;
            long neutral=0;
            for(int j=2;j<10;j++) {
                Evaluate(j,out lo,out hi);
                neutral+=MinSquare(lo,hi);
                if(neutral>=64*scale*scale)return;
            }
            if(candidates>=candidateCap) { capped=true;return; }
            ulong packed=0;
            for(int j=0;j<10;j++) {
                if(a[j]< -8 || a[j]>7)throw new InvalidOperationException("Packing outside four-bit domain");
                packed|=((ulong)(a[j]+8))<<(4*j);
            }
            output.Write(packed);candidates++;
        }
    }
    static void Visit(int j,long remaining) {
        if(capped)return;
        checked {
            nodes++;
            if(nodes>nodeCap) { capped=true;return; }
            if(j<0) { Leaf();return; }
            long center=0;
            for(int i=j+1;i<10;i++)center+=b[i]*T[i,j];
            long span=SqrtFloor(remaining),diagonal=T[j,j];
            long low=Math.Max(-bbounds[j],CeilDiv(-span-center,diagonal));
            long high=Math.Min(bbounds[j],FloorDiv(span-center,diagonal));
            for(long value=low;value<=high && !capped;value++) {
                b[j]=value;
                long term=value*diagonal+center;
                Visit(j-1,remaining-term*term);
            }
        }
    }
    public static string Run(long[,] triangle,long[,] transform,long[,] lower,long[,] upper,
        long[] originalBounds,long[] reducedBounds,long embeddingScale,long stableBound,long squaredRadius,
        long maxNodes,long maxCandidates,string path) {
        T=triangle;U=transform;Elo=lower;Ehi=upper;abounds=originalBounds;bbounds=reducedBounds;
        b=new long[10];a=new long[10];scale=embeddingScale;stable=stableBound;radius=squaredRadius;
        nodeCap=maxNodes;candidateCap=maxCandidates;nodes=leaves=candidates=0;capped=false;
        for(int i=0;i<10;i++)if(T[i,i]<=0)throw new InvalidOperationException("Nonpositive diagonal");
        using(output=new BinaryWriter(File.Open(path,FileMode.Create,FileAccess.Write)))Visit(9,radius);
        return "{\"completed\":"+(!capped?"true":"false")+",\"nodes\":"+nodes+
            ",\"ellipsoid_leaves\":"+leaves+",\"retained_candidates\":"+candidates+
            ",\"node_cap\":"+nodeCap+",\"candidate_cap\":"+candidateCap+"}";
    }
}
