class Guest:

    def __init__(self, name, cash, favourite_song):
        self.name = name
        self.cash = cash
        self.favourite_song = favourite_song

    def create_guest(self, name):
        return self.name

    def can_guest_afford(self, room):
        return self.cash >= room.entry_fee

    def spend_cash(self, entry_fee):
        self.cash-= entry_fee