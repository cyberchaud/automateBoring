# strings and lists are similar
# strings in Python are immutable
# lists are mutable
# when a string is modified a new slice of the string is created

# for example
# the value at an index of a string can be returned myStr[1]
# however the value at that index cannot be changed
# myStr[1] = 'X' returns an error
# myList[1] = 'New value' is allowed

myStr = 'Hello'
print(list(myStr))
print(myStr[2])
print(myStr[1:3])
for letter in myStr:
    print(letter)

# How references are handled in python
spam = 42
cheese = spam
spam = 100
print(cheese, spam)

# assigning a list to a variable assigns; a reference to the list is assigned to the value
# Python assigns a value to the list
spam = [1, 2, 3, 4, 5]
print(spam)

# When assigning cheese = spam
# Python assigns a reference to the memory
cheese = spam
cheese[1] = 'Hello'

# both spam and cheese get their index 1 value changed
print(spam, cheese)

# to pass a copy of the list's values
# the library copy has a deepcopy module for this
import copy

newspam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 'bb'
print(newspam)
print(cheese)