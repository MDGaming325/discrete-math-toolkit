from typing import DefaultDict, NamedTuple, Tuple, List
from math import sqrt, floor, gcd
from sympy import sign, factor, symbols
import random

EuclideanDivision = NamedTuple('EuclideanDivision', [(
    'dividend', int), ('divisor', int), ('quotient', int), ('remainder', int)])

EuclideanExtended = NamedTuple(
    'EuclideanExtended', [('d', int), ('alpha', int), ('beta', int)])

# Basic


def mod_exponentiation(b: int, e: int, n: int) -> int:
    """
    The mod_exponentiation function takes in three integers, b, e and n.
    It returns the result of b^e (mod n).


    :param b: int: Represent the base of the modular power
    :param e: int: Specify the exponent
    :param n: int: Specify the modulus
    :return: The result of b^e mod n

    """

    res = 1
    exp_bin = bin(e)[2:]
    ins = [exp_bin[0]]

    for e in exp_bin[1:]:
        ins.append('C')
        ins.append(e)

    for char in ins:
        if char == '1':
            res = (res*b) % n
        elif char == 'C':
            res = (res**2) % n

    return res


def totient(n: int) -> int:
    """
    The totient function, also known as Euler's totient function,
    is a multiplicative function that counts the number of positive integers
    less than or equal to n that are relatively prime to n.

    :param n: int: Specify the number that we want to find the totient of
    :return: The totient of n

    """

    if fermat_primality(n):
        return n - 1

    else:
        primes = divp_factorization(n)
        res = n

        for key, _ in primes:
            res = res * (1-1/key)

        return int(res)


# Primality Tests


def fermat_primality(n: int, confidence: int = 100) -> bool:
    """
    The fermat_primality function takes in a number n and a confidence level, 
    and returns True if the number is prime with high probability. The function 
    uses Fermat's Little Theorem to test for primality. Please note that this
    is a probability test. 

    :param n: int: Specify the number to test for primality
    :param confidence: int: Determine how many times the function should run
    :return: True if n is a PROBABLY prime number and false otherwise.

    """

    for _ in range(confidence):
        b = random.randint(2, n-1)
        if mod_exponentiation(b, n, n) != b % n:
            return False
    return True

# Factorization


def divp_factorization(n: int) -> List[Tuple[int, int]]:
    """
    The divp_factorization function takes a positive integer n and returns the prime factorization of n.

        Args:
            n (int): A positive integer.

        Returns: 
            List[Tuple[int, int]]: The prime factorization of n as a list of tuples where each tuple is in the form (p, e) where p is a prime number and e is its exponent in the factorization.

    :param n: int: Pass the number to be factored into the function
    :return: A list of tuples

    """

    res = DefaultDict(int)
    while n > 1:
        p = divp_algorithm(n)
        res[p] += 1
        n = n//p

    return res.items()


def fermat_factorization(n: int) -> Tuple[int, int]:
    """
    The fermat_factorization function takes an integer n and returns
    a tuple of two integers, the first being the factorization of n.
        Args:
            n (int): An integer to be factored using Fermat's method.
    :param n: int: Specify the value of n in the equation x^2 - n = y^2
    :return: A tuple of prime numbers that multiplied equals n
    """

    if n % 2 != 0:
        l = 0
        candidate = None
        while candidate == None or (n/(int(candidate)+l)).is_integer() != True:
            l = l + 1
            candidate = sqrt(n+(l**2))

        return (int(candidate)+l, int(candidate)-l)
    else:
        raise ValueError('n must be even')

# Primes


def sieve_of_eratosthenes(n: int) -> List[int]:
    """
    The sieve_of_eratosthenes function takes a number n and returns all prime numbers less than or equal to n.
        The function uses the Sieve of Eratosthenes algorithm, which is an ancient method for finding prime numbers.
        It works by first creating a list of all integers from 2 up to the inputted number (n). Then it iterates through 
        each element in this list and removes any multiples of that element from the list. After removing these multiples, 
        only primes remain in the list.

    :param n: int: Specify the upper limit of the range of numbers to be checked
    :return: A list of prime numbers up to n

    """

    primes = [2]
    not_primes = list()
    candidates = list(range(3, n+1, 2))

    for candidate in candidates:
        for elem in primes:
            if candidate % elem == 0:
                not_primes.append(candidate)

        if candidate not in not_primes:
            primes.append(candidate)

    return primes


