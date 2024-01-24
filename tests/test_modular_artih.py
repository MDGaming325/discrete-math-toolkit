import pytest
from src.modular_arith import *

special_case = [CongruenceEquation(1, 22, 2),
                CongruenceEquation(1, 7, 3),
                CongruenceEquation(1, 160, 5)]

# RSA Tests

bob = RSAKey(7369362041, 5460505879, 21117089390589805177)
bob_message = RSAMessage(101010)
bob_message_encrypted = RSAMessage(33457254919621869997)

alice = RSAKey(7369362041, 5460505879, 21117089390589805177)


def test_rsa_check_key(benchmark):
    check = benchmark(bob.check)
    assert check == True


def test_rsa_private_key(benchmark):
    check = benchmark(bob.private_key)
    assert check == 39690029651748795673


def test_crypt(benchmark):
    res = benchmark(bob_message.encrypt, alice)
    assert res == 33457254919621869997


def test_decrypt(benchmark):
    res = benchmark(bob_message_encrypted.decrypt, alice)
    assert res == 101010

# Other


def test_inverse_igneous(benchmark):
    inverse = benchmark(inverse_igneous, 12123, 5)
    assert inverse == 2


def test_normalize_equation(benchmark):
    normalized = benchmark(normalize_equation, CongruenceEquation(2, 5, 3))
    assert normalized == CongruenceEquation(1, 1, 3)


def test_CRT_solve_special_case(benchmark):

    solution = benchmark(CRT_solve_special_case, special_case)
    assert solution == CRTSolution(30, 10)


def test_inverse_elegant_eea(benchmark):
    res = benchmark(inverse_elegant_eea, 3, 10)
    assert res == 7
