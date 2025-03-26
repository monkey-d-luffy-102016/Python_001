import numpy as np

arr = np.array([1, 2, 3, 4])

x= arr.copy()

arr[0]= 5

print(arr)
print(x)