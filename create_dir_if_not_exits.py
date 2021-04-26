"""
检查用户主目录中是否存在目录。 如果目录不存在，则将创建一个目录。
Checks to see if a directory exists in the users home directory. If a directory does not exist, then one will be created.
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/19
# @Author : AlexZ33
# @Site :
# @description: 检查用户主目录中是否存在目录。 如果目录不存在，则将创建一个目录。
# @File : create_dir_if_not_exits.py
# @Software: PyCharm

# imort the os module
import os

MESSAGE = 'The directory already exits'
TESTDIR = 'testdir'

try:
    #  Set the variable home by expanding the user's set home directory
    home = os.path.expanduser("~")
    # Print the location
    print(home)

    # os.path.join() for making a full path safely
    if not os.path.exists(os.path.join(home, TESTDIR)):
        # If not create the directory, inside their home directory
        os.makedirs(os.path.join(home, TESTDIR))
    else:
        print(MESSAGE)

except Exception as e:
    print(e)
