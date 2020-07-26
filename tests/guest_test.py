import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Callum", 10.00, {"Crystal Lake": "Disobey"})
        self.guest_2 = Guest("James", 4.00, {"Currents": "Second Skin"})

        self.room = Room(1, 4, 5.00)
    
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
        self.assertTrue(self.guest.can_guest_afford(self.room))

    def test_customer_can_afford_false(self):
        self.assertFalse(self.guest_2.can_guest_afford(self.room))

    def test_customer_spend_cash(self):
        self.guest.spend_cash(self.room.entry_fee)
        self.assertEqual(5.00, self.guest.cash)

    def test_customer_has_favourite_song(self):
        self.assertEqual({"Crystal Lake": "Disobey"}, self.guest.favourite_song)