# Adapt the code to your code kata romans.

import unittest
from itertools import islice, izip_longest

class Romans:
    def to_numerical(self, roman_number):
        def add(rv1, rv2):
            v1 = values[rv1]
            if not rv2:
                return v1
            v2 = values[rv2]
            if v1 < v2:
                return v2 - v1
            return v1 + v2

        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
        return reduce(
            lambda s, (rv1, rv2): s + add(rv1, rv2),
            izip_longest(islice(roman_number, 0, None, 2), islice(roman_number, 1, None, 2)),
            0)


class TestRomans(unittest.TestCase):
    def test_to_numerical(self):
        roman = Romans()
        self.assertEqual(1, roman.to_numerical("I"))
        self.assertEqual(5, roman.to_numerical("V"))
        self.assertEqual(10, roman.to_numerical("X"))
        self.assertEqual(50, roman.to_numerical("L"))
        self.assertEqual(100, roman.to_numerical("C"))
        self.assertEqual(500, roman.to_numerical("D"))
        self.assertEqual(1000, roman.to_numerical("M"))

    def test_additional_roman_numbers(self):
        roman = Romans()
        self.assertEqual(2, roman.to_numerical("II"))
        self.assertEqual(3, roman.to_numerical("III"))
        self.assertEqual(6, roman.to_numerical("VI"))
        self.assertEqual(8, roman.to_numerical("VIII"))
        self.assertEqual(51, roman.to_numerical("LI"))
        self.assertEqual(151, roman.to_numerical("CLI"))

    def test_substraction_roman_numbers(self):
        roman = Romans()
        self.assertEqual(4, roman.to_numerical("IV"))
        self.assertEqual(9, roman.to_numerical("IX"))

    def test_complex_roman_numbers(self):
        roman = Romans()
        self.assertEqual(449, roman.to_numerical("CDIL"))
        self.assertEqual(449, roman.to_numerical("CDIL"))
        self.assertEqual(444, roman.to_numerical("CDXLIV"))
        self.assertEqual(42, roman.to_numerical("XLII"))
        self.assertEqual(999, roman.to_numerical("CMXCIX"))
        self.assertEqual(899, roman.to_numerical("DCCCXCIX"))
        self.assertEqual(898, roman.to_numerical("DCCCXCVIII"))

if __name__ == '__main__':
    unittest.main()
