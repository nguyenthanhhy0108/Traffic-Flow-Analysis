# Identifying People Not Wearing Helmets in a Video Using YOLOv9 and CNN

## Project Description

This project focuses on counting the number of people participating in traffic without wearing a helmet in a video. To accomplish this, we use the YOLOv9 model to detect and track humans from the video. Then, we preprocess the images of the detected individuals and use a self-trained CNN model to classify whether each person is wearing a helmet or not.

## Installation and Running the Project

1. **System Requirements**: Ensure that your computer has Python, Pip, and Git installed.

2. **Clone the Repository**: Use Git to clone the repository to your computer:

    ```
    git clone https://github.com/nguyenthanhhy0108/Traffic-Flow-Analysis.git
    ```

3. **Run the Application**: Navigate to the cloned directory, create two new folders and run the application using Python:

    You need to move into my project folder by:
    ```
    cd Traffic-Flow_Analysis
    ```

    You need to install all of nescessary libraries by:
    ```
    pip install -r requirements.txt
    ```

    Create two compulsory folders by:
    ```
    mkdir output_video
    ```
    ```
    mkdir output_images
    ```

    Run app by:
    ```
    ./run.sh
    ```
    
    * A web app will appear, you can choose a video and wait for the result.

    * All of ouput images (person image) will be placed in output_images folder.

    * An output video which is tracked person will be placed in output_video folder.

    **For an perfect experience in the next run:** Ensure that `output_video` and `output_images` folder are empty, you should remove all files in `output_video` and `output_images` folder by:

    ```
    rm -rf output_video/*
    ```

    ```
    rm -rf output_images/*
    ```

## Architecture

This is my project architecture:

![Architecture](https://raw.githubusercontent.com/nguyenthanhhy0108/Traffic-Flow-Analysis/main/readme_imgs/Yolov9.jpg)

## Example Results

There are some example result:

* Barchart plot

![Result1](https://raw.githubusercontent.com/nguyenthanhhy0108/Traffic-Flow-Analysis/main/readme_imgs/barchart.jpg)

* Piechart plot
  
![Result2](https://raw.githubusercontent.com/nguyenthanhhy0108/Traffic-Flow-Analysis/main/readme_imgs/pie.jpg)

* Some Violator

![Result3](https://raw.githubusercontent.com/nguyenthanhhy0108/Traffic-Flow-Analysis/main/readme_imgs/anh1.jpg)

![Result4](https://raw.githubusercontent.com/nguyenthanhhy0108/Traffic-Flow-Analysis/main/readme_imgs/anh2.jpg)

## More Information

Do you want to find more information about my project ?

Please read `description.pdf` on my project !

## Copyright

Showed results are extracted from [Youtube](https://www.youtube.com/watch?v=gWMDiKPI3Gg&t=39s)

- [YOLOv9](https://github.com/WongKinYiu/yolov9)
- [TensorFlow](https://www.tensorflow.org/)
- [OpenCV](https://opencv.org/)

## Author

Nguyen Thanh Hy

## License

The application is released under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

