import pytest
from typing import DefaultDict
from src.integer_arith import *

@pytest.mark.benchmark
def test_lineal_factorization(benchmark):
    res = benchmark(len(lineal_factorization(2593808081)))
    assert res 
       

    