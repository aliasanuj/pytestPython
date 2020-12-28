import demo1
import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = demo1.add(10,5)
        self.assertEqual(result,15)

