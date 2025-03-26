import tensorflow as tf
import time

print("Current Time:", time.time())

def compute():
    a = tf.random.normal([1000, 1000])  # Generate a random 1000x1000 tensor
    b = tf.random.normal([1000, 1000])
    return tf.matmul(a, b)  # Perform matrix multiplication

start_time = time.time()
result = compute()
end_time = time.time()

print("Execution Time:", end_time - start_time)  # Corrected time calculation
