from tensorflow.keras.models import load_model
import cv2
import numpy as np
import os
import re
from tqdm import tqdm

class classify_model:
    def __init__(self):
        self.model = load_model("weight/classify.h5")
        self.expect_shape = (240, 240)
        self.threshold = 255.0

    def predict(self, image_path):
        img = cv2.imread(image_path)
        img = cv2.resize(img, self.expect_shape)
        img = img / self.threshold
        img = np.expand_dims(img, axis=0)
        img = np.array(img)

        return self.model.predict(img)[0][0]
    
    def predict_all(self, images_folder_path):
        root = sorted(os.listdir(images_folder_path), key=lambda x: int(re.search(r'\d+', x).group()))

        result_dict = {}

        # Sử dụng tqdm để hiển thị thanh quá trình
        for path in tqdm(root, desc="Predicting"):
            img_path = os.path.join(images_folder_path, path)

            img = cv2.imread(img_path)
            img = cv2.resize(img, self.expect_shape)
            img = img / self.threshold
            img = np.expand_dims(img, axis=0)
            img = np.array(img)

            result_dict[path] = self.model.predict(img, verbose=0)[0][0]

        return result_dict