# Check if a number is an Armstrong number
x = int(input("Enter a number: "))
num_digits = len(str(x))
sum_of_powers = sum(int(digit) ** num_digits for digit in str(x))
print("Armstrong number" if sum_of_powers == x else "Not an Armstrong number")
