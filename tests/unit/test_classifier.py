import cv2
from unittest import TestCase
from indiana.elements import classifier, processor


class TestClassifier(TestCase):
    def test_classify_segments_level_01(self):
        base_path = "./resources/"
        RAW_IMAGE_URI = base_path + "levels/01.png"
        img = cv2.imread(RAW_IMAGE_URI)
        rows_segments = processor.from_image_to_segmented_matrix(img)
        classified_matrix = classifier.classify_segments(rows_segments)
        self.assertIsNotNone(classified_matrix)

    def test_get_templates_folders(self):
        res = classifier.get_templates_folders()
        self.assertIsNotNone(res)
