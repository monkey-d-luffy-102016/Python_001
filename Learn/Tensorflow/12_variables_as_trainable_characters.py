import tensorflow as tf
import numpy 

#create tensor with random value
tensor = tf.Variable(tf.random.normal([3,3])) # 3 x 3 matrix with random value

#print the random tensor
print(tensor.numpy())

