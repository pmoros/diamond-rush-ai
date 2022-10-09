import logging
from os import listdir
from random import choice
import sys
import cv2
from unittest import TestCase
from indiana.elements import classifier
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class TestClassifier(TestCase):

    def test_classify_image(self):
        test_samples_path = "./resources/samples/components/"
        test_samples = listdir(test_samples_path)
        chosen_sample = choice(test_samples)

        sample_folder = test_samples_path + chosen_sample
        sample_path = sample_folder + "/" + choice(listdir(sample_folder))
        sample = cv2.imread(sample_path)

        expected_label = chosen_sample
        actual_label = classifier.classifier.classify(sample)

        logging.getLogger().debug("Expected label: %s", expected_label)
        logging.getLogger().debug("Actual label: %s", actual_label)

        self.assertEqual(expected_label, actual_label)

    def test_get_templates_folders(self):
        res = classifier.classifier.get_templates_folders()
        self.assertIsNotNone(res)
