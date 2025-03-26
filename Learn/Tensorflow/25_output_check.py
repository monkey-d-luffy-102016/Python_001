import tensorflow as tf

# Define new input data (1 sample, 2 features)
X_new = tf.constant([[3.0, 4.0]])

# Use pretrained weights & bias
W_trained = tf.constant([[1.1250229],[1250229]])  # 1 features → 1 neuron
b_trained = tf.constant([0.79341745])  # Bias

# Compute output (X * W) + b
output = tf.matmul(X_new, W_trained) + b_trained

print("Prediction:", output.numpy())