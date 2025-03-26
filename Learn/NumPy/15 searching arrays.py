import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

x = np.where(arr ==4)

print(x)

#search sorted

sorted = np.searchsorted(arr,7,side = 'right')