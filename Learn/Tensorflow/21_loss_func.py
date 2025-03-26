# Mean Squared Error (MSE) – Used for regression tasks.
# Categorical Cross-Entropy – Used for multi-class classification.
# Binary Cross-Entropy – Used for binary classification.

import tensorflow as tf

# create a tensor
x = tf.constant([1.0, 2.0, 3.0])
y = tf.constant([1.0, 2.0, 3.0])

mse_loss = tf.keras.losses.MeanSquaredError()
mse_result = mse_loss(x, y)


# Binary Cross-Entropy (for binary classification)
bce_loss = tf.keras.losses.BinaryCrossentropy()
bce_result = bce_loss(x, y)


# Print results
print("Mean Squared Error Loss:", mse_result.numpy())
print("Binary Cross-Entropy Loss:", bce_result.numpy())
