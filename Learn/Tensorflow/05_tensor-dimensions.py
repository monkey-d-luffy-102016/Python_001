import tensorflow as tf

tensor = tf.constant([[1,2,3,4],[5,6,7,8]])

shape = tf.shape(tensor)

dim1 = shape[0]
dim2 = shape[1]

print("Dimension 1:", dim1) 
print("Dimension 2:", dim2)