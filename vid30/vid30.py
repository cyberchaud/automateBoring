# os module has a series of operating system related modules

import os

print(r'/home/robi/workspace/automateBoring/vid30')
print(os.getcwd())

os.chdir(r'/home')
print(os.getcwd())

os.chdir(r'/home/robi/workspace/automateBoring/vid30')
print(os.getcwd())

print(os.path.abspath(r'vid30.py'))
print(os.path.abspath(r'../README.md'))

print(os.path.isabs(r'../vid30'))
print(os.path.isabs(r'/home/robi/workspace/automateBoring/vid30'))

print(os.path.relpath(os.getcwd(),os.path.abspath(r'../vid01/vid01.py')))

print(os.path.dirname(r'/home/robi/workspace/automateBoring/vid30/vid30.py'))
print(os.path.basename(r'/home/robi/workspace/automateBoring/vid30/vid30.py'))

print(os.path.isfile(r'/home/robi/workspace/automateBoring/vid30/vid30.py'))
print(os.path.isdir(r'/home/robi/workspace/automateBoring/vid30/vid30.py'))

print(os.path.getsize(r'/home/robi/workspace/automateBoring/vid30/vid30.py'))

totalsize = 0

for filename in os.listdir(r'/home/robi/workspace/automateBoring'):
    print(filename)
    if not os.path.isfile(os.path.join(r'/home/robi/workspace/automateBoring', filename)):
        continue
    totalsize = totalsize + os.path.getsize(os.path.join(r'/home/robi/workspace/automateBoring', filename))

print(totalsize)