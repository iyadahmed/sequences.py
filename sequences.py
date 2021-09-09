import numpy as np
from math import sqrt, ceil


def hailstone(n=100):
    yield n
    while n > 1:
        if (n % 2) == 1:
            n = 3 * n + 1
        else:
            n //= 2
        yield n


def primes(max_num=10):
    """Generate primes less than max_num"""
    if max_num >= 1:
        yield 2

    # TODO: store isprime bool value for odd numbers only (max_num / 2)
    isprime = np.ones(max_num, dtype=bool)

    # odd only sieve
    i = 3
    while (i * i < max_num):
        if isprime[i]:
            isprime[i * i:max_num:2 * i] = False
        i += 2

    for i in range(3, max_num, 2):
        if isprime[i]:
            yield i


def odd(stop=10, start=1):
    if start % 2 == 0:
        start += 1
    for i in range(start, stop, 2):
        yield i


def even(stop=10, start=2):
    if start % 2 != 0:
        start += 1
    for i in range(start, stop, 2):
        yield i


def triangular(end=10, start=0):
    for n in range(start, end):
        yield (n * (n + 1)) // 2
