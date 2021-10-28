// 1.Qrup üzvlərinin ad, soyad və yaşlarının toplandığı adlar,soyadlar və yaslar adli array yaradin. Butun telebelerin ad soyad yaslarini bu arraylardan istifade ederek ekrana cap eden funksiya yazin. Numune(Telebe01 : Aysel Mustafayeva 21)


let adlar=["Aysel","Seyyad","Senan","Mehdi","Murad"];

let soyadlar=["Mustafayeva","Omerov","Mansurov","Cefer","Qafarli"]

let yas=['21','19','22','17', '18']

    function qrup() {

            for(i=0;i<adlar.length;i++)
        
            console.log('telebe'+i,adlar[i],soyadlar[i],yas[i])    }
   }


