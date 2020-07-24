import unittest
from classes.guest import Guest

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Callum")
        self.guest_2 = Guest("James")
    
    def test_guest_has_name(self):
        self.assertEqual("Callum", self.guest.name)

    def test_has_created_guest_callum(self):
        actual = self.guest.create_guest(self.guest)
        self.assertEqual("Callum", actual)

    def test_has_created_name_james(self):
        actual = self.guest_2.create_guest(self.guest_2)
        self.assertEqual("James", actual)