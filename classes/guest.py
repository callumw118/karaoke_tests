class Guest:

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def create_guest(self, name):
        return self.name