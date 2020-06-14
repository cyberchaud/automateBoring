# Escape characters in Python
# \' - single quote
# \" - double quote
# \t - Tab
# \n - Newline
# \\ - Backslash

# string = 'Alice\'s'
# result of print = Alice

print('Alice\'s')

# rawstring in Python is started with a small r
# rawstrings will not escape any characters
# for rawstrings

print(r'That cat is Carol\'s cat')

# Multiline line strings are identified with triple quotes """
print("""That cat 
is
Carol\'s 
cat""")

# strings are list-like variables
# all the same things that lists can do can be done on strings

spam = 'This is my text'
print(spam[-3])
print(spam[-3:])
print(spam[:-3])
print('z' in spam)
print('x' in spam)

# print the 3rd character in a string

print(spam[2])
