# -*- coding: utf-8 -*-

from unittest import TestCase
from bowling import Game

class GameTestCase(TestCase):
    def setUp(self):
        super(GameTestCase, self).setUp()
        self.game = Game()

    def tearDown(self):
        super(GameTestCase, self).tearDown()

    def testAllGutter(self):
        self.rollMany(20, 0)
        self.assertEqual(0, self.game.score())

    def testAllOne(self):
        self.rollMany(20, 1)
        self.assertEqual(20, self.game.score())

    def testOneSpare(self):
        self.rollSpare()
        self.game.roll(3)
        self.rollMany(17, 0)
        self.assertEqual(16, self.game.score())

    def testAllStrikeButLastFrame(self):
        self.rollMany(9, 10)
        self.rollMany(2, 0)
        self.assertEquals(240, self.game.score())

    def testAllStrikeButLastThrow(self):
        self.rollMany(11, 10)
        self.game.roll(9)
        self.assertEquals(299, self.game.score())

    def testAllStrikeButFirstFrameIsSpare(self):
        self.rollSpare()
        self.rollMany(11, 10)
        self.assertEquals(290, self.game.score())

    def testAllStrikeButFirstFrameIsNotSpare(self):
        self.game.roll(5)
        self.game.roll(4)
        self.rollMany(11, 10)
        self.assertEquals(279, self.game.score())

    def testTwoSpares(self):
        self.rollSpare()
        self.rollSpare()
        self.game.roll(3)
        self.game.roll(3)
        self.rollMany(14, 0)
        self.assertEqual(15 + 13 + 6, self.game.score())

    def testOneStrike(self):
        self.rollStrike()
        self.game.roll(3)
        self.game.roll(4)
        self.rollMany(16, 0)
        self.assertEqual(24, self.game.score())

    def testPerfectGame(self):
        self.rollMany(12, 10)
        self.assertEqual(300, self.game.score())

    def rollStrike(self):
        self.game.roll(10)

    def rollSpare(self):
        self.game.roll(5)
        self.game.roll(5) #spare

    def rollMany(self, n, pins):
        map(lambda x: self.game.roll(pins=pins), range(0, n))