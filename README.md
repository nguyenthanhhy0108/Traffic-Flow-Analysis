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
    pip install -r requirements.txt`
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

![Architecture](https://private-user-images.githubusercontent.com/121184152/323162621-e2a1bb78-7572-4afc-a1c6-2ac938a7ab8a.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTMzNDYyNzQsIm5iZiI6MTcxMzM0NTk3NCwicGF0aCI6Ii8xMjExODQxNTIvMzIzMTYyNjIxLWUyYTFiYjc4LTc1NzItNGFmYy1hMWM2LTJhYzkzOGE3YWI4YS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQxN1QwOTI2MTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02ZWY5ZmFlNTIzNmMzYjlmZDUyMzg3NzY3MTIzZDg3MGFkOTdmYWIzZTc1MDY4NWRhNTc4MTU3MGFmYmVjMmM1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.cUljKTpdkGfz3abjnAc_yW6smcqLzNycOrs94sfBneA)

## Example Results

There are some example result:

* Barchart plot

![Result1](https://private-user-images.githubusercontent.com/121184152/323162611-b049da74-1996-44b5-97bb-50f42b6671f3.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTMzNDYyNzQsIm5iZiI6MTcxMzM0NTk3NCwicGF0aCI6Ii8xMjExODQxNTIvMzIzMTYyNjExLWIwNDlkYTc0LTE5OTYtNDRiNS05N2JiLTUwZjQyYjY2NzFmMy5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQxN1QwOTI2MTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04YWZiMjY0MWE3OTU4Nzg1NDg2OTMwNGJlZDIzNDdlMmE2OGJlZjZlMmFhZjdmMjNhOWY5OTE0NzhhMmY1ZTY1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.zqqYdutn0J5rPpxnheOs1sxTGroTncZlzSfaM5Cg7Ng)

* Piechart plot
  
![Result2](https://private-user-images.githubusercontent.com/121184152/323162617-d37462c9-f596-487e-833e-cf1250e0c0ea.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTMzNDYyNzQsIm5iZiI6MTcxMzM0NTk3NCwicGF0aCI6Ii8xMjExODQxNTIvMzIzMTYyNjE3LWQzNzQ2MmM5LWY1OTYtNDg3ZS04MzNlLWNmMTI1MGUwYzBlYS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQxN1QwOTI2MTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NDQ2NTNiOGQ1ZWYwZmZhMjE2ODY4YzRkZjM1MGYxM2U2NWRmMjU3MDcxMmRmMDY5OWRlYjQyZWVmMzM3Nzg0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.kQ11QMyi8xC7HHN6Hz_WCHPk7CsuxlFGNYeOmHU3Ms8)

* Some Violator

![Result3](https://private-user-images.githubusercontent.com/121184152/323162577-88cb640f-b95e-4784-9763-916c05acf252.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTMzNDYyNzQsIm5iZiI6MTcxMzM0NTk3NCwicGF0aCI6Ii8xMjExODQxNTIvMzIzMTYyNTc3LTg4Y2I2NDBmLWI5NWUtNDc4NC05NzYzLTkxNmMwNWFjZjI1Mi5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQxN1QwOTI2MTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03ZDNiNmEyMTcwNmY0ZGY4ZGZhZTYxODJmOGQxNTNkNTViMWViNTk5ZGJlMzMxMTBjYjZlOWFjYjVlYzYzNTk5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.dc5aBg3rfm4Rl8ICJIfRJ-7lTq9a6b8eUNop2FxJ1GA)

![Result4](https://private-user-images.githubusercontent.com/121184152/323162605-1bc9db8d-07e2-4ac2-8ad9-610f16920f94.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTMzNDYyNzQsIm5iZiI6MTcxMzM0NTk3NCwicGF0aCI6Ii8xMjExODQxNTIvMzIzMTYyNjA1LTFiYzlkYjhkLTA3ZTItNGFjMi04YWQ5LTYxMGYxNjkyMGY5NC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQxN1QwOTI2MTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iN2MzODk4ZTg4NTZkZjRlNDdlMjlhNjM3NzU2NmM5MDA0OWI1Zjk0YTk4OWU2MjJmOTQ5YWUwMjdiZWY2NTRmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.GKxVZ4RknViP6NpE5oQFUZBwOunFJyq8NlQy3PM3-qw)

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

