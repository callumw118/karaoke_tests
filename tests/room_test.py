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