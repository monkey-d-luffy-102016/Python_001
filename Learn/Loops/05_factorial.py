# Factorial of a number
x = int(input("Enter a number: "))
f = 1
for i in range(1, x + 1):
    f *= i
print("Factorial:", f)
