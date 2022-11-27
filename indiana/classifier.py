from enum import Enum
from os import listdir
import numpy as np
import cv2


class Classifier:

    def __init__(self, base_path="./resources/levels"):
        self.base_path = base_path
        self.images_path = self.base_path + "/images"
        self.matrices_path = self.base_path + "/matrices"

    def classify(self, img):
        for file_name in listdir(self.images_path):
            if file_name.endswith(".png"):
                path_to_matrix = self.matrices_path + \
                    "/" + file_name[:-4] + ".txt"
                img_template = cv2.imread(self.images_path + "/" + file_name)
                if self.compare_images(img, img_template):
                    return self._load_matrix(path_to_matrix)

    def compare_images(self, img1, img2):
        img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img_template_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(
            img_gray, img_template_gray, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        return len(loc[0]) > 0

    def _load_matrix(self, path):
        return np.loadtxt(path, dtype=int)

    def _load_image(self, path):
        return cv2.imread(path)


class ItemCategory(Enum):
    BARRIER = 1
    FLOOR = 2
    DIAMOND = 3
    PLAYER = 4
    EXIT = 5
    PYKE = 6
    KEY = 7
    KEY_DOOR = 8
    ROCK = 9
    HOLE = 10
    BUTTOM = 11
    BUTTOM_DOOR = 12
