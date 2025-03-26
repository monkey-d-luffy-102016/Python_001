from numpy import random
import numpy as np

#shuffling arrays
arr = np.array([1, 2, 3, 4])

random.shuffle(arr)

print(arr)

#generating permutation of AI
perm = random.permutation(arr)

print(perm)