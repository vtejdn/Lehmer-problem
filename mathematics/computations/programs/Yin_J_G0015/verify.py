"""Independent integer-only witness verification; no optimizer/helper imports."""
from __future__ import annotations
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)


def times_alpha(v, p):
    out=[0]+v[:-1]
    for j in range(len(v)):
        out[j]-=v[-1]*p[j]
    return out


def determinant(a):
    a=[row[:] for row in a]
    n=len(a)
    previous=1
    sign=1
    for k in range(n-1):
        if not a[k][k]:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:
                return 0
            a[k],a[j]=a[j],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value%previous==0
                a[i][j]=value//previous
        for i in range(k+1,n):
            a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]


def norm(v,p):
    columns=[v]
    for _ in range(len(v)-1):
        columns.append(times_alpha(columns[-1],p))
    return determinant([list(r) for r in zip(*columns)])


def check(row):
    p=row['p_ascending']
    q=row['q_ascending']
    a=row['product_ascending']
    assert p[-1]==1
    assert all(type(x) is int for x in p+q+a)
    assert max(map(abs,a))<=1
    remainder=a[:]
    recovered=[0]*len(q)
    for k in range(len(q)-1,-1,-1):
        recovered[k]=remainder[k+len(p)-1]
        for j in range(len(p)):
            remainder[k+j]-=recovered[k]*p[j]
    assert not any(remainder)
    assert recovered==q
    assert max(map(abs,q))==row['quotient_height']
    state=[0]*(len(p)-1)
    returns=[]
    largest=0
    witness=None
    for i,digit in enumerate(reversed(a),1):
        state=times_alpha(state,p)
        state[0]+=digit
        if not any(state):
            returns.append(i)
        else:
            z=abs(norm(state,p))
            assert z>0
            if z>largest:
                largest=z
                witness={'cut_length':i,'state_ascending':state[:]}
    assert not any(state)
    return {'name':row['name'],'quotient_length':len(q),
        'quotient_height':max(map(abs,q)),'word_length':len(a),
        'nonzero_digits':sum(x!=0 for x in a),'return_times':returns,
        'max_absolute_state_norm':largest,'norm_witness':witness,
        'polynomial_division_and_horner_return':True}


def main():
    base= _J_OUTPUT
    out={'scope':'exact integer witnesses only; no optimality or unboundedness claim','inputs':{}}
    for filename in ['pilot.json','lehmer-long.json']:
        payload=json.loads((base/filename).read_text(encoding='utf-8'))
        rows=[check(r) for r in payload['cases'] if 'q_ascending' in r]
        out['inputs'][filename]=rows
        print(filename,[(r['name'],r['quotient_length'],r['quotient_height'],r['max_absolute_state_norm']) for r in rows])
    (base/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':
    main()