def divp_algorithm(n: int) -> int:
    """
    The divp_algorithm function takes a positive integer n as input and returns the smallest prime divisor of n.
        If n is prime, then it returns itself.

        The algorithm works by first checking if 2 or 3 are divisors of the number, since these are the only odd primes. 
        Then it checks all odd numbers up to sqrt(n) for primality using modular arithmetic.

    :param n: int: Specify that the function takes an integer as input
    :return: The smallest prime divisor of n

    """

    if n > 0:
        if n % 2 == 0:
            return 2
        elif n % 3 == 0:
            return 3

        m = floor(sqrt(n)-1//6)

        for k in range(1, m+1):
            if (6*k-1) % n == 0:
                return 6*k-1
            elif (6*k+1) % n == 0:
                return 6*k-1
            elif k == m:
                return n

    else:
        raise ValueError('n must be positive')


# Euclid


def euclidean_algorithm(a: int, b: int) -> List[EuclideanDivision]:
    """
    The euclidean_algorithm function takes two positive integers, a and b, as input.
    It returns the list of EuclideanDivision objects that represent the steps in 
    the Euclidean algorithm for finding the greatest common divisor of a and b.


    :param a: int: Represent the first number in the euclidean algorithm
    :param b: int: Represent the second number in the euclidean algorithm
    :return: A list of EuclideanDivision objects
    """

    operations = list()
    last_remainder = None

    # First append
    operations.append(EuclideanDivision(a, b, a // b, a % b))

    # Loop
    if operations[-1].remainder == 0:
        return operations
    else:
        while last_remainder != 0:
            e0 = operations[-1].divisor
            e1 = operations[-1].remainder

            r = e0 % e1
            operations.append(EuclideanDivision(e0, e1, e0 // e1, r))
            last_remainder = r

        return operations


def elegant_eea(a: int, b: int) -> EuclideanExtended:
    """
    The elegant_eea function is an elegant implementation of the extended Euclidean algorithm.
    It uses the same logic as the eea function, but it does use the invariant method.

    :param a: int: Any int
    :param b: int: Any int or the mod to get the inverse of a in Zb
    :return: An EuclideanExtended object

    """

    r, old_r = b, a
    s, old_s = 0, 1
    t, old_t = 1, 0

    while r > 0:
        c = int(floor(old_r/r))

        old_r, r = r, old_r - c*r
        old_s, s = s, old_s - c*s
        old_t, t = t, old_t - c*t

    return EuclideanExtended(old_r, old_s, old_t)

# Diophantine Equations


class Diophantine:

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = gcd(self.a, self.b)
        self.new_a = self.a//self.d
        self.new_b = self.b//self.d
        self.new_c = self.c//self.d

    def check(self):
        if self.c % self.d == 0:
            return True
        else:
            return False

    def particular_solution(self):

        if self.check():

            bezout = elegant_eea(abs(self.new_a), abs(self.new_b))

            return (sign(self.new_a)*bezout.alpha*self.new_c,
                    sign(self.new_b)*bezout.beta*self.new_c)
        else:
            return ValueError('Diophantine Equation has no solution')

    def general_solution(self):

        particular = self.particular_solution()

        k = symbols('k')
        sy_a = symbols('sy_a')  # Symbol associated with new_a
        sy_b = symbols('sy_b')  # Symbol associated with new_b

        sign_a = int(sign(self.new_a))
        sign_b = int(sign(self.new_b))

        if sign_b < 0:  # Improve
            sub = -1
        else:
            sub = 1

        add_and_subtract = sy_a * sy_b * k

        expr_x = (particular[0] + add_and_subtract)
        expr_y = (particular[1] - add_and_subtract)

        expr_x = factor(expr_x, sign_a*sy_a).subs(sy_a, sub)
        expr_y = factor(expr_y, sign_b*sy_b).subs(sy_b, sub)

        expr_x = expr_x.subs(sy_b, self.new_b)
        expr_y = expr_y.subs(sy_a, self.new_a)

        return (expr_x, expr_y)

    def restrictions(self):
        # TODO
        pass
