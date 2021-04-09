先来看下原图与最终效果图
![](../img/鬼刀.png)
![](../img/效果图.png)

# 首先安装Pillow库
终端运行命令：
```buildoutcfg
pip3 install pillow
```

# 实现思路
![](../img/实现思路.png)


# 代码实现

```python
"""
1、导入依赖库
"""

from PIL import Image

"""
2、填充图片为正方形
"""


def fill_image(image):
    width, height = image.size

    # 选取长和宽中较大值作为新图片的边长
    new_image_length = width if width > height else height

    # 生成新图片[白底]，底色可配置其他颜色
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')

    # 将之前的图片input image 粘贴在新图上，居中
    if width > height:  # 原图宽大于高，则填充图片的竖直维度  #(x,y)二元组表示粘贴上图相对下图的起始位置,是个坐标点
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))

    return new_image


"""
3、切割图片
"""


def cut_image(image):
    width, height = image.size

    item_width = int(width / 3)  # 因为朋友圈一行放3张图

    box_list = []

    for i in range(0, 3):

        for j in range(0, 3):
            box = (
            j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)  # (left, top, right, bottom)

            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]

    return image_list


"""
4、保存图片
"""


def save_images(image_list):
    index = 1

    for image in image_list:
        image.save('./img/postWechat/' + str(index) + '.png', 'PNG')

        index += 1


"""
5、 使用示例
"""

if __name__ == '__main__':
    file_path = "img/鬼刀.png"  # 把目标图片 input image 放到代码所处的文件夹里

    image = Image.open(file_path)
    image = fill_image(image)

    image_list = cut_image(image)

    save_images(image_list)

```

# 源码下载地址
