import tensorflow as tf

tensor = tf.random.normal([3,3])

#print the tensor
print(tensor.numpy())

#get first row
print(tensor[0].numpy()) # gets the first row value

#get first two rows
print(tensor[:2].numpy()) # gets the first two rows values

#get last column value
print(tensor[:, -1].numpy()) # gets the last column value

#get last two columns values
print(tensor[:, -2].numpy()) # gets the last column value
