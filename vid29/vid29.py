#! python3

import re
import pyperclip

# TODO: Create regex object for the phone
phoneRegex = re.compile(r'''
# 415-555-1234 555-1234

#Comment on the regex below:  We're looking for 555 and the escape character for an actual parenthesis is 
(((\d\d\d)|(\(\d\d\d\)))?  #area code optional
# first separator
(\s|-)
# first 3 digits
\d\d\d
# separator
-
# last 4 digits
\d\d\d\d
# extension
(((ext(\.)?\s)|x)
(\d{2,5}))?)
          ''', re.VERBOSE) #allows for a multiple line string without the new \n esecape characters


# TODO: Create regex object for the email address
emailRegex = re.compile(r'''

# name part
[a-zA-Z0-9_.+]+

# @ symbol
@

# domain name part
[a-zA-Z0-9_.+]+

''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Copy the extracted email/phone to the clipboard
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(extractedEmail)
print(allPhoneNumbers)
