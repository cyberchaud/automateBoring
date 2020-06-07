# While loops
# Each time through the loop is called an Iteration
# Difference between if and while statement
# End of the if statement Python executes the code under the if statement
# End of the while statement Python executes the begining of the while again until the condition is met

# break statement will exit the while loop and executes the code under the block
# continue statement will go back to the begining of the loop

spam = 0
while spam < 5:
    print('Hello World!')
    spam += 1
    if spam == 3:
        # When spam is equal to 3 this block is not executed
        continue
    print('Spam is equal to {}'.format(spam))

# Python continues to execute until the condition is true
# This is good use for input validation
name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('Thank you')
