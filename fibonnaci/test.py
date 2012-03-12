import unittest
from unittest import TestCase
import fib

import signal

def raise_timeout(*args, **kwargs):
    raise Exception('Timeout!')


def timeout_function(func):
    def decorator(*args, **kwargs):
        signal.signal(signal.SIGALRM, raise_timeout)
        signal.alarm(1) #1 seconds
        func(*args, **kwargs)
        signal.alarm(0)

    return decorator


class FibTest(TestCase):
    def __getattribute__(self, item):
        if item.startswith('test'):
            return timeout_function(super(FibTest, self).__getattribute__(item))
        else:
            return super(FibTest, self).__getattribute__(item)

    def testFibZero(self):
        self.assertEqual(1, fib.fib(0))

    def testFibOne(self):
        self.assertEqual(1, fib.fib(1))

    def testFibTwo(self):
        self.assertEqual(2, fib.fib(2))

    def testFibThree(self):
        self.assertEqual(3, fib.fib(3))

    def testFibFour(self):
        self.assertEqual(5, fib.fib(4))

    def testFibTen(self):
        self.assertEqual(89, fib.fib(10))

    def testFib20(self):
        self.assertEqual(10946, fib.fib(20))

    def testFib30(self):
        self.assertEqual(1346269, fib.fib(30))

    def testFib35(self):
        self.assertEqual(14930352, fib.fib(35))

    def testFib45(self):
        self.assertEqual(1836311903, fib.fib(45))

    def testFib75(self):
        self.assertEqual(3416454622906707, fib.fib(75))

    def testFib150(self):
        self.assertEqual(16130531424904581415797907386349L, fib.fib(150))

    def testFib250(self):
        self.assertEqual(12776523572924732586037033894655031898659556447352249L, fib.fib(250))

    def testFib500(self):
        self.assertEqual(
            225591516161936330872512695036072072046011324913758190588638866418474627738686883405015987052796968498626L,
            fib.fib(500))

    def testFib700(self):
        self.assertEqual(
            141530751622060734789349637541611806906560581814825656065057782655897254318057662142341135314844769422903905867863877139246681886097354486547763701L
            , fib.fib(700))

if __name__ == "__main__":
    unittest.main()

