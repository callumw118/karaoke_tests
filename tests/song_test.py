import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
<<<<<<< HEAD
    
=======

>>>>>>> feature/rooms
    def setUp(self):
        self.song = Song("Crystal Lake", "Disobey")

    def test_has_created_song(self):
        self.assertEqual("Crystal Lake", self.song.artist)
        self.assertEqual("Disobey", self.song.title)