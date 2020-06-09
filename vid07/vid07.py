# Python is delivered with a series of built-in modules

# import random
# functions inside random can be used with <module>.<function>
import random

print('This prints a random number between 1 and 10')
print(random.randint(1, 10))

# using from <module> import *
# from math import *
# functions from the module can be called directly

from math import *
print('This prints the absolute value of -10')
print(fabs(-10))
