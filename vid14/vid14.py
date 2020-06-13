# lists are index based starting with 0
# methods are available get the values from lists
# these methods are only available to lists
# cannot be used for strings for example
# lists are modified in place
# no return value are generated from the methods

spam = ['hello,', 'Hi', 'howdy', 'hiya', 'howdy']

# index method returns the location of the value in the list
# exception is raised if the value is not in the list
# when duplicate values exist, it returns the first hit
# index method searches are case sensitive

print(spam.index('Hi'))

try:
    print(spam.index('asdf'))
except ValueError:
    print('Not in the list')

print(spam.index('howdy'))

# add values to the end of the list
# with .append method

spam.append('hola')
print(spam)

# add value in a specific location
# with .insert method

spam.insert(2, 'kamusta')

print(spam)

# remove a specific value from the list
# with the .remove method
# only the first instance of the value will be removed

spam.remove('hola')
print(spam)

# to delete a value at an index
# del function can be called

del spam[3]

print(spam)

# list can be sorted with
# .sort method
# .sort will sort based on the context (numbers or alpha) in ASCII-betical order
# capital letters will be ordered first
# lists with both numbers and strings cannot be sorted
# this returns a Typeerror for unorderable types

spam.sort()
print(spam)

# sort method can access keywords as arguments
# key=str.lower forces an alphabetical sort

spam.sort(key=str.lower)
print(spam)


