import numpy as np
import cv2 as cv
import random
import math


class StainsGenerator:
    def __init__(self, image_size: int, pieces: int) -> None:
        self.image = None
        self.image_size = image_size
        self.pieces = pieces
        self.tile_size = image_size // pieces
        self.number_of_random_strokes = 0
        self.colors = []

    def set_parameters(self, image_size: int, pieces: int) -> "StainsGenerator":
        self.image_size = image_size
        self.pieces = pieces
        return self

    def generate_image(self) -> "StainsGenerator":  # TODO
        pass

    def get_image(self) -> np.ndarray:
        if self.image is None:
            raise ValueError("No image generated.")
        else:
            return self.image

    def save_image(self, file_name: str) -> "StainsGenerator":
        if self.image is None:
            raise ValueError("No image generated.")
        else:
            cv.imwrite(file_name, self.image)
            return self
