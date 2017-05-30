from mystic.symbolic import _denominator, _solve_zeros, equals, simplify

var = list('BC')
eqn = 'A = (B + 1/C)/(B*C/tan(B))'
assert _denominator(eqn, var) == ['C', '(B*C/tan(B))', 'tan(B)']
eqn = 'A = 1/B + 1/(C + B*(B - 2))'
assert _denominator(eqn , var) == ['B', '(C + B*(B - 2))']
eqn = 'A = 1/B + 1/tan(B*C)'
assert _denominator(eqn , var) == ['B', 'tan(B*C)']
eqn = 'A = B - 3/(B-2)**2 - 1/(B+C)'
assert _denominator(eqn , var) == ['(B-2)', '(B+C)']
eqn = 'A = (B + 2)/C'
assert _denominator(eqn , var) == ['C']
eqn = 'A = B/(C - 2)'
assert _denominator(eqn , var) == ['(C - 2)']
eqn = 'A = (B*C/tan(B))'
assert _denominator(eqn , var) == ['tan(B)']
eqn = 'A = (1 + 1/C)'
assert _denominator(eqn , var) == ['C']
eqn = 'A = 4/(C*B)'
assert _denominator(eqn , var) == ['(C*B)']
eqn = 'A = C*B'
assert _denominator(eqn , var) == []

eqn = 'A = (B - 1/C)/(1 - (B*C))'
assert _solve_zeros(eqn, var) == ['C = 0', 'B = 1/C']
eqn = 'A = (B - 1/C)/(1 - sin(B*C))'
assert _solve_zeros(eqn, var) == ['C = 0', '(1 - sin(B*C)) = 0']
eqn = 'A = (B - 1/C)/(1 - (B*C)**2)'
assert _solve_zeros(eqn, var) == ['C = 0', 'B = 1/C']
eqn = 'A = (B - 1/C)/(4 - (B*C)**2)'
assert _solve_zeros(eqn, var) == ['C = 0', 'B = 2/C']
eqn = 'A = (B - 1/C)/(B - 1)**2'
assert _solve_zeros(eqn, var) == ['C = 0', 'B = 1']
eqn = 'A = B + 1'
assert _solve_zeros(eqn, var) == []

eqn = 'A**2 + B*(2 - C) < C*A'
var = list('ABC')
res = simplify(eqn, variables=var, target=list('CAB'), all=True)
#print '\n#####\n'.join(res)
assert equals(eqn, res[0].split('\n')[-1], dict(A=-0.9,B=1.,C=1.))
assert equals(eqn, res[0].split('\n')[-1], dict(A=-0.9,B=1.,C=-1.))
assert equals(eqn, res[0].split('\n')[-1], dict(A=1.1,B=-1.,C=1.))
assert equals(eqn, res[0].split('\n')[-1], dict(A=1.1,B=-1.,C=-1.))
assert equals(eqn, res[1].split('\n')[-1], dict(A=-1.1,B=1.,C=1.))
assert equals(eqn, res[1].split('\n')[-1], dict(A=-1.1,B=1.,C=-1.))
assert equals(eqn, res[1].split('\n')[-1], dict(A=0.9,B=-1.,C=-1.))
assert equals(eqn, res[1].split('\n')[-1], dict(A=0.9,B=-1.,C=1.))

res = simplify(eqn, variables=var, target=list('BCA'), all=True)
#print '\n#####\n'.join(res)
assert equals(eqn, res[0].split('\n')[-1], dict(A=1.,B=1.,C=2.1))
assert equals(eqn, res[0].split('\n')[-1], dict(A=1.,B=-1.,C=2.1))
assert equals(eqn, res[0].split('\n')[-1], dict(A=-1.,B=-1.,C=2.1))
assert equals(eqn, res[0].split('\n')[-1], dict(A=-1.,B=1.,C=2.1))
assert equals(eqn, res[1].split('\n')[-1], dict(A=1.,B=1.,C=1.9))
assert equals(eqn, res[1].split('\n')[-1], dict(A=1.,B=-1.,C=1.9))
assert equals(eqn, res[1].split('\n')[-1], dict(A=-1.,B=-1.,C=1.9))
assert equals(eqn, res[1].split('\n')[-1], dict(A=-1.,B=1.,C=1.9))

from mystic import random_seed
random_seed(321) #FIXME: should be commented out

#FIXME: tests in this block sometimes fail... (due to negative sqrt?)
res = simplify(eqn, variables=var, target=list('ABC'), all=True)
#print res
sqrt = lambda x:x**.5
#_ = eval(res.split('<')[-1],dict(B=0.,C=1.,sqrt=sqrt))
assert equals(eqn, res, dict(A=1.1,B=0.,C=1.,sqrt=sqrt))
assert equals(eqn, res, dict(A=0.9,B=0.,C=1.,sqrt=sqrt))

eqn = 'A + B*(2 - C)/A < C'
res = simplify(eqn, variables=var, target=list('CAB'), all=True)
#print '\n#####\n'.join(res)
assert equals(eqn, res[0].split('\n')[-1], dict(A=0.1,B=0.0,C=1.))
assert equals(eqn, res[0].split('\n')[-1], dict(A=0.1,B=0.0,C=-1.))
assert equals(eqn, res[1].split('\n')[-1], dict(A=0.1,B=-0.2,C=1.))
assert equals(eqn, res[1].split('\n')[-1], dict(A=0.1,B=-0.2,C=-1.))
assert equals(eqn, res[2].split('\n')[-1], dict(A=-0.1,B=0.2,C=1.))
assert equals(eqn, res[2].split('\n')[-1], dict(A=-0.1,B=0.2,C=-1.))
assert equals(eqn, res[3].split('\n')[-1], dict(A=-0.1,B=0.0,C=-1.))
assert equals(eqn, res[3].split('\n')[-1], dict(A=-0.1,B=0.0,C=1.))

res = simplify(eqn, variables=var, target=list('BCA'), all=True)
#print '\n#####\n'.join(res)
assert equals(eqn, res[0].split('\n')[-1], dict(A=0.1,B=1.,C=2.1))
assert equals(eqn, res[0].split('\n')[-1], dict(A=0.1,B=-1.,C=2.1))
assert equals(eqn, res[1].split('\n')[-1], dict(A=0.1,B=1.,C=1.9))
assert equals(eqn, res[1].split('\n')[-1], dict(A=0.1,B=-1.,C=1.9))
assert equals(eqn, res[2].split('\n')[-1], dict(A=-0.1,B=1.,C=2.1))
assert equals(eqn, res[2].split('\n')[-1], dict(A=-0.1,B=-1.,C=2.1))
assert equals(eqn, res[3].split('\n')[-1], dict(A=-0.1,B=1.,C=1.9))
assert equals(eqn, res[3].split('\n')[-1], dict(A=-0.1,B=-1.,C=1.9))

#FIXME: tests in this block sometimes fail... (due to negative sqrt?)
res = simplify(eqn, variables=var, target=list('ABC'), all=True)
#print '\n#####\n'.join(res)
#_ = eval(res.split('<')[-1],dict(B=0.,C=1.,sqrt=sqrt))
#_ = eval(res.split('<')[-1],dict(B=2.,C=-10.,sqrt=sqrt))
assert equals(eqn, res[0].split('\n')[-1], dict(A=0.1,B=0.,C=1.,sqrt=sqrt))
assert equals(eqn, res[1].split('\n')[-1], dict(A=-0.1,B=2.,C=-10.,sqrt=sqrt))