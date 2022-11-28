import classifier
import networkx as nx


class Processor():
    def __init__(self):
        self.interactor = Interactor()
        self.resolver = Resolver()

    def get_path(self, game_map, player_node, exit_node, diamonds_nodes):
        resulting_path = []
        current_node = player_node
        started = False
        while len(diamonds_nodes) > 0:
            closest_diamond = self.get_best_diamond(
                game_map, current_node, diamonds_nodes)
            path = nx.shortest_path(
                game_map, source=current_node, target=closest_diamond, weight="weight")

            # path, game_map = self.resolve_path(game_map, path)
            if not started:
                resulting_path.extend(path)
                started = True
            else:
                resulting_path.extend(path[1:])
            current_node = closest_diamond
            diamonds_nodes.remove(closest_diamond)

        exit_path = nx.shortest_path(
            game_map, source=current_node, target=exit_node, weight="weight")

        resulting_path.extend(exit_path[1:])

        return resulting_path

    def resolve_path(self, game_map, path):
        resolved_path = self.resolver.resolve_path(game_map, path)
        game_map = self.interactor.interact(game_map, resolved_path)
        return resolved_path, game_map

    def get_best_diamond(self, game_map, player_node, diamonds_nodes):
        diamonds_nodes = self.sort_by_distance(
            game_map, player_node, diamonds_nodes)

        if len(diamonds_nodes) == 1:
            return diamonds_nodes[0]

        distance_to_first = nx.shortest_path_length(
            game_map, source=player_node, target=diamonds_nodes[0], weight="weight")
        distance_to_second = nx.shortest_path_length(
            game_map, source=player_node, target=diamonds_nodes[1], weight="weight")

        if distance_to_first == distance_to_second:
            best_diamond = diamonds_nodes[1]
        else:
            best_diamond = diamonds_nodes[0]

        return best_diamond

    def sort_by_distance(self, game_map, node, nodes):
        return sorted(nodes, key=lambda x: nx.shortest_path_length(
            game_map, source=node, target=x, weight="weight"))

    def get_closest_node(self, game_map, node, nodes):
        return min(nodes, key=lambda x: nx.shortest_path_length(
            game_map, source=node, target=x, weight="weight"))

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


class Interactor():
    def __init__(self):
        pass

    def interact(self):
        pass

    def interact_with_obstacle(self, game_map, node):
        pass

    def update_weights_in_node_edges(self, game_map, node, weight):
        sample_edges = nx.edges(game_map, [node])
        for edge in sample_edges:
            source_node = edge[0]
            destination_node = edge[1]
            game_map.remove_edge(source_node, destination_node)
            game_map.add_edge(source_node, destination_node, weight)


class Resolver():
    def __init__(self):
        pass

    def resolve_path(self, game_map, path):
        resolved_path = []
        last = 1
        for i, node in enumerate(path):
            previous_to_resolve = path[last-1:i]
            if game_map.nodes[node]["type"] == "obstacle":
                resolution = self.resolve_obstacle(
                    game_map, node)
            else:
                resolution = [node]

            result = previous_to_resolve + resolution

        for node in path:
            if game_map.node[node]["type"] == "obstacle":
                path = self.resolve_obstacle(game_map, path, node)

            resolved_path.extend(path)

        return resolved_path

    def resolve_obstacle(self, game_map, path, node):
        resolved_path = []
