"""Exact finite local interval extraction; no graph-path or word-length search."""
from fractions import Fraction as F
from functools import cmp_to_key
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
OUT = REPO / 'mathematics' / 'computations' / 'outputs' / HERE.name
ZERO = (F(0),)*4
ONE = (F(1),F(0),F(0),F(0))
BETA = (F(0),F(1),F(0),F(0))


def scalar(x):
    return (F(x),F(0),F(0),F(0))


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def neg(a):
    return tuple(-x for x in a)


def sub(a,b):
    return add(a,neg(b))


def mul(a,b):
    r=[F(0)]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            r[i+j]+=x*y
    for k in range(6,3,-1):
        q=r[k]
        for j,p in enumerate((1,-1,-1,-1)):
            r[k-4+j]-=q*p
    return tuple(r[:4])


def inv(a):
    columns=[mul(a,tuple(F(i==j) for i in range(4))) for j in range(4)]
    mat=[[columns[j][i] for j in range(4)]+[F(i==0)] for i in range(4)]
    for j in range(4):
        pivot=next(i for i in range(j,4) if mat[i][j])
        mat[j],mat[pivot]=mat[pivot],mat[j]
        q=mat[j][j];mat[j]=[x/q for x in mat[j]]
        for i in range(4):
            if i!=j:
                q=mat[i][j]
                mat[i]=[x-q*y for x,y in zip(mat[i],mat[j])]
    result=tuple(mat[i][4] for i in range(4))
    assert mul(a,result)==ONE
    return result


def scale(a,n):
    return tuple(x*n for x in a)


def poly_at(a,x):
    out=ZERO
    for d in reversed(a):
        out=add(mul(out,x),scalar(d))
    return out


def interval_mul(a,b):
    values=[x*y for x in a for y in b]
    return min(values),max(values)


def evaluate(a,bracket):
    r=(F(0),F(0))
    for d in reversed(a):
        r=interval_mul(r,bracket)
        r=(r[0]+d,r[1]+d)
    return r


def encoded(a):
    return [[x.numerator,x.denominator] for x in a]


