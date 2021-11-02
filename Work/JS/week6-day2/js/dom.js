let box=document.querySelector('.box');
let elementWidth=box.clientWidth;
let leftPos=0;
let topPos=0;
function rengiDeyis(){
    box.style.background='black'
}

function olcunuDeyis(){
    box.style.width='900px'
}

function hereketEletdir(){
    box.style.left='200px'
}

function yoxOlsun(){
    box.style.opacity='0'
}
function geriGelsin(){
    box.style.opacity='1'
}

function daimiHereketEle(){
    box.style.left=`${leftPos}px`
    leftPos+=1;
    if(leftPos>(window.innerWidth-elementWidth)){
        clearInterval(interval)
    }
    console.log(`letfPos=${leftPos}`)
}


// function asaqiHereketEle(){
//     let interval2=setInterval(asaqiHereketEle,1)
//     box.style.top=`${asaqiHereketEle}px`

//     topPos+=1;
//     if(topPos>(window.innerHeight-elementHeight)){
//         clearInterval(interval2)
//     }
//     console.log(`topPos=${topPos}`)
// }

let interval=setInterval(daimiHereketEle,1)
