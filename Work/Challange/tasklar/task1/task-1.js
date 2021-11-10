let color = ['blue', 'red', 'green', 'pink', 'orange', 'gray', 'brown', 'black'];
let i=0
document.querySelector('button').addEventListener('click',function(){
    
    x=(i<color.length?++i:0);

    document.querySelector('body').style.background=color[i]

    document.querySelector('h1').innerHTML=color[i]

})