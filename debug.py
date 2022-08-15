import os

import cv2
import numpy as np

"""
验证image_split NoneType是具体哪张图片有问题

发现是opencv报libpng read error:
1. 升级opencv
2. 替换有问题的图片（发现下载下来压缩包中图片有问题）

"""

if __name__ == '__main__':
    a = np.load('tools/a.npy', allow_pickle=True)
    a = a.tolist()

    img_dir = "/media/alex/80CA308ECA308288/datasets/DOTA/original/DOTA-v1.0/train/images"

    for info in a:
        path = os.path.join(img_dir, info['filename'])
        print("process: {}".format(path))
        img = cv2.imread(path)
        if img is None:
            print("!!!!!!!!!!!")
            exit(1)
