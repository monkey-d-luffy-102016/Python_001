import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# concatenate arrays

concated_array = np.concatenate((arr1, arr2))

print(concated_array)

#joining using stack functions
# We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.

arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([4,5,6,7])

arr_stack = np.stack((arr3, arr4),axis = 1)

#stacking along rows
arr_hstack = np.hstack((arr3, arr4))

print(arr_hstack)

#stacking along columns
arr_vstack = np.vstack((arr3, arr4))
print(arr_vstack)

#stacking along(depth)
arr_dstack = np.dstack((arr3, arr4))
print(arr_dstack)