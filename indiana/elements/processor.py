import numpy as np


def from_image_to_segmented_matrix(img):
    # crop image to remove the borders
    height, width, channels = img.shape
    cropped_img = img[int(0.15*height):, int(0.01*width)
                          :width - int(0.01*width)]

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
