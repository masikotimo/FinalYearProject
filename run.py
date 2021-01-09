import tensorflow as tf
import sys
import os

#suppress TF log-info messages - remove to display TF logs 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'





def predictTraffic(img):
    image_path = img

    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    label_lines = [line.rstrip() for line 
                    in tf.gfile.GFile("./pretrained_labels.txt")]

    with tf.gfile.FastGFile("./pretrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        predictions = sess.run(softmax_tensor, \
                {'DecodeJpeg/contents:0': image_data})
        
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        
        for node_id in top_k:
            congestion_type = label_lines[node_id]
            score = predictions[0][node_id]
            if (score >=0.5):
                print('%s (score = %.5f)' % (congestion_type, score))
                return congestion_type

