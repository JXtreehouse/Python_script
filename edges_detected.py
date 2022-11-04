import cv2

# 缘检测是一门图像处理学科，它结合了数学方法来查找数字图像中的边缘
# 边缘检测在内部通过在数字图像上运行过filter/Kernel 来工作，该过filter/Kernel 检测图像中的不连续性,它检测图像区域中的不连续性，例如像素的亮度/强度值的明显变化。
# There are two forms of edge detection:
#
# Search Based Edge detection (First order derivative)
# Zero Crossing Based Edge detection (Second order derivative)
# 常见的边缘检测方法有：
# -Laplacian Operator or Laplacian Based Edge detection (Second order derivative)
# Canny edge detector (First order derivative)
#Prewitt operator (First order derivative)
# Sobel Operator (First order derivative)
# read the original image

#有两种方法可以在我们的图像上实现边缘检测。 在第一种方法中，我们将使用枕头库 (ImageFilter.FIND_EDGES) 中提供的内置方法进行边缘检测。 在第二个中，我们将使用 PIL.ImageFilter.Kernel() 创建一个拉普拉斯滤波器，然后使用该滤波器进行边缘检测。

from PIL import Image, ImageFilter

# Opening the image
image=Image.open(r"img/cat.jpg")
# Converting the image to grayscale, as edge detection
# requires input image to be of mode = Grayscale (L)
image = image.convert("L")
# Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
image = image.filter(ImageFilter.FIND_EDGES)
image.save(r"Edge_Sample.png")
