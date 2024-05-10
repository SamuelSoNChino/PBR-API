from GeoShapesGenerator import GeoShapesGenerator
from GridGenerator import GridGenerator
import cv2 as cv

tiles = 4
image_size = 1000
image = GeoShapesGenerator(image_size, tiles).generate_image().get_image()
grid = GridGenerator(image_size, tiles).generate_circle_grid().get_grid()
cv.imwrite("puzzle.png", image)
cv.imwrite("grid.png", grid)
cv.imshow("Image", grid)
cv.waitKey(0)
()
