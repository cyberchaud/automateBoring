# for loop

print('My name is')
for i in range(5):
    print('Jimmy five times {}'.format(str(i)))


# sum total with for loops
total = 0
for num in range(101):
    total = total + num
print(total)

# while loop

i = 0
while i < 5:
    print('Jimmy five times {}'.format(str(i)))
    i += 1

# for loop with 2 arguments
# 2 arguments is the start and end range
for i in range(5, 10):
    print('Jimmy five times {}'.format(str(i)))
    i += 1

# for loop with 3 arguments
# 3 arguments is the start, end and the step value
for i in range(10, 5, -1):
    print('Jimmy five times {}'.format(str(i)))
    i += 1