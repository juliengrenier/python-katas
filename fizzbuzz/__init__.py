# -*- coding: utf-8 -*-

def fizzbuzz(x):
    if x % 15 == 0:
        return 'fizzbuzz'
    if x % 3 == 0:
        return 'fizz'
    if x % 5 == 0:
        return 'buzz'
    return x