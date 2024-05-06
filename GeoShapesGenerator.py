import numpy as np
import cv2 as cv


class GeoShapesGenerator:
    def __init__(self) -> None:
        self.image_size = None
        self.pieces = None
        self.colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0),
                       (255, 255, 0), (255, 255, 0), (255, 0, 255), (255, 255, 255)]
        self.shapes = ["C"]
        self.random_min_size = 50
        self.random_max_size = 250
        self.number_of_random_shapes = 20
        self.image = None

    def set_parameters(self, image_size: int, pieces: int) -> "GeoShapesGenerator":
        pass

    def generate_image(self) -> "GeoShapesGenerator":
        pass

    def get_image(self) -> np.ndarray:
        pass

    def save_image(self) -> "GeoShapesGenerator":
        pass
