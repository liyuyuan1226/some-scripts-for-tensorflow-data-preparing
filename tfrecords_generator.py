# -*- coding: utf-8 -*-
import os
import tensorflow as tf 
from PIL import Image

classes = ['ANGRY', 'DISGUST', 'FEAR', 'HAPPY', 'SAD', 'SURPRISE']

def _int64_feature(value):
    if not isinstance(value,list):
        value=[value]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))


writer = tf.python_io.TFRecordWriter("./data/tfrecords/train.tfrecords")
for index, name in enumerate(classes):
    class_path = './data/native/train/' + name
    for img_name in os.listdir(class_path):
        print "processing: " + img_name + "         " + str(index)
        img_path = class_path + '/' + img_name
        img = Image.open(img_path)
        img =img.convert("RGB")

        img = img.resize((248, 248))

        print img.size  
        print img.mode  
        print img.format
        # print img.shape([2])
          
        img_raw = img.tobytes()              #将图片转化为原生bytes
        # labels=[0]
        labels=[index]
        example = tf.train.Example(
            features=tf.train.Features(
                feature={
                    "label"  : _int64_feature(labels),
                    'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw]))
                }
            )
        )
        writer.write(example.SerializeToString())  #序列化为字符串
writer.close()
print "SUCCESS"