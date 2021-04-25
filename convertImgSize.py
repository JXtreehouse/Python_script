
"""
Author: AlexZ33
功能: 用于批量转换图片大小。
"""

from PIL import Image
import os
import glob

# 修改图片文件大小
# filename：图片文件名
# outdir：修改后要保存的路径
def convertImgSize(filename, outdir, width=128, height=128):
    img = Image.open(filename)
    try:
        new = img.resize((width, height), Image.BILINEAR)
        p = os.path.basename(filename)
        print(p)
        new.save(os.path.join(outdir, os.path.basename(filename)))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 查找给定路径下图片文件，并修改其大小
    for filename in glob.glob('./img/*.png'):
        convertImgSize(filename, './trainImage128')
