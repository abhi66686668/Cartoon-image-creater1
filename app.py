import cv2
import os
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER


def cartoonify_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Detect edges
    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    # Smooth colors
    color = cv2.bilateralFilter(img, 9, 250, 250)

    # Cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon


@app.route("/", methods=["GET", "POST"])
def index():

    image_url = None

    if request.method == "POST":

        file = request.files.get("image")

        if not file or file.filename == "":
            return render_template(
                "index.html",
                error="Please select an image."
            )

        filename = secure_filename(file.filename)

        input_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        output_filename = f"cartoon_{filename}"

        output_path = os.path.join(
            app.config["OUTPUT_FOLDER"],
            output_filename
        )

        file.save(input_path)

        cartoon = cartoonify_image(input_path)

        if cartoon is None:
            return render_template(
                "index.html",
                error="Error processing image."
            )

        cv2.imwrite(output_path, cartoon)

        image_url = f"/outputs/{output_filename}"

        return render_template(
            "index.html",
            image=image_url
        )

    return render_template("index.html")


@app.route("/outputs/<filename>")
def output_file(filename):
    return send_from_directory(
        app.config["OUTPUT_FOLDER"],
        filename
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
