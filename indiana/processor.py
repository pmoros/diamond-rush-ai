import classifier
import networkx as nx


class Processor():
    def __init__(self):
        pass

    def get_path(self, game_map, player_node, exit_node, diamonds_nodes):
        exit_path = nx.shortest_path(
            game_map, source=player_node, target=exit_node, weight="weight")

        return exit_path

    def get_movements(self, path):
        movements = []
        for i, node in enumerate(path):
            if i < len(path) - 1:
                movements.append(self.get_relative_position(
                    node, path[i + 1]))
        return movements

    def get_relative_position(self, n1, n2):
        x1, y1 = n1.split(",")
        x2, y2 = n2.split(",")
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if x1 == x2:
            if y1 > y2:
                return "up"
            else:
                return "down"
        else:
            if x1 > x2:
                return "left"
            else:
                return "right"
