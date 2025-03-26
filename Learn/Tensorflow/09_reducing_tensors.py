import tensorflow as tf

tensor = tf.constant([[1, 2, 3, 4],[5, 6, 7, 8]])


#total sum
sum = tf.reduce_sum(tensor)

#average
average = tf.reduce_mean(tensor)

#max value
max_value = tf.reduce_max(tensor)

#min value
min_value = tf.reduce_min(tensor)

#print all
print("Total sum:", sum)
print("Average:", average)
print("Max value:", max_value)
print("Min value:", min_value)
