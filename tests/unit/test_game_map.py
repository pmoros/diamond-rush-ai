import indiana.classifier as classifier
import indiana.map_reader as map_reader
import indiana.scrapper as scrapper
import indiana.game_engine as game_engine
import numpy as np
from unittest import TestCase
from unittest.mock import patch, Mock


def load_matrix(path):
    return np.loadtxt(path, dtype=int)


class GameMapTest(TestCase):
    def setUp(self):
        self.path = "resources/levels/matrices/"
        self.level = "l8.txt"
        self.path += self.level
        self.map_matrix = load_matrix(self.path)

        self.game_map = game_engine.GameMap(self.map_matrix)

    @patch("indiana.game_engine.GameEngine._get_coordinates", return_value=((2, 5), ))
    def test_set_exit(self):
        self.game_map._set_exit(self.map_matrix)

    def test_get_coordinates(self):
        item_value = classifier.Item.EXIT.value
        coordinates = self.game_map._get_coordinates(item_value)
        self.assertIsInstance(coordinates, tuple)
