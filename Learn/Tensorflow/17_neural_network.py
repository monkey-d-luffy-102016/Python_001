import tensorflow as tf
import numpy as np

# Define input data (batch_size=1, features=3)
X = tf.constant([[1.0, 2.0, 3.0]])  # Reshaped to (1,3)

# Initialize random weights (3 inputs → 2 neurons)
W = tf.Variable(tf.random.normal([3, 2]))  # Corrected shape

# Initialize random biases (1 per neuron)
b = tf.Variable(tf.random.normal([1, 2]))

# Compute the output of the layer: Y = XW + b
output = tf.matmul(X, W) + b

print("Output of the neural network layer:")
print(output.numpy())

