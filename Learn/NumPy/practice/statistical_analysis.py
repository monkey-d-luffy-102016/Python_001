import numpy as np


#generate a dataset of 1000 numbers
data = np.random.normal(0, 1, 1000)

#calculate the mean
mean = np.mean(data)

# calculate the median
median = np.median(data)

print(data)
print(mean, median)