import upyun
import os


class UpYun2(upyun.UpYun):
    """
    初始化
    """

    def __init__(self, bucket, username, password, timeout=None, endpoint=None, debug=False):
        upyun.UpYun.__init__(self, bucket, username, password, timeout=None, endpoint=None)
        self.debug = debug

    def exits(self, key):
        """
        文件或者目录是否存在，　返回True 或者 False
        :param key:
        :return:
        """
        try:
            self.getinfo(key)  # 若不存在, 会抛出异常
            return True
        except:
            return False

    def isdir(self, key):
        """
        是否为目录，　返回False
        :param key:
        :return:
        """
        if self.exits(key):
            info = self.getinfo(key)
            if info['file-type'] == 'folder':
                return True
        return False

    def isfile(self, key):
        """
        是否为文件，返回False
        :param key:
        :return:
        """
        if self.exits(key):
            info = self.getinfo(key)
            if info['file-type'] == 'file':
                return True
        return False

    def tree(self, key):
        """
        类似于linux下的tree. 返回由字典组成的列表. 每个字典如下
         {'time': '1397960869', 'type': 'folder',
        'path': 'ui.totop.css', 'size': '733'}
        :param key:
        :return:
        """
        if self.isfile(key):
            info = self.getinfo(key)
            yield {
                'path': key,
                'time': info['file-date'],
                'type': 'file',
                'size': ['file-size']
            }
            return 
