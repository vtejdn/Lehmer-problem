using System;
using System.Text;

public static class SalemBicyclicSearch {
  const int N=7;
  static int[] ei,ej,chosen;
  static int[,] v;
  static long examined,connected,tracePassed,cap;
  static bool stopped,found;
  static long[] winning;
  static int[,] winner;
  static long[] target={1,0,-1,-1,-1,-1,0,1};
  static long[,] binom=new long[8,8];
  static int Root(int[] parent,int x) { while(parent[x]!=x)x=parent[x];return x; }
  static int Bits(int x) { int count=0;while(x!=0){x&=x-1;count++;}return count; }
  static long TraceCoefficient() {
    long[,] inverse=new long[N,N];
    for(int i=N-1;i>=0;i--){
      inverse[i,i]=1;
      for(int j=i+1;j<N;j++){
        long sum=0;
        for(int k=i+1;k<=j;k++)sum+=v[i,k]*inverse[k,j];
        inverse[i,j]=-sum;
      }
    }
    long trace=N;
    for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)trace+=inverse[i,j]*v[i,j];
    return trace;
  }
  static void Permutations(int row,int used,int ascents,int fixedCount,long weight,long[] coefficients) {
    if(row==N){
      for(int k=0;k<=fixedCount;k++)coefficients[ascents+k]+=weight*binom[fixedCount,k];
      return;
    }
    for(int col=0;col<N;col++){
      if((used&(1<<col))!=0)continue;
      int value=row==col?1:v[Math.Min(row,col),Math.Max(row,col)];
      if(value==0)continue;
      int inversions=Bits(used&(~((1<<(col+1))-1)));
      long next=weight*value*((inversions&1)==0?1:-1);
      Permutations(row+1,used|(1<<col),ascents+(row<col?1:0),fixedCount+(row==col?1:0),next,coefficients);
    }
  }
  static void TestSupport() {
    int[] parent=new int[N];for(int i=0;i<N;i++)parent[i]=i;
    int[] chords=new int[2];int chordCount=0,forestCount=0;
    v=new int[N,N];for(int i=0;i<N;i++)v[i,i]=1;
    foreach(int edge in chosen){
      int i=ei[edge],j=ej[edge],a=Root(parent,i),b=Root(parent,j);
      v[i,j]=-1;
      if(a!=b){parent[a]=b;forestCount++;}
      else {if(chordCount>=2)return;chords[chordCount++]=edge;}
    }
    if(forestCount!=6||chordCount!=2)return;
    connected++;
    for(int mask=0;mask<4;mask++){
      if(examined>=cap){stopped=true;return;}
      examined++;
      for(int k=0;k<2;k++)v[ei[chords[k]],ej[chords[k]]]=((mask>>k)&1)==0?-1:1;
      if(TraceCoefficient()!=0)continue;
      tracePassed++;
      long[] poly=new long[8];
      Permutations(0,0,0,0,1,poly);
      if(poly[6]!=0)throw new Exception("Trace/determinant coefficient disagreement");
      bool equal=true;for(int i=0;i<8;i++)if(poly[i]!=target[i])equal=false;
      if(equal){found=true;stopped=true;winning=poly;winner=(int[,])v.Clone();return;}
    }
  }
  static void Supports(int depth,int start){
    if(stopped)return;
    if(depth==8){TestSupport();return;}
    for(int e=start;e<=21-(8-depth);e++){chosen[depth]=e;Supports(depth+1,e+1);if(stopped)return;}
  }
  public static string Run(long matrixCap){
    cap=matrixCap;examined=connected=tracePassed=0;stopped=found=false;
    chosen=new int[8];ei=new int[21];ej=new int[21];int index=0;
    for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){ei[index]=i;ej[index++]=j;}
    for(int n=0;n<=7;n++){binom[n,0]=binom[n,n]=1;for(int k=1;k<n;k++)binom[n,k]=binom[n-1,k-1]+binom[n-1,k];}
    Supports(0,0);
    StringBuilder output=new StringBuilder();
    output.Append("{\"scope\":\"connected labeled rank7 unit-entry supports with8edges; negative lexicographic spanning forest\",");
    output.Append("\"matrix_cap\":"+cap+",\"signed_matrices_examined\":"+examined+",\"connected_supports_started\":"+connected+",\"trace_filter_passes\":"+tracePassed+",");
    output.Append("\"found\":"+(found?"true":"false")+",\"cap_reached\":"+(!found&&examined>=cap?"true":"false"));
    if(found){
      output.Append(",\"matrix\":[");for(int i=0;i<N;i++){if(i>0)output.Append(',');output.Append('[');for(int j=0;j<N;j++){if(j>0)output.Append(',');output.Append(winner[i,j]);}output.Append(']');}output.Append(']');
      output.Append(",\"coefficients_ascending\":["+String.Join(",",winning)+"]");
    }
    output.Append('}');return output.ToString();
  }
}
