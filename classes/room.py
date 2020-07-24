class Room:

    def __init__(self, room_number):
        self.room_number = room_number
        self.guests_in_room = []
        self.songs_queued = {}

    def create_room(self, room_number):
        return self.room_number

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

    def add_song(self, song):
        self.songs_queued = song