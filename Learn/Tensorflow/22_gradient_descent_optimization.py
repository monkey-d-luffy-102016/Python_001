import tensorflow as tf
import numpy as np

def loss_function(x):
    return (x - 3) ** 2  # Function to minimize

# Initialize the variable
x = tf.Variable(0.0)

# Define optimizer
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

for step in range(50):
    with tf.GradientTape() as tape:
        loss = loss_function(x)

    # Compute gradients
    gradients = tape.gradient(loss, [x])  # Fix: Use [x] instead of x

    # Apply gradients using optimizer
    optimizer.apply_gradients(zip(gradients, [x]))

    if step % 10 == 0:
        print(f"Step: {step}, Loss: {loss.numpy()}, x: {x.numpy()}")

print("Final optimized output:", x.numpy())
