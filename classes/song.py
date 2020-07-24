class Song:

    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    def create_song(self, song):
        song = {self.artist: self.title}
        return song