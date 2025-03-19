# List to Store and Show Students' Name
# Author: Yujin Nie
# Using function, for loop and list

# a list to store and show student name
studentNames = ["Lisa", "liam", "Leo", "Larry", "Linda"]
lastName = "Evans"

# first function and for loop to show students full name
def studList(firstName, lastName):
    fullName = []
    for firstName in studentNames:
        fullName.append(firstName + " " + lastName)
    return fullName
    
# second function to add student name to the list
def addToList(newName):
    studentNames.append(newName)
    return studentNames

# calling the first function
fullName = studList(studentNames, lastName)
print("The full names are: ", fullName) 

# Input new name
newName = input("Enter your name: ")

# calling the second function
addName = addToList(newName)
res = studList(addName, lastName)
print("After add new student name, the full names are: ", res)
