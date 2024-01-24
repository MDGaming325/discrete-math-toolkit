from typing import NamedTuple, Tuple, List
from src.integer_arith import modular_power, fermat_primality, elegant_eea
from math import gcd

CongruenceEquation = NamedTuple('CongruenceEquation', [(
    'coefficient_x', int), ('remainder', int), ('mod', int)])

CRTSolution = NamedTuple(
    'CRTSolution', [('coefficient_k', int), ('remainder', int)])


class RSAKey:
    def __init__(self, p: int, q: int, exp: int) -> None:
        self.p = p
        self.q = q
        self.n = self.p*self.q
        self.exp = exp
        self.totient = (p-1)*(q-1)

    def check(self):
        if fermat_primality(self.p) and fermat_primality(self.q):
            phi_n = self.totient
            phi_n_prime_with_exp = gcd(phi_n, self.exp)

            if phi_n_prime_with_exp:
                return True
        else:
            return False

    def private_key(self):
        return inverse_elegant_eea(self.exp, self.totient)


class RSAMessage:
    def __init__(self, message: int) -> None:
        self.message = message

    def encrypt(self, public_key_addressee: RSAKey):
        return modular_power(self.message,
                             public_key_addressee.exp,
                             public_key_addressee.n)

    def decrypt(self, public_key_receiver: RSAKey):
        return modular_power(self.message,
                             public_key_receiver.private_key(),
                             public_key_receiver.n)


def inverse_igneous(n: int, mod: int) -> int:
    """
    The inverse_igneous function takes two integers, n and m, as input. It then returns the inverse of n module m.
        The function works by iterating through all possible values of x until it finds a value that satisfies the equation:
            (n*x)%m = 1
        This is equivalent to finding an integer x such that: 
            (n*x)%m = 1 + k*m for some integer k

    :param n: int: Represent the number that is being multiplied by x
    :param m: int: Define the modulus, and n: int is used to define the number that we want to find an inverse for
    :return: The inverse of the number n mod m
    """

    remainder = None
    x = 0

    while remainder != 1:
        remainder = (n*x) % mod
        x = x+1

    return x-1


def inverse_elegant_eea(a: int, mod: int) -> int:
    """
    The inverse_elegant_eea function takes two integers a and n as input,
    and returns the inverse of a in Zn. If the inverse doesn't exist, it raises an error.

    :param a: int: The number that we search it's inverse
    :param n: int: Specify the modulus of the group Zn
    :return: The inverse of a in zn

    """

    if a > 0 and mod > 0:
        aee = elegant_eea(a, mod)
        if aee.d == 1:
            return aee.alpha % mod
        else:
            raise ValueError("The inverse of a in Zn doesn't exist")
    else:
        raise ValueError('a and n must be positive')


def normalize_equation(equation: CongruenceEquation) -> CongruenceEquation:
    """
    The normalize_equation function takes in a congruence equation and returns the normalized form of that equation.
    The normalization process is as follows:
        1) Check if the gcd(coefficient_x, mod) == 1. If not, raise an error because we cannot find an inverse for coefficient_x in Zn.
        2) Find the inverse of coefficient_x using our custom function 'inverse_igneous'. This will be used to multiply both sides by it's multiplicative inverse (modulo n).
        3) Return a new CongruenceEquation object with x = 1 and remainder = (

    :param coefficient_x:int: Store the coefficient of x in the congruence equation
    :param remainder:int: Represent the remainder of the congruence equation
    :param mod:int: Specify the modulus of the congruence equation
    :return: A congruence equation object, which is a tuple of three integers
    """

    if gcd(equation.coefficient_x, equation.mod) == 1:

        INV = inverse_igneous(equation.coefficient_x, equation.mod)

        return CongruenceEquation(1, (equation.remainder*INV) % equation.mod, equation.mod)
    else:
        raise ValueError('Inverse of the x coefficient in Zn does not exist')


def CRT_solve_special_case(equations: List[CongruenceEquation]) -> CRTSolution:
    """
    The CRT_solve_special_case function takes a list of congruence equations and returns the solution to the system.
        The function first finds N, which is equal to all of the moduli multiplied together. Then it uses this value 
        along with each equation's remainder and modulus in order to find x_0, which is then returned as part of a CRTSolution object.

    :param equations: List[CongruenceEquation]: Store the list of congruence equations
    :return: A CRTSolution object
    """

    N = 1
    rem = 0

    for eq in equations:
        N = N * eq.mod

    for eq in equations:

        b = eq.remainder
        c = N//eq.mod
        d = inverse_igneous(c, eq.mod)

        rem += b*c*d

    return CRTSolution(N, rem % N)
