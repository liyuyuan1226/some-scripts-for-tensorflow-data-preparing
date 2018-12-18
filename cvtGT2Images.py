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

def main(facesdk_path):
    target_path        = facesdk_path + 'pose/data/native/train'
    source_images_path = facesdk_path + 'datasets/pose/images/'
    gt_path            = facesdk_path + 'datasets/pose/pose_groundtruth.txt'
    
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        
    pathlist = readTxtByLine(gt_path)

    for line in pathlist:
        tmp = re.split(r'[,]', line)
        src_img_path = tmp[0]
        label_yaw = tmp[1]
        label_pitch = tmp[2]
        label_roll = tmp[3]

        # if not os.path.exists(dst_img_path):
        #     os.makedirs(dst_img_path)
        target_file = target_path + '/' + src_img_path
        print 'Processing: ' + target_file
        # symbolic link(soft link) should use absolute path
        try:
            os.symlink(source_images_path + src_img_path, target_file)
        except:
            print target_file + ' exists'

if __name__ == '__main__':
    main('/home/liyuyuan/Workspaces/python-workspace/FaceSDK/')
    print "SUCCESS"
