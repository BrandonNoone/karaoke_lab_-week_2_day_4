class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.guest_list = []

    def add_guests(self, guest):
        self.guest_list.append(guest)