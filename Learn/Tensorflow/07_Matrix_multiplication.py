import tensorflow as tf

#create 2d tensors
a =tf.constant([[1,2],[4,5]])
b =tf.constant([[7,8],[9,10]])

#matrix multiplication
dot_product = tf.matmul(a,b)
print(dot_product)