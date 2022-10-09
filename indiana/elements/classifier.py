# TODO: Refactor base_path
from os import listdir
import numpy as np
import cv2


class Classifier:

    def __init__(self):
        self.base_path = "./resources/templates/components"
        self.categories = self.get_templates_categories()
        self.templates_folders = self.get_templates_folders()

    def classify_segments(self, row_segments):
        """Classify segments using the classifier."""
        classified_matrix = []
        for r in row_segments:
            classified_row = []
            for segment in r:
                assigned_category = self.classify(segment)
                classified_row.append(assigned_category)
            classified_matrix.append(classified_row)

        return classified_matrix

    def classify(self, segment):
        """Classify a segment."""
        max_score = 0
        assigned_category = ""

        for category, folder in zip(self.categories, self.templates_folders):
            for template in listdir(folder):
                segment = np.array(segment)
                template_image = cv2.imread(
                    folder + "/" + template)

                img_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
                template_gray = cv2.cvtColor(segment, cv2.COLOR_BGR2GRAY)
                max_b_w = cv2.matchTemplate(
                    img_gray, template_gray, cv2.TM_CCORR_NORMED).max()

                score = max_b_w
                if score > max_score:
                    max_score = score
                    assigned_category = category

        return assigned_category

    def get_templates_folders(self):
        """Get the path to the templates."""
        return [self.base_path + "/" + folder for folder in self.categories]

    def get_templates_categories(self):
        """Get the templates."""
        components_folders = listdir(self.base_path)

        return components_folders


classifier = Classifier()
