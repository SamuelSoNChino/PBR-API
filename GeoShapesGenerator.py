import numpy as np
import cv2 as cv
import random


class GeoShapesGenerator:
    def __init__(self, image_size: int, pieces: int) -> None:
        self.image = None
        self.image_size = image_size
        self.pieces = pieces
        self.tile_size = image_size // pieces
        self.random_min_size = int(0.05 * image_size)
        self.random_max_size = int(0.25 * image_size)
        self.number_of_random_shapes = 20
        self.colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0),
                       (255, 255, 0), (255, 255, 0), (255, 0, 255), (255, 255, 255)]
        self.shapes = ["C"]
        self.thickness = 5
        self.border_size = 1

    def set_parameters(self, image_size: int, pieces: int) -> "GeoShapesGenerator":
        self.image_size = image_size
        self.pieces = pieces
        return self

    def generate_image(self) -> "GeoShapesGenerator":
        def draw_square() -> None:  # TODO
            pass

        def draw_traingle() -> None:  # TODO
            pass

        def generate_possible_edges(y: int, x: int) -> list[set[int]]:
            edges = []
            if y != 0:  # top
                y_pos = random.randint(
                    y - int(0.1 * self.tile_size), y + int(0.1 * self.tile_size))
                x_pos = random.randint(x, x + self.tile_size)
                edges.append((y_pos, x_pos))
            if y != self.tile_size * (self.pieces - 1):  # bottom
                y_pos = random.randint(
                    y + self.tile_size - int(0.1 * self.tile_size), y + self.tile_size + int(0.1 * self.tile_size))
                x_pos = random.randint(x, x + self.tile_size)
                edges.append((y_pos, x_pos))
            if x != 0:  # left
                y_pos = random.randint(y, y + self.tile_size)
                x_pos = random.randint(
                    x - int(0.1 * self.tile_size), x + int(0.1 * self.tile_size))
                edges.append((y_pos, x_pos))
            if x != self.tile_size * (self.pieces - 1):  # right
                y_pos = random.randint(y, y + self.tile_size)
                x_pos = random.randint(
                    x + self.tile_size - int(0.1 * self.tile_size), x + self.tile_size + int(0.1 * self.tile_size))
                edges.append((y_pos, x_pos))
            return edges

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
                draw_square(center, radius, color)
            elif shape == "T":
                draw_traingle(center, radius, color)

        for y in range(0, self.image_size, self.tile_size):
            for x in range(0, self.image_size, self.tile_size):
                tile = self.image[y:min((y + self.tile_size), self.image_size),
                                  x:min((x + self.tile_size), self.image_size), :]
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
                    black_percentage = 1 - \
                        ((tile_colored - tile_center_colored) /
                         (self.tile_size ** 2 - (self.tile_size - 2) ** 2))
                else:
                    black_percentage = 1

                if black_percentage > 0.97:
                    color = self.colors[random.randrange(0, len(self.colors))]
                    shape = self.shapes[random.randrange(0, len(self.shapes))]
                    radius = random.randint(
                        (int)(self.tile_size * 0.8), self.tile_size) // 2

                    edges = generate_possible_edges(y, x)
                    edge = random.choice(edges)
                    y_pos, x_pos = edge[1], edge[0]
                    center = (y_pos, x_pos)

                    if shape == "C":
                        cv.circle(self.image, center, radius, color, 5)
                    elif shape == "S":
                        draw_square(center, radius, color)
                    elif shape == "T":
                        draw_traingle(center, radius, color)
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


GeoShapesGenerator(1000, 5).generate_image().save_image("Peter.png")
