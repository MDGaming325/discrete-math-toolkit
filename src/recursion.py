from typing import *
from math import sqrt

'''Please note that we define recursions like as the example given: Aa(n) = Ba(n-1) + Ca(n-2),
    where A,B,C are coefficients.'''

RecursionCase = NamedTuple('Case', [('index', int), ('value', int)])

RecursionSolution = NamedTuple('RecursionSolution', [('grade', int),
                                                     ('double_root', Union[bool,None]),
                                                     ('coefficient0', int),
                                                     ('root0', int),
                                                     ('coefficient1', Union[int,None]),
                                                     ('root1', Union[int,None])])

class HomogenousRecursion:

    def __init__(self, coefficients:Tuple[int,int,Optional[int]], cases:List[RecursionCase]) -> None: 
        self.coefficients = coefficients
        self.cases = cases

    def grade(self) -> int:
        if len(self.coefficients) == 2:
            grade = 1
        else:
            grade = 2
        return grade
        
    def solve(self) -> RecursionSolution:

        grade = self.grade()

        if grade == 1:

            root = self.coefficients[1]/self.coefficients[0]
            coefficient = self.cases[0].value/root**self.cases[0].index

            return RecursionSolution(1,None,coefficient,root,None,None)
        else:

            discriminant = sqrt(self.coefficients[1]**2-4*self.coefficients[0]*(-self.coefficients[2]))
    
            r0 = (self.coefficients[1] + discriminant)/2*self.coefficients[0]     
            r1 = (self.coefficients[1] - discriminant)/2*self.coefficients[0]

            if r0 == r1:
                C = self.cases[0].value
                D = self.cases[1].value/r0 - C

                res = RecursionSolution(2, True, C, r0, D, None)

            else:
                D = (self.cases[1].value -self.cases[0].value*r0)/(r1-r0)
                C = self.cases[0].value - D

                res = RecursionSolution(2, False, C, r0, D, r1) 
  
            return res

    def solve_for_n(self,n:int) -> float:
        grade = self.grade()
        solution = self.solve()

        if grade == 1:
            return solution.coefficient0*solution.root0**n
        else:
            if solution.double_root == True:
                return (solution.coefficient0+n*solution.coefficient1)*solution.root0**n
            else:
                return solution.coefficient0*solution.root0**n+solution.coefficient1*solution.root1**n
            

