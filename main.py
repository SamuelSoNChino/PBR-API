import threading
from flask import Flask, send_file, request
from GeoShapesGenerator import GeoShapesGenerator
from GridGenerator import GridGenerator
import cv2 as cv
import io
import random

app = Flask(__name__)

available_host = []
relay_code_uploaded_event = threading.Event()


@app.route("/request_match")
def request_match():
    relay_code_uploaded_event.wait()
    if available_host:
        relay_join_code, seed = available_host.pop(0)
        return f'CLIENT,{seed},{relay_join_code}'
    else:
        relay_code_uploaded_event.clear()
        seed = random.randint(1, 9999999)
        return f'HOST,{seed}'


@app.route("/upload_relay_join_code")
def upload_relay_join_code():
    relay_join_code = str(request.args.get("relay_join_code"))
    seed = int(request.args.get("seed"))
    available_host.append((relay_join_code, seed))
    relay_code_uploaded_event.set()
    return "OK"


@app.route("/request_new_seed")
def request_new_seed():
    seed = random.randint(1, 9999999)
    return str(seed)


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
    grid = GridGenerator(
        image_size, number_of_tiles).generate_circle_grid().get_grid()
    _, grid_encoded = cv.imencode("image.png", grid)
    grid_bit_array = io.BytesIO(grid_encoded)
    return send_file(grid_bit_array, "image/png")


if __name__ == '__main__':
    app.run(debug=True)
