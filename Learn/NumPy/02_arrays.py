import numpy as np

# a 1D array
arr1 = np.array([1,2,3,4,5,6])
print (arr1)

#A 2D array
arr2 = np.array([
    [1,2,3],
    [4,5,6]
])
print (arr2)

#checking shape,size adn dimensions
print ("Shape:", arr2.shape)
print ("Size:", arr2.size)
print ("Dimensions:", arr2.ndim)