import sys
sys.path.append('src')
from recursion import *



x = HomogenousRecursion(
    (1,4),[RecursionCase(0,0), RecursionCase(1,1)]
)

print(x.coefficients)
print(x.cases[0])
print(x.grade())
print(x.solve_for_n(3))