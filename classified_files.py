# https://blog.csdn.net/as604049322/article/details/119619221?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163706411016780274197422%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=163706411016780274197422&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v2~rank_v29-1-119619221.pc_v2_rank_blog_default&utm_term=%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB&spm=1018.2226.3001.4450

import os
from pathlib import Path
import shutil

# 需要把路径替换成你的文件夹所在路径，当把这个代码文件放在要处理的文件夹外一层时，可以使用下面的相对路径写法

path = os.getcwd()
print(path)
inputPath = path + '/data/originfiles'

# 定义分类字典：
file_dict = {

    '图片': ["jpeg", 'jpg', 'png', 'gif', 'webp', "bmp", "bpg", "svg", "heif", "psd"],
    '视频': ['rmvb', 'mp4', 'avi', 'mkv', 'flv', "wmv", "mov", "mpg", "mpeg", "3gp"],
    "音频": ['m4a', 'aac', 'ogg', 'oga', 'mp3', 'wma', "wav"],
    "电子书": ['pdf', "epub", "mobi", "azw3", "chm", "txt"],
    "数据与表格": ['xls', 'xlsx', "xlsm", 'csv', 'json', 'xml'],
    "文档": ['doc', 'docx', 'ppt', 'pptx', 'md', ".txt"],
    "思维导图": ["emmx", "mmap", "xmind"],
    '程序脚本': ['py', 'java', 'html', 'sql', 'r', 'css', 'cpp', 'c', 'js', 'go'],
    '压缩文件': ["tar", "gz", "rz", "7z", "dmg", "rar", "xar", "zip", "iso"],
    '可执行程序': ['exe', 'bat', 'sys', 'com'],
    '字体文件': ['eot', 'otf', 'fon', 'font', 'ttf', 'ttc', 'woff', 'woff2']
}


# 定义一个函数用于获取一个文件属于的类型：
def get_file_type(filename):
    """
    传入文件名，读取file_dict配置, 然后根据后缀判断文件类型
    :param filename:
    :return:
    """
    # print(file_dict.items())
    for file_type, suffixs in file_dict.items():
        for suffix in suffixs:
            #  Python lstrip()方法 https://www.runoob.com/python/att-string-lstrip.html
            if filename.endswith("." + suffix.lstrip(".")):
                return file_type
    return "未知类型"


# test get_file_type
d = get_file_type(inputPath + '1.jpeg')
print(d)


# 使用pathlib库保存移动信息：

def mkdirAndGeyChange(path) -> object:
    path = Path(path)
    result = []
    # 将文件以glob二进制读取
    for file in path.glob("*"):
        if file.is_dir():
            continue

        src_path = file.absolute()
        dest_dir = get_file_type(file.name)
        dest_path = path / dest_dir / file.name
        dest_dir = dest_path.parent

        if not dest_dir.exists():
            dest_dir.mkdir()
        result.append((src_path, dest_path))
    return result


# test

file_changes = mkdirAndGeyChange(inputPath)
print(file_changes)


# 需要改名时：

for src_path, dest_path in file_changes:
    src_path.rename(dest_path)

# 还原回来:

for src_path, dest_path in file_changes:
    dest_path.rename(src_path)