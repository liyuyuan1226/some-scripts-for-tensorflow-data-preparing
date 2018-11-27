# -*- coding: utf-8 -*-
import re
import sys
import os
import shutil

def readTxtByLine(path):
    dst = []
    if os.path.exists(path):
        f = open(path,'r')
        for line in f.readlines():
            line = line.strip()
            if not len(line) or line.startswith('#'):
                continue
            dst.append(line)
        f.close
    else:
        f = open(path,'w')
        f.close
    return dst

rootpath = "./data"
if not os.path.exists(rootpath):
    os.makedirs(rootpath)

source_path1 = '/home/liyuyuan/Workspaces/python-workspace/helloworld/emotion_pic/emo'
source_path2 = '/home/liyuyuan/Workspaces/python-workspace/helloworld/emotion_pic/emotion_groundtruth.txt'
pathlist = readTxtByLine(source_path2)

for line in pathlist:
    tmp = re.split(r'[@]', line)
    src_img_path = tmp[0]
    label = tmp[1]
    dst_img_path = os.path.join(rootpath, label)

    if not os.path.exists(dst_img_path):
        os.makedirs(dst_img_path)
        shutil.copy(os.path.join(source_path1,src_img_path), dst_img_path)
    else:
        shutil.copy(os.path.join(source_path1,src_img_path), dst_img_path)