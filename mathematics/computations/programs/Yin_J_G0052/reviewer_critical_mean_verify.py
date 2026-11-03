"""Independent C843 finite arithmetic; no new graph, no author imports.

The complete0..512 W/V input is reused at accepted C836/R1196 scope and every
entry is compared with that prior independent native result.  All renewals are
also rechecked.  New finite polynomials use ascending common-denominator integer
sums rather than author Horner evaluation.  Every exact arithmetic payload and
displayed difference in CM1--CM12 is checked.  The conditional-probability,
extended-mean and adopted-interface proof is reviewed separately in R.
All declared input files are capped at16MiB and JSON integer strings at20000
digits.  Success publishes atomically; failure has a separate incomplete output.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'repository/config.json').is_file())
OUTPUT = ROOT/'mathematics/computations/outputs'/HERE.name
LAST, CAP = 512, 16*1024**2
T, X = Q(68883,40000), Q(172208381,100000000)
DELTA = Q(2894667437079809876755951,302231454903657293676544000)
P512_NUM = 5298548391970129745344684892772394289057669827956111368871272718708030755799876567240009996275901111428878134985202079634126536883620984644784010837788567749143910392852997044503323399


def need(ok, message):
    if not ok:
        raise ValueError(message)


def fraction_record(value):
    return {'numerator':value.numerator,'denominator':value.denominator}


def load_bounded(path):
    need(path.stat().st_size<=CAP,'16MiB input cap: '+str(path))
    return json.loads(path.read_text(encoding='utf8'))


def finite_polynomials(coefficients, point):
    a,b = (point/4).as_integer_ratio()
    denominator = b**LAST
    remaining, power, total, moment = denominator,1,0,0
    for n in range(1,LAST+1):
        power *= a
        remaining //= b
        term = coefficients[n]*power*remaining
        total += term
        moment += n*term
    need(remaining==1,'Incomplete common-denominator evaluation')
    return Q(total,denominator),Q(moment,denominator)


def partial_log(eta, count):
    return sum((eta**j/Q(j) for j in range(1,count+1)),Q(0))


def atomic(path, value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temp = path.with_suffix(path.suffix+'.partial')
    temp.write_text(json.dumps(value,separators=(',',':'))+'\n',encoding='utf8')
    temp.replace(path)


def verify(args):
    source = load_bounded(args.input)
    prior = load_bounded(args.independent_prefix)
    need(source['status']=='complete' and prior['status']=='complete','Incomplete prefix input')
    required_scope = {'polynomial_coefficients_ascending':[1,-1,-1,-1,1],
        'digit_integer_weights':{'-1':1,'0':2,'1':1},'digit_denominator':4,
        'complete_return_times_including_zero':[0,LAST]}
    for key,value in required_scope.items():
        need(source['scope'][key]==value,'Wrong input scope '+key)
    need(prior['scope']['times_including_zero']==[0,LAST] and prior['scope']['digit_weights']==[1,2,1]
         and prior['scope']['digit_denominator']==4,'Wrong prior independent scope')
    W,V = (source[key] for key in ('complete_return_integer_weights','complete_first_return_integer_weights'))
    for key,values in [('complete_return_integer_weights',W),('complete_first_return_integer_weights',V)]:
        need(len(values)==513 and all(type(v) is int and v>=0 for v in values),'Invalid integer array '+key)
        need(values==prior[key],'Full accepted independent prefix mismatch '+key)
    need((W[0],V[0],W[1],V[1])==(1,0,2,2),'Wrong zero/one conventions')
    need(Q(W[512],4**512)==Q(P512_NUM,2**1019),'Adopted p512 mismatch')
    # Reconstruct every return from the nonnegative first-return coefficients.
    reconstructed = [1]
    for n in range(1,LAST+1):
        reconstructed.append(sum(V[j]*reconstructed[n-j] for j in range(1,n+1)))
        need(reconstructed[n]==W[n],'Renewal mismatch at '+str(n))
    del source,prior,reconstructed
    print('PASS: all513 W/V entries equal prior independent result; all512 renewals.',flush=True)

    polynomial = X**4-X**3-X**2-X+1
    need(polynomial==Q(3019729242318357479427921,10**32)>0,'Root certificate')
    need(1<T<X<2 and 0<DELTA<1,'Constants outside stated domains')
    epsilon, factor, fbar = 1-T/X,T/(X-T),1-DELTA
    need(epsilon==Q(881,172208381) and factor==Q(172207500,881),'Uniform interval constants')
    b1,a1 = 1-X/2,fbar-T/2
    need(0<a1<b1,'One-step conditional domain')
    eta1 = 1-a1/b1
    eta1floor = Q(6889,100000)
    eta1difference = eta1-eta1floor
    need(eta1difference==Q(416129438737099465895786109,136710635489878340046055014400000)>0,'CM1 eta difference')
    mean1 = T/2+b1*factor*partial_log(eta1floor,3)
    need(mean1-1939==Q(32189338518106811520971,70480000000000000000000)>0,'CM1 mean difference')
    need(10000*epsilon<1,'CM1 tail denominator')
    tail1 = b1-a1/(1-10000*epsilon)
    need(tail1-Q(1,400)==Q(4998293842243355529465352205232773,51441802519304284130821695078400000000)>0,'CM1 tail difference')

    ft,mt = finite_polynomials(V,T)
    fx,_ = finite_polynomials(V,X)
    b,a = 1-fx,fbar-ft
    eta = 1-a/b
    mf,bf,ef,ac = Q(2829,500),Q(45951,1000000),Q(1039,5000),Q(36403,1000000)
    need(0<a<b<1 and mt>mf and b>bf and eta>ef and a<ac,'CM7 complete-prefix inequalities')
    mean = mf+bf*factor*partial_log(ef,4)
    need(mean==Q(1847532308737880088962253,881000000000000000000),'CM8 exact expression')
    need(mean-2097==Q(75308737880088962253,881000000000000000000)>0,'CM8 mean difference')
    need(30000*epsilon<1,'CM9 tail denominator')
    tail = bf-ac/(1-30000*epsilon)
    need(tail-Q(1,350)==Q(3312757947,36444595250000)>0,'CM9 tail difference')
    # Expanded B and c expressions independently match the C828 coefficients.
    bT = T/2-3+4/T
    cT = 3*T/2+12/T-8
    need(cT==1+3*bT and bT>0 and X*X<8 and X<Q(12,5),'CM10 coefficient/monotonicity domain')
    kX = (X**5-8*X**4+16*X**3)/128
    derivative = (2097-cT)/kX
    phase = Q(2096)/bT-2
    zero_level = (T+8/T-5)/2097
    need(derivative>10121 and phase>11400 and 0<zero_level<Q(1,1500),'CM10/CM11 thresholds')
    mixed = DELTA*(1+T/(X-T))
    need(mixed-1872==Q(36206039264900899197839617331,266265911770122075729035264000)>0,'CM12 mixed norm difference')

    r = fraction_record
    calculated = {'status':'complete',
        'scope':{'input':'return_midpoint_512.json','prefix_times':[0,LAST],
            'source_input_byte_cap':CAP,'polynomial_coefficients_ascending':[1,-1,-1,-1,1],
            'digit_integer_weights':{'-1':1,'0':2,'1':1},'digit_denominator':4,
            'new_graph_or_return_times':False,'arithmetic':'exact integers and rational numbers'},
        'constants':{'t0':r(T),'x':r(X),'delta0':r(DELTA)},
        'root_upper_polynomial_value':r(polynomial),
        'input_checks':{'return_entries':513,'first_return_entries':513,
            'all_512_renewal_equalities':True,'p512_control':True},
        'one_step':{'eta':r(eta1),'eta_floor':r(eta1floor),'mean_floor':r(mean1),
            'mean_floor_exceeds_1939':True,'tail10000_floor':r(tail1),
            'tail_floor_exceeds_1_over_400':True,'mixed_critical_norm_floor':r(mixed),
            'mixed_norm_floor_exceeds_1872':True},
        'prefix512':{'F_t0':r(ft),'F_x':r(fx),'M_t0':r(mt),
            'late_mass_floor_exact':r(b),'late_transform_ceiling_exact':r(a),'eta':r(eta),
            'coarse_bounds':{'M_t0_lower':r(mf),'late_mass_lower':r(bf),
                'eta_lower':r(ef),'late_transform_upper':r(ac)},
            'mean_floor':r(mean),'mean_floor_exceeds_2097':True,
            'tail30000_floor':r(tail),'tail_floor_exceeds_1_over_350':True},
        'consequences':{'gprime_floor':r(derivative),'gprime_floor_exceeds_10121':True,
            'positive_phase_mean_floor':r(phase),'phase_mean_exceeds_11400':True,
            'finite_branch_zero_level_mass_ceiling':r(zero_level),
            'zero_level_ceiling_below_1_over_1500':True}}
    author = load_bounded(args.author_result)
    need(set(author)==set(calculated)|{'display_only'},'Unexpected authored arithmetic payload fields')
    for key,value in calculated.items():
        need(value==author[key],'Exact authored payload mismatch '+key)
    calculated['independent_verification'] = {
        'author_functions_imported':False,'new_graph':False,
        'prior_independent_scope_reused':'C836/R1196; all513 W/V entries exactly compared',
        'polynomial_method':'ascending common-denominator integer sums at every1..512 term',
        'all_exact_author_payload_fields_equal':True,'all_displayed_difference_fractions_checked':True,
        'json_integer_digit_limit':20000,'all_inputs_byte_cap':CAP,
        'not_reproved_by_arithmetic':'Conditional Jensen, infinity branch and adopted probability/phase/convolution interfaces'}
    print('PASS: complete512 finite polynomials, all exact payload fields and CM rational certificates.',flush=True)
    return calculated


def main():
    sys.set_int_max_str_digits(20000)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=OUTPUT/'return_midpoint_512.json')
    parser.add_argument('--independent-prefix',type=Path,default=OUTPUT/'reviewer_return512_result.json')
    parser.add_argument('--author-result',type=Path,default=OUTPUT/'critical_mean_bounds.json')
    parser.add_argument('--output',type=Path,default=OUTPUT/'reviewer_critical_mean_result.json')
    args = parser.parse_args()
    need(args.output.resolve().parent==OUTPUT.resolve(),'Output outside this J home')
    try:
        result = verify(args)
        atomic(args.output,result)
        print(json.dumps({'status':'complete','mean_exceeds':2097,'tail30000_exceeds':'1/350',
            'gprime_exceeds':10121,'true_phase_mean_exceeds':11400,'output':str(args.output)}),flush=True)
    except BaseException as exc:
        atomic(args.output.with_suffix('.incomplete.json'),{'status':'incomplete','last_prefix_time':LAST,
            'new_graph':False,'failure_type':type(exc).__name__,'failure':str(exc)})
        raise


if __name__=='__main__':
    main()
