from typing import DefaultDict, NamedTuple, Tuple, List
from math import sqrt, floor
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
    The fermat_factorization function takes an integer n as input and returns a tuple of two integers,
    the first being the smaller factor and the second being the larger factor. The function uses Fermat's 
    factorization method to find these factors.

    :param n:int: Specify that the function only accepts integers as input
    :return: A tuple of two integers
    """

    if n % 2 != 0:
        S = floor(sqrt(n))
        l = 1
        k = 1.1

        while k != int(k):
            k = sqrt((S+l)**2-n)
            l = l + 1

        return (S+l-k-1, S+l+k-1)
    else:
        raise ValueError('Candidate n must be an even number')

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

        The algorithm works by first checking if 2 or 3 are divisors of the number, since these are the only even primes. 
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
