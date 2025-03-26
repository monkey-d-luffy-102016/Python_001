# Sum of digits of a number
x = int(input("Enter a number: "))
sum_digits = sum(int(digit) for digit in str(x))
print("Sum of digits:", sum_digits)
