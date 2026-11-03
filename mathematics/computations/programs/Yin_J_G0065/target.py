"""Every proper rank-six coefficient lift to the target modulo four.

All 4^15 residue matrices are represented exactly by binary bases and the
integer-polynomial first-order expansion at step two. No basis congruence
or lattice-type hypothesis is imposed.
"""
import importlib.util,json,time
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

HERE=(_J_PROGRAM / 'target.py').parent
spec=importlib.util.spec_from_file_location('j63_binary',(_J_ROOT / 'mathematics/computations/programs/Yin_J_G0063/classify.py'))
binary=importlib.util.module_from_spec(spec);spec.loader.exec_module(binary)
UP=binary.UP
TARGET=(-2,1,-1)

def coefficients(u):
    inv=[[int(i==j) for j in range(6)] for i in range(6)]
    for i in range(5,-1,-1):
        for j in range(i+1,6):inv[i][j]=-sum(u[i][k]*inv[k][j] for k in range(i+1,j+1))
    c=[[-sum(inv[i][k]*u[j][k] for k in range(6)) for j in range(6)] for i in range(6)]
    s1=sum(c[i][i] for i in range(6))
    s2=sum(c[i][j]*c[j][i] for i in range(6) for j in range(6))
    s3=sum(c[i][j]*c[j][k]*c[k][i] for i in range(6) for j in range(6) for k in range(6))
    assert (s1*s1-s2)%2==0 and (s1**3-3*s1*s2+2*s3)%6==0
    return [-s1,(s1*s1-s2)//2,-(s1**3-3*s1*s2+2*s3)//6]

def run():
    start=time.monotonic()
    result={'scope':{'binary_forms':32768,'lift_bits_per_form':15,'all_residue_matrices':4**15,
                     'modulus':4,'target_coefficients':list(TARGET),
                     'bilinear_congruence_restriction':False},
            'counts':{'binary_forms':0,'annihilator_forms':0,'target_parity_forms':0,
                      'compatible_forms':0,'incompatible_forms':0},'forms':[],'complete':False}
    counts=result['counts']
    try:
        for mask in range(32768):
            if mask%32==0 and time.monotonic()-start>120:raise TimeoutError('Declared120-secondcap')
            rows=binary.IDENT[:]
            for k,(i,j) in enumerate(UP):rows[i] |= ((mask>>k)&1)<<j
            counts['binary_forms']+=1
            cu=binary.mm(binary.inv(rows),binary.transpose(rows))
            if not binary.annihilates(cu):continue
            counts['annihilator_forms']+=1
            u=[[(row>>j)&1 for j in range(6)] for row in rows]
            f=coefficients(u)
            if any((a-b)%2 for a,b in zip(f,TARGET)):continue
            counts['target_parity_forms']+=1
            columns=[]
            for i,j in UP:
                u[i][j]+=2;g=coefficients(u);u[i][j]-=2
                assert all((a-b)%2==0 for a,b in zip(g,f))
                columns.append(sum((((a-b)//2)%2)<<k for k,(a,b) in enumerate(zip(g,f))))
            image={0:0}
            for j,column in enumerate(columns):
                for old,preimage in list(image.items()):image.setdefault(old^column,preimage^(1<<j))
            rhs=sum((((a-b)//2)%2)<<k for k,(a,b) in enumerate(zip(TARGET,f)))
            record={'upper_mask':mask,'upper_rows':rows,'integer_coefficients':f,
                    'derivative_columns':columns,'image_vectors':sorted(image),'right_side':rhs}
            if rhs in image:
                counts['compatible_forms']+=1
                correction=image[rhs];record['correction_bits']=correction
                lifted=[row[:] for row in u]
                for k,(i,j) in enumerate(UP):lifted[i][j]+=2*((correction>>k)&1)
                assert all((a-b)%4==0 for a,b in zip(coefficients(lifted),TARGET))
                record['lifted_matrix']=lifted;record['lifted_full_coefficients']=coefficients(lifted)
            else:
                counts['incompatible_forms']+=1
                z=next(z for z in range(1,8)
                       if all((z&c).bit_count()%2==0 for c in columns) and (z&rhs).bit_count()%2==1)
                record['inconsistency_witness']=z
            result['forms'].append(record)
        if time.monotonic()-start>120:raise TimeoutError('Declared120-secondcap')
        result['complete']=True
    except TimeoutError as exc:result['cap_failure']=str(exc)
    pass
    return result

if __name__=='__main__':
    data=run();((_J_OUTPUT / 'target_result.json')).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in data.items() if k!='forms'},indent=2))
