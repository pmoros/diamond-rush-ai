import scrapper
import game_map
import processor


class GameEngine():
    def __init__(self):
        self.scrapper = scrapper.Scrapper()
        self.map_reader = game_map.MapReader()
        self.processor = processor.Processor()

    def launch_game(self, target, max_level=20, wait_time=0.03):
        self.scrapper.launch_game(target)
        # removes the tutorial
        self.scrapper.restart_level()

    def read_map(self):
        map_png = self.scrapper.read_map()
        self.game_map = self.map_reader.read_map(map_png)

        return self.game_map

    def restart_level(self):
        return self.scrapper.restart_level()

    def close_game(self):
        self.scrapper.close()

    def _save_image(self, name):
        return self.map_reader.save_image(self.scrapper.read_map(), name)
