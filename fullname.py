import unittest

def full_name(first, last):
    return first + " " + last

class NameTests(unittest.TestCase):
    def test_valid_names(self):
        self.assertEqual(full_name("Graham", "Chapman"), "Graham Chapman")
        self.assertEqual(full_name("Eric", "Idle"), "Eric Idle")
        self.assertEqual(full_name("Terry", "Gilliam"), "Terry Gilliam")
        self.assertEqual(full_name("Terry", "Jones"), "Terry Jones")

    def test_type_error(self):
        self.assertRaises(TypeError, lambda: full_name("Michael", 5))

    def test_unicode(self):
        self.assertEqual(full_name("Jøhn", "Cleése🦜"), "Jøhn Cleése🦜")
