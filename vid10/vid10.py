# Try and except code blocks to avoid crashing applications
# Good for input validation

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(6))
print(div42by(0))
print(div42by(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('Thats a lot of cats')
    else:
        print('Not very many cats')
except ValueError:
    print('You did not enter a value')

