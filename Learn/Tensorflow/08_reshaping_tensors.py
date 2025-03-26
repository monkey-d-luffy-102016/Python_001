import tensorflow as tf

a = tf.constant([1,2,3,4,5,6])

# Reshape the tensor to (2, 3)
b = tf.reshape(a,(2,3))

# Print the reshaped tensor
print(b)