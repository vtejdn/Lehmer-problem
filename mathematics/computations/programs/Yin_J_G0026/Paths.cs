using System;
using System.IO;
using System.Collections.Generic;

public static class LehmerPathsG26
{
    static readonly int[] polynomial={1,1,0,-1,-1,-1,-1,-1,0,1,1};
    static ulong Pack(int[] a) {
        ulong key=0;
        for(int j=0;j<10;j++) {
            if(a[j]<-16 || a[j]>15)return ulong.MaxValue;
            key|=((ulong)(a[j]+16))<<(5*j);
        }
        return key;
    }
    static void Unpack(ulong key,int[] a) { for(int j=0;j<10;j++)a[j]=(int)((key>>(5*j))&31)-16; }
    static bool Retain(int[] a,double[,] M,double plus,double minus,double radius) {
        double s=0;
        for(int i=0;i<10;i++)s+=a[i]*M[0,i];
        if(Math.Abs(s)>plus+1e-7)return false;
        s=0;
        for(int i=0;i<10;i++)s+=a[i]*M[1,i];
        if(Math.Abs(s)>minus+1e-7)return false;
        double norm=0;
        for(int j=2;j<10;j++) {
            s=0;for(int i=0;i<10;i++)s+=a[i]*M[j,i];norm+=s*s;
        }
        return norm<=radius*radius+1e-7;
    }
    public static string Run(double[,] M,double plus,double minus,double radius,int cap,string input,string outputDir) {
        var targets=new HashSet<ulong>();int[] a=new int[10],pre=new int[10];
        using(var reader=new BinaryReader(File.OpenRead(input))) {
            while(reader.BaseStream.Position<reader.BaseStream.Length) {
                ulong old=reader.ReadUInt64();for(int i=0;i<10;i++)a[i]=(int)((old>>(4*i))&15)-8;
                targets.Add(Pack(a));
            }
        }
        int targetCount=targets.Count;
        var remaining=new HashSet<ulong>(targets);
        var index=new Dictionary<ulong,int>(Math.Min(cap,1000000));
        ulong[] keys=new ulong[cap];int[] parents=new int[cap];byte[] digits=new byte[cap];
        ulong zero=0;for(int i=0;i<10;i++)zero|=16UL<<(5*i);
        keys[0]=zero;parents[0]=0;digits[0]=1;index.Add(zero,0);remaining.Remove(zero);
        int count=1,head=0;bool capped=false;int packedRejects=0;
        while(head<count && remaining.Count>0 && !capped) {
            Unpack(keys[head],a);
            for(int digit=-1;digit<=1;digit++) {
                int first=a[0]-digit;
                for(int i=0;i<9;i++)pre[i]=a[i+1]-first*polynomial[i+1];
                pre[9]=-first;
                ulong key=Pack(pre);
                if(key==ulong.MaxValue) { packedRejects++;continue; }
                if(index.ContainsKey(key) || !Retain(pre,M,plus,minus,radius))continue;
                if(count>=cap) { capped=true;break; }
                keys[count]=key;parents[count]=head;digits[count]=(byte)(digit+1);
                index.Add(key,count);remaining.Remove(key);count++;
            }
            head++;
        }
        // Retain only ancestral chains needed by covered compact targets.
        bool[] needed=new bool[count];needed[0]=true;
        foreach(ulong target in targets) {
            int current;if(!index.TryGetValue(target,out current))continue;
            while(!needed[current]) { needed[current]=true;current=parents[current]; }
        }
        int[] map=new int[count];int kept=0,maxDepth=0;int[] depth=new int[count];
        for(int i=0;i<count;i++)if(needed[i]) { map[i]=kept++;depth[i]=i==0?0:depth[parents[i]]+1;maxDepth=Math.Max(maxDepth,depth[i]); }
        int part=0,written=0;BinaryWriter writer=null;
        try {
            for(int i=0;i<count;i++)if(needed[i]) {
                if(written%1000000==0) {
                    if(writer!=null)writer.Dispose();
                    writer=new BinaryWriter(File.Open(Path.Combine(outputDir,"path-nodes-"+part.ToString("D3")+".bin"),FileMode.Create));part++;
                }
                writer.Write(keys[i]);writer.Write(map[parents[i]]);writer.Write(digits[i]);written++;
            }
        } finally { if(writer!=null)writer.Dispose(); }
        using(var writerMissing=new BinaryWriter(File.Open(Path.Combine(outputDir,"uncovered.bin"),FileMode.Create)))
            foreach(ulong key in remaining)writerMissing.Write(key);
        return "{\"radius\":"+radius.ToString(System.Globalization.CultureInfo.InvariantCulture)+
            ",\"target_count\":"+targetCount+",\"covered_targets\":"+(targetCount-remaining.Count)+
            ",\"uncovered_targets\":"+remaining.Count+",\"visited_nodes\":"+count+
            ",\"processed_nodes\":"+head+",\"node_cap\":"+cap+",\"capped\":"+(capped?"true":"false")+
            ",\"packing_rejections\":"+packedRejects+",\"retained_path_nodes\":"+kept+
            ",\"retained_parts\":"+part+",\"max_retained_path_length\":"+maxDepth+"}";
    }
}
