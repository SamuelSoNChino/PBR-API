from flask import Flask, send_file, request
from GeoShapesGenerator import GeoShapesGenerator
from GridGenerator import GridGenerator
import cv2 as cv
import io
import random

app = Flask(__name__)

waiting_host = []


@app.route("/request_match")
def request_match():
    ip_address = str(request.args.get("ip"))
    if waiting_host:
        host_ip, seed = waiting_host.pop(0)
        return f'{seed},CLIENT,{host_ip}'
    else:
        seed = random.randint(1, 9999999)
        waiting_host.append((ip_address, seed))
        return f'{seed},HOST'


@app.route("/generate_image")
def generate_image():
    image_size = int(request.args.get("image_size"))
    number_of_tiles = int(request.args.get("number_of_tiles"))
    seed = int(request.args.get("seed"))
    image = GeoShapesGenerator(
        image_size, number_of_tiles, seed).generate_image().get_image()
    _, image_encoded = cv.imencode("image.png", image)
    image_bit_array = io.BytesIO(image_encoded)
    return send_file(image_bit_array, "image/png")


@app.route("/generate_grid")
def generate_grid():
    image_size = int(request.args.get("image_size"))
    number_of_tiles = int(request.args.get("number_of_tiles"))
    grid = GridGenerator(image_size, number_of_tiles).generate_circle_grid().get_grid()
    _, grid_encoded = cv.imencode("image.png", grid)
    grid_bit_array = io.BytesIO(grid_encoded)
    return send_file(grid_bit_array, "image/png")


if __name__ == '__main__':
    app.run(debug=True)
