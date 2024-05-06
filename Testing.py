import cv2 as cv
import numpy as np
import random
 
IMAGE_SIZE = 1000
PIECES = 5
COLORS = [(0, 0, 255), (0, 255, 0), (255, 0, 0),
          (255, 255, 0), (255, 255, 0), (255, 0, 255), (255, 255, 255)]
SHAPES = ["C"]
RANDOM_MIN_SIZE = 50
RANDOM_MAX_SIZE = 250
NUMBER_OF_RANDOM_SHAPES = 20

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
    size = random.randint(RANDOM_MIN_SIZE, RANDOM_MAX_SIZE)
    if shape == "C":
        radius = size // 2
        center = (random.randint(radius, IMAGE_SIZE - radius),
                  random.randint(radius, IMAGE_SIZE - radius))
        cv.circle(image, center, radius, color, 5)
    elif shape == "S":
        cv.rectangle
        pass
    elif shape == "T":
        pass

tile_size = IMAGE_SIZE // PIECES
for y in range(0, IMAGE_SIZE, tile_size):
    for x in range(0, IMAGE_SIZE, tile_size):
        tile = image[y:min((y + tile_size), IMAGE_SIZE),
                     x:min((x + tile_size), IMAGE_SIZE), :]
        # cv.imshow("tile", tile)
        # cv.waitKey(0)
        border_size = 1
        tile_center = tile[border_size:-border_size,
                           border_size:-border_size, :]
        if np.any(tile):
            if np.any(tile_center):
                tile_center_colored = np.count_nonzero(
                    cv.cvtColor(tile_center, cv.COLOR_BGR2GRAY))
            else:
                tile_center_colored = 0
            tile_colored = np.count_nonzero(
                cv.cvtColor(tile, cv.COLOR_BGR2GRAY))
            black_percentage = 1 - \
                ((tile_colored - tile_center_colored) /
                 (tile_size ** 2 - (tile_size - 2) ** 2))
        else:
            black_percentage = 1
        image_with_grid = cv.bitwise_or(grid, image)
        # cv.imshow("Image", image_with_grid)
        # cv.waitKey(0)
        # print(black_percentage)
        if black_percentage > 0.97:
            color = COLORS[random.randrange(0, len(COLORS))]
            shape = SHAPES[random.randrange(0, len(SHAPES))]

            size = random.randint((int)(tile_size * 0.8), tile_size)

            edges = []
            if y != 0:  # top
                y_pos = random.randint(y - int(0.1 * tile_size), y + int(0.1 * tile_size))
                x_pos = random.randint(x, x + tile_size)
                edges.append((y_pos, x_pos))
            if y != tile_size * (PIECES - 1):  # bottom
                y_pos = random.randint(y + tile_size - int(0.1 * tile_size), y + tile_size + int(0.1 * tile_size))
                x_pos = random.randint(x, x + tile_size)
                edges.append((y_pos, x_pos))
            if x != 0:  # left
                y_pos = random.randint(y, y + tile_size)
                x_pos = random.randint(x - int(0.1 * tile_size), x + int(0.1 * tile_size))
                edges.append((y_pos, x_pos))
            if x != tile_size * (PIECES - 1):  # right
                y_pos = random.randint(y, y + tile_size)
                x_pos = random.randint(x + tile_size - int(0.1 * tile_size), x + tile_size + int(0.1 * tile_size))
                edges.append((y_pos, x_pos))
            edge = random.choice(edges)
            y_pos, x_pos = edge[1], edge[0]

            if shape == "C":
                radius = size // 2
                center = (y_pos, x_pos)
                cv.circle(image, center, radius, color, 5)
            elif shape == "S":
                cv.rectangle
                pass
            elif shape == "T":
                pass
        # image_with_grid = cv.bitwise_or(grid, image)
        # cv.imshow("Image", image_with_grid)
        # cv.waitKey(0)

image_with_grid = cv.bitwise_or(grid, image)
cv.imshow("Image", image_with_grid)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("puzzle.png", image)
