import unittest
from employee import Employee

class TestGiveRaise(unittest.TestCase):
    """Tests default raise and custom raise"""

    def setUp(self):
        """Tests give_raise() on an employee"""
        self.jumoke = Employee('jumoke', 'bolanle', 120000)