import numpy as np
import cv2 as cv


class GridGenerator:
    def __init__(self) -> None:
        self.image_size = None
        self.pieces = None
        self.grid = None

    def set_parameters(self, image_size: int, pieces: int) -> "GridGenerator":
        self.image_size = image_size
        self.pieces = pieces
        return self

    def generate_grid(self) -> "GridGenerator":
        if self.image_size is None or self.pieces is None:
            raise ValueError(
                "Parameters 'image_size' and 'pieces' must be set.")
        else:
            grid = np.ones(
                (self.image_size, self.image_size, 3), dtype=np.uint8)
            for i in range(1, self.pieces):
                cv.line(grid, (i * self.image_size // self.pieces, 0), (i *
                        self.image_size // self.pieces, self.image_size), (255, 255, 255), 1)
                cv.line(grid, (0, i * self.image_size // self.pieces), (self.image_size,
                        i * self.image_size // self.pieces), (255, 255, 255), 1)
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
