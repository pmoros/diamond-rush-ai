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
        segmented_matrix = self.from_image_to_segmented_matrix(img)
        map_matrix = []
        for row in segmented_matrix:
            aux = []
            for cell in row:
                aux.append(self.classifier.classify(cell))
            map_matrix.append(aux)

        return map_matrix

    def from_image_to_segmented_matrix(self, img):
        # crop image to remove the borders
        height, width, channels = img.shape
        cropped_img = img[int(0.15*height):, int(0.01*width)                          :width - int(0.01*width)]

        image_array = np.array(cropped_img)
        y_height = image_array.shape[0]
        x_width = image_array.shape[1]
        xs = x_width//10  # division lines for the picture
        ys = y_height//13
        # now slice up the image (in a shape that works well with subplots)
        splits = []
        for x, i in enumerate(range(0, y_height - xs, xs)):
            aux = []
            for y, j in enumerate(range(0, x_width - ys, ys)):
                aux.append(image_array[i:i+xs, j:j+ys])
            splits.append(aux)
        return splits
