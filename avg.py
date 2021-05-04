import unittest

def average(items):
    if len(items) == 0:
        return None
    else:
        return sum(items) / len(items)

class TestAverage(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([0]), 0)
        self.assertEqual(average([1, 2, 3]), 2)
        self.assertEqual(average([10, 20]), 15)
        self.assertAlmostEqual(average([1.5, 2.5]), 2)
        self.assertAlmostEqual(average([1, 2]), 1.5)

    def test_empty(self):
        self.assertEqual(average([]), None)

    def test_type_error(self):
        self.assertRaises(TypeError, lambda: average(["foo", "bar"]))
        self.assertRaises(TypeError, lambda: average([1, 2, None]))
