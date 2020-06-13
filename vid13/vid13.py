# Lists can be combined with range function

spam = list(range(0, 100, 2))
print(spam)

# Easy way to refer to the loop index and the list index value

supplies = ['pens', 'paper', 'crayons', 'erasers', 'tape']
for i in range(len(supplies)):
    print('Index {} in supplies is: {}'.format(i, supplies[i]))

# Multiple assignment works both ways
# Often used for swapping variables

cats = ['fat', 'orange', 'loud']
size = cats[0]
colour = cats[1]
disposition = cats[2]

print(cats)

size, colour, disposition = cats
print(cats)

size, colour, disposition = 'skinny', 'black', 'quiet'
print(size, colour, disposition)

# Swapping variables

a = '123'
b = '456'

a, b = b, a

print(a, b)

# Augmented assignment operators
spam = 6
print(spam)
spam += 1
print(spam)
spam -= 1
print(spam)
spam *= 5
print(spam)
spam /= 5
print(spam)
