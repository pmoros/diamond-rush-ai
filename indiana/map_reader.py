import cv2
import numpy as np

from classifier import Classifier


class MapReader():
    def __init__(self):
        self.classifier = Classifier()

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
