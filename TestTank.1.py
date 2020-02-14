#!/usr/bin/python


import unittest


class TestTank(unittest.TestCase):

    def testTankHasImage(self):
        tank = Tank()
        assert tank.image != None, "tank image is None"

if __name__=="__main__":
    unittest.main()
