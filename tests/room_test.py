import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1)
        self.room_2 = Room(2)

    def test_room_has_number(self):
        self.assertEqual(1, self.room.room_number)

    def test_create_room_1(self):
        self.assertEqual(1, self.room.create_room(self.room))

    def test_create_room_2(self):
        self.assertEqual(2, self.room_2.create_room(self.room_2))

    def test_empty_room(self):
        self.assertEqual(0, len(self.room.number_of_guests))

    def test_add_one_guest_to_room_callum(self):
        guest_to_add = "Callum"
        self.room.add_guest_to_room(guest_to_add)
        self.assertEqual(["Callum"], self.room.number_of_guests)

    def test_add_one_guest_to_room_james(self):
        guest_to_add = "James"
        self.room.add_guest_to_room(guest_to_add)
        self.assertEqual(["James"], self.room.number_of_guests)