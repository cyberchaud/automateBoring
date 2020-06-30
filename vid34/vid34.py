# os module

# os.walk module returns 3 values on each iteration of a loop

import os

for folderName, subFolders, fileNames in os.walk(r'/home/robi/workspace/automateBoring'):
    print('The folder is: {}'.format(folderName))
    print('The sub folders are: {}'.format(str(subFolders)))
    print('The filenames are: {}'.format(str(fileNames)))