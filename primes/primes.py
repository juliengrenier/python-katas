# -*- coding: utf-8 -*-

import math

def range_prime(x):
    _prime_array = [0] * (2 * x)
    p = 2
    _prime_array[p] = 1

    while p < x:
        for index in range(p, x, p):
            _prime_array[index] = 1
        yield p
        p += 1
        while _prime_array[p] == 1:
            p += 1

def factors(x):
    return [i for i in range_prime(int(math.sqrt(x)) + 1) if x % i == 0]


def primes(x):
    if x == 1:
        return []
    fs = factors(x)
    if not fs:
        return [x]

    sfs = reduce(lambda x, y: x * y, fs)
    if sfs == x:
        return fs

    fs.extend(primes(x / sfs))
    fs.sort()
    return fs