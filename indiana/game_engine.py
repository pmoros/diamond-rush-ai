from scrapper import Scrapper
from map_reader import MapReader


class GameEngine():
    def __init__(self):
        self.scrapper = Scrapper()
        self.map_reader = MapReader()

    def launch_game(self, target, max_level=20, wait_time=0.03):
        self.scrapper.launch_game(target)
        # removes the tutorial
        self.scrapper.restart_level()

    def read_map(self):
        map_png = self.scrapper.read_map()
        map_matrix = self.map_reader.get_game_map_from_image(map_png)
        self.game_map = GameMap(map_matrix)
        return self.game_map

    def restart_level(self):
        return self.scrapper.restart_level()

    def close_game(self):
        self.scrapper.close()

    def _save_image(self, name):
        return self.map_reader.save_image(self.scrapper.read_map(), name)


class GameMap():
    def __init__(self, map_matrix):
        self.map_matrix = map_matrix

    def all_diamonds_collected(self):
        raise NotImplementedError

    def can_reach_exit(self):
        raise NotImplementedError

    def can_reach_diamond(self):
        raise NotImplementedError

    def is_valid(self):
        raise NotImplementedError

    def _set_exit(self, map_matrix):
        raise NotImplementedError

    def _set_current_position(self, map_matrix):
        raise NotImplementedError
