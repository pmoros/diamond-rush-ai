import sys
import cv2
from indiana.elements import processor
from os import mkdir
import os.path


def level_partitions(level):
    base_path = "./resources/templates/levels/"
    RAW_IMAGE_URI = base_path + "{}.png".format(level)
    print(RAW_IMAGE_URI)
    img = cv2.imread(RAW_IMAGE_URI)
    segmented_matrix = processor.from_image_to_segmented_matrix(img)

    storage_path = "./resources/partitions/"
    if not os.path.exists(storage_path):
        mkdir(storage_path)
    storage_path = storage_path + "level_{}/".format(level)
    if not os.path.exists(storage_path):
        mkdir(storage_path)

    for i, row in enumerate(segmented_matrix):
        for j, col in enumerate(row):
            image_path = storage_path + f"{i}_{j}.png"
            print(image_path)
            cv2.imwrite(image_path, segmented_matrix[i][j])


if __name__ == "__main__":
    level = sys.argv[1]

    if (level_partitions(level)):
        print("Done")
