# Lists
# List will only return 1 value

myList = [0, 1, 2, 3, 4]
print(myList[1])

# Slices
# Slices will returns a list of values and evaluates a new list
print(myList[:2])
print(myList[2:])
print(myList[1:3])

# To delete a value from the list
# del function can be used
# del will remove the item and then shorten the list
del myList[2]
print(myList)

# print out all the values of the list
list(myList)

# List can be concated and can also be replicated.
# Many of the functions for strings can also be used for lists
print([1,2,3]*4)

# To determine if a value is in the list 'in' can be used
print(1 in myList)
print(2 in myList)
print(2 not in myList)