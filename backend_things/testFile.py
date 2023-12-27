print("East is Beast!!!\n")

a = 7
b = int(input("enter a number: "))
c = b + a
print("The \tnumber + 7 is: " + str(c))

print("hello")
print("omg")

print("Hello World")
# Example 1: Iterating over a list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Example 2: Iterating over a string
word = "Python"
for char in word:
    print(char)

# Example: Using enumerate to get both index and element
words = ["apple", "banana", "cherry"]
for index, word in enumerate(words):
    print(f"Index: {index}, Word: {word}")

for x in range(5):
    print(x)

import calendar
print(calendar.monthrange(2023, 12))