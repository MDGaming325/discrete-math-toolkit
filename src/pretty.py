from typing import *
import recursion as rec

def recursion(recursion:Union[rec.FirstLinealRecursion, rec.SecondLinealRecursion]) -> str:

    if type(recursion) == rec.FirstLinealRecursion:

        n_coeff = recursion.n_coeff
        n1_coeff = recursion.n1_coeff

        if n_coeff == 1:
            n_coeff = ''

        if n1_coeff == 1:
            n1_coeff = ''

        return f'{n_coeff}a(n) = {n1_coeff}a(n-1)'
    
    else:

        n_coeff = recursion.n_coeff
        n1_coeff = recursion.n1_coeff
        n2_coeff = recursion.n2_coeff
    
        if n_coeff == 1:
            n_coeff = ''

        if n1_coeff == 1:
            n1_coeff = ''

        if n2_coeff == 1:
            n2_coeff = ''

        return f'{n_coeff}a(n) = {n1_coeff}a(n-1) {n2_coeff}a(n-1)'

