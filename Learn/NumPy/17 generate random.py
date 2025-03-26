from numpy import random

x = random.randint(100)
x = random.rand()

print(x)

#generate random array
x = random.randint(100, size = (5))
x = random.randint(100, size = (3,5))

print(x)