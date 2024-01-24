import pytest
from typing import DefaultDict
from src.integer_arith import *


def test_modular_power(benchmark):
    res = benchmark(modular_power,
                    12345678,
                    23456789,
                    34567890)
    assert res == 32654808


def test_fermat_primality(benchmark):
    res = benchmark(fermat_primality,
                    1000000000000066600000000000001,
                    100)
    assert res == True


def test_sieve_of_eratosthenes(benchmark):
    res = benchmark(sieve_of_eratosthenes, 100)
    assert res == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                   43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def test_divp_algorithm(benchmark):
    res = benchmark(divp_algorithm, 44021)
    assert res == 44021


def test_divp_factorization(benchmark):
    expected = {2: 6, 3: 1, 643: 1}
    res = benchmark(divp_factorization, 123456)
    assert res == expected.items()


def test_fermat_factorization(benchmark):
    expected = {2: 6, 3: 1, 643: 1}
    res = benchmark(fermat_factorization, 2027651281)
    assert res == (44021, 46061)


def test_fermat_factorization2(benchmark):
    expected = {2: 6, 3: 1, 643: 1}
    res = benchmark(fermat_factorization, 64645311)
    assert res[0]*res[1] == 64645311


def test_totient_prime(benchmark):
    res = benchmark(totient, 46061)
    assert res == 46060


def test_totient_not_prime(benchmark):
    res = benchmark(totient, 972)
    assert res == 324


@pytest.mark.skip(reason='Depends on DIVP, too slow')
def test_totient_strong(benchmark):
    res = benchmark(totient, 73448480092567094497)
    assert res == 73448480075426676756


def test_elegant_eea(benchmark):
    res = benchmark(elegant_eea, 1492, 1066)
    assert (res.d, res.alpha, res.beta) == (2, -5, 7)
