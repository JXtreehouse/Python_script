import cv2
import numpy as np

from matplotlib import pyplot as plt

image_first = cv2.imread('./img/cat.jpg')

# cv2.cvtColor 应用于
# 应用参数的图像输入
# 将图像转换为灰度
img = cv2.cvtColor(image_first, cv2.COLOR_BGR2GRAY)

# 应用不同的阈值输入图像的技术
# 所有大于 120 的像素值都会设置为 255
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# cv2.imshow('Binary Threshold', thresh1)
# cv2.imshow('Binary Threshold Inverted', thresh2)
# cv2.imshow('Truncated Threshold', thresh3)
# cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)


# 取消分配任何相关的内存使用
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()



plt.subplot(1, 1, 1)
plt.imshow(thresh5)
plt.show()