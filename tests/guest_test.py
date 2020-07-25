import unittest
from classes.guest import Guest

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Callum", 10.00)
        self.guest_2 = Guest("James", 15.00)
    
    def test_guest_has_name(self):
        self.assertEqual("Callum", self.guest.name)

    def test_has_created_guest_callum(self):
        actual = self.guest.create_guest(self.guest)
        self.assertEqual("Callum", actual)

    def test_has_created_name_james(self):
        actual = self.guest_2.create_guest(self.guest_2)
        self.assertEqual("James", actual)

    def test_customer_has_cash(self):
        self.assertEqual(10.00, self.guest.cash)

    def test_customer_can_afford_true(self):
        self.assertTrue(self.guest.can_guest_afford(self.guest))

    def test_customer_spend_cash(self):
        entry_fee = 5.00
        self.guest.spend_cash(entry_fee)
        self.assertEqual(5.00, self.guest.cash)