def main():
    inp=json.loads((HERE/'inputs.json').read_text(encoding='utf-8'))
    assert inp['polynomial_ascending']==[1,-1,-1,-1,1]
    assert inp['source_columns']==[-1,0,1]
    root=json.loads((REPO/inp['root_input']).read_text(encoding='utf-8'))
    old=json.loads((REPO/inp['pair_input']).read_text(encoding='utf-8'))
    assert root['polynomial_ascending']==inp['polynomial_ascending']
    bracket=(F(*root['beta_lower']),F(*root['beta_upper']))
    words=old['pattern_words'];pairs=old['pairs']
    assert len(words)==81 and len(set(map(tuple,words)))==81
    assert all(len(w)==4 and set(w)<={-1,0,1} for w in words)
    assert len(pairs)==81**2
    assert {(p['u_index'],p['v_index']) for p in pairs}=={(i,j) for i in range(81) for j in range(81)}
    assert old['count']=={'YCY':183,'CYC':183,'YCY_lambda_change':36,'CYC_lambda_change':36}
    beta_inv=inv(BETA);bm1=sub(BETA,ONE)
    t=add(BETA,beta_inv)
    h=inv(mul(BETA,mul(bm1,bm1)))
    I={0:(neg(h),h),1:(neg(add(h,beta_inv)),sub(h,BETA)),
       -1:(sub(BETA,h),add(h,beta_inv))}

    def compare(a,b):
        delta=sub(a,b)
        if delta==ZERO:
            return 0
        lo,hi=evaluate(delta,bracket)
        assert hi<0 or lo>0, ('unresolved sign',delta,lo,hi)
        return -1 if hi<0 else 1

    def interval_record(interval):
        return {'lower':encoded(interval[0]),'upper':encoded(interval[1]),
                'lower_enclosure':encoded(evaluate(interval[0],bracket)),
                'upper_enclosure':encoded(evaluate(interval[1],bracket))}

    attempts=[];groups={};counts={}
    for order in ('YCY','CYC'):
        selected=[p for p in pairs if p[order] and p[order+'_lambda_change']==0]
        assert len(selected)==inp['expected_lambda_zero_pairs_per_order']
        counts[order]={'pairs':len(selected),'attempts':0,'nonempty':0}
        for pair in selected:
            ui,vi=pair['u_index'],pair['v_index']
            u,v=words[ui],words[vi]
            assert sum(u)==sum(v)
            theta=tuple(v[j]-u[j] if order=='YCY' else u[j]-v[j] for j in range(4))
            A=-theta[0];C=theta[3];B=A-theta[1]
            assert theta==(-A,A-B,B-C,C)
            dm=A-C;dx=add(scalar(B),scale(t,C))
            for m in inp['source_columns']:
                counts[order]['attempts']+=1
                rec={'order':order,'u_index':ui,'v_index':vi,'from_m':m,
                     'to_m':m+dm,'dx_integer':B,'dx_t':C}
                if m+dm not in I:
                    rec['result']='target-column-absent';attempts.append(rec);continue
                if order=='CYC':
                    center=neg(add(scale(beta_inv,m),mul(tuple(map(F,u)),inv(mul(BETA,bm1)))))
                else:
                    center=neg(add(scale(BETA,m),mul(mul(BETA,BETA),mul(poly_at(u,beta_inv),inv(bm1)))))
                intervals=(I[m],tuple(sub(z,dx) for z in I[m+dm]),(sub(center,h),add(center,h)))
                lower=max((p[0] for p in intervals),key=cmp_to_key(compare))
                upper=min((p[1] for p in intervals),key=cmp_to_key(compare))
                rec['intersection']=interval_record((lower,upper))
                if compare(lower,upper)>=0:
                    rec['result']='empty';attempts.append(rec);continue
                rec['result']='nonempty';attempts.append(rec);counts[order]['nonempty']+=1
                key=(m,m+dm,B,C)
                groups.setdefault(key,[]).append((lower,upper,len(attempts)-1))
    merged=[]
    for key,segments in sorted(groups.items()):
        segments.sort(key=cmp_to_key(lambda a,b:compare(a[0],b[0]) or compare(a[1],b[1])))
        pieces=[]
        for lo,hi,idx in segments:
            if pieces and compare(lo,pieces[-1][1])<0:
                pieces[-1][1]=max(pieces[-1][1],hi,key=cmp_to_key(compare))
                pieces[-1][2].append(idx)
            else:
                pieces.append([lo,hi,[idx]])
        dx=add(scalar(key[2]),scale(t,key[3]))
        endpoint_domain=(max(I[key[0]][0],sub(I[key[1]][0],dx),key=cmp_to_key(compare)),
                         min(I[key[0]][1],sub(I[key[1]][1],dx),key=cmp_to_key(compare)))
        assert len(pieces)==1 and tuple(pieces[0][:2])==endpoint_domain
        merged.append({'from_m':key[0],'to_m':key[1],'dx_integer':key[2],'dx_t':key[3],
                       'equals_full_endpoint_overlap':True,
                       'domains':[dict(interval_record((lo,hi)),attempt_indices=ids) for lo,hi,ids in pieces]})
    chosen=[]
    for u,v,dx in (((0,1,-1,0),(1,-1,0,0),(-1,0)),
                   ((1,0,1,-1),(1,1,-1,0),(1,-1))):
        matching=[(idx,a) for idx,a in enumerate(attempts) if a['order']=='CYC'
                  and a['from_m']==-1 and a['to_m']==0
                  and words[a['u_index']]==list(u) and words[a['v_index']]==list(v)]
        assert len(matching)==1
        idx,a=matching[0]
        assert a['result']=='nonempty' and (a['dx_integer'],a['dx_t'])==dx
        assert a['intersection']['lower']==encoded(I[-1][0])
        assert a['intersection']['upper']==encoded(I[-1][1])
        chosen.append({'attempt_index':idx,'u':u,'v':v,'covers_entire_outer_column':True})
    payload={'input_scope':inp,'counts':counts,'columns':{str(m):interval_record(v) for m,v in I.items()},
             'attempts':attempts,'merged_domains':merged,'selected_full_outer_bridges':chosen}
    output=json.dumps(payload,indent=2)+'\n'
    assert len(output.encode('utf-8'))<=inp['output_limit_bytes']
    OUT.mkdir(parents=True,exist_ok=True)
    pending=OUT/'domains.partial.json'
    pending.write_text(output,encoding='utf-8')
    pending.replace(OUT/'domains.json')
    print(json.dumps({'counts':counts,'transition_types':len(merged),'open_pieces':sum(len(r['domains']) for r in merged)}))
    for row in merged:
        pieces=[]
        for d in row['domains']:
            lo=tuple(F(*q) for q in d['lower']);hi=tuple(F(*q) for q in d['upper'])
            pieces.append((float(sum(evaluate(lo,bracket))/2),float(sum(evaluate(hi,bracket))/2)))
        print(row['from_m'],row['to_m'],row['dx_integer'],row['dx_t'],pieces)


if __name__=='__main__':
    main()
