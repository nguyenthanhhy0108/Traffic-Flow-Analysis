import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import cv2
import os
import re
from tqdm import tqdm
import shutil

class PreProcess:
    def __init__(self):
        self.mobilenet_model = models.mobilenet_v2(pretrained=True)

        self.mobilenet_model.eval()

        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def mobilenet_predict(self, img_path):
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img)
        input_tensor = self.preprocess(img_pil)

        with torch.no_grad():
            output_features = self.mobilenet_model(input_tensor.unsqueeze(0))

        return output_features

    def extract_histogram_features(self, image_path):
        image = cv2.imread(image_path)

        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        hist_hue = cv2.calcHist([hsv_image], [0], None, [256], [0, 256])
        hist_saturation = cv2.calcHist([hsv_image], [1], None, [256], [0, 256])
        hist_value = cv2.calcHist([hsv_image], [2], None, [256], [0, 256])

        feature_vector = np.concatenate((hist_hue.ravel(), hist_saturation.ravel(), hist_value.ravel()))

        normalized_feature_vector = feature_vector / np.sum(feature_vector)

        return normalized_feature_vector
    

    def euclidean_distance(self, vector1, vector2):
        distance = np.linalg.norm(vector1 - vector2)
        return distance
    

    def remove_duplicate_images(self, images_folder_path):
        index = 0
        root = sorted(os.listdir(images_folder_path), key=lambda x: int(re.search(r'\d+', x).group()))
        lst_img = sorted(os.listdir(images_folder_path), key=lambda x: int(re.search(r'\d+', x).group()))
        length = len(lst_img)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        for i in range(len(lst_img) - 1):
            try:
                img_path1 = lst_img[i]
            except IndexError:
                break
            total = len(lst_img)
            index += 1
            completion_percentage = index * 100 / total
            print(f"\rProgress: {completion_percentage:.2f}%", end='', flush=True)
            img1_path = os.path.join(images_folder_path, img_path1)
            count = 0
            try:
                for j in range(i + 1, len(lst_img)):
                    img_path2 = lst_img[j]
                    count += 1
                    if count == 6:
                        break
                    img2_path = os.path.join(images_folder_path, img_path2)
                    
                    vector_1 = torch.tensor(self.mobilenet_predict(img1_path)).to(device)
                    vector_2 = torch.tensor(self.mobilenet_predict(img2_path)).to(device)

                    dis1 = self.euclidean_distance(vector_1, vector_2)

                    hist_vector_1 = torch.tensor(self.extract_histogram_features(img1_path)).to(device)
                    hist_vector_2 = torch.tensor(self.extract_histogram_features(img2_path)).to(device)

                    dis2 = self.euclidean_distance(hist_vector_1, hist_vector_2) * 100

                    distance = dis1 + dis2

                    if distance <= 60:
                        lst_img.remove(img_path2)
            except IndexError:
                break

        for path in root:
            if path not in lst_img:
                rm_path = os.path.join(images_folder_path, path)
                os.remove(rm_path)
                continue
