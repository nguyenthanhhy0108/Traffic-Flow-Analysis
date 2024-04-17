from video_tracking import *
from preprocess_data import *
from classify_model import *
import os
import torch

if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

# video_tracking = video_tracking()

# input_video_path = "D:\\Computer_Vision_(CS231)\\Analysis_traffic\\yolov9\\data_ext\\thanhhoa.mp4"
# output_video_folder = "D:\\Computer_Vision_(CS231)\\Analysis_traffic\\yolov9\\output_video1"
output_images_folder = "D:\\Computer_Vision_(CS231)\\Analysis_traffic\\yolov9\\output_images1"

# video_tracking.tracking(input_video_path,
#                         output_video_folder,
#                         output_images_folder)

# # ---------Result is output_images

# preprocessor = PreProcess()

# preprocessor.remove_duplicate_images(images_folder_path=output_images_folder)

# ---------Result is imgs_after_preprocess

c_model = classify_model()

result_dict = c_model.predict_all(images_folder_path=output_images_folder)

for key, val in result_dict.items():
    if val < 0.5:
        print(key)