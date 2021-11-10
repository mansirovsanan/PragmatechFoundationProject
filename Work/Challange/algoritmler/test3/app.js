// user tərəfindən daxil 2 ədədin 30-70 arasında olmasını yoxlamaq. Rəqəmlərin hər ikisinin, yalnız birinin və ya heç birinin aralıqda olub-olmaması şərtlərini yoxlamaq və uyğun mesajı çıxarmaq.

let eded1=prompt(' birinci ededi daxil edin:')

let eded2=prompt('ikinci ededi daxil edin:')

let a=Number(eded1)
let b=Number(eded2)

if(a>30 && a<70 || b>30 && b<70){
    alert('her iki eded  30-70 arasindadir')
}else {
    alert('hec biri 30-70 arasinda deyil')
}

