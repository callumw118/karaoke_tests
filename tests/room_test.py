import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 4)
        self.room_2 = Room(2, 2)

    def test_room_has_number(self):
        self.assertEqual(1, self.room.room_number)

    def test_create_room_1(self):
        self.assertEqual(1, self.room.create_room(self.room))

    def test_create_room_2(self):
        self.assertEqual(2, self.room_2.create_room(self.room_2))

    def test_empty_room(self):
        self.assertEqual(0, len(self.room.guests_in_room))

    def test_add_one_guest_to_room_callum(self):
        guest_to_add = "Callum"
        self.room.add_guest_to_room(guest_to_add)
        self.assertEqual(["Callum"], self.room.guests_in_room)

    def test_add_one_guest_to_room_james(self):
        guest_to_add = "James"
        self.room.add_guest_to_room(guest_to_add)
        self.assertEqual(["James"], self.room.guests_in_room)

    def test_add_two_guests_to_room(self):
        guests_to_add = ["Callum", "James"]
        self.room.add_guest_to_room(guests_to_add)
        self.assertEqual(["Callum", "James"], self.room.guests_in_room)

    def test_add_three_guests_to_room(self):
        guests_to_add = ["Callum", "James", "Grant"]
        self.room.add_guest_to_room(guests_to_add)
        self.assertEqual(["Callum", "James", "Grant"], self.room.guests_in_room)

    def test_checkout_guest_from_room_callum(self):
        guest_to_add = "Callum"
        self.room.add_guest_to_room(guest_to_add)
        self.room.remove_guest_from_room(guest_to_add)
        self.assertEqual([], self.room.guests_in_room)

    def test_checkout_guest_from_room_james(self):
        guest_to_add = "James"
        self.room.add_guest_to_room(guest_to_add)
        self.room.remove_guest_from_room(guest_to_add)
        self.assertEqual([], self.room.guests_in_room)

    def test_checkout_all_guests(self):
        guests_to_add = ["Callum", "James", "Grant"]
        self.room.add_guest_to_room(guests_to_add)
        self.room.remove_guest_from_room(guests_to_add)
        self.assertEqual([], self.room.guests_in_room)

    def test_room_has_no_songs_queued(self):
        self.assertEqual(0, len(self.room.songs_queued))

    def test_room_adds_song(self):
        song_to_add = [{"Crystal Lake": "Disobey"}, {"Currents", "Second Skin"}]
        self.room.add_song(song_to_add)
        self.assertEqual(song_to_add, self.room.songs_queued)

    def test_room_has_songs_queued(self):
        songs_currently_queued = [{"Crystal Lake": "Disobey"}, {"Currents", "Second Skin"}]
        self.room.add_song(songs_currently_queued)
        add_more_songs = {"Bad Omens": "Dethrone"}
        self.room.add_song(add_more_songs)
        total_in_queue = [{"Crystal Lake": "Disobey"}, {"Currents", "Second Skin"}, {"Bad Omens": "Dethrone"}]
        self.assertEqual(total_in_queue, self.room.songs_queued)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_if_room_is_full_true(self):
        self.assertTrue(self.room.is_full(self.room.capacity))

    def test_if_room_is_full_false(self):
        self.assertFalse(self.room.is_full(self.room_2.capacity))

    def test_add_to_room_when_full(self):
        guests_already_in_room = ["Callum", "James", "Grant", "Jason"]
        self.room.add_guest_to_room(guests_already_in_room)
        add_another_guest = "Daniel"
        self.room.add_guest_to_room(add_another_guest)
        self.assertEqual("Room too full", self.room.check_if_room_too_full(self.room))

    def test_add_too_room_when_space(self):
        guests_already_in_room = ["Callum", "James"]
        self.room.add_guest_to_room(guests_already_in_room)
        self.assertEqual("Space for 2 more", self.room.check_if_room_too_full(self.room))