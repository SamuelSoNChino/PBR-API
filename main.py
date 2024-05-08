from flask import Flask, send_file, request
from GeoShapesGenerator import GeoShapesGenerator
import cv2 as cv
import io

app = Flask(__name__)


@app.route("/generate_image")
def generate_image():
    image_size = int(request.args.get("image_size"))
    pieces = int(request.args.get("pieces"))
    image = GeoShapesGenerator(image_size, pieces).generate_image().get_image()
    _, image_encoded = cv.imencode("image.png", image)
    image_bit_array = io.BytesIO(image_encoded)
    return send_file(image_bit_array, "image/png")


if __name__ == '__main__':
    app.run(debug=True)
