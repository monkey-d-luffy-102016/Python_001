x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

gcd = 1  # Start with 1 since 1 divides all numbers
for i in range(1, min(x, y) + 1):  # Loop up to the smaller number
    if x % i == 0 and y % i == 0:  # Check if 'i' divides both
        gcd = i  # Update the greatest common divisor

print("GCD:", gcd)
