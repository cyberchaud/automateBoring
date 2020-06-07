# This program says hello and asks for my name and my age
# Python executes each instructions in order from top to bottom

# Comments are ignored by Python
# Blank lines are also ignored
# Python files should end in a blank line

# Python functions are like mini-programs inside the program
# Python comes with a series of functions for convenience
# Values/Arguments are passed to functions using the parenthesis

# Functions in this program
# print() - displays the values to the CLI
# len() - displays the length of the values in the CLI
# input() - Python waits for the user to type something in the CLI defaults to string
# int() - returns the integer value of the value passed to the function
# format() - formats the specified values and inserts them inside the string's placeholder

print('Hello world!')
print('What is your name?') #asks for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()

print("You will be {} in a year".format(int(myAge) + 1))
print('{}, you will be {}  in a year'.format(myName, int(myAge) + 1))
