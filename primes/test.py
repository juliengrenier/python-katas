# -*- coding: utf-8 -*-
from __future__ import absolute_import

from unittest import TestCase
from primes import primes


class PrimesTestCase(TestCase):
    def testPrimes_one(self):
        self.assertEquals([], primes.primes(1))

    def testPrimes_two(self):
        self.assertEquals([2], primes.primes(2))

    def testPrimes_three(self):
        self.assertEquals([3], primes.primes(3))

    def testPrimes_four(self):
        self.assertEquals([2, 2], primes.primes(4))

    def testPrimes_six(self):
        self.assertEquals([2, 3], primes.primes(6))

    def testPrimes_eight(self):
        self.assertEquals([2, 2, 2], primes.primes(8))

    def testPrimes_nine(self):
        self.assertEquals([3, 3], primes.primes(9))

    def testPrimes_49(self):
        self.assertEquals([7, 7], primes.primes(49))

    def testPrimes_191(self):
        self.assertEquals([191], primes.primes(191))

    def testPrimes_490(self):
        self.assertEquals([2, 5, 7, 7], primes.primes(490))

    def testPrimes_1490(self):
        self.assertEquals([2, 5, 149], primes.primes(1490))

    def testPrimes_572(self):
        self.assertEquals([2, 2, 11, 13], primes.primes(572))

    def testPrimes_573(self):
        self.assertEquals([3, 191], primes.primes(573))

if __name__ == '__main__':
    import unittest

    unittest.main()
