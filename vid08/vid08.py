# Functions are made and define the code to be executed
# Code is only executed when the function is called
# Main purpose to is group code that will be called multiple times

# The print function returns the None value.
# It also passes a new line character by default
# print will separate multiple arguments on the same line separated by a space.
# None does not show up in the CLI
# None is the only value of the None type
# None represents the lack of a value
# If no return value is in a function - it returns None

def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there')

def hi(name):
    print('Hello {}'.format(name))

hello()
hi('Elliot')

def plusOne(number):
    return number + 1

newNumber = plusOne(6)
print(newNumber)

print('Hello')
print('World')
print('Hello', end='')
print('World')
print('Hello', 'World')
print('Hello', 'World', sep="; ")
