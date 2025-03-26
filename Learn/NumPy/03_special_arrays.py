import numpy as np

#a zero array
zero_array = np.zeros((3,3))

print(zero_array)

# a array of ones
ones_array = np.ones((3,3))

print(ones_array)

#arrat of random values
random_array = np.random.random((3,3))

print(random_array)

#array of specific values
full_arr = np.full((2, 3), 7)  # 2x3 array filled with 7
print(full_arr)

#sequnces of numbers
seq_arr = np.arange(1, 10, 2)  # Start from 1, go up to 10 (exclusive), step by 2
print(seq_arr)

#evenly spaced array
spaced_arr = np.linspace(0, 10, 5)  # Start from 0, go up to 10, with 5 equally spaced points
print(spaced_arr)