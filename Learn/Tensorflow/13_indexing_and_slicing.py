import tensorflow as tf

# Disable GPU
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(tensor[1, 2].numpy())  
