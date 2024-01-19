import unittest
from src.recursion import *

class TestRecursion(unittest.TestCase):

    def test_grade(self):
        recursion = HomogenousRecursion((1,2,3),[RecursionCase(0,0)])
        grade = recursion.grade()
        self.assertEqual(grade,2)


if __name__ == '__main__':
    unittest.main()