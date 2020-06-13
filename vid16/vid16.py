# Dictionaries are a collection of key value pairs
# Python gets the value by indexing the name of the dictionary with the key value in []
# key values in a dictionary are unordered
# the is no order to the keys - ie: no first and last value

myCat = {'size': 'fat',
        'colour': 'grey',
        'disposition': 'loud'}

print(myCat['colour'])

#dictionaries can also use integers as keys

myNumbers = {
    1: 'yes',
    2: 'no',
    3: 'maybe'
}

print(myNumbers[3])

# Trying to access a key that isn't in a dictionary will result in a KeyError

try:
    print(myNumbers[99])
except KeyError:
    print("This key is not in the dictionary")

myNumbers.keys()
myNumbers.values()
# Dictionary methods can be called and they return listlike lists

print(list(myNumbers.keys()))

# Dictionary method .items() will print a list of tupples for all the key value pairs

print(myNumbers.items())

# The IN and NOT IN operators can be used to verify if the key exists in a dictionary

print('fat' in myCat.values())
print('skinny' in myCat.values())
print('skinny' not in myCat.values())

# To avoid KeyError the .get method on a dictionary can return a default value
# if it doesn't exist in the dictionary
print(myCat.get('parent', 0))

# If a key is in the dictionary but no value is assigned to it
# the setdefault method can be used to give a default value
# It will take the correct value if one is given

myList = {1:'a', 2:'b', 3:'c'}
print(myList)
myList.setdefault(0, '')
print(myList)
myList = {1:'a', 2:'b', 3:'c', 0:'d'}
print(myList)

# the module pprint (pretty print) can be used to display dictionary key value pairs in a
# cleaner format

import pprint
pprint.pprint(myList)
pprint.pprint((pprint.pformat(myList)))

