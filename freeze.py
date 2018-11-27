# freeze a .ckpt model to .pb model
# need checkpoint,  model.ckpt.meta, model.ckpt.index and model.ckpt.data-xx-of-xx(4 kinds files totally)

import os
import tensorflow as tf
import re

model_path = ''
meta_path = ''

def freeze(meta_root_path, ckpt_root_path, output_name):
    model_path = ckpt_root_path
    list = os.listdir(meta_root_path)
    for item in list:
        if len(re.findall(r'.meta$', item) ):
            meta_path = meta_root_path + item
            break

    print model_path
    print meta_path

    if len(meta_path):
        with tf.Session() as sess:
            saver = tf.train.import_meta_graph(meta_path)

            saver.restore(sess, tf.train.latest_checkpoint(model_path))
            output_node_names = [output_name]

            # Freeze the graph
            frozen_graph_def = tf.graph_util.convert_variables_to_constants(
                sess,
                sess.graph_def,
                output_node_names
            )

            # Save the frozen graph
            with open(model_path + 'frozen.pb', 'wb') as f:
                f.write(frozen_graph_def.SerializeToString())
