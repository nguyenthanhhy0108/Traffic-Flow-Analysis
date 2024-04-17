from flask import Flask, request, jsonify
from preprocess_data import *
from video_tracking import *
from classify_model import *

app = Flask(__name__)

# Xử lý video và trả về kết quả
@app.route("/process_video", methods=["POST"])
def process_video():
    video_file = request.files["video"]

    if video_file != None:
        print("abc")
    # Xử lý video ở đây và trả về kết quả
    result = "Video đã được xử lý và trả về kết quả."
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=8080)
