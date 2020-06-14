# strings are immutable therefore the string returns a new string variable
# strings methods

# .lower() and .upper()

spam = 'Alice'
print(spam)
print(spam.upper())
print(spam.lower())
print('e' in spam.upper())
print('e' in spam)

# .islower() and .isupper()
# returns a boolean if the string contains an upper or a lower case
# methods can be chained

print('Is lower function')
print(spam.islower())
print(spam.lower().islower())

# lots of is methods in  python
# .isalpha
# .isspace

print('Checking for space')
space = ' '
print(space.isspace())

# .join
# can combine multiple lists of strings into 1 string

print('; '.join(['alice', 'bob', 'charlie']))

# split
# splits a string based on the whitepsace of a string
spam = 'This is my string'
print(spam.split())

# justify text by inserting text
# centre text
print('Hello'.ljust(15))
print('Hello'.rjust(15))
print('Hello'.ljust(15, '*'))
print('Hello'.center(20, '-'))

# strip removes whitespace
empty = '               Empty               '
print(empty)
print(empty.strip())
print(empty.lstrip())
print(empty.rstrip())

# replace
# looks for 1 character and replaces it with another

print('Replacing spaces with asterix')
print(empty.replace(' ', '*'))
