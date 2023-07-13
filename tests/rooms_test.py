import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_number_1 = Room("1")
        self.room_number_2 = Room("2")
        self.room_number_3 = Room("3")

        self.guest_list = Guest[self.guest_1, self.guest_2]
        self.guest_1 = Guest("Tammy", 50, 26)
        self.guest_2 = Guest("Brandon", 60, 26)

    def test_check_in(self):
        self.room_number_1.add_guests(self.guest_1)
        self.assertEqual("Tammy", self.name)

