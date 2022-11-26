from scrapper import Scrapper
import classifier as classifier
from map_reader import MapReader
import numpy as np


class GameEngine():
    def __init__(self):
        self.scrapper = Scrapper()
        self.map_reader = MapReader()

    def launch_game(self, target, max_level=20, wait_time=0.03):
        self.scrapper.launch_game(target)
        # removes the tutorial
        self.scrapper.restart_level()

    def start_game(self):
        self.game_matrix = self.read_map()
        self.game_map = GameMap(self.game_matrix)
        return self.game_map

    def read_map(self):
        map_png = self.scrapper.read_map()
        map_matrix = self.map_reader.get_game_map_from_image(map_png)

        return map_matrix

    def restart_level(self):
        return self.scrapper.restart_level()

    def close_game(self):
        self.scrapper.close()

    def _save_image(self, name):
        return self.map_reader.save_image(self.scrapper.read_map(), name)


class GameMap():
    def __init__(self, map_matrix):
        self.map_matrix = map_matrix
        self.diamonds = []
        self._set_current_position()
        self._set_exit()
        self._set_diamonds()

    def is_valid(self):
        raise NotImplementedError

    def all_diamonds_collected(self):
        raise NotImplementedError

    def can_reach_exit(self):
        raise NotImplementedError

    def can_reach_diamond(self):
        raise NotImplementedError

    def print_map(self):
        print(self.map_matrix)

    def _set_diamonds(self):
        item = classifier.Item.DIAMOND
        coordinates = self._get_coordinates(item.value)
        for coordinate in coordinates:
            diamond = {}
            current_position = self._set_position(
                coordinate, item)
            diamond["picked"] = False
            diamond["position"] = current_position
            self.diamonds.append(diamond)

    def _set_current_position(self):
        item = classifier.Item.INDIANA
        item_value = item.value
        coordinates = self._get_coordinates(item_value)
        current_position = self._set_position(
            coordinates[0], item)
        self.current_position = current_position

    def _set_exit(self):
        item = classifier.Item.EXIT
        item_value = item.value
        coordinates = self._get_coordinates(item_value)
        exit_position = self._set_position(
            coordinates[0], item)
        self.exit = exit_position

    def _set_position(self, coordinates, item):
        position = {"x": coordinates[1],
                    "y": coordinates[0], "item": item}
        return position

    def _get_coordinates(self, item_value):
        coordinates = np.where(self.map_matrix == item_value)
        coordinates = tuple(zip(*coordinates))
        return coordinates
