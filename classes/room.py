class Room:

    def __init__(self, room_number):
        self.room_number = room_number
        self.guests_in_room = []
        self.songs_queued = []
        self._capacity = 4

    def create_room(self, room_number):
        return self.room_number

    # Rather than having two functions to add one guest to the room or adding a list of guests to the room
    # this function combines the two by first checking if there is a list of guests being passed in
    def add_guest_to_room(self, guests_to_add):
        if isinstance(guests_to_add, list):
            for guest in guests_to_add:
                self.guests_in_room.append(guest)
        else:
            self.guests_in_room.append(guests_to_add)

    def remove_guest_from_room(self, guests_to_remove):
        if isinstance(guests_to_remove, list):
            for guest in guests_to_remove:
                self.guests_in_room.remove(guest)
        else:
            self.guests_in_room.remove(guests_to_remove)

    def add_song(self, songs):
        if isinstance(songs, list):
            for song in songs:
                self.songs_queued.append(song)
        else:
            self.songs_queued.append(songs)