
ORIGINAL_IMAGE_PATH = './c1.jpeg'

SELECTION = 1

MASK_PATH = f'./test_outputs/mask_{SELECTION}.jpg'
COLORS_PATH = f'./test_outputs/colors_{SELECTION}.jpg'
COLOR_SELECTION = 3

TARGET_COLOR = (201, 165, 117) # (61, 160, 217)

# TOLERANCE = 100. # higher means more colors will change, 100 is a decent base
TOLERANCE = 200. # higher means more colors will change, 100 is a decent base
GAUSSIAN = 5.

# grab original image and the colors
import cv2
image = cv2.imread(ORIGINAL_IMAGE_PATH)
mask = cv2.imread(MASK_PATH)
colors = cv2.imread(COLORS_PATH)

selection_color = colors[5, 5+10*COLOR_SELECTION, :] # NOTE: this is reversed

import numpy as np

mean_mask = np.mean(mask, 2, dtype=np.float32)
float_mask = np.zeros_like(mean_mask)
float_mask[mean_mask > 5.] = 1.

masked_image = image * float_mask[:,:,np.newaxis]

for i in range(masked_image.shape[0]):
    for j in range(masked_image.shape[1]):
        mean = np.sum(masked_image[i, j])
        if mean == 0.: continue
        color_dist = np.linalg.norm(np.array(masked_image[i, j]) - np.array(selection_color))
        if color_dist > TOLERANCE: 
            float_mask[i, j] = 0.

avg = np.sum(image * float_mask[:,:,np.newaxis], axis=(0, 1)) / np.count_nonzero(float_mask)

from scipy.ndimage import gaussian_filter
float_mask = gaussian_filter(float_mask, sigma=GAUSSIAN)

# image0 = image * (1.-float_mask)[:,:,np.newaxis]
image0 = image
image1 = float_mask[:,:,np.newaxis] * (np.flip(np.array(TARGET_COLOR)) - selection_color)

cv2.imwrite('./test_outputs/temp.jpg', image0 + image1)



# transform = np.array((np.flip(np.array(TARGET_COLOR)) - avg) * 1.00, dtype=np.uint8)

# why isn't this transform working...

# out_image = np.clip(image + float_mask[:,:,np.newaxis] * transform, 0, 255)

# cv2.imwrite('./test_outputs/temp.jpg', out_image)

