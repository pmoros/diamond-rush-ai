# TODO: Refactor base_path
from os import listdir
import numpy as np
import cv2


def classify_segments(row_segments):
    """Classify segments using the classifier."""
    classified_matrix = []
    for r in row_segments:
        classified_row = []
        for segment in r:
            assigned_category = classify(segment)
            classified_row.append(assigned_category)
        classified_matrix.append(classified_row)

    return classified_matrix


def classify(segment):
    """Classify a segment."""
    max_score = 0
    assigned_category = ""
    for category, folder in zip(get_templates_categories(), get_templates_folders()):
        for template in listdir(folder):
            segment = np.array(segment)
            template_image = cv2.imread(
                folder + "/" + template)

            methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
                       cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

            method = methods[3]
            img_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
            template_gray = cv2.cvtColor(segment, cv2.COLOR_BGR2GRAY)
            max_b_w = cv2.matchTemplate(
                img_gray, template_gray, method).max()

            score = max_b_w
            if score > max_score:
                max_score = score
                assigned_category = category

    return assigned_category


def get_templates_folders():
    """Get the path to the templates."""
    base_path = "./resources/templates/components"
    return [base_path + "/" + folder for folder in get_templates_categories()]


def get_templates_categories():
    """Get the templates."""
    base_path = "./resources/templates/components"
    components_folders = listdir(base_path)

    return components_folders
