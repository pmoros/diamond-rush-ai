from unittest import TestCase
from unittest.mock import mock_open, patch
import cv2
from indiana.elements import processor


class TestProcessor(TestCase):

    def test_from_image_to_symbols_matrix(self):
        pass

    def test_from_image_to_segmented_matrix(self):
        base_path = "./resources/templates/"
        RAW_IMAGE_URI = base_path + "levels/01.png"
        img = cv2.imread(RAW_IMAGE_URI)
        segmented_matrix = processor.from_image_to_segmented_matrix(img)
        self.assertEqual(
            (len(segmented_matrix), len(segmented_matrix[0])), (13, 10))

    def test_get_map_image_matrix(self):
        pass
