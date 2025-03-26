import numpy as np

def add(x,y):
    return x + y

add = np.frompyfunc(add,2,1)

y = add([1,2,3,4],[1,2,3,4])

print(y)