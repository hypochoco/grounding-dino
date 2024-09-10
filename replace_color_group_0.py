
# run grounding dino and split the selections.
# for each selection, kmeans the colors.

DEVICE = 'mps'

SOURCE_IMAGE_PATH = "./c1.jpeg"  # example: "./test_folder/test.jpg"
OUTPUT_DIR = "./test_outputs/"
CLASSES = ["Walls", "Floor"]            # example: ["Toys", "Furniture"]

from grounded import run_split
run_split(DEVICE=DEVICE, SOURCE_IMAGE_PATH=SOURCE_IMAGE_PATH, OUTPUT_DIR=OUTPUT_DIR, CLASSES=CLASSES)

