x = input("enter a word")

#check for vowels

vowels = 0

for i in range(len(x)):
    if x[i] in ['a','e','i','o','u']:
        vowels = vowels + 1
        i = i + 1

print (vowels)