# -*- coding: utf-8 -*-
from unittest import TestCase

from fizzbuzz import fizzbuzz

class FizzBuzzTest(TestCase):
    def testFizzbuzz1(self):
        self.assertEqual(1, fizzbuzz(1))

    def testFizzbuzz2(self):
        self.assertEqual(2, fizzbuzz(2))

    def testFizzbuzz3(self):
        self.assertEqual('fizz', fizzbuzz(3))

    def testFizzbuzz4(self):
        self.assertEqual(4, fizzbuzz(4))

    def testFizzbuzz5(self):
        self.assertEqual('buzz', fizzbuzz(5))

    def testFizzbuzz9(self):
        self.assertEqual('fizz', fizzbuzz(9))

    def testFizzbuzz10(self):
        self.assertEqual('buzz', fizzbuzz(10))


    def testFizzbuzz15(self):
        self.assertEqual('fizzbuzz', fizzbuzz(15))