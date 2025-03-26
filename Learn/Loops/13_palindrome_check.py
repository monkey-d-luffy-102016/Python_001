# Check if a number is palindrome
x = input("Enter a number: ")
print("Palindrome" if x == x[::-1] else "Not a palindrome")
