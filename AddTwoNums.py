# Version 3: AddTwoNums.py
# Add Two Numbers in Python
# Author: Yujin Nie
# Using a function

# function to add two numbers
def add(a, b):
    # converting input to float and adding
    result = float(a) + float(b)
    return result

# taking user input
a = input("First Number: ")
b = input("Second Number: ")

# calling function
res = add(a, b)
print("The result is: ")
print(res)

