import tensorflow as tf
import numpy as np

scalar = tf.constant(1)
vector = tf.constant([1, 2, 3])
matrix = tf.constant([[1, 2], [3, 4]])
tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

r_scalar = tf.rank(scalar)
r_vector = tf.rank(vector)
r_matrix = tf.rank(matrix)
r_tensor_3d = tf.rank(tensor_3d)

print("Rank of scalar:", r_scalar.numpy())
print("Rank of vector:", r_vector.numpy())
print("Rank of matrix:", r_matrix.numpy())
print("Rank of 3D tensor:", r_tensor_3d.numpy())    
