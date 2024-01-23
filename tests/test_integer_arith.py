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


@pytest.mark.skip
def test_lineal_factorization(benchmark):
    res = benchmark(lineal_factorization, 2593808081)
    assert res
