import unittest
from src.song import Song 

class TestSong(unittest.TestCase):
    def setUp(self):
        self.playlist = [self.song_1, self.song_2, self.song_3, self.song_4, self.song_5]
        self.song_1 = Song("All I Want")
        self.song_2 = Song("Paranoia")
        self.song_3 = Song("All Around Me")
        self.song_4 = Song("The Sound OF Silece")
        self.song_5 = Song("One Step Closer")

