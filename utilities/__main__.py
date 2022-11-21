import sys
import cv2
from . import indiana
from os import mkdir
import os.path


def level_partitions(level):
    base_path = "./resources/levels/"
    RAW_IMAGE_URI = base_path + "{}.png".format(level)
    print(RAW_IMAGE_URI)
    img = cv2.imread(RAW_IMAGE_URI)
    segmented_matrix = indiana.processor.from_image_to_segmented_matrix(img)

    return segmented_matrix


def store_partitions(level, partitions):

    storage_path = "./utilities/partitions/"
    if not os.path.exists(storage_path):
        mkdir(storage_path)
    storage_path = storage_path + "level_{}/".format(level)
    if not os.path.exists(storage_path):
        mkdir(storage_path)

    for i, row in enumerate(partitions):
        for j, col in enumerate(row):
            image_path = storage_path + f"{i}_{j}.png"
            print(image_path)
            cv2.imwrite(image_path, partitions[i][j])


if __name__ == "__main__":
    program = sys.argv[1]
    mode = sys.argv[2]
    level = sys.argv[3]

    if program == "part":
        if mode == "all":
            store_partitions(level, level_partitions(level))
    elif program == "start-scrapper":
        print("Starting scrapper")
        indiana.scrapper.start()
