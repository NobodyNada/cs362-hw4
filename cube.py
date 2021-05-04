import unittest

def volume_of_cube(edge_length):
    return edge_length**3

class CubeTests(unittest.TestCase):
    def test_normal_cubes(self):
        self.assertEqual(volume_of_cube(4), 64)
        self.assertEqual(volume_of_cube(10), 1000)
        self.assertEqual(volume_of_cube(1), 1)
        self.assertEqual(volume_of_cube(0), 0)
        self.assertAlmostEqual(volume_of_cube(0.5), 0.125)
        self.assertAlmostEqual(volume_of_cube(2.5), 15.625)

    def test_negative_complex(self):
        self.assertAlmostEqual(volume_of_cube(-1), -1)
        self.assertAlmostEqual(volume_of_cube(-2.5), -15.625)
        self.assertEqual(volume_of_cube(1j), -1j)   # i^3 == -1
        self.assertEqual(volume_of_cube(2 + 3j), -46 + 9j)

    def test_type_errors(self):
        self.assertRaises(TypeError, lambda: volume_of_cube("foo"))
        self.assertRaises(TypeError, lambda: volume_of_cube(None))
