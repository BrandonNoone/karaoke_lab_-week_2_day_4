import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_list = Guest[self.guest_1, self.guest_2]
        self.guest_1 = Guest("Tammy", 50, 25)
        self.guest_2 = Guest("Brandon", 60, 26)