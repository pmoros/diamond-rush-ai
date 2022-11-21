import logging
from unittest import TestCase
from unittest.mock import mock_open, patch

import cv2
import numpy as np

from indiana.classifiers import processor

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class TestProcessor(TestCase):
    def setUp(self):
        try:
            file_handler = logging.FileHandler('./logs/test_processor.log')
            logger.addHandler(file_handler)
        except Exception as e:
            logger.error(e)

    def test_from_image_to_map(self):
        # tested up to level 5
        base_path = "./resources/"
        level = "05"
        RAW_IMAGE_URI = base_path + "levels/{}.png".format(level)
        img = cv2.imread(RAW_IMAGE_URI)
        map_matrix = processor.from_image_to_map(img)

        # logging the map matrix
        logger.debug("Level is %s", level)
        for r in map_matrix:
            logger.debug(r)

        self.assertEqual(len(map_matrix), 13)
        self.assertEqual(len(map_matrix[0]), 10)

    def test_from_image_to_segmented_matrix(self):
        base_path = "./resources/"
        RAW_IMAGE_URI = base_path + "levels/02.png"
        img = cv2.imread(RAW_IMAGE_URI)
        segmented_matrix = processor.from_image_to_segmented_matrix(img)
        self.assertEqual(
            (len(segmented_matrix), len(segmented_matrix[0])), (13, 10))
