import tensorflow as tf
import numpy as np

# Define input data (batch_size=1, features=3)
X = tf.constant([[1.0, 2.0, 3.0]])  # Shape (1,3)

# Initialize random weights (3 inputs → 2 neurons)
W = tf.Variable(tf.random.normal([3, 2]))  # Shape (3,2)

# Initialize random biases (1 per neuron)
b = tf.Variable(tf.random.normal([1, 2]))  # Shape (1,2)

# Compute output before activation: Y = XW + b
linear_output = tf.matmul(X, W) + b

# Apply ReLU activation function
activated_output = tf.nn.relu(linear_output)  # ReLU(XW + b)

print("Activated Output:")
print(activated_output.numpy())
