import tensorflow as tf

# Example true labels (actual values)
Y_true = tf.constant([[5.0, 10.0]])  # Shape (1,2)

# Example predicted values from the model
Y_pred = tf.constant([[3.0, 8.0]])  # Shape (1,2)

# Compute Mean Squared Error (MSE) loss
mse_loss = tf.reduce_mean(tf.square(Y_true - Y_pred))

print("MSE Loss:", mse_loss.numpy())
