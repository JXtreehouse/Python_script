

我们将学习由 John F. Canny 在 1986 年开发的流行 Canny 边缘检测算法的工作原理。通常，在 Matlab 和 OpenCV 中，我们将 Canny 边缘检测用于边缘检测中的许多流行任务，例如车道检测、素描 ，边框去除，现在我们将从头开始学习该算法的内部工作和实现。

# 学习目标
在本章中，我们将了解
- Canny边缘检测的概念
- OpenCV中的Canny函数：[cv2.Canny()](https://docs.opencv.org/3.1.0/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de)


该算法涉及的基本步骤
- 1.使用高斯滤波器进行降噪 (Noise reduction using Gaussian filter)
- 2.沿水平和垂直轴进行梯度计算
- 3.假边缘的非最大抑制
- 4.用于分离强边缘和弱边缘的双阈值
- 5. 通过滞后进行边缘跟踪


<b>1.使用高斯滤波器进行降噪 (Noise reduction using Gaussian filter)</b>

这一步在 Canny 边缘检测中至关重要。 它使用高斯滤波器从图像中去除噪声，这是因为由于边缘检测器的强度突然变化，这种噪声可以被假定为边缘。 高斯核中元素的总和为 1，因此，在对图像应用卷积之前，应该对核进行归一化。 在本教程中，我们将使用大小为 5 X 5 和 sigma = 1.4 的内核，这将模糊图像并从中去除噪声。 高斯滤波器核的方程是


# References
- Canny Edge Detection Tutorial by Bill Green, 2002.
- [opencv docs Canny Edge Detection](https://docs.opencv.org/3.1.0/da/d22/tutorial_py_canny.html)
- [implement-canny-edge-detector-in-python-using-opencv](https://www.geeksforgeeks.org/implement-canny-edge-detector-in-python-using-opencv/?ref=lbp)

# Better Example
