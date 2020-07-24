import unittest
from classes.guest import Guest

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Callum")
    
    def test_has_created_guest(self):
        self.assertEqual("Callum", self.guest.name)