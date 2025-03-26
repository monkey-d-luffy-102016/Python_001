import tensorflow as tf

# Check if GPU is available
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# Get GPU details
print(tf.config.experimental.list_physical_devices())
