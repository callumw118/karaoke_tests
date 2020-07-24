class Room:

    def __init__(self, room_number):
        self.room_number = room_number
        self.number_of_guests = []
        self.songs_queued = {}

    def create_room(self, room_number):
        return self.room_number

    def add_guest_to_room(self, guests_to_add):
        if isinstance(guests_to_add, list):
            for guest in guests_to_add:
                self.number_of_guests.append(guest)
        else:
            self.number_of_guests.append(guests_to_add)