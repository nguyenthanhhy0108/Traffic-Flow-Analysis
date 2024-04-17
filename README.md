# Identifying People Not Wearing Helmets in a Video Using YOLOv9 and CNN

## Project Description

This project focuses on counting the number of people participating in traffic without wearing a helmet in a video. To accomplish this, we use the YOLOv9 model to detect and track humans from the video. Then, we preprocess the images of the detected individuals and use a self-trained CNN model to classify whether each person is wearing a helmet or not.

## Installation and Running the Project

1. **System Requirements**: Ensure that your computer has Python, Pip, and Git installed.

2. **Clone the Repository**: Use Git to clone the repository to your computer:

    ```
    git clone https://github.com/nguyenthanhhy0108/Traffic-Flow-Analysis.git
    ```

## Usage

1. Place the video to be analyzed in the `videos` directory.
2. Run the `detect_people.py` script to detect and track humans from the video: `python detect_people.py --video_path videos/video_name.mp4`
3. Run the `preprocess_images.py` script to preprocess the images of the detected individuals: `python preprocess_images.py`
4. Run the `train_model.py` script to train the CNN model: `python train_model.py`
5. Run the `classify_people.py` script to classify whether each person is wearing a helmet or not: `python classify_people.py`
6. The final results will be saved in the `output` directory.

## Resources

- [YOLOv9](https://github.com/ultralytics/yolov5)
- [Object Detection and Tracking Project](https://github.com/ultralytics/yolov5)
- [TensorFlow](https://www.tensorflow.org/)
- [OpenCV](https://opencv.org/)

## Author

John Doe

## License

This project is distributed under the [MIT License](https://opensource.org/licenses/MIT).

