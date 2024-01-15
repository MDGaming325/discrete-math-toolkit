import sys
from typing import NamedTuple, Tuple, List 

sys.path.append('src')
import modular_arith as modarith

def test_CRT_solve_special_case(equations: List[modarith.CongruenceEquation]):
    """
    The test_CRT_solve_special_case function tests the CRT_solve_special_case function.
        It takes a list of congruence equations as input and prints out the solution to those equations.


    :param equations: List[CongruenceEquation]: Pass a list of congruence equations to the function
    :return: The solution of the congruence equations
    """

    x = modarith.CRT_solve_special_case(equations)

    print('='*50)
    print('Test of the function CRT_solve_special_case')
    print(x)

if __name__ == '__main__':
    test_CRT_solve_special_case(
        [modarith.CongruenceEquation(1,22,2),
        modarith.CongruenceEquation(1,7,3),
        modarith.CongruenceEquation(1,160,5)]
    )