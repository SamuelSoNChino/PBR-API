from GeoShapesGenerator import GeoShapesGenerator
from GridGenerator import GridGenerator
import cv2 as cv

tiles = 6
image_size = 1000
image = GeoShapesGenerator(image_size, tiles).generate_image().get_image()
grid = GridGenerator(image_size, tiles).generate_grid().get_grid()
cv.imwrite("puzzle.png", image)  # TODO test v unity
cv.imwrite("grid.png", grid)
cv.imshow("Image", cv.bitwise_or(grid, image))
cv.waitKey(0)
