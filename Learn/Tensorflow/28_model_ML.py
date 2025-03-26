import tensorflow as tf
import numpy as np

# Generate sample training data (y = 2x + 3 with noise)
X_train = np.random.rand(100, 1).astype(np.float32) * 10  # Random x values between 0 and 10
Y_train = 2 * X_train + 3 + np.random.normal(0, 1, (100, 1)).astype(np.float32)  # y = 2x + 3 + noise

# Initialize weights and biases
W = tf.Variable(tf.random.normal([1, 1]))  # 1x1 matrix for single input
b = tf.Variable(tf.random.normal([1]))

# Define the learning rate
learning_rate = 0.01

# Training loop
for step in range(1000):
    with tf.GradientTape() as tape:
        Y_pred = tf.matmul(X_train, W) + b  # Linear equation: Y = WX + b
        loss = tf.reduce_mean(tf.square(Y_pred - Y_train))  # Mean Squared Error (MSE)

    # Compute gradients
    gradients = tape.gradient(loss, [W, b])

    # Update parameters manually
    W.assign_sub(learning_rate * gradients[0])  # W = W - lr * gradient
    b.assign_sub(learning_rate * gradients[1])  # b = b - lr * gradient

    # Print loss every 100 steps
    if step % 100 == 0:
        print(f"Step {step}: Loss = {loss.numpy()}, W = {W.numpy()}, b = {b.numpy()}")

print("\n🎯 Final Model Parameters 🎯")
print(f"Optimized W: {W.numpy()}, Optimized b: {b.numpy()}")

# Testing the model
test_input = tf.constant([[5.0]])  # Example test input x=5
test_output = tf.matmul(test_input, W) + b
print(f"\nPrediction for x=5: {test_output.numpy()} (Expected ~13)")
