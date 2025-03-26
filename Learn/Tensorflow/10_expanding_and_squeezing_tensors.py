import tensorflow as tf

tensor = tf.constant([[1, 2, 3],[4, 5, 6]])

#expand the tensor
expanded_tensor = tf.expand_dims(tensor, axis=1)

#squeeze the tensor
squeezed_tensor = tf.squeeze(expanded_tensor)

print("Expanded tensor:\n", expanded_tensor)
print("\nSqueezed tensor:\n", squeezed_tensor)
