import os
import re
dir="C:/Users/DX/Documents/Lightshot/"


def renameScreenshots():  # count should change depending
    count = 99  # count should change depending " 0, 9, 99"
    for filename in os.listdir(dir):
        src = dir + filename
        regex = re.compile(rf'Screenshot_...\.png')  # this should also change depending "., .., ..."
        if regex.search(src):
            count += 1
            dst = "Screenshot_" + str(count) + ".png"
            dst = dir + dst
            os.rename(src, dst)


renameScreenshots()