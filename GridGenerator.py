import numpy as np
import cv2 as cv


class GridGenerator:
    def __init__(self, image_size: int, pieces: int) -> None:
        self.image_size = image_size
        self.pieces = pieces
        self.grid = None
        self.circle_size = 5
        self.background_color = (255, 255, 255)
        self.grid_color = (0, 0, 0)

    def set_parameters(self, image_size: int, pieces: int) -> "GridGenerator":
        self.image_size = image_size
        self.pieces = pieces
        return self

    def generate_line_grid(self) -> "GridGenerator":
        grid = np.ndarray((self.image_size, self.image_size, 3))
        grid[:, :] = self.background_color

        for i in range(self.pieces + 1):
            pos = (i * self.image_size) // self.pieces
            if pos == self.image_size:  # So that the last line is still in the image
                pos -= 1
            cv.line(grid, (pos, 0), (pos, self.image_size), self.grid_color, 1)
            cv.line(grid, (0, pos), (self.image_size, pos), self.grid_color, 1)

        self.grid = grid
        return self

    def generate_circle_grid(self) -> "GridGenerator":
        grid = np.ndarray((self.image_size, self.image_size, 3))
        grid[:, :] = self.background_color

        radius = int(self.image_size / self.pieces / self.circle_size)
        for i in range(self.pieces):
            y = int((i * self.image_size) / self.pieces +
                    self.circle_size / 2 * radius)
            for j in range(self.pieces):
                x = int((j * self.image_size) / self.pieces +
                        self.circle_size / 2 * radius)
                cv.circle(grid, (y, x), radius, self.grid_color, 5)

        self.grid = grid
        return self

    def get_grid(self) -> np.ndarray:
        if self.grid is None:
            raise ValueError("No grid generated.")
        else:
            return self.grid

    def save_grid(self, file_name: str) -> "GridGenerator":
        if self.grid is None:
            raise ValueError("No grid generated.")
        else:
            cv.imwrite(file_name, self.grid)
            return self
