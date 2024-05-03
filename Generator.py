import cv2 as cv
import numpy as np
import random

IMAGE_SIZE = 1000
PIECES = 6
COLORS = [(0, 0, 255), (0, 255, 0), (255, 0, 0),
          (255, 255, 0), (255, 255, 0), (255, 0, 255), (255, 255, 255)]
SHAPES = ["C"]
MIN_SIZE = 50
MAX_SIZE = 250
THRESHOLD1 = 10
THRESHOLD2 = 1000

grid = np.ones((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
for i in range(1, PIECES):
    cv.line(grid, (i * IMAGE_SIZE // PIECES, 0),
            (i * IMAGE_SIZE // PIECES, IMAGE_SIZE), (255, 255, 255), 1)
    cv.line(grid, (0, i * IMAGE_SIZE // PIECES),
            (IMAGE_SIZE, i * IMAGE_SIZE // PIECES), (255, 255, 255), 1)

image = np.ones((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
for i in range(10):
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

grid_edges = cv.Canny(grid, THRESHOLD1, THRESHOLD2)
grid_contours, _ = cv.findContours(
    grid_edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
untouched_tile_size = max([cv.contourArea(grid_contour)
                          for grid_contour in grid_contours])

mixed_image = cv.bitwise_or(grid, image)
mixed_image = cv.cvtColor(mixed_image, cv.COLOR_BGR2GRAY)
cv.imshow("Image", mixed_image)
cv.waitKey(0)

edges = cv.Canny(mixed_image, THRESHOLD1, THRESHOLD2)
cv.imshow("Image", edges)
cv.waitKey(0)

contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(grid, contours, -1, (255, 255, 255), 1)
cv.imshow("Image", grid)
cv.waitKey(0)

untouched = []
for contour in contours:
    if cv.contourArea(contour) == untouched_tile_size:  # TODO Stvorec
        untouched.append(contour)

print(len(untouched))
cv.imshow("Image", image)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("puzzle.png", image)
