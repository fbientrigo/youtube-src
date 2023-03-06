from sympy import *
from sympy.abc import k
__MAX__ = symbols('__MAX__')

BracketSolverLib2 = {}
BracketSolverLib2[__MAX__] = 4

#=========================================================
def ExtractHypergeometricParameters(Function_):
 
    aux_ = Function_.find(Gamma, pochhammer)
    aux_ = list(filter(lambda x: any(k[i] in x.free_symbols for i in range(1, __MAX__+1)), expand(aux_)))
    
    return aux_
 
BracketSolverLib2['ExtractHypergeometricParameters'] = ExtractHypergeometricParameters
#=========================================================
def ExtractPreFactor(Function_):

    aux1_ = Function_.subs({Gamma(x): gamma(x), pochhammer(x, n): RisingFactorial(x, n)})
    aux2_ = aux1_.find(Gamma, pochhammer)
    aux1_ = expand(aux1_.subs(aux2_, 1) * aux2_.subs(Gamma(x), gamma(x)).subs(pochhammer(x, n), RisingFactorial(x, n)))
    for i_ in range(1, __MAX__+1):
        aux1_ = aux1_.subs(k[i_], 1)
    aux1_ = simplify(aux1_)
    
    return aux1_

BracketSolverLib2['ExtractPreFactor'] = ExtractPreFactor
