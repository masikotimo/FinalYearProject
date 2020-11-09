import unittest
import sys

import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result=calc.add(10,2)
        self.assertEqual(result,12)
        self.assertNotEqual(result,16)
