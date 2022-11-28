import cv2
import numpy as np
import networkx as nx

import classifier


class MapReader():
    def __init__(self):
        self.classifier = classifier.Classifier()

    def read_map(self, map_png):
        matrix_map = self.get_game_map_from_image(map_png)
        nodes_list = self.generate_nodes_list(matrix_map)
        filtered_list = self.filter_nodes_list(nodes_list)
        self.graph = self.generate_graph(filtered_list)

        return self.graph

    def generate_graph(self, nodes_list):
        graph = nx.Graph()
        for i, node in enumerate(nodes_list):
            item_category = node.items[0].category
            data_node = self.set_node_fields(item_category)
            node_identifier = str(
                node.coordinates["x"]) + "," + str(node.coordinates["y"])
            for neighbor in node.neighbors:
                data_neighbor = self.set_node_fields(
                    neighbor.items[0].category)
                neighbor_identifier = str(
                    neighbor.coordinates["x"]) + "," + str(neighbor.coordinates["y"])
                graph.add_edge(node_identifier, neighbor_identifier,
                               weight=data_neighbor["weight"])

                data_node["coordinates"] = node.coordinates
                nx.set_node_attributes(graph, {node_identifier: data_node})
                data_neighbor["coordinates"] = neighbor.coordinates
                nx.set_node_attributes(
                    graph, {neighbor_identifier: data_neighbor})

        return graph

    def set_node_fields(self, node_item_category):
        data = {}
        data["spot"] = {}
        data["obstacle"] = {}
        data["collectable"] = {}
        data["button"] = {}
        data["exit"] = {}
        data["weight"] = classifier.CellWeight.FLOOR.value

        if node_item_category in classifier.SPOTABLES:
            data["spot"]["active"] = True
            data["spot"]["category"] = node_item_category
        elif node_item_category in classifier.OBSTACLES:
            if node_item_category in classifier.DOORS:
                data["obstacle"]["active"] = True
                data["obstacle"]["category"] = node_item_category
                data["weight"] = classifier.CellWeight.DOOR.value
            elif node_item_category in classifier.HOLES:
                data["obstacle"]["active"] = True
                data["obstacle"]["category"] = node_item_category
                data["weight"] = classifier.CellWeight.HOLE.value
            elif node_item_category in classifier.PYKES:
                data["obstacle"]["active"] = False
                data["obstacle"]["category"] = node_item_category
                data["weight"] = classifier.CellWeight.PYKE.value
        elif node_item_category in classifier.COLLECTABLES:
            data["collectable"]["active"] = True
            data["collectable"]["category"] = node_item_category
            if node_item_category == classifier.ItemCategory.DIAMOND:
                data["weight"] = classifier.CellWeight.DIAMOND.value
            else:
                data["weight"] = classifier.CellWeight.KEY.value
        elif node_item_category in classifier.BUTTONS:
            data["button"]["active"] = False
            data["button"]["category"] = node_item_category
        elif node_item_category in classifier.EXITS:
            data["exit"]["active"] = False
            data["exit"]["category"] = node_item_category

        return data

    def filter_nodes_list(self, nodes_matrix):
        """deletes nodes that are obstacles or empty
        Args:
            nodes_matrix (list(list(Node))): nodes matrix
        """
        filtered_nodes = []
        for i in range(len(nodes_matrix)):
            for j in range(len(nodes_matrix[i])):
                node = nodes_matrix[i][j]
                item = node.items[0]
                if item.category == classifier.ItemCategory.BARRIER:
                    continue
                else:
                    neighbors = self._get_matrix_neighbors(nodes_matrix, i, j)
                    node.neighbors = neighbors
                    for neighbor in node.neighbors:
                        neighbor_item = neighbor.items[0]
                        if neighbor_item.category == classifier.ItemCategory.BARRIER:
                            node.neighbors.remove(neighbor)

                    filtered_nodes.append(node)

        return filtered_nodes

    def generate_nodes_list(self, matrix_map):
        nodes_matrix = []
        for i in range(len(matrix_map)):
            row = []
            for j in range(len(matrix_map[i])):
                item = Item()
                item.category = classifier.ItemCategory(matrix_map[i][j])
                node = Node()
                node.coordinates = {"x": j, "y": i}
                node.items = [item]
                row.append(node)
            nodes_matrix.append(row)

        return nodes_matrix

    def get_game_map_from_image(self, jpeg_original):
        jpeg_as_np = np.frombuffer(jpeg_original, dtype=np.uint8)
        img = cv2.imdecode(jpeg_as_np, flags=1)
        return self.from_image_to_map(img)

    def from_image_to_map(self, img):
        map_matrix = self.classifier.classify(img)
        return map_matrix

    def save_image(self, jpeg_original, name):
        jpeg_as_np = np.frombuffer(jpeg_original, dtype=np.uint8)
        img = cv2.imdecode(jpeg_as_np, flags=1)
        cv2.imwrite(name, img)

    def _get_matrix_neighbors(self, matrix, i, j):
        neighbors = []
        # left
        neighbor = self._catch_index_error(matrix, [i-1, j])
        if neighbor is not None:
            neighbors.append(neighbor)
        # right
        neighbor = self._catch_index_error(matrix, [i+1, j])
        if neighbor is not None:
            neighbors.append(neighbor)
        # top
        neighbor = self._catch_index_error(matrix, [i, j-1])
        if neighbor is not None:
            neighbors.append(neighbor)
        # bottom
        neighbor = self._catch_index_error(matrix, [i, j+1])
        if neighbor is not None:
            neighbors.append(neighbor)

        return neighbors

    def _catch_index_error(self, my_list, my_index):
        x = my_index[0]
        y = my_index[1]
        try:
            return my_list[x][y]
        except IndexError:
            return None


class GameMap():
    def __init__(self, map_matrix, map_graph):
        self.map_matrix = map_matrix
        self.map_graph = map_graph

    def is_valid(self):
        raise NotImplementedError

    def all_diamonds_collected(self):
        raise NotImplementedError

    def can_reach_exit(self):
        raise NotImplementedError

    def can_reach_diamonds(self):
        raise NotImplementedError

    def print_map(self):
        print(self.map_matrix)


class Node():
    def __init__(self, coordinates=None, items=None, neighbors=None):
        self.coordinates = coordinates
        self.items = items
        self.neighbors = neighbors


class Item():
    def __init__(self):
        self.category = None
