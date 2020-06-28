# .sub method returns a substitute string for all the regex matches
# VERBOSE mode excludes white space and new lines from the regex search
# A bitwise OR operator can be used to combine all the arguments of the re.compile
# re.IGNORECASE | re.DOTALL | re.VERBOSE

import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w) \*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))

print(namesRegex.sub(r'Agent \1*****', 'Agent Alice gave the secret documents to Agent Bob.'))

re.compile(r'''
\d\d\d # Area code
-
\d\d\d # First 3 digits
-
\d\d\d\d # Last 4 digits
''', re.VERBOSE)
