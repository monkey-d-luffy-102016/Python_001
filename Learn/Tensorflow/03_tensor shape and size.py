import tensorflow as tf

tensor = tf.constant([[1,2,3], [4,5,6]])

shape = tf.shape(tensor)

size = tf.size(tensor)

print("shape", shape)

print("size", size)