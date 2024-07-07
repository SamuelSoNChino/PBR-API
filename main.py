from flask import Flask, send_file, request
from GeoShapesGenerator import GeoShapesGenerator
from GridGenerator import GridGenerator
import cv2 as cv
import io

app = Flask(__name__)

relay_join_codes = {}
empty_spots = {}


@app.route("/test_connection")
def test_connection():
    return "OK"


@app.route("/request_match")
def request_match():
    number_of_players = str(request.args.get("number_of_players"))
    if int(number_of_players) < 2 or int(number_of_players) > 10:
        return "INVALID PLAYER COUNT"
    if number_of_players in relay_join_codes.keys():
        relay_join_code = relay_join_codes[number_of_players]
        empty_spots[number_of_players] -= 1
        if empty_spots[number_of_players] == 0:
            relay_join_codes.pop(number_of_players)
        return f'CLIENT,{relay_join_code}'
    else:
        return f'HOST'


@app.route("/upload_relay_join_code")
def upload_relay_join_code():
    relay_join_code = str(request.args.get("relay_join_code"))
    number_of_players = str(request.args.get("number_of_players"))
    relay_join_codes[number_of_players] = relay_join_code
    empty_spots[number_of_players] = int(number_of_players) - 1
    return "OK"


@app.route("/request_join_code_removal")
def request_join_code_removal():
    relay_join_code = str(request.args.get("relay_join_code"))
    number_of_players = relay_join_codes.keys()[list(
        relay_join_codes.values()).index(relay_join_code)]
    relay_join_codes.pop(number_of_players)
    empty_spots.pop(number_of_players)
    return "OK"


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
