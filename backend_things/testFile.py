print("East is Beast!!!\n")

a = 7
b = int(input("enter a number: "))
c = b + a
print("The \tnumber + 7 is: " + str(c))

import calendar
print(calendar.monthrange(2023, 12))

start = 1
end = 20

# Define the spacing you want
spacing = 2

# Generate a sequence of numbers
numbers = list(range(start, end + 1))

# Use the print function with the sep parameter
print(*numbers, sep=" " * spacing)
