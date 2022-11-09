import cv2
from matplotlib import pyplot as plt

# loading the image
img = cv2.imread("./img/footballteam.png")

# converting the image to grayscale
# 最初，图像是三层图像（即RGB），因此将其转换为一层图像（即灰度）。
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 加载所需的 haar-cascade XML 分类器文件
# cv2模块中的CascadeClassifier方法支持加载haar-cascade XML文件
# 要“haarcascade_frontalface_default.xml”进行人脸检测。
haar_cascade = cv2.CascadeClassifier("./img/haarcascade_frontalface_default.xml")

# Applying the face detection method on the grayscale image
#在灰度图像上应用人脸检测方法
# 这是使用 cv2::CascadeClassifier::detectMultiScale 方法完成的，该方法返回检测到的人脸的边界矩形（即 x、y、w、h）。
#  它有两个参数，即 scaleFactor 和 minNeighbors。 ScaleFactor 确定窗口大小的增加因子，最初从大小“minSize”开始，
# 并且在测试了该大小的所有窗口之后，窗口被“scaleFactor”放大，窗口大小上升到“maxSize”。
# 如果“scaleFactor”很大，（例如，2.0），步骤会更少，所以检测会更快，但我们可能会错过大小在两个测试尺度之间的对象。 （默认比例因子为 1.3）。
# “minNeighbors”的值越高，误报的数量就越少，在人脸错误检测方面的错误也就越少。 但是，也有可能遗漏一些不清楚的面部痕迹。

faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)

# Iterating through rectangles of detected faces
# 遍历检测到的人脸的矩形
# 通过 cv2 模块的 rectangle 方法通过迭代所有检测到的人脸，在检测到的人脸周围绘制矩形。

for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv2.imshow('Detected faces', img)
cv2.waitKey(0)

plt.subplot(1, 1, 1)
plt.imshow(img)
plt.show()

