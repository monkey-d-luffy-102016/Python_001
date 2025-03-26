import tensorflow as tf

#creating tensors
a = tf.constant([1,2,3,4])
b = tf.constant([1,2,3,4])

#element wise addition
print(tf.add(a, b))

#element wise subtraction
print(tf.subtract(a, b))

#element wise multiplication
print(tf.multiply(a,b))

#element wise division
print(tf.divide(a, b))

