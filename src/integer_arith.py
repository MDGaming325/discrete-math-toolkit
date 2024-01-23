from typing import DefaultDict, NamedTuple, Tuple, List
from math import sqrt, floor

EuclideanDivision = NamedTuple('EuclideanDivision', [('dividend', int), ('divisor', int), ('quotient', int), ('remainder', int)])

def sieve_of_eratosthenes(n:int) -> List[int]:
    
    primes = [2]
    not_primes = list()
    candidates = list(range(3,n+1,2))

    for candidate in candidates:
        for elem in primes:
            if candidate % elem == 0:
                not_primes.append(candidate)

        if candidate not in not_primes:
            primes.append(candidate)

    return primes


def lineal_factorization(n:int) -> List[Tuple[int,int]]:

    brk = True
    quotient = None
    res = DefaultDict(int)
    floor_sqrt_n = floor(sqrt(n))
    primes_to_check = sieve_of_eratosthenes(floor_sqrt_n)

    while quotient != 1 and brk:
            for prime in primes_to_check:

                if n%prime == 0:
                    while n%prime == 0 and (quotient == None or prime < sqrt(quotient)):
                        res[prime] += 1
                        quotient = n//prime
                        n = quotient

                elif prime == primes_to_check[-1]:
                    res[quotient] += 1
                    brk = False
                    break

    return list(res.items())    


def fast_check_prime(n:int) -> bool:
    """
    The fast_check_prime function is a fast way to check if a number is prime.
    It works by checking if the number can be expressed as 6k +/- 1, where k is an integer.
    If it can, then it returns True; otherwise False.
    
    :param n:int: Specify the input type of n, and the -&gt; bool parameter is used to specify that this function returns a boolean value
    :return: True or false
    """
    
    if n > 5:
        k0 = (n-1)/6
        k1 = (n+1)/6

        if float(k0).is_integer() != float(k1).is_integer():
            return True
        else:
            return False
        
    else:
        raise ValueError('Candidate n must be >5')




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
    remainder = None

    # First append
    operations.append(EuclideanDivision(a, b, a // b, a % b))


    # Loop
    while remainder != 1:
        e0 = operations[-1].divisor
        e1 = operations[-1].remainder

        r = e0 % e1
        operations.append(EuclideanDivision(e0, e1, e0 // e1, r))
        remainder = r

    return operations

def fermat_factorization(n:int) -> Tuple[int,int]:
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
