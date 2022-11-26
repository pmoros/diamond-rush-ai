import scrapper


class GameEngine():
    def __init__(self):
        self.scrapper = scrapper.Scrapper()

    def launch_game(self, target, max_level=20, wait_time=0.03):
        self.scrapper.launch_game(target)

    def read_map(self):
        return self.scrapper.read_map()

    def restart_level(self):
        return self.scrapper.restart_level()

    def close_game(self):
        self.scrapper.close()


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
