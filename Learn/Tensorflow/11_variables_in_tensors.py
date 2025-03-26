import tensorflow as tf
import numpy

var = tf.Variable(5)

#print var
print(var.numpy())

#update the value
var.assign(10)
print(var.numpy())

#increment the variable
var.assign_add(5)
print(var.numpy())