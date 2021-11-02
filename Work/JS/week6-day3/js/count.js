let count01=document.querySelectorAll('.count-item h1')[0]
let count02=document.querySelectorAll('.count-item h1')[1]
let count03=document.querySelectorAll('.count-item h1')[2]
let count04=document.querySelectorAll('.count-item h1')[3]


let countFirst=1;
let countSecond=1;
let countThird=1;
let countFourth=1;

let interval01=setInterval(function(){
    count01.innerHTML=countFirst
    countFirst++
    if(countFirst>333){
        clearInterval(interval01)
    }
},1)

let interval02=setInterval(function(){
    count02.innerHTML=countSecond
    countSecond++
    if(countSecond>233){
        clearInterval(interval02)
    }
},1)

let interval03=setInterval(function(){
    count03.innerHTML=countThird
    countThird++
    if(countThird>133){
        clearInterval(interval03)
    }
},1)

let interval04=setInterval(function(){
    count04.innerHTML=countFourth
    countFourth++
    if(countFourth>33){
        clearInterval(interval04)
    }
},1)