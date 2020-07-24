import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Crystal Lake", "Disobey")

    def test_has_artist_and_title(self):
        self.assertEqual("Crystal Lake", self.song.artist)
        self.assertEqual("Disobey", self.song.title)

    def test_created_song(self):
        actual = self.song.create_song(self.song)
        self.assertEqual({"Crystal Lake": "Disobey"}, actual)