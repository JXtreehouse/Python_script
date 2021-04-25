"""
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
"""

import argparse
import os


def batch_rename(dir, old_ext, new_ext):
    """
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    :param dir:
    :param old_ext:
    :param new_ext:
    :return:
    """
    files = os.listdir(dir)
    # print(files)
    for filename in os.listdir(dir):
        # Get the file extension
        # 返回的是是 tulple类型的　([文件名], [文件扩展名])
        splite_file = os.path.splitext(filename)
        print(splite_file)
        # Unpack tuple element
        root_name, file_ext = splite_file
        # Start of the logic to check the file extensions, if old_ext = file_ext
        if old_ext == file_ext:
            # Returns changed name of the file with new extention
            newfile = root_name + new_ext

            #  Write the file
            os.rename(
                os.path.join(dir, filename),
                os.path.join(dir, newfile)
            )

            print("rename is done!")
            print(os.listdir(dir))

def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('dir', metavar='DIR', type=str, nargs=1, help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser


def main():
    """
    This will be called if the script is directly invoked
    :return:
    """
    # adding command line argument
    parser = get_parser()
    args = vars(parser.parse_args())

    # Set the variable `dir` with the first argument passed
    dir = args['dir'][0]
    # Set the variable old_ext with the second argument passed
    old_ext = args['old_ext'][0]
    if old_ext and old_ext[0] != '.':
        old_ext = '.' + old_ext
    # Set the variable new_ext with the third argument passed
    new_ext = args['new_ext'][0]
    if new_ext and new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(dir, old_ext, new_ext)


if __name__ == '__main__':
    main()
