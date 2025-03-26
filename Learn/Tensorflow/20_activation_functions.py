import tensorflow as tf
import numpy as np

X = tf.constant([-2.0,-1.0,0.0,1.0, 2.0])

#apply diffrent activation functions
relu_output = tf.nn.relu(X) # ReLU: max(0, X) turns negatives into zero and keeps positives unchanged
sigmoid_output = tf.nn.sigmoid(X)# Sigmoid: 1 / (1 + exp(-X))
tanh_output = tf.nn.tanh(X) # Tanh: (exp(X) - exp(-X)) / (exp(X) + exp(-X))[like componendo/dividendo]

print("ReLU Output:", relu_output.numpy())
print("Sigmoid Output:", sigmoid_output.numpy())
print("Tanh Output:", tanh_output.numpy())

