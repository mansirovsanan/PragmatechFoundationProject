# List metodları və tuple metodlarını qarşılaşdırın aradakı fərqləri kod nümumələri ilə izah edin.

# List metodunda siyahı dəyişdirilə bilər, yəni biz siyahı yaratdıqdan sonra elementləri dəyişdirə, əlavə edə və silə bilərik.

telebeler=['Memmed','Murad','Kamil','Namiq']

telebeler.append('Senan')

telebeler[1:3]=['Emin','Taryel']

telebeler.insert(0,'Murad')

telebeler.pop(1)

print(telebeler)

print(type(telebeler))

# Tuple metodu dəyişməzdir, yəni siyahi yaradıldıqdan sonra elementləri dəyişdirə, əlavə edə və ya silə bilmərik.

telebeler=('Memmed','Murad','Kamil','Namiq')

print(telebeler)

print(telebeler[3])

print(type(telebeler))
