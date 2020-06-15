#! /usr/bin/python3

# Regex can be separated with parentheses
# Parentheses define where the group starts and ends
# Escape character to search on parenthesis: \(

import re

phoneNumbRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumbRegex.search('Call me at 444-555-1234 for more details')
print(mo.group(1))
print(mo.group(2))

# Pipe character | can be used to match one of several patterns

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Maybe the Batmobile lost a wheel')
print(mo.group())


mo = batRegex.search('Maybe the car lost a wheel')
try:
    print(mo.group())
except AttributeError:
    print('Value not found')