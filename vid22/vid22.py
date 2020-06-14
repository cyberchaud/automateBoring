#! /usr/bin/python3

def isPhoneNumber(text):
    if len(text) != 12:
            return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!= '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print(isPhoneNumber('444-53-1234'))

# Looping through 12 char slices in a string
def checkforNumber(message):
    foundNumber = False
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: {}'.format(chunk))
            foundNumber = True
            return True

    if not foundNumber:
        print('Could find any phone numbers')
        return False

print(checkforNumber('Call me at 444-555-1234 for more details'))
print(checkforNumber('Call me at 444-5234 for more details'))

# Regular expression to find a phone number within a string
# Regular expression are a mini-language for specifying text patterns
# Should use raw strings r'string' so Python doesn't try and use escape characters

# Using the re library
# Call compile function
# Call search function
# Use group() method

import re

print('Using a regular expression to see if a string has a phone number pattern')

phoneNumbRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumbRegex.search('Call me at 444-555-1234 for more details')
print(mo.group())