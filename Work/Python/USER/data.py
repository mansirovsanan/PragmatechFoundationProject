#  istifadeci melumatlarinin istehsal olunmasi ve bir yere toplanilmasi

# istifadecilerin bir yere toplanmasi ucun lazm olan data struktur(list)
users=[]
# istifadecinin istehsal olunmasi ucun lazm olan class diger adi ile esgiz 
class User:
    def __init__(self,_ad,_soyad,_username,_password):
        self.ad=_ad
        self.soyad=_soyad
        self.username=_username
        self.password=_password
    