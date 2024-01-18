from typing import *
from math import sqrt

# As a recursion like: Aa(n) = Ba(n-1) + C(n-2)

Case = NamedTuple('Case', [('n', int), ('value', int)])

FirstLinealRecursion = NamedTuple('FirstLinealRecursion', [('n_coeff', int),
                                                 ('n1_coeff', int)])

SecondLinealRecursion = NamedTuple('SecondLinealRecursion', [('n_coeff', int),
                                                 ('n1_coeff', int),
                                                 ('n2_coeff', int)])

FirstGradeSolution = NamedTuple('FirstGradeSolution', [('coeff', int),
                                                       ('root', int)])

SecondGradeSolution = NamedTuple('SecondGradeSolution', [('coeff0', int),
                                                       ('root0', int),
                                                       ('coeff1', int),
                                                       ('root1', int),
                                                       ('double_root', bool)])



def solve_first_grade_recursion(first_grade_recursion:FirstLinealRecursion, case:Case) -> FirstGradeSolution:

    root = first_grade_recursion.n1_coeff/first_grade_recursion.n_coeff
    coeff = case.value/root**case.n

    return FirstGradeSolution(coeff,root)

def solve_second_grade_recursion(second_grade_recursion:SecondLinealRecursion, initial_case:Case, case:Case) -> SecondGradeSolution:

    discriminant = sqrt(second_grade_recursion.n1_coeff**2-4*second_grade_recursion.n_coeff*(-second_grade_recursion.n2_coeff))
    
    r0 = (second_grade_recursion.n1_coeff + discriminant)/2*second_grade_recursion.n_coeff     
    r1 = (second_grade_recursion.n1_coeff - discriminant)/2*second_grade_recursion.n_coeff 

    if r0 == r1:
        C = initial_case.value
        D = case.value/r0 - C

        res = SecondGradeSolution(C, r0, D, r1, double_root=True)

    else:
        D = (case.value -initial_case.value*r0)/(r1-r0)
        C = initial_case.value - D

        res = SecondGradeSolution(C, r0, D, r1, double_root=False) 
  
    return res

print(solve_second_grade_recursion(SecondLinealRecursion(1,1,1), Case(0,0), Case(1,1)))