# Check if a number is prime
x = int(input("Enter a number: "))
is_prime = x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
print("Prime" if is_prime else "Not Prime")
