import tensorflow as tf

import sys

total = 0
counter = 0
arr = []
maxVal = 0

file = open("/star_wars/zData/data.txt", "r")
for line in file:
    if line == '\n' or line == "":
        break
    else:
        arr.append(float(line.rstrip("\n")))
        total += arr[counter]
        counter += 1

# change this as you see fit

image_path = sys.argv[1]



# Read in the image_data

image_data = tf.gfile.FastGFile(image_path, 'rb').read()



# Loads label file, strips off carriage return

label_lines = [line.rstrip() for line 

                   in tf.gfile.GFile("/star_wars/retrained_labels.txt")]



# Unpersists graph from file

with tf.gfile.FastGFile("/star_wars/retrained_graph.pb", 'rb') as f:

    graph_def = tf.GraphDef()

    graph_def.ParseFromString(f.read())

    _ = tf.import_graph_def(graph_def, name='')



with tf.Session() as sess:

    # Feed the image_data as input to the graph and get first prediction

    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    

    predictions = sess.run(softmax_tensor, \

             {'DecodeJpeg/contents:0': image_data})

    

    # Sort to show labels of first prediction in order of confidence

    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    
    print
    for node_id in top_k:

        human_string = label_lines[node_id]

        score = predictions[0][node_id]

        if human_string == "malachite":
            maxVal = score

        print('%s : (score = %.5f)' % (human_string, score))
    print

    
    arr.append(maxVal)
    total += maxVal
    counter += 1
    file.close()

    file = open("/star_wars/zData/data.txt", "w")

    for i in range(counter):
        file.write("%0.5f" %(arr[i]))
        file.write("\n")

    file.write("\n")
    avg = total/counter

    file.write("avg: %0.5f" %(avg))