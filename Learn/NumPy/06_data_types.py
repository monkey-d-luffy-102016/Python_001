# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array(['apple', 'orange', 'banana', 'guava' ])

print(arr.dtype)
print(arr1.dtype)