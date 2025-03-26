import numpy as np

arr = np.array([1, 2, 3, 4])

for x in arr:
    print(x)

arr2 = np.array([[1, 2, 3, 4],[5,6,7,8]])

for x in arr2:
    for y in x:
        print(y)

arr3 = np.array([[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]])

for x in arr3:
    for y in x:
        for z in y:
            print(z)