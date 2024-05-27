import numpy as np
import cv2 as cv
import random
import math


class GeoShapesGenerator:
    def __init__(self, image_size: int, pieces: int, seed: int = None) -> None:
        self.image = None
        self.image_size = image_size
        self.pieces = pieces
        self.seed = seed
        self.tile_size = image_size // pieces
        self.random_min_size = int(0.05 * image_size)
        self.random_max_size = int(0.25 * image_size)
        self.number_of_random_shapes = 0
        self.colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0),
                       (255, 255, 0), (255, 255, 0), (255, 0, 255)]
        self.shapes = ["C", "S", "T"]
        self.thickness = 5
        self.border_size = 1
        self.border_emptiness_thresh = 0.95
        self.extra_space_size = 0.1

    def set_parameters(self, image_size: int, pieces: int) -> "GeoShapesGenerator":
        self.image_size = image_size
        self.pieces = pieces
        return self

    def generate_image(self) -> "GeoShapesGenerator":
        def draw_polygon(n: int, center: tuple[int, int], radius: int, color: tuple[int, int, int]) -> None:
            angle_step = 360 // n
            angle = random.randrange(0, angle_step)
            points = []
            for _ in range(n):
                x_shift = int(radius * math.cos(math.radians(angle)))
                y_shift = int(radius * math.sin(math.radians(angle)))
                corner = [center[0] + x_shift, center[1] + y_shift]
                points.append(corner)
                angle += angle_step
            points = np.int32([points])
            cv.polylines(self.image, points, True, color, self.thickness)

        def generate_possible_edges(y: int, x: int, next_y: int, next_x: int) -> list[tuple[int, int]]:
            edges = []
            # Working with the approximated self.tile_size
            extra_space = int(self.extra_space_size * self.tile_size)
            if y != 0:  # top
                y_pos = random.randint(
                    y - extra_space, y + extra_space)
                x_pos = random.randint(x, next_x)
                edges.append((y_pos, x_pos))
            if next_y != self.image_size - 1:  # bottom
                y_pos = random.randint(
                    y + self.tile_size - extra_space, y + self.tile_size + extra_space)
                x_pos = random.randint(x, next_x)
                edges.append((y_pos, x_pos))
            if x != 0:  # left
                y_pos = random.randint(y, next_y)
                x_pos = random.randint(
                    x - extra_space, x + extra_space)
                edges.append((y_pos, x_pos))
            if next_x != self.image_size - 1:  # right
                y_pos = random.randint(y, next_y)
                x_pos = random.randint(
                    x + self.tile_size - extra_space, x + self.tile_size + extra_space)
                edges.append((y_pos, x_pos))
            return edges

        if self.seed:
            random.seed(self.seed)
        self.image = np.zeros(
            (self.image_size, self.image_size, 3), dtype=np.uint8)

        for i in range(self.number_of_random_shapes):
            color = self.colors[i % len(self.colors)]
            shape = self.shapes[i % len(self.shapes)]
            radius = random.randint(
                self.random_min_size, self.random_max_size) // 2
            center = (random.randint(radius, self.image_size - radius),
                      random.randint(radius, self.image_size - radius))
            if shape == "C":
                cv.circle(self.image, center, radius, color, self.thickness)
            elif shape == "S":
                draw_polygon(4, center, radius, color)
            elif shape == "T":
                draw_polygon(3, center, radius, color)

# The cycles go through the tiles to fill the image, so sometimes self.tile_size doesn't correspond with the real size
# It shouldn't cause any problems, since the difference is so small, but I marked the parts of the code where problems could occur
        for i in range(self.pieces):
            y = (i * self.image_size) // self.pieces
            next_y = (((i + 1) * self.image_size)) // self.pieces
            if next_y == self.image_size:
                next_y -= 1

            for j in range(self.pieces):
                x = (j * self.image_size) // self.pieces
                next_x = ((j + 1) * self.image_size) // self.pieces
                if next_x == self.image_size:
                    next_x -= 1

                tile = self.image[y:next_y, x:next_x, :]
                tile_center = tile[self.border_size:-self.border_size,
                                   self.border_size:-self.border_size, :]

                if np.any(tile):
                    if np.any(tile_center):
                        tile_center_colored = np.count_nonzero(
                            cv.cvtColor(tile_center, cv.COLOR_BGR2GRAY))
                    else:
                        tile_center_colored = 0
                    tile_colored = np.count_nonzero(
                        cv.cvtColor(tile, cv.COLOR_BGR2GRAY))
                    # Working with the approximated self.tile_size
                    border_colored = tile_colored - tile_center_colored
                    center_area = (self.tile_size - 2 * self.border_size) ** 2
                    border_area = self.tile_size ** 2 - center_area
                    black_percentage = 1 - (border_colored / border_area)
                else:
                    black_percentage = 1

                if black_percentage > self.border_emptiness_thresh:
                    color = self.colors[random.randrange(0, len(self.colors))]
                    shape = self.shapes[random.randrange(0, len(self.shapes))]
                    radius = random.randint(
                        int(self.tile_size * 0.8), int(self.tile_size)) // 2

                    edges = generate_possible_edges(y, x, next_y, next_x)
                    edge = random.choice(edges)
                    y_pos, x_pos = edge[1], edge[0]
                    center = (y_pos, x_pos)

                    if shape == "C":
                        cv.circle(self.image, center, radius,
                                  color, self.thickness)
                    elif shape == "S":
                        draw_polygon(4, center, radius, color)
                    elif shape == "T":
                        draw_polygon(3, center, radius, color)
        return self

    def get_image(self) -> np.ndarray:
        if self.image is None:
            raise ValueError("No image generated.")
        else:
            return self.image

    def save_image(self, file_name: str) -> "GeoShapesGenerator":
        if self.image is None:
            raise ValueError("No image generated.")
        else:
            cv.imwrite(file_name, self.image)
            return self


# cv.imshow("Image", GeoShapesGenerator(1000, 5).generate_image().get_image())
# cv.waitKey(0)
