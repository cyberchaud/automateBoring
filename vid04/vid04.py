# pythontutor.com/visualize.html

# Indentation in Python indicates a block of code
# Blocks start where the indentation begins and the block stops where the indentation stops

# if block statements are conditions/expressions
# if the condition evaluates to true; then Python executes the indented code

name = 'Bob'
if name == 'Alice':
    # Skips the indentation block because the condition is not True
    print('Hi {}'.format(name))
print('Done')

password = 'iloveu'
# Python executes one block only
if password == 'swordfish':
    print('Access granted')
elif password == 'iloveu':
    print('Access granted with your terrible password')
else:
    print('Try again')

# Python Truthy or Falsey
# Strings:
# Truthy is any string
# Falsey is a blank string
# Test - bool('Hello') -> True; bool('') -> False

# Integers:
# Truthy is any integer
# Falsey is 0
# Test - bool(42) -> True; bool(0) -> False

print('Enter a name')
name = input()

# Any input will print 'Thank you for entering your 'name'
# Pressing enter (blank input) prints 'You did not enter a name'
if name != '':
    print('Thank you for entering your name')
else:
    print('You did not enter a name')
