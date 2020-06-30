import shelve

myFile = open(r'/home/robi/workspace/automateBoring/vid31/hello.txt')
content = myFile.read()
myFile.close()
print(content)

myFile = open(r'/home/robi/workspace/automateBoring/vid31/hello.txt')
lines = myFile.readlines()
for line in lines:
    print(line)
myFile.close()

myFile = open(r'/home/robi/workspace/automateBoring/vid31/hello2.txt', 'w')
myFile.write('This is my new text')
myFile.write('This is my new text')
myFile.write('This is my new text')
myFile.write('This is my new text')
myFile.write('This is my new text')
myFile.close()

myFile = open(r'/home/robi/workspace/automateBoring/vid31/hello3.txt', 'a')
myFile.write('This is my new text')
myFile.write('This is my new text')
myFile.write('This is my new text')
myFile.write('This is my new text')
myFile.write('This is my new text')
myFile.close()

# shelve write data to a file on the HDD



shelfFile = shelve.open('mydata')
shelfFile['players'] = ['Judge', 'Jeter', 'John']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['players'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))