# Fibonacci series up to N terms
x = int(input("Enter number of terms: "))
a, b = 0, 1
print(a, b, end=" ")
for i in range(2, x):
    c = a + b
    print(c, end=" ")
    a, b = b, c
