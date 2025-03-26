import tensorflow as tf
import numpy



#random tensor
tensor = tf.random.normal([3,3])

#print the tensor
print(tensor.numpy())

reshaped = tf.reshape(tensor, (1,9))
print(reshaped.numpy())

trsnposed = tf.transpose(tensor)
print(trsnposed.numpy())