import os
# folder yaratmaq desktopda
# os.listdir('c:/')
# print(os.listdir('c:/users/dell/onedrive/İş masası'))
# os.mkdir(os.path.join('c:/users/dell/onedrive/İş masası/','OsModule'))
# eger silmey isdeyirsiyse bu papkani sadece os.rmdir elemey lazimdir

folderPath=os.path.join('c:/users/dell/onedrive/İş masası/', 'OsModule')
filePath=os.path.join(folderPath,'a.txt')
fileConnection=open(filePath, 'a')

fileConnection.write('Men Python yazmaqa cehd eliyirem')

