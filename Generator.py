import cv2 as cv
import numpy as np
import random

IMAGE_SIZE = 1000
PIECES = 5
COLORS = [(0, 0, 255), (0, 255, 0), (255, 0, 0),
          (255, 255, 0), (255, 255, 0), (255, 0, 255), (255, 255, 255)]
SHAPES = ["C"]
MIN_SIZE = 50
MAX_SIZE = 250
NUMBER_OF_RANDOM_SHAPES = 5


grid = np.ones((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
for i in range(1, PIECES):
    cv.line(grid, (i * IMAGE_SIZE // PIECES, 0),
            (i * IMAGE_SIZE // PIECES, IMAGE_SIZE), (255, 255, 255), 1)
    cv.line(grid, (0, i * IMAGE_SIZE // PIECES),
            (IMAGE_SIZE, i * IMAGE_SIZE // PIECES), (255, 255, 255), 1)

image = np.ones((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)

tile_size = IMAGE_SIZE / PIECES
for i in range(0, tile_size, IMAGE_SIZE + 1):
    for j in range(0, tile_size, IMAGE_SIZE + 1):
        color = COLORS[random.randrange(0, len(COLORS))]
        shape = SHAPES[random.randrange(0, len(SHAPES))]
        size = random.randint(MIN_SIZE, MAX_SIZE)
        pass

for i in range(NUMBER_OF_RANDOM_SHAPES):
    color = COLORS[i % len(COLORS)]
    shape = SHAPES[i % len(SHAPES)]
    size = random.randint(MIN_SIZE, MAX_SIZE)
    if shape == "C":
        radius = size // 2
        center = (random.randint(radius, IMAGE_SIZE - radius),
                  random.randint(radius, IMAGE_SIZE - radius))
        cv.circle(image, center, radius, color, 5)
    elif shape == "R":
        pass
    elif shape == "S":
        cv.rectangle
        pass
    elif shape == "T":
        pass

cv.imshow("Image", image)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("puzzle.png", image)
