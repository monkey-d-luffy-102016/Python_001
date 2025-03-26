import numpy as np

#slicing is passed like this [start:end]
# defining step [start:end:step]

# if we don't pass start it si taken as zero
# if we don't pass end it is considered legth of array
# if we don't pass step it is considered one
# 0 is 1st element , 1 is 2nd element and so on...  

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[1:5])
print(arr[:5])
print(arr[-5:-1])
print(arr[:5:2])

# return every other element from the array
print(arr[::2])

#slicing 2D arrays

arr2 = ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr2[1:2])
print(arr2[1:2])