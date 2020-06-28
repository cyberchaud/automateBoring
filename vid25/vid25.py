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

