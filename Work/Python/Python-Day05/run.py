import os
folderPath="c:/"
print(len(os.listdir(folderPath)))

for f in os.listdir(folderPath):
    newpath=os.path.join(folderPath,f)
    if os.path.isdir(newpath):
        print(f'{f}-bu directory dir')


