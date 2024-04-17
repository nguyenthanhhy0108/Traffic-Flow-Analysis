from flask import Flask, request, jsonify
from preprocess_data import *
from video_tracking import *
from classify_model import *
import os

app = Flask(__name__)

@app.route("/process_video", methods=["POST"])
def process_video():
    video_file = request.files["video"]

    nparr = np.frombuffer(video_file.read(), np.uint8)

    temp_video_path = "temp_video.mp4"
    with open(temp_video_path, "wb") as f:
        f.write(nparr)

    root_path = os.getcwd()

    video_traker = video_tracking()

    input_video_path = "temp_video.mp4"
    output_video_folder = os.path.join(root_path, "output_video")
    output_images_folder = os.path.join(root_path, "output_images")
    video_traker.tracking(input_video_path, output_video_folder, output_images_folder)

    temp_video_path = os.path.join(root_path, "temp_video.mp4")
    os.remove(temp_video_path)

    pre_precessor = PreProcess()
    pre_precessor.remove_duplicate_images(output_images_folder)

    c_model = classify_model()

    violator = []
    total_people = len(os.listdir(output_images_folder))

    result_dict = c_model.predict_all(images_folder_path=output_images_folder)

    for key, val in result_dict.items():
        if val < 0.5:
            print(key)
            violator.append(key)

    rate = len(violator) / total_people

    result = " Thành công !"

    response = {
        "result": result,
        "rate": rate,
        "violator": violator,
        "total_people": total_people,
        "number_of_violator": len(violator)
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
