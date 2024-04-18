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

![Architecture](https://private-user-images.githubusercontent.com/121184152/323162621-e2a1bb78-7572-4afc-a1c6-2ac938a7ab8a.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTM0NjA1ODIsIm5iZiI6MTcxMzQ2MDI4MiwicGF0aCI6Ii8xMjExODQxNTIvMzIzMTYyNjIxLWUyYTFiYjc4LTc1NzItNGFmYy1hMWM2LTJhYzkzOGE3YWI4YS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQxOFQxNzExMjJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hMWZmYmRiMjAyMWQ5ZThhNDAxMWY1NzFiNjliNWRiMDdkNTQxYTgwMWNjNWNmZTUyNTAxZjkyYTA0YzY2OWNmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.UsYncdJO30jb8bFV3jylCX19sWyaff3aaF7cd6sQ7-s)

## Example Results

There are some example result:

* Barchart plot

![Result1](https://private-user-images.githubusercontent.com/121184152/323162611-b049da74-1996-44b5-97bb-50f42b6671f3.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTM0NjA1ODIsIm5iZiI6MTcxMzQ2MDI4MiwicGF0aCI6Ii8xMjExODQxNTIvMzIzMTYyNjExLWIwNDlkYTc0LTE5OTYtNDRiNS05N2JiLTUwZjQyYjY2NzFmMy5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQxOFQxNzExMjJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wZjM1ZGM3YjNjNjMxMzlkMWFlMDhmMjA0YzEyNjg1ZmU2MDVkOWMyZWJmMGEyNDhhMGE2NmNjNzNkNzUxMjg3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Atbrexb64-nQgPHoZgCR5J4TwOgMHvsu9yvOotQ2zVw)

* Piechart plot
  
![Result2](https://private-user-images.githubusercontent.com/121184152/323162617-d37462c9-f596-487e-833e-cf1250e0c0ea.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTM0NjA1ODIsIm5iZiI6MTcxMzQ2MDI4MiwicGF0aCI6Ii8xMjExODQxNTIvMzIzMTYyNjE3LWQzNzQ2MmM5LWY1OTYtNDg3ZS04MzNlLWNmMTI1MGUwYzBlYS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQxOFQxNzExMjJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kM2I2YWQ5ODU4YWViZTY0NzhhYWNlZjRhYzRiZTFiZGQ4NmI3NWM4MTljN2EzODY2Njk3YTNmZjc4NDhmY2FmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Zaqf0w7H7oNlJfWbCCM0kUUe_6fuPG4btfSqGoYetAM)

* Some Violator

![Result3](https://private-user-images.githubusercontent.com/121184152/323162577-88cb640f-b95e-4784-9763-916c05acf252.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTM0NjA1ODIsIm5iZiI6MTcxMzQ2MDI4MiwicGF0aCI6Ii8xMjExODQxNTIvMzIzMTYyNTc3LTg4Y2I2NDBmLWI5NWUtNDc4NC05NzYzLTkxNmMwNWFjZjI1Mi5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQxOFQxNzExMjJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kYTY4N2MxYmU0MjI5ZmRiNzU2MzdkYzViNGU4Njc1Mjg1YWVlMGE3MzEwNGVjYzJkYWJlZjJmZjFhZjQwOGFkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.YFaGnVFT-7x8sIj9aihTT0QZde3YI4MfMG3eigWsUVc)

![Result4](https://private-user-images.githubusercontent.com/121184152/323162605-1bc9db8d-07e2-4ac2-8ad9-610f16920f94.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTM0NjA1ODIsIm5iZiI6MTcxMzQ2MDI4MiwicGF0aCI6Ii8xMjExODQxNTIvMzIzMTYyNjA1LTFiYzlkYjhkLTA3ZTItNGFjMi04YWQ5LTYxMGYxNjkyMGY5NC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQxOFQxNzExMjJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZmVhZjJiY2M2YzJhNGE4OTI5ZGFhNzA2OWE0Njg3ODMwZmJkMGNmZjNkNzZjMmMwYTk4YTAzNTJiMjdhNjU3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.wPQTNv9X5MADINt-y0mDqJkx_RFhrrn_AGnpZItH7P4)

## More Information

Do you want to find more information about my project ?

Please read `description.pdf` on my project !

## Copyright

Showed results are extracted from [Youtube](https://www.youtube.com/watch?v=gWMDiKPI3Gg&t=39s)

- [YOLOv9](https://github.com/WongKinYiu/yolov9)
- [TensorFlow](https://www.tensorflow.org/)
- [OpenCV](https://opencv.org/)

## Author

Nguyen Thanh hy

## License

The application is released under the MIT License. See the [LICENSE](LICENSE) file for details.

