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
NUMBER_OF_RANDOM_SHAPES = 10


grid = np.ones((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
for i in range(1, PIECES):
    cv.line(grid, (i * IMAGE_SIZE // PIECES, 0),
            (i * IMAGE_SIZE // PIECES, IMAGE_SIZE), (255, 255, 255), 1)
    cv.line(grid, (0, i * IMAGE_SIZE // PIECES),
            (IMAGE_SIZE, i * IMAGE_SIZE // PIECES), (255, 255, 255), 1)
cv.imwrite("grid.png", grid)

image = np.zeros((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)

for i in range(NUMBER_OF_RANDOM_SHAPES):
    color = COLORS[i % len(COLORS)]
    shape = SHAPES[i % len(SHAPES)]
    size = random.randint(MIN_SIZE, MAX_SIZE)
    if shape == "C":
        radius = size // 2
        center = (random.randint(radius, IMAGE_SIZE - radius),
                  random.randint(radius, IMAGE_SIZE - radius)) # TODO Nech sa to robi len na hranici
        cv.circle(image, center, radius, color, 5)
    elif shape == "R":
        pass
    elif shape == "S":
        cv.rectangle
        pass
    elif shape == "T":
        pass

tile_size = IMAGE_SIZE // PIECES
for i in range(0, IMAGE_SIZE, tile_size):
    for j in range(0, IMAGE_SIZE, tile_size):
        tile = image[i:min((i + tile_size), IMAGE_SIZE),
                     j:min((j + tile_size), IMAGE_SIZE), :]
        border_size = int(tile_size * 0.1)
        tile_center = tile[border_size:-border_size,
                           border_size:-border_size, :]
        if np.any(tile):
            tile_colored = np.count_nonzero(
                cv.cvtColor(tile, cv.COLOR_BGR2GRAY))
            tile_center_colored = np.count_nonzero(
                cv.cvtColor(tile_center, cv.COLOR_BGR2GRAY))
            black_percentage = 1 - \
                ((tile_colored - tile_center_colored) / tile_size ** 2)
        else:
            black_percentage = 1
        if black_percentage > 0.8:
            color = COLORS[random.randrange(0, len(COLORS))]
            shape = SHAPES[random.randrange(0, len(SHAPES))]
            size = random.randint(MIN_SIZE, MAX_SIZE)
            x_pos = random.randint(i, (i + tile_size))
            y_pos = random.randint(j, (j + tile_size))
            if shape == "C":
                radius = size // 2
                center = (x_pos, y_pos)
                cv.circle(image, center, radius, color, 5)
            elif shape == "R":
                pass
            elif shape == "S":
                cv.rectangle
                pass
            elif shape == "T":
                pass

image_with_grid = cv.bitwise_or(image, grid)
cv.imshow("Image", image_with_grid)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("puzzle.png", image)
