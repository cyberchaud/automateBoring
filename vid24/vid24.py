#! /usr/bin/python3

# The ? is used to identify a group as optional (zero or one times)
# The * is a wild card to identify (zero or more) matches
# The + is for one or more matches.  The group must appear one or more times.
# Curly braces can be used to identify the exact amount of matches required {x}
# Curly braces with a digit comma and digit {x,y} is a min and max matches.
# By default Python will match the first longest match.  Greedy matching.
# A question mark after the curly braces does a non-greedy match {,}?

import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')

def PrintGroup(x):
    try:
        print(mo.group())
    except AttributeError:
        print('Value not found')

PrintGroup(mo)

mo = batRegex.search('The Adventures of Batwoman')
PrintGroup(mo)

mo = batRegex.search('The Adventures of Batwowowowoman')
PrintGroup(mo)

phoneNumbRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumbRegex.search('My phone number is 415-555-1234.  Call me tomorrow')
PrintGroup(mo)

phoneNumbRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumbRegex.search('My phone number is 555-1234.  Call me tomorrow')
PrintGroup(mo)

phoneNumbRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneNumbRegex.search('My phone number is 555-1234.  Call me tomorrow')
PrintGroup(mo)
mo = phoneNumbRegex.search('My phone number is 415-555-1234.  Call me tomorrow')
PrintGroup(mo)

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
PrintGroup(mo)
mo = batRegex.search('The Adventures of Batwoman')
PrintGroup(mo)
mo = batRegex.search('The Adventures of Batwowowowoman')
PrintGroup(mo)

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman')
PrintGroup(mo)
mo = batRegex.search('The Adventures of Batwoman')
PrintGroup(mo)
mo = batRegex.search('The Adventures of Batwowowowoman')
PrintGroup(mo)

batRegex = re.compile(r'Bat(wo){4}man')
mo = batRegex.search('The Adventures of Batman')
PrintGroup(mo)
mo = batRegex.search('The Adventures of Batwoman')
PrintGroup(mo)
mo = batRegex.search('The Adventures of Batwowowowoman')
PrintGroup(mo)

digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('123456789')
PrintGroup(mo)

digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('123456789')
PrintGroup(mo)