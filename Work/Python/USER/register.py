# istifadecinin qeydiyyatdan kesmesi ucun lazim olan kodlar burda olacaq
from data import User,users
import login
def registerUser():
    ad=input('Adiniz:')
    soyad=input('Soyadiniz:')
    username=input('Istifadeci adiniz:')
    password=input('Sifreniz:')

    # terminaldan daxil edilen melumatlar esasinda yeni user obyekti yarat
    user=User(ad,soyad,username,password)
    # yaradilan yeni useri users listine elave et
    users.append(user)


    

