# local variables appear inside a function
# the rest of the variables are global variables
# variables cannot be local and variable at the same time
# local variables exist only within the local scope
# global variables exist while the application is running

def spam():
    global global_eggs
    eggs = 'Hello'
    global_eggs = 100
    print(eggs)

eggs = 42
global_eggs = 40
spam()
print(eggs, global_eggs)