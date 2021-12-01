# istifadecinin sisteme daxil olmasi prosesini helledecek kodlar burda olacaq

from data import users

def userLogin():
    #istifadəçidən username və password daxil etməsi tələb edilməlidir
    username=input('Istifadəçi adınızı daxil edin:')
    password=input('Şifrənizi daxil edin:')
    
    # daxil olunan username məlumatının data.py içərisində users listində olub olmadığı yoxlanılmalıdır
    for user in range(len(users)):
        if  users[user].username==username and users[user].password==password:
            print(' Sisteme daxil oldunuz, istifadeci melumatlariniz:', users[user].ad, users[user].soyad )
        else:
            print('Yanlis melumatlar daxil etdiniz')

            


        
        

