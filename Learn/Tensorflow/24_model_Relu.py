import tensorflow as tf

# Define input data (single feature)
X = tf.constant([[1.0], [2.0], [3.0], [4.0]], dtype=tf.float32)
Y = tf.constant([[2.0], [4.0], [6.0], [8.0]], dtype=tf.float32)  # Target values (Y = 2X)

# Initialize weights & biases for a simple neural network
W = tf.Variable(tf.random.normal([1, 1]))  # Weight for 1 neuron
b = tf.Variable(tf.random.normal([1]))  # Bias

# Learning rate
learning_rate = 0.01

# Training loop
for step in range(100):  # Train for 100 steps
    with tf.GradientTape() as tape:
        # Forward propagation (Simple Linear Model: Y_pred = X * W + b)
        Y_pred = tf.nn.relu(tf.matmul(X, W) + b)
        # Compute loss (Mean Squared Error)
        loss = tf.reduce_mean(tf.square(Y - Y_pred))
    
    # Compute gradients
    gradients = tape.gradient(loss, [W, b])
    
    # Apply gradients using manual gradient descent
    W.assign_sub(learning_rate * gradients[0])
    b.assign_sub(learning_rate * gradients[1])
    
    if step % 10 == 0:  # Print every 10 steps
        print(f"Step {step}: Loss = {loss.numpy()}, W = {W.numpy()}, b = {b.numpy()}")

# Final trained values
print("\nFinal Model Parameters:")
print(f"Weight: {W.numpy()}, Bias: {b.numpy()}")
