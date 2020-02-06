import unittest
from employee import Employee

class TestGiveRaise(unittest.TestCase):
    """Tests default raise and custom raise"""

    def setUp(self):
        """Sets up employee"""
        self.jumoke = Employee('jumoke', 'bolanle', 120000)

    def test_default_raise(self):
        """Tests if default raise works"""
        self.jumoke.give_raise()
        self.assertEqual(self.jumoke.annual_salary, 125000)

    def test_custom_raise(self):
        self.jumoke.give_raise(2000)
        self.assertEqual(self.jumoke.annual_salary, 122000)

unittest.main()