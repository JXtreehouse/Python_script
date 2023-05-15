from PIL import Image

img = Image.open(r".\img\youki-icon-150x150.png")
img = img.convert("RGBA")  # 转换获取信息
pixdata = img.load()

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y][0] > 220 and pixdata[x, y][1] > 220 and pixdata[x, y][2] > 220 and pixdata[x, y][3] > 220:
            pixdata[x, y] = (255, 255, 255, 0)
img.save(r".\img\youki-icon-150x150-nobackground.png")