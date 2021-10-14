import unittest
from typing import List
from Context6 import desicion_A, decision_B,decision_A_B,expression

class Test_Context(unittest.TestCase):
    def test_check_test1A(self):
        testA = desicion_A([10, 1, 10, 3, 4],5)
        self.assertEqual(testA.get_numbers_in_l_r(1,10),5)
        self.assertEqual(testA.get_numbers_in_l_r(2,9),2)
        self.assertEqual(testA.get_numbers_in_l_r(3,4),2)
        self.assertEqual(testA.get_numbers_in_l_r(2,2),0)
    def test_check_test2A(self):
        testA = desicion_A([1],1)
        self.assertEqual(testA.get_numbers_in_l_r(1,1),1)
        self.assertEqual(testA.get_numbers_in_l_r(-1000000000, -1000000000),0)
        self.assertEqual(testA.get_numbers_in_l_r(1000000000, 1000000000),0)
    def test_check_test3A(self):
        testA = desicion_A([-1000000000, 0, 1000000000],3)
        self.assertEqual(testA.get_numbers_in_l_r(-1000000000, -1000000000),1)
        self.assertEqual(testA.get_numbers_in_l_r(1000000000, 1000000000),1)
        self.assertEqual(testA.get_numbers_in_l_r(-1000000000, 1000000000),3)
        self.assertEqual(testA.get_numbers_in_l_r(-999999999, 999999999),1)
        self.assertEqual(testA.get_numbers_in_l_r(-999999999, 1000000000),2)
        self.assertEqual(testA.get_numbers_in_l_r(-1000000000, 999999999),2)
        self.assertEqual(testA.get_numbers_in_l_r(0, 999999999),1)
        self.assertEqual(testA.get_numbers_in_l_r(-1, 999999999),1)
        self.assertEqual(testA.get_numbers_in_l_r(1, 999999999),0)
        self.assertEqual(testA.get_numbers_in_l_r(-999999999,-1),0)
        self.assertEqual(testA.get_numbers_in_l_r(-999999999, 0),1)
        self.assertEqual(testA.get_numbers_in_l_r(-999999999, 1),1)

    def test_check_test1B(self):
        testB = decision_B([1, 2, 2, 3],4)
        self.assertEqual(testB.determine_borders(4),(0,0))
        self.assertEqual(testB.determine_borders(3),(4,4))
        self.assertEqual(testB.determine_borders(2),(2,3))
        self.assertEqual(testB.determine_borders(1),(1,1))

    def test_check_test2B(self):
        testB = decision_B([1, 2, 3, 4, 5, 6, 7, 7, 8, 9],10)
        self.assertEqual(testB.determine_borders(7),(7,8))
        self.assertEqual(testB.determine_borders(3),(3,3))
        self.assertEqual(testB.determine_borders(3),(3,3))
        self.assertEqual(testB.determine_borders(1),(1,1))
        self.assertEqual(testB.determine_borders(3),(3,3))
        self.assertEqual(testB.determine_borders(7),(7,8))
        self.assertEqual(testB.determine_borders(9),(10,10))
        self.assertEqual(testB.determine_borders(7),(7,8))
        self.assertEqual(testB.determine_borders(7),(7,8))
        self.assertEqual(testB.determine_borders(10),(0,0))

    def check_test3B(self):
        testB = None
        with open('2B 6 B 3.txt') as f:
            n = f.readline()
            lst = map(int, input().split())
            testB = self.decision_B(lst,n)
        self.assertEqual(testB.determine_borders(1),(1, 9805))
        self.assertEqual(testB.determine_borders(6),(49744, 59826))
        self.assertEqual(testB.determine_borders(3),(19863, 29802))
        self.assertEqual(testB.determine_borders(2),(9806, 19862))
        self.assertEqual(testB.determine_borders(6),(49744, 59826))
        self.assertEqual(testB.determine_borders(9),(79865, 89838))
        self.assertEqual(testB.determine_borders(2),(9806, 19862))
        self.assertEqual(testB.determine_borders(4),(29803, 39857))
        self.assertEqual(testB.determine_borders(7),(59827, 69859))
        self.assertEqual(testB.determine_borders(7),(59827, 69859))

    def test_check_test1C(self):
        testC = expression(1, -3, 3, -1)
        self.assertEqual(round(testC.root(),5), 1.00001)
    def test_check_test2C(self):
        testC = expression(-1, -6, -12, -7)
        self.assertEqual(round(testC.root(),5), -1.0)

if __name__ == '__main__':
    unittest.main().runTests()