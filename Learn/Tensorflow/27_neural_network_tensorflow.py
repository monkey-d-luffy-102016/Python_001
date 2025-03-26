import tensorflow as tf

# Define input data (2 samples, 3 features each)
X = tf.constant([[2.0, 3.0, 4.0], [1.0, 5.0, 2.0]])

# Initialize random weights (3 inputs → 2 neurons)
W = tf.Variable(tf.random.normal([3, 2]))

# Initialize random biases (for 2 neurons)
b = tf.Variable(tf.random.normal([1, 2]))

# Compute the output: (X * W) + b
output = tf.matmul(X, W) + b

# Apply activation function (ReLU)
activated_output = tf.nn.relu(output)

print("Raw Output:\n", output.numpy())
print("Activated Output (ReLU Applied):\n", activated_output.numpy())
