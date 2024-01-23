from pytest import approx
from src.modular_arith import *

special_case = [CongruenceEquation(1, 22, 2),
                CongruenceEquation(1, 7, 3),
                CongruenceEquation(1, 160, 5)]

def test_inverse_igneous():
    inverse = inverse_igneous(12123,5)
    assert inverse == 2

def test_normalize_equation():
    normalized = normalize_equation(CongruenceEquation(2,5,3))
    assert normalized == CongruenceEquation(1,1,3)

def test_CRT_solve_special_case():

    solution = CRT_solve_special_case(special_case)
    assert solution == CRTSolution(30, 10)