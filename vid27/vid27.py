# Regex patterns.
# ^ signifies patterns must appear at the beginning
# $ signifies patterns must appear at the end
# . any number of digits
# .* match anything

# Shortcuts
# 2nd argument to the compile method re.DOTALL
# then the . will match new lines as well
# 2nd argument to the compile method re.IGNORECASE
# will find all matches case insensitive

import re

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))

endsWithHelloRegex = re.compile('world!$')
print(endsWithHelloRegex.search('Hello world!'))

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('123456789'))

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat not attack.'))

fullName = 'First Name: Alice Last Name: Blake'

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(fullName))

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*>)')
print(greedy.findall(serve))

prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law.'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime))
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))





