import cv2
import numpy as np
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

def get_string (img_path):
    # read image from which text needs to be extracted with opencv
    # 使用 opencv 的 imread 函数读取示例图像。
    img = cv2.imread(img_path)

    # 图像预处理开始
    # 01. convert to grayscale
    img = cv2.cvColor(img, cv2.COLOR_BGR2GRAY)

    # apply dilation and erosion to remove some noise
    kernel = np.ones((1,1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel,iterations=1)
    cv2.imwrite(src_path + "removed_noise.png", img)
    # Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


