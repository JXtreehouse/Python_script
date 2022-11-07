from PIL import Image, ImageFilter
img = Image.open("img/cat.jpg")

# Converting the image to grayscale, as Sobel Operator requires
# input image to be of mode Grayscale (L)
# 我们将使用 PIL.ImageFilter.Kernel() 创建一个拉普拉斯滤波器，然后使用该滤波器进行边缘检测。
img = img.convert("L")
# Calculating Edges using the passed laplican Kernel
final = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,
                                           -1, -1, -1, -1), 1, 0))
# Saving the Image Under the name Edge_Sample.png
final.save("EDGE_sample2.png")