from sympy import *
from sympy.abc import k
__MAX__ = symbols('__MAX__')

BracketSolverLib2 = {}
BracketSolverLib2[__MAX__] = 4


#===========================================================
# objeto braket

from sympy import *

class braket(Symbol):
    def __new__(cls, argument, **kwargs):
        # cls es una referencia a la clase siendo creada
        # re escrbimos para nuevos atributos
        obj = super().__new__(cls, str(argument), **kwargs)
        # el inside es un symbol, se asume generalidad, puede hasta ser un symbol
        obj.argument = argument
        # print(type(obj.argument)) # quick debugging
        return obj

    def __str__(self):
        return f"braket({self.argument})"

    
    def _latex(self, printer):
        """
        Permite incluir una representacion de printing de latex
        """
        return "\\langle " + printer._print(self.argument) + "\\rangle "

    def args(self):
        # experimental, al correr braket(..).args() se devuelve a si mismo
        return (self,)
    
    #def __mul__(self, other):
    #    pass

    def solve(self, symbol_to_solve : Symbol, debug_print: bool = False):
        """
        Takes input of a symbol included inside the braket, and returns the solution
        """
        solutions = solve(self.argument, symbol_to_solve)
        if debug_print:
            print(f'number of solutions: {len(solutions)}')

        if len(solutions) == 0:
            print('no solutions found')
        else:
            return solutions[0]

    def coefficients(self, symbol : Symbol):
        """
        Returns the coefficients of the symbol inside the braket.
        """
        return self.argument.coeff(symbol)

    def normalize(self, symbol : Symbol):
        """
        Returns a new braket object with the modified argument as described.

        \sum_n <a*n + b> = \sum_n (1/|a|) <n + b/a>

        """
        coeff_n = self.coefficients(symbol)
        if coeff_n == 0:
            return self
        else:
            new_arg = self.argument / coeff_n
            return coeff_n * braket(new_arg)


def get_equations(expresion):
    """
    Extract the equations from all brakets present in themselves or multiplication
    """
    equations = []
    symbols_in_braket = []

    
    if isinstance(expresion, braket):
        eq = expresion.argument
        equations.append(eq) # append as equation

        free_symbols = eq.free_symbols #see symbols inside a braket
        for symbol in free_symbols: 
            if symbol not in symbols_in_braket: # add the symbol if not already added
                symbols_in_braket.append(symbol)

        return {'symbols': symbols_in_braket, 'equations': equations}


    if isinstance(expresion, Mul):
        for term in expresion.args:
            if isinstance(term, braket):
                # get the inside of a braket
                eq = term.argument
                equations.append(eq) # append as equation

                free_symbols = eq.free_symbols #see symbols inside a braket
                for symbol in free_symbols: 
                    if symbol not in symbols_in_braket: # add the symbol if not already added
                        symbols_in_braket.append(symbol)
        return {'symbols': symbols_in_braket, 'equations': equations}




def normalize_braket(expresion):
    """
    Not neccesary, the use of going throught every braket and using braket.modified()
    but all of this occurs in the use of matrix
    """
    pass



def solve_braket_equations(expresion):
    """
    Extracts all equations from the argument of the multibraket.
    
    Extracts all the symbols contained inside all of brakets
    then creates a J matrix (square)
    and solves the system of equations

    returns 
        - the normalization_coefficient = 1 / |det J|
        - the solutions of the equations

    """

    # obtains equations of the shape of dict {'symbols': [..], 'equations': [..]}
    data = get_equations(expresion)

    # square matrix for the normalization of brakets in bulk
    J = Matrix([[eq.diff(var) for var in data['symbols']] for eq in data['equations']])
    solutions = solve(data['equations'], data['symbols'])

    return {'coefficient': 1/abs(det(J)), 'solutions': solutions}


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
