telebeler=[
    {
    'ad':'Samir',
    'soyad':'Hemidov',
    'yas':30
    },
    {
    'ad':'Memmed',
    'soyad':'Salamov',
    'yas':20
    },
    {
    'ad':'Aliye',
    'soyad':'Qurbanova',
    'yas':16
    },
    {
    'ad':'Sahil',
    'soyad':'Qeniyev',
    'yas':45
    },
    {
    'ad':'Ehmed',
    'soyad':'Qeniyev',
    'yas':50
    }
]   


# Butun adlari ekrana cap edin

for x in telebeler:
    print(x)


print(len(telebeler))


for x in range(len(telebeler)):
    print(telebeler[x]['ad'])


# Istidadecilerin yaslarinin cemini tapin


for x in range(len(telebeler)):
    print(telebeler[x]['yas'])


Yas=0
for x in range(len(telebeler)):
    Yas += telebeler[x]['yas']
print('Telebe yaslarinin cemi:', Yas)




# adi Ehmed olan istifadecinin butun melumatlarini ekrana cap edin

print(telebeler[4]['ad'])
print(telebeler[4]['soyad'])
print(telebeler[4]['yas'])



Ad=input('telebe adini daxi edin: ')

for x in range(len(telebeler)):

    if (telebeler[x]['ad']) == Ad :

        print(Ad, 'adli telebenin melumatlari', (telebeler[x]))




 
# findUser(userName) adli metod yaradin
    # daxil edilen ada əsasən o istifadecinin butun melumatlarini ekrana cap etsin


def findUser(userName):
        
        for x in range(len(telebeler)):

            if (telebeler[x]['ad']) == userName:

                return telebeler[x]

print(findUser('Ehmed'))
    

