from tensorflow.keras.models import load_model
import cv2
import numpy as np
import os
import re
from tqdm import tqdm
import joblib
from skimage.feature import hog
from skimage import color, exposure
import matplotlib.pyplot as plt


class classify_helmet_model:
    def __init__(self):
        self.model = joblib.load('weight/svm_classifier2.pkl')
        self.expect_shape = (240, 240)
        self.threshold = 255.0

    def extract_hog_features(self, image, visualize=False):
        if len(image.shape) == 3:
            image = color.rgb2gray(image)
        
        # Extract HOG features
        if visualize:
            features, hog_image = hog(image,
                                    orientations=9,
                                    pixels_per_cell=(8, 8),
                                    cells_per_block=(2, 2),
                                    block_norm='L2-Hys',
                                    visualize=visualize,
                                    transform_sqrt=True)
            return features, hog_image
        else:
            features = hog(image,
                        orientations=9,
                        pixels_per_cell=(8, 8),
                        cells_per_block=(2, 2),
                        block_norm='L2-Hys',
                        visualize=visualize,
                        transform_sqrt=True)
            return features

    def predict(self, image_path):
        img = cv2.imread(image_path)
        img = cv2.resize(img, self.expect_shape)
        img = img / self.threshold
        # img = np.expand_dims(img, axis=0)
        # img = np.array(img)

        img = self.extract_hog_features(img)
        img = np.array(img)

        return self.model.predict(img.reshape(1, -1))