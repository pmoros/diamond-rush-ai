import cv2
import numpy as np

import classifier


class MapReader():
    def __init__(self):
        self.classifier = classifier.Classifier()

    def read_map(self, map_png):
        matrix_map = self.get_game_map_from_image(map_png)
        nodes_matrix = self.generate_nodes_matrix(matrix_map)
        filtered_matrix = self.filter_nodes_matrix(nodes_matrix)
        return filtered_matrix

    def filter_nodes_matrix(self, nodes_matrix):
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

    def generate_nodes_matrix(self, matrix_map):
        nodes_matrix = []
        for i in range(len(matrix_map)):
            row = []
            for j in range(len(matrix_map[i])):
                item = Item()
                item.category = classifier.ItemCategory(matrix_map[i][j])
                node = Node()
                node.coordinates = {"x": i, "y": j}
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
